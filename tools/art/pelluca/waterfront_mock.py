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
BEACH_X = (8, 32)
WY = dict(zip(range(8, 33), [45, 45, 46, 46, 46, 47, 47, 48, 48, 48, 48, 48, 47, 47, 47, 46, 46, 46, 46, 46, 46, 45, 45, 45, 44]))
QUAY = (32, 36, 71, 40)                      # paving rows 36-40; kerb row 41, its face row 42
PIERS = [(35, 7, 53, True), (50, 5, 47, False), (64, 4, 52, False)]   # (left x, width, kerb row, bunting at its root)
LAB = (44, 40, 49, 44, -4)                   # the lab's cells in the old map, moved up 4
TAVERN = (25, 36, 31, 43)
STAIRS_DOWN = [(32, 41), (32, 42), (32, 43)]  # quay -> beach
STALLS = [(55, 'red'), (59, 'blue'), (63, 'red'), (68, 'blue')]      # left cell x, rows 36-38
FLOWERS = [(35, 36, '2bf'), (36, 36, '2c7'), (40, 36, '2bf'), (41, 36, '2c7')]
CRATES = [(33, 36, '2c9'), (34, 36, '2cc'), (33, 37, '2cc'), (36, 52, '2cc'), (40, 52, '2c9'), (51, 40, '2cc'),
          (66, 51, '2c9'), (70, 36, '2cc'), (70, 37, '2c9'), (58, 38, '2cc'), (66, 38, '2c9'), (54, 36, '2c9')]
LAMPS = [(34, 40, '2cb'), (43, 40, '2c8'), (49, 40, '2cb'), (57, 40, '2c8'), (62, 40, '2cb'), (69, 40, '2c8')]
ROCKS = [(72, 46), (71, 48), (70, 50), (69, 52), (67, 54), (65, 55), (63, 56), (61, 56), (59, 57),   # the east arm
         (42, 56), (44, 58),                                                                     # west of the mouth
         (8, 49), (10, 51), (12, 53), (4, 47)]                                                   # off the beach's point
JETTY = (18, 49, 20, 53)
SHIPS = [('ss_tidal', 45, 53), ('ss_tidal', 60, 51), ('mr_brineys_boat', 48, 45), ('mr_brineys_boat', 56, 45),
         ('mr_brineys_boat', 22, 53)]
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
            if x == 32 and y < 44: continue
            land[y, x] = True
            west = x - 1 >= BEACH_X[0] and WY[x - 1] >= y or x == BEACH_X[0]
            east = x + 1 <= BEACH_X[1] and WY[x + 1] >= y and not (x + 1 == 32 and y < 44)
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
    for x in range(x0 + 1, x1 + 1):
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
    st = base[blk(24, 35)]
    for (x, y) in STAIRS_DOWN: img[blk(x, y)] = st; land[y, x] = True
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
    # 6. the jetty (Cascade's planks)
    jx0, jy0, jx1, jy1 = JETTY
    for y in range(jy0, jy1 + 1):
        for x in range(jx0, jx1 + 1):
            m = '262' if y < jy1 else '268'                    # (planks; posts only along its end)
            img[blk(x, y)] = cb(m)
        if y < jy1:                                             # (its sides: a dark plank edge)
            img[y * S:(y + 1) * S, jx0 * S] = (88, 60, 40); img[y * S:(y + 1) * S, (jx1 + 1) * S - 1] = (88, 60, 40)
    for x in range(jx0, jx1 + 1): img[blk(x, jy1 + 1)] = cb('27d')
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
        a = np.array(Image.open(os.path.join(ROOT, 'assets/crown_reference/pieces/stall_%s.png' % col)).convert('RGBA'))
        m = a[..., 3] > 0; Y0, X0 = 36 * S, x * S; sub = img[Y0:Y0 + a.shape[0], X0:X0 + a.shape[1]]
        sub[m] = a[..., :3][m]
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
    # 11. objects: the shrine, the ships and boats
    for gfx, x, y in [('dr_shrine', *SHRINE)] + SHIPS:
        sp = Image.open(os.path.join(C, 'graphics/object_events/pics/misc/%s.png' % gfx))
        pal = sp.getpalette(); a = np.array(sp)
        if gfx == 'mr_brineys_boat': a = a[:, :32]
        hh, ww = a.shape
        if gfx == 'dr_shrine' and hh > 32: a = a[:32]; hh = 32
        X0, Y0 = x * S + 8 - ww // 2, (y + 1) * S - hh
        for yy in range(hh):
            for xx in range(ww):
                if a[yy, xx] and 0 <= Y0 + yy < H * S and 0 <= X0 + xx < W * S:
                    img[Y0 + yy, X0 + xx] = pal[a[yy, xx] * 3:a[yy, xx] * 3 + 3]
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
    town = Image.open(sys.argv[2] if len(sys.argv) > 2 else '/home/claude/scratch/pelluca_now.png')
    img = compose(town)
    Image.fromarray(img).save(os.path.join(out, 'waterfront_mock_v1_full.png'))
    Image.fromarray(img[24 * S:, :]).save(os.path.join(out, 'waterfront_mock_v1.png'))
