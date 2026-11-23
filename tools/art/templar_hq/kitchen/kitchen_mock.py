"""The kitchen, mock v1 (behind the nave's west door at its foot): the prime cathedral's kitchen, where the Templars
cook and feed themselves (user 2026-11-22). Built from MonoMyth's restaurant (user 2026-11-23: its kitchen-plus-
restaurant; the red-walled rooms 8822718, 8823d94, 88235c8 and the banquet hall 882346c), in the cathedral's cream and
the Order's blue, with the user's pot-bellied stove from MonoMyth's cabin (8864c00).
18x13 tiles: wall rows 0-1 (cream), panelling row 2, cream marble rows 3-11, the door from the nave at the bottom
centre (row 12, x 8-9). The study's room materials.
- The back wall, cooking: the pot-bellied stove (its pipe to the ceiling) with firewood stacked beside it; the kitchen
  line (8822718: a stone counter with plates and the stove top with its pan, a prep table with a sheet of paper and a
  flowerpot); the shelf of bottles on the wall (88235c8); barrels at the east end (Odyssey 30.0).
- The pass: the marble serving counter (8823d94, a pot on its corner) in front of the line, the cooks between them.
- Eating: two banquet tables (882346c's, shortened to five tiles, two serving bowls each) either side of the aisle from the door, chairs on both long
  sides, their cushions in the Order's blue.
Credits: MonoMyth, Odyssey, Pokemon Crown.  Usage: python3 kitchen_mock.py OUT.png"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'study'))
from cutter import load, cell, cut, T
import study_mock as SM
W, H = 18, 13
BLUE = ((36, 74, 155), (62, 96, 190), (28, 60, 130))

def blue_cushions(p):
    """MonoMyth's red cushions in the Order's blue (by brightness)."""
    a = p[..., :3]; r, g, b = a[..., 0], a[..., 1], a[..., 2]; m = (p[..., 3] > 0) & (r > g + 60) & (r > b + 50)
    L = .3 * r + .59 * g + .11 * b
    for sel, c in ((m & (L >= 110), BLUE[1]), (m & (L >= 75) & (L < 110), BLUE[0]), (m & (L < 75), BLUE[2])):
        a[sel] = c

def pieces():
    P, c79 = SM.pieces()
    k1 = load(os.path.join(HERE, '8822718_12x16.png')); k2 = load(os.path.join(HERE, '8823d94_14x14.png'))
    k3 = load(os.path.join(HERE, '88235c8_16x16.png')); bq = load(os.path.join(HERE, '882346c_30x12_s240.png'))
    cab = load(os.path.join(HERE, '8864c00_11x10.png'))
    cols = lambda a, cells: {tuple(p) for x, y in cells for p in cell(a, x, y).reshape(-1, 3)}
    warm = lambda S: {c for c in S if c[0] > c[2] + 15}
    l = cut(k1, 4, 3, 4, 2, [(4, 5), (5, 5), (6, 5), (7, 5), (5, 2), (6, 2), (7, 2)])
    l[:9, :, 3] = 0; l[9:12, :40, 3] = 0; l[9:12, 48:, 3] = 0     # (the alcove's brick above it)
    l[12:30, 40:63, 3] = 255                                      # (the prep table's wood matched the brick)
    P['line'] = l
    fl2 = [(x, y) for x in (1, 2, 3, 9, 10, 11) for y in (3, 4, 5)]
    sv = cut(k2, 4, 2, 5, 3, fl2, bgcols=[(2, cols(k2, [(3, 2), (9, 2), (10, 2)]))])
    sv[:T, T:4 * T, 3] = 0                                    # (specks of its room between the counter's arms)
    P['serve'] = sv
    P['bottles'] = cut(k3, 1, 0, 2, 2, [], bgcols=[(0, cols(k3, [(4, 0), (5, 0)])), (1, cols(k3, [(4, 1), (5, 1)]))])
    flb = [(x, y) for x in (8, 9, 10, 11) for y in (7,)] + [(4, 4), (4, 5), (25, 4), (25, 5)]
    t = cut(bq, 6, 4, 18, 2, flb)
    tb = t[:, list(range(0, 16)) + [60] * (5 * T - 32) + list(range(272, 288))].copy()   # (5 tiles: its ends, plain middle)
    bowl = t[5:19, 15:33].copy()                              # (one of its serving bowls, whole)
    for bx in (12, 50):
        m = bowl[..., 3] > 0; tb[5:19, bx:bx + 18][m] = bowl[m]
    P['table'] = tb
    P['chairN'] = cut(bq, 6, 3, 1, 1, flb + [(5, 3), (7, 3)]); P['chairS'] = cut(bq, 6, 6, 1, 1, flb + [(5, 6), (7, 6)])
    for k in ('chairN', 'chairS'): blue_cushions(P[k])
    flc = [(x, y) for x in (5, 6, 7, 8) for y in (3, 4)] + [(1, 4), (2, 4)]
    wc = warm({tuple(p) for p in cab[0:32, 16:24].reshape(-1, 3)} | {tuple(p) for p in cab[0:32, 64:80].reshape(-1, 3)}
              | {tuple(p) for p in cab[0:16, 144:160].reshape(-1, 3)})
    P['stove'] = cut(cab, 2, 0, 2, 3, flc, bgcols=[(0, wc), (1, wc), (2, wc)])
    wcab = cols(cab, [(1, 0), (4, 0), (9, 0)]) | {tuple(p) for p in cab[0:16, 16:24].reshape(-1, 3)}
    P['wood'] = cut(cab, 1, 1, 1, 2, flc, bgcols=[(1, wcab)])
    o3 = load(os.path.join(HERE, '..', 'registry', 'ody_300.png'))
    ofl3 = [(x, y) for x in (3, 4, 10, 11) for y in (5, 6, 7)]
    P['barrel'] = cut(o3, 5, 4, 1, 1, ofl3)
    return P, c79

def put(img, p, x, y):
    h, w = p.shape[:2]; m = p[..., 3] > 0
    img[y:y + h, x:x + w][m] = p[..., :3][m]

def main(out):
    P, c79 = pieces()
    img = np.zeros((H * T, W * T, 3), int)
    for x in range(1, W - 1):
        img[0:2 * T, x * T:(x + 1) * T] = c79[0:2 * T, 3 * T:4 * T]
        img[2 * T:3 * T, x * T:(x + 1) * T] = cell(c79, 3, 2)
        for y in range(3, H - 1):
            src = (5, 3) if y == 3 else (1, 4) if x == 1 else (3, 6)
            img[y * T:(y + 1) * T, x * T:(x + 1) * T] = cell(c79, *src)
    rows = np.arange(H * T)[:, None].repeat(W * T, 1)
    SM.recolour(img, SM.WALL, rows < 2 * T)
    img[(H - 1) * T:H * T, 8 * T:10 * T] = c79[8 * T:9 * T, 4 * T:6 * T]
    SM.recolour(img, SM.MAT, rows >= (H - 1) * T)
    # the back wall
    s = P['stove']; ys, xs = np.nonzero(s[..., 3] > 0)
    put(img, s, 1 * T, 4 * T - (ys.max() + 1))                     # (standing on the floor line)
    top = 4 * T - (ys.max() + 1) + ys.min()
    pipe = s[ys.min():ys.min() + 1]                                  # (its pipe carried up to the ceiling)
    for y in range(0, top): put(img, pipe, 1 * T, y)
    SM.paste(img, P['wood'], 3, 2)
    put(img, P['line'], 5 * T, 4 * T - 32)
    SM.paste(img, P['bottles'], 11, 0)
    for x in (13, 14, 16): SM.paste(img, P['barrel'], x, 3)
    # the pass
    SM.paste(img, P['serve'], 6, 4)
    # eating: two tables either side of the aisle (x 7-10)
    for x0 in (1, 12):
        SM.paste(img, P['table'], x0, 8)
        for x in range(x0, x0 + 5):
            SM.paste(img, P['chairN'], x, 7); SM.paste(img, P['chairS'], x, 10)
    o = Image.fromarray(img.astype(np.uint8)); o.save(out)
    o.resize((W * T * 3, H * T * 3), Image.NEAREST).save(out.replace('.png', '_3x.png'))

if __name__ == '__main__':
    main(sys.argv[1])
