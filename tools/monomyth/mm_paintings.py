"""The four framed paintings of North Edelweiss's museum (MonoMyth map header 0x886AA48) (user 2026-11-19: hang
museum paintings in Cadmus's manor, recoloured to make them unique).

In the museum map the frames are blank wall tiles; the paintings are object events (graphics ids 316-319, 32x32,
palette tags 0x1268-0x126B) hung over them. Their sheets are in MonoMyth's packed container, so they are decoded the
way mm_overworld.py decodes sprites: by the game, from the bedroom save state, with the player's images pointer
swapped for the painting's; the 32x32 frame (16 tiles, row-major) is read from OBJ VRAM. The graphics-info table
is at 0x893BF90.
Usage: python3 -I tools/monomyth/mm_paintings.py MONOMYTH.gba
Output: assets/monomyth_reference/pieces/painting_<name>.png (RGBA; the museum's name plaque kept below each frame).
"""
import os, struct, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mm_overworld as M

INFO_TABLE = 0x93BF90
NAMES = {316: 'starry', 317: 'dunes', 318: 'harbour', 319: 'figures'}
OUT = os.path.join(HERE, '..', '..', 'assets', 'monomyth_reference', 'pieces')

def palette(d, tag):
    for a in range(0, len(d) - 8, 4):
        p, t, z = struct.unpack_from('<IHH', d, a)
        if t == tag and z == 0 and 0x08000000 <= p < 0x0A000000:
            cols = struct.unpack_from('<16H', d, p - 0x08000000)
            if all(c < 0x8000 for c in cols):
                return np.array([((c & 31) << 3, ((c >> 5) & 31) << 3, ((c >> 10) & 31) << 3) for c in cols], np.uint8)

def main(rom):
    d = open(rom, 'rb').read(); g, base = M._gba(rom)
    for gid, name in NAMES.items():
        info = struct.unpack_from('<I', d, INFO_TABLE + 4 * gid)[0] - 0x08000000
        tag = struct.unpack_from('<H', d, info + 2)[0]; images = struct.unpack_from('<I', d, info + 28)[0]
        st = bytearray(base); st[M.SLOT:M.SLOT + 4] = struct.pack('<I', images); g.restore(bytes(st))
        g.run(2, 'UP'); g.run(20); g.run(2, 'DOWN'); g.run(20)
        v = np.frombuffer(bytes(g.state())[M.VRAM_OBJ:M.VRAM_OBJ + 512], np.uint8); px = np.zeros((32, 32), np.uint8)
        for t in range(16):
            tb = v[t * 32:(t + 1) * 32]; tile = np.zeros((8, 8), np.uint8)
            tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
            px[(t // 4) * 8:(t // 4) * 8 + 8, (t % 4) * 8:(t % 4) * 8 + 8] = tile
        rgba = np.zeros((32, 32, 4), np.uint8); rgba[..., :3] = palette(d, tag)[px]; rgba[..., 3] = (px != 0) * 255
        ys, xs = np.nonzero(px); rgba = rgba[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        Image.fromarray(rgba).save(os.path.join(OUT, 'painting_%s.png' % name)); print(name, rgba.shape)

if __name__ == '__main__':
    main(sys.argv[1])
