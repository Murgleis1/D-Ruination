"""Mirroh Peak, re-planned (user 2026-11-24): dressed "Mt. Thunder style like 1F"; "re-do that whole final climb to
resemble Mt. Thunder's peak climb more. DM's climb on that part up to the summit is ugly"; the summit's abandoned
ruins in Crown stone, snowed over; the cave mouth to Winterlily Hollow kept but blocked in Chapter 1.
Studied: MonoMyth's Mt. Thunder outdoor maps (0x86d6b0 0x86d678 0x86d694 0x86d6e8 0x86d720 0x86d624) and its summit,
the Peak of Kings (0x86d758): snowfields cut by stacked one-tile cliff bands, stairs set in the bands, a frozen stream
dropping through them in falls, blue ice-grass, snowy pines and boulders; the summit a stepped pyramid of terraces
narrowing to a plateau, the sky all round it.

Plan only (cells, 50x110, DM's size): '#' cliff band, '.' snow, 'g' ice grass, 'T' snowy pine, '~' frozen stream /
pond, 'S' stairs, 'K' sky, 'H' a ruined hut, 'Q' the broken shrine, 'E' the cave mouth from 1F, 'W' the blocked
mouth to Winterlily Hollow, 'P' a raised snow top in DM's foot (scenery, not walked). Writes plan_peak.txt and, with an argument, a colour-blocked picture."""
import os, sys
import numpy as np
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 50, 110
G = np.full((H, W), '#', dtype='<U1')
def r(x0, y0, x1, y1, ch): G[y0:y1 + 1, x0:x1 + 1] = ch

# ---- sky round the summit pyramid ------------------------------------------------------------------------------
r(0, 0, W - 1, 34, 'K')
# ---- the summit (Peak of Kings-like; art v1 review 2026-11-24: its body stacked rock, as the Peak of Kings'). The
# plateau a small oval, its north half receding onto open sky (user 2026-11-24: "scale the north part of the walkable
# peak and ruins back a bit so you can see more of the mountains in the backdrop as you approach the edge"; "recede the
# back part more so that its not a giant square peak area and more rounded/oval in shape ... I just think you made the
# peak too wide and square"; "I don't like how these edges obscure the mountains in the distance"; studied: Ghost
# Grey's Mt. Silver summit, a small crown on a narrow climb with the sky all round it): its rim a snowy lip onto the
# sky all round its north half, the mountain's flanks stepping out a tile a row from its widest row; ledges across the
# flanks between two-row bands, stairs switching sides
OVAL = {8: (22, 27), 9: (21, 28), 10: (20, 29), 11: (19, 30), 12: (18, 31), 13: (18, 31), 14: (19, 30), 15: (20, 29)}
PLATEAU = (18, 8, 31, 15)                               # (its bounding box)
def L_(y): return 99 if y < 12 else max(0, 17 - (y - 12))
def R_(y): return W - 1 - L_(y)
for y in range(12, 35): r(L_(y), y, R_(y), y, '#')
for y, (x0, x1) in OVAL.items(): r(x0, y, x1, y, '.')
TERR = [(18, 22), (25, 28), (31, 33)]                   # (top row, bottom row) of each ledge; bands between
for (t0, t1) in TERR:
    for y in range(t0, t1 + 1): r(L_(y) + 1, y, R_(y) - 1, y, '.')
r(24, 16, 25, 17, 'S')                                  # down off the summit, in the middle
r(12, 23, 13, 24, 'S'); r(36, 29, 37, 30, 'S'); r(12, 34, 13, 34, 'S')   # switchbacks
# the ruins: the broken shrine on the summit's crown, against the sky (the cardinal's place, the stage before it); the
# two huts just below, on the first ledge either side of the stairs down from the summit (the summit itself left to
# the shrine and the stage)
SHRINE, HUTS = (23, 8), ((16, 18), (30, 18))            # (top-left cells; each 4x4)
r(SHRINE[0], SHRINE[1], SHRINE[0] + 3, SHRINE[1] + 3, 'Q')
for (hx, hy) in HUTS: r(hx, hy, hx + 3, hy + 3, 'H')
# ---- the middle climb: snow terraces across the mountain, cut by stepped bands (they rise and fall a row or two
# along their length, as Mt. Thunder's do), stairs in them, part-bands making alcoves, a frozen stream falling
# through the bands at the west edge into a pond, ice grass and pines
def band(pts, ch='#'):
    """a one-tile band through the points, horizontal runs joined by vertical steps"""
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        r(min(x0, x1), y0, max(x0, x1), y0, ch)
        if y1 != y0: r(x1, min(y0, y1), x1, max(y0, y1), ch)
r(1, 35, W - 2, 66, '.')
band([(1, 41), (11, 41), (11, 43), (23, 43), (23, 40), (35, 40), (35, 42), (48, 42)]); r(16, 43, 17, 43, 'S')
band([(1, 50), (15, 50), (15, 48), (29, 48), (29, 51), (48, 51)]);                    r(40, 51, 41, 51, 'S')
band([(1, 59), (21, 59), (21, 61), (37, 61), (37, 58), (48, 58)]);                    r(12, 59, 13, 59, 'S')
band([(27, 36), (40, 36), (40, 38)]); band([(31, 45), (44, 45), (44, 47)]); band([(5, 54), (12, 54), (12, 57)])   # alcoves
r(1, 67, W - 2, 67, '#'); r(22, 67, 23, 67, 'S')                                      # down onto DM's foot
r(1, 35, 1, 66, '#')
r(2, 35, 3, 60, '~'); r(2, 61, 9, 66, '~')                                            # the stream and its pond
def patch(x0, y0, x1, y1, seed):
    """ice grass in a loose drift (as Mt. Thunder's: rounded, ragged edges), only on open snow"""
    import random as _r; rr = _r.Random(seed); cx, cy = (x0 + x1) / 2, (y0 + y1) / 2; rx, ry = (x1 - x0) / 2 + .6, (y1 - y0) / 2 + .6
    for y in range(y0 - 1, y1 + 2):
        for x in range(x0 - 1, x1 + 2):
            d = ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2
            if d <= 0.75 or (d <= 1.25 and rr.random() < 0.55):
                if G[y, x] == '.': G[y, x] = 'g'
patch(20, 37, 25, 39, 1); patch(33, 53, 43, 56, 2); patch(15, 62, 24, 65, 3); patch(5, 45, 9, 48, 4); patch(30, 38, 37, 39, 5)
for x, y in ((44, 37), (7, 36), (14, 45), (24, 45), (46, 54), (27, 54), (44, 63), (30, 64), (16, 37)): r(x, y, x + 1, y + 1, 'T')
# ---- the foot (rows 68-109): Dreamstone Mysteries' own, kept (user 2026-11-24: "the lower area ... that leads up to
# the final climb of the mountain is good and just needs a bit of re-tiling"); read from its map, cell by cell:
# its ice cliffs as bands, its pines, its snowy grass, its stairs, its two cave mouths (DM's drills and signs gone)
import struct as _st
_C = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'codebase'))
_snap = os.path.join(HERE, 'dm_peak_map.bin')
if not os.path.exists(_snap):
    import shutil; shutil.copy(os.path.join(_C, 'data/layouts/MirrohPeak/map.bin'), _snap)
_c = list(_st.unpack('<%dH' % (W * H), open(_snap, 'rb').read()))
TREE = {0x1D4, 0x1D5, 0x1DC, 0x1DD, 0x1E4, 0x1E5, 0x016, 0x211, 0x218, 0x203, 0x3B0, 0x3B1}
GRASS = {0x00D, 0x1C6, 0x1C7}
GONE = {0x003, 0x394, 0x395, 0x39C, 0x39D}
for y in range(68, H):
    for x in range(W):
        v = _c[y * W + x]; m = v & 0x3FF; solid = (v >> 10) & 3
        if m == 0x25E: ch = 'E'
        elif m == 0x29E: ch = 'S'
        elif m in TREE: ch = 'T'
        elif m in GRASS: ch = 'g'
        elif m in GONE: ch = '.'
        elif solid: ch = '#'
        else: ch = '.'
        G[y, x] = ch
G[78, 40] = 'W'                                           # Winterlily Hollow's mouth: kept, blocked in Chapter 1

LEVEL = {'.': 3, 'g': 3, 'S': 0, 'E': 3, 'H': 3, 'Q': 3}
SPOTS = {'from 1F': (26, 102), 'Winterlily (blocked)': (40, 79), 'summit stage': (25, 14), 'cardinal (shrine)': (25, 12),
         'ruined hut': (18, 22), 'ruined hut ': (31, 22), 'stairs to the plateau': (24, 17), 'lookout west': (21, 9), 'lookout east': (28, 9), 'down onto the foot': (22, 67)}

def check():
    walk = lambda ch: ch in '.gSE'
    start = (26, 102); seen = {start}; q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and (nx, ny) not in seen and walk(G[ny, nx]): seen.add((nx, ny)); q.append((nx, ny))
    return seen

def settle_foot():
    """DM's foot has raised ice mesas whose tops are not walked on (scenery, as in Mt. Thunder's outdoor maps). Any
    walkable-looking cell there the walk from 1F cannot reach is one of those: a top of 10+ cells becomes 'P' (a
    raised snow top, drawn but not walked), a sliver of fewer becomes '#' (part of its cliff) -- no sealed pockets."""
    seen = check()
    rest = {(x, y) for y in range(68, H) for x in range(W) if G[y, x] in '.g' and (x, y) not in seen}
    while rest:
        a = rest.pop(); comp = {a}; q = [a]
        while q:
            x, y = q.pop()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (x + dx, y + dy)
                if n in rest: rest.remove(n); comp.add(n); q.append(n)
        for (x, y) in comp: G[y, x] = 'P' if len(comp) >= 10 else '#'

def picture(out):
    from PIL import Image, ImageDraw
    COL = {'#': (52, 62, 92), '.': (236, 244, 252), 'g': (120, 168, 230), 'T': (40, 110, 80), '~': (70, 130, 210),
           'S': (250, 200, 90), 'K': (150, 200, 240), 'H': (150, 140, 130), 'Q': (210, 190, 120), 'E': (10, 10, 10), 'W': (120, 40, 40), 'P': (170, 190, 215)}
    S = 8; im = Image.new('RGB', (W * S + 260, H * S), (20, 22, 30)); d = ImageDraw.Draw(im)
    for y in range(H):
        for x in range(W): d.rectangle((x * S, y * S, x * S + S - 1, y * S + S - 1), fill=COL[G[y, x]])
    for n, (x, y) in SPOTS.items():
        d.ellipse((x * S - 4, y * S - 4, x * S + S + 3, y * S + S + 3), outline=(255, 0, 255), width=2)
        d.line((x * S + S, y * S + 4, W * S + 6, y * S + 4), fill=(255, 0, 255)); d.text((W * S + 10, y * S - 2), n.strip(), fill=(255, 220, 255))
    leg = [('cliff band', '#'), ('snow', '.'), ('ice grass', 'g'), ('pine', 'T'), ('frozen stream / pond', '~'), ('stairs', 'S'),
           ('sky', 'K'), ('ruined hut (Crown stone)', 'H'), ('broken shrine', 'Q'), ('raised top (not walked)', 'P')]
    for i, (n, ch) in enumerate(leg):
        x, y = W * S + 10, 300 + i * 22
        d.rectangle((x, y, x + 14, y + 14), fill=COL[ch], outline=(200, 200, 200)); d.text((x + 20, y + 2), n, fill=(230, 230, 230))
    im.save(out)

settle_foot()

if __name__ == '__main__':
    seen = check()
    miss = [n for n, p in SPOTS.items() if G[p[1], p[0]] in '.gSE' and p not in seen]
    print('walkable from 1F:', len(seen), '| spots unreachable:', miss)
    open(HERE + '/plan_peak.txt', 'w').write('\n'.join(''.join(r_) for r_ in G) + '\n')
    if len(sys.argv) > 1: picture(sys.argv[1])
