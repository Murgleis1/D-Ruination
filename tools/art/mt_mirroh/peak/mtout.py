"""MonoMyth's Mt. Thunder outdoors (0x86d6b0 0x86d678 0x86d694 0x86d6e8 0x86d624) and its summit, the Peak of Kings
(0x86d758), as a construction vocabulary for Mirroh Peak (user 2026-11-24: "Mt. Thunder style like 1F"; "re-do that
whole final climb to resemble Mt. Thunder's peak climb more").

How they build (studied; assets/mt_mirroh_reference/mt_thunder_outdoor_study.png): pale snow ground; one-tile bands of
dark rock under a snowy crest, stacked row on row where the mountain is thick, ended and turned by their own pieces;
stairs straight through a band; blue ice grass; rivers with their own shores falling through the bands; around the
Peak of Kings, nothing (black: the sky, which this map paints).
As mt.py does for the interiors: each cell's metatile is learned from these maps by its 3x3 neighbourhood of classes
(K sky, W rock, F snow, G ice grass, A water, S stairs), corner diagonals normalised, the commonest taken. Props
(pines, boulders, rocks, flowers: small solid clusters and anything green) are not learned (placed on their own)."""
import os, sys, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, '/home/claude/mono')
import mm_render as MR
from romlib import u16, off
OUT = (0x86d6b0, 0x86d678, 0x86d694, 0x86d6e8, 0x86d624)
POK = 0x86d758
N8 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
SNOW, GRASS, WATER = 0xFE, 0xF0, 0x259

def norm(key):
    k = list(key); me = k[0]
    for d, (a, b) in ((1, (2, 4)), (3, (2, 5)), (6, (4, 7)), (8, (5, 7))):
        if not (k[a] == me and k[b] == me): k[d] = me
    return ''.join(k)

class Vocab:
    def __init__(self, maps=OUT + (POK,)):
        self.samples = collections.defaultdict(collections.Counter); self.ts = {}; self.cls_of = {}
        for a in maps:
            img, c, ts, L = MR.render(a); W, H = L['w'], L['h']; src = 'pok' if a == POK else 'out'
            self.ts.setdefault(src, ts)
            sa, pa = off(L['secondary']['attr']), off(L['primary']['attr'])
            beh = lambda m: (u16(sa + 2 * (m - 512)) if m >= 512 else u16(pa + 2 * m)) & 0xFF
            green = lambda m: self._green(src, m)
            solid = {(i % W, i // W) for i, v in enumerate(c) if (v >> 10) & 3 and (v & 0x3FF) != 0 and beh(v & 0x3FF) not in (0x5B, 0x5A)}
            comp = {}; prop = set()
            for p in solid:
                if p in comp: continue
                st, cc = [p], [p]; comp[p] = 1
                while st:
                    x, y = st.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        q = (x + dx, y + dy)
                        if q in solid and q not in comp: comp[q] = 1; st.append(q); cc.append(q)
                if len(cc) <= 6: prop.update(cc)
            cls = {}
            for y in range(H):
                for x in range(W):
                    m = c[y * W + x] & 0x3FF; b = beh(m); isprop = (x, y) in prop or (green(m) and b != 0x5A)
                    if m == 0: k = 'K'
                    elif b == 0x4F: k = 'S'
                    elif b in (0x15, 0x13): k = 'A'
                    elif b == 0x5A: k = 'G'
                    elif isprop or b == 0x5B or not (c[y * W + x] >> 10) & 3: k = 'F'
                    else: k = 'W'
                    if 0x49 <= b <= 0x4E: isprop = True                       # (sideways stairs: not learned)
                    cls[(x, y)] = (k, m, isprop)
            get = lambda x, y: cls[(x, y)][0] if (x, y) in cls else 'W'
            for y in range(1, H - 1):
                for x in range(1, W - 1):
                    k, m, isprop = cls[(x, y)]
                    if isprop: continue
                    key = norm(k + ''.join(get(x + dx, y + dy) for dx, dy in N8))
                    self.samples[key][(src, m)] += 1
    def _green(self, src, m):
        t = self.ts[src].meta(m).astype(int)
        return ((t[..., 1] - t[..., 0] > 20) & (t[..., 1] > t[..., 2] + 8)).mean() > 0.04
    def pick(self, key):
        key = norm(key)
        if key not in self.samples:
            w = [1, 3, 1, 3, 3, 1, 3, 1]
            best = min((k for k in self.samples if k[0] == key[0]),
                       key=lambda k: (sum(wi for wi, a, b in zip(w, k[1:], key[1:]) if a != b), -sum(self.samples[k].values())))
            self.samples[key] = self.samples[best]; self.missed = getattr(self, 'missed', 0) + 1
        return self.samples[key].most_common(1)[0][0]
    def meta(self, sm): return self.ts[sm[0]].meta(sm[1])
