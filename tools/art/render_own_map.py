"""Render one of our own maps from the codebase's data (tiles.png, palettes, metatiles.bin, map.bin), as the game draws
it (no animation, no objects). Triple-layer metatiles (12 entries) or the classic two layers (8).
Usage: python3 tools/art/render_own_map.py MapName OUT.png"""
import os, sys, re, json, struct
import numpy as np
from PIL import Image
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'codebase')

def ts_dir(sym):
    """gTileset_X -> its data directory, via graphics.h's tiles INCBIN"""
    h = open(os.path.join(C, 'src/data/tilesets/headers.h')).read()
    m = re.search(r'const struct Tileset %s\s*=\s*\{(.*?)\};' % sym, h, re.S)
    tiles_sym = re.search(r'\.tiles\s*=\s*(\w+)', m.group(1)).group(1)
    g = open(os.path.join(C, 'src/data/tilesets/graphics.h')).read()
    p = re.search(r'%s\[\]\s*=\s*INCBIN_U32\("([^"]+)"' % tiles_sym, g).group(1)
    return os.path.join(C, os.path.dirname(p))

def load(d, base):
    im = Image.open(os.path.join(d, 'tiles.png')); a = np.array(im)
    if im.mode != 'P': raise SystemExit('tiles.png not indexed: ' + d)
    a = a & 15
    tiles = {base + i: a[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] for i in range(a.shape[0] // 8 * 16)}
    pals = {}
    for f in sorted(x for x in os.listdir(os.path.join(d, 'palettes')) if x.endswith('.pal')):
        n = int(f[:2]); L = open(os.path.join(d, 'palettes', f)).read().split()
        pals[n] = [tuple(int(v) for v in L[3 + i * 3:6 + i * 3]) for i in range(16)]
    mt = open(os.path.join(d, 'metatiles.bin'), 'rb').read()
    return tiles, pals, mt

def render(name):
    L = {l['id']: l for l in json.load(open(os.path.join(C, 'data/layouts/layouts.json')))['layouts'] if 'id' in l}
    j = json.load(open(os.path.join(C, 'data/maps', name, 'map.json'))); lay = L[j['layout']]
    pt, pp, pm = load(ts_dir(lay['primary_tileset']), 0)
    st, sp, sm = load(ts_dir(lay['secondary_tileset']), 512)
    tiles = {**pt, **st}
    pals = {i: (pp[i] if i < 6 else sp.get(i, pp.get(i))) for i in range(13)}
    W, H = lay['width'], lay['height']
    grid = np.fromfile(os.path.join(C, lay['blockdata_filepath']), '<u2').reshape(H, W)
    npm = len(pm) // 24 if len(pm) % 24 == 0 and len(pm) // 24 <= 512 else None
    per = 12 if (len(pm) % 24 == 0 and len(sm) % 24 == 0) else 8
    out = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            m = int(grid[y, x] & 0x3FF)
            src, idx = (pm, m) if m < 512 else (sm, m - 512)
            ent = struct.unpack_from('<%dH' % per, src, idx * per * 2) if (idx + 1) * per * 2 <= len(src) else [0] * per
            cell = out[y * 16:y * 16 + 16, x * 16:x * 16 + 16]
            for q, e in enumerate(ent):
                tid, xf, yf, pl = e & 0x3FF, (e >> 10) & 1, (e >> 11) & 1, e >> 12
                t = tiles.get(tid)
                if t is None: continue
                if xf: t = t[:, ::-1]
                if yf: t = t[::-1]
                pal = pals.get(pl) or pals[0]
                oy, ox = ((q % 4) // 2) * 8, (q % 2) * 8
                sub = cell[oy:oy + 8, ox:ox + 8]
                if q < 4: sub[:] = np.array(pal)[t]
                else:
                    m_ = t != 0; sub[m_] = np.array(pal)[t][m_]
    return out

if __name__ == '__main__':
    Image.fromarray(render(sys.argv[1])).save(sys.argv[2])
