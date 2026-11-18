"""v7 tail motion (centreline rig keys from tail_fwd) + outline repair only.
Defects measured on the outline: notch = empty px with >=3 of 4 side-neighbours filled; spur = filled px with
<=1 side-neighbour filled.  Repair (keys 1-4 only): fill notches from the neighbour colour, re-home spurs into
an adjacent notch if one exists, else leave."""
import numpy as np, pickle
from PIL import Image
import tail_fwd as T
from tail_rig import TAIL, a, tx, ty
KEYS = [(0.0, 0.0), (0.08, 0.04), (0.17, 0.09), (0.27, 0.14), (0.36, 0.20)]
N4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cp = np.load('mask_cp.npy'); BODY = {(int(x), int(y)) for y, x in zip(*np.nonzero(cp & ~TAIL))}
def defects(o):
    filled = set(o) | BODY
    xs = [x for x, _ in o]; ys = [y for _, y in o]
    notch = [(x, y) for y in range(min(ys) - 1, max(ys) + 2) for x in range(min(xs) - 1, max(xs) + 2)
             if (x, y) not in filled and sum((x + dx, y + dy) in filled for dx, dy in N4) >= 3]
    spur = [p for p in o if sum((p[0] + dx, p[1] + dy) in filled for dx, dy in N4) <= 1]
    return notch, spur
ORIG_NOTCH = None
def repair(o):
    global ORIG_NOTCH
    if ORIG_NOTCH is None:
        ORIG_NOTCH = set(defects({(int(x), int(y)): a[y, x] for y, x in zip(ty, tx)})[0])
    o = dict(o)
    for _ in range(3):
        notch, spur = defects(o)
        notch = [p for p in notch if p not in ORIG_NOTCH]           # never fill gaps that are in the original art
        if not notch: break
        for (x, y) in notch:
            nb = [o[(x + dx, y + dy)] for dx, dy in N4 if (x + dx, y + dy) in o]
            if nb: o[(x, y)] = max(set(nb), key=nb.count)
    return o
orig = {(int(x), int(y)): a[y, x] for y, x in zip(ty, tx)}
base_n, base_s = defects(orig)
print('original outline: notches', len(base_n), 'spurs', len(base_s))
raw = [T.pose_fwd(T.bendf(*k)) for k in KEYS]
fixed = [raw[0]] + [repair(o) for o in raw[1:]]
for j in range(5):
    n0, s0 = defects(raw[j]); n1, s1 = defects(fixed[j])
    print('key', j, 'raw: px %d notches %d spurs %d  ->  repaired: px %d notches %d spurs %d' % (len(raw[j]), len(n0), len(s0), len(fixed[j]), len(n1), len(s1)))
print('key0 == original', fixed[0] == orig)
pickle.dump(fixed, open('tail_keys_v7fix.pkl', 'wb'))
im = Image.open('dr_title.png'); tp = np.array(im.getpalette()[:768]).reshape(256, 3)
bg = np.load('bg_filled_tail.npy'); scene = a.copy(); scene[TAIL] = bg[TAIL]
rows = []
for set_ in (raw, fixed):
    tiles = []
    for o in set_:
        sc = tp[scene].copy()
        for (x, y), v in o.items(): sc[y, x] = tp[v]
        tiles.append(Image.fromarray(sc[104:125, 62:92].astype(np.uint8)).resize((300, 210), Image.NEAREST))
    rows.append(tiles)
s = Image.new('RGB', (5 * 306, 426))
for r, tiles in enumerate(rows):
    for i, t in enumerate(tiles): s.paste(t, (i * 306, r * 216))
s.save('/tmp/v7fix.png')
