"""Tile-palette quantisation: make a picture GBA-legal by construction (every 8x8 tile drawn from one of n palettes
of 15 colours), for pictures too rich for mapbuild's packing (screenshots, stained glass).

  1. Group the tiles into n sets by their colours (k-means on each tile's mean and spread in Lab).
  2. Give each set its own best 15 colours (k-means in Lab over that set's pixels).
  3. Re-assign every tile to the palette that draws it best (least error); repeat.
  4. snap: colours that must be kept exactly (a palette whose tiles are mostly such colours has its colours snapped
     to the nearest of them).
Everything on the GBA's 5-bit grid. quantise(img, n=13) -> (picture, palettes).
"""
import numpy as np
from skimage.color import rgb2lab
from scipy.cluster.vq import kmeans2

def _q(a): return (np.asarray(a) >> 3) << 3

def quantise(img, n=13, k=15, iters=8, snap=(), seed=7, always=((0, 0, 0),)):
    """always: colours in every palette (black, so the void and outlines stay true black)."""
    always = np.array(always, int).reshape(-1, 3); k = k - len(always)
    img = _q(img.astype(int)); H, W = img.shape[:2]
    tiles = img.reshape(H // 8, 8, W // 8, 8, 3).transpose(0, 2, 1, 3, 4).reshape(-1, 64, 3)
    lab = rgb2lab((tiles / 255.).reshape(-1, 1, 3)).reshape(tiles.shape)
    # 1. initial groups
    feat = np.concatenate([lab.mean(1), lab.std(1)], 1)
    rng = np.random.default_rng(seed)
    _, grp = kmeans2(feat, n, minit='++', seed=seed, iter=30)
    snap = np.array(sorted(set(map(tuple, _q(np.array(list(snap))).tolist())))) if len(snap) else np.zeros((0, 3), int)
    snap_lab = rgb2lab((snap / 255.).reshape(-1, 1, 3)).reshape(-1, 3) if len(snap) else None
    pals = [None] * n
    for _ in range(iters):
        # 2. palettes
        for g in range(n):
            px = lab[grp == g].reshape(-1, 3)
            if len(px) == 0:
                pals[g] = lab[rng.integers(len(lab))].reshape(-1, 3)[:k]; continue
            uniq = np.unique(px.round(1), axis=0)
            if len(uniq) <= k: pals[g] = uniq; continue
            sub = px[rng.choice(len(px), min(len(px), 6000), replace=False)]
            c, _ = kmeans2(sub, k, minit='++', seed=seed, iter=20)
            pals[g] = c
        # 3. re-assign
        err = np.zeros((len(tiles), n))
        for g in range(n):
            d = ((lab[:, :, None, :] - pals[g][None, None, :, :]) ** 2).sum(-1).min(-1)
            err[:, g] = d.sum(1)
        new = err.argmin(1)
        if (new == grp).all(): break
        grp = new
    # 4. to RGB on the 5-bit grid; snap
    from skimage.color import lab2rgb
    out_pals = []
    for g in range(n):
        rgb = _q(np.clip(lab2rgb(pals[g].reshape(-1, 1, 3)).reshape(-1, 3) * 255, 0, 255).round().astype(int))
        if len(snap):
            tl = lab[grp == g].reshape(-1, 3)
            if len(tl):
                near = ((tl[:, None, :] - snap_lab[None]) ** 2).sum(-1).min(1)
                if (near < 30).mean() > 0.5:                      # (mostly kept colours: snap the palette to them)
                    pl = rgb2lab((rgb / 255.).reshape(-1, 1, 3)).reshape(-1, 3)
                    rgb = snap[((pl[:, None, :] - snap_lab[None]) ** 2).sum(-1).argmin(1)]
        out_pals.append(np.unique(np.concatenate([rgb, always]), axis=0))
    pal_lab = [rgb2lab((p / 255.).reshape(-1, 1, 3)).reshape(-1, 3) for p in out_pals]
    out = np.zeros_like(tiles)
    for i, g in enumerate(grp):
        d = ((lab[i][:, None, :] - pal_lab[g][None]) ** 2).sum(-1)
        out[i] = out_pals[g][d.argmin(1)]
    pic = out.reshape(H // 8, W // 8, 8, 8, 3).transpose(0, 2, 1, 3, 4).reshape(H, W, 3)
    return pic, out_pals
