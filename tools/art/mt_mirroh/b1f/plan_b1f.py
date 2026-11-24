"""Mt. Mirroh B1F, plan v1: the scarred site of Harbinger Alaric's Ting-Lu ritual (bible 12: two years ago the Vessels
Cult incarnated Ting-Lu at an ancient altar deep in the Mt. Mirroh caves; the Leyline point was misaligned and the
Mt. Mirroh Dreamstone shattered into the nine Shards; Nemo let the incarnation finish, then killed Alaric and took
Ting-Lu). Made in stage 1, unreachable in Chapter 1: the only way in is the ladder under the Rock Smash rock beside the
exterior's cave mouth (9, 13) (user 2026-11-23). Expands Dreamstone Mysteries' B1F great icy hall (its slippery ice
field with rocks to stop on). Same construction as 1F (Mt. Thunder's interiors: dark slate bands, pale ice floor).

Drawn on 2x2 blocks (24x22 = 48x44 tiles) as 1F's plan, every change of level a rock face with stairs.
Levels (north higher): 1 the landing and the cult's camp (south-west), 2 the ice hall (the middle), 3 the ritual
chamber (north) and Nemo's ledge (north-east, over the chamber).
Letters: '#' rock, '.' floor, ':' slippery ice, 'o' a rock in the ice (stops a slide), 'L' the ladder up, 'S' stairs,
'D' the dais, 'A' the altar, 'O' a ritual standing stone (some toppled), 'f' the fissure (the Leyline scar, a violet
glow, cracking the ice south from the altar), 'c' the cult's camp, 'x' rubble sealing the way east (Winterlily Hollow,
a later chapter), 'n' Nemo's ledge. Usage: python3 plan_b1f.py OUT.png"""
import sys
import numpy as np
from collections import deque
BW, BH = 24, 22; W, H = BW * 2, BH * 2
B = np.full((BH, BW), '#', dtype='<U1')
def r(x0, y0, x1, y1, ch): B[y0:y1 + 1, x0:x1 + 1] = ch
def at(pts, ch):
    for x, y in pts: B[y, x] = ch
# ---- level 1: the landing (south-west) and the passage east; the cult's camp in a side cave
r(2, 16, 6, 19, '.'); at([(3, 16)], 'L')
r(6, 17, 12, 18, '.'); r(12, 15, 14, 18, '.')                 # the passage east to the hall's foot
r(1, 11, 4, 14, '.'); r(3, 14, 4, 16, '.')                    # the camp's cave, north of the landing
at([(1, 11), (2, 11), (1, 12)], 'c')
# ---- the face up into the ice hall (row 14), stairs
at([(13, 14)], 'S')
# ---- level 2: the ice hall (slippery ice, rocks to stop on)
r(6, 8, 19, 13, ':'); r(8, 7, 17, 7, ':')
at([(9, 9), (12, 11), (16, 9), (8, 12), (18, 12), (14, 8), (11, 13)], 'o')
r(20, 10, 21, 11, 'x')                                        # rubble: the way east to Winterlily Hollow, sealed
# ---- the face up into the ritual chamber (row 6), stairs
at([(12, 6)], 'S')
# ---- level 3: the ritual chamber (north), the altar on its dais in a ring of standing stones; Nemo's ledge
r(6, 1, 18, 5, '.'); r(8, 0, 16, 0, '.')
r(10, 1, 14, 4, 'D'); at([(12, 2)], 'A')
at([(8, 1), (16, 1), (7, 3), (17, 3), (9, 5), (15, 5)], 'O')
at([(12, 3), (12, 4), (12, 5), (11, 7), (12, 8), (11, 9), (10, 10)], 'f')
r(19, 1, 22, 3, 'n')                                          # Nemo's ledge: over the chamber's east side
r(19, 4, 21, 4, '.')
SPOTS = {'the ladder (in)': (3, 17), 'the camp': (2, 13), 'the hall stairs': (13, 15), 'across the ice': (12, 7),
         'the altar': (12, 3), "Nemo's ledge": (20, 2), 'the rubble seal': (19, 11)}

COL = {'#': (60, 62, 74), '.': (196, 206, 220), ':': (170, 214, 240), 'o': (90, 96, 110), 'L': (250, 220, 90),
       'S': (240, 180, 80), 'D': (150, 130, 110), 'A': (120, 60, 160), 'O': (110, 100, 90), 'f': (200, 90, 240),
       'c': (190, 120, 70), 'x': (130, 110, 100), 'n': (160, 170, 190)}
LEG = [('rock', '#'), ('cave floor', '.'), ('slippery ice', ':'), ('rock in the ice', 'o'), ('ladder up (exterior)', 'L'),
       ('stairs', 'S'), ('the dais', 'D'), ('the altar', 'A'), ('standing stone', 'O'), ('Leyline fissure', 'f'),
       ("the cult's camp", 'c'), ('rubble (Winterlily, later)', 'x'), ("Nemo's ledge", 'n')]
def picture(out):
    from PIL import Image, ImageDraw
    S = 22; im = Image.new('RGB', (BW * S + 300, BH * S), (24, 22, 28)); d = ImageDraw.Draw(im)
    for y in range(BH):
        for x in range(BW): d.rectangle((x * S, y * S, x * S + S - 1, y * S + S - 1), fill=COL[B[y, x]])
    for n, (x, y) in SPOTS.items():
        d.ellipse((x * S + 5, y * S + 5, x * S + S - 6, y * S + S - 6), outline=(255, 0, 255), width=2)
        d.text((BW * S + 10, 10 + list(SPOTS).index(n) * 14), '%s (%d,%d)' % (n, x, y), fill=(255, 210, 255))
    for i, (n, ch) in enumerate(LEG):
        x, y = BW * S + 10, 130 + i * 16
        d.rectangle((x, y, x + 12, y + 12), fill=COL[ch], outline=(200, 200, 200)); d.text((x + 18, y), n, fill=(230, 230, 230))
    im.save(out)
def walk(ch):
    return ch not in '#oAOx'
def check():
    start = (3, 17); seen = {start}; q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (x + dx, y + dy)
            if 0 <= n[0] < BW and 0 <= n[1] < BH and n not in seen and walk(B[n[1], n[0]]): seen.add(n); q.append(n)
    return [k for k, p in SPOTS.items() if p not in seen]
if __name__ == '__main__':
    print('unreachable:', check())
    if len(sys.argv) > 1: picture(sys.argv[1])
