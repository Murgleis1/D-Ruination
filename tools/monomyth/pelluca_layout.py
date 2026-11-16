"""Pelluca Valley layout v2 -- a deliberate plan built from Wood Avens / Port Ginseng pieces.

The plan is written as regions (forest belts, cliff bands, cobble roads, lake, buildings);
every region is drawn with the piece rules verified on screen in cliff_tests.png:
  forest  : tip 33/34, body 24/23 (edge 22/25), overlap 31/30 (edge 29/32), base 40/41;
            regions are aligned to the 2x2 tree grid (even x, even width)
  cliff   : south-facing band = 10 (lip) over 11 (face); stairs 45/46; band ends run into forest
  cobble  : 9-slice 63 64 65 / 77 78 79 / 130 131 136, inner corners 124 125 133 134
  quay    : pavement 147, wall 155, water under wall 159, open water 162,
            vertical stone edges 160 (water W) / 161 (water E), corners 156 / 158, pier 160 157 161
Output: map.bin-ready grid of (metatile, collision, elevation) + a 1:1 render.

Usage: python3 -I tools/monomyth/pelluca_layout.py codebase OUT_PREFIX
"""
import os, sys, json, struct
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import layout_kit as lk

W, H = 80, 60
GRASS = 6

# ---------------------------------------------------------------- the plan
FOREST = [  # (x0, y0, x1, y1) inclusive; x0 even, width even
    (0, 0, 7, 27), (0, 32, 7, 59),            # west belt, gap y28-31 for Route 11
    (72, 0, 79, 23), (72, 28, 79, 59),        # east belt, gap y24-27 for Hoya Delta
    (8, 0, 17, 3), (22, 0, 35, 3), (42, 0, 71, 3),  # north belt, gaps: river x18-21, road x36-41
]
BANDS = [  # (y, x0, x1, [(stairs left column, width)]) -- width 3 = 45 46 46, lines up with a 3-wide road
    (15, 8, 45, [(16, 2), (37, 3)]),   # upper terrace -> town (west/centre); 3-wide under the road
    (12, 48, 71, [(58, 2)]),           # upper terrace -> town (east, one tier higher)
    (34, 8, 71, [(24, 2), (37, 3)]),   # town -> lakeshore
]
STEPS = [  # vertical cliff joining two bands: (x, y_top, y_bottom); high ground WEST
    (46, 12, 16),                # 9/10 at the top (east band), 35/11 at the bottom (west band)
]
COBBLE = [
    (37, 0, 39, 14),             # north road to the Ivy River exit
    (37, 17, 39, 20),            # stairs -> the monument's north edge
    (0, 28, 28, 30), (26, 24, 28, 30), (26, 24, 30, 26),   # west road (Route 11), jogs north into the west arm
    (47, 24, 79, 26),            # east road (Hoya Delta), straight into the east arm
    (37, 30, 39, 33),            # monument -> lakeshore stairs
    (37, 36, 39, 43),            # down to the quay
]
QUAY_PAVEMENT = [(10, 44, 50, 45)]           # promenade rows above the quay wall
WATER = [
    (10, 47, 42, 59), (46, 47, 50, 59), (43, 53, 45, 59),   # lake around the pier (locked)
    (51, 42, 70, 59),                                      # east bay (locked x51-52)
    (19, 0, 20, 10),                                       # river from the north (Ivy River)
    (17, 8, 22, 11),                                       # pool where it goes underground (dive spot)
]
PIER = (43, 47, 45, 52)
BUILDINGS = {  # name: (x, y) of the grid's top-left; doors land where the warps go
    'academy': (24, 5),        # door (27,12)
    'residence': (10, 4),      # student dormitory (Osrid has a room here), by the river; door (13,8)
    'cadmus_house': (9, 19),   # door (13,23)
    'church': (19, 18),        # Templar Monastery; door (22,27)
    'tavern': (30, 37),        # 7 wide (full lodge); door (33,43)
    'lab_tower': (44, 40),     # door (47,44) LOCKED
}
EXTRA_RESIDENCES = [(56, 4)]                      # house 5
COTTAGES = [(51, 19), (61, 19), (51, 29), (61, 29)]  # houses 6, 7, 8, 8b (user: gabled cottages); door (x+3, y+3)
MONUMENT = (31, 21)                                  # wellspring fountain ring, 16x9, fills the plaza
TRIM = {'lab_tower': [(0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)]}  # (row, col) -> grass

# dressing (positions chosen by hand; every one keeps door fronts, stairs and roads clear)
LAMPS = [  # lamp post: top (walkable) over base (blocked); left-of-road 76/88, right-of-road 80/89
    (36, 5, 'L'), (40, 5, 'R'), (36, 10, 'L'), (40, 10, 'R'),
    (36, 17, 'L'), (40, 17, 'R'), (40, 38, 'R'),
    (16, 26, 'L'), (29, 27, 'R'), (59, 27, 'L'), (68, 27, 'R'),
]
TREES = [  # single tree 2x3, top-left cell
    (32, 5), (33, 9), (43, 5), (44, 9), (50, 5), (66, 9),
    (17, 19), (27, 18), (29, 21), (57, 18), (68, 18), (57, 28), (68, 29),
    (10, 37), (15, 39), (20, 37), (27, 37), (42, 36), (50, 36), (55, 37), (62, 36), (67, 38),
    (8, 4), (8, 9),
]
HEDGES = [  # 2-wide flower hedge 42/43, left cell
    (51, 23), (61, 23), (51, 33), (61, 33),
    (9, 24), (14, 24),
]
LAWNS = [  # framed lawn (x0, y0, x1, y1): 99 100 101 / 108 126 109 / 102 103 104
    (9, 25, 13, 27), (64, 4, 69, 7),
]
FLOWER_IDS = (21, 36, 21, 36, 51)
FLOWER_DENSITY = 0.025


def rects(lst):
    m = np.zeros((H, W), bool)
    for x0, y0, x1, y1 in lst:
        m[y0:y1 + 1, x0:x1 + 1] = True
    return m


def build(C):
    man = json.load(open(os.path.join(C, 'data/tilesets/secondary/pelluca_valley/assembly_manifest.json')))
    grid = np.full((H, W), GRASS, int)
    blocked = np.zeros((H, W), bool)
    water = rects(WATER)
    forest = rects(FOREST)
    cob = rects(COBBLE)

    # forest
    F = lambda y, x: True if not (0 <= y < H and 0 <= x < W) else forest[y, x]
    for y in range(H):
        for x in range(W):
            if not forest[y, x]: continue
            left = x % 2 == 0
            top_open, bot_open = not F(y - 1, x), not F(y + 1, x)
            side_open = not F(y, x - 1) if left else not F(y, x + 1)
            # rows count from the region top: tip / body / overlap / body / ... / base
            r = 0
            while F(y - r - 1, x) and y - r - 1 >= 0: r += 1
            if top_open: t = (33, 34)
            elif bot_open: t = (40, 41)
            elif r % 2 == 1: t = (22, 25) if side_open else (24, 23)
            else: t = (29, 32) if side_open else (31, 30)
            grid[y, x] = t[0] if left else t[1]
            blocked[y, x] = True

    # cliff bands
    for y, x0, x1, stairs in BANDS:
        for x in range(x0, x1 + 1):
            if forest[y, x]: continue
            grid[y, x], grid[y + 1, x] = 10, 11
            blocked[y, x] = blocked[y + 1, x] = True
        for sx, sw in stairs:
            for i in range(sw):
                grid[y, sx + i] = grid[y + 1, sx + i] = 45 if i == 0 else 46
            blocked[y, sx:sx + sw] = blocked[y + 1, sx:sx + sw] = False

    for x, yt, yb in STEPS:
        grid[yt, x], grid[yt + 1, x], grid[yt + 1, x + 1] = 9, 7, 2
        for y in range(yt + 2, yb - 1):
            grid[y, x], grid[y, x + 1] = 7, 8
        grid[yt, x + 1] = 10
        grid[yb - 1, x], grid[yb - 1, x + 1] = 35, 8
        grid[yb, x], grid[yb, x + 1] = 11, 5
        blocked[yt:yb + 1, x:x + 2] = True

    # cobble 9-slice
    Cb = lambda y, x: True if not (0 <= y < H and 0 <= x < W) else cob[y, x]
    for y in range(H):
        for x in range(W):
            if not cob[y, x]: continue
            n, s, w, e = Cb(y - 1, x), Cb(y + 1, x), Cb(y, x - 1), Cb(y, x + 1)
            if not n: m = 63 if not w else (65 if not e else 64)
            elif not s: m = 130 if not w else (136 if not e else 131)
            elif not w: m = 77
            elif not e: m = 79
            elif not Cb(y - 1, x - 1): m = 124
            elif not Cb(y - 1, x + 1): m = 125
            elif not Cb(y + 1, x - 1): m = 133
            elif not Cb(y + 1, x + 1): m = 134
            else: m = 78
            grid[y, x] = m

    # quay promenade
    qp = rects(QUAY_PAVEMENT)
    grid[qp] = 147

    # water + its stone edges
    pier = rects([PIER])
    Wt = lambda y, x: False if not (0 <= y < H and 0 <= x < W) else water[y, x]
    for y in range(H):
        for x in range(W):
            if water[y, x]:
                grid[y, x] = 159 if (y > 0 and not water[y - 1, x] and not pier[y - 1, x] and grid[y - 1, x] == 155) else 162
                continue
            if forest[y, x]: continue
            s, w_, e = Wt(y + 1, x), Wt(y, x - 1), Wt(y, x + 1)
            if pier[y, x]:
                grid[y, x] = 160 if x == PIER[0] else (161 if x == PIER[2] else 157)
            elif s and not w_ and not e:
                grid[y, x] = 155
            elif w_:
                grid[y, x] = 160
            elif e:
                grid[y, x] = 161
            elif Wt(y + 1, x - 1) and not s:
                grid[y, x] = 156
            elif Wt(y + 1, x + 1) and not s:
                grid[y, x] = 158
    # pier joins the quay wall: 156 157 158 on the wall row
    py = PIER[1] - 1
    grid[py, PIER[0]], grid[py, PIER[0] + 1], grid[py, PIER[2]] = 156, 157, 158
    # second pass: water directly under a wall row gets the wall shadow
    for y in range(1, H):
        for x in range(W):
            if water[y, x] and grid[y - 1, x] in (155, 156, 158) and not pier[y, x]:
                grid[y, x] = 159
    blocked[water] = False

    # buildings
    def stamp(name, ox, oy):
        g = man['regions'][name]['grid']
        for yy, row in enumerate(g):
            for xx, m in enumerate(row):
                if m is None: continue
                grid[oy + yy, ox + xx] = m
                blocked[oy + yy, ox + xx] = True
    for name, (ox, oy) in BUILDINGS.items():
        stamp(name, ox, oy)
        for r, c in TRIM.get(name, []):
            grid[oy + r, ox + c] = GRASS; blocked[oy + r, ox + c] = False
    for ox, oy in EXTRA_RESIDENCES:
        stamp('residence', ox, oy)
    for ox, oy in COTTAGES:
        stamp('cottage', ox, oy)
    stamp('monument', *MONUMENT)
    mb = np.array(man['monument_blocked'], bool)
    mx, my = MONUMENT
    blocked[my:my + mb.shape[0], mx:mx + mb.shape[1]] = mb    # only the basin blocks; ring paving + lawn walk

    free = lambda x, y: grid[y, x] == GRASS
    for x0, y0, x1, y1 in LAWNS:
        assert all(free(x, y) for y in range(y0, y1 + 1) for x in range(x0, x1 + 1)), ('lawn', x0, y0)
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                l, r = x == x0, x == x1
                if y == y0: grid[y, x] = 99 if l else (101 if r else 100)
                elif y == y1: grid[y, x] = 102 if l else (104 if r else 103)
                else: grid[y, x] = 108 if l else (109 if r else 126)
    for x, y, side in LAMPS:
        assert free(x, y) and free(x, y + 1), ('lamp', x, y)
        grid[y, x], grid[y + 1, x] = (76, 88) if side == 'L' else (80, 89)
        blocked[y + 1, x] = True
    for x, y in TREES:
        assert all(free(x + i, y + j) for i in (0, 1) for j in (0, 1, 2)), ('tree', x, y)
        grid[y, x], grid[y, x + 1] = 33, 34
        grid[y + 1, x], grid[y + 1, x + 1] = 22, 25
        grid[y + 2, x], grid[y + 2, x + 1] = 40, 41
        blocked[y + 1:y + 3, x:x + 2] = True
    for x, y in HEDGES:
        assert free(x, y) and free(x + 1, y), ('hedge', x, y)
        grid[y, x], grid[y, x + 1] = 42, 43
        blocked[y, x:x + 2] = True

    # flowers on open grass, never on a cell in front of a door or next to stairs/roads
    rnd = np.random.default_rng(11)
    near = np.zeros((H, W), bool)
    for y in range(H):
        for x in range(W):
            if grid[y, x] != GRASS:
                near[max(0, y - 1):y + 2, max(0, x - 1):x + 2] = True
    for y in range(H):
        for x in range(W):
            if grid[y, x] == GRASS and not near[y, x] and rnd.random() < FLOWER_DENSITY:
                grid[y, x] = FLOWER_IDS[rnd.integers(len(FLOWER_IDS))]

    return grid, blocked, water, man


QUAY_WALKABLE = {155, 156, 157, 158, 160, 161}   # Pelluca's quay/pier is walkable at ground level (dock lock)

def collision_elevation(grid, blocked, water):
    """Per cell (collision, elevation). Terrain/building pieces use how MonoMyth's own maps set
    them (data/source_collision.json); stairs keep elevation 0 (level change). Overrides:
    the quay wall + pier are walkable at elevation 3 (locked dock), water is (0,1), and pieces
    with no source (Evernahn church) are blocked except grass."""
    src = json.load(open(os.path.join(HERE, 'data/source_collision.json')))
    coll = np.zeros((H, W), int); elev = np.zeros((H, W), int)
    for y in range(H):
        for x in range(W):
            m = int(grid[y, x])
            if water[y, x]: c, e = 0, 1
            elif m in QUAY_WALKABLE: c, e = 0, 3
            elif str(m) in src: c, e = src[str(m)]
            else: c, e = (1, 0) if blocked[y, x] else (0, 3)
            coll[y, x], elev[y, x] = c, e
    return coll, elev


def render(grid, C, path):
    from PIL import Image
    pm, sm, draw = lk.tilesets(C); cache = {}
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            m = int(grid[y, x])
            if m not in cache: cache[m] = draw(m).astype(np.uint8)
            img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cache[m]
    Image.fromarray(img).save(path)
    return img


if __name__ == '__main__':
    C, out = sys.argv[1], sys.argv[2]
    grid, blocked, water, man = build(C)
    coll, elev = collision_elevation(grid, blocked, water)
    np.savez(out + '.npz', grid=grid, coll=coll, elev=elev)
    render(grid, C, out + '.png')
    print('rendered', out + '.png')
