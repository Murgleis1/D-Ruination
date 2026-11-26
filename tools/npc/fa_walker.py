"""Extract a Fantasma overworld walker (all 9 frames: S, N, W, walk S x2, walk N x2, walk W x2) as an indexed
144x32 PNG, index 0 transparent. Fantasma is pokeemerald-expansion based: the graphics info's images pointer is a
SpriteFrameImage table {data, size} (8 bytes a frame). The catalogue index n is ow_scan.scan's order (the numbers on
assets/npc_survey/ow_fantasma.png).
Usage: python3 fa_walker.py N OUT.png"""
import os
import struct
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ow_scan  # noqa: E402

ROMP = os.environ.get('FANTASMA_ROM', '/home/claude/fantasma/fantasma.gba')


def sheet_bytes(d, images, size, frames):
    """The walker's frames: the images table's first entry points at its sheet, every frame size bytes, back to back;
    LZ77 or smol when compressed, else raw."""
    p = struct.unpack_from('<I', d, images - 0x08000000)[0]
    q = p - 0x08000000
    if d[q] == 0x10:
        b = ow_scan.lz77(d, q)
    else:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fantasma'))
        import fsread
        try:
            b = fsread.unsmol(q)
        except Exception:
            b = None
    if b and len(b) >= size * frames:
        return b
    # uncompressed: the entry's data is the whole sheet, the frames back to back (the table's next entries are the
    # next walkers' sheets, 9 x size bytes apart)
    return d[q:q + size * frames]


def tiles(b, w, h):
    tw, th = w // 8, h // 8
    px = np.zeros((h, w), np.uint8)
    for t in range(tw * th):
        tb = np.frombuffer(b[t * 32:(t + 1) * 32], np.uint8); tile = np.zeros((8, 8), np.uint8)
        tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
        px[(t // tw) * 8:(t // tw) * 8 + 8, (t % tw) * 8:(t % tw) * 8 + 8] = tile
    return px


def walker(n, frames=9):
    d = open(ROMP, 'rb').read()
    infos, pals = ow_scan.scan(d)
    a, tag, images, w, h, size = infos[n]
    b = sheet_bytes(d, images, size, frames)
    out = [tiles(b[k * size:(k + 1) * size], w, h) for k in range(frames)]
    return np.concatenate(out, axis=1), [tuple(int(v) for v in c) for c in pals[tag]], (w, h)


if __name__ == '__main__':
    n, path = int(sys.argv[1]), sys.argv[2]
    px, pal, (w, h) = walker(n)
    im = Image.fromarray(px.astype(np.uint8), 'P')
    im.putpalette([v for c in pal for v in c] + [0] * (768 - 48))
    im.save(path, transparency=0)
    print(n, px.shape, (w, h))
