"""Lay a class plan (W S G T P R B per cell) out in real metatiles, using the
transitions MonoMyth's artists drew: every cell of the source maps (Wood Avens
terrain, quay, sandbank) records its 3x3 class neighbourhood and the metatile placed
there. A plan cell takes the most-used metatile for its neighbourhood; fallbacks:
4-neighbour pattern, then its own class. Reports how many cells matched at each level.
"""
import json, random
from collections import Counter, defaultdict

def learn(manifest, cls):
    full, four, own = defaultdict(Counter), defaultdict(Counter), defaultdict(Counter)
    for name in ('wa_terrain', 'quay', 'sandbank'):
        g = manifest['regions'][name]['grid']; H, W = len(g), len(g[0])
        C = lambda y, x: cls.get(str(g[y][x]), '?') if 0 <= y < H and 0 <= x < W and g[y][x] is not None else '?'
        for y in range(H):
            for x in range(W):
                m = g[y][x]
                if m is None: continue
                k9 = tuple(C(y + dy, x + dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1))
                if '?' in k9: continue
                full[k9][m] += 1
                four[(k9[4], k9[1], k9[3], k9[5], k9[7])][m] += 1
                own[k9[4]][m] += 1
    return full, four, own

def lay(plan, full, four, own, seed=7):
    rnd = random.Random(seed); H, W = len(plan), len(plan[0])
    P = lambda y, x: plan[max(0, min(H - 1, y))][max(0, min(W - 1, x))]
    out = [[0] * W for _ in range(H)]; stats = Counter()
    def pick(cnt):
        ids, w = zip(*cnt.items()); return rnd.choices(ids, weights=w)[0]
    for y in range(H):
        for x in range(W):
            k9 = tuple(P(y + dy, x + dx) for dy in (-1, 0, 1) for dx in (-1, 0, 1))
            k5 = (k9[4], k9[1], k9[3], k9[5], k9[7])
            if k9 in full: out[y][x] = pick(full[k9]); stats['3x3'] += 1
            elif k5 in four: out[y][x] = pick(four[k5]); stats['4-neighbour'] += 1
            elif k9[4] in own: out[y][x] = pick(own[k9[4]]); stats['class only'] += 1
            else: stats['unmatched'] += 1
    return out, stats
