"""The Trial: the frozen underground lake of the dead (user 2026-11-21).

The great catacomb chamber (Ghost Grey's map 1.93, 41x32) with its floor frozen over: slippery ice everywhere
(Heater Forest's: step onto it and you slide until something stops you), graves sticking up out of the ice as the
stoppers, a few patches of grave-soil (Ghost Grey's normal catacomb ground) where you stop and walk as usual.
In each corner a bonfire on a platform of grave-soil, a necromancer beside it; light all four and the sealed
arch at the top opens on the way to Kimaris. You come in on the landing at the bottom.

This module is the puzzle: the room, the fixed pieces, a search for grave placings that make a good puzzle, and a
solver that proves it: every bonfire and the arch reachable from the landing, nothing anywhere you can get stuck
(from every place you can stop you can get back to the landing), and no bonfire reached in a handful of moves.
"""
import numpy as np, random, zlib
from collections import deque

W, H = 41, 32
# rows the room spans per row (from the chamber's own outline; the old chasm's rows filled in)
SPAN = {5: (4, 38), 6: (3, 39), 7: (3, 39)}
for y in range(8, 26): SPAN[y] = (2, 40)
SPAN.update({26: (2, 40), 27: (3, 39), 28: (3, 39), 29: (4, 38), 30: (6, 36), 31: (8, 34)})
ICE, SOIL, BLOCK = 0, 1, 2
GG93 = '/home/claude/scratch/necro/f1/gg_1_93.npz'
DOOR = [(20, 4), (21, 4), (22, 4)]              # the sealed arch (rows 3-4 of the back wall)
DOOR_LANDING = [(20, 5), (21, 5), (22, 5)]
MAT = [(x, y) for x in (20, 21, 22) for y in (29, 30, 31)]
START = (21, 31)
# the corners: bonfire, the necromancer, the platform of soil (3 x 3)
CORNERS = {
    'NW': dict(plat=[(x, y) for x in (3, 4, 5) for y in (9, 10, 11)], fire=(3, 9), trainer=(5, 9)),
    'NE': dict(plat=[(x, y) for x in (35, 36, 37) for y in (9, 10, 11)], fire=(37, 9), trainer=(35, 9)),
    'SW': dict(plat=[(x, y) for x in (3, 4, 5) for y in (26, 27, 28)], fire=(3, 28), trainer=(5, 28)),
    'SE': dict(plat=[(x, y) for x in (35, 36, 37) for y in (26, 27, 28)], fire=(37, 28), trainer=(35, 28)),
}
# the bronze demon heads kept from the chamber (2x2): only the two by the arch (user 2026-11-21: the four by the
# landing went; one very weathered head, centred, takes the place of the pair on the middle island)
DEMONS = [(18, 5), (23, 5)]
# a small stone gargoyle out on the ice to the right of the landing, where the right-hand demon stood (user)
GARGOYLE = (25, 29)
# the middle island (x 18-24, y 18-21): its two demon heads (cells 19-20 and 22-23, rows 19-20) become one,
# centred on the island to the pixel (it straddles cells 20-22, so those three columns block)
CENTRE_OLD = [(x, y) for x in (19, 20, 22, 23) for y in (19, 20)]
CENTRE_STATUE = [(x, y) for x in (20, 21, 22) for y in (19, 20)]

BRICKS = {0x3f0, 0x3f1, 0x3f2, 0x3f8, 0x3f9, 0x3fa}
def base():
    g = np.full((H, W), BLOCK, np.int8)
    c = np.load(GG93)['cells']
    for y, (a, b) in SPAN.items():
        for x in range(a, b + 1):
            if int(c[y, x]) not in BRICKS: g[y, x] = ICE
    for c in DOOR_LANDING + MAT: g[c[1], c[0]] = SOIL
    for k, v in CORNERS.items():
        for c in v['plat']: g[c[1], c[0]] = SOIL
        g[v['fire'][1], v['fire'][0]] = BLOCK; g[v['trainer'][1], v['trainer'][0]] = BLOCK
    for (x, y) in DEMONS:
        g[y:y + 2, x:x + 2] = BLOCK
    g[GARGOYLE[1], GARGOYLE[0]] = BLOCK
    return g

DIRS = ((0, -1), (0, 1), (-1, 0), (1, 0))
def blocked(g, x, y): return not (0 <= x < W and 0 <= y < H) or g[y, x] == BLOCK
PUSH_OFF = False   # the user's push-off rule, under test in the game (2026-11-21); the engine decides
def move(g, p, d):
    """One move from a place the player has stopped. On soil you walk one step any way. Stopped on the ice you
    can only set off pushing against something (user 2026-11-21): the cell behind you, opposite the way you
    go, must be solid (a grave, a wall, the room's edge); with nothing there you cannot start a slide that way."""
    x, y = p; nx, ny = x + d[0], y + d[1]
    if blocked(g, nx, ny): return None
    if PUSH_OFF and g[y, x] == ICE and not blocked(g, x - d[0], y - d[1]): return None
    if g[ny, nx] == SOIL: return (nx, ny)
    cx, cy = nx, ny
    while True:
        tx, ty = cx + d[0], cy + d[1]
        if blocked(g, tx, ty): return (cx, cy)
        if g[ty, tx] == SOIL: return (tx, ty)
        cx, cy = tx, ty

def bfs(g, s):
    dist = {s: 0}; q = deque([s]); prev = {s: None}
    while q:
        p = q.popleft()
        for d in DIRS:
            n = move(g, p, d)
            if n is not None and n not in dist: dist[n] = dist[p] + 1; prev[n] = (p, d); q.append(n)
    return dist, prev

def targets():
    t = {'door': DOOR_LANDING}
    for k, v in CORNERS.items():
        fx, fy = v['fire']
        t[k] = [(fx + dx, fy + dy) for dx, dy in DIRS if (fx + dx, fy + dy) in v['plat'] and (fx + dx, fy + dy) != v['trainer']]
    return t

def evaluate(g):
    dist, prev = bfs(g, START)
    T = targets(); need = {}
    for k, cells in T.items():
        ds = [dist[c] for c in cells if c in dist]
        if not ds: return None
        need[k] = min(ds)
    # no getting stuck: from every place you can stop, the landing is reachable again (reverse search over the
    # moves between the places you can stop)
    back = {p: [] for p in dist}
    for p in dist:
        for d in DIRS:
            n = move(g, p, d)
            if n is not None: back[n].append(p)
    seen = {START}; q = deque([START])
    while q:
        p = q.popleft()
        for r in back[p]:
            if r not in seen: seen.add(r); q.append(r)
    if len(seen) != len(dist): return None
    return need, len(dist)

def islands():
    """Ghost Grey's islands in its chasm (rows 14-24), kept as patches of grave-soil in the ice; their own
    graves and demon heads kept as stoppers."""
    c = np.load(GG93)['cells']; soil, block = [], []
    for y in range(14, 25):
        for x in range(W):
            m = int(c[y, x])
            if m in (0x281, 0x3fe): continue
            if (x, y) in CENTRE_OLD: soil.append((x, y))
            elif m in (0x3d7, 0x3d4, 0x3d3, 0x3f3, 0x3f4, 0x3fb, 0x3fc): block.append((x, y))
            else: soil.append((x, y))
    soil = [c for c in soil if c not in CENTRE_STATUE]; block += CENTRE_STATUE
    return soil, block

def generate(seed, n_graves=30, n_soil=0, grid=False):
    rng = random.Random(seed)
    g = base()
    isl_soil, isl_block = islands()
    for (x, y) in isl_soil: g[y, x] = SOIL
    for (x, y) in isl_block: g[y, x] = BLOCK
    ice = [(x, y) for y in range(H) for x in range(W) if g[y, x] == ICE]
    keep_clear = set()
    for k, v in CORNERS.items():
        for (x, y) in v['plat']:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1): keep_clear.add((x + dx, y + dy))
    for (x, y) in MAT + DOOR_LANDING:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1): keep_clear.add((x + dx, y + dy))
    ice = [(x, y) for y in range(H) for x in range(W) if g[y, x] == ICE]
    cand = [c for c in ice if c not in keep_clear]
    if grid:                                        # (the drowned graveyard's rows, loosely: every other cell)
        cand = [(x, y) for (x, y) in cand if (y % 2 == 1) and ((x + (y // 2) % 2) % 2 == 0)]
    graves = rng.sample(cand, min(n_graves, len(cand)))
    for (x, y) in graves: g[y, x] = BLOCK
    soil = []
    left = [c for c in cand if c not in graves]
    for (x, y) in rng.sample(left, n_soil):
        for dx in (0, 1):
            if x + dx < W and g[y, x + dx] == ICE: g[y, x + dx] = SOIL; soil.append((x + dx, y))
    return g, graves, soil

def search(trials=3000, seed0=0, **kw):
    best = None; ok = 0
    for t in range(trials):
        g, graves, soil = generate(seed0 + t, **kw)
        r = evaluate(g)
        if r is None: continue
        need, n = r
        corners = [need[k] for k in CORNERS]
        if min(corners) < 6: continue
        score = sum(corners) + 0.5 * need['door'] - 0.15 * max(corners)
        ok += 1
        if best is None or score > best[0]: best = (score, seed0 + t, need, g, graves, soil)
    print('valid layouts', ok, 'of', trials)
    return best

def solution(g, target_cells):
    dist, prev = bfs(g, START)
    end = min((c for c in target_cells if c in dist), key=lambda c: dist[c])
    path = []; p = end
    while prev[p] is not None: q, d = prev[p]; path.append((q, d, p)); p = q
    return path[::-1]

if __name__ == '__main__':
    b = search()
    print('best seed', b[1], 'moves', b[2])
