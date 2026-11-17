"""MonoMyth trainer BACK pics: extraction by letting the game decode them (2026-11-17).

Measured:
  * Back pic table @ ROM 0x49ADCC: 11 x {u32 ptr, u16 size=0x2000, u16 tag}; palette table
    @ 0x49AE24: 11 x {u32 ptr -> LZ77 32-byte palette, u16 tag, u16 0}.
  * The pixel data is NOT LZ77 and NOT expansion smol. It is the same MonoMyth packed sprite
    container used for overworld sheets (see mm_overworld.py). Header byte 2 = OAM size code
    (3 = 64x64), byte 3 = frame count (4 for the player characters, 1 for #9/#10).
  * DecompressPicFromTable (0x080167F0) just wraps BIOS LZ77 and does NOT handle these; the
    sprite engine decodes the container on frame copy when an image entry's size field reads
    0xFF00|frame. So: point the bedroom player sprite's images pointer (state 0x424DC) at a fake
    array of {backpic_ptr, 0xFF00|frame} entries, turn, and read 64x64 out of OBJ VRAM.

Usage:  python3 -I mm_backpics.py ROM OUT_DIR
        writes back_NN.png (256 px tall, 4 frames of 64x64, indexed) + backs_sheet.png
"""
import os, sys, struct
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from mm_overworld import patched_rom, STATE, SLOT, VRAM_OBJ  # noqa: E402

BACK_TABLE, BACK_PALS, COUNT = 0x49ADCC, 0x49AE24, 11
ARR = 0x0202AA00          # zero-filled EWRAM in the bedroom state; holds the fake images array
EWRAM = 0x21000           # mGBA state offset of EWRAM


def lz(rom, off):
    size = rom[off + 1] | rom[off + 2] << 8 | rom[off + 3] << 16; o = bytearray(); i = off + 4
    while len(o) < size:
        f = rom[i]; i += 1
        for b in range(8):
            if len(o) >= size: break
            if f & (0x80 >> b):
                x = rom[i] << 8 | rom[i + 1]; i += 2
                for _ in range((x >> 12) + 3): o.append(o[-((x & 0xFFF) + 1)])
            else: o.append(rom[i]); i += 1
    return bytes(o)


def px64(b):
    a = np.zeros((64, 64), np.uint8)
    for t in range(64):
        tb = np.frombuffer(b[t * 32:t * 32 + 32], np.uint8); tile = np.zeros((8, 8), np.uint8)
        tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
        a[(t // 8) * 8:(t // 8) * 8 + 8, (t % 8) * 8:(t % 8) * 8 + 8] = tile
    return a


def extract_all(rom_path):
    sys.path.insert(0, os.path.join(HERE, '../playtest'))
    from gba_harness import GBA
    rom = open(rom_path, 'rb').read(); g = GBA(patched_rom(rom_path))
    base = bytearray(open(STATE, 'rb').read()); out = {}
    for k in range(COUNT):
        ptr = struct.unpack_from('<I', rom, BACK_TABLE + 8 * k)[0]
        nframes = rom[ptr - 0x08000000 + 3]
        raw = lz(rom, struct.unpack_from('<I', rom, BACK_PALS + 8 * k)[0] - 0x08000000)
        pal = np.array([((c & 31) << 3, (c >> 5 & 31) << 3, (c >> 10 & 31) << 3)
                        for c in struct.unpack_from('<16H', raw)], np.uint8)
        frames = []
        for j in range(nframes):
            st = bytearray(base)
            ent = b''.join(struct.pack('<IHH', ptr, 0xFF00 | j, 0) for _ in range(16))
            o = EWRAM + ARR - 0x02000000; st[o:o + len(ent)] = ent
            st[SLOT:SLOT + 4] = struct.pack('<I', ARR)
            g.restore(bytes(st)); g.run(2, 'UP'); g.run(20); g.run(2, 'DOWN'); g.run(20)
            frames.append(px64(bytes(g.state())[VRAM_OBJ:VRAM_OBJ + 0x800]))
        out[k] = (frames, pal)
    return out


if __name__ == '__main__':
    from PIL import Image
    rom, dst = sys.argv[1], sys.argv[2]; os.makedirs(dst, exist_ok=True)
    out = extract_all(rom); S = 3
    sheet = Image.new('RGB', (4 * (64 * S + 4), COUNT * (64 * S + 4)), (30, 30, 36))
    for k, (frames, pal) in out.items():
        img = Image.fromarray(np.concatenate(frames, 0), 'P')
        img.putpalette([int(v) for c in pal for v in c] + [0] * (768 - 48))
        img.save(os.path.join(dst, 'back_%02d.png' % k), transparency=0)
        for j, f in enumerate(frames):
            rgb = pal[f]; rgb[f == 0] = (110, 110, 130)
            sheet.paste(Image.fromarray(rgb).resize((64 * S, 64 * S), Image.NEAREST),
                        (j * (64 * S + 4), k * (64 * S + 4)))
    sheet.save(os.path.join(dst, 'backs_sheet.png')); print('backs', len(out))
