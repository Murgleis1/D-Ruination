"""Logan Orphel's battle front. DECIDED (user 2026-11-26, "its this one"): MonoMyth front 114 is post-game Monty
(blond ponytail, blue coat, orange sash). logan_114() below; the 98/99 recolours further down were a wrong guess
(98-101 are a different character) kept only for the record.

Earlier: Logan Orphel's battle front (user 2026-11-26: "It should be post-game Monty from monomyth (your male rival). You'll
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


def tunic(a):
    """(user 2026-11-26: "make it so it looks less like a karate suit and more like a tunic on the battle front
    sprite"): the gi's crossed lapels (the orange V, 8, rows 16-30) become plain tunic cloth (1; an orange trim along
    the collar read as the lapel again, so the neck is left plain); the tied sash and its hanging tails become a leather belt (5,
    rows 34-35, an orange buckle at its middle) with the tails gone (8/5 below it to coat shade 3); the coat runs on
    as a tunic skirt to row 43, hemmed in orange at row 44; the trousers below stay the same light grey. Coordinates
    are MonoMyth 114's own, before the flip."""
    a = a.copy()
    v = np.zeros_like(a, bool); v[16:31] = True
    a[v & (a == 8)] = 1
    chest = np.zeros_like(a, bool); chest[19:33, 22:40] = True   # the gi's brown fold shading: grey cloth shade
    a[chest & (a == 5)] = 3
    # the belt, after the belts on MonoMyth's and Fantasma's fronts (MonoMyth 30 and 37, Fantasma 55: a band of dark
    # leather two pixels deep with the cloth meeting it above and below, and a small metal buckle with a dark centre):
    # rows 34-35 near-black across the waist, the cloth rows 33 and 36 left plain, the buckle a 3x4 orange-gold frame
    # (rows 33-36, x 29-31) round a dark centre
    for y in (34, 35):
        for x in range(22, 39):
            if a[y, x] in (1, 3, 4, 8, 5, 2):
                a[y, x] = 2
    for y in (33, 36):
        for x in range(22, 39):
            if a[y, x] in (8, 5):
                a[y, x] = 3
    for y in range(33, 37):
        for x in range(29, 32):
            a[y, x] = 2 if (x == 30 and y in (34, 35)) else 8
    # the sash's hanging tails, rows 37-44 between x 26 and 33: their colours AND their outlines go to cloth (user:
    # "what is this", of a U of dark lines left where only their colours had been taken out the first time)
    strip = np.zeros_like(a, bool); strip[37:45, 26:34] = True
    a[strip & np.isin(a, (8, 5, 2, 4, 3))] = 1               # plain cloth, as the skirt round it
    for x in range(20, 43):                                  # the hem
        if a[44, x] in (1, 3, 4, 2) and a[44, x - 1] != 0 and a[44, x + 1] != 0:
            a[44, x] = 8
    # trousers: the tunic's own light grey, as before the tunic rework (user: "The pants are not supposed to be two
    # toned at all. look at your original"; a brown pair under the grey tunic had read as two-tone)
    return a


def logan_114():
    """MonoMyth 114: his hair is 7 (light gold) and 10 (gold) only, plus the brown 5 as its outline and shading where
    it touches them in the hair's rows (5 is also his sash and shoes): 7 and 10 go light and mid blue; the hair's 5
    moves to the unused slot 14, a deep blue."""
    a, pal = load(114)
    hair5 = np.zeros_like(a, bool)
    for y, x in zip(*np.where(a == 5)):
        if y > 24:
            continue
        nb = [a[y + dy, x + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1) if (dy or dx)
              and 0 <= y + dy < 64 and 0 <= x + dx < 64]
        if y <= 12 or any(v in (7, 10) for v in nb):
            hair5[y, x] = True
    a[hair5] = 14
    a = tunic(a)
    pal = list(pal)
    pal[7], pal[10], pal[14] = (118, 136, 210), (84, 100, 176), (52, 64, 132)   # Logan's dark blue
    # (user 2026-11-26: "change their clothes color on both overworld and front battle sprite to an orange and light
    # grey mix and flip the front battle sprite horizontally to make his pose more unique than monomyth's"):
    # the blue coat and trousers (1 light, 3 mid, 4 dark) light grey; his orange sash and trim kept and warmed
    pal[1], pal[3], pal[4] = (208, 208, 214), (156, 156, 166), (92, 88, 96)
    pal[8] = (236, 132, 44)
    pal[5] = (124, 86, 60)                                   # shoes and collar edge: plain brown
    return a[:, ::-1].copy(), pal                            # flipped


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
    sheet.save('/tmp/cult/logan_front_9899.png')
    idx, pal = logan_114()
    save(idx, pal, os.path.join(HERE, 'out', 'logan_front.png'))
    sheet = Image.new('RGB', (2 * (64 * S + 10) + 10, 64 * S + 34), (110, 110, 125)); d = ImageDraw.Draw(sheet)
    for j, (ii, pp, lab) in enumerate((load(114) + ('MonoMyth 114 (post-game Monty)',), (idx, pal, 'Logan'))):
        P = np.array(pp, np.uint8); o = np.zeros((64, 64, 3), np.uint8); o[:] = (110, 110, 125)
        for k in range(1, 16):
            o[ii == k] = P[k]
        sheet.paste(Image.fromarray(o).resize((64 * S, 64 * S), Image.NEAREST), (10 + j * (64 * S + 10), 26))
        d.text((10 + j * (64 * S + 10), 6), lab, fill=(255, 255, 0))
    sheet.save('/tmp/cult/logan_front.png'); print(sheet.size)
