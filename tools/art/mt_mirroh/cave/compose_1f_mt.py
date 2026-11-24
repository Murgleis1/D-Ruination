"""Mt. Mirroh 1F, second art pass (user 2026-11-23, on the first: "find a ground tileset that contrasts a little more
vibrantly ... with the dark stone of the cliffs"; "a lot of broken looking cliffs, stairs, mini rivers ... look at
other indoor caves and study them more"). Built the way Mt. Thunder's interiors are built (mt.py): dark slate wall
bands with snowy crests on pale smooth ice, stairs straight through the bands, water between bands with its own
shores, plank bridges with rails. Kept from the first pass (user-approved): the Glittering Grotto's crystals as
glassy ice, ice chunks, snow blown in at the way in, the rest stop's flagstones and candles, the cave mouth, the rubble.
Same plan (plan_1f.py), same cells (collision, levels, behaviours) as compose_1f.py.
Usage: python3 compose_1f_mt.py OUT.png"""
import os, sys, random
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gg, mt, plan_1f as P, compose_1f as C1
W = H = 60; S = 16; G = P.G
blk = lambda x, y: (slice(y * S, y * S + S), slice(x * S, x * S + S))

def cls(x, y):
    if not (0 <= x < W and 0 <= y < H): return 'W'
    p = (x, y)
    if p in C1.CRYSTAL_CELLS: return 'F'
    if p in (C1.EXIT_N, C1.EXIT_S): return 'W'
    ch = G[y, x]
    if ch in '#v|': return 'W'
    if ch in 'AB': return 'S'
    if ch == '~': return 'A'
    if ch in '=r':                                   # the bridge rows: what lies under them (cliff or river)
        R = [R for R in P.RAVINES if R['x0'] <= x < R['x0'] + 8][0]
        return 'W' if x - R['x0'] in (0, 1, 6, 7) else 'A'
    return 'F'

def compose(seed=7):
    rnd = random.Random(seed)
    V = mt.Vocab(); GV = gg.Vocab()
    img = np.zeros((H * S, W * S, 3), np.uint8)
    mid = np.zeros_like(img); mid_a = np.zeros((H * S, W * S), bool)
    top = np.zeros_like(img); top_a = np.zeros((H * S, W * S), bool)
    ids = {}
    for y in range(H):
        for x in range(W):
            key = cls(x, y) + ''.join(cls(x + dx, y + dy) for dx, dy in mt.N8)
            m = V.pick(key)
            if cls(x, y) == 'S': m = 0x21C if cls(x - 1, y) != 'S' else 0x21D
            ids[(x, y)] = m; img[blk(x, y)] = V.meta(m)
    floor = V.meta(mt.FLOOR)
    # the frozen rivers: plain water between the ravine's cliffs (the cliffs draw the banks), floes on it
    for y in range(H):
        for x in range(W):
            if cls(x, y) == 'A' and G[y, x] in '~=r': img[blk(x, y)] = V.meta(0x259)
    for y in range(H):                                   # thin plates of ice drifting on the river (flat, pale)
        for x in range(W):
            if G[y, x] == '~' and rnd.random() < 0.14 and all(abs(y - R['path']) > 3 for R in P.RAVINES):
                b = img[blk(x, y)]; cx, cy = rnd.randint(4, 11), rnd.randint(5, 11); rx, ry = rnd.randint(3, 5), 1.6
                yy, xx = np.mgrid[0:S, 0:S]; m = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1
                b[m] = (178, 206, 240); b[m & (yy <= cy - 1)] = (222, 238, 252)
    # the ravine cliffs: Mt. Thunder's tall cliff faces (0x20A where the drop is east of the bank, 0x208 where it
    # is west), solid from the bank to the water, as its own ravine under its bridge is drawn
    for R in P.RAVINES:
        for y in range(R['y0'], R['y1'] + 1):
            for i, m in ((0, 0x20A), (1, 0x20A), (6, 0x208), (7, 0x208)):
                img[blk(R['x0'] + i, y)] = V.meta(m)
    # the bridges: Mt. Thunder's, built as it builds them (posts on the cliffs, rails above and below, the walkway
    # between), its shade on the water below
    COLS = [(0x284, 0x240, 0x248), (0x241, 0x285, 0x249)] + [(0x230, 0x239, 0x238)] * 4 + [(0x232, 0x231, 0x23A), (0x233, 0x286, 0x23B)]
    fl = V.meta(mt.FLOOR)
    for R in P.RAVINES:
        for i, trio in enumerate(COLS):
            for j, m in enumerate(trio):
                x, y = R['x0'] + i, R['path'] - 1 + j; t = V.meta(m)
                if 2 <= i < 6 and j != 1:                # the rails over the river: only the wood, the water shows round it
                    a = ~(t == fl).all(2); img[blk(x, y)][a] = t[a]
                else: img[blk(x, y)] = t
        # its shade on the water: soft, fading over a tile and a half below the bridge
        y0 = (R['path'] + 2) * S
        for k in range(24):
            f = 0.70 + 0.30 * (k / 23.0)
            row = img[y0 + k, (R['x0'] + 2) * S:(R['x0'] + 6) * S]; row[:] = (row * f).astype(np.uint8)
    # the rest stop: flagstones, rug, candles (as before)
    _, _, MTS, _ = __import__('mm_render').render(0x86d65c)
    PATCH = {(x, y) for y in range(42, 46) for x in range(35, 46) if G[y, x] == '.'} - {(35, 42), (45, 42), (35, 45), (45, 45), (44, 45)}
    FLAGE = {'----': 0x2F9, '---f': 0x302, '--f-': 0x2F0, '--ff': 0x2F2, '-f--': 0x300, '-f-f': 0x301, '-ff-': 0x2F0,
             '-fff': 0x2F1, 'f---': 0x300, 'f--f': 0x302, 'f-f-': 0x2F8, 'f-ff': 0x2FA, 'ff--': 0x300, 'ff-f': 0x301,
             'fff-': 0x2F8, 'ffff': 0x2F9}
    for (x, y) in PATCH:
        k = ''.join('f' if (x + dx, y + dy) in PATCH else '-' for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)))
        t = MTS.meta(FLAGE[k]); a = ~(t == MTS.meta(0x209)).all(2); img[blk(x, y)][a] = t[a]
    for (x, y), m in {(40, 44): 0x2CB, (41, 44): 0x2CE, (36, 43): 0x2F3, (44, 43): 0x303, (36, 45): 0x2F7}.items():
        t = MTS.meta(m); a = ~(t == MTS.meta(0x2F9)).all(2); mid[blk(x, y)][a] = t[a]; mid_a[blk(x, y)] |= a
    # the great ice crystals (the Grotto's, glassy; a little bluer, to stand out on the pale floor)
    TINT = {'white': (196, 228, 250), 'blue': (128, 188, 238)}
    sprites = [gg.cutout(GV, mi, b) for mi, b in gg.BIG_CRYSTALS if b[2] - b[0] == 2 and b[3] - b[1] == 2]
    for i, ((bx, by), tint) in enumerate(sorted(C1.CRYSTAL_BLOCKS.items())):
        rgb, a = sprites[i % len(sprites)]
        x0, y0 = 2 * bx * S - S // 2, 2 * by * S + 2 * S - rgb.shape[0]
        g = C1.glass(rgb, a, img[y0:y0 + rgb.shape[0], x0:x0 + rgb.shape[1]], TINT[tint])
        foot = 2 * by * S
        for yy in range(rgb.shape[0]):
            Y = y0 + yy; lay, la = (mid, mid_a) if Y >= foot else (top, top_a); row = a[yy]
            lay[Y, x0:x0 + rgb.shape[1]][row] = g[yy][row]; la[Y, x0:x0 + rgb.shape[1]] |= row
    # small props in floor corners: glass ice chunks, and Mt. Thunder's snowy boulders and stalagmites
    small = [GV.meta(m) for m in gg.SMALL_CRYSTALS]; f200 = GV.meta(0x200)
    MTPROPS = [0x205, 0x205, 0x20F]
    def corner(x, y):
        if cls(x, y) != 'F' or (x, y) in C1.CRYSTAL_CELLS or (x, y) in PATCH or G[y, x] not in '.,;': return False
        if ids.get((x, y)) != mt.FLOOR: return False
        rk = [cls(x + dx, y + dy) == 'W' for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
        return sum(rk) >= 2 and not (rk[0] and rk[1]) and not (rk[2] and rk[3])
    chunks = set(); spots = list(P.SPOTS.values())
    for y in range(H):
        for x in range(W):
            if corner(x, y) and rnd.random() < 0.5 and all(abs(x - sx) + abs(y - sy) > 3 for sx, sy in spots):
                if any(abs(x - a) + abs(y - b) < 3 for a, b in chunks): continue
                if rnd.random() < 0.6:
                    t = small[rnd.randrange(len(small))]; a = ~(t == f200).all(2)
                    g = C1.glass(t, a, img[blk(x, y)], TINT[rnd.choice(['white', 'white', 'blue'])])
                else:
                    t = V.meta(rnd.choice(MTPROPS)); a = ~(t == floor).all(2); g = t
                mid[blk(x, y)][a] = g[a]; mid_a[blk(x, y)] |= a; chunks.add((x, y))
    # the rubble (frosted stones, the Shard's glint)
    x, y = C1.RUBBLE; b = np.zeros((S, S, 3), np.uint8); a = np.zeros((S, S), bool); yy, xx = np.mgrid[0:S, 0:S]
    for cx, cy, rx, ry in ((4, 11, 3.6, 2.6), (11, 11.5, 3.6, 2.6), (7.5, 8, 3.8, 2.8), (2.5, 6.5, 2.2, 1.8), (12.5, 6, 2.4, 1.9), (8, 4.2, 2.6, 2.0)):
        m = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1
        rim = m & ~(((xx - cx) / (rx - 1)) ** 2 + ((yy - cy) / (ry - 1)) ** 2 <= 1); hi = m & (yy < cy - ry * 0.35)
        b[m] = (78, 96, 128); b[hi] = (220, 236, 248); b[rim] = (36, 46, 74); a |= m
    b[9, 9] = b[8, 10] = b[9, 10] = (255, 214, 90); b[8, 9] = (255, 248, 200)
    mid[blk(x, y)][a] = b[a]; mid_a[blk(x, y)] |= a
    # snow blown in at the way in: soft drifts, whiter than the ice
    from scipy.ndimage import gaussian_filter
    nz = gaussian_filter(np.random.default_rng(seed).random((H * S, W * S)), 9); nz = (nz - nz.mean()) / nz.std()
    YY = np.mgrid[0:H * S, 0:W * S][0]; lift = np.clip((YY / S - 44) / 14.0, 0, 1) * 2.4 - 1.2
    hall = np.zeros((H * S, W * S), bool)
    for y in range(42, 59):
        for x in range(45, 59):
            if cls(x, y) == 'F' and (x, y) not in C1.CRYSTAL_CELLS and (x, y) not in PATCH and ids[(x, y)] in (mt.FLOOR, 0x207):
                hall[blk(x, y)] = True
    snow = hall & (nz + lift > 0.55); edge = hall & (nz + lift > 0.3) & ~snow
    img[snow] = (248, 252, 255); img[edge] = (226, 240, 250)
    sh = np.zeros_like(snow); sh[1:] = snow[:-1] & ~snow[1:]; img[sh & hall] = (196, 220, 238)
    # the way-in mat (the Grotto's, in Mt. Thunder's colours) and the cave mouth to the Peak
    t = GV.meta(0x229).astype(float); img[blk(*C1.EXIT_S)] = np.clip(t * 0.4 + np.array([60, 80, 110]) + (t.mean(2, keepdims=True) > 120) * 90, 0, 255).astype(np.uint8)
    x, y = C1.EXIT_N; X0, Y0 = (x - 1) * S, (y - 1) * S; yy, xx = np.mgrid[0:2 * S, 0:3 * S]
    arch = ((xx - 23.5) / 17.0) ** 2 + ((yy - 32) / 26.0) ** 2 <= 1; region = img[Y0:Y0 + 2 * S, X0:X0 + 3 * S]
    region[arch] = (16, 22, 40)
    ring = arch & ~(((xx - 23.5) / 15.0) ** 2 + ((yy - 32) / 24.0) ** 2 <= 1); region[ring] = (60, 76, 110)
    for ix, ln in ((12, 5), (17, 7), (22, 4), (27, 8), (32, 5), (36, 4)):
        ty = int(32 - 26 * np.sqrt(max(0, 1 - ((ix - 23.5) / 17.0) ** 2))) + 1
        for k in range(ln): region[ty + k, ix:ix + (1 if k > ln // 2 else 2)] = (214, 238, 255) if k < ln - 1 else (250, 254, 255)
    glow = arch & (yy > 22); region[glow] = (region[glow] * 0.5 + np.array([70, 100, 150]) * 0.5).astype(np.uint8)
    flat = img.copy(); flat[mid_a] = mid[mid_a]; flat[top_a] = top[top_a]
    LEVEL = dict(C1.LEVEL, **{'|': 0, 'r': 0, '=': 3})
    solid = np.zeros((H, W), bool); beh = np.zeros((H, W), int); elev = np.zeros((H, W), int)
    for y in range(H):
        for x in range(W):
            ch = G[y, x]; elev[y, x] = LEVEL.get(ch, 3)
            solid[y, x] = ch in '#Rv|r~' and ch != '~' or (x, y) in C1.CRYSTAL_CELLS or (x, y) in chunks
            if ch == '~': beh[y, x] = C1.MB_OCEAN_WATER
            if ch == 'v': beh[y, x] = C1.MB_JUMP_SOUTH
    xn, yn = C1.EXIT_N; solid[yn, xn - 1] = solid[yn, xn + 1] = True
    solid[yn, xn] = False; beh[yn, xn] = C1.MB_NORTH_ARROW_WARP; elev[yn, xn] = 5
    xs, ys = C1.EXIT_S; solid[ys, xs] = False; beh[ys, xs] = C1.MB_SOUTH_ARROW_WARP; elev[ys, xs] = 3
    return dict(solid=solid, beh=beh, elev=elev, bottom=img, mid=mid, mid_a=mid_a, top=top, top_a=top_a, flat=flat, chunks=chunks, ids=ids, missed=getattr(V, 'missed', 0))

if __name__ == '__main__':
    r = compose(); print('unseen patterns:', r['missed'])
    Image.fromarray(r['flat']).save(sys.argv[1] if len(sys.argv) > 1 else '/tmp/m2.png')
