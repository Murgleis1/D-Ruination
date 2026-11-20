"""Seam repair by adjacency: fill chosen cells of a metatile grid with ids that agree with their neighbours the way
the source game's own maps do (counts of horizontal and vertical neighbour pairs over a corpus of maps sharing the
tilesets). Used where a lifted block of a map meets new ground: the cliff bands, banks and lips get proper ends
instead of being cut off. Iterated conditional modes with restarts; fixed cells are never changed.
"""
import math, random
import numpy as np
from collections import Counter, defaultdict

class Adjacency:
    def __init__(self, grids):
        self.h = Counter(); self.v = Counter(); self.n = Counter()
        for g in grids:
            g = np.asarray(g)
            for a, b in zip(g[:, :-1].ravel(), g[:, 1:].ravel()): self.h[(int(a), int(b))] += 1
            for a, b in zip(g[:-1, :].ravel(), g[1:, :].ravel()): self.v[(int(a), int(b))] += 1
            for a in g.ravel(): self.n[int(a)] += 1
        self.right = defaultdict(set); self.left = defaultdict(set); self.down = defaultdict(set); self.up = defaultdict(set)
        for (a, b) in self.h: self.right[a].add(b); self.left[b].add(a)
        for (a, b) in self.v: self.down[a].add(b); self.up[b].add(a)
    def pair(self, c, a, b):
        k = c[(a, b)]
        if k == 0: return -12.0
        return math.log(k / (self.n[a] + 1)) + math.log(k / (self.n[b] + 1)) * 0.5

    def score(self, g, x, y, v):
        H, W = g.shape; s = 0.0
        if x > 0 and g[y, x - 1] >= 0: s += self.pair(self.h, int(g[y, x - 1]), v)
        if x < W - 1 and g[y, x + 1] >= 0: s += self.pair(self.h, v, int(g[y, x + 1]))
        if y > 0 and g[y - 1, x] >= 0: s += self.pair(self.v, int(g[y - 1, x]), v)
        if y < H - 1 and g[y + 1, x] >= 0: s += self.pair(self.v, v, int(g[y + 1, x]))
        return s

def fill(adj, grid, free, iters=40, restarts=6, seed=0):
    """grid: 2-D int array of ids (any value at free cells); free: list of (x, y) to choose. Returns the best grid."""
    rng = random.Random(seed); best = None; best_s = -1e18
    vocab = list(adj.n)
    for r in range(restarts):
        g = np.array(grid, dtype=int).copy()
        for (x, y) in free: g[y, x] = -1
        order = list(free)
        for it in range(iters):
            rng.shuffle(order); changed = False
            for (x, y) in order:
                H, W = g.shape; cand = set()
                if x > 0 and g[y, x - 1] >= 0: cand |= adj.right[int(g[y, x - 1])]
                if x < W - 1 and g[y, x + 1] >= 0: cand |= adj.left[int(g[y, x + 1])]
                if y > 0 and g[y - 1, x] >= 0: cand |= adj.down[int(g[y - 1, x])]
                if y < H - 1 and g[y + 1, x] >= 0: cand |= adj.up[int(g[y + 1, x])]
                if not cand: cand = set(vocab)
                cand = list(cand); rng.shuffle(cand)
                v = max(cand, key=lambda c: adj.score(g, x, y, c) + rng.random() * (0.3 if it < iters // 2 else 0))
                if v != g[y, x]: g[y, x] = v; changed = True
            if not changed and it > 3: break
        s = sum(adj.score(g, x, y, int(g[y, x])) for (x, y) in free)
        if s > best_s: best, best_s = g, s
    return best, best_s
