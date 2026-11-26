"""Tavern and dormitory staff walkers, one at a time (user 2026-11-26).
  Cook <- Fantasma 255 (chef's cap and whites, navy hair): "a greener haired version of this guy". Hair (11/12/13)
          green; cap, whites and skin kept. Fantasma gives it three frames (S, N, W): a cook stands at his counter.
  Barkeep <- MonoMyth 144 (user 2026-11-26: "a bartender sprite in the tavern of MonoMyth at fort elderflower we
          could recolor"): the bald man standing behind the bar counter in Elderflower's tavern (map header 0x86B244,
          objects 1-2, graphics id 80 = catalogue 144 by the graphics-info pointer table at 0x93BF90; our Pelluca
          tavern is built from the same map). Recoloured off MonoMyth's maroon: the waistcoat and trousers bronze
          (first forest green; the user chose bronze to set him apart), brown hair added, the shirt and skin kept.
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
    # (user 2026-11-26: "green is fine for him"). His clothes' darkest shade is the skin's outline brown (1): below
    # the face (row 22 on a standing frame) it moves to a free slot (13) so the waistcoat is green throughout
    for f in range(9):
        sub = idx[:, f * 16:(f + 1) * 16]
        t = min(y for y in range(32) if sub[y].any())
        body = sub[t + 11:]
        body[body == 1] = 13
    # (user 2026-11-26: "can we give him some hair too"): brown hair over his bald crown. Skin slots 2-5 become hair
    # (14, with 15 on its lower and outer edge) where hair grows: south, the crown (rows t+1..t+4), the temples
    # (t+5) and sideburns (t+6); north, the whole back of the head down to the nape (t+1..t+8); west, the crown and
    # the back half of the head behind the ear (t+5..t+8, x 7 and over). His side tufts (6) take the same brown.
    FACE = {0: 'S', 1: 'N', 2: 'W', 3: 'S', 4: 'S', 5: 'N', 6: 'N', 7: 'W', 8: 'W'}
    SKIN = (2, 3, 4, 5)
    for f in range(9):
        sub = idx[:, f * 16:(f + 1) * 16]
        t = min(y for y in range(32) if sub[y].any())
        fac = FACE[f]
        for y in range(t, t + 9):
            xs = [x for x in range(16) if sub[y, x] in SKIN]
            if not xs:
                continue
            x0, x1 = min(xs), max(xs)
            for x in xs:
                k = y - t
                grow = (fac == 'S' and (k <= 4 or (k == 5 and (x <= x0 + 1 or x >= x1 - 1))
                                        or (k == 6 and (x == x0 or x == x1))))
                grow |= fac == 'N' and k <= 8
                grow |= fac == 'W' and (k <= 4 or (k <= 8 and x >= 7))
                if grow:
                    edge = x in (x0, x1) or (fac == 'S' and k >= 4) or (fac == 'N' and k == 8)
                    sub[y, x] = 15 if edge else 14
    pal[14], pal[15], pal[6] = (100, 64, 40), (64, 40, 28), (64, 40, 28)         # brown hair, a shade darker than the bronze
    # (user 2026-11-26, after the green: "Maybe make his clothing colors bronze instead to distinguish him more")
    pal[10], pal[12], pal[13] = (184, 128, 64), (104, 64, 30), (144, 96, 46)   # waistcoat and trousers: bronze
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
