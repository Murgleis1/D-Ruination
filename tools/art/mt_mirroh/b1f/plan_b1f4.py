"""Mt. Mirroh B1F, tile plan v4: the Blast Crater (user 2026-11-24 chose option B of plan_b1f3.py; the ice hall
dropped).

The Vessels Cult's ritual site, two years after: Harbinger Alaric raised Ting-Lu here on a misaligned Leyline point and
the Mt. Mirroh Dreamstone burst, into the nine Shards. One great round cavern under the mountain:
  * **the crater**: where the altar's dais stood, a pit (after Lazarus' blast pit, facf4c), its far wall lit, its
    depth dark with a faint violet at the bottom (the wound; the only violet light on the floor);
  * **the cracked floor** in rings about it, denser near (Lazarus' crack decal);
  * **the altar**: what is left of it, its cracked table slab tipped over the pit's north lip;
  * **the pillar ring**: the temple's ten pillars (Lazarus facaec's ring), flung outward: three still standing, the
    rest snapped to stumps, their shafts thrown down radially, rubble beyond them;
  * **the rim**: the temple's surviving terrace across the cavern's north, a band of rock, stairs up either side, its
    dressed floor, its facade along the back wall, face on, broken through in places;
  * **the camp**: in an alcove south-west, the cult's, abandoned;
  * **the ladder**: in a short passage south, up to the exterior (9,13).
Letters: '#' rock, '.' floor, 'S' stairs, 'L' ladder, 'D' dressed floor (rim), 'w' facade (solid, on rock),
'P' pit (solid), 'A' altar slab (solid), 'k' cracked floor, 'p' pillar standing (solid), 'b' stump (solid),
'f' fallen shaft (solid), 'r' rubble (solid), 'c' camp (solid).
Usage: python3 plan_b1f4.py OUTDIR"""
import os, sys, math
import numpy as np
from PIL import Image, ImageDraw
W, H = 40, 40
CX, CY = 20, 21                           # the crater's centre (cell)
G = np.full((H, W), '#', dtype='<U1')
def r(x0, y0, x1, y1, ch): G[y0:y1 + 1, x0:x1 + 1] = ch
def ell(cx, cy, rx, ry, ch, only=None):
    for y in range(H):
        for x in range(W):
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1 and (only is None or G[y, x] in only): G[y, x] = ch

# the cavern: a round hall, its edge broken a little (cells cut, cells added), so it is a cave, not a drawn circle
ell(CX, 20, 17.6, 14.6, '.')
for (x, y) in ((4, 12), (3, 13), (36, 13), (37, 14), (3, 27), (36, 28), (35, 30), (5, 29)): G[y, x] = '#'
for (x, y) in ((2, 19), (2, 20), (2, 21), (38, 19), (38, 20), (37, 25)): G[y, x] = '.'
# the rim: the terrace across the north, behind a band, stairs up at both sides
r(10, 3, 30, 7, '.'); r(8, 8, 32, 9, '#'); r(9, 8, 10, 9, 'S'); r(30, 8, 31, 9, 'S')
r(11, 4, 29, 7, 'D'); r(10, 2, 30, 3, '#'); r(11, 3, 29, 3, 'w')
# the pit and its rings of cracked floor
ell(CX, CY, 9.6, 6.6, 'k', only='.')
P = [(15, 25, 18), (14, 26, 19), (14, 26, 20), (14, 26, 21), (14, 26, 22), (15, 25, 23)]
for (x0, x1, y) in P: r(x0, y, x1, y, 'P')
r(18, 17, 22, 17, 'A')                    # the altar's slab, tipped over the north lip
# the pillar ring, radius 12.5 x 8.6 about the crater: k -> (standing?, fall direction outward)
RING = []
for k in range(10):
    a = math.radians(18 + 36 * k)
    x, y = int(round(CX + 12.5 * math.cos(a))), int(round(CY + 8.6 * math.sin(a)))
    RING.append((x, y, a))
STANDING = {2, 6, 9}
SHAFTS = []                      # (south, north-west, east-north-east)
for k, (x, y, a) in enumerate(RING):
    if k in STANDING: G[y, x] = 'p'; continue
    G[y, x] = 'b'
    dx, dy = math.cos(a), math.sin(a)
    # the shaft thrown down outward, lying east-west (as fallen pillars lie in the games): two cells
    if abs(dx) >= abs(dy): cells = [(x + int(math.copysign(1, dx)), y), (x + int(math.copysign(2, dx)), y)]
    else:
        fy = y + int(math.copysign(1, dy)); fx = x if dx >= 0 else x - 1
        cells = [(fx, fy), (fx + 1, fy)]
    for (fx, fy) in cells:
        if G[fy, fx] in '.k': G[fy, fx] = 'f'
    SHAFTS.append(cells)
    rx_, ry_ = int(round(x + dx * 3.6 - dy * 1.0)), int(round(y + dy * 3.6 + dx * 1.0))
    if G[ry_, rx_] == '.': G[ry_, rx_] = 'r'
# stone flung by the blast: boulders strewn outward beyond the ring (as round Lazarus' pit), none on the ways through
import random as _r
_rnd = _r.Random(8); _n = 0
while _n < 12:
    a = _rnd.uniform(0, 2 * math.pi); t = _rnd.uniform(1.18, 1.6)
    x, y = int(round(CX + 12.5 * t * math.cos(a))), int(round(CY + 8.6 * t * math.sin(a)))
    if 0 < x < W - 1 and 10 < y < 33 and G[y, x] == '.' and (G[y - 1:y + 2, x - 1:x + 2] == '.').sum() >= 8 \
            and not (16 <= x <= 24 and y >= 28):
        G[y, x] = 'r'; _n += 1
# the camp's alcove (south-west) and the ladder passage (south)
r(2, 27, 8, 32, '.'); r(3, 28, 5, 29, 'c'); G[31, 3] = 'c'
r(17, 34, 23, 38, '.'); r(17, 38, 18, 38, '#'); r(22, 38, 23, 38, '#'); G[37, 20] = 'L'

SOLID = set('#wPApbfrcL') - {'L'}
SPOTS = {'the ladder': (20, 36), 'the camp': (6, 30), 'the pit lip (south)': (20, 25), 'the rim': (20, 5),
         'east of the pit': (31, 21), 'west of the pit': (8, 21)}

def check():
    L = tuple(np.argwhere(G == 'L')[0]); seen = {L}; st = [L]
    while st:
        y, x = st.pop()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (y + dy, x + dx)
            if 0 <= q[0] < H and 0 <= q[1] < W and q not in seen and G[q] not in SOLID: seen.add(q); st.append(q)
    walk = {tuple(p) for p in np.argwhere(~np.isin(G, list(SOLID)))}
    return sorted(walk - seen), {k: (v[1], v[0]) in seen for k, v in SPOTS.items()}

COL = {'#': (58, 60, 78), '.': (176, 196, 220), 'S': (240, 180, 80), 'L': (250, 220, 60), 'D': (214, 214, 226),
       'A': (120, 90, 160), 'P': (14, 8, 24), 'k': (150, 150, 170), 'p': (240, 240, 250), 'b': (130, 130, 150),
       'f': (170, 160, 190), 'r': (110, 100, 96), 'w': (150, 140, 170), 'c': (190, 120, 70)}
def picture(out, s=12):
    im = Image.new('RGB', (W * s, H * s), (0, 0, 0)); d = ImageDraw.Draw(im)
    for y in range(H):
        for x in range(W): d.rectangle((x * s, y * s, x * s + s - 1, y * s + s - 1), fill=COL[G[y, x]])
    im.save(out)

if __name__ == '__main__':
    un, spots = check(); print('unreachable', un, spots)
    for y in range(H): print('%2d' % y, ''.join(G[y]))
    if len(sys.argv) > 1: picture(os.path.join(sys.argv[1], 'b1f_plan_v4.png'))
