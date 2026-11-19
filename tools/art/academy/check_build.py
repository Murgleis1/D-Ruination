"""Render the built Academy hall from the files the build wrote (tiles.png, .pal, metatiles, map.bin) and compare
it with the approved mock: every pixel must match, apart from colours the build merged (one GBA step apart).
Writes /home/claude/scratch/academy_built.png (the render) and prints the mismatch count."""
import os, sys, json, struct
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
C = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'codebase'))
import build_hall as B
def load(d):
    t = np.array(Image.open(os.path.join(d, 'tiles.png'))); n = t.shape[0] // 8 * 16
    tiles = [t[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] for i in range(n)]
    pals = []
    for i in range(16):
        L = open(os.path.join(d, 'palettes', f'{i:02d}.pal')).read().split('\n')[3:19]; pals.append([tuple(map(int, l.split())) for l in L])
    mt = open(os.path.join(d, 'metatiles.bin'), 'rb').read(); meta = [struct.unpack_from('<12H', mt, k) for k in range(0, len(mt), 24)]
    return tiles, pals, meta
pt, pp, pm = load(os.path.join(C, 'data/tilesets/primary/academy_interior'))
st, sp, sm = load(os.path.join(C, 'data/tilesets/secondary/academy_hall'))
pal = [pp[i] if i < 6 else sp[i] for i in range(16)]
def tile(t): return pt[t] if t < 512 else st[t - 512]
L = [l for l in json.load(open(os.path.join(C, 'data/layouts/layouts.json')))['layouts'] if l.get('id') == 'LAYOUT_PELLUCA_ACADEMY_HALL'][0]
W, H = L['width'], L['height']; grid = np.fromfile(os.path.join(C, L['blockdata_filepath']), '<u2').reshape(H, W)
under = np.zeros((H * 16, W * 16, 3), np.uint8); full = under.copy()
for y in range(H):
    for x in range(W):
        mid = int(grid[y, x] & 0x3FF); e = pm[mid] if mid < 512 else sm[mid - 512]
        for layer in range(3):
            for q in range(4):
                v = e[layer * 4 + q]; t = tile(v & 0x3FF)
                if v & 0x400: t = t[:, ::-1]
                if v & 0x800: t = t[::-1, :]
                P = np.array(pal[v >> 12], np.uint8); yy, xx = y * 16 + (q // 2) * 8, x * 16 + (q % 2) * 8
                mk = t != 0 if layer else np.ones((8, 8), bool)
                full[yy:yy + 8, xx:xx + 8][mk] = P[t][mk]
                if layer < 2: under[yy:yy + 8, xx:xx + 8][mk] = P[t][mk]
mock = B.UNDER.copy(); mock[B.OM] = B.OVER[B.OM]
bad = (np.abs(full.astype(int) - mock.astype(int)).sum(-1) > 0)
print('mismatched pixels', int(bad.sum()), '| under-layer mismatches', int((np.abs(under.astype(int) - B.UNDER.astype(int)).sum(-1) > 0).sum()))
Image.fromarray(full).resize((W * 32, H * 32), 0).save('/home/claude/scratch/academy_built.png')
