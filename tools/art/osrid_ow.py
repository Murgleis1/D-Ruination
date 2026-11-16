"""Osrid's overworld sprite from MonoMyth's Sunbeached Cliffs masked man (#156, user 2026-11-16).

Same shapes and animation; Osrid's identity by region + palette:
  * spikes / crown of the helmet -> his spiky red-orange hair (helmet ramp 1-4 keeps its indices,
    the palette entries become the hair ramp sampled from his portrait source)
  * the face (from the forehead mark down to the chin, inner columns) -> his cream mask:
    1/4/3 -> new mask ramp d/e/f, mouth skin -> mask, eye holes stay dark, the yellow forehead
    mark -> the black Eye glyph
  * light scarf 9/a/c -> his dark green scarf; olive cloak 5/7 -> dark armour leather
Run: python3 -I osrid_ow.py SRC_9FRAME.png OUT.png
"""
import sys
import numpy as np
from PIL import Image

PAL = {
    1: (148, 62, 23),   # hair mid            (was helmet mid)
    2: (40, 16, 12),    # outline             (was helmet dark / outline)
    3: (216, 112, 48),  # hair light
    4: (180, 82, 30),   # hair mid-light
    5: (39, 39, 38),    # armour dark
    7: (78, 70, 58),    # armour mid
    8: (16, 16, 16),    # (unused after remap)
    9: (24, 38, 28),    # scarf dark green
    10: (40, 62, 46),   # scarf mid
    12: (66, 94, 70),   # scarf light
    13: (172, 146, 108),  # mask shadow
    14: (220, 204, 166),  # mask
    15: (240, 228, 196),  # mask light
}
FACE = {1: 13, 4: 14, 3: 15, 0xB: 14, 8: 6}


def build(src):
    im = Image.open(src); px = np.array(im).copy()
    pal = np.array(im.getpalette()[:48]).reshape(16, 3)
    for fi in range(px.shape[1] // 16):
        f = px[:, fi * 16:(fi + 1) * 16]
        ym, xm = np.nonzero(f == 8); ys, xs = np.nonzero(f == 0xB)
        if len(ym) == 0: continue                      # back views: no face
        front = xm.min() >= 6                          # mark centred = facing the camera
        y0, y1 = ym.min(), ys.max()
        x0, x1 = (3, 12) if front else (1, 7)
        sub = f[y0:y1 + 1, x0:x1 + 1]
        out = sub.copy()
        for a, b in FACE.items(): out[sub == a] = b
        f[y0:y1 + 1, x0:x1 + 1] = out
    for i, c in PAL.items(): pal[i] = c
    o = Image.fromarray(px, 'P'); o.putpalette([int(v) for c in pal for v in c] + [0] * (768 - 48))
    return o


if __name__ == '__main__':
    build(sys.argv[1]).save(sys.argv[2], transparency=0)
