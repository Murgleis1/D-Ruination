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
    'MM_22': ('old woman', 'the gown brown, the blue ribbons rose, the orange flowers cream-gold', {
        1: (84, 56, 40), 2: (116, 80, 56), 4: (150, 110, 78), 9: (140, 56, 76), 11: (204, 104, 124), 8: (226, 186, 96)}),
    'FA_212': ('farmer', 'the denim overalls green-grey wool, the red hat straw', {
        4: (138, 146, 108), 6: (122, 130, 96), 7: (118, 126, 92), 12: (98, 106, 76), 10: (88, 94, 68), 13: (60, 64, 46),
        8: (186, 150, 86)}),
    'MM_89': ('labourer / smith', 'the hair and beard dark brown, the vest leather, the sleeves linen, the trousers slate, the bead belt brass', {
        4: (120, 76, 52), 7: (72, 50, 42), 12: (100, 68, 50), 6: (92, 100, 118), 15: (62, 68, 84),
        13: (200, 184, 150), 9: (236, 224, 196), 14: (204, 164, 76)}),
    'MM_116': ('Merchant', 'the coat teal, the hat and collar with it, the hair chestnut; the hat\'s crown raised, a red band; flipped', {
        1: (96, 178, 176), 4: (46, 124, 128), 3: (26, 58, 62), 10: (66, 112, 116), 9: (92, 56, 40), 13: (150, 96, 60),
        14: (112, 80, 64)}),
    'FA_110': ('monk / Templar priest', 'the robe white, the stole the Order\'s blue, the orb on the staff gold', {
        10: (236, 236, 240), 13: (196, 200, 214), 11: (252, 252, 252), 5: (150, 180, 232), 6: (88, 128, 208),
        7: (56, 88, 160), 12: (232, 192, 72)}),
    'MM_68': ('minstrel', 'the turban and bag teal, the shirt mustard', {
        8: (96, 168, 184), 7: (64, 128, 152), 5: (40, 80, 104), 13: (232, 184, 72), 12: (184, 128, 48)}),
    'FA_14': ('witch', 'the hat and cloak moss green, the hair plum', {
        5: (128, 160, 104), 6: (96, 128, 80), 7: (64, 92, 60), 8: (40, 60, 40), 11: (156, 96, 156), 13: (120, 64, 120),
        12: (80, 40, 80)}),
    'FA_196': ('Revenant', 'a ghost of Hollow Hill: spectral blue; a skull face, rotted hair, the coat in rags', {
        1: (196, 232, 238), 2: (156, 204, 218), 3: (124, 178, 198), 4: (96, 150, 174), 5: (72, 112, 140),
        6: (58, 86, 112), 7: (50, 72, 98), 8: (42, 58, 82), 9: (34, 46, 66), 10: (28, 36, 54), 11: (20, 24, 40),
        12: (16, 20, 32), 14: (236, 60, 60)}),
}

# The Imperial Officer: the leather (11, 2) becomes the uniform, the fur (10, and 14 below the face, moved to the
# unused slot 15) the mantle; the steel and his white hair stay. Options, since the army has no colours yet.
# DECIDED (user 2026-11-25): purple, "the Empire's main color". A and C are kept for the record only.
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
    # close the notch the bag left between his collar and the pauldron (rows 16-19): the pauldron's dark plate (7)
    # carried up to the collar, its top edge outlined (6)
    for y in range(16, 20):
        row = idx[y]
        xs = [x for x in range(39, 52) if row[x] == 0]
        right = [x for x in range(40, 56) if row[x] != 0]
        for x in xs:
            if right and x < max(right) and any(row[x2] != 0 for x2 in range(30, x)):
                idx[y, x] = 7
    for x in range(39, 52):
        col = [y for y in range(14, 22) if idx[y, x] != 0]
        if col and idx[col[0], x] == 7:
            idx[col[0], x] = 6
    # black hair and brows (user 2026-11-25). Done by feature, not by colour: a first pass that turned every white and
    # grey in his head dark merged his bushy white brows (two rows, set straight on his black eye lines) and an eye
    # white into one dark band across his face ("racoon eyes"). Now: the hair (the crown and the locks either side
    # of the face) black with the sprite's dark steel as its sheen; each brow a thin two-pixel black stroke with a
    # row of skin between it and the eye; the rest of the old brow skin; the white of his right eye kept.
    BROW = {(23, 7): 6, (24, 7): 6, (27, 6): 6, (28, 6): 6}          # thin black strokes, a row above each eye
    BROW_TO_SKIN = [(23, 8), (24, 8), (26, 8), (27, 8), (27, 7), (28, 7), (29, 7)]   # the old bushy brows
    EYE_WHITE = [(29, 9)]
    FACE = (23, 31, 5, 16)                                            # x0, x1, y0, y1: brows and eyes live here
    for (x, y), v in BROW.items():
        idx[y, x] = v
    for x, y in BROW_TO_SKIN:
        idx[y, x] = 1
    for y in range(0, 18):
        for x in range(64):
            if (x, y) in BROW or (x, y) in EYE_WHITE:
                continue
            if FACE[0] <= x <= FACE[1] and FACE[2] <= y <= FACE[3]:
                if 12 <= y <= 14:
                    continue                                          # his grin stays white
                if (x, y) not in BROW and idx[y, x] in (9, 13) and 7 <= y <= 9:
                    continue                                          # nothing else white near the eyes is hair
            v = idx[y, x]
            if v in (9, 13, 4):
                idx[y, x] = {9: 7, 13: 8, 4: 6}[v]
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


def merchant_hat(idx):
    """The hat reshaped (user 2026-11-25: "slightly reshaped"): the crown raised two rows into a taller felt crown
    (a capotain, period for a merchant): new rows 0-1 = the old top rows 2-3, rows 2-4 = its body row 4, row 5 as it
    was (where the brim meets it); a red band round its base (a plume was tried and read as a stick). Then the whole picture is flipped (user: "flip him horizontally since I think his pose would look
    better")."""
    idx = idx.copy()
    C0, C1 = 26, 47                                 # the crown's columns
    old = idx.copy()
    idx[0, C0:C1] = old[2, C0:C1]
    idx[1, C0:C1] = old[3, C0:C1]
    for y in (2, 3, 4):
        idx[y, C0:C1] = old[4, C0:C1]
    for x in (29, 30, 31):                          # the old brooch, now specks on the raised crown: felt
        if idx[1, x] in (10, 8, 1):
            idx[1, x] = 3
    R = 15
    for x in range(29, 45):                         # the band, over the crown's base row (in the ball's red)
        if idx[4, x] in (3, 10):
            idx[4, x] = R
    # his face: 3 (dark brown; eyes, mouth) and 10 (shading under mouth and chin) are also the coat's and the hat's
    # colours, so they would turn teal with them. In the face (rows 12-16 x 26-39, row 17 x 26-34) 3 becomes the
    # outline black (2) and 10 moves to slot 14, freed by merging its 18 skin-highlight pixels into 6 (a step lighter)
    idx[idx == 14] = 6
    for y in range(12, 18):
        for x in range(26, 40 if y < 17 else 35):
            if idx[y, x] == 3:
                idx[y, x] = 2
            elif idx[y, x] == 10:
                idx[y, x] = 14
    return idx[:, ::-1].copy()


def revenant_rework(idx):
    """The Revenant (user 2026-11-25: "needs more of a skeletal face and rotting looking hair and his coat should look
    more ragged"). Index roles in Fantasma 196 (light to dark): 1-5 the pale greys (face, wisps), 6-12 the coat's
    greys, 13 black, 14 his red eye. Face: two dark sockets each with a red pinpoint, a nose cavity, hollow cheeks, a
    row of teeth with dark gaps. Hair: thinned into hanging strands with gaps of scalp. Coat: torn notches down both
    edges, a ragged hem the wisps eat into, rips with spectral light through them."""
    idx = idx.copy()
    SOCK, DEEP, RED = 12, 13, 14
    # ---- the skull (3/4 view, facing left) ----
    for p in [(22, 9), (23, 9), (22, 10), (24, 9), (24, 10)]:          # the far socket
        idx[p[1], p[0]] = SOCK
    idx[10, 23] = RED
    for p in [(26, 9), (27, 9), (28, 9), (26, 10), (28, 10), (27, 11)]:  # the near socket
        idx[p[1], p[0]] = SOCK
    idx[10, 27] = RED
    idx[11, 25] = DEEP                                                  # the nose cavity
    idx[12, 25] = SOCK
    for p in [(23, 12), (29, 12), (29, 11)]:                            # hollow cheeks
        idx[p[1], p[0]] = 5
    for x in range(24, 29):                                             # teeth: bone with dark gaps
        idx[13, x] = 1 if x % 2 == 0 else SOCK
    for x in range(24, 29):                                             # the jaw below
        if idx[14, x] != 0:
            idx[14, x] = 3 if x % 2 else 4
    # ---- rotting hair ----
    for p in [(25, 3), (28, 2), (30, 4), (24, 5), (27, 5)]:            # bald patches showing the scalp
        idx[p[1], p[0]] = 4
    for x, y0, y1 in [(22, 8, 12), (30, 8, 13), (20, 9, 14), (31, 9, 12)]:   # lank strands hanging over the face
        for y in range(y0, y1):
            idx[y, x] = 9 if (y - y0) % 2 == 0 else 10
    for x in (21, 24, 27, 30, 33):                                      # a ragged crown: bites out of the outline
        top = next((y for y in range(0, 10) if idx[y, x] != 0), None)
        if top is not None:
            idx[top, x] = 0
            idx[top + 1, x] = DEEP
    # ---- the ragged coat ----
    def coat(v):
        return 6 <= v <= 13
    for y in range(14, 50):                                             # torn notches down the right edge
        xs = [x for x in range(32, 52) if coat(idx[y, x])]
        if not xs:
            continue
        r = max(xs)
        cut = (2 if y % 7 in (0, 1) else 1 if y % 7 == 2 else 0)
        for x in range(r - cut + 1, r + 1):
            idx[y, x] = 0
        if cut and idx[y, r - cut] != 0:
            idx[y, r - cut] = DEEP
    for y in range(18, 46):                                             # and down the left edge
        xs = [x for x in range(14, 30) if coat(idx[y, x])]
        if not xs:
            continue
        l = min(xs)
        cut = (2 if y % 6 in (0, 1) else 1 if y % 6 == 2 else 0)
        for x in range(l, l + cut):
            idx[y, x] = 0
        if cut and idx[y, l + cut] != 0:
            idx[y, l + cut] = DEEP
    for x in range(20, 50):                                             # a ragged hem: wisps eat up into the coat
        ys = [y for y in range(38, 54) if coat(idx[y, x])]
        if not ys:
            continue
        b = max(ys)
        eat = (3 if x % 5 == 0 else 2 if x % 5 == 3 else 0)
        for y in range(b - eat + 1, b + 1):
            idx[y, x] = 3 if (y + x) % 2 else 2
    for x, y in [(33, 24), (36, 31), (29, 37), (40, 40), (24, 33)]:      # rips with ghost-light through them
        if coat(idx[y, x]) and coat(idx[y, x + 1]):
            idx[y, x] = 2
            idx[y, x + 1] = 3
            idx[y - 1, x] = DEEP
            idx[y - 1, x + 1] = DEEP
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
            for opt, (lab, ed) in [('B', OFFICER['B'])]:          # decided: purple, the Empire's colour
                p2 = list(pal)
                for k, c in list(ed.items()) + list(OFFICER_FACE.items()):
                    p2[k] = c
                save(idx2, p2, os.path.join(OUT, 'officer_%s.png' % opt))
                save(idx2, p2, os.path.join(OUT, 'officer.png'))
                tiles.append((before, rgba(idx2, p2), 'Imperial Officer: purple and gold, black hair'))
            continue
        role, note, ed = EDITS[name]
        p2 = list(pal)
        for k, c in ed.items():
            p2[k] = c
        if name == 'FA_196':
            idx = revenant_rework(idx)
        if name == 'MM_116':
            idx = merchant_hat(idx)
            before = Image.fromarray(np.array(before)[:, ::-1])   # shown flipped too, to compare like with like
        save(idx, p2, os.path.join(OUT, '%s.png' % name))
        tiles.append((before, rgba(idx, p2), '%s (%s)' % (role, name.replace('_', ' '))))
    # board: before -> after, 4 per row
    S = 3
    cw = 64 * S * 2 + 30
    rows = (len(tiles) + 3) // 4
    B = Image.new('RGB', (4 * cw + 20, rows * (64 * S + 44) + 40), (36, 36, 44))
    d = ImageDraw.Draw(B)
    d.text((10, 10), 'Your ten picks, recoloured v2 (left: source, right: ours).', fill=(240, 220, 120))
    for i, (b, a, lab) in enumerate(tiles):
        x, y = 10 + (i % 4) * cw, 36 + (i // 4) * (64 * S + 44)
        if b is not None:
            B.paste(b.resize((64 * S, 64 * S), Image.NEAREST), (x, y))
        B.paste(a.resize((64 * S, 64 * S), Image.NEAREST), (x + 64 * S + 8, y))
        d.text((x, y + 64 * S + 4), lab, fill=(230, 230, 230))
    B.save('/tmp/cult/picks_v1.png')
    print(B.size)
