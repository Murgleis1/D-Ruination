"""Trace -> MonoMyth transplant (user 2026-11-17: "once you trace something over, ... go back to the
monomyth aesthetic with those exact pixels and shading and transplant them").

Stage 1, trace(): the user's design art gives STRUCTURE only: silhouette (with partial-coverage
strands kept when they are >= COVER covered), material regions, and a coarse light/dark map.
Stage 2, transplant(): every pixel of a material is re-rendered from MonoMyth's own pixels.
Texture-by-numbers: for each target pixel (raster order) pick the MonoMyth source pixel whose
context matches best: coarse tone in the trace, distance to the silhouette edge, the edge's facing
(light comes from the upper right), and the already-chosen neighbours (left, up-left, up, up-right),
which keeps MonoMyth's clusters coherent. The chosen source value is copied, so the clusters, lit
tips and dark separations are MonoMyth's, in the user's shape.
"""
import numpy as np
from PIL import Image

COVER = 0.5


def coverage(rgb, bg, fg):
    """How far each pixel is from the background toward a foreground colour (0..1)."""
    rgb = rgb.astype(float); bg = np.array(bg, float); fg = np.array(fg, float)
    v = fg - bg
    return np.clip(((rgb - bg) @ v) / (v @ v), 0, 1)


def features(mask):
    """distance to the outside (0..3) and the outward direction (0..7, 8 = interior) per pixel."""
    H, W = mask.shape
    dist = np.full((H, W), 3); odir = np.full((H, W), 8)
    for y in range(H):
        for x in range(W):
            if not mask[y, x]: continue
            best = 99; bd = (0, 0)
            for dy in range(-4, 5):
                for dx in range(-4, 5):
                    yy, xx = y + dy, x + dx
                    if not (0 <= yy < H and 0 <= xx < W) or not mask[yy, xx]:
                        d = max(abs(dy), abs(dx))
                        if d < best: best, bd = d, (dy, dx)
            if best <= 4:
                dist[y, x] = best - 1
                ang = (np.degrees(np.arctan2(-bd[0], bd[1])) + 360) % 360
                odir[y, x] = int(((ang + 22.5) % 360) // 45)
    return dist, odir


def coarse(vals, mask):
    """3x3 mean tone inside the mask (tones 0 dark .. 2 light)."""
    H, W = vals.shape; c = np.zeros((H, W))
    for y in range(H):
        for x in range(W):
            if not mask[y, x]: continue
            win = vals[max(0, y - 1):y + 2, max(0, x - 1):x + 2]
            m = mask[max(0, y - 1):y + 2, max(0, x - 1):x + 2]
            c[y, x] = win[m].mean()
    return c


def transplant(t_mask, t_coarse, s_vals, s_mask, w_tone=2.0, w_dist=1.0, w_dir=0.6, w_nb=1.2):
    """Return target values (source alphabet) for every pixel of t_mask."""
    s_c = coarse(s_vals, s_mask)
    s_d, s_o = features(s_mask)
    t_d, t_o = features(t_mask)
    sy, sx = np.nonzero(s_mask)
    SV = s_vals[sy, sx]; SC = s_c[sy, sx]; SD = s_d[sy, sx]; SO = s_o[sy, sx]
    def snb(dy, dx):
        yy, xx = sy + dy, sx + dx
        ok = (yy >= 0) & (yy < s_vals.shape[0]) & (xx >= 0) & (xx < s_vals.shape[1])
        v = np.full(len(sy), -1)
        v[ok] = np.where(s_mask[yy[ok], xx[ok]], s_vals[yy[ok], xx[ok]], -1)
        return v
    NB = [(0, -1), (-1, -1), (-1, 0), (-1, 1)]
    SN = [snb(dy, dx) for dy, dx in NB]
    H, W = t_mask.shape
    out = np.full((H, W), -1)
    for y in range(H):
        for x in range(W):
            if not t_mask[y, x]: continue
            cost = w_tone * np.abs(SC - t_coarse[y, x]) + w_dist * (SD != t_d[y, x])
            dd = np.abs(SO - t_o[y, x]); dd = np.minimum(dd, 8 - dd); dd[(SO == 8) != (t_o[y, x] == 8)] = 4
            cost = cost + w_dir * dd / 4
            for (dy, dx), sn in zip(NB, SN):
                yy, xx = y + dy, x + dx
                tv = out[yy, xx] if (0 <= yy < H and 0 <= xx < W) else -1
                cost = cost + w_nb * (sn != tv)
            out[y, x] = SV[int(np.argmin(cost))]
    return out
