"""Mirroh mock v2 (zone plan v3 approved 2026-11-21; the user's notes on the first draft, 2026-11-21: gatehouses as
real walk-through buildings, every piece cleanly cut out, the ice set in snow, a looser graveyard, no tile cut from
its old ground, everything audited).

A walled city climbing the Mirroh massif, a mix of a Crown village and MonoMyth's Fort Elderflower; light snow in
the lower town, deeper uphill; gothic, gloomy, wintry. Three terraces behind crenellated walls, stairs staggered so
the way winds up; walk-through gatehouses south (from Hollow Hill) and north-west (toward the mountain and the Templar
HQ), each a building with its front door and a doormat on its far side into a hallway map; an open stair north-east
to the Necropolis.

How pieces are laid: Mirroh's own ground first (Elderflower's snow, its dark paving, the drifts where they meet), then
every object cut out of its source map: a pixel of the object is dropped only where it is exactly the pixel of its
source's own ground at that place (the ground tiles round it in its map), so nothing of its old ground comes along
and it stands on Mirroh's.

Pieces: Fort Elderflower (MonoMyth, its map 0x86960C): snow, paving, drifts, the crenellated walls, the terrace walls
and stairs, lamp posts, snowy pines, its small houses, its lodge (Pelluca's Tavern, here in dark slate); Pokemon Crown
(Blah and the Crown team, with permission): the walled capital's gate (the gatehouses' fronts), its townhouses, its
dragon statues (gargoyles), its barrels; the front of its cathedral as the chapel; its seaside village's fence;
Ghost Grey (JoeyZeed, with permission): Opal Village's reflecting ice in its brick rim (coloured); Dreamstone
Mysteries' own headstones (its Mirroh Base Camp graveyard); Hollow Hill's own blocks along the south edge.
Usage: python3 tools/art/mirroh/mirroh_mock.py [outdir]
"""
import os, sys, struct, json
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'route11'))
import kit
from kit import RL

W, H = 60, 72
SEAM = 64                       # rows 64-71: Hollow Hill's own blocks (its rows 1, 0, 1, 0 ... upward from its top)
HHX = 12                        # Mirroh x = Hollow Hill x + 12 (Hollow Hill's way north, its columns 16-19, is 28-31 here)
SRC = '/home/claude/scratch/mirroh'

def _npz(p): return np.load(p)
ATL = {'ef': _npz(f'{SRC}/mm_elderflower.npz'), 'c33': _npz(f'{SRC}/crown33.npz'), 'c32': _npz(f'{SRC}/crown32.npz'),
       'gg': _npz(f'{SRC}/gg_opal.npz'), 'c31': _npz('/home/claude/scratch/route11/atlas/crown31.npz')}

def full(src, m): return ATL[src]['full'][m]

# ------------------------------------------------------------------ cutting pieces out cleanly
_CNT = {}
def _outside(gl):
    """Ground-like pixels joined to the block's border (4-connected), then any opaque crumbs left (8-connected,
    under 40 pixels, cut off from the body: a stray bit of a neighbour) too."""
    from scipy.ndimage import label
    lab, n = label(gl)
    edge = set(lab[0, :]) | set(lab[-1, :]) | set(lab[:, 0]) | set(lab[:, -1]); edge.discard(0)
    drop = np.isin(lab, list(edge))
    from scipy.ndimage import binary_closing, binary_fill_holes
    keep = binary_fill_holes(binary_closing(~drop, np.ones((3, 3), bool), border_value=0) | ~drop)
    drop = ~keep                                        # (no pinholes or ragged teeth along an outline)
    lab2, n2 = label(~drop, structure=np.ones((3, 3), int))
    if n2 > 1:
        sizes = np.bincount(lab2.ravel())
        for i in range(1, n2 + 1):
            if sizes[i] < 40: drop |= lab2 == i
    return drop

def _counts(src):
    if src not in _CNT:
        u, n = np.unique(ATL[src]['cells'], return_counts=True); _CNT[src] = dict(zip(u.tolist(), n.tolist()))
    return _CNT[src]

def cut(src, sx, sy, w, h, ground=(), ring=True, rows=None):
    """The w x h block of a source map at (sx, sy) (or the given source rows, stacked) as RGBA cells, its own ground
    dropped like a magic wand from outside: a pixel is dropped only if it is ground (equal, at the same place, to one
    of the source's ground tiles: those given and those round the block) AND joined to the block's outside through
    ground pixels. Nothing inside a building, a window or a roof can go."""
    c = ATL[src]['cells']; Hs, Ws = c.shape
    g = set(ground)
    rows = list(rows) if rows is not None else list(range(sy, sy + h))
    if ring:                                            # only true ground round the block: ids common in the map
        inside = {int(c[y, x]) for y in rows for x in range(sx, sx + w)}   # (never a building's or a statue's piece,
        cnt = _counts(src)                                                  #  and never a piece of the block itself)
        for y in range(rows[0] - 1, rows[-1] + 2):
            for x in range(sx - 1, sx + w + 1):
                if 0 <= x < Ws and 0 <= y < Hs and not (sx <= x < sx + w and rows[0] <= y <= rows[-1]):
                    m = int(c[y, x])
                    if m not in inside and cnt.get(m, 0) >= 20: g.add(m)
    G = [full(src, m) for m in g]
    hh = len(rows)
    big = np.zeros((hh * 16, w * 16, 3), np.uint8); gl = np.zeros((hh * 16, w * 16), bool); ids = np.zeros((hh, w), int)
    for k, y in enumerate(rows):
        for dx in range(w):
            m = int(c[y, sx + dx]); ids[k, dx] = m; img = full(src, m)
            big[k * 16:k * 16 + 16, dx * 16:dx * 16 + 16] = img
            if m in g: gl[k * 16:k * 16 + 16, dx * 16:dx * 16 + 16] = True
            else:
                for gi in G: gl[k * 16:k * 16 + 16, dx * 16:dx * 16 + 16] |= (img == gi).all(-1)
    cnt = _counts(src)                                  # the map's commonest ground (its grass, its paving): any
    base = [m for m in g if cnt.get(m, 0) >= 200]       # pixel of their colours, joined to the outside, is ground
    if base:
        cols = np.unique(np.concatenate([full(src, m).reshape(-1, 3) for m in base]), axis=0)
        key = lambda a: (a[..., 0].astype(np.int32) << 16) | (a[..., 1].astype(np.int32) << 8) | a[..., 2]
        gl |= np.isin(key(big), key(cols))
    drop = _outside(gl)
    out = []
    for k in range(hh):
        row = []
        for dx in range(w):
            a = ~drop[k * 16:k * 16 + 16, dx * 16:dx * 16 + 16]
            row.append(None if not a.any() else (big[k * 16:k * 16 + 16, dx * 16:dx * 16 + 16].copy(), a))
        out.append(row)
    return out

def cut_ids(src, rows, ground):
    """Cells by id (None: nothing), cut out the same way (the block's outside is the ground given)."""
    c = ATL[src]['cells']
    G = [full(src, m) for m in ground]
    hh, w = len(rows), len(rows[0])
    big = np.zeros((hh * 16, w * 16, 3), np.uint8); gl = np.ones((hh * 16, w * 16), bool)
    for k, r in enumerate(rows):
        for dx, m in enumerate(r):
            if m is None: continue
            img = full(src, m); big[k * 16:k * 16 + 16, dx * 16:dx * 16 + 16] = img
            q = np.zeros((16, 16), bool)
            for gi in G: q |= (img == gi).all(-1)
            gl[k * 16:k * 16 + 16, dx * 16:dx * 16 + 16] = q
    drop = _outside(gl)
    out = []
    for k, r in enumerate(rows):
        row = []
        for dx, m in enumerate(r):
            a = ~drop[k * 16:k * 16 + 16, dx * 16:dx * 16 + 16]
            row.append(None if m is None or not a.any() else (big[k * 16:k * 16 + 16, dx * 16:dx * 16 + 16].copy(), a))
        out.append(row)
    return out

# ------------------------------------------------------------------ colours
def recolour(img, pairs):
    out = img.copy(); flat = out.reshape(-1, 3)
    for a, b in pairs.items(): flat[(flat == a).all(1)] = b
    return out
GG_ICE = {(248, 248, 248): (228, 242, 250), (168, 168, 168): (160, 204, 230), (80, 80, 80): (96, 140, 186), (0, 0, 0): (44, 64, 104)}
GG_RIM = {(248, 248, 248): (236, 242, 250), (168, 168, 168): (146, 150, 170), (80, 80, 80): (86, 88, 110), (0, 0, 0): (36, 36, 52)}

def gloom(img, t=0.28, to=(40, 44, 62), keep_snow=True):
    """Toward Mirroh's gloom: less colour, darker, colder; snow left white."""
    f = img.astype(float); g = f.mean(-1, keepdims=True)
    out = np.clip((f * 0.7 + g * 0.3) * (1 - t) + np.array(to) * t, 0, 255)
    if keep_snow:
        snowy = (f.min(-1) > 190) & (f.max(-1) - f.min(-1) < 50); out[snowy] = f[snowy]
    return out.astype(np.uint8)

def slate(img):
    """Elderflower's red roofs (and any warm red) to Mirroh's dark slate; the rest a shade gloomier."""
    f = img.astype(int); r, g, b = f[..., 0], f[..., 1], f[..., 2]
    red = (r > g + 14) & (r >= b - 6)
    out = img.astype(float); lum = f.mean(-1)
    out[red] = np.stack([lum[red] * 0.55 + 10, lum[red] * 0.58 + 12, lum[red] * 0.72 + 24], -1)
    return gloom(out.clip(0, 255).astype(np.uint8), 0.12)

def slate_roof(img):
    """The cathedral's green copper to slate, its stone colder."""
    f = img.astype(int); r, g, b = f[..., 0], f[..., 1], f[..., 2]
    green = (g > r + 12) & (g >= b - 8)
    out = img.copy().astype(float); lum = f.mean(-1)
    out[green] = np.stack([lum[green] * 0.62, lum[green] * 0.66, lum[green] * 0.82], -1)
    return gloom(out.astype(np.uint8), 0.18, keep_snow=False)

# ------------------------------------------------------------------ the map
class Map:
    def __init__(self):
        self.g = [[None] * W for _ in range(H)]          # the ground (RGB per cell)
        self.gtag = np.full((H, W), None, object)        # 'snow', 'pave', 'wall', 'stairs', 'seam', ...
        self.obj = [[[] for _ in range(W)] for _ in range(H)]   # objects laid on it (RGB, alpha)
        self.otag = np.full((H, W), None, object)        # what stands there ('house', 'tree', 'lamp', ...)

    def ground(self, x, y, img, tag):
        if 0 <= x < W and 0 <= y < H: self.g[y][x] = img.copy(); self.gtag[y, x] = tag

    def place(self, block, x0, y0, tag, fn=None, check=True):
        """Lay a cut-out block; refuse (and report) laying it over another object, a wall, the ice, or off the map."""
        for dy, row in enumerate(block):
            for dx, c in enumerate(row):
                if c is None: continue
                x, y = x0 + dx, y0 + dy
                if not (0 <= x < W and 0 <= y < H): print('REFUSED', tag, (x0, y0), 'off the map'); return False
                if check and self.otag[y, x] is not None: print('REFUSED', tag, (x0, y0), 'over', self.otag[y, x], (x, y)); return False
                if check and self.gtag[y, x] in ('wall', 'stairs', 'ice', 'rim', 'gate', 'gate-in'):
                    print('REFUSED', tag, (x0, y0), 'on', self.gtag[y, x], (x, y)); return False
        for dy, row in enumerate(block):
            for dx, c in enumerate(row):
                if c is None: continue
                img, a = c; img = fn(img) if fn else img
                self.obj[y0 + dy][x0 + dx].append((img, a)); self.otag[y0 + dy, x0 + dx] = tag
        return True

    def free(self, x0, y0, w, h, ground=('snow',)):
        return all(0 <= x < W and 0 <= y < H and self.otag[y, x] is None and self.gtag[y, x] in ground
                   for y in range(y0, y0 + h) for x in range(x0, x0 + w))

    def render(self):
        out = np.zeros((H * 16, W * 16, 3), np.uint8)
        for y in range(H):
            for x in range(W):
                c = self.g[y][x].copy() if self.g[y][x] is not None else np.zeros((16, 16, 3), np.uint8)
                for img, a in self.obj[y][x]: c[a] = img[a]
                out[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = c
        return out

# ------------------------------------------------------------------ ground: snow, paving, drifts
def snow_all(M, rng):
    for y in range(SEAM):
        for x in range(W): M.ground(x, y, full('ef', 0xee if rng.random() < 0.04 else 0xed), 'snow')

def pave(M, cells):
    """Streets and squares: Elderflower's dark paving, the snow round them meeting it with its own drift edges."""
    P = set(c for c in cells if M.gtag[c[1], c[0]] == 'snow')
    changed = True
    while changed:                                        # (fill one-cell gaps, never a sliver of snow)
        changed = False
        for y in range(H):
            for x in range(W):
                if (x, y) in P or M.gtag[y, x] != 'snow': continue
                if ((x, y - 1) in P and (x, y + 1) in P) or ((x - 1, y) in P and (x + 1, y) in P):
                    P.add((x, y)); changed = True
    for x, y in P: M.ground(x, y, full('ef', 0x275), 'pave')
    for y in range(H):
        for x in range(W):
            if M.gtag[y, x] != 'snow': continue
            n, s_, e, w = (x, y - 1) in P, (x, y + 1) in P, (x + 1, y) in P, (x - 1, y) in P
            ne, nw, se, sw = (x + 1, y - 1) in P, (x - 1, y - 1) in P, (x + 1, y + 1) in P, (x - 1, y + 1) in P
            m = None
            if s_ and e: m = 0x33a
            elif s_ and w: m = 0x338
            elif n and e: m = 0x32a
            elif n and w: m = 0x328
            elif s_: m = 0x339
            elif n: m = 0x329
            elif e: m = 0x332
            elif w: m = 0x330
            elif se: m = 0x32e
            elif sw: m = 0x32f
            elif ne: m = 0x336
            elif nw: m = 0x337
            if m is not None: M.ground(x, y, full('ef', m), 'edge')

def rect(x0, y0, x1, y1): return [(x, y) for y in range(y0, y1 + 1) for x in range(x0, x1 + 1)]

def drift(M, x0, y0, x1, y1):
    """Snow lying on the paving (Elderflower's patch pieces), only where all of it is paving."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if M.gtag[y, x] != 'pave': return
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            cx = 0 if x == x0 else 2 if x == x1 else 1; cy = 0 if y == y0 else 2 if y == y1 else 1
            M.ground(x, y, full('ef', ((0x328, 0x329, 0x32a), (0x330, 0x331, 0x332), (0x338, 0x339, 0x33a))[cy][cx]), 'pave')

# ------------------------------------------------------------------ walls (ground-level structures)
def city_wall(M, x0, x1, y0):
    """Elderflower's crenellated wall, four rows: crenels, band, face (its shields here and there), foot."""
    rows = ((0x21a, 0x21b, 0x25e), (0x222, 0x223, 0x224), (0x22a, 0x20e, 0x22c), (0x232, 0x233, 0x234))
    for dy, (a, b, c) in enumerate(rows):
        for x in range(x0, x1 + 1):
            m = a if x == x0 else c if x == x1 else b
            if dy == 2 and x0 < x < x1 and (x - x0) % 9 == 4: m = 0x268
            if dy == 2 and x0 < x < x1 and (x - x0) % 9 == 5: m = 0x269
            M.ground(x, y0 + dy, full('ef', m), 'wall')

def terrace_wall(M, x0, x1, y0, stairs=()):
    """A terrace's wall (Elderflower's rows 11-14: crenels, band, face, foot); its stairs three wide through it, their
    landing on the terrace above, pillars beside them (cut from Elderflower's own stair, its paving dropped)."""
    for dy, m in enumerate((0x272, 0x223, 0x20e, 0x233)):
        for x in range(x0, x1 + 1): M.ground(x, y0 + dy, full('ef', m), 'wall')
    for sx in stairs:
        # Elderflower's stair: columns 2-6, rows 10-14 (landing, steps, pillars), laid as ground
        c = ATL['ef']['cells']
        for dy in range(5):
            for dx in range(5):
                m = int(c[10 + dy, 2 + dx])
                if m in (0x275, 0x291, 0x2a9, 0x2a3, 0x272, 0x226): continue
                M.ground(sx - 1 + dx, y0 - 1 + dy, full('ef', m), 'stairs' if 1 <= dx <= 3 else 'wall')

# ------------------------------------------------------------------ objects
EF_GROUND = (0xed, 0xee, 0xe8, 0x275, 0x226, 0x331)
def lamp(M, x, y):
    M.place(cut_ids('ef', [[0x245], [0x24d]], EF_GROUND), x, y, 'lamp')

def pine(M, x, y, big=True):
    """Elderflower's snowy pines: big (2x3) or small (1x2); only on snow."""
    b = cut_ids('ef', [[0xe9, 0xea], [0xf1, 0xf2], [0xf9, 0xfa]] if big else [[0x109], [0x111]], EF_GROUND)
    M.place(b, x, y, 'tree')

def ef_house(M, x0, y0):
    """Elderflower's small snowy house (5x5), slate roofed."""
    M.place(cut('ef', 27, 41, 5, 5, ground=EF_GROUND), x0, y0, 'house', fn=slate)

def tavern(M, x0, y0):
    """Elderflower's lodge (Pelluca's Tavern), in Mirroh's dark slate (8x8 with its chimney)."""
    b = cut('ef', 37, 39, 7, 8, ground=EF_GROUND)           # (7 wide: the eighth column is Elderflower's wall)
    M.place(b, x0, y0, 'house', fn=slate)

C33_GROUND = (0x8, 0x9, 0xa, 0xb, 0x2, 0x3, 0x1bd, 0x1bc, 0x1be, 0x1bf, 0x1bb, 0x1c6, 0x1b9, 0x1b8, 0x1c1, 0x155,
              0x156, 0x15e, 0x14e, 0x138, 0x139, 0x13a, 0x131, 0x141, 0x157, 0x153, 0x154, 0x15d, 0x15f)
def c33_house(M, kind, x0, y0):
    """Crown's townhouses: 'small' (5x6), 'long' (7x6), 'shop' (5x6, an awning over its front); gloomed."""
    sx, sy, w, h = {'small': (7, 10, 5, 6), 'long': (15, 10, 7, 6), 'shop': (32, 25, 5, 5)}[kind]
    M.place(cut('c33', sx, sy, w, h), x0, y0, 'house', fn=lambda i: gloom(i, keep_snow=False))

def gargoyle(M, x0, y0):
    """Crown's dragon statue on its plinth, darkened into a gargoyle (2x3)."""
    M.place(cut('c33', 22, 8, 2, 3), x0, y0, 'statue',
            fn=lambda i: gloom(i, 0.5, (34, 32, 46), keep_snow=False))

def chapel(M, x0, y0):
    """A small gothic chapel (9x10): the front of Crown's cathedral, its spires and the top of its roof over its west
    front (rose window, door), slate roofed, cold stone."""
    C32_GROUND = (0x1, 0x2, 0x13, 0x14, 0x1b, 0x1c, 0x1d, 0x93, 0x94, 0x95, 0xa9, 0xb0, 0xb1, 0xb2, 0xb4, 0xb9, 0xbb,
                  0x6f, 0x77, 0x18, 0x19, 0x10, 0x11, 0x12, 0xc, 0xd, 0x2e, 0x2f, 0x36, 0x37)
    block = cut('c32', 26, 1, 9, 10, ground=C32_GROUND, ring=False, rows=[1, 2, 3, 8, 9, 10, 11, 12, 13, 14])
    for k in range(3):                                   # (above the roof only the two spires: no stray ridge)
        for dx in range(2, 7): block[k][dx] = None
    M.place(block, x0, y0, 'chapel', fn=slate_roof)

def headstone(M, x, y):
    ts = RL.TS('LAYOUT_MIRROH_BASE_CAMP_GRAVEYARD')
    s, g = np.asarray(ts.metatile(0x3A5), np.uint8), np.asarray(ts.metatile(0x1E3), np.uint8)
    M.place([[(s, ~(s == g).all(-1))]], x, y, 'grave')

def fence(M, x0, x1, y, gaps=()):
    """Crown's village fence (its seaside village), its grass dropped, standing in the snow; gaps for gates."""
    gr = [full('c31', m) for m in (0x7, 0x6, 0x8, 0x1, 0x2, 0x0)]
    for x in range(x0, x1 + 1):
        if x in gaps: continue
        m = 0x34 if x == x0 or (x - 1) in gaps else 0x2b if x == x1 or (x + 1) in gaps else 0x29
        img = full('c31', m); a = np.ones((16, 16), bool)
        for g in gr: a &= ~(img == g).all(-1)
        M.place([[(gloom(img, 0.2), a)]], x, y, 'fence')

def barrels(M, x, y):
    M.place(cut('c33', 12, 15, 1, 1), x, y, 'thing', fn=gloom)

def ice_sheet(M, x0, y0, w, h):
    """Opal Village's reflecting ice in its brick rim (Ghost Grey, coloured), laid as ground: its back wall with the
    steps down, the ice with boulders at its corners, its front rim. In a snowy yard."""
    G = lambda m, pal: recolour(full('gg', m), pal)
    for x in range(x0, x0 + w):
        top = 0x2b0 if x == x0 else 0x2b2 if x == x0 + w - 1 else 0x28f
        face = 0x2a7 if x == x0 else 0x2bd if x == x0 + w - 1 else 0x2b5
        if x == x0 + w // 2: top, face = 0x2d3, 0x2b4
        M.ground(x, y0, G(top, GG_RIM), 'rim'); M.ground(x, y0 + 1, G(face, GG_RIM), 'rim')
    for y in range(y0 + 2, y0 + h - 1):
        for x in range(x0, x0 + w):
            m = 0x29f if x == x0 else 0x2c4 if x == x0 + w - 1 else 0x34b
            if y in (y0 + 2, y0 + h - 2) and x in (x0 + 1, x0 + w - 2): m = 0x282
            M.ground(x, y, G(m, GG_ICE if m in (0x34b, 0x282) else GG_RIM), 'ice')
    for x in range(x0, x0 + w):                                   # the front: Opal's low rim along the snow
        m = 0x2cc if x == x0 else 0x2bc if x == x0 + w - 1 else 0x28f
        M.ground(x, y0 + h - 1, G(m, GG_RIM), 'rim')

# ------------------------------------------------------------------ gatehouses
def gatehouse(M, x0, y0):
    """A walk-through gatehouse (11 wide x 7): a squat stone building astride the wall. Its front is the gate of
    Crown's walled capital (its rows 37-41: banners, the portcullis between lanterns), capped by Elderflower's crenels;
    the portcullis is its front door (into the hallway map); on its far side a dark doormat set in its top (the way
    out of the hallway, as Ghost Grey's and Crown's gates have it)."""
    for dx in range(11): M.ground(x0 + dx, y0, full('ef', 0x21a if dx == 0 else 0x25e if dx == 10 else 0x21b), 'gate')
    c = ATL['c33']['cells']
    for dy in range(5):
        for dx in range(11):
            M.ground(x0 + dx, y0 + 1 + dy, gloom(full('c33', int(c[37 + dy, 19 + dx])), 0.3), 'gate')
    # the far side's doormat: two dark slabs set in the crenels
    mat = full('ef', 0x2ae).copy(); mat = (mat.astype(float) * 0.35 + np.array([20, 20, 30]) * 0.65).astype(np.uint8)
    for dx in (4, 5, 6): M.ground(x0 + dx, y0, mat, 'gate-in')

# ------------------------------------------------------------------ Hollow Hill along the south edge
def hh_seam(M):
    d = open(os.path.join(RL.C, 'data/layouts/HollowHill/map.bin'), 'rb').read()
    v = struct.unpack('<%dH' % (66 * 64), d)
    ts = RL.TS('LAYOUT_HOLLOW_HILL')
    for y in range(SEAM, H):
        r = (H - y) % 2
        for x in range(W):
            hx = x - HHX
            if hx < 0: hx = hx % 2
            M.ground(x, y, np.asarray(ts.metatile(v[r * 66 + hx] & 0x3FF), np.uint8), 'seam')
    # outside the gate: Hollow Hill's floor, snow lying down onto it (Elderflower's drift edge, its paving as the floor)
    floor = np.asarray(ts.metatile(v[12 * 66 + 18] & 0x3FF), np.uint8)
    pave_c = full('ef', 0x275)
    for x in range(W):
        e = full('ef', 0x339).copy(); k = (e == pave_c).all(-1); e[k] = floor[k]
        M.ground(x, SEAM - 2, e, 'snow-floor'); M.ground(x, SEAM - 1, floor, 'floor')

# ------------------------------------------------------------------ the composition
def compose(seed=7):
    rng = np.random.default_rng(seed)
    M = Map()
    snow_all(M, rng); hh_seam(M)
    # the walls first (the terraces' shape), then the streets round them
    city_wall(M, 4, 55, 5); city_wall(M, 4, 55, 58)
    terrace_wall(M, 4, 55, 23, stairs=(17,)); terrace_wall(M, 4, 55, 43, stairs=(40,))
    terrace_wall(M, 46, 48, 5, stairs=(47,))                                          # the open stair north-east
    gatehouse(M, 24, 55); gatehouse(M, 6, 2)
    P = []
    # lower town: from the south gatehouse's doormat north, east to the stairs; lanes to the houses
    P += rect(28, 47, 32, 54) + rect(28, 47, 42, 49) + rect(40, 46, 42, 49)
    P += rect(8, 53, 27, 54) + rect(43, 53, 54, 54) + rect(33, 53, 42, 54)
    # the square: round the ice yard, before the Tavern and the market, up to the west stairs
    P += rect(15, 27, 46, 29) + rect(15, 27, 19, 41) + rect(38, 27, 46, 41) + rect(15, 39, 46, 41)
    P += rect(6, 37, 14, 39) + rect(16, 27, 20, 27)
    # upper terrace: the street from the north-west gatehouse to the stair north-east; the chapel's and the house's
    # forecourts; the lane from the west stairs
    P += rect(8, 9, 49, 10) + rect(16, 11, 19, 22) + rect(6, 22, 15, 22) + rect(36, 20, 48, 22) + rect(46, 11, 48, 11)
    P += rect(10, 0, 12, 1) + rect(46, 0, 48, 4) + rect(28, SEAM - 2, 31, SEAM - 1)
    pave(M, P)
    drift(M, 34, 47, 37, 48); drift(M, 21, 9, 26, 10); drift(M, 31, 9, 34, 10); drift(M, 42, 39, 45, 40)
    drift(M, 16, 31, 18, 33)
    # the ice: in snowy yards, a ring of snow round each
    ice_sheet(M, 24, 31, 11, 7); ice_sheet(M, 18, 47, 7, 5)
    # --- the upper terrace: the chapel, its graveyard (loose rows among small pines, a fence round it), House
    # Langerin's town house between its gargoyles
    chapel(M, 6, 12)
    for x, y in ((21, 14), (24, 13), (28, 14), (30, 13), (23, 17), (26, 16), (29, 18), (21, 19), (25, 19), (31, 16)):
        headstone(M, x, y)
    fence(M, 20, 32, 12); fence(M, 20, 32, 21, gaps=(25, 26))
    pine(M, 33, 15, False); pine(M, 27, 19, False)
    c33_house(M, 'long', 39, 14); gargoyle(M, 37, 17); gargoyle(M, 46, 17)
    for x, y in ((51, 12), (53, 15), (50, 17)): pine(M, x, y, (x + y) % 2 == 0)
    pine(M, 35, 12, True)
    # --- the square: the Tavern, the market (Crown's shop and a townhouse), barrels, the ice yard
    tavern(M, 6, 29)
    c33_house(M, 'shop', 48, 28); c33_house(M, 'long', 48, 35)
    barrels(M, 46, 33)
    for x, y in ((22, 31), (35, 31), (22, 36), (35, 36)): pine(M, x, y, False)
    # --- the lower town: cottages, gardens fenced in the snow, pines
    ef_house(M, 7, 47); ef_house(M, 13, 47); c33_house(M, 'small', 44, 47); c33_house(M, 'small', 50, 47)
    fence(M, 6, 18, 56, gaps=(9, 10, 15, 16))
    for x, y in ((5, 49), (26, 48), (37, 51), (5, 56), (22, 56)): pine(M, x, y, False)
    # --- the massif's pines at the sides (on snow, never over the walls)
    for x0 in (0, 56):
        for y in range(0, SEAM - 3):
            for x in (x0, x0 + 2):
                if (y + x) % 5 == 0 and M.free(x, y, 2, 3): pine(M, x, y, True)
                elif (y * 3 + x) % 7 == 0 and M.free(x, y, 1, 2): pine(M, x, y, False)
    # --- lamps: flanking every stair's foot and landing, at the gatehouses, the Tavern's door, along the streets
    for x, y in ((15, 27), (21, 20), (39, 47), (43, 40), (27, 51), (33, 50), (14, 37), (14, 9), (45, 9), (36, 20),
                 (23, 52), (49, 11), (6, 37), (46, 29), (16, 41)):
        if M.free(x, y, 1, 2, ground=('snow', 'pave', 'edge')): lamp(M, x, y)
        else: print('no room for a lamp at', x, y)
    return M

# ------------------------------------------------------------------ audit
def audit(M):
    """Problems a mock must not have: an object standing on a wall, the ice or a stair; a tree on paving; a cell left
    unset."""
    bad = []
    for y in range(H):
        for x in range(W):
            if M.g[y][x] is None: bad.append(('no ground', x, y))
            o, g = M.otag[y, x], M.gtag[y, x]
            if o and g in ('wall', 'stairs', 'ice', 'rim', 'gate', 'gate-in'): bad.append((o, 'on', g, x, y))
            if o == 'tree' and g not in ('snow',): bad.append(('tree on', g, x, y))
    return bad

LABELS = [((29, 64), 'from Hollow Hill'), ((29, 60), 'south gatehouse (into its hallway)'), ((29, 55), 'its far door (into the city)'),
          ((11, 6), 'north-west gatehouse'), ((11, 2), 'its far door (to the mountain, the Templar HQ)'),
          ((47, 3), 'open stair to the Necropolis'), ((10, 33), 'Tavern'), ((50, 31), 'market'), ((29, 34), 'reflecting ice'),
          ((21, 49), 'reflecting ice'), ((10, 16), 'chapel'), ((26, 16), 'graveyard'), ((42, 16), 'House Langerin'),
          ((9, 50), 'cottages'), ((18, 25), 'stairs'), ((41, 45), 'stairs')]

def annotate(img, scale=2):
    im = Image.fromarray(img).resize((img.shape[1] * scale, img.shape[0] * scale), 0); d = ImageDraw.Draw(im)
    for (x, y), t in LABELS:
        px, py = x * 16 * scale + 8 * scale, y * 16 * scale + 8 * scale
        d.ellipse([px - 7, py - 7, px + 7, py + 7], outline=(255, 230, 80), width=3)
        d.rectangle([px + 10, py - 8, px + 14 + len(t) * 6, py + 8], fill=(20, 20, 30)); d.text((px + 14, py - 6), t, fill=(255, 230, 80))
    return im

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    M = compose(); img = M.render()
    bad = audit(M)
    print('audit:', len(bad), bad[:12])
    Image.fromarray(img).save(os.path.join(outdir, 'mirroh_mock.png'))
    Image.fromarray(img).resize((W * 32, H * 32), 0).save(os.path.join(outdir, 'mirroh_mock_2x.png'))
    annotate(img).save(os.path.join(outdir, 'mirroh_mock_labels.png'))
    return M

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/mirroh')
