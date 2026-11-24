"""MonoMyth's Glittering Grotto (mapsec 56; its two floors 0x86ddcc, 0x86dde8) as a tile vocabulary: every cell
classed rock (R) or open (O), each tile's 8-neighbour pattern learned, so any R/O grid can be drawn in the
Grotto's own rounded rock masses. Crystals, carts and other props are kept apart (they are placed by hand).
MonoMyth's blockdata is LZ77-compressed (mm_render.py)."""
import os, sys, random, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, '/home/claude/mono')
import mm_render as MR
FLOORS = (0x86ddcc, 0x86dde8)
# props (not rock, not plain floor): crystals small and large, carts, the bucket, signs, ladders, stairs, exit mat, rocks
PROPS = set(range(0x232, 0x247)) | set(range(0x248, 0x27d)) | {0x280, 0x281, 0x282, 0x283, 0x288, 0x289, 0x28a, 0x28b} \
    | set(range(0x290, 0x2a5)) | {0x202, 0x20a, 0x203, 0x206, 0x207, 0x229, 0x22f, 0x247, 0x2ad, 0x2ae, 0x2af, 0x2d4,
       0x2d5, 0x2d6, 0x2d7, 0x2df, 0x2e6, 0x2e7, 0x2eb, 0x2ec, 0x2fb, 0x2fc, 0x201, 0x2c5, 0x2c6}
N8 = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
WEIGHT = [1, 3, 1, 3, 3, 1, 3, 1]

def norm(key):
    """a diagonal only matters at a corner: where both orthogonals beside it match the cell itself."""
    k = list(key); me = k[0]
    # N8 order: NW N NE W E SW S SE -> key[1..8]
    for d, (a, b) in ((1, (2, 4)), (3, (2, 5)), (6, (4, 7)), (8, (5, 7))):
        if not (k[a] == me and k[b] == me): k[d] = me
    return ''.join(k)

def keys(get, x, y):
    """three keys, most specific first: the 3x5 window (two rows up and down: the Grotto's faces are two rows tall),
    the 3x3 with the cells two above and below, the 3x3 (corner diagonals normalised)."""
    k9 = norm(get(x, y) + ''.join(get(x + dx, y + dy) for dx, dy in N8))
    k11 = k9 + get(x, y - 2) + get(x, y + 2)
    k15 = k11 + ''.join(get(x + dx, y + dy) for dy in (-2, 2) for dx in (-1, 1))
    return k15, k11, k9

class Vocab:
    def __init__(self):
        self.ts = None; self.samples = collections.defaultdict(collections.Counter)
        self.maps = []
        for a in FLOORS:
            img, c, ts, L = MR.render(a); self.ts = ts; W, H = L['w'], L['h']
            self.maps.append((img, c, W, H))
            cls = {}
            for y in range(H):
                for x in range(W):
                    v = c[y * W + x]; m = v & 0x3FF
                    cls[(x, y)] = 'R' if ((v >> 10) & 3) and m not in PROPS else 'O'
            get = lambda x, y: cls.get((x, y), 'R')
            self.cls = getattr(self, 'cls', []) + [(cls, c, W, H)]
        # each tile's own side: floor tiles are mostly walkable in the Grotto, rock tiles mostly not; a cell only
        # learns tiles of its own side (the Grotto has a few walkable-looking blocked cells and the reverse)
        side = collections.defaultdict(collections.Counter)
        for cls, c, W, H in self.cls:
            for (x, y), k in cls.items(): side[c[y * W + x] & 0x3FF][k] += 1
        self.side = {m: cnt.most_common(1)[0][0] for m, cnt in side.items()}
        for cls, c, W, H in self.cls:
            get = lambda x, y: cls.get((x, y), 'R')
            for y in range(1, H - 1):
                for x in range(1, W - 1):
                    m = c[y * W + x] & 0x3FF
                    if m in PROPS or self.side[m] != cls[(x, y)]: continue
                    for k in keys(get, x, y): self.samples[k][m] += 1
    def pick_at(self, get, x, y, rnd):
        """the Grotto's tile for the cell's surroundings, at the most specific key it has seen; level used returned."""
        for lvl, k in enumerate(keys(get, x, y)):
            if k in self.samples:
                cnt = self.samples[k]; ids = list(cnt)
                return rnd.choices(ids, [cnt[i] for i in ids])[0], lvl
        return self.pick(keys(get, x, y)[2], rnd), 3
    def pick(self, key, rnd):
        """the Grotto's tile for an R/O pattern (self + 8 neighbours); nearest pattern if never seen."""
        key = norm(key)
        if key not in self.samples:
            self.missed = getattr(self, 'missed', 0) + 1
            best = min((k for k in self.samples if k[0] == key[0]),
                       key=lambda k: (sum(w for w, a, b in zip(WEIGHT, k[1:], key[1:]) if a != b), -sum(self.samples[k].values())))
            self.samples[key] = self.samples[best]
        cnt = self.samples[key]; ids = list(cnt); w = [cnt[i] for i in ids]
        return rnd.choices(ids, w)[0]
    def meta(self, m): return self.ts.meta(m)

def cutout(V, mi, box):
    """a prop cut from the Grotto (map mi, cells box x0,y0,x1,y1 inclusive): RGBA, where it differs from plain floor."""
    img, c, W, H = V.maps[mi]; x0, y0, x1, y1 = box
    rgb = img[y0 * 16:(y1 + 1) * 16, x0 * 16:(x1 + 1) * 16].copy()
    fl = np.tile(V.meta(0x200), (y1 - y0 + 1, x1 - x0 + 1, 1))
    a = (np.abs(rgb.astype(int) - fl.astype(int)).sum(2) > 0)
    return rgb, a
BIG_CRYSTALS = [(0, (16, 10, 18, 11)), (0, (44, 17, 46, 19)), (0, (27, 29, 29, 31)), (0, (4, 42, 6, 44)),
                (1, (5, 3, 6, 5)), (1, (24, 25, 26, 27)), (1, (34, 45, 36, 47))]
SMALL_CRYSTALS = list(range(0x232, 0x247)) + list(range(0x290, 0x2a5))
