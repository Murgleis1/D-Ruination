"""Gate before building Pelluca's tilesets: do the approved tiles' colours pack
into the engine's 13 BG palettes (6 primary + 7 secondary) x 15 colours?

Every 8x8 tile must take ALL its colours from ONE palette, so the real limit is
a packing problem, not a colour count. Greedy: biggest colour sets first, each
placed in the palette that grows least while staying <= 15.
"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import budget_terrain as bt
from romlib import *
from PIL import Image

def selection():
    """Return {group: set(tile bytes)} for the approved, budget-closed set."""
    rare = {i: m for i, m, _ in json.load(open('/home/claude/scratch/wa_rare.json'))}
    drop = {rare[i] for i in [1,2,3,4,5,7,8,9,10,11,31,35,36,51,52,58,49,50,48,45,46,56,57,59,60,
                              14,15,16,28,29,30,32,33,34]}
    WA = bt.WA; L = bt.ctx(WA)[0]; mo = off(L['map']); W = L['w']
    G = {}
    t = set()
    for y in range(9, 46):
        for x in range(W):
            if any(a <= x <= b and c <= y <= d for a, c, b, d in bt.WA_BUILDINGS): continue
            if (u16(mo + (y * W + x) * 2) & 0x3ff) in drop: continue
            t |= bt.region_tiles(WA, x, y, x, y)
    G['terrain: Wood Avens'] = t
    for n, a, box, ex in bt.REGIONS:
        if n[0] in 'GJ': G['terrain: ' + n] = bt.region_tiles(a, *box, exclude=ex)
    FE = 0x86960c
    for n, a, box in [('Academy', WA, (18, 26, 24, 33)), ('Cadmus house', WA, (5, 28, 11, 32)),
                      ('Lab tower', WA, (15, 10, 20, 14)), ('Residence', WA, (5, 20, 11, 24)),
                      ('Tavern (FE G)', FE, (37, 40, 44, 47)), ('Guardhouse (FE gate)', FE, (27, 12, 34, 18))]:
        G[n] = bt.region_tiles(a, *box)
    G['Church (Evernahn)'] = church_tiles()
    return G

def church_tiles():
    ev = np.array(Image.open(os.path.join(os.path.dirname(__file__), '../../assets/pelluca_tileset_source/Evernahn.png')).convert('RGBA'))
    junk = {(17, 0), (17, 1), (17, 5), (17, 6), (18, 0), (18, 6)}
    T = set()
    for r in range(17, 27):
        for c in range(7):
            if (r, c) in junk: continue
            a = ev[r * 32:(r + 1) * 32, c * 32:(c + 1) * 32]
            small = np.full((16, 16, 3), -1, int)
            for y in range(16):
                for x in range(16):
                    blk = a[y * 2:y * 2 + 2, x * 2:x * 2 + 2].reshape(-1, 4); op = blk[blk[:, 3] > 0]
                    if len(op) >= 2:
                        u, k = np.unique(op[:, :3], axis=0, return_counts=True)
                        small[y, x] = (u[k.argmax()] >> 3) << 3      # snap to GBA 15-bit colour
            for ty in (0, 8):
                for tx in (0, 8):
                    q = small[ty:ty + 8, tx:tx + 8]
                    if (q >= 0).any(): T.add(bt.canon(q))
    return T

def colours(tb):
    a = np.frombuffer(tb, dtype=int).reshape(-1, 3)
    return frozenset(map(tuple, a[(a >= 0).all(1)]))

def pack(sets, cap=15):
    sets = sorted({s for s in sets if s}, key=len, reverse=True)
    pals, over = [], [s for s in sets if len(s) > cap]
    for s in sets:
        if len(s) > cap: continue
        best = None
        for p in pals:
            grow = len(s - p)
            if len(p) + grow <= cap and (best is None or grow < best[0]): best = (grow, p)
        if best: best[1].update(s)
        else: pals.append(set(s))
    return pals, over

if __name__ == '__main__':
    G = selection(); allsets = []; allc = set()
    for g, T in G.items():
        cs = [colours(t) for t in T]; allsets += cs
        u = set().union(*cs); allc |= u
        p, o = pack(cs)
        print('%-40s tiles %3d  colours %3d  palettes alone %2d  tiles >15 colours %d' % (g, len(T), len(u), len(p), len(o)))
    p, o = pack(allsets)
    print('ALL: distinct colours %d, greedy palettes needed %d (limit 13), tiles with >15 colours %d' % (len(allc), len(p), len(o)))

def merge_map(T_all, tol):
    """Map each colour to a MORE-USED colour within RGB distance tol (pixel-weighted)."""
    from collections import Counter
    use = Counter()
    for t in T_all:
        a = np.frombuffer(t, dtype=int).reshape(-1, 3)
        for c in map(tuple, a[(a >= 0).all(1)]): use[c] += 1
    reps, m = [], {}
    for c, _ in use.most_common():
        v = np.array(c)
        hit = next((r for r in reps if np.abs(v - np.array(r)).max() <= tol), None)
        if hit is None: reps.append(c); m[c] = c
        else: m[c] = hit
    return m, len(reps)

def sweep():
    G = selection(); T_all = set().union(*G.values())
    for tol in (0, 8, 16, 24, 32):
        m, n = merge_map(T_all, tol)
        sets = [frozenset(m[c] for c in colours(t)) for t in T_all]
        p, o = pack(sets)
        print('tolerance %2d (max per-channel RGB step): colours %3d  palettes %2d' % (tol, n, len(p)))

def pack_best(sets, cap=15, tries=400, seed=1):
    """Greedy with many shuffled orders + a merge pass; keep the fewest palettes."""
    import random
    rnd = random.Random(seed)
    base = sorted({s for s in sets if s}, key=len, reverse=True)
    # drop sets that are subsets of another set: they ride along for free
    keep = [s for s in base if not any(s < o for o in base)]
    best = None
    for i in range(tries):
        order = keep[:] if i == 0 else sorted(keep, key=lambda s: (-len(s) + rnd.random() * 6))
        pals = []
        for s in order:
            cand = [(len(s - p), j) for j, p in enumerate(pals) if len(p | s) <= cap]
            if cand: pals[min(cand)[1]] |= s
            else: pals.append(set(s))
        merged = True
        while merged:
            merged = False
            for a in range(len(pals)):
                for b in range(a + 1, len(pals)):
                    if len(pals[a] | pals[b]) <= cap:
                        pals[a] |= pals.pop(b); merged = True; break
                if merged: break
        if best is None or len(pals) < len(best): best = pals
    return best

def merge_map_safe(T_all, tol):
    """Like merge_map, but NEVER merge two colours that co-occur in any tile.
    Merging co-occurring shades is exactly what flattens texture (tol 24 turned
    grass into fill); colours that never share a tile can merge without erasing
    any tile's internal detail."""
    from collections import Counter
    use = Counter(); co = {}
    for t in T_all:
        cs = colours(t)
        for c in cs:
            use[c] += 1; co.setdefault(c, set()).update(cs)
    reps, m, members = [], {}, {}
    for c, _ in use.most_common():
        v = np.array(c); hit = None
        for r in reps:
            if np.abs(v - np.array(r)).max() <= tol and not (co[c] & members[r]):
                hit = r; break
        if hit is None:
            reps.append(c); m[c] = c; members[c] = {c}
        else:
            m[c] = hit; members[hit].add(c)
    return m, len(reps)
