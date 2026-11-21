"""Render a built map from the codebase's own files (its layout, both tilesets' tiles, palettes and metatiles):
what the game will draw. Usage: python3 render_built.py MapName OUT.png"""
import os, sys, json, struct, re
import numpy as np
from PIL import Image
C = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'codebase'))
HDR = open(C + '/src/data/tilesets/headers.h').read(); GR = open(C + '/src/data/tilesets/graphics.h').read()
MT = open(C + '/src/data/tilesets/metatiles.h').read()
def tileset(sym):
    m = re.search(r'const struct Tileset ' + sym + r'\s*=\s*\{(.*?)\};', HDR, re.S).group(1)
    g = lambda k, src: re.search(re.search(r'\.' + k + r' = (\w+)', m).group(1) + r'\[\]\[?1?6?\]? = (?:\{\s*)?INCBIN_U\d+\("([^"]+)"', src, re.S)
    tiles = re.search(re.search(r'\.tiles = (\w+)', m).group(1) + r'\[\] = INCBIN_U32\("([^"]+)"', GR).group(1)
    d = os.path.dirname(C + '/' + tiles)
    mts = re.search(re.search(r'\.metatiles = (\w+)', m).group(1) + r'\[\] = INCBIN_U16\("([^"]+)"', MT).group(1)
    return d, C + '/' + mts
def load(d):
    sheet = np.array(Image.open(d + '/tiles.png')); n = sheet.shape[0] // 8 * 16
    tiles = [sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] & 15 for i in range(n)]
    pals = []
    for i in range(16):
        L = open(d + '/palettes/%02d.pal' % i).read().split('\n')[3:19]; pals.append(np.array([[int(v) for v in l.split()] for l in L], np.uint8))
    return tiles, pals
def main(name, out, swaps=None, anim=None):
    """swaps: {(x, y): metatile id} (a script's setmetatile); anim: (first tile, frame PNG) for a tileset animation's frame."""
    m = json.load(open(C + '/data/maps/%s/map.json' % name))
    L = [l for l in json.load(open(C + '/data/layouts/layouts.json'))['layouts'] if l.get('id') == m['layout']][0]
    (pd, pm), (sd, sm) = tileset(L['primary_tileset']), tileset(L['secondary_tileset'])
    pt, pp = load(pd); st, sp = load(sd)
    pals = [pp[i] if i < 6 else sp[i] for i in range(16)]
    meta = lambda f: [struct.unpack('<12H', f[i * 24:i * 24 + 24]) for i in range(len(f) // 24)]
    PM, SM = meta(open(pm, 'rb').read()), meta(open(sm, 'rb').read())
    W, H = L['width'], L['height']; grid = np.fromfile(C + '/' + L['blockdata_filepath'], '<u2').reshape(H, W)
    for (x, y), v in (swaps or {}).items(): grid[y, x] = (grid[y, x] & 0xFC00) | v
    if anim:
        a = np.array(Image.open(anim[1])) & 15
        for i in range(a.shape[0] // 8): pt[anim[0] + i] = a[i * 8:i * 8 + 8, :8]
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            mid = grid[y, x] & 0x3FF; e = PM[mid] if mid < 512 else SM[mid - 512]
            for q, v in enumerate(e):
                t = v & 0x3FF
                if q >= 4 and not t: continue
                tl = pt[t] if t < 512 else st[t - 512] if t - 512 < len(st) else np.zeros((8, 8), np.uint8)
                if v & 0x400: tl = tl[:, ::-1]
                if v & 0x800: tl = tl[::-1]
                qq = q % 4; yy, xx = y * 16 + (qq // 2) * 8, x * 16 + (qq % 2) * 8
                mk = tl != 0 if q >= 4 else np.ones((8, 8), bool); img[yy:yy + 8, xx:xx + 8][mk] = pals[v >> 12][tl][mk]
    Image.fromarray(img).save(out)
if __name__ == '__main__': main(*sys.argv[1:3])
