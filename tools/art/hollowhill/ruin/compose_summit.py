"""Hollow Hill's summit, art mock v2 (plan B, user 2026-11-25: the summit as its own map; story as proposed).

v2 (user 2026-11-25: "the temple doesn't look correct. Study the bastion part that leads to the open sky area in
monomyth"; and a visual audit of the rest): the north half is now MonoMyth's bastion ascent (bastion.py): four flights
narrowing up the axis between massive stone tiers, columns and knight statues flanking each flight, to the arcade at
the top, its middle arch burst open from inside and webbed shut: the guardian's lair. South of it, as before: the
court with the stele where Phancero was erased, the paving cracked out from it, four empty plinths, a broken
colonnade, and the stair sunk in the ground that the tunnel from the sealed door climbs out of.
Credits: MonoMyth (the bastion, columns, webbing), Pokemon Odyssey (tileset, stele, stair, pines), Lazarus (fallen
column).
Usage: python3 compose_summit.py OUTDIR"""
import os, sys, random, math
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools/art/mt_mirroh/b1f')); sys.path.insert(0, os.path.join(ROOT, 'tools/art/mt_mirroh'))
sys.path.insert(0, os.path.join(ROOT, 'tools/art/ancient_cormoria')); sys.path.insert(0, os.path.join(ROOT, 'tools/art/mt_mirroh/cave'))
import hh_mock as hh

S = 16
W, H = 43, 49
AX = 20 + 1                                    # the axis (one cell)
hh.W, hh.H = W, H                              # (hh_mock's shape helpers read these)
ody = hh.ody
import bastion as BA
BX, BY = AX - BA.CX, 1                         # the bastion's cut: cells BX..BX+26, rows BY..BY+27
DOOR = (AX, BY + BA.ARCADE_ROW)                # the burst arch (the lair's door; the player steps in from below)
COURT_TOP = BY + BA.CH                         # the court's first row below the bastion's floor

def levels():
    yy, xx = np.mgrid[0:H, 0:W]
    P1 = ((xx >= BX - 3) & (xx <= BX + BA.CW + 2) & (yy >= BY) & (yy <= COURT_TOP + 2)) | \
         (np.abs((xx - AX) / 17.0) ** 3 + np.abs((yy - 36.5) / 9.6) ** 3 <= 1)
    P1 = hh.clean(P1)
    return hh.cheb_depth(P1, 3), (P1,)

PLINTHS = [(AX - 5, 31), (AX + 4, 31), (AX - 5, 37), (AX + 4, 37)]   # 2x2 each, symmetric about the axis
STELE = (AX, 34)                                    # 2e5 over 2ed
ARRIVE = (AX - 2, 41)                               # the sunk stair the tunnel climbs out of (5 wide, 2 rows)
COLS = [(AX - 10, y) for y in (30, 33, 36, 39)] + [(AX + 10, y) for y in (30, 33, 36, 39)]
STANDING = {(AX - 10, 30), (AX + 10, 33), (AX - 10, 36), (AX + 10, 39), (AX + 10, 30)}
FALLEN = {(AX - 10, 39): +1}

def faces(E):
    F = {}
    for y in range(H):
        for x in range(W):
            p = hh.face_piece(E, x, y)
            if p is not None: F[x, y] = p
    return F

# ------------------------------------------------------------------------------------------------- the canvas
class Canvas:
    def __init__(self, img):
        self.img = img; self.mid = np.zeros_like(img); self.mid_a = np.zeros(img.shape[:2], bool)
        self.top = np.zeros_like(img); self.top_a = np.zeros(img.shape[:2], bool)
    def put(self, rgb, a, X0, Y0, foot=None, layer='mid'):
        h, w = a.shape
        for yy in range(h):
            Y = Y0 + yy
            if not (0 <= Y < H * S): continue
            xs = slice(max(0, X0), min(W * S, X0 + w)); r0 = max(0, X0) - X0
            row = a[yy][r0:r0 + (xs.stop - xs.start)]; src = rgb[yy][r0:r0 + (xs.stop - xs.start)]
            if layer == 'bottom': self.img[Y, xs][row] = src[row]; continue
            if foot is not None and Y < foot: self.top[Y, xs][row] = src[row]; self.top_a[Y, xs] |= row
            else: self.mid[Y, xs][row] = src[row]; self.mid_a[Y, xs] |= row
    def flat(self):
        f = self.img.copy(); f[self.mid_a] = self.mid[self.mid_a]; f[self.top_a] = self.top[self.top_a]; return f

def cellput(img, x, y, rgb): img[y * S:y * S + S, x * S:x * S + S] = rgb

def piece(m):
    """an Odyssey metatile as a sprite: its floor colours keyed out"""
    raw = hh.ody_raw(m); key = [tuple(p) for p in raw.reshape(-1, 3).tolist()]
    a = np.array([k not in hh.TEAL_GRASS for k in key]).reshape(16, 16)
    return ody(m).copy(), a

# ------------------------------------------------------------------------------- the temple's stone (bone) ramp
def stone_ramp():
    return list(BA.BONE_RAMP)                       # (the bastion's own bone stone: the columns and plinths match it)
RAMP = None
def to_bone(rgb, a=None):
    """MonoMyth's / Lazarus' stone mapped by lightness onto the temple's own bone stone; greens -> Hollow Hill's weeds"""
    global RAMP
    if RAMP is None: RAMP = np.array(stone_ramp(), float)
    out = rgb.copy(); flat = out.reshape(-1, 3); lum = (flat * [0.3, 0.55, 0.15]).sum(1)
    rl = (RAMP * [0.3, 0.55, 0.15]).sum(1)
    lo, hi = np.percentile(lum, 2), np.percentile(lum, 98)
    t = (lum - lo) / max(1, hi - lo) * (rl.max() - rl.min()) + rl.min()
    idx = np.abs(t[:, None] - rl[None, :]).argmin(1); new = RAMP[idx].astype(np.uint8)
    g = (flat[:, 1].astype(int) > flat[:, 0].astype(int) + 12) & (flat[:, 1].astype(int) > flat[:, 2].astype(int) - 10)
    weeds = np.array([(80, 74, 50), (122, 118, 80), (170, 164, 110)])
    new[g] = weeds[np.clip(((lum[g] - 60) / 70).astype(int), 0, 2)]
    flat[:] = new; return out

def columns():
    import compose_b1f5 as B5, compose_b1f as V1
    B5.cool_img = to_bone; B5.STONE7 = [tuple(int(v) for v in c) for c in stone_ramp()][::max(1, len(stone_ramp()) // 7)][:7]
    while len(B5.STONE7) < 7: B5.STONE7.append(B5.STONE7[-1])
    return B5, V1

# --------------------------------------------------------------------------------------------- the flagstones
FLAGS = [0x2fc, 0x301] * 9 + [0x305, 0x306]  # Odyssey's paving, whole slabs (the last two with a broken stone)
def flag_cells(rnd):
    """the court's paving, cell by cell: a square round the stele and the plinths, the axis down to the sunk stair;
    broken away at its edges and in holes (never on the axis' walking line)"""
    on = set()
    for x in range(AX - 7, AX + 8):
        for y in range(COURT_TOP, COURT_TOP + 12): on.add((x, y))
    for x in range(AX - 2, AX + 3):
        for y in range(COURT_TOP, ARRIVE[1]): on.add((x, y))
    for (x, y) in list(on):
        edge = any((x + dx, y + dy) not in on for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        corner = abs(x - AX) >= 5 and (y - COURT_TOP >= 9 or y - COURT_TOP <= 0)
        if y == COURT_TOP and abs(x - AX) <= 5: continue                       # (it runs on from the bastion's floor)
        if (edge and abs(x - AX) > 2 and rnd.random() < 0.4) or (corner and rnd.random() < 0.5): on.discard((x, y))
    for _ in range(12):
        x, y = rnd.randint(AX - 7, AX + 7), rnd.randint(COURT_TOP + 1, COURT_TOP + 11)
        if abs(x - AX) <= 2: continue
        for c in ((x, y), (x + rnd.choice((0, 1)), y)): on.discard(c)
    return on

_B = {}
def floor_cell(x, y):
    """the bastion's own paving (its floor below the last flight), carried on into the court"""
    b = BA.paving(); r = (y - COURT_TOP) % 2; c = (x - BX) % BA.CW
    return b[r * S:r * S + S, c * S:c * S + S]

def lay_flags(img, on, F, rnd):
    """slabs on the cells; each edge broken irregularly (a pixel noise line), outlined, the floor shadowed below"""
    m = np.zeros((H * S, W * S), bool)
    for (x, y) in on:
        if (x, y) in F: continue
        cellput(img, x, y, floor_cell(x, y)); m[y * S:y * S + S, x * S:x * S + S] = True
    keep = m.copy()                                                             # chew the outer edges
    yy, xx = np.nonzero(m)
    for Y, X in zip(yy, xx):
        if not (m[max(0, Y - 3):Y + 4, max(0, X - 3):X + 4]).all() and rnd.random() < 0.35: keep[Y, X] = False
    from scipy.ndimage import binary_opening
    keep = binary_opening(keep, np.ones((2, 2), bool)) | (m & keep & False)
    lost = m & ~keep
    floor = np.tile(hh.TEAL, (H, W, 1)); img[lost] = floor[lost]
    dark, shade = np.array((92, 84, 96)), np.array((84, 76, 72))
    e = keep & ~(np.roll(keep, 1, 0) & np.roll(keep, -1, 0) & np.roll(keep, 1, 1) & np.roll(keep, -1, 1))
    img[e] = dark
    sh = np.zeros_like(keep); sh[1:, 1:] = keep[:-1, :-1]; sh &= ~keep
    for (x, y) in F: sh[y * S:y * S + S, x * S:x * S + S] = False
    img[sh] = (img[sh] * 0.6 + shade * 0.4).astype(np.uint8)
    return keep

def cracks(img, fm, rnd):
    """the floor broken out from the stele: dark cracks branching outward, old blood dried in the nearest"""
    cx, cy = (STELE[0] + 0.5) * S, (STELE[1] + 2) * S - 3
    dark, deep = np.array((52, 42, 46)), np.array((70, 10, 18))
    def walk(x, y, a, n, w, gen):
        for i in range(n):
            a += rnd.uniform(-0.22, 0.22); x += math.cos(a); y += math.sin(a) * 0.9
            X, Y = int(x), int(y)
            if not (0 <= X < W * S and 0 <= Y < H * S) or not fm[Y, X]: return
            img[Y, X] = deep if (i < 22 and gen == 0) else dark
            if w > 1 and Y + 1 < H * S and fm[Y + 1, X]: img[Y + 1, X] = dark
            if gen < 2 and rnd.random() < 0.035: walk(x, y, a + rnd.choice((-0.8, 0.8)), n // 2, 1, gen + 1)
    for k in range(10):
        a = k * 2 * math.pi / 10 + rnd.uniform(-0.2, 0.2)
        walk(cx + math.cos(a) * 8, cy + math.sin(a) * 5, a, rnd.randint(50, 90), 2 if k % 3 == 0 else 1, 0)

# ------------------------------------------------------------------------------------------------- the pieces
def plinth(seed, broken=False):
    """an empty plinth in the temple's stone, 2x2 cells: a stepped base, a squat block on it, the top's socket empty
    (what stood in it taken); cracked"""
    r = random.Random(seed); R = [tuple(int(v) for v in c) for c in stone_ramp()]
    L, M_, D, DD = R[1], R[len(R) // 3], R[2 * len(R) // 3], R[-1]
    rgb = np.zeros((32, 32, 3), np.uint8); a = np.zeros((32, 32), bool)
    def box(x0, y0, x1, y1, c): rgb[y0:y1, x0:x1] = c; a[y0:y1, x0:x1] = True
    box(1, 22, 31, 31, DD); box(2, 22, 30, 30, M_); box(2, 22, 30, 24, L)          # the lower step
    box(4, 18, 28, 23, DD); box(5, 18, 27, 22, M_); box(5, 18, 27, 19, L)          # the upper step
    box(6, 4, 26, 19, DD); box(7, 5, 25, 18, M_); box(7, 5, 25, 11, L)              # the block: top face, front
    box(7, 11, 25, 12, D); box(7, 12, 8, 18, L)
    box(12, 6, 20, 10, DD); box(13, 7, 19, 8, D)                                   # the empty socket
    rgb[14, 9:24] = D
    cx, cy = r.randint(10, 22), 12
    for i in range(12):                                                            # a crack down the front
        rgb[cy, cx] = DD; cy += 1; cx += r.choice((-1, 0, 0, 1)); cx = min(23, max(9, cx))
        if cy >= 22: break
    if broken:                                                                     # a corner knocked off the block
        for y in range(4, 12):
            for x in range(18 + (y - 4) // 2, 27): a[y, x] = False
            x = 18 + (y - 4) // 2
            if x < 27: rgb[y, x] = DD
    return rgb, a

def breach(cv, rnd, B5):
    """the bastion's arcade: its middle arch burst open from inside, a ragged hole broken out brick by brick up into the
    wall above (its edges stepping with the courses), the wall's thickness lit inside its top; its stones (MonoMyth's
    own rubble) thrown down onto the landing; blood soaked into the landing's stones below it"""
    X, Y = DOOR[0] * S + 8, DOOR[1] * S + S - 3              # the hole's foot, centred on the axis
    HT, HW = 46, 22
    void, thick, rim = np.array((14, 10, 18)), np.array(BA.BONE_RAMP[5]), np.array(BA.BONE_RAMP[7])
    img = cv.img; mask = np.zeros(img.shape[:2], bool)
    for band in range(0, HT, 4):                              # a course of bricks at a time, from the foot up
        h = band / HT; w = HW * (1 - h ** 2.2) ** 0.5
        w = int(round((w + rnd.choice((-4, 0, 0, 4))) / 4) * 4)
        if w <= 0: continue
        off = rnd.choice((-4, 0, 0, 4)) if band > 8 else 0
        for yy in range(Y - band - 4, Y - band):
            mask[yy, X - w + off:X + w + off] = True
    cv.mid[mask] = void; cv.mid_a[mask] = True
    above = np.zeros_like(mask); above[:-1] = mask[1:]                    # the top edge: the wall's thickness, lit
    top = mask & ~np.roll(mask, 3, 0)
    cv.mid[top] = thick
    edge = ~mask & (np.roll(mask, 1, 0) | np.roll(mask, -1, 0) | np.roll(mask, 1, 1) | np.roll(mask, -1, 1))
    cv.mid[edge] = rim; cv.mid_a[edge] = True
    # the thrown-down stones: a spill of broken blocks, each lit on top, dark at its foot, outlined
    R_ = BA.BONE_RAMP; yy, xx = np.mgrid[0:img.shape[0], 0:img.shape[1]]
    for k in range(14):
        cx = X + rnd.gauss(0, 15); cy = Y + 7 + abs(rnd.gauss(0, 7))
        if abs(cx - X) < 6 and cy < Y + 10: cx += rnd.choice((-9, 9))          # (the door cell's foot kept clear)
        rx, ry = rnd.uniform(4, 7.5), rnd.uniform(3, 5)
        x0, x1, y0, y1 = int(cx - rx - 2), int(cx + rx + 3), int(cy - ry - 2), int(cy + ry + 3)
        sub = (((xx[y0:y1, x0:x1] - cx) / rx) ** 2 + ((yy[y0:y1, x0:x1] - cy) / ry) ** 2) <= 1
        sub &= ~((np.abs(xx[y0:y1, x0:x1] - cx) + np.abs(yy[y0:y1, x0:x1] - cy) * 0.6) > rx * 0.95)   # (faceted)
        reg = cv.img[y0:y1, x0:x1]
        reg[sub] = R_[3]
        hi = sub & (yy[y0:y1, x0:x1] < cy - ry * 0.25); reg[hi] = R_[1]
        lo = sub & (yy[y0:y1, x0:x1] > cy + ry * 0.4); reg[lo] = R_[5]
        e = sub & ~(np.roll(sub, 1, 0) & np.roll(sub, -1, 0) & np.roll(sub, 1, 1) & np.roll(sub, -1, 1)); reg[e] = R_[7]
    g = np.random.default_rng(3)
    for k in range(80):
        px = int(X + g.normal(0, 10)); py = int(Y + 4 + abs(g.normal(0, 7)))
        if not mask[py, px]: cv.img[py, px] = hh.BLOOD[int(g.integers(0, 2))]

def webs(cv, rnd):
    """the guardian's: the net across the breach; webs in the corners where the arcade meets the columns and statues;
    round webs between the columns and the tiers up the flights; sheets in the court's colonnade"""
    L = np.zeros((H * S, W * S, 4), np.uint8); g = np.random.default_rng(rnd.randint(0, 99999))
    net = hh.web('web_net'); nh, nw = net.shape[:2]
    X = DOOR[0] * S + 8 - nw // 2; Y = (DOOR[1] - 1) * S - 2
    sl = L[Y:Y + nh, X:X + nw]; mm = net[..., 3] > 0; sl[mm] = net[mm]
    for (cx, cy, R) in ((BX + 7, BY + 10, 13), (BX + 19, BY + 9, 12), (BX + 4, BY + 15, 15), (BX + 22, BY + 16, 13),
                        (BX + 1, BY + 20, 14)):
        C = (cx * S + 8, cy * S + 8)
        hh.orb(L, C, R, [(C[0] - R - 4, C[1] - R), (C[0] + R + 4, C[1] - R + 3)], g, torn=0.35)
    for x, ys in ((AX - 10, (30, 33)), (AX + 10, (33, 36)), (AX + 10, (30, 33))):
        top_a = (x * S + 8, (ys[0] + 1) * S - 34); top_b = (x * S + 8, (ys[1] + 1) * S - 34)
        C = (x * S + 8 + (5 if x < AX else -5), (top_a[1] + top_b[1]) // 2 + 4)
        hh.orb(L, C, 17, [top_a, top_b, (x * S + 8, top_b[1] + 26)], g, torn=0.35)
    a = L[..., 3] > 0
    cv.put(L[..., :3], a, 0, 0, foot=H * S)                                    # (webs hang over the player)

def webbed_rock(seed):
    """a boulder wrapped in blood web (the user's reference): Odyssey's rock with a net drawn over it"""
    rgb, a = piece(0x2fe); rgb = rgb.copy(); r = random.Random(seed)
    pts = [(r.randint(2, 13), r.randint(5, 13)) for _ in range(5)]
    L = np.zeros((16, 16, 4), np.uint8)
    for i, p in enumerate(pts):
        hh._line(L, p, pts[(i + 2) % len(pts)], hh.WEB_LIGHT if i % 2 else hh.WEB_DARK)
    m = (L[..., 3] > 0) & a; rgb[m] = L[..., :3][m]
    return rgb, a

def blob(rnd, x0, y0, n):
    """an organic patch of n cells grown from (x0, y0)"""
    cells = {(x0, y0)}
    while len(cells) < n:
        x, y = rnd.choice(sorted(cells)); d = rnd.choice(((1, 0), (-1, 0), (0, 1), (0, -1), (1, 0), (-1, 0)))
        cells.add((x + d[0], y + d[1]))
    return cells

# ------------------------------------------------------------------------------------------------- compose
def compose(seed=7):
    rnd = random.Random(seed)
    E, (P1,) = levels(); F = faces(E)
    inb = lambda x, y: BX <= x < BX + BA.CW and BY <= y < BY + BA.CH
    for k in [k for k in F if inb(*k)]: del F[k]
    for (x, y), v in list(F.items()):
        if v == 0x2f1 and rnd.random() < 0.10: F[x, y] = rnd.choice([0x2df, 0x2e7])
    img = np.zeros((H * S, W * S, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            cellput(img, x, y, ody(F[x, y]) if (x, y) in F else hh.TEAL)
    class _M: pass
    M = _M(); M.face = F; hh.DOOR = (AX - 1, H - 1)
    img = hh.blood(M, img, seed=21, n=6)
    on = flag_cells(rnd); fm = lay_flags(img, on, F, rnd)
    cv = Canvas(img)
    used = np.zeros((H, W), object)
    for (x, y) in F: used[y, x] = 'cliff'
    # the woods far below, all round: Odyssey's pines, darkened and greyed (they are far down, in the fog)
    for y in range(H):
        for x in range(W):
            if E[y, x] == 0:
                pair = (0x289, 0x28a) if (y % 2) else (0x283, 0x284)
                rgb, a = piece(pair[x % 2]); cellput(cv.img, x, y, hh.TEAL); cv.put(rgb, a, x * S, y * S, layer='bottom'); used[y, x] = 'woods'
                c = cv.img[y * S:y * S + S, x * S:x * S + S].astype(float)
                cv.img[y * S:y * S + S, x * S:x * S + S] = (c * 0.55 + np.array((70, 70, 84)) * 0.45).astype(np.uint8)
    # the bastion
    brgb, bwalk = BA.bastion()
    cv.img[BY * S:(BY + BA.CH) * S, BX * S:(BX + BA.CW) * S] = brgb
    tm = BA.top_mask()                                       # (its columns' upper drums: over the player)
    reg = (slice(BY * S, (BY + BA.CH) * S), slice(BX * S, (BX + BA.CW) * S))
    cv.top[reg][tm] = brgb[tm]; cv.top_a[reg] |= tm
    for y in range(BA.CH):
        for x in range(BA.CW): used[BY + y, BX + x] = 'bwalk' if bwalk[y, x] else 'bastion'
    used[DOOR[1], DOOR[0]] = 'door'
    # the court's paving meets the bastion's floor; the cracks run out from the stele over both
    fm[COURT_TOP * S - 2 * S:COURT_TOP * S, :] |= False
    cracks(cv.img, fm, rnd)
    for i, m in enumerate((0x2e5, 0x2ed)):
        rgb, a = piece(m); cv.put(rgb, a, STELE[0] * S, (STELE[1] + i) * S, foot=(STELE[1] + 1) * S + 10); used[STELE[1] + i, STELE[0]] = 'stele'
    for k, (px, py) in enumerate(PLINTHS):
        rgb, a = plinth(k, broken=k == 3); cv.put(rgb, a, px * S, py * S, foot=(py + 1) * S + 6)
        for dy in range(2):
            for dx in range(2): used[py + dy, px + dx] = 'plinth'
    ax, ay = ARRIVE
    for dx, (t, b) in enumerate(((0x330, 0x332), (0x32c, 0x333), (0x32c, 0x333), (0x32c, 0x334), (0x330, 0x331))):
        for dy, m in enumerate((t, b)):
            cv.put((to_bone(ody(m)) * 0.86).astype(np.uint8), np.ones((16, 16), bool), (ax + dx) * S, (ay + dy) * S, layer='bottom')
            used[ay + dy, ax + dx] = 'arrive' if 1 <= dx <= 3 else 'plinth'
    B5, V1 = columns(); parts = B5.column_parts()
    breach(cv, rnd, B5)
    for (x, y) in COLS:
        if (x, y) in FALLEN:
            rgb, a = B5.laz_fallen(2, rnd); X = x * S + 10
            cv.put(rgb, a, X, y * S + 8 - rgb.shape[0] // 2, foot=y * S + 10)
            used[y, x + 1] = used[y, x + 2] = 'column'
            rgb, a = B5.column(1, True, rnd, parts)
        else:
            rgb, a = B5.column(3 if (x, y) in STANDING else rnd.choice((1, 2)), (x, y) not in STANDING, rnd, parts)
        cv.put(rgb, a, x * S, (y + 1) * S - rgb.shape[0], foot=(y + 1) * S - 5); used[y, x] = 'column'
    for k, (x, y) in enumerate(((AX - 8, 41), (AX + 8, 42), (AX - 13, 33), (AX + 13, 37), (AX + 6, 29))):
        if used[y, x] == 0 and E[y, x] == 3: rgb, a = webbed_rock(k); cv.put(rgb, a, x * S, y * S); used[y, x] = 'rock'
    def tree(x, y, kind):
        ids = ((0x2a0,), (0x2a8,)) if kind == 'dead' else ((0x281, 0x282), (0x289, 0x28a), (0x291, 0x292))
        hgt, wid = len(ids), len(ids[0])
        if any(used[y + dy, x + dx] != 0 or E[y + dy, x + dx] != 3 for dy in range(hgt) for dx in range(wid)) or \
           any(fm[(y + dy) * S + 8, (x + dx) * S + 8] for dy in range(hgt) for dx in range(wid)): return False
        for dy, row in enumerate(ids):
            for dx, m in enumerate(row):
                rgb, a = piece(m); cv.put(rgb, a, (x + dx) * S, (y + dy) * S, foot=(y + hgt - 1) * S + 4); used[y + dy, x + dx] = 'tree'
        return True
    for x, y, k in ((7, 33, 'pine'), (33, 32, 'pine'), (9, 38, 'pine'), (31, 39, 'pine'),
                    (12, 30, 'dead'), (30, 29, 'dead'), (13, 41, 'dead'), (28, 42, 'dead'), (34, 36, 'dead')):
        if not tree(x, y, k): print('no room for', k, x, y)
    for x, y in ((14, 35), (28, 34), (11, 42), (32, 30), (26, 41)):
        if used[y, x] == 0 and not fm[y * S + 8, x * S + 8]:
            rgb, a = piece(0x290); cv.put(rgb, a, x * S, y * S, layer='bottom'); used[y, x] = 'grass'
    for (x0, y0, n) in ((8, 35, 7), (33, 34, 6), (15, 42, 5), (25, 43, 4)):
        for (x, y) in blob(rnd, x0, y0, n):
            if 0 <= x < W and 0 <= y < H and used[y, x] == 0 and E[y, x] == 3 and not fm[y * S:y * S + S, x * S:x * S + S].any():
                rgb, a = piece(0x2b8); cv.put(rgb, a, x * S, y * S, layer='bottom'); used[y, x] = 'grass'
    webs(cv, rnd)
    return cv, E, F, used, DOOR, fm

def walk_check(E, used, door):
    ok = np.zeros((H, W), bool)
    for y in range(H):
        for x in range(W): ok[y, x] = used[y, x] in ('bwalk', 'door', 'grass', 'arrive') or (used[y, x] == 0 and E[y, x] == 3)
    start = (AX, ARRIVE[1] + 1); seen = {start}; todo = [start]
    while todo:
        x, y = todo.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            xx, yy = x + dx, y + dy
            if not (0 <= xx < W and 0 <= yy < H) or (xx, yy) in seen or not ok[yy, xx]: continue
            seen.add((xx, yy)); todo.append((xx, yy))
    need = {'the door': door, 'top landing': (AX, BY + 6), 'court': (AX, COURT_TOP + 1), 'plinth NW': (PLINTHS[0][0], PLINTHS[0][1] + 2),
            'colonnade W': (AX - 10, 35), 'colonnade E': (AX + 10, 35)}
    return [k for k, p in need.items() if p not in seen], seen

def main(outdir):
    cv, E, F, used, door, fm = compose()
    img = cv.flat()
    miss, seen = walk_check(E, used, door)
    os.makedirs(outdir, exist_ok=True)
    Image.fromarray(img).save(os.path.join(outdir, 'summit_mock_v2_clear.png'))
    fg = hh.fog(img, seed=5, amount=0.30)
    Image.fromarray(fg).save(os.path.join(outdir, 'summit_mock_v2.png'))
    dbg = img.copy()
    for (x, y) in seen: dbg[y * S + 6:y * S + 10, x * S + 6:x * S + 10] = (0, 255, 0)
    Image.fromarray(dbg).save(os.path.join(outdir, 'summit_walk_debug.png'))
    assert not miss, ('cut off', miss)
    print('ok: door', door)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/tmp/summit')
