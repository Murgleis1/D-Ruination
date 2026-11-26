"""Walking sprites for the seafolk (user 2026-11-25: "proceed"; Pelluca Valley's NPCs are replaced with these first),
from MonoMyth bodies at our cast's size, dressed to match their fronts (tools/npc/picks/recolour.py):
  Mariner  <- MonoMyth 194 (the red cap kept; the black clothes cream linen, the red trim leather, the hair brown)
  Corsair  <- MonoMyth 45  (bald, white-bearded, purple vest: MonoMyth's own walker for front 67): the vest
              oxblood, the greys sailcloth, a knotted headscarf in the vest's oxblood over his bald crown
  Fisher   <- MonoMyth 233 (a round felt hat): the crown drawn up into a leaning point (his front's pointed hat),
              tan felt, the jacket a leather jerkin
Frames: S, N, W, walk S x2, walk N x2, walk W x2 (16x32).
Run: python3 seafolk.py  -> out/<name>_ow.png, /tmp/cult/seafolk_ow.png"""
import os

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
FACING = {0: 'S', 1: 'N', 2: 'W', 3: 'S', 4: 'S', 5: 'N', 6: 'N', 7: 'W', 8: 'W'}


def load(n):
    im = Image.open(os.path.join(HERE, 'mm_%d.png' % n))
    return np.array(im), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


def frames(idx):
    return [idx[:, f * 16:(f + 1) * 16] for f in range(9)]       # views into idx


def head_top(sub, vals):
    ys = [y for y in range(32) if np.isin(sub[y], vals).any()]
    return ys[0] if ys else None


def mariner():
    idx, pal = load(194)
    idx = idx.copy()
    for f, sub in enumerate(frames(idx)):
        body = sub[22:]                                            # below the head
        out = body.copy()
        for a, b in {6: 14, 7: 13, 3: 15, 1: 15, 4: 12}.items():
            out[body == a] = b
        sub[22:] = out
    pal = list(pal)
    pal[14] = (232, 222, 196)          # linen
    pal[13] = (196, 184, 156)          # linen shade
    pal[15] = (150, 100, 62)           # leather
    pal[12] = (104, 66, 42)            # leather dark
    pal[9] = (120, 84, 56)             # hair brown
    pal[5] = (80, 56, 40)
    pal[1], pal[3], pal[4] = (210, 78, 62), (160, 52, 44), (112, 34, 30)    # the cap: the front's red
    return idx, pal


def corsair():
    idx, pal = load(45)
    idx = idx.copy()
    L, D, O = 15, 4, 8                                            # the vest's oxblood (light, dark); his outline
    for f, sub in enumerate(frames(idx)):
        t = head_top(sub, (8,))
        if t is None:
            continue
        for y in range(t + 1, t + 4):                             # the scarf over the crown, a dark band below
            for x in range(16):
                if sub[y, x] in (6, 10, 5, 12):
                    sub[y, x] = D if y == t + 3 else L
        fac = FACING[f]
        if fac == 'N':                                            # the knot, at the back of his head
            for (x, y), v in {(7, t + 4): D, (8, t + 4): D, (7, t + 5): O, (8, t + 5): O}.items():
                sub[y, x] = v
        elif fac == 'W':                                          # the tails, behind (he faces left)
            xs = [x for x in range(16) if sub[t + 3, x] != 0]
            if xs:
                bx = max(xs)
                for (dx, dy), v in {(1, 3): D, (1, 4): D, (2, 4): O, (1, 5): O}.items():
                    if bx + dx < 16:
                        sub[t + dy, bx + dx] = v
    pal = list(pal)
    pal[15], pal[4] = (150, 70, 56), (100, 44, 40)               # vest and scarf, oxblood
    pal[7], pal[1], pal[9], pal[14] = (220, 208, 180), (176, 160, 128), (140, 124, 96), (110, 96, 72)
    return idx, pal


def fisher():
    idx, pal = load(233)
    idx = idx.copy()
    LIGHT, SHADE, DARK, O = 1, 2, 4, 3
    for f, sub in enumerate(frames(idx)):
        # his body's browns (from row 18) move to the free slots, so the hat's can turn tan alone
        body = sub[18:]
        out = body.copy()
        for a, b in {1: 14, 2: 15}.items():
            out[body == a] = b
        sub[18:] = out
        # the pointed crown: from the hat's top row, five rows up, narrowing and leaning back
        t = head_top(sub, (2, 1, 4))
        xs = [x for x in range(16) if sub[t, x] != 0]
        x0, x1 = min(xs), max(xs)
        lean = 1                                                   # the tip leans back (right; facing left too)
        base = x1 - x0 + 1
        for k in range(1, 6):
            w = max(2, base - k)                                   # one narrower a row: 5, 4, 3, 2, 2
            cx0 = x0 + (k + 1) // 2 + (k // 2) * lean
            cx1 = cx0 + w - 1
            y = t - k
            for x in range(cx0, cx1 + 1):
                if not 0 <= x < 16:
                    continue
                if k == 5 or x in (cx0, cx1):
                    sub[y, x] = O
                else:
                    sub[y, x] = LIGHT if x - cx0 < w / 2 else SHADE
        # the old crown's top row: no longer the top, so felt, not outline
        for x in range(x0 + 1, x1):
            if sub[t, x] in (2, O):
                sub[t, x] = SHADE
    pal = list(pal)
    pal[1], pal[2], pal[4] = (208, 168, 80), (168, 128, 72), (104, 64, 40)    # the hat: tan felt
    pal[14], pal[15] = (150, 96, 56), (104, 64, 40)                         # his jerkin's leather
    pal[5], pal[6] = (60, 52, 44), (84, 74, 62)                             # the dark jacket: wool under the jerkin
    return idx, pal


def rgba(idx, pal, bg=(110, 110, 125)):
    o = np.zeros(idx.shape + (3,), np.uint8)
    o[:] = bg
    for k in range(1, 16):
        o[idx == k] = pal[k]
    return Image.fromarray(o)


def save(idx, pal, path):
    im = Image.fromarray(idx.astype(np.uint8), 'P')
    im.putpalette([v for c in pal for v in c] + [0] * (768 - 48))
    im.save(path, transparency=0)


if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    rows = []
    PICKS = os.path.join(HERE, '..', 'picks', 'out')
    for name, fn, front in (('mariner', mariner, 'FA_94'), ('corsair', corsair, 'MM_67'), ('fisher', fisher, 'FA_129')):
        idx, pal = fn()
        save(idx, pal, os.path.join(HERE, 'out', name + '_ow.png'))
        fr = Image.open(os.path.join(PICKS, front + '.png')).convert('RGBA')
        c = Image.new('RGBA', fr.size, (110, 110, 125, 255)); c.alpha_composite(fr)
        rows.append((name, c.convert('RGB').resize((192, 192), Image.NEAREST), rgba(idx, pal).resize((144 * 5, 32 * 5), Image.NEAREST)))
    W = 192 + 20 + 144 * 5 + 20
    S = Image.new('RGB', (W, len(rows) * 214 + 10), (36, 36, 44)); d = ImageDraw.Draw(S)
    for i, (n, fr, ow) in enumerate(rows):
        y = 10 + i * 214
        d.text((10, y), n.capitalize(), fill=(240, 220, 120))
        S.paste(fr, (10, y + 16)); S.paste(ow, (222, y + 16 + 16))
    S.save('/tmp/cult/seafolk_ow.png'); print(S.size)
