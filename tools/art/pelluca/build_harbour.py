"""Build Pelluca Harbour, the waterfront as its own map (user 2026-11-25: the approved waterfront, mock v3 with the deeper
stone and the walled quay, built as a separate map below a six-row retaining wall; the stairs split between the maps).

The map (80 x 33): rows 0-2 the town's tree line above the wall (backdrop, solid), rows 3-8 the wall (Pelluca's cliff
courses, its two stairs at x 24-25 and 37-39, the sealed cave door at its foot, x 10-11), rows 9-32 the waterfront of
waterfront_mock.py (its rows 36-59). Its own tileset pair (mapbuild.py).
Cells: sand (MB_SAND), the quay, kerb and the piers' inner columns walkable; the piers' rims, the quay's drop and the
water at the water's level (elevation 1, surfable: MB_OCEAN_WATER); the Tavern, the lab, sheds, cargo, lamps, candle
stands, palms' trunks, the INN board, rocks, the woods, the wall solid. Top layer (the player walks behind): lamp tops,
palm fronds, the pennants, candle flames, crates' upper edges.
Stairs: row 6 of each stair is MB_NON_ANIMATED_DOOR: stepping onto it going up fades to the town's stair (its row 36);
arriving on it from the town the player faces south and takes one step down (the climb carries on).
Doors: the Tavern (28, 16) and the lab (47, 12), non-animated.
Water: MonoMyth's 8-frame water over every water pixel (harbour_water.py).
Usage: python3 tools/art/pelluca/build_harbour.py   (then make)"""
import os, sys, json
import numpy as np
from PIL import Image
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import waterfront_mock as M
import mapbuild as MB
import tilequant as TQN
import harbour_water as HW
C = MB.C
S = 16
NAME, LAYOUT, MAPID = 'PellucaHarbour', 'LAYOUT_PELLUCA_HARBOUR', 'MAP_PELLUCA_HARBOUR'
W, H, DY = 80, 33, 27                      # (harbour row = mock row - 27 for the waterfront)
STAIRS = [24, 25, 37, 38, 39]
CAVE = (10, 11)
MB_SAND, MB_OCEAN, MB_DOOR = 0x21, 0x15, 0x60
TAVERN_DOOR, LAB_DOOR = (28, 43), (47, 39)        # (mock coordinates)
TOWN_PNG = '/home/claude/scratch/pelluca_now.png'

def wall_rows(town):
    """the town's cliff, six courses: its top course (town row 34), then its second (row 35) five times; the cave door
    at the foot (town rows 34-35 at x 10-11 in the bottom two rows), plain wall above it"""
    out = np.zeros((6 * S, W * S, 3), np.uint8)
    cell = lambda x, y: town[y * S:(y + 1) * S, x * S:(x + 1) * S]
    for r in range(6):
        for x in range(W):
            src = 34 if r == 0 else 35
            if x in CAVE:
                c = cell(x, 34 if r == 4 else 35) if r >= 4 else cell(x + 4, src)
            else: c = cell(x, src)
            out[r * S:(r + 1) * S, x * S:(x + 1) * S] = c
    return out

def plan():
    """walkable cells and behaviours in mock coordinates (rows 36-59), and the solid land"""
    walk, beh, land_solid = set(), {}, set()
    for x in range(M.BEACH_X[0], M.BEACH_X[1] + 1):
        for y in range(36, M.WY[x] + 1):
            if x >= 32 and y < 44: continue
            walk.add((x, y)); beh[(x, y)] = MB_SAND
    for (x, y) in M.STAIRS_DOWN: walk.add((x, y)); beh.pop((x, y), None)
    x0, y0, x1, y1 = M.QUAY
    for y in range(y0, y1 + 1):
        for x in range(x0 + 1, x1 + 1): walk.add((x, y))
    K = y1 + 1
    pier_cols = {px + i: (px, w, kr, i) for (px, w, kr, b) in M.PIERS for i in range(w)}
    for x in range(35, x1 + 1):
        if x in pier_cols:
            px, w, kr, i = pier_cols[x]
            walk.add((x, K))                                  # (the kerb row runs on across a pier's root)
            if 0 < i < w - 1:
                for y in range(K + 1, kr + 1): walk.add((x, y))
        else: walk.add((x, K))
    solid = set()
    tx0, ty0, tx1, ty1 = M.TAVERN
    solid |= {(x, y) for x in range(tx0, tx1 + 1) for y in range(ty0, ty1 + 1)} - {TAVERN_DOOR}
    solid |= {(x, y) for x in range(44, 50) for y in range(36, 40)} - {LAB_DOOR}
    solid |= {(23, 44), (24, 44)}                                        # the INN board
    solid |= set(M.SEAWALL)
    for (x, y, m) in M.FLOWERS + M.CRATES: solid.add((x, y))
    for (x, col) in M.STALLS: solid |= {(xx, yy) for xx in range(x, x + 3) for yy in range(36, 39)}
    solid |= set(M.BARRELS) | set(M.CRATES_SMALL) | set(M.SACKS) | set(M.ROPES) | set(M.NETS) | set(M.IRON_LAMPS)
    solid |= set(M.CANDLES)
    for (x, y) in M.BARREL_STACKS: solid |= {(x, y), (x, y + 1)}
    for (x, y) in M.PALMS: solid |= {(x, y), (x + 1, y)}
    for (x, y) in M.ROCKS: land_solid |= {(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)}
    walk -= solid
    return walk, beh, solid | land_solid

def check(walk):
    """every walkable cell reachable from the quay at the main stair's foot (the stairs count as walkable)"""
    start = (38, 37); seen = {start}; q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (x + dx, y + dy)
            if n in walk and n not in seen: seen.add(n); q.append(n)
    return sorted(walk - seen)

def main():
    town = np.array(Image.open(TOWN_PNG).convert('RGB'))
    M.SHIPS = []; M.PEOPLE_AT = []; M.SCENE = []; M.DRAW_SHRINE = False
    flat_m = M.compose(Image.open(TOWN_PNG))
    ground_m = M.SNAP['ground']
    walk_m, beh_m, solid_m = plan()
    # (user 2026-11-25: an NPC "smooshed in some tiny crates") no prop may be drawn into a walkable cell unless it is
    # the top of something standing just below it (the player walks behind it) or the pennants overhead
    overhead = {(x, y) for x in range(35, 42) for y in range(41, 44)}
    spill = []
    for (x, y) in walk_m:
        sl = (slice(y * S, (y + 1) * S), slice(x * S, (x + 1) * S))
        if not (flat_m[sl] != ground_m[sl]).any(): continue
        if (x, y + 1) in solid_m or (x, y) in overhead: continue
        if beh_m.get((x, y)) == MB_SAND: continue
        spill.append((x, y))
    assert not spill, 'props drawn into walkable cells: %s' % sorted(spill)
    pockets = check(walk_m)
    assert not pockets, 'cells walkable but not reachable: %s' % pockets
    bad, clash = M.check_walk(); assert not bad, bad
    # the picture: backdrop, wall, waterfront
    flat = np.concatenate([town[31 * S:34 * S], wall_rows(town), flat_m[36 * S:60 * S]], 0)
    ground = np.concatenate([town[31 * S:34 * S], wall_rows(town), ground_m[36 * S:60 * S]], 0)
    # the lab's top course stands against the wall's bottom row (its old row 40, cut off its old quay stone)
    ref = town[38 * S:39 * S, 40 * S:41 * S]
    for x in range(44, 50):
        c = town[40 * S:41 * S, x * S:(x + 1) * S]; m = (c != ref).any(-1)
        for im in (flat, ground):
            t = im[8 * S:9 * S, x * S:(x + 1) * S]; t[m] = c[m]
    # the top layer: in walkable cells, what the props drew over the ground (on open sand only where a solid thing
    # stands just below: palm fronds over their trunk; the beach's tufts and driftwood stay on the ground)
    top_a = np.zeros(flat.shape[:2], bool)
    for (x, y) in walk_m:
        Y = y - DY; sl = (slice(Y * S, (Y + 1) * S), slice(x * S, (x + 1) * S))
        d = (flat[sl] != ground[sl]).any(-1)
        if not d.any(): continue
        if beh_m.get((x, y)) == MB_SAND and (x, y + 1) not in solid_m: continue
        top_a[sl] |= d
    under = flat.copy(); under[top_a] = ground[top_a]
    both = np.concatenate([flat, under], 0).astype(int)
    q, _ = TQN.quantise(both, n=13); q = q.astype(np.uint8)
    flat_q, under_q = q[:H * S], q[H * S:]
    # cells in harbour coordinates
    walk = {(x, y - DY) for (x, y) in walk_m}
    for x in STAIRS: walk |= {(x, 6), (x, 7), (x, 8)}
    water = set()
    for y in range(9, H):
        for x in range(W):
            m = (x, y + DY)
            if m in walk_m or m in solid_m: continue
            if y + DY <= 45 and (x < 8 or x >= 72): continue                  # (the woods)
            water.add((x, y))
    def beh(x, y):
        if (x, y) in water: return MB_OCEAN
        if y == 6 and x in STAIRS: return MB_DOOR
        if (x, y) == (TAVERN_DOOR[0], TAVERN_DOOR[1] - DY) or (x, y) == (LAB_DOOR[0], LAB_DOOR[1] - DY): return MB_DOOR
        return beh_m.get((x, y + DY), 0)
    b = MB.build(under_q, None, (flat_q, top_a), W, H, walk | water, beh)
    runs = HW.install(b, under, range(9, H))           # MonoMyth's water animation over the waterfront's water
    g = b['grid']
    for y in range(H):
        for x in range(W):
            if (x, y) in water: col, el = 0, 1
            elif (x, y) in walk: col, el = 0, 3
            else: col, el = 1, 3
            g[y, x] = (g[y, x] & 0x3FF) | (col << 10) | (el << 12)
    border = int(g[H - 1, W // 2] & 0x3FF)
    mapj = {'id': MAPID, 'name': NAME, 'layout': LAYOUT, 'music': 'MUS_DR_CROWN_PELLUCA_PIANO',
            'region_map_section': 'MAPSEC_PELLUCA_VALLEY', 'requires_flash': False, 'weather': 'WEATHER_NONE',
            'map_type': 'MAP_TYPE_CITY', 'allow_cycling': True, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None}
    mp = os.path.join(C, 'data/maps', NAME, 'map.json')
    if os.path.exists(mp):
        prev = json.load(open(mp))
        for k in ('warp_events', 'object_events', 'coord_events', 'bg_events'): mapj[k] = prev.get(k, [])
    else:
        for k in ('warp_events', 'object_events', 'coord_events', 'bg_events'): mapj[k] = []
    MB.write(b, NAME, LAYOUT, ('pelluca_harbour_tiles', 'PellucaHarbourTiles'), ('pelluca_harbour', 'PellucaHarbour'), mapj,
             border=[border] * 4, after_layout='LAYOUT_PELLUCA_CITY', after_map='PellucaCity')
    HW.wire(runs)
    print('harbour built: tiles', len(b['tiles']), 'metatiles', len(b['meta']), 'palettes', len(b['pals']))

if __name__ == '__main__':
    main()
