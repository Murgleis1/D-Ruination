import json, os, struct, sys
from collections import deque
sys.path.insert(0, '/home/claude/scratch/review'); sys.path.insert(0, '/home/claude/scratch/dorm')
from maps import CH1
import walklib as W
C = '/home/claude/repo/codebase'
allmaps = {m for v in CH1.values() for m in v}
ids = {}
for d in os.listdir(C + '/data/maps'):
    p = f'{C}/data/maps/{d}/map.json'
    if os.path.exists(p): ids[json.load(open(p))['id']] = d
probs = []
for m in sorted(allmaps):
    p = f'{C}/data/maps/{m}/map.json'
    if not os.path.exists(p): probs.append((m, 'no such map')); continue
    j = json.load(open(p)); G = W.Grid(m)
    for i, w in enumerate(j.get('warp_events', [])):
        dm = ids.get(w['dest_map'])
        if dm is None and w['dest_map'] not in ('MAP_DYNAMIC',): probs.append((m, 'warp %d -> missing map %s' % (i, w['dest_map']))); continue
        if dm:
            dj = json.load(open(f'{C}/data/maps/{dm}/map.json'))
            k = int(w['dest_warp_id']) if str(w['dest_warp_id']).isdigit() else None
            if k is not None and k >= len(dj.get('warp_events', [])): probs.append((m, 'warp %d -> %s warp %d does not exist' % (i, dm, k)))
        if (w['x'], w['y']) not in G.cell: probs.append((m, 'warp %d off the map' % i))
    for o in j.get('object_events', []):
        c = G.cell.get((o['x'], o['y']))
        if c is None: probs.append((m, 'object %s off the map' % o.get('graphics_id')))
    for b in j.get('bg_events', []):
        if (b['x'], b['y']) not in G.cell: probs.append((m, 'bg event off the map'))
for p in probs: print(p)
print(len(allmaps), 'maps checked,', len(probs), 'problems')
