"""Mt. Mirroh B1F, art mock v2: the Blast Crater (plan_b1f4.py).

Terrain: MonoMyth's Mt. Thunder interiors, solved (mtcorpus.py + tilesolve.py), open floor fixed to its plain floor.
Set pieces and where they come from:
  * the pit, drawn as Lazarus draws its blast pit (facf4c: its far wall lit in a band, falling away into the dark),
    in Mt. Thunder's colours; at its bottom, faint, the violet of the wound;
  * the cracked floor: Lazarus' crack decal (one decal, flipped four ways, as Lazarus scatters it), denser near the pit;
  * the altar: Rejuvenation's cracked stone table slab (Arceus ruins), tipped over the north lip, a second block
    gone half over;
  * the pillar ring: Rejuvenation's violet temple pillars (Arceus ruins): three standing, seven snapped to stumps,
    their shafts thrown down outward; Mt. Thunder's boulder piles as their rubble;
  * the rim: the temple's terrace, dressed flagstones (painted in the cave's stone), some lifted, some gone; its
    facade along the back wall face on, Rejuvenation's temple wall, broken through;
  * the camp (as mock v1), the ladder (Crown's), 1F's glass-ice crystals round the cavern's edge, a few violet
    Dreamstone splinters on the pit's lip (Rejuvenation's violet crystal, small).
Credits: MonoMyth, Lazarus, Rejuvenation, Crown, Odyssey (the camp's barrel).
Usage: python3 compose_b1f4.py OUTDIR"""
import os, sys, random, math
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'ancient_cormoria')); sys.path.insert(0, os.path.join(HERE, '..', 'cave'))
import tilesolve as T
import mtcorpus as MC
import plan_b1f4 as P
import compose_b1f as V1
from compose_b1f import png, Canvas, recolour, jag, deepen, STONE, VIO, S
W, H, G = P.W, P.H, P.G
blk = lambda x, y: (slice(y * S, y * S + S), slice(x * S, x * S + S))
R = 'assets/rejuvenation/pieces/ruins/%s.png'
LAV = [(200, 204, 224), (166, 170, 196), (130, 134, 164), (94, 96, 128), (54, 54, 80)]   # (slate: the pillars recoloured)

def terrain():
    cls = np.full(G.shape, 'F', dtype='<U1'); cls[np.isin(G, ['#', 'w', 'F'])] = 'W'; cls[G == 'S'] = 'S'
    C = MC.corpus(); fixed = {}
    for y in range(1, H - 1):
        for x in range(1, W - 1):
            if (cls[y - 1:y + 2, x - 1:x + 2] == 'F').all(): fixed[(x, y)] = 0x209
    g, rep = T.solve(cls, fixed=fixed, C=C); return cls, g, rep

# ------------------------------------------------------------------------------------------------------------ pieces
def pit(img):
    """the pit, over its 'P' cells: a chamfered hole; its far (north) wall a lit band of the cave's stone falling into
    the dark by a dither (as Lazarus' pit), its sides and near lip edged; the depth dark, violet faint at the bottom"""
    m = np.repeat(np.repeat(G == 'P', S, 0), S, 1)
    Hh, Ww = m.shape
    # chamfer the corners: cut a triangle off each corner cell of the hole
    ys, xs = np.nonzero(m)
    yy, xx = np.mgrid[0:Hh, 0:Ww]
    cut = np.zeros_like(m)
    for (cy, cx) in np.argwhere(G == 'P'):
        for (dy, dx) in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            if G[cy + dy, cx] != 'P' and G[cy, cx + dx] != 'P':
                y0, x0 = cy * S, cx * S
                ly = yy[y0:y0 + S, x0:x0 + S] - y0; lx = xx[y0:y0 + S, x0:x0 + S] - x0
                fy = ly if dy < 0 else S - 1 - ly; fx = lx if dx < 0 else S - 1 - lx
                cut[y0:y0 + S, x0:x0 + S] |= (fx + fy) < 9
    m &= ~cut
    deep = np.array((22, 22, 40)); face = [(150, 160, 190), (120, 128, 160), (96, 102, 134), (70, 74, 104)]
    out = img.copy()
    top = np.full(Ww, 10 ** 6)
    for x in range(Ww):
        c = np.nonzero(m[:, x])[0]
        if len(c): top[x] = c[0]
    for x in range(Ww):
        c = np.nonzero(m[:, x])[0]
        if not len(c): continue
        y0 = c[0]
        for y in c:
            d = y - y0
            if d < 2: col = face[0]
            elif d < 6: col = face[1]
            elif d < 11: col = face[2] if (d != 8) else face[3]
            elif d < 15: col = face[3] if ((x + y) % 2 == 0 or d < 13) else deep
            elif d < 17: col = face[3] if ((x + y) % 4 == 0) else deep
            else: col = deep
            out[y, x] = col
    # the sides and the near lip: a dark outline on the hole's edge, a light lip on the floor just south of it
    e = m & ~(np.roll(m, 1, 0) & np.roll(m, -1, 0) & np.roll(m, 1, 1) & np.roll(m, -1, 1))
    out[e] = (34, 34, 56)
    lip = np.roll(m, 1, 0) & ~m
    out[lip] = (196, 206, 228)
    out[np.roll(lip, 1, 0) & ~m] = (np.array(out[np.roll(lip, 1, 0) & ~m], float) * 0.85).astype(np.uint8)
    # the wound: violet, faint, deep
    cyc, cxc = (np.mean(ys) + 14), np.mean(xs)
    dd = np.sqrt(((xx - cxc) / 70.0) ** 2 + ((yy - cyc) / 30.0) ** 2)
    glow = m & (dd < 1) & (yy > top[np.clip(xx, 0, Ww - 1)] + 18)
    k = np.clip(1 - dd, 0, 1)[..., None] * 0.55
    out = np.where(glow[..., None], out * (1 - k) + np.array(VIO[1]) * k, out).astype(np.uint8)
    rnd = random.Random(4)
    for _ in range(18):
        y, x = int(cyc + rnd.gauss(0, 6)), int(cxc + rnd.gauss(0, 26))
        if 0 <= y < Hh and 0 <= x < Ww and glow[y, x]: out[y, x] = VIO[3] if rnd.random() < 0.7 else VIO[4]
    return out, m

def crack_decals():
    a = np.load(os.path.join(V1.ROOT, 'assets/lazarus_reference/crack_decal.npy'))
    return [a, a[:, ::-1], a[::-1], a[::-1, ::-1]]

def cracks(img, rnd):
    """Lazarus' crack decal on the cracked floor (likelier near the pit), a few further out"""
    dec = crack_decals(); out = img.copy()
    for y in range(H):
        for x in range(W):
            d = math.hypot((x - P.CX) / 9.6, (y - P.CY) / 6.6)
            p = 0.6 if G[y, x] == 'k' and d < 0.8 else 0.38 if G[y, x] == 'k' else 0.12 if (G[y, x] == '.' and d < 1.35) else 0
            if rnd.random() < p:
                m = dec[rnd.randrange(4)]; sl = blk(x, y); t = out[sl]
                t[m == 2] = (104, 112, 146); t[m == 1] = (58, 62, 92); out[sl] = t
    return out

def pillar(kind, rnd):
    """Rejuvenation's violet pillar: 'p' standing (its capital, shaft, plinth: 52 px), 'b' a stump, jagged"""
    rgb, a = png(R % 'column_tall')
    rows = np.nonzero(a.any(1))[0]; rgb, a = rgb[rows[0]:rows[-1] + 1], a[rows[0]:rows[-1] + 1]
    rgb = recolour(rgb, a, LAV)
    if kind == 'p':
        rgb = np.concatenate([rgb[:18], rgb[-34:]]); a = np.concatenate([a[:18], a[-34:]])
        return rgb.copy(), a.copy()
    h = rnd.randint(20, 27); rgb, a = rgb[-h:].copy(), a[-h:].copy()
    return jag(rgb, a, rnd.randrange(99), 0, 5, edge=LAV[4])

def shaft(vertical, L, rnd):
    """a pillar's shaft thrown down: the pillar's panelled shaft on its side (or lengthways), both ends broken"""
    rgb, a = png(R % 'column_tall')
    rows = np.nonzero(a.any(1))[0]; rgb, a = rgb[rows[0] + 18:rows[0] + 18 + L].copy(), a[rows[0] + 18:rows[0] + 18 + L].copy()
    rgb = recolour(rgb, a, LAV)
    rgb, a = jag(rgb, a, rnd.randrange(99), 0, 4, edge=LAV[4]); rgb, a = jag(rgb, a, rnd.randrange(99), 0, 4, edge=LAV[4], side='bottom')
    if not vertical: rgb, a = np.rot90(rgb, 1).copy(), np.rot90(a, 1).copy()
    return rgb, a

def flagstones(img, rnd):
    """the rim's dressed floor: 16x16 flags in the cave's stone, joints dark, some cracked, a few lifted or gone"""
    out = img.copy(); base = [(178, 186, 206), (164, 172, 194), (150, 158, 182)]
    for (y, x) in np.argwhere(G == 'D'):
        if rnd.random() < 0.10: continue                                   # (gone: the cave floor shows)
        sl = blk(x, y); t = np.zeros((S, S, 3), np.uint8); t[:] = base[rnd.randrange(3)]
        t[0, :] = (210, 216, 232); t[:, 0] = (196, 202, 222)
        t[-1, :] = (92, 96, 124); t[:, -1] = (110, 114, 140)
        if rnd.random() < 0.3:                                            # (a crack across it)
            yy = rnd.randrange(3, 12)
            for xx in range(1, S - 1):
                yy = min(S - 2, max(1, yy + rnd.choice((-1, 0, 0, 1)))); t[yy, xx] = (92, 96, 124)
        if rnd.random() < 0.08: t[2:-2, 2:-2] = (np.array(t[2:-2, 2:-2], float) * 0.85).astype(np.uint8)   # (sunk)
        out[sl] = t
    return out

def facade(cv, rnd):
    """the temple's facade along the back of the rim (row 3, face on): Rejuvenation's temple wall, its courses and its
    posts, run along; broken down to different heights, breached twice, rubble at its foot"""
    tw, ta = png('assets/rejuvenation/pieces/temple_wall.png')
    seg, sa = tw[21:56, 8:56], ta[21:56, 8:56]              # (caps + brick, 48 x 35)
    post, pa = tw[18:56, 0:8], ta[18:56, 0:8]
    x0, x1 = 11 * S - 4, 30 * S + 4; Yb = 4 * S          # (its foot on the rim's floor)
    X = x0; k = 0
    while X < x1:
        w = min(48, x1 - X)
        r_, a_ = seg[:, :w].copy(), sa[:, :w].copy()
        lo, hi = ((0, 6), (6, 16), (0, 8), (12, 24), (2, 10), (0, 6), (8, 18))[k % 7]
        r_, a_ = jag(r_, a_, 30 + k, lo, hi)
        if k in (1, 4):                                     # the breaches: down to the footing in the middle
            a_[:30, 14:34] = False
            r_[30, 14:34] = (54, 52, 70)
        cv.put(r_, a_, X, Yb - r_.shape[0], foot=Yb)
        p_, pa_ = jag(post, pa, 60 + k, 0, 3 + (k % 3) * 4)
        cv.put(p_, pa_, X - 4, Yb - p_.shape[0] + 3, foot=Yb)
        X += 48; k += 1
    p_, pa_ = jag(post, pa, 99, 0, 6); cv.put(p_, pa_, x1 - 4, Yb - p_.shape[0] + 3, foot=Yb)
    sm, sma = png(R % 'pebbles'); sma[:2] = False; sm = recolour(sm, sma, STONE[1:])
    for xx in (14, 19, 24, 27): cv.put(sm, sma, xx * S + rnd.randrange(-4, 4), 4 * S + rnd.randrange(0, 6), layer='bottom')

def altar(cv):
    """what is left of the altar: its cracked table slab, thrown back onto the pit's north lip"""
    rgb, a = png(R % 'cracked_long')
    cv.put(rgb, a, 18 * S + 8, 17 * S - 10, foot=17 * S + 12)

def ring(cv, rnd, C):
    for k, (x, y, a) in enumerate(P.RING):
        kind = 'p' if k in P.STANDING else 'b'
        rgb, al = pillar(kind, rnd)
        cv.put(rgb, al, x * S, (y + 1) * S - rgb.shape[0], foot=(y + 1) * S - 4)
        if kind == 'p': continue
        cells = [q for q in P.SHAFTS[[i for i, (xx, yy, aa) in enumerate(P.RING) if i not in P.STANDING].index(k)]
                 if G[q[1], q[0]] == 'f']
        if not cells: continue
        L = 14 * len(cells) + 4
        rgb, al = shaft(False, L, rnd)
        cx = (min(q[0] for q in cells) * S + (max(q[0] for q in cells) + 1) * S) // 2
        cy = cells[0][1] * S + S // 2
        cv.put(rgb, al, cx - rgb.shape[1] // 2, cy - rgb.shape[0] // 2 + 2, foot=cy + 10)

def compose(seed=11):
    rnd = random.Random(seed); C = MC.corpus()
    cls, g, rep = terrain()
    img = T.render(g, C=C)
    for (y, x) in np.argwhere(G == 'r'): img[blk(x, y)] = C.meta[(0x205, 0x20F)[(x + y) % 2]]
    img = flagstones(img, rnd)
    img = cracks(img, rnd)
    img, pm = pit(img)
    img = deepen(img, k=0.86)
    cv = Canvas(img)
    facade(cv, rnd)
    ring(cv, rnd, C)
    altar(cv)
    # 1F's glass-ice crystals round the cavern's edge
    import gg, compose_1f as C1
    GV = gg.Vocab()
    sprites = [gg.cutout(GV, mi, b) for mi, b in gg.BIG_CRYSTALS if b[2] - b[0] == 2 and b[3] - b[1] == 2]
    for k, (x, y) in enumerate(((5, 13), (35, 15), (36, 25), (4, 24), (26, 31), (11, 11))):
        rgb, a = sprites[k % len(sprites)]
        X0, Y0 = x * S - S // 2, (y + 1) * S - rgb.shape[0]
        under = cv.flat()[Y0:Y0 + rgb.shape[0], X0:X0 + rgb.shape[1]]
        if under.shape[:2] != a.shape: continue
        cv.put(C1.glass(rgb, a, under, (196, 228, 250)), a, X0, Y0, foot=y * S)
    camp(cv)
    lrgb, la = png('assets/crown_reference/pieces/cave_ladder.png')
    cv.put(lrgb, la, 20 * S, 37 * S - 16, foot=37 * S)
    return dict(cv=cv, cls=cls, grid=g, rep=rep)

def camp(cv):
    """mock v1's camp, moved into the south-west alcove (three rows up, the same pieces)"""
    class Shift:
        def __init__(s, cv): s.cv = cv
        def put(s, rgb, a, X, Y, foot=None, layer='mid'):
            s.cv.put(rgb, a, X, Y - 3 * S, foot=None if foot is None else foot - 3 * S, layer=layer)
    V1.camp(Shift(cv), random.Random(2), None)

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
    r = compose(); C = MC.corpus()
    print('unseen', len(r['rep']['unseen']), 'conflicts', len(r['rep']['conflicts']), 'seams', len(T.seams(r['grid'], C)))
    Image.fromarray(r['cv'].flat()).save(os.path.join(out, 'b1f_mock_v2.png'))
