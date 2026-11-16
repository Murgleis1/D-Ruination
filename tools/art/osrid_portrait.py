"""Osrid's portrait redone in MonoMyth's manner (user 2026-11-16, 14:12): "Osrid in general needs a
less AI looking portrait. I just wanted you to see Kakugo as a reference for positioning, shading,
colors". His own design (auburn spiky hair, white mask with the Horus eye, dark green scarf, dark
armour), rendered the way MonoMyth's busts are (Kakugo #69 as the reference):

  * MATERIALS: every pixel of his master is classed (mask / glyph / hair / scarf / armour / skin) by
    colour; each material gets a short FLAT ramp (MonoMyth uses 2-4 tones per material) and pixels
    are posterised into it by brightness -- the airbrushed gradients and per-pixel noise that read
    as "AI" become flat cel bands.
  * BANDS: a 3x3 majority filter inside each material removes stray specks so bands have clean
    shapes; the Horus glyph is kept pixel-exact (it is line art).
  * SCALE/FRAME: 2/3 dominant-colour reduction (portrait_rebuild) -> 64px bust, bottom-aligned,
    1px dark outline -- the same frame as the rest of the cast.
Run: python3 -I osrid_portrait.py OSRID_MASTER.png OUT.png [--preview sheet.png]
"""
import os, sys
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from portrait_rebuild import downscale_32, outline, despeckle, OUT

# flat ramps, darkest -> lightest (his colours; tone counts after MonoMyth's busts)
RAMPS = {
    'hair':   [(78, 28, 14), (128, 52, 22), (176, 78, 32), (214, 112, 52)],
    'mask':   [(170, 146, 108), (214, 198, 160), (238, 226, 192)],
    'scarf':  [(20, 36, 26), (36, 60, 44), (58, 88, 64)],
    'armour': [(40, 38, 40), (74, 68, 62)],
    'skin':   [(150, 92, 64), (206, 140, 104)],
    # the Horus glyph is drawn in the outline colour (index 1), 15 colours in all
}
OUTLINE = (12, 10, 10)


def classify(rgb):
    r, g, b = rgb[..., 0].astype(int), rgb[..., 1].astype(int), rgb[..., 2].astype(int)
    lum = (r + g + b) / 3; sat = np.max(rgb, -1).astype(int) - np.min(rgb, -1)
    cls = np.full(rgb.shape[:2], 'armour', object)
    cls[(lum < 34)] = 'glyph'
    cls[(lum >= 130) & (sat < 90) & (r >= b)] = 'mask'
    cls[(r > g + 25) & (r > b + 40) & (lum >= 34) & (lum < 150)] = 'hair'
    cls[(g > r + 6) & (lum >= 20) & (lum < 110)] = 'scarf'
    cls[(r > 140) & (g > 80) & (g < 160) & (b < 130) & (r - b > 50) & (lum >= 100)] = 'skin'
    return cls, lum


def posterise(rgb, mask):
    cls, lum = classify(rgb)
    names = list(RAMPS)
    pal = [OUTLINE] + [c for n in names for c in RAMPS[n]]
    base = {n: 1 + sum(len(RAMPS[m]) for m in names[:names.index(n)]) for n in names}
    idx = np.full(mask.shape, -1, np.int16)
    idx[mask & (cls == 'glyph')] = 0                          # glyph -> outline colour
    for n in names:
        sel = mask & (cls == n)
        if not sel.any(): continue
        ramp = RAMPS[n]
        if len(ramp) == 1: idx[sel] = base[n]; continue
        q = np.quantile(lum[sel], np.linspace(0, 1, len(ramp) + 1)[1:-1])   # equal-area tone bands
        t = np.searchsorted(q, lum[sel])
        idx[sel] = base[n] + t
    return idx, np.array(pal, int), cls


def majority(idx, cls, keep=('glyph',)):
    out = idx.copy(); H, W = idx.shape
    for y in range(1, H - 1):
        for x in range(1, W - 1):
            if idx[y, x] < 0 or cls[y, x] in keep: continue
            win = idx[y - 1:y + 2, x - 1:x + 2].ravel()
            win = win[(win >= 0)]
            vals, cnt = np.unique(win, return_counts=True)
            if cnt.max() >= 5 and vals[np.argmax(cnt)] != idx[y, x]: out[y, x] = vals[np.argmax(cnt)]
    return out


def build(path):
    rgba = np.array(Image.open(path).convert('RGBA'))
    mask = rgba[..., 3] >= 96
    idx, pal, cls = posterise(rgba[..., :3], mask)
    idx = majority(majority(idx, cls), cls)
    small = downscale_32(idx, pal)
    big = np.full((OUT, OUT), -1, np.int16)
    h, w = small.shape; y0 = OUT - h; x0 = (OUT - w) // 2
    big[y0:y0 + h, x0:x0 + w] = small
    big = despeckle(outline(big, pal))
    canvas = np.where(big >= 0, big + 1, 0).astype(np.uint8)
    full = np.zeros((16, 3), int); full[0] = (255, 0, 255); full[1:1 + len(pal)] = pal
    assert len(pal) <= 15
    return canvas, full.astype(np.uint8)


if __name__ == '__main__':
    from portrait_adapt import save
    idx, pal = build(sys.argv[1]); save(idx, pal, sys.argv[2])
