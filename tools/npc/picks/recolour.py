"""The user's ten front picks (2026-11-25), recoloured so they read as our own and not MonoMyth's or Fantasma's
(user: "You would need to recolor them to make them different from Monomyth and distinguish them more"), with the
three reworks the user asked for: MonoMyth 116 the Merchant (new colours, hair, the hat altered), MonoMyth 30 the
Imperial Officer ("some major color changes and tweaks"; three colour options, since the army has no colours on record
yet), Fantasma 196 the Revenant (Hollow Hill's ghosts). Palette edits keep every sprite's own shading.

Run: python3 recolour.py   -> out/*.png, /tmp/cult/picks_v1.png"""
import os

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')


def load(name):
    im = Image.open(os.path.join(HERE, 'src', name + '.png'))
    return np.array(im), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


def save(idx, pal, path):
    im = Image.fromarray(idx.astype(np.uint8), 'P')
    flat = [v for c in pal for v in c]
    im.putpalette(flat + [0] * (768 - len(flat)))
    im.save(path, transparency=0)


# palette edits by index: {index: new colour}
EDITS = {
    'FA_138': ('old man', 'the suit in dark green tweed (the gold watch and cane kept)', {
        5: (132, 152, 112), 6: (94, 116, 84), 7: (64, 82, 60), 8: (36, 46, 34)}),
    'MM_22': ('old woman', 'the gown forest green, the blue ribbons rose, the orange flowers cream-gold', {
        1: (50, 82, 60), 2: (72, 110, 80), 4: (104, 140, 104), 9: (140, 56, 76), 11: (204, 104, 124), 8: (226, 186, 96)}),
    'FA_212': ('farmer', 'the denim overalls green-grey wool, the red hat straw', {
        4: (138, 146, 108), 6: (122, 130, 96), 7: (118, 126, 92), 12: (98, 106, 76), 10: (88, 94, 68), 13: (60, 64, 46),
        8: (186, 150, 86)}),
    'MM_89': ('labourer / smith', 'the hair and beard dark brown, the vest leather, the sleeves linen, the trousers slate, the bead belt brass', {
        4: (120, 76, 52), 7: (72, 50, 42), 12: (100, 68, 50), 6: (92, 100, 118), 15: (62, 68, 84),
        13: (200, 184, 150), 9: (236, 224, 196), 14: (204, 164, 76)}),
    'MM_116': ('Merchant', 'the coat bottle green, the hat and collar with it, the hair chestnut; a plume in the hat (white and red)', {
        1: (110, 168, 124), 4: (62, 116, 86), 3: (40, 58, 46), 10: (82, 110, 88), 9: (92, 56, 40), 13: (150, 96, 60)}),
    'FA_110': ('monk / Templar priest', 'the robe white, the stole the Order\'s blue, the orb on the staff gold', {
        10: (236, 236, 240), 13: (196, 200, 214), 11: (252, 252, 252), 5: (150, 180, 232), 6: (88, 128, 208),
        7: (56, 88, 160), 12: (232, 192, 72)}),
    'MM_68': ('minstrel', 'the turban and bag teal, the shirt mustard', {
        8: (96, 168, 184), 7: (64, 128, 152), 5: (40, 80, 104), 13: (232, 184, 72), 12: (184, 128, 48)}),
    'FA_14': ('witch', 'the hat and cloak moss green, the hair plum', {
        5: (128, 160, 104), 6: (96, 128, 80), 7: (64, 92, 60), 8: (40, 60, 40), 11: (156, 96, 156), 13: (120, 64, 120),
        12: (80, 40, 80)}),
    'FA_196': ('Revenant', 'a ghost of Hollow Hill: ashen spectral blue, the red eyes burning brighter', {
        1: (196, 232, 238), 2: (156, 204, 218), 3: (124, 178, 198), 4: (96, 150, 174), 5: (72, 112, 140),
        6: (58, 86, 112), 7: (50, 72, 98), 8: (42, 58, 82), 9: (34, 46, 66), 10: (28, 36, 54), 11: (20, 24, 40),
        12: (16, 20, 32), 14: (236, 60, 60)}),
}

# The Imperial Officer: the leather (11, 2) becomes the uniform, the fur (10, and 14 below the face, moved to the
# unused slot 15) the mantle; the steel and his white hair stay. Options, since the army has no colours yet.
OFFICER = {
    'A': ('crimson and grey fur', {11: (138, 36, 44), 2: (180, 70, 70), 10: (210, 210, 204), 15: (150, 150, 150)}),
    'B': ('imperial purple and gold', {11: (84, 48, 116), 2: (128, 90, 164), 10: (236, 204, 104), 15: (186, 140, 52)}),
    'C': ('forest green and brass', {11: (44, 92, 60), 2: (78, 134, 88), 10: (218, 186, 116), 15: (168, 128, 72)}),
}


def officer_rework(idx):
    """Clear the torch and its shaft (above row 13, right of his head) and the round leather bag slung behind his
    right shoulder (rows 13-19), down to the pauldron's own outline and short of his fur collar, so the pauldron,
    its spike and the collar keep every pixel and outline they had (user 2026-11-25: a first cut through rows 17-21
    had sliced the pauldron off: "his shoulder busted"). Then give the fur its own slot (15)."""
    idx = idx.copy()
    for y in range(0, 13):
        idx[y, 39:] = 0                             # the torch, its flame and shaft
    for y in range(13, 17):
        idx[y, 39:50] = 0                           # the bag (row 16 keeps the pauldron's spike at x 50-51)
    idx[17, 40:48] = 0                              # x 39: the collar's outline; x 48-51: the spike's outline
    idx[18, 41:47] = 0                              # x 40: the collar's outline; x 47: the pauldron's
    idx[19, 42:46] = 0                              # row 20 x 42-45 is the pauldron's top outline
    fur = (idx == 14)
    fur[:17] = False                               # 14 shades his face and hands too: only the fur moves
    fur[38:] = False                               # (collar, pauldron trims and cuffs, rows 17-37; hands from 38)
    idx[fur] = 15
    # the torch's yellow (3) is left only on his collar buckle: steel (13); its orange (5) only on a belt pouch:
    # skin-brown (14). That frees 3 and 5 for his face, whose shading used the leather's 2 and 11.
    idx[idx == 3] = 13
    idx[idx == 5] = 14
    face2 = (idx == 2); face2[17:] = False
    face11 = (idx == 11); face11[17:] = False
    idx[face2] = 3
    idx[face11] = 5
    return idx


OFFICER_FACE = {3: (120, 88, 80), 5: (104, 64, 48)}   # the leather's old shades, now only on his face


def merchant_plume(idx):
    """A plume in his hat: white with a red tip, rising from the crown's right, outlined (index 2 is black)."""
    idx = idx.copy()
    W, R, O = 11, 15, 2
    pts = {  # (x, y): index; a curved feather leaning back
        (41, 3): O, (42, 2): O, (43, 1): O, (44, 0): O, (45, 0): O,
        (42, 3): W, (43, 2): W, (44, 1): W, (45, 1): R, (46, 1): O,
        (43, 3): W, (44, 2): W, (45, 2): R, (46, 2): O,
        (44, 3): O, (45, 3): O,
    }
    for (x, y), v in pts.items():
        idx[y, x] = v
    # a band round the crown in the plume's red, over the row where crown meets brim
    for x in range(30, 44):
        if idx[5, x] == 3:
            idx[5, x] = R
    return idx


def rgba(idx, pal, bg=(110, 110, 125)):
    o = np.zeros(idx.shape + (3,), np.uint8)
    o[:] = bg
    for k in range(1, 16):
        o[idx == k] = pal[k]
    return Image.fromarray(o)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    tiles = []
    order = ['FA_138', 'MM_22', 'FA_212', 'MM_89', 'MM_116', 'FA_110', 'MM_30', 'MM_68', 'FA_14', 'FA_196']
    for name in order:
        idx, pal = load(name)
        before = rgba(idx, pal)
        if name == 'MM_30':
            idx2 = officer_rework(idx)
            for opt, (lab, ed) in OFFICER.items():
                p2 = list(pal)
                for k, c in list(ed.items()) + list(OFFICER_FACE.items()):
                    p2[k] = c
                save(idx2, p2, os.path.join(OUT, 'officer_%s.png' % opt))
                tiles.append((before if opt == 'A' else None, rgba(idx2, p2), 'Imperial Officer %s: %s' % (opt, lab)))
            continue
        role, note, ed = EDITS[name]
        p2 = list(pal)
        for k, c in ed.items():
            p2[k] = c
        if name == 'MM_116':
            idx = merchant_plume(idx)
        save(idx, p2, os.path.join(OUT, '%s.png' % name))
        tiles.append((before, rgba(idx, p2), '%s (%s)' % (role, name.replace('_', ' '))))
    # board: before -> after, 4 per row
    S = 3
    cw = 64 * S * 2 + 30
    rows = (len(tiles) + 3) // 4
    B = Image.new('RGB', (4 * cw + 20, rows * (64 * S + 44) + 40), (36, 36, 44))
    d = ImageDraw.Draw(B)
    d.text((10, 10), 'Your ten picks, recoloured v1 (left: source, right: ours). The Officer in three colour options.', fill=(240, 220, 120))
    for i, (b, a, lab) in enumerate(tiles):
        x, y = 10 + (i % 4) * cw, 36 + (i // 4) * (64 * S + 44)
        if b is not None:
            B.paste(b.resize((64 * S, 64 * S), Image.NEAREST), (x, y))
        B.paste(a.resize((64 * S, 64 * S), Image.NEAREST), (x + 64 * S + 8, y))
        d.text((x, y + 64 * S + 4), lab, fill=(230, 230, 230))
    B.save('/tmp/cult/picks_v1.png')
    print(B.size)
