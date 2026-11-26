"""Commoner men walkers, one at a time (user 2026-11-26).
  Commoner man A <- Fantasma 150 (spiky brown hair, pale-blue tunic and vest): "Darker skinned version of first one
                    here". Skin slots 1-4 onto Fantasma's own dark ramp (women.DARK); hair and clothes kept.
  Commoner man B <- Fantasma 270 (curly olive-brown hair, rose shirt, dark skin): "White version of this one". Skin
                    slots 1-4 onto Fantasma's own fair ramp (women.FAIR); hair and clothes kept.
  Commoner man C <- Fantasma 104 (purple hair, blue tunic, a purple neckerchief): "blonde haired version of this guy
                    with grey clothes". Hair (8/9/10) blonde; tunic and trousers (5/6/7) grey; the neckerchief, which
                    shared the hair's slots, onto the unused greys 12/13 so it stays with the clothes; skin kept.
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


def man_b():
    idx, pal = load('fa_270')
    pal[1:5] = FAIR
    return idx, pal


def man_c():
    idx, pal = load('fa_104')
    for f in range(9):
        sub = idx[:, f * 16:(f + 1) * 16]
        t = min(y for y in range(32) if sub[y].any())
        body = sub[t + 10:]                                     # below the hair and face (row 22 on a standing frame)
        src = body.copy()
        body[src == 8] = 12
        body[(src == 9) | (src == 10)] = 13
    pal[8], pal[9], pal[10] = (236, 204, 120), (204, 160, 76), (142, 104, 48)    # blonde
    pal[5], pal[6], pal[7] = (156, 156, 162), (112, 112, 120), (64, 64, 74)      # grey tunic and trousers
    pal[12], pal[13] = (128, 128, 136), (84, 84, 94)                            # the neckerchief, grey
    return idx, pal


ROWS = [('fa_150', man_a, 'commoner_man_a'), ('fa_270', man_b, 'commoner_man_b'), ('fa_104', man_c, 'commoner_man_c')]

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
