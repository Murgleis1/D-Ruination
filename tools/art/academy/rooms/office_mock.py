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
TABLE = os.environ.get('TABLE', 'cloth')
OBJ = os.environ.get('OBJ', 'book_pink')                      # on the cloth: flowers | book_pink | book_stack | papers
SHELF_KIND = os.environ.get('SHELF', 'archive')              # archive: Fort Elderflower's archive shelves (user)
ARCH_WOOD = None                                              # filled lazily: the archive's mauve wood -> the hall's walnut
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

def walnut(rgb):
    """MonoMyth's mauve-brown furniture wood onto the hall's walnut ramp by brightness (the book spines kept)."""
    out = rgb.copy()
    for c in {tuple(v) for v in rgb.reshape(-1, 3).tolist()}:
        r, g, b = c
        if abs(r - b) <= 40 and r >= g and r - g >= 8 and max(c) - min(c) < 70:      # the mauve/brown family
            out[(rgb == c).all(-1)] = HALL.honey(c, HALL.WALNUT)
    return out

def table_piece():
    """(rgb, mask) of the table on the carpet, by TABLE."""
    P = os.path.join(ASSETS, 'monomyth_reference', 'pieces')
    if TABLE == 'card':
        t = np.array(Image.open(os.path.join(P, 'card_table.png')).convert('RGBA')); return t[..., :3], t[..., 3] > 0
    if TABLE == 'cloth':                                         # the same table, candelabra off, a small object on it
        t = np.array(Image.open(os.path.join(P, 'candelabra_table.png')).convert('RGBA'))[12:]; rgb = t[..., :3].copy()
        m = t[..., 3] > 0; inner = np.zeros(m.shape, bool); inner[0:7, 3:23] = True
        rgb[inner & m] = (248, 248, 248)                         # the candelabra's foot -> the cloth's white
        low = np.zeros(m.shape, bool); low[17:] = True; rgb[low & (t[..., :3] == (120, 120, 128)).all(-1)] = (16, 28, 64)
        if OBJ:
            src = os.path.join(ASSETS, 'crown_reference' if OBJ == 'flowers' else 'monomyth_reference', 'pieces', OBJ + '.png')
            o = np.array(Image.open(src).convert('RGBA')); om = o[..., 3] > 0
            py, px = 9 - o.shape[0] // 2, 13 - o.shape[1] // 2; sub = rgb[py:py + o.shape[0], px:px + o.shape[1]]; sub[om] = o[..., :3][om]
        return rgb, m
    if TABLE.startswith('candelabra'):                           # the Old HQ's clothed table with its gold candelabra
        t = np.array(Image.open(os.path.join(P, 'candelabra_table.png')).convert('RGBA')); rgb = t[..., :3].copy()
        m = t[..., 3] > 0; low = np.zeros(m.shape, bool); low[29:] = True
        rgb[low & (t[..., :3] == (120, 120, 128)).all(-1)] = (16, 28, 64)          # its shadow, on the carpet's navy
        if TABLE == 'candelabra_maroon':                         # the cloth in the Academy maroon (candles, gold kept)
            body = np.zeros(m.shape, bool); body[8:] = True
            for c, w in {(248, 248, 248): (118, 36, 48), (184, 192, 200): (84, 22, 34), (224, 232, 232): (152, 62, 70)}.items():
                rgb[body & (t[..., :3] == c).all(-1)] = w
        return rgb, m
    if TABLE == 'archive_desk':                                  # the archive's writing desk: lamp, papers, inlaid top
        t = np.array(Image.open(os.path.join(P, 'arch_desk_clean.png')).convert('RGBA'))   # lamp kept, stool and gallery cut
        return walnut(t[..., :3]), t[..., 3] > 0
    if TABLE == 'hall_table':                                    # the hall's low table, in walnut (its candle and cup)
        ts = HALL.cabin_ts('A ivory plaster'); tst = HALL.cabin_ts('A ivory plaster')
        for i, w in ((3, HALL.WALNUT[3]), (11, HALL.WALNUT[4]), (14, HALL.WALNUT[5])): tst.pal[9][i] = w
        a = np.hstack([HALL.meta_layers(ts, m, ts_obj=tst, clean=False, floor=0x18B)[0] for m in (0x1B0, 0x1B1)])
        f = np.hstack([HALL.meta_layers(ts, 0x18B, clean=False)[0]] * 2); return a, (a != f).any(-1)
    cells = {'manor_table': ((0x30, 0x31), (0x38, 0x39)), 'crown': ((0x05, 0x06),), 'crown_290': ((0x290, 0x291),)}[TABLE]
    T = TSM if TABLE == 'manor_table' else TSC
    a = np.vstack([np.hstack([T.meta(m) for m in row]) for row in cells])
    f = np.vstack([np.hstack([T.meta(0x1)] * len(cells[0]))] * len(cells)); return a, (a != f).any(-1)

def compose():
    img = np.zeros((H * 16, W * 16, 3), np.uint8); solid = set()
    def put(x, y, cell): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cell
    def paste(rgb, m, px, py): sub = img[py:py + rgb.shape[0], px:px + rgb.shape[1]]; sub[m] = rgb[m]
    for x in range(1, W - 1):
        put(x, 0, TSC.meta(TRIM)); put(x, 1, TSC.meta(WALL)); put(x, 2, TSC.meta(FLOOR_SHADE))
        for y in range(3, H - 1): put(x, y, TSC.meta(FLOOR))
    for x0 in SHELVES:
        if SHELF_KIND == 'archive':
            a = np.array(Image.open(os.path.join(ASSETS, 'monomyth_reference', 'pieces', 'arch_shelf.png')).convert('RGBA'))
            rgb, m = walnut(a[..., :3]), a[..., 3] > 0; paste(rgb, m, x0 * 16, 1 * 16)
        else:
            for dy in range(2):
                for dx in range(2): put(x0 + dx, 1 + dy, TSC.meta(SHELF[dy][dx]))
        solid |= {(x0 + dx, 1 + dy) for dx in range(2) for dy in range(2)}
    cx, cy = COUCH_AT; mid = cx + 36                              # the wall pieces centred over the couch's back run
    k = koi(); paste(k, np.ones(k.shape[:2], bool), mid - k.shape[1] // 2, 7)
    for px, rec in ((mid - k.shape[1] // 2 - 18, HALL.BANNER_RECOLOUR), (mid + k.shape[1] - k.shape[1] // 2 + 2, WATER_BANNER)):
        b, bm = HALL.decor_piece('heraldic_banner.png', rec); paste(b[:28], bm[:28], px, 3)
    rug = np.array(Image.open(os.path.join(ASSETS, 'water_rug_rebuilt.png')).convert('RGBA'))
    paste(rug[..., :3], rug[..., 3] > 0, cx - 12, cy + 26)       # the carpet in the couch's corner, out past its open sides
    c, cm = couch(); paste(c, cm, cx, cy)
    t, tm = table_piece()                                        # centred in the couch's corner, on the carpet
    ty = cy + 18 if TABLE.startswith('candelabra') else cy + 30 if TABLE == 'cloth' else cy + 26 + max(0, (30 - t.shape[0]) // 2)
    paste(t, tm, cx + 32 - t.shape[1] // 2, ty)
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
