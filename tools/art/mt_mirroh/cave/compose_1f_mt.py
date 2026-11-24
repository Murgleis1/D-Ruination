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
    if ch == 'C': return 'F'
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
            me = cls(x, y)
            nb = [cls(x + dx, y + dy) for dx, dy in mt.N8]
            if me == 'W': nb = ['W' if c == 'S' else c for c in nb]
            m = V.pick(me + ''.join(nb))
            if me == 'W' and m in (0x200, 0x201, 0x202, 0x203):
                # Mt. Thunder's diagonal slope caps (its mountain faces) read as stumps on a cave wall's end: round the
                # band off with its own band ends instead (0x20B open to the west, 0x20C open to the east)
                e, w_ = cls(x + 1, y), cls(x - 1, y)
                m = 0x20C if e != 'W' else 0x20B if w_ != 'W' else mt.BAND
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
    import colorsys
    def wood(t):
        """the bridge's own pixels: the planks, rails and posts (not the pale ground Mt. Thunder draws round them)"""
        a = np.zeros(t.shape[:2], bool)
        for yy in range(S):
            for xx in range(S):
                r, g, b_ = t[yy, xx] / 255.0; h, sat, v = colorsys.rgb_to_hsv(r, g, b_)
                a[yy, xx] = not (v > 0.62 and sat < 0.30)
        return a
    for R in P.RAVINES:
        lowest = {}; woodmask = np.zeros((H * S, W * S), bool)
        for i, trio in enumerate(COLS):
            for j, m in enumerate(trio):
                x, y = R['x0'] + i, R['path'] - 1 + j; t = V.meta(m)
                a = wood(t)                                     # wood only; through the walkway's gaps, the water in shade
                if j == 1 and 2 <= i < 6:
                    b = img[blk(x, y)]; b[~a] = (b[~a] * 0.55).astype(np.uint8)
                img[blk(x, y)][a] = t[a]; woodmask[blk(x, y)] |= a
                if 2 <= i < 6:
                    for xx in range(S):
                        ys = np.nonzero(a[:, xx])[0]
                        if len(ys): lowest[x * S + xx] = max(lowest.get(x * S + xx, 0), y * S + ys[-1])
        # its shadow on the water: straight below the wood, soft, fading over a tile and a half
        Y0 = min(lowest.values()) - 3                     # one even shadow line under the deck, behind the rail's posts
        for X in lowest:
            for k in range(0, 30):
                Y = Y0 + k
                if woodmask[Y, X]: continue
                f = 0.64 + 0.36 * (max(0, k - 4) / 25.0); img[Y, X] = (img[Y, X] * min(1.0, f)).astype(np.uint8)
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
    # the crystal maze ('C' blocks) and the cliffs' free ends (blocks of rock with one rock neighbour): great ice
    # crystals, Mt. Thunder's big snowy boulders, or clusters of ice chunks, so no band just stops in the open
    BOULDER = [[0x200, 0x202], [0x210, 0x212]]
    def rockb(bx, by):
        if not (0 <= bx < 30 and 0 <= by < 30): return True
        return all(G[2 * by + j, 2 * bx + i] in '#AB' for i in (0, 1) for j in (0, 1))
    def openb(bx, by):
        return 0 <= bx < 30 and 0 <= by < 30 and all(G[2 * by + j, 2 * bx + i] in '.,;C' for i in (0, 1) for j in (0, 1))
    TIPS = []
    for by in range(30):
        for bx in range(30):
            if not all(G[2 * by + j, 2 * bx + i] == '#' for i in (0, 1) for j in (0, 1)) or (bx, by) in C1.CRYSTAL_BLOCKS: continue
            nr = [rockb(bx + dx, by + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
            no = [openb(bx + dx, by + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
            if sum(nr) == 1 and sum(no) >= 2: TIPS.append((bx, by))
    MAZE = sorted({(x // 2, y // 2) for y in range(H) for x in range(W) if G[y, x] == 'C'})
    rkind = random.Random(seed + 5)
    def put_sprite(rgb, a, X0, Y0, foot):
        for yy in range(rgb.shape[0]):
            Y = Y0 + yy; lay, la = (mid, mid_a) if Y >= foot else (top, top_a); row = a[yy]
            if not (0 <= Y < H * S): continue
            lay[Y, X0:X0 + rgb.shape[1]][row] = rgb[yy][row]; la[Y, X0:X0 + rgb.shape[1]] |= row
    def boulder(bx, by):
        for j in (0, 1):
            for i in (0, 1):
                x, y = 2 * bx + i, 2 * by + j; img[blk(x, y)] = floor
                t = V.meta(BOULDER[j][i]); a = ~(t == floor).all(2); mid[blk(x, y)][a] = t[a]; mid_a[blk(x, y)] |= a
    def crystal(bx, by, k):
        rgb, a = sprites[k % len(sprites)]
        X0, Y0 = 2 * bx * S - S // 2, 2 * by * S + 2 * S - rgb.shape[0]
        g = C1.glass(rgb, a, img[Y0:Y0 + rgb.shape[0], X0:X0 + rgb.shape[1]], TINT[rkind.choice(['white', 'white', 'blue'])])
        put_sprite(g, a, X0, Y0, 2 * by * S)
    def cluster(bx, by):
        for (i, j) in ((0, 0), (1, 0), (0, 1), (1, 1)):
            x, y = 2 * bx + i, 2 * by + j
            t = small[rkind.randrange(len(small))]; a = ~(t == f200).all(2)
            g = C1.glass(t, a, img[blk(x, y)], TINT[rkind.choice(['white', 'blue'])]); mid[blk(x, y)][a] = g[a]; mid_a[blk(x, y)] |= a
    small = [GV.meta(m) for m in gg.SMALL_CRYSTALS]; f200 = GV.meta(0x200)
    for (bx, by) in TIPS:
        for j in (0, 1):
            for i in (0, 1): img[blk(2 * bx + i, 2 * by + j)] = floor
        (boulder if rkind.random() < 0.6 else (lambda a, b: crystal(a, b, rkind.randrange(9))))(bx, by)
    MZS = set(MAZE)
    for n, (bx, by) in enumerate(MAZE):
        r = rkind.random()
        if r < 0.7: crystal(bx, by, n)
        else: boulder(bx, by)
    # between neighbouring crystals of a maze wall, a smaller shard at their feet, so the wall reads as one hedge
    for (bx, by) in MAZE:
        if (bx + 1, by) in MZS:
            x, y = 2 * bx + 1, 2 * by + 1
            t = small[(bx * 7 + by) % len(small)]; a = ~(t == f200).all(2) & (t.max(2) > 110)
            xs_ = np.nonzero(a.any(0))[0]
            if len(xs_):
                sh = S // 2
                g = C1.glass(t, a, img[y * S:(y + 1) * S, x * S + sh:x * S + sh + S], TINT['white'])
                reg = mid[y * S:(y + 1) * S, x * S + sh:x * S + sh + S]; ra = mid_a[y * S:(y + 1) * S, x * S + sh:x * S + sh + S]
                reg[a] = g[a]; ra |= a
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
                    t = small[rnd.randrange(len(small))]
                    a = ~(t == f200).all(2) & (t.max(2) > 110)          # the crystal only (not the Grotto's dark floor)
                    g = C1.glass(t, a, img[blk(x, y)], TINT[rnd.choice(['white', 'white', 'blue'])])
                else:
                    t = V.meta(rnd.choice(MTPROPS)); a = ~(t == floor).all(2); g = t
                mid[blk(x, y)][a] = g[a]; mid_a[blk(x, y)] |= a; chunks.add((x, y))
    # ---- dressing (user 2026-11-24: "way too much open space overall everywhere"): groups of rocks, ice crystals and
    # stalagmites across the open floors (solid), and patches of glassy ice and snow (walkable). A corridor along the
    # route is kept clear (the shortest way between its stops, a tile either side), and after every piece every open
    # cell must still be reachable, so nothing walls off a pocket.
    from collections import deque
    def walkable(x, y):
        if not (0 <= x < W and 0 <= y < H): return False
        ch = G[y, x]
        return ch in '.,;AB=' and (x, y) not in C1.CRYSTAL_CELLS and (x, y) not in chunks and (x, y) not in DRESS
    LV = dict(C1.LEVEL, **{'=': 3})
    def bfs(start, goal=None):
        prev = {start: None}; q = deque([start])
        while q:
            p = q.popleft()
            if p == goal: break
            x, y = p; e = LV.get(G[y, x], 3)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (x + dx, y + dy)
                if n in prev or not walkable(*n): continue
                ne = LV.get(G[n[1], n[0]], 3)
                if e and ne and e != ne: continue
                prev[n] = p; q.append(n)
        return prev
    DRESS = set(); DRESS_DECOR = set()
    ROUTE = [(55, 57), (41, 43), (42, 31), (33, 31), (26, 27), (17, 27), (10, 18), (10, 15), (38, 10), (38, 7), (4, 3),
             (50, 6), (54, 2)]
    keep = set()
    for a, b_ in zip(ROUTE, ROUTE[1:]):
        prev = bfs(a, b_); p = b_
        while p:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1): keep.add((p[0] + dx, p[1] + dy))
            p = prev[p]
    for sx, sy in P.SPOTS.values():
        for dx in range(-2, 3):
            for dy in range(-2, 3): keep.add((sx + dx, sy + dy))
    all_open = lambda: {(x, y) for y in range(H) for x in range(W) if walkable(x, y)}
    def ok_to_fill(cells):
        for c in cells:
            if c in keep or not walkable(*c) or G[c[1], c[0]] not in '.,;' or ids.get(c) != mt.FLOOR or c in PATCH: return False
            if 42 <= c[0] <= 57 and 10 <= c[1] <= 39: return False     # the crystal maze and its nook: dressed already
        return True
    def still_connected(cells):
        for c in cells: DRESS.add(c)
        reach = bfs((55, 57)); opened = all_open()
        good = opened <= set(reach) | {p for p in opened if G[p[1], p[0]] in 'AB'}
        if not good:
            for c in cells: DRESS.discard(c)
        return good
    drnd = random.Random(seed + 11)
    def place_boulder(x, y):
        for j in (0, 1):
            for i in (0, 1):
                t = V.meta(BOULDER[j][i]); a = ~(t == floor).all(2); mid[blk(x + i, y + j)][a] = t[a]; mid_a[blk(x + i, y + j)] |= a
    def place_crystal(x, y):
        rgb, a = sprites[drnd.randrange(len(sprites))]
        X0, Y0 = x * S - S // 2, (y + 2) * S - rgb.shape[0]
        g = C1.glass(rgb, a, img[Y0:Y0 + rgb.shape[0], X0:X0 + rgb.shape[1]], TINT[drnd.choice(['white', 'white', 'blue'])])
        put_sprite(g, a, X0, Y0, y * S)
    def place_one(x, y, m):
        t = V.meta(m); a = ~(t == floor).all(2); mid[blk(x, y)][a] = t[a]; mid_a[blk(x, y)] |= a
    def place_chunk(x, y):
        t = small[drnd.randrange(len(small))]; a = ~(t == f200).all(2) & (t.max(2) > 110)
        g = C1.glass(t, a, img[blk(x, y)], TINT[drnd.choice(['white', 'blue'])]); mid[blk(x, y)][a] = g[a]; mid_a[blk(x, y)] |= a
    KINDS = [('crystal', 2, 2, place_crystal, 4), ('boulder', 2, 2, place_boulder, 3), ('rock', 1, 1, lambda x, y: place_one(x, y, 0x205), 3),
             ('stalagmite', 1, 1, lambda x, y: place_one(x, y, 0x20F), 3), ('chunk', 1, 1, place_chunk, 3)]
    cands = [(x, y) for y in range(H) for x in range(W) if (x, y) not in keep and walkable(x, y) and G[y, x] in '.,;']
    drnd.shuffle(cands); groups = 0; placed = 0
    for cx, cy in cands:
        if groups >= 34: break
        if not any(cls(cx + dx, cy + dy) == 'W' for dx in (-1, 0, 1) for dy in (-1, 0, 1)): continue   # by a wall, as Mt. Thunder sets them
        if any(abs(cx - a) + abs(cy - b_) < 4 for a, b_ in DRESS): continue
        n = 0
        for _ in range(drnd.randint(2, 4)):
            kind = drnd.choices(KINDS, [k[4] for k in KINDS])[0]
            x, y = cx + drnd.randint(-1, 1), cy + drnd.randint(-1, 1)
            cells = [(x + i, y + j) for i in range(kind[1]) for j in range(kind[2])]
            if not ok_to_fill(cells) or any(abs(c[0] - d[0]) <= 0 and abs(c[1] - d[1]) <= 0 for c in cells for d in DRESS): continue
            if not still_connected(cells): continue
            kind[3](x, y); n += 1; placed += 1
        if n: groups += 1
    # centrepieces where the floor is still widest: a great crystal with boulders or rocks round it
    from scipy import ndimage as nd
    for _ in range(10):
        openm = np.zeros((H, W), bool)
        for y in range(H):
            for x in range(W): openm[y, x] = walkable(x, y) and G[y, x] in '.,;'
        dist = nd.distance_transform_cdt(np.pad(openm, 1), metric='chessboard')[1:-1, 1:-1]
        cand = sorted(((dist[y, x], (x, y)) for y in range(H) for x in range(W) if dist[y, x] >= 3 and (x, y) not in keep
                       and not (42 <= x <= 57 and 10 <= y <= 39)), reverse=True)
        done = False
        for _d, (cx, cy) in cand:
            cells = [(cx, cy), (cx + 1, cy), (cx, cy + 1), (cx + 1, cy + 1)]
            if not ok_to_fill(cells) or not still_connected(cells): continue
            place_crystal(cx, cy); placed += 1
            for (ox, oy, m) in ((-1, 1, 0x205), (2, 1, 0x20F), (2, 0, 0x205)):
                c = (cx + ox, cy + oy)
                if ok_to_fill([c]) and still_connected([c]): place_one(c[0], c[1], m); placed += 1
            done = True; break
        if not done: break
    # walkable patches: glassy ice and snow, in the open
    for _ in range(40):
        x, y = drnd.randrange(2, W - 6), drnd.randrange(2, H - 6)
        rx, ry = drnd.uniform(1.4, 2.6), drnd.uniform(0.9, 1.5)
        cells_ = [(x + i, y + j) for j in range(-2, 3) for i in range(-3, 4)
                  if ((i * S) / (rx * S)) ** 2 + ((j * S) / (ry * S)) ** 2 <= 1.6]
        def fine(c):
            return (0 <= c[0] < W and 0 <= c[1] < H and ids.get(c) == mt.FLOOR and G[c[1], c[0]] in '.,;' and c not in PATCH
                    and c not in DRESS and all(cls(c[0] + a_, c[1] + b2) == 'F' for a_ in (-1, 0, 1) for b2 in (-1, 0, 1)))
        if not all(fine(c) for c in cells_): continue
        for (cx_, cy_) in cells_:
            b = img[blk(cx_, cy_)]; yy, xx = np.mgrid[0:S, 0:S]
            d = (((cx_ * S + xx) - x * S) / (rx * S)) ** 2 + (((cy_ * S + yy) - y * S) / (ry * S)) ** 2
            m = d <= 1; sheen = ((cx_ * S + xx + cy_ * S + yy) % 11 < 2)
            b[m] = (b[m] * 0.45 + np.array([170, 214, 244]) * 0.55).astype(np.uint8); b[m & sheen] = (236, 248, 255)
            b[(d > 0.86) & m] = (128, 176, 222)
            DRESS_DECOR.add((cx_, cy_))
    # ---- floor detail (study 2026-11-24: Crown's caves wear trodden trails through their floors; Barbed Cave strews
    # loose stones along its walls; the Grotto's crystal floors glitter)
    from scipy.ndimage import gaussian_filter, binary_dilation
    from scipy import ndimage as nd
    # the trail follows the middle of the floor (a path weighted away from the walls), not the shortest corners
    import heapq
    openm = np.array([[walkable(x, y) for x in range(W)] for y in range(H)])
    dwall = nd.distance_transform_edt(openm)
    def centre_path(a, b_):
        dist = {a: 0}; prev = {a: None}; pq = [(0, a)]
        while pq:
            d0, p = heapq.heappop(pq)
            if p == b_: break
            if d0 > dist[p]: continue
            x, y = p; e = LV.get(G[y, x], 3)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (x + dx, y + dy)
                if not walkable(*n): continue
                ne = LV.get(G[n[1], n[0]], 3)
                if e and ne and e != ne: continue
                c = d0 + 1 + 3.0 / (0.6 + dwall[n[1], n[0]])
                if c < dist.get(n, 1e9): dist[n] = c; prev[n] = p; heapq.heappush(pq, (c, n))
        out = []; p = b_
        while p is not None and p in prev: out.append(p); p = prev[p]
        return out
    trail = np.zeros((H, W), float)
    for a, b_ in zip(ROUTE, ROUTE[1:]):
        for (x, y) in centre_path(a, b_): trail[y, x] = 1
    tm = gaussian_filter(np.kron(trail, np.ones((S, S))), 9)
    tm = tm / max(1e-6, tm.max()) + (gaussian_filter(np.random.default_rng(seed + 3).random(tm.shape), 4) - 0.5) * 0.8
    fm = np.zeros((H * S, W * S), bool)
    for y in range(H):
        for x in range(W):
            if ids.get((x, y)) == mt.FLOOR and G[y, x] in '.,;' and (x, y) not in PATCH: fm[blk(x, y)] = True
    hallsnow = np.zeros_like(fm); hallsnow[44 * S:, 45 * S:] = True
    # (per cell, three strengths: the floor keeps to a few tiles, the GBA's 1024 are finite)
    for y in range(H):
        for x in range(W):
            if not fm[y * S, x * S] or hallsnow[y * S, x * S]: continue
            v = tm[y * S:(y + 1) * S, x * S:(x + 1) * S].mean()
            lvl = 0 if v < 0.38 else 1 if v < 0.55 else 2 if v < 0.75 else 3
            if lvl:
                k = (0.07, 0.13, 0.19)[lvl - 1]; b = img[blk(x, y)]
                b[:] = (b * (1 - k) + np.array([112, 152, 192]) * k).astype(np.uint8)
    # loose stones at the walls' feet (walkable decoration)
    srnd = random.Random(seed + 4)
    STONES = [[(srnd.randint(1, 12), srnd.randint(0, 5), srnd.choice((2, 3))) for _ in range(srnd.randint(1, 3))] for _ in range(4)]
    for y in range(1, H):
        for x in range(W):
            if not (fm[y * S, x * S] and cls(x, y - 1) == 'W') or srnd.random() > 0.35: continue
            for (ox, oy, w_) in STONES[srnd.randrange(4)]:
                px, py = x * S + ox, y * S + oy
                img[py:py + 2, px:px + w_] = (84, 100, 132); img[py, px:px + w_] = (206, 222, 238); img[py + 2, px:px + w_] = (150, 176, 204)
    # the crystal maze's floor glitters (frost stars) and takes a cold tint
    mz = np.zeros_like(fm); mz[16 * S:40 * S, 42 * S:58 * S] = True; mz &= fm
    img[mz] = (img[mz] * 0.86 + np.array([150, 200, 240]) * 0.14).astype(np.uint8)
    GL = [[(srnd.randrange(1, 15), srnd.randrange(1, 15), srnd.random() < 0.3) for _ in range(srnd.randint(1, 3))] for _ in range(4)]
    for y in range(16, 40):
        for x in range(42, 58):
            if not fm[y * S, x * S]: continue
            for (ox, oy, star) in GL[srnd.randrange(4)]:
                Y, X = y * S + oy, x * S + ox
                if star: img[Y - 1:Y + 2, X] = (236, 250, 255); img[Y, X - 1:X + 2] = (236, 250, 255)
                img[Y, X] = (255, 255, 255)
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
            solid[y, x] = ch in '#Rv|rC' or (x, y) in C1.CRYSTAL_CELLS or (x, y) in chunks or (x, y) in DRESS
            if ch == '~': beh[y, x] = C1.MB_OCEAN_WATER
            if ch == 'v': beh[y, x] = C1.MB_JUMP_SOUTH
    xn, yn = C1.EXIT_N; solid[yn, xn - 1] = solid[yn, xn + 1] = True
    solid[yn, xn] = False; beh[yn, xn] = C1.MB_NORTH_ARROW_WARP; elev[yn, xn] = 5
    xs, ys = C1.EXIT_S; solid[ys, xs] = False; beh[ys, xs] = C1.MB_SOUTH_ARROW_WARP; elev[ys, xs] = 3
    return dict(DRESS=DRESS, placed=placed, TIPS=TIPS, solid=solid, beh=beh, elev=elev, bottom=img, mid=mid, mid_a=mid_a, top=top, top_a=top_a, flat=flat, chunks=chunks, ids=ids, missed=getattr(V, 'missed', 0))

if __name__ == '__main__':
    r = compose(); print('unseen patterns:', r['missed'])
    Image.fromarray(r['flat']).save(sys.argv[1] if len(sys.argv) > 1 else '/tmp/m2.png')
