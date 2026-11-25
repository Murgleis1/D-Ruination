"""Route 11 mock, revision 2 (90x30; the layout is tools/art/route11/layout_sketch.py main_v3, approved by the user
2026-11-20 with the river's way down past the beach to be refined).

West from Pelluca's west road to the woods that open into Hollow Hill. Every cell is a ground (the grass of its
shade, sand, or the sea) with pieces laid over it, each piece's own grass left out so the ground shows through:
  - the grass shades from Pelluca's mint to the woods' olive by a smooth field (kit.py), with Crown's patch edges
    wherever two shades meet, so the ground darkens gradually and in patches, never along a straight line;
  - trees are whole units only (a Pelluca pine 2x3, a Crown broadleaf 3x3, Crown's woods as columns three cells wide),
    every placement checked against everything already there, so nothing is cut or stacked;
  - the gorge is MonoMyth's kit (its Route 7 family: ledges, slopes, faces, falls, pools, the bridge) in MonoMyth's own
    grammar: the river comes in off the north edge, drops in three falls through a chasm, passes under the bridge,
    falls a last time over the coastal cliff and crosses the beach to the sea. The cove's walls close the beach.
  - the farm is Crown's cottage, fences and flowers with Odyssey's cabbages, sown field and hay.
Pelluca's own columns run along the east edge (columns 82-89, Pelluca's 0-7 on rows 14-43), Cormoria only.
Usage: python3 tools/art/route11/route11_v2.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kit
from kit import RL

# The approved picture is 90x30; in the game it gets five rows of woods (and sea, and the chasm) above and below,
# out of the player's reach, so the camera never shows past the map's edge. OY shifts the picture's rows down.
OY, PB = 5, 5
W, H = 90, 30 + OY + PB
ROAD = 14 + OY                 # the road's three rows (Pelluca's rows 28-30: the connection offset is ROAD - 28)
PEL = 28 - ROAD                # Pelluca's row = Route 11's row + PEL
SEAM = 82                      # columns 82-89 are Pelluca's own

# ------------------------------------------------------------------ sources and their grass (left out of the pieces)
GRASS = {'mm': {(144, 208, 152), (160, 216, 152), (136, 200, 152)},
         'c31': {(112, 184, 136), (128, 192, 136), (144, 200, 152), (80, 160, 112)},
         'c325': set(kit.OLIVE4) | {(104, 160, 88)},
         'ody': {(80, 184, 152), (112, 200, 160), (136, 216, 184), (184, 224, 160), (96, 184, 144)},
         'cor': set(kit.MINT)}
ATL = {'mm': 'mm_route7', 'c31': 'crown31', 'c325': 'crown325', 'ody': 'ody232'}

# MonoMyth's water to Pelluca's: its flat blue becomes Pelluca's water texture, its other blues darkened to match
_SEA = kit.cor_full(175)
MM_FLAT = (112, 160, 248)
MM_WATER = {(136, 184, 248): (136, 160, 240), (80, 144, 224): (96, 136, 208), (64, 136, 216): (72, 120, 216),
            (56, 112, 216): (72, 120, 176), (48, 112, 192): (72, 120, 176), (48, 96, 160): (48, 96, 176),
            (176, 208, 248): (176, 208, 248), (200, 216, 232): (208, 216, 232), (232, 240, 240): (224, 240, 248),
            (200, 224, 240): (224, 240, 248)}        # (all Pelluca's own water colours: its palette 5)

def _piece(src, mid):
    if src == 'cor': return kit.cor_full(mid)
    return kit.atlas(ATL[src])['full'][mid]

def overlay(src, mid, flip=False, clear=()):
    """A piece as RGBA: its own grass (and any colours in clear) transparent; MonoMyth's water turned to Pelluca's."""
    img = _piece(src, mid).copy()
    if flip: img = img[:, ::-1].copy()
    flat = img.reshape(-1, 3); key = [tuple(p) for p in flat.tolist()]
    gone = GRASS[src] | set(clear)
    alpha = np.array([0 if k in gone else 255 for k in key], np.uint8).reshape(16, 16)
    if src == 'mm':
        sea = _SEA.reshape(-1, 3)
        for i, k in enumerate(key):
            if k == MM_FLAT: flat[i] = sea[i]
            elif k in MM_WATER: flat[i] = MM_WATER[k]
    out = np.zeros((16, 16, 4), np.uint8).view(Piece); out[..., :3] = img; out[..., 3] = alpha
    return out

class Piece(np.ndarray):
    top = False

# ------------------------------------------------------------------ the map
class Map:
    def __init__(self):
        self.ground = [['grass'] * W for _ in range(H)]      # 'grass' | 'sand' | ('cor', id) | ('img', rgb)
        self.over = [[[] for _ in range(W)] for _ in range(H)]
        self.used = np.zeros((H, W), object)                 # what occupies each cell (None = open grass)
        self.used[:] = None
        self.field = None
        self.lock = np.zeros((H + 1, W + 1), bool)          # vertices a piece has fixed (its ground is one shade)
        self.wet = {}                                        # stream cells on the beach: (x, y) -> water (bool)

    def flatten(self, x0, y0, w, h, k, rim=True):
        """One shade under a piece (its tiles then repeat wherever it stands on that shade). rim=False: only the
        vertices inside the piece, so a shade edge may still run along its outer cells (no box round it)."""
        a = 0 if rim else 1
        self.field[y0 + a:y0 + h + 1 - a, x0 + a:x0 + w + 1 - a] = k
        self.lock[y0 + a:y0 + h + 1 - a, x0 + a:x0 + w + 1 - a] = True

    def shade_at(self, x0, y0, w, h):
        v = self.field[y0:y0 + h + 1, x0:x0 + w + 1].ravel()
        return int(np.bincount(v, minlength=4).argmax())

    def settle(self):
        """After flattening: no cell may span more than two neighbouring shades; unlocked vertices give way."""
        f, lk = self.field, self.lock
        for _ in range(12):
            bad = False
            for yy in range(H):
                for xx in range(W):
                    q = f[yy:yy + 2, xx:xx + 2]; l = lk[yy:yy + 2, xx:xx + 2]
                    if q.max() - q.min() <= 1: continue
                    bad = True
                    if l.any() and q[l].max() - q[l].min() > 1:      # two pieces' grounds meet too far apart:
                        q[q > q.min() + 1] = q.min() + 1; continue   # the darker gives way a shade
                    ref = q[l] if l.any() else np.array([q.max()])
                    hi, lo = ref.max(), ref.min()
                    q[(~l) & (q > lo + 1)] = lo + 1; q[(~l) & (q < hi - 1)] = hi - 1
            if not bad: return
        raise SystemExit('the grass field cannot settle')

    def lay(self, x, y, src, mid, what, flip=False, check=True, clear=(), top=False):
        """top: the piece is drawn over the player (a tree's crown he walks behind)."""
        if not (0 <= x < W and 0 <= y < H): return
        if check and self.used[y, x] is not None:
            raise ValueError(f'{what} at {x},{y} over {self.used[y, x]}')
        o = overlay(src, mid, flip, clear); o.top = top
        self.over[y][x].append(o); self.used[y, x] = what

    def mark(self, x, y, what):
        if self.used[y, x] is not None: raise ValueError(f'{what} at {x},{y} over {self.used[y, x]}')
        self.used[y, x] = what

    def free(self, x0, y0, w, h, margin=0, avoid=None):
        for y in range(y0 - margin, y0 + h + margin):
            for x in range(x0 - margin, x0 + w + margin):
                if not (0 <= x < W and 0 <= y < H): continue
                inside = x0 <= x < x0 + w and y0 <= y < y0 + h
                u = self.used[y, x]
                if inside and u is not None: return False
                if not inside and u is not None and (avoid is None or u.split(':')[0] in avoid): return False
        return True

    def ground_img(self, x, y):
        g = self.ground[y][x]
        if g == 'grass':
            f = self.field; return kit.grass_cell((f[y, x], f[y, x + 1], f[y + 1, x], f[y + 1, x + 1]))
        if g == 'sand': return kit.cor_full(163).copy()
        if g[0] == 'cor': return kit.cor_full(g[1]).copy()
        return g[1].copy()

    def primary(self, x, y):
        """Pelluca's own metatile id if the cell is one as it stands, else None."""
        g = self.ground[y][x]
        if g == 'grass' and not self.over[y][x]:
            f = self.field[y:y + 2, x:x + 2]
            return 6 if f.max() == 0 else None
        if isinstance(g, tuple) and g[0] == 'cor' and not self.over[y][x]: return g[1]
        return None

    def layers(self, x, y):
        """(under RGB, over RGB, over mask) of a cell."""
        img = self.ground_img(x, y); ov = np.zeros_like(img); om = np.zeros((16, 16), bool)
        for o in self.over[y][x]:
            m = o[..., 3] > 0
            if o.top: ov[m] = o[..., :3][m]; om |= m
            else: img[m] = o[..., :3][m]
        return img, ov, om

    def cell(self, x, y):
        g = self.ground[y][x]
        if g == 'grass':
            f = self.field; img = kit.grass_cell((f[y, x], f[y, x + 1], f[y + 1, x], f[y + 1, x + 1]))
        elif g == 'sand': img = kit.cor_full(163).copy()
        elif g[0] == 'cor': img = kit.cor_full(g[1]).copy()
        else: img = g[1].copy()
        for o in self.over[y][x]:
            m = o[..., 3] > 0; img[m] = o[..., :3][m]
        return img

    def render(self):
        out = np.zeros((H * 16, W * 16, 3), np.uint8)
        for y in range(H):
            for x in range(W): out[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = self.cell(x, y)
        return out

# ------------------------------------------------------------------ the grass field
def shade_field(seed=28):
    """Vertex shades 0 (mint) .. 3 (olive): a ramp west across the route, roughened by smooth noise so the shades
    meet in patches and tongues; no cell spans more than two neighbouring shades."""
    rng = np.random.default_rng(seed)
    def noise(cell):
        gh, gw = H // cell + 3, W // cell + 3
        g = rng.random((gh, gw))
        ys = np.arange(H + 1) / cell; xs = np.arange(W + 1) / cell
        y0 = ys.astype(int); x0 = xs.astype(int); fy = (ys - y0)[:, None]; fx = (xs - x0)[None, :]
        fy = fy * fy * (3 - 2 * fy); fx = fx * fx * (3 - 2 * fx)
        a = g[y0][:, x0]; b = g[y0][:, x0 + 1]; c = g[y0 + 1][:, x0]; d = g[y0 + 1][:, x0 + 1]
        return (a * (1 - fx) + b * fx) * (1 - fy) + (c * (1 - fx) + d * fx) * fy
    n = noise(8) * 0.5 + noise(4) * 0.35 + noise(2) * 0.15 - 0.5
    x = np.arange(W + 1)[None, :].astype(float)
    ramp = np.interp(x, [0, 10, 27, 43, 58, 90], [3.2, 3, 2, 1, 0, 0])
    s = ramp + n * 2.4 * np.interp(x, [0, 10, 54, 59, 90], [0.4, 1, 1, 0, 0])
    v = np.clip(np.rint(s), 0, 3).astype(int)
    v[:, 59:] = 0
    for _ in range(6):                                      # no cell may span three shades
        bad = False
        for yy in range(H):
            for xx in range(W):
                q = v[yy:yy + 2, xx:xx + 2]
                if q.max() - q.min() > 1:
                    bad = True; q[q == q.max()] -= 1
        if not bad: break
    return v

# ------------------------------------------------------------------ units
PINE = ((33, 34), (24, 23), (40, 41))                                   # Pelluca's pine, standing alone
BROAD = ((0xb, 0xc, 0xd), (0x13, 0x14, 0x15), (0x1b, 0x1c, 0x1d))      # Crown's broadleaf, standing alone

def pine(M, x, y):
    """Pelluca's pine on mint or sage (on mint it is Pelluca's own metatiles, free from its primary)."""
    assert M.free(x, y, 2, 3, 1, avoid={'cliff', 'water', 'house', 'bridge', 'road', 'tree', 'ptree', 'farm'}), ('pine', x, y)
    k = min(1, M.shade_at(x, y, 2, 3)); M.flatten(x, y, 2, 3, k)
    for dy, row in enumerate(PINE):
        for dx, v in enumerate(row):
            tag = 'pcanopy' if dy == 0 else f'ptree:{x},{y}'        # the crown row: he walks behind it
            if k == 0: M.ground[y + dy][x + dx] = ('cor', v); M.mark(x + dx, y + dy, tag)
            else: M.lay(x + dx, y + dy, 'cor', v, tag, top=dy == 0)

def broad(M, x, y):
    assert M.free(x, y, 3, 3, 1, avoid={'cliff', 'water', 'house', 'bridge', 'road', 'farm'}), ('broad', x, y)
    M.flatten(x, y, 3, 3, M.shade_at(x, y, 3, 3))
    for dy, row in enumerate(BROAD):
        for dx, v in enumerate(row):
            M.lay(x + dx, y + dy, 'c325', v, 'canopy' if dy == 0 else f'tree:broad{x},{y}', top=dy == 0)

def woods(M, cols, kind):
    """Crown's woods as columns three cells wide: (x0, top, bottom). 'north' columns hang from the map top and end in
    a row of trunks (13 14 15 over 1b 1c 1d, after an 18-row); 'south' columns rise from the map bottom under a
    canopy edge (b c d, then a 10-row). (Crown's open-end trunk pieces 1e/26, 1f/27 carry cobwebs: not used.)"""
    span = {}
    for x0, yt, yb in cols:
        for k in range(3): span[x0 + k] = (yt, yb)
    def wood(x, y): return x in span and span[x][0] <= y <= span[x][1]
    for x0, yt, yb in cols:
        for y in range(yt, yb + 1):
            for k in range(3):
                x = x0 + k
                if kind == 'north':
                    if y == yb - 1:
                        v = (0x13, 0x14, 0x15)[k]
                    elif y == yb:
                        v = (0x1b, 0x1c, 0x1d)[k]
                    else: v = ((0x18, 0x19, 0x1a), (0x10, 0x11, 0x12))[(yb - 2 - y) % 2][k]
                else:
                    if y == yt: v = (0xb, 0xc, 0xd)[k]
                    else: v = ((0x10, 0x11, 0x12), (0x18, 0x19, 0x1a))[(y - yt - 1) % 2][k]
                edge = kind == 'south' and y == yt
                M.lay(x, y, 'c325', v, 'canopy' if edge else 'tree:woods', top=edge)
                M.flatten(x, y, 1, 1, max(2, M.shade_at(x, y, 1, 1)))      # spring or olive under Crown's woods

def pine_woods(M, cols, kind, shade=None):
    """Pelluca's own pine forest as columns two cells wide (x0 even, (x0, top, bottom)), its pattern as in Pelluca:
    rows alternate 31 30 / 24 23 in step with Pelluca's (a row is a 31-row when Pelluca's matching row is even);
    'north' columns end in trunks (40 41) on a 31-row, 'south' columns start with crowns (33 34) on a 31-row. A side
    with no forest beside it takes Pelluca's edge pieces (29/22 left, 32/25 right). On mint: Pelluca's own
    metatiles; on sage: laid over the grass."""
    span = {}
    for x0, yt, yb in cols:
        for k in range(2): span[x0 + k] = (yt, yb)
    def wood(x, y): return (x in span and span[x][0] <= y <= span[x][1]) or x >= SEAM
    for x0, yt, yb in cols:
        assert x0 % 2 == 0
        k = shade if shade is not None else min(1, M.shade_at(x0, yt, 2, yb - yt + 1))
        M.flatten(x0, yt, 2, yb - yt + 1, k)
        for y in range(yt, yb + 1):
            r31 = (y + PEL) % 2 == 0
            if kind == 'north' and y == yb: assert r31, ('trunks off pattern', x0, yb); pair = (40, 41)
            elif kind == 'south' and y == yt: assert r31, ('crowns off pattern', x0, yt); pair = (33, 34)
            else: pair = (31, 30) if r31 else (24, 23)
            for i in range(2):
                x = x0 + i; v = pair[i]
                if i == 0 and not wood(x - 1, y): v = {31: 29, 24: 22}.get(v, v)
                if i == 1 and not wood(x + 1, y): v = {30: 32, 23: 25}.get(v, v)
                crown = kind == 'south' and y == yt
                tag = 'pcanopy' if crown else 'ptree:woods'
                inner = v in (31, 30, 24, 23)                    # (all crown: Pelluca's own metatile, free)
                if k == 0 or inner: M.ground[y][x] = ('cor', v); M.mark(x, y, tag)
                else: M.lay(x, y, 'cor', v, tag, top=crown)

def tall_grass(M, x0, x1, y0, y1):
    M.flatten(x0, y0, x1 - x0 + 1, y1 - y0 + 1, M.shade_at(x0, y0, x1 - x0 + 1, y1 - y0 + 1), rim=False)
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            cx = 0 if x == x0 else 2 if x == x1 else 1; cy = 0 if y == y0 else 2 if y == y1 else 1
            M.lay(x, y, 'c325', ((0x21, 0x22, 0x23), (0x29, 0x2a, 0x2b), (0x31, 0x32, 0x33))[cy][cx], 'tall')

def block(M, src, sx, sy, w, h, x0, y0, what, sub=None, clear=(), shade=None):
    c = kit.atlas(ATL[src])['cells'][sy:sy + h, sx:sx + w]
    k = M.shade_at(x0, y0, w, h) if shade is None else shade         # the block stands on the grass it is in
    for dy in range(h):
        for dx in range(w):
            v = int(c[dy, dx]); v = (sub or {}).get(v, v)
            M.flatten(x0 + dx, y0 + dy, 1, 1, k)
            M.lay(x0 + dx, y0 + dy, src, v, what, clear=clear)

def fence(M, x0, x1, y, gaps=()):
    for x in range(x0, x1 + 1):
        if x in gaps: continue
        v = 0x34 if x == x0 or x - 1 in gaps else 0x2b if x == x1 or x + 1 in gaps else 0x29
        M.flatten(x, y, 1, 1, 0); M.lay(x, y, 'c31', v, 'farm:fence')

# ------------------------------------------------------------------ the gorge, the coast (MonoMyth's kit)
GW0, GE0 = 62, 75              # the chasm's land edges: 1b6 (land west of it) and 1b4 (land east of it)
LIP = 20 + OY                  # the coastal cliff's lip row; its two face rows below it; then the beach
SEA = 26 + OY                  # the waterline row
COVE_W, COVE_E = 47, 81        # the cove's side walls (their land-edge columns)
STAIRS = (58, 59)              # stone stairs cut down the coastal cliff to the west beach, just past the bridge
EAST_STAIRS = (77, 78)         # (and their twin to the east beach, user 2026-11-25; patched in by east_beach_stairs.py: draw them
                               # here as the west ones if this composer is ever rebuilt)
                               # (user 2026-11-20: the beach holds a trainer, more later): Pelluca's own stairs
                               # (45/46, as in its sea wall), with dark rock cheeks either side.

def gorge(M):
    """The chasm (GW0..GE0): 1b6 | 29 29 | the river's eight columns | 28 28 | 1b4. Down it: a pool off the north
    edge, falls (69-70), a pool, falls (67-68) under the bridge, a pool on the coastal cliff's lip, the last falls
    (66-67) over the coastal faces onto the beach."""
    L = lambda x, y, v: M.lay(x, y, 'mm', v, 'cliff' if v not in WATER else 'water')
    inner = range(GW0 + 3, GE0 - 2)                          # 65..72
    rows = {}
    def pool(y, kind):                                        # kind: 'top' (bank under a face) or 'mid'
        r = {}
        for x in inner:
            r[x] = 0xc6
        r[inner[0]] = 0xc0; r[inner[-1]] = 0xc1
        return r
    def face(y, falls, top):
        r = {x: 0x1a for x in inner}
        for x in falls: r[x] = 0xb4 if top else 0xb5
        return r
    def bank(falls):
        r = {x: 0xbe for x in inner}; r[inner[0]] = 0xae; r[inner[-1]] = 0xa7
        for x in falls: r[x] = 0xbc
        return r
    F0, F1, F2, F3 = (70, 71), (69, 70), (67, 68), (66, 67)
    o = OY
    rows[0] = face(0, F0, False); rows[1] = face(1, F0, False)  # (in the woods above the picture: the river falls in
    rows[2] = bank(F0)                                         #  from off the map's top edge)
    for y in range(3, o + 2): rows[y] = pool(y, 'mid')
    rows[o + 2] = face(o + 2, F1, True)
    for y in (o + 3, o + 4, o + 5): rows[y] = face(y, F1, False)
    rows[o + 6] = bank(F1); rows[o + 7] = pool(o + 7, 'mid'); rows[o + 8] = pool(o + 8, 'mid')
    rows[o + 9] = face(o + 9, F2, True)
    for y in range(o + 10, o + 19): rows[y] = face(y, F2, False)     # the road's rows lie under the bridge
    rows[o + 19] = bank(F2); rows[o + 20] = pool(o + 20, 'mid')
    rows[o + 21] = face(o + 21, F3, True); rows[o + 22] = face(o + 22, F3, False)
    for y, r in rows.items():
        if ROAD <= y <= ROAD + 2: continue
        for x, v in r.items(): L(x, y, v)
    # the walls: land edges, slopes; at the coastal lip the edges turn into it and the slopes end on the faces
    for y in range(0, LIP + 3):
        if ROAD <= y <= ROAD + 2: continue
        w = {GW0: 0x1b6 if y < LIP else 0x1c7 if y == LIP else 0x1a,
             GW0 + 1: 0x29 if y <= LIP else 0x37 if y == LIP + 1 else 0x1a,
             GW0 + 2: 0x29 if y <= LIP + 1 else 0x37,
             GE0 - 2: 0x28 if y <= LIP + 1 else 0x36,
             GE0 - 1: 0x28 if y <= LIP else 0x36 if y == LIP + 1 else 0x1a,
             GE0: 0x1b4 if y < LIP else 0x1c6 if y == LIP else 0x1a}
        for x, v in w.items(): L(x, y, v)

WATER = {0xc6, 0xc0, 0xc1, 0xbe, 0xae, 0xa7, 0xbc, 0xb4, 0xb5, 0xb8, 0xb9}

def coast(M):
    """The coastal cliff from cove wall to cove wall (lip on row 20, faces 21-22), the beach (rows 23-25) and the sea;
    the cove's walls run down to the map's bottom edge (MonoMyth's concave corners 1af and 1be). The river: foam
    where the last falls land (row 23), then its channel across the sand into the sea."""
    L = lambda x, y, v: M.lay(x, y, 'mm', v, 'cliff' if v not in WATER else 'water')
    for x in range(COVE_W + 1, COVE_E):
        if GW0 <= x <= GE0: continue
        if x in STAIRS:
            for y in (LIP, LIP + 1, LIP + 2):
                M.lay(x, y, 'cor', 45 if x == STAIRS[0] else 46, 'stairs')
                o = M.over[y][x][-1]                        # cut into the rock: a dark cheek either side
                cols = (0, 1) if x == STAIRS[0] else (15, 14)  # (in the stairs' own palette: Pelluca's 2)
                o[:, cols[0], :3] = (72, 56, 80); o[:, cols[1], :3] = (72, 56, 80)
            continue
        L(x, LIP, 0x1bd)
        for y in (LIP + 1, LIP + 2):
            if x == COVE_W + 1 and y == LIP + 1: v = 0x6e
            elif x == COVE_E - 1 and y == LIP + 1: v = 0x6f
            elif x == COVE_W + 1: v = 0x29
            elif x == COVE_E - 1: v = 0x28
            else: v = 0x1a
            L(x, y, v)
    L(COVE_W, LIP, 0x1af); L(COVE_E, LIP, 0x1be)
    for y in range(LIP + 1, H):
        L(COVE_W, y, 0x1b6); L(COVE_E, y, 0x1b4)
        if y > LIP + 2: L(COVE_W + 1, y, 0x29); L(COVE_E - 1, y, 0x28)
    # the beach and the sea between the walls
    for x in range(COVE_W + 2, COVE_E - 1):
        for y in range(LIP + 3, H):
            if y < SEA: M.ground[y][x] = 'sand'
            else: M.ground[y][x] = ('cor', {SEA: 171, SEA + 1: 173, SEA + 2: 175}.get(y, 162))
            if y >= SEA: M.mark(x, y, 'sea')
    for x in (COVE_W + 1, COVE_E - 1):                      # under the slopes: sand, then sea
        for y in range(LIP + 3, H): M.ground[y][x] = 'sand' if y < SEA else ('cor', 175 if y < H - 1 else 162)
    # the river across the beach: the last falls land in a rock-banked pool under the cliff; from it a stream bends
    # west over the sand to the surf (its water vertices below; edges as Crown's, a foam rim, wet sand)
    R0, R1 = 65, 68
    M.lay(R0, LIP + 3, 'mm', 0xae, 'stream'); M.lay(R1, LIP + 3, 'mm', 0xa7, 'stream')
    for x in (66, 67): M.lay(x, LIP + 3, 'mm', 0xbc, 'stream')
    wet = {LIP + 4: {66, 67, 68}, LIP + 5: {65, 66, 67}, SEA: {63, 64, 65, 66}, SEA + 1: set(range(62, 68))}
    def water_v(vx, vy): return vx in wet.get(vy, ())
    sand, sea = kit.cor_full(163), kit.cor_full(175)
    for y in range(LIP + 4, SEA + 1):
        for x in range(59, 73):
            c = [water_v(x, y), water_v(x + 1, y), water_v(x, y + 1), water_v(x + 1, y + 1)]
            if not any(c): continue                              # sand, or the ordinary shoreline (171)
            img = sea.copy() if all(c) else kit.edge_cell(sand, sea, c, rim_lo=(216, 184, 128), rim_hi=(224, 240, 248))
            M.ground[y][x] = ('img', img)
            M.wet[(x, y)] = sum(c) >= 2                          # half or more water: water to walk into
            if y < SEA and M.wet[(x, y)]: M.mark(x, y, 'stream')

def bridge(M):
    """MonoMyth's bridge over the chasm on the road's rows: posts on the grass at 61 and 77."""
    cols = {GW0 - 1: (0x2b9, 0x2c1, 0x2c9), GE0 + 2: (0x2ba, 0x2c2, 0x2ca)}
    for x in range(GW0, GE0 + 2):                       # (the same deck all the way: fewer tiles)
        if x in cols: continue
        cols[x] = (0x2d2, 0x2e4, 0x2f0) if x in (67, 68) else (0x2eb, 0x2e3, 0x2ee)
    for x, vs in cols.items():
        for dy, v in enumerate(vs): M.lay(x, ROAD + dy, 'mm', v, 'bridge')

# ------------------------------------------------------------------ Pelluca's side
def pelluca_seam(M):
    """Columns 82-89: Pelluca's columns 0-7 (its rows 9-48) as they are, so the pines and the road run straight
    on; Pelluca's column 7 pines' right edges become interior ones (its column 0 follows), column 82 takes left edges."""
    g = np.fromfile(os.path.join(RL.C, 'data/layouts/PellucaCity/map.bin'), '<u2').reshape(60, 80) & 0x3FF
    inner = {32: 30, 25: 23}; left = {31: 29, 24: 22}
    for y in range(H):
        for c in range(8):
            v = int(g[y + PEL, c])
            if c == 7: v = inner.get(v, v)
            if c == 0: v = left.get(v, v)
            M.ground[y][SEAM + c] = ('cor', v); M.mark(SEAM + c, y, 'seam' if v not in (64, 78, 131) else 'road')

def road(M):
    for x in range(GE0 + 3, SEAM):
        for dy, (a, b) in enumerate(((63, 64), (77, 78), (130, 131))):
            M.ground[ROAD + dy][x] = ('cor', a if x == GE0 + 3 else b); M.mark(x, ROAD + dy, 'road')
    for x in range(0, GW0 - 1):                              # Crown's worn dirt road, its east end at the bridge
        end = x == GW0 - 2
        for dy, v in enumerate((0x2c2, 0x2ca, 0x2d2) if end else (0x2c1, 0x7e, 0x2d1)):
            M.lay(x, ROAD + dy, 'c31', v, 'road')

# ------------------------------------------------------------------ the composition
# (rows as in the approved 90x30 picture; compose() adds OY)
# Pelluca's pines keep to the light grass (their shadows are drawn in the pines' own greens): east of column 38.
# The picture's trees along its top edge now belong to the woods above it (the five rows out of reach).
BROADS = ((22, 5), (25, 5), (29, 6), (34, 6), (23, 19), (27, 18), (33, 19), (30, 22), (37, 24), (24, 25), (28, 27),
          (33, 27), (43, 22))
PINES = ((39, 4), (77, 5))

def compose():
    M = Map(); M.field = shade_field()
    pelluca_seam(M); road(M); gorge(M); bridge(M); coast(M)
    o = OY
    # the woods above the picture (out of reach): Crown's in the west, Pelluca's pines from column 38 east, their
    # lower edge ragged, ending a row or more above anything in the picture
    woods(M, [(0, 0, 10 + o), (3, 0, 8 + o), (6, 0, 10 + o), (9, 0, 7 + o), (12, 0, 6 + o), (15, 0, 4 + o),
              (18, 0, 2 + o), (21, 0, 2 + o), (24, 0, 3 + o), (27, 0, 2 + o), (30, 0, 1 + o), (33, 0, 2 + o)], 'north')
    # (on sage where they meet Crown's woods, so the two grounds are a shade apart)
    pine_woods(M, [(36, 0, 0 + o), (38, 0, -2 + o)], 'north', shade=1)
    pine_woods(M, [(40, 0, 0 + o), (42, 0, 2 + o), (44, 0, 0 + o), (46, 0, 2 + o),
                   (48, 0, 0 + o), (50, 0, -2 + o), (52, 0, 0 + o), (54, 0, 2 + o), (56, 0, 0 + o), (58, 0, 2 + o),
                   (60, 0, 0 + o)], 'north')
    pine_woods(M, [(76, 0, 0 + o), (78, 0, 2 + o), (80, 0, -2 + o)], 'north')
    # below the picture: the woods close in again; the cove's sea runs on
    woods(M, [(0, 19 + o, H - 1), (3, 21 + o, H - 1), (6, 18 + o, H - 1), (9, 22 + o, H - 1), (12, 20 + o, H - 1),
              (15, 23 + o, H - 1), (18, 25 + o, H - 1), (21, 31 + o, H - 1), (24, 32 + o, H - 1),
              (27, 31 + o, H - 1), (30, 32 + o, H - 1), (33, 31 + o, H - 1)], 'south')
    pine_woods(M, [(36, 30 + o, H - 1), (38, 32 + o, H - 1)], 'south', shade=1)
    pine_woods(M, [(40, 30 + o, H - 1), (42, 32 + o, H - 1), (44, 30 + o, H - 1)], 'south')
    tall_grass(M, 3, 8, 11 + o, 12 + o); tall_grass(M, 9, 13, 18 + o, 19 + o); tall_grass(M, 31, 36, 10 + o, 12 + o)
    tall_grass(M, 37, 42, 18 + o, 19 + o); tall_grass(M, 76, 80, 17 + o, 19 + o)
    # the farm north of the road: cottage, yard fence, cabbages, the sown field, hay
    # (Crown's cottage stands on a dirt yard and a paler grass: those are left out too)
    block(M, 'c31', 12, 9, 7, 4, 52, 6 + o, 'house', clear={(224, 208, 160), (208, 184, 136), (200, 216, 144), (176, 208, 128)})
    fence(M, 50, 60, 11 + o, gaps=(55, 56))
    # (the farm's own plots on Pelluca's mint: the farm palette has room for one grass only)
    block(M, 'ody', 18, 7, 6, 3, 43, 4 + o, 'farm:crops', sub={64: 10, 9: 10}, shade=0)   # (a stump, a gap: cabbages)
    block(M, 'ody', 17, 12, 8, 4, 42, 8 + o, 'farm:field', shade=0)
    block(M, 'ody', 9, 9, 2, 2, 59, 7 + o, 'farm:hay'); block(M, 'ody', 9, 9, 2, 2, 50, 8 + o, 'farm:hay')
    # flower beds on the cliff-top south of the road
    for x in range(50, 58):
        M.flatten(x, 17 + o, 1, 2, 0)
        M.lay(x, 17 + o, 'c31', 0x282, 'farm:flowers'); M.lay(x, 18 + o, 'c31', 0x283, 'farm:flowers')
    # trees: the mixed groves of the middle, pines by the farm and Pelluca, broadleaf westward
    # each tree goes at its spot or the nearest one (within two cells) where the grass under it is already one shade,
    # so flattening the grass under it leaves no box round it; never touching another tree or the woods
    bad = []; pts_pine = [(x, y + o) for x, y in PINES]
    for f, pts, w in ((broad, [(x, y + o) for x, y in BROADS], 3), (pine, pts_pine, 2)):
        for x, y in pts:
            best = None
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    xx, yy = x + dx, y + dy
                    if xx < 0 or yy < 0 or yy + 3 > H: continue
                    av = {'cliff', 'water', 'house', 'bridge', 'road', 'farm', 'tree', 'canopy', 'ptree', 'pcanopy', 'seam',
                          'sea', 'stream'}
                    if not M.free(xx, yy, w, 3, 1, avoid=av): continue
                    v = M.field[yy:yy + 4, xx:xx + w + 1]; k = np.bincount(v.ravel(), minlength=4).argmax()
                    if f is pine: k = min(1, k)
                    elif k < 2: continue                         # broadleaf keep to the darker grass
                    if M.lock[yy:yy + 4, xx:xx + w + 1].any() and (v[M.lock[yy:yy + 4, xx:xx + w + 1]] != k).any(): continue
                    score = ((v != k).sum(), abs(dx) + abs(dy))
                    if best is None or score < best[0]: best = (score, xx, yy)
            if best is None and f is broad: pts_pine.append((x, y)); continue    # in light grass: a pine instead
            if best is None: bad.append((f.__name__, x, y)); continue
            f(M, best[1], best[2])
    if bad: raise SystemExit(f'trees that do not fit: {bad}')
    # the woods' small growth in the darker grass: Crown's tufts, never on anything else
    rng = np.random.default_rng(7)
    for y in range(H):
        for x in range(W - 8):
            if M.used[y, x] is not None or M.ground[y][x] != 'grass': continue
            q = M.field[y:y + 2, x:x + 2]; k = q.min()
            if q.max() != k: continue                               # only on one shade (its tiles repeat)
            r = rng.random()
            if k >= 2 and r < 0.05: M.lay(x, y, 'c325', 0xa, 'tuft'); M.flatten(x, y, 1, 1, k)
    # flowers by the road (the route sign is a stage-2 object)
    for x, y in ((77, 10 + o), (80, 9 + o), (58, 13 + o), (46, 13 + o)):
        if M.used[y, x] is None and M.field[y:y + 2, x:x + 2].max() == 0: M.ground[y][x] = ('cor', 21); M.mark(x, y, 'flower')
    M.settle()
    return M

def main(out):
    M = compose(); img = M.render()
    Image.fromarray(img).save(out)
    Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), 0).save(out.replace('.png', '_2x.png'))
    print(out)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/route11/route11_v2.png')
