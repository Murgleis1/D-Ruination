"""Walking sprites for the old woman and the witch (user 2026-11-26: the seafolk approved; on with the walkers, the
female ones early since Pelluca Valley's NPCs are replaced first), MonoMyth bodies at our cast's size, dressed to
match their fronts (tools/npc/picks/recolour.py: MM_22 the old woman, FA_14 the witch).
  Old woman <- MonoMyth 108 (grey-blue hair, grey dress; 12 frames): the hair white, the skin fair, the dress the
               front's brown with a cream collar, a wide felt hat drawn over her hair, in the gown's brown, with a
               rose and a cream-gold flower (as her front's flowered hat)
  Witch     <- MonoMyth 87 (MonoMyth's witch; 12 frames): the greens the front's moss green, the red hair plum
MonoMyth's 12-frame walkers (S N W E, walk S x2, N x2, W x2, E x2) onto Emerald's 9: 0 1 2 4 5 6 7 8 9.
Run: python3 women.py  -> out/<name>_ow.png, /tmp/cult/women_ow.png"""
import os

import numpy as np
from PIL import Image, ImageDraw

from seafolk import FACING, rgba, save

HERE = os.path.dirname(os.path.abspath(__file__))
TO9 = [0, 1, 2, 4, 5, 6, 7, 8, 9]


def load12(n):
    im = Image.open(os.path.join(HERE, 'mm_%d.png' % n))
    a = np.array(im)
    idx = np.concatenate([a[:, k * 16:(k + 1) * 16] for k in TO9], axis=1)
    return idx.copy(), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


def frames(idx):
    return [idx[:, f * 16:(f + 1) * 16] for f in range(9)]


def old_woman():
    idx, pal = load12(108)
    HAIR = {2: 14, 3: 15, 4: 12, 1: 13, 5: 13}               # hair (rows to 20) onto spare slots: white
    LIGHT, MID, DARK, O, ROSE, GOLD = 10, 12, 13, 8, 6, 7     # placeholders resolved below
    for f, sub in enumerate(frames(idx)):
        head = sub[:21]
        out = head.copy()
        for a, b in HAIR.items():
            out[head == a] = b
        sub[:21] = out
    pal = list(pal)
    # hair white (14 light, 15 mid, 12 shade, 13 dark edge)
    pal[14], pal[15], pal[12], pal[13] = (252, 252, 252), (226, 228, 236), (186, 188, 200), (130, 132, 146)
    # the dress: the front's brown (A grey -> brown; 1 and 5 on the body -> darker browns); the collar cream
    pal[10], pal[1], pal[5] = (150, 110, 78), (116, 80, 56), (84, 56, 40)
    pal[11] = (232, 222, 196)
    pal[6], pal[9] = (240, 196, 164), (206, 148, 116)         # skin, fair
    # the hat: the gown's browns (10 light, 1 mid, 5 dark), outline 8; flowers in two slots freed here: 2 and 3
    # (their hair pixels moved to 14 and 15 above; no body pixel uses them)
    pal[2], pal[3] = (204, 104, 124), (226, 186, 96)
    for f, sub in enumerate(frames(idx)):
        fac = FACING[f]
        ys = [y for y in range(32) if sub[y].any()]
        t = ys[0]                                              # the top of her hair
        xs = [x for x in range(16) if sub[t + 2, x] != 0]
        x0, x1 = min(xs), max(xs)
        # the hat covers the top of her hair (user's front: hair tucked under a wide hat; set on top of MonoMyth
        # 108's big hair it sat like a small cap): the crown over her hair's top rows, the brim at its widest row
        bt = t + 4                                             # the brim's row
        xs = [x for x in range(16) if sub[bt, x] != 0]
        x0, x1 = min(xs), max(xs)
        for k, y in enumerate(range(t - 1, bt)):
            inset = 3 if k == 0 else (2 if k == 1 else 1)
            l, r = x0 + inset, x1 - inset
            for x in range(l, r + 1):
                sub[y, x] = 8 if (k == 0 or x in (l, r)) else (10 if x - l < (r - l + 1) / 2 else 1)
        for x in range(16):                                    # hair left showing beside the crown above the brim
            for y in range(t - 1, bt):
                if sub[y, x] in (14, 15, 12, 13):
                    sub[y, x] = 0
        bl, br = max(0, x0 - 1), min(15, x1 + 1)
        for x in range(bl, br + 1):
            sub[bt, x] = 8 if x in (bl, br) else 10
        for x in (bl, bl + 1, br - 1, br):
            sub[bt + 1, x] = 8 if x in (bl, br) else 5
        t = bt - 3                                             # the flowers' rows: on the crown, low on its side
        # the flowers: a rose and a cream-gold bloom on the crown's side (south: her right; west: at the back)
        if fac == 'S':
            spots = [(x1 - 2, t), (x1 - 3, t), (x1 - 2, t + 1)]
        elif fac == 'N':
            spots = [(x0 + 2, t), (x0 + 3, t), (x0 + 2, t + 1)]
        else:
            spots = [(x1 - 2, t), (x1 - 3, t), (x1 - 2, t + 1)]
        for k, (x, y) in enumerate(spots):
            sub[y, x] = 2 if k < 2 else 3
    return idx, pal


def witch():
    idx, pal = load12(87)
    pal = list(pal)
    pal[3], pal[1], pal[2] = (128, 160, 104), (96, 128, 80), (52, 76, 50)          # moss green
    pal[10], pal[8], pal[9] = (156, 96, 156), (120, 64, 120), (80, 40, 80)          # plum hair
    return idx, pal


if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    PICKS = os.path.join(HERE, '..', 'picks', 'out')
    rows = []
    for name, fn, front in (('old woman', old_woman, 'MM_22'), ('witch', witch, 'FA_14')):
        idx, pal = fn()
        save(idx, pal, os.path.join(HERE, 'out', name.replace(' ', '_') + '_ow.png'))
        fr = Image.open(os.path.join(PICKS, front + '.png')).convert('RGBA')
        c = Image.new('RGBA', fr.size, (110, 110, 125, 255)); c.alpha_composite(fr)
        rows.append((name, c.convert('RGB').resize((192, 192), Image.NEAREST), rgba(idx, pal).resize((144 * 5, 32 * 5), Image.NEAREST)))
    S = Image.new('RGB', (192 + 20 + 144 * 5 + 20, len(rows) * 214 + 10), (36, 36, 44)); d = ImageDraw.Draw(S)
    for i, (n, fr, ow) in enumerate(rows):
        y = 10 + i * 214
        d.text((10, y), n.capitalize(), fill=(240, 220, 120))
        S.paste(fr, (10, y + 16)); S.paste(ow, (222, y + 32))
    S.save('/tmp/cult/women_ow.png'); print(S.size)
