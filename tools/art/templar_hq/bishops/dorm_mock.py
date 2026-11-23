"""The bishops' dormitory, mock v2 (user 2026-11-23: v1's beds, chests and drawers "looks really awkward"; redesign
after other games' multi-bed rooms, `assets/templar_hq_reference/dorm_references.png`: MonoMyth's inn 87ed300 and hut
87f6e98, Odyssey 11.8. Their rule: beds grouped and bare, one shared set of furniture; no bed has its own stand or
footlocker. User's pick: beds down both sides, monastery style).
14x16 tiles: wall rows 0-1 (cream), panelling row 2, cream marble rows 3-14, the door back to the study hall at the
bottom centre (row 15, x 6-7).
- Six beds, three down each side, heads north, end to end as in Odyssey 11.8 (Odyssey's bed: a wooden headboard, a
  blue quilt): x 1-2 and 11-12, rows 3-6, 7-10, 11-14.
- The centre aisle: a long blue-and-gold rug from the door to the head; on it one shared table (MonoMyth's long
  table, dark wood) with chairs either side, for reading and the evening meal.
- At the head on the axis: the Arceus wheel on the wall, an altar (Crown 9.3's cream table) between candelabras, as
  in the study hall.
- By the door: one wardrobe for the six (Fantasma's drawer cabinet) and a washstand (MonoMyth's white stand).
Credits: Odyssey, Pokemon Crown, MonoMyth; Fantasma's art is public.  Usage: python3 dorm_mock.py OUT.png"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'study'))
from cutter import load, cell, cut, T
import study_mock as SM
import hall_mock as HM
W, H = 14, 16

def pieces():
    P, c79 = HM.pieces()
    o = load(os.path.join(HERE, 'ody_118.png'))
    fl = [(x, y) for x in (1, 2, 3, 4, 5, 6) for y in (7, 8)] + [(6, 3), (6, 4), (6, 5), (6, 6)]
    bed = cut(o, 7, 5, 2, 4, fl)
    foot = bed[56:]; foot[(foot[..., 0] > foot[..., 2] + 10), 3] = 0     # (Odyssey's floor under the quilt's hem)
    P['bed'] = bed
    cab = load(os.path.join(HERE, '..', 'study', 'mm_cabin.png'))
    wallcols = {tuple(p) for p in cab[0:32, 16:24].reshape(-1, 3)} | {tuple(p) for p in cab[0:16, 56:64].reshape(-1, 3)}
    fl_cab = [(x, y) for x in range(5, 9) for y in (3, 4, 5)]
    w = cut(cab, 4, 1, 1, 2, fl_cab + [(6, 2), (9, 2), (10, 2), (1, 3), (2, 3)], bgcols=[(1, wallcols)])
    low = w[25:]; low[(low[..., 0] > 150) & (low[..., 0] > low[..., 2] + 50) & (low[..., 1] > 100), 3] = 0
    foot = w[27:]; foot[(.3 * foot[..., 0] + .59 * foot[..., 1] + .11 * foot[..., 2]) > 90, 3] = 0
    P['washstand'] = w
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
    img[(H - 1) * T:H * T, 6 * T:8 * T] = c79[8 * T:9 * T, 4 * T:6 * T]
    SM.recolour(img, SM.MAT, rows >= (H - 1) * T)
    img[4 * T:15 * T, 5 * T:9 * T] = SM.rug(c79, 4, 11)                 # the aisle rug
    img = HM.emblem(img, 7 * T, 18)
    SM.paste(img, P['altar'], 6, 2)
    SM.paste(img, P['candelabra'], 5, 2); SM.paste(img, P['candelabra'], 8, 2)
    for y in (3, 7, 11):
        SM.paste(img, P['bed'], 1, y); SM.paste(img, P['bed'], 11, y)
    SM.paste(img, P['longtable'], 6, 6)
    for y in range(6, 10):
        SM.paste(img, P['chairW'], 5, y); SM.paste(img, P['chairE'], 8, y)
    SM.paste(img, P['drawers'], 3, 13)
    SM.paste(img, P['washstand'], 10, 13)
    o = Image.fromarray(img.astype(np.uint8)); o.save(out)
    o.resize((W * T * 3, H * T * 3), Image.NEAREST).save(out.replace('.png', '_3x.png'))

if __name__ == '__main__':
    main(sys.argv[1])
