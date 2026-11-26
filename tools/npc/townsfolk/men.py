"""Commoner men walkers, one at a time (user 2026-11-26).
  Commoner man A <- Fantasma 150 (spiky brown hair, pale-blue tunic and vest): "Darker skinned version of first one
                    here". Skin slots 1-4 onto Fantasma's own dark ramp (women.DARK); hair and clothes kept.
Run: python3 men.py -> out/commoner_man_*_ow.png, /tmp/cult/commoner_men.png"""
import os
import sys
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'walkers'))
from seafolk import save          # noqa: E402
sys.path.insert(0, HERE)
from women import load, DARK, FAIR  # noqa: E402,F401  (this folder's women.py, not walkers/)


def man_a():
    idx, pal = load('fa_150')
    pal[1:5] = DARK
    return idx, pal


ROWS = [('fa_150', man_a, 'commoner_man_a')]

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
            for f in range(9):
                sub = ii[:, f * 16:(f + 1) * 16]
                o = np.zeros((32, 16, 3), np.uint8); o[:] = (110, 110, 125)
                for k in range(1, 16):
                    o[sub == k] = P[k]
                sheet.paste(Image.fromarray(o).resize((16 * S, 32 * S), Image.NEAREST),
                            (8 + f * (16 * S + 8), 8 + r * (32 * S + 12)))
            r += 1
    sheet.save('/tmp/cult/commoner_men.png'); print(sheet.size)
