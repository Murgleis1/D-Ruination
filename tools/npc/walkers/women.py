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
        # (user 2026-11-26: "her hat on the front sprite is wide brimmed but not on her overworld one"): MonoMyth
        # 108's hair is as wide as the frame, so a brim one pixel past it read as a cap. The brim now spans the
        # whole frame and sags at the tips (light top, mid lip), and the hair under it is trimmed in to x3-12
        # (x2-13 side on), so the brim stands clear of her head on both sides.
        for x in range(1, 15):
            sub[bt, x] = 8 if x in (1, 14) else 10
        for x in range(16):
            sub[bt + 1, x] = 8 if x in (0, 15) else 1
        lo, hi = (3, 12) if fac in ('S', 'N') else (2, 13)
        for y in range(bt + 2, bt + 6):
            for x in range(16):
                if (x < lo or x > hi) and sub[y, x] in (14, 15, 12, 13, 8):
                    sub[y, x] = 0
            xs = [x for x in range(16) if sub[y, x] != 0]
            for x in (min(xs), max(xs)) if xs else ():
                if sub[y, x] in (14, 15, 12, 13):
                    sub[y, x] = 8
        for x in (0, 1, 2, 13, 14, 15):                        # the brim's underside edge at the tips
            if sub[bt + 2, x] == 0 and x not in (0, 15):
                sub[bt + 2, x] = 8
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
    """(user 2026-11-26: "the back of her purple hair isn't long enough on the overworld sprite"; then "the long hair
    behind the witch overworld sprite should be more wide like her front battle sprite suggests"): her front shows
    plum hair flaring out past both shoulders down to the waist, so the walker gets
      north: a curtain 12 wide (x2-13) from the brim down six rows, ending in uneven tips;
      west:  a mass down her back (x11-14), as long, overhanging the cloak behind her;
      south: locks falling past both shoulders beside her face and body (x2-3, x12-13).
    Shading: 8 mid, 10 light streaks, 9 dark edges; outline 4 only where the hair meets empty space."""
    idx, pal = load12(87)
    HAIR = (8, 10)                                           # mid, light
    def put(sub, y, x, v):
        if 0 <= x < 16 and 0 <= y < 32 and v != ' ':
            sub[y, x] = int(v, 16)
    def outline(sub, y, x):
        if 0 <= x < 16 and 0 <= y < 32 and sub[y, x] == 0:
            sub[y, x] = 4
    def paint(sub, y, x0, row):
        for i, v in enumerate(row):
            put(sub, y, x0 + i, v)
        xs = [x0 + i for i, v in enumerate(row) if v != ' ']
        outline(sub, y, min(xs) - 1); outline(sub, y, max(xs) + 1)
    CURTAIN = [(2, '9A88A88A88A9'), (2, '98A88A88A889'), (2, '98A88A88A889'), (2, '98A88A88A889'),
               (3, '9A88A88A89'), (3, '98 988 899')]               # strands: light streaks at x4, x7, x10
    BACK = [(12, '889'), (12, '889'), (11, '9889'), (11, '98A9'), (11, '98A9'), (11, '9889'), (11, '9889'),
            (12, '9 9')]
    for f, sub in enumerate(frames(idx)):
        fac = FACING[f]
        if fac == 'N':
            rt = min(y for y in range(16, 30) if np.isin(sub[y], HAIR).sum() >= 8)   # the first full hair row
            for k, (x0, row) in enumerate(CURTAIN):
                paint(sub, rt + k, x0, row)
            for x in range(16):                                # rim under the tips where they hang over nothing
                outline(sub, rt + len(CURTAIN), x) if sub[rt + len(CURTAIN) - 1, x] in (8, 9) else None
        elif fac == 'W':
            r = max(y for y in range(16, 30) for x in range(8, 16) if sub[y, x] in HAIR)
            for k, (x0, row) in enumerate(BACK):
                paint(sub, r - 2 + k, x0, row)
            for x in (12, 14):
                outline(sub, r - 2 + len(BACK), x)
        else:                                                  # south: locks past both shoulders
            rs = max(y for y in range(16, 26) if sub[y, 2] in (8, 9, 10))
            for k in range(4):
                lock = '89' if k < 3 else '99'
                paint(sub, rs + 1 + k, 2, lock)
                paint(sub, rs + 1 + k, 12, lock[::-1])
            for x in (2, 3, 12, 13):
                outline(sub, rs + 5, x)
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
