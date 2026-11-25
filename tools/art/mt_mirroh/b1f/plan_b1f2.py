"""Mt. Mirroh B1F, plan v2 at tile scale (plan v1, plan_b1f.py, approved 2026-11-24: "lets proceed with the design";
"make this map as authentic and strikingly fantastic/beautiful as you can"). Same route as v1 (the ladder in, the
cult's camp, the slippery ice hall, the ritual site north, Nemo's ledge, ruins sealing the way east); its shapes now
drawn in Mt. Thunder's own manner (MonoMyth's 0x86d774: a room raised in concentric banded terraces):
  * **the ritual mound**: the altar on a dais atop three concentric terraces of Mt. Thunder's slate bands, stairs cut
    straight up the south axis through each; the outer terrace a broad ring round it, where the cult stood;
  * **the ice hall** below it to the south, wide, slippery, rocks to stop on;
  * **the landing** (the ladder up, south-west), a short passage, stairs up into the hall;
  * **the camp** in a side cave off the hall's west end; **the ruins** of a gateway in the hall's east end (the way
    east, sealed); **Nemo's ledge** up a stair in the north-east corner, over the mound.
Letters: '#' rock, '.' floor, ':' slippery ice, 'S' stairs (two wide, through a band), 'L' the ladder, 'D' the dais,
'R' ruins (solid, painted over floor), 'o' a rock in the ice, 'c' the camp. Usage: python3 plan_b1f2.py [OUT.png]"""
import sys
import numpy as np
from collections import deque
W, H = 48, 46
G = np.full((H, W), '#', dtype='<U1')
def r(x0, y0, x1, y1, ch): G[y0:y1 + 1, x0:x1 + 1] = ch
def ring(x0, y0, x1, y1, t, ch):
    """a band of thickness t round the inside of the box"""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if min(x - x0, x1 - x, y - y0, y1 - y) < t: G[y, x] = ch
def corners(x0, y0, x1, y1, ch, k=1):
    """round a box's corners by k cells (set to ch)"""
    for i in range(k):
        for j in range(k - i):
            for (x, y) in ((x0 + i, y0 + j), (x1 - i, y0 + j), (x0 + i, y1 - j), (x1 - i, y1 - j)): G[y, x] = ch

# ---- the ritual mound: the outer ring, two banded terraces, the dais on top
r(6, 2, 42, 24, '.'); corners(6, 2, 42, 24, '#', 2)
ring(11, 6, 37, 22, 2, '#')                  # terrace 1's band
ring(15, 9, 33, 19, 2, '#')                  # terrace 2's band
r(19, 12, 29, 17, 'D')                       # the dais (painted: a round stepped platform, the altar on it)
for (y0, y1) in ((21, 22), (18, 19)): r(23, y0, 24, y1, 'S')        # stairs up the south axis
# the north-east alcove and Nemo's ledge above it (a band, stairs up)
r(38, 5, 46, 12, '.'); corners(38, 5, 46, 12, '#', 1)
r(40, 1, 46, 3, '.'); r(40, 4, 46, 4, '#'); r(42, 4, 43, 4, 'S')
# ---- the face between the mound's ring and the ice hall (rows 25-28), stairs
r(23, 25, 24, 28, 'S')
# ---- the ice hall
r(8, 29, 40, 38, ':'); corners(8, 29, 40, 38, '#', 2)
for (x, y) in ((12, 31), (18, 33), (27, 30), (33, 35), (14, 37), (37, 31), (22, 36), (30, 33)): G[y, x] = 'o'
# the camp's side cave, west; the ruins in the east end
r(1, 30, 8, 37, '.'); corners(1, 30, 8, 37, '#', 2); r(2, 31, 4, 33, 'c')
r(41, 30, 46, 37, '.'); corners(41, 30, 46, 37, '#', 1); r(44, 31, 46, 36, 'R')
# ---- the landing (south-west) and the passage up into the hall
r(2, 41, 10, 44, '.'); corners(2, 41, 10, 44, '#', 1); G[41, 4] = 'L'
r(10, 41, 17, 43, '.'); r(15, 39, 16, 40, 'S')
SPOTS = {'the landing': (4, 42), 'the camp': (5, 34), 'the hall (south stairs)': (15, 38), 'the mound stairs': (23, 29),
         'the outer ring': (8, 12), 'the altar': (24, 18), "Nemo's ledge": (43, 2), 'the ruins': (42, 33)}
SOLID = '#oRL'

def check():
    s = (4, 42); seen = {s}; q = deque([s])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (x + dx, y + dy)
            if 0 <= n[0] < W and 0 <= n[1] < H and n not in seen and G[n[1], n[0]] not in SOLID + 'D' or n == (24, 17):
                if 0 <= n[0] < W and 0 <= n[1] < H and n not in seen: seen.add(n); q.append(n)
    return [k for k, p in SPOTS.items() if p not in seen]

COL = {'#': (60, 62, 74), '.': (196, 206, 220), ':': (170, 214, 240), 'o': (90, 96, 110), 'L': (250, 220, 90),
       'S': (240, 180, 80), 'D': (150, 130, 110), 'R': (130, 110, 100), 'c': (190, 120, 70)}
def picture(out):
    from PIL import Image
    im = np.zeros((H, W, 3), np.uint8)
    for ch, c in COL.items(): im[G == ch] = c
    Image.fromarray(im).resize((W * 12, H * 12), Image.NEAREST).save(out)

if __name__ == '__main__':
    print('unreachable:', check())
    if len(sys.argv) > 1: picture(sys.argv[1])
