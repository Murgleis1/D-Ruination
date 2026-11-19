"""Mock of Cadmus's office (G1, off the hall's ground floor) (user design 2026-11-19).

User brief, in order: desk and bookshelves, the Academy banner and a rug, a Water-type touch; then smaller and
cosier, no fountain; the Water touch = a Water banner, the koi painting and a Water rug (the wave rug looked bad;
the user then designed a Water-Pokemon rug, rebuilt here from their screenshot: assets/water_rug_rebuilt.png);
the visitors' chairs off it; then (user) the L-shaped couch and its table from La Costa Nostra, Luciano's
restaurant in North Edelweiss (MonoMyth), set round the new carpet the way they sit in the restaurant, in place of
the desk: the couch in the Academy's maroon (its white frame in walnut), Cadmus's seat; the table either the
restaurant's card table or Crown's desk (TABLE=card|crown).

A small study in the classroom's finish (Crown's trim wall and plank floor; credit: Blah and the Crown team, used
with permission): two bookcases on the left of the back wall; on the right the couch's back run along the wall,
under the purple Academy banner, the koi painting (frame in walnut) and Cadmus's Water banner (the same Crown
banner in sea blue); its side run down the right; the carpet and the table in its corner; candle stands in front.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/academy/rooms/office_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'crown')); sys.path.insert(0, HERE)
from crown_pieces import map_layout, TS
from classroom_mock import TSC, TRIM, WALL, FLOOR, FLOOR_SHADE, SHELF, MAT, MAROON_MAT, recolour
ASSETS = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'assets'))
sys.path.insert(0, os.path.join(HERE, '..'))
import compose_mock as HALL

TSM = TS(map_layout(17, 0))                                       # the manor room's set: its candle stands
W, H = 12, 10                                                     # x0, x11 void; rows 0-1 wall, 2-8 floor, 9 the mat
TABLE = os.environ.get('TABLE', 'card')
SHELVES = [1, 3]
COUCH_AT = (W - 1) * 16 - 72, 2 * 16 + 1                          # the couch (72 x 55): its side run against the right
CANDLES = [(1, 7), (10, 7)]
WATER_BANNER = {(96, 112, 88): (28, 56, 112), (136, 152, 104): (52, 96, 168), (208, 208, 176): (200, 224, 240)}
KOI_FRAME = {(80, 80, 104): HALL.WALNUT[0], (192, 192, 208): HALL.WALNUT[6], (152, 152, 168): HALL.WALNUT[5],
             (120, 96, 104): HALL.WALNUT[2], (160, 128, 136): HALL.WALNUT[4], (136, 112, 120): HALL.WALNUT[3],
             (168, 168, 176): HALL.WALNUT[5]}
# the restaurant's red velvet in the Academy maroon, its white frame in walnut
COUCH_RECOLOUR = {(200, 120, 120): (152, 62, 70), (152, 88, 112): (116, 34, 46), (112, 88, 96): (84, 22, 34),
                  (80, 80, 104): (52, 24, 30), (248, 248, 248): HALL.WALNUT[6], (208, 208, 216): HALL.WALNUT[5],
                  (120, 120, 128): HALL.WALNUT[3]}

def koi():
    a = np.array(Image.open(os.path.join(ASSETS, 'monomyth_reference', 'koi_painting.png')).convert('RGB'))
    out = a.copy(); canvas = np.zeros(a.shape[:2], bool); canvas[5:14, 5:23] = True     # the white canvas and its fish
    for c, w in KOI_FRAME.items(): out[(a == c).all(-1) & ~canvas] = w
    return out

def couch():
    a = np.array(Image.open(os.path.join(ASSETS, 'monomyth_reference', 'pieces', 'l_couch.png')).convert('RGBA'))
    rgb, m = a[..., :3].copy(), a[..., 3] > 0
    m &= ~(rgb == (112, 160, 112)).all(-1)                        # a sliver of the restaurant's green wall
    for c, w in COUCH_RECOLOUR.items(): rgb[(a[..., :3] == c).all(-1)] = w
    return rgb, m

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
    cx, cy = COUCH_AT; mid = cx + 36                              # the wall pieces centred over the couch's back run
    k = koi(); paste(k, np.ones(k.shape[:2], bool), mid - k.shape[1] // 2, 7)
    for px, rec in ((mid - k.shape[1] // 2 - 18, HALL.BANNER_RECOLOUR), (mid + k.shape[1] - k.shape[1] // 2 + 2, WATER_BANNER)):
        b, bm = HALL.decor_piece('heraldic_banner.png', rec); paste(b[:28], bm[:28], px, 3)
    rug = np.array(Image.open(os.path.join(ASSETS, 'water_rug_rebuilt.png')).convert('RGBA'))
    paste(rug[..., :3], rug[..., 3] > 0, cx - 12, cy + 26)       # the carpet in the couch's corner, out past its open sides
    c, cm = couch(); paste(c, cm, cx, cy)
    if TABLE == 'card':
        t = np.array(Image.open(os.path.join(ASSETS, 'monomyth_reference', 'pieces', 'card_table.png')).convert('RGBA'))
        paste(t[..., :3], t[..., 3] > 0, cx + 18, cy + 27)
    else:
        for dx, m in enumerate((0x05, 0x06)):
            d = TSC.meta(m); keep = (d != TSC.meta(FLOOR)).any(-1); sub = img[cy + 30:cy + 46, cx + 14 + dx * 16:cx + 30 + dx * 16]
            sub[keep] = d[keep]
    for x, y in CANDLES:                                         # two cells: candles (0xA7) over the stand (0xAF)
        for dy, m in ((-1, 0xA7), (0, 0xAF)):
            c2 = TSM.meta(m); f = TSC.meta(FLOOR).copy(); keep = (c2 != TSM.meta(0x1)).any(-1); f[keep] = c2[keep]
            put(x, y + dy, f)
        solid.add((x, y))
    put(5, H - 1, recolour(TSC.meta(MAT[0]), MAROON_MAT)); put(6, H - 1, recolour(TSC.meta(MAT[1]), MAROON_MAT))
    return img, solid

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/rooms/office_mock.png'
    img, _ = compose(); Image.fromarray(img).resize((W * 32, H * 32), 0).save(out); print(out)
