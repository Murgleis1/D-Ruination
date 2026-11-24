"""The first slip into Ancient Cormoria (Beat 8e), plan v3: the approved layout (plan v1/v2, plan_slip_v1.py) rebuilt in
MonoMyth's own shapes after mock v1's review (user 2026-11-24: "There's a lot of broken looking weird things ... I
think you need to re-analyze all the stuff you can on various desert reference maps and see what looks normal versus
not"; "The cliffs, oasis, etc. all need more work"; "the arches you have don't line up perfectly").

The story and the route are unchanged (plan_slip_v1.py has them): arrival at the south altar in a ring of dreamstone
obelisks on pink sand; north under the dragon's ribs, past its skull and spine across the dunes; up the step; over the
river by the rope bridge below the falls; up the mesa's ladder to the north altar on the rim over the blood-red sky.

What changed, from the study of MonoMyth's canyon maps (tilesolve.py; seam heat maps in
assets/ancient_cormoria_reference/):
  * every wall is a rock mass seen from above (its rock top, 'W') with a face of two banded rows on its south side
    (upper 'U' over lower 'L'), as MonoMyth's are; a tall wall (the falls') is two bands (U L U L);
  * the plan is only terrain classes; the solver (tilesolve.solve) picks the tiles, so each cell's tile agrees with
    its neighbours the way MonoMyth's do; any neighbourhood MonoMyth never shows is reported and the shape changed;
  * dunes are organic fields of ripples at least three rows deep (never rectangles); outcrops in the dunes are whole
    small mesas (top, two face rows), not 2-wide stubs;
  * the river keeps MonoMyth's stepped banks; the falls are four wide, fed by a spring pool on the wall's top;
  * the oasis is a real pool in the sand with its own banks, palms and green round it;
  * the rib cage: three identical ribs, each the same width, their feet in the same two columns, evenly spaced.

Terrain letters: 'K' sky (the ancient backdrop), '#' red rock (its class from its depth: L, U, W), '.' sand, 'r'
rippled dune, '~' water. Set pieces are listed separately (LADDERS, BRIDGE, FALLS, HOUSES, PANELS, OBELISKS, ALTARS,
SKULL, SPINE, RIBS, RIB_STUBS, CLAW, PALMS, CACTI, OASIS_GREEN, PINK). Usage: python3 plan_slip.py [OUT.png]"""
import os, sys, math, random
import numpy as np
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 50, 56
G = np.full((H, W), '.', dtype='<U1')
def r(x0, y0, x1, y1, ch): G[y0:y1 + 1, x0:x1 + 1] = ch
def blob(cx, cy, rx, ry, ch, only=None, seed=0, wob=0.18):
    """an organic patch: an ellipse whose radius wanders with the angle (no 1-cell spurs: smoothed after)"""
    rnd = random.Random(seed); ph = [rnd.uniform(0, 6.28) for _ in range(3)]
    for y in range(max(0, int(cy - ry) - 2), min(H, int(cy + ry) + 3)):
        for x in range(max(0, int(cx - rx) - 2), min(W, int(cx + rx) + 3)):
            a = math.atan2((y - cy) / ry, (x - cx) / rx)
            k = 1 + wob * (math.sin(2 * a + ph[0]) + 0.6 * math.sin(3 * a + ph[1]) + 0.4 * math.sin(5 * a + ph[2])) / 2
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= k * k and (only is None or G[y, x] in only): G[y, x] = ch

# ---- the sky and the mesa: the land north of row 13 is only the mesa's oval, rising into the sky
r(0, 0, W - 1, H - 1, '#')
# (mock v2: the summit made a small crown out in the sky, joined to the wall by a narrow neck, so that standing at
# the altar the sky shows above and on both sides of it, as the Peak's summit was made (user, the Peak: "scale the
# north part ... back so you can see more of the mountains in the backdrop as you approach the edge"))
MESA_OVAL = (24.5, 6.0, 5.8, 4.0)                         # (cx, cy, rx, ry in cells; the rim is drawn on it, pixel-smooth)
NECK = (21.5, 27.5, 8.5)                                  # (u from, u to, v from: the neck down to the wall)
def in_land(u, v):
    cx, cy, rx, ry = MESA_OVAL
    return (((u - cx) / rx) ** 2 + ((v - cy) / ry) ** 2 <= 1) | ((NECK[0] <= u) & (u <= NECK[1]) & (v >= NECK[2]))
for y in range(0, 13):
    for x in range(W):
        if not any(in_land(x + dx, y + dy) for dx in (-0.5, 0.5) for dy in (-0.5, 0.5)): G[y, x] = 'K'
# its top: a plaza of sand to the rim (the rim painted round it against the sky), the north altar at its heart in a
# ring of obelisks; the rock of the wall below it
for y in range(0, 13):
    for x in range(W):
        if G[y, x] == '#': G[y, x] = '.'
r(23, 13, 26, 15, '.')                                    # (the way cut down through the rock to the ladder's head)
# ---- the north wall (rows 13-18): rock top, its face rows 17-18; a bulge south east of the ladder (face 18-19)
r(30, 19, 36, 19, '#')
# the spring on the wall's top and the falls (four wide) over its face into the pool below
r(39, 15, 42, 16, '~')                                    # (a spring under a little face of its own, rows 13-14)
FALLS = dict(x0=39, x1=42, top=17, rows=2)                # (a0 at the upper face, a1 at the lower; foam a2 below)
# ---- the river plain (rows 19-31)
r(11, 19, 43, 31, '.')
# the pool under the falls; the river, its banks stepping as MonoMyth's do, west under the cliff homes and off the map
r(37, 19, 43, 21, '~')
RIVER = [(36, 21, 3), (34, 22, 3), (31, 23, 3), (27, 23, 3), (22, 24, 3), (18, 25, 3), (14, 26, 3), (11, 27, 3)]
for i, (x, y, w) in enumerate(RIVER):
    xe = RIVER[i - 1][0] if i else 37
    r(x, y, xe, y + w - 1, '~')
r(0, 27, 11, 29, '~'); r(0, 29, 10, 30, '.')                # (off the map's west edge; a sand bank under it)
BRIDGE = dict(x=24, y0=23, y1=27)                         # (its north end on the bank, deck over the water, south end)
for y in range(BRIDGE['y0'], BRIDGE['y1'] + 1):
    if G[y, 24] != '~': G[y, 24] = G[y, 25] = '.'
# the west: the cliff homes of a people long gone on a mesa over the river (its face over the water)
r(0, 19, 10, 26, '#')                                     # (its rock top 19-24, face 25-26 over the river)
HOUSES = []                                               # (v2's cliff homes, MonoMyth's pueblo: gone, user 2026-11-24)
# on the west mesa, where the cliff homes stood (user 2026-11-24: "replace the adobe buildings with a partly sand buried
# and sand-worn looking version of this skeleton"): the skeleton of a Tyrantrum, Lazarus's statue of one (its
# conservation-centre town, header 0xfaa648, metatiles 0x288-0x2a3) worn to bone and half buried in drifted sand,
# turned to face east over the canyon; 64x64 px at pixel (px, py); scenery (the mesa is not walked)
TYRANTRUM = dict(px=50, py=326, flip=True)
# the east: the canyon's wall
r(44, 19, 49, 31, '#'); r(43, 22, 43, 31, '#')
# the oasis: a pool in the sand south of the river, palms and green round it
r(38, 26, 41, 28, '~')                                    # (a pool east of the river: MonoMyth's pools are square-cut)
OASIS_GREEN = [(38, 29), (40, 29), (39, 30), (36, 27), (42, 25), (39, 25), (35, 28), (36, 30)]   # (flowers, grass)
PALMS = [(37, 26), (42, 27), (37, 29), (41, 30), (13, 21), (31, 28)]
# ripples on the plain
blob(18, 21, 4.5, 1.6, 'r', only='.', seed=1); blob(31, 20.5, 3.6, 1.5, 'r', only='.', seed=2)
blob(16, 30, 4.0, 1.5, 'r', only='.', seed=3)
# ---- the step down to the dunes (rows 31-34): rock top 31-32, face 33-34; ladders at the way and in the west
r(0, 31, W - 1, 34, '#')                                  # (rock top 31-32, face 33-34; sand bank row 30 over it)
LADDERS = [dict(x=24, y=17), dict(x=24, y=33), dict(x=13, y=33)]   # (stairs cut in the face (v2: were rope ladders); 2 wide; from the rock top's last row to the ground)
PANELS = [(18, 17), (29, 17), (15, 33), (33, 33)]                  # (2x2 carved alcoves in the faces)
# ---- the dune field (rows 35-53), walls either side, the south edge
r(2, 35, 47, 53, '.')
for (x0, x1, y0, y1) in ((2, 3, 35, 38), (2, 2, 39, 41), (46, 47, 35, 37), (47, 47, 38, 44), (2, 4, 50, 53),
                         (45, 47, 49, 53), (5, 6, 53, 53), (42, 44, 53, 53)):
    r(x0, y0, x1, y1, '#')
# two outcrops: whole small mesas (rock top over a two-row face)
r(5, 43, 9, 47, '#'); r(6, 42, 8, 42, '#'); r(4, 45, 4, 47, '#')
r(41, 46, 45, 50, '#'); r(42, 45, 44, 45, '#')
# the walls' feet step out a row here and there (MonoMyth's are never ruled straight for long)
r(14, 19, 16, 19, '#')
for (x0, x1) in ((10, 17), (27, 31), (39, 44)): r(x0, 35, x1, 35, '#')
# rippled dune fields: organic, three rows deep or more
blob(14, 37, 5.0, 1.7, 'r', only='.', seed=4); blob(35, 37, 4.5, 1.6, 'r', only='.', seed=5)
blob(11, 50, 5.0, 2.0, 'r', only='.', seed=6); blob(38, 52, 4.0, 1.5, 'r', only='.', seed=7)
blob(16, 45, 3.0, 1.5, 'r', only='.', seed=8); blob(35, 47, 3.2, 1.5, 'r', only='.', seed=9)
# ---- the dragon: the skull east (facing west), the spine west along the dunes (broken where the way crosses it), three
# identical ribs arching over the way just south of it, rib stubs standing either side, a forelimb's claw
SKULL = (37, 39)                                          # (6x5 cells from its top-left)
SPINE = [(36, 41), (33, 41), (30, 40), (27, 40), (22, 40), (18, 41), (14, 41), (10, 40), (7, 39), (5, 38)]
SPINE_GAP = {(23, 40), (24, 40), (25, 40), (26, 40)}
RIBS = [dict(y=43), dict(y=45), dict(y=47)]               # (each: feet at x 21 and 28, rows y and y+1; span 22-27)
RIB_X = (21, 28)
RIB_STUBS = [(15, 43), (18, 43), (31, 43), (34, 43)]
CLAW = [(33, 45), (34, 46), (36, 45)]
CACTI = [(9, 37), (40, 35), (20, 36), (29, 37), (44, 42), (6, 50), (39, 51), (13, 23), (34, 29)]
# ---- the arrival: pink crystal sand (painted soft, round the ring), the obelisks, the south altar
PINK = dict(cx=24.5, cy=51.0, rx=7.0, ry=3.6)
OBELISKS_SOUTH = [(19, 49), (30, 49), (18, 51), (31, 51), (20, 53), (29, 53)]
OBELISKS_NORTH = [(21, 5), (28, 5), (21, 8), (28, 8)]
ALTARS = [dict(x=24, y=4, north=True), dict(x=24, y=51, north=False)]
ARRIVE = (24, 50)

def load():
    """the plan as normalize_plan.py left it (MonoMyth-normal), if it has been run"""
    f = os.path.join(HERE, 'plan_normal.npy')
    if os.path.exists(f): G[:] = np.load(f)

# ---- the terrain classes for the solver
def classes():
    """K sky (left out of the solve, rock to its neighbours' eyes), W/U/L rock by depth, F sand, r ripples, A water"""
    out = np.full((H, W), 'F', dtype='<U1')
    for y in range(H):
        for x in range(W):
            ch = G[y, x]
            if ch == 'K': out[y, x] = 'K'
            elif ch == '#':
                d = 1
                while y + d < H and G[y + d, x] == '#': d += 1
                out[y, x] = 'L' if d == 1 and y + d < H else 'U' if d == 2 and y + d < H else 'W'
            elif ch == '~': out[y, x] = 'A'
            elif ch == 'r': out[y, x] = 'r'
    # the falls' wall: rows 17-18 are the face either side of the falls; the falls' cells are water
    for x in range(FALLS['x0'], FALLS['x1'] + 1):
        for y in range(FALLS['top'], FALLS['top'] + FALLS['rows']): out[y, x] = 'A'
    return out

EXTRA_SOLID = set()                                       # (props compose_slip scatters that stand in the way)
def solid():
    """cells the player cannot walk"""
    s = np.isin(G, ['#', '~', 'K'])
    for (x, y) in EXTRA_SOLID: s[y, x] = True
    for L in LADDERS:                                     # (and the rock top over its head, up to the ground above)
        for x in (L['x'], L['x'] + 1):
            y = L['y']
            while y < H and G[y, x] == '#': s[y, x] = False; y += 1      # (down the face to the ground)
            y = L['y'] - 1
            while y >= 0 and G[y, x] == '#': s[y, x] = False; y -= 1
    for y in range(BRIDGE['y0'], BRIDGE['y1'] + 1): s[y, 24] = s[y, 25] = False
    for R in RIBS:
        for x in RIB_X: s[R['y'], x] = s[R['y'] + 1, x] = True
    for (x, y) in RIB_STUBS: s[y, x] = True
    for (x, y) in CLAW + CACTI + PALMS + OBELISKS_SOUTH + OBELISKS_NORTH: s[y, x] = True
    sx, sy = SKULL; s[sy:sy + 5, sx:sx + 6] = True
    for (x, y) in spine_cells(): s[y, x] = True
    for A in ALTARS: s[A['y']:A['y'] + 2, A['x']:A['x'] + 2] = True
    return s

def spine_cells():
    out = set()
    for (ax, ay), (bx, by) in zip(SPINE, SPINE[1:]):
        n = max(abs(bx - ax), abs(by - ay))
        for t in range(n + 1):
            out.add((int(round(ax + (bx - ax) * t / n)), int(round(ay + (by - ay) * t / n))))
    return out - SPINE_GAP

SPOTS = {'arrival (south altar)': ARRIVE, 'under the ribs': (24, 45), 'the skull': (38, 45), 'up the step': (24, 35),
         'the oasis': (39, 30), 'the rope bridge': (24, 25), 'the mesa ladder': (24, 19), 'north altar': (24, 6)}

def check():
    s = solid(); seen = {ARRIVE}; q = deque([ARRIVE])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in seen and not s[ny, nx]: seen.add((nx, ny)); q.append((nx, ny))
    return seen

if __name__ == '__main__':
    seen = check()
    print('walkable from the arrival:', len(seen), '| unreachable:', [n for n, p in SPOTS.items() if p not in seen])
    c = classes()
    for y in range(H): print('%2d ' % y + ''.join(c[y]))
