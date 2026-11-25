"""Mt. Mirroh B1F, art mock v3: the Blast Crater with its temple from MonoMyth's ruined temple (plan_b1f5.py).

Kept from v2 (the user liked it): the sinkhole, the cracked floor about it (Lazarus' blast pit and crack decal), the
camp, the ladder, the cavern (Mt. Thunder, MonoMyth).
New, from MonoMyth's forest temple ruin (868f44; credit the MonoMyth team), frosted and cooled to the cave:
  * the rim: the temple's terrace laid tile for tile in its own pieces: a back face and a front face, each a colonnade
    of short pillars in cracked courses (its knight statues left out, their places fallen in), a brick floor between,
    one stair up the middle of the front face on the pit's axis;
  * the pillar ring: its round columns (cap, shaft, base): three still standing, three cells high; seven snapped to
    stumps of different heights; their shafts lying where the blast threw them: Lazarus' fallen fluted column
    (its autumn ruins, faa62c), cooled the same way;
  * the rubble: its fallen wall courses lying flat about the stumps and on the terrace; Mt. Thunder's boulders;
  * its moss, under the mountain, becomes frost: every green of MonoMyth's goes to a pale ice blue.
Usage: python3 compose_b1f5.py OUTDIR"""
import os, sys, random, math
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'ancient_cormoria')); sys.path.insert(0, os.path.join(HERE, '..', 'cave'))
import plan_b1f5 as P
sys.modules['plan_b1f4'] = P                      # (compose_b1f4's helpers read the plan: give them v5)
import compose_b1f4 as V2
import compose_b1f as V1
import tilesolve as T
import mtcorpus as MC
import mono_pieces as MP
from scipy.ndimage import binary_fill_holes
from compose_b1f import png, Canvas, deepen, S
W, H, G = P.W, P.H, P.G
blk = lambda x, y: (slice(y * S, y * S + S), slice(x * S, x * S + S))
TEMPLE = 0x868f44
GROUND = [0x12d, 0x2, 0x10d, 0x35]

# ---------------------------------------------------------------------------------------------- MonoMyth -> the cave
STONE7 = [(236, 240, 248), (210, 216, 232), (180, 188, 210), (148, 156, 184), (114, 120, 154), (80, 84, 116), (46, 48, 72)]
FROST = [(226, 240, 252), (196, 222, 244), (160, 196, 230), (124, 160, 206)]
_cmap = {}
def cool(c):
    """one colour of MonoMyth's temple -> the cave's: stone by its lightness; greens (moss, grass) -> frost"""
    c = tuple(int(v) for v in c)
    if c in _cmap: return _cmap[c]
    r, g, b = c; lum = 0.3 * r + 0.55 * g + 0.15 * b
    if g > r + 12 and g > b - 10:
        out = FROST[min(3, int((255 - lum) / 255 * 5) + 1)]
    else:
        out = STONE7[min(6, max(0, int((250 - lum) / 230 * 7) + 1))]
    _cmap[c] = out; return out
def cool_img(rgb):
    out = rgb.copy(); flat = out.reshape(-1, 3)
    for i, c in enumerate(flat): flat[i] = cool(c)
    return out

def meta(m):
    img, g, ts = MP.grid(TEMPLE); return cool_img(ts.meta(m))

# ------------------------------------------------------------------------------------------------------------ the rim
UP = ['69', '6c', '6e', '6b', '84', '85', '69', '6e']          # (a face's upper course: brick, cracked brick)
LO = ['99', '71', '74', '76', '99', '74']                       # (its lower course)
FLOOR = ['59', '5e', '59', '58', '89', '81', '59', '5e']
LIP = ['d1', 'd2', 'd1', '143', 'd2', '142']
def rim(img, rnd):
    """the terrace, cell by cell in MonoMyth's own metatiles: faces with a short pillar every fourth cell (some broken,
    '8f'), the statues' places fallen in ('7c', a dark breach), the stair up the middle"""
    h = lambda s: int(s, 16)
    for x in range(9, 32):
        col = (x - 9) % 4 == 0 or x == 31
        for (y_up, y_lo) in ((2, 3), (7, 8)):
            if y_up == 7 and 19 <= x <= 21: continue
            if col:
                up = '8f' if rnd.random() < 0.35 else '8e'; lo = '97' if up == '8f' else '96'
            else:
                up = '7c' if rnd.random() < 0.10 else rnd.choice(UP); lo = rnd.choice(LO)
            img[blk(x, y_up)] = meta(h(up)); img[blk(x, y_lo)] = meta(h(lo))
        img[blk(x, 4)] = meta(h(rnd.choice(LIP)))
        for y in (5, 6): img[blk(x, y)] = meta(h(rnd.choice(FLOOR)))
        if not 19 <= x <= 21: img[blk(x, 9)] = meta(h(rnd.choice(['d1', 'd2', 'd1', 'd3'])))
    for (x, a, b, c) in ((19, '9b', '93', '8b'), (20, '9c', '8c', '94'), (21, '8d', '9d', '9d')):
        img[blk(x, 7)] = meta(h(a)); img[blk(x, 8)] = meta(h(b)); img[blk(x, 9)] = meta(h(c))
    return img

# ------------------------------------------------------------------------------------------------------- the columns
def column_parts():
    """MonoMyth's round column, cut from its ground: cap (0x11b), shaft (0x123), base (0x13c), frosted"""
    img, g, ts = MP.grid(TEMPLE)
    gc = set()
    for m in GROUND: gc |= {tuple(c) for c in ts.meta(m).reshape(-1, 3)}
    parts = {}
    for name, m in (('cap', 0x11b), ('shaft', 0x123), ('base', 0x13c)):
        t = ts.meta(m); a = np.array([[tuple(c) not in gc for c in row] for row in t])
        r_, g_, b_ = [t[..., i].astype(int) for i in range(3)]
        a &= ~((g_ > r_ + 12) & (g_ > b_ - 10) & (np.arange(16)[None, :] > 11))   # (grass beside it, not moss on it)
        a = binary_fill_holes(a)
        parts[name] = (cool_img(t), a)
    return parts

def column(cells_high, broken, rnd, P_=None):
    p = P_ or column_parts()
    if broken: stack = [p['shaft']] * max(1, cells_high - 1) + [p['base']]
    else: stack = [p['cap']] + [p['shaft']] * max(0, cells_high - 2) + [p['base']]
    rgb = np.concatenate([s[0] for s in stack]); a = np.concatenate([s[1] for s in stack])
    if broken:
        cut = rnd.randint(3, 9); rgb, a = V1.jag(rgb[cut:], a[cut:], rnd.randrange(99), 0, 5, edge=STONE7[5])
    return rgb, a

def lying(cells_long, rnd, P_=None):
    """a column on its side: its shaft turned (its light then falls from above, as on a lying drum), broken at both
    ends, its cap's round face at one end"""
    p = P_ or column_parts()
    sh = np.concatenate([p['shaft'][0]] * cells_long); sa = np.concatenate([p['shaft'][1]] * cells_long)
    rgb, a = np.rot90(sh, 1).copy(), np.rot90(sa, 1).copy()
    rows = np.nonzero(a.any(1))[0]; rgb, a = rgb[rows[0]:rows[-1] + 1], a[rows[0]:rows[-1] + 1]
    rgb, a = np.rot90(rgb, -1).copy(), np.rot90(a, -1).copy()
    rgb, a = V1.jag(rgb, a, rnd.randrange(99), 0, 4, edge=STONE7[5]); rgb, a = V1.jag(rgb, a, rnd.randrange(99), 0, 4, edge=STONE7[5], side='bottom')
    return np.rot90(rgb, 1).copy(), np.rot90(a, 1).copy()

def laz_fallen(cells_long, rnd):
    """Lazarus' fallen fluted column (faa62c, 2 cells; credit the Lazarus team), its path-colour ground dropped, cooled
    to the cave's stone; one cell long: its broken half"""
    d = np.load(os.path.join(V1.ROOT, 'assets/lazarus_reference/fallen_column.npz'))   # (lazarus_pieces.cut_on, faa62c 8,12)
    rgb, a = d['rgb'].copy(), d['a'].copy()
    a &= ~(rgb == (248, 248, 224)).all(-1); a = binary_fill_holes(a)
    rgb = cool_img(rgb)
    rows = np.nonzero(a.any(1))[0]; cols = np.nonzero(a.any(0))[0]
    rgb, a = rgb[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1].copy(), a[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1].copy()
    if cells_long == 1:
        h = rgb.shape[1] // 2 + 2; rgb, a = rgb[:, :h].copy(), a[:, :h].copy()
        r2, a2 = V1.jag(np.rot90(rgb, 1).copy(), np.rot90(a, 1).copy(), rnd.randrange(99), 0, 3, edge=STONE7[5])
        rgb, a = np.rot90(r2, -1).copy(), np.rot90(a2, -1).copy()
    return rgb, a

def rubble_pieces():
    out = []
    for (x, y) in ((28, 28), (28, 17), (28, 36)):
        rgb, a = MP.cut_on(TEMPLE, x, y, 3, 2, GROUND); a = binary_fill_holes(a)
        rows = np.nonzero(a.any(1))[0]; cols = np.nonzero(a.any(0))[0]
        out.append((cool_img(rgb)[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1], a[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1]))
    return out

def ring(cv, rnd):
    parts = column_parts(); rub = rubble_pieces()
    broken_k = [k for k in range(10) if k not in P.STANDING]
    for k, (x, y, a) in enumerate(P.RING):
        if k in P.STANDING:
            rgb, al = column(3, False, rnd, parts)
        else:
            rgb, al = column(rnd.choice((2, 2, 3)), True, rnd, parts)
        cv.put(rgb, al, x * S, (y + 1) * S - rgb.shape[0], foot=(y + 1) * S - 5)
        if k in P.STANDING: continue
        cells = [q for q in P.SHAFTS[broken_k.index(k)] if G[q[1], q[0]] == 'f']
        if cells:
            rgb, al = laz_fallen(len(cells), rnd)
            cx = (min(q[0] for q in cells) * S + (max(q[0] for q in cells) + 1) * S) // 2; cy = cells[0][1] * S + S // 2
            cv.put(rgb, al, cx - rgb.shape[1] // 2, cy - rgb.shape[0] // 2 + 1, foot=cy + 8)
        # a fallen course of its wall beside it, flat
        rr, ra = rub[k % 3]
        ox = int(round(math.cos(a) * 20 - math.sin(a) * 14)); oy = int(round(math.sin(a) * 14 + math.cos(a) * 10))
        cv.put(rr, ra, x * S + ox - rr.shape[1] // 2 + 8, y * S + oy, layer='bottom')

def rim_debris(cv, rnd):
    parts = column_parts(); rub = rubble_pieces()
    for (y, x) in np.argwhere(G[:10] == 'b'):
        rgb, al = column(2, True, rnd, parts); cv.put(rgb, al, x * S, (y + 1) * S - rgb.shape[0], foot=(y + 1) * S - 5)
    for k, (y, x) in enumerate(np.argwhere(G[:10] == 'r')):
        rr, ra = rub[k % 3]; cv.put(rr, ra, x * S - rr.shape[1] // 2 + 8, y * S + 2)
    rgb, al = laz_fallen(2, rnd); cv.put(rgb, al, 22 * S + 2, 5 * S + 2, foot=6 * S)      # (one down on the terrace)

def compose(seed=11):
    rnd = random.Random(seed); C = MC.corpus()
    cls, g, rep = V2.terrain()
    img = T.render(g, C=C)
    for (y, x) in np.argwhere(G == 'r'):
        if y >= 10: img[blk(x, y)] = C.meta[(0x205, 0x20F)[(x + y) % 2]]
    img = V2.cracks(img, rnd)
    img, pm = V2.pit(img)
    img = deepen(img, k=0.86)
    img = rim(img, random.Random(5))
    cv = Canvas(img)
    ring(cv, rnd)
    rim_debris(cv, rnd)
    # a course of the dais' masonry gone half over the north lip (where the altar stood)
    rub = rubble_pieces(); rr, ra = rub[1]; cv.put(rr, ra, 19 * S, 17 * S - 4, foot=17 * S + 8)
    import gg, compose_1f as C1
    GV = gg.Vocab()
    sprites = [gg.cutout(GV, mi, b) for mi, b in gg.BIG_CRYSTALS if b[2] - b[0] == 2 and b[3] - b[1] == 2]
    for k, (x, y) in enumerate(((5, 13), (35, 15), (36, 25), (4, 24), (26, 31), (11, 11))):
        rgb, a = sprites[k % len(sprites)]
        X0, Y0 = x * S - S // 2, (y + 1) * S - rgb.shape[0]
        under = cv.flat()[Y0:Y0 + rgb.shape[0], X0:X0 + rgb.shape[1]]
        if under.shape[:2] != a.shape: continue
        cv.put(C1.glass(rgb, a, under, (196, 228, 250)), a, X0, Y0, foot=y * S)
    V2.camp(cv)
    lrgb, la = png('assets/crown_reference/pieces/cave_ladder.png'); cv.put(lrgb, la, 20 * S, 37 * S - 16, foot=37 * S)
    return dict(cv=cv, cls=cls, grid=g, rep=rep)

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
    r = compose(); C = MC.corpus()
    print('unseen', len(r['rep']['unseen']), 'conflicts', len(r['rep']['conflicts']), 'seams', len(T.seams(r['grid'], C)))
    Image.fromarray(r['cv'].flat()).save(os.path.join(out, 'b1f_mock_v3.png'))
