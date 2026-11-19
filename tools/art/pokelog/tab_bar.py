"""PokéLog info-page tab bar: parchment strip with blackletter labels (user 2026-11-18).
render_bar(selected) -> 240x16 array of palette-0 indices. Uses only indices 10-14 of the PokéLog's BG
palette 0, which nothing else on those screens uses (checked: tilesets, page tilemaps, text colours)."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, '..', 'trainer_card', 'fonts', 'JacquardaBastarda9-Regular.ttf')
INK, ACCENT, PARCH, PARCH_D, RULE = 10, 11, 12, 13, 14
COLOURS = {INK: (64, 40, 24), ACCENT: (152, 40, 32), PARCH: (224, 200, 152), PARCH_D: (192, 160, 112), RULE: (104, 72, 40)}
LABELS = ['Info', 'Area', 'Stats', 'Evo', 'Cry', 'Size']
X0, X1 = 14, 226                       # labels sit between the two arrows

def _glyphs(text):
    f = ImageFont.truetype(FONT, 13)
    l, t, r, b = f.getbbox(text)
    im = Image.new('L', (r - l + 2, 16), 0)
    ImageDraw.Draw(im).text((-l + 1, 0), text, font=f, fill=255)
    a = np.asarray(im) > 127
    cols = np.where(a.any(0))[0]
    return a[:, cols.min():cols.max() + 1]

def render_bar(selected):
    bar = np.full((16, 240), PARCH, np.uint8)
    yy, xx = np.mgrid[0:16, 0:240]
    bar[((xx * 3 + yy * 5) % 23 == 0) & (yy > 1) & (yy < 14)] = PARCH_D       # faint paper grain
    bar[0, :] = RULE; bar[15, :] = RULE; bar[1, :] = PARCH_D; bar[14, :] = PARCH_D
    for tip, d in ((4, 1), (235, -1)):                                         # arrows point outward
        for k in range(4):
            bar[8 - k - 1:8 + k, tip + d * k] = INK
    widths = [_glyphs(t).shape[1] for t in LABELS]
    gap = (X1 - X0 - sum(widths)) / (len(LABELS) + 1)
    x = X0 + gap
    for i, (t, w) in enumerate(zip(LABELS, widths)):
        g = _glyphs(t); xi = int(round(x))
        region = bar[0:16, xi:xi + w]
        halo = np.zeros_like(g); halo[:, 1:] |= g[:, :-1]; halo[:, :-1] |= g[:, 1:]; halo[1:] |= g[:-1]; halo[:-1] |= g[1:]
        region[halo & (region == PARCH_D)] = PARCH                               # clear grain around letters
        region[g] = ACCENT if i == selected else INK
        if i == selected:                                                       # underline flourish
            bar[14, xi - 1:xi + w + 1] = ACCENT
        x += w + gap
    return bar

def to_rgb(a):
    lut = np.zeros((16, 3), np.uint8)
    for k, v in COLOURS.items(): lut[k] = v
    return lut[a]

if __name__ == '__main__':
    rows = [to_rgb(render_bar(i)) for i in range(6)]
    Image.fromarray(np.concatenate(rows, 0)).resize((960, 384), Image.NEAREST).save('/tmp/tabbar_mock.png')
