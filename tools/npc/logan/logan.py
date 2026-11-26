"""Logan Orphel's battle front (user 2026-11-26: "It should be post-game Monty from monomyth (your male rival). You'll
just need to make his battle sprite the appropriate blue color you just updated the overworld sprite to").
MonoMyth's older Monty: fronts 98 and 99 (standing; 100 and 101 throw a ball). His long spiky hair goes the dark blue
of Logan's walker (townsfolk/students.py: 92,108,184 / 56,70,140 / 30,38,86); the gold stripes on his shirt, the
navy, the headband, skin and boots are kept.
Hair mask: the hair's tones (6 light gold, 1 gold, 13 white shine; 9 and 2 its shading, unless touching skin 4/11)
inside each front's hair regions (REGIONS): the crown, the long hair falling behind him, on 98 the strands over his
shoulder; never the gold sash and tassels at his waist or the boots.
Slots: 6 -> 12 (one stray pixel moved to 15 first) light blue; 1 -> 15 mid blue; 13 in the hair -> 12;
9 -> 7 (the clothes' violet-navy, nudged bluer) ; 2 -> 8 navy.
Run: python3 logan.py -> out/logan_front_98.png, out/logan_front_99.png, /tmp/cult/logan_front.png"""
import os


import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))


def load(n):
    im = Image.open(os.path.join(HERE, 'src', 'MM_%d.png' % n))
    return np.array(im).copy(), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


def save(idx, pal, path):
    im = Image.fromarray(idx.astype(np.uint8), 'P')
    im.putpalette([v for c in pal for v in c] + [0] * (768 - 48))
    im.save(path, transparency=0)


# where his hair is, by front: the crown (rows <= 22), the long hair falling behind him on the left (x <= 24 down to
# row 46 or 50), and on 98 the strands over his right shoulder; the gold sash and tassels at his waist (x >= 25 below
# row 23) and the boots (row 51 down) are kept out
REGIONS = {98: [(0, 22, 0, 63), (20, 46, 0, 24), (14, 21, 40, 49)],
           99: [(0, 22, 0, 63), (14, 50, 0, 24)]}


def hair_mask(a, n):
    region = np.zeros_like(a, bool)
    for y0, y1, x0, x1 in REGIONS[n]:
        region[y0:y1 + 1, x0:x1 + 1] = True
    cand = region & np.isin(a, (6, 1, 13, 9, 2))
    m = cand & np.isin(a, (6, 1, 13))
    shade = cand & np.isin(a, (9, 2))
    for y, x in zip(*np.where(shade)):                       # shading that touches skin is the face's own
        nb = [a[y + dy, x + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dy or dx)
              and 0 <= y + dy < 64 and 0 <= x + dx < 64]
        if any(v in (4, 11) for v in nb):
            shade[y, x] = False
    return m, shade


def logan(n):
    a, pal = load(n)
    a[a == 12] = 15                                          # the one stray pixel of 12
    m, shade = hair_mask(a, n)
    out = a.copy()
    out[m & (a == 6)] = 12
    out[m & (a == 1)] = 15
    out[m & (a == 13)] = 12
    out[shade & (a == 9)] = 7
    out[shade & (a == 2)] = 8
    pal = list(pal)
    pal[12] = (118, 136, 210)                                # hair light
    pal[15] = (88, 104, 180)                                 # hair mid (was the shirt's blue: it follows)
    pal[7] = (56, 70, 140)                                   # hair shade (was violet-navy on the clothes)
    pal[8] = (30, 38, 86)                                    # hair dark (the navy)
    return out, pal


if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    S = 3
    sheet = Image.new('RGB', (4 * (64 * S + 10) + 10, 64 * S + 34), (110, 110, 125)); d = ImageDraw.Draw(sheet)
    x = 10
    for n in (98, 99):
        idx, pal = logan(n)
        save(idx, pal, os.path.join(HERE, 'out', 'logan_front_%d.png' % n))
        for ii, pp, lab in (load(n) + ('MM %d' % n,), (idx, pal, 'Logan')):
            P = np.array(pp, np.uint8); o = np.zeros((64, 64, 3), np.uint8); o[:] = (110, 110, 125)
            for k in range(1, 16):
                o[ii == k] = P[k]
            sheet.paste(Image.fromarray(o).resize((64 * S, 64 * S), Image.NEAREST), (x, 26))
            d.text((x, 6), lab, fill=(255, 255, 0)); x += 64 * S + 10
    sheet.save('/tmp/cult/logan_front.png'); print(sheet.size)
