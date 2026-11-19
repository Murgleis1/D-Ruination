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
    return ts
WALL_META = {0x170, 0x178, 0x179, 0x17A, 0x17B, 0x180, 0x182, 0x183, 0x1C7, 0x1CF, 0x1C8, 0x1C9}
WALL_ROWS = {6, 7, 8, 12, 13, 17, 18}                    # every tile in the wall rows carries plaster (windows, chimney, doors)
import struct as _st
from render import ROM as _ROM
def meta_clean(ts, m, top=False, ts_obj=None, clean=True):
    """A wall metatile with its stains and moss painted out: in palette 7, 14 and 10 -> 15, except a straight
    3-pixel band at the top of the pieces under the ceiling."""
    base = off(CABIN['primary']['mt']) + 24 * m if m < 512 else off(CABIN['secondary']['mt']) + 24 * (m - 512)
    e = _st.unpack_from('<12H', _ROM, base); img = np.zeros((16, 16, 3), np.uint8)
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
            else: mk = t != 0; img[y:y + 8, x:x + 8][mk] = pal[t][mk]
    return img

# ---- the edits, in cabin map coordinates ----
WOOD_DOOR = (0x1CF, 0x1D7)                               # top, bottom
INTACT_WINDOW = [(0x1E6, 0x1E7), (0x1EE, 0x1EF), (0x1F5, 0x1F7)]
EDITS = {}
for x0 in (12, 18):                                      # boarded (12-13) and broken (18-19) windows -> intact
    for dy, (a, b) in enumerate(INTACT_WINDOW): EDITS[(x0, 6 + dy)] = a; EDITS[(x0 + 1, 6 + dy)] = b
for (x, ytop) in ((8, 7), (8, 12), (20, 12), (20, 17)):  # T1, M1, M4, G1: dark broken doors -> wood doors
    EDITS[(x, ytop)], EDITS[(x, ytop + 1)] = WOOD_DOOR
EDITS[(11, 7)], EDITS[(11, 8)] = 0x17B, 0x183            # T2 removed (the top landing)
EDITS[(16, 18)], EDITS[(16, 19)] = 0x182, 0x188          # the stuffed Ursaring removed
for p, m in {(6, 21): 0, (6, 22): 0, (7, 21): 0x18B, (7, 22): 0x18B, (21, 20): 0x18B, (21, 21): 0x18B,
             (22, 20): 0, (22, 21): 0, (21, 9): 0x188, (21, 10): 0x1BA, (22, 9): 0, (22, 10): 0}.items():
    EDITS[p] = m                                         # side-wall exit rugs removed
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
CARPET = os.environ.get('CARPET', 'purple')
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
    if CARPET == 'purple':
        for i, c in PURPLE9.items(): pal[i] = c
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
VELVET = [(64, 32, 96), (96, 56, 136), (128, 88, 168)]
def bench(w=16, h=11):
    a = np.zeros((h, w, 3), np.uint8); m = np.zeros((h, w), bool)
    a[0:6, 0:w] = B_OUTLINE; m[0:6, 0:w] = True
    a[1:3, 1:w - 1] = VELVET[2]; a[3:5, 1:w - 1] = VELVET[1]; a[1, 2:w - 2] = (168, 132, 204)   # cushion
    a[5, 1:w - 1] = B_FRAME_D
    for x in (1, w - 3):                                        # legs
        a[6:h, x:x + 2] = B_FRAME; a[6:h, x - 1] = B_OUTLINE; a[6:h, x + 2] = B_OUTLINE; m[6:h, x - 1:x + 3] = True
    a[h - 1, :] = a[h - 1, :]
    return a, m

PIANO = {0x1FA, 0x1FB, 0x1FC, 0x202, 0x203, 0x204}
def compose(wall):
    ts = cabin_ts(wall); W, H = X1 - X0, Y1 - Y0
    tsp = cabin_ts(wall)
    for p in (7, 8, 10, 11): tsp.pal[p] = wood_pal(TS(CABIN).pal[p], WALNUT)
    tsp.cache = {}
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(Y0, Y1):
        for x in range(X0, X1):
            m = EDITS.get((x, y), CELLS[y * CW + x] & 0x3FF)
            if (x, y) in RUG_CELLS: m = 0x18B
            if (x, y) in MAT_CELLS: m = 0x18B if y == 25 else 0
            if m in PIANO: cell = meta_clean(ts, m, top=False, ts_obj=tsp, clean=y in WALL_ROWS)   # piano layer in walnut
            else: cell = meta_clean(ts, m, top=(y == 6)) if y in WALL_ROWS else ts.meta(m)
            img[(y - Y0) * 16:(y - Y0 + 1) * 16, (x - X0) * 16:(x - X0 + 1) * 16] = cell
    # T4, the haunted lounge: its old dark door in the old dingy colours
    old = TS(CABIN)
    for (x, y) in ((20, 7), (20, 8)): img[(y - Y0) * 16:(y - Y0 + 1) * 16, (x - X0) * 16:(x - X0 + 1) * 16] = old.meta(CELLS[y * CW + x] & 0x3FF)
    def put(a, px, py, m=None):
        h, w = a.shape[:2]; sub = img[py:py + h, px:px + w]
        if m is None: sub[:] = a
        else: sub[m] = a[m]
    plain = np.vstack([np.hstack([meta_clean(ts, m, top=(r == 0)) for m in row]) for r, row in enumerate(((0x179, 0x179), (0x17B, 0x17B), (0x183, 0x183)))])
    for xa, xb in WINDOW_PAIRS:
        sub = img[(6 - Y0) * 16:(9 - Y0) * 16, (xa - X0) * 16:(xb + 1 - X0) * 16]; clean_window(sub, plain)
    # the piano bench: floor under it, then the clean bench centred on the old one
    for x in (9, 10): img[(20 - Y0) * 16:(21 - Y0) * 16, (x - X0) * 16:(x + 1 - X0) * 16] = ts.meta(0x18B)
    b, bm = bench(); put(b, (9 - X0) * 16 + 8, (20 - Y0) * 16 + 2, bm)
    a, m = rug_rgb(ts, 'centre'); put(a, (13 - X0) * 16, (21 - Y0) * 16, m)
    a, m = rug_rgb(ts, 'mat'); put(a, (13 - X0) * 16, (25 - Y0) * 16, m)
    for fx, fy in FLIGHTS:
        for dy, row in enumerate(stair_pieces(wall)):
            for dx, (piece, mask) in enumerate(row):
                px, py = (fx + dx - X0) * 16, (fy + dy - Y0) * 16
                if dx != 1 and SIDE_BG[dy] is not None:
                    y = fy + dy; img[py:py + 16, px:px + 16] = meta_clean(ts, SIDE_BG[dy]) if y in WALL_ROWS else ts.meta(SIDE_BG[dy])
                put(piece, px, py, mask)
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/academy_mock'
    ims = [(k, compose(k)) for k in WALLS]
    S = Image.new('RGB', (sum(i.shape[1] for _, i in ims) + 12 * len(ims), ims[0][1].shape[0] + 14), (28, 28, 28)); d = ImageDraw.Draw(S); x = 0
    for k, i in ims:
        S.paste(Image.fromarray(i), (x, 14)); d.text((x + 2, 2), k, fill=(255, 230, 120)); x += i.shape[1] + 12
    S.resize((S.width * 2, S.height * 2), 0).save(out + '.png'); print(out + '.png')
