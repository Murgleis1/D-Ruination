"""(user design 2026-11-19) Mock of the Pelluca Academy main hall: MonoMyth's Ironbark Cabin reskinned from "really
old and worn down" to "aged yet regal" (user).

  * walls cleaned: moss and damp stains become plain plaster; the plaster lightened (two colour options)
  * all wood lightened (floors, galleries, railings, doors, furniture)
  * carpets redrawn straight-edged in regal purple and white
  * boarded / broken windows -> the cabin's intact window; dark broken doors -> its wood door, except the haunted
    teachers' lounge (T4), which keeps its old dark door
  * real stairs (user): ground -> middle between the hearth and the office door (where the stuffed Ursaring sat,
    which goes), middle -> top in place of door M2; the saloon staircase from the dormitory, its banisters lifted
    onto the hall's own railing and wall; walkable up the centre column. T2 removed (the top landing).
  * the cabin's side-wall exit rugs removed (the Academy has one front door)
Rooms: G1 Cadmus's office, M3 classroom (top of the first stairs), M1 library, M4 / T1 / T3 locked (remodelling),
T4 haunted lounge (rusted key after the second badge). Image-level mock only.
"""
import os, sys, colorsys
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, '/home/claude/repo/tools/monomyth')
from romlib import u32, off, layout
from render import TS, map_cells
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location('dorm_cm', '/home/claude/repo/tools/monomyth/dormitory/compose_mock.py')
DORM = _ilu.module_from_spec(_spec); _spec.loader.exec_module(DORM)

CABIN = layout(u32(off(0x0886B35C))); CW = CABIN['w']; CELLS = map_cells(CABIN)
X0, X1, Y0, Y1 = 6, 23, 4, 27                      # the hall in the cabin map

# ---- colour ----
# The cabin's wall is palette 7: index 15 the plaster, 14 a darker teal that forms the stains and the blotchy band
# under the ceiling, 10 the moss, 6/7 dark outlines, 8 the grey baseboard. Its wood is the browns/olives of
# palettes 7-11. Walls are cleaned per tile (WALL_META: stains and moss -> plaster; the darker shade kept only as
# a straight band under the cornice); wood goes onto one honey-oak ramp by brightness, outlines staying dark.
def hls(c): return colorsys.rgb_to_hls(*(v / 255 for v in c))
def rgb(h, l, s): return tuple(int(round(v * 255)) for v in colorsys.hls_to_rgb(h, l, s))
WALLS = {'A ivory plaster': ((236, 226, 202), (206, 194, 168))}       # user picked A (B pale stone dropped)
HONEY = [(78, 50, 34), (106, 70, 44), (136, 96, 58), (164, 122, 76), (190, 148, 98), (210, 172, 120), (226, 196, 146)]
MAROON = [(84, 22, 34), (116, 34, 46), (152, 62, 70)]          # palette 8's upholstery greens 9, 10, 12 -> maroon
WALNUT = [(34, 18, 16), (52, 26, 22), (72, 36, 28), (94, 48, 34), (118, 64, 42), (142, 84, 54), (168, 108, 72)]   # the piano: dark, elegant
def is_wood(c):
    r, g, b = c; return c not in ((0, 248, 248), (0, 0, 0)) and r >= b and (r - b) >= 12 and not (g > r + 8)
def honey(c, ramp=None):
    ramp = ramp or HONEY; l = hls(c)[1]; t = min(1.0, max(0.0, (l - 0.14) / 0.42)); return ramp[int(round(t * (len(ramp) - 1)))]
def wood_pal(pal, ramp=None): return [honey(tuple(c), ramp) if is_wood(tuple(c)) else tuple(c) for c in pal]
def cabin_ts(wall):
    ts = TS(CABIN); ts.cache = {}
    for p in (7, 8, 10, 11): ts.pal[p] = wood_pal(ts.pal[p])          # not 9: the carpets keep their own colours
    plaster, shade = WALLS[wall]
    ts.pal[7][15], ts.pal[7][14], ts.pal[7][10] = plaster, shade, plaster
    ts.pal[7][6] = ts.pal[7][7] = (84, 62, 52); ts.pal[7][8] = (150, 120, 96)          # outlines, baseboard: warm
    ts.pal[8][9], ts.pal[8][10], ts.pal[8][12] = MAROON                             # the upholstery (user: maroon)
    return ts
WALL_META = {0x170, 0x178, 0x179, 0x17A, 0x17B, 0x180, 0x182, 0x183, 0x1C7, 0x1CF, 0x1C8, 0x1C9}
WALL_ROWS = {6, 7, 8, 12, 13, 17, 18}                    # every tile in the wall rows carries plaster (windows, chimney, doors)
import struct as _st
from render import ROM as _ROM
def meta_layers(ts, m, top=False, ts_obj=None, clean=True, floor=None):
    """(under, over, over mask) of a cabin metatile: under = its bottom and middle layers (below the player),
    over = its top layer (drawn over the player). With `clean`, a wall metatile has its stains and moss painted
    out: in palette 7, 14 and 10 -> 15, except a straight 3-pixel band at the top of the pieces under the ceiling.
    With `floor` (a metatile id), furniture moved elsewhere: its own bottom layer (the floor it stood on) is replaced
    by that floor's, so the boards run on unbroken under it."""
    if floor is not None:
        img = meta_layers(ts, floor, clean=False)[0]; _, over, om = meta_layers(ts, m, top, ts_obj, clean)
        e = _st.unpack_from('<12H', _ROM, (off(CABIN['primary']['mt']) + 24 * m) if m < 512 else off(CABIN['secondary']['mt']) + 24 * (m - 512))
        for q in range(4):
            v = e[4 + q]; T = ts_obj if ts_obj is not None else ts; t = T.tile(v & 0x3FF)
            if t is None or not v & 0x3FF: continue
            if v & 0x400: t = t[:, ::-1]
            if v & 0x800: t = t[::-1, :]
            y, x = (q // 2) * 8, (q % 2) * 8; mk = t != 0
            img[y:y + 8, x:x + 8][mk] = np.array(T.pal[v >> 12], np.uint8)[t][mk]
        return img, over, om
    base = off(CABIN['primary']['mt']) + 24 * m if m < 512 else off(CABIN['secondary']['mt']) + 24 * (m - 512)
    e = _st.unpack_from('<12H', _ROM, base); img = np.zeros((16, 16, 3), np.uint8)
    over = np.zeros((16, 16, 3), np.uint8); om = np.zeros((16, 16), bool)
    for layer in range(3):
        for q in range(4):
            v = e[layer * 4 + q]; T = ts_obj if (ts_obj is not None and layer > 0) else ts
            t = T.tile(v & 0x3FF)
            if t is None: continue
            t = t.copy()
            if v & 0x400: t = t[:, ::-1]
            if v & 0x800: t = t[::-1, :]
            y, x = (q // 2) * 8, (q % 2) * 8
            if v >> 12 == 7 and clean and T is ts:
                band = np.zeros((8, 8), bool)
                if top and q < 2: band[:3] = True
                t = np.where(np.isin(t, (10, 14)) & ~band, 15, t); t = np.where(band & (t != 0), 14, t)
            pal = np.array(T.pal[v >> 12], np.uint8)
            if layer == 0: img[y:y + 8, x:x + 8] = pal[t]
            elif layer == 1: mk = t != 0; img[y:y + 8, x:x + 8][mk] = pal[t][mk]
            else: mk = t != 0; over[y:y + 8, x:x + 8][mk] = pal[t][mk]; om[y:y + 8, x:x + 8] |= mk
    return img, over, om
def meta_clean(ts, m, top=False, ts_obj=None, clean=True):
    """The metatile as it looks (all three layers)."""
    img, over, om = meta_layers(ts, m, top, ts_obj, clean); img = img.copy(); img[om] = over[om]; return img

# ---- the edits, in cabin map coordinates ----
WOOD_DOOR = (0x1CF, 0x1D7)                               # top, bottom
INTACT_WINDOW = [(0x1E6, 0x1E7), (0x1EE, 0x1EF), (0x1F5, 0x1F7)]
EDITS = {}
for x0 in (12, 18):                                      # boarded (12-13) and broken (18-19) windows -> intact
    for dy, (a, b) in enumerate(INTACT_WINDOW): EDITS[(x0, 6 + dy)] = a; EDITS[(x0 + 1, 6 + dy)] = b
for (x, ytop) in ((8, 7), (8, 12), (20, 12), (20, 17)):  # T1, M1, M4, G1: dark broken doors -> wood doors
    EDITS[(x, ytop)], EDITS[(x, ytop + 1)] = WOOD_DOOR
# the top floor (user 2026-11-19): the haunted lounge (T4) stands alone at the right end; the other door there (T3)
# goes left of the chimney, between the two windows (the old T2 place, at the top of the second stairs)
EDITS[(17, 7)], EDITS[(17, 8)] = 0x17B, 0x183            # T3's old place: plain wall
EDITS[(16, 18)], EDITS[(16, 19)] = 0x182, 0x188          # the stuffed Ursaring removed
EDITS[(13, 17)] = 0x17A                                  # the ground-floor clock removed (user): a banner instead
EDITS[(15, 12)] = 0x17B                                  # the little middle-gallery clock: Crown's pendulum clock instead
for ytop in (7, 12, 17):                                 # the left wall edge's grime specks (0x170/0x180) -> plain plaster
    EDITS[(7, ytop)], EDITS[(7, ytop + 1)] = 0x17A, 0x183
for p, m in {(6, 21): 0, (6, 22): 0, (7, 21): 0x18B, (7, 22): 0x18B, (21, 20): 0x18B, (21, 21): 0x18B,
             (22, 20): 0, (22, 21): 0, (21, 9): 0x188, (21, 10): 0x1BA, (22, 9): 0, (22, 10): 0}.items():
    EDITS[p] = m                                         # side-wall exit rugs removed
# the sitting group (sofa, armchair, low table, stools) on the left, the sofa facing the table (user 2026-11-19:
# the reception desk takes the right side; then one tile further left, clear of the entrance lamp)
SOFA = {(19, 22): (8, 22), (20, 22): (9, 22), (21, 22): (10, 22), (19, 23): (8, 23), (20, 23): (9, 23), (21, 23): (10, 23),
        (8, 24): (7, 24), (9, 24): (8, 24), (10, 24): (9, 24), (11, 24): (10, 24)}       # source cell -> new cell
MOVED = {}                                               # new cell -> furniture metatile (drawn on its new floor)
for (sx, sy), (dx, dy) in SOFA.items(): MOVED[(dx, dy)] = CELLS[sy * CW + sx] & 0x3FF
for (sx, sy) in SOFA:
    if (sx, sy) not in MOVED: EDITS[(sx, sy)] = 0x18B
SITTING = set(MOVED)                                     # all solid
DESK = (18, 21)                                          # the reception desk's top-left cell (4 x 4)
for x in range(DESK[0], DESK[0] + 4):
    for y in range(DESK[1], DESK[1] + 4): EDITS[(x, y)] = 0x18B
# the notice board stands on the ground floor (user 2026-11-19: it looked cramped between the gallery doors);
# the top gallery is kept clean (user: the crates and the step ladder read as broken junk; the doors closed for
# renovation tell the story)
BOARD = (7, 18)                                          # top-left cell of the standing board (2 x 2): it stands on
EDITS[(8, 18)], EDITS[(8, 19)] = 0x183, 0x188            # the floor by the wall, left of the piano, in the floor lamp's place
RUG_CELLS = {(x, y) for x in (13, 14, 15) for y in (21, 22)}
MAT_CELLS = {(x, 25) for x in (13, 14, 15)} | {(x, 26) for x in (13, 14, 15)}
FLIGHTS = [(16, 15), (10, 10)]                           # (left column, top row): 3 wide x 4 tall, top row = gallery edge

# ---- the saloon staircase, recoloured to the new wood ----
# Each saloon stair-side tile draws the saloon wall on its bottom layer and the banister alone on its middle
# layer (tile 496 = empty filler), so the banisters are taken from the middle layer: an exact cut-out. Four rows:
# the top row stands in the upper gallery's edge row and replaces the railing there (an opening in it, the newel
# posts capping the railing's ends); then down through the railing and the back wall to the posts at the floor.
STAIR_ROWS = [(192, 193, 194), (227, 185, 228), (200, 201, 202), (208, 209, 210)]
def stair_pieces(wall):
    pal = [wood_pal(p) for p in DORM.SAL.pal]
    L = [h for h in DORM.H if h['addr'] + 0x08000000 == 0x886A39C][0]['layout']
    rows = []
    for r in STAIR_ROWS:
        row = []
        for k, m in enumerate(r):
            base = off(L['primary']['mt']) + 24 * m if m < 512 else off(L['secondary']['mt']) + 24 * (m - 512)
            e = _st.unpack_from('<12H', _ROM, base); img = np.zeros((16, 16, 3), np.uint8); mask = np.zeros((16, 16), bool)
            layers = (0, 1) if k == 1 else (1,)            # the steps: base fill + treads; the sides: banister only
            for layer in layers:
                for q in range(4):
                    v = e[layer * 4 + q]; tid = v & 0x3FF
                    if k != 1 and tid == 496: continue
                    t = DORM.SAL.tile(tid)
                    if t is None: continue
                    if v & 0x400: t = t[:, ::-1]
                    if v & 0x800: t = t[::-1, :]
                    y, x = (q // 2) * 8, (q % 2) * 8; P = np.array(pal[v >> 12], np.uint8)
                    nz = t != 0 if not (k == 1 and layer == 0) else np.ones((8, 8), bool)
                    img[y:y + 8, x:x + 8][nz] = P[t][nz]; mask[y:y + 8, x:x + 8] |= nz
            row.append((img, mask))
        rows.append(row)
    return rows
# under the side columns: the gallery floor without its handrail (top row), then plain plaster
SIDE_BG = [0x188, None, 0x17A, 0x183]                   # None: keep the railing row as it is

# ---- the cabin's own carpets, cleaned up (user: the drawn ones were too clean and lifeless) ----
# Its ornate pattern kept; the worn parts fixed: each rug squared to a true rectangle (the borders stepped out of
# line halfway across), its top and bottom edges redrawn straight in its own outline colour, the grime notches in
# the corners filled with its base colour. Colours: palette 9's reds -> regal purple and white, or the original red.
RUGS = {'centre': ((0x1A0, 0x1A1, 0x1A2), (0x1A8, 0x1A9, 0x1AA)), 'mat': ((0x19E, 0x19F, 0x1AF), (0x1A6, 0x1A7, 0x1B7))}
PURPLE9 = {5: (88, 50, 124), 6: (104, 62, 144), 8: (136, 96, 176), 12: (236, 230, 244), 7: (176, 156, 208)}
MAROON9 = {5: (96, 26, 40), 6: (118, 36, 48), 8: (148, 58, 64), 12: (230, 210, 182), 7: (186, 150, 100)}   # user: maroon-ish; cream, gold trim
CARPET = os.environ.get('CARPET', 'maroon')
def rug_index(ts, grid):
    """The rug's own pixels (palette 9 layer) as indices, 0 elsewhere, over its cells."""
    H, W = len(grid) * 16, len(grid[0]) * 16; idx = np.zeros((H, W), np.uint8)
    for r, row in enumerate(grid):
        for c, m in enumerate(row):
            base = off(CABIN['primary']['mt']) + 24 * m if m < 512 else off(CABIN['secondary']['mt']) + 24 * (m - 512)
            e = _st.unpack_from('<12H', _ROM, base)
            for k, v in enumerate(e):
                if v >> 12 != 9 or not v & 0x3FF: continue
                t = ts.tile(v & 0x3FF)
                if t is None: continue
                if v & 0x400: t = t[:, ::-1]
                if v & 0x800: t = t[::-1, :]
                q = k % 4; y, x = r * 16 + (q // 2) * 8, c * 16 + (q % 2) * 8
                sub = idx[y:y + 8, x:x + 8]; sub[t != 0] = t[t != 0]
    return idx
def clean_rug(idx):
    """Mirror the rug's clean right half onto its worn left half (the pattern is left-right symmetric; the
    stepped border and the grime notches are on the left), about the rug's own centre."""
    m = idx > 0; rc = m.mean(1); rows = np.where(rc > 0.6 * rc.max())[0]
    cc = m[rows.min():rows.max() + 1].mean(0); cols = np.where(cc > 0.3)[0]
    x0, x1 = cols.min(), cols.max(); w = x1 - x0 + 1; half = w // 2
    out = idx.copy(); right = idx[:, x1 - half + 1:x1 + 1]
    out[:, x0:x0 + half] = right[:, ::-1]
    return out
def rug_rgb(ts, name):
    idx = clean_rug(rug_index(ts, RUGS[name])); pal = list(ts.pal[9])
    for i, c in {'purple': PURPLE9, 'maroon': MAROON9}.get(CARPET, {}).items(): pal[i] = c
    P = np.array(pal, np.uint8); return P[idx], idx > 0

# ---- the windows and the piano bench, cleaned (user 2026-11-19) ----
# The windows kept their frames but had dark, smudged, cracked glass; each is re-glazed inside its own outline:
# pale blue glass lighter at the top, a highlight streak, a honey-oak cross mullion. The piano bench (cabin
# metatiles 0x20B/0x20C) is redrawn sound: honey-oak frame and legs, a purple velvet cushion (the carpets').
WINDOW_PAIRS = [(9, 10), (12, 13), (15, 16), (18, 19)]       # each window straddles two cells, rows 6-8
OUTLINE, FRAME, FRAME_D = (84, 62, 52), HONEY[4], HONEY[2]
B_FRAME, B_FRAME_D, B_OUTLINE = WALNUT[4], WALNUT[2], WALNUT[0]   # the bench matches the piano
GLASS = [(206, 224, 236), (186, 208, 226), (166, 192, 214)]
def clean_window(img, plain):
    """Inside a window's bounding box (where the cells differ from plain wall rendered in the same place): an
    outline ring, the frame, clean glass, a cross mullion."""
    m = np.abs(img.astype(int) - plain.astype(int)).sum(-1) > 30
    ys, xs = np.where(m)
    if len(ys) == 0: return
    y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
    w, h = x1 - x0 + 1, y1 - y0 + 1; out = img
    out[y0:y1 + 1, x0:x1 + 1] = OUTLINE                         # outline ring (redrawn square)
    out[y0 + 1:y1, x0 + 1:x1] = FRAME                           # frame
    gy0, gy1, gx0, gx1 = y0 + 2, y1 - 2, x0 + 2, x1 - 2         # glass area
    for yy in range(gy0, gy1 + 1):
        t = (yy - gy0) / max(1, gy1 - gy0); out[yy, gx0:gx1 + 1] = GLASS[min(2, int(t * 3))]
    mx = (gx0 + gx1) // 2; my = gy0 + int((gy1 - gy0) * 0.45)
    out[gy0:gy1 + 1, mx] = FRAME; out[my, gx0:gx1 + 1] = FRAME  # cross mullion
    for k in range(3):                                          # highlight streak, top-left pane
        yy, xx = gy0 + 1 + k, gx0 + 2 - k
        if gx0 <= xx < mx and yy < my: out[yy, xx] = (236, 244, 248)
    out[y1, x0:x1 + 1] = OUTLINE; out[y1 - 1, x0 + 1:x1] = FRAME_D   # sill shadow
VELVET = [(84, 22, 34), (116, 34, 46), (152, 62, 70)]          # maroon, as the upholstery and the carpets
def bench(w=16, h=11):
    a = np.zeros((h, w, 3), np.uint8); m = np.zeros((h, w), bool)
    a[0:6, 0:w] = B_OUTLINE; m[0:6, 0:w] = True
    a[1:3, 1:w - 1] = VELVET[2]; a[3:5, 1:w - 1] = VELVET[1]; a[1, 2:w - 2] = (184, 96, 100)   # cushion
    a[5, 1:w - 1] = B_FRAME_D
    for x in (1, w - 3):                                        # legs
        a[6:h, x:x + 2] = B_FRAME; a[6:h, x - 1] = B_OUTLINE; a[6:h, x + 2] = B_OUTLINE; m[6:h, x - 1:x + 3] = True
    a[h - 1, :] = a[h - 1, :]
    return a, m

PIANO = {0x1FA, 0x1FB, 0x1FC, 0x202, 0x203, 0x204}
TABLE = {0x1B0, 0x1B1}
# the hearth and the chimney column rising through the centre (user: a darker, deeper grey-blue stone): palette 10
# on these tiles only (the railings borrow a few of its greys), onto a deep slate ramp by brightness
STONE = {0x1BF, 0x1BB, 0x194, 0x1BD, 0x1BE, 0x1C5, 0x1C6, 0x1C3, 0x19B, 0x19C, 0x19D, 0x1A3, 0x1A4, 0x1A5}
SLATE = [(26, 30, 44), (38, 46, 64), (52, 62, 84), (68, 80, 104), (86, 98, 124), (106, 118, 146), (132, 144, 170)]
def slate(pal): return [c if tuple(c) in ((0, 248, 248), (0, 0, 0), (248, 0, 0)) else SLATE[min(6, int(hls(tuple(c))[1] / 0.75 * 7))] for c in pal]
# ---- wall decor from Pokemon Crown (user 2026-11-19; credit Blah and the Crown team): cut-outs in
# assets/crown_reference/pieces/ ----
PIECES = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'assets', 'crown_reference', 'pieces')
BANNER_RECOLOUR = {(96, 112, 88): (88, 50, 124), (136, 152, 104): (128, 88, 168), (208, 208, 176): (236, 230, 244)}
CLOCK_RECOLOUR = {(128, 80, 56): (94, 48, 34), (160, 120, 72): (142, 84, 54), (72, 56, 56): (52, 26, 22)}
def narrow(rgb, m, cols):
    """Drop whole pixel columns (the notice board is 38 px wide; its gap on the gallery wall is 32)."""
    keep = [x for x in range(m.shape[1]) if x not in cols]; return rgb[:, keep], m[:, keep]
# the standing notice board: Crown's park signboard on two posts (its weathered grey wood warmed to walnut), its
# carved panel replaced by the notice board's cork with two of its pinned papers; the ground shadow made floor-dark
SIGN_RECOLOUR = {(104, 80, 72): WALNUT[4], (152, 144, 120): WALNUT[6], (120, 120, 128): HONEY[1]}
CORK, CORK_EDGE = (112, 104, 88), (72, 72, 80)
def standing_board():
    a, m = decor_piece('park_sign.png', SIGN_RECOLOUR)
    a[10:21, 6:26] = CORK; a[10, 6:26] = CORK_EDGE; m[10:21, 6:26] = True       # the cork face
    nb, nm = decor_piece('notice_board.png', {})
    for (sx, sy, dx, dy) in ((18, 5, 8, 11), (32, 4, 17, 11)):             # two papers (with their shadows)
        w, h = 6, 9; pa, pm = nb[sy:sy + h, sx:sx + w], nm[sy:sy + h, sx:sx + w]
        keep = pm & ~(pa == CORK).all(-1); sub = a[dy:dy + h, dx:dx + w]; sub[keep] = pa[keep]
    return a, m
def decor_piece(name, recolour):
    a = np.array(Image.open(os.path.join(PIECES, name)).convert('RGBA')); rgb = a[..., :3].copy(); m = a[..., 3] > 0
    for old, new in recolour.items(): rgb[(a[..., :3] == old).all(-1) & m] = new
    return rgb, m

def compose(wall):
    under, over, om = compose_layers(wall); img = under.copy(); img[om] = over[om]; return img
def compose_layers(wall):
    """The hall as (under, over, over mask): `under` is everything below the player (the cabin's bottom and
    middle layers and all the new pieces), `over` the cabin's top layer (railing tops, lamp shades, the sofa's
    back, the hearth glow), cleared where the staircases replaced the railing."""
    ts = cabin_ts(wall); W, H = X1 - X0, Y1 - Y0
    tsp = cabin_ts(wall)
    for p in (7, 8, 10, 11): tsp.pal[p] = wood_pal(TS(CABIN).pal[p], WALNUT)
    tsp.cache = {}
    tss = cabin_ts(wall); tss.pal[10] = slate(TS(CABIN).pal[10]); tss.cache = {}
    tst = cabin_ts(wall)                                     # the low table: its grey slab in walnut, as the piano
    for i, w in ((3, WALNUT[3]), (11, WALNUT[4]), (14, WALNUT[5])): tst.pal[9][i] = w
    img = np.zeros((H * 16, W * 16, 3), np.uint8); OV = np.zeros_like(img); OM = np.zeros((H * 16, W * 16), bool)
    for y in range(Y0, Y1):
        for x in range(X0, X1):
            m = EDITS.get((x, y), CELLS[y * CW + x] & 0x3FF)
            if (x, y) in MOVED:                          # moved furniture on the floor of its new place
                fl = m if m in (0x188, 0x18B) else 0x18B; m = MOVED[(x, y)]
                sl = (slice((y - Y0) * 16, (y - Y0 + 1) * 16), slice((x - X0) * 16, (x - X0 + 1) * 16))
                img[sl], OV[sl], OM[sl] = meta_layers(ts, m, ts_obj=tst if m in TABLE else None, clean=False, floor=fl)
                continue
            if (x, y) in RUG_CELLS: m = 0x18B
            if (x, y) in MAT_CELLS: m = 0x18B if y == 25 else 0
            if m in PIANO: cell = meta_layers(ts, m, top=False, ts_obj=tsp, clean=y in WALL_ROWS)   # piano layer in walnut
            elif m in TABLE: cell = meta_layers(ts, m, ts_obj=tst, clean=False)
            elif m in STONE: cell = meta_layers(tss, m, top=(y == 6), clean=y in WALL_ROWS)
            else: cell = meta_layers(ts, m, top=(y == 6), clean=y in WALL_ROWS)
            sl = (slice((y - Y0) * 16, (y - Y0 + 1) * 16), slice((x - X0) * 16, (x - X0 + 1) * 16))
            img[sl], OV[sl], OM[sl] = cell
    # T4, the haunted lounge: its old dark door in the old dingy colours
    old = TS(CABIN)
    for (x, y), mm in zip(((20, 7), (20, 8)), WOOD_DOOR):    # a sound door, but old and dark (the cabin's dingy wood)
        sl = (slice((y - Y0) * 16, (y - Y0 + 1) * 16), slice((x - X0) * 16, (x - X0 + 1) * 16))
        img[sl], OV[sl], OM[sl] = meta_layers(old, mm, clean=False)
        wall = meta_layers(ts, 0x17B if y == 7 else 0x183, clean=True)[0]   # its frame sits on clean plaster
        door = img[sl]; bg = (meta_layers(old, 0x17B if y == 7 else 0x183, clean=False)[0] == door).all(-1)
        door[bg] = wall[bg]
    def put(a, px, py, m=None):
        h, w = a.shape[:2]; sub = img[py:py + h, px:px + w]
        if m is None: sub[:] = a
        else: sub[m] = a[m]
    plain = np.vstack([np.hstack([meta_clean(ts, m, top=(r == 0)) for m in row]) for r, row in enumerate(((0x179, 0x179), (0x17B, 0x17B), (0x183, 0x183)))])
    for xa, xb in WINDOW_PAIRS:
        sub = img[(6 - Y0) * 16:(9 - Y0) * 16, (xa - X0) * 16:(xb + 1 - X0) * 16]; clean_window(sub, plain)
    # the piano bench: floor under it, then the clean bench centred on the old one
    for x in (9, 10): img[(20 - Y0) * 16:(21 - Y0) * 16, (x - X0) * 16:(x + 1 - X0) * 16] = meta_layers(ts, 0x18B, clean=False)[0]
    b, bm = bench(); put(b, (9 - X0) * 16 + 8, (20 - Y0) * 16 + 2, bm)
    b, bm = decor_piece('heraldic_banner.png', BANNER_RECOLOUR); put(b, (11 - X0) * 16 + 8, (17 - Y0) * 16, bm)
    c, cm = decor_piece('wall_clock.png', CLOCK_RECOLOUR); put(c, (15 - X0) * 16, (12 - Y0) * 16, cm)
    a, m = decor_piece('reception_counter.png', {}); put(a, (DESK[0] - X0) * 16, (DESK[1] - Y0) * 16, m)
    a, m = standing_board(); put(a, (BOARD[0] - X0) * 16, (BOARD[1] - Y0) * 16, m)
    a, m = rug_rgb(ts, 'centre'); put(a, (13 - X0) * 16, (21 - Y0) * 16, m)
    a, m = rug_rgb(ts, 'mat'); put(a, (13 - X0) * 16, (25 - Y0) * 16, m)
    for fx, fy in FLIGHTS:
        for dy, row in enumerate(stair_pieces(wall)):
            for dx, (piece, mask) in enumerate(row):
                px, py = (fx + dx - X0) * 16, (fy + dy - Y0) * 16
                if dx != 1 and SIDE_BG[dy] is not None:
                    y = fy + dy; img[py:py + 16, px:px + 16] = meta_layers(ts, SIDE_BG[dy], clean=y in WALL_ROWS)[0]
                OM[py:py + 16, px:px + 16] = False
                put(piece, px, py, mask)
    return img, OV, OM

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/academy_mock'
    ims = [(k, compose(k)) for k in WALLS]
    S = Image.new('RGB', (sum(i.shape[1] for _, i in ims) + 12 * len(ims), ims[0][1].shape[0] + 14), (28, 28, 28)); d = ImageDraw.Draw(S); x = 0
    for k, i in ims:
        S.paste(Image.fromarray(i), (x, 14)); d.text((x + 2, 2), k, fill=(255, 230, 120)); x += i.shape[1] + 12
    S.resize((S.width * 2, S.height * 2), 0).save(out + '.png'); print(out + '.png')
