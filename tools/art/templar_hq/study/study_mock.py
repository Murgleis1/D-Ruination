"""Ambrose's study, mock v2: built to the approved floor plan v2 (study_plan.py; user 2026-11-23: v1 "doesn't really
feel like an office": no chair behind the desk, none facing it, nowhere to rest overnight, a stray bureau behind the
desk).  14x12 tiles: wall rows 0-1 (Crown 7.9's wallpaper, in the cathedral's cream) and row 2 (its wood panelling),
floor rows 3-10 (its cream marble; the top row and the west edge in its wall shadow), the door from the nave at the
bottom centre (row 11, x 6-7).
By use:
- work: MonoMyth's writing desk (paper, quill, inkwell; in a darker wood than his chair) centred on a blue-and-gold rug (Crown 7.9's, widened),
  Ambrose's chair behind it facing the door (Crown 9.3's armchair), two visitor chairs before it facing him (Crown
  7.9's), the walkway from the door straight up to them kept clear;
- back wall: two bookcases west (Crown 7.9), the Order's banner with Arceus's wheel behind his chair (drawn as in the
  Sanctum);
- rest (east): a bed in the corner, head to the wall (Crown 1.18's: white sheets, a blue frame), a small chest as
  its bedside stand (Crown 7.9), the chest of drawers for his robes (MonoMyth's bureau, wood toned to the bookcases),
  a pair of folding-screen panels (MonoMyth) at its foot shielding it from the room; the bed is reached from the
  tile beside it (x 11, row 4);
- reading (west): an armchair facing a tea table (Crown 9.3, MonoMyth);
- by the door: two busts on plinths (Crown 7.9) and two candelabras in the corners (Crown 18.1).
Credits: Pokemon Crown, MonoMyth.  Usage: python3 study_mock.py OUT.png"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
from cutter import load, cell, cut, T
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 14, 12
WOOD = {(56, 56, 64): (40, 40, 48), (72, 64, 64): (64, 40, 32), (88, 72, 72): (96, 60, 44), (104, 80, 88): (128, 80, 56),
        (104, 80, 80): (128, 80, 56), (128, 96, 96): (168, 120, 72), (152, 136, 128): (200, 152, 96),
        (168, 152, 144): (224, 184, 128)}
DARKWOOD = {(56, 56, 64): (32, 28, 32), (72, 64, 64): (48, 32, 28), (88, 72, 72): (64, 40, 32), (104, 80, 88): (96, 60, 44),
            (104, 80, 80): (96, 60, 44), (128, 96, 96): (128, 80, 56), (152, 136, 128): (168, 120, 72),
            (168, 152, 144): (200, 152, 96)}
WALL = {(152, 136, 104): (208, 200, 180), (120, 104, 96): (166, 156, 130), (184, 184, 160): (230, 224, 208),
        (96, 80, 72): (140, 132, 110)}
RUG = {(216, 112, 104): (36, 74, 155), (200, 88, 80): (28, 60, 130), (160, 64, 104): (0, 40, 82),
       (104, 56, 88): (0, 30, 64), (208, 216, 104): (177, 149, 48)}
MAT = {(160, 64, 104): (36, 74, 155), (200, 88, 80): (0, 40, 82), (192, 168, 168): (177, 149, 48)}

def recolour(a, table, mask=None):
    m = np.ones(a.shape[:2], bool) if mask is None else mask
    for s, d in table.items():
        a[m & (a[..., :3] == s).all(-1)] = d

def paste(img, p, tx, ty, dy=0):
    h, w = p.shape[:2]; x, y = tx * T, ty * T + dy; m = p[..., 3] > 0
    img[y:y + h, x:x + w][m] = p[..., :3][m]

def pieces():
    c79 = load(os.path.join(HERE, 'crown79.png')); c93 = load(os.path.join(HERE, 'cr_93.png'))
    c181 = load(os.path.join(HERE, 'cr_181.png')); scr = load(os.path.join(HERE, 'mm_screens.png'))
    cab = load(os.path.join(HERE, 'mm_cabin.png')); off = load(os.path.join(HERE, 'mm_office.png'))
    P = {}
    fl79 = [(x, y) for x in range(2, 8) for y in (6, 7)]
    P['bookcase'] = cut(c79, 1, 2, 2, 2, [(x, 2) for x in (3, 4, 5, 6)] + [(x, 3) for x in (3, 4, 5)] + fl79)
    P['bust'] = cut(c79, 8, 6, 1, 2, fl79)
    # visitor chairs: Crown 7.9's, cut against its rug (the rug's own column x=60 carried across where they stand)
    rugfill = c79.copy(); rugfill[4 * T:6 * T, 4 * T:6 * T] = c79[4 * T:6 * T, 60:61]
    for k, x in (('chairL', 4), ('chairR', 5)):
        p = np.zeros((T, T, 4), int); p[..., :3] = cell(c79, x, 5)
        p[..., 3] = np.where((cell(c79, x, 5) == cell(rugfill, x, 5)).all(-1), 0, 255)
        for c in RUG: p[(p[..., :3] == c).all(-1), 3] = 0         # (no specks of Crown's old rug)
        P[k] = p
    rug93 = [(x, y) for x in range(3, 10) for y in range(3, 8) if not (4 <= x <= 7 and 3 <= y <= 6)]
    P['armchair'] = cut(c93, 5, 3, 2, 2, rug93)
    P['sidechair'] = cut(c93, 4, 5, 1, 2, rug93)
    fl181 = [(x, y) for x in range(3, 5) for y in range(3, 6)] + [(x, y) for x in range(6, 9) for y in range(3, 5)]
    P['candelabra'] = cut(c181, 5, 5, 1, 2, fl181)
    flscr = [(x, 3) for x in range(2, 10)] + [(x, 6) for x in range(2, 9)] + [(x, y) for x in range(5, 9) for y in (4, 5)]
    P['screen'] = cut(scr, 3, 7, 1, 2, flscr)
    P['teatable'] = cut(scr, 3, 4, 2, 2, flscr)
    fl_cab = [(x, y) for x in range(5, 9) for y in (3, 4, 5)]
    wallcols = {tuple(p) for p in cab[0:16, 16:48].reshape(-1, 3)} | {tuple(p) for p in cab[16:32, 0:16].reshape(-1, 3)}
    c118 = load(os.path.join(HERE, 'cr_118.png'))
    fl118 = [(x, y) for x in (2, 3, 5) for y in (5, 6, 7)] + [(1, 5), (1, 6)]
    floorc = {tuple(p) for x, y in fl118 for p in cell(c118, x, y).reshape(-1, 3)}
    bed = cut(c118, 4, 2, 1, 2, fl118, bgcols=[(2, floorc)])
    top = bed[:5]; orange = (top[..., 0] > 200) & (top[..., 1] > 140) & (top[..., 2] < 120); top[orange, 3] = 0
    P['bed'] = bed                                            # (Crown 1.18's bed: white sheets, a blue frame)
    P['chest'] = cut(c79, 6, 3, 1, 1, [(5, 3), (4, 3), (3, 3)])
    floors = [(x, y) for y in (4, 5, 6, 7) for x in range(3, 9)]
    orefs = floors + [(3, 1), (4, 1), (1, 1), (3, 0), (4, 0)]
    P['bureau'] = cut(off, 5, 1, 2, 2, orefs)
    d = cut(off, 7, 1, 2, 3, orefs)[:2 * T + 4]
    d[0:12, T:2 * T, 3] = 0                                   # (the wall picture above MonoMyth's desk)
    d[2 * T:, :, 3] = np.where(d[2 * T:, :, :3].sum(-1) < 200, 255, 0)   # (only the dark leg rail of row 3)
    P['desk'] = d
    recolour(P['bureau'][..., :3], WOOD, P['bureau'][..., 3] > 0)
    recolour(P['desk'][..., :3], DARKWOOD, P['desk'][..., 3] > 0)   # (darker, to stand off his gold chair)
    return P, c79

def bed_colours(p):
    """The cabin bed's plaid in the Order's blue and gold (its reds -> blue, its greens -> gold)."""
    a = p[..., :3]; r, g, b = a[..., 0], a[..., 1], a[..., 2]; m = p[..., 3] > 0
    red = m & (r > g + 40) & (r > b + 40); grn = m & (g > r + 20) & (g >= b)
    lum = .3 * r + .59 * g + .11 * b
    a[red] = np.where((lum[red] > 110)[:, None], (62, 96, 190), (36, 74, 155))
    a[grn] = np.where((lum[grn] > 120)[:, None], (210, 178, 72), (177, 149, 48))

def rug(c79, w, h):
    """Crown 7.9's rug (64x32 px), its desk and chairs taken out, widened to w x h tiles: its middle column and row
    repeated, corners and borders kept."""
    r = c79[4 * T:6 * T, 3 * T:7 * T].copy()
    r[:, T:3 * T] = r[:, 12:13]
    cw, ch = min(12, w * T // 2), min(12, h * T // 2)        # (borders shrink for small rugs: a one-tile mat)
    cols = list(range(0, cw)) + [12] * (w * T - 2 * cw) + list(range(64 - cw, 64))
    rows = list(range(0, ch)) + [16] * (h * T - 2 * ch) + list(range(32 - ch, 32))
    out = r[rows][:, cols]
    recolour(out, RUG); return out

def banner(img, cx):
    """The Order's banner with Arceus's wheel, as in the Sanctum (sanctum_mock.py), centred on x=cx."""
    im = Image.fromarray(img.astype(np.uint8)); d = ImageDraw.Draw(im)
    G0, G1, G2 = (112, 76, 28), (192, 142, 44), (244, 214, 116)
    x0, x1, y0, y1 = cx - 6, cx + 5, 9, 41
    d.rectangle((x0 - 1, y0 - 2, x1 + 1, y0 - 1), fill=G0)
    d.polygon([(x0, y0), (x1, y0), (x1, y1), ((x0 + x1) / 2, y1 + 3), (x0, y1)], fill=(51, 60, 128), outline=(22, 24, 38))
    d.line((x0 + 1, y0 + 1, x0 + 1, y1 - 1), fill=(62, 74, 163))
    bx, by = (x0 + x1) / 2, 24
    d.ellipse((bx - 4.5, by - 4.5, bx + 4.5, by + 4.5), outline=G1)
    for (dx, dy) in ((0, -1), (0, 1), (-1, 0), (1, 0)): d.line((bx, by, bx + dx * 4, by + dy * 4), fill=G2)
    d.line((x0 + 1, y1 - 3, x1 - 1, y1 - 3), fill=G1)
    return np.array(im).astype(int)

def main(out):
    P, c79 = pieces()
    img = np.zeros((H * T, W * T, 3), int)
    for x in range(1, W - 1):
        img[0:2 * T, x * T:(x + 1) * T] = c79[0:2 * T, 3 * T:4 * T]          # wallpaper
        img[2 * T:3 * T, x * T:(x + 1) * T] = cell(c79, 3, 2)                # panelling
        for y in range(3, H - 1):
            src = (5, 3) if y == 3 else (1, 4) if x == 1 else (3, 6)          # shadowed top row and west edge
            img[y * T:(y + 1) * T, x * T:(x + 1) * T] = cell(c79, *src)
    recolour(img, WALL, np.arange(H * T)[:, None].repeat(W * T, 1) < 2 * T)
    img = banner(img, 7 * T)
    img[(H - 1) * T:H * T, 6 * T:8 * T] = c79[8 * T:9 * T, 4 * T:6 * T]       # the door mat
    recolour(img, MAT, np.arange(H * T)[:, None].repeat(W * T, 1) >= (H - 1) * T)
    r = rug(c79, 6, 4); img[4 * T:8 * T, 4 * T:10 * T] = r
    paste(img, P['bookcase'], 1, 2); paste(img, P['bookcase'], 3, 2)
    paste(img, P['bureau'], 9, 2)
    paste(img, P['chest'], 11, 3)                             # (the bedside stand, at the bed's head)
    paste(img, P['bed'], 12, 3)
    paste(img, P['screen'], 11, 5); paste(img, P['screen'], 12, 5)   # (a pair of panels at the bed's foot)
    paste(img, P['armchair'], 6, 2)                           # (his chair against the panelling, under the banner)
    paste(img, P['desk'], 6, 3)                               # (the desk's top on row 4, its quill on row 3)
    paste(img, P['chairL'], 6, 5); paste(img, P['chairR'], 7, 5)
    paste(img, P['sidechair'], 1, 7); paste(img, P['teatable'], 2, 7)
    paste(img, P['bust'], 4, 9); paste(img, P['bust'], 9, 9)
    paste(img, P['candelabra'], 1, 9); paste(img, P['candelabra'], 12, 9)
    o = Image.fromarray(img.astype(np.uint8)); o.save(out)
    o.resize((W * T * 3, H * T * 3), Image.NEAREST).save(out.replace('.png', '_3x.png'))

if __name__ == '__main__':
    main(sys.argv[1])
