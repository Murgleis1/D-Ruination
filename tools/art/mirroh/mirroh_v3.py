"""Mirroh mock v3 (the user's notes on the first draft and on v2, 2026-11-21).

Mirroh climbs the massif in terraces, the way Fort Elderflower does: each terrace a raised, paved level behind its
own crenellated wall, narrower than the one below it, so the city steps up like a ziggurat and its sides step in.
Snow lies on the paving in drifts (Elderflower's own snow-on-paving pieces), deeper uphill; the lower town is snow
with cobbled lanes, Crown-village fashion. Outside the walls: the snowy slope, pines in clumps, snow-buried rocks.

Gates (the user's answers, 2026-11-21):
  south (from Hollow Hill) and north-west (toward the mountain, the Templar HQ): roofed gatehouse buildings, Ghost
    Grey's and Crown's walk-through gates: a slate roof behind the crenels, a stone front with banners, a portcullis
    door between lanterns, round towers either side. The door leads into the gatehouse's hallway map. The south
    one's far door is a short flight of steps up from it on the city side (the city is uphill); the north-west
    one's far door is on the map beyond.
  north-east (to the Necropolis): no guards. A standalone gate: Elderflower's skull arch between two round towers
    capped with gothic spires (Crown's cathedral's); you walk through the dark arch onto the Necropolis map.

Terraces: L0 outside, L1 the lower town (behind the city wall), L2 the square, L3 the sacred terrace (chapel,
graveyard, the Necropolis gate). Usage: python3 tools/art/mirroh/mirroh_v3.py [outdir]
"""
import os, sys, zlib
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mirroh_mock as mm
from mirroh_mock import W, H, SEAM, ATL, full, cut, gloom, slate_roof, recolour, GG_ICE, Map

ef = lambda m: full('ef', m)
cr = lambda m: full('c33', m)
fx = lambda a: a[:, ::-1]
EFC = ATL['ef']['cells']

def rnd(*k):                                     # a stable per-place random number in [0, 1)
    return (zlib.crc32(repr(k).encode()) & 0xFFFF) / 65536.0

# ------------------------------------------------------------------ colour: Crown's stone in Elderflower's
_lum = lambda a: a[..., 0] * 0.3 + a[..., 1] * 0.59 + a[..., 2] * 0.11
_RAMP = np.unique(np.concatenate([ef(m).reshape(-1, 3) for m in (0x20e, 0x272, 0x21e, 0x222)]), axis=0)
_RAMP = _RAMP[np.argsort(_lum(_RAMP.astype(float)))]
_RL = _lum(_RAMP.astype(float))
def to_ef(img):
    """Crown's warm grey stone onto Elderflower's cold lilac-grey (by lightness); its colours (banners, lanterns, the
    slate) kept, a little gloomier."""
    f = img.astype(float); out = _RAMP[np.clip(np.searchsorted(_RL, _lum(f)), 0, len(_RAMP) - 1)].copy()
    col = (f.max(-1) - f.min(-1)) > 60
    out[col] = gloom(img, 0.25)[col]
    return out

# ------------------------------------------------------------------ the plan: levels
L = np.zeros((H, W), int)                         # 0 outside; 1 lower town; 2 the square; 3 the sacred terrace
def level(l, x0, y0, x1, y1): L[y0:y1 + 1, x0:x1 + 1] = l
level(1, 3, 0, 56, 50)
level(2, 7, 0, 53, 33)
level(3, 23, 0, 50, 15)
FACES = {1: 5, 2: 2, 3: 2}                         # face rows under each level's crenels (the city wall is tall)

# ------------------------------------------------------------------ ground
def snow_tile(x, y):
    return ef(0xee) if rnd('fl', x, y) < 0.035 else ef(0xed)

def snow_on(M, S, floor, cells, tag):
    """Snow S (a set of cells) lying on a floor (paving, or the ice): its edge cells take Elderflower's drift pieces,
    the floor's own pixels showing where the piece shows paving. S must be at least two cells thick."""
    pave = ef(0x275)
    for (x, y) in cells:
        if (x, y) in S: continue
        M.ground(x, y, floor(x, y), tag)
    for (x, y) in S:
        isf = lambda a, b: (a, b) in cells and (a, b) not in S
        n, s, e, w = isf(x, y - 1), isf(x, y + 1), isf(x + 1, y), isf(x - 1, y)
        ne, nw, se, sw = isf(x + 1, y - 1), isf(x - 1, y - 1), isf(x + 1, y + 1), isf(x - 1, y + 1)
        m = None
        if n and w: m = 0x328
        elif n and e: m = 0x32a
        elif s and w: m = 0x338
        elif s and e: m = 0x33a
        elif n: m = 0x329
        elif s: m = 0x339
        elif w: m = 0x330
        elif e: m = 0x332
        elif nw: m = 0x337
        elif ne: m = 0x336
        elif sw: m = 0x32f
        elif se: m = 0x32e
        if m is None: M.ground(x, y, snow_tile(x, y), 'snow'); continue
        piece = ef(m).copy(); k = (piece == pave).all(-1)
        piece[k] = floor(x, y)[k]
        M.ground(x, y, piece, 'snow')

def thick(S):
    """Snow thinner than two cells (a one-cell neck or tip) given back to the floor: the drift pieces need two."""
    S = set(S)
    while True:
        bad = {(x, y) for (x, y) in S
               if not any(all((x + dx + i, y + dy + j) in S for i in (0, 1) for j in (0, 1))
                          for dx in (-1, 0) for dy in (-1, 0))}
        if not bad: return S
        S -= bad

def cobbles(M, C):
    """Elderflower's cobbled lanes on the snow (its 200-212 pieces)."""
    for (x, y) in C:
        n, s, e, w = (x, y - 1) in C, (x, y + 1) in C, (x + 1, y) in C, (x - 1, y) in C
        row = 0 if not n else 2 if not s else 1
        col = 0 if not w else 2 if not e else 1
        m = ((0x200, 0x201, 0x202), (0x208, 0x209, 0x20a), (0x210, 0x211, 0x212))[row][col]
        M.ground(x, y, ef(m), 'cobble')

# ------------------------------------------------------------------ walls from the levels
def walls(M):
    """Every terrace's walls from the level map: a front wall where a level drops to the south (crenels on its last
    row, then its face, then its foot, its ends round towers), a parapet where it drops to the west or east (and the
    paving beside it shaded); the paving under a wall's foot in its shadow."""
    for y in range(H - 1):
        for x in range(W):
            l = L[y, x]
            if l == 0 or L[y + 1, x] >= l: continue
            fh = FACES[l]
            left = x == 0 or L[y, x - 1] < l
            right = x == W - 1 or L[y, x + 1] < l
            col = [0x2a3] + [0x222] * (fh - 1) + [0x22a, 0x307] if (left or right) else \
                  [0x272] + [0x22b if rnd('dec', x, y, k) < 0.07 else 0x216 if rnd('dc2', x, y, k) < 0.04 else 0x20e
                             for k in range(fh)] + [0x21e]
            for k, m in enumerate(col):
                t = ef(m); t = fx(t) if right and not left else t
                M.ground(x, y + k, t, 'wall')
            yb = y + fh + 2
            if yb < SEAM and M.gtag[yb, x] == 'pave': M.ground(x, yb, ef(0x2d6), 'pave')
    for y in range(H):
        for x in range(W):
            l = L[y, x]
            if l == 0 or M.gtag[y, x] == 'wall': continue
            if x > 0 and L[y, x - 1] < l:
                M.ground(x, y, ef(0x291), 'wall')
                if M.gtag[y, x + 1] == 'pave': M.ground(x + 1, y, ef(0x2a9), 'pave')
            elif x < W - 1 and L[y, x + 1] < l:
                M.ground(x, y, fx(ef(0x291)), 'wall')
                if M.gtag[y, x - 1] == 'pave': M.ground(x - 1, y, fx(ef(0x2a9)), 'pave')

def stair(M, x, ycren):
    """Elderflower's stair through a terrace wall (crenels and two face rows): its landing on the level above, its
    pillars, its steps; centred on x."""
    for dy in range(5):
        for dx in range(5):
            m = int(EFC[10 + dy, 2 + dx])
            if m in (0x275, 0x338, 0x339, 0x226, 0x246): continue
            M.ground(x - 2 + dx, ycren - 1 + dy, ef(m), 'stairs' if 1 <= dx <= 3 else 'wall')

# ------------------------------------------------------------------ gates
def to_ef_all(img):
    """Every pixel to Elderflower's stone ramp by lightness (no colour kept)."""
    return _RAMP[np.clip(np.searchsorted(_RL, _lum(img.astype(float))), 0, len(_RAMP) - 1)]

def mat(M, x, y, n, tone):
    """A doormat n wide on the ground (North Edelweiss's hall mat, in the runner's colour): the far door of a gate."""
    ne = np.load('/home/claude/scratch/mirroh/ref/mm_ne_gate.npz')['full']
    ids = [0x1cb] + [0x1cc] * (n - 2) + [0x1cd]
    for k, m in enumerate(ids):
        t = ne[m]; under = M.g[y][x + k].copy()
        f = t.astype(int); a = f.sum(-1) > 0
        img = tone(t); under[a] = img[a]
        M.ground(x + k, y, under, 'gate-in')

def gatehouse(M, x0, ycren, style='roof', far_mat=False, tone=None):
    """A gatehouse on Crown's castle gate (its rows 36-42: crenels, banners, a portcullis between lanterns),
    restoned in Elderflower's stone, with Elderflower's foot. Its door is the portcullis.
    style 'roof' (14 wide): round towers either side, a hip roof behind the crenels (Crown's townhouse's) in
      slate, restoned to the stone's own darks, no timber; the portcullis at columns x0+5..x0+8.
    style 'towers' (18 wide): no roof; three-wide towers a row taller than the crenellated walk, capped with the
      Necropolis gate's spires (the same family); the portcullis at columns x0+7..x0+10.
    far_mat: the hallway's far door on the city side, a mat on the ground behind it (Ghost Grey's Saffron gates)."""
    c = ATL['c33']['cells']
    tw = 1 if style == 'roof' else 3
    for dy in range(7):
        for dx in range(12):
            m = int(c[36 + dy, 20 + dx])
            t = ef(0x21e) if dy == 6 else ef(0x20e) if m == 0x66 else to_ef(cr(m))   # (its moat-dark course: wall)
            M.ground(x0 + tw + dx, ycren + dy, t, 'gate')
    xr = x0 + tw + 12
    if style == 'roof':
        for dy, m in enumerate([0x2a3, 0x222, 0x222, 0x222, 0x222, 0x22a, 0x307]):
            M.ground(x0, ycren + dy, ef(m), 'gate'); M.ground(xr, ycren + dy, fx(ef(m)), 'gate')
        rows = ([0x80] + [0x81, 0x82, 0x83, 0x84] * 3, [0x88] + [0x89, 0x8a, 0x8b, 0x8c] * 3,
                [0x90] + [0x91, 0x92, 0x93, 0x94] * 3)
        for dy, r in enumerate(rows):
            r = r[:11]
            roof = [cr(m) for m in r] + [fx(cr(r[0]))]
            for dx, t in enumerate(roof):
                under = M.g[ycren - 3 + dy][x0 + 1 + dx]
                a = ~(t == cr(0x8)).all(-1)                  # (the roof's own corners: Crown's grass under them)
                img = under.copy(); img[a] = to_ef_all(slate_roof(t))[a]
                M.ground(x0 + 1 + dx, ycren - 3 + dy, img, 'gate')
        mx, my = x0 + 5, ycren - 4
    else:
        body = [[0x2a3, 0x272, 0x272]] + [[0x222, 0x20e, 0x20e]] * 2 + [[0x222, 0x22b, 0x20e]] + \
               [[0x222, 0x20e, 0x20e]] * 2 + [[0x22a, 0x20e, 0x20e], [0x307, 0x21e, 0x21e]]
        for side, xs in ((0, x0), (1, xr)):
            for dy, r in enumerate(body):
                for dx, m in enumerate(r):
                    if side: M.ground(xs + 2 - dx, ycren - 1 + dy, fx(ef(m)), 'gate')
                    else: M.ground(xs + dx, ycren - 1 + dy, ef(m), 'gate')
            _spires(M, xs, ycren - 4, side)
        mx, my = x0 + 7, ycren - 1
    if far_mat:
        mat(M, mx, my, 4, tone or crimson_tone)

def crimson_tone(img): return ramp_tone(img, (46, 10, 20), (150, 36, 46))
def ramp_tone(img, lo, hi):
    l = _lum(img.astype(float)) / 255.0; lo, hi = np.array(lo), np.array(hi)
    return (lo + (hi - lo) * np.clip((l - 0.25) / 0.65, 0, 1)[..., None]).astype(np.uint8)
CARPETS = {'brown-purple': ((44, 26, 40), (124, 82, 104)), 'copper': ((50, 24, 16), (158, 88, 54))}

def _spires(M, xs, y0, side):
    global _SPIRE
    if _SPIRE is None: necro_gate(Map(), 0, 0)
    blk = [[None if c is None else ((fx(c[0]), fx(c[1])) if side else c) for c in (r[::-1] if side else r)]
           for r in _SPIRE]
    M.place(blk, xs, y0, 'spire', fn=lambda i: to_ef(slate_roof(i)), check=False)

_SPIRE = None
def necro_gate(M, x0, y0):
    """The Necropolis gate, 11 wide x 10: Elderflower's skull arch (its keep door) under a crenellated walk, between
    two round towers capped with the gothic spires of Crown's cathedral (slate, restoned). No guards: the dark arch
    (x0+5, y0+9) is the way onto the Necropolis map."""
    global _SPIRE
    if _SPIRE is None:
        C32G = (0x1, 0x2, 0x4, 0xa, 0xb, 0xc, 0xd, 0x10, 0x11, 0x12, 0x13, 0x14, 0x18, 0x19, 0x1b, 0x1c, 0x1d, 0x2e,
                0x2f, 0x36, 0x37, 0x6f, 0x77, 0x93, 0x94, 0x95, 0xa9, 0xb0, 0xb1, 0xb2, 0xb4, 0xb9, 0xbb)
        s = cut('c32', 26, 1, 3, 3, ground=C32G, ring=False)
        for k in range(3):                          # (its right column is the cathedral roof's edge: mirror the left)
            s[k][2] = None if s[k][0] is None else (fx(s[k][0][0]), fx(s[k][0][1]))
        _SPIRE = s
    for side, xs in ((0, x0), (1, x0 + 8)):
        blk = [[None if c is None else ((fx(c[0]), fx(c[1])) if side else c) for c in (r[::-1] if side else r)]
               for r in _SPIRE]
        M.place(blk, xs, y0, 'spire', fn=lambda i: to_ef(slate_roof(i)), check=False)
        body = [[0x2a3, 0x272, 0x272], [0x222, 0x20e, 0x20e], [0x222, 0x22b, 0x20e], [0x222, 0x20e, 0x20e],
                [0x222, 0x20e, 0x20e], [0x22a, 0x20e, 0x20e], [0x307, 0x21e, 0x21e]]
        for dy, r in enumerate(body):
            for dx, m in enumerate(r):
                if side: M.ground(xs + 2 - dx, y0 + 3 + dy, fx(ef(m)), 'gate')
                else: M.ground(xs + dx, y0 + 3 + dy, ef(m), 'gate')
    for dx in range(5):
        M.ground(x0 + 3 + dx, y0 + 4, ef(0x2b4), 'gate'); M.ground(x0 + 3 + dx, y0 + 5, ef(0x20e), 'gate')
        for dy in range(4):
            M.ground(x0 + 3 + dx, y0 + 6 + dy, ef(int(EFC[14 + dy, 28 + dx])), 'gate')
    for dx in (1, 2, 3):                                 # the arch's floor: the way through
        M.gtag[y0 + 9, x0 + 3 + dx] = 'gate-in'

# ------------------------------------------------------------------ objects
def chapel(M, x0, y0):
    """The chapel, 9 x 12: the front of Crown's cathedral, its gabled roof between its spires (slate), cold stone."""
    C32G = (0x1, 0x2, 0x13, 0x14, 0x1b, 0x1c, 0x1d, 0x93, 0x94, 0x95, 0xa9, 0xb0, 0xb1, 0xb2, 0xb4, 0xb9, 0xbb,
            0x6f, 0x77, 0x18, 0x19, 0x10, 0x11, 0x12, 0xc, 0xd, 0x2e, 0x2f, 0x36, 0x37)
    b = cut('c32', 26, 1, 9, 12, ground=C32G, ring=False, rows=[1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14])
    for dx in range(3, 6): b[0][dx] = b[1][dx] = None   # (above the roof's peak: the cathedral's woods, not ours)
    M.place(b, x0, y0, 'chapel', fn=lambda i: to_ef(slate_roof(i)))

def fence(M, x0, x1, y, gaps=()):
    mm.fence(M, x0, x1, y, gaps)

def bench(M, x, y): M.place(cut('c33', 6, 15, 1, 1), x, y, 'thing', fn=lambda i: gloom(i, 0.2))
def rock(M, x, y): M.place(mm.cut_ids('ef', [[0xe8]], mm.EF_GROUND), x, y, 'rock')

# ------------------------------------------------------------------ composition
def rect(x0, y0, x1, y1): return {(x, y) for y in range(y0, y1 + 1) for x in range(x0, x1 + 1)}
def rrect_cells(x0, y0, x1, y1, r):
    """A rectangle with rounded (stepped) corners."""
    out = set()
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            dx = max(x0 + r - x, x - (x1 - r), 0); dy = max(y0 + r - y, y - (y1 - r), 0)
            if dx * dx + dy * dy <= r * r + 1: out.add((x, y))
    return out

def blob(cx, cy, rx, ry, seed):
    """An organic patch: an ellipse with a ragged edge (whole cells)."""
    out = set()
    for y in range(cy - ry - 1, cy + ry + 2):
        for x in range(cx - rx - 1, cx + rx + 2):
            d = ((x - cx) / (rx + 0.5)) ** 2 + ((y - cy) / (ry + 0.5)) ** 2
            if d < 1 + 0.35 * (rnd(seed, x, y) - 0.5): out.add((x, y))
    return out

def compose():
    M = Map()
    for y in range(SEAM):
        for x in range(W): M.ground(x, y, snow_tile(x, y), 'snow')
    mm.hh_seam(M)
    lv = lambda l: {(x, y) for y in range(SEAM) for x in range(W) if L[y, x] == l}

    # --- L2 (the square) and L3 (the sacred terrace): paving, with snow lying on it in drifts; the ice in a snowy
    # yard in the square. L3 snowier than L2 (deeper uphill).
    for l, snows in ((2, [blob(14, 24, 4, 3, 'a'), blob(48, 13, 2, 4, 'b'), blob(12, 13, 3, 2, 'c'),
                          rrect_cells(22, 21, 38, 31, 3), blob(44, 30, 3, 1, 'd'), blob(20, 31, 3, 1, 'e')]),
                     (3, [blob(33, 7, 6, 5, 'gy'), blob(46, 13, 3, 1, 'f'), blob(26, 13, 2, 1, 'g')])):
        cells = lv(l); S = set()
        for b in snows: S |= b
        S = thick(S & cells)
        snow_on(M, S, lambda x, y: ef(0x275), cells, 'pave')
    # the reflecting ice, in the square's snowy yard: Opal Village's ice (coloured), the yard's snow drifting onto it
    ice = rect(26, 24, 34, 28)
    yard = thick(rrect_cells(22, 21, 38, 31, 3) & lv(2))
    icef = lambda x, y: recolour(full('gg', 0x282 if (x, y) in ((26, 24), (34, 24), (26, 28), (34, 28)) else 0x34b),
                                 GG_ICE)
    banks = thick({c for c in yard if c not in ice or c in rect(26, 24, 34, 24)} )
    snow_on(M, banks, icef, yard, 'snow')
    for c in ice - banks: M.gtag[c[1], c[0]] = 'ice'

    # --- L1 (the lower town): snow, cobbled lanes
    C = set()
    C |= rect(28, 40, 33, 42) | rect(10, 40, 49, 41)                # the street along the square's wall
    C |= rect(14, 37, 16, 39) | rect(43, 37, 45, 39)                # to the two stairs up
    C |= rect(30, 43, 31, 44)                                       # to the steps up from the south gatehouse
    C |= rect(8, 42, 10, 46) | rect(49, 42, 51, 46)                 # lanes to the cottages, the market
    C &= lv(1)
    cobbles(M, C)
    # a small frozen pond by the cottages (the same ice, its snow drifting onto it)
    pond = rect(18, 45, 22, 47); pondyard = rect(16, 43, 24, 49) - rect(24, 43, 24, 43)
    snow_on(M, thick(pondyard - pond), icef, pondyard, 'snow')
    for c in pond: M.gtag[c[1], c[0]] = 'ice'
    # --- L0 (outside): the cobbled way up from Hollow Hill to the south gatehouse
    C0 = rect(29, 57, 32, SEAM - 3)
    cobbles(M, C0)

    walls(M)
    stair(M, 15, 33); stair(M, 44, 33)                               # lower town -> square
    stair(M, 37, 15)                                                 # square -> sacred terrace
    gatehouse(M, 24, 50, far_mat=True)                                 # south, from Hollow Hill
    gatehouse(M, 8, 3)                                               # north-west, to the mountain
    necro_gate(M, 39, 0)                                             # north-east, to the Necropolis

    # --- L3: the chapel, its graveyard loose among small pines on the snow, the way to the Necropolis gate
    chapel(M, 24, 1)
    graves = [(34, 2), (37, 3), (34, 5), (37, 6), (34, 9), (37, 10), (40, 12), (47, 12), (48, 10)]
    for x, y in graves: mm.headstone(M, x, y)
    for x, y in ((36, 7), (45, 12)): mm.pine(M, x, y, False)
    # --- L2: the Tavern (west), House Langerin's town house between its gargoyles (east), benches by the ice
    mm.tavern(M, 9, 22)
    mm.c33_house(M, 'long', 43, 21); mm.gargoyle(M, 41, 24); mm.gargoyle(M, 50, 24)
    for x, y in ((24, 30), (36, 30)): bench(M, x, y)
    for x, y in ((12, 12), (17, 25)): mm.pine(M, x, y, False)
    # --- L1: cottages west, the market east (Crown's shop and a townhouse), barrels, a bench
    mm.ef_house(M, 5, 43); mm.c33_house(M, 'small', 11, 43)
    mm.c33_house(M, 'shop', 46, 43); mm.c33_house(M, 'long', 37, 43)
    mm.barrels(M, 51, 47); mm.barrels(M, 44, 47); mm.barrels(M, 44, 48); bench(M, 26, 44)
    for x, y in ((17, 43), (53, 44), (4, 33), (55, 34)): mm.pine(M, x, y, False)
    for x, y in ((4, 2), (54, 6), (4, 19), (54, 23)): mm.pine(M, x, y, True)
    for x, y in ((6, 11), (55, 15), (5, 27)): rock(M, x, y)
    fence(M, 5, 16, 49, gaps=(9,)); fence(M, 45, 54, 49, gaps=(49,))
    # --- L0: the slope outside, pines in clumps, rocks under the snow
    for x0, y0 in ((0, 2), (57, 4), (0, 15), (57, 18), (0, 28), (57, 31), (0, 41), (57, 44), (1, 56), (54, 56),
                   (8, 58), (18, 57), (38, 58), (47, 57), (24, 59), (34, 59)):
        if M.free(x0, y0, 2, 3): mm.pine(M, x0, y0, True)
    for x, y in ((2, 8), (58, 11), (2, 22), (58, 25), (2, 35), (58, 38), (2, 49), (58, 51), (13, 59), (44, 60),
                 (5, 58), (51, 59), (21, 61), (40, 61)):
        if M.free(x, y, 1, 2): mm.pine(M, x, y, False)
    for x, y in ((1, 12), (58, 1), (1, 37), (58, 29), (11, 61), (27, 60), (35, 61), (50, 61), (16, 60)):
        if M.free(x, y, 1, 1): rock(M, x, y)
    # --- lamps: at every stair's foot, the gates, the Tavern's and Langerin's doors, along the street
    for x, y in ((13, 37), (17, 37), (42, 37), (46, 37), (35, 12), (39, 12), (28, 41), (35, 41), (27, 57), (34, 57),
                 (22, 10), (38, 10), (49, 11), (19, 28), (47, 27), (7, 41), (52, 41)):
        if M.free(x, y, 1, 2, ground=('snow', 'pave', 'cobble')): mm.lamp(M, x, y)
        else: print('no room for a lamp at', x, y)
    return M

def audit(M):
    bad = []
    for y in range(H):
        for x in range(W):
            if M.g[y][x] is None: bad.append(('no ground', x, y))
            o, g = M.otag[y, x], M.gtag[y, x]
            if o and o != 'spire' and g in ('wall', 'stairs', 'ice', 'gate', 'gate-in'): bad.append((o, 'on', g, x, y))
            if o == 'tree' and g not in ('snow',): bad.append(('tree on', g, x, y))
    return bad

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    M = compose(); img = M.render()
    bad = audit(M); print('audit:', len(bad), bad[:12])
    Image.fromarray(img).save(os.path.join(outdir, 'mirroh_v3.png'))
    Image.fromarray(img).resize((W * 32, H * 32), 0).save(os.path.join(outdir, 'mirroh_v3_2x.png'))
    return M

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/mirroh')
