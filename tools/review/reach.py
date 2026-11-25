import json, sys
from collections import deque
sys.path.insert(0, '/home/claude/scratch/review'); sys.path.insert(0, '/home/claude/scratch/dorm')
from maps import CH1
import walklib as W
C = '/home/claude/repo/codebase'
for area, ms in CH1.items():
    for m in ms:
        j = json.load(open(f'{C}/data/maps/{m}/map.json')); G = W.Grid(m)
        land = lambda p: p in G.cell and G.cell[p][0] == 0 and G.cell[p][1] != 1 and 'WATER' not in G.cell[p][2] and 'OCEAN' not in G.cell[p][2]
        starts = [(w['x'], w['y']) for w in j.get('warp_events', [])]
        for c in (j.get('connections') or []):
            d = c['direction']
            for i in range(max(G.w, G.h)):
                p = {'left': (0, i), 'right': (G.w - 1, i), 'up': (i, 0), 'down': (i, G.h - 1)}[d]
                if land(p): starts.append(p)
        seen = set(s for s in starts if s in G.cell); q = deque(seen)
        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                n = (x + dx, y + dy)
                if n in seen or not land(n): continue
                e1, e2 = G.cell[(x, y)][1], G.cell[n][1]
                if e1 != e2 and e1 not in (0, 15) and e2 not in (0, 15): continue
                seen.add(n); q.append(n)
        allland = [p for p in G.cell if land(p)]
        un = [p for p in allland if p not in seen]
        if len(un) > 6 and starts: print('%-28s land %4d  unreached %4d' % (m, len(allland), len(un)))
