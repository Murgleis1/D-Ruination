"""MonoMyth's Mt. Thunder interiors as a corpus for the tile solver (tools/art/ancient_cormoria/tilesolve.py), so B1F
is built the way the Ancient Cormoria slip was (user 2026-11-24, on the slip's first mock: "re-analyze ... and see what
looks normal versus not"): each cell a tile Mt. Thunder puts in that neighbourhood, each neighbouring pair one Mt.
Thunder has. Same maps and classes as 1F's vocabulary (tools/art/mt_mirroh/cave/mt.py, which 1F was built from):
W wall (the slate bands with their snowy crests), F floor (pale smooth ice), A water, S stairs; props (boulders,
stalagmites, candles: small solid clusters) never a class's sample."""
import os, sys, collections, pickle
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..')); sys.path.insert(0, os.path.join(HERE, '..', '..', 'ancient_cormoria'))
sys.path.insert(0, '/home/claude/mono')
import tilesolve as T
MAPS = (0x86d608, 0x86d640, 0x86d65c, 0x86d6cc, 0x86d704, 0x86d73c)   # (0x86d774 is on another primary: left out)
STAIRS = {0x21C, 0x21D}
CACHE = '/home/claude/scratch/b1f/mtcorpus.pkl'

class MTCorpus(T.Corpus):
    def __init__(self):
        if os.path.exists(CACHE):
            self.__dict__.update(pickle.load(open(CACHE, 'rb'))); return
        import mm_render as MR
        from romlib import u16, off
        self.meta, self.beh, self.maps = {}, {}, []
        self.H, self.V = collections.Counter(), collections.Counter()
        self.samples = collections.defaultdict(collections.Counter)
        wl = {}
        for a in MAPS:
            img, c, ts, L = MR.render(a); W, H = L['w'], L['h']
            sa, pa = off(L['secondary']['attr']), off(L['primary']['attr'])
            g = np.array([v & 0x3FF for v in c]).reshape(H, W); sol = np.array([(v >> 10) & 3 for v in c]).reshape(H, W)
            for m in set(g.ravel().tolist()):
                self.beh[m] = (u16(sa + 2 * (m - 512)) if m >= 512 else u16(pa + 2 * m)) & 0xFF; self.meta[m] = ts.meta(m)
            solid = sol > 0
            # props: solid clusters of six cells or fewer
            from scipy.ndimage import label
            lab, n = label(solid); sizes = np.bincount(lab.ravel())
            prop = solid & (sizes[lab] <= 6)
            cls = np.full((H, W), 'F', dtype='<U1')
            for y in range(H):
                for x in range(W):
                    m = int(g[y, x]); b = self.beh[m]
                    if m in STAIRS: cls[y, x] = 'S'
                    elif b in (0x15, 0x13): cls[y, x] = 'A'
                    elif solid[y, x] and not prop[y, x]:
                        if m not in wl:
                            t = self.meta[m].astype(int)
                            warm = ((t[:, :, 0] > t[:, :, 2] + 40) & (t[:, :, 0] > 120)).mean()
                            wl[m] = warm < 0.02
                        cls[y, x] = 'W' if wl[m] else 'x'           # (flagstone landings, torches: not wall)
            self.maps.append(dict(addr=a, g=g, sol=sol, cls=cls, prop=prop, W=W, H=H))
            self.H.update(zip(g[:, :-1].ravel().tolist(), g[:, 1:].ravel().tolist()))
            self.V.update(zip(g[:-1, :].ravel().tolist(), g[1:, :].ravel().tolist()))
            for y in range(1, H - 1):
                for x in range(1, W - 1):
                    if cls[y, x] == 'x' or prop[y, x]: continue
                    self.samples[T.norm(cls[y, x] + ''.join(cls[y + dy, x + dx] for dx, dy in T.N8))][int(g[y, x])] += 1
        self.proptiles = set()
        for M in self.maps:
            for (y, x) in zip(*np.nonzero(M['prop'])): self.proptiles.add(int(M['g'][y, x]))
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        pickle.dump(dict(self.__dict__), open(CACHE, 'wb'))
    def red(self, m): return True                         # (the solver's family filter: one family here)


_C = None
def corpus():
    global _C
    if _C is None: _C = MTCorpus()
    return _C

if __name__ == '__main__':
    C = corpus()
    print('pairs %d / %d, neighbourhoods %d, props %d' % (len(C.H), len(C.V), len(C.samples), len(C.proptiles)))
    M = C.maps[2]
    g, rep = T.solve(M['cls'].copy(), C=C)
    print('re-solve 0x86d65c: seams', len(T.seams(g, C)), 'unseen', len(rep['unseen']), 'conflicts', len(rep['conflicts']))
    from PIL import Image
    Image.fromarray(T.seam_map(T.render(g, C=C), T.seams(g, C), rep['conflicts'])).save('/home/claude/scratch/b1f/mt_selftest.png')
