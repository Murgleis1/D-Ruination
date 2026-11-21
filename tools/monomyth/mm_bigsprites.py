"""MonoMyth's 64x64 overworld sprites (user 2026-11-21: the giant Druddighul that attacks you on top of the
Apocryphal Bastion, deep in the Webbed Woods, as stone statues in the Necropolis yard).

Its bastion top (map header 0x86E034, region section 48 "Apocryphal Bastion") holds four 64x64 object
graphics (ids 0x129, 0x175, 0x1DD, 0x1DE). Decoded by the game the way mm_paintings.py decodes the paintings:
the player's images pointer swapped for the sprite's, a turn, its frame read from OBJ VRAM (64 tiles, row-major,
8 a row).
Usage: python3 -I tools/monomyth/mm_bigsprites.py MONOMYTH.gba OUTDIR [gid ...]
"""
import os, struct, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mm_overworld as M
from mm_paintings import palette, INFO_TABLE

def frame(g, base, images, k, w=64, h=64):
    st = bytearray(base); st[M.SLOT:M.SLOT + 4] = struct.pack('<I', images + 8 * k); g.restore(bytes(st))
    g.run(2, 'UP'); g.run(20); g.run(2, 'DOWN'); g.run(20)
    n = (w // 8) * (h // 8); tw = w // 8
    v = np.frombuffer(bytes(g.state())[M.VRAM_OBJ:M.VRAM_OBJ + 32 * n], np.uint8); px = np.zeros((h, w), np.uint8)
    for t in range(n):
        tb = v[t * 32:(t + 1) * 32]; tile = np.zeros((8, 8), np.uint8)
        tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
        px[(t // tw) * 8:(t // tw) * 8 + 8, (t % tw) * 8:(t % tw) * 8 + 8] = tile
    return px

def main(rom, out, gids):
    os.makedirs(out, exist_ok=True)
    d = open(rom, 'rb').read(); g, base = M._gba(rom)
    for gid in gids:
        info = struct.unpack_from('<I', d, INFO_TABLE + 4 * gid)[0] - 0x08000000
        tag = struct.unpack_from('<H', d, info + 2)[0]; images = struct.unpack_from('<I', d, info + 28)[0]
        pal = palette(d, tag)
        if pal is None: pal = np.array([(i * 16, i * 16, i * 16) for i in range(16)], np.uint8)
        w, h = struct.unpack_from('<hh', d, info + 8)
        px = frame(g, base, images, 0, w, h)
        rgba = np.zeros((h, w, 4), np.uint8); rgba[..., :3] = pal[px]; rgba[..., 3] = (px != 0) * 255
        Image.fromarray(rgba).save(os.path.join(out, 'big_%03x.png' % gid)); print(hex(gid), (px != 0).sum())

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], [int(a, 16) for a in sys.argv[3:]] or [0x129, 0x175, 0x1DD, 0x1DE])
