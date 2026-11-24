"""The summit's abandoned ruins, in Crown stone, snowed over (user 2026-11-24): painted from Crown's own masonry
(Crown 33's bastion bricks and its pale dressed stone; Crown 32's cathedral portal), in Mirroh's cold gloom.
  * hut(seed): a roofless stone hut, 4x4 cells, seen from above and in front as the GBA draws a building: its back
    wall's inner face, the tops of its side walls, its front wall, all broken along their tops and capped with snow;
    its roof fallen in, a snow-covered heap of stones and a beam filling it; its doorway choked with fallen stones (so
    it reads as closed: the hut is solid and nothing invites the player in).
  * shrine(): Crown's cathedral portal (rose window, arch, door), 4x4, its top crumbled and snowed on, its doorway
    walled up with fallen blocks and a drift (closed for the same reason).
Both return (rgb, alpha) of 64x64 pixels."""
import random
import numpy as np
import mirroh_mock as mm
S = 16
SNOW, SNOW_SH, SNOW_DK = (246, 250, 255), (214, 230, 246), (186, 208, 232)

def _tile(m, h, w, src='c33'):
    t = mm.full(src, m); return np.tile(t, (h // S + 1, w // S + 1, 1))[:h, :w]

def _stones(rgb, a, box, n, r, seed, cols=((112, 116, 132), (88, 92, 110), (140, 144, 158))):
    rr = random.Random(seed); x0, y0, x1, y1 = box; yy, xx = np.mgrid[0:rgb.shape[0], 0:rgb.shape[1]]
    for _ in range(n):
        cx, cy = rr.uniform(x0, x1), rr.uniform(y0, y1); rx, ry = rr.uniform(r * 0.7, r * 1.3), rr.uniform(r * 0.5, r * 0.9)
        m = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1
        c = np.array(rr.choice(cols)); rgb[m] = c; a |= m
        hi = m & (yy < cy - ry * 0.3); rgb[hi] = SNOW                       # (snow on each stone)
        lo = m & (yy > cy + ry * 0.5); rgb[lo] = (c * 0.7).astype(int)

def _jag(rr, n, lo, hi, step=(-2, -1, 0, 0, 1, 2)):
    v = rr.randint(lo, hi); out = []
    for _ in range(n): v = max(lo, min(hi, v + rr.choice(step))); out.append(v)
    return out

def _cap(rgb, a, x, ytop, d=3):
    d = 3 if d >= 3 else 2
    rgb[ytop:ytop + d, x] = SNOW; rgb[ytop + d, x] = SNOW_SH

def hut(seed):
    rr = random.Random(seed); N = 4 * S
    rgb = np.zeros((N, N, 3), int); a = np.zeros((N, N), bool)
    brick, top, lower = _tile(0x56, N, N), _tile(0x11b, N, N), _tile(0x66, N, N)
    # inside: the snow on its floor in the walls' shade (darkest under the back wall), the fallen roof's stones and
    # beams lying in it under a little snow
    yy, xx = np.mgrid[0:N, 0:N]
    inner = (xx >= 6) & (xx < N - 6) & (yy >= 14) & (yy < 48)
    t = np.clip((yy - 18) / 26.0, 0, 1)[..., None]
    rgb[inner] = (np.array([120, 136, 168]) * (1 - t) + np.array(SNOW_DK) * t)[inner].astype(int); a |= inner
    for (bx0, by0, bx1, by1) in ((10, 26, 50, 38), (16, 40, 44, 30)):                 # (two beams, crossed)
        for t_ in np.linspace(0, 1, 60):
            bx, by = int(bx0 + (bx1 - bx0) * t_), int(by0 + (by1 - by0) * t_)
            rgb[by:by + 3, bx:bx + 2] = (70, 56, 50); rgb[by, bx:bx + 2] = (104, 84, 72); rgb[by + 3, bx:bx + 2] = SNOW_SH
    _stones(rgb, a, (12, 28, 52, 44), 9, 2.8, seed, cols=((96, 100, 116), (78, 82, 98), (120, 124, 138)))
    # the back wall's inner face (behind the heap), its top broken and snowed
    back = _jag(rr, N, 4, 12)
    for x in range(2, N - 2):
        y0 = back[x]; rgb[y0 + 4:24, x] = brick[y0 + 4:24, x]; rgb[y0:y0 + 4, x] = top[y0:y0 + 4, x]; a[y0:24, x] = True
        _cap(rgb, a, x, y0, 2 + (x % 5 == 0))
    # the side walls' tops, running down to the front; the east one broken through
    for x0 in (0, N - 7):
        for x in range(x0, x0 + 7):
            for y in range(back[min(max(x, 2), N - 3)] + 2, 50):
                if x0 and 30 <= y < 37 + (x % 3): continue                       # (a breach)
                rgb[y, x] = (top[y, x] * 0.8).astype(int); a[y, x] = True
            rgb[back[min(max(x, 2), N - 3)] + 2:back[min(max(x, 2), N - 3)] + 5, x] = SNOW
        for y in range(10, 50):
            if x0 and 30 <= y < 37 + (y % 3 == 0): continue
            rgb[y, x0 + 1:x0 + 6] = SNOW; rgb[y, x0 + (5 if x0 == 0 else 1)] = SNOW_SH     # (snow lying along each wall top)
        rgb[14:48, x0 + (6 if x0 == 0 else 0)] = (62, 64, 80)              # (the wall's inner edge in shadow)
    # the front wall: its top (dressed stone, snowed), its face (bricks, the lower courses darker); broken low on the
    # east; the doorway choked with fallen stones under a drift
    ftop = [40 + j for j in _jag(rr, N, 0, 3)]
    for x in range(N):
        if x >= 44: ftop[x] = max(ftop[x], 44 + min(4, (x - 44) // 2))
        y0 = ftop[x]; rgb[y0:y0 + 4, x] = top[y0:y0 + 4, x]; rgb[y0 + 4:N, x] = brick[y0 + 4:N, x]
        rgb[56:N, x] = lower[56:N, x]; a[y0:N, x] = True; _cap(rgb, a, x, y0, 2 + (x % 4 == 1))
    door = (xx >= 22) & (xx < 36) & (yy >= 46)
    rgb[door] = (34, 38, 52)
    _stones(rgb, a, (23, 47, 35, 62), 16, 3.2, seed + 1, cols=((104, 108, 122), (86, 90, 106), (128, 132, 146)))
    drift = door & (yy >= 58 - ((xx - 29) ** 2) // 18); rgb[drift] = SNOW; rgb[drift & (yy == yy)] = rgb[drift]
    out = mm.gloom(rgb.clip(0, 255).astype(np.uint8), 0.22, (52, 60, 84), keep_snow=True)
    return out, a

def shrine(seed=41):
    rr = random.Random(seed); N = 4 * S
    C32G = (0x1, 0x2, 0x13, 0x14, 0x1b, 0x1c, 0x1d, 0x93, 0x94, 0x95, 0xa9, 0xb0, 0xb1, 0xb2, 0xb4, 0xb9, 0xbb, 0x6f, 0x77,
            0x18, 0x19, 0x10, 0x11, 0x12, 0xc, 0xd)
    pc = mm.cut('c32', 29, 11, 4, 4, ground=C32G, ring=False)
    rgb = np.zeros((N, N, 3), np.uint8); a = np.zeros((N, N), bool)
    for dy, r in enumerate(pc):
        for dx, p in enumerate(r):
            if p is not None: rgb[dy * S:dy * S + S, dx * S:dx * S + S] = p[0]; a[dy * S:dy * S + S, dx * S:dx * S + S] = p[1]
    rgb = mm.slate_roof(rgb).astype(int)
    # the top crumbled: an irregular broken line, deeper toward the sides (the arch's crown stands)
    yy, xx = np.mgrid[0:N, 0:N]
    brk = _jag(rr, N, 0, 6)
    for x in range(N):
        d = brk[x] + int(9 * (abs(x - 31.5) / 32.0) ** 2 * 2)
        col = np.where(a[:, x])[0]
        if len(col): a[col[0]:col[0] + d, x] = False
    for x in range(N):
        col = np.where(a[:, x])[0]
        if len(col): _cap(rgb, a, x, col[0], 2 + (x % 6 == 2))
    # the doorway walled up with fallen blocks, a drift against it
    from scipy.ndimage import label
    dark = a & (rgb.sum(-1) < 150) & (yy > 30)
    lb, n = label(dark)
    if n:
        k = 1 + int(np.argmax(np.bincount(lb.ravel())[1:])); door = lb == k              # (the doorway: the big dark)
        wall = (_tile(0x56, N, N).astype(float) * 0.62 + np.array([20, 26, 34])).astype(int)
        rgb[door] = wall[door]
        ys, xs = np.where(door); _stones(rgb, a, (xs.min() + 2, N - 12, xs.max() - 2, N - 4), 6, 3.0, seed,
                                         cols=((96, 104, 100), (76, 84, 82), (122, 130, 124)))
    drift = a & (yy >= N - 5 + ((xx - 32) ** 2) // 220); rgb[drift] = SNOW
    rgb[drift & (yy == N - 5)] = SNOW_SH
    return rgb.clip(0, 255).astype(np.uint8), a
