"""Extract a Crown (FireRed base) overworld walker as an indexed PNG, index 0 transparent: the main sprite table at
0x839FDB0 (152 entries; the numbers on assets/crown_reference/npcs_main_table.png), each a graphics-info struct whose
images table lists its frames {data, size} (raw 4bpp); the palette by tag from the expanded palette table at
0x9BCB4FC (entries {data, tag, pad}). FireRed's frame order is Emerald's 9: S N W, walk S x2, N x2, W x2.
Usage: python3 cr_walker.py N OUT.png"""
import os
import struct
import sys

import numpy as np
from PIL import Image

ROMP = os.environ.get('CROWN_ROM', '/home/claude/crown/Crown.gba')
TABLE = 0x39FDB0
PALS = 0x1BCB4FC


def tiles(b, w, h):
    tw, th = w // 8, h // 8
    px = np.zeros((h, w), np.uint8)
    for t in range(tw * th):
        tb = np.frombuffer(b[t * 32:(t + 1) * 32], np.uint8)
        tile = np.zeros((8, 8), np.uint8)
        tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
        px[(t // tw) * 8:(t // tw) * 8 + 8, (t % tw) * 8:(t % tw) * 8 + 8] = tile
    return px


def palette(d, tag):
    a = PALS
    for k in range(400):
        p, t = struct.unpack_from('<IH', d, a + 8 * k)
        if t == tag and 0x08000000 <= p < 0x0A000000:
            q = p - 0x08000000
            cols = struct.unpack_from('<16H', d, q)
            return [((c & 31) << 3, ((c >> 5) & 31) << 3, ((c >> 10) & 31) << 3) for c in cols]
        if t == 0x11FF:
            break
    raise KeyError(hex(tag))


def walker(n, frames=9):
    d = open(ROMP, 'rb').read()
    p = struct.unpack_from('<I', d, TABLE + 4 * n)[0] - 0x08000000
    tag, paltag, refl, size, w, h = struct.unpack_from('<HHHHhh', d, p)
    images = struct.unpack_from('<I', d, p + 0x1C)[0] - 0x08000000
    out = []
    for k in range(frames):
        fp, fs = struct.unpack_from('<II', d, images + 8 * k)
        out.append(tiles(d[fp - 0x08000000:fp - 0x08000000 + size], w, h))
    return np.concatenate(out, axis=1), palette(d, paltag), (w, h)


if __name__ == '__main__':
    n, path = int(sys.argv[1]), sys.argv[2]
    px, pal, wh = walker(n)
    im = Image.fromarray(px.astype(np.uint8), 'P')
    im.putpalette([v for c in pal for v in c] + [0] * (768 - 48))
    im.save(path, transparency=0)
    print(n, wh, px.shape)
