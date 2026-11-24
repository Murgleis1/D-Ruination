"""Mt. Mirroh 1F drawn from the approved plan (plan_1f.py, user 2026-11-23: "This appears to be ideal. Let's rock n
roll"): MonoMyth's Glittering Grotto made icy (option A: deep glacier-blue rock, packed-ice floor), with extra ice and
snow (user): the Grotto's large and small crystals re-skinned as chunks of semi-see-through glassy ice at key places;
Mt. Thunder's frozen streams, flagstones and candles (the rest stop); Dreamstone Mysteries' plank bridges, cooled;
frost on the ledge; snow blown in at the way in.

compose() -> dict(bottom, mid, top, mid_a, top_a, flat, solid, beh, elev): layers for mapbuild (bottom: the ground;
mid: props drawn under the player; top: what the player walks behind) and each cell's collision, behaviour, level.
Usage: python3 compose_1f.py OUT.png  (the flattened mock)."""
import os, sys, random, colorsys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, '/home/claude/mono')
import gg, plan_1f as P
import mm_render as MR
W = H = 60; S = 16
G = P.G
MB_JUMP_SOUTH, MB_NORTH_ARROW_WARP, MB_SOUTH_ARROW_WARP, MB_OCEAN_WATER = 0x3B, 0x64, 0x65, 0x15

# ---- the plan's cells -------------------------------------------------------------------------------------------
def cells(ch): return {(x, y) for y in range(H) for x in range(W) if G[y, x] == ch}
WATER, BRIDGE, LEDGE, STAIRS = cells('~'), cells('='), cells('v'), cells('A') | cells('B')
EXIT_N, EXIT_S, RUBBLE = (54, 1), (55, 58), (4, 2)
# rock islands inside the caves that become great ice crystals (block coordinates in the plan, 2x2 cells each)
CRYSTAL_BLOCKS = {(15, 6): 'white', (26, 2): 'white', (11, 1): 'blue', (7, 10): 'blue', (13, 15): 'white',
                  (27, 9): 'blue', (26, 23): 'white'}
CRYSTAL_CELLS = {(2 * bx + i, 2 * by + j) for (bx, by) in CRYSTAL_BLOCKS for i in (0, 1) for j in (0, 1)}
LEVEL = {'.': 3, ',': 4, ';': 5, 'A': 0, 'B': 0, '=': 3, '~': 3, 'X': 5, 'E': 3, 'R': 5, 'v': 5, '#': 0}

def art_class(x, y):
    """rock or open, for the Grotto's rock masses: rock is the plan's rock and the exits' walls; the crystal islands,
    streams, bridges, stairs and the ledge sit on open floor."""
    if not (0 <= x < W and 0 <= y < H): return 'R'
    if (x, y) in CRYSTAL_CELLS: return 'O'
    if (x, y) in (EXIT_N, EXIT_S): return 'R'
    return 'R' if G[y, x] == '#' else 'O'

# ---- colours ------------------------------------------------------------------------------------------------------
_c1, _c2 = {}, {}
def rock_col(c):
    c = tuple(int(v) for v in c)
    if c not in _c1:
        h, s, v = colorsys.rgb_to_hsv(*(np.array(c) / 255))
        if s > 0.45 and v > 0.6: r = colorsys.hsv_to_rgb(0.53 + 0.05 * np.sin(h * 6.28), min(1, s * 0.4), 1.0)
        else: r = colorsys.hsv_to_rgb(0.595, min(1, s * 0.85 + 0.18), min(1, v * 1.25 + 0.04))
        _c1[c] = tuple(int(round(t * 255)) for t in r)
    return _c1[c]
def floor_col(c):
    c = tuple(int(v) for v in c)
    if c not in _c2:
        h, s, v = colorsys.rgb_to_hsv(*(np.array(c) / 255))
        if s > 0.45 and v > 0.6: r = colorsys.hsv_to_rgb(0.53, min(1, s * 0.3), 1.0)
        else: r = colorsys.hsv_to_rgb(0.565, min(1, s * 0.45 + 0.10), min(1, v * 1.5 + 0.28))
        _c2[c] = tuple(int(round(t * 255)) for t in r)
    return _c2[c]
def recolour(img, floor_mask):
    out = img.copy()
    for fn, m in ((rock_col, ~floor_mask), (floor_col, floor_mask)):
        sub = out[m]
        for c in {tuple(p) for p in sub.tolist()}:
            sub[(sub == c).all(1)] = fn(c)
        out[m] = sub
    return out

def glass(rgb, a, bg, tint):
    """a crystal as a chunk of clear ice over bg: outline deep blue, faces see-through, glints white."""
    lum = rgb.astype(float).mean(2) / 255; out = bg.astype(float).copy()
    if not a.any(): return out.astype(np.uint8)
    lo, hi = np.percentile(lum[a], 10), np.percentile(lum[a], 94)
    t = np.clip((lum - lo) / max(1e-3, hi - lo), 0, 1)
    edge = a & (t < 0.10); glint = a & (t > 0.95); face = a & ~edge & ~glint
    T = np.array(tint, float); k = (0.40 + 0.45 * t)[..., None]
    mix = out * (1 - k) + (T * (0.70 + 0.30 * t[..., None])) * k
    out[face] = mix[face]; out[edge] = (44, 82, 140); out[glint] = (250, 254, 255)
    return out.astype(np.uint8)
TINT = {'white': (214, 240, 255), 'blue': (150, 210, 250), 'gold': (255, 236, 170)}

def mt_tile(ts, m): return ts.meta(m)

def compose(seed=7):
    rnd = random.Random(seed)
    V = gg.Vocab()
    _, _, MT, _ = MR.render(0x86d65c)                      # Mt. Thunder's tiles (water, flagstones, candles)
    bottom = np.zeros((H * S, W * S, 3), np.uint8); fmask = np.zeros((H * S, W * S), bool)
    mid = np.zeros_like(bottom); mid_a = np.zeros((H * S, W * S), bool)
    top = np.zeros_like(bottom); top_a = np.zeros((H * S, W * S), bool)
    blk = lambda x, y: (slice(y * S, y * S + S), slice(x * S, x * S + S))
    f200 = V.meta(0x200)
    # 1. the Grotto's rock and floor
    for y in range(H):
        for x in range(W):
            key = art_class(x, y) + ''.join(art_class(x + dx, y + dy) for dx, dy in gg.N8)
            m = 0x219 if key == 'R' * 9 else V.pick_at(art_class, x, y, rnd)[0]
            t = V.meta(m); bottom[blk(x, y)] = t
            if V.side.get(m) == 'O': fmask[blk(x, y)] = True
            elif m != 0x219:
                fl = (t == f200).all(2)
                if fl.mean() < 0.5:                        # a rock tile: its floor pixels only where no rock top shares them
                    for r in (0x219, 0x214, 0x211, 0x213, 0x215): fl &= ~(t == V.meta(r)).all(2)
                fmask[blk(x, y)] = fl
    # 2. stairs, the ledge (the Grotto's ledge line), the way-in mat
    for p in STAIRS: bottom[blk(*p)] = V.meta(0x207); fmask[blk(*p)] = False
    for (x, y) in LEDGE:
        l, r = (x - 1, y) in LEDGE, (x + 1, y) in LEDGE
        bottom[blk(x, y)] = V.meta(0x2C2 if l and r else 0x2C0 if r else 0x2BE); fmask[blk(x, y)] = True
    bottom[blk(*EXIT_S)] = V.meta(0x229); fmask[blk(*EXIT_S)] = False
    img = recolour(bottom, fmask)
    # snow on the rock masses' north rims (where floor lies north of the rock): a snowy crest, as on Mt. Thunder
    rnd2 = random.Random(seed + 1)
    for y in range(1, H):
        for x in range(W):
            if art_class(x, y) != 'R' or art_class(x, y - 1) != 'O' or (x, y) in (EXIT_N, EXIT_S): continue
            if (x - 1, y) == EXIT_N or (x + 1, y) == EXIT_N: continue
            b = img[blk(x, y)]; fm = fmask[blk(x, y)]
            for xx in range(S):
                col = np.nonzero(~fm[:, xx])[0]
                if not len(col): continue
                t0 = col[0]; depth = 2 + (1 if rnd2.random() < 0.4 else 0)
                for k in range(depth):
                    if t0 + k < S: b[t0 + k, xx] = (240, 248, 255) if k < depth - 1 else (196, 220, 240)
    # frost along the ledge: a pale rim over its dark line
    for (x, y) in LEDGE:
        b = img[blk(x, y)]; lum = b.astype(int).sum(2); dark = lum < np.percentile(lum, 20)
        for yy in range(1, S):
            for xx in range(S):
                if dark[yy, xx] and not dark[yy - 1, xx]: b[yy - 1, xx] = (228, 245, 255)
    # 3. the frozen streams (Mt. Thunder's water, edges by its own neighbours; colder, with floes)
    def wat(x, y): return (x, y) in WATER or (x, y) in BRIDGE
    EDGE = {'-www': 0x251, 'w-ww': 0x25A, 'ww-w': 0x25C, 'www-': 0x258, '-ww-': 0x250, '--ww': 0x252,
            'w--w': 0x268, 'ww--': 0x26A}
    for (x, y) in WATER | BRIDGE:
        k = ''.join('w' if wat(x + dx, y + dy) else '-' for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)))
        t = MT.meta(EDGE.get(k, 0x259)).astype(float)
        g = t.mean(2, keepdims=True); t = (t * 0.7 + g * 0.3) * np.array([0.62, 0.80, 0.92]) + np.array([10, 26, 44])
        img[blk(x, y)] = np.clip(t, 0, 255).astype(np.uint8)
    for (x, y) in WATER:                                     # ice floes: pale rounded patches on the water
        if rnd.random() < 0.35:
            b = img[blk(x, y)]; cx, cy, rr = rnd.randint(4, 11), rnd.randint(4, 11), rnd.randint(2, 4)
            yy, xx = np.mgrid[0:S, 0:S]; m = (xx - cx) ** 2 + (yy - cy) ** 2 <= rr * rr
            b[m] = (214, 236, 250); b[m & ((yy - cy) == -rr + 1)] = (250, 254, 255)
    # 4. bridges: Dreamstone Mysteries' planks (its upper bridge), cooled
    dm = np.array(Image.open(os.path.join(HERE, 'dm_bridge.png')).convert('RGB')).astype(float)
    for (x, y) in BRIDGE:
        row = y - min(yy for xx, yy in BRIDGE if xx == x)
        col = 0 if (x - 1, y) not in BRIDGE else (2 if (x + 1, y) not in BRIDGE else 1)
        piece = dm[row * S:(row + 1) * S, col * S:(col + 1) * S]
        g = piece.mean(2, keepdims=True)
        img[blk(x, y)] = np.clip(piece * 0.62 + g * 0.28 + np.array([6, 16, 30]), 0, 255).astype(np.uint8)
    # 5. the rest stop: a ragged patch of Mt. Thunder's flagstones (its own edge tiles, by neighbours), a rug, candles
    PATCH = {(x, y) for y in range(40, 45) for x in range(37, 45) if G[y, x] == '.'} - {(37, 40), (44, 40), (37, 44), (44, 44), (43, 44), (44, 43)}
    FLAGE = {'----': 0x2F9, '---f': 0x302, '--f-': 0x2F0, '--ff': 0x2F2, '-f--': 0x300, '-f-f': 0x301, '-ff-': 0x2F0,
             '-fff': 0x2F1, 'f---': 0x300, 'f--f': 0x302, 'f-f-': 0x2F8, 'f-ff': 0x2FA, 'ff--': 0x300, 'ff-f': 0x301,
             'fff-': 0x2F8, 'ffff': 0x2F9}
    for (x, y) in PATCH:
        k = ''.join('f' if (x + dx, y + dy) in PATCH else '-' for dx, dy in ((0, -1), (1, 0), (0, 1), (-1, 0)))
        t = MT.meta(FLAGE[k]); fl = MT.meta(0x209)
        a = ~(t == fl).all(2)                                  # the stones only; the ice floor shows between
        img[blk(x, y)][a] = t[a]
    for (x, y), m in {(40, 42): 0x2CB, (41, 42): 0x2CE, (38, 41): 0x2F3, (43, 41): 0x303, (38, 43): 0x2F7}.items():
        t = MT.meta(m); base = MT.meta(0x2F9); a = ~(t == base).all(2)
        mid[blk(x, y)][a] = t[a]; mid_a[blk(x, y)] |= a
    # 6. the great ice crystals (the Grotto's, re-skinned glassy) on the islands, their tips over the cells above
    sprites = [gg.cutout(V, mi, b) for mi, b in gg.BIG_CRYSTALS if b[2] - b[0] == 2 and b[3] - b[1] == 2]
    for i, ((bx, by), tint) in enumerate(sorted(CRYSTAL_BLOCKS.items())):
        rgb, a = sprites[i % len(sprites)]
        x0, y0 = 2 * bx * S - S // 2, 2 * by * S + 2 * S - rgb.shape[0]          # centred on the 2x2, standing on its foot
        bg = img[y0:y0 + rgb.shape[0], x0:x0 + rgb.shape[1]]
        g = glass(rgb, a, bg, TINT[tint])
        foot = 2 * by * S                                                          # rows from here down: under the player
        for yy in range(rgb.shape[0]):
            Y = y0 + yy
            lay, la = (mid, mid_a) if Y >= foot else (top, top_a)
            row = a[yy]
            lay[Y, x0:x0 + rgb.shape[1]][row] = g[yy][row]; la[Y, x0:x0 + rgb.shape[1]] |= row
    # 7. small ice chunks (the Grotto's small crystals, glassy) in floor corners, and glints in the rock
    small = [V.meta(m) for m in gg.SMALL_CRYSTALS]
    def corner(x, y):
        if G[y, x] not in '.,;' or (x, y) in CRYSTAL_CELLS: return False
        rk = [art_class(x + dx, y + dy) == 'R' for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
        return sum(rk) >= 2 and not (rk[0] and rk[1]) and not (rk[2] and rk[3])
    chunks = set()
    spots = list(P.SPOTS.values())
    for y in range(H):
        for x in range(W):
            if corner(x, y) and rnd.random() < 0.45 and all(abs(x - sx) + abs(y - sy) > 3 for sx, sy in spots):
                if any(abs(x - a) + abs(y - b) < 3 for a, b in chunks): continue
                t = small[rnd.randrange(len(small))]; a = ~(t == f200).all(2)
                g = glass(t, a, img[blk(x, y)], TINT[rnd.choice(['white', 'white', 'blue'])])
                mid[blk(x, y)][a] = g[a]; mid_a[blk(x, y)] |= a; chunks.add((x, y))
    # 8. the rubble: a small heap of loose stones (frosted), and the Shard's faint gold glint between them
    x, y = RUBBLE; b = np.zeros((S, S, 3), np.uint8); a = np.zeros((S, S), bool)
    yy, xx = np.mgrid[0:S, 0:S]
    for cx, cy, rx, ry in ((4, 11, 3.6, 2.6), (11, 11.5, 3.6, 2.6), (7.5, 8, 3.8, 2.8), (2.5, 6.5, 2.2, 1.8), (12.5, 6, 2.4, 1.9), (8, 4.2, 2.6, 2.0)):
        m = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1
        rim = m & ~(((xx - cx) / (rx - 1)) ** 2 + ((yy - cy) / (ry - 1)) ** 2 <= 1)
        hi = m & (yy < cy - ry * 0.35)
        b[m] = (70, 96, 132); b[hi] = (176, 204, 228); b[rim] = (28, 44, 72); a |= m
    b[9, 9] = b[8, 10] = b[9, 10] = (255, 228, 120); b[8, 9] = (255, 250, 210)
    mid[blk(x, y)][a] = b[a]; mid_a[blk(x, y)] |= a
    # 9. snow blown in at the way in: soft drifts (a smoothed noise field) on the hall's floor, thinning northwards
    from scipy.ndimage import gaussian_filter
    nz = gaussian_filter(np.random.default_rng(seed).random((H * S, W * S)), 9)
    nz = (nz - nz.mean()) / nz.std()
    yy, xx = np.mgrid[0:H * S, 0:W * S]
    lift = np.clip((yy / S - 44) / 14.0, 0, 1) * 2.4 - 1.2
    hall = np.zeros((H * S, W * S), bool)
    for y in range(42, 59):
        for x in range(45, 59):
            if G[y, x] == '.' and (x, y) not in CRYSTAL_CELLS and fmask[blk(x, y)].any(): hall[blk(x, y)] = True
    hall &= fmask
    snow = hall & (nz + lift > 0.55); edge = hall & (nz + lift > 0.25) & ~snow
    img[snow] = (236, 246, 255); img[edge] = (198, 222, 242)
    sh = np.zeros_like(snow); sh[1:] = snow[:-1] & ~snow[1:]
    img[sh & hall] = (176, 204, 232)
    # 10. the exit to the Peak: a dark mouth in the north wall (three tiles wide, two tall; only the middle is the
    # way), icicles hanging from its brow, cold light at its foot
    x, y = EXIT_N; X0, Y0 = (x - 1) * S, (y - 1) * S
    yy, xx = np.mgrid[0:2 * S, 0:3 * S]
    arch = ((xx - 23.5) / 17.0) ** 2 + ((yy - 32) / 26.0) ** 2 <= 1
    region = img[Y0:Y0 + 2 * S, X0:X0 + 3 * S]
    region[arch] = (12, 18, 34)
    ring = arch & ~(((xx - 23.5) / 15.0) ** 2 + ((yy - 32) / 24.0) ** 2 <= 1); region[ring] = (60, 92, 140)
    for ix, ln in ((12, 5), (17, 7), (22, 4), (27, 8), (32, 5), (36, 4)):
        top_y = int(32 - 26 * np.sqrt(max(0, 1 - ((ix - 23.5) / 17.0) ** 2))) + 1
        for k in range(ln):
            w = 1 if k > ln // 2 else 2
            region[top_y + k, ix:ix + w] = (214, 238, 255) if k < ln - 1 else (250, 254, 255)
    glow = arch & (yy > 22); region[glow] = (region[glow] * 0.5 + np.array([60, 96, 150]) * 0.5).astype(np.uint8)
    # flatten
    flat = img.copy(); flat[mid_a] = mid[mid_a]; flat[top_a] = top[top_a]
    # cells: collision, behaviour, level
    solid = np.zeros((H, W), bool); beh = np.zeros((H, W), int); elev = np.zeros((H, W), int)
    for y in range(H):
        for x in range(W):
            ch = G[y, x]; elev[y, x] = LEVEL.get(ch, 3)
            solid[y, x] = ch in '#Rv' or (x, y) in CRYSTAL_CELLS or (x, y) in chunks
            if ch == '~': beh[y, x] = MB_OCEAN_WATER
            if ch == 'v': beh[y, x] = MB_JUMP_SOUTH
    solid[EXIT_N[1], EXIT_N[0] - 1] = solid[EXIT_N[1], EXIT_N[0] + 1] = True
    solid[EXIT_N[1], EXIT_N[0]] = False; beh[EXIT_N[1], EXIT_N[0]] = MB_NORTH_ARROW_WARP; elev[EXIT_N[1], EXIT_N[0]] = 5
    solid[EXIT_S[1], EXIT_S[0]] = False; beh[EXIT_S[1], EXIT_S[0]] = MB_SOUTH_ARROW_WARP; elev[EXIT_S[1], EXIT_S[0]] = 3
    return dict(bottom=img, mid=mid, mid_a=mid_a, top=top, top_a=top_a, flat=flat, solid=solid, beh=beh, elev=elev,
                chunks=chunks)

if __name__ == '__main__':
    r = compose(); Image.fromarray(r['flat']).save(sys.argv[1] if len(sys.argv) > 1 else '/tmp/c1f.png')
