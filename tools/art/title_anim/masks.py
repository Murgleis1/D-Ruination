"""Masks for the animated title: SKY (moves) = rows 0..SKY_ROWS-1 minus the cliff and the logo."""
from PIL import Image
import numpy as np
SKY_ROWS = 43
im = Image.open('dr_title.png'); a = np.array(im)
H, W = a.shape
# cliff right edge per row (hand-traced from the 12x zoom)
CLIFF = {}
for y in range(SKY_ROWS):
    CLIFF[y] = 9 if y < 5 else 12 if y < 10 else 15 if y < 15 else 19 if y < 21 else 20 if y < 23 else 22 if y < 25 else 34 if y < 35 else 37 if y < 38 else 40
TUFT = (21, 36, 20, 42)                  # rows y0..y1, cols x0..x1 where grass tufts poke into the sky
blue = set(a[22:43, 45:62].ravel())      # the sky's light blues
cliff = np.zeros_like(a, bool)
for y in range(SKY_ROWS):
    cliff[y, :CLIFF[y]] = True
    if TUFT[0] <= y <= TUFT[1]:
        for x in range(CLIFF[y], TUFT[3]):
            if a[y, x] not in blue: cliff[y, x] = True
# logo: white fill + near-black outline inside its box (and anything they enclose)
LX0, LX1 = 62, 179
logo = np.zeros_like(a, bool)
for y in range(SKY_ROWS):
    for x in range(LX0, LX1):
        if a[y, x] in (0, 64, 65, 63): logo[y, x] = True
from collections import deque
outside = np.zeros_like(a, bool); q = deque([(y, x) for y in range(SKY_ROWS) for x in (LX0, LX1 - 1)] + [(0, x) for x in range(LX0, LX1)])
while q:
    y, x = q.popleft()
    if not (0 <= y < SKY_ROWS and LX0 <= x < LX1) or outside[y, x] or logo[y, x]: continue
    outside[y, x] = True; q.extend([(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)])
for y in range(SKY_ROWS):
    for x in range(LX0, LX1):
        if not outside[y, x] and not logo[y, x] and y < SKY_ROWS - 1: logo[y, x] = True   # enclosed (counters)
sky = np.zeros_like(a, bool); sky[:SKY_ROWS] = True; sky &= ~cliff & ~logo
np.save('mask_sky.npy', sky); np.save('mask_logo.npy', logo); np.save('mask_cliff.npy', cliff)
rgb = np.array(im.convert('RGB')); ov = rgb.copy()
ov[sky] = (ov[sky] * 0.35 + np.array([255, 0, 0]) * 0.65).astype(np.uint8)
ov[logo] = (ov[logo] * 0.5 + np.array([0, 255, 0]) * 0.5).astype(np.uint8)
Image.fromarray(ov[:60]).resize((960, 240), Image.NEAREST).save('/tmp/masks.png')
print('sky px', sky.sum(), 'logo px', logo.sum(), 'cliff px', cliff.sum())
