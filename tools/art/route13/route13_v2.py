"""Route 13 mock v2 (zone plan v3 approved by the user 2026-11-22: 40x124; v1 was too short; after MonoMyth's
northern routes). Composed in pixels with collision and behaviour alongside, ready for tools/art/mapbuild.py.

Sources (credit): MonoMyth (permission pending before release): two climbs lifted whole from its Route 22 (header
0x869874), keeping its own collision and stairs: its rows 57-74 (a stair, a meadow of its ice grass, a stair) as
TERRACES I, its rows 15-46 (a defile of rock walls and side-stairs, then a central stairway) as the DEFILE and
TERRACES II; Fort Elderflower's pieces (its Route 23 shares the tileset): snow, pines, rocks, boulders, rock arches,
its ice grass (0xf0), its stone stairs (0x47/0xe1), its log rails (0x350-0x352, laid two deep as a bridge deck);
Ghost Grey (JoeyZeed): the reflecting ice (the tarn, the stream); Crown: the signpost; Mirroh's north wall (built).
Behaviours: MonoMyth's 0x5a (its snow grass) -> MB_TALL_GRASS; 0x5b (its snow) -> normal; its sideways and rock
stairs (0x49-0x4f) are the same numbers in our engine and are kept.
Usage: python3 tools/art/route13/route13_v2.py [out.png]
"""
import os, sys, json, struct
import numpy as np
from PIL import Image
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__)); ART = os.path.join(HERE, '..')
REPO = os.path.abspath(os.path.join(ART, '..', '..')); C = os.path.join(REPO, 'codebase')
for p in (os.path.join(ART, 'mirroh'), ART, HERE, os.path.join(REPO, 'tools', 'monomyth')): sys.path.insert(0, p)
import mirroh_mock as mm
W, H = 40, 124
mm.W, mm.H = W, H
import mirroh_v3 as v3
from mirroh_v3 import rnd, vnoise, _seg_dist, thick, snow_on, cobbles
import route13_mock as r1                                   # (the waystone, the grass test, lane)
import romlib as RL, render as RR

MB_NORMAL, MB_TALL_GRASS, MB_ICE = 0x00, 0x02, 0x20
ef = lambda m: mm.full('ef', m)

class Canvas:
    """The map: pixels, collision, behaviour, a tag per cell; ground() so Mirroh's snow_on and cobbles work on it."""
    def __init__(self):
        self.img = np.zeros((H * 16, W * 16, 3), np.uint8); self.solid = np.zeros((H, W), bool)
        self.beh = np.zeros((H, W), np.uint8); self.tag = np.full((H, W), 'snow', object)
        for y in range(H):
            for x in range(W): self.put(x, y, ef(0xee if rnd('r13v2', x, y) < 0.035 else 0xed), 'snow')
    def put(self, x, y, img, tag, solid=False, beh=MB_NORMAL):
        if 0 <= x < W and 0 <= y < H:
            self.img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = img; self.tag[y, x] = tag
            self.solid[y, x] = solid; self.beh[y, x] = beh
    def ground(self, x, y, img, tag):                      # (Mirroh's helpers: ice stays walkable as set after)
        self.put(x, y, img, tag, solid=False)
    def free(self, x, y, w, h, tags=('snow',)):
        return all(0 <= xx < W and 0 <= yy < H and self.tag[yy, xx] in tags for yy in range(y, y + h) for xx in range(x, x + w))
    def ids(self, x0, y0, rows, tag, solid=True, beh=MB_NORMAL):
        for dy, r in enumerate(rows):
            for dx, m in enumerate(r):
                if m is not None: self.put(x0 + dx, y0 + dy, ef(m), tag, solid, beh)
    def overlay(self, rgb, mask, px, py, tag, solid=True):
        h, w = mask.shape
        reg = self.img[py:py + h, px:px + w]; reg[mask] = rgb[mask]
        for cy in range(py // 16, (py + h - 1) // 16 + 1):
            for cx in range(px // 16, (px + w - 1) // 16 + 1):
                if mask[max(0, cy * 16 - py):cy * 16 - py + 16, max(0, cx * 16 - px):cx * 16 - px + 16].any():
                    self.tag[cy, cx] = tag; self.solid[cy, cx] = solid or self.solid[cy, cx]

# ------------------------------------------------------------------ pieces
BIG_PINE = [[0xe9, 0xea], [0xf1, 0xf2], [0xf9, 0xfa]]; SMALL_PINE = [[0x109], [0x111]]
BOULDER = [[0xf5, 0xf7], [0x105, 0x107]]
ARCH = [[0x10d, 0x106, 0x10e], [0xff, 0xed, 0xfd], [0x115, 0xf6, 0x116]]      # (Route 23: its lower middle open)
def pine(K, x, y, big):
    w, h = (2, 3) if big else (1, 2)
    if K.free(x, y, w, h): K.ids(x, y, BIG_PINE if big else SMALL_PINE, 'tree'); return True
    return False
def rock(K, x, y):
    if K.free(x, y, 1, 1): K.ids(x, y, [[0xe8]], 'rock'); return True
def boulder(K, x, y):
    if K.free(x, y, 2, 2): K.ids(x, y, BOULDER, 'rock'); return True
def arch(K, x, y):
    if K.free(x, y, 3, 3):
        K.ids(x, y, ARCH, 'rock'); K.solid[y + 2, x + 1] = False; return True
def grass(K, cells):
    for (x, y) in cells:
        if K.tag[y, x] == 'snow': K.put(x, y, ef(0xf0), 'grass', beh=MB_TALL_GRASS)
def blob(cx, cy, rx, ry, seed, j=0.35):
    return {(x, y) for y in range(int(cy - ry - 2), int(cy + ry + 3)) for x in range(int(cx - rx - 2), int(cx + rx + 3))
            if 0 <= x < W and 0 <= y < H and ((x - cx) / (rx + 0.5)) ** 2 + ((y - cy) / (ry + 0.5)) ** 2 < 1 + j * (vnoise(x, y, 1.7, seed) - 0.5)}
def forest(K, cells, seed):
    """Dense pinewood over the given cells: big pines staggered, small pines and rocks in the gaps (every cell solid)."""
    cells = set(cells)
    for (x, y) in sorted(cells, key=lambda c: (c[1], c[0])):
        if (x + y * 3) % 2 == 0 and all((x + i, y + j) in cells for i in (0, 1) for j in (0, 1, 2)): pine(K, x, y, True)
    for (x, y) in sorted(cells, key=lambda c: (c[1], c[0])):
        if K.tag[y, x] != 'snow': continue
        if (x, y + 1) in cells and pine(K, x, y, False): continue
        K.put(x, y, ef(0xe8 if rnd(seed, x, y) < 0.5 else 0xed), 'woodfill', solid=True)
def lane(pts, half, seed, wob=0.5):
    return {(x, y) for y in range(H) for x in range(W)
            if min(_seg_dist((x, y), a, b) for a, b in zip(pts, pts[1:])) < half + wob * (vnoise(x, y, 3.0, seed) - 0.5)}

# ------------------------------------------------------------------ MonoMyth Route 22, lifted
_SRC = {}
def route22():
    if 'r22' not in _SRC:
        L = RL.layout(RL.u32(0x869874)); w, h = L['w'], L['h']
        cells = np.array(RR.map_cells(L), np.uint16).reshape(h, w); ids = cells & 0x3FF
        pa, sa = L['primary']['attr'], L['secondary']['attr']
        beh = lambda m: (struct.unpack_from('<H', RL.ROM, RL.off(pa) + 2 * m)[0] if m < 512 else struct.unpack_from('<H', RL.ROM, RL.off(sa) + 2 * (m - 512))[0]) & 0xFF
        ts = RR.TS(L); img = np.zeros((h * 16, w * 16, 3), np.uint8)
        for y in range(h):
            for x in range(w): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = ts.meta(int(ids[y, x]))
        B = np.vectorize(lambda m: beh(int(m)))(ids)
        _SRC['r22'] = (img, ((cells >> 10) & 3) != 0, ids, B)
    return _SRC['r22']
YELLOW = 0xef                                               # (its little yellow figures: snow there instead)
def paste_r22(K, sy0, sy1, dy0, dx=1):
    img, solid, ids, B = route22()
    for sy in range(sy0, sy1 + 1):
        for sx in range(img.shape[1] // 16):
            x, y = sx + dx, dy0 + sy - sy0
            if not (0 <= x < W): continue
            t = img[sy * 16:sy * 16 + 16, sx * 16:sx * 16 + 16]; b = int(B[sy, sx])
            if ids[sy, sx] == YELLOW: K.put(x, y, ef(0xed), 'snow'); continue
            beh = MB_TALL_GRASS if b == 0x5a else MB_NORMAL if b in (0x5b, 0) else b
            K.put(x, y, t, 'r22grass' if b == 0x5a else 'r22', bool(solid[sy, sx]), beh)

# ------------------------------------------------------------------ the composition (rows from the top)
FOOT, FOREST, TERR1, MEADOW, DEFILE, FORK = (121, 123), (99, 120), (81, 98), (66, 80), (34, 65), (24, 33)

def compose():
    K = Canvas(); notes = []
    # --- the foot: Mirroh's north wall (its top, from the built Upper Mirroh), the road's passage at x 19-20
    sys.path.insert(0, ART); import render_built as RB
    RB.main('MirrohUpper', '/tmp/_r13_upper.png'); U = np.asarray(Image.open('/tmp/_r13_upper.png').convert('RGB'))
    uc = lambda x, y: U[y * 16:y * 16 + 16, x * 16:x * 16 + 16].copy()
    for x in range(W):
        if x in (19, 20): continue
        K.put(x, 122, uc(22 + x % 2, 0), 'wall', True); K.put(x, 123, uc(22 + x % 2, 1), 'wall', True)
    for x in (19, 20): K.put(x, 123, uc(x - 6, 9), 'passage', False)          # (the gatehouse's dark doorway)

    # --- the lifted climbs
    paste_r22(K, 57, 74, TERR1[0])                    # stair (its 72-74), ice-grass meadow, stair (57-60)
    paste_r22(K, 15, 46, DEFILE[0])                   # the defile (its 25-46) and the central stairway (15-24)
    for y in list(range(*[TERR1[0], TERR1[1] + 1])) + list(range(DEFILE[0], DEFILE[1] + 1)):
        for x in (0, W - 1): K.put(x, y, ef(0xe8 if (x + y) % 2 else 0xed), 'woodfill', True)

    # --- the forest out of Mirroh: the road through a clearing up to terraces I's stair (its x 11-12 -> 12-13 here)
    road_lo = lane(((19.5, 122), (19.5, 116), (17.5, 111), (15, 106), (13, 102), (12.5, 99)), 1.3, 'r1', 0.4)
    clearing = blob(17, 110, 5.5, 4.5, 'clear') | road_lo
    glade = blob(5.5, 104, 2.6, 2.2, 'glade') | lane(((6, 105), (10.5, 107), (12.5, 108)), 0.75, 'gap', 0.15)
    open_f = {(x, y) for (x, y) in clearing | glade if FOREST[0] <= y <= FOREST[1]}
    forest(K, {(x, y) for y in range(FOREST[0], FOREST[1] + 1) for x in range(W)} - open_f, 'fw')
    grass(K, {c for c in blob(19.5, 109, 2.6, 2.0, 'cg') if c not in road_lo})
    for (x, y) in ((21, 113), (14, 113)): rock(K, x, y)

    # --- the high meadow: the tarn, ice grass, boulders, rock arches, a frozen puddle; pine flanks
    mo = {(x, y) for y in range(MEADOW[0], MEADOW[1] + 1) for x in range(W)}
    flank = {(x, y) for (x, y) in mo if x < 3 + int(2 * vnoise(x, y, 4, 'mf')) or x > 36 - int(2 * vnoise(x, y, 4, 'mg'))}
    forest(K, flank, 'mf')
    pond = thick({c for c in blob(10, 72, 4.2, 2.6, 'tarn', 0.3) if c not in flank})
    yard = {c for c in blob(10, 72, 6.2, 4.4, 'tyard', 0.1) if c not in flank and MEADOW[0] <= c[1] <= MEADOW[1]}
    icef = lambda x, y: mm.recolour(mm.full('gg', 0x34b), mm.GG_ICE)
    snow_on(K, thick(yard - pond), icef, yard, 'snow')
    for (x, y) in pond: K.tag[y, x] = 'ice'; K.beh[y, x] = MB_ICE
    grass(K, {c for c in blob(27, 70, 3.4, 2.4, 'mg1') if c not in flank})
    grass(K, {c for c in blob(20, 77, 2.6, 1.6, 'mg2') if c not in flank})
    for (x, y) in ((22, 67), (31, 75)): boulder(K, x, y)
    for (x, y) in ((16, 68), (29, 66)): arch(K, x, y)
    for (x, y) in ((18, 73), (33, 72), (6, 78)): pine(K, x, y, False)
    for (x, y) in ((24, 74), (13, 79)): rock(K, x, y)

    # --- the defile's frozen stream (R22's open row 40 -> 59 here), the log deck over it on the way up
    sy = DEFILE[0] + 40 - 15
    for y in (sy, sy + 1):
        for x in range(W):
            if not K.solid[y, x] and K.tag[y, x] in ('r22', 'r22grass', 'snow'):
                t = mm.recolour(mm.full('gg', 0x34b), mm.GG_ICE).astype(int); t = np.clip(t * [0.78, 0.86, 1.0], 0, 255).astype(np.uint8)
                K.put(x, y, t, 'stream', True)
    for y in (sy, sy + 1):                                            # (the deck: two rows of logs, x 19-21)
        K.ids(19, y, [[0x350, 0x351, 0x352]], 'bridge', solid=False)

    # --- the fork: a snowy plateau above the central stair (R22's x 18-19 -> 19-20 here); waystone and signpost
    plateau = blob(20, 28.5, 7.5, 4.2, 'plat', 0.2)
    # (user 2026-11-22: the paved road starts at the top of the stairs, so the fork shows the difference: the Templars'
    # cobbles carry on to their HQ, the wilds of Mt. Mirroh are an unpaved trail breaking off them)
    road_ne = lane(((19.5, 33.4), (19.8, 31), (21.5, 29), (24, 27), (27.5, 23), (30, 17), (31.5, 11), (32.5, 5), (33, -1)), 1.25, 'ne', 0.3)
    trail = lane(((18.5, 30.5), (15, 27), (11, 22), (9, 16), (8.5, 8), (8.5, -1)), 1.0, 'nw', 0.3)
    spur = {(x, y) for y in range(0, 26) for x in range(W) if 13 + y * 0.28 <= x <= 27 - y * 0.30 and (x, y) not in plateau}
    upper = {(x, y) for y in range(0, FORK[1] + 1) for x in range(W)}
    openu = plateau | road_ne | trail | blob(31, 6, 2.5, 2.0, 'g6') | blob(6, 18, 2.0, 2.5, 'g5') \
        | {(x, y) for y in range(0, 24) for x in range(4, 13) if y % 4 != 1}                 # (the steep terraces' ledges)
    openu = {c for c in openu if c not in spur} | {c for c in road_ne | trail}
    forest(K, upper - openu - {(x, y) for y in range(0, 24) for x in range(4, 13)}, 'uf')
    # steep terraces up to Mt. Mirroh: a rock wall every fourth row, each running unbroken from the trees on the left
    # to the trees on the right (user 2026-11-22: stubs and gaps by the stairs looked wrong; no way round either),
    # the stone stair (x 8-9) its only way through
    for y in range(1, 24, 4):
        x0 = 4
        while x0 > 0 and not K.solid[y, x0 - 1]: x0 -= 1
        x1 = 12
        while x1 < W - 1 and not K.solid[y, x1 + 1]: x1 += 1
        for x in range(x0, x1 + 1):
            if x in (8, 9): continue
            K.put(x, y, ef(0x105 if x == x0 else 0x107 if x == x1 else 0x106), 'cliff', True)
        K.ids(8, y, [[0x47, 0xe1]], 'stairs', solid=False, beh=0x4F)
    cob = thick({c for c in road_lo | road_ne if K.tag[c[1], c[0]] in ('snow',)})
    cobbles(K, cob)
    for (x, y) in cob: K.solid[y, x] = False; K.beh[y, x] = MB_NORMAL
    wi, wm = r1.waystone(); K.overlay(wi, wm, 18 * 16, 26 * 16, 'waystone')
    sgn = mm.cut('c31', 23, 20, 1, 1)[0][0]
    if sgn: K.overlay(sgn[0], sgn[1], 23 * 16, 30 * 16, 'sign')
    grass(K, blob(31, 6, 2.5, 2.0, 'g6') - road_ne); grass(K, blob(6, 18, 2.0, 2.5, 'g5') - trail)
    # the wild trail's look (user 2026-11-22: show the difference at the fork): Elderflower's trodden icy track in
    # staggered patches from the plateau up to the first stone stair, a few rocks along its edges
    seg = set()
    for (x, y0, y1) in ((16, 27, 30), (13, 24, 26), (8, 18, 20), (8, 14, 16), (8, 10, 12)):   # (between the walls, in line with the stairs)
        seg |= {(xx, y) for y in range(y0, y1 + 1) for xx in (x, x + 1)}
    seg = {c for c in seg if K.tag[c[1], c[0]] == 'snow'}
    r1.icy_track(K, seg)
    for (x, y) in ((15, 25), (18, 29), (11, 25), (11, 19)): rock(K, x, y)
    return K, notes

def reach(K, start):
    seen = {start}; q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (x + dx, y + dy)
            if 0 <= n[0] < W and 0 <= n[1] < H and n not in seen and not K.solid[n[1], n[0]]: seen.add(n); q.append(n)
    return seen

def main(out):
    K, notes = compose()
    R = reach(K, (19, 123))
    for name, c in (('fork', (20, 29)), ('Mt. Mirroh exit', (8, 0)), ('Templar HQ exit', (33, 0)), ('glade', (5, 104)),
                    ('tarn shore', (10, 76)), ('top of terraces I', (12, 81))):
        print('%-18s %s %s' % (name, c, 'REACHED' if c in R else 'not reached'))
    Image.fromarray(K.img).save(out)
    Image.fromarray(K.img).resize((W * 32, H * 32), Image.NEAREST).save(out.replace('.png', '_2x.png'))
    np.savez_compressed(out.replace('.png', '.npz'), solid=K.solid, beh=K.beh)
    return K, R

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/route13_v2.png')
