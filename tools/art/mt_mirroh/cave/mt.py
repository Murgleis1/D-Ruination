"""MonoMyth's Mt. Thunder interiors (mapsecs 59/73/126: 0x86d608 0x86d640 0x86d65c 0x86d6cc 0x86d704 0x86d73c 0x86d774)
as a construction vocabulary (user 2026-11-23: "look at other indoor caves and study them more and fix the broken
cliffs, and stairs and water patterns"; "a smoother better contrasting ground").

How Mt. Thunder builds (studied from its maps; assets/mt_mirroh_reference/cave_study_mt_thunder.png):
  * walls are one-tile bands of dark slate with a snowy crest (0x211), stacked row on row for thicker rock, ended and
    turned by their own corner and side pieces; every other cell is pale smooth ice floor (0x209);
  * stairs (0x21C/0x21D, two wide, rock-stairs behaviour) run straight through every band of a wall, one pair a row;
  * water sits between bands: plain water (0x259), its shore rows and sides (0x25C bottom, 0x258/0x25A sides, corners)
    against floor; a band directly above or below water needs no shore;
  * bridges are planks with rails (0x230 top rail, 0x231 deck, 0x233 bottom rail).
Each cell's tile is learned from these maps by its 3x3 neighbourhood of classes (W wall, F floor, A water, S stairs),
corner diagonals normalised, the commonest tile taken (no random mixing: the same shape always draws the same way)."""
import os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, '/home/claude/mono')
import mm_render as MR
from romlib import u16, off
MAPS = (0x86d608, 0x86d640, 0x86d65c, 0x86d6cc, 0x86d704, 0x86d73c, 0x86d774)
STAIRS = {0x21C, 0x21D}
N8 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
FLOOR, BAND = 0x209, 0x211

def norm(key):
    k = list(key); me = k[0]
    for d, (a, b) in ((1, (2, 4)), (3, (2, 5)), (6, (4, 7)), (8, (5, 7))):
        if not (k[a] == me and k[b] == me): k[d] = me
    return ''.join(k)

class Vocab:
    def __init__(self):
        self.samples = collections.defaultdict(collections.Counter); self.ts = None; self._wl = {}
        for a in MAPS:
            img, c, ts, L = MR.render(a); self.ts = self.ts or ts; W, H = L['w'], L['h']
            sa, pa = off(L['secondary']['attr']), off(L['primary']['attr'])
            beh = lambda m: (u16(sa + 2 * (m - 512)) if m >= 512 else u16(pa + 2 * m)) & 0xFF
            solid = {(i % W, i // W) for i, v in enumerate(c) if (v >> 10) & 3}
            # props: small solid clusters (boulders, stalagmites, candles), not walls
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
                    m = c[y * W + x] & 0x3FF; b = beh(m)
                    if m in STAIRS: k = 'S'
                    elif b in (0x15, 0x13): k = 'A'
                    elif (x, y) in solid and (x, y) not in prop: k = 'W'
                    else: k = 'F'
                    cls[(x, y)] = (k, m, (x, y) in prop)
            get = lambda x, y: cls[(x, y)][0] if (x, y) in cls else 'W'
            for y in range(1, H - 1):
                for x in range(1, W - 1):
                    k, m, isprop = cls[(x, y)]
                    if isprop: continue
                    if k == 'W' and not self.wall_like(m): continue     # (flagstone landings, torches: not wall)
                    key = norm(k + ''.join(get(x + dx, y + dy) for dx, dy in N8))
                    self.samples[key][m] += 1
    def wall_like(self, m):
        if m not in self._wl:
            import numpy as np
            t = self.ts.meta(m).astype(int); lum = t.mean(2)
            warm = ((t[:, :, 0] > t[:, :, 2] + 40) & (t[:, :, 0] > 120)).mean()
            self._wl[m] = lum.mean() < 150 and warm < 0.02
        return self._wl[m]
    def pick(self, key):
        key = norm(key)
        if key not in self.samples:
            w = [1, 3, 1, 3, 3, 1, 3, 1]
            best = min((k for k in self.samples if k[0] == key[0]),
                       key=lambda k: (sum(wi for wi, a, b in zip(w, k[1:], key[1:]) if a != b), -sum(self.samples[k].values())))
            self.samples[key] = self.samples[best]; self.missed = getattr(self, 'missed', 0) + 1
        return self.samples[key].most_common(1)[0][0]
    def meta(self, m): return self.ts.meta(m)
