"""Remove painted snow from MonoMyth (Fort Elderflower) building art.

Snow colours were chosen by LOOKING at per-colour masks on the tavern
(scratch tavern_snowmask.png), not by a brightness rule: the stone walls are pale
too. Snow = main white, pale/shade blues, and the blue cap outlines.

Per layer image (HxWx3, -1 = transparent):
 1. Exterior snow -- caps and bulges above/beside the roof outline: scanning in
    from every open (transparent) edge, leading snow becomes transparent. The
    first surviving pixel is set to the outline colour so the roof edge is redrawn.
 2. Interior snow -- ledges, sills, eaves: filled from the material BELOW at an
    even offset (keeps the 2-pixel dither), else from above, else the nearest
    non-snow pixel in the row.
 3. Protected pixels (e.g. the lamp post's blue glass) are never touched.
"""
import numpy as np

SNOW = [(248, 248, 248), (216, 248, 248), (224, 240, 248), (184, 232, 248), (192, 216, 240),
        (184, 216, 248), (136, 216, 248), (96, 160, 216), (48, 112, 192)]


def snow_mask(img, protect=None, colours=SNOW):
    m = np.zeros(img.shape[:2], bool)
    for c in colours:
        m |= (img == np.array(c)).all(-1)
    if protect is not None:
        m &= ~protect
    return m


def desnow(img, outline, protect=None):
    out = img.copy()
    H, W = img.shape[:2]
    snow = snow_mask(img, protect)
    clear = ~(img >= 0).all(-1)
    gone = np.zeros_like(snow)
    edge = np.zeros_like(snow)
    # 1. exterior snow: from each side, peel the leading snow run after transparency
    def peel(lines):
        for line in lines:
            open_ = True
            for (y, x) in line:
                if clear[y, x]:
                    open_ = True; continue
                if snow[y, x] and open_:
                    gone[y, x] = True; continue
                if open_ and not snow[y, x] and not gone[y, x]:
                    edge[y, x] = True
                open_ = False
    peel([[(y, x) for y in range(H)] for x in range(W)])              # from top
    peel([[(y, x) for x in range(W)] for y in range(H)])              # from left
    peel([[(y, x) for x in range(W - 1, -1, -1)] for y in range(H)])  # from right
    out[gone] = -1
    # outline only where we actually cut through snow (not on untouched edges)
    cut = np.zeros_like(edge)
    for y in range(H):
        for x in range(W):
            if edge[y, x]:
                for dy, dx in ((-1, 0), (0, -1), (0, 1)):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < H and 0 <= xx < W and gone[yy, xx]:
                        cut[y, x] = True
    out[cut] = outline
    # 2. interior snow: fill from below at even offsets, else above, else row-nearest
    inner = snow & ~gone
    src = (out >= 0).all(-1) & ~snow
    for y in range(H):
        for x in range(W):
            if not inner[y, x]:
                continue
            v = None
            for d in list(range(2, H, 2)) + [-d for d in range(2, H, 2)]:
                yy = y + d
                if 0 <= yy < H and src[yy, x]:
                    v = out[yy, x]; break
            if v is None:
                for d in range(1, W):
                    for xx in (x - d, x + d):
                        if 0 <= xx < W and src[y, xx]:
                            v = out[y, xx]; break
                    if v is not None: break
            out[y, x] = v if v is not None else -1
    return out


ROOF = [(176, 120, 168), (152, 96, 96), (136, 88, 104), (128, 80, 120), (96, 48, 80), (80, 48, 80)]
VALLEY = (80, 48, 80)


def desnow_roof(img, outline, protect=None, period=4, reach=14):
    """v2 -- row-wise. v1 peeled valley snow from the top (holes through the roof)
    and filled from far below (vertical streaks). Measured: shingles repeat weakly
    at 4 px (45% self-match), so fill copies the SAME ROW at multiples of 4."""
    out = img.copy(); H, W = img.shape[:2]
    snow = snow_mask(img, protect)
    roof = np.zeros_like(snow)
    for c in ROOF:
        roof |= (img == np.array(c)).all(-1)
    clear = ~(img >= 0).all(-1)
    done = np.zeros_like(snow)
    # 1. snow enclosed by roof on both sides in its row -> shingles from the same row
    for y in range(H):
        x = 0
        while x < W:
            if not snow[y, x]:
                x += 1; continue
            r = x
            while r + 1 < W and snow[y, r + 1]:
                r += 1
            left = next((xx for xx in range(x - 1, max(-1, x - reach), -1) if not snow[y, xx]), None)
            right = next((xx for xx in range(r + 1, min(W, r + reach)) if not snow[y, xx]), None)
            if left is not None and right is not None and roof[y, left] and roof[y, right]:
                for xx in range(x, r + 1):
                    v = None
                    for k in range(1, reach):
                        for sx in (xx - k * period, xx + k * period):
                            if 0 <= sx < W and roof[y, sx]:
                                v = img[y, sx]; break
                        if v is not None: break
                    out[y, xx] = v if v is not None else img[y, left]
                    done[y, xx] = True
                if r - x >= 2:                       # roof faces meet: draw the valley seam
                    out[y, (x + r) // 2] = VALLEY
            x = r + 1
    # 2. remaining snow touching open air above or beside it = caps/bulges -> remove
    rest = snow & ~done
    changed = True
    gone = np.zeros_like(snow)
    while changed:
        changed = False
        for y in range(H):
            for x in range(W):
                if rest[y, x] and not gone[y, x]:
                    for dy, dx in ((-1, 0), (0, -1), (0, 1)):
                        yy, xx = y + dy, x + dx
                        if not (0 <= yy < H and 0 <= xx < W) or clear[yy, xx] or gone[yy, xx]:
                            gone[y, x] = True; changed = True; break
    out[gone] = -1
    for y in range(H):                             # redraw outline where caps were cut away
        for x in range(W):
            if (out[y, x] >= 0).all() and not gone[y, x]:
                for dy, dx in ((-1, 0), (0, -1), (0, 1)):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < H and 0 <= xx < W and gone[yy, xx]:
                        out[y, x] = outline; break
    # 3. what is left (ledge snow) -> nearest material within 4 px: below, above, sideways
    left_over = snow & ~done & ~gone
    src = (out >= 0).all(-1) & ~snow
    for y, x in zip(*np.nonzero(left_over)):
        v = None
        for dy, dx in ((2, 0), (1, 0), (4, 0), (3, 0), (-2, 0), (-1, 0), (0, -1), (0, 1), (0, -2), (0, 2)):
            yy, xx = y + dy, x + dx
            if 0 <= yy < H and 0 <= xx < W and src[yy, xx]:
                v = out[yy, xx]; break
        out[y, x] = v if v is not None else -1
    return out
