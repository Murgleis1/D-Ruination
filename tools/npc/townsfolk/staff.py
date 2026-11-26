"""Tavern and dormitory staff walkers, one at a time (user 2026-11-26).
  Cook <- Fantasma 255 (chef's cap and whites, navy hair): "a greener haired version of this guy". Hair (11/12/13)
          green; cap, whites and skin kept. Fantasma gives it three frames (S, N, W): a cook stands at his counter.
  Barkeep <- MonoMyth 144 (user 2026-11-26: "a bartender sprite in the tavern of MonoMyth at fort elderflower we
          could recolor"): the bald man standing behind the bar counter in Elderflower's tavern (map header 0x86B244,
          objects 1-2, graphics id 80 = catalogue 144 by the graphics-info pointer table at 0x93BF90; our Pelluca
          tavern is built from the same map). Recoloured off MonoMyth's maroon: the waistcoat and trousers a forest
          green, the shirt and skin kept.
Run: python3 staff.py -> out/<name>_ow.png, /tmp/cult/staff.png"""
import os
import sys
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'walkers'))
from seafolk import save          # noqa: E402
sys.path.insert(0, HERE)
from women import load            # noqa: E402  (this folder's women.py)


def cook():
    idx, pal = load('fa_255')
    pal[11], pal[12], pal[13] = (120, 170, 96), (72, 124, 72), (36, 74, 46)       # green hair
    return idx, pal


def barkeep():
    idx, pal = load('mm_144')
    pal[10], pal[12] = (96, 132, 88), (44, 70, 46)              # waistcoat and trousers: forest green
    return idx, pal


ROWS = [('fa_255', cook, 'cook'), ('mm_144', barkeep, 'barkeep')]

if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    S = 6
    sheet = Image.new('RGB', (9 * (16 * S + 8) + 8, 2 * len(ROWS) * (32 * S + 12) + 8), (110, 110, 125))
    r = 0
    for src, fn, name in ROWS:
        idx, pal = fn()
        save(idx, pal, os.path.join(HERE, 'out', name + '_ow.png'))
        for ii, pp in (load(src), (idx, pal)):
            P = np.array(pp, np.uint8)
            for f in range(9 if src.startswith('mm_') else 3):
                sub = ii[:, f * 16:(f + 1) * 16]
                o = np.zeros((32, 16, 3), np.uint8); o[:] = (110, 110, 125)
                for k in range(1, 16):
                    o[sub == k] = P[k]
                sheet.paste(Image.fromarray(o).resize((16 * S, 32 * S), Image.NEAREST),
                            (8 + f * (16 * S + 8), 8 + r * (32 * S + 12)))
            r += 1
    sheet.save('/tmp/cult/staff.png'); print(sheet.size)
