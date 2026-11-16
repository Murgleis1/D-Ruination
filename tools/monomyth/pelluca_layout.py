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
# GROVES: small woods drawn with the forest rules (height 5 = two trees deep, 3 = one row).
# Draft-4 feedback: evenly spaced single trees read generic -> clusters of varied size,
# backing buildings and cliffs, with singles/slim conifers/bushes as accents.
GROVES = [
    (8, 10, 11, 14),                          # behind the dorm, against the terrace edge
    (32, 4, 35, 8), (42, 4, 45, 8),           # flanking the north road at the forest gap
    (48, 4, 53, 8),                           # upper-east, beside house 5
    (26, 17, 29, 21),                         # between the monastery and the fountain
    (48, 14, 51, 18), (54, 14, 57, 18),       # under the east terrace, behind the cottages (lane at x58-59)
    (8, 31, 23, 33), (26, 31, 35, 33),        # tree ROW along the top of the lower cliff (stairs x24-25 open)
    (40, 31, 51, 33), (66, 31, 71, 33),
    (66, 15, 69, 17),                         # a row of trees by the east forest
]                                             # (the shore below the lower cliff is beach: palms, not woods)
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
    (27, 44, 36, 45),            # beach lane -> the tavern door (user: paths to the tavern and lab)
    (26, 13, 36, 14),            # small 2-wide cobbled road: Academy door -> north road (user)
    # LANES (approved plan 2026-11-16): 2-wide cobble from each major door into the main roads
    (13, 9, 14, 14), (13, 13, 17, 14), (16, 17, 17, 27), (13, 24, 17, 25),   # dorm -> (round the pool) west stairs -> Cadmus -> W road
    (58, 9, 59, 11), (58, 14, 59, 23),                                     # house 5 -> east-terrace stairs -> E road
    (58, 27, 59, 30), (53, 31, 65, 32),                                    # E road -> cottages 8 / 8b
]
LAWN_PATHS = []                  # lawn-frame/path pieces read as flat patches (user 2026-11-16): not used
QUAY_PAVEMENT = []                           # replaced by the beach (user 2026-11-16)
BEACH = None
# THE BEACH (user 2026-11-16): ALL land below the lower cliff, around the dock and the lab.
# Per column: surf row s and first water row w (shore.py); neighbours differ by <= 1 row.
SHORE_TOP = 36
def _profile():
    s, w = {}, {}
    for x in range(8, 37):                 # the beach is WEST of the harbour road
        if x <= 12: s[x] = 44
        elif x <= 24: s[x] = 45
        else: s[x] = 46                    # surf row y46 = the harbour's wall row: the waterline runs on into the quay wall
        w[x] = s[x] + 2
    w[36] = 47                             # the wet band tapers (water step) into the harbour corner
    return s, w
SHORE_S, SHORE_W = _profile()
WATER = [
    (19, 0, 20, 10),                                       # river from the north (Ivy River)
    (17, 8, 22, 11),                                       # pool where it goes underground (dive spot)
]
# HARBOUR (user 2026-11-16): everything east of the harbour road below the lower cliff is one stone
# quay -- the beach is under the stone. Its seaward wall row is the beach's surf row (y46), so the
# beach's waterline runs straight on into the quay wall; nowhere does foam meet stone.
HARBOUR = [(37, 36, 50, 46), (51, 36, 71, 41)]
HARBOUR_WATER = [(37, 47, 50, 59), (51, 42, 71, 59)]
PIER = HARBOUR + [(43, 47, 45, 48), (40, 49, 48, 52),           # quay + stem + HEAD
                  (62, 42, 64, 45)]                              # a short jetty in the bay: the rowboats' mooring
# (user: the dock stone clashed with the road cobbles -> the dock is its own stone surface; the
# harbour road ends at the apron's west rim instead of running onto it)
PIER_LAMPS = [(41, 50), (47, 50)]
BUILDINGS = {  # name: (x, y) of the grid's top-left; doors land where the warps go
    'academy': (24, 5),        # door (27,12)
    'residence': (10, 4),      # student dormitory (Osrid has a room here), by the river; door (13,8)
    'cadmus_house': (9, 19),   # door (13,23)
    'church': (19, 18),        # Templar Monastery; door (22,27)
    'tavern_sand': (25, 37),   # on the beach; 7 wide (full lodge), moved left (user); door (28,43)
    'lab_tower_stone': (44, 40),  # on the harbour quay; door (47,44) LOCKED
}
EXTRA_RESIDENCES = [(56, 4)]                      # house 5
COTTAGES = [(51, 20), (61, 20), (51, 27), (61, 27)]  # houses 6, 7 (door onto the road), 8, 8b; door (x+3, y+3)
MONUMENT = (31, 21)                                  # wellspring fountain ring, 16x9, fills the plaza
TRIM = {'lab_tower_stone': [(0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5)],   # (row, col) -> grass
        'academy': [(0, 0), (0, 6)],
        'tavern_sand': [(7, 5)]}         # its lamp post stood in the beach lane       # Wood Avens lawn-frame pieces at the roof corners (read as patches)

# dressing (positions chosen by hand; every one keeps door fronts, stairs and roads clear)
LAMPS = [  # lamp post: top (walkable) over base (blocked); left-of-road 76/88, right-of-road 80/89
    (36, 5, 'L'), (40, 10, 'R'),
    (36, 17, 'L'), (40, 17, 'R'),
    (15, 26, 'L'), (29, 27, 'R'), (57, 27, 'L'), (69, 27, 'R'),
]
TREES = [  # single round tree 2x3, top-left cell -- accents only now
    (68, 9),
]
SLIM = [  # slim conifer 44/47/20 (1x3), top cell
    (23, 4), (41, 10), (47, 18), (57, 20), (60, 21), (71, 19),
    (9, 5), (17, 5), (18, 19), (55, 5), (63, 5), (50, 20), (66, 20), (50, 27), (66, 27),   # pairs framing buildings
]
BUSHES = []                                                     # round bush 97
HEDGES = [  # 2-wide flower hedge 42/43, left cell -- not every house (user: more variety)
    (9, 24), (66, 30),
]
FENCES = [  # rows of picket fence 98: (x0, x1, y)
    (64, 69, 8),                 # house 5's garden
]
LAWNS = [  # framed lawn (x0, y0, x1, y1): 99 100 101 / 108 126 109 / 102 103 104
]
STUMPS = [(56, 29)]              # 114 115: chopping stumps by cottage 8
FLOWERS = [(50, 23), (56, 22), (66, 23),
           (65, 6), (67, 5), (69, 7), (68, 20), (70, 21), (10, 26), (12, 27)]
# beach dressing: palm groups along the cliff foot and framing the tavern, lab and pier (2x3, top-left)
CAVE_MOUTH = (10, 34)                        # Umbra cavern, sealed (author 2026-11-16); slab cells (10,35),(11,35) = door
PALMS = [(8, 40), (13, 38), (16, 36), (19, 39), (22, 37), (32, 37), (32, 41),
         (35, 36), (35, 40)]                 # two along the beach/harbour edge so it is not one long straight cut
BEACH_LAMPS = []
# ships + boats are OBJECT events (added with the map's events); drawn on previews only:
# (gfx, x, y) -- S.S. Tidal at the main pier (locked arrival), a second ship at the bay jetty
# (user: the docks should look bustling), Mr. Briney's rowboats moored on the jetty's west side
SHIPS = [('ss_tidal', 44, 54), ('ss_tidal', 67, 45), ('mr_brineys_boat', 60, 43), ('mr_brineys_boat', 60, 45)]
# (the S.S. Tidal moves (44,55)->(44,54) so it lies alongside the pier head; cosmetic, not on the arrival path)
HARBOUR_LAMPS = [(40, 36), (42, 40), (49, 42), (55, 38), (62, 38), (69, 38)]   # lamps on stone (pier kit)
PIER_LAMPS = PIER_LAMPS + HARBOUR_LAMPS
FLOWER_IDS = (21, 36, 21, 36, 51)
FLOWER_DENSITY = 0.0


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
    forest = rects(FOREST) | rects(GROVES)
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

    # THE BEACH: shore columns from the cliff foot to the lake (shore.py), then the pier on top
    import shore as sh
    F172, F174, F176 = man['regions']['shore_flip']['grid'][0]
    beach = np.zeros((H, W), bool)
    for x in SHORE_S:
        col = sh.shore_columns([SHORE_S[x - 1] if x - 1 in SHORE_S else SHORE_S[x], SHORE_S[x]],
                               [SHORE_W[x - 1] if x - 1 in SHORE_W else SHORE_W[x], SHORE_W[x]],
                               SHORE_TOP, H - 1, F172, F174, F176)[1]
        nxt = sh.shore_columns([SHORE_S[x], SHORE_S.get(x + 1, SHORE_S[x])],
                               [SHORE_W[x], SHORE_W.get(x + 1, SHORE_W[x])], SHORE_TOP, H - 1, F172, F174, F176)[0]
        for y in range(SHORE_TOP, H):
            m = col[y]
            if nxt[y] in (F172, F174, F176): m = nxt[y]       # a rising step lands in THIS column
            beach[y, x] = True
            if cob[y, x]: continue                            # the harbour road stays (sand twin below)
            grid[y, x] = m
            water[y, x] = m in (162, 175)
            blocked[y, x] = False
    pier = rects(PIER)
    water |= rects(HARBOUR_WATER)
    water &= ~pier
    K = dict(zip(('N', 'NW', 'NE', 'S', 'SW', 'SE', 'iNW', 'iNE', 'lampT', 'lampB'),
                 man['regions']['pier_kit']['grid'][0]))
    WALL_ROW = {155, 156, 158, K['S'], K['SW'], K['SE']}
    Wt = lambda y, x: False if not (0 <= y < H and 0 <= x < W) else water[y, x]
    for y in range(H):
        for x in range(W):
            if water[y, x] or forest[y, x]: continue
            if beach[y, x] and not pier[y, x]: continue
            n, s_, w_, e = Wt(y - 1, x), Wt(y + 1, x), Wt(y, x - 1), Wt(y, x + 1)
            if pier[y, x]:
                P = lambda yy, xx: 0 <= yy < H and 0 <= xx < W and pier[yy, xx]
                # rims only where stone meets WATER; against sand the paving simply stops (user 2026-11-16:
                # the rim line between the beach and the dock looked strange)
                n, w_, e = Wt(y - 1, x), Wt(y, x - 1), Wt(y, x + 1)
                s_ = not P(y + 1, x) and Wt(y + 1, x)                      # the wall lip only over water
                if s_ and w_: m = K['SW']
                elif s_ and e: m = K['SE']
                elif s_: m = K['S']
                elif n and w_: m = K['NW']
                elif n and e: m = K['NE']
                elif n: m = K['N']
                elif w_: m = 160
                elif e: m = 161
                elif Wt(y - 1, x - 1): m = K['iNW']
                elif Wt(y - 1, x + 1): m = K['iNE']
                elif Wt(y + 1, x + 1): m = 158                       # wall turns: water at the SE diagonal
                elif Wt(y + 1, x - 1): m = 156
                else: m = 157
                grid[y, x] = m
            elif s_ and not w_ and not e:
                grid[y, x] = 155
            elif w_:
                grid[y, x] = 160
            elif e:
                grid[y, x] = 161
            elif Wt(y + 1, x - 1) and not s_:
                grid[y, x] = 156
            elif Wt(y + 1, x + 1) and not s_:
                grid[y, x] = 158
    for y in range(H):
        for x in range(W):
            if water[y, x] and not beach[y, x]:
                grid[y, x] = 159 if y > 0 and grid[y - 1, x] in WALL_ROW else 162
            elif water[y, x] and y > 0 and grid[y - 1, x] in (K['S'], K['SW'], K['SE']):
                grid[y, x] = 159                                # shadow under the pier head
    for x, y in PIER_LAMPS:
        grid[y, x], grid[y + 1, x] = K['lampT'], K['lampB']
        blocked[y + 1, x] = True
    blocked[water] = False
    # sand twins where the town meets the beach: the cliff foot, stairs and harbour road
    ONSAND = dict(zip((63, 65, 77, 78, 79, 130, 131, 136, 124, 125, 133, 134, 76, 88, 80, 89, 11, 45, 46, 64),
                      man['regions']['onsand']['grid'][0]))
    ONSTONE = dict(zip((11, 45, 46), man['regions']['onstone']['grid'][0]))
    for y in range(SHORE_TOP - 1, H):
        for x in range(W):
            m0 = int(grid[y, x])
            if y == SHORE_TOP - 1 and pier[SHORE_TOP, x] and m0 in ONSTONE:
                grid[y, x] = ONSTONE[m0]                          # cliff foot / stairs onto the quay
            elif m0 in ONSAND and (y == SHORE_TOP - 1 or beach[y, x]):
                grid[y, x] = ONSAND[m0]

    # buildings
    def stamp(name, ox, oy):
        g = man['regions'][name]['grid']
        trim = set(TRIM.get(name, []))
        for yy, row in enumerate(g):
            for xx, m in enumerate(row):
                if m is None or (yy, xx) in trim: continue      # trimmed: the ground already there stays
                grid[oy + yy, ox + xx] = m
                blocked[oy + yy, ox + xx] = True
    for name, (ox, oy) in BUILDINGS.items():
        stamp(name, ox, oy)

    for ox, oy in EXTRA_RESIDENCES:
        stamp('residence', ox, oy)
    for ox, oy in COTTAGES:
        stamp('cottage', ox, oy)
    stamp('monument', *MONUMENT)
    mb = np.array(man['monument_blocked'], bool)
    mx, my = MONUMENT
    blocked[my:my + mb.shape[0], mx:mx + mb.shape[1]] = mb    # only the basin blocks; ring paving + lawn walk

    free = lambda x, y: grid[y, x] == GRASS
    SKIP = []
    for x0, y0, x1, y1 in LAWNS:
        if not (all(free(x, y) for y in range(y0, y1 + 1) for x in range(x0, x1 + 1))):
            SKIP.append(('lawn', x0, y0)); continue
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                l, r = x == x0, x == x1
                if y == y0: grid[y, x] = 99 if l else (101 if r else 100)
                elif y == y1: grid[y, x] = 102 if l else (104 if r else 103)
                else: grid[y, x] = 108 if l else (109 if r else 126)
    for x, y, side in LAMPS:
        if not (free(x, y) and free(x, y + 1)):
            SKIP.append(('lamp', x, y)); continue
        grid[y, x], grid[y + 1, x] = (76, 88) if side == 'L' else (80, 89)
        blocked[y + 1, x] = True
    for x, y in TREES:
        if not (all(free(x + i, y + j) for i in (0, 1) for j in (0, 1, 2))):
            SKIP.append(('tree', x, y)); continue
        grid[y, x], grid[y, x + 1] = 33, 34
        grid[y + 1, x], grid[y + 1, x + 1] = 22, 25
        grid[y + 2, x], grid[y + 2, x + 1] = 40, 41
        blocked[y + 1:y + 3, x:x + 2] = True
    for x, y in HEDGES:
        if not (free(x, y) and free(x + 1, y)):
            SKIP.append(('hedge', x, y)); continue
        grid[y, x], grid[y, x + 1] = 42, 43
        blocked[y, x:x + 2] = True
    for x0, y0, x1, y1 in LAWN_PATHS:          # 2-row lawn path: 99 100 101 / 102 103 104
        if not (all(free(x, y) for y in (y0, y1) for x in range(x0, x1 + 1))):
            SKIP.append(('path', x0, y0)); continue
        for x in range(x0, x1 + 1):
            l, r = x == x0, x == x1
            grid[y0, x] = 99 if l else (101 if r else 100)
            grid[y1, x] = 102 if l else (104 if r else 103)
    for x, y in SLIM:                           # slim conifer: tip (walk-behind) / body / base
        if not (all(free(x, y + j) for j in (0, 1, 2))):
            SKIP.append(('slim', x, y)); continue
        grid[y, x], grid[y + 1, x], grid[y + 2, x] = 44, 47, 20
        blocked[y + 1:y + 3, x] = True
    for x, y in BUSHES:
        if not (free(x, y)):
            SKIP.append(('bush', x, y)); continue
        grid[y, x] = 97; blocked[y, x] = True
    for x0, x1, y in FENCES:
        if not (all(free(x, y) for x in range(x0, x1 + 1))):
            SKIP.append(('fence', x0, y)); continue
        grid[y, x0:x1 + 1] = 98; blocked[y, x0:x1 + 1] = True
    for x, y in STUMPS:
        if not (free(x, y) and free(x + 1, y)):
            SKIP.append(('stumps', x, y)); continue
        grid[y, x], grid[y, x + 1] = 114, 115
    CM = man['regions']['cave_mouth']['grid']
    cx_, cy_ = CAVE_MOUTH
    for r in range(2):
        for c in range(2):
            grid[cy_ + r, cx_ + c] = CM[r][c]; blocked[cy_ + r, cx_ + c] = True
    PALM = man['regions']['palm']['grid']
    sandy = lambda x, y: grid[y, x] == 163
    for x, y in PALMS:
        if not all(sandy(x + i, y + j) for i in (0, 1) for j in (0, 1, 2)):
            SKIP.append(('palm', x, y)); continue
        for j in range(3):
            for i in range(2): grid[y + j, x + i] = PALM[j][i]
        blocked[y + 2, x:x + 2] = True                  # trunk row; the crown is walk-behind
    for x, y in BEACH_LAMPS:
        if not (sandy(x, y) and sandy(x, y + 1)): SKIP.append(('beachlamp', x, y)); continue
        grid[y, x], grid[y + 1, x] = ONSAND[80], ONSAND[89]; blocked[y + 1, x] = True
    for x, y in FLOWERS:
        if not (free(x, y)):
            SKIP.append(('flower', x, y)); continue
        grid[y, x] = (21, 36, 51)[(x + y) % 3]

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

    if SKIP: print('SKIPPED (clash):', SKIP)
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


def paste_ships(img, C):
    from PIL import Image
    for gfx, x, y in SHIPS:
        sp = Image.open(os.path.join(C, f'graphics/object_events/pics/misc/{gfx}.png'))
        pal = sp.getpalette(); a = np.array(sp)
        if gfx == 'mr_brineys_boat': a = a[:, :32]            # one frame of the 3-frame sheet
        h, w = a.shape
        x0, y0 = x * 16 + 8 - w // 2, (y + 1) * 16 - h
        for yy in range(h):
            for xx in range(w):
                if a[yy, xx] and 0 <= y0 + yy < img.shape[0] and 0 <= x0 + xx < img.shape[1]:
                    img[y0 + yy, x0 + xx] = pal[a[yy, xx] * 3:a[yy, xx] * 3 + 3]
    return img


def render(grid, C, path):
    from PIL import Image
    pm, sm, draw = lk.tilesets(C); cache = {}
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            m = int(grid[y, x])
            if m not in cache: cache[m] = draw(m).astype(np.uint8)
            img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cache[m]
    img = paste_ships(img, C)
    Image.fromarray(img).save(path)
    return img


if __name__ == '__main__':
    C, out = sys.argv[1], sys.argv[2]
    grid, blocked, water, man = build(C)
    coll, elev = collision_elevation(grid, blocked, water)
    np.savez(out + '.npz', grid=grid, coll=coll, elev=elev)
    render(grid, C, out + '.png')
    print('rendered', out + '.png')
