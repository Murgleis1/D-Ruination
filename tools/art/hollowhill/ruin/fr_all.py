import os, sys
sys.path.insert(0, '/home/claude/repo/tools/odyssey')
from frlib import ROM, u32, off, isptr, layout
from frrender import render
from PIL import Image
name, gptr, ng = sys.argv[1], int(sys.argv[2], 16), int(sys.argv[3])
O = '/home/claude/scratch/hhruin/' + name; os.makedirs(O, exist_ok=True)
starts = [u32(off(gptr) + 4 * g) for g in range(ng)]
bounds = sorted(set(starts)) + [gptr]
seen = set(); n_ok = 0
for g, s in enumerate(starts):
    nxt = min([b for b in bounds if b > s] or [s + 800])
    for n in range((nxt - s) // 4):
        hp = u32(off(s) + 4 * n)
        if not isptr(hp): break
        h = off(hp); L = layout(u32(h))
        if not L or L['addr'] in seen: continue
        mtype = ROM[h + 0x17]
        if mtype in (8, 9): continue        # indoor / secret base
        if L['w'] < 20 or L['h'] < 20: continue
        seen.add(L['addr'])
        try: img = render(L)
        except Exception: continue
        Image.fromarray(img).save('%s/%d.%d_t%d_%dx%d.png' % (O, g, n, mtype, L['w'], L['h'])); n_ok += 1
print(name, n_ok)
