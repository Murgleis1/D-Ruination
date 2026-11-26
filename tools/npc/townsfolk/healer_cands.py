"""Tavern healer candidates (user 2026-11-26: "Lets look at the candidates"): nurses, nuns, herbalists and robed
healers across MonoMyth, Fantasma, Crown and Odyssey (south frames from the survey catalogues).
Run: python3 healer_cands.py -> /tmp/cult/healer_cands_v1.png"""
import sys
sys.path.insert(0, '/home/claude/repo/tools/npc')
import numpy as np
from PIL import Image, ImageDraw
import board_src as B

GROUPS = [
    ('MonoMyth', B.mm_ow, [18, 22, 53, 137, 85, 188, 57, 115, 116, 68]),
    ('Fantasma', B.fa_ow, [137, 138, 139, 140, 186, 284, 287, 289, 122, 125]),
    ('Crown (FireRed style)', B.cr_ow, [45, 46, 64, 66, 39, 40, 63]),
    ('Odyssey (FireRed style)', B.od_ow, [172, 26, 35, 170, 133]),
]
TW, TH = 64, 98; cols = 10; pad = 8
H = 20 + sum(22 + ((len(ns) + cols - 1) // cols) * (TH + 16) for _, _, ns in GROUPS)
sh = Image.new('RGB', (cols * (TW + pad) + 10, H), (40, 40, 48)); dr = ImageDraw.Draw(sh)
dr.text((6, 4), 'Tavern healer candidates (south frames)', fill=(255, 220, 120))
y0 = 22
for title, fn, ns in GROUPS:
    dr.text((6, y0), title, fill=(200, 200, 255)); y0 += 18
    for i, n in enumerate(ns):
        im = fn(n); a = np.array(im).astype(int); bgc = a[0, 0]
        m = np.abs(a - bgc).sum(2) > 24
        if m.any():
            ys, xs = np.where(m); im = im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
        k = min(TW / im.width, (TH - 4) / im.height); k = max(1, int(k)) if k >= 1 else k
        im2 = im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))), Image.NEAREST)
        tile = Image.new('RGB', (TW, TH), (110, 110, 125)); tile.paste(im2, ((TW - im2.width) // 2, TH - im2.height))
        x = 6 + (i % cols) * (TW + pad); y = y0 + (i // cols) * (TH + 16)
        dr.text((x, y), str(n), fill=(255, 255, 0)); sh.paste(tile, (x, y + 12))
    y0 += ((len(ns) + cols - 1) // cols) * (TH + 16) + 4
sh.save('/tmp/cult/healer_cands_v1.png'); print(sh.size)
