"""Make the slip's plan MonoMyth-normal (user 2026-11-24: "see what looks normal versus not"): every cell's 3x3
neighbourhood of terrain classes must be one MonoMyth's canyon maps actually have (tilesolve.Corpus.samples). Where
the plan makes one they never have, cells near it are changed, one at a time, keeping each change that leaves fewer
such neighbourhoods: sand and ripples trade freely; a rock or water edge may grow or shrink by a cell. Never touched:
the sky, the set pieces' cells, the way (every spot stays reachable), the river's course (its water stays one body)
and the oasis pool. Writes plan_normal.npy (the plan's letters) beside this file; plan_slip.load() reads it.
Usage: python3 normalize_plan.py"""
import os, sys
import numpy as np
from collections import deque
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import tilesolve as T
import plan_slip as P

def protected():
    keep = set()
    for L in P.LADDERS:
        for dx in (-1, 0, 1, 2):
            for y in range(L['y'] - 3, L['y'] + 3): keep.add((L['x'] + dx, y))
    for y in range(P.BRIDGE['y0'] - 1, P.BRIDGE['y1'] + 2):
        for x in range(22, 28): keep.add((x, y))
    F = P.FALLS
    for y in range(12, F['top'] + F['rows'] + 2):
        for x in range(F['x0'] - 1, F['x1'] + 2): keep.add((x, y))
    for h in P.HOUSES:
        for dy in range(-1, 7):
            for dx in range(-1, 5): keep.add((h['x'] + dx, h['y'] + dy))
    for y in range(25, 30):
        for x in range(37, 43): keep.add((x, y))                       # (the oasis' pool)
    for y in range(P.H):
        for x in range(P.W):
            if P.G[y, x] == 'K': keep.add((x, y))
            if y < 13 and P.G[y, x] != 'K': keep.add((x, y))          # (the mesa's top: the rim is painted)
    return keep

def unseen_cells(cls):
    C = T.corpus(); keys = T.keys_of(cls); out = set()
    for (x, y), k in keys.items():
        if cls[y, x] in 'Kx': continue
        if T.norm(k) not in C.samples: out.add((x, y))
    return out

def water_bodies(G):
    seen = np.zeros(G.shape, bool); n = 0
    for y in range(P.H):
        for x in range(P.W):
            if G[y, x] == '~' and not seen[y, x]:
                n += 1; q = deque([(x, y)]); seen[y, x] = True
                while q:
                    a, b = q.popleft()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        c, d = a + dx, b + dy
                        if 0 <= c < P.W and 0 <= d < P.H and G[d, c] == '~' and not seen[d, c]: seen[d, c] = True; q.append((c, d))
    return n

def reachable():
    seen = P.check(); return all(p in seen for p in P.SPOTS.values())

def main():
    keep = protected()
    cls = P.classes(); bad = unseen_cells(cls); n0 = len(bad)
    print('unseen neighbourhoods before:', n0)
    wb = water_bodies(P.G)
    for it in range(12):
        changed = 0
        cand = sorted({(x + dx, y + dy) for (x, y) in bad for dx in (-1, 0, 1) for dy in (-1, 0, 1)})
        for (x, y) in cand:
            if not (0 <= x < P.W and 0 <= y < P.H) or (x, y) in keep: continue
            old = P.G[y, x]
            opts = {'.': 'r#~', 'r': '.#', '#': '.', '~': '.'}.get(old, '')
            best = None
            for new in opts:
                if new == '~' and not any(0 <= x + dx < P.W and 0 <= y + dy < P.H and P.G[y + dy, x + dx] == '~' for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))): continue
                if new == '#' and not any(0 <= x + dx < P.W and 0 <= y + dy < P.H and P.G[y + dy, x + dx] == '#' for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))): continue
                P.G[y, x] = new
                c2 = P.classes(); b2 = unseen_cells(c2)
                ok = len(b2) < len(bad) and (new != '~' and old != '~' or water_bodies(P.G) == wb) and \
                     (new not in '#~' or reachable())
                if ok and (best is None or len(b2) < best[1]): best = (new, len(b2), b2)
                P.G[y, x] = old
            if best:
                P.G[y, x] = best[0]; bad = best[2]; changed += 1
        print('pass', it, 'changed', changed, 'unseen', len(bad))
        if not changed: break
    np.save(os.path.join(HERE, 'plan_normal.npy'), P.G)
    print('left unseen:', sorted(bad))

if __name__ == '__main__':
    main()
