"""Mock of Cadmus's office (G1, off the hall's ground floor) (user design 2026-11-19).

User brief: desk and bookshelves, the Academy banner and a rug, a Water-type touch; then: smaller and cosier, no
fountain ("no good logistics for a water fountain"), and for the Water touch all three of: a Water banner, the koi
painting and the blue wave rug.

A small study in the classroom's finish (Crown's trim wall and plank floor; credit: Blah and the Crown team, used
with permission): a bookcase in each back corner; centred above Cadmus's desk, MonoMyth's framed koi painting (its
grey frame in the hall's walnut) between the purple Academy banner and his own Water banner (the same Crown banner
in sea blue); before the desk MonoMyth's Watercress Port wave rug (its grey edge in the Academy's gold) with two
visitors' chairs on it; the manor room's iron candle stands in the front corners.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/academy/rooms/office_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'crown')); sys.path.insert(0, HERE)
from crown_pieces import map_layout, TS
from classroom_mock import TSC, TRIM, WALL, FLOOR, FLOOR_SHADE, SHELF, CHAIR, MAT, MAROON_MAT, recolour
ASSETS = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'assets'))
sys.path.insert(0, os.path.join(HERE, '..'))
import compose_mock as HALL

TSM = TS(map_layout(17, 0))                                       # the manor room's set: its candle stands
W, H = 12, 9                                                      # x0, x11 void; rows 0-1 wall, 2-7 floor, 8 the mat
DESK = (0x05, 0x06)
SHELVES = [1, 9]
VISITORS = [(4, 4), (7, 4)]                                       # chairs facing the desk; talk from (5,4)/(6,4)
RUG_AT = (4 * 16 + 4, 4 * 16 + 1)                                 # the wave rug (56 x 30 px) under them, centred
RUG_KIND = os.environ.get('RUG', 'ornate_blue')
# the hall's own ornate carpet (the cabin's rug, cleaned) in Water colours: deep sea blues, cream, gold trim
BLUE9 = {5: (28, 48, 104), 6: (40, 68, 136), 8: (64, 104, 176), 12: (226, 222, 204), 7: (186, 150, 100)}
CROWN_BLUE = {(216, 112, 104): (40, 68, 136), (200, 88, 80): (28, 48, 104), (160, 64, 104): (20, 36, 84),
              (104, 56, 88): (16, 28, 64), (208, 216, 104): (186, 150, 100), (192, 160, 56): (186, 150, 100)}
RUG_SET = {'tl': 0x40, 't': 0x326, 'tr': 0x41, 'l': 0x85, 'm': 0xDC, 'r': 0x86, 'bl': 0x48, 'b': 0x8D, 'br': 0x49}
CANDLES = [(1, 6), (10, 6)]
WATER_BANNER = {(96, 112, 88): (28, 56, 112), (136, 152, 104): (52, 96, 168), (208, 208, 176): (200, 224, 240)}
GOLD = (186, 150, 100)
KOI_FRAME = {(80, 80, 104): HALL.WALNUT[0], (192, 192, 208): HALL.WALNUT[6], (152, 152, 168): HALL.WALNUT[5],
             (120, 96, 104): HALL.WALNUT[2], (160, 128, 136): HALL.WALNUT[4], (136, 112, 120): HALL.WALNUT[3],
             (168, 168, 176): HALL.WALNUT[5]}

def koi():
    a = np.array(Image.open(os.path.join(ASSETS, 'monomyth_reference', 'koi_painting.png')).convert('RGB'))
    out = a.copy(); canvas = np.zeros(a.shape[:2], bool); canvas[5:14, 5:23] = True     # the white canvas and its fish
    for c, w in KOI_FRAME.items(): out[(a == c).all(-1) & ~canvas] = w
    return out

def compose():
    img = np.zeros((H * 16, W * 16, 3), np.uint8); solid = set()
    def put(x, y, cell): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cell
    def paste(rgb, m, px, py): sub = img[py:py + rgb.shape[0], px:px + rgb.shape[1]]; sub[m] = rgb[m]
    for x in range(1, W - 1):
        put(x, 0, TSC.meta(TRIM)); put(x, 1, TSC.meta(WALL)); put(x, 2, TSC.meta(FLOOR_SHADE))
        for y in range(3, H - 1): put(x, y, TSC.meta(FLOOR))
    for x0 in SHELVES:
        for dy in range(2):
            for dx in range(2): put(x0 + dx, 1 + dy, TSC.meta(SHELF[dy][dx])); solid.add((x0 + dx, 1 + dy))
    k = koi(); paste(k, np.ones(k.shape[:2], bool), 6 * 16 - k.shape[1] // 2, 7)
    for px, rec in ((4 * 16, HALL.BANNER_RECOLOUR), (7 * 16, WATER_BANNER)):     # Academy left, Water right
        b, bm = HALL.decor_piece('heraldic_banner.png', rec); paste(b[:28], bm[:28], px, 3)
    if RUG_KIND == 'wave':
        rug = np.array(Image.open(os.path.join(ASSETS, 'monomyth_reference', 'wave_rug.png')).convert('RGBA'))
        rgb, rm = rug[..., :3].copy(), rug[..., 3] > 0; rgb[(rgb == (120, 120, 120)).all(-1) & rm] = GOLD
        paste(rgb, rm, *RUG_AT)
    elif RUG_KIND.startswith('ornate'):                          # the hall's carpet design
        saved = dict(HALL.MAROON9)
        if RUG_KIND == 'ornate_blue': HALL.MAROON9.clear(); HALL.MAROON9.update(BLUE9)
        rgb, rm = HALL.rug_rgb(HALL.cabin_ts('A ivory plaster'), 'centre'); HALL.MAROON9.clear(); HALL.MAROON9.update(saved)
        ys, xs = np.where(rm); rgb, rm = rgb[ys.min():ys.max() + 1, xs.min():xs.max() + 1], rm[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
        paste(rgb, rm, 6 * 16 - rgb.shape[1] // 2, 4 * 16 + 16 - rgb.shape[0] // 2)
    else:                                                        # Crown's rug set, 4 x 2, in sea blue
        for y in (4, 5):
            for x in range(4, 8):
                v = 't' if y == 4 else 'b'; h = 'l' if x == 4 else 'r' if x == 7 else ''
                put(x, y, recolour(TSM.meta(RUG_SET[v + h]), CROWN_BLUE))
    for x, y in VISITORS:
        chair = TSC.meta(CHAIR); keep = (chair != TSC.meta(FLOOR)).any(-1)
        img[y * 16:y * 16 + 16, x * 16:x * 16 + 16][keep] = chair[keep]; solid.add((x, y))
    put(5, 3, TSC.meta(DESK[0])); put(6, 3, TSC.meta(DESK[1])); solid |= {(5, 3), (6, 3)}
    for x, y in CANDLES:                                         # two cells: candles (0xA7) over the stand (0xAF)
        for dy, m in ((-1, 0xA7), (0, 0xAF)):
            c = TSM.meta(m); f = TSC.meta(FLOOR).copy(); keep = (c != TSM.meta(0x1)).any(-1); f[keep] = c[keep]
            put(x, y + dy, f)
        solid.add((x, y))
    put(5, H - 1, recolour(TSC.meta(MAT[0]), MAROON_MAT)); put(6, H - 1, recolour(TSC.meta(MAT[1]), MAROON_MAT))
    return img, solid

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/rooms/office_mock.png'
    img, _ = compose(); Image.fromarray(img).resize((W * 32, H * 32), 0).save(out); print(out)
