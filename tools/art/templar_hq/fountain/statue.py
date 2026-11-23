"""The Citadel's fountain statues (user 2026-11-22): Arceus's overworld sprite (the expansion's follower sprite, its
side-facing frame) as worn stone on a plinth; facing left, and mirrored to face right."""
import numpy as np
from PIL import Image
from scipy.ndimage import binary_erosion
SRC = '/home/claude/repo/codebase/graphics/pokemon/arceus/overworld.png'
im = Image.open(SRC); idx = np.array(im); p = im.getpalette(); p = (p + [0] * 48)[:48]; pal = np.array(p).reshape(16, 3)
fr = idx[:, 4 * 64:5 * 64]                                   # (frame 4: side, facing left)
mask = fr != 0
ys, xs = np.nonzero(mask); fr = fr[ys.min():ys.max() + 1, xs.min():xs.max() + 1]; mask = fr != 0
# stone, by palette colour: each of the sprite's colours keeps its place in the order of lightness (the outline the
# darkest), so the figure keeps its own shading; a cool grey ramp
STONE = np.array([(28, 28, 34), (52, 52, 60), (72, 72, 80), (92, 92, 98), (112, 111, 114), (132, 130, 130),
                  (150, 148, 146), (168, 166, 160)], float)              # (weathered: mid greys, no white)
used = sorted({int(v) for v in np.unique(fr) if v}, key=lambda i: .30 * pal[i][0] + .59 * pal[i][1] + .11 * pal[i][2])
ls = [.30 * pal[i][0] + .59 * pal[i][1] + .11 * pal[i][2] for i in used]
lo, hi = ls[1] if len(ls) > 2 else ls[0], ls[-1]
step = {}
for i, l in zip(used, ls):
    step[i] = 0 if l == ls[0] else int(np.clip(round(1 + (l - lo) / (hi - lo) * (len(STONE) - 2)), 1, len(STONE) - 1))
q = np.vectorize(lambda v: step.get(int(v), 0))(fr)
out = np.zeros(fr.shape + (4,), np.uint8)
o = STONE[q].copy()
rng = np.random.default_rng(11)
# worn, lightly: grime in some of the shadows (a step darker), a little pitting on the lit stone, two hairline cracks
for y, x in zip(*np.nonzero(mask)):
    if q[y, x] == 0: continue
    r = rng.random()
    if 1 <= q[y, x] <= 3 and r < 0.12: o[y, x] = STONE[q[y, x] - 1] * np.array([0.97, 1.0, 0.95])
    elif q[y, x] >= 5 and r < 0.06: o[y, x] = STONE[q[y, x] - 2]
out[mask, :3] = np.clip(o[mask], 0, 255).astype(np.uint8); out[mask, 3] = 255
inner = binary_erosion(mask, iterations=2)
for (y0, x0, n) in ((15, 17, 3), (9, 27, 2)):
    for i in range(n):
        y, x = y0 + i, x0 + (i // 2)
        if 0 <= y < mask.shape[0] and 0 <= x < mask.shape[1] and inner[y, x]: out[y, x, :3] = STONE[1]
fig = Image.fromarray(out)
# the plinth: a block of the same stone, worn at its corners
w = max(fig.size[0] + 4, 36); can = Image.new('RGBA', (w, fig.size[1] + 10), (0, 0, 0, 0))
from PIL import ImageDraw
d = ImageDraw.Draw(can); H = can.size[1]
S = [tuple(int(v) for v in c) + (255,) for c in STONE]
d.rectangle((1, H - 11, w - 2, H - 1), fill=S[0]); d.rectangle((2, H - 10, w - 3, H - 2), fill=S[3])
d.rectangle((2, H - 10, w - 3, H - 9), fill=S[5]); d.rectangle((2, H - 3, w - 3, H - 2), fill=S[2])
for (x, y) in ((2, H - 10), (w - 3, H - 10), (5, H - 6), (w - 9, H - 4)): can.putpixel((x, y), S[1])
can.alpha_composite(fig, ((w - fig.size[0]) // 2, 0))
can.save('statue_left.png'); can.transpose(Image.FLIP_LEFT_RIGHT).save('statue_right.png')
print('statue', can.size)
