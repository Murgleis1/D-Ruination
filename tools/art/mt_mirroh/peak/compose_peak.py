"""Mirroh Peak, art v1 (user 2026-11-24): plan v2 (plan_peak.py) dressed "Mt. Thunder style like 1F": built the way
MonoMyth's Mt. Thunder outdoors and its Peak of Kings are built (mtout.py: snow, one-tile rock bands under snowy
crests stacked where the mountain is thick, stairs through the bands, ice grass, the stream falling through the bands
into its pond); Dreamstone Mysteries' foot re-tiled in the same (its masses become stacked bands); its pinewood the
exterior's (Fort Elderflower's snowy pines, whole trees, staggered), so the two maps match; pines on the climb; the
two cave mouths Mt. Thunder's own band mouth (Winterlily Hollow's blocked by a snowy boulder); the sky round the
summit painted (bands of blue paling toward the mountain, a few clouds); the summit's ruins in Crown stone, snowed
over: two roofless huts of Crown's bastion masonry (its crenellations broken) and the broken shrine, Crown's
cathedral portal (rose window, the door) with its top crumbled.
Usage: python3 compose_peak.py OUT.png"""
import os, sys, random
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'mirroh'))
import mtout
import plan_peak as P
import mirroh_mock as mm
W, H, S = P.W, P.H, 16
G = P.G
blk = lambda x, y: (slice(y * S, y * S + S), slice(x * S, x * S + S))
MOUTH_1F, MOUTH_WL = (26, 101), (40, 78)
# Mt. Thunder's props: never learned as ground (pines, flowers, small rocks, its shrines' pieces)
NOT_GROUND = {('out', m) for m in (0x109, 0xEE, 0x29F, 0xFB, 0x28E, 0xE9, 0xEA, 0xED, 0xE8, 0x255, 0x2B5, 0x2B6,
                                    0x290, 0x104, 0x103, 0x277, 0x2CC, 0x2CD, 0x275, 0xF6, 0x330)}
BAND_END_PROPS = {('out', m) for m in (0x114, 0x338, 0x29F, 0x272, 0x26C, 0x296)}
CLS = {'K': 'K', '#': 'W', 'E': 'W', 'W': 'W', '~': 'A', 'S': 'S', 'g': 'G', 'H': 'F', 'Q': 'F'}

def cls(x, y):
    if not (0 <= x < W and 0 <= y < H): return 'W'
    return CLS.get(G[y, x], 'F')

def sky_px():
    """The sky: bands of blue from a deep top paling toward the mountain's shoulders (row 34), each band dithered
    into the next over its last four pixel rows; periodic every 16 pixels across (few tiles)."""
    rows = 35 * S
    stops = [(0, (92, 138, 206)), (8, (112, 158, 220)), (16, (136, 180, 232)), (24, (168, 204, 240)), (30, (200, 224, 248)), (35, (222, 236, 252))]
    def band_col(cy):
        for (a, ca), (b, cb) in zip(stops, stops[1:]):
            if a <= cy < b: return ca, cb, a, b
        return stops[-1][1], stops[-1][1], 34, 35
    sky = np.zeros((rows, S, 3), np.uint8)
    for py in range(rows):
        cy = py / S; ca, cb, a, b = band_col(cy)
        into = b * S - py                                       # (pixels left in this band)
        for px in range(S):
            dith = into <= 4 and ((px + py) % 2 == 0 if into > 2 else (px + py) % 4 != 0)
            sky[py, px] = cb if dith else ca
    return sky

CLOUD_W, CLOUD_H = 4, 2
def cloud_stamp(seed):
    """A soft pale cloud, 4x2 cells, alpha mask (white puffs, a cool shaded underside)."""
    r = random.Random(seed); yy, xx = np.mgrid[0:CLOUD_H * S, 0:CLOUD_W * S]
    a = np.zeros(yy.shape, bool); shade = np.zeros(yy.shape, bool)
    puffs = [(10 + 44 * t + r.uniform(-3, 3), 18 + r.uniform(-3, 2), r.uniform(7, 11)) for t in np.linspace(0, 1, 5)]
    for cx, cy, rad in puffs:
        m = (xx - cx) ** 2 + ((yy - cy) * 1.25) ** 2 <= rad ** 2; a |= m
    a &= yy < 27
    shade = a & (yy > 20)
    rgb = np.zeros(yy.shape + (3,), np.uint8); rgb[a] = (246, 250, 255); rgb[shade] = (214, 228, 246)
    edge = a & ~np.roll(a, 1, 0); rgb[edge] = (255, 255, 255)
    return rgb, a

def snowcap(rgb, a, depth=3):
    """Snow on every top edge of a shape (its topmost opaque pixels in each column, and on its ledges)."""
    out = rgb.copy(); h, w = a.shape
    for x in range(w):
        col = np.where(a[:, x])[0]
        if not len(col): continue
        t = col[0]; d = depth + (x * 7 % 3 == 0)
        out[t:t + d, x] = (246, 250, 255); out[t + d - 1, x] = (214, 230, 246) if d > 1 else out[t + d - 1, x]
    # ledges: an opaque pixel whose pixel above is markedly lighter-dark edge (a horizontal moulding) gets a dusting
    f = rgb.astype(int).sum(-1)
    led = a[1:] & a[:-1] & (f[:-1] < 260) & (f[1:] > 420)
    ys, xs = np.where(led)
    for y_, x_ in zip(ys, xs):
        if (x_ * 5 + y_) % 3: out[y_ + 1, x_] = (236, 244, 252)
    return out

def crumble(a, seed, top_rows=10, depth=7):
    """A broken top: the shape's top edge eaten into an irregular line (deeper in places)."""
    r = random.Random(seed); a = a.copy(); h, w = a.shape
    cut = 0; line = []
    for x in range(w):
        cut = max(0, min(depth, cut + r.choice((-2, -1, 0, 0, 1, 2))))
        line.append(cut)
    for x in range(w):
        col = np.where(a[:, x])[0]
        if len(col): a[col[0]:col[0] + line[x], x] = False
    return a

def compose(seed=11):
    rnd = random.Random(seed)
    V = mtout.Vocab()
    for k in list(V.samples):
        if k[0] in 'FG':
            for sm in [sm for sm in V.samples[k] if sm in NOT_GROUND or (sm[0] == 'pok' and sm[1] < 0x200)]:
                del V.samples[k][sm]
            if not V.samples[k]: del V.samples[k]
    img = np.zeros((H * S, W * S, 3), np.uint8)
    top = np.zeros_like(img); top_a = np.zeros((H * S, W * S), bool)
    ids = {}
    for y in range(H):
        for x in range(W):
            me = cls(x, y); nb = [cls(x + dx, y + dy) for dx, dy in mtout.N8]
            sm = V.pick(me + ''.join(nb))
            if me == 'W' and sm in BAND_END_PROPS:
                # (Mt. Thunder caps a band's end with a pine or a cairn standing in it; on its own, that half-pine
                # reads as a stump: its own rounded band ends instead)
                sm = ('out', 0x27B) if cls(x - 1, y) != 'W' else ('out', 0x27E) if cls(x + 1, y) != 'W' else ('out', 0x27C)
            if sm in (('pok', 0x2F), ('pok', 0x37)): sm = ('out', 0x29C)   # (the Peak of Kings' blank flank pieces: its stacked rock)
            ids[(x, y)] = sm; img[blk(x, y)] = V.meta(sm)
    # ---- the sky (and the black of the Peak of Kings' edge pieces: sky behind them)
    sky = sky_px(); sky_a = np.zeros((H * S, W * S), bool)      # (sky_a: where the sky shows: a backdrop goes there)
    for y in range(35):
        for x in range(W):
            if cls(x, y) == 'K': img[blk(x, y)] = sky[y * S:y * S + S]; sky_a[blk(x, y)] = True
            else:
                b = img[blk(x, y)]; k = (b.astype(int).sum(-1) == 0)
                if k.any(): b[k] = sky[y * S:y * S + S][k]; sky_a[blk(x, y)] |= k
    # the plateau's north edge: a snowy lip onto the sky (a rounded white crest, its shade under it), no wall behind
    for y in range(1, 35):
        for x in range(W):
            if cls(x, y) != 'K' and cls(x, y - 1) == 'K' and G[y, x] in '.QH':
                b = img[blk(x, y)]
                for px in range(S):
                    t = 1 + ((x * 16 + px) * 7 % 5 == 0)
                    b[0:t, px] = sky[y * S:y * S + t, px]; sky_a[y * S:y * S + t, x * S + px] = True
                    b[t:t + 2, px] = (250, 253, 255); b[t + 2, px] = (214, 232, 248); b[t + 3, px] = (184, 210, 236)
    for i, (cx, cy) in enumerate(((2, 3), (38, 6), (5, 12), (41, 15), (0, 21), (44, 25))):
        rgb, a = cloud_stamp(i % 3)
        reg = img[cy * S:cy * S + CLOUD_H * S, cx * S:cx * S + CLOUD_W * S]
        kk = np.zeros_like(a)
        for dy in range(CLOUD_H):
            for dx in range(CLOUD_W):
                if cls(cx + dx, cy + dy) == 'K': kk[dy * S:dy * S + S, dx * S:dx * S + S] = True
        m = a & kk; reg[m] = rgb[m]
    # ---- the pines: on the climb, Elderflower's big pine (2x3) on each 2x2 'T' block, its crown above on the top
    # layer (walked behind); the foot's pinewood as the exterior's (big pines staggered, small pines, rocks)
    EFG = mm.EF_GROUND
    BIG, SMALL, ROCK = [[0xe9, 0xea], [0xf1, 0xf2], [0xf9, 0xfa]], [[0x109], [0x111]], [[0xe8]]
    snow = V.meta(('out', mtout.SNOW)); e8 = V.meta(('out', 0xE8))
    ROCKP = [[(e8, (np.abs(e8.astype(int) - snow.astype(int)).sum(-1) > 30))]]   # (Mt. Thunder's snowy boulder, off its snow)
    fb = V.meta(('out', 0xFB)); SHRUB = [[(fb, (np.abs(fb.astype(int) - snow.astype(int)).sum(-1) > 30))]]   # (its snow-laden shrub)
    def place(rows, x, y, top_rows=0):
        pc = ROCKP if rows is ROCK else SHRUB if rows == 'shrub' else mm.cut_ids('ef', rows, EFG)
        for dy, r in enumerate(pc):
            for dx, p in enumerate(r):
                if p is None: continue
                rgb, a = p
                if dy < top_rows:
                    top[blk(x + dx, y + dy)][a] = rgb[a]; top_a[blk(x + dx, y + dy)] |= a
                else:
                    reg = img[blk(x + dx, y + dy)]; reg[a] = rgb[a]
    tree = {(x, y) for y in range(H) for x in range(W) if G[y, x] == 'T'}
    used = set(); solid_tree = set()
    climb = {(x, y) for (x, y) in tree if y < 68}
    for (x, y) in sorted(climb, key=lambda c: (c[1], c[0])):
        if (x, y) in used: continue
        if all((x + i, y + j) in climb for i in (0, 1) for j in (0, 1)):
            place(BIG, x, y - 1, top_rows=1); used |= {(x + i, y + j) for i in (0, 1) for j in (0, 1)}
    foot = sorted(tree - climb, key=lambda c: (c[1], c[0]))
    for (x, y) in foot:
        img[blk(x, y)] = V.meta(('out', mtout.SNOW))
    for (x, y) in foot:
        if (x + y * 3) % 2 == 0 and all((x + i, y + j) in tree and (x + i, y + j) not in used for i in (0, 1) for j in (0, 1, 2)):
            place(BIG, x, y); used |= {(x + i, y + j) for i in (0, 1) for j in (0, 1, 2)}
    for (x, y) in foot:
        if (x, y) in used: continue
        if (x, y + 1) in tree and (x, y + 1) not in used: place(SMALL, x, y); used |= {(x, y), (x, y + 1)}
        elif any(G[y + dy, x + dx] in '.g' for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= x + dx < W and 0 <= y + dy < H):
            G[y, x] = '.'; used.add((x, y))                         # (a lone cell at the wood's edge: open snow, not a wall)
        else: place('shrub', x, y); used.add((x, y))                # (a lone cell inside the wood: a snow-laden shrub)
    # ---- the cave mouths: a dark arch cut up through the band's two rows (as 1F's own exit to the Peak), icicles
    # hanging in it; Winterlily Hollow's choked with a snowy boulder and stones (Chapter 1: closed)
    def arch(x, y, blocked):
        X0, Y0 = (x - 1) * S, (y - 1) * S; yy, xx = np.mgrid[0:2 * S, 0:3 * S]
        a = ((xx - 23.5) / 12.5) ** 2 + ((yy - 32) / 24.0) ** 2 <= 1; reg = img[Y0:Y0 + 2 * S, X0:X0 + 3 * S]
        ring = a & ~(((xx - 23.5) / 10.5) ** 2 + ((yy - 32) / 22.0) ** 2 <= 1)
        reg[a] = (14, 20, 36); reg[ring] = (58, 72, 104)
        reg[ring & (yy < 14)] = (236, 244, 252)                                     # (snow on its lip)
        for ix, ln in ((17, 4), (20, 6), (24, 3), (27, 5), (30, 4)):
            ty = int(32 - 24 * np.sqrt(max(0, 1 - ((ix - 23.5) / 12.5) ** 2))) + 2
            for k in range(ln): reg[ty + k, ix:ix + (1 if k > ln // 2 else 2)] = (214, 238, 255) if k < ln - 1 else (250, 254, 255)
        if blocked:
            t, m = ROCKP[0][0]; sub = reg[S:2 * S, S:2 * S]; sub[m] = t[m]
            from ruins import _stones
            st = reg.astype(int); aa = np.zeros(st.shape[:2], bool)
            _stones(st, aa, (14, 26, 34, 31), 5, 2.6, 7); reg[aa & a] = st[aa & a].astype(np.uint8)
    arch(*MOUTH_1F, False); arch(*MOUTH_WL, True)
    # ---- the ruins (Crown stone, snowed over: ruins.py)
    import ruins
    for n, (hx, hy) in enumerate(P.HUTS):
        rgb, a = ruins.hut(30 + n); img[hy * S:hy * S + 4 * S, hx * S:hx * S + 4 * S][a] = rgb[a]
    rgb, a = ruins.shrine(); qx, qy = P.SHRINE; img[qy * S:qy * S + 4 * S, qx * S:qx * S + 4 * S][a] = rgb[a]
    # ---- dressing, as Mt. Thunder and the Peak of Kings dress theirs: at the foot of the bands and against their
    # ends, never on a stair or its approach, never closing a way: on the summit and its ledges the Peak of Kings'
    # cairns (some with their purple cloth), snowy boulders and purple flowers; on the climb and the foot Mt. Thunder's
    # snowballs and flowers, and cairns. Flowers are walked over; the rest are solid.
    SNOWS = [V.meta(sm) for sm in (('out', mtout.SNOW), ('pok', 0x318), ('out', 0x318), ('pok', 0x7), ('out', 0x266), ('out', 0x26e))]
    from scipy.ndimage import binary_fill_holes
    def prop(sm):
        """the prop's own pixels: those that differ from the snow it was drawn on (the snow tile it matches best)"""
        t = V.meta(sm); eq = max(((t == b).all(-1) for b in SNOWS), key=lambda e: e.sum())
        a = binary_fill_holes(~eq)
        assert a.sum() > 20, sm                                     # (never an invisible solid prop)
        return t, a
    PROPS = {'cairn': (('pok', 0xC), 1), 'flagcairn': (('pok', 0xA), 1), 'boulder': (('pok', 0xB), 1),
             'pflowers': (('pok', 0x12), 0), 'snowball': (('out', 0xE8), 1),
             'tflowers': (('out', 0xEE), 0), 'mflowers': (('out', 0x29F), 0)}
    PX = {k: prop(v[0]) for k, v in PROPS.items()}
    clear = set()
    for y in range(H):
        for x in range(W):
            if G[y, x] in 'SEW':
                for dx in (-1, 0, 1):
                    for dy in (-2, -1, 0, 1, 2): clear.add((x + dx, y + dy))
    for (x, y) in P.SPOTS.values():
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1): clear.add((x + dx, y + dy))
    for y in range(11, 15):
        for x in range(19, 31): clear.add((x, y))                     # (the stage in the middle of the plateau)
    for x in range(P.PLATEAU[0], P.PLATEAU[2] + 1): clear.add((x, P.PLATEAU[1]))   # (the north edge: a clear lookout)
    def h(x, y, k): return ((x * 73856093) ^ (y * 19349663) ^ (k * 83492791)) % 1000 / 1000.0
    dress = {}
    def walkable(): return {(x, y) for y in range(H) for x in range(W) if G[y, x] in '.gSE' and dress.get((x, y), (0, 0))[1] == 0}
    def reach(cells):
        st = [(26, 102)]; seen = {(26, 102)}
        while st:
            x, y = st.pop()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (x + dx, y + dy)
                if q in cells and q not in seen: seen.add(q); st.append(q)
        return seen
    base_n = len(reach(walkable()))
    for y in range(H):
        for x in range(W):
            if G[y, x] != '.' or (x, y) in clear or (x, y) in dress: continue
            if any((x + dx, y + dy) in dress for dx in (-1, 0, 1) for dy in (-1, 0, 1)): continue
            foot = G[y - 1, x] == '#'; side = G[y, x - 1] == '#' or G[y, x + 1] == '#'
            if not (foot or side): continue
            zone = 'summit' if y < 35 else 'climb' if y < 68 else 'foot'
            pr = h(x, y, 1)
            if pr > {'summit': 0.30, 'climb': 0.20, 'foot': 0.10}[zone]: continue
            pick = h(x, y, 2)
            if zone == 'summit': k = 'pflowers' if pick < 0.30 else 'cairn' if pick < 0.55 else 'flagcairn' if pick < 0.70 else 'boulder'
            elif zone == 'climb': k = 'tflowers' if pick < 0.25 else 'mflowers' if pick < 0.45 else 'cairn' if pick < 0.70 else 'snowball'
            else: k = 'snowball' if pick < 0.6 else 'tflowers'
            dress[(x, y)] = (k, PROPS[k][1])
            if PROPS[k][1] and len(reach(walkable())) < base_n - sum(1 for v in dress.values() if v[1]):
                del dress[(x, y)]                                           # (it closed a way: not there)
    for (x, y), (k, sol) in dress.items():
        t, a = PX[k]; reg = img[blk(x, y)]; reg[a] = t[a]
    # ---- cells: rock, pines, ruins, mouths and water solid; ice grass tall grass; one level
    solid = np.zeros((H, W), bool); beh = np.zeros((H, W), int); elev = np.full((H, W), 3)
    for y in range(H):
        for x in range(W):
            ch = G[y, x]
            solid[y, x] = ch in '#KTHQPEW~' or dress.get((x, y), (0, 0))[1] == 1
            if ch == 'g': beh[y, x] = 0x02
            if ch == '~': beh[y, x] = 0x15
    x, y = MOUTH_1F; solid[y, x] = False; beh[y, x] = 0x60          # (MB_NON_ANIMATED_DOOR: the way into 1F)
    flat = img.copy(); flat[top_a] = top[top_a]
    return dict(sky_a=sky_a, bottom=img, top=top, top_a=top_a, flat=flat, solid=solid, beh=beh, elev=elev, ids=ids, dress=dress, missed=getattr(V, 'missed', 0))

if __name__ == '__main__':
    r = compose(); print('unseen patterns:', r['missed'])
    Image.fromarray(r['flat']).save(sys.argv[1] if len(sys.argv) > 1 else '/tmp/peak_art.png')
