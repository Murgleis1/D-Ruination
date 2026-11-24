"""The Ancient Cormoria slip, art (plan_slip.py; user 2026-11-24). Built the way MonoMyth's red-rock canyon country is
built (canyon.py); its props, the skeleton, the obelisks, the altars, the cliff homes and the carved wall placed on it.
Usage: python3 compose_slip.py OUT.png"""
import os, sys, random
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import canyon
import plan_slip as P
import props_slip  # noqa
W, H, S = P.W, P.H, 16
G = P.G
blk = lambda x, y: (slice(y * S, y * S + S), slice(x * S, x * S + S))
ROCKY = set('#DPS')                 # (cells drawn as red rock in the base: cliffs, the homes' and panels' walls, ladders)
WATERY = set('~FBo')

def base_class(x, y):
    if not (0 <= x < W and 0 <= y < H): return 'W'
    ch = G[y, x]
    if ch in ROCKY:
        d = 1
        while y + d < H and G[y + d, x] in ROCKY: d += 1
        if y + d >= H: d = 9
        return canyon.rock_class(d)
    if ch in WATERY: return 'A'
    if ch == 'r': return 'r'
    return 'F'

def compose(seed=5):
    V = canyon.Vocab()
    img = np.zeros((H * S, W * S, 3), np.uint8)
    top = np.zeros_like(img); top_a = np.zeros((H * S, W * S), bool)
    ids = {}
    for y in range(H):
        for x in range(W):
            if G[y, x] == 'K': continue
            me = base_class(x, y); nb = [base_class(x + dx, y + dy) for dx, dy in canyon.N8]
            nb = ['F' if (0 <= x + dx < W and 0 <= y + dy < H and G[y + dy, x + dx] == 'K') else c for c, (dx, dy) in zip(nb, canyon.N8)]
            m = V.pick(me + ''.join(nb)); ids[(x, y)] = m; img[blk(x, y)] = V.meta(m)
    import props_slip as PS
    rnd = random.Random(seed)
    sand = V.meta(canyon.SAND)
    def put(rgb, a, x, y, top_rows=0):
        """a piece at cell (x, y); its first top_rows rows of cells on the top layer (walked behind)"""
        h, w = a.shape
        for py in range(h):
            Y = y * S + py
            if not (0 <= Y < H * S): continue
            row_a = a[py]; X0 = x * S
            if py < top_rows * S:
                top[Y, X0:X0 + w][row_a] = rgb[py][row_a]; top_a[Y, X0:X0 + w] |= row_a
            else:
                img[Y, X0:X0 + w][row_a] = rgb[py][row_a]
    # ---- the sky over the mesa's rim (the ancient backdrop shows here) and the rim itself: a band of red rock with a
    # dark outline, rounded smooth (as the Peak's summit)
    sky_a = np.zeros((H * S, W * S), bool)
    for y in range(H):
        for x in range(W):
            if G[y, x] == 'K': sky_a[blk(x, y)] = True; img[blk(x, y)] = (164, 30, 28)
    from scipy.ndimage import gaussian_filter, distance_transform_edt
    TR = 15 * S
    land = ~sky_a[:TR]
    cut = land & ~(gaussian_filter(land.astype(float), 5.0) > 0.5)
    sub = img[:TR]; sub[cut] = (164, 30, 28); sky_a[:TR] |= cut
    dist = distance_transform_edt(land & ~cut)
    rock = np.tile(V.meta(0x20C), (TR // S + 1, W, 1))[:TR, :W * S]
    for d in range(1, 9):
        m = (land & ~cut) & (dist > d - 1) & (dist <= d)
        if d == 1: sub[m] = (44, 14, 16)
        elif d <= 7: sub[m] = (rock[m].astype(int) * (0.8 if d == 2 else 1.0)).astype(np.uint8)
        else: sub[m] = (150, 70, 50)
    # ---- the falls out of the mesa's face, the rope bridge, the rope ladders
    fx = min(x for (x, y) in P.FALLS); fy = min(y for (x, y) in P.FALLS); fh = max(y for (x, y) in P.FALLS) - fy + 2
    img[fy * S:(fy + fh) * S, fx * S:(fx + 2) * S] = PS.falls(fh)
    bys = sorted({y for y in range(H) if G[y, 24] == 'B'})
    if bys: img[bys[0] * S:(bys[-1] + 1) * S, 24 * S:26 * S] = PS.bridge(len(bys))
    done = set()
    for y in range(H):
        for x in range(W):
            if G[y, x] != 'S' or (x, y) in done: continue
            w = 2 if x + 1 < W and G[y, x + 1] == 'S' else 1
            hgt = 1
            while y + hgt < H and G[y + hgt, x] == 'S': hgt += 1
            img[y * S:(y + hgt) * S, x * S:(x + w) * S] = PS.ladder(hgt, w)
            done |= {(x + i, y + j) for i in range(w) for j in range(hgt)}
    # ---- the adobe homes on the west mesa, the carved panels in the faces
    hk = 0; done = set()
    for y in range(H):
        for x in range(W):
            if G[y, x] == 'D' and (x, y) not in done:
                img[y * S:(y + 5) * S, x * S:(x + 4) * S] = PS.house(hk); hk += 1
                done |= {(x + i, y + j) for i in range(4) for j in range(5)}
            if G[y, x] == 'P' and (x, y) not in done:
                img[y * S:(y + 2) * S, x * S:(x + 2) * S] = PS.panel(x + y)
                done |= {(x + i, y + j) for i in range(2) for j in range(2)}
    # ---- the pink crystal sand round the arrival ring
    for y in range(H):
        for x in range(W):
            if G[y, x] == 'p' or (G[y, x] in 'OA' and y > 40):
                b = img[blk(x, y)]; b[:] = PS.pink_sand(b)
                if G[y, x] == 'p':
                    for (gx, gy) in PS.GEMS[(x * 7 + y * 3) % len(PS.GEMS)]: PS.gem(b, gx, gy)
    # ---- the skeleton: the skull, the spine's vertebrae, the rib arches over the way, ribs and bone spikes standing
    sx = min(x for x in range(W) for y in range(H) if G[y, x] == 'X'); sy = min(y for y in range(H) if 'X' in G[y])
    rgb, a = PS.skull(); put(rgb, a, sx, sy)
    # the spine: a chain of bone knuckles along the curve from behind the skull west to the tail, each with a dorsal
    # spike rising north (drawn over the sand above on the top layer: walked behind); broken where the way crosses it
    pts = [(x * S + 8, y * S + 9) for (x, y) in P.spine]
    path = []
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        n = int(max(abs(bx - ax), abs(by - ay)))
        for t in range(n): path.append((ax + (bx - ax) * t / n, ay + (by - ay) * t / n))
    yy, xx = np.mgrid[0:H * S, 0:W * S]
    for k, (px, py) in enumerate(path[::9]):
        cx_, cy_ = int(px) // S, int(py) // S
        if G[cy_, cx_] != 'x': continue                                     # (the break for the way)
        x0, y0 = int(px) - 8, int(py) - 6
        reg = (slice(max(0, y0 - 18), y0 + 12), slice(max(0, x0), x0 + 17))
        Y, X = yy[reg], xx[reg]
        knuckle = ((X - px) / 6.5) ** 2 + ((Y - py) / 4.8) ** 2 <= 1
        L = 8 + (k * 7) % 9
        spike = (abs(X - px - (py - Y) * 0.15) <= np.maximum(0, (Y - (py - 4 - L)) * 0.22)) & (Y <= py - 3) & (Y >= py - 4 - L)
        bone = knuckle | spike
        col = np.zeros(X.shape + (3,), np.uint8); col[bone] = PS.BONE[1]
        col[knuckle & (Y < py - 1)] = PS.BONE[0]; col[knuckle & (Y > py + 2)] = PS.BONE[2]
        col[spike & (X > px + 0.5)] = PS.BONE[2]
        e = bone & (~np.roll(bone, 1, 0) | ~np.roll(bone, -1, 0) | ~np.roll(bone, 1, 1) | ~np.roll(bone, -1, 1))
        col[e] = PS.BONE[4]
        ground = bone & ((Y // S) == cy_); over = bone & ((Y // S) < cy_)
        img[reg][ground] = col[ground]
        top[reg][over] = col[over]; top_a[reg] |= over
    for A in P.ARCHES:
        rgb, a = PS.arch(A['x1'] - A['x0'] - 1)
        put(rgb, a, A['x0'], A['y'] - 1, top_rows=2)
    k = 0
    for y in range(H):
        for x in range(W):
            if G[y, x] == 'x' and (x, y) not in P.SPINE_CELLS:
                if any(x in (A['x0'], A['x1']) and y in (A['y'], A['y'] + 1) for A in P.ARCHES): continue
                rgb, a = PS.spike(k, tall=(y % 2 == 0)); put(rgb, a, x, y - (1 if a.shape[0] > S else 0), top_rows=1 if a.shape[0] > S else 0); k += 1
    # ---- the dreamstone obelisks (their shafts' upper halves on the top layer) and the two altars
    for y in range(H):
        for x in range(W):
            if G[y, x] == 'O': rgb, a = PS.obelisk(); put(rgb, a, x, y - 1, top_rows=1)
    done = set()
    for y in range(H):
        for x in range(W):
            if G[y, x] == 'A' and (x, y) not in done:
                rgb, a = PS.altar(north=y < 20); put(rgb, a, x, y)
                done |= {(x + i, y + j) for i in range(2) for j in range(2)}
    # ---- the canyon's plants: on the sand, along the walls' feet; on the rock tops; palms and cacti as planned
    PLANTS = [0x245, 0x247, 0x243, 0x233, 0x266]
    def plant(m, x, y):
        t = V.meta(m); msk = np.abs(t.astype(int) - sand.astype(int)).sum(-1) > 40
        b = img[blk(x, y)]; b[msk] = t[msk]
    for y in range(H):
        for x in range(W):
            ch = G[y, x]
            h_ = ((x * 73856093) ^ (y * 19349663)) % 1000 / 1000.0
            if ch == 'T' or ch == 'c': plant(PLANTS[(x + y) % 4] if ch == 'T' else 0x233, x, y)
            elif ch == '#' and base_class(x, y) == 'W' and h_ < 0.10:
                t = V.meta(PLANTS[int(h_ * 40) % 4]); m0 = V.meta(0x20C)
                msk = np.abs(t.astype(int) - sand.astype(int)).sum(-1) > 40
                b = img[blk(x, y)]; b[msk] = t[msk]
    for y in range(H):
        for x in range(W):
            if G[y, x] == 'g':
                b = img[blk(x, y)]; f = b.astype(int)
                b[:] = np.clip(f * 0.55 + np.array([60, 110, 50]) * 0.45, 0, 255).astype(np.uint8)
                if (x + y) % 2: plant(0x245, x, y)
    return dict(bottom=img, top=top, top_a=top_a, sky_a=sky_a, ids=ids, missed=getattr(V, 'missed', 0))

if __name__ == '__main__':
    r = compose(); print('unseen patterns:', r['missed'])
    flat = r['bottom'].copy(); flat[r['top_a']] = r['top'][r['top_a']]
    Image.fromarray(flat).save(sys.argv[1] if len(sys.argv) > 1 else '/tmp/slip.png')
