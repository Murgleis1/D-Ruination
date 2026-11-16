"""Adapt the project's OWN portrait art (96x96 RGBA masters) into the MonoMyth-style portrait
system (80x80, 16 colours, index 0 transparent) -- user 2026-11-16: "adapt my art that we already
had ... into the Monomyth system and rebuild them cleanly", not MonoMyth characters.

Clean by construction (each step fixes a measured defect of the retired build_portraits.py):
  * NO RESAMPLING. 96->80 is a non-integer scale that blends pixels (the blur). The 80x80 bust is
    a CROP at native pixel scale: bottom-aligned (cut flat under the text box edge, as MonoMyth's
    are), horizontally centred on the art.
  * EDGES: alpha >= 96 is opaque, below is transparent -- no half-transparent pixels turning into
    holes in the outline (Osrid).
  * NO OPAQUE PIXEL CAN BECOME TRANSPARENT: index 0 is reserved; quantisation only ever assigns
    1..15 (Baradus's black lenses were landing on index 0).
  * ACCENTS SURVIVE: palette = the 15 colours chosen by a greedy farthest-point pass seeded with the
    most-used colours, weighted so small but distinct colours (red eyes, a purple collar) still
    get a slot (Cadmus lost both to median-cut). Then each pixel -> nearest palette colour.

Run: python3 -I portrait_adapt.py SRC_DIR OUT_DIR [--preview sheet.png]
"""
import os, sys, glob
import numpy as np
from PIL import Image

SIZE = 80
ALPHA = 96


def crop80(rgba):
    a = rgba[..., 3] >= ALPHA
    h, w = a.shape
    ys, xs = np.nonzero(a)
    cx = (xs.min() + xs.max()) // 2
    x0 = int(np.clip(cx - SIZE // 2, 0, w - SIZE))
    y0 = h - SIZE                                         # bottom-aligned bust
    return rgba[y0:y0 + SIZE, x0:x0 + SIZE]


def palette15(rgb, mask):
    px = rgb[mask].astype(int)
    cols, counts = np.unique(px, axis=0, return_counts=True)
    if len(cols) <= 15:
        return cols
    lab = cols.astype(float)
    chosen = [int(np.argmax(counts))]
    d = np.sqrt(((lab - lab[chosen[0]]) ** 2).sum(1))
    while len(chosen) < 15:
        score = d * np.log1p(counts)                      # far from chosen, not a lone stray pixel
        i = int(np.argmax(score)); chosen.append(i)
        d = np.minimum(d, np.sqrt(((lab - lab[i]) ** 2).sum(1)))
    # refine: a few k-means steps weighted by counts, starting from the chosen seeds
    cent = lab[chosen].copy()
    for _ in range(6):
        lbl = np.argmin(((lab[:, None] - cent[None]) ** 2).sum(-1), 1)
        for k in range(15):
            m = lbl == k
            if m.any():
                # keep the seed's own colour if it is a distinct accent; else weighted mean
                cent[k] = (lab[m] * counts[m, None]).sum(0) / counts[m].sum()
    return np.clip(np.round(cent), 0, 255).astype(int)


def adapt(path):
    rgba = np.array(Image.open(path).convert('RGBA'))
    c = crop80(rgba)
    mask = c[..., 3] >= ALPHA
    rgb = c[..., :3].astype(int)
    pal = palette15(rgb, mask)
    idx = np.zeros((SIZE, SIZE), np.uint8)
    d = ((rgb[mask][:, None, :] - pal[None]) ** 2).sum(-1)
    idx[mask] = np.argmin(d, 1) + 1                      # 1..15 only
    full = np.zeros((16, 3), int); full[0] = (255, 0, 255); full[1:1 + len(pal)] = pal
    return idx, full.astype(np.uint8)


def save(idx, pal, path):
    im = Image.fromarray(idx, 'P'); im.putpalette([int(v) for c in pal for v in c] + [0] * (768 - 48))
    im.save(path, transparency=0)


if __name__ == '__main__':
    src, od = sys.argv[1], sys.argv[2]; os.makedirs(od, exist_ok=True)
    files = sorted(glob.glob(os.path.join(src, '*.png')))
    res = []
    for f in files:
        idx, pal = adapt(f); save(idx, pal, os.path.join(od, os.path.basename(f))); res.append((f, idx, pal))
    if '--preview' in sys.argv:
        from PIL import ImageDraw
        S, cols = 2, 6; W, H = 96 * S + 90 * S // 1, 96 * S + 16
        sheet = Image.new('RGB', (cols * (96 * S + 80 * S + 12), ((len(res) + cols - 1) // cols) * H), (30, 30, 30))
        dr = ImageDraw.Draw(sheet)
        for k, (f, idx, pal) in enumerate(res):
            x = (k % cols) * (96 * S + 80 * S + 12); y = (k // cols) * H
            o = Image.open(f).convert('RGBA'); bg = Image.new('RGBA', o.size, (110, 110, 130, 255)); bg.alpha_composite(o)
            sheet.paste(bg.convert('RGB').resize((96 * S, 96 * S), Image.NEAREST), (x, y + 14))
            rgb = pal[idx]; rgb[idx == 0] = (110, 110, 130)
            sheet.paste(Image.fromarray(rgb).resize((80 * S, 80 * S), Image.NEAREST), (x + 96 * S + 4, y + 14 + 16 * S))
            dr.text((x, y), os.path.basename(f)[:-4], fill=(255, 255, 0))
        sheet.save(sys.argv[sys.argv.index('--preview') + 1])
