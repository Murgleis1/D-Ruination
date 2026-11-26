"""The male Templar (user 2026-11-25: "Here is the male variant one that should be recolored blue properly"; the
existing Templar, now in the Order's blue, is the female). Sources: the user's trainer322 (front) and trchar322
(Essentials 4x4 overworld, 16x32 frames: our cast's size), halved from 2x.
The Order's blue is the cathedral nave runner's ramp (as the female Templar); gold is the Order's gold.
  coat and trousers (the dark greys)        -> the Order's navy, matched by brightness
  the round shield (its browns)             -> the face Order blue, the spokes and boss gold
  the staff, its flame, hair, skin          -> as drawn
Front: fitted to 64x64 (nearest), 15 colours. Overworld: Emerald's 9 frames.
Run: python3 male.py  -> out/templar_male_front.png, out/templar_male_ow.png, /tmp/cult/templar_male.png"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'sword_cult'))
from templar_blue import on_ramp, lum, NAVE      # noqa: E402
from sword_cult import fit64_phased as fit64, ow9   # noqa: E402

GOLD = [(240, 212, 120), (216, 180, 84), (168, 128, 48)]
CLOTH = [(123, 114, 104), (106, 98, 98), (74, 74, 82), (64, 61, 57), (41, 41, 49)]
SHIELD_F = {(148, 85, 61): NAVE[2], (110, 60, 41): GOLD[2]}        # face; (105, 59, 42) spokes -> gold
SHIELD_SPOKE = (105, 59, 42)


def recolour_front(a):
    a = a.copy()
    h, w = a.shape[:2]
    for y in range(h):
        for x in range(w):
            if not a[y, x, 3]:
                continue
            c = tuple(int(v) for v in a[y, x, :3])
            in_shield = 36 <= x <= 61 and 25 <= y <= 55
            if in_shield and c == (148, 85, 61):
                a[y, x, :3] = NAVE[2]
            elif in_shield and c in (SHIELD_SPOKE, (110, 60, 41)):
                a[y, x, :3] = GOLD[1]
            elif in_shield and c == (191, 135, 100):
                a[y, x, :3] = GOLD[0]
            elif y > 22 and c in CLOTH:
                a[y, x, :3] = on_ramp(lum(c) * 0.9)
    return a


def recolour_ow(a):
    """Per 16x32 frame: below the head (frame row 17 on), the shield's browns -> Order blue and gold; the dark greys
    of his clothes -> navy; the staff (its own darker browns) and the head as drawn."""
    a = a.copy()
    H, W = a.shape[:2]
    for y in range(H):
        fy = y % 32
        for x in range(W):
            if not a[y, x, 3]:
                continue
            c = tuple(int(v) for v in a[y, x, :3])
            if fy >= 17 and c == (148, 85, 61):
                a[y, x, :3] = NAVE[2]
            elif fy >= 17 and c == (191, 135, 100):
                a[y, x, :3] = GOLD[1]
            elif fy >= 15 and c in ((64, 61, 57), (78, 66, 51), (75, 53, 40)):
                a[y, x, :3] = on_ramp(lum(c) * 0.9)
            elif fy >= 15 and c == (123, 114, 104):
                a[y, x, :3] = NAVE[1]
    return a


def quant15(a):
    """At most 15 colours: merge the closest pair (weighted by the smaller count) until 15 remain."""
    a = a.copy()
    while True:
        m = a[..., 3] > 0
        cols, counts = np.unique(a[m][:, :3], axis=0, return_counts=True)
        if len(cols) <= 15:
            return a
        best = None
        for i in range(len(cols)):
            for j in range(len(cols)):
                if i == j:
                    continue
                d = float(((cols[i].astype(int) - cols[j].astype(int)) ** 2).sum()) ** 0.5
                cost = d * min(counts[i], counts[j]) ** 0.5
                if best is None or cost < best[0]:
                    best = (cost, i, j)
        _, i, j = best
        src, dst = (i, j) if counts[i] < counts[j] else (j, i)
        sel = m & (a[..., :3] == cols[src]).all(-1)
        a[sel, :3] = cols[dst]


if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    f = np.array(Image.open(os.path.join(HERE, 'src_front.png')).convert('RGBA'))
    o = np.array(Image.open(os.path.join(HERE, 'src_ow.png')).convert('RGBA'))
    f2 = quant15(fit64(recolour_front(f)))
    o2 = ow9(recolour_ow(o), 16, 32)
    Image.fromarray(f2).save(os.path.join(HERE, 'out', 'templar_male_front.png'))
    Image.fromarray(o2).save(os.path.join(HERE, 'out', 'templar_male_ow.png'))
    fem_f = Image.open(os.path.join(HERE, '..', 'out', 'templar_front.png')).convert('RGBA')
    fem_o = Image.open(os.path.join(HERE, '..', 'out', 'templar_ow.png')).convert('RGBA')

    def tile(im, s):
        im = im if isinstance(im, Image.Image) else Image.fromarray(im)
        c = Image.new('RGBA', im.size, (110, 110, 125, 255)); c.alpha_composite(im.convert('RGBA'))
        return c.resize((im.width * s, im.height * s), Image.NEAREST)
    T = [(tile(f, 3), 'yours'), (tile(f2, 4), 'male, front 64'), (tile(fem_f, 4), 'female (approved)')]
    R = [(tile(o2, 4), 'male overworld: S N W, walk S, walk N, walk W'), (tile(fem_o, 4), 'female overworld')]
    W = max(sum(t.width + 16 for t, _ in T), max(t.width for t, _ in R)) + 16
    H = max(t.height for t, _ in T) + sum(t.height + 24 for t, _ in R) + 70
    c = Image.new('RGB', (W, H), (36, 36, 44)); d = ImageDraw.Draw(c)
    d.text((8, 8), 'Templar, male: the Order\'s blue (coat, trousers, shield face) and gold (shield spokes)', fill=(240, 220, 120))
    x, y = 8, 30
    for t, l in T:
        c.paste(t, (x, y)); d.text((x, y + t.height + 2), l, fill=(230, 230, 230)); x += t.width + 16
    y += max(t.height for t, _ in T) + 22
    for t, l in R:
        c.paste(t, (8, y)); d.text((8, y + t.height + 2), l, fill=(230, 230, 230)); y += t.height + 24
    c.save('/tmp/cult/templar_male.png'); print(c.size)
