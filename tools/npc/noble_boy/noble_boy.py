"""The spoiled noble boy trainer set (user 2026-11-25: "a young nobleman child ... three variations of this boy with
black, light brown and blonde hair plus his overworld sprite (and slightly different shades of skin color)"; "you'd
need to change the color of his outfit a bit for each variation too on front plus overworld sprites").
Source: the user's own sprite pair (src_front.png, an Essentials-style front at 2x; src_ow.png, a 4x4 Essentials
walking sheet at 2x, 16x24 frames). Each variant recolours, by lightness ramp, the hair (the source's blue), the skin,
the coat and trousers (the source's greys) and the waistcoat (the source's gold); the outline and whites are kept.
Out: front 64x64 (two fits for the user to choose: scaled to fit, or cropped at the shins), overworld 16x32 x 9 frames
in Emerald's order (S, N, W, walk S x2, walk N x2, walk W x2), each quantised to 15 colours + transparency.
Usage: python3 noble_boy.py OUTDIR"""
import os, sys, colorsys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))

def native(p):
    return np.array(Image.open(os.path.join(HERE, p)).convert('RGBA'))[::2, ::2].copy()

def hsv(c): return colorsys.rgb_to_hsv(*[v / 255 for v in c[:3]])
def lum(c): return 0.3 * c[0] + 0.55 * c[1] + 0.15 * c[2]

def role(c):
    h, s, v = hsv(c)
    if c[:3] in ((38, 38, 38), (0, 0, 0)) or v < 0.13: return 'outline'
    if s < 0.06 and v > 0.8: return 'white'
    if 0.55 <= h <= 0.67 and s > 0.5: return 'hair'
    if s < 0.06: return 'coat'
    if 0.12 <= h <= 0.16 and s > 0.4: return 'vest'
    if (h < 0.08 or h > 0.98) and 0.25 < s < 0.5 and v > 0.55: return 'skin'
    if h > 0.85 and s > 0.35: return 'shoes'
    return 'other'

def ramp(dark, light, n=6):
    d, l = np.array(dark, float), np.array(light, float)
    return [tuple(int(v) for v in d + (l - d) * i / (n - 1)) for i in range(n)]

VARIANTS = {
    'black':  dict(hair=ramp((14, 12, 18), (88, 84, 98)), skin=ramp((150, 92, 78), (250, 214, 192)),
                   coat=ramp((40, 18, 26), (150, 74, 88)), vest=ramp((96, 76, 20), (236, 206, 112))),     # burgundy, gold
    'brown':  dict(hair=ramp((58, 34, 20), (178, 128, 82)), skin=ramp((132, 80, 58), (238, 190, 156)),
                   coat=ramp((20, 40, 30), (88, 136, 104)), vest=ramp((110, 98, 78), (240, 230, 200))),    # forest, cream
    'blonde': dict(hair=ramp((120, 84, 30), (250, 230, 150)), skin=ramp((160, 104, 82), (252, 222, 202)),
                   coat=ramp((22, 30, 54), (104, 124, 170)), vest=ramp((90, 94, 106), (226, 232, 242))),   # navy, silver
}

def recolour(a, var):
    out = a.copy(); cols = {tuple(c) for c in a[a[..., 3] > 0][:, :3]}
    groups = {}
    for c in cols: groups.setdefault(role(c), []).append(c)
    m = {}
    for g, cs in groups.items():
        if g not in var: continue
        ls = sorted(set(lum(c) for c in cs)); lo, hi = ls[0], ls[-1]
        for c in cs:
            t = 0 if hi == lo else (lum(c) - lo) / (hi - lo)
            r = var[g]; m[c] = r[min(len(r) - 1, int(round(t * (len(r) - 1))))]
    for c, n in m.items():
        sel = (a[..., :3] == c).all(-1) & (a[..., 3] > 0); out[sel, :3] = n
    return out

def quant(a, n=15):
    """to n colours + transparency: repeatedly merge the two closest colours (redmean distance, weighted by the rarer
    one's pixel count) into the commoner one, so small but distinct features (eyes, the skin's highlight) survive"""
    op = a[..., 3] > 0
    from collections import Counter
    cnt = Counter(tuple(int(v) for v in c) for c in a[op][:, :3])
    def dist(p, q):
        r = (p[0] + q[0]) / 2; d = np.array(p, float) - np.array(q, float)
        return ((2 + r / 256) * d[0] ** 2 + 4 * d[1] ** 2 + (2 + (255 - r) / 256) * d[2] ** 2) ** 0.5
    m = {c: c for c in cnt}
    while len(cnt) > n:
        cs = list(cnt); best = None
        for i in range(len(cs)):
            for j in range(i + 1, len(cs)):
                p, q = cs[i], cs[j]; cost = dist(p, q) * min(cnt[p], cnt[q]) ** 0.5
                if best is None or cost < best[0]: best = (cost, p, q)
        _, p, q = best
        keep, drop = (p, q) if cnt[p] >= cnt[q] else (q, p)
        cnt[keep] += cnt.pop(drop)
        for k, v in m.items():
            if v == drop: m[k] = keep
    out = a.copy()
    for k, v in m.items():
        if k != v: out[(a[..., :3] == k).all(-1) & op, :3] = v
    out[~op] = 0
    return out

def front_fits(a):
    ys, xs = np.nonzero(a[..., 3]); y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()
    fig = a[y0:y1 + 1, x0:x1 + 1]; h, w = fig.shape[:2]
    # A: scaled to fit 64 tall (nearest; the figure keeps its proportions)
    sc = 63 / h; A = np.array(Image.fromarray(fig).resize((max(1, round(w * sc)), 63), Image.NEAREST))
    ca = np.zeros((64, 64, 4), np.uint8); ox = (64 - A.shape[1]) // 2; ca[1:64, ox:ox + A.shape[1]] = A
    # B: full size, cropped at the shins (the bottom 64 rows of the head-down figure: keep the head, lose the feet)
    B = fig[:64]; cb = np.zeros((64, 64, 4), np.uint8); ox = (64 - w) // 2; cb[64 - B.shape[0]:, ox:ox + w] = B
    return ca, cb

def overworld(a):
    """Essentials rows: down, left, right, up; columns: stand, step, stand, step -> Emerald's 9 frames, 16x32"""
    f = lambda r, c: a[r * 24:(r + 1) * 24, c * 16:(c + 1) * 16]
    order = [f(0, 0), f(3, 0), f(1, 0), f(0, 1), f(0, 3), f(3, 1), f(3, 3), f(1, 1), f(1, 3)]
    out = np.zeros((32, 16 * 9, 4), np.uint8)
    for i, fr in enumerate(order): out[8:32, i * 16:(i + 1) * 16] = fr
    return out

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    fr, ow = native('src_front.png'), native('src_ow.png')
    res = {}
    for name, var in VARIANTS.items():
        f = recolour(fr, var); o = recolour(ow, var)
        fa, fb = front_fits(f)
        res[name] = (quant(fa), quant(fb), quant(overworld(o)))
        for k, im in zip(('front_fit', 'front_crop', 'ow'), res[name]):
            Image.fromarray(im).save(os.path.join(outdir, '%s_%s.png' % (name, k)))
    return res

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/tmp/noble')
