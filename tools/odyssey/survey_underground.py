"""Render every underground map of a FireRed-based ROM (Crown / Odyssey); sheets grouped by secondary tileset."""
import os, sys, struct, numpy as np
sys.path.insert(0, '/home/claude/repo/tools/odyssey')
from frlib import ROM, u32, off, isptr, layout
from frrender import render
from PIL import Image, ImageDraw
name, gptr = sys.argv[1], int(sys.argv[2], 16)
O = '/home/claude/scratch/cave_survey/' + name; os.makedirs(O, exist_ok=True)
# groups: pointers until a non-pointer
starts = []
o = off(gptr)
while isptr(u32(o)) and len(starts) < 60: starts.append(u32(o)); o += 4
bounds = sorted(set(starts)) + [gptr]
seen = {}; rows = []
for g, s in enumerate(starts):
    nxt = min([b for b in bounds if b > s] or [s + 4 * 200])
    for n in range((nxt - s) // 4):
        hp = u32(off(s) + 4 * n)
        if not isptr(hp): break
        h = off(hp)
        L = layout(u32(h))
        if not L: continue
        mtype = ROM[h + 0x17]; weather = ROM[h + 0x16]
        if mtype != 4: continue                       # underground
        if L['addr'] in seen: continue
        seen[L['addr']] = (g, n)
        try: img = render(L)
        except Exception as e: continue
        rows.append((g, n, L['secondary']['addr'], L['w'], L['h'], img))
print(name, 'underground layouts', len(rows))
from collections import defaultdict
by = defaultdict(list)
for r in rows: by[r[2]].append(r)
for k, (sec, rs) in enumerate(sorted(by.items(), key=lambda kv: -len(kv[1]))):
    thumbs = []
    for g, n, _, w, h, img in rs:
        im = Image.fromarray(img); sc = min(1.0, 320 / max(im.size)); im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))))
        thumbs.append(('%d.%d %dx%d' % (g, n, w, h), im))
    W = 1400; x = y = 0; rowh = 0; pos = []
    for lab, im in thumbs:
        if x + im.width > W: x = 0; y += rowh + 14; rowh = 0
        pos.append((x, y, lab, im)); x += im.width + 6; rowh = max(rowh, im.height)
    S = Image.new('RGB', (W, y + rowh + 14), (30, 30, 30)); d = ImageDraw.Draw(S)
    for x, y, lab, im in pos: S.paste(im, (x, y + 12)); d.text((x, y), lab, fill=(255, 255, 0))
    S.save('%s/sec%02d_%x.png' % (O, k, sec))
    print(k, hex(sec), len(rs), [r[0:2] for r in rs][:12])
