"""Pelluca's central monument: the wellspring fountain (user, 2026-11-15).

Chamomile Town's paved garden ring (MonoMyth), enlarged to fill the plaza, with the
Watercress Port statue fountain (MonoMyth) at its centre, recoloured so it is not
MonoMyth's: sandstone statue (the ring's brick shades) in a basin of the ring's rim stone --
one colour family, so the monument fits the palette budget.

  ring      Chamomile x26-39 y26-32 (14x7). Stretched to 16 wide by repeating the plain
            band column x30; to 9 tall by repeating the W/E entrance-arm row (y29) above
            and below it with the diamond swapped for plain brick.
  interior  cleared (Chamomile's own flowers/fountain/sign) -> Pelluca grass shows through.
  fountain  Watercress x23-29 y12-15 (7x4), background paving/hedge cut away.

monument() -> (img, blocked): img is (9*16, 16*16, 3) RGB with -1 = transparent (the
builder puts Wood Avens grass under it); blocked is a 9x16 cell mask (fountain basin).
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_cormoria as b

CH, WC = 0x8694D8, 0x869C10
RING_BOX = (26, 26, 39, 32)
FOUNTAIN_BOX = (23, 12, 28, 15)
W_CELLS, H_CELLS = 16, 9

# bronze statue + Pelluca stone (mauve-tinted greys) -- luminance ramps, dark -> light
BRONZE = [(72, 48, 32), (112, 72, 40), (152, 104, 56), (192, 144, 80), (224, 184, 120)]
STONE = [(80, 72, 96), (112, 104, 128), (144, 136, 160), (184, 176, 200), (224, 216, 232)]


def _colours(img, cells):
    s = set()
    for cx, cy in cells:
        c = img[cy * 16:cy * 16 + 16, cx * 16:cx * 16 + 16].reshape(-1, 3)
        s |= {tuple(v) for v in c if v[0] >= 0}
    return s


def _cut(img, colours):
    out = img.copy()
    if not colours: return out
    arr = np.array(sorted(colours))
    m = (out[..., None, :] == arr).all(-1).any(-1)
    out[m] = -1
    return out


def _ramp(img, mask, ramp):
    out = img.copy()
    lum = img[..., :3].sum(-1) / 3.0
    sel = mask & (img >= 0).all(-1)
    if not sel.any(): return out
    lo, hi = lum[sel].min(), lum[sel].max()
    k = np.clip(((lum - lo) / max(1, hi - lo) * (len(ramp) - 1)).round().astype(int), 0, len(ramp) - 1)
    for i, c in enumerate(ramp):
        out[sel & (k == i)] = c
    return out


def _cut_bg(img, pink=False, dark_rows=0):
    """Background by colour KIND (sampling colours also caught rim/basin stone)."""
    out = img.copy(); rgb = out.astype(int)
    r, g, bl = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    lum = rgb.sum(-1) / 3.0
    m = (g > r + 15) & (g > bl + 5)                            # grass / green paving / foliage
    if pink:
        m |= (r > bl + 15) & (r > g + 15) & (lum > 140)        # pink paving
    if dark_rows:
        d = np.zeros_like(m); d[:dark_rows] = lum[:dark_rows] < 110
        m |= d                                                 # hedge wall behind the basin
    out[m & (out >= 0).all(-1)] = -1
    return out


def ring():
    _, comp = b.region_layers(CH, RING_BOX)
    x0, y0 = RING_BOX[:2]
    r = _cut_bg(comp)
    r[(28 - y0) * 16:(31 - y0) * 16, (29 - x0) * 16:(37 - x0) * 16] = -1   # interior cleared
    cell = lambda cx, cy: r[(cy - y0) * 16:(cy - y0) * 16 + 16, (cx - x0) * 16:(cx - x0) * 16 + 16]
    # plain arm cell: the diamond cell with the diamond replaced by the same brick rows from the
    # cell to its right (inner rim starts at x=10 there, so shift by one brick (8px) beyond that)
    brick = cell(28, 29)
    plain = cell(27, 29).copy()
    for x in range(1, 16):
        sx = x if x < 8 else x - 8
        plain[:, x] = brick[:, sx]
    mirror = lambda c: c[:, ::-1].copy()
    rows = []
    for cy in range(y0, y0 + 7):
        left = [cell(cx, cy) for cx in range(x0, x0 + 6)]       # x26-31: arm + band + 2 interior/band cols
        mid = [cell(30, cy)] * 4                                # plain band / interior column, repeated
        rows.append(left + mid + [mirror(c) for c in reversed(left)])
    plain_row = list(rows[3]); plain_row[1] = plain; plain_row[-2] = mirror(plain)
    rows = rows[:3] + [plain_row, rows[3], plain_row] + rows[4:]
    return np.concatenate([np.concatenate(rw, axis=1) for rw in rows], axis=0)


def fountain():
    _, comp = b.region_layers(WC, FOUNTAIN_BOX)
    f = _cut_bg(comp, pink=True)
    H, W = f.shape[:2]
    yy, xx = np.mgrid[0:H, 0:W]
    outside = ((xx - 47.5) / 48.0) ** 2 + ((yy - 28.0) / 24.0) ** 2 > 1.0
    f[outside & (yy < 28)] = -1                                 # hedge behind the basin's top rim
    rgb = f.astype(int); lum = rgb.sum(-1) / 3.0
    blue = (rgb[..., 2] > rgb[..., 0] + 30)
    f[(yy < 10) & (xx >= 34) & (xx < 62) & ~blue & (lum < 120) & (yy < 8)] = -1   # hedge peeking over the rim
    rgb = f.astype(int); lum = rgb.sum(-1) / 3.0
    statue = (xx >= 38) & (xx < 58) & (yy >= 9) & (yy < 30) & ~blue & (f >= 0).all(-1)
    stone = ~blue & ~statue & (lum > 120) & ((rgb.max(-1) - rgb.min(-1)) < 48) & (f >= 0).all(-1)
    f = _ramp(f, statue, BRONZE)
    f = _ramp(f, stone, STONE)
    return f


def _ring_ramps(img):
    """The monument is recoloured from its OWN materials (one palette family):
    statue = sandstone in the ring's brick shades, basin = the ring's rim stone."""
    from collections import Counter
    px = Counter(tuple(v) for v in img.reshape(-1, 3) if v[0] >= 0)
    lum = lambda c: sum(c) / 3.0
    grey = [c for c in px if max(c) - min(c) < 40 and lum(c) > 90]
    warm = [c for c in px if c[0] > c[2] + 30 and lum(c) > 70]
    pick = lambda cs: [cs[round(i * (len(cs) - 1) / 4)] for i in range(5)] if len(cs) >= 2 else cs
    return pick(sorted(warm, key=lum)), pick(sorted(grey, key=lum))


def quantize(img, n):
    """The monument gets exactly ONE palette: reduce its opaque pixels to n colours
    (median cut), transparency untouched."""
    from PIL import Image
    m = (img >= 0).all(-1)
    cols = sorted({tuple(v) for v in img[m]})
    if len(cols) <= n: return img
    strip = Image.fromarray(np.array(cols, np.uint8).reshape(1, -1, 3))
    weights = {}
    for v in map(tuple, img[m]): weights[v] = weights.get(v, 0) + 1
    big = np.repeat(np.array(cols, np.uint8), [max(1, weights[c] // 4) for c in cols], axis=0).reshape(1, -1, 3)
    q = Image.fromarray(big).quantize(colors=n, method=Image.Quantize.MEDIANCUT)
    pal = np.array(q.getpalette()[:n * 3], int).reshape(n, 3)
    pal = (pal // 8) * 8                                       # GBA 15-bit colour steps
    lut = {c: tuple(pal[np.sqrt(((pal - np.array(c)) ** 2).sum(1)).argmin()]) for c in cols}
    out = img.copy()
    out[m] = np.array([lut[tuple(v)] for v in img[m]])
    return out


def monument():
    img = ring()
    global BRONZE, STONE
    BRONZE, STONE = _ring_ramps(img)
    f = fountain()
    fy, fx = 2 * 16 + 8, 5 * 16                                    # centred in the 10x5 interior
    m = (f >= 0).all(-1)
    sub = img[fy:fy + f.shape[0], fx:fx + f.shape[1]]
    sub[m] = f[m]
    img = quantize(img, 15)
    blocked = np.zeros((H_CELLS, W_CELLS), bool)
    for cy in range(H_CELLS):
        for cx in range(W_CELLS):
            fm = m[max(0, cy * 16 - fy):max(0, cy * 16 - fy + 16), max(0, cx * 16 - fx):max(0, cx * 16 - fx + 16)]
            if fm.size and fm.mean() > 0.25: blocked[cy, cx] = True
    return img, blocked


if __name__ == '__main__':
    from PIL import Image
    img, blocked = monument()
    show = np.where((img >= 0).all(-1)[..., None], img, np.array([150, 200, 150])).astype(np.uint8)
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp/monument.png'
    Image.fromarray(show).resize((show.shape[1] * 3, show.shape[0] * 3), Image.NEAREST).save(out)
    print(img.shape, 'blocked cells', int(blocked.sum()))
