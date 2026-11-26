"""Marauder front candidates (user 2026-11-26: the class is Marauders, "like pillagers and thieves that rob and steal
from travellers and they form gangs on occasion to invade towns"): rogues, bandits and bruisers from the MonoMyth and
Fantasma front sets, pulled from the ROMs into src/, on one sheet with each one's own walker where known.
Run: python3 cands.py -> src/<SRC>_<n>.png, /tmp/cult/marauder_cands_v1.png"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'picks'))
import extract as X

MALE = [('MM', 39, 'torch-bearing brute'), ('MM', 6, 'bandana bruiser'), ('MM', 37, 'scarfed rogue'),
        ('MM', 112, 'bare-chested swordsman'), ('MM', 91, 'bald thug'), ('MM', 79, 'red-haired brawler'),
        ('MM', 138, 'leaping cat-burglar'), ('FA', 55, 'cloaked highwayman'), ('FA', 168, 'crouching scarf bandit'),
        ('FA', 181, 'masked hooded thief'), ('FA', 8, 'red-hooded bandit'), ('FA', 151, 'bald brute')]
FEMALE = [('MM', 38, 'pink-haired swordswoman'), ('MM', 123, 'hatted gunhand'), ('FA', 26, 'red-hooded thief'),
          ('FA', 95, 'red-hooded rogue'), ('FA', 113, 'black-clad rogue')]

if __name__ == '__main__':
    X.FA_TABLE = X.fa_table()
    os.makedirs(os.path.join(HERE, 'src'), exist_ok=True)
    S = 2; cw = 64 * S + 40; cols = 6
    groups = [('Male', MALE), ('Female', FEMALE)]
    H = 30
    for _, g in groups:
        H += 20 + ((len(g) + cols - 1) // cols) * (64 * S + 44)
    sheet = Image.new('RGB', (cols * cw + 10, H), (40, 40, 48)); d = ImageDraw.Draw(sheet)
    d.text((6, 6), 'Marauder front candidates (originals, before any recolour)', fill=(255, 220, 120))
    y0 = 26
    for gname, g in groups:
        d.text((6, y0), gname, fill=(200, 200, 255)); y0 += 18
        for i, (s, n, note) in enumerate(g):
            px, pal = (X.mm if s == 'MM' else X.fa)(n)
            X.save(px, pal, os.path.join(HERE, 'src', '%s_%d.png' % (s, n)))
            o = np.zeros((64, 64, 3), np.uint8); o[:] = (110, 110, 125)
            for k in range(1, 16): o[px == k] = pal[k]
            x = 6 + (i % cols) * cw; y = y0 + (i // cols) * (64 * S + 44)
            sheet.paste(Image.fromarray(o).resize((64 * S, 64 * S), Image.NEAREST), (x, y + 28))
            d.text((x, y), '%s %d' % ('MonoMyth' if s == 'MM' else 'Fantasma', n), fill=(255, 255, 0)); d.text((x, y + 13), note, fill=(200, 200, 200))
        y0 += ((len(g) + cols - 1) // cols) * (64 * S + 44)
    sheet.save('/tmp/cult/marauder_cands_v1.png'); print(sheet.size)
