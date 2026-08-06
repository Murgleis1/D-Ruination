#!/usr/bin/env python3
"""
Reduce Evernahn source art to GBA-native 15-colour sub-palettes.

THE POINT
---------
Every GBA tileset lives inside 15 colours + 1 transparent per sub-palette. The
Evernahn source is not GBA-native art -- it carries smooth shading (the
monastery has 37 structural colours, the lab 31) that a GBA tileset simply does
not have room for. Reducing it is not a compromise to be avoided; it is the
conversion, and doing it WELL is what separates a distinctive tileset from a
muddy one.

(The "avoid quantising" note in the conversion README applied to the autumn
cliff/path merge, where the source palettes were ALREADY GBA-native 15-colour
sets and could be taken verbatim. Different situation entirely.)

HOW THIS REDUCES, AND WHY
-------------------------
Naive median-cut splits the colour cube by population, which on architectural
art spends most of its budget on the large flat wall areas and starves the
outlines and highlights -- exactly the features that carry readability at 16px.
This does three things differently:

1. CLUSTER IN A PERCEPTUAL SPACE. Distances are computed with luminance
   weighted roughly 2x against chroma, so the reducer preserves the light/dark
   structure (which reads as form) in preference to hue nuance (which does not,
   at this size).

2. PIN THE ANCHORS. The darkest and lightest structural colours are forced into
   the output palette before clustering runs on the remainder. Outlines and
   speculars are single-digit percentages of pixels, so any population-weighted
   method drops them -- and dropping them is what makes converted art look
   washed out and shapeless.

3. WEIGHT BY POPULATION, BUT SUBLINEARLY. Cluster centroids use sqrt(count)
   weighting. Linear weighting lets a big flat wall dominate its cluster and
   drag the centroid off the shaded tones; unweighted treats a 4-pixel
   antialiasing tail as equal to a 2000-pixel wall face. sqrt sits between.

NO DITHERING, deliberately. Established earlier in this project on the title
screen: dithering on GBA-scale art magnifies into visible noise on modern
displays and destroys the crisp flat regions that make pixel art read. Flat
regions are the goal.

Usage:
  python3 tools/evernahn_conversion/reduce_palette.py --preview
  python3 tools/evernahn_conversion/reduce_palette.py --set monastery --colors 15
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image

REPO = Path(__file__).resolve().parents[2]
SHEET = REPO / "assets" / "pelluca_tileset_source" / "Evernahn.png"

# name -> (first row, last row) on the source sheet.
# ROWS ARE 32px CELLS, not 16. This is the sheet's native cell size and it is
# recorded in assets/pelluca_ship/ship_spec.json ("cell_px": 32). Reading these
# as 16px rows silently returns a completely different slice of the sheet -- it
# does not error, it just measures the wrong art. Validated by reproducing the
# ship spec's recorded 218x124 bbox and 10-colour count from rows 180-183 c0-c6.
CELL = 32
SETS = {
    "monastery": (18, 23),
    "tavern": (69, 71),
    "house": (100, 104),
    "lab": (173, 178),
    "ship": (179, 186),
}

# luminance weighted against chroma for the distance metric
W = np.array([0.30, 0.59, 0.11])


def load(name):
    a = np.array(Image.open(SHEET).convert("RGBA"))
    r0, r1 = SETS[name]
    return a[r0 * CELL:(r1 + 1) * CELL]


def perceptual(rgb):
    """RGB -> a space where euclidean distance approximates perceived difference."""
    rgb = rgb.astype(float)
    lum = rgb @ W
    return np.column_stack([lum * 2.0, rgb[:, 0] - lum, rgb[:, 2] - lum])


def reduce_palette(px, counts, k):
    """px: unique RGB (n,3).  counts: pixel population per colour.  -> k colours."""
    lum = px @ W
    anchors = [int(np.argmin(lum)), int(np.argmax(lum))]          # darkest + lightest
    anchors = list(dict.fromkeys(anchors))

    P = perceptual(px)
    w = np.sqrt(counts.astype(float))                              # sublinear weighting

    # seed remaining centroids by weighted k-means++ on the non-anchor colours
    cent = [P[i] for i in anchors]
    rng = np.random.default_rng(0)
    while len(cent) < k:
        d = np.min([((P - c) ** 2).sum(1) for c in cent], axis=0) * w
        if d.sum() <= 0:
            break
        cent.append(P[rng.choice(len(P), p=d / d.sum())])
    cent = np.array(cent[:k])

    for _ in range(60):
        lbl = np.argmin(((P[:, None, :] - cent[None]) ** 2).sum(2), axis=1)
        new = cent.copy()
        for j in range(len(cent)):
            m = lbl == j
            if m.any():
                new[j] = (P[m] * w[m, None]).sum(0) / w[m].sum()
        if np.allclose(new, cent):
            break
        cent = new

    # map each centroid back to the nearest ACTUAL source colour, so every output
    # colour is one the artist chose rather than an invented average
    out, used = [], set()
    for c in cent:
        order = np.argsort(((P - c) ** 2).sum(1))
        for i in order:
            if i not in used:
                used.add(int(i))
                out.append(px[i])
                break
    # force the anchors back in if clustering displaced them
    for i in anchors:
        if not any((np.array(o) == px[i]).all() for o in out):
            out[-1] = px[i]
    return np.array(out[:k])


def apply_palette(block, pal):
    """Nearest-colour map, no dithering. Alpha preserved."""
    rgb = block[:, :, :3].astype(int)
    op = block[:, :, 3] > 128
    P = perceptual(rgb.reshape(-1, 3))
    Q = perceptual(pal)
    idx = np.argmin(((P[:, None, :] - Q[None]) ** 2).sum(2), axis=1)
    out = pal[idx].reshape(rgb.shape).astype(np.uint8)
    res = block.copy()
    res[:, :, :3] = out
    res[~op] = 0
    return res


def run(name, k):
    blk = load(name)
    op = blk[blk[:, :, 3] > 128][:, :3].astype(int)
    px, counts = np.unique(op, axis=0, return_counts=True)
    pal = reduce_palette(px, counts, k)
    red = apply_palette(blk, pal)
    o = blk[:, :, :3].astype(int)
    r = red[:, :, :3].astype(int)
    m = blk[:, :, 3] > 128
    err = np.abs(o[m] - r[m]).mean()
    return blk, red, pal, len(px), err


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--set", default=None)
    ap.add_argument("--colors", type=int, default=15)
    ap.add_argument("--preview", action="store_true")
    a = ap.parse_args()
    names = [a.set] if a.set else list(SETS)
    for n in names:
        blk, red, pal, orig, err = run(n, a.colors)
        print(f"{n:10s} {orig:3d} -> {len(pal):2d} colours   mean abs error {err:5.2f}")
    if a.preview:
        print("(use render_reduction.py to produce the comparison sheet)")


if __name__ == "__main__":
    main()
