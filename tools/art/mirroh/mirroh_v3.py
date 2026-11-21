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

# ------------------------------------------------------------------ copper: Mirroh's colour, House Langerin's crest's
COPPER = ((44, 22, 20), (74, 36, 26), (112, 58, 36), (150, 82, 48), (186, 112, 66), (222, 160, 108))
PATINA = ((70, 112, 100), (96, 150, 132))
def copper_tone(img):
    """Anything to copper by lightness (the crest's colour)."""
    l = _lum(img.astype(float)) / 255.0
    lo, hi = np.array(COPPER[0], float), np.array(COPPER[5], float)
    return (lo + (hi - lo) * np.clip((l - 0.12) / 0.75, 0, 1)[..., None]).astype(np.uint8)

def to_mirroh(img):
    """Crown's stone restoned (to_ef), its purple banners in copper."""
    out = to_ef(img); f = img.astype(int)
    purple = (f[..., 2] > f[..., 1] + 30) & (f[..., 0] > f[..., 1] + 10)
    out[purple] = copper_tone(img)[purple]
    return out

def cathedral_roof(w, h):
    """The roof of Crown's cathedral as it runs back between its towers (real Crown art: its metal sheets, its
    ridge, the stone band at its back end), cut out between the towers and widened to w pixels at mid-slope, in
    copper. h pixels from its back end down."""
    a = ATL['c32']; cc = a['cells']
    src = np.vstack([np.hstack([a['full'][int(cc[y, x])] for x in range(26, 35)]) for y in range(3, 9)])
    reg = src[:h, 9:135]                              # between the towers; its ridge at x 63
    L, R = reg[:, :63], reg[:, 63:]
    need = w // 2
    while L.shape[1] < need: L = np.concatenate([L[:, :20], L[:, 12:20], L[:, 20:]], axis=1)   # one 8 px strip
    while R.shape[1] < w - need: R = np.concatenate([R[:, :40], R[:, 40:48], R[:, 40:]], axis=1)
    img = np.concatenate([L[:, -need:], R[:, :w - need]], axis=1)
    # only the roof itself (its sheets and their dark outline): not the back towers' feet beside its top
    from scipy.ndimage import binary_dilation
    f = img.astype(int); green = (f[..., 1] > f[..., 0] + 28) & (f[..., 1] > f[..., 2] + 12)
    from scipy.ndimage import label
    lab, n = label(green)                             # (the roof is one sheet: no stray bits of the towers' roofs)
    if n > 1: green = lab == (np.argmax(np.bincount(lab.ravel())[1:]) + 1)
    alpha = binary_dilation(green, np.ones((3, 3), bool))
    # a clean hip: its top edge a straight line down from the ridge's end to each side (the cut leaves it ragged),
    # any sheet newly inside it filled from the same column ten rows down (the pattern repeats every five rows),
    # a dark outline along it
    hh, ww = alpha.shape; mid = ww // 2
    tops = np.array([np.argmax(alpha[:, x]) if alpha[:, x].any() else hh for x in range(ww)], float)
    out = copper_roofs(img)
    o = out.astype(int); cold = o[..., 2] > o[..., 0]   # (its weathering streaks and seams in the copper's own dark,
    out[cold] = copper_tone(out)[cold]                  #  not the stone's blue-grey)
    line = np.zeros(ww)
    for xs in (np.arange(0, mid), np.arange(mid, ww)):
        ok = tops[xs] < hh
        k, b = np.polyfit(xs[ok], tops[xs][ok], 1); line[xs] = k * xs + b
    line -= line[mid - 1:mid + 1].min()                 # (its peak at the top: the far door's mat meets it)
    line = np.clip(np.round(line), 0, hh - 1).astype(int)
    for x in range(ww):
        for y in range(line[x], hh):
            old_edge = abs(y - tops[x]) <= 3 and not green[y, x]      # (the cut's old ragged outline, inside now)
            if not alpha[y, x] or old_edge:
                yy = y + 10
                while yy < hh and not alpha[yy, x]: yy += 5
                if yy < hh: out[y, x] = out[yy, x]
            alpha[y, x] = True
        alpha[:line[x], x] = False
        out[line[x], x] = COPPER[0]
    return out, alpha

def copper_roof(w, h, seed='roof'):
    """A pitched copper roof seen from above, its ridge running back from the middle (the way the roof of Crown's
    cathedral runs back between its towers): standing seams leaning down each slope, staggered joints, the lit west
    slope and the shaded east one, a bright ridge, a little verdigris in the seams near the eaves. w, h in pixels."""
    img = np.zeros((h, w, 3), np.uint8); mid = w // 2
    for y in range(h):
        for x in range(w):
            west = x < mid; d = (mid - 1 - x) if west else (x - mid)
            k = (d + y // 5) % 5                     # seams lean outward as they run down the slope
            base, seam = (COPPER[3], COPPER[2]) if west else (COPPER[2], COPPER[1])
            c = seam if k == 0 or (y % 5 == 4 and k in (1, 2)) else base
            if y >= h - 2: c = COPPER[1] if y == h - 2 else COPPER[0]          # the eave
            if k == 0 and y > h * 0.55 and rnd(seed, x // 3, y // 4) < 0.18:
                c = PATINA[1] if west else PATINA[0]
            img[y, x] = c
        img[y, mid - 1] = COPPER[5]; img[y, mid - 2] = COPPER[4]; img[y, mid] = COPPER[0]
        img[y, 0] = img[y, w - 1] = COPPER[0]
    # snow lying on its upper slopes: a soft drift edge (depth varying smoothly along the roof), shaded east
    knots = [10 + 7 * rnd(seed, 'k', i) for i in range(w // 12 + 2)]
    for x in range(1, w - 1):
        i, t = divmod(x, 12); t /= 12.0
        depth = int(knots[i] * (1 - t) + knots[i + 1] * t)
        for y in range(min(depth + 1, h - 3)):
            west = x < w // 2
            c = (236, 240, 248) if west else (200, 210, 232)
            if y == depth: c = (176, 190, 216) if west else (150, 160, 192)
            img[y, x] = c
    return img

# ------------------------------------------------------------------ the fortress stone: copper-shaded (user 2026-11-21)
# Every wall, tower, parapet, stair and gate of Mirroh in one stone, a cold stone warmed toward copper, to go with
# the copper roofs (the user: the same colour everywhere, for consistency). Mapped by lightness from Elderflower's
# stone (and Crown's restoned); snow on the crenels kept; the paving keeps its dark slate.
CSTONE = np.array([(30, 26, 32), (56, 46, 50), (86, 70, 68), (118, 98, 90), (148, 126, 116), (176, 156, 146),
                   (206, 192, 184), (234, 226, 222)], float)
_EF_STONE_IDS = (0x272, 0x20e, 0x21e, 0x222, 0x22a, 0x307, 0x2a3, 0x22b, 0x216, 0x291, 0x206, 0x2b4, 0x223, 0x233,
                 0x21a, 0x21b, 0x25e, 0x224, 0x22c, 0x232, 0x234, 0x2a5, 0x2ae, 0x2a7, 0x2ab, 0x2b6, 0x2ac, 0x2b5,
                 0x2b7, 0x2bd, 0x2be, 0x2bf, 0x258, 0x25c, 0x260, 0x264, 0x249, 0x24a, 0x24b, 0x250, 0x251, 0x252,
                 0x253, 0x254, 0x259, 0x25a, 0x25b, 0x261, 0x262, 0x263)
def _key(a): a = a.astype(np.int64); return (a[..., 0] << 16) | (a[..., 1] << 8) | a[..., 2]
_STONE_KEYS = np.unique(np.concatenate([_key(ef(m)).ravel() for m in _EF_STONE_IDS] + [_key(_RAMP)]))
def cstone(img):
    """Mirroh's copper-shaded stone: every pixel of the stone's own colours, by lightness, onto CSTONE."""
    f = img.astype(float); l = _lum(f)
    stone = np.isin(_key(img), _STONE_KEYS)
    snow = (l > 214) & (f[..., 2] >= f[..., 0])
    sel = stone & ~snow
    t = np.clip((l - 30) / 200.0, 0, 1) * (len(CSTONE) - 1)
    i = np.floor(t).astype(int); i1 = np.minimum(i + 1, len(CSTONE) - 1); w = (t - i)[..., None]
    out = img.copy(); col = (CSTONE[i] * (1 - w) + CSTONE[i1] * w).astype(np.uint8)
    out[sel] = col[sel]
    return out

def stone_pass(M):
    for y in range(H):
        for x in range(W):
            if M.gtag[y, x] in ('wall', 'gate', 'stairs', 'gate-in') and M.g[y][x] is not None:
                M.g[y][x] = cstone(M.g[y][x])

# ------------------------------------------------------------------ the plan: levels
L = np.zeros((H, W), int)                         # 0 outside; 1 lower town; 2 the square; 3 the sacred terrace
def level(l, x0, y0, x1, y1): L[y0:y1 + 1, x0:x1 + 1] = l
level(1, 3, 0, 56, 50)
level(2, 6, 0, 53, 33)
level(3, 25, 0, 50, 15)
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
        fl = floor(x, y); piece[k] = fl[k]
        if not (fl == pave).all():                      # (on the ice: the drift's dark edge line a cold ice-blue)
            p = piece.astype(int); dark = ~k & (_lum(p.astype(float)) < 150)
            piece[dark] = (132, 160, 196)
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
        t = ne[m]; under = ef(0xed) if M.gtag[y, x + k] == 'snow' else M.g[y][x + k].copy()
        f = t.astype(int); a = f.sum(-1) > 0
        body = np.where(a.any(1))[0]                     # (the mat, six rows, to the foot of its cell: it meets
        if len(body):                                    #  the building behind it)
            r0, r1 = body[0], body[-1]; t2 = np.zeros_like(t); a2 = np.zeros_like(a)
            t2[16 - (r1 - r0 + 1):] = t[r0:r1 + 1]; a2[16 - (r1 - r0 + 1):] = a[r0:r1 + 1]; t, a = t2, a2
        img = tone(t); under[a] = img[a]
        M.ground(x + k, y, under, 'mat')                # (the far door's warp; not restoned: the path shows round it)

def gatehouse(M, x0, ycren, style='roof', far_mat=False, tone=None):
    """A gatehouse on Crown's castle gate (its rows 36-42: crenels, banners, a portcullis between lanterns),
    restoned in Elderflower's stone, with Elderflower's foot. Its door is the portcullis.
    style 'roof' (14 wide): round towers either side, a hip roof behind the crenels (Crown's townhouse's) in
      slate, restoned to the stone's own darks, no timber; the portcullis at columns x0+5..x0+8.
    style 'cathedral' (14 wide, the chosen one, user 2026-11-21): see below.
    style 'towers' (18 wide): no roof; three-wide towers a row taller than the crenellated walk, capped with the
      Necropolis gate's spires (the same family); the portcullis at columns x0+7..x0+10.
    far_mat: the hallway's far door on the city side, a mat on the ground behind it (Ghost Grey's Saffron gates)."""
    c = ATL['c33']['cells']
    tw = 1 if style == 'roof' else 3
    for dy in range(7 if style != 'cathedral' else 0):
        for dx in range(12):
            m = int(c[36 + dy, 20 + dx])
            t = ef(0x21e) if dy == 6 else ef(0x20e) if m == 0x66 else to_mirroh(cr(m))   # (its moat-dark course: wall)
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
    elif style == 'towers':
        body = [[0x2a3, 0x272, 0x272]] + [[0x222, 0x20e, 0x20e]] * 2 + [[0x222, 0x22b, 0x20e]] + \
               [[0x222, 0x20e, 0x20e]] * 2 + [[0x22a, 0x20e, 0x20e], [0x307, 0x21e, 0x21e]]
        for side, xs in ((0, x0), (1, xr)):
            for dy, r in enumerate(body):
                for dx, m in enumerate(r):
                    if side: M.ground(xs + 2 - dx, ycren - 1 + dy, fx(ef(m)), 'gate')
                    else: M.ground(xs + dx, ycren - 1 + dy, ef(m), 'gate')
            _spires(M, xs, ycren - 4, side)
        mx, my = x0 + 7, ycren - 5
    else:   # 'cathedral'
        # 14 wide: Crown's gate core (its columns 22-29: pillar, lantern, the portcullis, lantern, pillar; its banners
        # over the lanterns) between three-wide spired towers, and over the core, running back between the towers,
        # the real roof of Crown's cathedral (its roof between its towers, cut at its ridge's back end), in copper.
        for dy in range(7):
            for dx in range(8):
                m = int(c[36 + dy, 22 + dx])
                if dx in (0, 7) and dy in (0, 1): m = (0x39, 0x45)[dy]       # (no half banners at its ends)
                t = ef(0x21e) if dy == 6 else ef(0x20e) if m == 0x66 else to_mirroh(cr(m))
                M.ground(x0 + 3 + dx, ycren + dy, t, 'gate')
        xr = x0 + 11
        body = [[0x2a3, 0x272, 0x272]] + [[0x222, 0x20e, 0x20e]] * 2 + [[0x222, 0x22b, 0x20e]] + \
               [[0x222, 0x20e, 0x20e]] * 2 + [[0x22a, 0x20e, 0x20e], [0x307, 0x21e, 0x21e]]
        roof, ra = cathedral_roof(10 * 16, 3 * 16)     # (a column wider each side: it runs in behind the towers)
        for dy in range(3):
            for dx in range(10):
                sl = (slice(dy * 16, dy * 16 + 16), slice(dx * 16, dx * 16 + 16))
                t = M.g[ycren - 3 + dy][x0 + 2 + dx].copy(); t[ra[sl]] = roof[sl][ra[sl]]
                M.ground(x0 + 2 + dx, ycren - 3 + dy, t, 'roof')
        # its eave: the roof comes down over the crenels' walk (their top half) to a dark copper edge, its shadow
        # on the wall face under it, the banners still hanging from the wall (user: the roof and the stone did not
        # meet naturally)
        ext = roof[-10:-2]                                 # (the sheets' pattern repeats every five rows)
        for dx in range(8):
            t = M.g[ycren][x0 + 3 + dx].copy()
            band = to_mirroh(cr(0x45))                     # (under the eave plain wall, not the merlons' feet;
            f = cr(int(c[36, 22 + dx])).astype(int)          #  the banners' tops kept)
            ban = (f[..., 2] > f[..., 1] + 30) & (f[..., 0] > f[..., 1] + 10)
            t[8:][~ban[8:]] = band[8:][~ban[8:]]
            t[:8] = ext[:, 16 + dx * 16:32 + dx * 16]
            t[6] = copper_tone(np.full((16, 3), 70, np.uint8))[0]; t[7] = COPPER[0]
            t[8:10] = (t[8:10].astype(float) * 0.62).astype(np.uint8)
            M.ground(x0 + 3 + dx, ycren, t, 'gate')
        for side, xs in ((0, x0), (1, xr)):
            for dy, r in enumerate(body):
                for dx, m in enumerate(r):
                    if side: M.ground(xs + 2 - dx, ycren - 1 + dy, fx(ef(m)), 'gate')
                    else: M.ground(xs + dx, ycren - 1 + dy, ef(m), 'gate')
            _spires(M, xs, ycren - 4, side)
        mx, my = x0 + 5, ycren - 4
    if far_mat:
        # the hallway's far door: no mat (a mat against a roof read wrong, user 2026-11-21): the lane runs on to the
        # gatehouse's back, flat to its roof, and the two cells there are the warp
        for k in (1, 2):
            if M.gtag[my, mx + k] == 'cobble':
                M.ground(mx + k, my, ef((0x208, 0x20a)[k - 1]), 'warp')
            else:
                M.gtag[my, mx + k] = 'warp'

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
    for r in range(4, 8):                               # (beside its front towers: the cathedral's long roof running
        for dx, cols in ((0, slice(0, 9)), (8, slice(7, 16))):    #  back down its sides, not part of our front)
            if b[r][dx] is not None:
                img, a = b[r][dx]; a = a.copy(); a[:, cols] = False; b[r][dx] = (img, a)
    M.place(b, x0, y0, 'chapel', fn=copper_roofs)

def copper_roofs(img):
    """Crown's verdigris-green roofs to Mirroh's copper (a touch of the green kept in the darkest seams); the rest
    restoned."""
    f = img.astype(int); green = (f[..., 1] > f[..., 0] + 28) & (f[..., 1] > f[..., 2] + 12)   # (the roof, not its green-grey stone)
    out = to_ef(slate_roof(img)); cu = copper_tone(img); out[green] = cu[green]
    return out

def langerin(M, x0, y0):
    """House Langerin's town house: Crown's long townhouse, its slate roof in the family's copper."""
    def tone(i):
        f = i.astype(int); blue = (f[..., 2] > f[..., 0] + 18)
        out = gloom(i, keep_snow=False); out[blue] = copper_tone(i)[blue]; return out
    M.place(cut('c33', 15, 10, 7, 6), x0, y0, 'house', fn=tone)

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

def vnoise(x, y, scale, seed):
    """Smooth value noise in [0, 1): random values on a grid every `scale` cells, blended between."""
    gx, gy = x / scale, y / scale; x0, y0 = int(np.floor(gx)), int(np.floor(gy)); tx, ty = gx - x0, gy - y0
    sm = lambda t: t * t * (3 - 2 * t); tx, ty = sm(tx), sm(ty)
    v = lambda i, j: rnd(seed, i, j)
    return (v(x0, y0) * (1 - tx) + v(x0 + 1, y0) * tx) * (1 - ty) + (v(x0, y0 + 1) * (1 - tx) + v(x0 + 1, y0 + 1) * tx) * ty

def _seg_dist(p, a, b):
    p, a, b = np.array(p, float), np.array(a, float), np.array(b, float); ab = b - a
    t = np.clip(np.dot(p - a, ab) / max(np.dot(ab, ab), 1e-9), 0, 1); return np.linalg.norm(p - (a + t * ab))

def snow_field(l, cells, ways, keep, base):
    """Where snow lies on a paved level: in ragged drifts of every size (smooth noise at two scales), a little more
    toward its edges (walls, parapets, the map's top), cleared along the ways; always round `keep`."""
    from scipy.ndimage import distance_transform_edt
    mask = np.zeros((H, W), bool)
    for (x, y) in cells: mask[y, x] = True
    d = distance_transform_edt(mask)
    S = set(); F = {}
    for (x, y) in cells:
        dd = min(d[y, x], y + 1)
        f = base + 0.45 * np.exp(-(dd - 1) / 3.0) + 1.0 * (vnoise(x, y, 6.0, ('s', l)) - 0.5) \
            + 0.45 * (vnoise(x, y, 2.6, ('t', l)) - 0.5)
        w = min(_seg_dist((x, y), a, b) for way in ways for a, b in zip(way, way[1:]))
        if w < 1.6: f -= 1.2 * (1.6 - w) / 1.6
        if any(abs(x - kx) <= 1 and -1 <= y - ky <= 2 for kx, ky in keep): f = max(f, 0.6)
        F[(x, y)] = f
        if f > 0.5: S.add((x, y))
    return S, F

_DUST = {}
def dust_tile(level, seed):
    """Elderflower's paving with snow dusted on it: specks and little tufts, `level` 1 (a few) to 3 (thick);
    two variants each (the in-game build will hold these few pieces)."""
    key = (level, seed)
    if key not in _DUST:
        t = ef(0x275).copy(); n = (0, 5, 11, 19)[level]
        for k in range(n):
            x = int(rnd('dx', level, seed, k) * 15); y = int(rnd('dy', level, seed, k) * 14)
            t[y, x] = (236, 240, 248); t[y, min(x + 1, 15)] = (236, 240, 248)
            if rnd('dz', level, seed, k) < 0.5: t[y + 1, x] = (204, 212, 232)
            if level == 3 and rnd('dw', seed, k) < 0.5: t[max(y - 1, 0), x] = (236, 240, 248)
        _DUST[key] = t
    return _DUST[key]

def dust(M, S, cells, F, ways, l):
    """The paving round the drifts, and here and there in the open, dusted: thicker next to the snow, thinning
    out, none on the swept ways. So the drifts fade into the stone instead of stopping at a hard edge."""
    for (x, y) in cells:
        if (x, y) in S or M.gtag[y, x] != 'pave': continue
        near = min((max(abs(x - a), abs(y - b)) for a in range(x - 2, x + 3) for b in range(y - 2, y + 3)
                    if (a, b) in S), default=9)
        w = min(_seg_dist((x, y), a, b) for way in ways for a, b in zip(way, way[1:]))
        if w < 1.2: continue
        f = F[(x, y)] + (0.35 if near == 1 else 0.15 if near == 2 else 0) + 0.25 * (rnd('du', x, y) - 0.5)
        lev = 3 if f > 0.42 else 2 if f > 0.3 else 1 if f > 0.16 else 0
        if lev:
            sh = M.g[y][x]
            if not (sh == ef(0x275)).all(): continue        # (shaded paving by a wall or parapet left as it is)
            M.ground(x, y, dust_tile(lev, int(rnd('dv', x, y) * 2)), 'pave')

def clean_snow(S, cells):
    """Snow the drift pieces can draw: no crumbs (fewer than five cells), no one-cell necks or tips, no paving
    holes of one or two cells inside it, no cell with bare paving only at two opposite corners."""
    from scipy.ndimage import label
    for _ in range(4):
        S = thick(S & cells)
        m = np.zeros((H, W), bool)
        for (x, y) in S: m[y, x] = True
        lab, n = label(m)
        for i in range(1, n + 1):
            if (lab == i).sum() < 5: S -= {(int(x), int(y)) for y, x in np.argwhere(lab == i)}
        hole = np.zeros((H, W), bool)
        for (x, y) in cells:
            if (x, y) not in S: hole[y, x] = True
        lab, n = label(hole)
        for i in range(1, n + 1):
            if (lab == i).sum() <= 2: S |= {(int(x), int(y)) for y, x in np.argwhere(lab == i)}
        bad = set()
        for (x, y) in S:
            pv = lambda a, b: (a, b) in cells and (a, b) not in S
            if not (pv(x - 1, y) or pv(x + 1, y) or pv(x, y - 1) or pv(x, y + 1)):
                if (pv(x - 1, y - 1) and pv(x + 1, y + 1)) or (pv(x + 1, y - 1) and pv(x - 1, y + 1)): bad.add((x, y))
        S -= bad
    return thick(S & cells)

def north_wall(M):
    """The city's north wall along the map's top (rows 0-1: Elderflower's back parapet, its snowy crenels and its
    inner face), from wall to wall, broken only by the two gates: nobody leaves north but through them."""
    for x in range(4, 56):
        if any(M.gtag[y, x] in ('gate', 'roof') for y in range(0, 4)) or 7 <= x <= 20 or 39 <= x <= 49: continue
        M.ground(x, 0, ef(0x206), 'wall'); M.ground(x, 1, ef(0x2aa), 'wall')

def flanks(M):
    """Close the flanks: in each three-column strip, stacked bands (top to bottom, chosen by place) of either a
    big pine with a small pine and a buried rock beside it (three rows), or a ridge of rock right across (one row),
    or two small pines beside a big one's... The bands meet exactly, so no cell is left to walk through."""
    for side, xs in (('w', 0), ('e', 57)):
        big_x = xs if side == 'w' else xs + 1          # (the big pines on the outside, the small ones by the wall)
        small_x = xs + 2 if side == 'w' else xs
        y = 0; k = 0
        while y <= 56:
            left = 56 - y + 1
            if left >= 3 and (rnd('fl', side, k) < 0.72 or left in (3,)):
                pine(M, big_x, y, True)
                pine(M, small_x, y, False)
                M.ground(small_x, y + 2, ef(0xe8), 'rock')     # (a snow-buried rock: solid)
                y += 3
            else:
                for dx, m in enumerate((0x105, 0x106, 0x107)):
                    M.ground(xs + dx, y, ef(m), 'rock')
                y += 1
            k += 1

def pine(M, x, y, big):
    for dy in range(3 if big else 2):
        for dx in range(2 if big else 1): M.ground(x + dx, y + dy, ef(0xed), 'snow')
    mm.pine(M, x, y, big)

def compose():
    M = Map()
    for y in range(SEAM):
        for x in range(W): M.ground(x, y, snow_tile(x, y), 'snow')
    mm.hh_seam(M)
    lv = lambda l: {(x, y) for y in range(SEAM) for x in range(W) if L[y, x] == l}

    # --- L2 (the square) and L3 (the sacred terrace): paving, with snow lying on it as it would: drifted deep
    # against the walls, the parapets and round the buildings, thinning out into the open in ragged tongues and
    # islands, and swept clear along the ways people walk (stair to door to gate); deeper on L3 (uphill). The
    # reflecting ice sits in a drift of its own in the square.
    BOULDERS = ((26, 25), (34, 27), (17, 45))
    icef = lambda x, y: recolour(full('gg', 0x282 if (x, y) in BOULDERS else 0x34b), GG_ICE)
    def pool(cx, cy, rx, ry, seed):                     # (the ice in a rounded, uneven shape, two cells thick or more)
        return thick({(x, y) for y in range(cy - ry - 1, cy + ry + 2) for x in range(cx - rx - 1, cx + rx + 2)
                      if ((x - cx) / (rx + 0.5)) ** 2 + ((y - cy) / (ry + 0.5)) ** 2
                      < 1 + 0.3 * (vnoise(x, y, 1.8, seed) - 0.5)})
    ice = pool(30, 26, 5, 2, 'ice')
    WAYS = {2: [((15, 32), (15, 27), (12, 30)), ((44, 32), (44, 28), (46, 27)), ((15, 27), (22, 22), (37, 20)),
                ((44, 28), (40, 22), (37, 20)), ((15, 27), (15, 12)), ((22, 22), (20, 32))],
            3: [((37, 14), (31, 13)), ((37, 14), (40, 11), (44, 10))]}
    KEEP = {2: [(12, 12), (17, 25), (13, 11), (19, 11), (49, 11)],            # pines, lamps: stand in snow
            3: [(36, 2), (38, 4), (36, 6), (38, 8), (36, 10), (40, 12), (43, 13), (47, 12), (48, 10), (38, 11),
                (45, 12)]}
    for l, base in ((2, 0.2), (3, 0.42)):
        cells = lv(l)
        S, F = snow_field(l, cells, WAYS[l], KEEP[l], base)
        yard = set()
        if l == 2:
            yard = {(x, y) for (x, y) in cells
                    if ((x - 30) / 8.0) ** 2 + ((y - 26) / 5.3) ** 2 < 1 + 0.3 * (vnoise(x, y, 2.5, 'yd') - 0.5)}
            S |= yard
        S = clean_snow(S - ice, cells - ice) | (yard - ice)
        near_ice = lambda x, y: any((x + i, y + j) in ice for i in (-1, 0, 1) for j in (-1, 0, 1))
        floor = (lambda x, y: (icef(x, y) if (x, y) in ice else recolour(full('gg', 0x34b), GG_ICE))
                 if near_ice(x, y) else ef(0x275))         # (a bank's drift shows the ice it lies against)
        snow_on(M, S, floor, cells, 'pave')
        dust(M, S, cells - ice, F, WAYS[l], l)
        if l == 2:
            for (x, y) in ice:
                if (x, y) not in S: M.gtag[y, x] = 'ice'

    # --- L1 (the lower town): snow, cobbled lanes
    def lane(pts, half, seed):                          # (a worn lane: its width and line wander a little)
        out = set()
        for y in range(H):
            for x in range(W):
                w = min(_seg_dist((x, y), a, b) for a, b in zip(pts, pts[1:]))
                if w < half + 0.7 * (vnoise(x, y, 3.0, seed) - 0.5): out.add((x, y))
        return out
    C = lane(((10, 41), (20, 40.5), (30, 41.5), (40, 40.5), (50, 41)), 1.25, 'st')   # the street under the wall
    C |= lane(((15, 37), (15, 41)), 1.3, 'w1') | lane(((44, 37), (44, 41)), 1.3, 'w2')   # to the stairs up
    C |= lane(((30.5, 41), (30.5, 46)), 1.1, 'gt')                   # to the south gatehouse's back
    C |= lane(((10, 41), (9, 46)), 1.2, 'w3') | lane(((50, 41), (51, 47)), 1.2, 'w4')    # the cottages, the market
    C |= {c for c in rect(29, 43, 32, 46) if ((c[0] - 30.5) / 2.2) ** 2 + ((c[1] - 46) / 2.4) ** 2 < 1}  # (its foot)
    C = thick(C & lv(1)) | (rect(30, 45, 31, 46))
    cobbles(M, C)
    # a small frozen pond by the cottages (the same ice, its snow drifting onto it)
    pond = pool(18, 46, 2, 1, 'pond'); pondyard = {c for c in rect(14, 43, 22, 49)
                                                 if ((c[0] - 18) / 4.6) ** 2 + ((c[1] - 46) / 3.4) ** 2 < 1.15} | pond
    snow_on(M, thick(pondyard - pond), icef, pondyard, 'snow')
    for c in pond: M.gtag[c[1], c[0]] = 'ice'
    # --- L0 (outside): the cobbled way up from Hollow Hill to the south gatehouse
    C0 = thick(lane(((30.5, 57), (30, 59.5), (30.8, SEAM - 2.6)), 1.6, 'hh'))
    cobbles(M, C0)

    walls(M)
    stair(M, 15, 33); stair(M, 44, 33)                               # lower town -> square
    stair(M, 37, 15)                                                 # square -> sacred terrace
    gatehouse(M, 24, 50, style='cathedral', far_mat=True, tone=lambda i: copper_tone(i))   # south, from Hollow Hill
    gatehouse(M, 7, 4, style='cathedral')                            # north-west, to the mountain
    necro_gate(M, 39, 0)                                             # north-east, to the Necropolis

    # --- L3: the chapel, its graveyard loose among small pines on the snow, the way to the Necropolis gate
    chapel(M, 26, 2)
    graves = [(36, 2), (38, 4), (36, 6), (38, 8), (36, 10), (40, 12), (43, 13), (47, 12), (48, 10)]
    for x, y in graves: mm.headstone(M, x, y)
    for x, y in ((38, 11), (45, 12)): mm.pine(M, x, y, False)
    # --- L2: the Tavern (west), House Langerin's town house between its gargoyles (east), benches by the ice
    mm.tavern(M, 9, 22)
    langerin(M, 43, 21); mm.gargoyle(M, 41, 24); mm.gargoyle(M, 50, 24)
    for x, y in ((24, 30), (36, 30)): bench(M, x, y)
    for x, y in ((12, 12), (17, 25)): mm.pine(M, x, y, False)
    # --- L1: cottages west, the market east (Crown's shop and a townhouse), barrels, a bench
    mm.ef_house(M, 4, 43); mm.c33_house(M, 'small', 9, 43)
    mm.c33_house(M, 'shop', 49, 43); mm.c33_house(M, 'long', 41, 43)
    mm.barrels(M, 54, 46); mm.barrels(M, 48, 48); mm.barrels(M, 54, 47); bench(M, 26, 44)
    for x, y in ((20, 43), (4, 33), (55, 34)): mm.pine(M, x, y, False)
    for x, y in ((4, 2), (54, 6), (4, 19), (54, 23)): mm.pine(M, x, y, True)
    for x, y in ((6, 11), (55, 15), (5, 27)): rock(M, x, y)
    fence(M, 4, 14, 49, gaps=(9,)); fence(M, 41, 54, 49, gaps=(47,))
    # --- L0: the flanks. Nobody gets round Mirroh (user 2026-11-21): the three columns either side of the walls,
    # from the map's top down to the city wall's foot, are closed by the massif's own pinewood and rock (every
    # cell a tree, a boulder or a rock ridge; Elderflower's pines and its rock ledges 105/106/107)
    flanks(M)
    north_wall(M)
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
    stone_pass(M)
    for x, y in ((13, 37), (17, 37), (42, 37), (46, 37), (35, 12), (39, 12), (28, 41), (35, 41), (27, 57), (34, 57),
                 (13, 11), (19, 11), (49, 11), (19, 28), (47, 27), (7, 41), (52, 41)):
        if M.free(x, y, 1, 2, ground=('snow', 'pave', 'cobble')): mm.lamp(M, x, y)
        else: print('no room for a lamp at', x, y)
    return M

def audit(M):
    bad = []
    for y in range(H):
        for x in range(W):
            if M.g[y][x] is None: bad.append(('no ground', x, y))
            o, g = M.otag[y, x], M.gtag[y, x]
            if o and o != 'spire' and g in ('wall', 'stairs', 'ice', 'gate', 'gate-in', 'roof'): bad.append((o, 'on', g, x, y))
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
