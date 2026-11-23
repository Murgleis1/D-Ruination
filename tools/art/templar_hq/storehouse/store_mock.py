"""The storehouse, mock v1, to the approved floor plan v1 (store_plan.py; user 2026-11-23): where the Templars keep
their food. 16x12 tiles: wall rows 0-1 (cream), panelling row 2, cream marble rows 3-10, the door from the nave at the
bottom centre (row 11, x 7-8). The study's room materials.
- Back wall: two shelves of preserves and bottles (MonoMyth 88235c8's bottle shelf); crate stacks against it at the
  ends (MonoMyth's warehouse 87f254c).
- The middle: rows of stacked crates (the warehouse's, three stacks a row) with aisles between and around them.
- East wall: barrels (Odyssey 30.0). West wall: clay jars and pots of grain and flour (MonoMyth's desert house
  8840fe0; no source has sacks).
- The quartermaster's small desk with the stores ledger (MonoMyth's writing desk), in the south-east, a chair before
  it.
Credits: MonoMyth, Odyssey, Pokemon Crown.  Usage: python3 store_mock.py OUT.png"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'study')); sys.path.insert(0, os.path.join(HERE, '..', 'kitchen'))
from cutter import load, cell, cut, T
import study_mock as SM
import kitchen_mock as KM
W, H = 16, 12

def pieces():
    P, c79 = KM.pieces()
    wh = load(os.path.join(HERE, '87f254c_11x11.png'))
    whfl = [(x, y) for x in range(0, 11) for y in (9, 10)]
    c = cut(wh, 3, 4, 3, 2, whfl + [(4, 3), (5, 3), (6, 3)])
    P['crates'] = c
    c2 = cut(wh, 1, 2, 2, 2, whfl + [(4, 3), (5, 3)], bgcols=[(2, {tuple(p) for p in cell(wh, 4, 2).reshape(-1, 3)})])
    r, g, b = c2[..., 0], c2[..., 1], c2[..., 2]
    c2[(r > 180) & (g > 180) & (b > 180), 3] = 0              # (the warehouse's white floor; the crates are wood)
    P['crates2'] = c2
    ds = load(os.path.join(HERE, '8840fe0_10x14.png'))
    dfl = [(x, 3) for x in (2, 3, 4, 5, 6, 7)] + [(4, 7), (5, 7), (3, 6), (6, 6), (2, 8)]
    P['jar'] = cut(ds, 2, 11, 1, 1, dfl + [(1, 11), (1, 10), (3, 11)])   # (a jar from the room's middle, not its edge)
    P['pots'] = cut(ds, 3, 9, 1, 1, dfl + [(2, 9)])
    P['jar2'] = cut(ds, 6, 9, 1, 1, dfl + [(5, 9), (7, 9)])
    return P, c79

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
    img[(H - 1) * T:H * T, 7 * T:9 * T] = c79[8 * T:9 * T, 4 * T:6 * T]
    SM.recolour(img, SM.MAT, rows >= (H - 1) * T)
    # back wall
    SM.paste(img, P['bottles'], 5, 0); SM.paste(img, P['bottles'], 9, 0)
    SM.paste(img, P['crates2'], 1, 2); SM.paste(img, P['crates2'], 13, 2)
    # crate rows, aisles between (row 6) and around
    SM.paste(img, P['crates'], 3, 4); SM.paste(img, P['crates'], 10, 4)
    SM.paste(img, P['crates'], 3, 7)
    # east wall barrels, west wall jars
    for y in (5, 6, 7, 8, 9): SM.paste(img, P['barrel'], 14, y)
    for y, k in ((5, 'jar'), (6, 'pots'), (7, 'jar2'), (8, 'jar'), (9, 'pots')): SM.paste(img, P[k], 1, y)
    # the quartermaster
    SM.paste(img, P['desk'], 10, 7); SM.paste(img, P['chairL'], 11, 9)
    o = Image.fromarray(img.astype(np.uint8)); o.save(out)
    o.resize((W * T * 3, H * T * 3), Image.NEAREST).save(out.replace('.png', '_3x.png'))

if __name__ == '__main__':
    main(sys.argv[1])
