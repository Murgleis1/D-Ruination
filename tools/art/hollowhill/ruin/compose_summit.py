"""Hollow Hill's summit, art mock v1 (plan B, user 2026-11-25: the summit as its own map; story as proposed).

The sealed door at the knoll's foot opens (later in the game) on a tunnel climbing inside the knoll; it comes out on
the summit through a stair sunk in the ground (Odyssey's own, from its haunted forest), at the south end of one axis:
  arrival stair -> a broken flagstone causeway -> the court: the stele where Phancero was erased, the floor cracked out
  from it, four empty plinths (the Treasures of Ruin) -> a wide stair -> the terrace -> the temple front cut into the
  summit's crag (Odyssey 3.43's, same tileset as Hollow Hill), its middle burst open, the breach webbed shut: the
  guardian's lair. A broken colonnade down both sides of the court (MonoMyth's temple columns, Lazarus' fallen column,
  in the temple's bone stone). Blood webs thickest on the temple; blood run down the crag; bone pines and dead trees
  at the margins; the woods far below round the plateau; fog.
Hollow Hill's own colours (hh_mock.bone): Odyssey's pieces recoloured one for one.
Credits: Pokemon Odyssey (tileset, temple, stele, stair), MonoMyth (columns, webbing), Lazarus (fallen column).
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
W, H = 41, 42
AX = 20                                        # the axis (one cell: the temple, the stele, the stairs are odd widths)
hh.W, hh.H = W, H                              # (hh_mock's shape helpers read these)
ody = hh.ody

# ------------------------------------------------------------------------------------------------- the ground
def levels():
    P1 = hh.clean(hh.rrect(5, 5, 35, 38, 5))         # the summit plateau
    P2 = hh.clean(hh.rrect(9, 5, 31, 18, 3))         # the terrace before the temple
    CR = hh.clean(hh.rrect(12, 5, 28, 11, 2))        # the crag the temple is cut into
    E = hh.cheb_depth(P1, 3) + hh.cheb_depth(P2, 2) + hh.cheb_depth(CR, 2)
    return E, (P1, P2, CR)

# Odyssey 3.43's temple front (x 7..15, y 3..7), its accidents taken out (the dead tree, the vine): columns 0 edge,
# 1 panel, 2 pilaster, 3-5 the tablet and steps, 6 pilaster, 7 panel, 8 edge
TEMPLE9 = [[0x2b1, 0x2b2, 0x2b3, 0x2dd, 0x2f1, 0x2de, 0x2b7, 0x2f1, None],
           [0x2b9, 0x2ba, 0x2bb, 0x2bc, 0x2bd, 0x2be, 0x2bf, 0x2f1, None],
           [0x2c0, 0x2c1, 0x2c2, 0x2c3, 0x2c4, 0x2c5, 0x2c6, 0x2c7, 0x2d8],
           [0x2c8, 0x2c9, 0x2ca, 0x2cb, 0x30b, 0x2cd, 0x2ce, 0x2cf, 0x2d9],
           [0x2d0, 0x2d1, 0x2d2, 0x2d3, 0x2d4, 0x2d5, 0x2d6, 0x2d7, 0x2da]]
SEQ = [0, 1, 2, 1, 2, 3, 4, 5, 6, 7, 6, 7, 8]       # widened to 13: a bay more each side, symmetric
TEMPLE = [[row[c] for c in SEQ] for row in TEMPLE9]
TW = len(SEQ)
TX, TY = AX - TW // 2, 7                            # the temple front: cells TX..TX+12, rows 7..11 (its steps on 11)
STAIR = (AX - 2, 17, 5)                             # the wide stair (x0, top row, width), two bands
PLINTHS = [(AX - 5, 22), (AX + 4, 22), (AX - 5, 29), (AX + 4, 29)]   # 2x2 each, symmetric about the axis
STELE = (AX, 25)                                    # 2e5 over 2ed
ARRIVE = (AX - 2, 34)                               # the sunk stair the tunnel climbs out of (5 wide, 2 rows)
COLS = [(AX - 9, y) for y in (21, 24, 27, 30)] + [(AX + 9, y) for y in (21, 24, 27, 30)]   # the colonnade (foot cells)
STANDING = {(AX - 9, 21), (AX + 9, 24), (AX - 9, 27), (AX + 9, 30), (AX + 9, 21)}
FALLEN = {(AX - 9, 30): +1}                         # lying in toward the court

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
    cs = set()
    for row in TEMPLE:
        for m in row:
            if m and m not in (0x2f1, 0x2dd, 0x2de): cs |= {tuple(c) for c in ody(m).reshape(-1, 3).tolist()}
    cs = [c for c in cs if not (c[1] > c[0] + 10)]                    # (no vine greens)
    return sorted(cs, key=lambda c: -(0.3 * c[0] + 0.55 * c[1] + 0.15 * c[2]))
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
    """the paving, cell by cell: the apron before the temple, the court's square round the stele and the plinths, the
    causeway; broken away at its edges and in holes (never on the axis' walking line)"""
    on = set()
    for x in range(AX - 3, AX + 4):
        for y in range(12, 17): on.add((x, y))                                  # the apron
    for x in range(AX - 6, AX + 7):
        for y in range(20, 32): on.add((x, y))                                  # the court
    for x in range(AX - 2, AX + 3):
        for y in range(19, 34): on.add((x, y))                                  # the axis (stair foot to causeway)
    for (x, y) in list(on):                                                     # ragged edges
        edge = any((x + dx, y + dy) not in on for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        if edge and abs(x - AX) > 1 and rnd.random() < 0.45: on.discard((x, y))
    for _ in range(16):                                                         # holes, a slab or two
        x, y = rnd.randint(AX - 6, AX + 6), rnd.randint(13, 33)
        if abs(x - AX) <= 1: continue
        for c in ((x, y), (x + rnd.choice((0, 1)), y)): on.discard(c)
    return on

def lay_flags(img, on, F, rnd):
    """slabs on the cells; each edge broken irregularly (a pixel noise line), outlined, the floor shadowed below"""
    m = np.zeros((H * S, W * S), bool)
    for (x, y) in on:
        if (x, y) in F: continue
        cellput(img, x, y, ody(rnd.choice(FLAGS))); m[y * S:y * S + S, x * S:x * S + S] = True
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

def temple(cv, rnd):
    """the front, its middle burst open from inside: a jagged dark breach where the carved tablet stood; the cornice's
    broken gap kept (the crag shows through)"""
    T = np.zeros((5 * S, TW * S, 3), np.uint8); A = np.zeros((5 * S, TW * S), bool)
    for r, row in enumerate(TEMPLE):
        for c, m in enumerate(row):
            if m is None or m in (0x2f1, 0x2dd, 0x2de): continue
            rgb, a = piece(m); T[r * S:r * S + S, c * S:c * S + S][a] = rgb[a]; A[r * S:r * S + S, c * S:c * S + S] |= a
    # vines back on two panels (Odyssey's own: its 2c7/2cf vine variants 307/30f)
    for c in (1, 11):
        for r, m in ((2, 0x307), (3, 0x30f)):
            if rnd.random() < 0.8: rgb, a = piece(m); T[r * S:r * S + S, c * S:c * S + S][a] = rgb[a]
    mid = TW // 2
    bx0, bx1, by0, by1 = mid * S - 10, mid * S + S + 10, 2 * S - 8, 4 * S + 2
    void = np.array((16, 12, 20))
    for y in range(by0, by1):
        taper = max(0, (by0 + 12 - y)) // 2
        jl, jr = rnd.randint(-2, 2), rnd.randint(-2, 2)
        T[y, bx0 + taper + jl:bx1 - taper + jr] = void; A[y, bx0 + taper + jl:bx1 - taper + jr] = True
    vd = (T == void).all(-1)
    rim = ~vd & A & (np.roll(vd, 1, 1) | np.roll(vd, -1, 1) | np.roll(vd, 1, 0) | np.roll(vd, -1, 0))
    T[rim] = (58, 50, 64)
    cv.put(T, A, TX * S, TY * S, foot=(TY + 4) * S + 4)
    return (AX, TY + 4)                                                        # the lair's door: the breach's foot

def webs(cv, door, rnd):
    """the guardian's: the net across the breach; webs packed in the corners where the temple meets the crag; sheets
    hung between neighbouring columns down the colonnade; one torn orb between the stair's foot columns"""
    L = np.zeros((H * S, W * S, 4), np.uint8); g = np.random.default_rng(rnd.randint(0, 99999))
    net = hh.web('web_net'); nh, nw = net.shape[:2]
    X = door[0] * S + 8 - nw // 2; Y = (TY + 2) * S - 10
    sl = L[Y:Y + nh, X:X + nw]; mm = net[..., 3] > 0; sl[mm] = net[mm]
    for C, R, anc in ((((TX) * S + 2, (TY + 2) * S + 4), 15, [((TX - 1) * S, TY * S + 6), ((TX + 1) * S, (TY + 1) * S)]),
                      (((TX + TW) * S - 2, (TY + 2) * S + 4), 15, [((TX + TW + 1) * S, TY * S + 6), ((TX + TW - 1) * S, (TY + 1) * S)])):
        hh.orb(L, C, R, anc, g, torn=0.3)
    for x, ys in ((AX - 9, (21, 24)), (AX + 9, (24, 27)), (AX + 9, (21, 24))):
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

# ------------------------------------------------------------------------------------------------- compose
def compose(seed=7):
    rnd = random.Random(seed)
    E, (P1, P2, CR) = levels(); F = faces(E)
    x0, y0, w = STAIR
    for i in range(w):
        for b in range(2):
            assert F.get((x0 + i, y0 + b)) == 0x2f1, ('stair not on a straight edge', x0 + i, y0 + b, F.get((x0 + i, y0 + b)))
            F[x0 + i, y0 + b] = 0x339 if b == 0 else 0x338
    for (x, y), v in list(F.items()):
        if v == 0x2f1 and rnd.random() < 0.10: F[x, y] = rnd.choice([0x2df, 0x2e7])
    img = np.zeros((H * S, W * S, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            cellput(img, x, y, ody(F[x, y]) if (x, y) in F else hh.TEAL)
    class _M: pass
    M = _M(); M.face = F; hh.DOOR = (AX - 1, TY + 4)
    img = hh.blood(M, img, seed=21, n=14)
    on = flag_cells(rnd); fm = lay_flags(img, on, F, rnd); cracks(img, fm, rnd)
    cv = Canvas(img)
    used = np.zeros((H, W), object)
    for (x, y) in F: used[y, x] = 'stair' if F[x, y] in (0x338, 0x339) else 'cliff'
    # the woods far below, all round the plateau (Odyssey's pines, two cells wide, each over the one below)
    for y in range(H):
        for x in range(W):
            if E[y, x] == 0:
                pair = (0x289, 0x28a) if (y % 2) else (0x283, 0x284)
                rgb, a = piece(pair[x % 2]); cv.put(rgb, a, x * S, y * S, layer='bottom'); used[y, x] = 'woods'
    door = temple(cv, rnd)
    for r in range(5):
        for c in range(TW):
            if TEMPLE[r][c] is not None: used[TY + r, TX + c] = 'temple'
    used[door[1], door[0]] = 'door'
    for dx, dy, m in ((-2, 1, 0x2fd), (2, 1, 0x305), (-3, 2, 0x2fe)):           # stones spilled from the breach
        X, Y = door[0] + dx, door[1] + dy
        rgb, a = piece(m); cv.put(rgb, a, X * S, Y * S, foot=Y * S + 6); used[Y, X] = 'rubble'
    for i, m in enumerate((0x2e5, 0x2ed)):
        rgb, a = piece(m); cv.put(rgb, a, STELE[0] * S, (STELE[1] + i) * S, foot=(STELE[1] + 1) * S + 10); used[STELE[1] + i, STELE[0]] = 'stele'
    for k, (px, py) in enumerate(PLINTHS):
        rgb, a = plinth(k, broken=k == 3); cv.put(rgb, a, px * S, py * S, foot=(py + 1) * S + 6)
        for dy in range(2):
            for dx in range(2): used[py + dy, px + dx] = 'plinth'
    ax, ay = ARRIVE
    for dx, (t, b) in enumerate(((0x330, 0x332), (0x32c, 0x333), (0x32c, 0x333), (0x32c, 0x334), (0x330, 0x331))):
        for dy, m in enumerate((t, b)):
            cv.put(ody(m), np.ones((16, 16), bool), (ax + dx) * S, (ay + dy) * S, layer='bottom')
            used[ay + dy, ax + dx] = 'arrive' if 1 <= dx <= 3 else 'plinth'
    B5, V1 = columns(); parts = B5.column_parts()
    for (x, y) in COLS:
        if (x, y) in FALLEN:
            rgb, a = B5.laz_fallen(2, rnd); X = x * S + 10
            cv.put(rgb, a, X, y * S + 8 - rgb.shape[0] // 2, foot=y * S + 10)
            used[y, x + 1] = used[y, x + 2] = 'column'
            rgb, a = B5.column(1, True, rnd, parts)
        else:
            rgb, a = B5.column(3 if (x, y) in STANDING else rnd.choice((1, 2)), (x, y) not in STANDING, rnd, parts)
        cv.put(rgb, a, x * S, (y + 1) * S - rgb.shape[0], foot=(y + 1) * S - 5); used[y, x] = 'column'
    for (x, y, h_) in ((AX - 4, 19, 2), (AX + 4, 19, 3), (TX - 2, TY + 6, 2), (TX + TW + 1, TY + 6, 1)):
        rgb, a = B5.column(h_, h_ < 3, rnd, parts); cv.put(rgb, a, x * S, (y + 1) * S - rgb.shape[0], foot=(y + 1) * S - 5); used[y, x] = 'column'
    rgb, a = B5.laz_fallen(2, rnd); cv.put(rgb, a, (TX + TW - 3) * S, (TY + 7) * S + 2, foot=(TY + 8) * S); used[TY + 7, TX + TW - 3] = used[TY + 7, TX + TW - 2] = 'column'
    for k, (x, y) in enumerate(((TX - 1, TY + 5), (TX + TW, TY + 5), (TX - 3, TY + 8), (AX + 7, 33), (AX - 8, 32))):
        if used[y, x] == 0: rgb, a = webbed_rock(k); cv.put(rgb, a, x * S, y * S); used[y, x] = 'rock'
    def tree(x, y, kind):
        ids = ((0x2a0,), (0x2a8,)) if kind == 'dead' else ((0x281, 0x282), (0x289, 0x28a), (0x291, 0x292))
        hgt, wid = len(ids), len(ids[0])
        if any(used[y + dy, x + dx] != 0 for dy in range(hgt) for dx in range(wid)) or \
           any(fm[(y + dy) * S + 8, (x + dx) * S + 8] for dy in range(hgt) for dx in range(wid)): return False
        for dy, row in enumerate(ids):
            for dx, m in enumerate(row):
                rgb, a = piece(m); cv.put(rgb, a, (x + dx) * S, (y + dy) * S, foot=(y + hgt - 1) * S + 4); used[y + dy, x + dx] = 'tree'
        return True
    for x, y, k in ((9, 9, 'pine'), (30, 9, 'pine'), (8, 22, 'pine'), (31, 27, 'pine'), (8, 30, 'pine'),
                    (12, 13, 'dead'), (28, 14, 'dead'), (14, 33, 'dead'), (27, 20, 'dead'), (30, 33, 'dead')):
        if not tree(x, y, k): print('no room for', k, x, y)
    for x, y in ((13, 26), (27, 25), (10, 34), (29, 12), (11, 15)):
        if used[y, x] == 0 and not fm[y * S + 8, x * S + 8]:
            rgb, a = piece(0x290); cv.put(rgb, a, x * S, y * S, layer='bottom'); used[y, x] = 'grass'
    for x0_, y0_, x1_, y1_ in ((8, 25, 10, 28), (30, 22, 32, 25), (10, 11, 12, 13), (29, 15, 31, 16), (25, 33, 28, 34)):
        for y in range(y0_, y1_ + 1):
            for x in range(x0_, x1_ + 1):
                if used[y, x] == 0 and E[y, x] == E[y0_, x0_] and not fm[y * S:y * S + S, x * S:x * S + S].any():
                    rgb, a = piece(0x2b8); cv.put(rgb, a, x * S, y * S, layer='bottom'); used[y, x] = 'grass'
    webs(cv, door, rnd)
    return cv, E, F, used, door, fm

def walk_check(E, used, door):
    ok = np.zeros((H, W), bool)
    for y in range(H):
        for x in range(W): ok[y, x] = used[y, x] in (0, 'stair', 'grass', 'arrive', 'door') and E[y, x] > 0
    start = (AX, ARRIVE[1] + 1); seen = {start}; todo = [start]
    while todo:
        x, y = todo.pop()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            xx, yy = x + dx, y + dy
            if not (0 <= xx < W and 0 <= yy < H) or (xx, yy) in seen or not ok[yy, xx]: continue
            special = {used[y, x], used[yy, xx]}
            if 'stair' in special and dx: continue
            if not special & {'stair', 'arrive', 'door'} and E[yy, xx] != E[y, x]: continue
            seen.add((xx, yy)); todo.append((xx, yy))
    need = {'the door': door, 'terrace': (AX, TY + 6), 'court': (AX, 22), 'plinth NW': (PLINTHS[0][0], PLINTHS[0][1] + 2),
            'colonnade W': (AX - 9, 26), 'colonnade E': (AX + 9, 26)}
    return [k for k, p in need.items() if p not in seen], seen

def main(outdir):
    cv, E, F, used, door, fm = compose()
    img = cv.flat()
    miss, seen = walk_check(E, used, door)
    os.makedirs(outdir, exist_ok=True)
    Image.fromarray(img).save(os.path.join(outdir, 'summit_mock_v1_clear.png'))
    fg = hh.fog(img, seed=5, amount=0.30)
    Image.fromarray(fg).save(os.path.join(outdir, 'summit_mock_v1.png'))
    dbg = img.copy()
    for (x, y) in seen: dbg[y * S + 6:y * S + 10, x * S + 6:x * S + 10] = (0, 255, 0)
    Image.fromarray(dbg).save(os.path.join(outdir, 'summit_walk_debug.png'))
    assert not miss, ('cut off', miss)
    print('ok: door', door)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/tmp/summit')
