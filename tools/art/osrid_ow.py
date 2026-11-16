"""Osrid's overworld sprite designed on KAKUGO's (MonoMyth, Sunbleached Cliffs; graphics id 0xCD,
assets/monomyth_ow/mm_ow_kakugo.png) -- user 2026-11-16: "Kakugo's sprite is meant to be the new
base for Osrid ... design a new overworld sprite for Osrid using Kakugo's as the base".
(Drafts 1-2 on #156 / #136 were the wrong character and are superseded.)

Kakugo's shapes, proportions and animation; Osrid's identity:
  * spiked helmet (brown ramp 1-4)       -> his spiky red-orange hair
  * visor band + ruby goggles (the face) -> his cream mask; the ruby eyes -> the black eye glyph
  * light scarf d/e                      -> his dark green scarf
  * dark coat 9/a/b/c, gold trim 7       -> kept (dark armour, the gold buttons)
Face region per frame: from 3 rows above the eye row to 1 below, inner columns (front) or the
leading side (profile); back views have no face.
Run: python3 -I osrid_ow.py KAKUGO_SHEET.png OUT.png
"""
import sys
import numpy as np
from PIL import Image

PAL = {
    1: (124, 44, 22),     # hair mid-dark      (helmet 104,64,40)
    2: (204, 92, 38),     # hair mid           (helmet 160,120,72)
    3: (160, 62, 28),     # hair dark-mid      (helmet 120,80,48)
    4: (92, 28, 16),      # hair darkest       (helmet 80,40,32)
    6: (240, 228, 196),   # mask light         (was gold highlight)
    8: (172, 146, 108),   # mask shadow        (was ruby eyes)
    13: (46, 70, 52),     # scarf dark green   (was 176,160,168)
    14: (72, 106, 76),    # scarf green        (was 216,216,216)
    15: (222, 206, 168),  # mask
}
FACE = {5: 15, 3: 8, 4: 8, 1: 8, 2: 15, 6: 6, 7: 6, 8: 5}     # ruby eyes -> black glyph (5)
HAIR_OUTSIDE = {6: 2}                                         # gold highlight on the helmet -> hair


def build(src):
    im = Image.open(src); px = np.array(im).copy()
    pal = np.array(im.getpalette()[:48]).reshape(16, 3)
    nf = px.shape[1] // 16
    for fi in range(nf):
        f = px[:, fi * 16:(fi + 1) * 16]
        face = np.zeros_like(f, bool)
        ye, xe = np.nonzero(f == 8)
        if len(ye):
            y = ye.min(); front = xe.min() >= 4 and xe.max() <= 11 and len(set(xe)) >= 3
            x0, x1 = (4, 11) if front else ((1, 7) if xe.mean() < 8 else (8, 14))
            face[max(y - 3, 0):y + 2, x0:x1 + 1] = True
        out = f.copy()
        for a, b in FACE.items(): out[face & (f == a)] = b
        for a, b in HAIR_OUTSIDE.items(): out[~face & (f == a) & (np.arange(32)[:, None] < 22)] = b
        px[:, fi * 16:(fi + 1) * 16] = out
    for i, c in PAL.items(): pal[i] = c
    o = Image.fromarray(px, 'P'); o.putpalette([int(v) for c in pal for v in c] + [0] * (768 - 48))
    return o


if __name__ == '__main__':
    build(sys.argv[1]).save(sys.argv[2], transparency=0)
