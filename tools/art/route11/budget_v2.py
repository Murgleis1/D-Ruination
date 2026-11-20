"""Rough tile budget of the Route 11 mock: cells that are Pelluca's own metatiles cost nothing (its primary); the
rest must fit Route 11's secondary (512 metatiles, 512 tiles, 7 palettes of 15)."""
import sys, collections, random
import numpy as np
import route11_v2 as R, kit
M = R.compose(); img = (M.render() >> 3) << 3
MERGE = int(next((a[2:] for a in sys.argv if a.startswith('-m')), '0'))
if MERGE:                                   # colours this close per channel merged into the more common (as the build)
    pix = collections.Counter(map(tuple, img.reshape(-1, 3).tolist())); rep = {}
    for c, _ in pix.most_common():
        if c in rep: continue
        rep[c] = c
        for d in pix:
            if d not in rep and max(abs(a - b) for a, b in zip(c, d)) <= MERGE: rep[d] = c
    flat = img.reshape(-1, 3)
    for k, v in rep.items():
        if k != v: flat[(flat == k).all(1)] = v
prim = {}
for m in range(512):
    try: prim[(kit.cor_full(m) >> 3 << 3).tobytes()] = m
    except Exception: pass
cells, tiles, sets = set(), set(), set()
ptiles = set()
for m in range(512):
    try: c = kit.cor_full(m) >> 3 << 3
    except Exception: continue
    for q in range(4): ptiles.add(c[(q // 2) * 8:(q // 2) * 8 + 8, (q % 2) * 8:(q % 2) * 8 + 8].tobytes())
free = 0
for y in range(R.H):
    for x in range(R.W):
        c = img[y * 16:y * 16 + 16, x * 16:x * 16 + 16]
        if c.tobytes() in prim: free += 1; continue
        cells.add(c.tobytes())
        for q in range(4):
            t = c[(q // 2) * 8:(q // 2) * 8 + 8, (q % 2) * 8:(q % 2) * 8 + 8]
            if t.tobytes() in ptiles: continue
            k = min(np.ascontiguousarray(v).tobytes() for v in (t, t[:, ::-1], t[::-1], t[::-1, ::-1]))
            tiles.add(k); sets.add(frozenset(map(tuple, t.reshape(-1, 3).tolist())))
big = max(len(s) for s in sets)
red = []
for s in sorted(sets, key=len, reverse=True):
    if not any(s <= r for r in red): red.append(s)
best = None; rng = random.Random(1)
for _ in range(300):
    o = list(red); rng.shuffle(o); o.sort(key=lambda s: -len(s) + rng.random() * 4); pals = []
    for s in o:
        b = None
        for i, p in enumerate(pals):
            n = len(p | s)
            if n <= 15 and (b is None or n - len(p) < b[0]): b = (n - len(p), i)
        if b is None: pals.append(set(s))
        else: pals[b[1]] |= s
    if best is None or len(pals) < len(best): best = pals
print(f'cells from Pelluca primary: {free}; secondary metatiles: {len(cells)}; new tiles: {len(tiles)}; '
      f'max colours/tile: {big}; palettes (no merging): {len(best)}; distinct colours: {len(set().union(*sets))}')
if '-v' in sys.argv:
    cat = collections.defaultdict(set); seen = set()
    for y in range(R.H):
        for x in range(R.W):
            c = img[y * 16:y * 16 + 16, x * 16:x * 16 + 16]
            if c.tobytes() in prim: continue
            u = M.used[y, x]; g = M.ground[y][x]
            tag = (u.split(':')[0] if u else 'grass' if g == 'grass' else 'ground') + ('' if g == 'grass' or u else '')
            for q in range(4):
                t = c[(q // 2) * 8:(q // 2) * 8 + 8, (q % 2) * 8:(q % 2) * 8 + 8]
                if t.tobytes() in ptiles: continue
                k = min(np.ascontiguousarray(v).tobytes() for v in (t, t[:, ::-1], t[::-1], t[::-1, ::-1]))
                if k not in seen: seen.add(k); cat[tag].add(k)
    print({k: len(v) for k, v in sorted(cat.items(), key=lambda kv: -len(kv[1]))})
