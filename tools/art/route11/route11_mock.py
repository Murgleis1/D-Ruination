"""Route 11 mock (layout approved by the user 2026-11-20; tools/art/route11/layout_sketch.py).

45x30 cells, west from Pelluca's west road (the road meets Pelluca at its rows 28-30: Route 11 rows 14-16; the
connection offset is 14). Composed from metatiles, so the build can cut it straight into tiles:
  cor    Pelluca's own Cormoria tiles (tools/render_layout.py): mint grass, the pines, the cobble road, sand and sea.
         The eight columns next to Pelluca (37-44) use these only: across a map connection the neighbour is drawn
         with this map's tilesets, so the seam must be tiles both maps share.
  c31    Pokemon Crown's seaside farm village (map 3.1; credit Blah and the Crown team, used with permission):
         thatched farmhouse, fences, flower rows, worn dirt path, tan cliffs. Its grass is recoloured to Pelluca's
         mint.
  c325   Crown's dark woods (map 3.25): broadleaf forest, dark grass, tall grass, cobwebs, the woods trail.
  ody    Pokemon Odyssey's farm (map 0.232): cabbage rows, the sown field, hay bales (grass recoloured to mint).
Atlases: tools/art/route11/export_atlas.py (one per source map) into ATLAS (default /home/claude/scratch/route11/atlas).
Usage: python3 tools/art/route11/route11_mock.py out.png
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import render_layout as RL
ATLAS = os.environ.get('ROUTE11_ATLAS', '/home/claude/scratch/route11/atlas')
W, H = 45, 30
ROAD = 14                                         # the road's top row (Pelluca row 28)
SEAM = 37                                         # columns SEAM.. use Cormoria tiles only

_cor = RL.TS('LAYOUT_PELLUCA_CITY')
_at = {k: np.load(os.path.join(ATLAS, f), allow_pickle=False) for k, f in
       (('c31', 'crown31.npz'), ('c325', 'crown325.npz'), ('ody', 'ody232.npz'))}
# Crown's and Odyssey's grass greens -> Pelluca's mint (darkest to lightest)
MINT = [(112, 208, 160), (136, 216, 176), (160, 224, 176)]
RECOLOUR = {'c31': {(112, 184, 136): MINT[0], (128, 192, 136): MINT[1], (144, 200, 152): MINT[2], (80, 160, 112): (88, 192, 144)},
            'c31d': {(112, 184, 136): (80, 136, 64), (128, 192, 136): (104, 160, 88), (144, 200, 152): (112, 168, 80), (80, 160, 112): (96, 144, 80)},
            'c325m': {(80, 136, 64): MINT[0], (96, 144, 80): MINT[0], (104, 160, 88): MINT[1], (112, 168, 80): MINT[2]},
            'ody': {(80, 184, 152): MINT[0], (112, 200, 160): MINT[1], (136, 216, 184): MINT[2], (184, 224, 160): MINT[2]}}

def recolour(img, src):
    m = RECOLOUR.get(src)
    if not m: return img
    out = img.copy(); flat = out.reshape(-1, 3)
    for a, b in m.items(): flat[(flat == a).all(1)] = b
    return out

def _src(src): return {'c325m': 'c325', 'c31d': 'c31'}.get(src, src)

def full(src, mid):
    if src == 'cor': return np.asarray(_cor.metatile(mid), np.uint8)
    return recolour(_at[_src(src)]['full'][mid], src)

def top(src, mid):
    t = _at[_src(src)]['top'][mid]; rgb = recolour(t[..., :3].copy(), src); return rgb, t[..., 3] > 0

def cells_of(src, x0, y0, w, h):
    return _at[_src(src)]['cells'][y0:y0 + h, x0:x0 + w]

class Map:
    def __init__(self):
        self.g = [[[('cor', 6, 'full')] for _ in range(W)] for _ in range(H)]
        self.over = []                                       # pixel pastes after the cells: (rgba, x, y)
    def put(self, x, y, src, mid):
        if 0 <= x < W and 0 <= y < H: self.g[y][x] = [(src, mid, 'full')]
    def obj(self, x, y, src, mid):                            # an object (top layer) over what is there
        if 0 <= x < W and 0 <= y < H: self.g[y][x].append((src, mid, 'top'))
    def custom(self, x, y, img):
        self.g[y][x] = [('img', img, 'full')]
    def render(self):
        out = np.zeros((H * 16, W * 16, 3), np.uint8)
        for y in range(H):
            for x in range(W):
                c = out[y * 16:y * 16 + 16, x * 16:x * 16 + 16]
                for src, mid, kind in self.g[y][x]:
                    if src == 'img': c[:] = mid
                    elif kind == 'full': c[:] = full(src, mid)
                    else: rgb, m = top(src, mid); c[m] = rgb[m]
        return out
    def cell_img(self, x, y):
        return self.render_cell(x, y)

# ---------------------------------------------------------------- the pieces of the route
def pelluca_seam(M):
    """Columns 37-44: Pelluca's own columns 0-7 (its rows 14-43), so the pines and the road run straight on; the
    pines' right-edge pieces (Pelluca's forest ends at its column 7) become interior ones, and column 37 gets the
    left-edge pieces (the farm opens west of it)."""
    g = np.fromfile(os.path.join(RL.C, 'data/layouts/PellucaCity/map.bin'), '<u2').reshape(60, 80) & 0x3FF
    inner = {32: 30, 25: 23}; left = {31: 29, 24: 22}
    for y in range(H):
        for c in range(8):
            v = int(g[y + ROAD, c])
            if c == 7: v = inner.get(v, v)
            if c == 0: v = left.get(v, v)
            M.put(SEAM + c, y, 'cor', v)

def road(M, x0):
    for x in range(x0, SEAM):
        M.put(x, ROAD, 'cor', 64); M.put(x, ROAD + 1, 'cor', 78); M.put(x, ROAD + 2, 'cor', 131)
    for dy, v in enumerate((63, 77, 130)):                   # the road's west end, on the dirt track
        img = full('cor', v).copy(); path = full('c31', 0x7e)
        grass = np.isin(img.reshape(-1, 3).view([('', np.uint8)] * 3), np.array(MINT, np.uint8).view([('', np.uint8)] * 3)).reshape(16, 16)
        img[grass] = path[grass]; M.custom(x0, ROAD + dy, img)

def track(M, x0, x1, xw):
    """The dirt track west of the cobbles: Crown's worn path; west of xw its grassy edges are the woods' dark grass."""
    for x in range(x0, x1):
        for dy, v in enumerate((0x2c1, 0x7e, 0x2d1)): M.put(x, ROAD + dy, 'c31' if x >= xw else 'c31d', v)

def dark_forest(M, x0, x1, y0, y1, top_edge=True, bottom_edge=True):
    """Crown's broadleaf woods: three-cell-wide canopies in rows of two (10 11 12 / 18 19 1a), a canopy top edge
    over grass (b c d), the last row of trees with trunks (13 14 15 / 1b 1c 1d)."""
    for y in range(y0, y1 + 1):
        r = y - y0
        for x in range(x0, x1 + 1):
            k = (x - x0) % 3
            if top_edge and r == 0: v = (0xb, 0xc, 0xd)[k]
            elif bottom_edge and y == y1 - 1: v = (0x13, 0x14, 0x15)[k]
            elif bottom_edge and y == y1: v = (0x1b, 0x1c, 0x1d)[k]
            else:
                rr = r - (1 if top_edge else 0)
                v = ((0x10, 0x11, 0x12), (0x18, 0x19, 0x1a))[rr % 2][k]
                if v == 0x1a and (x * 7 + y * 3) % 11 == 0: v = 0x3e           # a cobweb here and there
            M.put(x, y, 'c325', v)

def dark_grass(M, x0, x1, y0, y1):
    var = [0x1] * 9 + [0x4, 0xa]
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1): M.put(x, y, 'c325', var[(x * 5 + y * 3) % len(var)])

def tall_grass(M, src, x0, x1, y0, y1):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            cx = 0 if x == x0 else 2 if x == x1 else 1; cy = 0 if y == y0 else 2 if y == y1 else 1
            M.put(x, y, src, ((0x21, 0x22, 0x23), (0x29, 0x2a, 0x2b), (0x31, 0x32, 0x33))[cy][cx])

def blend(M, x, y, frac, seed=0):
    """A cell part dark grass, part mint (frac of it dark, by a stable noise): the woods' grass giving way."""
    rng = np.random.default_rng(seed + x * 31 + y * 17)
    d = full('c325', 0x1); m = full('cor', 6)
    n = rng.random((16, 16)); xs = np.linspace(0, 1, 16)[None, :]
    mask = (n * 0.6 + (1 - xs) * 0.8) > (1.4 - frac * 1.4)
    img = m.copy(); img[mask] = d[mask]; M.custom(x, y, img)

def cliffs(M, x0, x1):
    """Tan cliffs along the north edge: plateau (5e) and a two-row face (52)."""
    for x in range(x0, x1 + 1):
        for y in (0, 1): M.put(x, y, 'c31', 0x5e)
        for y in (2, 3): M.put(x, y, 'c31', 0x52)

def cottage(M, x0, y0):
    """Crown's thatched cottage (its cells 12..18 x 9..12), objects over the grass."""
    c = cells_of('c31', 12, 9, 7, 4)
    for dy in range(4):
        for dx in range(7): M.obj(x0 + dx, y0 + dy, 'c31', int(c[dy, dx]))

def block(M, src, sx, sy, w, h, x0, y0, as_obj=False):
    c = cells_of(src, sx, sy, w, h)
    for dy in range(h):
        for dx in range(w):
            if as_obj: M.obj(x0 + dx, y0 + dy, src, int(c[dy, dx]))
            else: M.put(x0 + dx, y0 + dy, src, int(c[dy, dx]))

def fence_row(M, x0, x1, y, gaps=()):
    for x in range(x0, x1 + 1):
        if x in gaps: continue
        M.obj(x, y, 'c31', 0x300 if (x - x0) % 2 == 0 else 0x302)

def woods(M, cols, kind):
    """Crown's broadleaf woods as columns of trees (three cells wide): cols = [(x0, y_top, y_bottom)], each column
    with its own reach, so the wood's edge is ragged. kind 'north' (from the map top: trunks at the bottom) or
    'south' (to the map bottom: a canopy top edge at y_top)."""
    for x0, yt, yb in cols:
        for y in range(yt, yb + 1):
            for k in range(3):
                x = x0 + k
                if kind == 'north':
                    if y == yb - 1: v = (0x13, 0x14, 0x15)[k]
                    elif y == yb: v = (0x1b, 0x1c, 0x1d)[k]
                    else: v = ((0x18, 0x19, 0x1a), (0x10, 0x11, 0x12))[(yb - 1 - y) % 2][k]
                else:
                    if y == yt: v = (0xb, 0xc, 0xd)[k]
                    else: v = ((0x10, 0x11, 0x12), (0x18, 0x19, 0x1a))[(y - yt - 1) % 2][k]
                if v == 0x1a and (x * 7 + y * 3) % 11 == 0: v = 0x3e           # a cobweb here and there
                M.put(x, y, 'c325', v)

def north_cliffs(M, x0):
    """The tan cliffs: a piece of Crown's own stepped cliffs (its cells 3..21 x 0..8, descending to the east), the
    sand it stands on in Crown turned to grass. Crown's kit has no west-facing side: the west end is its
    east-facing side (54), corner (5c) and foot (59) mirrored."""
    c = cells_of('c31', 3, 0, 19, 9); sub = {0x125: 0xe, 0x2b8: 0x54, 0x2ed: 0x5c}
    for y in range(9):
        for x in range(19):
            v = int(c[y, x]); v = sub.get(v, v)
            if v == 0xe: continue                              # grass: keep the mint already there
            if x == 0:                                          # the west end, mirrored
                v = {0x52: 0x5c}.get(v, 0x54) if y < 8 else 0x59
                if y == 7: v = 0x5c
                M.custom(x0 + x, y, full('c31', v)[:, ::-1].copy()); continue
            M.put(x0 + x, y, 'c31', v)

def sea_wall(M, x0, x1, y, stair):
    """Pelluca's own dark sea wall (Cormoria 10 over 203) above the cove, with stone steps down."""
    for x in range(x0, x1 + 1):
        a, b = (45, 208) if x == stair else (46, 209) if x == stair + 1 else (10, 203)
        M.put(x, y, 'cor', a); M.put(x, y + 1, 'cor', b)

def shore(M, x0, x1, ytop, depth):
    """Sand from ytop down to the waterline, then Pelluca's foam (171), wave edge (173), shallows (175) and sea
    (162); depth(x) = the row of the foam. A step down to the right uses 172/174/176, a step up 256/257/258."""
    for x in range(x0, x1 + 1):
        r = depth(x)
        for y in range(ytop, r): M.put(x, y, 'cor', 163)
        seq = [171, 173, 175]
        if x < x1 and depth(x + 1) > r: seq = [172, 174, 176]
        if x > x0 and depth(x - 1) > r: seq = [256, 257, 258]
        for i, v in enumerate(seq): M.put(x, r + i, 'cor', v)
        for y in range(r + 3, H): M.put(x, y, 'cor', 162)
        if seq[0] in (172, 256) and r + 3 < H: M.put(x, r + 3, 'cor', 175)

def fence(M, x0, x1, y, gaps=()):
    for x in range(x0, x1 + 1):
        if x in gaps: continue
        v = 0x34 if x == x0 or x - 1 in gaps else 0x2b if x == x1 or x + 1 in gaps else 0x29
        M.put(x, y, 'c31', v)

def compose():
    M = Map()
    pelluca_seam(M)
    # the west woods: dark grass, ragged broadleaf woods north and south of the trail, tall grass by it
    dark_grass(M, 0, 17, 0, H - 1)
    woods(M, [(0, 0, 11), (3, 0, 9), (6, 0, 11), (9, 0, 7), (12, 0, 5), (15, 0, 3)], 'north')
    woods(M, [(0, 18, H - 1), (3, 20, H - 1), (6, 18, H - 1), (9, 21, H - 1), (12, 19, H - 1), (15, 20, H - 1)], 'south')
    tall_grass(M, 'c325', 3, 8, 12, 13); tall_grass(M, 'c325', 1, 5, 17, 18); tall_grass(M, 'c325', 10, 13, 9, 11)
    # the woods' grass giving way to the farm's mint, along a ragged line
    edge = {y: 16 + (0, 1, 1, 2, 1, 0, -1, 0, 1, 2, 2, 1, 0, 0, 0, 0, 0, 1, 2, 1, 0, -1, 0, 1, 2, 1, 1, 0, 0, 1)[y] for y in range(H)}
    for y in range(H):
        for x in range(edge[y] + 1, edge[y] + 4):
            if 0 <= x < W and M.g[y][x][0][:2] == ('c325', 1) or M.g[y][x][0][0] == 'c325' and M.g[y][x][0][1] in (4, 10):
                M.put(x, y, 'cor', 6)
        for x, fr in ((edge[y], 0.8), (edge[y] + 1, 0.4)):
            if M.g[y][x][0][0] == 'c325' and M.g[y][x][0][1] in (1, 4, 10): blend(M, x, y, fr)
    # the road: Pelluca's cobbles to the farm, the worn dirt track, the woods trail
    road(M, 23)
    track(M, 0, 23, 15)
    # north: Crown's stepped tan cliffs, their west end behind the woods' last trees
    north_cliffs(M, 18)
    woods(M, [(15, 0, 9)], 'north')
    # the farm north of the road: farmhouse and yard, cabbages, the sown field, hay
    cottage(M, 27, 8)
    fence(M, 26, 35, 12, gaps=(30, 31))
    block(M, 'ody', 18, 7, 6, 3, 19, 7)                      # cabbage rows
    block(M, 'ody', 17, 12, 8, 4, 18, 10)                    # the sown field
    block(M, 'ody', 9, 9, 2, 2, 34, 9, as_obj=True)          # hay bales
    block(M, 'ody', 15, 10, 2, 2, 25, 9, as_obj=True)
    M.obj(26, 11, 'c31', 0x28)                               # a stump
    # south of the road: fenced flower rows, tall grass, the sea wall and the cove
    for y in (18, 19):
        for x in range(29, 35): M.put(x, y, 'c31', 0x282 if y == 18 else 0x283)
    fence(M, 28, 35, 20, gaps=(31,))
    tall_grass(M, 'c325m', 19, 25, 18, 20)
    sea_wall(M, 17, SEAM - 1, 21, 27)
    shore(M, 17, SEAM - 1, 23, lambda x: 26 if x < 20 or x > 32 else 25 if x < 23 or x > 29 else 24)
    # a few flowers and tufts in the grass, a sign by the road
    for x, y, v in ((24, 6, 0x285), (36, 18, 0x285), (17, 12, 0x285), (34, 15 + 2, 0x285)):
        if M.g[y][x][0][:2] == ('cor', 6): M.obj(x, y, 'c31', v)
    for x, y in ((26, 17), (27, 16 + 1), (36, 13), (21, 12)):
        if M.g[y][x][0][:2] == ('cor', 6): M.put(x, y, 'cor', 21)
    M.obj(26, 13, 'c31', 0x88)
    M.obj(22, 17, 'c31', 0x17)                               # a boulder by the road
    return M

def main(out):
    M = compose(); img = M.render()
    Image.fromarray(img).save(out)
    Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), 0).save(out.replace('.png', '_2x.png'))
    print(out)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/route11/route11_mock.png')
