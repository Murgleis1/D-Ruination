"""The Umbra deep cavern's surface entrance (author, 2026-11-16): a sealed cave mouth in the lower
cliff at the far west end of Pelluca's beach. Reachable on foot, Umbra-sealed until Trial 4.

Drawn INTO the Wood Avens cliff band (10 over 11, two cells wide) using only that band's own
colours, so it adds no palette: an arched opening with a light stone rim, filled by a grey stone
slab with a centre seam and two pale studs (sealed).

cave_mouth(top_img, bottom_img) -> 32x32 RGB: top_img/bottom_img are the flattened 16x16 band
pieces (lip row, face row on sand); the result is cut into 2x2 cells by the builder.
"""
import numpy as np

RIM = (144, 144, 152)
RIM_DARK = (88, 88, 96)
HOLLOW = (48, 48, 56)
SLAB = (120, 120, 128)
SEAM = (48, 56, 80)
STUD = (176, 176, 144)


def cave_mouth(top_img, bottom_img):
    a = np.zeros((32, 32, 3), int)
    a[0:16, 0:16] = top_img; a[0:16, 16:32] = top_img
    a[16:32, 0:16] = bottom_img; a[16:32, 16:32] = bottom_img
    cx, top, half = 15.5, 9, 11                 # arch: centre column, crown row, half-width
    for y in range(top, 32):
        for x in range(32):
            dx = abs(x - cx)
            r = half if y >= top + half else np.sqrt(max(0, half ** 2 - (top + half - y) ** 2))
            if dx <= r:
                edge = dx > r - 1.6 or y < top + 1.5
                a[y, x] = RIM if edge and y < top + half else (RIM_DARK if edge else HOLLOW)
    for y in range(top + 4, 32):                # the seal: a stone slab inside the arch
        for x in range(32):
            dx = abs(x - cx)
            r = half - 2.5 if y >= top + half else np.sqrt(max(0, (half - 2.5) ** 2 - (top + half - y) ** 2))
            if dx <= r:
                a[y, x] = SLAB
    a[top + 6:32, 15:17] = SEAM                 # centre seam of the slab
    for sx, sy in ((11, 22), (20, 22)):
        a[sy:sy + 2, sx:sx + 2] = STUD          # two studs
    return a
