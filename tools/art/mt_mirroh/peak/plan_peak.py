"""Mirroh Peak, re-planned (user 2026-11-24): dressed "Mt. Thunder style like 1F"; "re-do that whole final climb to
resemble Mt. Thunder's peak climb more. DM's climb on that part up to the summit is ugly"; the summit's abandoned
ruins in Crown stone, snowed over; the cave mouth to Winterlily Hollow kept but blocked in Chapter 1.
Studied: MonoMyth's Mt. Thunder outdoor maps (0x86d6b0 0x86d678 0x86d694 0x86d6e8 0x86d720 0x86d624) and its summit,
the Peak of Kings (0x86d758): snowfields cut by stacked one-tile cliff bands, stairs set in the bands, a frozen stream
dropping through them in falls, blue ice-grass, snowy pines and boulders; the summit a stepped pyramid of terraces
narrowing to a plateau, the sky all round it.

Plan only (cells, 50x110, DM's size): '#' cliff band, '.' snow, 'g' ice grass, 'T' snowy pine, '~' frozen stream /
pond, 'S' stairs, 'K' sky, 'H' a ruined hut, 'Q' the broken shrine, 'E' the cave mouth from 1F, 'W' the blocked
mouth to Winterlily Hollow. Writes plan_peak.txt and, with an argument, a colour-blocked picture."""
import os, sys
import numpy as np
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 50, 110
G = np.full((H, W), '#', dtype='<U1')
def r(x0, y0, x1, y1, ch): G[y0:y1 + 1, x0:x1 + 1] = ch

# ---- sky round the summit pyramid ------------------------------------------------------------------------------
r(0, 0, W - 1, 34, 'K')
# ---- the summit (Peak of Kings-like): a plateau, then terraces widening downward, stairs switching sides ---------
r(15, 4, 34, 13, '.')                                   # the plateau: the ruins, the shrine, the stage for 8b-8c
r(14, 3, 35, 3, '#'); r(14, 4, 14, 14, '#'); r(35, 4, 35, 14, '#'); r(14, 14, 35, 14, '#')
TERR = [  # (top row, bottom row, x0, x1) of each terrace; its band below it runs one wider each side
    (15, 17, 11, 38), (19, 22, 7, 42), (24, 27, 4, 45), (29, 33, 2, 47)]
for (t0, t1, x0, x1) in TERR:
    r(x0 - 1, t0, x0 - 1, t1 + 1, '#'); r(x1 + 1, t0, x1 + 1, t1 + 1, '#')
    r(x0, t0, x1, t1, '.'); r(x0 - 1, t1 + 1, x1 + 1, t1 + 1, '#')
r(24, 14, 25, 14, 'S')                                  # up onto the plateau, in the middle
r(12, 18, 13, 18, 'S'); r(36, 23, 37, 23, 'S'); r(8, 28, 9, 28, 'S'); r(40, 34, 41, 34, 'S')   # switchbacks
# the ruins: two huts and the broken shrine (north middle), the stage left open in the middle and south
r(16, 5, 19, 8, 'H'); r(30, 5, 33, 8, 'H'); r(23, 4, 26, 6, 'Q')
# ---- the middle climb: snow terraces across the mountain, cut by stepped bands (they rise and fall a row or two
# along their length, as Mt. Thunder's do), stairs in them, part-bands making alcoves, a frozen stream falling
# through the bands at the west edge into a pond, ice grass and pines
def band(pts, ch='#'):
    """a one-tile band through the points, horizontal runs joined by vertical steps"""
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        r(min(x0, x1), y0, max(x0, x1), y0, ch)
        if y1 != y0: r(x1, min(y0, y1), x1, max(y0, y1), ch)
r(1, 35, W - 2, 73, '.')
band([(1, 43), (11, 43), (11, 45), (23, 45), (23, 42), (35, 42), (35, 44), (48, 44)]); r(16, 45, 17, 45, 'S')
band([(1, 53), (15, 53), (15, 51), (29, 51), (29, 54), (48, 54)]);                    r(40, 54, 41, 54, 'S')
band([(1, 63), (21, 63), (21, 65), (37, 65), (37, 62), (48, 62)]);                    r(12, 63, 13, 63, 'S')
band([(27, 37), (40, 37), (40, 40)]); band([(31, 47), (44, 47), (44, 49)]); band([(5, 57), (12, 57), (12, 60)])   # alcoves
r(1, 35, 1, 73, '#')
r(2, 35, 3, 64, '~'); r(2, 65, 10, 70, '~')                                           # the stream and its pond
r(20, 38, 25, 40, 'g'); r(33, 56, 43, 60, 'g'); r(15, 67, 24, 71, 'g'); r(5, 47, 9, 50, 'g'); r(30, 39, 37, 40, 'g')
for x, y in ((44, 38), (7, 37), (14, 48), (24, 48), (46, 57), (27, 58), (44, 68), (30, 70), (16, 39)): r(x, y, x + 1, y + 1, 'T')
# ---- the foot: a snowfield in pines, from the cave mouth out of 1F -----------------------------------------------
r(1, 74, W - 2, 74, '#'); r(26, 74, 27, 74, 'S')
r(1, 75, W - 2, 107, '.')
r(34, 77, 47, 79, '#'); G[78, 40] = 'W'                  # the cliff with Winterlily Hollow's mouth (blocked)
r(16, 99, 36, 101, '#'); G[101, 26] = 'E'                 # the cliff with the cave mouth from 1F
r(1, 108, W - 2, 108, '#')
for x in range(1, W - 2, 2):                              # pines round the field's edges
    for y in (75, 105, 106):
        if G[y, x] == '.' and abs(x - 26) > 4: r(x, y, x + 1, y + 1 if y < 106 else y, 'T')
for y in range(76, 104, 2):
    for x in (1, 46):
        if G[y, x] == '.': r(x, y, x + 1, y + 1, 'T')
r(6, 82, 14, 88, 'g'); r(30, 86, 40, 92, 'g'); r(8, 94, 13, 97, 'g')
for x, y in ((20, 80), (24, 90), (38, 96), (11, 101)): r(x, y, x + 1, y + 1, 'T')
r(0, 0, 0, H - 1, '#') if False else None

LEVEL = {'.': 3, 'g': 3, 'S': 0, 'E': 3, 'H': 3, 'Q': 3}
SPOTS = {'from 1F': (26, 102), 'Winterlily (blocked)': (40, 79), 'summit stage': (25, 10), 'cardinal (shrine)': (25, 7),
         'ruined hut': (18, 9), 'ruined hut ': (31, 9), 'stairs to the plateau': (24, 14)}

def check():
    walk = lambda ch: ch in '.gSE'
    start = (26, 102); seen = {start}; q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in seen and walk(G[ny, nx]): seen.add((nx, ny)); q.append((nx, ny))
    return seen

def picture(out):
    from PIL import Image, ImageDraw
    COL = {'#': (52, 62, 92), '.': (236, 244, 252), 'g': (120, 168, 230), 'T': (40, 110, 80), '~': (70, 130, 210),
           'S': (250, 200, 90), 'K': (150, 200, 240), 'H': (150, 140, 130), 'Q': (210, 190, 120), 'E': (10, 10, 10), 'W': (120, 40, 40)}
    S = 8; im = Image.new('RGB', (W * S + 260, H * S), (20, 22, 30)); d = ImageDraw.Draw(im)
    for y in range(H):
        for x in range(W): d.rectangle((x * S, y * S, x * S + S - 1, y * S + S - 1), fill=COL[G[y, x]])
    for n, (x, y) in SPOTS.items():
        d.ellipse((x * S - 4, y * S - 4, x * S + S + 3, y * S + S + 3), outline=(255, 0, 255), width=2)
        d.line((x * S + S, y * S + 4, W * S + 6, y * S + 4), fill=(255, 0, 255)); d.text((W * S + 10, y * S - 2), n.strip(), fill=(255, 220, 255))
    leg = [('cliff band', '#'), ('snow', '.'), ('ice grass', 'g'), ('pine', 'T'), ('frozen stream / pond', '~'), ('stairs', 'S'),
           ('sky', 'K'), ('ruined hut (Crown stone)', 'H'), ('broken shrine', 'Q')]
    for i, (n, ch) in enumerate(leg):
        x, y = W * S + 10, 300 + i * 22
        d.rectangle((x, y, x + 14, y + 14), fill=COL[ch], outline=(200, 200, 200)); d.text((x + 20, y + 2), n, fill=(230, 230, 230))
    im.save(out)

if __name__ == '__main__':
    seen = check()
    miss = [n for n, p in SPOTS.items() if G[p[1], p[0]] in '.gSE' and p not in seen]
    print('walkable from 1F:', len(seen), '| spots unreachable:', miss)
    open(HERE + '/plan_peak.txt', 'w').write('\n'.join(''.join(r_) for r_ in G) + '\n')
    if len(sys.argv) > 1: picture(sys.argv[1])
