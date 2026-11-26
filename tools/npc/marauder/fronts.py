"""The Marauders (user 2026-11-26): a trainer class of pillagers and thieves who rob travellers and sometimes band into
gangs to invade towns. Three fronts, from the user's picks on marauder_cands_v1.png:
  Marauder Goon (male)   <- MonoMyth 91, the bald thug: tank top to an undyed linen shirt, camo trousers to brown
                            leather, the camo face cloth to the gang's oxblood
  Marauder Goon (female) <- Fantasma 113, the black-clad rogue: the purple top and gloves oxblood, the pink streak in
                            her hair oxblood, black kept, the belt brass
  Marauder Chief         <- Fantasma 151, the bald brute (user: "get rid of his bike, center him and give him a
                            little hair and more medieval clothing"): the motorcycle removed, the figure centred, a
                            short dark crop, the jeans and wristbands oxblood wool and leather (the gang's colour, worn
                            by the chief), the leather vest with its fur collar and the black shirt kept
The gang colour, oxblood, is the one shared mark: purple is the Empire's, so the Marauders are kept off it.
Run: python3 fronts.py -> out/marauder_*.png, /tmp/cult/marauder_fronts_v1.png"""
import os
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OX = [(176, 60, 62), (128, 40, 44), (86, 26, 32)]          # oxblood: light, mid, dark


def load(name):
    im = Image.open(os.path.join(HERE, 'src', name + '.png'))
    return np.array(im).copy(), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


def save(idx, pal, path):
    im = Image.fromarray(idx.astype(np.uint8), 'P')
    im.putpalette([v for c in pal for v in c] + [0] * (768 - 48))
    im.save(path, transparency=0)


def remap(block, m):
    src = block.copy()
    for a, b in m.items():
        block[src == a] = b


def goon_m():
    idx, pal = load('MM_91')
    remap(idx[13:], {2: 15, 3: 15})                         # below the head: the darks onto a free slot
    remap(idx[31:], {7: 13, 4: 14})                         # trousers off the camo slots
    pal[13], pal[14], pal[15] = (112, 80, 56), (94, 66, 46), (66, 46, 36)       # brown leather, boots darker
    pal[6], pal[8] = (226, 214, 184), (186, 170, 136)       # undyed linen shirt
    pal[7], pal[2] = OX[1], OX[2]                           # 7 and 2 are left only on his face cloth
    return idx, pal


def goon_f():
    idx, pal = load('FA_113')
    pal[5], pal[6], pal[7] = OX                             # top and gloves
    pal[13] = OX[0]                                         # the streak in her hair
    pal[11] = (204, 164, 76)                                # belt brass
    return idx, pal


def chief():
    idx, pal = load('FA_151')
    m = idx
    m[:, :19] = 0                                            # the motorcycle: its wheel and frame left of x 19
    for y in range(0, 37):                                   # its handlebar where it meets his shoulder
        for x in range(19, 25):
            if m[y, x] in (5, 6, 7, 8, 9, 14):
                m[y, x] = 0
    for y in range(37, 57):                                  # its engine beside his hand and knee
        for x in range(19, 26):
            if m[y, x] in (5, 6, 7, 8, 9, 11, 12, 13, 14):
                m[y, x] = 0
    changed = True                                           # outline pixels left floating on the cut side
    while changed:
        changed = False
        for y in range(64):
            for x in range(27):
                if m[y, x] == 15:
                    nb = [m[y + dy, x + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1)
                          if (dy or dx) and 0 <= y + dy < 64 and 0 <= x + dx < 64]
                    if not any(v not in (0, 15) for v in nb):
                        m[y, x] = 0
                        changed = True
    # the bike's mirror, poking up behind his right shoulder (rows 3-6, the jeans' blue 8 there), with its outline
    for y in range(0, 8):
        for x in range(40, 56):
            if m[y, x] == 8:
                m[y, x] = 0
    for y in range(0, 8):
        for x in range(40, 56):
            if m[y, x] == 15:
                nb = [m[y + dy, x + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1)
                      if (dy or dx) and 0 <= y + dy < 64 and 0 <= x + dx < 64]
                if not any(v not in (0, 15) for v in nb):
                    m[y, x] = 0
    # (user 2026-11-26: "this thing ... between his legs is a remnant of the bike"): the seat and engine block
    # showing between his knees (rows 46-53, the vest-brown 11/12/13 there) and the tyre's bottom below them (row 56)
    # cleared; the floating outline swept; the inner edges of his legs outlined where they now meet empty space
    gap = np.zeros_like(m, bool); gap[45:57, 33:47] = True
    m[gap & np.isin(m, (11, 12, 13))] = 0
    m[56, 35:42][m[56, 35:42] == 9] = 0
    for _ in range(3):
        for y in range(45, 57):
            for x in range(33, 47):
                if m[y, x] == 15:
                    nb = [m[y + dy, x + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dy or dx)]
                    if not any(v not in (0, 15) for v in nb):
                        m[y, x] = 0
    cleared = gap & (m == 0)
    for y, x in zip(*np.where(cleared)):
        if any(m[y + dy, x + dx] in (8, 9) for dy, dx in ((0, 1), (0, -1), (-1, 0), (1, 0))):
            m[y, x] = 15
    # (user 2026-11-26: "what are these things behind his legs sticking out?"): the bike's lower frame and the stub of
    # its tyre behind his shins (rows 52-56): any blue there not joined to either leg's own trouser pixels (flood from
    # each thigh through the trouser blues) is the bike; cleared, floating outline swept, the shins outlined
    from collections import deque
    legs = np.zeros_like(m, bool)
    for seed in ((50, 30), (50, 50)):
        q = deque([seed])
        while q:
            y, x = q.popleft()
            if not (0 <= y < 57 and 0 <= x < 64) or legs[y, x] or m[y, x] not in (8, 9):
                continue
            legs[y, x] = True
            q.extend(((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)))
    win = np.zeros_like(m, bool); win[52:57, 33:50] = True
    m[win & np.isin(m, (8, 9)) & ~legs] = 0
    for _ in range(3):
        for y in range(52, 58):
            for x in range(33, 50):
                if m[y, x] == 15:
                    nb = [m[y + dy, x + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dy or dx)]
                    if not any(v not in (0, 15) for v in nb):
                        m[y, x] = 0
    for y in range(52, 58):                                  # the bar's outline that ran along under his shins
        for x in range(33, 50):
            if m[y, x] == 15 and not any(m[y + dy, x + dx] in (8, 9) or (legs[y + dy, x + dx])
                                         for dy in (-1, 0, 1) for dx in (-1, 0, 1)) \
                    and not any(m[y + dy, x + dx] in (4, 11, 12, 13) for dy in (-1, 0, 1) for dx in (-1, 0, 1)):
                m[y, x] = 0
    for y in range(52, 58):
        for x in range(33, 50):
            if m[y, x] == 0 and any(legs[y + dy, x + dx] for dy, dx in ((0, 1), (0, -1), (1, 0))):
                m[y, x] = 15
    for y in range(37, 64):                                  # close the cut edge of his legs
        xs = [x for x in range(64) if m[y, x]]
        if xs and m[y, xs[0]] != 15 and xs[0] > 0:
            m[y, xs[0] - 1] = 15
    # free slot 7 for his hair: its few fur pixels to the fur's 6, on the belt buckle to 5
    belt = np.zeros_like(m, bool); belt[37:42, 30:46] = True
    m[belt & (m == 7)] = 5
    m[m == 7] = 6
    # a little hair: a short dark crop over the crown (rows 1-5) and down the temples (rows 6-8 at the sides),
    # the scalp's shine (14) with it; outline kept
    for y in range(0, 9):
        xs = [x for x in range(64) if m[y, x] in (1, 2, 3, 4, 14)]
        if not xs:
            continue
        x0, x1 = min(xs), max(xs)
        for x in xs:
            if y <= 5 or x <= x0 + 1 or x >= x1 - 1:
                if y <= 6 or m[y, x] != 14:
                    m[y, x] = 7 if (x + y) % 5 else 13
    # centre the figure
    xs = np.where(m.any(0))[0]
    shift = int(round((xs.min() + xs.max()) / 2 - 31.5))
    m2 = np.zeros_like(m)
    if shift > 0:
        m2[:, :64 - shift] = m[:, shift:]
    else:
        m2[:, -shift:] = m[:, :64 + shift]
    pal[7] = (64, 46, 36)                                    # hair
    pal[8], pal[9] = OX[1], OX[2]                            # trousers and bracers, oxblood
    return m2, pal


FRONTS = [('Marauder Goon (M)', goon_m, 'MM_91'), ('Marauder Goon (F)', goon_f, 'FA_113'),
          ('Marauder Chief', chief, 'FA_151')]

if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    S = 3
    sheet = Image.new('RGB', (len(FRONTS) * (64 * S * 2 + 40) + 10, 64 * S + 40), (40, 40, 48))
    d = ImageDraw.Draw(sheet)
    for i, (name, fn, src) in enumerate(FRONTS):
        idx, pal = fn()
        save(idx, pal, os.path.join(HERE, 'out', name.lower().replace(' ', '_').replace('(', '').replace(')', '') + '.png'))
        x = 10 + i * (64 * S * 2 + 40)
        d.text((x, 6), name + '  (' + src.replace('_', ' ') + ': before | after)', fill=(255, 220, 120))
        for j, (ii, pp) in enumerate((load(src), (idx, pal))):
            o = np.zeros((64, 64, 3), np.uint8); o[:] = (110, 110, 125)
            for k in range(1, 16):
                o[ii == k] = pp[k]
            sheet.paste(Image.fromarray(o).resize((64 * S, 64 * S), Image.NEAREST), (x + j * (64 * S + 8), 24))
    sheet.save('/tmp/cult/marauder_fronts_v1.png')
    print(sheet.size)
