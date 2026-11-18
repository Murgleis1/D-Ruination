import pickle, numpy as np, sys
from PIL import Image, ImageDraw
import tail_repair as R
from tail_rig import TAIL, a, tx, ty
im = Image.open('dr_title.png'); tp = np.array(im.getpalette()[:768]).reshape(256, 3)
bg = np.load('bg_filled_tail.npy'); scene = a.copy(); scene[TAIL] = bg[TAIL]
poses = pickle.load(open(sys.argv[1], 'rb')); ks = [int(k) for k in sys.argv[2].split(',')]
orig = {(int(x), int(y)): a[y, x] for y, x in zip(ty, tx)}
Z = 16; X0, Y0, X1, Y1 = 62, 104, 92, 125
tiles = []
for k in ks:
    o = poses[k]; sc = tp[scene].copy()
    for (x, y), v in o.items(): sc[y, x] = tp[v]
    t = Image.fromarray(sc[Y0:Y1, X0:X1].astype(np.uint8)).resize(((X1 - X0) * Z, (Y1 - Y0) * Z), Image.NEAREST); d = ImageDraw.Draw(t)
    n, s = R.defects(o)
    for (x, y) in s: d.rectangle([(x - X0) * Z, (y - Y0) * Z, (x - X0) * Z + Z - 1, (y - Y0) * Z + Z - 1], outline=(255, 0, 0), width=2)
    for (x, y) in n: d.rectangle([(x - X0) * Z, (y - Y0) * Z, (x - X0) * Z + Z - 1, (y - Y0) * Z + Z - 1], outline=(255, 255, 0), width=2)
    tiles.append(t)
W = tiles[0].size[0]; s_ = Image.new('RGB', (len(tiles) * (W + 6), tiles[0].size[1]))
for i, t in enumerate(tiles): s_.paste(t, (i * (W + 6), 0))
s_.save('/tmp/zoomcheck.png')
