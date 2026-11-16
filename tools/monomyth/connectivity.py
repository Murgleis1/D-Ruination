"""Whole-map coherence check (user 2026-11-16: everything connected in the right ways).
Walk from the arrival point over walkable land (collision 0, not water) and report:
every door's front cell reached? every exit reached? any walkable pocket cut off?"""
import sys, json, os
from collections import deque
import numpy as np

def check(npz, man_path, doors, exits, start):
    d = np.load(npz); coll, elev, grid = d['coll'], d['elev'], d['grid']
    H, W = coll.shape
    walk = (coll == 0) & (elev != 1)
    seen = np.zeros((H, W), bool); q = deque([start]); seen[start[1], start[0]] = True
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and walk[ny, nx] and not seen[ny, nx]:
                seen[ny, nx] = True; q.append((nx, ny))
    ok = True
    for name, (x, y) in doors.items():
        r = seen[y + 1, x]
        print(f'  door {name:16s} ({x},{y}) front reachable: {"yes" if r else "NO"}'); ok &= bool(r)
    for name, cells in exits.items():
        r = any(seen[y, x] for x, y in cells)
        print(f'  exit {name:16s} reachable: {"yes" if r else "NO"}'); ok &= r
    lab = np.zeros((H, W), int); n = 0
    for y in range(H):
        for x in range(W):
            if walk[y, x] and not seen[y, x] and lab[y, x] == 0:
                n += 1; size = 0; q = deque([(x, y)]); lab[y, x] = n
                while q:
                    a, b = q.popleft(); size += 1
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        u, v = a + dx, b + dy
                        if 0 <= u < W and 0 <= v < H and walk[v, u] and not seen[v, u] and lab[v, u] == 0:
                            lab[v, u] = n; q.append((u, v))
                if size > 2: print(f'  cut-off walkable pocket of {size} cells at ({x},{y})')
    return ok
