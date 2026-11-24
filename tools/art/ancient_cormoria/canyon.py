"""MonoMyth's red-rock canyon country (its maps 0x86daf4 and 0x86db10: red mesas, rippled golden dunes, a river) as a
construction vocabulary for the Ancient Cormoria slip (plan_slip.py).

How it builds (studied): red rock masses whose tops are rough red stone and whose south faces are two rows of banded
cliff (the lower row at the foot, the upper above it), their sides and corners rounded by their own pieces; golden
sand floors with patches of rippled dune sand (their own edge pieces); a river with its own shores.
As mt.py / mtout.py do: each cell's metatile learned from these maps by its 3x3 neighbourhood of classes, here
W rock top, U upper face, L lower face (a rock cell's distance above the sand below it), F sand, r rippled sand,
A water; corner diagonals normalised; the commonest taken. Props (plants, small rocks: small solid clusters and
anything green) are not learned."""
import os, sys, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'mt_mirroh')); sys.path.insert(0, '/home/claude/mono')
import mm_render as MR
from romlib import u16, off
MAPS = (0x86daf4, 0x86db10)
N8 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
SAND = 0x24B
NOT_FLOOR = {0x196, 0x18E, 0x266, 0x1, 0x3, 0x6, 0x88, 0x91, 0xC, 0xD}   # (a pier's posts, flowers, pale grass: not sand)

def norm(key):
    k = list(key); me = k[0]
    for d, (a, b) in ((1, (2, 4)), (3, (2, 5)), (6, (4, 7)), (8, (5, 7))):
        if not (k[a] == me and k[b] == me): k[d] = me
    return ''.join(k)

def rock_class(depth):
    return 'L' if depth == 1 else 'U' if depth == 2 else 'W'

class Vocab:
    def __init__(self):
        self.samples = collections.defaultdict(collections.Counter); self.ts = None
        for a in MAPS:
            img, c, ts, L = MR.render(a); self.ts = self.ts or ts; W, H = L['w'], L['h']
            sa, pa = off(L['secondary']['attr']), off(L['primary']['attr'])
            beh = lambda m: (u16(sa + 2 * (m - 512)) if m >= 512 else u16(pa + 2 * m)) & 0xFF
            solid = lambda x, y: (c[y * W + x] >> 10) & 3
            water = lambda m: beh(m) in (0x15, 0x13, 0x10, 0x11, 0x12)
            S = {(i % W, i // W) for i, v in enumerate(c) if (v >> 10) & 3 and not water(v & 0x3FF)}
            comp = {}; prop = set()
            for p in S:
                if p in comp: continue
                st, cc = [p], [p]; comp[p] = 1
                while st:
                    x, y = st.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        q = (x + dx, y + dy)
                        if q in S and q not in comp: comp[q] = 1; st.append(q); cc.append(q)
                if len(cc) <= 6: prop.update(cc)
            cls = {}
            for y in range(H):
                for x in range(W):
                    m = c[y * W + x] & 0x3FF; b = beh(m)
                    isprop = (x, y) in prop or self.green(m)
                    if water(m): k = 'A'
                    elif (x, y) in S and (x, y) not in prop:
                        d = 1
                        while y + d < H and (x, y + d) in S and (x, y + d) not in prop: d += 1
                        k = rock_class(d)
                    elif b == 0x06: k = 'r'
                    else: k = 'F'
                    cls[(x, y)] = (k, m, isprop)
            get = lambda x, y: cls[(x, y)][0] if (x, y) in cls else 'W'
            for y in range(1, H - 1):
                for x in range(1, W - 1):
                    k, m, isprop = cls[(x, y)]
                    if isprop or (k in 'Fr' and (m in NOT_FLOOR or self.green(m, 0.01))): continue
                    key = norm(k + ''.join(get(x + dx, y + dy) for dx, dy in N8))
                    self.samples[key][m] += 1
    def green(self, m, frac=0.05):
        t = self.ts.meta(m).astype(int)
        return ((t[..., 1] - t[..., 0] > 10) & (t[..., 1] > t[..., 2] + 10)).mean() > frac
    def pick(self, key):
        key = norm(key)
        if key not in self.samples:
            w = [1, 3, 1, 3, 3, 1, 3, 1]
            cand = [k for k in self.samples if k[0] == key[0]]
            best = min(cand, key=lambda k: (sum(wi for wi, a, b in zip(w, k[1:], key[1:]) if a != b), -sum(self.samples[k].values())))
            self.samples[key] = self.samples[best]; self.missed = getattr(self, 'missed', 0) + 1
        return self.samples[key].most_common(1)[0][0]
    def meta(self, m): return self.ts.meta(m)
