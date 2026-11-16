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


def leaf_patch(wa_render):
    """A 16x16 all-foliage patch from Wood Avens' own art (green-dominant pixels only)."""
    import numpy as np
    a = wa_render
    best = None
    for y in range(0, a.shape[0] - 16, 4):
        for x in range(0, a.shape[1] - 16, 4):
            p = a[y:y + 16, x:x + 16]
            g = ((p[..., 1] > p[..., 0] + 20) & (p[..., 1] >= p[..., 2])).mean()
            k = len(np.unique(p.reshape(-1, 3), axis=0))
            if g == 1.0 and k >= 4:
                lum = p.mean()
                if best is None or lum < best[0]:
                    best = (lum, y, x)       # darkest: hedge/conifer greens read as ivy, not lawn
    _, y, x = best
    return a[y:y + 16, x:x + 16].copy(), (x, y)


def desnow_v3(img, outline, protect=None, mode='roof', leaves=None, period=4, ground_from=None, roof_patch=None):
    """v3: the user's call -- snow INSIDE the building's outline is roof (A) or
    roof-valleys + leaves on ledges (B). Only caps standing above the roofline go.

    inside  = snow with building pixels on BOTH sides in its row (anywhere in row)
    cap     = not inside, and open air directly above it (follows up through snow)
    ledge   = the rest (cornice/sill drifts)
    """
    out = img.copy(); H, W = img.shape[:2]
    snow = snow_mask(img, protect)
    solid = (img >= 0).all(-1) & ~snow
    roof = np.zeros_like(snow)
    for c in ROOF:
        roof |= (img == np.array(c)).all(-1)
    inside = np.zeros_like(snow); cap = np.zeros_like(snow)
    for y in range(H):
        xs = np.nonzero(solid[y])[0]
        if len(xs):
            l, r = xs.min(), xs.max()
            inside[y, l:r + 1] = snow[y, l:r + 1]
    for x in range(W):                      # caps: from the top, snow reached through air/snow only
        open_ = True
        for y in range(H):
            if not (img[y, x] >= 0).all():
                open_ = True; continue
            if snow[y, x] and open_ and not inside[y, x]:
                cap[y, x] = True; continue
            open_ = False
    # caps only where no roof sits beside them in the row (closes holes next to gables)
    for y, x in zip(*np.nonzero(cap)):
        if any(roof[y, xx] for xx in range(max(0, x - 3), min(W, x + 4))):
            cap[y, x] = False; inside[y, x] = True
    ground = np.zeros_like(snow)
    if ground_from is not None:                 # snow GROUND kept in this layer below the facade
        ground[ground_from:] = snow[ground_from:]
        inside &= ~ground; cap &= ~ground
    ledge = snow & ~inside & ~cap & ~ground
    def roof_fill(y, x):
        if roof_patch is not None:           # tile a clean 16x16 roof patch: no bars
            return roof_patch[y % 16, x % 16]
        for k in range(1, W):
            for sx in (x - k * period, x + k * period):
                if 0 <= sx < W and roof[y, sx]:
                    return img[y, sx]
        for d in range(1, H):                # no roof in this row: nearest roof above/below
            for yy in (y - d, y + d):
                if 0 <= yy < H and roof[yy, x]:
                    return img[yy, x]
        return None
    def near(y, x):
        # ledges are horizontal: continue the material along the ROW (vertical copy striped)
        for d in range(1, W):
            for xx in (x - d, x + d):
                if 0 <= xx < W and solid[y, xx]:
                    return out[y, xx]
        return None
    leaf_mode = mode == 'leaves' and leaves is not None
    for y, x in zip(*np.nonzero(inside)):
        # B keeps roof in the valleys; drifts sitting on stone/trim become leaves
        on_roof = any(roof[y, xx] for xx in range(max(0, x - 6), min(W, x + 7)))
        if leaf_mode and not on_roof:
            out[y, x] = leaves[y % 16, x % 16]
        else:
            v = roof_fill(y, x); out[y, x] = v if v is not None else -1
    for y, x in zip(*np.nonzero(ledge)):
        if leaf_mode:
            out[y, x] = leaves[y % 16, x % 16]
        else:
            v = near(y, x); out[y, x] = v if v is not None else -1
    out[cap] = -1
    out[ground] = -1
    # holes: a removed cap pixel that ends up with building on both sides of it in
    # its row (e.g. between a gable and a lower tower) is roof, not sky
    changed = True
    while changed:
        changed = False
        opaque = (out >= 0).all(-1)
        for y, x in zip(*np.nonzero(cap & ~opaque)):
            if opaque[y, :x].any() and opaque[y, x + 1:].any():
                v = roof_fill(y, x)
                if v is not None:
                    out[y, x] = v; changed = True
    for y in range(H):                        # redraw the outline where caps were removed
        for x in range(W):
            if (out[y, x] >= 0).all() and not cap[y, x] and y > 0 and cap[y - 1, x]:
                out[y, x] = outline
    return out


def desnow_building(mid, top, outline, protect, roof_until, ground_from, roof_patch=None, facade_leaves=None):
    """v3.3 -- two zones. Roof zone (rows < roof_until): inside snow -> shingles.
    Facade zone: snow -> the material beside it in its row (sill, cornice, wall),
    never roof. Holes are judged on the COMBINED mid+top (a gap only shows if both
    layers are empty) and filled in the mid layer."""
    H, W = mid.shape[:2]
    res = []
    for img in (mid, top):
        out = img.copy()
        roofz = desnow_v3(img, outline, protect, 'roof', ground_from=ground_from, roof_patch=roof_patch)
        out[:roof_until] = roofz[:roof_until]
        # facade zone: row-wise nearest non-snow material
        snow = snow_mask(img, protect)
        solid = (img >= 0).all(-1) & ~snow
        for y in range(roof_until, H):
            for x in np.nonzero(snow[y])[0]:
                if y >= ground_from:
                    out[y, x] = -1; continue
                if facade_leaves is not None:          # user's idea: drifts on ledges become ivy
                    out[y, x] = facade_leaves[y % 16, x % 16]; continue
                v = None
                for d in range(1, W):
                    for xx in (x - d, x + d):
                        if 0 <= xx < W and solid[y, xx]:
                            v = img[y, xx]; break
                    if v is not None: break
                out[y, x] = v if v is not None else -1
        res.append(out)
    mid2, top2 = res
    # holes on the composite: transparent in both layers, building on both sides in
    # the row and below in the column, and it was snow in the source -> fill in mid
    was_snow = snow_mask(mid, protect) | snow_mask(top, protect)
    roof = np.zeros(mid.shape[:2], bool)
    for c in ROOF:
        roof |= (mid == np.array(c)).all(-1) | (top == np.array(c)).all(-1)
    comp = np.where((top2 >= 0).all(-1)[..., None], top2, mid2)
    for _ in range(4):
        op = (comp >= 0).all(-1)
        for y in range(ground_from):
            for x in range(W):
                if op[y, x] or not was_snow[y, x]: continue
                if op[y, :x].any() and op[y, x + 1:].any() and op[y + 1:ground_from, x].any():
                    v = None
                    if y < roof_until and roof_patch is not None:
                        v = roof_patch[y % 16, x % 16]
                    elif y < roof_until:
                        for k in range(1, W // 4 + 1):
                            for sx in (x - 4 * k, x + 4 * k):
                                if 0 <= sx < W and roof[y, sx]:
                                    v = comp[y, sx]; break
                            if v is not None: break
                    if v is None:
                        for d in range(1, W):
                            for xx in (x - d, x + d):
                                if 0 <= xx < W and op[y, xx]:
                                    v = comp[y, xx]; break
                            if v is not None: break
                    mid2[y, x] = v; comp[y, x] = v
    return mid2, top2


def clean_roof_patch(layers, size=16):
    """The size x size window that is 100% roof colours with the most colour variety.
    Measured on the Elderflower lodge: no 16x16 pure-roof window exists (outlines and
    windows intrude), so callers fall back to 8."""
    best = None
    for img in layers:
        rm = np.zeros(img.shape[:2], bool)
        for c in ROOF:
            rm |= (img == np.array(c)).all(-1)
        for y in range(0, img.shape[0] - size + 1, 1):
            for x in range(0, img.shape[1] - size + 1, 1):
                if rm[y:y + size, x:x + size].all():
                    k = len(np.unique(img[y:y + size, x:x + size].reshape(-1, 3), axis=0))
                    if best is None or k > best[0]:
                        p = img[y:y + size, x:x + size].copy()
                        if size < 16:
                            p = np.tile(p, (16 // size, 16 // size, 1))
                        best = (k, p, (x, y))
    return best


def patch_from_above(mid, top, src_mid, src_top, box, shift=16, protect=None):
    """Hand-directed repair: inside box (x0, y0, x1, y1), replace pixels that were
    SNOW in the source with the same roof face's real shingles `shift` rows above.
    Used for the tavern's right lower roof, where row-copy fill left vertical bars."""
    x0, y0, x1, y1 = box
    was = snow_mask(src_mid, protect) | snow_mask(src_top, protect)
    roof = np.zeros(mid.shape[:2], bool)
    comp = np.where((top >= 0).all(-1)[..., None], top, mid)
    for c in ROOF:
        roof |= (comp == np.array(c)).all(-1)
    mid = mid.copy()
    for y in range(y0, y1):
        for x in range(x0, x1):
            if was[y, x] and roof[y - shift, x] and not (top[y, x] >= 0).all():
                mid[y, x] = comp[y - shift, x]
    return mid
