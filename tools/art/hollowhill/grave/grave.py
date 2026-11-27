"""Alphonse's grave (Hollow Hill's southwest woods; user 2026-11-27): a 16x32 object, since Hollow Hill's tiles are
full. Drawn here in Hollow Hill's own stone and soil colours: a weathered headstone (bone-lit left edge, charcoal face,
an engraved cross, a crack, a drip of the hill's blood-red) over a grave dug open from below (Helga's rite woke him).
Run: python3 grave.py [--write]  (preview /tmp/r11/grave_preview.png)"""
import sys, os
import numpy as np
from PIL import Image
PAL = [(0, 0, 0), (24, 24, 32), (56, 48, 64), (88, 80, 96), (120, 112, 120), (176, 168, 144), (216, 208, 192),
       (104, 16, 24), (80, 72, 72), (104, 96, 88), (144, 136, 120), (16, 12, 16)] + [(0, 0, 0)] * 4
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'codebase', 'graphics',
                   'object_events', 'pics', 'misc', 'dr_grave.png')
a = np.zeros((32, 16), np.uint8)
# headstone: x 3-12, y 2-16, top rounded
for y in range(2, 17):
    for x in range(3, 13):
        r = 3 - min(y - 2, 3)                      # round the top corners
        if (x < 3 + r or x > 12 - r) and y < 5: continue
        a[y, x] = 3
for y in range(2, 17):                           # outline, then light left edge, dark right edge
    xs = [x for x in range(16) if a[y, x]]
    if not xs: continue
    a[y, xs[0]] = 1; a[y, xs[-1]] = 1
    if len(xs) > 3: a[y, xs[0] + 1] = 5; a[y, xs[-1] - 1] = 2
for x in range(16):
    ys = [y for y in range(32) if a[y, x]]
    if ys: a[ys[0], x] = 1
a[3, 6:10] = 6; a[4, 5] = 6                       # lit crown
for y in range(6, 13): a[y, 7] = 1                  # engraved cross, its lower lip catching the light
for y in range(7, 13): a[y, 8] = 4
a[8, 5:10] = 1; a[9, 5:7] = 4; a[9, 8:10] = 4
for y, x in ((3, 10), (4, 10), (5, 9), (6, 10), (7, 10), (11, 5), (12, 5)): a[y, x] = 1      # cracks
for y, x in ((3, 6), (4, 6), (5, 6), (6, 5)): a[y, x] = 7                                    # a drip of the hill's red
a[15:18, 2:14] = 2; a[15, 3:13] = 4; a[17, 2:14] = 1; a[15:18, 2] = 1; a[15:18, 13] = 1      # plinth
# the grave dug open from below: a long pit at the stone's foot, the soil thrown up in heaps either side
for y in range(18, 31):
    for x in range(4, 12):
        a[y, x] = 11
a[18, 4:12] = 8; a[19, 4:12] = 8                                                           # the pit's far wall
for y in range(18, 31): a[y, 4] = 8; a[y, 11] = 8
a[30, 4:12] = 10
heaps = {1: (20, 29), 2: (19, 30), 3: (18, 31), 12: (18, 31), 13: (19, 30), 14: (21, 28)}
for x, (y0, y1) in heaps.items():
    for y in range(y0, y1): a[y, x] = 9
    a[y0, x] = 10; a[y1 - 1, x] = 8
for y, x in ((22, 2), (25, 3), (27, 1), (23, 13), (26, 12), (20, 14)): a[y, x] = 10           # clods
for y, x in ((24, 1), (28, 3), (21, 12), (27, 14)): a[y, x] = 8
if '--write' in sys.argv:
    im = Image.fromarray(a, 'P'); im.putpalette([v for c in PAL for v in c] + [0] * (768 - 48)); im.save(OUT, transparency=0)
    with open(OUT[:-4] + '.pal', 'w', newline='\r\n') as f:
        f.write('JASC-PAL\n0100\n16\n' + ''.join('%d %d %d\n' % c for c in PAL))
rgb = np.array(PAL, np.uint8)[a]; bg = np.zeros((48, 48, 3), np.uint8); bg[:] = (120, 112, 96)
m = a > 0; tile = bg.copy(); tile[8:40, 16:32][m] = rgb[m]
Image.fromarray(tile).resize((48 * 8, 48 * 8), Image.NEAREST).save('/tmp/r11/grave_preview.png')
