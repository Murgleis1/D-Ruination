"""The slip's terrain, built only from what MonoMyth's canyon country actually does (user 2026-11-24, on mock v1:
"There's a lot of broken looking weird things ... re-analyze all the stuff you can on various desert reference maps
and see what looks normal versus not").

Mock v1 picked each cell's metatile from its 3x3 neighbourhood of classes alone (canyon.py). Where the plan made a
shape MonoMyth never makes (a 2-wide pillar, a square ripple patch, a sharp river corner) it guessed, and the guesses
left seams. Here:
  * the corpus is every MonoMyth map on the canyon's tilesets (primary 0x87311dc, secondary 0x873147c): 0x86da4c
    (the pueblo strip), 0x86da68 (the forest's canyon edge), 0x86daf4 and 0x86db10 (the red canyon), 0x86db9c and
    0x86dbb8 (the lighthouse coast and its dunes);
  * "normal" is measured: every pair of side-by-side and over-and-under metatiles in the corpus is recorded; a pair
    that never occurs there is a seam (`seams()`), drawn on a heat map (`seam_map()`);
  * each cell may take any metatile the corpus puts at that class in that 3x3 neighbourhood (not just the commonest),
    and a solver picks among them so that every neighbouring pair is one the corpus has (`solve()`): arc consistency,
    then a fill that looks ahead one cell, the commonest choice first;
  * families are kept apart: the red rock (its colour, red minus green >= 40), the canyon's golden-red sand and its
    rippled dunes; the pale yellow sand, the yellow dunes and the brown rock of the other deserts are never used;
  * a neighbourhood the corpus never shows is reported (`unseen`), so the plan's shape there is changed, not guessed.
Classes: W rock top, U upper face, L lower face (a rock cell's depth above the ground below it: 3+, 2, 1), F sand,
r rippled dune, A water, x anything else (only ever a neighbour)."""
import os, sys, collections, pickle
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'mt_mirroh')); sys.path.insert(0, '/home/claude/mono')
CACHE = '/home/claude/scratch/anc2/tilesolve_corpus.pkl'
MAPS = (0x86da4c, 0x86da68, 0x86daf4, 0x86db10, 0x86db9c, 0x86dbb8)
VOCAB_MAPS = (0x86da4c, 0x86da68, 0x86daf4, 0x86db10)
N8 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
WATER_BEH = (0x10, 0x11, 0x12, 0x13, 0x15)

def norm(key):
    k = list(key); me = k[0]
    for d, (a, b) in ((1, (2, 4)), (3, (2, 5)), (6, (4, 7)), (8, (5, 7))):
        if not (k[a] == me and k[b] == me): k[d] = me
    return ''.join(k)

def rock_class(depth): return 'L' if depth == 1 else 'U' if depth == 2 else 'W'

class Corpus:
    def __init__(self):
        if os.path.exists(CACHE):
            self.__dict__.update(pickle.load(open(CACHE, 'rb'))); return
        import mm_render as MR
        from romlib import u16, off
        self.meta, self.beh, self.maps = {}, {}, []
        for a in MAPS:
            img, c, ts, L = MR.render(a); W, H = L['w'], L['h']
            sa, pa = off(L['secondary']['attr']), off(L['primary']['attr'])
            g = np.array([v & 0x3FF for v in c]).reshape(H, W); sol = np.array([(v >> 10) & 3 for v in c]).reshape(H, W)
            for m in set(g.ravel().tolist()):
                self.beh[m] = (u16(sa + 2 * (m - 512)) if m >= 512 else u16(pa + 2 * m)) & 0xFF; self.meta[m] = ts.meta(m)
            self.maps.append(dict(addr=a, g=g, sol=sol, W=W, H=H))
        for M in self.maps: M['cls'], M['prop'] = self._classes(M)
        self._finish_classes()
        self.H, self.V = collections.Counter(), collections.Counter()
        for M in self.maps:
            g = M['g']
            self.H.update(zip(g[:, :-1].ravel().tolist(), g[:, 1:].ravel().tolist()))
            self.V.update(zip(g[:-1, :].ravel().tolist(), g[1:, :].ravel().tolist()))
        self.samples = collections.defaultdict(collections.Counter)
        for M in self.maps:
            if M['addr'] not in VOCAB_MAPS: continue
            cls, g = M['cls'], M['g']; H, W = g.shape
            for y in range(1, H - 1):
                for x in range(1, W - 1):
                    k = cls[y, x]
                    if k == 'x' or M['prop'][y, x]: continue
                    self.samples[norm(k + ''.join(cls[y + dy, x + dx] for dx, dy in N8))][int(g[y, x])] += 1
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        pickle.dump({k: v for k, v in self.__dict__.items()}, open(CACHE, 'wb'))

    def rgb_mean(self, m): return self.meta[m].astype(int).reshape(-1, 3).mean(0)
    def red(self, m): t = self.rgb_mean(m); return t[0] - t[1] >= 40
    def greenish(self, m, frac=0.05):
        t = self.meta[m].astype(int)
        return ((t[..., 1] - t[..., 0] > 10) & (t[..., 1] > t[..., 2] + 10)).mean() > frac

    def material(self, m):
        """what a metatile is made of: A water, r the red dunes' ripples, F the golden-red sand (and anything green on
        it: plants are props), R red rock, x anything else (pale sand, yellow dunes, brown rock, grass, paths)"""
        b = self.beh[m]; t = self.rgb_mean(m); rg = t[0] - t[1]
        if b in WATER_BEH: return 'A'
        if self.greenish(m):                       # (a plant: what it grows on, from the rest of its pixels)
            f = self.meta[m].astype(int).reshape(-1, 3)
            g = (f[:, 1] - f[:, 0] > 10) & (f[:, 1] > f[:, 2] + 10)
            rest = f[~g].mean(0) if (~g).sum() > 20 else f.mean(0)
            return 'R' if rest[0] - rest[1] >= 48 else 'F'
        if b == 0x06: return 'r' if rg >= 35 else 'x'
        if b == 0x21: return 'F' if rg >= 25 else 'x'
        if rg >= 48: return 'R' if m < 0x2A0 else 'x'          # (0x2a0 on: the pueblo's adobe and planks)
        if rg >= 25 and t.mean() > 150: return 'F'
        return 'x'

    def _classes(self, M):
        """each cell's material (props: what they stand on); red rock's depth above the ground below it"""
        g = M['g']; H, W = g.shape
        mat = np.vectorize(self.material)(g)
        M['_mat0'] = mat
        return mat.copy(), np.zeros((H, W), bool)

    def _props(self):
        """a prop is a tile mostly found standing alone in another material (a boulder on the sand, a plant or a
        pot on the rock), or anything green; a prop cell takes the material round it"""
        alone, seen = collections.Counter(), collections.Counter()
        for M in self.maps:
            mat = M['_mat0']; g = M['g']; H, W = g.shape
            for y in range(1, H - 1):
                for x in range(1, W - 1):
                    n4 = [mat[y - 1, x], mat[y + 1, x], mat[y, x - 1], mat[y, x + 1]]
                    c = collections.Counter(n4).most_common(1)[0]
                    m = int(g[y, x]); seen[m] += 1
                    if c[1] >= 3 and c[0] != mat[y, x] and c[0] in 'FRr': alone[m] += 1
        self.proptiles = {m for m in seen if alone[m] / seen[m] > 0.5 or (self.greenish(m) and self.material(m) in 'FR')}
        for M in self.maps:
            mat = M['_mat0'].copy(); g = M['g']; H, W = g.shape
            prop = np.vectorize(lambda m: m in self.proptiles)(g)
            for y in range(H):
                for x in range(W):
                    if prop[y, x]:
                        n4 = [mat[q] for q in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)) if 0 <= q[0] < H and 0 <= q[1] < W and not prop[q]]
                        if n4: mat[y, x] = collections.Counter(n4).most_common(1)[0][0]
            depth = np.zeros((H, W), int)
            for y in range(H - 1, -1, -1):
                for x in range(W):
                    if mat[y, x] == 'R': depth[y, x] = 1 + (depth[y + 1, x] if y + 1 < H else 9)
            M['_mat'], M['_depth'], M['prop'], M['cls'] = mat, depth, prop, mat.copy()
            del M['_mat0']

    def _finish_classes(self):
        """red rock's classes by the tile: the canyon's walls are bands of an upper face over a lower face (seeds:
        0x210-0x212 over 0x218-0x21a), standing on sand, on dunes, on water or on a lower terrace of rock, so a rock
        cell's class cannot come from its depth; a tile is a lower face if what is above it is mostly an upper face,
        an upper face if what is below it is mostly a lower face; every other rock tile is rock top (W)"""
        self._props()
        U0, L0 = {0x210, 0x211, 0x212}, {0x218, 0x219, 0x21a}
        above, below = collections.defaultdict(collections.Counter), collections.defaultdict(collections.Counter)
        for M in self.maps:
            g = M['g']; H, W = g.shape
            for y in range(H - 1):
                for x in range(W): below[int(g[y, x])][int(g[y + 1, x])] += 1; above[int(g[y + 1, x])][int(g[y, x])] += 1
        frac = lambda c, S: sum(v for k, v in c.items() if k in S) / max(1, sum(c.values()))
        self.rockcls = {}
        for M in self.maps:
            for (y, x) in zip(*np.nonzero(M['_mat'] == 'R')):
                m = int(M['g'][y, x])
                if m in self.rockcls: continue
                self.rockcls[m] = 'U' if m in U0 or frac(below[m], L0) > 0.5 else 'L' if m in L0 or frac(above[m], U0) > 0.5 else 'W'
        for M in self.maps:
            cls = M['cls']
            for (y, x) in zip(*np.nonzero(M['_mat'] == 'R')):
                cls[y, x] = 'W' if M['prop'][y, x] else self.rockcls[int(M['g'][y, x])]
            del M['_mat'], M['_depth']

    def domain(self, key):
        """(tiles with weights, seen?) for a cell of this neighbourhood: the tiles MonoMyth puts in exactly this
        neighbourhood first (weight x10000), then those it puts where the four sides match (x100), then any tile of
        the class (x1); the pairs decide among them"""
        key = norm(key)
        if not hasattr(self, '_orth'):
            self._orth = collections.defaultdict(collections.Counter); self._cls = collections.defaultdict(collections.Counter)
            for k, v in self.samples.items():
                self._orth[k[0] + k[2] + k[4] + k[5] + k[7]].update(v); self._cls[k[0]].update(v)
        out = collections.Counter()
        for m, n in self._cls[key[0]].items(): out[m] += n
        for m, n in self._orth[key[0] + key[2] + key[4] + key[5] + key[7]].items(): out[m] += 100 * n
        for m, n in self.samples.get(key, {}).items(): out[m] += 10000 * n
        return out, key in self.samples

_C = None
def corpus():
    global _C
    if _C is None: _C = Corpus()
    return _C

def keys_of(cls):
    """each cell's 3x3 class key (out of bounds: the cell's own class)"""
    H, W = cls.shape; out = {}
    for y in range(H):
        for x in range(W):
            me = cls[y, x]
            nb = [cls[y + dy, x + dx].replace('-', 'x') if 0 <= x + dx < W and 0 <= y + dy < H else me for dx, dy in N8]
            nb = [(me if me in 'FrA' else 'W') if c == 'K' else c for c in nb]   # (the sky: the ground carries on into it, cut by the rim; rock is rock top behind it)
            out[(x, y)] = me + ''.join(nb)
    return out

def solve(cls, fixed=None, free=None):
    """cls: (H, W) array of class letters ('-' a cell left out, e.g. under the sky). fixed: {(x, y): metatile}.
    free: cells whose tile does not matter to the solver (left out). Returns (grid of metatiles or -1, report)."""
    C = corpus(); fixed = fixed or {}; free = free or set()
    H, W = cls.shape; keys = keys_of(cls)
    dom, wt, unseen = {}, {}, []
    for y in range(H):
        for x in range(W):
            p = (x, y)
            if p in fixed: dom[p] = {fixed[p]}; wt[p] = {fixed[p]: 1}; continue
            if cls[y, x] in '-xK' or p in free: continue
            d, ok = C.domain(keys[p])
            if not ok: unseen.append(p)
            fam = {m: k for m, k in d.items() if cls[y, x] not in 'WUL' or C.red(m)}
            dom[p] = set(fam) or set(d); wt[p] = fam or dict(d)
    okH = lambda a, b: (a, b) in C.H
    okV = lambda a, b: (a, b) in C.V
    def nbrs(p):
        x, y = p
        for q, rel in (((x - 1, y), 'L'), ((x + 1, y), 'R'), ((x, y - 1), 'U'), ((x, y + 1), 'D')):
            if q in dom: yield q, rel
    def compat(a, b, rel):         # a at p, b at its neighbour in direction rel
        return okH(b, a) if rel == 'L' else okH(a, b) if rel == 'R' else okV(b, a) if rel == 'U' else okV(a, b)
    # arc consistency (a cell whose domain would empty keeps it: that cell is a conflict, reported)
    from collections import deque
    conflicts = set()
    q = deque(dom.keys())
    inq = set(dom.keys())
    while q:
        p = q.popleft(); inq.discard(p)
        for nq, rel in nbrs(p):
            keep = {a for a in dom[p] if any(compat(a, b, rel) for b in dom[nq])}
            if not keep: conflicts.add(p); continue
            if keep != dom[p]:
                dom[p] = keep
                for r, _ in nbrs(p):
                    if r not in inq: q.append(r); inq.add(r)
    # fill: north-west to south-east, the commonest tile that agrees with what is placed and leaves each unplaced
    # neighbour a choice
    out = np.full((H, W), -1, int)
    for y in range(H):
        for x in range(W):
            p = (x, y)
            if p not in dom: continue
            def score(a):
                bad = 0
                for nq, rel in nbrs(p):
                    v = out[nq[1], nq[0]]
                    if v >= 0: bad += 0 if compat(a, v, rel) else 1
                    elif not any(compat(a, b, rel) for b in dom[nq]): bad += 1
                return (bad, -wt[p].get(a, 0))
            out[y, x] = min(sorted(dom[p]), key=score)
    return out, dict(unseen=unseen, conflicts=sorted(conflicts))

def seams(grid):
    """every neighbouring pair of placed metatiles the corpus never shows: [((x, y), (x2, y2))]"""
    C = corpus(); H, W = grid.shape; bad = []
    for y in range(H):
        for x in range(W):
            a = grid[y, x]
            if a < 0: continue
            if x + 1 < W and grid[y, x + 1] >= 0 and (a, grid[y, x + 1]) not in C.H: bad.append(((x, y), (x + 1, y)))
            if y + 1 < H and grid[y + 1, x] >= 0 and (a, grid[y + 1, x]) not in C.V: bad.append(((x, y), (x, y + 1)))
    return bad

def render(grid, S=16):
    C = corpus(); H, W = grid.shape; img = np.zeros((H * S, W * S, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            if grid[y, x] >= 0: img[y * S:y * S + S, x * S:x * S + S] = C.meta[int(grid[y, x])]
    return img

def seam_map(img, bad, extra=(), S=16):
    """the picture darkened, each seam a red bar across the shared edge, each cell in `extra` boxed in magenta"""
    out = (img.astype(int) * 0.55).astype(np.uint8)
    for (x, y), (x2, y2) in bad:
        if x2 > x: out[y * S + 2:y * S + S - 2, x2 * S - 2:x2 * S + 2] = (255, 40, 40)
        else: out[y2 * S - 2:y2 * S + 2, x * S + 2:x * S + S - 2] = (255, 40, 40)
    for (x, y) in extra:
        out[y * S, x * S:x * S + S] = out[y * S + S - 1, x * S:x * S + S] = (255, 0, 255)
        out[y * S:y * S + S, x * S] = out[y * S:y * S + S, x * S + S - 1] = (255, 0, 255)
    return out

def ref_block(addr, x0, y0, x1, y1):
    """a corpus map's metatiles and classes over a box: ({(dx, dy): metatile}, {(dx, dy): class})"""
    C = corpus(); M = [m for m in C.maps if m['addr'] == addr][0]
    t, k = {}, {}
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1): t[(x - x0, y - y0)] = int(M['g'][y, x]); k[(x - x0, y - y0)] = M['cls'][y, x]
    return t, k

if __name__ == '__main__':
    # self-test: the corpus maps themselves have no seams; re-solving a canyon map from its own classes
    C = corpus()
    print('pairs: %d across, %d down; neighbourhoods: %d' % (len(C.H), len(C.V), len(C.samples)))
    M = [m for m in C.maps if m['addr'] == 0x86daf4][0]
    print('seams in 0x86daf4 itself:', len(seams(M['g'])))
    cls = M['cls'].copy()
    g, rep = solve(cls)
    print('re-solved 0x86daf4 from its classes: seams', len(seams(g)), 'unseen', len(rep['unseen']), 'conflicts', len(rep['conflicts']))
    from PIL import Image
    Image.fromarray(render(g)).save('/home/claude/scratch/anc2/resolve_86daf4.png')
