"""Osrid trainer FRONT pic, candidate A (2026-11-17).

Base: Kakugo's MonoMyth front pic (#10), used for anatomy and pose only. This follows the
user-approved overworld approach ("Osrid's head on Kakugo's body"). Everything Kakugo-specific is
replaced:
  * Helmet and goggles: removed. Osrid's head is drawn new (red-orange spiky hair swept by the same
    wind as the scarf, a flat cream mask with the black eye glyph and drip), built from primitives.
    It is cel-shaded in 3 tones per material with light from the upper left, then given a black
    outline.
  * White scarf: Osrid's dark green. White gloves: tan leather. Charcoal coat: his dark armour
    brown-grey. Red lining: his hair orange-red as the accent. Grey trousers: dark leather.
Spec: tools/art/MONOMYTH_TRAINER_STYLE.md (black selective outline, 15 colours, 3 tones each).

Usage: python3 -I osrid_trainer_front.py MM_TRAINERS_PKL OUT.png
"""
import sys, pickle
import numpy as np
from PIL import Image

# Kakugo index -> role. 0 bg, D outline, E/F coat, 5 trousers, 2/C/4/9 scarf ramp (also gloves),
# 3/B/8/A/1 helmet, 6/7 eyes (7 = coat lining too).
PAL = {
    0x0: (255, 0, 255),
    0xD: (8, 8, 10),        # outline
    0xE: (44, 40, 42),      # armour/coat dark
    0xF: (108, 96, 82),     # armour/coat mid
    0x5: (74, 56, 44),      # leather trousers
    0x2: (24, 38, 28),      # scarf darkest
    0xC: (40, 64, 44),      # scarf dark
    0x4: (62, 94, 62),      # scarf mid
    0x9: (96, 130, 84),     # scarf light
    0x3: (90, 34, 18),      # hair dark / leather shadow
    0x7: (156, 62, 26),     # hair mid / lining
    0x6: (210, 104, 50),    # hair light
    0xB: (126, 84, 52),     # leather (gloves, belts, boots)
    0x8: (184, 158, 118),   # mask shadow / glove light
    0xA: (230, 214, 172),   # mask
    0x1: (248, 240, 212),   # mask highlight
}
HELMET = {0x3, 0xB, 0x8, 0xA, 0x1, 0x6, 0x7}
SCARF = [0x2, 0xC, 0x4, 0x9]
LEATHER = {0x9: 0x8, 0x4: 0xB, 0xC: 0xB, 0x2: 0x3}   # glove/boot repaint of the white ramp
D, HD, HM, HL, MS, MK, MH = 0xD, 0x3, 0x7, 0x6, 0x8, 0xA, 0x1


# Osrid's head, hand-authored at sprite scale from his portrait (silhouette guide: a dominant-vote
# downscale of portrait rows 16-60). Mask faces right, hair streams left with the wind; light
# from the upper right (the base is mirrored).
# K outline, d/m/l hair dark/mid/light, s/o/w mask shadow/cream/highlight, g glyph (black).
HEAD = [
    ".........K..K........",
    "........KlK.KlK.K....",
    "......K.KmlKKlmKKlK..",
    ".....KmKmlmmllmlllK..",
    "..KKddmmlmmlmlllllK..",
    "KdddddmmdmmlmllmlllK.",
    ".KKddddmmdmmmlKKKKK..",
    "...KddmmdmmmKsoooowK.",
    ".KdddddmmdmmKsoooooK.",
    "..KKdddmmdmdKsogggoK.",
    ".KKKdddmmdsoKsgogogK.",
    "KddddddmmdssKsogggoK.",
    ".KKdddddmdddKssgooK..",
    ".....KKddddKKssgoK...",
    ".......KKKKKKKssK....",
    ".............KKK.....",
]
HEAD_CODE = {'K': 0xD, 'g': 0xD, 'd': 0x3, 'm': 0x7, 'l': 0x6, 's': 0x8, 'o': 0xA, 'w': 0x1}


def head_layer():
    W = max(len(r) for r in HEAD)
    out = np.zeros((len(HEAD), W), int)
    for y, row in enumerate(HEAD):
        for x, ch in enumerate(row):
            if ch in HEAD_CODE:
                out[y, x] = HEAD_CODE[ch]
    return out, out > 0


def build(F):
    a, _ = F[10]
    a = a.copy()[:, ::-1]      # mirrored: points right, scarf blows left, faces right
    # gloves and boots: white ramp -> leather (left glove, chest hand, boots)
    for (y0, y1, x0, x1) in ((18, 28, 53, 64), (22, 27, 35, 43), (55, 64, 14, 44)):
        sub = a[y0:y1, x0:x1]
        for k, v in LEATHER.items():
            sub[a[y0:y1, x0:x1] == k] = v
    # belt buckle keeps its own metal colours (the white ramp there would turn green)
    bk = a[28:35, 30:38]; bk[bk == 0x9] = 0x1; bk[bk == 0x4] = 0x8
    # remove the helmet: every helmet-coloured pixel in the head box, then orphan outline there
    y0, y1, x0, x1 = 1, 19, 22, 44
    box = a[y0:y1, x0:x1]
    box[np.isin(box, list(HELMET))] = 0
    keep = {0x2, 0xC, 0x4, 0x9, 0xE, 0xF, 0x5}
    for y in range(y0, y1):
        for x in range(x0, x1):
            if a[y, x] == D:
                nb = a[max(0, y - 1):y + 2, max(0, x - 1):x + 2]
                if not np.any(np.isin(nb, list(keep))):
                    a[y, x] = 0
    # chin gap above the neck scarf -> scarf
    for y in range(15, 19):
        for x in range(27, 37):
            x = 63 - x
            if a[y, x] == 0 and a[y + 1, x] in SCARF + [D]:
                a[y, x] = 0xC
    head, hm = head_layer()
    hy, hx = 1, 18
    region = a[hy:hy + head.shape[0], hx:hx + head.shape[1]]
    region[hm] = head[hm]
    # orphan outline: D in the head box with no coloured 8-neighbour
    for y in range(y0, y1):
        for x in range(x0, x1):
            if a[y, x] == D:
                nb = a[max(0, y - 1):y + 2, max(0, x - 1):x + 2]
                if not np.any((nb != 0) & (nb != D)):
                    a[y, x] = 0
    # enclosed transparent pixels left by the helmet removal -> outline
    for y in range(1, 63):
        for x in range(1, 63):
            if a[y, x] == 0 and all(a[y + dy, x + dx] != 0 for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                a[y, x] = D
    return a


def save(a, path):
    img = Image.fromarray(a.astype(np.uint8), 'P')
    flat = []
    for i in range(16):
        flat += list(PAL[i])
    img.putpalette(flat + [0] * (768 - 48))
    img.save(path, transparency=0)


if __name__ == '__main__':
    F = pickle.load(open(sys.argv[1], 'rb'))
    save(build(F), sys.argv[2])
