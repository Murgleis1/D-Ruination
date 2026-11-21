"""Mirroh mock (zone plan v3 approved by the user 2026-11-21; bible/20_chapter1_build.md, Mirroh).

A walled city climbing the Mirroh massif, a mix of a Crown village and MonoMyth's Fort Elderflower: light snow in
the lower town, deeper uphill; gothic, gloomy, wintry. Three terraces behind crenellated walls, stairs staggered so
the way winds up; walk-through gatehouses south (from Hollow Hill) and north-west (toward the mountain and the Templar
HQ); an open path north-east to the Necropolis.

Pieces, each laid as whole blocks cut from its own map (so its tiles meet as their artist drew them):
  Fort Elderflower (MonoMyth, its map 0x86960C): the snow, the dark paving and its snow drifts, the crenellated city
    walls, the terrace walls with their stairs, the keep's door (the gatehouses), the lamp posts, the small houses,
    the lodge that is Pelluca's Tavern (here in Mirroh's dark slate);
  Pokemon Crown (Blah and the Crown team, with permission): its walled capital's brick townhouses (slate roofs), the
    dragon statues (gargoyles), benches, barrels; the front of its cathedral as a small gothic chapel;
  Ghost Grey (JoeyZeed, with permission): Opal Village's sheets of reflecting ice in their brick rims (Game Boy grey,
    coloured here);
  Hollow Hill's own blocks along the south edge (the seam: Hollow Hill's row 0 is below Mirroh's last row).
Usage: python3 tools/art/mirroh/mirroh_mock.py [outdir]
"""
import os, sys, struct
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'route11'))
import kit
from kit import RL

W, H = 60, 72
SEAM = 64                       # rows 64-71 are Hollow Hill's own blocks (its rows 1, 0, 1, 0... upward)
HHX = 12                        # Mirroh's x = Hollow Hill's x + HHX (Hollow Hill's way north, its columns 16-19, is 28-31 here)
SRC = '/home/claude/scratch/mirroh'

def _atlas(name): return np.load(os.path.join(SRC, name + '.npz'))
ATL = {k: _atlas(v) for k, v in (('ef', 'mm_elderflower'), ('c33', 'crown33'), ('c32', 'crown32'), ('gg', 'gg_opal'))}

# ------------------------------------------------------------------ colours
def recolour(img, pairs):
    out = img.copy(); flat = out.reshape(-1, 3)
    for a, b in pairs.items(): flat[(flat == a).all(1)] = b
    return out
# Ghost Grey's four greys, per kind of piece (it is all Game Boy grey): the ice, the brick rims and fences
GG_ICE = {(248, 248, 248): (228, 242, 250), (168, 168, 168): (160, 204, 230), (80, 80, 80): (96, 140, 186), (0, 0, 0): (44, 64, 104)}
GG_RIM = {(248, 248, 248): (236, 242, 250), (168, 168, 168): (146, 150, 170), (80, 80, 80): (86, 88, 110), (0, 0, 0): (36, 36, 52)}
# Crown's warm town toward Mirroh's gloom: its slate roofs darker, its red brick to soot-dark stone, its greens dimmed
def gloom(img, t=0.28, to=(40, 44, 62), keep_snow=True):
    """Toward Mirroh's gloom: less colour, darker, colder; the snow left white."""
    f = img.astype(float); g = f.mean(-1, keepdims=True)
    out = np.clip((f * 0.7 + g * 0.3) * (1 - t) + np.array(to) * t, 0, 255)
    snowy = (f.min(-1) > 190) & (f.max(-1) - f.min(-1) < 50)
    if keep_snow: out[snowy] = f[snowy]
    return out.astype(np.uint8)
# the cathedral's green copper roof to slate, its pale stone to a cold grey
CATH = None
def slate_roof(img):
    f = img.astype(int); r, g, b = f[..., 0], f[..., 1], f[..., 2]
    green = (g > r + 12) & (g >= b - 8)
    out = img.copy().astype(float)
    lum = f.mean(-1)
    out[green] = np.stack([lum[green] * 0.62, lum[green] * 0.66, lum[green] * 0.82], -1)
    return gloom(out.astype(np.uint8), 0.18)

def piece(src, m):
    a = ATL[src]['full'][m]
    if src == 'gg': return a
    return a

# ------------------------------------------------------------------ the map
class Map:
    def __init__(self):
        self.cell = [[None] * W for _ in range(H)]         # an RGB image per cell
        self.tag = np.full((H, W), None, object)

    def put(self, x, y, img, tag=None):
        if 0 <= x < W and 0 <= y < H:
            self.cell[y][x] = img.copy()
            if tag: self.tag[y, x] = tag

    def overlay(self, x, y, img, alpha, tag=None):
        if 0 <= x < W and 0 <= y < H:
            base = self.cell[y][x] if self.cell[y][x] is not None else np.zeros((16, 16, 3), np.uint8)
            base = base.copy(); base[alpha] = img[alpha]; self.cell[y][x] = base
            if tag: self.tag[y, x] = tag

    def stamp(self, src, sx0, sy0, w, h, x0, y0, tag=None, keep=None, fn=None, skip=()):
        """Copy a w x h block of a source map's cells to (x0, y0). keep(id) -> False leaves the cell as it is (the
        block's own background left out); fn recolours."""
        c = ATL[src]['cells']
        for dy in range(h):
            for dx in range(w):
                m = int(c[sy0 + dy, sx0 + dx])
                if m in skip or (keep and not keep(m)): continue
                img = ATL[src]['full'][m]
                if fn: img = fn(img)
                self.put(x0 + dx, y0 + dy, img, tag)

    def ids(self, src, rows, x0, y0, tag=None, fn=None):
        for dy, row in enumerate(rows):
            for dx, m in enumerate(row):
                if m is None: continue
                img = ATL[src]['full'][m]
                if fn: img = fn(img)
                self.put(x0 + dx, y0 + dy, img, tag)

    def render(self):
        out = np.zeros((H * 16, W * 16, 3), np.uint8)
        for y in range(H):
            for x in range(W):
                if self.cell[y][x] is not None: out[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = self.cell[y][x]
        return out

# ------------------------------------------------------------------ Elderflower's ground
def snow(M, x0, y0, x1, y1, rng):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1): M.put(x, y, ATL['ef']['full'][0xee if rng.random() < 0.05 else 0xed], 'snow')

def pave(M, cells):
    """Streets and squares: Elderflower's dark paving on the cells given, the snow round them meeting it with its own
    drift edges (each snow cell's piece from which of its neighbours are paved)."""
    P = set(cells)
    for x, y in P: M.put(x, y, ATL['ef']['full'][0x275], 'pave')
    for y in range(H):
        for x in range(W):
            if (x, y) in P or M.tag[y, x] not in ('snow', None): continue
            n, s_, e, w = (x, y - 1) in P, (x, y + 1) in P, (x + 1, y) in P, (x - 1, y) in P
            ne, nw, se, sw = (x + 1, y - 1) in P, (x - 1, y - 1) in P, (x + 1, y + 1) in P, (x - 1, y + 1) in P
            m = None
            if (n and s_) or (e and w): m = 0x275; P.add((x, y))                      # (a one-cell gap: paved over)
            elif s_ and e: m = 0x33a
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
            if m is not None: M.put(x, y, ATL['ef']['full'][m], 'pave' if m == 0x275 else 'snow')

def drift(M, x0, y0, x1, y1):
    """A drift of snow lying on the paving (Elderflower's own edge pieces)."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            cx = 0 if x == x0 else 2 if x == x1 else 1; cy = 0 if y == y0 else 2 if y == y1 else 1
            m = ((0x328, 0x329, 0x32a), (0x330, 0x331, 0x332), (0x338, 0x339, 0x33a))[cy][cx]
            M.put(x, y, ATL['ef']['full'][m], 'pave')

def rect(x0, y0, x1, y1): return [(x, y) for y in range(y0, y1 + 1) for x in range(x0, x1 + 1)]

def pine(M, x, y, big=True):
    """Elderflower's snowy pines: the big one (2x3) or the small (1x2)."""
    if big: M.ids('ef', [[0xe9, 0xea], [0xf1, 0xf2], [0xf9, 0xfa]], x, y, 'tree')
    else: M.ids('ef', [[0x109], [0x111]], x, y, 'tree')

# ------------------------------------------------------------------ walls
def city_wall(M, x0, x1, y0):
    """Elderflower's crenellated wall, four rows: crenels, band, face (its shields here and there), foot."""
    rows = ((0x21a, 0x21b, 0x25e), (0x222, 0x223, 0x224), (0x22a, 0x20e, 0x22c), (0x232, 0x233, 0x234))
    for dy, (a, b, c) in enumerate(rows):
        for x in range(x0, x1 + 1):
            m = a if x == x0 else c if x == x1 else b
            if dy == 2 and x not in (x0, x1) and (x - x0) % 9 == 4: m = 0x268
            if dy == 2 and x not in (x0, x1) and (x - x0) % 9 == 5: m = 0x269
            M.put(x, y0 + dy, ATL['ef']['full'][m], 'wall')

def side_wall(M, x0, y0, y1, right=False):
    """The city's side walls running up the slope: Elderflower's wall walk (its east wall)."""
    for y in range(y0, y1 + 1):
        for k, m in enumerate((0x225, 0x226, 0x226, 0x218)):
            M.put(x0 + k, y, ATL['ef']['full'][m], 'wall')

def terrace_wall(M, x0, x1, y0, stairs=()):
    """A terrace's wall: Elderflower's crenels, band, face, foot (rows 11-14 of its map), its stairs three wide
    through it (with their landing on the terrace above and the pillars beside them)."""
    body = ((0x272,), (0x223,), (0x20e,), (0x233,))
    for dy, (m,) in enumerate(body):
        for x in range(x0, x1 + 1):
            M.put(x, y0 + dy, ATL['ef']['full'][m], 'wall')
    for sx in stairs:
        M.stamp('ef', 2, 10, 5, 5, sx - 1, y0 - 1, 'stairs', keep=lambda m: m not in (0x275, 0x2a9, 0x291))
        for dy in range(1, 5): M.tag[y0 - 1 + dy, sx:sx + 3] = 'stairs'

# ------------------------------------------------------------------ buildings
def gatehouse(M, x0, y0, rng):
    """A walk-through gatehouse astride the wall (11x6): the gate of Crown's walled capital, its portcullis the way
    in from the south between lanterns, banners hung either side (House Langerin's, in time); a dark doorway in
    its top, the way out on the far side."""
    M.stamp('c33', 19, 36, 11, 6, x0, y0, 'gate', fn=lambda i: gloom(i, 0.3))
    M.ids('ef', [[0x249, 0x24a, 0x24b]], x0 + 4, y0, 'gate')

def tavern(M, x0, y0):
    M.stamp('ef', 37, 39, 8, 8, x0, y0, 'house', keep=lambda m: m not in (0xed, 0xee, 0xe8), fn=slate)

def ef_house(M, x0, y0):
    M.stamp('ef', 27, 41, 5, 5, x0, y0, 'house', fn=slate)

CROWN_GROUND = None
def _crown_ground():
    """Crown's paving and grass colours (left out of its houses so they stand on Mirroh's snow and stone)."""
    global CROWN_GROUND
    if CROWN_GROUND is None:
        f = ATL['c33']['full']; cols = set()
        for m in (0x8, 0x9, 0xa, 0xb, 0x2, 0x3, 0x1bd, 0x1bc, 0x1be, 0x1bf, 0x1bb, 0x1c6, 0x1b9, 0x1b8, 0x1c1, 0x155, 0x156, 0x14e, 0x15e, 0x138, 0x139):
            cols |= set(map(tuple, f[m].reshape(-1, 3).tolist()))
        CROWN_GROUND = cols
    return CROWN_GROUND

def c33_block(M, sx, sy, w, h, x0, y0, tag='house'):
    """A block of Crown's walled capital, its own ground left out, gloomed."""
    c = ATL['c33']['cells']; G = _crown_ground()
    for dy in range(h):
        for dx in range(w):
            img = ATL['c33']['full'][int(c[sy + dy, sx + dx])]
            a = np.array([[tuple(p) not in G for p in row] for row in img.tolist()])
            if not a.any(): continue
            M.overlay(x0 + dx, y0 + dy, gloom(img), a, tag)

def c33_house(M, kind, x0, y0):
    """Crown's townhouses: 'small' (5x6), 'long' (7x6), 'shop' (5x6, an awning over its front)."""
    sx, sy, w, h = {'small': (7, 10, 5, 6), 'long': (15, 10, 7, 6), 'shop': (32, 24, 5, 6)}[kind]
    c33_block(M, sx, sy, w, h, x0, y0)

def slate(img):
    """Elderflower's red roofs to Mirroh's dark slate; the rest a shade gloomier."""
    f = img.astype(int); r, g, b = f[..., 0], f[..., 1], f[..., 2]
    red = (r > g + 14) & (r >= b - 6)
    out = img.astype(float)
    lum = f.mean(-1)
    out[red] = np.stack([lum[red] * 0.55 + 10, lum[red] * 0.58 + 12, lum[red] * 0.72 + 24], -1)
    return gloom(out.clip(0, 255).astype(np.uint8), 0.12)

def ice_sheet(M, x0, y0, w, h):
    """Opal Village's reflecting ice sunk in a brick rim (Ghost Grey, coloured): its back wall with the steps down,
    the ice with boulders at its corners, a low fence along its front with a gap."""
    G = lambda m, pal: recolour(ATL['gg']['full'][m], pal)
    for x in range(x0, x0 + w):
        top = 0x2b0 if x == x0 else 0x2b2 if x == x0 + w - 1 else 0x28f
        face = 0x2a7 if x == x0 else 0x2bd if x == x0 + w - 1 else 0x2b5
        if x == x0 + w // 2: top, face = 0x2d3, 0x2b4
        M.put(x, y0, G(top, GG_RIM), 'rim'); M.put(x, y0 + 1, G(face, GG_RIM), 'rim')
    for y in range(y0 + 2, y0 + h - 1):
        for x in range(x0, x0 + w):
            m = 0x29f if x == x0 else 0x2c4 if x == x0 + w - 1 else 0x34b
            corner = (y in (y0 + 2, y0 + h - 2)) and x in (x0 + 1, x0 + w - 2)
            if corner: m = 0x282
            M.put(x, y, G(m, GG_ICE if m in (0x34b, 0x282) else GG_RIM), 'ice')
    y = y0 + h - 1
    for x in range(x0, x0 + w):
        m = 0x295 if x == x0 else 0x293 if x == x0 + w - 1 else 0x2ec
        mid = x0 + w // 2
        if x == mid - 1: m = 0x2e3
        elif x == mid + 1: m = 0x2eb
        elif x == mid: m = 0x34b
        M.put(x, y, G(m, GG_ICE if m == 0x34b else GG_RIM), 'rim' if m != 0x34b else 'ice')

def fence(M, x0, x1, y):
    """Crown's village fence (its seaside farm village), its own grass left out, standing in the snow."""
    f = np.load(os.path.join('/home/claude/scratch/route11/atlas', 'crown31.npz'))['full']
    grass = {(112, 184, 136), (128, 192, 136), (144, 200, 152), (80, 160, 112)}
    for x in range(x0, x1 + 1):
        m = 0x34 if x == x0 else 0x2b if x == x1 else 0x29
        img = f[m]; a = np.array([[tuple(p) not in grass for p in row] for row in img.tolist()])
        M.overlay(x, y, gloom(img, 0.2), a, 'fence')

def lamp(M, x, y):
    M.ids('ef', [[0x245], [0x24d]], x, y, 'thing')

def chapel(M, x0, y0):
    """A small gothic chapel: the front of Crown's cathedral (its spires and the top of its roof, then its west
    front, the rose window and the door), slate roofed."""
    rows = [1, 2, 3, 8, 9, 10, 11, 12, 13, 14]
    for k, sy in enumerate(rows):
        M.stamp('c32', 26, sy, 9, 1, x0, y0 + k, 'chapel', fn=slate_roof,
                keep=lambda m: m not in (0xb1, 0xb2, 0xb4, 0xb9, 0xb0, 0x13, 0x1b, 0x18, 0x19, 0xa9))

def graveyard(M, x0, y0, w, h):
    """Rows of headstones on the snow (DM's own graveyard stone, metatile 0x3A5 of its base camp graveyard)."""
    ts = RL.TS('LAYOUT_MIRROH_BASE_CAMP_GRAVEYARD')
    stone = np.asarray(ts.metatile(0x3A5), np.uint8)
    for y in range(y0, y0 + h, 2):
        for x in range(x0, x0 + w, 2): M.put(x, y, stone, 'grave')

def gargoyle(M, x0, y0):
    """Crown's dragon statue on its plinth, darkened into a gargoyle."""
    c = ATL['c33']['cells']; G = _crown_ground()
    for dy in range(3):
        for dx in range(2):
            img = ATL['c33']['full'][int(c[8 + dy, 22 + dx])]
            a = np.array([[tuple(p) not in G for p in row] for row in img.tolist()])
            M.overlay(x0 + dx, y0 + dy, gloom(img, 0.5, (34, 32, 46), keep_snow=False), a, 'thing')

# ------------------------------------------------------------------ Hollow Hill along the south edge
def hh_seam(M):
    d = open(os.path.join(RL.C, 'data/layouts/HollowHill/map.bin'), 'rb').read()
    v = struct.unpack('<%dH' % (66 * 64), d)
    ts = RL.TS('LAYOUT_HOLLOW_HILL')
    for y in range(SEAM, H):
        r = (H - y) % 2                                    # Hollow Hill's rows 1, 0, 1, 0 ... upward from its top
        for x in range(W):
            hx = x - HHX
            if hx < 0: hx = hx % 2                            # (west of Hollow Hill: its wall's pattern)
            M.put(x, y, np.asarray(ts.metatile(v[r * 66 + hx] & 0x3FF), np.uint8), 'seam')

# ------------------------------------------------------------------ the composition
def compose(seed=3):
    rng = np.random.default_rng(seed)
    M = Map()
    snow(M, 0, 0, W - 1, SEAM - 1, rng)
    hh_seam(M)
    ts = RL.TS('LAYOUT_HOLLOW_HILL'); floor = None
    d = open(os.path.join(RL.C, 'data/layouts/HollowHill/map.bin'), 'rb').read()
    v = struct.unpack('<%dH' % (66 * 64), d); floor = np.asarray(ts.metatile(v[12 * 66 + 18] & 0x3FF), np.uint8)
    pave_cols = set(map(tuple, ATL['ef']['full'][0x275].reshape(-1, 3).tolist()))
    for x in range(W):
        e = ATL['ef']['full'][0x339].copy(); k = np.array([[tuple(p) in pave_cols for p in row] for row in e.tolist()])
        e[k] = floor[k]
        M.put(x, 62, e, 'snow'); M.put(x, 63, floor, 'floor')
    # the streets (lower town, the square, the upper terrace) and the ways out
    P = []
    P += rect(27, 47, 32, 57) + rect(27, 47, 41, 49)                                    # lower town: gate to stairs
    P += rect(10, 52, 26, 53) + rect(33, 52, 34, 57)
    P += rect(15, 27, 45, 41) + rect(39, 42, 41, 42)                                    # the square
    P += rect(8, 36, 14, 38)                                                            # before the Tavern
    P += rect(9, 9, 50, 11) + rect(9, 21, 36, 22) + rect(15, 12, 18, 20) + rect(40, 12, 42, 14) + rect(38, 21, 46, 22)
    P += rect(9, 0, 12, 2) + rect(28, 62, 31, 63) + rect(46, 0, 48, 4)                   # the ways out; the track from Hollow Hill
    pave(M, P)
    # snow lying on the streets (more uphill)
    drift(M, 34, 54, 34, 56); drift(M, 17, 29, 21, 31); drift(M, 39, 38, 44, 40); drift(M, 20, 9, 27, 10)
    drift(M, 31, 10, 36, 10); drift(M, 22, 21, 28, 22)
    # the massif's rock and snowy pines at the sides, the city between
    for x0 in (0, 56):
        for y in range(0, SEAM, 3):
            pine(M, x0 + (y // 3) % 2, y, True)
    # the city walls north and south; gatehouses south (from Hollow Hill) and north-west (toward the mountain)
    city_wall(M, 4, 55, 5); city_wall(M, 4, 55, 58)
    gatehouse(M, 23, 56, rng); gatehouse(M, 5, 3, rng)
    terrace_wall(M, 47, 47, 5, stairs=(46,))                                             # the open way north-east
    # terrace walls between upper and middle, middle and lower, their stairs staggered
    terrace_wall(M, 4, 55, 23, stairs=(15,)); terrace_wall(M, 4, 55, 43, stairs=(39,))
    # upper terrace: the chapel and its graveyard; House Langerin's town house between gargoyles
    chapel(M, 6, 12); graveyard(M, 20, 14, 9, 6)
    c33_house(M, 'long', 38, 15); gargoyle(M, 36, 18); gargoyle(M, 45, 18)
    pine(M, 30, 13); pine(M, 50, 13); pine(M, 52, 16, False)
    # the square: the Tavern, the market (Crown's shop with its awning, a long townhouse), the reflecting ice
    tavern(M, 6, 28)
    c33_house(M, 'shop', 47, 28); c33_house(M, 'long', 47, 35)
    ice_sheet(M, 24, 30, 11, 7)
    pine(M, 15, 27, False); pine(M, 45, 27, False)
    # the lower town: cottages (Elderflower's and Crown's), gardens, the second sheet of ice, pines
    ef_house(M, 6, 47); ef_house(M, 13, 47); ef_house(M, 19, 54); c33_house(M, 'small', 44, 50); c33_house(M, 'small', 50, 50)
    ice_sheet(M, 35, 52, 7, 5)
    fence(M, 6, 17, 55); fence(M, 44, 54, 57)
    for x, y in ((7, 54), (12, 55), (24, 50), (42, 47), (52, 47)): pine(M, x, y, False)
    # lamps along the way
    for x, y in ((26, 52), (33, 50), (14, 33), (46, 40), (19, 25), (37, 20), (31, 11), (12, 6), (44, 6), (26, 56), (34, 56)):
        lamp(M, x, y)
    return M

def fog(img, seed=3, amount=0.22):
    rng = np.random.default_rng(seed); h, w = img.shape[:2]
    def smooth(cell):
        g = rng.random((h // cell + 2, w // cell + 2))
        return np.array(Image.fromarray((g * 255).astype(np.uint8)).resize((g.shape[1] * cell, g.shape[0] * cell), Image.BICUBIC))[:h, :w] / 255.0
    n = np.clip((smooth(96) * 0.6 + smooth(40) * 0.4 - 0.25) * 1.6, 0, 1)[..., None] * amount
    return (img * (1 - n) + np.array([190, 198, 214], float) * n).astype(np.uint8)

LABELS = [((28, 64), 'from Hollow Hill'), ((28, 58), 'south gatehouse'), ((10, 3), 'north-west gatehouse (the mountain, the Templar HQ)'),
          ((47, 3), 'open path to the Necropolis'), ((9, 31), 'Tavern'), ((48, 29), 'market'), ((28, 32), 'reflecting ice'),
          ((37, 53), 'reflecting ice'), ((9, 14), 'chapel'), ((22, 15), 'graveyard'), ((40, 16), 'House Langerin'),
          ((8, 48), 'cottages'), ((16, 24), 'stairs'), ((40, 44), 'stairs')]

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
    Image.fromarray(img).save(os.path.join(outdir, 'mirroh_mock.png'))
    Image.fromarray(img).resize((W * 32, H * 32), 0).save(os.path.join(outdir, 'mirroh_mock_2x.png'))
    Image.fromarray(fog(img)).save(os.path.join(outdir, 'mirroh_mock_fog.png'))
    annotate(img).save(os.path.join(outdir, 'mirroh_mock_labels.png'))
    print(outdir)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/mirroh')
