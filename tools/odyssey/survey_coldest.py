import os, sys, numpy as np
sys.path.insert(0, '/home/claude/repo/tools/odyssey')
from frlib import ROM, u32, off, isptr, layout
from frrender import render
from PIL import Image, ImageDraw
name, gptr = sys.argv[1], int(sys.argv[2], 16)
starts = []; o = off(gptr)
while isptr(u32(o)) and len(starts) < 60: starts.append(u32(o)); o += 4
bounds = sorted(set(starts)) + [gptr]
first = {}
for g, s in enumerate(starts):
    nxt = min([b for b in bounds if b > s] or [s + 800])
    for n in range((nxt - s) // 4):
        hp = u32(off(s) + 4 * n)
        if not isptr(hp): break
        h = off(hp); L = layout(u32(h))
        if not L: continue
        k = L['secondary']['addr']
        if k not in first or L['w'] * L['h'] > first[k][2]['w'] * first[k][2]['h']: first[k] = (g, n, L, ROM[h + 0x17], ROM[h+0x16])
th = []
for k, (g, n, L, mt, we) in first.items():
    try: im = Image.fromarray(render(L))
    except Exception: continue
    a = np.array(im).reshape(-1, 3).astype(int)
    cold = ((a[:, 2] > a[:, 0] + 15) & (a[:, 2] > 120)).mean() + ((a.min(1) > 190).mean())
    im.thumbnail((260, 260)); th.append((cold, '%d.%d t%d w%d' % (g, n, mt, we), im))
th.sort(key=lambda t: -t[0])
W = 1400; x = y = 0; rowh = 0; S = Image.new('RGB', (W, 4000), (30, 30, 30)); d = ImageDraw.Draw(S)
for c, lab, im in th[:40]:
    if x + im.width > W: x = 0; y += rowh + 14; rowh = 0
    S.paste(im, (x, y + 12)); d.text((x, y), lab, fill=(255, 255, 0)); x += im.width + 6; rowh = max(rowh, im.height)
S.crop((0, 0, W, y + rowh + 14)).save(name + '_coldest.png'); print(len(first), 'tilesets')
