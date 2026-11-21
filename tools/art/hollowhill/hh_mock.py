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

# ------------------------------------------------------------------ pieces
def ody(m): return kit.atlas('ody_0_97')['full'][m]
TEAL_GRASS = {(32, 96, 96), (48, 128, 128), (32, 88, 88)}
OLIVE_GRASS = set(kit.OLIVE4) | {(104, 160, 88)}
SRC = {'ody': (ody, TEAL_GRASS), 'c325': (lambda m: kit.atlas('crown325')['full'][m], OLIVE_GRASS),
       'c31': (lambda m: kit.atlas('crown31')['full'][m], {(112, 184, 136), (128, 192, 136), (144, 200, 152), (80, 160, 112)})}

def overlay(src, m, keep_grass=False):
    f, grass = SRC[src]; img = f(m).copy()
    key = [tuple(p) for p in img.reshape(-1, 3).tolist()]
    a = np.array([255 if keep_grass or k not in grass else 0 for k in key], np.uint8).reshape(16, 16)
    out = np.zeros((16, 16, 4), np.uint8); out[..., :3] = img; out[..., 3] = a
    return out

# ------------------------------------------------------------------ the four grounds, olive (Route 11) to teal
def _recolour(img, pairs):
    out = img.copy(); flat = out.reshape(-1, 3)
    for a, b in pairs: flat[(flat == a).all(1)] = b
    return out
TEAL = ody(0x2e9).copy()
def _teal(base, blade, dark): return _recolour(TEAL, [((32, 96, 96), base), ((48, 128, 128), blade), ((32, 88, 88), dark)])
GROUNDS = [kit.plain(3),                                                                           # Route 11's olive
           _recolour(kit.plain(3), zip(kit.OLIVE, [(72, 126, 66), (86, 138, 76), (98, 150, 86)])),
           _recolour(kit.plain(3), zip(kit.OLIVE, [(62, 116, 72), (74, 126, 80), (86, 138, 90)])),
           _teal((52, 110, 84), (70, 136, 104), (48, 102, 80)),
           _teal((42, 104, 90), (58, 132, 116), (38, 96, 86)),
           TEAL]                                                                                    # Odyssey's teal
RIM = [(80, 136, 64), (72, 126, 66), (62, 116, 72), (48, 102, 80), (38, 96, 86), (32, 88, 88)]
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
class Map:
    def __init__(self):
        self.field = None
        self.lock = np.zeros((H + 1, W + 1), bool)
        self.E, self.P = rings()
        self.face = {}                                     # (x, y) -> Odyssey metatile (terraces, stairs, door)
        self.over = [[[] for _ in range(W)] for _ in range(H)]
        self.used = np.full((H, W), None, object)
        self.ground = [[None] * W for _ in range(H)]       # an RGB image replacing the grass, or None
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
    s = np.interp(x, [0, 50, 52, 54, 56, 58, 60, 62, 64, 66], [5, 5, 4.5, 3.8, 3, 2.2, 1.4, 0.7, 0, 0]) + n * 3 * np.interp(x, [0, 50, 53, 61, 64], [0, 0, 1, 1, 0])
    v = np.clip(np.rint(s), 0, TOP).astype(int); v = np.broadcast_to(v, (H + 1, W + 1)).copy()
    v[:, 64:] = 0; v[:, :51] = TOP
    for _ in range(8):
        bad = False
        for yy in range(H):
            for xx in range(W):
                q = v[yy:yy + 2, xx:xx + 2]
                if q.max() - q.min() > 1: bad = True; q[q == q.max()] -= 1
        if not bad: break
    return v

def tint(rgb, t, to=(36, 92, 92)):
    """Crown's greens drawn toward the haunted teal (its trees darkening as the woods change)."""
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

def pine_column(M, x0, yt, yb, kind):
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
                if not 0 <= x < W: continue
                v = CROWN_WOODS_N(yb, y, k) if kind == 'north' else CROWN_WOODS_S(yt, y, k)
                M.lay(x, y, 'c325', v, 'woods', top=kind == 'south' and y == yt)
                if t: o = M.over[y][x][-1][0]; o[..., :3] = tint(o[..., :3], t)
        flatten(M, x0, yt, 3, yb - yt + 1, k if k is not None else min(1, int(M.field[yt:yb + 2, x0:x0 + 4].min())))

def broad(M, x, y):
    assert M.free(x, y, 3, 3), ('broad', x, y)
    k = min(3, int(np.bincount(M.field[y:y + 4, x:x + 4].ravel()).argmax())); flatten(M, x, y, 3, 3, k)
    for dy, row in enumerate(((0xb, 0xc, 0xd), (0x13, 0x14, 0x15), (0x1b, 0x1c, 0x1d))):
        for dx, v in enumerate(row):
            M.lay(x + dx, y + dy, 'c325', v, f'tree:broad{x},{y}', top=dy == 0)
            if k: o = M.over[y + dy][x + dx][-1][0]; o[..., :3] = tint(o[..., :3], 0.13 * k)

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
    for x in range(57, W):
        for dy, v in enumerate((0x2c0, 0x2c8, 0x2d0) if x == 57 else (0x2c1, 0x7e, 0x2d1)):
            M.lay(x, ROAD + dy, 'c31', v, 'road')
    flatten(M, 57, ROAD, W - 57, 3, 0)
    # --- the woods round the edge
    # east: Route 11's own woods (Crown's), as its west end has them (its rows shifted by OFF), then, westward,
    # Crown's woods and Odyssey's pines mixing before the pines take over
    crown_woods(M, [(63, 0, 15 + OFF)], 'north'); crown_woods(M, [(63, 24 + OFF, H - 1)], 'south')
    crown_woods(M, [(60, 0, 25)], 'north', 0.18); crown_woods(M, [(60, 50, H - 1)], 'south', 0.18)
    crown_woods(M, [(57, 0, 30)], 'north', 0.3); crown_woods(M, [(57, 53, H - 1)], 'south', 0.34)
    crown_woods(M, [(54, 0, 34)], 'north', 0.42, k=2)
    pine_column(M, 52, 0, 18, 'north')
    for x0, yt in ((55, 52), (53, 55), (50, 55)): pine_column(M, x0, yt, H - 1, 'south')
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
    near(M, broad, 3, [(56, 37), (59, 49), (61, 30)])
    # the knoll's top: one dead tree, rocks (out of reach until late in the game)
    thing(M, 29, 29, [[0x2a0], [0x2a8]], 'thing:dead'); thing(M, 27, 30, 0x2fe, 'thing:rock'); thing(M, 31, 31, 0x2fe, 'thing:rock')
    # --- trees, dead trees, stumps, logs, rocks, mushrooms, weeds: scattered, never cut, stacked or touching a cliff,
    # and never closing the way between the key spots
    near(M, pine, 2, [(53, 39), (54, 48), (50, 16)])    # Odyssey's pines in the mixed band
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
    fogc = np.array([196, 210, 214], float)
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

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    M = compose(); img = M.render()
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
