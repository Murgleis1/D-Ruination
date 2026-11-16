"""Beach palm for Pelluca's shore (user 2026-11-16: "more beachy trees" on the beach).

Source: MonoMyth Mandrake City palm, cells x34-35 y29-31 (2 wide, 3 tall). Its crown is the
whole TOP layer (players walk behind it); the trunk + tuft is the MIDDLE layer of the bottom
row (the middle layer above it is a fence/pavement there -> dropped).
Recoloured into Wood Avens' own foliage: leaf greens -> the WA tree crown ramp by luminance rank,
outline -> the WA tree outline; the trunk keeps its own browns. The palm then belongs with
the town's trees and shares their colours.

palm() -> (top, mid): RGB layer images (48x32), -1 = transparent.
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_cormoria as b

MANDRAKE = 0x869564
BOX = (34, 29, 35, 31)


def _ramp_of(pixels):
    cols = sorted({tuple(v) for v in pixels}, key=lambda c: sum(c))
    return np.array(cols, int)


def _map_by_rank(img, mask, ramp):
    out = img.copy()
    if not mask.any() or not len(ramp): return out
    lum = img.sum(-1)
    vals = np.unique(lum[mask])
    for i, v in enumerate(vals):
        k = int(round(i * (len(ramp) - 1) / max(1, len(vals) - 1)))
        out[mask & (lum == v)] = ramp[k]
    return out


def palm():
    lay, _ = b.region_layers(MANDRAKE, BOX)
    top = lay[2].copy()
    mid = np.full_like(lay[1], -1)
    mid[32:48] = lay[1][32:48]                                 # trunk + tuft only (bottom row)
    # Wood Avens tree colours, measured on the forest pieces as built (crown teals + outline)
    WA_GREENS = np.array([(0, 80, 88), (8, 120, 88), (40, 168, 112), (80, 184, 112), (120, 232, 128)], int)
    WA_DARK = np.array([48, 56, 80])                           # crown ramp + outline of the WA trees (22-25, 29-32)
    for img in (top, mid):
        rgb = img.astype(int); op = (img >= 0).all(-1)
        lum = rgb.sum(-1)
        leaf = op & (rgb[..., 1] > rgb[..., 0] + 10)                   # every leaf green keeps its shade rank
        dark = op & ~leaf & (lum <= 200) & ~(rgb[..., 0] > rgb[..., 2] + 15)   # outline (not trunk brown)
        img[:] = _map_by_rank(img, leaf, WA_GREENS)
        img[dark] = WA_DARK
    return top, mid


if __name__ == '__main__':
    from PIL import Image
    top, mid = palm()
    img = np.zeros(top.shape, int); img[:] = (232, 208, 152)
    for L in (mid, top):
        m = (L >= 0).all(-1); img[m] = L[m]
    Image.fromarray(img.astype(np.uint8)).resize((img.shape[1] * 5, img.shape[0] * 5), Image.NEAREST).save(
        sys.argv[1] if len(sys.argv) > 1 else '/tmp/palm.png')
