"""The Templars in the Order's blue (user 2026-11-25: "The templar's should move to the order's blue for sure").
The blue is the cathedral nave's runner ramp (tools/art/templar_hq/nave/nave_mock.py). Only the robe's slots change,
each matched by brightness onto the ramp (so the shading keeps its depth); skin, the leather belt and the legs stay.
Mock: python3 templar_blue.py  -> out/templar_front.png, out/templar_ow.png, /tmp/cult/templar_blue.png.
Install (after approval): python3 templar_blue.py --install  (originals kept in src/)."""
import os, sys, shutil
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
CB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'codebase'))
NAVE = [(150, 166, 220), (96, 112, 190), (62, 74, 163), (51, 60, 128), (34, 40, 89), (22, 24, 50)]
ASSETS = {'front': ('graphics/trainers/front_pics/templar.png', [3, 4, 6, 7, 8, 9, 10, 11, 12, 14, 15]),
          'ow': ('graphics/object_events/pics/people/templar.png', [2, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15])}


def lum(c):
    return 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]


def on_ramp(L, ramp=NAVE):
    """The colour on the ramp with brightness L (linear between its steps)."""
    pts = sorted(((lum(c), c) for c in ramp))
    if L <= pts[0][0]:
        return pts[0][1]
    for (l0, c0), (l1, c1) in zip(pts, pts[1:]):
        if L <= l1:
            t = (L - l0) / (l1 - l0)
            return tuple(round(a + (b - a) * t) for a, b in zip(c0, c1))
    return pts[-1][1]


def recolour(rel, robe):
    src = os.path.join(HERE, 'src', os.path.basename(os.path.dirname(rel)) + '__' + os.path.basename(rel))
    if not os.path.exists(src):
        os.makedirs(os.path.dirname(src), exist_ok=True)
        shutil.copy(os.path.join(CB, rel), src)               # the original, kept
    im = Image.open(src)
    pal = [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]
    new = list(pal)
    for k in robe:
        new[k] = on_ramp(lum(pal[k]))
    out = im.copy()
    if rel.endswith('front_pics/templar.png'):
        a = np.array(im).copy()
        # 13, a dark brown in the robe's creases, joins the robe; 5 keeps shading his hands but its other pixels (the
        # cord at his waist, creases on chest and sleeves) become the Order's gold, in slot 4: robe slots 3 and 4 land
        # on the same blue, so 4's pixels move to 3
        new[13] = on_ramp(lum(pal[13]))
        a[a == 4] = 3
        new[4] = (216, 180, 84)
        skin = np.isin(a, (1, 2))
        near = np.zeros_like(skin)
        near[1:] |= skin[:-1]; near[:-1] |= skin[1:]; near[:, 1:] |= skin[:, :-1]; near[:, :-1] |= skin[:, 1:]
        a[(a == 5) & ~near] = 4
        out = Image.fromarray(a, 'P')
    out.putpalette([v for c in new for v in c] + [0] * (768 - 48))
    return im, out


def rgb(im, s):
    a = np.array(im); p = np.array(im.getpalette()[:48]).reshape(16, 3)
    o = p[a].astype(np.uint8); o[a == 0] = (110, 110, 125)
    return Image.fromarray(o).resize((im.width * s, im.height * s), Image.NEAREST)


if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    tiles = []
    for name, (rel, robe) in ASSETS.items():
        before, after = recolour(rel, robe)
        after.save(os.path.join(HERE, 'out', 'templar_%s.png' % name), transparency=0)
        if '--install' in sys.argv:
            after.save(os.path.join(CB, rel))
        s = 4 if name == 'front' else 4
        tiles.append((rgb(before, s), rgb(after, s), name))
    W = max(b.width + a.width + 30 for b, a, _ in tiles)
    H = sum(b.height + 24 for b, a, _ in tiles) + 30
    c = Image.new('RGB', (W, H), (36, 36, 44)); d = ImageDraw.Draw(c)
    d.text((8, 8), 'Templar in the Order\'s blue (the nave runner\'s ramp): before | after', fill=(240, 220, 120))
    y = 30
    for b, a, n in tiles:
        c.paste(b, (8, y)); c.paste(a, (8 + b.width + 14, y)); d.text((8, y + b.height + 2), n, fill=(230, 230, 230))
        y += b.height + 24
    c.save('/tmp/cult/templar_blue.png'); print(c.size)
