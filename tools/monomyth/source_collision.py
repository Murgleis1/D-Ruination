"""Per-metatile (collision, elevation) as MonoMyth's own maps set them, keyed by the NEW
metatile ids -> data/source_collision.json. Re-run after every tileset rebuild (ids of the
Pelluca tileset shift when a building region changes size). Needs the MonoMyth ROM."""
import os, sys, json
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from romlib import *
import build_cormoria as b
C = sys.argv[1]
man = json.load(open(os.path.join(C, 'data/tilesets/secondary/pelluca_valley/assembly_manifest.json')))
votes = defaultdict(Counter)
for name, r in man['regions'].items():
    if not r.get('source_map'): continue
    a = int(r['source_map'], 16); x0, y0 = r['origin']; L = b.bt.ctx(a)[0]; mo = off(L['map']); W = L['w']
    for yy, row in enumerate(r['grid']):
        for xx, mid in enumerate(row):
            if mid is None: continue
            raw = u16(mo + ((y0 + yy) * W + (x0 + xx)) * 2)
            votes[mid][((raw >> 10) & 3, raw >> 12)] += 1
out = {str(m): list(v.most_common(1)[0][0]) for m, v in votes.items()}
json.dump(out, open(os.path.join(HERE, 'data/source_collision.json'), 'w'))
print(len(out), 'metatiles')
