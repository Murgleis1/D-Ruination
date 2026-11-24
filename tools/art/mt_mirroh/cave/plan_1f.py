"""Mt. Mirroh 1F, re-drawn in Glittering Grotto's grammar (user 2026-11-23: the DM layout re-skinned "looks really
awful"; "do it": a new layout on the same route). Plan only: walkable areas by level, rock, the frozen streams and
their bridges, stairs, the ledge, exits and the story spots.

Drawn on a grid of 2x2 blocks (30x30 blocks = the 60x60 map), so every rock mass, wall and passage is at least two
tiles thick, as the Grotto's own masses are; every change of level is a rock face with stairs in it (or the one-way
ledge), so nothing is an invisible wall. Shapes placed by hand.

Levels (higher is north, as the GBA draws it): 1 the lower caves (way in, rest stop, streams), 2 the upper level
(stair A), 3 the top band (stair B): the rubble with the Shard west; the torture spot and the exit to the Peak east;
the ledge drops from the top band's east end back down to the lower caves (the way out without the climb).
Writes plan_1f.txt (the 60x60 grid) and, with an argument, a colour-blocked picture."""
import os, sys
import numpy as np
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__))
BW = 30; W = H = 60
B = np.full((BW, BW), '#', dtype='<U1')
def r(x0, y0, x1, y1, ch): B[y0:y1 + 1, x0:x1 + 1] = ch
def at(pts, ch):
    for x, y in pts: B[y, x] = ch

# ---- level 3: the top band --------------------------------------------------------------------------------------
r(1, 1, 3, 2, ';')                      # the rubble's pocket, west
r(3, 2, 9, 2, ';'); r(6, 1, 9, 1, ';')
r(9, 1, 13, 3, ';'); r(13, 2, 17, 3, ';'); r(17, 1, 21, 2, ';'); r(21, 2, 23, 3, ';')
r(23, 1, 28, 4, ';')                    # the torture chamber, east (Sword Cultists and the Beads cultist)
at([(11, 1)], '#'); at([(26, 2)], '#')  # a pillar in the gallery and one in the chamber
at([(27, 0)], 'X')                      # the exit up to the Peak
at([(2, 1)], 'R')                       # the rubble (the Shard)
r(25, 5, 27, 5, 'v')                    # the ledge (one-way, south)
# ---- the face between top band and upper level (row 4), stair B ------------------------------------------------
at([(19, 4)], 'B')
# ---- level 2: the upper level ------------------------------------------------------------------------------------
r(3, 5, 8, 7, ','); r(8, 6, 13, 7, ','); r(12, 5, 17, 7, ','); r(17, 5, 21, 6, ',')
at([(15, 6)], '#')                      # the big ice crystal's plinth
# ---- the face between upper level and lower caves (row 8), stair A -----------------------------------------------
at([(5, 8)], 'A')
# ---- level 1: the lower caves ------------------------------------------------------------------------------------
r(2, 9, 9, 12, '.'); r(1, 12, 8, 16, '.'); r(3, 16, 9, 17, '.')          # the west cave
at([(4, 13)], '#'); at([(7, 10)], '#')
r(10, 10, 10, 18, '~'); at([(10, 13)], '=')                               # stream 1 and its bridge
r(11, 10, 16, 13, '.'); r(11, 13, 17, 17, '.'); r(13, 9, 15, 9, '.')     # the middle cave
at([(14, 11)], '#'); at([(13, 15)], '#')
r(18, 10, 18, 20, '~'); at([(18, 15)], '=')                               # stream 2 and its bridge
r(19, 10, 22, 13, '.'); r(19, 13, 21, 19, '.')                            # the east cave
at([(21, 16)], '#')
r(17, 20, 23, 22, '.'); r(18, 19, 22, 20, '.')                             # the rest stop (nurse), at stream 2's foot
at([(18, 20)], '#')                     # stream 2 runs into the rock above the rest stop
r(24, 19, 28, 28, '.'); r(23, 22, 24, 23, '.')                             # the way-in hall
at([(26, 23)], '#')
at([(27, 29)], 'E')
r(25, 6, 28, 18, '.')                                                      # the east passage up to the ledge's foot
at([(27, 9)], '#'); at([(25, 14)], '#')

# ---- links and hand-made irregularities (bites into rock, bulges of rock), block coordinates --------------------
r(9, 12, 9, 14, '.')                   # the west cave reaches bridge 1
r(18, 3, 20, 3, ';')                   # the top band reaches stair B
for x, y, ch in [
        # top band: a wider bay mid-gallery, a nook, a bulge
        (15, 1, ';'), (16, 1, ';'), (7, 3, ';'), (8, 3, ';'), (19, 1, '#'), (22, 4, ';'),
        # upper level: a bay north, a nook south-east, bulges
        (10, 5, ','), (11, 5, ','), (20, 7, ','), (21, 7, ','), (3, 7, '#'), (13, 7, '#'),
        # west cave: bays and a bulge
        (1, 10, '.'), (1, 11, '.'), (6, 18, '.'), (7, 18, '.'), (9, 9, '#'), (2, 16, '.'),
        # middle cave: a bay north-west, a bay south, a bulge
        (11, 9, '.'), (12, 9, '.'), (14, 18, '.'), (15, 18, '.'), (16, 10, '#'), (11, 17, '#'),
        # east cave: a nook north-east, a bulge
        (22, 9, '.'), (23, 11, '.'), (23, 12, '.'), (22, 18, '.'), (21, 10, '#'),
        # east passage: bays and a bulge
        (24, 8, '.'), (24, 9, '.'), (24, 16, '.'), (28, 13, '#'),
        # the way-in hall: bays and bulges
        (23, 25, '.'), (23, 26, '.'), (28, 21, '#'), (24, 27, '#'), (17, 23, '.'), (18, 23, '.')]:
    B[y, x] = ch

# ---- smoothing (user 2026-11-23: "a lot of broken looking cliffs"): no one-block stubs of rock poking into a cave
# (rock with floor on three sides) and no one-block nicks into the rock (floor with rock on three sides); Mt. Thunder's
# walls run long and turn cleanly. The crystal islands and the plinth stay (they are props, not cliffs).
KEEP = {(15, 6), (26, 2), (11, 1), (7, 10), (13, 15), (27, 9), (26, 23)}
def smooth():
    for _ in range(4):
        changed = False
        for y in range(1, BW - 1):
            for x in range(1, BW - 1):
                if (x, y) in KEEP: continue
                c = B[y, x]; n4 = [B[y - 1, x], B[y + 1, x], B[y, x - 1], B[y, x + 1]]
                if c == '#':
                    fl = [v for v in n4 if v in '.,;']
                    if len(fl) >= 3 and len(set(fl)) == 1: B[y, x] = fl[0]; changed = True
                elif c in '.,;':
                    if sum(v == '#' for v in n4) >= 3 and all(v in '#' + c for v in n4): B[y, x] = '#'; changed = True
        if not changed: break
B[1, 4:6] = ';'                        # (a two-block lump hanging from the gallery's north wall: gone)
smooth()

# ---- the crystal maze (user 2026-11-23: the long thin wall between the east cave and the east passage "needs to be
# something completely different with better more interesting rocks or a lot of crystals like a whole mini maze of
# them"): the east cave and the east passage become one field, blocks x 21-28, y 9-19, walled by great ice crystals
# and snowy boulders ('C') in a seeded maze; rooms on odd columns and rows, every room reachable, open to the east
# passage's head (north, by the ledge's foot), the hall (south) and bridge 2 (west, room (21, 15)).
import random as _r
MX0, MX1, MY0, MY1 = 21, 28, 9, 19
for y in range(MY0, MY1 + 1):
    for x in range(MX0, MX1 + 1): B[y, x] = 'C'
rooms = [(x, y) for x in range(MX0, MX1 + 1, 2) for y in range(MY0, MY1 + 1, 2)]
for x, y in rooms: B[y, x] = '.'
rnd = _r.Random(23); seen = {rooms[0]}; stack = [rooms[0]]
while stack:
    x, y = stack[-1]
    nb = [(x + dx, y + dy) for dx, dy in ((2, 0), (-2, 0), (0, 2), (0, -2)) if (x + dx, y + dy) in rooms and (x + dx, y + dy) not in seen]
    if not nb: stack.pop(); continue
    nx, ny = rnd.choice(nb); B[(y + ny) // 2, (x + nx) // 2] = '.'; seen.add((nx, ny)); stack.append((nx, ny))
for x, y in rnd.sample([p for p in rooms], 4):                       # a few loops, so it is a maze, not a corridor
    for dx, dy in ((1, 0), (0, 1)):
        if MX0 <= x + dx <= MX1 and MY0 <= y + dy <= MY1 and B[y + dy, x + dx] == 'C' and (x + 2 * dx, y + 2 * dy) in rooms:
            B[y + dy, x + dx] = '.'; break
B[MY0 - 1, 25] = '.'; B[MY1 + 1, MX0:MX1 + 1] = '.'                  # open north (the passage's head) and south (the hall)

LEVEL = {'.': 3, ',': 4, ';': 5, 'A': 0, 'B': 0, '=': 3, 'X': 5, 'E': 3, 'R': 5, '|': 3, 'r': 3}

def upscale():
    G = np.repeat(np.repeat(B, 2, 0), 2, 1)
    for y in range(BW):
        for x in range(BW):
            c = B[y, x]
            if c == 'v':                   # a ledge block: the ledge row, then the landing below it
                G[2 * y, 2 * x:2 * x + 2] = 'v'; G[2 * y + 1, 2 * x:2 * x + 2] = '.'
            if c == 'X':
                G[2 * y:2 * y + 2, 2 * x:2 * x + 2] = '#'; G[1, 54] = 'X'
            if c == 'E':
                G[2 * y:2 * y + 2, 2 * x:2 * x + 2] = '#'; G[58, 55] = 'E'
            if c == 'R':
                G[2 * y:2 * y + 2, 2 * x:2 * x + 2] = ';'; G[2 * y, 2 * x] = 'R'
    return G
G = upscale()

# ---- the two crossings as ravines (user 2026-11-23: "why not do wider bodies of water then make bridge like this" -
# Mt. Thunder's plank bridge with rails, spanning cliff to cliff): a frozen river four tiles wide in a ravine, a cliff
# two tiles thick on each side ('|'), rock across both ends (the river runs under the rock); the bridge three rows tall:
# rails above and below ('r', solid), the walkway between ('=', the only way across), its posts on the cliffs.
RAVINES = [dict(x0=18, y0=20, y1=37, path=27), dict(x0=34, y0=20, y1=39, path=31)]
for R in RAVINES:
    x0 = R['x0']
    G[R['y0'] - 2:R['y1'] + 3, x0:x0 + 8] = '#'                       # rock round the ends
    G[R['y0']:R['y1'] + 1, x0:x0 + 2] = '|'; G[R['y0']:R['y1'] + 1, x0 + 6:x0 + 8] = '|'
    G[R['y0']:R['y1'] + 1, x0 + 2:x0 + 6] = '~'
    G[R['path'] - 1, x0:x0 + 8] = 'r'; G[R['path'] + 1, x0:x0 + 8] = 'r'; G[R['path'], x0:x0 + 8] = '='
# ---- ridges (user 2026-11-24: "way too much open space overall everywhere"; "study Mt. Thunder and other interior
# mountain maps across Crown, MonoMyth and Odyssey"): measured, those caves keep almost no open floor wider than seven
# tiles (about 1% of it; this floor had 9%), dividing their rooms with one-tile rock ridges into terraces, alcoves
# and zigzags (assets/mt_mirroh_reference/cave_study_sheet.png). One-tile ridges here, as Mt. Thunder draws them,
# each leaving the route a gap of at least two tiles (cell coordinates, inclusive).
RIDGES = [
    # the west cave: a terrace across its north-west, an alcove south-west, a spur from the south wall
    (2, 24, 8, 24), (6, 25, 6, 28), (2, 31, 9, 31), (13, 30, 13, 35), (13, 20, 13, 22),
    # the middle cave: an alcove north (behind a ridge), a spur south
    (26, 22, 29, 22), (30, 34, 33, 34), (29, 28, 29, 30),
    # the upper level: a zigzag of spurs from its north and south walls
    (18, 10, 18, 12), (24, 13, 24, 15), (36, 10, 36, 12), (12, 13, 12, 15),
    # the top band: spurs from either wall, so the gallery winds
    (11, 2, 11, 3), (17, 4, 17, 5), (30, 2, 30, 3), (37, 4, 37, 5), (43, 2, 43, 4),
    # the hall: a ridge splitting off the camp's south side, a spur by the way in
    (48, 49, 53, 49), (48, 50, 48, 53), (56, 52, 56, 55),
]
for x0, y0, x1, y1 in RIDGES: G[y0:y1 + 1, x0:x1 + 1] = '#'
SPOTS = {'rubble: the Shard': (4, 2), 'torture spot (8a)': (50, 5), 'exit to the Peak': (54, 1), 'stair A': (10, 16),
         'stair B': (38, 8), 'ledge (one-way down)': (52, 10), 'rest stop (nurse)': (40, 44), 'way in': (55, 58),
         'bridge 1': (21, 27), 'bridge 2': (37, 31), 'big ice crystal': (30, 12)}

def check():
    walk = lambda ch: ch not in '#~v|rC'
    start = (55, 57); seen = {start}; q = deque([start])
    while q:
        x, y = q.popleft(); e = LEVEL.get(G[y, x], 3)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < W and 0 <= ny < H) or (nx, ny) in seen: continue
            ch = G[ny, nx]
            if ch == 'v':
                if dy == 1 and walk(G[ny + 1, nx]): seen.add((nx, ny + 1)); q.append((nx, ny + 1))
                continue
            if not walk(ch): continue
            ne = LEVEL.get(ch, 3)
            if e and ne and e != ne: continue
            seen.add((nx, ny)); q.append((nx, ny))
    probs = [n for n, p in SPOTS.items() if G[p[1], p[0]] not in '#~' and p not in seen and G[p[1], p[0]] not in 'vR']
    steps = [((x, y), (x + dx, y + dy)) for y in range(H - 1) for x in range(W - 1) for dx, dy in ((1, 0), (0, 1))
             if G[y, x] in '.,;' and G[y + dy, x + dx] in '.,;' and G[y, x] != G[y + dy, x + dx]]
    # the caves must not touch a ravine's water or the outside of its walls except through the bridge

    return probs, steps, seen

def picture(out):
    from PIL import Image, ImageDraw
    COL = {'C': (190, 230, 255), '|': (70, 80, 110), 'r': (120, 90, 60), '#': (34, 44, 70), '.': (150, 196, 228), ',': (110, 200, 150), ';': (236, 200, 120), '~': (60, 120, 200),
           '=': (150, 110, 80), 'A': (255, 255, 255), 'B': (255, 255, 255), 'v': (255, 120, 60), 'X': (10, 10, 10),
           'E': (10, 10, 10), 'R': (240, 220, 40)}
    S = 14; im = Image.new('RGB', (W * S, H * S + 110), (20, 22, 30)); d = ImageDraw.Draw(im)
    for y in range(H):
        for x in range(W):
            d.rectangle((x * S, y * S, x * S + S - 1, y * S + S - 1), fill=COL[G[y, x]])
    for n, (x, y) in SPOTS.items():
        d.ellipse((x * S - 4, y * S - 4, x * S + S + 3, y * S + S + 3), outline=(255, 0, 255), width=2)
        tw = d.textlength(n); tx = min(max(2, x * S - tw / 2), W * S - tw - 2); ty = y * S + S + 4 if y < 55 else y * S - 14
        d.rectangle((tx - 2, ty - 1, tx + tw + 2, ty + 11), fill=(0, 0, 0)); d.text((tx, ty), n, fill=(255, 220, 255))
    leg = [('lower caves (level 1)', '.'), ('upper level (2)', ','), ('top band (3)', ';'), ('rock', '#'),
           ('frozen stream (impassable)', '~'), ('bridge', '='), ('stairs', 'A'), ('ledge, one-way down', 'v')]
    for i, (n, ch) in enumerate(leg):
        x, y = 10 + (i % 4) * 210, H * S + 12 + (i // 4) * 24
        d.rectangle((x, y, x + 16, y + 16), fill=COL[ch], outline=(200, 200, 200)); d.text((x + 22, y + 3), n, fill=(230, 230, 230))
    d.text((10, H * S + 66), 'way in -> rest stop -> east cave -> bridge 2 -> middle cave -> bridge 1 -> west cave -> stair A -> '
           'upper level -> stair B -> top band', fill=(230, 230, 230))
    d.text((10, H * S + 82), 'top band: rubble + Shard (west); torture spot + exit to the Peak (east); the ledge drops back to '
           'the east passage and the way in', fill=(230, 230, 230))
    im.save(out)

if __name__ == '__main__':
    probs, steps, seen = check()
    print('walkable from the way in:', len(seen), '| spots unreachable:', probs, '| level steps without stairs:', len(steps), steps[:6])
    open(HERE + '/plan_1f.txt', 'w').write('\n'.join(''.join(r) for r in G) + '\n')
    if len(sys.argv) > 1: picture(sys.argv[1])
