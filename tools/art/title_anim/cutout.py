"""Cut Chien-Pao out of the title as a sprite; fill the background behind it."""
from PIL import Image
import numpy as np
from collections import deque
im = Image.open('dr_title.png'); a = np.array(im); pal = np.array(im.getpalette()[:768]).reshape(256, 3)
H, W = a.shape
X0, X1, Y0, FEET = 58, 134, 78, 128          # search box; the ledge starts at row FEET
DARK = set(range(45, 66))
seed = (110, 105)                              # inside the body
m = np.zeros_like(a, bool); q = deque([seed])
while q:
    y, x = q.popleft()
    if not (Y0 <= y < FEET and X0 <= x < X1) or m[y, x] or a[y, x] not in DARK: continue
    m[y, x] = True; q.extend([(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)])
# the light rim on the right of the head and neck: light-blue pixels touching the silhouette's right edge
RIM = {16, 17, 18, 22, 25, 29}
rim = np.zeros_like(m)
for y in range(Y0, FEET):
    for x in range(X0, X1 - 1):
        if not m[y, x] and a[y, x] in RIM and m[y, x - 1] and x > 108: rim[y, x] = True
cp = m | rim
# whisker-blades (thin 44 / dark lines either side of the head) and the eye glints enclosed by the head
for (y, xa, xb) in ((91, 98, 103), (92, 98, 106), (90, 122, 129)):
    for x in range(xa, xb + 1):
        if a[y, x] in DARK or a[y, x] == 44: cp[y, x] = True
outside = np.zeros_like(cp); q = deque([(Y0, X0)])
while q:
    y, x = q.popleft()
    if not (Y0 <= y < FEET and X0 <= x < X1) or outside[y, x] or cp[y, x]: continue
    outside[y, x] = True; q.extend([(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)])
for y in range(Y0, FEET):
    for x in range(X0, X1):
        if not outside[y, x] and not cp[y, x] and 84 <= y <= 100 and 108 <= x <= 124: cp[y, x] = True   # eyes
ys, xs = np.nonzero(cp); print('Chien-Pao bbox x %d..%d  y %d..%d  pixels %d' % (xs.min(), xs.max(), ys.min(), ys.max(), cp.sum()))
np.save('mask_cp.npy', cp)
# background fill behind it: repeatedly take the most common non-creature neighbour (diffuses snow/rock in)
bg = a.copy(); hole = cp.copy()
for _ in range(60):
    if not hole.any(): break
    nh = hole.copy()
    for y, x in zip(*np.nonzero(hole)):
        nb = [bg[y + q, x + p] for q, p in ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1)) if 0 <= y + q < H and 0 <= x + p < W and not hole[y + q, x + p]]
        if len(nb) >= 2:
            vals, cnt = np.unique(nb, return_counts=True); bg[y, x] = vals[np.argmax(cnt)]; nh[y, x] = False
    hole = nh
np.save('bg_filled.npy', bg)
rgb = pal[a].astype(np.uint8); rgb2 = pal[bg].astype(np.uint8)
ov = rgb.copy(); ov[cp] = (ov[cp] * 0.3 + np.array([255, 60, 60]) * 0.7).astype(np.uint8)
o = Image.new('RGB', (3 * 80 * 6, 56 * 6))
for i, img in enumerate((rgb, ov, rgb2)):
    o.paste(Image.fromarray(img[78:134, 56:136]).resize((480, 336), Image.NEAREST), (i * 480, 0))
o.save('/tmp/cutout.png')
