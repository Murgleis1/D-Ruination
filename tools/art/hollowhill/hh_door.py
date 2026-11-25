"""Hollow Hill's sealed door, v2 (user 2026-11-25, of the two blue tablets in the knoll's face: "This is not a door").
Odyssey's own sealed door (its map 3.46: a monolithic slab set into a terraced hill, a great tree carved on it, a small
low door at its foot; Pokemon Odyssey, the same art family as Hollow Hill's), cut from its cliff and made Hollow
Hill's: the slab in the hill's cold slate (its old door's blue kept, darker), the tree carved on it a dead one (the
woods' own), the small door at its foot shut with a stone; blood soaked down its face from the top, a blood web across
the low door. 3 cells wide, 4 tall: it stands in the knoll's three bands (rows 33-35) and rises one row above them onto
the knoll's top (row 32), as Odyssey's does.
Credits: Pokemon Odyssey (the door)."""
import os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '..', '..', 'assets', 'odyssey_reference', 'pieces', 'sealed_door_346.npz')
X0, Y0, CW, CH = 28, 32, 3, 4                  # cells

def _cut():
    d = np.load(SRC); rgb = d['rgb'].astype(int)
    # the slab: the box x 16..64, y 16..80 of the 5x5 cut, less the cliff's colours (browns, mint) found outside it
    out = np.zeros((64, 48, 4), np.uint8)
    cliff = {tuple(c) for c in np.concatenate([rgb[:, :16].reshape(-1, 3), rgb[:, 64:].reshape(-1, 3), rgb[:16].reshape(-1, 3)])}
    sub = rgb[16:80, 16:64]
    keep = np.array([[tuple(c) not in cliff for c in row] for row in sub])
    from scipy.ndimage import binary_fill_holes
    keep = binary_fill_holes(keep)
    out[..., :3] = sub; out[keep, 3] = 255
    return out

# Odyssey's teal greys -> Hollow Hill's cold slate (lightness kept, hue to the old door's blue, darker)
def _slate(c):
    lum = 0.3 * c[0] + 0.55 * c[1] + 0.15 * c[2]
    t = min(1.0, max(0.0, (lum - 20) / 120))
    lo, hi = np.array((26, 28, 46)), np.array((132, 144, 176))
    return tuple(int(v) for v in lo + (hi - lo) * t)

def door():
    """(rgba 48x64): the slab, recoloured, its foot door shut, blood down its face, a web across the low door"""
    d = _cut(); a = d[..., 3] > 0
    # the carved tree made a dead one: its leaves (Odyssey's two leaf colours, inside the medallion) cut back to the
    # medallion's ground, its branches (the darkest colour) left bare
    yy, xx = np.mgrid[0:64, 0:48]
    med = (xx - 23.5) ** 2 + (yy - 30) ** 2 <= 17.5 ** 2
    for leaf in ((24, 40, 40), (56, 104, 96)):
        m = med & a & (d[..., :3] == leaf).all(-1) & (yy < 46); d[m, :3] = (40, 72, 80)
    from scipy.ndimage import binary_dilation
    br = med & a & (d[..., :3] == (8, 32, 24)).all(-1)
    thick = binary_dilation(br, np.array([[0, 0, 0], [0, 1, 1], [0, 1, 0]], bool)) & med & a & (yy < 47)
    d[thick & ~br, :3] = (8, 32, 24)                                                # (the bare branches carved deeper)
    cols = {tuple(int(v) for v in p) for p in d[a][:, :3]}
    m = {c: _slate(c) for c in cols}
    for y in range(64):
        for x in range(48):
            if a[y, x]: d[y, x, :3] = m[tuple(int(v) for v in d[y, x, :3])]
    # the low door (Odyssey's dark opening and its steps, x 17-30, y 49-63 of the slab): shut by a stone door set
    # back in a deep dark frame; a few torn threads of web across its top
    x0, x1, y0, y1 = 17, 30, 49, 63
    d[y0 - 1:y1 + 1, x0 - 1:x1 + 2, :3] = (16, 16, 26)                              # (the recess)
    d[y0 + 1:y1 + 1, x0 + 1:x1, :3] = (100, 108, 138)                               # (the stone door's face)
    d[y0 + 1, x0 + 1:x1, :3] = (138, 148, 176); d[y0 + 1:y1 + 1, x1 - 1, :3] = (70, 76, 102)
    d[y0 + 7, x0 + 2:x1 - 1, :3] = (62, 66, 92)                                     # (its two leaves' seam)
    for k in range(3):
        d[y0 + 3 + 6 * (k // 2), x0 + 4 + 5 * (k % 2), :3] = (52, 56, 80)              # (iron studs)
    import hh_mock as HM
    for (p, q) in (((x0 - 1, y0 + 1), (x0 + 6, y0 + 9)), ((x0 + 3, y0), (x0 + 9, y0 + 6)), ((x1 + 1, y0 + 2), (x1 - 5, y0 + 10)),
                   ((x0 + 6, y0 + 9), (x1 - 5, y0 + 10)), ((x0 + 9, y0 + 6), (x1 - 3, y0 + 4))):
        L = np.zeros((64, 48, 4), np.uint8); HM._line(L, p, q, HM.WEB_LIGHT); w = L[..., 3] > 0; d[w, :3] = L[w, :3]
    # blood: run down the slab's face from its top edge in a few drips, darker where it pooled at the foot
    import hh_mock as HM
    g = np.random.default_rng(3)
    for px, L in ((12, 22), (34, 15)):
        x = px
        for j in range(L):
            y = 4 + j
            if j and g.random() < 0.18: x += int(g.choice((-1, 1)))
            if y < 64 and a[y, x]: d[y, x, :3] = HM.BLOOD[2] if j < 3 else HM.BLOOD[1] if j < L - 4 else HM.BLOOD[0]
        d[4, px - 1:px + 2, :3] = HM.BLOOD[1]
    return d

def place(img, origin=(0, 0)):
    """paint the door onto a picture of the map whose cell (0, 0) is at pixel origin"""
    d = door(); a = d[..., 3] > 0
    X, Y = origin[0] + X0 * 16, origin[1] + Y0 * 16
    img[Y:Y + 64, X:X + 48][a] = d[a][:, :3]
    return img
