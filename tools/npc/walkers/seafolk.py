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


def load_fa(n):
    im = Image.open(os.path.join(HERE, 'fa_%d.png' % n))
    return np.array(im), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


def mariner():
    """Fantasma 87 (user 2026-11-25: Fantasma's own sailor; the MonoMyth body first chosen was wrong)."""
    idx, pal = load_fa(87)
    idx = idx.copy()
    for f, sub in enumerate(frames(idx)):
        head = sub[:17]
        out = head.copy()
        for a, b in {8: 5, 10: 11}.items():                       # the cap's blues onto spare slots: red
            out[head == a] = b
        out[head == 14] = 5
        sub[:17] = out
        hair = sub[:22]
        out = hair.copy()
        out[hair == 12] = 4                                       # his hair onto browns of its own, so 12/13 can
        out[hair == 13] = 15                                      # be the slops' cream
        sub[:22] = out
    pal = list(pal)
    pal[5], pal[9], pal[11] = (210, 78, 62), (160, 52, 44), (112, 34, 30)    # the knitted cap, the front's red
    pal[8], pal[10] = (150, 100, 62), (104, 66, 42)                          # the shirt's stripes: leather
    pal[14] = (232, 222, 196)                                                # the shirt's white: linen
    pal[12], pal[13] = (196, 184, 156), (150, 136, 110)                      # the slops: cream linen
    return idx, pal


def mariner_mm194():
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


MM87_TO_EMERALD = [0, 1, 2, 4, 5, 6, 7, 8, 9]          # its 12 frames: S N W E, walk S x2, N x2, W x2, E x2


def witch_hat(sub, f, brim):
    """The Fisher's hat (user 2026-11-26: "go look at witch overworld sprites in MonoMyth so you can see how a witch
    hat looks"): MonoMyth 87's witch hat itself (a short crown whose floppy tip folds over to the back, a dark band
    with a buckle, a wide floppy brim drooping past the face at both sides), frame for frame, its brim set on the
    Fisher's cap line; greens -> tan felt (light 11, mid 12, dark 9), the band -> dark leather (10), the buckle ->
    tan (5), outlines black (15). Replaces a drawn tall cone ("looks like a string" at its tip)."""
    m = MM87_TO_EMERALD[f]
    w87 = np.array(Image.open(os.path.join(HERE, 'mm_87.png')))[:, m * 16:(m + 1) * 16]
    HAT = {3: 11, 1: 12, 2: 9, 5: 10, 6: 10, 7: 5}
    hat = np.isin(w87, list(HAT))
    hat[20:] = False                                       # the hat ends with the brim's drooping tips (row 19)
    # its outline (4, 15): only where it borders the hat, above the face
    edge = np.isin(w87, (4, 15)) & False
    near = np.zeros_like(hat)
    near[1:] |= hat[:-1]; near[:-1] |= hat[1:]; near[:, 1:] |= hat[:, :-1]; near[:, :-1] |= hat[:, 1:]
    edge = np.isin(w87, (4, 15)) & near
    edge[19:] = False
    rows = [y for y in range(32) if hat[y].sum() >= 8]
    b87 = max(y for y in rows if y <= 18)                  # its brim's main row
    dy = brim - b87
    for y in range(32):
        ty = y + dy
        if not 0 <= ty < 32:
            continue
        for x in range(16):
            if hat[y, x]:
                sub[ty, x] = HAT[int(w87[y, x])]
            elif edge[y, x]:
                sub[ty, x] = 15


def fisher():
    """Fantasma 221 (user 2026-11-25: "the Fisher is FA 221 ... what needs the pointy hat to match your new front
    sprite"): the baseball cap cleared and a pointed felt hat drawn in its place; the red jacket a leather jerkin, the
    white an undyed wool hood, the yellows tan breeches."""
    idx, pal = load_fa(221)
    idx = idx.copy()
    LIGHT, MID, DARK, O, HAIR = 11, 12, 9, 15, 15
    for f, sub in enumerate(frames(idx)):
        fac = FACING[f]
        ys = [y for y in range(32) if sub[y].any()]
        top = ys[0]                                               # the cap's top row
        band = sub[top:top + 7]
        xs = [x for x in range(16) if band[:, x].any()]
        x0, x1 = min(xs), max(xs)
        brim = top + 5                                            # the cap's visor row: the new brim
        sub[top:brim + 1] = 0
        for x in range(16):                                       # the cap's shadow on the forehead: black hair
            if sub[brim + 1, x] in (10, 14, 8, 9) and x0 < x < x1:
                sub[brim + 1, x] = HAIR
        witch_hat(sub, f, brim)
        # (the drawn brim, band and crown above are replaced: see witch_hat below)
    pal = list(pal)
    pal[11], pal[12] = (208, 168, 80), (168, 128, 72)             # the felt
    pal[8], pal[9], pal[10] = (150, 96, 56), (104, 64, 40), (72, 44, 30)    # the jerkin's leather
    pal[14] = (196, 188, 172)                                     # the hood: undyed wool
    pal[5], pal[6] = (190, 150, 96), (150, 112, 64)               # the breeches: tan
    return idx, pal


def fisher_mm233():
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
