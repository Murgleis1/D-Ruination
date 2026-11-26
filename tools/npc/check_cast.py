"""Check the installed cast in the built ROM (after install_cast.py and make): every walker and front decoded from the
ROM by its symbol and compared with its PNG, index for index and colour for colour (GBA 5-bit); and the tables that
reach them: gObjectEventGraphicsInfoPointers[gfx id] -> its info -> palette tag and images -> the pic; the palette tag
in sObjectEventSpritePalettes -> the palette; gTrainerSprites[pic id] -> the front pic and palette; gTrainerClasses
names. Usage: python3 check_cast.py"""
import os
import re
import struct
import subprocess
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import install_cast as I   # noqa: E402

CB = I.CB
ROM = open(os.path.join(CB, 'pokeemerald.gba'), 'rb').read()
SYMS = {}
for line in subprocess.run(['arm-none-eabi-nm', os.path.join(CB, 'pokeemerald.elf')], capture_output=True,
                           text=True).stdout.split('\n'):
    p = line.split()
    if len(p) == 3:
        SYMS[p[2]] = int(p[0], 16) - 0x08000000
u32 = lambda o: struct.unpack_from('<I', ROM, o)[0]
u16 = lambda o: struct.unpack_from('<H', ROM, o)[0]


def lz77(off):
    assert ROM[off] == 0x10
    size = u32(off) >> 8
    out = bytearray(); i = off + 4
    while len(out) < size:
        f = ROM[i]; i += 1
        for b in range(8):
            if len(out) >= size:
                break
            if f & (0x80 >> b):
                x = ROM[i] << 8 | ROM[i + 1]; i += 2
                for _ in range((x >> 12) + 3):
                    out.append(out[-((x & 0xFFF) + 1)])
            else:
                out.append(ROM[i]); i += 1
    return bytes(out)


def tiles(data, w, h):
    a = np.zeros((h, w), np.uint8); k = 0
    for ty in range(h // 8):
        for tx in range(w // 8):
            for y in range(8):
                for x in range(0, 8, 2):
                    b = data[k]; k += 1
                    a[ty * 8 + y, tx * 8 + x] = b & 15; a[ty * 8 + y, tx * 8 + x + 1] = b >> 4
    return a


def pal(data):
    return [((v & 31), (v >> 5) & 31, (v >> 10) & 31) for v in struct.unpack_from('<16H', data)]


def png(path):
    im = Image.open(path); p = im.getpalette()[:48]
    return np.array(im), [(p[k] >> 3, p[k + 1] >> 3, p[k + 2] >> 3) for k in range(0, 48, 3)]


def main():
    ok = True
    ptrs = SYMS['gObjectEventGraphicsInfoPointers']
    pals = SYMS['sObjectEventSpritePalettes']
    paltab = {}
    k = 0
    while True:
        d, tag = u32(pals + 8 * k), u16(pals + 8 * k + 4)
        if d == 0:
            break
        paltab[tag] = d - 0x08000000; k += 1
    for i, (key, cam, stem, _) in enumerate(I.WALKERS):
        gid = I.GFX0 + i
        want_i, want_p = png(os.path.join(CB, 'graphics/object_events/pics/people/dr_%s.png' % stem))
        pic = SYMS['gObjectEventPic_Dr' + cam]
        got = np.concatenate([tiles(ROM[pic + f * 256:pic + (f + 1) * 256], 16, 32) for f in range(9)], axis=1)
        info = u32(ptrs + 4 * gid) - 0x08000000
        ok_info = info == SYMS['gObjectEventGraphicsInfo_Dr' + cam]
        tag = u16(info + 2)
        images = u32(info + 0x1C) - 0x08000000
        ok_img = u32(images) - 0x08000000 == pic
        ok_tag = tag == I.TAG0 + i and paltab.get(tag) == SYMS['gObjectEventPal_Dr' + cam]
        gp = pal(ROM[SYMS['gObjectEventPal_Dr' + cam]:])
        ok_px = got.shape == want_i.shape and (got == want_i).all()
        ok_pal = gp[1:] == want_p[1:]
        good = ok_info and ok_img and ok_tag and ok_px and ok_pal
        ok &= good
        print('walker %3d %-18s %s%s' % (gid, stem, 'OK' if good else 'PROBLEM',
                                         '' if good else ' info %s images %s tag %s pixels %s palette %s' % (
                                             ok_info, ok_img, ok_tag, ok_px, ok_pal)))
    spr = SYMS['gTrainerSprites']
    stride = None
    for st in range(8, 64, 4):
        if u32(spr + st * 136 + 4) - 0x08000000 == SYMS['gTrainerFrontPic_TemplarMale']:
            stride = st
            break
    assert stride, 'gTrainerSprites stride'
    for i, (key, cam, stem, _) in enumerate(I.FRONTS):
        pid = I.PIC0 + i
        want_i, want_p = png(os.path.join(CB, 'graphics/trainers/front_pics/dr_%s.png' % stem))
        got = tiles(lz77(SYMS['gTrainerFrontPic_Dr' + cam]), 64, 64)
        gp = pal(lz77(SYMS['gTrainerPalette_Dr' + cam]))
        e = spr + stride * pid
        ok_tab = (u32(e + 4) - 0x08000000 == SYMS['gTrainerFrontPic_Dr' + cam]
                  and u32(e + 12) - 0x08000000 == SYMS['gTrainerPalette_Dr' + cam])
        ok_px = (got == want_i).all(); ok_pal = gp[1:] == want_p[1:]
        good = ok_tab and ok_px and ok_pal
        ok &= good
        print('front  %3d %-18s %s%s' % (pid, stem, 'OK' if good else 'PROBLEM',
                                         '' if good else ' table %s pixels %s palette %s' % (ok_tab, ok_px, ok_pal)))
    cls = SYMS['gTrainerClasses']
    CH = {**{0xBB + i: chr(65 + i) for i in range(26)}, **{0xD5 + i: chr(97 + i) for i in range(26)}, 0x00: ' '}
    for i, (key, name, money) in enumerate(I.CLASSES):
        cid = I.CLS0 + i
        raw = ROM[cls + 16 * cid:cls + 16 * cid + 13]
        txt = ''.join(CH.get(b, '?') for b in raw.split(b'\xff')[0])
        good = txt == name and ROM[cls + 16 * cid + 13] == money
        ok &= good
        print('class 0x%02X %-12s %s' % (cid, txt, 'OK' if good else 'PROBLEM (want %s, %d)' % (name, money)))
    print('ALL OK' if ok else 'PROBLEM')


if __name__ == '__main__':
    main()
