"""Osrid's overworld sprite from MonoMyth's Sunbeached Cliffs masked man: the dark green bug mask
(overworld #136, portraits #383-390; user 2026-11-16 -- NOT the spiked-helmet man #156 of draft 1).

Same shapes and animation; Osrid's identity by region + palette:
  * the bug hood (teal ramp 5/7)        -> his dark green hood (his scarf's green)
  * the red antennae (top rows)         -> tufts of his red-orange hair
  * the visor + red face plate (the eye row down 4 rows, inner columns) -> his cream mask:
    reds -> mask ramp d/e/f, eye glints -> the black eye holes of the mask
  * grey-teal body 9/a, dark 3          -> dark armour; red trim elsewhere -> bronze straps
Run: python3 -I osrid_ow.py SRC_9FRAME.png OUT.png
"""
import sys
import numpy as np
from PIL import Image

PAL = {
    1: (16, 12, 12),      # outline
    2: (96, 30, 20),      # hair dark
    3: (44, 44, 48),      # armour dark
    4: (200, 90, 36),     # hair mid
    5: (70, 104, 74),     # hood light
    6: (232, 128, 56),    # hair light
    7: (40, 66, 46),      # hood mid
    8: (248, 248, 248),
    9: (128, 116, 96),    # armour light
    10: (88, 80, 66),     # armour mid
    11: (40, 32, 28),     # boots
    12: (120, 80, 44),    # bronze straps
    13: (172, 146, 108),  # mask shadow
    14: (220, 204, 166),  # mask
    15: (240, 228, 196),  # mask light
}
REDS = (2, 4, 6, 12)
MASK = {2: 13, 12: 13, 6: 13, 4: 14, 8: 1, 5: 15, 7: 14}
BODY = {4: 12}


def build(src):
    im = Image.open(src); px = np.array(im).copy()
    pal = np.array(im.getpalette()[:48]).reshape(16, 3)
    for fi in range(px.shape[1] // 16):
        f = px[:, fi * 16:(fi + 1) * 16]
        rows = [y for y in range(32) if f[y].any()]; top = rows[0]
        hair = np.zeros_like(f, bool); hair[top:top + 4] = True          # antennae rows
        mask = np.zeros_like(f, bool)
        ye, xe = np.nonzero(f == 8)
        if len(ye):                                                       # a face is visible
            y0 = ye.min(); front = xe.min() >= 4
            x0, x1 = (3, 12) if front else (1, 6)
            mask[y0:y0 + 5, x0:x1 + 1] = True
        out = f.copy()
        for a, b in MASK.items(): out[mask & (f == a)] = b
        for a, b in BODY.items(): out[~mask & ~hair & (f == a)] = b
        px[:, fi * 16:(fi + 1) * 16] = out
    for i, c in PAL.items(): pal[i] = c
    o = Image.fromarray(px, 'P'); o.putpalette([int(v) for c in pal for v in c] + [0] * (768 - 48))
    return o


if __name__ == '__main__':
    build(sys.argv[1]).save(sys.argv[2], transparency=0)
