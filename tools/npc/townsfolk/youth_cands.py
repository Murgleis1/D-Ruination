"""Young men, young women and children across all four games (user 2026-11-26: "find me more young men/women/kids
across Crown and the rest of the games"). South-facing frame of each, from the survey catalogues (board_src.py).
Crown and Odyssey are drawn in FireRed's smaller style; MonoMyth and Fantasma in the chunkier style used so far.
Run: python3 youth_cands.py -> /tmp/cult/youth_cands_v1.png"""
import sys
sys.path.insert(0, '/home/claude/repo/tools/npc')
from PIL import Image, ImageDraw
import board_src as B

GROUPS = [
    ('MonoMyth', B.mm_ow, [1, 3, 4, 5, 6, 8, 9, 11, 12, 17, 18, 20, 27, 28, 31, 32, 34, 40, 43, 59, 61, 62,
                           64, 69, 77, 79, 85, 86, 97, 98, 99, 113, 117, 172, 173, 174, 176, 177, 178, 180, 181,
                           182, 190, 191, 194, 195, 197, 198, 202, 203, 204, 205, 212, 226, 227, 236, 237]),
    ('Fantasma', B.fa_ow, list(range(32, 48)) + [100, 101, 102, 103, 266, 267, 268, 269, 271, 272, 273, 274, 275, 276]),
    ('Crown (FireRed style)', B.cr_ow, [14, 16, 17, 18, 19, 20, 22, 23, 24, 26, 29, 31, 47, 48, 52, 58, 59, 66, 67, 73,
                                        74, 76, 77, 79, 80, 82, 83, 85, 88]),
    ('Odyssey (FireRed style)', B.od_ow, [9, 10, 11, 13, 14, 15, 19, 20, 26, 27, 33, 35, 55, 57, 65, 66, 67, 105, 106,
                                          128, 130, 132, 133, 136, 138, 140, 152, 164, 165, 168, 171, 172, 173, 174,
                                          176, 180, 181, 183, 189, 190, 193, 194, 195, 210, 216, 222, 223]),
]
TW, TH = 64, 98; cols = 16; pad = 6
H = 20
for _, _, ns in GROUPS:
    H += 22 + ((len(ns) + cols - 1) // cols) * (TH + 16)
sh = Image.new('RGB', (cols * (TW + pad) + 10, H), (40, 40, 48)); dr = ImageDraw.Draw(sh)
dr.text((6, 4), 'Young men, young women and children (south frames)', fill=(255, 220, 120))
y0 = 22
for title, fn, ns in GROUPS:
    dr.text((6, y0), title, fill=(200, 200, 255)); y0 += 18
    for i, n in enumerate(ns):
        im = fn(n)
        import numpy as np
        a = np.array(im).astype(int); bgc = a[0, 0]
        m = np.abs(a - bgc).sum(2) > 24
        if m.any():
            ys, xs = np.where(m)
            im = im.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
        k = min(TW / im.width, (TH - 4) / im.height)
        k = max(1, int(k)) if k >= 1 else k
        im2 = im.resize((max(1, int(im.width * k)), max(1, int(im.height * k))), Image.NEAREST)
        tile = Image.new('RGB', (TW, TH), (110, 110, 125)); tile.paste(im2, ((TW - im2.width) // 2, TH - im2.height))
        im = tile
        x = 6 + (i % cols) * (TW + pad); y = y0 + (i // cols) * (TH + 16)
        dr.text((x, y), str(n), fill=(255, 255, 0)); sh.paste(im, (x, y + 12))
    y0 += ((len(ns) + cols - 1) // cols) * (TH + 16) + 4
sh.save('/tmp/cult/youth_cands_v1.png'); print(sh.size)
