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
    """The old woman's walker, rebuilt on Fantasma 128 (user 2026-11-26, of the MonoMyth 108 version: "do you think this
    actually looks good ... Come on now"; 108's big hair buried her face and the hat sat on a blob). FA 128 is
    Fantasma's own little old woman: short stooped shape, hair to the shoulders, clear face. Dressed to the front
    (MonoMyth 22): white hair, a cream shawl collar, the brown gown, and a wide-brimmed brown hat with a rose and a
    cream bloom on its band. Her spectacles go (the front has none): lenses to skin, each lens's top row a squinting
    eye. Palette: 1-4 skin, 5/6/7 hair (7 its outline), 8/9/A shawl, B/C/D gown and hat, E rose (freed from the
    lenses), F outline."""
    im = Image.open(os.path.join(HERE, 'fa_128.png'))
    idx = np.array(im).copy()
    pal = [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]
    for f, sub in enumerate(frames(idx)):
        fac = FACING[f]
        # spectacles off
        lens = [(y, x) for y in range(17, 23) for x in range(16) if sub[y, x] == 14]
        for y in range(17, 22):
            for x in range(16):
                if sub[y, x] == 10:
                    nb = [sub[y + dy, x + dx] for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)) if 0 <= x + dx < 16]
                    sub[y, x] = 2 if any(v in (1, 2, 3, 4, 14) for v in nb) else 7
        top = min((y for y, x in lens), default=None)
        for y, x in lens:
            sub[y, x] = 15 if y == top else 2
        # the hat
        t = min(y for y in range(32) if sub[y].any())          # the top of her head
        xs = [x for x in range(16) if sub[t + 3, x] != 0]
        c = (min(xs) + max(xs) + 1) // 2                       # head centre
        l, r = c - 4, c + 3                                    # crown 8 wide
        for x in range(l + 1, r):
            sub[t - 4, x] = 15
        for y in (t - 3, t - 2):
            for x in range(l, r + 1):
                sub[y, x] = 15 if x in (l, r) else (11 if x < c else 12)
        for x in range(l, r + 1):
            sub[t - 1, x] = 15 if x in (l, r) else 13            # the band
        for x in range(1, 15):
            sub[t, x] = 15 if x in (1, 14) else 11              # brim, top
        for x in range(16):
            sub[t + 1, x] = 15 if x in (0, 15) else 12          # brim, lip
        for x in (1, 2, 13, 14):
            if sub[t + 2, x] in (0, 5, 6, 7):
                sub[t + 2, x] = 15                               # the tips' underside
        for x in (0, 15):
            sub[t + 2, x] = 0
        # flowers on the band: south her right, north her left (seen from behind), side towards the back
        fx = {'S': (r - 3, r - 2, r - 1), 'N': (l + 1, l + 2, l + 3), 'W': (r - 3, r - 2, r - 1)}[fac]
        sub[t - 1, fx[0]] = 14; sub[t - 1, fx[1]] = 14; sub[t - 2, fx[1]] = 14; sub[t - 1, fx[2]] = 8
    pal[5], pal[6], pal[7] = (244, 244, 248), (204, 206, 220), (120, 122, 142)        # white hair, a touch of grey for form
    pal[8], pal[9], pal[10] = (240, 232, 208), (178, 136, 98), (112, 80, 56)         # shawl: tan, cream lights
    pal[11], pal[12], pal[13] = (150, 110, 78), (116, 80, 56), (78, 52, 36)           # brown gown and hat
    pal[14] = (214, 96, 120)                                                          # rose
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
