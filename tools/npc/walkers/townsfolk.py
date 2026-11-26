"""Walking sprites for the last townsfolk classes, each on the source game's own walker for the character its front
was drawn from (user 2026-11-26), dressed to the RECOLOURED fronts (user: walkers match the recoloured fronts;
tools/npc/picks/recolour.py).

  Old man        <- Fantasma 133  (bald crown, white hair and moustache, a pink suit): suit and trousers the front's
                    green tweed, the watch gold, the shoes brown
  Farmer         <- Fantasma 262  (wide brown hat, beard, blue overalls; user: Fantasma 212 "does not match the
                    battle sprite at all"): hat straw, skin fair, beard brown, overalls green-grey wool, shirt brown
  Templar priest <- Fantasma 231  (bald elder, long white beard, blue robe): robe white, the Order's blue at the
                    stole, the LOWER robe gold (user: "make sure the old man's pants area is gold"; his front gets the
                    gold lower robe too)
  Adventurer     <- Fantasma 142  (green brimmed hat and vest): hat tan with a red band, vest and hose red, sleeves
                    beige linen, boots dark brown
  Woodsman       <- MonoMyth 7    (spiky orange hair; the class was "labourer", renamed by the user): hair and a
                    beard in the front's russet, vest dark leather, shirt linen at the shoulders, trousers slate
  Minstrel       <- MonoMyth 0    (green turban with a white band, moustache, red coat; user: double-check 199, which
                    turned out a faceless hooded figure): turban teal, coat mustard
  Imperial Soldier <- MonoMyth 138 (white-haired warrior in brown furs; the class filed as "Imperial Officer" until
                    the user, 2026-11-26: "That's an Imperial Soldier"): hair black, uniform purple, fur gold

Fantasma walkers: 9 frames S N W walkS x2 walkN x2 walkW x2 (fa_walker.py); MonoMyth: mm_overworld.py extract.
Region remaps split a slot shared by two parts (hat and body, say) by row, from each frame's own top (walking frames
bob a row).
Run: python3 townsfolk.py  -> out/<name>_ow.png, /tmp/cult/townsfolk_ow.png"""
import os

import numpy as np
from PIL import Image, ImageDraw

from seafolk import rgba, save

HERE = os.path.dirname(os.path.abspath(__file__))
PICKS = os.path.join(HERE, '..', 'picks', 'out')


def load(name):
    im = Image.open(os.path.join(HERE, name + '.png'))
    return np.array(im).copy(), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


def frames(idx):
    return [idx[:, f * 16:(f + 1) * 16] for f in range(9)]


def remap(block, m):
    src = block.copy()
    for a, b in m.items():
        block[src == a] = b


def split(idx, row, above, below, top0=None):
    """Remap the rows above `row` with `above` and the rest with `below`; `row` is given for the standing frame and
    follows each frame's own top (walking frames bob)."""
    t0 = top0
    for sub in frames(idx):
        t = min(y for y in range(32) if sub[y].any())
        if t0 is None:
            t0 = t
        r = row + t - t0
        remap(sub[:r], above)
        remap(sub[r:], below)


def add_steps(idx, outline):
    """Draw stepping frames for a walker that has none (Fantasma 133 and 142: their walk entries point back at the
    standing frames, so in Fantasma they glide). Fantasma's own convention, read off its walkers that do step (262,
    231): the whole figure drops a row, and
      south/north: one foot steps in under the body (that foot's half of the bottom three rows moves a column
                   inward) while the other lifts out of sight behind the hem; the two walking frames are mirror
                   images (left foot, right foot);
      west:        the stride: the front foot a column forward, the back foot a column back; in the second frame
                   the front foot is lifted a row instead.
    `outline` closes the cut edges."""
    fr = frames(idx)
    for base, pair in ((0, (3, 4)), (1, (5, 6)), (2, (7, 8))):
        src = fr[base].copy()
        bottom = max(y for y in range(32) if src[y].any())
        for k, dst in enumerate(pair):
            out = np.zeros_like(src)
            out[1:] = src[:-1]                                 # the figure drops a row
            b = bottom + 1
            feet = out[b - 2:b + 1].copy()
            out[b - 2:b + 1] = 0
            xs = [x for x in range(16) if feet[:, x].any()]
            c = (min(xs) + max(xs) + 1) // 2
            if base in (0, 1):
                keep = range(0, c) if k == 0 else range(c, 16)
                dx = 1 if k == 0 else -1
                for y in range(3):
                    for x in keep:
                        if feet[y, x] and 0 <= x + dx < 16:
                            out[b - 2 + y, x + dx] = feet[y, x]
                    row = [x for x in range(16) if out[b - 2 + y, x]]
                    if row:                                    # close the cut side with the outline
                        edge = max(row) + 1 if k == 0 else min(row) - 1
                        if 0 <= edge < 16 and out[b - 2 + y, edge] == 0 and y < 2:
                            out[b - 2 + y, edge] = outline
            else:
                for y in range(3):
                    for x in range(16):
                        v = feet[y, x]
                        if not v:
                            continue
                        if x < c:                              # the front foot (he faces west)
                            nx, ny = (x - 1, y) if k == 0 else (x, y - 1)
                        else:
                            nx, ny = x + 1, y
                        if 0 <= nx < 16 and out[b - 2 + ny, nx] == 0:
                            out[b - 2 + ny, nx] = v
            fr[dst][:] = out


def old_man():
    idx, pal = load('fa_133')
    add_steps(idx, 7)
    split(idx, 22, {}, {4: 10})                                 # waistcoat to the darkest green
    split(idx, 28, {}, {12: 3, 13: 4})                         # the shoes brown
    pal[8], pal[9], pal[10] = (132, 152, 112), (94, 116, 84), (64, 82, 60)       # green tweed
    pal[7] = (40, 52, 38)                                       # trousers and outline below, dark green
    pal[5] = (192, 152, 48)                                     # the watch (5, only there) gold
    pal[11], pal[13] = (208, 208, 200), (144, 144, 136)        # hair greys, the front's
    return idx, pal


def farmer():
    idx, pal = load('fa_262')
    split(idx, 19, {1: 5, 2: 6, 3: 7, 10: 13, 9: 13}, {})      # hat: its own straw slots, the band dark brown
    split(idx, 28, {}, {2: 12, 3: 12, 4: 13})                  # boots brown
    pal[5], pal[6], pal[7], pal[11] = (220, 188, 116), (186, 150, 86), (140, 108, 60), (160, 128, 76)   # straw
    pal[1], pal[2], pal[3], pal[4] = (232, 208, 168), (216, 168, 128), (170, 118, 86), (110, 70, 50)    # skin, shirt
    pal[12], pal[13] = (122, 86, 60), (84, 58, 44)             # beard, boots
    pal[8], pal[9], pal[10] = (138, 146, 108), (110, 118, 86), (76, 82, 60)      # green-grey wool overalls
    return idx, pal


def priest():
    idx, pal = load('fa_231')
    split(idx, 26, {}, {6: 9, 5: 8})                           # the lower robe takes the gold slots
    split(idx, 29, {}, {13: 4})                                 # sandals brown
    pal[5], pal[6], pal[7] = (252, 252, 252), (226, 228, 238), (128, 136, 170)  # robe white, its outline blue-grey
    pal[13] = (80, 94, 177)                                     # the stole, the Order's blue
    pal[8], pal[9], pal[10] = (240, 212, 120), (216, 180, 84), (176, 136, 52)   # gold
    return idx, pal


def adventurer():
    idx, pal = load('fa_142')
    add_steps(idx, 15)
    split(idx, 18, {9: 5, 10: 6, 8: 7}, {})                    # hat: tan, red band
    split(idx, 21, {}, {4: 14})                                 # under the vest: beige linen
    pal[5], pal[6], pal[7] = (208, 176, 96), (168, 144, 96), (150, 50, 46)
    pal[8], pal[9], pal[10] = (224, 96, 88), (200, 76, 64), (150, 50, 46)       # vest and hose red
    pal[14] = (236, 222, 190)
    pal[12], pal[13] = (96, 64, 40), (64, 44, 30)              # hair and boots dark brown
    return idx, pal


def woodsman():
    idx, pal = load('mm_7')
    # MonoMyth 7's grey (12) is both the shirt at his shoulders and his boots, and his dark (1) both the vest and the
    # trousers: split by row. Shirt to a linen slot (14, unused), the arms bare (rolled sleeves), the shirt open at
    # the chest; trousers slate; boots dark.
    for f, sub in enumerate(frames(idx)):
        t = min(y for y in range(32) if sub[y].any())
        o = t - 8                                               # standing frames start at row 8
        remap(sub[21 + o:27 + o], {12: 14})
        remap(sub[27 + o:], {1: 2})
        # his beard (the front's): chin and jaw russet, the mouth a darker line in it
        fac = 'S' if f in (0, 3, 4) else 'W' if f in (2, 7, 8) else 'N'
        if fac == 'S':
            for x, v in zip(range(5, 11), (11, 11, 8, 8, 11, 11)):
                sub[21 + o, x] = v
            for x, v in zip(range(5, 11), (8, 11, 11, 11, 11, 8)):
                sub[22 + o, x] = v
        elif fac == 'W':
            for x, v in zip(range(3, 8), (11, 8, 8, 11, 11)):
                sub[21 + o, x] = v
            for x, v in zip(range(4, 8), (8, 11, 11, 11)):
                sub[22 + o, x] = v
    pal[10], pal[11], pal[8] = (184, 104, 92), (152, 80, 84), (112, 52, 72)     # hair and beard the front's russet
    pal[14] = (236, 224, 196)                                  # linen
    pal[12] = (60, 50, 46)                                     # boots dark
    pal[1], pal[2] = (100, 68, 50), (70, 78, 96)               # vest leather, trousers slate
    return idx, pal


def minstrel():
    idx, pal = load('mm_0')
    pal[1], pal[2], pal[3], pal[4] = (64, 128, 152), (40, 80, 104), (96, 168, 184), (150, 206, 214)   # teal
    pal[14], pal[11] = (232, 184, 72), (184, 128, 48)          # coat mustard
    return idx, pal


def soldier():
    idx, pal = load('mm_138')
    split(idx, 21, {}, {3: 13, 4: 14, 7: 15})                  # body: fur gold (its own slots)
    pal[2], pal[3], pal[1] = (60, 60, 76), (36, 36, 48), (22, 22, 30)           # hair black
    pal[9], pal[10] = (128, 90, 164), (84, 48, 116)            # uniform purple
    pal[13], pal[14], pal[15] = (248, 224, 140), (236, 204, 104), (186, 140, 52)  # fur gold
    return idx, pal


CLASSES = [('Old man', old_man, 'FA_138'), ('Farmer', farmer, 'FA_212'), ('Templar priest', priest, 'FA_110'),
           ('Adventurer', adventurer, 'FA_0'), ('Woodsman', woodsman, 'MM_89'), ('Minstrel', minstrel, 'MM_68'),
           ('Imperial Soldier', soldier, 'officer')]

if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    S = 4
    RH = 64 * 2 + 40
    sheet = Image.new('RGB', (64 * 2 + 30 + 144 * S + 20, len(CLASSES) * RH), (40, 40, 48))
    d = ImageDraw.Draw(sheet)
    for i, (name, fn, front) in enumerate(CLASSES):
        idx, pal = fn()
        save(idx, pal, os.path.join(HERE, 'out', name.lower().replace(' ', '_') + '_ow.png'))
        y = i * RH
        d.text((6, y + 4), name, fill=(255, 220, 120))
        bg = Image.new('RGBA', (128, 128), (110, 110, 125, 255))
        bg.alpha_composite(Image.open(os.path.join(PICKS, front + '.png')).convert('RGBA').resize((128, 128), Image.NEAREST))
        sheet.paste(bg, (6, y + 20))
        sheet.paste(rgba(idx, pal).resize((144 * S, 32 * S), Image.NEAREST), (64 * 2 + 30, y + 20))
    sheet.save('/tmp/cult/townsfolk_ow.png')
    print(sheet.size)
