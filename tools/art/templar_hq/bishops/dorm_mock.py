"""The bishops' dormitory, mock v1, to the approved floor plan (bishops_plan.py; user 2026-11-23: one shared sleeping
room, six bishops).  20x10 tiles: wall rows 0-1 (cream), panelling row 2, cream marble rows 3-8, the door back to the
study hall at the bottom (row 9, x 9-10).
- Six beds along the north wall, heads to the wall (Crown 1.18's: white sheets, a blue frame), at x 2, 5, 8, 11, 14,
  17, rows 3-4; a bedside stand at each bed's head (Crown 7.9's small chest) and a footlocker at its foot (Crown
  9.3's chest of drawers); each bed reached from the tile right of its foot.
- The aisle (row 6) runs the room's length; the door's walkway runs up to it.
- Below the aisle: a wardrobe at each end (Crown 9.3's), with a candelabra beside it in the corner (Crown 18.1); a
  stone washbasin west (MonoMyth's); a small shrine east (Fantasma's lectern with its holy book between candelabras),
  under nothing but the room's quiet.
Credits: Pokemon Crown, MonoMyth; Fantasma's art is public.  Usage: python3 dorm_mock.py OUT.png"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'study'))
from cutter import load, cell, cut, T
import study_mock as SM
import hall_mock as HM
W, H = 20, 10
BEDS = (2, 5, 8, 11, 14, 17)

def pieces():
    P, c79 = HM.pieces()
    c93 = load(os.path.join(HERE, '..', 'study', 'cr_93.png'))
    junk = [(x, 11) for x in (2, 3, 8, 9)]                  # (the plain cells of that bottom row)
    P['footlocker'] = cut(c93, 5, 11, 1, 1, junk)
    P['wardrobe'] = cut(c93, 6, 11, 1, 1, junk)
    m18 = load(os.path.join(HERE, 'mm_8822718.png'))
    mfl = [(x, y) for x in (1, 2, 9, 10) for y in (9, 10)] + [(0, 10), (11, 10), (4, 10), (7, 10)]
    cab = load(os.path.join(HERE, '..', 'study', 'mm_cabin.png'))
    wallcols = {tuple(p) for p in cab[0:32, 16:24].reshape(-1, 3)} | {tuple(p) for p in cab[0:16, 56:64].reshape(-1, 3)}   # (bare planks only)
    fl_cab = [(x, y) for x in range(5, 9) for y in (3, 4, 5)]
    P['washstand'] = cut(cab, 4, 1, 1, 2, fl_cab + [(6, 2), (9, 2), (10, 2), (1, 3), (2, 3)], bgcols=[(1, wallcols)])
    w = P['washstand']; low = w[25:]; r, g, b_ = low[..., 0], low[..., 1], low[..., 2]
    low[(r > 150) & (r > b_ + 50) & (g > 100), 3] = 0          # (the cabin's light planks below the stand)
    foot = w[27:]; foot[(.3 * foot[..., 0] + .59 * foot[..., 1] + .11 * foot[..., 2]) > 90, 3] = 0   # (the cabin's white stand with its jug)
    fl = load(os.path.join(HERE, 'fantasma_library.png'))
    ffl = [(x, y) for x in (4, 5, 10, 11) for y in (8, 9)] + [(3, 6), (4, 6), (11, 6), (12, 6), (4, 10), (11, 10)]
    fcol = HM.cool({tuple(p) for x, y in ffl for p in cell(fl, x, y).reshape(-1, 3)})
    P['lectern'] = cut(fl, 4, 7, 1, 1, ffl, bgcols=[(7, fcol)])
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
    img[(H - 1) * T:H * T, 9 * T:11 * T] = c79[8 * T:9 * T, 4 * T:6 * T]
    SM.recolour(img, SM.MAT, rows >= (H - 1) * T)
    for x in BEDS:
        SM.paste(img, P['bed'], x, 3); SM.paste(img, P['chest'], x + 1, 3); SM.paste(img, P['footlocker'], x, 5)
    SM.paste(img, P['wardrobe'], 1, 6); SM.paste(img, P['wardrobe'], 18, 6)
    SM.paste(img, P['candelabra'], 1, 7); SM.paste(img, P['candelabra'], 18, 7)
    SM.paste(img, P['washstand'], 1, 2)                       # (in the north-west corner, against the panelling)
    img = HM.emblem(img, 10 * T, 18)                          # (the Arceus wheel over the door's axis)
    SM.paste(img, P['candelabra'], 14, 6); SM.paste(img, P['lectern'], 15, 7); SM.paste(img, P['candelabra'], 16, 6)
    o = Image.fromarray(img.astype(np.uint8)); o.save(out)
    o.resize((W * T * 3, H * T * 3), Image.NEAREST).save(out.replace('.png', '_3x.png'))

if __name__ == '__main__':
    main(sys.argv[1])
