"""The bishops' study hall, mock v1, to the approved floor plan (bishops_plan.py; user 2026-11-23): the bishops' day
room for prayer, discussion and record keeping, where visiting diplomats and notables mingle.
18x13 tiles: wall rows 0-1 (Crown 7.9's wallpaper in the cathedral's cream), panelling row 2, cream marble rows 3-11,
the door from the nave at the bottom centre (row 12, x 8-9). The same room materials as Ambrose's study.
- Prayer, at the head on the axis from the door: a gold Arceus wheel on a blue roundel on the wall, an altar below it
  (Crown 9.3's cream table), a candelabra each side, the Order's banners at x 6 and 11; a prayer mat across the axis
  in front (the kneelers), a blue runner from it down to the door.
- Records, west: a scroll cabinet and a basket of scrolls against the west wall (Fantasma), the record clerk's table
  with its open ledger and inkwell (Fantasma) with his chair beside it; below it the writing desk with a sheet of
  paper, THE CLUE DESK (MonoMyth's writing desk, a chair before it; the paper is the letter the player can read).
- Discussion, east: a long table running north-south (MonoMyth's, lengthened), eight chairs, four each side facing it
  (MonoMyth's, the west four mirrored); bookcases (Crown 7.9) and a drawer cabinet for records (Fantasma) on the back
  wall; a sitting corner for visitors: two armchairs facing each other across a low table (Crown 9.3's own set).
- The dormitory's door in the north wall's west end (Crown 1.12's door), x 2.
- Busts on plinths flanking the runner near the door, a candelabra in the south-west corner.
(Plan change: the long table runs north-south instead of east-west, so its chairs can face it from the sides; same
footprint, same eight seats.)  Credits: Pokemon Crown, MonoMyth; Fantasma's art is public.
Usage: python3 hall_mock.py OUT.png"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'study'))
from cutter import load, cell, cut, T
import study_mock as SM
W, H = 18, 13
cool = lambda S: {c for c in S if not (c[0] > c[2] + 12)}       # stone is grey / blue-grey; wood is warm

def pieces():
    P, c79 = SM.pieces()
    fl = load(os.path.join(HERE, 'fantasma_library.png'))
    ffl = [(x, y) for x in (4, 5, 10, 11) for y in (8, 9)] + [(3, 6), (4, 6), (11, 6), (12, 6), (4, 10), (11, 10)]
    fcol = cool({tuple(p) for x, y in ffl for p in cell(fl, x, y).reshape(-1, 3)})
    alc = cool({tuple(p) for p in fl[6 * T:10 * T, 0:T].reshape(-1, 3)} | {tuple(p) for p in fl[6 * T:10 * T, 15 * T:17 * T].reshape(-1, 3)}
               | {tuple(p) for p in fl[5 * T:7 * T, 13 * T:16 * T].reshape(-1, 3)})
    wallr3 = cool({tuple(p) for p in fl[3 * T:4 * T, 4 * T:12 * T].reshape(-1, 3)})
    P['drawers'] = cut(fl, 2, 3, 2, 2, ffl, bgcols=[(3, fcol | wallr3), (4, fcol)])
    P['ledger'] = cut(fl, 1, 7, 2, 2, ffl, bgcols=[(7, fcol | alc), (8, fcol | alc)])
    P['basket'] = cut(fl, 2, 9, 1, 1, ffl, bgcols=[(9, fcol)])
    s = cut(fl, 14, 7, 2, 2, ffl, bgcols=[(7, fcol | alc), (8, fcol | alc)])[:, 8:24].copy()
    s[1:31, 1:15, 3] = 255                                   # (its dark interior matched the alcove: filled back)
    P['scrolls'] = s
    m18 = load(os.path.join(HERE, 'mm_8822718.png'))
    mfl = [(x, y) for x in (1, 2, 9, 10) for y in (9, 10)] + [(0, 10), (11, 10), (4, 10), (7, 10)]
    mcol = {tuple(p) for x, y in mfl for p in cell(m18, x, y).reshape(-1, 3)}
    t = cut(m18, 1, 7, 2, 2, mfl, bgcols=[(7, mcol), (8, mcol)])
    P['longtable'] = t[list(range(0, 14)) + [14] * 32 + list(range(14, 32))]   # lengthened to 2x4: its middle row repeated
    tone(P['longtable'])
    ch = cut(m18, 3, 7, 1, 1, mfl, bgcols=[(7, mcol)])
    P['chairE'] = ch; P['chairW'] = ch[:, ::-1].copy()
    c112 = load(os.path.join(HERE, 'cr_112.png'))
    door = cut(c112, 2, 0, 1, 2, [], fill_holes=False)
    door[(door[..., :3] > 200).all(-1), 3] = 0             # (Crown's pale wall above the door)
    P['walldoor'] = door
    c93 = load(os.path.join(HERE, '..', 'study', 'cr_93.png'))
    rug93 = [(x, y) for x in range(3, 10) for y in range(3, 8) if not (4 <= x <= 7 and 3 <= y <= 6)]
    P['sidechairE'] = cut(c93, 7, 5, 1, 2, rug93)          # (faces west)
    P['lowtable'] = cut(c93, 5, 5, 2, 2, rug93)
    P['altar'] = P['lowtable']
    return P, c79

def tone(p):
    """MonoMyth's table in the desks' dark wood: its colours ranked by brightness onto that ramp."""
    ramp = sorted(set(SM.DARKWOOD.values()), key=lambda c: sum(c))
    m = p[..., 3] > 0; cols = sorted({tuple(c) for c in p[m][:, :3]}, key=lambda c: .3 * c[0] + .59 * c[1] + .11 * c[2])
    for i, c in enumerate(cols):
        p[m & (p[..., :3] == c).all(-1), :3] = ramp[min(len(ramp) - 1, i * len(ramp) // len(cols))]

def emblem(img, cx, cy):
    """The Arceus wheel, gold on a blue roundel, on the wall above the altar."""
    im = Image.fromarray(img.astype(np.uint8)); d = ImageDraw.Draw(im)
    G0, G1, G2 = (112, 76, 28), (192, 142, 44), (244, 214, 116)
    d.ellipse((cx - 11, cy - 11, cx + 11, cy + 11), fill=(51, 60, 128), outline=G0)
    d.ellipse((cx - 8, cy - 8, cx + 8, cy + 8), outline=G1)
    for (dx, dy) in ((0, -1), (0, 1), (-1, 0), (1, 0)): d.line((cx, cy, cx + dx * 8, cy + dy * 8), fill=G2)
    for (dx, dy) in ((1, 1), (1, -1), (-1, 1), (-1, -1)): d.point((cx + dx * 6, cy + dy * 6), fill=G1)
    d.ellipse((cx - 2, cy - 2, cx + 2, cy + 2), fill=G2)
    return np.array(im).astype(int)

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
    # prayer: emblem, banners, altar, candelabras; the prayer mat and the runner
    img = emblem(img, 9 * T, 18)
    img = SM.banner(img, 6 * T + 8); img = SM.banner(img, 11 * T + 8)
    img[4 * T:5 * T, 7 * T:11 * T] = SM.rug(c79, 4, 1)
    img[5 * T:12 * T, 8 * T:10 * T] = SM.rug(c79, 2, 7)
    SM.paste(img, P['altar'], 8, 2)
    SM.paste(img, P['candelabra'], 7, 2); SM.paste(img, P['candelabra'], 10, 2)
    # dormitory door
    SM.paste(img, P['walldoor'], 2, 1)
    # records, west
    SM.paste(img, P['scrolls'], 1, 4); SM.paste(img, P['basket'], 1, 6)
    SM.paste(img, P['bookcase'], 4, 2)
    SM.paste(img, P['ledger'], 3, 5); SM.paste(img, P['chairW'], 2, 6)
    SM.paste(img, P['desk'], 3, 7)                                     # THE CLUE DESK (its paper: the letter)
    SM.paste(img, P['chairL'], 4, 9)                                   # (its clerk's chair, facing the desk)
    # discussion, east
    SM.paste(img, P['bookcase'], 12, 2); SM.paste(img, P['drawers'], 14, 2)
    SM.paste(img, P['longtable'], 13, 5)
    for y in range(5, 9):
        SM.paste(img, P['chairW'], 12, y); SM.paste(img, P['chairE'], 15, y)
    SM.paste(img, P['sidechair'], 13, 10); SM.paste(img, P['lowtable'], 14, 10); SM.paste(img, P['sidechairE'], 16, 10)
    # by the door
    SM.paste(img, P['bust'], 6, 10); SM.paste(img, P['bust'], 11, 10)
    SM.paste(img, P['candelabra'], 1, 10); SM.paste(img, P['candelabra'], 16, 3)
    o = Image.fromarray(img.astype(np.uint8)); o.save(out)
    o.resize((W * T * 3, H * T * 3), Image.NEAREST).save(out.replace('.png', '_3x.png'))

if __name__ == '__main__':
    main(sys.argv[1])
