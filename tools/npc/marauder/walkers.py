"""Marauder walkers, each on its front's own character's walker, dressed to the recoloured fronts (fronts.py):
  Goon (male)   <- MonoMyth 123, the masked bald thug in a tank top (MonoMyth 91's walker): shirt and head top undyed
                   linen as the front, the face cloth charcoal, an oxblood sash at the belt, trousers brown
  Bandit        <- Fantasma 412, long black hair, pink-purple top (Fantasma 113's walker): top oxblood
  Marauder      <- Fantasma 227, a big short-haired brute in a grey top (the front's biker has no walker of his own;
                   227 fits the build and the new short crop): hair dark brown, shirt black under a leather vest
                   with the front's grey fur collar, trousers oxblood
Run: python3 walkers.py -> out/marauder_*_ow.png, /tmp/cult/marauder_walkers_v1.png"""
import os
import sys
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'walkers'))
from seafolk import rgba, save          # noqa: E402
from fronts import OX                   # noqa: E402

TO9 = [0, 1, 2, 4, 5, 6, 7, 8, 9]       # MonoMyth's 12-frame order onto Emerald's 9


def load(name, mm12=False):
    im = Image.open(os.path.join(HERE, name + '.png'))
    a = np.array(im)
    if mm12:
        a = np.concatenate([a[:, k * 16:(k + 1) * 16] for k in TO9], axis=1)
    return a.copy(), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


def frames(idx):
    return [idx[:, f * 16:(f + 1) * 16] for f in range(9)]


def remap(block, m):
    src = block.copy()
    for a, b in m.items():
        block[src == a] = b


def goon_m():
    idx, pal = load('mm_123', mm12=True)
    for sub in frames(idx):
        o = min(y for y in range(32) if sub[y].any()) - 11      # walking frames bob a row
        remap(sub[27 + o:], {5: 9, 11: 9, 4: 9})               # trousers brown
        remap(sub[19 + o:23 + o], {3: 5, 9: 5, 11: 5})          # the face cloth (rows 19-22) charcoal
        remap(sub[26 + o:27 + o], {4: 11})                      # the sash over his belt, oxblood
    pal[2], pal[4] = (226, 214, 184), (186, 170, 136)           # linen (shirt; the head top, as the front)
    pal[5] = (76, 74, 78)                                        # charcoal (face cloth; the head's shading)
    pal[11] = OX[1]                                              # the sash
    return idx, pal


def goon_f():
    idx, pal = load('fa_412')
    pal[8], pal[9], pal[10] = OX
    return idx, pal


def chief():
    idx, pal = load('fa_227')
    # the front's grey fur collar: the vest's top edge across the shoulders (the first row of 10 under the face, and
    # the 9/10 pixels of the row above it) onto the free slot 14
    for sub in frames(idx):
        rows = [y for y in range(16, 26) if (sub[y] == 10).sum() >= 3]
        if rows:
            r = rows[0]
            remap(sub[r:r + 2], {10: 14})
    pal[11], pal[12], pal[13] = (110, 80, 60), (84, 60, 46), (44, 32, 26)     # hair dark brown
    pal[8] = (40, 36, 42)                                                       # shirt black
    pal[9], pal[10] = (124, 96, 78), (86, 66, 54)                               # the vest, leather
    pal[5], pal[6], pal[7] = OX                                                 # trousers oxblood
    pal[14] = (176, 186, 200)                                                   # fur collar, grey
    return idx, pal


WALKERS = [('Goon', goon_m, 'marauder_goon_m'), ('Bandit', goon_f, 'marauder_goon_f'),
           ('Marauder', chief, 'marauder_chief')]

if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    S = 4
    RH = 128 + 40
    sheet = Image.new('RGB', (128 + 30 + 144 * S + 20, len(WALKERS) * RH), (40, 40, 48))
    d = ImageDraw.Draw(sheet)
    for i, (name, fn, front) in enumerate(WALKERS):
        idx, pal = fn()
        save(idx, pal, os.path.join(HERE, 'out', front + '_ow.png'))
        y = i * RH
        d.text((6, y + 4), name, fill=(255, 220, 120))
        bg = Image.new('RGBA', (128, 128), (110, 110, 125, 255))
        bg.alpha_composite(Image.open(os.path.join(HERE, 'out', front + '.png')).convert('RGBA').resize((128, 128), Image.NEAREST))
        sheet.paste(bg, (6, y + 20))
        sheet.paste(rgba(idx, pal).resize((144 * S, 32 * S), Image.NEAREST), (128 + 30, y + 20))
    sheet.save('/tmp/cult/marauder_walkers_v1.png')
    print(sheet.size)
