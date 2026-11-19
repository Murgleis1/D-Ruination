"""Export the painted empire-era region map as the game's region-map graphics.

    python3 tools/region_map/export.py            # writes codebase/graphics/pokenav/region_map/map.{png,bin,pal}

The map is an 8bpp text background (Fly map and Town map): pixel values are 112 + palette index, so the
48 colours load into BG palette slots 7-9 (colours 112-159), clear of the frame (slot 1) and the text
palettes (13-15). Tiles are de-duplicated with horizontal/vertical flips; the tilemap is 32 x 20 entries
(the visible 30 x 20 screen plus two unseen columns). The engine side lives in src/region_map.c
(DR_REGION_MAP_CHAR_BASE: char block 1, room for 512 tiles before the frame's tiles at char block 3).
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import classify, paint

REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
SRC = os.path.join(REPO, 'assets', 'region_map', 'cormorian_empire_illustrated.png')
OUT = os.path.join(REPO, 'codebase', 'graphics', 'pokenav', 'region_map')
PAL_BASE = 112          # BG palette slot 7
MAX_TILES = 512

def painted():
    """Painted map with the parchment finish: returns (indices, 48-colour palette)."""
    paint.rng = np.random.default_rng(7)
    cls = classify.class_map(SRC)
    return paint.antique(paint.paint(cls), cls)

def tiles_and_map(idx):
    H, W = idx.shape                                  # 160 x 240
    full = np.full((160, 256), 7, np.uint8)           # unseen columns: open sea
    full[:H, :W] = idx
    full = full + PAL_BASE
    tiles, lookup, tmap = [], {}, np.zeros((20, 32), np.uint16)
    for ty in range(20):
        for tx in range(32):
            t = full[ty*8:ty*8+8, tx*8:tx*8+8]
            for flip, v in ((0, t), (1, t[:, ::-1]), (2, t[::-1, :]), (3, t[::-1, ::-1])):
                k = v.tobytes()
                if k in lookup:
                    tmap[ty, tx] = lookup[k] | ((flip & 1) << 10) | ((flip >> 1) << 11)
                    break
            else:
                lookup[t.tobytes()] = len(tiles); tmap[ty, tx] = len(tiles); tiles.append(t.copy())
    if len(tiles) > MAX_TILES:
        raise SystemExit(f'{len(tiles)} unique tiles: over the {MAX_TILES}-tile budget')
    return tiles, tmap

def write(tiles, tmap, colours, outdir=OUT):
    n = len(tiles); rows = (n + 15) // 16
    sheet = np.full((rows * 8, 128), PAL_BASE + 7, np.uint8)
    for i, t in enumerate(tiles):
        r, c = divmod(i, 16); sheet[r*8:r*8+8, c*8:c*8+8] = t
    im = Image.fromarray(sheet, 'P')
    pal = [0] * 768
    for i, (r, g, b) in enumerate(colours):
        pal[(PAL_BASE + i) * 3:(PAL_BASE + i) * 3 + 3] = [r, g, b]
    im.putpalette(pal); im.save(os.path.join(outdir, 'map.png'), optimize=False)
    tmap.astype('<u2').tofile(os.path.join(outdir, 'map.bin'))
    with open(os.path.join(outdir, 'map.pal'), 'w', newline='\r\n') as f:
        f.write('JASC-PAL\n0100\n%d\n' % len(colours))
        for r, g, b in colours: f.write(f'{r} {g} {b}\n')
    return n

if __name__ == '__main__':
    idx, colours = painted()
    tiles, tmap = tiles_and_map(idx)
    print('tiles', write(tiles, tmap, colours), 'colours', len(colours))
