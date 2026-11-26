"""Check Baradus's five assets in the built ROM against the PNGs: decode each graphic and palette from the ROM by its
symbol (LZ77 where compressed) and compare index for index, colour for colour (GBA 5-bit).
Usage: python3 check_rom.py   (after make)"""
import os
import subprocess
import struct

import numpy as np
from PIL import Image

CB = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'codebase'))
ROM = open(os.path.join(CB, 'pokeemerald.gba'), 'rb').read()
SYMS = {}
for line in subprocess.run(['arm-none-eabi-nm', os.path.join(CB, 'pokeemerald.elf')], capture_output=True, text=True).stdout.split('\n'):
    p = line.split()
    if len(p) == 3:
        SYMS[p[2]] = int(p[0], 16) - 0x08000000


def lz77(off):
    assert ROM[off] == 0x10, hex(ROM[off])
    size = struct.unpack_from('<I', ROM, off)[0] >> 8
    out = bytearray()
    i = off + 4
    while len(out) < size:
        flags = ROM[i]
        i += 1
        for b in range(8):
            if len(out) >= size:
                break
            if flags & (0x80 >> b):
                v = ROM[i] << 8 | ROM[i + 1]
                i += 2
                n, d = (v >> 12) + 3, (v & 0xFFF) + 1
                for _ in range(n):
                    out.append(out[-d])
            else:
                out.append(ROM[i])
                i += 1
    return bytes(out)


def tiles(data, w, h):
    a = np.zeros((h, w), np.uint8)
    k = 0
    for ty in range(h // 8):
        for tx in range(w // 8):
            for y in range(8):
                for x in range(0, 8, 2):
                    b = data[k]
                    k += 1
                    a[ty * 8 + y, tx * 8 + x] = b & 15
                    a[ty * 8 + y, tx * 8 + x + 1] = b >> 4
    return a


def pal(data):
    return [((v & 31), (v >> 5) & 31, (v >> 10) & 31) for v in struct.unpack_from('<16H', data)]


def png(rel):
    im = Image.open(os.path.join(CB, rel))
    p = im.getpalette()[:48]
    return np.array(im), [(p[k] >> 3, p[k + 1] >> 3, p[k + 2] >> 3) for k in range(0, 48, 3)]


def ow_frames(data):
    """Object pics are frame after frame (16x32 = 4x... tiles per frame, row-major within a frame)."""
    fr = []
    for f in range(9):
        fr.append(tiles(data[f * 256:(f + 1) * 256], 16, 32))
    return np.concatenate(fr, axis=1)


ok = True
cases = [
    ('front', 'graphics/trainers/front_pics/baradus.png', lambda: tiles(lz77(SYMS['gTrainerFrontPic_Baradus']), 64, 64),
     lambda: pal(lz77(SYMS['gTrainerPalette_Baradus']))),
    ('ow', 'graphics/object_events/pics/people/baradus.png', lambda: ow_frames(ROM[SYMS['gObjectEventPic_Baradus']:]),
     lambda: pal(ROM[SYMS['gObjectEventPal_Baradus']:])),
]
for e in ('Positive', 'Anger', 'Negative'):
    cases.append((e.lower(), 'graphics/portraits/baradus_%s.png' % e.lower(),
                  (lambda e=e: tiles(lz77(SYMS['sPortraitGfx_Baradus' + e]), 80, 80)),
                  (lambda e=e: pal(ROM[SYMS['sPortraitPal_Baradus' + e]:]))))
for name, rel, gfx, pl in cases:
    want_i, want_p = png(rel)
    got_i, got_p = gfx(), pl()
    same_i = got_i.shape == want_i.shape and (got_i == want_i).all()
    same_p = got_p[1:] == want_p[1:]               # index 0 is transparent
    ice = [k for k in range(1, 16) if got_p[k] in ((216 >> 3, 244 >> 3, 255 >> 3), (160 >> 3, 216 >> 3, 248 >> 3), (104 >> 3, 168 >> 3, 224 >> 3))]
    print('%-9s pixels %s  palette %s  ice slots %s  ice pixels %d' % (
        name, 'match' if same_i else 'DIFFER', 'match' if same_p else 'DIFFER', ice, int(np.isin(got_i, ice).sum())))
    ok &= same_i and same_p and len(ice) == 3
print('ALL OK' if ok else 'PROBLEM')
