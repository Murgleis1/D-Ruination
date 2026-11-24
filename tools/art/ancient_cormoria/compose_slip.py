"""The Ancient Cormoria slip, art v2 (plan_slip.py v3, normalised by normalize_plan.py). The terrain solved from
MonoMyth's canyon (tilesolve.py): each cell a tile MonoMyth puts in that neighbourhood, agreeing with its neighbours as
MonoMyth's do (the falls and the cliff homes are MonoMyth's own tiles, solved round); MonoMyth's own props scattered on
it only where they meet their neighbours as MonoMyth's do; then the set pieces. Every seam left is reported.
Usage: python3 compose_slip.py OUTDIR"""
import os, sys, random
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tilesolve as T
import plan_slip as P
import props_slip as PS
S = 16
CANYON, DESERT = 0x86daf4, 0x869708
HOUSE_SRC = [(39, 0, 42, 4), (39, 7, 42, 11)]            # (MonoMyth's canyon pueblo: two houses, 4x5)
# MonoMyth's canyon props (studied: assets/ancient_cormoria_reference/canyon_props_sheet.png), by what they stand on
ROCK_PROPS = [0x232, 0x233, 0x234, 0x235, 0x23a, 0x23b, 0x23c, 0x23d, 0x243, 0x245, 0x245, 0x243, 0x21c, 0x21d,
              0x25f, 0x3bf, 0x3c7]
SAND_PROPS = [0x241, 0x241, 0x16d, 0x247, 0x230, 0x231, 0x239, 0x22d, 0x266]
RIPPLE_PROPS = [0x247, 0x247, 0x236, 0x237]
WALKABLE_PROPS = {0x241, 0x16d, 0x247, 0x266}

def terrain():
    P.load(); cls = P.classes(); fixed = {}
    for h in P.HOUSES:
        x0, y0, x1, y1 = HOUSE_SRC[h['src']]
        t, k = T.ref_block(CANYON, x0, y0, x1, y1)
        for (dx, dy), m in t.items():                    # (the whole 4x5 block as MonoMyth has it; round it solved)
            fixed[(h['x'] + dx, h['y'] + dy)] = m; cls[h['y'] + dy, h['x'] + dx] = k[(dx, dy)]
    F = P.FALLS                                            # (MonoMyth's falls: their lip, their fall, their foam)
    for x in range(F['x0'], F['x1'] + 1):
        fixed[(x, F['top'])] = 0xA0; fixed[(x, F['top'] + 1)] = 0xA1; fixed[(x, F['top'] + 2)] = 0xA2
    g, rep = T.solve(cls, fixed=fixed)
    for p, m in fixed.items(): g[p[1], p[0]] = m
    return cls, g, rep

def busy():
    """cells the set pieces use or stand by: no props there"""
    b = set()
    def box(x0, y0, x1, y1):
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1): b.add((x, y))
    for L in P.LADDERS: box(L['x'] - 1, L['y'] - 2, L['x'] + 2, L['y'] + 2)
    box(22, P.BRIDGE['y0'] - 1, 27, P.BRIDGE['y1'] + 1)
    for h in P.HOUSES: box(h['x'] - 1, h['y'] - 1, h['x'] + 4, h['y'] + 5)
    for (x, y) in P.PANELS: box(x - 1, y - 1, x + 2, y + 2)
    sx, sy = P.SKULL; box(sx - 1, sy - 2, sx + 6, sy + 5)
    for (x, y) in P.spine_cells(): box(x, y - 1, x, y)
    for R in P.RIBS: box(P.RIB_X[0], R['y'] - 1, P.RIB_X[1], R['y'] + 1)
    for (x, y) in P.RIB_STUBS + P.CLAW + P.CACTI + P.PALMS + P.OASIS_GREEN: box(x, y - 1, x, y)
    for (x, y) in P.OBELISKS_SOUTH + P.OBELISKS_NORTH: box(x, y - 2, x, y)
    for A in P.ALTARS: box(A['x'] - 1, A['y'] - 1, A['x'] + 2, A['y'] + 2)
    pk = P.PINK; box(int(pk['cx'] - pk['rx']) - 1, int(pk['cy'] - pk['ry']) - 1, int(pk['cx'] + pk['rx']) + 1, int(pk['cy'] + pk['ry']) + 1)
    box(23, 13, 26, 16)                                    # (the way down to the mesa's ladder)
    return b

_WAY = None
def near_way(x, y):
    """on or beside the shortest walk from the arrival to the north altar (props there are ones walked through)"""
    global _WAY
    if _WAY is None:
        from collections import deque
        s = P.solid(); start, goal = P.ARRIVE, P.SPOTS['north altar']; prev = {start: None}; q = deque([start])
        while q:
            p = q.popleft()
            if p == goal: break
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (p[0] + dx, p[1] + dy)
                if 0 <= n[0] < P.W and 0 <= n[1] < P.H and n not in prev and not s[n[1], n[0]]: prev[n] = p; q.append(n)
        _WAY = set(); p = goal
        while p: _WAY.add(p); p = prev.get(p)
    return any((x + dx, y + dy) in _WAY for dx in (-1, 0, 1) for dy in (-1, 0, 1))

def scatter(cls, g, seed=11):
    """MonoMyth's props on the rock tops, the sand and the dunes: each where its four neighbours meet it as they do in
    MonoMyth (never across a seam), a few cells apart; by the way only the ones walked through"""
    C = T.corpus(); rnd = random.Random(seed); H, W = g.shape; B = busy(); placed = []
    dens = {'W': 0.12, 'F': 0.035, 'r': 0.04}
    cells = [(x, y) for y in range(1, H - 1) for x in range(1, W - 1)]
    rnd.shuffle(cells)
    for (x, y) in cells:
        c = cls[y, x]
        if c not in dens or (x, y) in B or rnd.random() > dens[c]: continue
        if any(abs(x - a) + abs(y - b) < 3 for (a, b) in placed): continue
        pool = ROCK_PROPS if c == 'W' else SAND_PROPS if c == 'F' else RIPPLE_PROPS
        if c != 'W' and near_way(x, y): pool = [m for m in pool if m in WALKABLE_PROPS]
        for m in rnd.sample(pool, len(pool)):
            nb = [(g[y, x - 1], m, 'H'), (m, g[y, x + 1], 'H'), (g[y - 1, x], m, 'V'), (m, g[y + 1, x], 'V')]
            if all(a >= 0 and b >= 0 and ((int(a), int(b)) in (C.H if d == 'H' else C.V)) for a, b, d in nb):
                g[y, x] = m; placed.append((x, y))
                if m not in WALKABLE_PROPS and c != 'W': P.EXTRA_SOLID.add((x, y))
                break
    for k, (x, y) in enumerate(P.OASIS_GREEN):             # (the oasis' flowers and grass, where they meet as MonoMyth's)
        for m in ((0x266, 0x16d, 0x241)[k % 3], 0x266, 0x16d, 0x241):
            nb = [(g[y, x - 1], m, 'H'), (m, g[y, x + 1], 'H'), (g[y - 1, x], m, 'V'), (m, g[y + 1, x], 'V')]
            if cls[y, x] == 'F' and all(a >= 0 and b >= 0 and ((int(a), int(b)) in (C.H if d == 'H' else C.V)) for a, b, d in nb):
                g[y, x] = m; placed.append((x, y)); break
    return placed

# ---- painted set pieces
SANDSTONE = [(255, 226, 180), (236, 190, 140), (206, 150, 104), (164, 104, 74), (112, 62, 50), (58, 26, 30)]
def obelisk():
    """a dreamstone obelisk, 16x48 (its upper two cells on the top layer): a weathered sandstone shaft on a stepped
    plinth, its pyramidion cap, glyphs cut down its face, a shard of dreamstone set in it glowing pink; lit from the
    west as the canyon's rock is"""
    Hh = 48; rgb = np.zeros((Hh, 16, 3), np.uint8); a = np.zeros((Hh, 16), bool)
    def fill(x0, x1, y0, y1, c): rgb[y0:y1, x0:x1] = c; a[y0:y1, x0:x1] = True
    fill(1, 15, 40, 46, SANDSTONE[3]); fill(1, 15, 40, 41, SANDSTONE[1]); fill(1, 15, 45, 46, SANDSTONE[5])
    rgb[40:46, 1] = rgb[40:46, 14] = SANDSTONE[5]
    fill(2, 14, 36, 40, SANDSTONE[2]); fill(2, 14, 36, 37, SANDSTONE[0]); rgb[36:40, 2] = rgb[36:40, 13] = SANDSTONE[5]
    for y in range(7, 36):                                 # the shaft, a little narrower above
        w = 4 if y < 16 else 5
        x0, x1 = 8 - w, 8 + w
        fill(x0, x1, y, y + 1, SANDSTONE[2])
        rgb[y, x0:x0 + 2] = SANDSTONE[1]; rgb[y, x1 - 2:x1] = SANDSTONE[3]; rgb[y, x0] = rgb[y, x1 - 1] = SANDSTONE[5]
    for y in range(1, 7):                                  # the pyramidion
        w = max(1, (y + 1) * 4 // 7)
        fill(8 - w, 8 + w, y, y + 1, SANDSTONE[1]); rgb[y, 8:8 + w] = SANDSTONE[3]
        rgb[y, 8 - w] = rgb[y, 7 + w] = SANDSTONE[5]
    rgb[0, 7:9] = SANDSTONE[5]; a[0, 7:9] = True
    for (y, x) in ((21, 7), (24, 5), (24, 9), (27, 7), (30, 5), (30, 9), (33, 7)):   # glyphs
        rgb[y, x:x + 2] = SANDSTONE[4]
    crys = [(10, 7), (10, 8), (11, 6), (11, 7), (11, 8), (11, 9), (12, 6), (12, 7), (12, 8), (12, 9),
            (13, 6), (13, 7), (13, 8), (13, 9), (14, 7), (14, 8)]
    for (y, x) in crys: rgb[y, x] = PS.PINK[2] if x > 7 else PS.PINK[3]
    rgb[11, 7] = rgb[12, 6] = PS.PINK[4]
    for (y, x) in ((9, 7), (9, 8), (15, 7), (15, 8)): rgb[y, x] = PS.PINK[1]       # (its glow on the stone)
    for y in (8, 19, 29):                                  # weathering: chips out of its edges
        rgb[y, 8 - (4 if y < 16 else 5)] = SANDSTONE[3]; rgb[y + 1, 7 + (4 if y < 16 else 5)] = SANDSTONE[4]
    return rgb, a

def stairs(rows=3):
    """steps cut down through the cliff, 32 wide and 48 tall (the rock top's last row and the face's two rows) (user
    2026-11-24, on mock v2's rope ladders: "replace it with actual stairs like you have inside of Mt. Mirroh or other
    maps"): six steps as MonoMyth's stone stairs are drawn (broad light treads, a narrow riser in shade under each, a
    bright nosing on each tread's front), in the canyon's sandstone; the cut's two cheeks in the face's shade"""
    TREAD, NOSE, RISER, SHADE = (236, 186, 136), (252, 214, 166), (196, 136, 100), (150, 92, 74)
    CHEEK, CHEEK_D, EDGE = (184, 120, 92), (150, 90, 72), (96, 48, 44)
    Hh = rows * 16; out = np.zeros((Hh, 32, 3), np.uint8)
    rnd = random.Random(4)
    for y in range(Hh):
        r = y % 8
        c = NOSE if r == 0 else TREAD if r <= 4 else RISER if r <= 6 else SHADE
        out[y, :] = c
        if r in (1, 2, 3, 4):                                # (grain in the treads)
            for x in range(4, 28):
                if rnd.random() < 0.06: out[y, x] = RISER if rnd.random() < 0.5 else NOSE
    out[:, 0:3] = CHEEK; out[:, 29:32] = CHEEK_D; out[:, 3] = EDGE; out[:, 28] = EDGE
    for y in range(0, Hh, 8): out[y + 7, 0:3] = CHEEK_D; out[y + 7, 29:32] = EDGE      # (the cheeks' courses)
    return out

def pink_mask(Hp, Wp):
    """the pink sand: a soft round field round the arrival ring, its edge dithered into the sand as MonoMyth's darker
    sand patches are (a checkerboard thinning out), its outline wandering"""
    pk = P.PINK; yy, xx = np.mgrid[0:Hp, 0:Wp]
    cx, cy = (pk['cx'] + 0.5) * S, (pk['cy'] + 0.5) * S
    ang = np.arctan2(yy - cy, xx - cx)
    rr = 1 + 0.07 * np.sin(3 * ang + 1.0) + 0.05 * np.sin(5 * ang + 2.0) + 0.03 * np.sin(9 * ang)
    d = np.sqrt(((xx - cx) / (pk['rx'] * S)) ** 2 + ((yy - cy) / (pk['ry'] * S)) ** 2) / rr
    chk = (xx + yy) % 2 == 0; chk4 = (xx % 2 == 0) & (yy % 2 == 0)
    return (d <= 0.86) | ((d <= 0.94) & chk) | ((d <= 1.0) & chk4)

def palm():
    """MonoMyth's desert palm (Sandwell's, its map 0x869708 at about cells 4-5, 32-34), cut from its sand; its shadow
    on the sand recoloured to the canyon's sand; 32 wide (centred on its cell), 48 tall"""
    from scipy.ndimage import label
    img = PS.src(DESERT)[0]
    c = img[512 - 16:560, 64 - 16:96].copy()              # (48 tall, 48 wide: the palm and its shadow)
    sand = {tuple(int(v) for v in p) for p in img[496:512, 48:112].reshape(-1, 3)} | \
           {tuple(int(v) for v in p) for p in img[496:576, 48:58].reshape(-1, 3)}
    a = np.array([[tuple(int(v) for v in p) not in sand for p in row] for row in c])
    lab, n = label(a)
    a = lab == 1 + int(np.argmax(np.bincount(lab.ravel())[1:]))
    sh = (c == (144, 128, 80)).all(-1); c[sh] = (206, 154, 104)
    ys, xs = np.nonzero(a); cx = (xs.min() + xs.max()) // 2
    x0 = max(0, cx - 16); c = c[:, x0:x0 + 32]; a = a[:, x0:x0 + 32]
    return c, a

def compose():
    cls, g, rep = terrain()
    P.EXTRA_SOLID = set()
    placed = scatter(cls, g)
    bad = T.seams(g)
    img = T.render(g); H, W = g.shape
    top = np.zeros_like(img); top_a = np.zeros((H * S, W * S), bool)
    def put(rgb, a, x, y, top_rows=0, dx=0):
        h, w = a.shape
        for py in range(h):
            Y = y * S + py
            if not (0 <= Y < H * S): continue
            row_a = a[py]; X0 = x * S + dx
            if py < top_rows * S: top[Y, X0:X0 + w][row_a] = rgb[py][row_a]; top_a[Y, X0:X0 + w] |= row_a
            else: img[Y, X0:X0 + w][row_a] = rgb[py][row_a]
    # ---- the sky and the mesa's rim (v1's, the Peak's way): the land cut round smooth, a dark outline, a stone lip
    sky_a = np.zeros((H * S, W * S), bool)
    for y in range(H):
        for x in range(W):
            if P.G[y, x] == 'K': sky_a[y * S:y * S + S, x * S:x * S + S] = True; img[y * S:y * S + S, x * S:x * S + S] = (164, 30, 28)
    yy, xx = np.mgrid[0:13 * S, 0:W * S]
    out_oval = ~P.in_land(xx / S - 0.5, yy / S - 0.5)
    img[:13 * S][out_oval] = (164, 30, 28); sky_a[:13 * S] |= out_oval
    from scipy.ndimage import gaussian_filter, distance_transform_edt
    TR = 15 * S; land = ~sky_a[:TR]
    cut = land & ~(gaussian_filter(land.astype(float), 2.5) > 0.5)
    sub = img[:TR]; sub[cut] = (164, 30, 28); sky_a[:TR] |= cut
    dist = distance_transform_edt(land & ~cut)
    rock = np.tile(T.corpus().meta[0x20C], (TR // S + 1, W, 1))[:TR, :W * S]
    for d in range(1, 9):
        m = (land & ~cut) & (dist > d - 1) & (dist <= d)
        if d == 1: sub[m] = (44, 14, 16)
        elif d <= 7: sub[m] = (rock[m].astype(int) * (0.8 if d == 2 else 1.0)).astype(np.uint8)
        else: sub[m] = (150, 70, 50)
    # ---- the rope bridge, the rope ladders, the carved panels
    n = P.BRIDGE['y1'] - P.BRIDGE['y0'] + 1
    img[P.BRIDGE['y0'] * S:(P.BRIDGE['y1'] + 1) * S, 24 * S:26 * S] = PS.bridge(n)
    for L in P.LADDERS:                                    # (from the rock top's last row down through the face to the ground)
        y1 = L['y']
        while y1 + 1 < H and P.G[y1 + 1, L['x']] == '#': y1 += 1
        img[(L['y'] - 1) * S:(y1 + 1) * S, L['x'] * S:(L['x'] + 2) * S] = stairs(y1 - L['y'] + 2)
    for k, (x, y) in enumerate(P.PANELS): img[y * S:(y + 2) * S, x * S:(x + 2) * S] = PS.panel(k)
    # ---- the pink crystal sand round the arrival, soft-edged, gems glinting in it
    pm = pink_mask(H * S, W * S) & np.isin(np.repeat(np.repeat(cls, S, 0), S, 1), ['F', 'r'])
    img[pm] = PS.pink_sand(img[pm][None])[0]
    rnd = random.Random(5); ys, xs = np.nonzero(pm)
    for i in rnd.sample(range(len(ys)), 40):
        y, x = ys[i], xs[i]
        if 1 <= y < H * S - 1 and 1 <= x < W * S - 1 and pm[y - 1:y + 2, x - 1:x + 2].all(): PS.gem(img, x, y)
    # ---- the dragon: the skull, the spine (knuckles, dorsal spikes on the top layer), the ribs, stubs, the claw
    rgb, a = PS.skull(); put(rgb, a, *P.SKULL)
    pts = [(x * S + 8, y * S + 9) for (x, y) in P.SPINE]
    path = []
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        m = int(max(abs(bx - ax), abs(by - ay)))
        for t in range(m): path.append((ax + (bx - ax) * t / m, ay + (by - ay) * t / m))
    yy, xx = np.mgrid[0:H * S, 0:W * S]
    for k, (px, py) in enumerate(path[::9]):
        cx_, cy_ = int(px) // S, int(py) // S
        if (cx_, cy_) in P.SPINE_GAP: continue
        reg = (slice(max(0, int(py) - 24), int(py) + 6), slice(max(0, int(px) - 8), int(px) + 9))
        Y, X = yy[reg], xx[reg]
        knuckle = ((X - px) / 6.5) ** 2 + ((Y - py) / 4.8) ** 2 <= 1
        Ln = 8 + (k * 7) % 9
        spike = (abs(X - px - (py - Y) * 0.15) <= np.maximum(0, (Y - (py - 4 - Ln)) * 0.22)) & (Y <= py - 3) & (Y >= py - 4 - Ln)
        bone = knuckle | spike
        col = np.zeros(X.shape + (3,), np.uint8); col[bone] = PS.BONE[1]
        col[knuckle & (Y < py - 1)] = PS.BONE[0]; col[knuckle & (Y > py + 2)] = PS.BONE[2]
        col[spike & (X > px + 0.5)] = PS.BONE[2]
        e = bone & (~np.roll(bone, 1, 0) | ~np.roll(bone, -1, 0) | ~np.roll(bone, 1, 1) | ~np.roll(bone, -1, 1))
        col[e] = PS.BONE[4]
        ground = bone & ((Y // S) == cy_); over = bone & ((Y // S) < cy_)
        img[reg][ground] = col[ground]; top[reg][over] = col[over]; top_a[reg] |= over
    for R in P.RIBS:                                       # (three identical ribs: one width, feet in the same columns)
        rgb, a = PS.arch(P.RIB_X[1] - P.RIB_X[0] - 1); put(rgb, a, P.RIB_X[0], R['y'] - 1, top_rows=2)
    for k, (x, y) in enumerate(P.RIB_STUBS + P.CLAW):
        rgb, a = PS.spike(k, tall=k < len(P.RIB_STUBS))
        put(rgb, a, x, y - (1 if a.shape[0] > S else 0), top_rows=1 if a.shape[0] > S else 0)
    # ---- the obelisks, the altars, palms, cacti
    for (x, y) in P.OBELISKS_SOUTH + P.OBELISKS_NORTH:
        rgb, a = obelisk(); put(rgb, a, x, y - 2, top_rows=2)
    for A in P.ALTARS: rgb, a = PS.altar(north=A['north']); put(rgb, a, A['x'], A['y'])
    prgb, pa = palm()
    for (x, y) in P.PALMS: put(prgb, pa, x, y - 2, top_rows=2, dx=-8)
    C = T.corpus(); sand = C.meta[0x24B].astype(int)
    for k, (x, y) in enumerate(P.CACTI):
        t = C.meta[(0x230, 0x231, 0x239)[k % 3]]; msk = np.abs(t.astype(int) - sand).sum(-1) > 40
        b = img[y * S:y * S + S, x * S:x * S + S]; b[msk] = t[msk]
    return dict(bottom=img, top=top, top_a=top_a, sky_a=sky_a, grid=g, cls=cls, report=rep, seams=bad, props=placed)

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
    r = compose()
    print('unseen neighbourhoods:', len(r['report']['unseen']), '| conflicts:', len(r['report']['conflicts']),
          '| seams:', len(r['seams']), '| props:', len(r['props']))
    flat = r['bottom'].copy(); flat[r['top_a']] = r['top'][r['top_a']]
    Image.fromarray(flat).save(os.path.join(out, 'slip_flat.png'))
    Image.fromarray(T.seam_map(T.render(r['grid']), r['seams'])).save(os.path.join(out, 'slip_seams.png'))
