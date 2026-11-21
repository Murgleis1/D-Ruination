"""Hollow Hill mock (user concept approved 2026-11-20; bible/20_chapter1_build.md, Route 11 and Hollow Hill).

About 50x50 of woods rising in three rings, each a cliff step up, to a central rock knoll. The path in from Route 11
(east) climbs the rings by stairs to the sealed tunnel door at the knoll's foot; the north exit to Mirroh leaves from
the outer ring (Glaive there); the Eiscue and the 1v2 in a clearing on the outer ring (south-west). Very foggy,
spooky, unsettling. Room for secrets: burrow mouths as scenery now.

Art: Pokemon Odyssey's haunted forest (its maps 0.94/0.95/0.97): the teal floor, dark pines, dead trees, stumps, logs,
mushrooms, stone ruins, the stone terraces and stairs, the sealed blue door, the void pits with red eyes, the burrows.
At the east edge Route 11's own west end carries on (Crown's olive woods and the dirt track) and the ground darkens
gradually from Route 11's olive to the haunted teal (four shades meeting in Crown's patch-edge shapes, kit.py).

The terraces: an elevation per cell (each ring a plateau, its edge stepping down in bands one cell wide, two bands a
ring, three for the knoll), every edge cell drawn by Odyssey's own grammar from which neighbours are lower:
  south face 2f1 (ends 2f0 west, 2f2 east), west-facing 2e8 (lit), east-facing 2ea (shaded), north lip 2e1 (corners
  2e0, 2e2), inner corners 2dc (south-west lower), 2db (south-east), 2e4 (north-west), 2e3 (north-east).
The layout is 56x60: five rows of woods above and below the picture, out of reach; Route 11 joins the east edge
(Route 11's row = Hollow Hill's row - OFF; its road rows 19-21 are rows 40-42 here).
Usage: python3 tools/art/hollowhill/hh_mock.py [outdir]
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'route11'))
import kit
from kit import RL

W, H = 66, 64
OFF = 24                        # Route 11 row = Hollow Hill row - OFF
ROAD = 19 + OFF                 # the track's three rows (Route 11's road rows 19-21)
SEAM = 58                       # columns 58-65 are Route 11's own (its columns 1-8, its metatiles): a connected map is
                                # drawn with the tilesets of the map the player stands in, so the columns each map shows
                                # of the other are the same metatiles on both sides (as Route 11 does with Pelluca)

def r11_cell(x, y):
    """Route 11's block (metatile | collision) for one of the seam's cells: its column x - 57, its row y - OFF (above
    its top, its woods' two-row pattern carried up)."""
    import struct
    if not hasattr(r11_cell, 'v'):
        d = open(os.path.join(RL.C if hasattr(RL, 'C') else '/home/claude/repo/codebase', 'data/layouts/Route11/map.bin'), 'rb').read()
        r11_cell.v = struct.unpack('<%dH' % (90 * 40), d)
    ry = y - OFF if y >= OFF else y % 2
    return r11_cell.v[ry * 90 + (x - 57)]

# ------------------------------------------------------------------ pieces
def ody_raw(m): return kit.atlas('ody_0_97')['full'][m]

# Hollow Hill's own colours (user 2026-11-20): the woods and their floor an off-white, creepy bone; the cliffs a
# sinister stone, dark and light mixed. Odyssey's colours, one for one (its trunks, mushrooms and the door's cold blue kept).
BONE = {(32, 96, 96): (124, 116, 102), (48, 128, 128): (150, 142, 124), (32, 88, 88): (108, 100, 90),   # floor
        (16, 64, 64): (84, 76, 72), (16, 40, 40): (52, 42, 46), (16, 32, 32): (32, 26, 32),             # shadow
        (104, 128, 120): (224, 218, 202), (88, 136, 96): (192, 188, 178), (56, 112, 96): (146, 144, 144),  # pines: bone
        (40, 72, 64): (90, 88, 96),                                     # going to a sinister grey
        (64, 40, 56): (60, 40, 48), (128, 96, 104): (140, 120, 112), (88, 72, 80): (96, 80, 82),         # wood
        (160, 136, 112): (186, 172, 150),
        (64, 72, 104): (58, 50, 64), (40, 48, 88): (30, 24, 36), (96, 96, 120): (92, 84, 96),             # stone
        (144, 144, 136): (176, 168, 150), (192, 192, 168): (222, 214, 192), (120, 120, 128): (124, 114, 120),
        (128, 136, 136): (146, 138, 130), (176, 184, 192): (198, 190, 176), (200, 200, 200): (232, 226, 210),
        (160, 168, 168): (176, 168, 156), (88, 88, 104): (80, 72, 84),
        (48, 136, 40): (122, 118, 80), (112, 200, 80): (170, 164, 110), (40, 72, 8): (80, 74, 50),       # weeds
        (176, 240, 120): (204, 198, 150)}

def bone(img):
    out = img.copy(); flat = out.reshape(-1, 3); key = [tuple(p) for p in flat.tolist()]
    for i, k in enumerate(key):
        if k in BONE: flat[i] = BONE[k]
    return out

_ody = {}
def ody(m):
    if m not in _ody: _ody[m] = bone(ody_raw(m))
    return _ody[m]
TEAL_GRASS = {(32, 96, 96), (48, 128, 128), (32, 88, 88)}
OLIVE_GRASS = set(kit.OLIVE4) | {(104, 160, 88)}
SRC = {'ody': (ody_raw, TEAL_GRASS), 'c325': (lambda m: kit.atlas('crown325')['full'][m], OLIVE_GRASS),
       'c31': (lambda m: kit.atlas('crown31')['full'][m], {(112, 184, 136), (128, 192, 136), (144, 200, 152), (80, 160, 112)})}

def overlay(src, m, keep_grass=False):
    f, grass = SRC[src]; img = f(m).copy()
    key = [tuple(p) for p in img.reshape(-1, 3).tolist()]
    a = np.array([255 if keep_grass or k not in grass else 0 for k in key], np.uint8).reshape(16, 16)
    out = np.zeros((16, 16, 4), np.uint8); out[..., :3] = bone(img) if src == 'ody' else img; out[..., 3] = a
    return out

# ------------------------------------------------------------------ the four grounds, olive (Route 11) to teal
def _recolour(img, pairs):
    out = img.copy(); flat = out.reshape(-1, 3)
    for a, b in pairs: flat[(flat == a).all(1)] = b
    return out
TEAL = ody(0x2e9).copy()
def _teal(base, blade, dark): return _recolour(ody_raw(0x2e9), [((32, 96, 96), base), ((48, 128, 128), blade), ((32, 88, 88), dark)])
GROUNDS = [kit.plain(3),                                                                           # Route 11's olive
           _recolour(kit.plain(3), zip(kit.OLIVE, [(72, 126, 66), (86, 138, 76), (98, 150, 86)])),
           _recolour(kit.plain(3), zip(kit.OLIVE, [(84, 122, 70), (96, 132, 80), (108, 142, 90)])),
           _teal((104, 118, 88), (126, 140, 106), (94, 106, 80)),
           _teal((116, 116, 98), (140, 136, 116), (104, 104, 88)),
           TEAL]                                                                                    # the bone floor
RIM = [(80, 136, 64), (72, 126, 66), (84, 122, 70), (94, 106, 80), (104, 104, 88), (108, 100, 90)]
TOP = len(GROUNDS) - 1

def ground_cell(v):
    ks = sorted(set(v))
    if len(ks) == 1: return GROUNDS[ks[0]].copy()
    lo, hi = ks
    return kit.edge_cell(GROUNDS[lo], GROUNDS[hi], [c == hi for c in v], rim_lo=RIM[hi])

# ------------------------------------------------------------------ the shapes
def superellipse(cx, cy, a, b, p):
    y, x = np.mgrid[0:H, 0:W]
    return (np.abs((x - cx) / a) ** p + np.abs((y - cy) / b) ** p) <= 1

def cheb_depth(mask, cap):
    """Each cell's Chebyshev distance to the outside of mask (1 on its edge), capped."""
    d = np.zeros(mask.shape, int); cur = mask.copy()
    from scipy.ndimage import binary_erosion
    for k in range(1, cap + 1):
        d[cur] = k; cur = binary_erosion(cur, np.ones((3, 3), bool), border_value=0)
    return d

def rrect(x0, y0, x1, y1, r):
    """Cells x0..x1, y0..y1 with corners rounded at radius r."""
    y, x = np.mgrid[0:H, 0:W]
    cx = np.clip(x, x0 + r, x1 - r); cy = np.clip(y, y0 + r, y1 - r)
    return (x >= x0) & (x <= x1) & (y >= y0) & (y <= y1) & ((x - cx) ** 2 + (y - cy) ** 2 <= r * r + r)

def clean(m):
    """No spur or notch one cell wide (they make no shape the terrace grammar can draw)."""
    from scipy.ndimage import binary_opening, binary_closing
    k = np.ones((3, 3), bool)
    for _ in range(3): m = binary_closing(binary_opening(m, k), k)
    return m

def rings():
    P1 = rrect(10, 14, 49, 50, 7) & ~rrect(2, 43, 14, 63, 5)     # ring 1, the south-west clearing bitten out of it
    P2 = rrect(17, 19, 41, 43, 5) | rrect(12, 27, 47, 33, 0)     # ring 2 runs out to ring 1's edge west and east,
                                                               # cutting ring 1 in two (north and south halves)
    P3 = rrect(23, 24, 35, 35, 4)                               # the knoll
    P1, P2, P3 = clean(P1), clean(P2), clean(P3)
    E = cheb_depth(P1, 2) + cheb_depth(P2, 2) + cheb_depth(P3, 3)
    return E, (P1, P2, P3)

def face_piece(E, x, y):
    h = E[y, x]
    def low(dx, dy):
        xx, yy = x + dx, y + dy
        return 0 <= xx < W and 0 <= yy < H and E[yy, xx] < h
    n, s, e, w = low(0, -1), low(0, 1), low(1, 0), low(-1, 0)
    if s and w: return 0x2f0
    if s and e: return 0x2f2
    if s: return 0x2f1
    if n and w: return 0x2e0
    if n and e: return 0x2e2
    if n: return 0x2e1
    if w: return 0x2e8
    if e: return 0x2ea
    if low(-1, 1): return 0x2dc
    if low(1, 1): return 0x2db
    if low(-1, -1): return 0x2e4
    if low(1, -1): return 0x2e3
    return None

# ------------------------------------------------------------------ the map
_r11ts = {}
def r11_img(m):
    if m not in _r11ts:
        if 'ts' not in _r11ts: _r11ts['ts'] = RL.TS('LAYOUT_ROUTE11')
        _r11ts[m] = np.asarray(_r11ts['ts'].metatile(m), np.uint8)
    return _r11ts[m].copy()

class Map:
    def __init__(self):
        self.field = None
        self.lock = np.zeros((H + 1, W + 1), bool)
        self.E, self.P = rings()
        self.face = {}                                     # (x, y) -> Odyssey metatile (terraces, stairs, door)
        self.over = [[[] for _ in range(W)] for _ in range(H)]
        self.used = np.full((H, W), None, object)
        self.units = []                                    # the pines of the woods' columns: (x0, top row)
        self.ground = [[None] * W for _ in range(H)]       # an RGB image replacing the grass, or None
        self.seam = {(x, y): r11_cell(x, y) for y in range(H) for x in range(SEAM, W)}
        for (x, y) in self.seam: self.used[y, x] = 'seam'
        for y in range(H):
            for x in range(W):
                p = face_piece(self.E, x, y)
                if p is not None: self.face[x, y] = p; self.used[y, x] = 'cliff'

    def lay(self, x, y, src, m, what, top=False, check=True):
        if not (0 <= x < W and 0 <= y < H): return
        if check and self.used[y, x] is not None: raise ValueError(f'{what} at {x},{y} over {self.used[y, x]}')
        o = overlay(src, m); self.over[y][x].append((o, top)); self.used[y, x] = what

    def free(self, x0, y0, w, h, margin=1, avoid=('cliff', 'tree', 'road', 'pit', 'woods', 'thing')):
        for y in range(y0 - margin, y0 + h + margin):
            for x in range(x0 - margin, x0 + w + margin):
                if not (0 <= x < W and 0 <= y < H):
                    if x0 <= x < x0 + w and y0 <= y < y0 + h: return False
                    continue
                u = self.used[y, x]; inside = x0 <= x < x0 + w and y0 <= y < y0 + h
                if inside and u is not None: return False
                if not inside and u is not None and u.split(':')[0] in avoid: return False
        return True

    def cell(self, x, y):
        if (x, y) in self.seam: return r11_img(self.seam[x, y] & 0x3FF)
        if (x, y) in self.face:
            v = self.face[x, y]; img = ody(abs(v)).copy()
            if v < 0: img = img[::-1].copy()              # (negative: drawn upside down, stairs on a north edge)
        elif self.ground[y][x] is not None: img = self.ground[y][x].copy()
        else:
            f = self.field; img = ground_cell((f[y, x], f[y, x + 1], f[y + 1, x], f[y + 1, x + 1]))
        for o, _ in self.over[y][x]:
            m = o[..., 3] > 0; img[m] = o[..., :3][m]
        return img

    def render(self):
        out = np.zeros((H * 16, W * 16, 3), np.uint8)
        for y in range(H):
            for x in range(W): out[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = self.cell(x, y)
        return out

def shade_field(seed=11):
    """0 olive (Route 11's west end) .. TOP teal: a ramp from the east edge, roughened; teal west of column 51."""
    rng = np.random.default_rng(seed)
    def noise(cell):
        g = rng.random((H // cell + 3, W // cell + 3))
        ys = np.arange(H + 1) / cell; xs = np.arange(W + 1) / cell
        y0 = ys.astype(int); x0 = xs.astype(int); fy = (ys - y0)[:, None]; fx = (xs - x0)[None, :]
        fy = fy * fy * (3 - 2 * fy); fx = fx * fx * (3 - 2 * fx)
        a = g[y0][:, x0]; b = g[y0][:, x0 + 1]; c = g[y0 + 1][:, x0]; d = g[y0 + 1][:, x0 + 1]
        return (a * (1 - fx) + b * fx) * (1 - fy) + (c * (1 - fx) + d * fx) * fy
    n = noise(6) * 0.6 + noise(3) * 0.4 - 0.5
    x = np.arange(W + 1)[None, :].astype(float)
    s = np.interp(x, [0, 49, 51, 53, 54, 55, 56, 57, 58, 66], [5, 5, 4.4, 3.6, 3, 2.2, 1.4, 0.6, 0, 0]) + n * 2.4 * np.interp(x, [0, 49, 51, 55, 57], [0, 0, 1, 1, 0])
    v = np.clip(np.rint(s), 0, TOP).astype(int); v = np.broadcast_to(v, (H + 1, W + 1)).copy()
    v[:, 57:] = 0; v[:, :50] = TOP
    for _ in range(8):
        bad = False
        for yy in range(H):
            for xx in range(W):
                q = v[yy:yy + 2, xx:xx + 2]
                if q.max() - q.min() > 1: bad = True; q[q == q.max()] -= 1
        if not bad: break
    return v

def tint(rgb, t, to=(186, 176, 152)):
    """Crown's greens drawn toward the bone woods (its trees paling as the woods change)."""
    return (rgb * (1 - t) + np.array(to) * t).astype(np.uint8)

def flatten(M, x0, y0, w, h, k):
    M.field[y0:y0 + h + 1, x0:x0 + w + 1] = k
    M.lock[y0:y0 + h + 1, x0:x0 + w + 1] = True

def settle(M):
    """After flattening: no cell may span more than two neighbouring shades; unlocked vertices give way."""
    f, lk = M.field, M.lock
    for _ in range(80):
        bad = False
        for yy in range(H):
            for xx in range(W):
                q = f[yy:yy + 2, xx:xx + 2]; l = lk[yy:yy + 2, xx:xx + 2]
                if q.max() - q.min() <= 1: continue
                bad = True
                if l.any() and q[l].max() - q[l].min() > 1: q[q > q.min() + 1] = q.min() + 1; continue
                ref = q[l] if l.any() else np.array([q.min()])
                hi, lo = ref.max(), ref.min()
                q[(~l) & (q > lo + 1)] = lo + 1; q[(~l) & (q < hi - 1)] = hi - 1
        if not bad: return
    raise SystemExit('the ground cannot settle')

# ------------------------------------------------------------------ units
PINE = ((0x281, 0x282), (0x289, 0x28a), (0x291, 0x292))

def pine(M, x, y, check=True):
    if check: assert M.free(x, y, 2, 3), ('pine', x, y)
    for dy, row in enumerate(PINE):
        for dx, v in enumerate(row): M.lay(x + dx, y + dy, 'ody', v, f'tree:pine{x},{y}', top=dy == 0)

def column_units(x0, yt, yb, kind):
    if kind == 'north': return [(x0, f - 2) for f in range(yb, 1, -2)]
    if kind == 'south': return [(x0, t) for t in range(yt, H - 2, 2)]
    if kind == 'stack': return [(x0, t) for t in range(yt, yb - 1, 2)]
    return [(x0, t) for t in range((yt + 1) // 2 * 2, yb - 1, 2)]           # 'wall': a crown on every even row

def pine_column(M, x0, yt, yb, kind):
    M.units += column_units(x0, yt, yb, kind)
    """Odyssey's pine forest: a column of pines two cells wide, each overlapping the one below (283 284: one pine's
    foot over the next one's crown). kind 'north' hangs from above yt (cut by the map's top), ends in a foot at yb;
    'south' starts with a crown at yt and runs off the bottom; 'wall' runs through (cut both ends)."""
    for y in range(yt, yb + 1):
        if kind == 'north': r = (yb - y)            # 0 foot, 1 trunk, 2 overlap, 3 trunk ...
        else: r = None
        if kind == 'north': pair = (0x291, 0x292) if r == 0 else (0x289, 0x28a) if r % 2 else (0x283, 0x284)
        elif kind == 'south':
            r = y - yt; pair = (0x281, 0x282) if r == 0 else (0x289, 0x28a) if r % 2 else (0x283, 0x284)
        elif kind == 'stack':                      # a crown at yt, a foot at yb, standing free
            assert (yb - yt) % 2 == 0, ('stack', x0, yt, yb)
            r = y - yt; pair = (0x281, 0x282) if r == 0 else (0x291, 0x292) if y == yb else (0x289, 0x28a) if r % 2 else (0x283, 0x284)
        else: pair = (0x289, 0x28a) if (y % 2) else (0x283, 0x284)
        for i in range(2):
            if M.used[y, x0 + i] is not None: raise ValueError(('pines', x0 + i, y, M.used[y, x0 + i]))
            M.lay(x0 + i, y, 'ody', pair[i], 'woods', top=kind in ('south', 'stack') and y == yt)

CROWN_WOODS_N = lambda yb, y, k: ((0x13, 0x14, 0x15)[k] if y == yb - 1 else (0x1b, 0x1c, 0x1d)[k] if y == yb
                                  else ((0x18, 0x19, 0x1a), (0x10, 0x11, 0x12))[(yb - 2 - y) % 2][k])
CROWN_WOODS_S = lambda yt, y, k: ((0xb, 0xc, 0xd)[k] if y == yt else ((0x10, 0x11, 0x12), (0x18, 0x19, 0x1a))[(y - yt - 1) % 2][k])

def crown_woods(M, cols, kind, t=0.0, k=None):
    """Route 11's own woods (Crown's), columns three wide, as at Route 11's west end (on olive or moss ground)."""
    for x0, yt, yb in cols:
        for y in range(yt, yb + 1):
            for k in range(3):
                x = x0 + k
                if not 0 <= x < SEAM: continue
                v = CROWN_WOODS_N(yb, y, k) if kind == 'north' else CROWN_WOODS_S(yt, y, k)
                M.lay(x, y, 'c325', v, 'woods', top=kind == 'south' and y == yt)
                if t: o = M.over[y][x][-1][0]; o[..., :3] = tint(o[..., :3], t)
        flatten(M, x0, yt, min(3, SEAM - x0), yb - yt + 1, k if k is not None else min(1, int(M.field[yt:yb + 2, x0:x0 + 4].min())))

def broad(M, x, y):
    assert M.free(x, y, 3, 3), ('broad', x, y)
    k = min(3, int(np.bincount(M.field[y:y + 4, x:x + 4].ravel()).argmax())); flatten(M, x, y, 3, 3, k)
    for dy, row in enumerate(((0xb, 0xc, 0xd), (0x13, 0x14, 0x15), (0x1b, 0x1c, 0x1d))):
        for dx, v in enumerate(row):
            M.lay(x + dx, y + dy, 'c325', v, f'tree:broad{x},{y}', top=dy == 0)
            if k: o = M.over[y + dy][x + dx][-1][0]; o[..., :3] = tint(o[..., :3], 0.18 * k)

def thing(M, x, y, ids, what='thing', w=1):
    """A small piece (or a row/column of them): stump, log, rock, dead tree, burrow, mushrooms."""
    if isinstance(ids, int): ids = [[ids]]
    h = len(ids); w = len(ids[0])
    assert all(M.used[yy, xx] is None for yy in range(y, y + h) for xx in range(x, x + w)), (what, x, y)
    for dy, row in enumerate(ids):
        for dx, v in enumerate(row): M.lay(x + dx, y + dy, 'ody', v, what)

def pit(M, x0, y0, w, h, eyes):
    """A void pit (Odyssey's dark hole: 360-372 round a void 340), red eyes in it."""
    for y in range(y0, y0 + h):
        for x in range(x0, x0 + w):
            cx = 0 if x == x0 else 2 if x == x0 + w - 1 else 1; cy = 0 if y == y0 else 2 if y == y0 + h - 1 else 1
            v = ((0x360, 0x361, 0x362), (0x368, 0x340, 0x36a), (0x370, 0x371, 0x372))[cy][cx]
            if (x, y) in eyes: v = eyes[x, y]
            assert M.used[y, x] is None, ('pit', x, y, M.used[y, x])
            M.ground[y][x] = ody(v).copy(); M.used[y, x] = 'pit'

# ------------------------------------------------------------------ the composition
# stairs, two wide, two bands: (x, top row, 'S' on a south face | 'N' on a north edge)
STAIRS = {'ring 1, from the south-east': (35, 49, 'S'), 'ring 1, from the clearing': (19, 49, 'S'),
          'ring 1, down to the north woods': (20, 14, 'N'), 'ring 1, down to the north-east woods': (40, 14, 'N'),
          'ring 2, south-west': (23, 42, 'S'), 'ring 2, south-east': (33, 42, 'S'),
          'ring 2, north-west': (22, 19, 'N'), 'ring 2, north-east': (34, 19, 'N')}
DOOR = (29, 35)                 # the sealed door, in the knoll's lowest band
KEY = {'from Route 11': (57, 44), 'to Mirroh': (17, 5), 'clearing': (8, 50), 'north-east woods': (46, 11),
       'ring 1 south': (35, 48), 'ring 1 north': (30, 17), 'ring 2': (23, 41), 'the door': (29, 36)}
# kept open: the clearing, the way north, the stairs' approaches, the door's forecourt, the track's end
RESERVED = [(5, 46, 13, 54), (15, 0, 20, 13), (27, 36, 32, 39), (48, 42, 65, 46), (50, 36, 52, 50)] + \
           [(x - 1, y - 3, x + 2, y + 4) for x, y, _ in STAIRS.values()]
SOFT = {0x2ef, 0x2f6, 0x308, 0x30a, 0x290}      # weeds, slabs, mushrooms: walked over

def walkable(M):
    ok = np.zeros((H, W), bool)
    for y in range(H):
        for x in range(W):
            u = M.used[y, x]
            if u is None or u == 'stairs' or u == 'road' or u.startswith('soft'): ok[y, x] = True
    return ok

def connected(M, blocked=()):
    """Every key spot reachable from the track's end on foot (levels change only on the stairs)."""
    ok = walkable(M); E = M.E
    for x, y in blocked: ok[y, x] = False
    start = KEY['from Route 11']; seen = {start}; todo = [start]
    while todo:
        x, y = todo.pop()
        st = M.used[y, x] == 'stairs'
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            xx, yy = x + dx, y + dy
            if not (0 <= xx < W and 0 <= yy < H) or (xx, yy) in seen or not ok[yy, xx]: continue
            st2 = M.used[yy, xx] == 'stairs'
            if st or st2:
                if dx: continue                                   # stairs are climbed straight up or down
            elif E[yy, xx] != E[y, x]: continue
            seen.add((xx, yy)); todo.append((xx, yy))
    return [k for k, p in KEY.items() if p not in seen]

def reserved(x0, y0, w, h):
    return any(not (x0 + w - 1 < a or x0 > c or y0 + h - 1 < b or y0 > d) for a, b, c, d in RESERVED)

def scatter(M, n, w, h, place, rng, tries=4000, levels=None, minfield=2, keep=True):
    done = 0
    for _ in range(tries):
        if done >= n: break
        x = int(rng.integers(0, W - w)); y = int(rng.integers(5, H - 5 - h))
        if reserved(x, y, w, h) or not M.free(x, y, w, h): continue
        if M.field[y:y + h + 1, x:x + w + 1].min() < TOP: continue
        lv = M.E[y:y + h, x:x + w]
        if lv.min() != lv.max() or (levels is not None and lv.min() not in levels): continue
        snap = (M.used.copy(), [[list(c) for c in r] for r in M.over])
        place(M, x, y)
        if keep and connected(M):                                 # it would cut a key spot off: undo
            M.used, M.over = snap; continue
        done += 1
    return done

def near(M, fn, w, pts, r=3):
    """Each tree at its spot or the nearest free one (within r), clear of the reserved ways."""
    for x, y in pts:
        best = None
        for d in range(r + 1):
            for dx in range(-d, d + 1):
                for dy in range(-d, d + 1):
                    if best is None and max(abs(dx), abs(dy)) == d and M.free(x + dx, y + dy, w, 3) \
                            and not reserved(x + dx, y + dy, w, 3):
                        best = (x + dx, y + dy)
        if best: fn(M, *best)
        else: print('no room for', fn.__name__, 'near', x, y)

def compose(seed=5):
    M = Map(); M.field = shade_field()
    rng = np.random.default_rng(seed)
    # --- stairs and the door (cut into the south faces)
    for name, (x0, y0, side) in STAIRS.items():
        for i in range(2):
            for b in range(2):
                want = 0x2f1 if side == 'S' else 0x2e1
                assert M.face.get((x0 + i, y0 + b)) == want, ('stairs not on a straight edge', name, x0 + i, y0 + b)
                # the landing on the high side: the top row on a south face, the bottom row (flipped) on a north edge
                M.face[x0 + i, y0 + b] = (0x339 if b == 0 else 0x338) if side == 'S' else (0x338 if b == 0 else -0x339)
                M.used[y0 + b, x0 + i] = 'stairs'
    for i, v in enumerate((0x2ed, 0x2ee)):
        assert M.face.get((DOOR[0] + i, DOOR[1])) == 0x2f1, ('door', DOOR)
        M.face[DOOR[0] + i, DOOR[1]] = v; M.used[DOOR[1], DOOR[0] + i] = 'door'
    # vines on some south faces (Odyssey's own variants of 2f1)
    for (x, y), v in list(M.face.items()):
        if v == 0x2f1 and rng.random() < 0.12: M.face[x, y] = int(rng.choice([0x2df, 0x2e7]))
    # --- Route 11's dirt track carries on from the east edge and ends in the woods floor
    for x in range(52, SEAM):
        for dy, v in enumerate((0x2c0, 0x2c8, 0x2d0) if x == 52 else (0x2c1, 0x7e, 0x2d1)):
            M.lay(x, ROAD + dy, 'c31', v, 'road')
    flatten(M, 52, ROAD, SEAM - 52, 3, 0)
    # --- the woods round the edge
    # east: Route 11's own woods (Crown's), as its west end has them (its rows shifted by OFF), then, westward,
    # Crown's woods and Odyssey's pines mixing before the pines take over
    # (column 57 is the first column of Route 11's own westmost woods, the rest of it in the seam: untinted, its
    # rows as Route 11 has them, so the trees are whole)
    crown_woods(M, [(57, 0, 15 + OFF)], 'north'); crown_woods(M, [(57, 24 + OFF, H - 1)], 'south')
    crown_woods(M, [(54, 0, 34)], 'north', 0.35, k=1); crown_woods(M, [(54, 50, H - 1)], 'south', 0.35, k=1)
    pine_column(M, 52, 0, 18, 'north')
    for x0, yt in ((52, 52), (50, 55)): pine_column(M, x0, yt, H - 1, 'south')
    # west: two columns of Odyssey's pines the whole height
    pine_column(M, 0, 0, H - 1, 'wall'); pine_column(M, 2, 0, H - 1, 'wall')
    # north: pines hanging from the top, the gap for the way north to Mirroh (columns 16-19)
    for x0, yb in ((4, 22), (6, 21), (8, 22), (10, 16), (12, 14), (14, 13),     # (closing the north-west corner)
                    (20, 7), (22, 9), (24, 6), (26, 8), (28, 10),
                   (30, 13), (32, 13), (34, 6), (36, 8), (38, 7), (40, 6), (42, 7), (44, 8), (46, 10), (48, 8)):
        pine_column(M, x0, 0, yb, 'north')
    # south: pines rising from the bottom
    for x0, yt in ((4, 56), (6, 58), (8, 57), (10, 55), (12, 57), (14, 56), (16, 58), (18, 56), (20, 57), (22, 55),
                   (24, 58), (26, 51), (28, 51), (30, 55), (32, 58), (34, 56), (36, 57), (38, 55), (40, 58), (42, 56),
                   (44, 57), (46, 55), (48, 57)):
        pine_column(M, x0, yt, H - 1, 'south')
    # the west strip's edge, ragged: free-standing stacks of pines
    pine_column(M, 4, 36, 40, 'stack')
    # the forest floor closes off into sections where the woods meet the hill's cliffs: from one section to the
    # next the way is always up into the hill (west, north, east and south)
    for x0, yt, yb in ((50, 26, 34), (52, 25, 35)):
        pine_column(M, x0, yt, yb, 'stack')
    # --- the void pits, red eyes watching
    # --- burrow mouths (scenery now; secrets later): Odyssey's hollow, 314 over 31c
    for x, y in ((7, 30), (27, 16), (44, 24), (36, 38), (19, 36), (16, 52), (14, 42), (44, 39)):
        try: thing(M, x, y, [[0x314], [0x31c]], 'thing:burrow')
        except AssertionError: print('no room for a burrow at', x, y)
    # --- the knoll's forecourt: broken slabs before the door
    for x, y, v in ((29, 36, 0x308), (30, 36, 0x30a), (29, 38, 0x30a), (31, 37, 0x308)):
        M.lay(x, y, 'ody', v, 'soft:slab')
    # --- the east, between Route 11's woods and the haunted floor: a Crown broadleaf, then Odyssey's pines
    near(M, broad, 3, [(53, 37)]) if False else None
    # the knoll's top: one dead tree, rocks (out of reach until late in the game)
    thing(M, 29, 29, [[0x2a0], [0x2a8]], 'thing:dead'); thing(M, 27, 30, 0x2fe, 'thing:rock'); thing(M, 31, 31, 0x2fe, 'thing:rock')
    # --- trees, dead trees, stumps, logs, rocks, mushrooms, weeds: scattered, never cut, stacked or touching a cliff,
    # and never closing the way between the key spots
    near(M, pine, 2, [(51, 39), (52, 48), (50, 16)])    # Odyssey's pines in the mixed band

    # tall grass (the wild Pokemon's): Odyssey's dark tufts, in patches
    for x0, y0, x1, y1 in ((5, 25, 8, 29), (12, 37, 15, 40), (38, 52, 42, 54), (22, 52, 26, 54), (43, 18, 46, 20),
                           (24, 16, 28, 17), (36, 33, 38, 36), (20, 22, 22, 25), (46, 34, 47, 38)):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if M.used[y, x] is None and M.E[y, x] == M.E[y0, x0]: M.lay(x, y, 'ody', 0x2b8, 'soft:grass')
    n = scatter(M, 26, 2, 3, lambda M, x, y: pine(M, x, y, check=False), rng)
    n2 = scatter(M, 9, 1, 2, lambda M, x, y: thing(M, x, y, [[0x2a0], [0x2a8]], 'thing:dead'), rng)
    n3 = scatter(M, 7, 1, 1, lambda M, x, y: thing(M, x, y, 0x288, 'thing:stump'), rng)
    n4 = scatter(M, 3, 3, 1, lambda M, x, y: thing(M, x, y, [[0x299, 0x29a, 0x29b]], 'thing:log'), rng)
    n5 = scatter(M, 8, 1, 1, lambda M, x, y: thing(M, x, y, 0x2fe, 'thing:rock'), rng)
    n6 = scatter(M, 10, 1, 1, lambda M, x, y: M.lay(x, y, 'ody', 0x290, 'soft:mush'), rng, keep=False)
    n7 = scatter(M, 12, 1, 1, lambda M, x, y: M.lay(x, y, 'ody', int(rng.choice([0x2ef, 0x2f6])), 'soft:weed'), rng, keep=False)
    # the clearing: a ring of stumps and a fallen log, open in the middle (the Eiscue, the cultists' 1v2)
    for x, y, ids in ((6, 47, 0x288), (12, 48, 0x288), (7, 53, [[0x299, 0x29a, 0x29b]]), (12, 53, 0x2fe)):
        thing(M, x, y, ids)
    print('placed pines %d dead %d stumps %d logs %d rocks %d mush %d weeds %d' % (n, n2, n3, n4, n5, n6, n7))
    settle(M)
    miss = connected(M)
    assert not miss, ('cut off', miss)
    # the hill is the only way between the sections: with ring 2's stairs closed the north is out of reach
    ring2 = [(x + i, y + b) for n, (x, y, _) in STAIRS.items() if n.startswith('ring 2') for i in range(2) for b in range(2)]
    assert 'to Mirroh' in connected(M, ring2), 'the north can be reached without crossing ring 2'
    ring1 = [(x + i, y + b) for n, (x, y, _) in STAIRS.items() if n.startswith('ring 1') for i in range(2) for b in range(2)]
    assert set(connected(M, ring1)) >= {'clearing', 'to Mirroh', 'north-east woods'}, 'the woods join round the hill'
    return M

# ------------------------------------------------------------------ output
def route11_strip():
    ts = RL.TS('LAYOUT_ROUTE11')
    import struct
    d = open(os.path.join(RL.ROOT if hasattr(RL, 'ROOT') else '/home/claude/repo/codebase', 'data/layouts/Route11/map.bin'), 'rb').read()
    v = struct.unpack('<%dH' % (90 * 40), d)
    out = np.zeros((H * 16, 8 * 16, 3), np.uint8)
    for y in range(H):
        ry = y - OFF
        for x in range(8):
            m = v[ry * 90 + x] & 0x3ff if 0 <= ry < 40 else v[(ry % 2) * 90 + x] & 0x3ff
            out[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = np.asarray(ts.metatile(m), np.uint8)
    return out

def fog(img, seed=3, amount=0.42):
    rng = np.random.default_rng(seed); h, w = img.shape[:2]
    def smooth(cell):
        g = rng.random((h // cell + 2, w // cell + 2))
        return np.array(Image.fromarray((g * 255).astype(np.uint8)).resize((g.shape[1] * cell, g.shape[0] * cell), Image.BICUBIC))[:h, :w] / 255.0
    n = smooth(96) * 0.6 + smooth(40) * 0.4
    n = np.clip((n - 0.25) * 1.6, 0, 1)[..., None] * amount
    fogc = np.array([170, 182, 196], float)
    return (img * (1 - n) + fogc * n).astype(np.uint8)

LABELS = [((17, 6), 'north to Mirroh (Glaive)'), ((8, 50), 'clearing: Eiscue, the 1v2'), ((59, 47), 'from Route 11'),
          ((29, 37), 'sealed door'), ((29, 27), 'knoll top (late game)'), ((7, 17), 'trees close the way'),
          ((51, 30), 'trees close the way'), ((31, 6), 'trees close the way'), ((27, 54), 'trees close the way'),
          ((46, 11), 'north-east woods'), ((6, 32), 'west woods')] + \
         [((x, y), 'stairs') for x, y, _ in STAIRS.values()]

def annotate(img, scale=2):
    im = Image.fromarray(img).resize((img.shape[1] * scale, img.shape[0] * scale), 0); d = ImageDraw.Draw(im)
    for (x, y), t in LABELS:
        px, py = x * 16 * scale + 8 * scale, y * 16 * scale + 8 * scale
        d.ellipse([px - 7, py - 7, px + 7, py + 7], outline=(255, 230, 80), width=3)
        tw = len(t) * 6 + 8
        d.rectangle([px + 10, py - 8, px + 10 + tw, py + 8], fill=(20, 20, 30))
        d.text((px + 14, py - 6), t, fill=(255, 230, 80))
    return im

# ------------------------------------------------------------------ the unsettling touches
# blood: dark red stains running down the cliffs from their tops (drawn on the faces only)
BLOOD = [(70, 10, 18), (104, 18, 26), (140, 30, 36)]

def blood(M, img, seed=13, n=22):
    """Stains as a few patterns, each used again and again (the game's tiles repeat): drips that start at a cliff's
    top and run down two bands of a south face (four patterns) or of a lit west face (two), blots soaked into a face
    (two), and smears round the sealed door."""
    rng = np.random.default_rng(seed)
    def drips(face, k):
        """A 16x32 pattern of drips over two cells of one face (its own stone left where no blood is)."""
        r = np.random.default_rng(100 + k + (50 if face == 0x2e8 else 0))
        base = np.concatenate([ody(face), ody(face)], 0).copy()
        stone = np.ones((32, 16), bool)
        for _ in range(int(r.integers(1, 3))):
            px = int(r.integers(3, 13)); py = int(r.integers(0, 3))
            base[py:py + 2, px - 1:px + 2] = BLOOD[1]; base[py, px] = BLOOD[2]
            for d in range(int(r.integers(1, 3))):
                dx = min(14, max(1, px + int(r.integers(-2, 3)))); L = int(r.integers(8, 28)); w = 2 if r.random() < 0.3 else 1
                for j in range(L):
                    yy = py + j
                    if yy >= 31: break
                    base[yy, dx:dx + w] = BLOOD[2] if j < 2 else BLOOD[1] if j < L - 3 else BLOOD[0]
                base[min(31, py + L), dx - 1:dx + w + 1] = BLOOD[0]
        return base
    def blot(face, k):
        r = np.random.default_rng(200 + k); c = ody(face).copy(); cx, cy = int(r.integers(5, 11)), int(r.integers(5, 11))
        rad = r.uniform(2.2, 3.4)
        for yy in range(16):
            for xx in range(16):
                d = ((xx - cx) ** 2 + (yy - cy) ** 2) ** 0.5 + r.uniform(-0.8, 0.8)
                if d < rad: c[yy, xx] = BLOOD[0] if d > rad - 1.2 else BLOOD[1]
        return c
    PAT = {0x2f1: [drips(0x2f1, k) for k in range(4)], 0x2e8: [drips(0x2e8, k) for k in range(2)]}
    BLOT = {0x2f1: [blot(0x2f1, k) for k in range(2)], 0x2e8: [blot(0x2e8, k + 2) for k in range(1)]}
    sites = [(x, y) for (x, y), v in M.face.items() if v in (0x2f1, 0x2e8) and M.face.get((x, y + 1)) == v
             and M.face.get((x, y - 1)) not in (0x2f1, 0x2e8, 0x2df, 0x2e7)]
    sites = [sites[i] for i in rng.permutation(len(sites))]
    used = set()
    for x, y in sites[:n]:
        if (x - 1, y) in used or (x + 1, y) in used: continue          # (never two side by side: no fence of drips)
        v = M.face[x, y]; p = PAT[v][int(rng.integers(0, len(PAT[v])))]
        img[y * 16:y * 16 + 32, x * 16:x * 16 + 16] = p; used.add((x, y))
    cells = [(x, y) for (x, y), v in M.face.items() if v in BLOT and (x, y) not in used and (x, y - 1) not in used]
    for i in rng.permutation(len(cells))[:10]:
        x, y = cells[i]; v = M.face[x, y]
        img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = BLOT[v][int(rng.integers(0, len(BLOT[v])))]
    # the sealed door: a dark stain spread under it and smeared up its frame
    dx0, dy0 = DOOR[0] * 16, DOOR[1] * 16
    for x in range(dx0 - 4, dx0 + 36):
        for yy in range(dy0 - 6, dy0 + 2):
            if rng.random() < 0.18 and M.face.get((x // 16, yy // 16)) in (0x2f1, 0x2df, 0x2e7): img[yy, x] = BLOOD[int(rng.integers(0, 2))]
    return img

# webs (user 2026-11-20): the Webbed Woods' own webbing (MonoMyth), as MonoMyth hangs it, blood red. It lives in the
# trees: on a webbed tree a fan of web at each side of its crown and a drape sagging under it; trees side by side
# share a fan in the V between them; a zig-zag strand crosses an open gap from one webbed tree to the next; a big
# sagging net closes a narrow path between two webbed trees. Webbing comes in patches (whole stretches of woods), not
# on every tree. Layers cut from MonoMyth's webbed trees (its map 0x886DD40: cells 236 234 237 / 21e 22c 21f, the
# shared fans 235 233 / 21d 21b, the strand 279 277 275 26e 26f / 27a 278 272 273 274), keyed out by the two web
# colours: assets/monomyth_reference/pieces/webtree_*.png; the net: web_net.png (0x886DD5C).
WEB_DIR = os.path.join(HERE, '..', '..', '..', 'assets', 'monomyth_reference', 'pieces')
WEB_RED = {(240, 240, 248): (146, 30, 36), (200, 216, 232): (92, 16, 24)}          # (old blood, not paint)
def web(name):
    im = np.array(Image.open(os.path.join(WEB_DIR, name + '.png')).convert('RGBA'))
    for a, b in WEB_RED.items(): im[(im[..., :3] == a).all(-1), :3] = b
    im[im[..., 3] == 0] = 0
    return im

# Hung across the trees (user 2026-11-20: a web on each tree looked strange; hang them across more of the trees,
# more naturally): sheets of web sag from tree to tree along the woods' edges, a few threads deep with MonoMyth's
# zig-zag lace between them and torn threads trailing from their lower edge; the big net closes the narrow way north;
# round orb webs, some torn, in the corners where the woods meet the cliffs. Drawn a pixel at a time in the webbing's
# two colours (MonoMyth's, made old-blood red), so they read as the same webbing.
WEB_LIGHT, WEB_DARK = (140, 30, 36), (104, 18, 26)    # (the blood's own reds)
NETS = [(16, 4, 5)]                   # (gap's first cell x, width, tree row): the big net across the way north

def _line(layer, a, b, c):
    (x0, y0), (x1, y1) = (int(round(a[0])), int(round(a[1]))), (int(round(b[0])), int(round(b[1])))
    dx, dy = abs(x1 - x0), -abs(y1 - y0); sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1); err = dx + dy
    while True:
        if 0 <= y0 < layer.shape[0] and 0 <= x0 < layer.shape[1]: layer[y0, x0] = (*c, 255)
        if x0 == x1 and y0 == y1: break
        e2 = 2 * err
        if e2 >= dy: err += dy; x0 += sx
        if e2 <= dx: err += dx; y0 += sy

def sheet(layer, A, B, rng, depth=3, sag=None, bulge=(0, 1)):
    """Threads sagging from A to B (pixels), one under another, laced by zig-zags; torn ends trailing below."""
    L = ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** 0.5
    sag = sag if sag is not None else 3 + L * 0.16
    n = max(4, int(L / 3))
    rows = []
    for i in range(depth):
        bx, by = bulge                                           # the way the web sags (down; out from a woods' side)
        a = (A[0] + bx * i * 2, A[1] + by * i * 2); b = (B[0] + bx * i * 2, B[1] + by * i * 2); sg = sag + i * 3.5
        pts = [(a[0] + (b[0] - a[0]) * t + bx * sg * 4 * t * (1 - t), a[1] + (b[1] - a[1]) * t + by * sg * 4 * t * (1 - t))
               for t in np.linspace(0, 1, n + 1)]
        rows.append(pts)
        for p, q in zip(pts, pts[1:]): _line(layer, p, q, WEB_LIGHT if i == 0 else WEB_DARK)
    for i in range(depth - 1):                                   # the lace: zig-zags between one thread and the next
        for k in range(1, n):
            j = k + (1 if (k + i) % 2 else -1)
            if 0 < j < n: _line(layer, rows[i][k], rows[i + 1][j], WEB_DARK)
    for k in rng.choice(np.arange(2, n - 1), size=min(3, max(0, n - 3)), replace=False) if n > 4 else []:
        x, y = rows[-1][k]; _line(layer, (x, y), (x + bulge[0] * rng.integers(2, 6) + rng.integers(-1, 2), y + rng.integers(3, 8)), WEB_DARK)

def orb(layer, C, R, anchors, rng, torn=0.25):
    """A round web: spokes to its anchors and out, a spiral, broken in places."""
    spokes = [np.arctan2(ay - C[1], ax - C[0]) for ax, ay in anchors] + list(np.linspace(0, 2 * np.pi, 9)[:-1] + 0.2)
    for ax, ay in anchors: _line(layer, C, (ax, ay), WEB_LIGHT)
    for t in spokes: _line(layer, C, (C[0] + R * np.cos(t), C[1] + R * np.sin(t)), WEB_LIGHT)
    ang = sorted(t % (2 * np.pi) for t in spokes)
    for r in np.arange(4, R, 3.2):
        for t0, t1 in zip(ang, ang[1:] + [ang[0] + 2 * np.pi]):
            if rng.random() < torn: continue
            _line(layer, (C[0] + r * np.cos(t0), C[1] + r * np.sin(t0)), (C[0] + r * np.cos(t1), C[1] + r * np.sin(t1)), WEB_DARK)

_TPL = {}
def _template(kind, *key):
    """A web drawn once on its own small canvas and stamped wherever its shape recurs (the same tiles each time)."""
    k = (kind,) + key
    if k in _TPL: return _TPL[k]
    import zlib; rng = np.random.default_rng(zlib.crc32(repr(k).encode()))       # (a fixed seed: the same webs every build)
    if kind == 'garland':                                 # from one pine's crown side to another's, L cells on, dt rows
        L, dt = key; rows = abs(dt) + 2
        c = np.zeros((rows * 16, L * 16, 4), np.uint8)
        ya = 8 + (dt < 0) * abs(dt) * 16; yb = 8 + (dt > 0) * dt * 16
        sheet(c, (10, ya), (L * 16 - 10, yb), rng, depth=2, sag=min(8, 2 + L * 1.6))
    elif kind == 'side':                                  # down a woods' side, from one pine to the next (two rows on)
        side, = key; c = np.zeros((48, 32, 4), np.uint8)
        x = 14 if side > 0 else 18
        sheet(c, (x, 8), (x, 40), rng, depth=2, sag=6, bulge=(side, 0.3))
    _TPL[k] = c; return c

GARLANDS = {(2, 0), (2, 1), (2, -1), (2, 2), (2, -2), (4, 0)}

def hang_webs(M, img, seed=4):
    rng = np.random.default_rng(seed)
    layer = np.zeros(img.shape[:2] + (4,), np.uint8)
    def stamp(t, cx, cy):
        h, w = t.shape[:2]; sl = layer[cy * 16:cy * 16 + h, cx * 16:cx * 16 + w]
        m = t[..., 3] > 0; sl[m] = t[m]
    units = set(M.units)
    alone = sorted({tuple(map(int, u[len('tree:pine'):].split(','))) for u in M.used.ravel()
                    if isinstance(u, str) and u.startswith('tree:pine')})
    def north(x0): return max(t for x, t in units if x == x0 and t < 30)
    def south(x0): return min(t for x, t in units if x == x0 and t > 40)
    def garland(a, b):
        (xa, ta), (xb, tb) = a, b
        L, dt = xb - xa, tb - ta
        if (L, dt) not in GARLANDS: return                # (only the shapes that recur: the tileset has room for few)
        stamp(_template('garland', L, dt), xa + 1, min(ta, tb) + 1)
    def line(us):
        """Along a woods' edge: each pine to the next one along (or the one after) if it hangs at the same height
        or one tree's step (two rows) above or below."""
        for i, a in enumerate(us):
            for b in us[i + 1:i + 3]:
                if abs(b[1] - a[1]) <= 2: garland(a, b); break
    line([(x, north(x)) for x in (4, 6, 8, 10, 12, 14)])                 # the woods' edge west of the way north
    line([(x, north(x)) for x in (20, 22, 24, 26, 28)])                  # and east of it, over the dead tree (user)
    line([(x, north(x)) for x in range(34, 50, 2)])                      # the north-east woods
    line([(x, south(x)) for x in range(4, 26, 2)])                       # the treeline along the south
    line([(x, south(x)) for x in range(30, 52, 2) if any(u[0] == x and u[1] > 40 for u in units)])
    # pines standing near each other or near a woods' edge, crowns level: webbed together
    edge = [u for u in units if M.used[u[1] + 1, u[0]] == 'woods']
    for a in alone:
        for b in alone + edge:
            if b[1] == a[1] and 3 <= b[0] - a[0] <= 6: garland(a, b)
        for e in edge:
            if e[1] == a[1] and 3 <= a[0] - e[0] <= 6: garland(e, a)
    # down the west woods' side and the trees closing the way east, from tree to tree, in stretches
    wall = sorted(t for x, t in units if x == 2 and 22 <= t <= 52)
    for t0, t1 in zip(wall, wall[1:]):
        if (t0 // 2) % 3 and t1 - t0 == 2: stamp(_template('side', 1), 3, t0 + 1)
    st = sorted(t for x, t in units if x == 50 and 24 <= t <= 36)
    for t0, t1 in zip(st, st[1:]):
        if t1 - t0 == 2: stamp(_template('side', -1), 49, t0 + 1)
    # small round webs: in the dead tree's branches under the woods' edge (user), in the V where the two columns
    # closing the way south meet
    orb(layer, (23 * 16 + 9, 11 * 16 + 9), 9, [(23 * 16 + 3, 11 * 16 + 2), (23 * 16 + 14, 11 * 16 + 4)], rng, torn=0.3)
    orb(layer, (28 * 16, 52 * 16 + 2), 11, [(27 * 16 + 4, 51 * 16 + 6), (28 * 16 + 12, 51 * 16 + 6)], rng)
    out = Image.fromarray(layer)
    for gx, w, row in NETS:
        net = Image.open(os.path.join(HERE, '..', '..', '..', 'assets', 'monomyth_reference', 'pieces', 'web_net.png')).convert('RGBA')
        a = np.array(net); m = a[..., 3] > 0
        light = (a[..., :3] == (240, 240, 248)).all(-1)
        a[m & light, :3] = WEB_LIGHT; a[m & ~light, :3] = WEB_DARK
        out.alpha_composite(Image.fromarray(a), (gx * 16 + (w * 16 - a.shape[1]) // 2, row * 16 + 2))
    return np.array(out)                                   # (RGBA: the webs, drawn over everything, walked under)

def layers(M):
    """The whole map as the game draws it: under (the ground, cliffs, everything the player stands in front of, the
    blood) and over (tree crowns, the webs: drawn over the player), with the over layer's mask. Seam cells left black."""
    U = np.zeros((H * 16, W * 16, 3), np.uint8); O = np.zeros_like(U); OM = np.zeros((H * 16, W * 16), bool)
    for y in range(H):
        for x in range(W):
            if (x, y) in M.seam: continue
            c = M.cell.__func__(M, x, y) if False else None
            if (x, y) in M.face:
                v = M.face[x, y]; img = ody(abs(v)).copy()
                if v < 0: img = img[::-1].copy()
            elif M.ground[y][x] is not None: img = M.ground[y][x].copy()
            else:
                f = M.field; img = ground_cell((f[y, x], f[y, x + 1], f[y + 1, x], f[y + 1, x + 1]))
            ov = np.zeros_like(img); om = np.zeros((16, 16), bool)
            for o, top in M.over[y][x]:
                m = o[..., 3] > 0
                if top: ov[m] = o[..., :3][m]; om |= m
                else: img[m] = o[..., :3][m]
            U[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = img
            O[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = ov; OM[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = om
    U = blood(M, U)
    webs = hang_webs(M, U)
    wm = webs[..., 3] > 0
    for y in range(H):                                     # (no web over the seam: Route 11's own cells)
        for x in range(SEAM, W): wm[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = False
    O[wm] = webs[..., :3][wm]; OM |= wm
    return U, O, OM

def flat(M, U, O, OM):
    img = U.copy(); img[OM] = O[OM]
    for (x, y), v in M.seam.items(): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = r11_img(v & 0x3FF)
    return img

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    M = compose(); img = flat(M, *layers(M))
    strip = route11_strip()
    strip[:, :1] = (255, 64, 64)                       # the seam (Route 11 to the right)
    full = np.concatenate([img, strip], 1)
    fogged = np.concatenate([fog(img), strip], 1)
    Image.fromarray(full).save(os.path.join(outdir, 'hollow_hill_mock.png'))
    Image.fromarray(full).resize((full.shape[1] * 2, full.shape[0] * 2), 0).save(os.path.join(outdir, 'hollow_hill_mock_2x.png'))
    Image.fromarray(fogged).save(os.path.join(outdir, 'hollow_hill_mock_fog.png'))
    annotate(full).save(os.path.join(outdir, 'hollow_hill_mock_labels.png'))
    print(outdir)
    return M

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/hollowhill')
