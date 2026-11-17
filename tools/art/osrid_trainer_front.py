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
PAL = {                     # colours: his character sheet (assets/osrid_reference) + the approved portrait
    0x0: (255, 0, 255),
    0xD: (10, 10, 12),      # outline
    0x2: (26, 34, 28),      # green-black (jacket, scarf and cloak shadows)
    0xF: (56, 64, 54),      # jacket dark green (sheet swatch 58,63,55)
    0xC: (38, 60, 42),      # scarf / cloak green
    0x4: (64, 90, 62),      # scarf / cloak light
    0xE: (58, 58, 58),      # iron dark (pauldron, gloves)
    0x9: (108, 104, 96),    # iron light (pauldron, buckle)
    0x5: (52, 38, 28),      # brown dark (trousers, boots)
    0xB: (92, 64, 44),      # brown mid (straps, belt, bracers, boots, lit trousers)
    0x3: (114, 42, 18),     # hair dark
    0x7: (160, 64, 28),     # hair mid
    0x6: (206, 104, 52),    # hair light
    0x8: (178, 152, 112),   # mask shadow / skin (fingers)
    0xA: (226, 210, 170),   # mask
    0x1: (246, 238, 210),   # mask highlight
}
HELMET = {0x3, 0xB, 0x8, 0xA, 0x1, 0x6, 0x7}
SCARF = [0x2, 0xC, 0x4, 0x9]
LEATHER = {0x9: 0x8, 0x4: 0xB, 0xC: 0xB, 0x2: 0x3}   # glove/boot repaint of the white ramp
D, HD, HM, HL, MS, MK, MH = 0xD, 0x3, 0x7, 0x6, 0x8, 0xA, 0x1


# Osrid's head, hand-authored at sprite scale from his portrait (silhouette guide: a dominant-vote
# downscale of portrait rows 16-60). Mask faces right, hair streams left with the wind; light
# from the upper right (the base is mirrored).
# K outline, d/m/l hair dark/mid/light, s/o/w mask shadow/cream/highlight, g glyph (black).
HEAD = [            # the approved head (round 2 head + the approved Eye of Horus), exact pixels
    ".....K...K..K.....",
    "....KlK.KlKKmK....",
    "..KmKmlKKmlmKmlK..",
    ".KmmmmlmmlmllmllK.",
    "KdmmmmmmmdsooowK..",
    ".KddmmmmdsooooowK.",
    ".KddmmmdsooKKKowK.",
    "KddmmmmdsoKoooKoK.",
    ".KddmssdsooKKKooK.",
    "..KdmsodsKKoKoKKK.",
    "KdddmmddsooKKKooK.",
    ".KdddmmdsooKoKooK.",
    "..KdddmdsKoKoKooK.",
    "...KddddKsKooKoK..",
    "....KKKKKssooKoK..",
    "........Kossoo....",
    ".........KKKK.....",
]
# The Eye of Horus on his left eye, canvas coordinates. Approved by the user 2026-11-17 13:11
# ("the mask looks correct here now"). Studied from the sheet's mask and the portrait: arched brow
# with dropping ends; almond with thick lids, pupil, inner line and outer tail; the straight
# vertical line from under the eye to the jaw; the spiral going down then curling left and up.
HORUS = [(33, 7), (34, 7), (35, 7), (32, 8), (36, 8),
         (33, 9), (34, 9), (35, 9),
         (31, 10), (32, 10), (34, 10), (36, 10), (37, 10),
         (33, 11), (34, 11), (35, 11),
         (35, 12), (35, 13), (35, 14), (35, 15),
         (33, 12), (33, 13), (32, 14), (31, 13)]
HEAD_CODE = {'K': 0xD, 'g': 0xD, 'd': 0x3, 'm': 0x7, 'l': 0x6, 's': 0x8, 'o': 0xA, 'w': 0x1}


def head_layer():
    W = max(len(r) for r in HEAD)
    out = np.zeros((len(HEAD), W), int)
    for y, row in enumerate(HEAD):
        for x, ch in enumerate(row):
            if ch in HEAD_CODE:
                out[y, x] = HEAD_CODE[ch]
    return out, out > 0


def line_px(x0, y0, x1, y1):
    n = max(abs(x1 - x0), abs(y1 - y0))
    return [(round(x0 + (x1 - x0) * i / n), round(y0 + (y1 - y0) * i / n)) for i in range(n + 1)]


PAULDRON = {16: (41, 45), 17: (39, 46), 18: (38, 47), 19: (38, 47), 20: (39, 47), 21: (40, 46), 22: (41, 45)}
PAULDRON_R = {17: (21, 24), 18: (20, 25), 19: (19, 26), 20: (19, 26), 21: (20, 25)}   # his right shoulder
HANDS = [(18, 29, 53, 64), (21, 28, 35, 43)]           # (y0, y1, x0, x1): pointing hand, chest hand
BRACERS = [(18, 27, 47, 53), (21, 28, 30, 35)]
SCARF_SET = {0x2, 0xC, 0x4}


def body(k):
    """Osrid's outfit on Kakugo's mirrored body, from Kakugo's own indices (k)."""
    a = np.zeros_like(k)
    H, W = k.shape
    in_hand = np.zeros_like(k, bool)
    for y0, y1, x0, x1 in HANDS:
        in_hand[y0:y1, x0:x1] = True
    for y in range(H):
        for x in range(W):
            v = k[y, x]
            if v == 0: continue
            if v == D: a[y, x] = D; continue
            if in_hand[y, x] and v in (0x9, 0x4, 0xC, 0x2):          # fingerless dark gloves
                a[y, x] = {0x9: 0x8, 0x4: 0xE, 0xC: 0x2, 0x2: D}[v]; continue
            if v in (0x9, 0x4, 0xC, 0x2):                             # scarf: his dark green
                a[y, x] = {0x9: 0x4, 0x4: 0xC, 0xC: 0xC, 0x2: 0x2}[v]; continue
            if v in (0xE, 0xF):
                if y <= 34 or (x >= 44 and y <= 28) or (y <= 40 and x >= 23):   # quilted jacket, to mid-thigh
                    a[y, x] = 0x2 if v == 0xE else 0xF
                    if v == 0xF and ((x + y) % 6 == 0 or (x - y) % 6 == 0):
                        a[y, x] = 0x2
                elif x <= 22 and y <= 50:                             # the cloak behind
                    a[y, x] = 0xC if v == 0xF else 0x2
                else:                                                 # trousers
                    a[y, x] = 0xB if v == 0xF else 0x5
                continue
            if v == 0x5:
                a[y, x] = 0x5; continue
            if v in (0x6, 0x7, 0x3) and y >= 35:                      # coat lining -> cloak inside
                a[y, x] = 0x2; continue
            if y >= 50:                                               # boots
                a[y, x] = 0xB if v in (0xB, 0x1, 0x4, 0x8, 0xA) else 0x5; continue
            a[y, x] = 0xB if v in (0xB, 0x3) else 0x9 if v in (0x1, 0xA, 0x8) else 0x2
    # light rim on the cloak's upper edges
    for y in range(35, 51):
        for x in range(0, 25):
            if a[y, x] == 0xC and a[y - 1, x] in (0, D):
                a[y, x] = 0x4
    jacket = lambda v: v in (0x2, 0xF, 0x9)
    # straps crossing the chest (under the scarf)
    for (x0, y0, x1, y1) in ((41, 18, 22, 30), (24, 18, 40, 30)):
        for x, y in line_px(x0, y0, x1, y1):
            if jacket(a[y, x]): a[y, x] = 0xB
            if y + 1 < H and jacket(a[y + 1, x]): a[y + 1, x] = 0x5
    # belt, square buckle, pouch
    for x in range(18, 45):
        if jacket(a[30, x]) or a[30, x] == 0xB: a[30, x] = 0xB
        if jacket(a[31, x]) or a[31, x] in (0xB, 0x5): a[31, x] = 0x5
    for x in range(30, 34):
        for y in range(29, 33):
            a[y, x] = 0x9 if (x in (30, 33) or y in (29, 32)) else 0x5
    for x in range(29, 35):
        for y in (28, 33):
            if a[y, x] != 0: a[y, x] = D
    for y in range(32, 37):
        for x in range(37, 41):
            a[y, x] = D if (x in (37, 40) or y in (32, 36)) else 0xB
    a[34, 38] = 0x9
    # pauldron on his left shoulder (viewer's right); the scarf stays on top
    pm = np.zeros_like(a, bool)
    for y, (x0, x1) in list(PAULDRON.items()) + list(PAULDRON_R.items()):
        for x in range(x0, x1 + 1):
            if a[y, x] not in SCARF_SET:
                pm[y, x] = True
    for y, x in zip(*np.nonzero(pm)):
        a[y, x] = 0x9 if y <= 17 else 0xE
    for (x, y) in ((42, 17), (43, 17), (41, 18), (40, 19), (22, 18), (23, 18), (21, 19)):
        if pm[y, x]: a[y, x] = 0x9
    ring = np.zeros_like(pm)
    ring[1:] |= pm[:-1]; ring[:-1] |= pm[1:]; ring[:, 1:] |= pm[:, :-1]; ring[:, :-1] |= pm[:, 1:]
    for y, x in zip(*np.nonzero(ring & ~pm)):
        if a[y, x] not in SCARF_SET: a[y, x] = D
    for y in range(17, 23):                                           # lower rim line
        x = PAULDRON[y][1]
        if pm[y, x]: a[y, x] = D
    for y, (x0, x1) in PAULDRON_R.items():
        if pm[y, x0]: a[y, x0] = D
    # leather bracers (wrapped: darker band every third column)
    for y0, y1, x0, x1 in BRACERS:
        for y in range(y0, y1):
            for x in range(x0, x1):
                if jacket(a[y, x]): a[y, x] = 0x5 if x % 3 == 0 else 0xB
    # trousers: flatten Kakugo's coat-panel noise into two clean tones
    tr = np.isin(a, [0x5, 0xB]) & (np.arange(H)[:, None] >= 41) & (np.arange(H)[:, None] < 50)
    for _ in range(2):
        src = a.copy()
        for y, x in zip(*np.nonzero(tr)):
            win = src[y - 1:y + 2, x - 1:x + 2]; win = win[np.isin(win, [0x5, 0xB])]
            if len(win) >= 5: a[y, x] = 0xB if np.count_nonzero(win == 0xB) > len(win) // 2 else 0x5
    # shin wraps: single diagonal leather bands into the boots
    for y in range(47, 56):
        for x in range(14, 45):
            if a[y, x] in (0x5, 0xB):
                a[y, x] = 0xB if (x + y) % 3 == 0 else 0x5
    # jacket hem: a dark line where the jacket meets the trousers
    for x in range(23, 44):
        if a[41, x] in (0x5, 0xB) and a[40, x] in (0x2, 0xF, 0x9): a[41, x] = D
    return a


def build(F):
    k, _ = F[10]
    k = k.copy()[:, ::-1]      # mirrored: points right, scarf blows left, faces right
    a = body(k)
    # remove the helmet: every helmet-coloured pixel in Kakugo's head box (by Kakugo's indices)
    y0, y1, x0, x1 = 1, 19, 22, 44
    hb = np.isin(k[y0:y1, x0:x1], list(HELMET))
    a[y0:y1, x0:x1][hb] = 0
    keep = {0x2, 0xC, 0x4, 0xE, 0xF, 0x5}
    for y in range(y0, y1):
        for x in range(x0, x1):
            if a[y, x] == D:
                nb = a[max(0, y - 1):y + 2, max(0, x - 1):x + 2]
                if not np.any(np.isin(nb, list(keep))):
                    a[y, x] = 0
    for y in range(15, 19):                      # chin gap above the neck scarf -> scarf
        for x in range(27, 37):
            x = 63 - x
            if a[y, x] == 0 and a[y + 1, x] in SCARF_SET | {D}:
                a[y, x] = 0xC
    head, hm = head_layer()
    hy, hx = 1, 22
    region = a[hy:hy + head.shape[0], hx:hx + head.shape[1]]
    region[hm] = head[hm]
    for (x, y) in HORUS:
        a[y, x] = D
    for y in range(y0, y1):
        for x in range(x0, x1):
            if a[y, x] == D:
                nb = a[max(0, y - 1):y + 2, max(0, x - 1):x + 2]
                if not np.any((nb != 0) & (nb != D)):
                    a[y, x] = 0
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
