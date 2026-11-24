"""The first slip into Ancient Cormoria (Beat 8e), plan v1 (user 2026-11-24: "proceed with a new design for our first
foray into Ancient Cormoria. You can study the first one with all the sand and stuff, but it needs to be remade into
something more visually arresting. Study the desert areas of Sandwell from Monomyth and others ... There's this big
monster skeleton buried in the desert we can use as part of the landscape ... get as many good visual ideas as you
can and come up with something cool").

Studied (assets/ancient_cormoria_reference/moodboard_v1.png): Dreamstone Mysteries' Ancient Mirroh (a sandy canyon of
channels and plateaus round a jade tower); MonoMyth's Sandwell desert (dune bands, palms, cacti, darker sand), the
canyon north-east of Sandwell where Santana is fought (a desert graveyard ring, the giant skull and bone spikes in the
sand), its red-rock canyon country (cliff pueblos, rippled dunes, a river with falls and rope bridges, mesas, a
carved amphitheatre wall), its oasis and its pink crystal-sand basin.

The place: Mirroh, ages before the Empire, before the mountain froze: a red-rock canyon under a hot sky, the dunes in
its floor, a river from the mesa, the cliff homes of a people long gone, and in the sand the bones of a colossal dragon.
The player arrives in a ring of dreamstone obelisks on sand turned pink by their power (south); walks north through
the rib cage of the great skeleton; crosses the dunes and the canyon floor; crosses the river by a rope bridge below the
falls; climbs past the cliff dwellings to the mesa's top, where an altar in a second ring of obelisks stands on the
rim over the sunset (the resonance: where the slip ends). The sky behind the rim: MonoMyth's bastion backdrop in its
own sunset colours (the Peak's sky, ages earlier: the same mountains).

Cells (50 x 56): 'K' sky, '#' red-rock cliff, 'm' mesa top, '.' sand, 'r' rippled dune, 'p' pink crystal sand,
'~' river, 'F' falls, 'B' rope bridge, 'S' stairs / ladder, 'O' dreamstone obelisk, 'A' the altar, 'D' a cliff
dwelling (ruin, closed), 'P' carved panels in the cliff, 'X' the skull, 'x' spine and bones, 'R' a rib arching over
(walked under), 'T' palm, 'c' cactus, 'o' oasis pool, 'g' oasis grass.
Usage: python3 plan_slip.py [OUT.png]"""
import os, sys
import numpy as np
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 50, 56
G = np.full((H, W), '.', dtype='<U1')
def r(x0, y0, x1, y1, ch): G[y0:y1 + 1, x0:x1 + 1] = ch
def ell(cx, cy, rx, ry, ch, only=None):
    for y in range(max(0, int(cy - ry) - 1), min(H, int(cy + ry) + 2)):
        for x in range(max(0, int(cx - rx) - 1), min(W, int(cx + rx) + 2)):
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1 and (only is None or G[y, x] in only): G[y, x] = ch

# ---- the frame: red rock all round; the sky above the mesa's rim
r(0, 0, W - 1, H - 1, '#')
r(0, 0, W - 1, 6, 'K')
# ---- the mesa (north): its top an oval on the rim over the sunset, the altar in a ring of obelisks; its face below
MESA = {7: (19, 30), 8: (17, 32), 9: (16, 33), 10: (15, 34), 11: (15, 34), 12: (15, 34), 13: (16, 33)}
for y, (x0, x1) in MESA.items(): r(x0, y, x1, y, 'm')
for (x, y) in ((20, 8), (29, 8), (17, 10), (32, 10), (18, 12), (31, 12)): G[y, x] = 'O'
r(24, 9, 25, 10, 'A')
r(24, 14, 25, 18, 'S')                                   # (the stair cut up the mesa's face, rows 14-18)
# ---- the river plain (rows 19-31): the river from the falls in the mesa's east face, west across the plain
r(9, 19, 41, 31, '.')
FALLS = [(40, y) for y in range(15, 19)] + [(41, y) for y in range(15, 19)]
for (x, y) in FALLS: G[y, x] = 'F'
river = [(41, 19), (40, 21), (37, 22), (33, 23), (29, 24), (26, 25), (22, 25), (18, 26), (14, 26), (10, 27), (6, 27), (2, 28), (0, 28)]
for (ax, ay), (bx, by) in zip(river, river[1:]):
    n = max(abs(bx - ax), abs(by - ay)) * 2 + 1
    for t in np.linspace(0, 1, n):
        x, y = int(round(ax + (bx - ax) * t)), int(round(ay + (by - ay) * t))
        for dy in (0, 1, 2):
            for dx in (-1, 0, 1):
                if 0 <= x + dx < W and 0 <= y + dy < H and G[y + dy, x + dx] in '.#': G[y + dy, x + dx] = '~'
for y in range(23, 30):                                  # the rope bridge below the falls
    for x in (24, 25):
        if G[y, x] == '~': G[y, x] = 'B'
# the west wall: the cliff homes of a people long gone, in tiers, with ladders (ruins: closed by fallen rock)
r(1, 19, 8, 31, '#')
for (x0, y0) in ((2, 19), (5, 19), (2, 23), (5, 23)): r(x0, y0, x0 + 2, y0 + 1, 'D')
for y in (21, 25): G[y, 8] = 'S'
# the east wall: a carved face, panels of the old people's figures; the oasis below it
r(42, 19, 48, 31, '#')
for y in (21, 24, 27, 30): G[y, 42] = 'P'
ell(36, 29, 3.0, 1.6, 'o', only='.'); ell(36, 29, 4.4, 2.6, 'g', only='.')
for (x, y) in ((32, 28), (40, 30), (31, 31), (12, 21), (15, 30), (38, 21)): G[y, x] = 'T'
# ---- the step down to the dunes: a red-rock band across the canyon (rows 32-33), stairs in it
r(1, 32, 48, 33, '#'); r(24, 32, 25, 33, 'S'); r(10, 32, 11, 33, 'S')
# ---- the dune field (rows 34-54), widening south
for y in range(34, 55):
    w = 22 if y < 50 else 22 - (y - 49) * 3
    for x in range(25 - w, 25 + w + 1):
        if 0 < x < W - 1: G[y, x] = '.'
# sandstone hoodoos standing in the dunes (2x2 / 2x3 pillars)
for (x, y, h) in ((7, 46, 3), (14, 36, 2), (32, 36, 2), (44, 46, 3), (16, 50, 2), (35, 51, 2), (41, 38, 2)): r(x, y, x + 1, y + h - 1, '#')
# the colossal dragon in the sand: its skull east (facing west), its spine curving west along the dunes, its ribs
# arching over the way (the path runs under them), a forelimb's claw bones before the skull, the tail tip west
r(37, 40, 42, 44, 'X')
spine = [(36, 42), (34, 43), (31, 43), (28, 42), (25, 42), (22, 42), (19, 43), (16, 43), (13, 42), (10, 41), (7, 41), (5, 40)]
for (x, y) in spine:
    if G[y, x] == '.': G[y, x] = 'x'
G[42, 24] = G[42, 25] = '.'                              # (the way: between two vertebrae)
for x in (21, 23, 26, 28):                               # the ribs over the way (walked under)
    for y in (43, 44, 45): G[y, x] = 'R'
for x in (14, 17, 31, 33):                               # the ribs either side, standing in the sand (solid)
    for y in (44, 45): G[y, x] = 'x'
for (x, y) in ((34, 47), (35, 48), (37, 47)): G[y, x] = 'x'   # (a forelimb's claw)
for (x, y) in ((9, 38), (39, 49), (6, 51), (43, 41), (20, 37), (29, 38)): G[y, x] = 'c'
for (x, y) in ((11, 45), (29, 52), (40, 35)): G[y, x] = 'T'
# rippled dunes; pink crystal sand round the arrival ring (the obelisks' power soaked into it)
for (cx, cy, rx, ry) in ((10, 48, 5, 2.2), (39, 46, 5, 2.0), (12, 38, 4, 1.6), (36, 37, 4, 1.4), (24, 38, 5, 1.4)):
    ell(cx, cy, rx, ry, 'r', only='.')
ell(25, 50, 6, 3.0, 'p', only='.r')
for (x, y) in ((21, 48), (29, 48), (20, 50), (30, 50), (22, 52), (28, 52)): G[y, x] = 'O'
ARRIVE = (25, 50)
G[H - 1, :] = '#'
SPOTS = {'arrival (the obelisk ring)': ARRIVE, 'under the ribs': (25, 44), 'the skull': (40, 45),
         'up the step': (24, 33), 'the oasis': (38, 31), 'the rope bridge': (24, 26), 'cliff homes (ladder)': (9, 21),
         'carved panels': (41, 24), 'the mesa stair': (24, 18), 'the altar on the rim': (24, 11)}

def check():
    walk = lambda ch: ch in '.rpmSBgRA'
    start = ARRIVE; seen = {start}; q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in seen and walk(G[ny, nx]): seen.add((nx, ny)); q.append((nx, ny))
    return seen

COL = {'K': (232, 150, 90), '#': (150, 72, 52), 'm': (196, 112, 78), '.': (236, 206, 140), 'r': (222, 186, 118),
       'p': (240, 180, 196), '~': (60, 150, 210), 'F': (200, 232, 250), 'B': (140, 96, 56), 'S': (250, 210, 100),
       'O': (120, 70, 200), 'A': (250, 240, 255), 'D': (120, 56, 40), 'P': (90, 40, 30), 'X': (250, 250, 240),
       'x': (220, 216, 200), 'R': (190, 186, 170), 'T': (60, 150, 70), 'c': (90, 170, 80), 'o': (40, 120, 200), 'g': (130, 200, 140)}
LEG = [('red-rock cliff', '#'), ('mesa top', 'm'), ('sand', '.'), ('rippled dune', 'r'), ('pink crystal sand', 'p'),
       ('river / falls', '~'), ('rope bridge', 'B'), ('stairs, ladders', 'S'), ('dreamstone obelisk', 'O'),
       ('the altar', 'A'), ('cliff dwelling (ruin)', 'D'), ('carved panels', 'P'), ('the skull', 'X'),
       ('spine, bones', 'x'), ('rib (walked under)', 'R'), ('palm / cactus', 'T'), ('oasis', 'o'), ('sky (backdrop)', 'K')]

def picture(out):
    from PIL import Image, ImageDraw
    S = 10; im = Image.new('RGB', (W * S + 280, H * S), (24, 22, 28)); d = ImageDraw.Draw(im)
    for y in range(H):
        for x in range(W): d.rectangle((x * S, y * S, x * S + S - 1, y * S + S - 1), fill=COL[G[y, x]])
    for n, (x, y) in SPOTS.items():
        d.ellipse((x * S - 4, y * S - 4, x * S + S + 3, y * S + S + 3), outline=(255, 0, 255), width=2)
        d.line((x * S + S, y * S + 4, W * S + 6, y * S + 4), fill=(255, 0, 255)); d.text((W * S + 10, y * S - 2), n, fill=(255, 220, 255))
    for i, (n, ch) in enumerate(LEG):
        x, y = W * S + 10, 330 + i * 12
        d.rectangle((x, y, x + 10, y + 10), fill=COL[ch], outline=(200, 200, 200)); d.text((x + 16, y), n, fill=(230, 230, 230))
    im.save(out)

if __name__ == '__main__':
    seen = check()
    miss = [n for n, p in SPOTS.items() if p not in seen]
    print('walkable from the arrival:', len(seen), '| spots unreachable:', miss)
    if len(sys.argv) > 1: picture(sys.argv[1])
