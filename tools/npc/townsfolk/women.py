"""Commoner women walkers, one at a time (user 2026-11-26: "Lets just do them one by one").
  Commoner woman A <- Fantasma 60 (long blue hair, rose dress, dark skin): "a pale skinned version of this one".
                      Skin slots 1-4 onto Fantasma's own fair ramp (its fair villagers', e.g. 133); hair and dress
                      kept.
  Commoner woman B <- Fantasma 48 (red hair, green dress and white apron, fair skin): "a darker skinned version of
                      this one". Skin slots 1-4 onto Fantasma's own dark ramp (Fantasma 60's original skin); hair and
                      dress kept.
Run: python3 women.py -> out/commoner_woman_{a,b}_ow.png, /tmp/cult/commoner_women.png"""
import os
import sys
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'walkers'))
from seafolk import save          # noqa: E402

FAIR = [(240, 208, 184), (224, 176, 144), (192, 136, 112), (112, 64, 64)]     # Fantasma's fair skin, light to dark
DARK = [(160, 104, 72), (120, 72, 48), (88, 48, 32), (48, 24, 24)]            # Fantasma's dark skin (60's own)


def load(name):
    im = Image.open(os.path.join(HERE, name + '.png'))
    return np.array(im).copy(), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


def woman_a():
    idx, pal = load('fa_60')
    pal[1:5] = FAIR
    return idx, pal


def woman_b():
    idx, pal = load('fa_48')
    pal[1:5] = DARK
    return idx, pal


if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    S = 6
    rows = [('fa_60', woman_a, 'commoner_woman_a'), ('fa_48', woman_b, 'commoner_woman_b')]
    sheet = Image.new('RGB', (9 * (16 * S + 8) + 8, 2 * len(rows) * (32 * S + 12) + 8), (110, 110, 125))
    r = 0
    for src, fn, name in rows:
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
    sheet.save('/tmp/cult/commoner_women.png'); print(sheet.size)
