"""Pelluca Valley's south waterfront, art mock v1: option A (Watercress' harbour) with bits of B and C (user 2026-11-24:
"Primarily A with bits of B and C where necessary").

From A (MonoMyth's Watercress Port, 0x869C10, in its own metatiles; credit the MonoMyth team): one quay of pale dressed
stone, its white kerb and its drop into the water, from the Tavern to the east woods; three stone piers at a rhythm:
the great pier on the main stair's axis (7 wide, Watercress' left pier with its lamp posts and bunting across the
root) where the Pale Veluza berths, a short pier for the rowboats, a long east pier for the second ship; its lamp posts,
crates and flower boxes; rocks round the basin.
From B (Crown's harbour market; credit Blah and the Crown team): the market's striped stalls along the back of the quay.
From C (Lazarus' cove, Odyssey's shores): the basin inside the breakwater pale and shallow, deep water beyond; the
breakwater a close reef arm from the east woods.
The beach: MonoMyth's Cascade Boardwalk sand with its clean edge on the water (stepped, no grey surf band), palms in
groups (Pelluca's), the fisherman's jetty in Cascade's boardwalk planks; a short stair from the quay down onto the sand.
Kept: everything above row 36, the Seaside Tavern, the woods either side, the lab tower (moved up four rows to the
cliff foot, its door (47, 40)), the INN board. Objects drawn: the two ships, the rowboats, the shrine.
v2 (user 2026-11-24 on v1): (1) Watercress' pastel bunting out: timber poles with pennants in Pelluca's roof plum and
cream across the great pier's root; its pastel lantern posts out too: Pelluca's own iron harbour lamps along the kerb;
(2) the market stalls become cargo sheds: Crown's awnings recoloured to weathered sailcloth (one in Pelluca's plum),
cargo under and before them (Crown's barrels and crates, sacks, rope, nets); dockhands, sailors, merchants, a captain
and visitors off the ships placed (stage 2 makes them people); (3) the stair down to the beach three wide (Pelluca's
own main-stair pieces); (4) the beach jetty removed; (5) three different ships: the Pale Veluza is Crown's wooden
ship (its one large medieval vessel) bleached pale, with an ivory sail; a merchantman, the same hull mirrored in
dark tarred wood under a dyed madder sail, at the east pier; a fishing sloop (Lazarus' small sailboat in wood and
canvas) at the short pier; Crown's wooden rowboats in place of the motorboats.
Usage: python3 waterfront_mock.py OUTDIR [pelluca_now.png]"""
import os, sys, math, random
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
C = os.path.join(ROOT, 'codebase')
sys.path.insert(0, os.path.join(HERE, '..', 'mt_mirroh'))
import mono_pieces as MP
S = 16
W, H = 80, 60
WC, CB = 0x869C10, 0x869B84
blk = lambda x, y: (slice(y * S, y * S + S), slice(x * S, x * S + S))
h = lambda s: int(s, 16)

def wc(m):
    img, g, ts = MP.grid(WC); return ts.meta(h(m) if isinstance(m, str) else m).copy()
def cb(m):
    img, g, ts = MP.grid(CB); return ts.meta(h(m) if isinstance(m, str) else m).copy()

# ------------------------------------------------------------------------------------------------------- the plan
BEACH_X = (8, 34)
WY = dict(zip(range(8, 35), [45, 45, 46, 46, 46, 47, 47, 48, 48, 48, 48, 48, 47, 47, 47, 46, 46, 46, 46, 46, 46, 45, 45, 45, 44, 44, 44]))
QUAY = (32, 36, 71, 40)                      # paving rows 36-40; kerb row 41, its face row 42
PIERS = [(35, 7, 53, False), (50, 5, 47, False), (64, 4, 52, False)]   # (left x, width, kerb row, bunting at its root)
LAB = (44, 40, 49, 44, -4)                   # the lab's cells in the old map, moved up 4
TAVERN = (25, 36, 31, 43)
STAIRS_DOWN = [(x, y) for x in (32, 33, 34) for y in (41, 42, 43)]   # quay -> beach, three wide
STALLS = [(55, 'canvas'), (59, 'plum'), (63, 'canvas'), (68, 'canvas')]  # cargo sheds: left cell x, rows 36-38
FLOWERS = [(35, 36, '2bf'), (36, 36, '2c7'), (40, 36, '2bf'), (41, 36, '2c7')]
CRATES = [(33, 36, '2c9'), (34, 36, '2cc'), (33, 37, '2cc'), (36, 52, '2cc'), (40, 52, '2c9'), (51, 40, '2cc'),
          (66, 51, '2c9'), (70, 36, '2cc'), (70, 37, '2c9'), (58, 38, '2cc'), (66, 38, '2c9'), (54, 36, '2c9')]
LAMPS = []
IRON_LAMPS = [(43, 40), (58, 40), (62, 40), (69, 40)]     # Pelluca's harbour lamp (base cell; its top above)
ROCKS = [(72, 46), (71, 48), (70, 50), (69, 52), (67, 54), (65, 55), (63, 56), (61, 56), (59, 57),   # the east arm
         (42, 56), (44, 58),                                                                     # west of the mouth
         (8, 49), (10, 51), (12, 53), (4, 47)]                                                   # off the beach's point
SHIPS = [('veluza', 42, 47), ('merchant', 56, 48), ('sloop', 55, 43), ('rowboat', 30, 47), ('rowboat', 68, 44)]   # (top-left cell)
SHRINE = (42, 39)
PALMS = [(9, 38), (11, 37), (10, 42), (16, 37), (18, 39), (14, 44), (21, 41), (23, 38)]

def basin(x, y):
    """inside the breakwater: east of the great pier, west of the east arm, north of the arm's curve"""
    if x < 42 or y < 43: return False
    arm = {72: 46, 71: 48, 70: 50, 69: 52, 68: 53, 67: 54, 66: 55, 65: 55, 64: 56, 63: 56, 62: 56, 61: 56, 60: 57, 59: 57}
    lim = arm.get(x, 57)
    return x <= 72 and y <= lim

# --------------------------------------------------------------------------------------------------- composition
def compose(town):
    img = np.array(town.convert('RGB')).copy()
    base = img.copy()
    land = np.zeros((H, W), bool)                          # (for the shallows)
    # 1. water everywhere below row 36 outside the kept woods
    for y in range(36, H):
        for x in range(W):
            if y <= 45 and (x < 8 or x >= 72): land[y, x] = True; continue
            img[blk(x, y)] = wc('e0')
    # 2. the beach (Cascade sand, its edge on the water)
    for x in range(BEACH_X[0], BEACH_X[1] + 1):
        for y in range(36, WY[x] + 1):
            if x >= 32 and y < 44: continue
            land[y, x] = True
            west = x - 1 >= BEACH_X[0] and WY[x - 1] >= y or x == BEACH_X[0]
            east = x + 1 <= BEACH_X[1] and WY[x + 1] >= y and not (x + 1 >= 32 and y < 44)
            if x == 31 and y < 44: east = True
            bottom = y == WY[x]
            if bottom and not west: t = cb('280')
            elif bottom and not east: t = cb('280')[:, ::-1]
            elif bottom: t = cb('281')
            elif not west: t = cb('278')
            elif not east: t = cb('278')[:, ::-1]
            else: t = cb('279')
            img[blk(x, y)] = t
    # 3. the quay, its kerb and face; the piers
    x0, y0, x1, y1 = QUAY
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            land[y, x] = True
            img[blk(x, y)] = wc('2df' if x == x1 else '2b7')
    pier_cols = {}
    for (px, w, kr, bunt) in PIERS:
        for i in range(w): pier_cols[px + i] = (px, w, kr, bunt, i)
    K = y1 + 1
    for x in range(35, x1 + 1):
        land[K, x] = True
        if x in pier_cols:
            px, w, kr, bunt, i = pier_cols[x]
            if bunt: k42 = ['2ff', '2e8', '2e1', '2e2', '2e9', '2e0', '2f7'][i]; k43 = ['2d5', '2d8', '2ea', '2eb', '2ec', '2d0', '2d3'][i]
            else:
                k42 = '2ff' if i == 0 else '2f7' if i == w - 1 else '2b7'
                k43 = '2d5' if i == 0 else '2d3' if i == w - 1 else '2d6' if i == 1 else '2d7' if i == w - 2 else '2b7'
            img[blk(x, K)] = wc(k42); img[blk(x, K + 1)] = wc(k43); land[K + 1, x] = True
            for y in range(K + 2, kr):
                img[blk(x, y)] = wc('2dd' if i == 0 else '2db' if i == w - 1 else '2e6' if i == 1 else '2df' if i == w - 2 else '2b7')
                land[y, x] = True
            img[blk(x, kr)] = wc('2dd' if i == 0 else '2db' if i == w - 1 else '2de' if i == 1 else '2ee' if i == w - 2 else '2dc')
            img[blk(x, kr + 1)] = wc('2e5' if i == 0 else '2e3' if i == w - 1 else '2d4'); land[kr, x] = True
        else:
            img[blk(x, K)] = wc('2de' if x == x0 + 1 else '2ee' if x == x1 else '2dc')
            img[blk(x, K + 1)] = wc('2e5' if x == x0 + 1 else '2e3' if x == x1 else '2d4')
    # the stair down onto the beach (Pelluca's own cliff stair, from the west stairs)
    for (x, y) in STAIRS_DOWN: img[blk(x, y)] = base[blk(37 + (x - 32), 35)]; land[y, x] = True
    # 4. the shallows: inside the basin, and two cells out from any land (C, Odyssey)
    from scipy.ndimage import binary_dilation
    near = binary_dilation(land, iterations=2)
    pale = wc('6c')
    for y in range(36, H):
        for x in range(W):
            if land[y, x]: continue
            if basin(x, y) or near[y, x]:
                c = img[blk(x, y)]
                # recolour this cell's deep water to the pale water (where it is plain deep water)
                if (c == wc('e0')).all(): img[blk(x, y)] = pale
    # the faces and rims carry Watercress' pale water under them already
    # 5. rocks (Watercress' rock in the water, 2x2)
    for k, (x, y) in enumerate(ROCKS):
        ids = (('d2', 'd3', 'da', 'db') if k % 2 == 0 else ('d4', 'd5', 'dc', 'dd'))
        for (dx, dy), m in zip(((0, 0), (1, 0), (0, 1), (1, 1)), ids):
            if 0 <= x + dx < W and 0 <= y + dy < H: img[blk(x + dx, y + dy)] = wc(m)
    # 7. kept pieces: the tavern, the INN board, the woods' edge cells
    sandref = base[blk(15, 41)]                       # (Pelluca's plain sand: cut the kept pieces off it)
    def keep(x, y, dx=0, dy=0):
        c = base[blk(x, y)]; m = (c != sandref).any(-1)
        t = img[blk(x + dx, y + dy)]; t[m] = c[m]; img[blk(x + dx, y + dy)] = t
    tx0, ty0, tx1, ty1 = TAVERN
    for y in range(ty0, ty1 + 1):
        for x in range(tx0, tx1 + 1): keep(x, y)
    for (x, y) in ((23, 43), (24, 43), (23, 44), (24, 44)): keep(x, y)               # (the INN board: caps, board)
    # 8. the lab, moved up: its own pixels (not the old quay stone under it)
    lx0, ly0, lx1, ly1, dy = LAB
    ref = base[blk(40, 38)]
    for y in range(ly0, ly1 + 1):
        for x in range(lx0, lx1 + 1):
            c = base[blk(x, y)]; m = (c != ref).any(-1)
            t = img[blk(x, y + dy)]; t[m] = c[m]; img[blk(x, y + dy)] = t
    # 9. quay furniture
    for (x, y, m) in FLOWERS + CRATES + LAMPS:
        t = wc(m); cur = img[blk(x, y)]; pav = wc('2b7'); d = (t != pav).any(-1); cur[d] = t[d]; img[blk(x, y)] = cur
    for (x, col) in STALLS:
        a = np.array(Image.open(os.path.join(ROOT, 'assets/crown_reference/pieces/stall_%s.png' % ('red' if col == 'canvas' else 'blue'))).convert('RGBA'))
        rgb = a[..., :3].astype(int); m = a[..., 3] > 0
        stripe = m & (((rgb[..., 0] > rgb[..., 1] + 40)) | ((rgb[..., 2] > rgb[..., 0] + 30)))
        cream = m & (rgb.sum(-1) > 560) & ~stripe
        lum = rgb.mean(-1)
        if col == 'plum': sc = [(168, 128, 176), (144, 104, 152), (120, 88, 128)]
        else: sc = [(156, 128, 96), (136, 110, 80), (112, 88, 64)]
        oat = [(222, 210, 178), (204, 190, 156), (184, 170, 138)]
        out = a[..., :3].copy()
        for msk, ramp in ((stripe, sc), (cream, oat)):
            if msk.any():
                lo, hi = lum[msk].min(), lum[msk].max() + 1
                k = ((hi - lum) / (hi - lo) * len(ramp)).clip(0, len(ramp) - 1).astype(int)
                for i, c in enumerate(ramp): out[msk & (k == i)] = c
        Y0, X0 = 36 * S, x * S; sub = img[Y0:Y0 + a.shape[0], X0:X0 + a.shape[1]]; sub[m] = out[m]
    # the harbour's own iron lamps (Pelluca's, cut off its old cobble)
    for (x, y) in IRON_LAMPS:
        for dy in (-1, 0):
            c = base[blk(55, 39 + dy)]; ref = base[blk(53, 39 + dy)]; mk = (c != ref).any(-1)
            t = img[blk(x, y + dy)]; t[mk] = c[mk]; img[blk(x, y + dy)] = t
    # pennants across the great pier's root: two timber poles, a rope, pennants in Pelluca's plum and cream
    plum = [(144, 104, 152), (120, 88, 128)]; cream = [(236, 226, 196), (214, 200, 170)]
    for X in (36 * S + 7, 40 * S + 7):
        img[43 * S - 18:44 * S + 6, X:X + 2] = (104, 72, 48); img[43 * S - 18:44 * S + 6, X] = (72, 50, 36)
        img[43 * S - 20:43 * S - 17, X - 1:X + 3] = (64, 72, 104); img[44 * S + 6:44 * S + 8, X - 1:X + 3] = (56, 56, 72)
    xa, xb = 36 * S + 9, 40 * S + 7; ytop = 43 * S - 16
    for X in range(xa, xb):
        t = (X - xa) / (xb - xa); Y = int(ytop + 6 * 4 * t * (1 - t)); img[Y, X] = (88, 70, 56)
    k = 0
    for X in range(xa + 3, xb - 6, 9):
        t = (X - xa) / (xb - xa); Y = int(ytop + 6 * 4 * t * (1 - t)) + 1
        c = (plum if k % 2 == 0 else cream)
        for r in range(7):
            w_ = max(1, 6 - r)
            img[Y + r, X:X + w_] = c[0]; img[Y + r, X] = c[1]
        img[Y + 7, X] = (72, 56, 80); k += 1
    # cargo: Crown's barrels and crates, sacks, rope coils, nets: under and before the sheds, at the pier roots
    def piece(name):
        q = np.array(Image.open(os.path.join(ROOT, 'assets/crown_reference/pieces/%s.png' % name)).convert('RGBA')); return q[..., :3], q[..., 3] > 0
    def put(rgb, m, X, Y):
        sub = img[Y:Y + m.shape[0], X:X + m.shape[1]]; sub[m] = rgb[m]
    def sack(X, Y):
        yy, xx = np.mgrid[0:12, 0:10]; m = ((xx - 4.5) / 4.6) ** 2 + ((yy - 7) / 5) ** 2 <= 1
        m |= (abs(xx - 4.5) <= 1.5) & (yy < 4) & (yy >= 1)
        rgb = np.zeros((12, 10, 3), np.uint8); rgb[m] = (200, 180, 136); rgb[m & (xx > 6)] = (168, 148, 108)
        rgb[(yy == 3) & m] = (120, 96, 64); e = m & ~(np.roll(m, 1, 0) & np.roll(m, -1, 0) & np.roll(m, 1, 1) & np.roll(m, -1, 1)); rgb[e] = (96, 76, 52)
        put(rgb, m, X, Y)
    def rope(X, Y):
        yy, xx = np.mgrid[0:8, 0:12]; d = np.sqrt(((xx - 5.5) / 5.5) ** 2 + ((yy - 3.5) / 3.5) ** 2)
        m = d <= 1; rgb = np.zeros((8, 12, 3), np.uint8); rgb[m] = (176, 140, 92)
        rgb[m & ((np.round(d * 4) % 2) == 0)] = (128, 98, 60); rgb[d < 0.25] = (96, 72, 44); put(rgb, m, X, Y)
    def net(X, Y):
        m = np.zeros((10, 16), bool); m[1:9, 0:16] = True
        rgb = np.zeros((10, 16, 3), np.uint8); rgb[m] = (120, 132, 120)
        for i in range(0, 16, 3): rgb[1:9, i] = (84, 92, 84)
        for j in range(1, 9, 3): rgb[j, :] = (84, 92, 84)
        rgb[4:6, 6:9] = (200, 120, 70); put(rgb, m, X, Y)
    br, bm = piece('barrel'); bsr, bsm = piece('barrel_stack'); cr, cm = piece('crate_small')
    for (x, y) in [(56, 38), (60, 38), (64, 38), (69, 38), (66, 39), (53, 37), (71, 39), (35, 38), (41, 53)]:
        put(br, bm, x * S, y * S)
    for (x, y) in [(57, 37), (61, 37), (65, 37), (70, 37), (33, 38)]:
        put(bsr, bsm, x * S, y * S)
    for (x, y) in [(55, 39), (59, 39), (63, 39), (68, 39), (52, 40), (37, 52)]:
        put(cr, cm, x * S, y * S + 2); put(cr, cm, x * S + 6, y * S - 4)
    for (X, Y) in [(57 * S + 4, 39 * S + 3), (61 * S + 2, 39 * S + 4), (60 * S + 10, 39 * S + 2), (65 * S + 6, 39 * S + 3), (70 * S + 2, 39 * S + 4)]:
        sack(X, Y)
    for (X, Y) in [(50 * S + 2, 41 * S + 6), (64 * S + 3, 41 * S + 7), (39 * S + 2, 51 * S + 6), (67 * S + 2, 51 * S + 6)]:
        rope(X, Y)
    for (X, Y) in [(53 * S, 46 * S + 2), (65 * S, 50 * S + 4)]:
        net(X, Y)
    # 10. palms (Pelluca's, two cells tall; cut off the old sand)
    palm = base[39 * S:42 * S, 8 * S:10 * S]       # (the palm at (8, 40): two cells wide, its fronds and trunk)
    sand = base[blk(15, 41)]
    pa = np.array([[(palm[y, x] != sand[y % 16, x % 16]).any() for x in range(palm.shape[1])] for y in range(palm.shape[0])])
    rows = np.nonzero(pa.any(1))[0]; palm, pa = palm[rows[0]:rows[-1] + 1], pa[rows[0]:rows[-1] + 1]
    for (x, y) in PALMS:
        Y0 = (y + 1) * S - palm.shape[0]; sub = img[Y0:Y0 + palm.shape[0], x * S:x * S + 32]; sub[pa] = palm[pa]
    # beach things (MonoMyth's Route 24, 0x8698AC: tufts, driftwood, twigs, a boulder), cut off its sand
    img24, g24, ts24 = MP.grid(0x8698AC); s24 = ts24.meta(0x204)
    def r24(m, x, y):
        t = ts24.meta(m); d = (t != s24).any(-1); cur = img[blk(x, y)]; cur[d] = t[d]; img[blk(x, y)] = cur
    for (m, x, y) in [(0x20b, 13, 40), (0x202, 20, 44), (0x207, 9, 44), (0x208, 26, 45), (0x214, 15, 46), (0x215, 16, 46),
                      (0x212, 22, 46), (0x213, 11, 45), (0x20b, 29, 44), (0x202, 17, 42)]:
        r24(m, x, y)
    for (m, dx, dy) in ((0x20c, 0, 0), (0x20d, 1, 0), (0x211, 0, 1), (0x210, 1, 1)):
        pass
    # 11. the ships (Crown's ship and rowboat, Lazarus' sloop; recoloured), the shrine, people
    def ramp_map(rgb, m, ramp):
        out = rgb.copy(); lum = rgb.astype(int).mean(-1)
        if not m.any(): return out
        lo, hi = np.percentile(lum[m], 2), np.percentile(lum[m], 98) + 1
        k = ((hi - lum) / (hi - lo) * len(ramp)).clip(0, len(ramp) - 1).astype(int)
        for i, c in enumerate(ramp): out[m & (k == i)] = c
        return out
    def ship(kind):
        if kind in ('veluza', 'merchant'):
            q = np.array(Image.open(os.path.join(ROOT, 'assets/crown_reference/pieces/ship_galleon.png')).convert('RGBA'))
        elif kind == 'rowboat':
            q = np.array(Image.open(os.path.join(ROOT, 'assets/crown_reference/pieces/rowboat.png')).convert('RGBA'))
        else:
            q = np.array(Image.open(os.path.join(ROOT, 'assets/lazarus_reference/sailboat.png')).convert('RGBA'))
        rgb, m = q[..., :3].copy(), q[..., 3] > 0
        r_, g_, b_ = [rgb[..., i].astype(int) for i in range(3)]
        yy = np.arange(m.shape[0])[:, None] * np.ones((1, m.shape[1]), int)
        water = m & (b_ > r_ + 25) & (yy >= m.shape[0] - 8)
        if kind == 'veluza':
            sail = m & (b_ > r_ + 10) & ~water
            rgb = ramp_map(rgb, m & ~sail & ~water, [(244, 240, 230), (222, 216, 204), (196, 190, 180), (164, 160, 156), (124, 122, 126), (80, 78, 90)])
            rgb = ramp_map(rgb, sail, [(252, 250, 242), (232, 228, 214), (206, 204, 196), (170, 176, 186)])
        elif kind == 'merchant':
            sail = m & (b_ > r_ + 10) & ~water
            rgb = ramp_map(rgb, m & ~sail & ~water, [(150, 110, 70), (120, 84, 54), (96, 66, 44), (72, 48, 34), (50, 34, 26)])
            rgb = ramp_map(rgb, sail, [(196, 96, 72), (164, 72, 56), (130, 54, 46), (96, 40, 38)])
            rgb, m = rgb[:, ::-1].copy(), m[:, ::-1].copy()
        elif kind == 'sloop':
            sail = m & (g_ > 190) & (r_ > 150)
            hull = m & ~sail
            rgb = ramp_map(rgb, hull, [(176, 132, 84), (150, 108, 66), (120, 84, 52), (88, 60, 40), (56, 40, 30)])
            rgb = ramp_map(rgb, sail, [(234, 222, 190), (212, 198, 162), (186, 170, 134)])
            rows = np.nonzero(m.any(1))[0]; rgb, m = rgb[rows[0]:], m[rows[0]:]
        return rgb, m
    for kind, x, y in SHIPS:
        rgb, m = ship(kind)
        if kind == 'sloop': Y0 = (y + 4) * S - m.shape[0]
        else: Y0 = y * S
        sub = img[Y0:Y0 + m.shape[0], x * S:x * S + m.shape[1]]; sub[m] = rgb[m]
    PEOPLE = [('sailor', 40, 49, 'L'), ('sailor', 36, 47, 'R'), ('gentleman', 38, 45, 'U'), ('woman_2', 39, 44, 'U'),
              ('hiker', 52, 39, 'R'), ('fat_man', 58, 40, 'D'), ('man_2', 62, 39, 'L'), ('expert_m', 66, 46, 'L'),
              ('sailor', 65, 49, 'L'), ('fisherman', 36, 52, 'L'), ('woman_4', 52, 37, 'D'), ('templar', 33, 39, 'D'),
              ('man_4', 45, 41, 'R'), ('old_man', 70, 40, 'L')]
    for (gfx, x, y, f) in [('dr_shrine', *SHRINE, 'D')] + PEOPLE:
        path = os.path.join(C, 'graphics/object_events/pics/%s/%s.png' % ('misc' if gfx == 'dr_shrine' else 'people', gfx))
        sp = Image.open(path); pal = sp.getpalette(); a = np.array(sp)
        if gfx != 'dr_shrine':
            fi = {'D': 0, 'U': 1, 'L': 2, 'R': 2}[f]; a = a[:32, fi * 16:fi * 16 + 16]
            if f == 'R': a = a[:, ::-1]
        hh, ww = a.shape
        if gfx == 'dr_shrine' and hh > 32: a = a[:32]; hh = 32
        X0, Y0 = x * S + 8 - ww // 2, (y + 1) * S - hh
        for yy_ in range(hh):
            for xx_ in range(ww):
                if a[yy_, xx_] and 0 <= Y0 + yy_ < H * S and 0 <= X0 + xx_ < W * S:
                    img[Y0 + yy_, X0 + xx_] = pal[a[yy_, xx_] * 3:a[yy_, xx_] * 3 + 3]
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
    town = Image.open(sys.argv[2] if len(sys.argv) > 2 else '/home/claude/scratch/pelluca_now.png')
    img = compose(town)
    Image.fromarray(img).save(os.path.join(out, 'waterfront_mock_v2_full.png'))
    Image.fromarray(img[24 * S:, :]).save(os.path.join(out, 'waterfront_mock_v2.png'))
