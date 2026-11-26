"""Walking sprites for the Merchant and the Revenant, each on the walker of the character its front was drawn from
(user 2026-11-26: "the merchant's overworld sprite is the main male character choice in the post-game of monomyth,
and the revenant is your main character you play as, the ghost Lorenzo in Fantasma").

  Merchant <- MonoMyth 70 (the post-game hero: wide brown hat with a gold band, blue hair, gold coat; 9 frames).
              Dressed to the recoloured front (tools/npc/picks/recolour.py, MM_116): the hat dark teal with a RED
              band, the hair chestnut, the coat TEAL, brown trousers, dark boots and tie.
  Revenant <- Fantasma 545 (Lorenzo's own walk set, palette tag 4409 shared with his run/bike/fish sets 537-545;
              32x32 frames, the figure in columns 9-22, cropped to x8-23 for a 16x32 walker).
              Dressed to the recoloured front (FA_196): the icy-blue ramp of the front; skull face (bone-blue, dark
              sockets over the red eyes, a dark nose), navy-black hair and coat, the strap a dark fold, the misty
              legs icy blue.

Palette slots (Merchant, MonoMyth 70's): 1/2/3 hat on the head rows, trousers on the body rows (onto 14/15, which
70 leaves unused); 4/5 the hat band on the head rows (onto 7/8, freed by the hair moving to 14/15), the coat on the
body rows; 7/8 on the body (tie, boots) onto the hat's darks 2/1; 6 outline; 9/A skin; B/C shirt.
Run: python3 merchant_revenant.py  -> out/<name>_ow.png, /tmp/cult/merchant_revenant_ow.png"""
import os

import numpy as np
from PIL import Image, ImageDraw

from seafolk import FACING, rgba, save

HERE = os.path.dirname(os.path.abspath(__file__))
BODY = 23                       # first body row (row 22 still carries the face's lower edge)


def load(name):
    im = Image.open(os.path.join(HERE, name))
    return np.array(im).copy(), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


def frames(idx):
    return [idx[:, f * 16:(f + 1) * 16] for f in range(9)]


def remap(block, m):
    src = block.copy()
    for a, b in m.items():
        block[src == a] = b


def merchant():
    idx, pal = load('mm_70.png')
    for sub in frames(idx):
        b = BODY + min(y for y in range(32) if sub[y].any()) - 12  # walking frames bob a row
        remap(sub[:b], {4: 7, 5: 8, 7: 15, 8: 14})               # band -> red (7/8), hair -> chestnut (15/14)
        remap(sub[b:], {1: 14, 2: 15, 7: 2, 8: 1})               # trousers brown; tie and boots dark teal
    pal = list(pal)
    pal[3], pal[1], pal[2] = (66, 112, 116), (40, 82, 86), (22, 46, 50)        # hat, dark teal (front's)
    pal[8], pal[7] = (200, 72, 78), (150, 40, 48)                               # band, red
    pal[5], pal[4] = (96, 178, 176), (46, 124, 128)                             # coat, teal
    pal[14], pal[15] = (150, 98, 64), (96, 60, 42)                              # hair and trousers, chestnut/brown
    return idx, pal


def revenant():
    idx, pal = load('fa_545.png')
    for f, sub in enumerate(frames(idx)):
        fac = FACING[f]
        sub[sub == 13] = 3                                        # the strap: a dark fold
        if fac == 'N':
            continue
        eyes = list(zip(*np.where(sub == 14)))
        for y, x in eyes:                                         # sockets: dark over each red eye
            if sub[y - 1, x] in (5, 6, 7):
                sub[y - 1, x] = 3
        if fac == 'S' and len(eyes) == 2:                         # a dark nose between and below the eyes
            (y0, x0), (y1, x1) = eyes
            sub[max(y0, y1) + 1, (x0 + x1) // 2] = 3
    pal = list(pal)
    pal[1] = (16, 20, 32)                                         # outline
    pal[9], pal[3], pal[10], pal[11] = (28, 36, 54), (34, 46, 66), (50, 72, 98), (72, 112, 140)   # hair, coat
    pal[7], pal[6], pal[5] = (196, 232, 238), (138, 190, 210), (88, 140, 168)  # bone face, icy mist
    pal[14] = (236, 60, 60)                                       # eyes
    return idx, pal


if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    PICKS = os.path.join(HERE, '..', 'picks', 'out')
    S = 4
    rows = []
    for name, fn, front in (('Merchant', merchant, 'MM_116'), ('Revenant', revenant, 'FA_196')):
        idx, pal = fn()
        save(idx, pal, os.path.join(HERE, 'out', name.lower() + '_ow.png'))
        rows.append((name, Image.open(os.path.join(PICKS, front + '.png')).convert('RGBA'), rgba(idx, pal)))
    W = 64 * 3 + 30 + 144 * S + 20
    sheet = Image.new('RGB', (W, len(rows) * (64 * 3 + 30)), (40, 40, 48))
    d = ImageDraw.Draw(sheet)
    for i, (name, fr, ow) in enumerate(rows):
        y = i * (64 * 3 + 30)
        d.text((6, y + 4), name, fill=(255, 220, 120))
        bg = Image.new('RGBA', (192, 192), (110, 110, 125, 255))
        bg.alpha_composite(fr.resize((192, 192), Image.NEAREST))
        sheet.paste(bg, (6, y + 20))
        sheet.paste(ow.resize((144 * S, 32 * S), Image.NEAREST), (64 * 3 + 30, y + 20 + 32))
    sheet.save('/tmp/cult/merchant_revenant_ow.png')
    print(sheet.size)
