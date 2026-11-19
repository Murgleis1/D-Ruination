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
WALLS = {'A ivory plaster': ((236, 226, 202), (206, 194, 168)), 'B pale stone': ((214, 216, 222), (184, 186, 196))}
HONEY = [(78, 50, 34), (106, 70, 44), (136, 96, 58), (164, 122, 76), (190, 148, 98), (210, 172, 120), (226, 196, 146)]
def is_wood(c):
    r, g, b = c; return c not in ((0, 248, 248), (0, 0, 0)) and r >= b and (r - b) >= 12 and not (g > r + 8)
def honey(c):
    l = hls(c)[1]; t = min(1.0, max(0.0, (l - 0.14) / 0.42)); return HONEY[int(round(t * (len(HONEY) - 1)))]
def wood_pal(pal): return [honey(tuple(c)) if is_wood(tuple(c)) else tuple(c) for c in pal]
def cabin_ts(wall):
    ts = TS(CABIN); ts.cache = {}
    for p in range(7, 12): ts.pal[p] = wood_pal(ts.pal[p])
    plaster, shade = WALLS[wall]
    ts.pal[7][15], ts.pal[7][14], ts.pal[7][10] = plaster, shade, plaster
    ts.pal[7][6] = ts.pal[7][7] = (84, 62, 52); ts.pal[7][8] = (150, 120, 96)          # outlines, baseboard: warm
    return ts
WALL_META = {0x170, 0x178, 0x179, 0x17A, 0x17B, 0x180, 0x182, 0x183, 0x1C7, 0x1CF, 0x1C8, 0x1C9}
WALL_ROWS = {6, 7, 8, 12, 13, 17, 18}                    # every tile in the wall rows carries plaster (windows, chimney, doors)
import struct as _st
from render import ROM as _ROM
def meta_clean(ts, m, top=False):
    """A wall metatile with its stains and moss painted out: in palette 7, 14 and 10 -> 15, except a straight
    3-pixel band at the top of the pieces under the ceiling."""
    base = off(CABIN['primary']['mt']) + 24 * m if m < 512 else off(CABIN['secondary']['mt']) + 24 * (m - 512)
    e = _st.unpack_from('<12H', _ROM, base); img = np.zeros((16, 16, 3), np.uint8)
    for layer in range(3):
        for q in range(4):
            v = e[layer * 4 + q]; t = ts.tile(v & 0x3FF)
            if t is None: continue
            t = t.copy()
            if v & 0x400: t = t[:, ::-1]
            if v & 0x800: t = t[::-1, :]
            y, x = (q // 2) * 8, (q % 2) * 8
            if v >> 12 == 7:
                band = np.zeros((8, 8), bool)
                if top and q < 2: band[:3] = True
                t = np.where(np.isin(t, (10, 14)) & ~band, 15, t); t = np.where(band & (t != 0), 14, t)
            pal = np.array(ts.pal[v >> 12], np.uint8)
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
FLIGHTS = [(16, 16), (10, 11)]                           # (left column, top row): 3 wide x 3 tall

# ---- the saloon staircase, recoloured to the new wood ----
STAIR_ROWS = [(192, 193, 194, 247), (200, 201, 202, 240), (208, 209, 210, 248)]   # + the saloon's background
def stair_pieces(wall):
    pal_backup = [list(p) for p in DORM.SAL.pal]; DORM.SAL.cache.clear()
    for p in range(len(DORM.SAL.pal)): DORM.SAL.pal[p] = wood_pal(DORM.SAL.pal[p])
    rows = []
    for a, b, c, bg in STAIR_ROWS:
        bgi = DORM.SAL.meta(bg).astype(int); row = []
        for k, m in enumerate((a, b, c)):
            img = DORM.SAL.meta(m).copy()
            mask = np.ones((16, 16), bool) if k == 1 else (np.abs(img.astype(int) - bgi).sum(-1) > 24)
            row.append((img, mask))
        rows.append(row)
    DORM.SAL.pal[:] = pal_backup; DORM.SAL.cache.clear()
    return rows

# ---- straight-edged regal carpets, drawn ----
PURPLE = {'deep': (64, 32, 96), 'mid': (96, 56, 136), 'light': (128, 88, 168), 'white': (240, 236, 248), 'line': (200, 188, 224)}
def rug(w, h):
    a = np.zeros((h, w, 3), np.uint8); a[:] = PURPLE['mid']
    a[0, :] = a[-1, :] = PURPLE['deep']; a[:, 0] = a[:, -1] = PURPLE['deep']
    a[1:3, 1:-1] = PURPLE['white']; a[-3:-1, 1:-1] = PURPLE['white']; a[1:-1, 1:3] = PURPLE['white']; a[1:-1, -3:-1] = PURPLE['white']
    a[5, 5:-5] = PURPLE['line']; a[-6, 5:-5] = PURPLE['line']; a[5:-5, 5] = PURPLE['line']; a[5:-5, -6] = PURPLE['line']
    a[6:-6, 6:-6] = PURPLE['deep']; a[7:-7, 7:-7] = PURPLE['mid']
    return a

def compose(wall):
    ts = cabin_ts(wall); W, H = X1 - X0, Y1 - Y0
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(Y0, Y1):
        for x in range(X0, X1):
            m = EDITS.get((x, y), CELLS[y * CW + x] & 0x3FF)
            if (x, y) in RUG_CELLS: m = 0x18B
            img[(y - Y0) * 16:(y - Y0 + 1) * 16, (x - X0) * 16:(x - X0 + 1) * 16] = meta_clean(ts, m, top=(y == 6)) if y in WALL_ROWS else ts.meta(m)
    # T4, the haunted lounge: its old dark door in the old dingy colours
    old = TS(CABIN)
    for (x, y) in ((20, 7), (20, 8)): img[(y - Y0) * 16:(y - Y0 + 1) * 16, (x - X0) * 16:(x - X0 + 1) * 16] = old.meta(CELLS[y * CW + x] & 0x3FF)
    def put(a, px, py, m=None):
        h, w = a.shape[:2]; sub = img[py:py + h, px:px + w]
        if m is None: sub[:] = a
        else: sub[m] = a[m]
    put(rug(48, 32), (13 - X0) * 16, (21 - Y0) * 16)
    mat = rug(48, 24); put(mat, (13 - X0) * 16, (25 - Y0) * 16)
    for fx, fy in FLIGHTS:
        for dy, row in enumerate(stair_pieces(wall)):
            for dx, (piece, mask) in enumerate(row): put(piece, (fx + dx - X0) * 16, (fy + dy - Y0) * 16, mask)
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/academy_mock'
    ims = [(k, compose(k)) for k in WALLS]
    S = Image.new('RGB', (sum(i.shape[1] for _, i in ims) + 12 * len(ims), ims[0][1].shape[0] + 14), (28, 28, 28)); d = ImageDraw.Draw(S); x = 0
    for k, i in ims:
        S.paste(Image.fromarray(i), (x, 14)); d.text((x + 2, 2), k, fill=(255, 230, 120)); x += i.shape[1] + 12
    S.resize((S.width * 2, S.height * 2), 0).save(out + '.png'); print(out + '.png')
