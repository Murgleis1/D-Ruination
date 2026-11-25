"""Hollow Hill's webs, v2 (user 2026-11-24: "I like these webbed rocks and the way the webs cover these trees, so you
may want to study them"; 2026-11-25: go ahead). Studied as whole designs: the user's reference
(assets/hollowhill_reference/webbed_trees_and_rocks_user_ref.png) and MonoMyth's Webbed Woods (its maps 0x86DD40 and
0x86DD5C), where the webbing **drapes round the skirt of each crown** (a lace band following the crown's lower edge,
strands hanging under it), **runs on from crown to crown in a thread at the band's foot**, and comes in **patches**:
whole stretches of a treeline webbed, two and three rows deep where the infestation is worst (round the exits), a few
lone trees webbed between; and Crown 3.25's small cobwebs tucked in the trees. Plus the reference's **webbed rock**: a
boulder half-wrapped in a net of web.
Here, in Hollow Hill's blood red, replacing v1's garlands strung between the crowns:
  * crown_web(): the band round a pine's crown (one pattern for a pine in a woods' column, one for a pine standing
    free: the tiles repeat wherever the shape does);
  * the threads joining neighbouring webbed crowns;
  * boulder(): a boulder of Hollow Hill's stone (2x2 cells), its lower part wrapped in a net of web, its threads
    pegged to the ground; a few placed in the open where they close no way;
  * kept from v1: MonoMyth's big net across the way north, the round web in the dead tree's branches.
Credits: MonoMyth (the webbing), the user's reference."""
import numpy as np
import hh_mock as HM

S = 16
LIGHT, DARK = (150, 34, 40), (100, 18, 26)              # (Hollow Hill's old-blood reds, HM.BLOOD's)
STONE = [(222, 214, 192), (198, 190, 176), (176, 168, 150), (146, 138, 130), (124, 114, 120), (92, 84, 96),
         (58, 50, 64), (30, 24, 36)]                    # (the hill's own stone, light to dark: hh_mock.BONE's)

def crown_web(img, L, x0, t, seed=0, drop=36, rise=8, depth=9):
    """the band round the skirt of the pine at (x0, t) (its left cell, its top row): over its crown only. Drawn the
    same on every pine of a kind and mirror-symmetric (the pine's two halves are mirror images), so its tiles repeat
    and flip: Hollow Hill's tileset has little room"""
    X0, Y0 = x0 * S, t * S
    for dx in range(16):
        u = (dx - 15.5) / 16.5
        yb = int(round(Y0 + drop - rise * u * u)); ytop = yb - depth + int(round(2 * u * u))
        for X in (X0 + dx, X0 + 31 - dx):
            if not (0 <= X < img.shape[1]): continue
            for y in range(max(0, ytop), min(img.shape[0], yb + 1)):
                lum = img[y, X].astype(int) @ (3, 6, 1) / 10
                if lum < 70 and y > ytop + 1: continue
                k = y - ytop
                if k == 0 or (k == depth // 2 and dx % 3 != 1) or (dx % 2 == 0 and (k + dx // 2) % 3 != 0):
                    L[y, X] = (*(LIGHT if (k == 0 or dx % 4 == 0) else DARK), 255)
            if dx % 2 == 0:
                for y in range(yb + 1, min(img.shape[0], yb + 1 + (dx * 7 + 3) % 4)): L[y, X] = (*DARK, 255)

def thread(L, a, b, sag=1.5):
    n = max(2, int(abs(b[0] - a[0]) / 2))
    pts = [(a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n + sag * 4 * (i / n) * (1 - i / n)) for i in range(n + 1)]
    for p, q in zip(pts, pts[1:]): HM._line(L, p, q, LIGHT)

def boulder(seed=0):
    """(rgba 32x32): a boulder of the hill's stone, lit from the upper left, its lower part netted in web"""
    r = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:32, 0:32].astype(float)
    ang = np.arctan2(yy - 18, xx - 16); rad = 13.5 + 1.4 * np.sin(3 * ang + seed) + 0.9 * np.sin(5 * ang + 2 * seed)
    d = np.hypot((xx - 16) / 1.05, (yy - 18) / 0.88)
    m = d <= rad; m[31] = False
    rgb = np.zeros((32, 32, 3), np.uint8)
    nx = (xx - 16) / 15.0; ny = (yy - 18) / 13.0; nz = np.sqrt(np.clip(1 - nx ** 2 - ny ** 2, 0.05, 1))
    lit = (-0.55 * nx - 0.65 * ny + 0.55 * nz) + 0.12 * np.sin(xx * 1.3 + seed) * np.cos(yy * 1.1)   # (a lumpy face)
    idx = np.clip((1.15 - lit) * 3.3 + 1.2, 1, 6.99).astype(int)                    # (the cliffs' darker stone)
    for i in range(1, 7): rgb[m & (idx == i)] = STONE[i]
    for k in range(3):                                                   # cracks
        cx, cy = int(r.integers(8, 24)), int(r.integers(9, 20))
        for j in range(int(r.integers(4, 9))):
            if m[cy, cx]: rgb[cy, cx] = STONE[6]
            cx += int(r.integers(-1, 2)); cy += 1
            if cy > 30: break
    edge = m & ~(np.roll(m, 1, 0) & np.roll(m, -1, 0) & np.roll(m, 1, 1) & np.roll(m, -1, 1))
    rgb[edge] = STONE[7]
    # the net: a jittered grid of knots over the boulder's lower two thirds, each tied to its right and lower neighbour
    L = np.zeros((32, 32, 4), np.uint8)
    knots = {}
    for gy in range(5):                                                  # staggered rows: a mesh of open diamonds
        for gx in range(7):
            x = gx * 5.2 + (2.6 if gy % 2 else 0) + r.uniform(-1.2, 1.2)
            y = 14 + gy * 4.2 + r.uniform(-0.9, 0.9) - 2.5 * np.cos((x - 16) / 16 * 1.5)
            knots[gx, gy] = (x, y)
    for (gx, gy), p in knots.items():
        nb = [knots.get((gx + 1, gy))] if gy == 0 else []
        nb += [knots.get((gx + (gy % 2), gy + 1)), knots.get((gx - 1 + (gy % 2), gy + 1))]
        for q in nb:
            if q is not None and r.random() > 0.12: HM._line(L, p, q, LIGHT if gy < 2 else DARK)
    wm = (L[..., 3] > 0) & m
    rgb[wm] = L[..., :3][wm]
    top = m & (yy < 14)
    sh = np.zeros_like(m); sh[2:, 1:] = m[:-2, :-1]; sh &= ~m                  # (its shadow on the ground)
    out = np.zeros((32, 32, 4), np.uint8); out[..., :3] = rgb; out[m, 3] = 255
    out[sh] = (*STONE[7], 110)
    for px, py in ((3, 30), (29, 29), (16, 31)):                             # threads pegged to the ground
        HM._line(out, (px, py), (min(31, max(0, px + (16 - px) // 3)), 24), (*DARK,))
    out[out[..., 3] == 0, :3] = 0
    return out

# ------------------------------------------------------------------ where
# patches (stretches of a treeline webbed, deeper where it is worst), as MonoMyth hangs them:
#   (kind, columns, rows deep): 'north' woods hang from the top (their front pine lowest), 'south' rise from the bottom
PATCHES = [('north', range(4, 16, 2), 1), ('north', (12, 14), 2),            # west of the way north, worst at the net
           ('north', (20, 22, 24), 2), ('north', (26, 28), 1),             # east of it, round the dead tree
           ('north', range(40, 48, 2), 1),                                 # the north-east pocket
           ('south', range(4, 16, 2), 2), ('south', (16, 18), 1),          # round the clearing (the Eiscue, the 1v2)
           ('south', range(36, 46, 2), 1)]
SIDES = [(2, range(22, 54, 2)), (50, range(26, 36, 2))]                    # the west woods' face, the trees closing the east
BOULDERS = [(9, 44), (45, 12), (25, 37), (38, 16), (21, 23), (32, 53)]        # wanted spots (the nearest free 2x2 is taken)

def place_boulders(M):
    """2x2 webbed boulders in the open: never on a reserved way, never closing a way (connected() checked)"""
    placed = []
    for k, (x0, y0) in enumerate(BOULDERS):
        done = False
        for d in range(7):
            for dx in range(-d, d + 1):
                for dy in range(-d, d + 1):
                    if done or max(abs(dx), abs(dy)) != d: continue
                    x, y = x0 + dx, y0 + dy
                    if not (0 < x < HM.W - 2 and 0 < y < HM.H - 2) or HM.reserved(x, y, 2, 2): continue
                    if any(M.used[y + cy, x + cx] is not None for cy in range(2) for cx in range(2)): continue
                    ring = [M.used[yy, xx] for yy in range(y - 1, y + 3) for xx in range(x - 1, x + 3)]
                    if any(u is not None and u.split(':')[0] in ('cliff', 'stairs', 'door', 'thing', 'road') for u in ring): continue
                    lv = M.E[y:y + 2, x:x + 2]
                    if lv.min() != lv.max() or M.field[y:y + 3, x:x + 3].min() < HM.TOP: continue
                    b = boulder(0)                                    # (one design, mirrored: tiles are short)
                    if k % 4 >= 2: b = b[:, ::-1].copy()               # (two designs, mirrored: the tiles repeat)
                    snap = (M.used.copy(), [[list(c) for c in r] for r in M.over])
                    for cy in range(2):
                        for cx in range(2):
                            M.over[y + cy][x + cx].append((b[cy * S:cy * S + S, cx * S:cx * S + S].copy(), False))
                            M.used[y + cy, x + cx] = 'thing:rock'
                    if HM.connected(M): M.used, M.over = snap; continue
                    placed.append((x, y)); done = True
        if not done: print('no room for a boulder near', x0, y0)
    return placed

def hang_webs2(M, img, seed=4):
    L = np.zeros(img.shape[:2] + (4,), np.uint8)
    units = set(M.units)
    webbed = []
    for kind, cols, deep in PATCHES:
        for x0 in cols:
            col = sorted(t for x, t in units if x == x0 and ((t < 30) if kind == 'north' else (t > 40)))
            if not col: continue
            front = col[-deep:] if kind == 'north' else col[:deep]
            for t in front:
                crown_web(img, L, x0, t, x0 * 97 + t); webbed.append((x0, t))
    for x0, rows in SIDES:
        for t in sorted(t for x, t in units if x == x0 and t in rows):
            if (t // 2) % 3: crown_web(img, L, x0, t, x0 * 97 + t); webbed.append((x0, t))
    # threads from each webbed crown to the next one along at the same height (touching, or across a gap)
    ws = set(webbed)
    for (x0, t) in webbed:
        for gap in (2, 4, 6):
            if (x0 + gap, t) in ws:
                y = t * S + 36; thread(L, (x0 * S + 30, y), ((x0 + gap) * S + 2, y), sag=0.8 if gap == 2 else 2.5); break
    # lone pines: about half webbed, joined to a webbed neighbour level with them
    alone = sorted({tuple(map(int, u[len('tree:pine'):].split(','))) for u in M.used.ravel()
                    if isinstance(u, str) and u.startswith('tree:pine')})
    for i, (x, t) in enumerate(alone):
        if i % 2 == 0: crown_web(img, L, x, t, x * 31 + t, drop=40)
    # kept: the big net across the way north, the round web in the dead tree's branches
    rng = np.random.default_rng(seed)
    HM.orb(L, (23 * 16 + 9, 11 * 16 + 9), 9, [(23 * 16 + 3, 11 * 16 + 2), (23 * 16 + 14, 11 * 16 + 4)], rng, torn=0.3)
    from PIL import Image
    import os
    out = Image.fromarray(L)
    for gx, w, row in HM.NETS:
        net = Image.open(os.path.join(HM.HERE, '..', '..', '..', 'assets', 'monomyth_reference', 'pieces', 'web_net.png')).convert('RGBA')
        a = np.array(net); m = a[..., 3] > 0
        light = (a[..., :3] == (240, 240, 248)).all(-1)
        a[m & light, :3] = HM.WEB_LIGHT; a[m & ~light, :3] = HM.WEB_DARK
        out.alpha_composite(Image.fromarray(a), (gx * 16 + (w * 16 - a.shape[1]) // 2, row * 16 + 2))
    return np.array(out)

def install():
    """hh_mock with the v2 webs: compose() places the boulders, layers() hangs the v2 webs"""
    if getattr(HM, '_webs2', False): return
    _compose = HM.compose
    def compose(seed=5):
        M = _compose(seed); place_boulders(M)
        assert not HM.connected(M), 'a boulder cut a way'
        return M
    HM.compose = compose; HM.hang_webs = hang_webs2; HM._webs2 = True
