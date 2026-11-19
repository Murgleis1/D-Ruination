"""Export the flat 16-colour version of the empire map for the PokéLog habitat (area) screen.

    python3 tools/region_map/export_dex.py      # writes codebase/graphics/pokedex/map.{png,bin,pal}

The area screen draws its habitat glow over this map, so it is deliberately flat: terrain in solid
colours, no tree/peak stamps, roads and markers simplified. Same 240 x 160 geometry and 28 x 15 grid as
the Fly/Town map. 4bpp, one 16-colour palette; tiles de-duplicated with flips.
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import classify, paint
from layout import LAYOUT
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(REPO, 'codebase', 'graphics', 'pokedex')

PAL = [  # index 0 is transparent on a 4bpp BG and never drawn
 (0, 0, 0), (80, 104, 128), (88, 136, 136), (192, 224, 224), (128, 168, 120), (56, 96, 64),
 (192, 176, 152), (136, 128, 80), (248, 248, 248), (216, 216, 136), (56, 40, 40), (248, 152, 40),
 (64, 136, 120), (208, 216, 168), (16, 112, 48), (248, 88, 56)]
DEEP, SHALLOW, FOAM, GRASS, FOREST, ROCK, ROCK_D, SNOW, SAND, ASH, LAVA, MARSH, ROAD, ROAD_E, CITY = range(1, 16)
CLASS_COL = {classify.DEEP: DEEP, classify.SHALLOW: SHALLOW, classify.GRASS: GRASS, classify.FOREST: FOREST,
             classify.MOUNTAIN: ROCK, classify.SNOW: SNOW, classify.SAND: SAND, classify.ASH: ASH, classify.MARSH: MARSH}

def flat_map(cls):
    out = np.zeros(cls.shape, np.uint8)
    for c, v in CLASS_COL.items(): out[cls == c] = v
    water = cls <= classify.SHALLOW
    d = paint.dist_to(~water, 2); out[water & (d == 1) & (cls == classify.DEEP)] = FOAM     # thin coast line
    # roads: 2-px pale with a 1-px dark edge, as on the painted map
    fill = np.zeros(cls.shape, bool)
    for pts in paint.ROADS:
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            (x0, y0), (x1, y1) = paint.cell_px(ax, ay), paint.cell_px(bx, by)
            xs, xe = sorted((x0, x1)); ys, ye = sorted((y0, y1))
            fill[ys - 1:ye + 1, xs - 1:xe + 1] = True
    p = np.pad(fill, 1); edge = (p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:]) & ~fill
    out[edge] = ROAD_E; out[fill] = ROAD
    for name, kind, x, y, w, h in LAYOUT:                     # markers: towns small squares, cities long ones
        if kind not in ('town', 'city'): continue
        x0, y0 = 8 + 8 * x + 1, 16 + 8 * y + 1
        ww = 8 * w - 3 if kind == 'city' else 5
        out[y0:y0 + 6, x0:x0 + ww + 1] = ROAD_E
        out[y0 + 1:y0 + 5, x0 + 1:x0 + ww] = CITY if kind == 'city' else ROAD
    return out

def tiles_and_map(idx, pal_bits=0):
    full = np.full((160, 256), DEEP, np.uint8); full[:, :240] = idx
    tiles, lookup, tmap = [], {}, np.zeros((20, 32), np.uint16)
    for ty in range(20):
        for tx in range(32):
            t = full[ty*8:ty*8+8, tx*8:tx*8+8]
            for flip, v in ((0, t), (1, t[:, ::-1]), (2, t[::-1, :]), (3, t[::-1, ::-1])):
                k = v.tobytes()
                if k in lookup:
                    tmap[ty, tx] = lookup[k] | ((flip & 1) << 10) | ((flip >> 1) << 11) | (pal_bits << 12); break
            else:
                lookup[t.tobytes()] = len(tiles); tmap[ty, tx] = len(tiles) | (pal_bits << 12); tiles.append(t.copy())
    return tiles, tmap

def write(tiles, tmap, outdir=OUT):
    n = len(tiles); rows = (n + 15) // 16
    sheet = np.full((rows * 8, 128), DEEP, np.uint8)
    for i, t in enumerate(tiles):
        r, c = divmod(i, 16); sheet[r*8:r*8+8, c*8:c*8+8] = t
    im = Image.fromarray(sheet, 'P'); pal = [v for rgb in PAL for v in rgb] + [0] * (768 - 48)
    im.putpalette(pal); im.save(os.path.join(outdir, 'map.png'))
    tmap.astype('<u2').tofile(os.path.join(outdir, 'map.bin'))
    with open(os.path.join(outdir, 'map.pal'), 'w', newline='\r\n') as f:
        f.write('JASC-PAL\n0100\n16\n')
        for r, g, b in PAL: f.write(f'{r} {g} {b}\n')
    return n

if __name__ == '__main__':
    cls = classify.class_map(os.path.join(REPO, 'assets', 'region_map', 'cormorian_empire_illustrated.png'))
    idx = flat_map(cls)
    tiles, tmap = tiles_and_map(idx, 1)          # palette slot 1: where pokedex_area_region_map.c copies map.gbapal
    if '--preview' in sys.argv:
        Image.fromarray(np.array(PAL, np.uint8)[idx]).resize((720, 480), Image.NEAREST).save('/tmp/dex_flat.png')
        print('tiles', len(tiles))
    else:
        print('tiles', write(tiles, tmap))
