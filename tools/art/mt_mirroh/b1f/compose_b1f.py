"""Mt. Mirroh B1F, art mock v1 (plan_b1f2.py; user 2026-11-24: "lets proceed with the design. The rubble needs to look
like a broken set of ruins, so look through the usual games we have (MonoMyth, Crown, Odyssey, Lazarus) for anything
you need to make this map as authentic and strikingly fantastic/beautiful as you can").

The terrain: MonoMyth's Mt. Thunder interiors, solved (mtcorpus.py + tilesolve.py: only its tiles, only pairs it has),
as 1F was built from them; drawn deeper and colder than 1F (this is under the mountain), so the ritual's violet light
carries.
The set pieces, and where they come from:
  * **the altar on its dais** (painted, Ancient Cormorian, the slip's altars' kin): a round stone dais of two tiers
    carved with a ring, on it the altar table split in two, the Dreamstone's socket empty, scorched; **the Vessels
    Cult's sigil** on the dais (Rejuvenation's ritual sigil, credit the Rejuvenation team), burnt in violet;
  * **Mt. Thunder's purple ritual candles** round the dais and the terraces (its own props 0x2f3-0x306, some lit,
    most guttered);
  * **the Leyline fissure**: a crack glowing violet from the altar south down the stairs and across the hall's ice;
  * **Dreamstone crystals**: the Glittering Grotto's great crystals (1F's) grown violet along the fissure, where the
    shattered Dreamstone's power seeped; the rest of the cave keeps 1F's glass-ice crystals;
  * **standing stones** round the mound (the slip's obelisks in grey stone, their shards dark), one toppled;
  * **the ruins** sealing the way east: a gateway of the old temple's walls broken open and fallen in (Rejuvenation's
    Arceus-ruins walls, their tops broken off; its great rubble stones; a fallen column), rubble and shards before it;
  * **the cult's camp**: bedrolls, a dead fire in a ring of stones, crates and a barrel (Crown's, Odyssey's), broken
    clay vessels (the Vessels Cult's own), a torn banner;
  * **the ice hall**: glassy slippery ice (Dreamstone Mysteries' sliding floor kept), Mt. Thunder's boulders to stop on;
  * **the ladder** up (Crown's cave ladder; credit Blah and the Crown team, with permission);
  * **Nemo's ledge**: claw-scored stone and old scorch, a frayed rope over its edge.
Usage: python3 compose_b1f.py OUTDIR"""
import os, sys, random, math
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'ancient_cormoria')); sys.path.insert(0, os.path.join(HERE, '..', 'cave'))
sys.path.insert(0, os.path.join(HERE, '..'))
import tilesolve as T
import mtcorpus as MC
import plan_b1f2 as P
S = 16
W, H = P.W, P.H
G = P.G
VIO = [(34, 10, 52), (76, 26, 110), (132, 58, 190), (186, 112, 240), (232, 186, 255), (252, 240, 255)]
STONE = [(232, 236, 244), (196, 202, 216), (150, 156, 176), (108, 112, 134), (70, 72, 92), (36, 36, 52)]
def png(rel):
    a = np.array(Image.open(os.path.join(ROOT, rel)).convert('RGBA')); return a[..., :3].copy(), a[..., 3] > 0
blk = lambda x, y: (slice(y * S, y * S + S), slice(x * S, x * S + S))

def classes():
    c = np.full(G.shape, 'F', dtype='<U1'); c[G == '#'] = 'W'; c[G == 'S'] = 'S'; return c

def terrain():
    """open floor (a cell whose eight neighbours are all floor) fixed to Mt. Thunder's plain floor 0x209, so the
    solver does not run its bands' crest tiles out across open floor; the edges it solves"""
    cls = classes(); C = MC.corpus(); fixed = {}
    for y in range(1, H - 1):
        for x in range(1, W - 1):
            if (cls[y - 1:y + 2, x - 1:x + 2] == 'F').all(): fixed[(x, y)] = 0x209
    g, rep = T.solve(cls, fixed=fixed, C=C); return cls, g, rep

class Canvas:
    def __init__(self, img):
        self.img = img; self.mid = np.zeros_like(img); self.mid_a = np.zeros(img.shape[:2], bool)
        self.top = np.zeros_like(img); self.top_a = np.zeros(img.shape[:2], bool)
    def put(self, rgb, a, X0, Y0, foot=None, layer='mid'):
        """a sprite at pixel (X0, Y0); rows above `foot` (pixel y) on the top layer (the player walks behind them)"""
        h, w = a.shape
        for yy in range(h):
            Y = Y0 + yy
            if not (0 <= Y < H * S): continue
            row = a[yy].copy(); xs = slice(max(0, X0), min(W * S, X0 + w)); r0 = max(0, X0) - X0
            row = row[r0:r0 + (xs.stop - xs.start)]; src = rgb[yy][r0:r0 + (xs.stop - xs.start)]
            if layer == 'bottom': self.img[Y, xs][row] = src[row]; continue
            if foot is not None and Y < foot: self.top[Y, xs][row] = src[row]; self.top_a[Y, xs] |= row
            else: self.mid[Y, xs][row] = src[row]; self.mid_a[Y, xs] |= row
    def flat(self):
        f = self.img.copy(); f[self.mid_a] = self.mid[self.mid_a]; f[self.top_a] = self.top[self.top_a]; return f

def recolour(rgb, a, ramp):
    """a sprite's colours mapped by brightness onto a ramp (light to dark)"""
    lum = rgb.astype(float).mean(2); out = rgb.copy()
    if not a.any(): return out
    lo, hi = np.percentile(lum[a], 3), np.percentile(lum[a], 97)
    t = np.clip((hi - lum) / max(1, hi - lo), 0, 0.999) * len(ramp)
    idx = t.astype(int)
    for i, c in enumerate(ramp): out[(idx == i) & a] = c
    return out

# ---------------------------------------------------------------------------------------------------- painted pieces
def dais_and_altar():
    """the dais (11x6 cells, its top an oval of two tiers seen from above and in front) and the altar on it, as one
    picture 176x104, with its mask; the cult's sigil burnt on its top tier; the altar's table split, its socket empty"""
    Wd, Hd = 176, 104; rgb = np.zeros((Hd, Wd, 3), np.uint8); a = np.zeros((Hd, Wd), bool)
    yy, xx = np.mgrid[0:Hd, 0:Wd]; cx = Wd / 2 - 0.5
    def tier(cy, rx, ry, h, top, side, dark, light):
        topm = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1
        side_m = np.zeros_like(topm)
        for d in range(1, h + 1): side_m |= np.roll(topm, d, 0)
        side_m &= ~topm
        rgb[side_m] = side; a[side_m] = True
        for k in range(2, h, 4): rgb[side_m & (np.roll(topm, k, 0) & ~np.roll(topm, k - 1, 0))] = dark   # (courses)
        rgb[side_m & ~np.roll(side_m, -1, 0)] = STONE[5]
        rgb[topm] = top; a[topm] = True
        inner = ((xx - cx) / (rx - 2)) ** 2 + ((yy - cy) / (ry - 1.5)) ** 2 <= 1
        rgb[topm & ~inner & (yy < cy)] = light; rgb[topm & ~inner & (yy >= cy)] = dark
        return topm
    t1 = tier(62, 86, 30, 9, STONE[2], STONE[3], STONE[4], STONE[1])
    t2 = tier(52, 60, 19, 8, STONE[1], STONE[3], STONE[4], STONE[0])
    # flagstone joints on the tiers' tops
    for r_ in (40, 52, 64, 76):
        ring = (np.abs(np.sqrt(((xx - cx) / 1.0) ** 2 + ((yy - 52) * 3.0) ** 2) - r_ * 1.0) < 0.6)
        rgb[ring & t2 & ~np.roll(~t2, 2, 0)] = STONE[3]
    for ang in range(0, 360, 30):
        dx, dy = math.cos(math.radians(ang)), math.sin(math.radians(ang)) / 3.0
        for t in np.linspace(0.62, 0.98, 30):
            X, Y = int(cx + dx * 86 * t), int(62 + dy * 86 * t)
            if 0 <= X < Wd and 0 <= Y < Hd and t1[Y, X] and not t2[Y, X]: rgb[Y, X] = STONE[3]
    # the sigil (Rejuvenation's), burnt violet into the top tier
    srgb, sa = png('assets/rejuvenation/pieces/sigil.png')
    sa = sa & (srgb.astype(int).sum(2) < 400)
    sh, sw = sa.shape; sy0, sx0 = 52 - sh // 2 + 2, int(cx - sw / 2)
    for y in range(sh):
        for x in range(sw):
            if sa[y, x] and 0 <= sy0 + y < Hd and 0 <= sx0 + x < Wd and t2[sy0 + y, sx0 + x]:
                for (oy, ox, c) in ((0, 0, VIO[2]), (1, 0, VIO[1])):
                    Y, X = sy0 + y + oy, sx0 + x + ox
                    if Y < Hd and t2[Y, X]: rgb[Y, X] = c
    # the altar: a heavy stone table split down the middle, its halves shoved apart, the socket between them empty
    for half in (0, 1):
        x0 = int(cx) - 25 if half == 0 else int(cx) + 4; x1 = x0 + 21
        ty0, ty1, fy1 = 24, 33, 47
        sh = np.zeros_like(a); sh[fy1:fy1 + 3, x0 + 2:x1 + 2] = True
        rgb[sh & a] = (np.array(rgb[sh & a], float) * 0.6).astype(np.uint8)
        rgb[ty0:ty1, x0:x1] = STONE[1]; rgb[ty0 + 1, x0 + 1:x1 - 1] = STONE[0]; a[ty0:fy1, x0:x1] = True
        rgb[ty1:fy1, x0:x1] = STONE[3]
        rgb[ty1 + 2:fy1 - 2, x0 + 3:x1 - 3] = STONE[4]; rgb[ty1 + 3:fy1 - 3, x0 + 4:x1 - 4] = STONE[3]   # (a carved panel)
        rgb[ty1 + 6, x0 + 6:x1 - 6] = STONE[2]
        rgb[ty1, x0:x1] = STONE[2]
        rgb[ty0, x0:x1] = STONE[5]; rgb[fy1 - 1, x0:x1] = STONE[5]; rgb[ty0:fy1, x0] = STONE[5]; rgb[ty0:fy1, x1 - 1] = STONE[5]
        ex = x1 - 1 if half == 0 else x0                                          # (the broken edge, jagged)
        for y in range(ty0, fy1):
            j = (0, 1, 2, 1, 0, 2, 1)[y % 7] * (-1 if half == 0 else 1)
            a[y, ex] = j == 0 and a[y, ex]
            rgb[y, ex + j] = STONE[5]
            if half == 0: a[y, ex + j + 1:ex + 1] = False
            else: a[y, ex:ex + j] = False
    # the crack the Leyline tore across the dais, from the socket to the dais' lip
    rnd0 = random.Random(5); X = cx
    for y in range(42, 101):
        X += rnd0.choice((-1, 0, 0, 1)) * 0.8
        xi = int(X)
        if a[y, xi]:
            rgb[y, xi] = VIO[4]; rgb[y, xi + 1] = VIO[2]; rgb[y, xi - 1] = VIO[1]
    # the empty socket and its residue glow; scorch radiating
    sock = ((xx - cx) / 5) ** 2 + ((yy - 40) / 3) ** 2 <= 1
    rgb[sock] = VIO[0]; a |= sock
    rgb[((xx - cx) / 3) ** 2 + ((yy - 40) / 1.6) ** 2 <= 1] = VIO[3]
    rnd = random.Random(3)
    for _ in range(26):
        ang = rnd.uniform(0, 2 * math.pi); L = rnd.uniform(18, 60)
        for t in np.linspace(0, 1, 40):
            X = int(cx + math.cos(ang) * L * t); Y = int(48 + math.sin(ang) * L * t / 2.6)
            if 0 <= X < Wd and 0 <= Y < Hd and (t1[Y, X] or t2[Y, X]) and not ((28 <= Y < 46) and abs(X - cx) < 26):
                rgb[Y, X] = (np.array(rgb[Y, X], float) * 0.55).astype(np.uint8)
    return rgb, a

def standing_stone(toppled=False):
    """the slip's obelisk in grey stone, its dreamstone shard gone dark; toppled: lying on its side, cracked"""
    sys.path.insert(0, os.path.join(HERE, '..', '..', 'ancient_cormoria'))
    import compose_slip as CS
    rgb, a = CS.obelisk()
    pink = np.zeros(a.shape, bool)
    for c in CS.PS.PINK: pink |= (rgb == c).all(-1)
    out = recolour(rgb, a & ~pink, STONE[1:])
    out[pink & a] = VIO[1]; out[(rgb == CS.PS.PINK[4]).all(-1)] = VIO[2]
    if toppled:
        h = out.shape[0]; cut = int(h * 0.55)
        stump, sa = out[cut:].copy(), a[cut:].copy()
        for x in range(sa.shape[1]):
            k = (2, 0, 3, 1, 4)[x % 5]; sa[:k, x] = False
            if k < sa.shape[0]: stump[k, x] = STONE[4]
        top, ta = np.rot90(out[:cut], -1).copy(), np.rot90(a[:cut], -1).copy()
        return (stump, sa), (top, ta)
    return out, a

WAX = [(196, 150, 232), (150, 100, 196), (100, 62, 140), (52, 30, 74)]
def candle(C, m):
    """the cult's ritual candles, after Mt. Thunder's purple ones (painted here, 16x16): a cluster of two or three of
    violet wax on a pool of drips; `m` keeps Mt. Thunder's ids as the variety: 0x305/0x2f3/0x304 lit, 0x306/0x2f7
    guttered"""
    lit = m in (0x305, 0x2F3, 0x304); r = random.Random(m)
    rgb = np.zeros((16, 16, 3), np.uint8); a = np.zeros((16, 16), bool)
    pool = [(13, x) for x in range(2, 14)] + [(14, x) for x in range(3, 13)] + [(12, x) for x in range(4, 12)]
    for (y, x) in pool: rgb[y, x] = WAX[2]; a[y, x] = True
    for x in range(3, 13): rgb[14, x] = WAX[3]
    sticks = [(4, r.randint(7, 10)), (8, r.randint(4, 8)), (11, r.randint(8, 11))][:3 if m != 0x2F7 else 2]
    for (x, top) in sticks:
        if not lit: top = max(top, 9 + r.randint(0, 2))
        for y in range(top, 13):
            rgb[y, x] = WAX[1]; rgb[y, x + 1] = WAX[2]; rgb[y, x - 1] = WAX[3]; a[y, x - 1:x + 2] = True
        rgb[top, x - 1:x + 2] = WAX[0]
        if lit:
            rgb[top - 1, x] = (60, 40, 40); a[top - 1, x] = True
            for (dy, c) in ((2, (255, 140, 40)), (3, (255, 200, 90)), (4, (255, 244, 200))):
                if top - dy >= 0: rgb[top - dy, x] = c; a[top - dy, x] = True
            if top - 2 >= 0: rgb[top - 2, x + 1] = (230, 110, 40); a[top - 2, x + 1] = True
        else:
            rgb[top + 1, x + 1] = WAX[0]                                           # (a drip)
    return rgb, a

def fissure_path():
    """the Leyline scar: from the socket south down the mound's stairs, across the hall, forking"""
    main = [(24.0, 15.2), (23.8, 17.5), (24.4, 20.0), (23.6, 23.0), (24.2, 26.0), (23.4, 29.5), (21.0, 32.0), (18.0, 33.5),
            (14.5, 35.0), (11.0, 36.8)]
    fork = [(21.0, 32.0), (24.0, 34.0), (28.5, 35.0), (33.0, 37.0), (36.0, 36.5)]
    twig = [(18.0, 33.5), (17.0, 31.0), (15.5, 30.0)]
    return [main, fork, twig]

def draw_fissure(cv, rnd):
    H_, W_ = cv.img.shape[:2]; glow = np.zeros((H_, W_), float); core = np.zeros((H_, W_), bool)
    for path in fissure_path():
        pts = [(x * S + 8, y * S + 8) for (x, y) in path]
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            n = int(max(abs(bx - ax), abs(by - ay))) * 2
            for t in range(n + 1):
                X = ax + (bx - ax) * t / n + rnd.uniform(-1.2, 1.2); Y = ay + (by - ay) * t / n + rnd.uniform(-1.2, 1.2)
                xi, yi = int(X), int(Y)
                if 0 <= xi < W_ - 1 and 0 <= yi < H_ - 1:
                    core[yi, xi] = True
                    if rnd.random() < 0.5: core[yi, xi + 1] = True
    from scipy.ndimage import distance_transform_edt
    d = distance_transform_edt(~core)
    floorish = np.repeat(np.repeat(np.isin(G, list('.:SDco')), S, 0), S, 1)
    img = cv.img.astype(float)
    halo = (d <= 7) & floorish & ~core
    k = np.clip(1 - d / 7.0, 0, 1)[..., None] * 0.55
    img = np.where(halo[..., None], img * (1 - k) + np.array(VIO[3]) * k, img)
    edge = (d > 0) & (d <= 1.5) & floorish
    img[edge] = VIO[2]; img[core & floorish] = VIO[4]
    img[core & floorish & (np.random.RandomState(1).rand(H_, W_) < 0.25)] = VIO[5]
    cv.img = img.astype(np.uint8)
    return core

def deepen(img, k=0.80, cool=(0.94, 0.96, 1.06)):
    """deeper under the mountain than 1F: the whole cave a little darker and colder"""
    f = img.astype(float) * k * np.array(cool)
    return np.clip(f, 0, 255).astype(np.uint8)

def glassy(img, mask, rnd):
    """Dreamstone Mysteries' sliding ice, as glass: the floor's light and shade mapped onto a cold glassy ramp, a
    sheen of long diagonal glints"""
    ramp = np.array([(120, 168, 214), (146, 196, 232), (176, 220, 246), (214, 238, 252)], float)
    lum = img.astype(float).mean(2)
    lo, hi = np.percentile(lum[mask], 5), np.percentile(lum[mask], 95)
    t = np.clip((lum - lo) / max(1, hi - lo), 0, 0.999); idx = (t * 4).astype(int)
    out = img.copy()
    for i in range(4): out[mask & (idx == i)] = ramp[i].astype(np.uint8)
    yy, xx = np.mgrid[0:img.shape[0], 0:img.shape[1]]
    for (c0, w_) in ((0, 1), (37, 2), (91, 1), (140, 1)):
        band = (((xx + yy * 2 + c0) % 180) < w_) & mask
        out[band] = (236, 248, 255)
    return out

# ---------------------------------------------------------------------------------------------------- the whole map
DAIS_CELL = (19, 11)                          # (top-left cell of the dais picture: 11 cells x 6.5)
STONES = [(9, 4), (39, 4), (7, 13), (41, 14), (9, 22)]
TOPPLED = (40, 19)
CANDLES = [((18, 12), 0x305), ((30, 12), 0x306), ((18, 17), 0x2F7), ((30, 17), 0x304), ((21, 18), 0x306),
           ((27, 18), 0x2F3), ((13, 8), 0x306), ((35, 8), 0x2F7), ((13, 20), 0x2F3), ((35, 20), 0x306)]
VIOLET_CRYSTALS = [(20, 23), (27, 24), (19, 30), (25, 33), (31, 34), (12, 35), (16, 31)]
ICE_CRYSTALS = [(4, 3), (44, 9), (3, 22), (44, 26), (33, 41), (20, 42), (38, 38)]

def compose(seed=7):
    rnd = random.Random(seed); C = MC.corpus()
    cls, g, rep = terrain()
    img = T.render(g, C=C)
    fl = C.meta[0x209]
    for y in range(30, 38):
        for x in range(41, 47):
            if G[y, x] in '.R' and g[y][x] != 0x209 and int(g[y][x]) in C.proptiles: img[blk(x, y)] = fl
    # boulders in the ice (Mt. Thunder's own, dark and snowy)
    for k, (x, y) in enumerate(zip(*np.nonzero(G == 'o')[::-1])):
        t = C.meta[(0x20F, 0x20E, 0x205)[k % 3]]; img[blk(x, y)] = t
    # the glassy sliding ice
    ice = np.repeat(np.repeat(G == ':', S, 0), S, 1)
    img = glassy(img, ice, rnd)
    img = deepen(img)
    cv = Canvas(img)
    core = draw_fissure(cv, rnd)
    # the dais and the altar
    rgb, a = dais_and_altar(); X0, Y0 = DAIS_CELL[0] * S - 8 + 8, DAIS_CELL[1] * S + 4
    cv.put(rgb, a, X0, Y0, foot=Y0 + 40)
    # candles
    for (x, y), m in CANDLES:
        t, a = candle(C, m); cv.put(t, a, x * S, y * S)
    # standing stones and the toppled one
    for (x, y) in STONES:
        rgb, a = standing_stone(); cv.put(rgb, a, x * S, (y - 2) * S, foot=y * S)
    (srgb, sa), (trgb, ta) = standing_stone(toppled=True)
    cv.put(srgb, sa, TOPPLED[0] * S, (TOPPLED[1] + 1) * S - srgb.shape[0], foot=(TOPPLED[1] + 1) * S - 6)
    cv.put(trgb, ta, TOPPLED[0] * S + 14, (TOPPLED[1] + 1) * S - trgb.shape[0] + 2)
    # crystals: the Grotto's great crystals, violet along the fissure, glass ice elsewhere
    import gg, compose_1f as C1
    GV = gg.Vocab()
    sprites = [gg.cutout(GV, mi, b) for mi, b in gg.BIG_CRYSTALS if b[2] - b[0] == 2 and b[3] - b[1] == 2]
    for k, (x, y) in enumerate(VIOLET_CRYSTALS + ICE_CRYSTALS):
        rgb, a = sprites[k % len(sprites)]
        X0, Y0 = x * S - S // 2, (y + 1) * S - rgb.shape[0]
        under = cv.flat()[max(0, Y0):Y0 + rgb.shape[0], X0:X0 + rgb.shape[1]]
        if under.shape[:2] != a.shape: continue
        tint = (196, 120, 250) if (x, y) in VIOLET_CRYSTALS else (196, 228, 250)
        gl = C1.glass(rgb, a, under, tint)
        if (x, y) in VIOLET_CRYSTALS: gl[a & (gl.astype(int).sum(2) < 300)] = VIO[1]
        cv.put(gl, a, X0, Y0, foot=y * S)
    ruins(cv, rnd)
    camp(cv, rnd, C)
    # the ladder up
    lrgb, la = png('assets/crown_reference/pieces/cave_ladder.png')
    cv.put(lrgb, la, 4 * S, 41 * S - 16, foot=41 * S)
    nemo(cv, rnd)
    return dict(cv=cv, cls=cls, grid=g, rep=rep)

def jag(rgb, a, seed, lo, hi, edge=(54, 52, 70), side='top'):
    """break a piece's top (or bottom) edge: a jagged profile in runs of 2-4 px, the new edge outlined"""
    r = random.Random(seed); rgb, a = rgb.copy(), a.copy(); x = 0
    while x < a.shape[1]:
        run = r.randint(2, 4); cut = r.randint(lo, hi)
        for xx in range(x, min(a.shape[1], x + run)):
            col = a[:, xx]
            if side == 'top':
                col[:cut] = False; k = cut
            else:
                col[a.shape[0] - cut:] = False; k = a.shape[0] - cut - 1
            if 0 <= k < a.shape[0] and col[k]: rgb[k, xx] = edge
        x += run
    return rgb, a

def fallen_column(L, D):
    """a column lying on its side: a shaded cylinder, fluted, its drum joints marked, its ends broken"""
    rgb = np.zeros((D, L, 3), np.uint8); a = np.ones((D, L), bool)
    for y in range(D):
        t = (y + 0.5) / D
        rgb[y] = STONE[1] if t < 0.35 else STONE[2] if t < 0.7 else STONE[3]
    rgb[0], rgb[-1] = STONE[5], STONE[5]
    for y in range(3, D - 2, 3): rgb[y, :] = [int(v * 0.88) for v in rgb[y, 0]]
    for x in range(12, L, 13): rgb[1:D - 1, x] = STONE[4]
    for end in (0, L - 1):
        for y in range(D):
            j = (0, 2, 1, 3, 1, 0, 2)[y % 7]; xs = slice(0, j) if end == 0 else slice(L - j, L); a[y, xs] = False
            rgb[y, (j if end == 0 else L - 1 - j)] = STONE[5]
    return rgb, a

def ruins(cv, rnd):
    """the old temple at the hall's east end (R, 44-46 x 31-36), a shrine's footprint fallen in, seen from above:
    its back wall standing to half its height (Rejuvenation's Arceus-ruins temple wall, its violet capstones mostly
    fallen), the corner pillars snapped at different heights, the side wall's top a broken line, the front wall down
    to its footings; inside, the roof's rubble, a column fallen into drums, the lintel cracked; chips spilled onto the
    floor before it (flat). All Rejuvenation's masonry (credit the Rejuvenation team)."""
    R = 'assets/rejuvenation/pieces/ruins/%s.png'
    X, Y = 44 * S, 31 * S
    tw, ta = png('assets/rejuvenation/pieces/temple_wall.png')
    # the back wall: caps and brick (rows 21-46 of the piece, between its posts)
    wr, wa = tw[21:47, 8:56], ta[21:47, 8:56]
    wr, wa = jag(wr, wa, 11, 0, 9)
    wa[:, 30:] &= ~(np.arange(wa.shape[0])[:, None] < 12)            # (the right half fallen lower)
    cv.put(wr, wa, X, Y - 12, foot=Y + 14)
    # the side wall (west) as its top: a broken line of capstones down the footprint's edge
    cap = tw[46:52, 8:12]; side = np.zeros((70, 6, 3), np.uint8); sa = np.zeros((70, 6), bool)
    side[:, :] = (176, 180, 200); side[:, 0] = (54, 52, 70); side[:, 5] = (96, 98, 122); sa[:, :] = True
    for k in range(0, 70, 8): side[k, :] = (96, 98, 122)
    for (g0, g1) in ((22, 34), (50, 56)): sa[g0:g1] = False
    cv.put(side, sa, X - 1, Y + 14)
    # the front wall down to its footings: a course or two of brick, broken
    fr, fa = tw[34:47, 8:56], ta[34:47, 8:56]
    fr, fa = jag(fr, fa, 5, 2, 10); fa[:, 14:34] = False
    cv.put(fr, fa, X, Y + 82, foot=Y + 84)
    # the pillars: the left one snapped high, the right one low
    post, pa = tw[18:56, 0:8], ta[18:56, 0:8]
    p1, p1a = jag(post, pa, 2, 0, 4); cv.put(p1, p1a, X - 4, Y - 18, foot=Y + 18)
    p2, p2a = jag(post[14:], pa[14:], 3, 0, 5); cv.put(p2, p2a, X + 38, Y - 4, foot=Y + 18)
    p3, p3a = jag(post[22:], pa[22:], 4, 0, 4); cv.put(p3, p3a, X - 4, Y + 80, foot=Y + 96)
    # inside: the roof's rubble, the fallen column's drums, the lintel
    rgb, a = png(R % 'rubble_pile_dark'); cv.put(rgb, a, X + 3, Y + 6, foot=Y + 40)
    rgb, a = png(R % 'cracked_long'); cv.put(rgb, a, X + 2, Y + 50, foot=Y + 70)
    rgb, a = fallen_column(40, 13)                                                # (a fallen column, broken in two)
    cv.put(rgb[:, :18], a[:, :18], X + 2, Y + 42, foot=Y + 60); cv.put(rgb[:, 18:], a[:, 18:], X + 22, Y + 39, foot=Y + 60)                                   # (a fallen column, in drums)
    rgb, a = png(R % 'block_slot'); rgb, a = jag(rgb[:, :20], a[:, :20], 9, 0, 6, side='bottom')
    cv.put(rgb, a, X + 26, Y + 64, foot=Y + 84)
    # chips spilled before it, cold stone (flat)
    rgb, a = png(R % 'pebbles'); a[:2] = False; rgb = recolour(rgb, a, STONE[1:])
    for (px, py) in ((X - 24, Y + 30), (X - 14, Y + 60), (X - 36, Y + 74), (X + 14, Y + 98)):
        cv.put(rgb, a, px, py, layer='bottom')

def camp(cv, rnd, C):
    """the Vessels Cult's camp, abandoned two years: two bedrolls, a dead fire, crates and a barrel, broken vessels,
    a torn banner of the cult on the wall"""
    def bedroll(X, Y, col):
        rgb = np.zeros((14, 28, 3), np.uint8); a = np.zeros((14, 28), bool)
        a[2:12, 1:27] = True; rgb[2:12, 1:27] = col
        rgb[2, 1:27] = (40, 24, 24); rgb[11, 1:27] = (40, 24, 24); rgb[2:12, 1] = (40, 24, 24); rgb[2:12, 26] = (40, 24, 24)
        rgb[3:11, 2:8] = (200, 190, 170); rgb[3, 2:8] = (230, 224, 210)              # (the rolled end)
        for k in range(10, 26, 4): rgb[3:11, k] = tuple(int(v * 0.7) for v in col)
        cv.put(rgb, a, X, Y)
    bedroll(2 * S + 2, 31 * S + 2, (120, 52, 44)); bedroll(2 * S + 4, 33 * S - 2, (70, 78, 96))
    # the dead fire: a ring of stones, charred logs, ash
    X, Y = 5 * S + 8, 34 * S + 6; yy, xx = np.mgrid[0:20, 0:24]
    ring_ = (((xx - 11.5) / 11) ** 2 + ((yy - 9.5) / 8) ** 2 <= 1) & ~(((xx - 11.5) / 8) ** 2 + ((yy - 9.5) / 5.5) ** 2 <= 1)
    rgb = np.zeros((20, 24, 3), np.uint8); a = ring_ | (((xx - 11.5) / 8) ** 2 + ((yy - 9.5) / 5.5) ** 2 <= 1)
    rgb[a] = (86, 84, 90); rgb[ring_] = STONE[3]; rgb[ring_ & (yy < 9)] = STONE[2]
    for (x0, y0, x1, y1) in ((6, 7, 17, 12), (8, 12, 16, 6)):
        for t in np.linspace(0, 1, 20): rgb[int(y0 + (y1 - y0) * t), int(x0 + (x1 - x0) * t)] = (30, 22, 22)
    cv.put(rgb, a, X, Y)
    # crates and a barrel (Crown's crate, Odyssey's barrel), against the cave wall
    crgb, ca = png('assets/crown_reference/pieces/crate.png'); cv.put(crgb, ca, 1 * S + 4, 35 * S, foot=36 * S)
    brgb, ba = png('assets/odyssey_reference/pieces/barn_barrel.png'); cv.put(brgb, ba, 2 * S + 8, 35 * S + 4, foot=37 * S)
    # broken clay vessels (the cult's): an urn on its side, shards
    def urn(X, Y, broken_):
        rgb = np.zeros((16, 14, 3), np.uint8); yy, xx = np.mgrid[0:16, 0:14]
        body = ((xx - 6.5) / 6) ** 2 + ((yy - 9) / 6) ** 2 <= 1
        neck = (abs(xx - 6.5) <= 2.5) & (yy >= 1) & (yy < 5)
        a = body | neck
        rgb[a] = (178, 96, 62); rgb[a & (xx < 5)] = (210, 130, 84); rgb[a & (xx > 9)] = (130, 64, 46)
        rgb[body & ((yy == 8) | (yy == 10))] = (90, 40, 34)
        e = a & ~(np.roll(a, 1, 0) & np.roll(a, -1, 0) & np.roll(a, 1, 1) & np.roll(a, -1, 1)); rgb[e] = (60, 28, 24)
        if broken_: a &= ~((xx > 7) & (yy < 9)); rgb[(xx == 8) & a] = (60, 28, 24)
        cv.put(rgb, a, X, Y)
    urn(6 * S + 2, 31 * S, False); urn(7 * S + 2, 32 * S + 6, True)
    # the torn banner on the back wall: dark cloth, the cult's vessel in old gold, the hem in tatters
    rgb = np.zeros((26, 14, 3), np.uint8); a = np.zeros((26, 14), bool); a[0:26, 1:13] = True
    rgb[a] = (54, 34, 60); rgb[0:2, 0:14] = (120, 90, 60); a[0:2, 0:14] = True
    for x in range(1, 13):
        cut = 18 + ((x * 7) % 8); a[cut:, x] = False
    v = [(8, 5), (8, 8), (9, 4), (9, 9), (10, 4), (10, 9), (11, 5), (11, 8), (12, 6), (12, 7), (7, 6), (7, 7), (6, 5), (6, 8)]
    for (y, x) in v: rgb[y, x] = (200, 160, 70)
    cv.put(rgb, a, 3 * S + 1, 29 * S + 8)

def nemo(cv, rnd):
    """Nemo's ledge (40-46, 1-3): claw-scored stone, old scorch, a frayed rope hanging over its edge"""
    img = cv.img
    for _ in range(4):
        X, Y = rnd.randrange(40 * S, 46 * S), rnd.randrange(1 * S + 4, 3 * S + 8)
        for k in range(3):
            for t in range(7):
                if 0 <= Y + t < img.shape[0] and 0 <= X + k * 3 + t < img.shape[1]: img[Y + t, X + k * 3 + t] = STONE[4]
    yy, xx = np.mgrid[0:img.shape[0], 0:img.shape[1]]
    d = np.sqrt(((xx - 44 * S) / 1.0) ** 2 + ((yy - 2 * S - 8) * 2.2) ** 2)
    ang = np.arctan2((yy - 2 * S - 8) * 2.2, xx - 44 * S)
    streak = (np.sin(ang * 7) * 0.5 + 0.5) * np.clip(1 - d / 34.0, 0, 1)
    k = (1 - 0.5 * streak)[..., None]
    reg = np.zeros(img.shape[:2], bool); reg[S:4 * S, 40 * S:47 * S] = True
    img[reg] = (img[reg] * k[reg]).astype(np.uint8)
    rope = np.zeros((26, 4, 3), np.uint8); ra = np.zeros((26, 4), bool)
    for y in range(26): x = 1 + int(math.sin(y / 3.0)); ra[y, x:x + 2] = True; rope[y, x:x + 2] = (150, 120, 80) if y % 3 else (110, 84, 56)
    cv.put(rope, ra, 41 * S + 6, 3 * S + 12)

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
    r = compose(); C = MC.corpus()
    print('unseen', len(r['rep']['unseen']), 'conflicts', len(r['rep']['conflicts']), 'seams', len(T.seams(r['grid'], C)))
    Image.fromarray(r['cv'].flat()).save(os.path.join(out, 'b1f_mock_v1.png'))
