"""Rebuild the project's own portraits as MonoMyth-scale busts (user 2026-11-16: "Rebuild the
portraits please" -- after v2 showed our face close-ups read as square panels in game).

Per portrait (96x96 RGBA master -> 80x80, 16 colours, index 0 transparent):
  1. palette  = the master's own 15 colours (accent-preserving pick, portrait_adapt.palette15):
                the rebuild never invents a colour the artist didn't use.
  2. scale    = 2/3 (96 -> 64): every output pixel is the 3:2 block's dominant palette colour
                (vote by area, ties to the darker colour so lines survive) -- no blended colours.
  3. outline  = 1px dark outline around the silhouette, as MonoMyth's busts have.
  4. cleanup  = lone pixels (no same-colour 4-neighbour, majority of 8 differ) take the majority.
  5. framing  = bottom-aligned (cut flat under the text box edge), centred, transparent around.
Run: python3 -I portrait_rebuild.py SRC_DIR OUT_DIR [--preview sheet.png]
"""
import os, sys, glob
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from portrait_adapt import palette15, save, ALPHA

OUT, BODY = 80, 64


def to_index(rgb, mask, pal):
    idx = np.zeros(mask.shape, np.int16) - 1
    d = ((rgb[mask][:, None, :].astype(int) - pal[None]) ** 2).sum(-1)
    idx[mask] = np.argmin(d, 1)
    return idx                                            # -1 transparent, 0..14 palette


def downscale_32(idx, pal):
    H, W = idx.shape; h, w = H * 2 // 3, W * 2 // 3
    lum = pal.sum(1)
    out = np.full((h, w), -1, np.int16)
    for oy in range(h):
        for ox in range(w):
            # output pixel covers source [oy*1.5, oy*1.5+1.5) -- weights per source pixel
            y0, x0 = oy * 1.5, ox * 1.5
            votes = {}
            for sy in range(int(y0), int(np.ceil(y0 + 1.5))):
                wy = min(sy + 1, y0 + 1.5) - max(sy, y0)
                for sx in range(int(x0), int(np.ceil(x0 + 1.5))):
                    wx = min(sx + 1, x0 + 1.5) - max(sx, x0)
                    if wy <= 0 or wx <= 0: continue
                    v = int(idx[sy, sx]); votes[v] = votes.get(v, 0) + wy * wx
            if votes.get(-1, 0) >= 1.125: continue        # mostly transparent
            votes.pop(-1, None)
            best = max(votes.items(), key=lambda kv: (round(kv[1], 3), -lum[kv[0]]))
            out[oy, ox] = best[0]
    return out


NATIVE = os.environ.get('PORTRAIT_SCALE', 'native') == 'native'


def downscale_2x(idx, pal):
    """The masters are 2x enlargements of 48x48 pixel art (measured: Ambrose, Eden, Glaive, Kimaris
    exact 2x2 blocks; Baradus/Cadmus all but ~40-80 single pixels from detail edits at 96px). Halving
    by 2x2 block returns the artist's ORIGINAL pixels exactly -- no uneven 1.33x pixel widths.
    Mixed blocks (the edits) take the block's darkest opaque colour so added details survive."""
    H, W = idx.shape; lum = pal.sum(1)
    out = np.full((H // 2, W // 2), -1, np.int16)
    for y in range(H // 2):
        for x in range(W // 2):
            b = idx[2 * y:2 * y + 2, 2 * x:2 * x + 2].ravel()
            op = b[b >= 0]
            if len(op) < 2: continue
            vals, cnt = np.unique(op, return_counts=True)
            out[y, x] = vals[np.argmax(cnt)] if cnt.max() >= 3 else min(op, key=lambda v: lum[v])
    return out


def outline(img, pal):
    # darkest NEUTRAL colour (low saturation): a dark red scarf must not become everyone's outline
    sat = pal.max(1) - pal.min(1)
    neutral = [i for i in range(len(pal)) if sat[i] <= 40] or list(range(len(pal)))
    dark = min(neutral, key=lambda i: int(pal[i].sum()))
    op = img >= 0; out = img.copy()
    H, W = img.shape
    for y in range(H):
        for x in range(W):
            if not op[y, x]: continue
            for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                yy, xx = y + dy, x + dx
                if 0 <= yy < H and 0 <= xx < W and not op[yy, xx] and yy < H - 1:
                    out[y, x] = dark; break
    return out


def despeckle(img):
    out = img.copy(); H, W = img.shape
    for y in range(1, H - 1):
        for x in range(1, W - 1):
            c = img[y, x]
            if c < 0: continue
            n4 = [img[y - 1, x], img[y + 1, x], img[y, x - 1], img[y, x + 1]]
            if c in n4: continue
            n8 = [img[y + dy, x + dx] for dy in (-1, 0, 1) for dx in (-1, 0, 1) if dy or dx]
            vals, cnt = np.unique(n8, return_counts=True)
            m = vals[np.argmax(cnt)]
            if cnt.max() >= 5 and m >= 0: out[y, x] = m
    return out


def crown(img, top, flat=False):
    """Close the hair cut by the masters' top edge (16-56 opaque px on row 0, all but Osrid) by
    CONTINUING THE HEAD'S OWN CURVE. History (all rejected on screen by the user): per-segment domes
    (lumps), one ellipse on the cut (pinch -> lump), slope continuation (peaks). Measured on the
    masters: the outline is already curving at the cut (Eden narrows ~1.3 px/row/side). So the
    half-width below the cut is fitted as an ellipse -- hw^2 = A + B*y + C*y^2 (C < 0) over the 9
    rows under the cut, centre from the same rows -- and extended upward until it closes: the
    crown has the head's own curvature, round, no pinch, no peak. Fill: the hair rows mirrored
    upward, the cut's dominant hair colours only; existing art is never overwritten."""
    out = img.copy(); H, W = img.shape
    ys, hws, cs = [], [], []
    for y in range(top, min(top + 9, H)):
        xs = np.nonzero(img[y] >= 0)[0]
        if len(xs) < 2: continue
        ys.append(y); hws.append((xs.max() - xs.min() + 1) / 2.0); cs.append((xs.max() + xs.min()) / 2.0)
    if len(ys) < 4: return out
    ys = np.array(ys, float); hw2 = np.array(hws) ** 2
    A, B, C = np.polyfit(ys - top, hw2, 2)[::-1]
    if C >= -0.02:                                   # straight/diverging sides: close as a half-circle
        C = -A / max(1.0, hws[0]) ** 2
    if flat:                                         # hats: a low, flat-topped close (3 rows)
        A, B, C = hws[0] ** 2, 0.0, -(hws[0] ** 2) / 9.0
    cx = float(np.mean(cs[:4]))
    band = img[top:top + 4].ravel(); band = band[band >= 0]
    vals, cnt = np.unique(band, return_counts=True)
    hair = [int(v) for v, c in sorted(zip(vals, cnt), key=lambda t: -t[1]) if c >= 0.10 * cnt.sum()]
    for r in range(1, top + 1):
        t = -r
        h2 = A + B * t + C * t * t
        if h2 <= 0.25: break
        half = np.sqrt(h2); y = top - r
        for x in range(int(np.ceil(cx - half - 0.25)), int(np.floor(cx + half + 0.25)) + 1):
            if not (0 <= x < W) or out[y, x] >= 0: continue
            src = img[min(top + r - 1, H - 1), x]
            if src < 0 or src not in hair:
                src = img[top, x] if 0 <= x < W and img[top, x] in hair else hair[0]
            out[y, x] = src
    return out


# Lore recolours applied to the master before anything else (user 2026-11-16): Baradus is of the
# Yo'aki tribe -- bronzed, darker skin. His masters' 7-step skin ramp -> a bronze ramp, same ranks.
RECOLOUR = {'baradus': {
    (255, 214, 189): (196, 136, 92), (254, 213, 187): (196, 136, 92),
    (223, 167, 126): (164, 106, 66), (222, 165, 123): (164, 106, 66),
    (189, 113, 87): (134, 80, 52), (176, 108, 84): (124, 74, 48),
    (144, 80, 56): (100, 58, 38), (123, 90, 70): (92, 62, 46), (112, 58, 37): (76, 42, 28),
}}

# ---------------------------------------------------------------------------------------------
# Master-level edits (96px, before scaling; the masters are 2x art, so edits use 2x2 blocks)

BRONZE_SKIN = {(196, 136, 92), (164, 106, 66), (134, 80, 52), (124, 74, 48), (100, 58, 38),
               (92, 62, 46), (76, 42, 28)}


def baradus_facial_hair(rgb, mask):
    """User 2026-11-16: Baradus "too clean shaven ... more dangerous"; reference MonoMyth #351.
    Rejected before: filled areas, a painted wedge, black strands drawn up from the jaw (read as a
    slash from mouth to jaw).  How #351 is actually built (pixel study): the beard is the JAW OUTLINE
    itself grown thick -- a solid dark band along the bottom of the chin (2 rows), above it a row of
    vertical strands (dark/skin alternating), above that a few staggered flecks; it thins to the
    outline alone up the jaw sides; the moustache is a mid-shadow SKIN tone band above the mouth,
    not black.  Colours: the beard is his hair black, the moustache his jaw-shadow brown -- no new
    palette entries.  Drawn on the native 48px grid (masters are 2x).  Native jaw (identical in all
    three expressions): left edge (12,35)(13,36)(14,37)(15-16,38)(17-18,39), chin (19-22,40), right
    edge (23-24,39)(25-26,38)(27-28,37)(29-30,36)(31,35); mouth row 33."""
    HAIR = (0, 0, 0)        # the beard is his hair black.  User 2026-11-16: keep the chin beard, but
    # his mouth and nose stay exactly as drawn (moustache rejected) -- nothing above row 35 is edited
    H, W = mask.shape
    skin = np.zeros((H, W), bool)
    for c in BRONZE_SKIN: skin |= mask & (rgb == c).all(-1)
    out = rgb.copy()
    def px(x, y, c):
        if skin[2 * y, 2 * x]: out[2 * y:2 * y + 2, 2 * x:2 * x + 2] = c
    # #351's proportions, mouth-to-chin both 8 rows: 2 solid rows at the bottom, 2 rows mostly dark
    # with skin gaps (strands), 1 row of flecks, filling the whole chin V across its width.
    rows = {40: (range(19, 23), ()),
            39: (range(17, 25), ()),
            38: (range(15, 27), (18, 23)),
            37: (range(14, 29), (16, 19, 21, 24, 26)),
            36: ((13, 15, 18, 22, 25, 27, 29, 30), ()),
            35: ((12, 31), ()),
            34: ((32,), ())}
    for y, (xs, gaps) in rows.items():
        for x in xs:
            if x not in gaps: px(x, y, HAIR)
    return out


def complete_sides(rgba, pad):
    """Art cut by the master's LEFT/RIGHT frame edge (Cadmus's hat brim; hair on Eden, Glaive)
    continues outward: every run of rows touching an edge gets a rounded tip (elliptical profile,
    up to 45% of the run's height), filled with the art's own columns mirrored at the edge."""
    H, W = rgba.shape[:2]
    op = rgba[..., 3] >= ALPHA
    for side in ('L', 'R'):
        ex = pad if side == 'L' else W - pad - 1           # the original frame edge column
        rows = [y for y in range(H) if op[y, ex]]
        runs, cur = [], []
        for y in rows:
            if cur and y != cur[-1] + 1: runs.append(cur); cur = []
            cur.append(y)
        if cur: runs.append(cur)
        for run in runs:
            if len(run) < 3: continue
            y0, y1 = run[0], run[-1]; yc = (y0 + y1) / 2.0; hr = (y1 - y0 + 1) / 2.0
            L = min(pad, 0.45 * (y1 - y0 + 1))
            for y in run:
                k = int(round(L * np.sqrt(max(0.0, 1 - ((y - yc) / (hr + 0.5)) ** 2))))
                for i in range(1, k + 1):
                    sx = ex + i if side == 'L' else ex - i     # mirror source inside the art
                    tx = ex - i if side == 'L' else ex + i
                    if 0 <= tx < W and 0 <= sx < W and op[y, sx]:
                        rgba[y, tx] = rgba[y, sx]
    return rgba


MASTER_EDITS = {'baradus': baradus_facial_hair}
# User 2026-11-16: the collar flap rising beside Baradus's chin "runs into his neck too much" -- trim
# it down; the outline step then borders the new top edge.  Native px cleared (collar only, never
# skin): the flap's peak rows 36-37, row 38 from x9, row 39 from x13, row 40 from x16 -- the new top
# edge steps down from the shoulder (row 38) to row 41 at the neck.
MASTER_TRIM = {'baradus': [(x, y) for y, x0 in ((36, 0), (37, 0), (38, 9), (39, 13), (40, 16))
                           for x in range(x0, 19)]}
# what the trimmed flap uncovers: under the jaw it is the shadowed side of his neck (jaw-shadow
# brown), outside his silhouette it is background
TRIM_FILL = {'baradus': ((100, 58, 38), lambda x, y: y >= 39 and x >= 15)}
CROWN_FLAT = ('cadmus',)          # a hat crown closes flat with rounded corners, not a dome


def rebuild(path, edits=True, _inner=False):
    name = os.path.basename(path)
    if edits and not _inner and any(name.startswith(n) for n in list(MASTER_EDITS) + list(MASTER_TRIM)):
        return protect(path)
    PAD = 12
    raw = np.array(Image.open(path).convert('RGBA'))
    # lore recolour + drawn edits on the UNPADDED master (their coordinates are the master's own)
    rrgb = raw[..., :3].astype(int); rmask = raw[..., 3] >= ALPHA
    for n, table in RECOLOUR.items():
        if name.startswith(n):
            for a, b in table.items(): rrgb[(rrgb == a).all(-1)] = b
    pre_edit = rrgb.copy()                               # after the lore recolour, before drawn edits
    for n, fn in MASTER_EDITS.items():
        if edits and name.startswith(n): rrgb = fn(rrgb, rmask)
    raw = raw.copy(); raw[..., :3] = np.clip(rrgb, 0, 255)
    edited = (rrgb != np.array(Image.open(path).convert('RGBA'))[..., :3]).any(-1)
    raw[edited, 3] = 255                                 # beard below the chin is opaque art
    trimmed = np.zeros(rmask.shape, bool)
    for n, pts in MASTER_TRIM.items():
        if edits and name.startswith(n):
            skin = np.zeros(rmask.shape, bool)
            for c in BRONZE_SKIN: skin |= (pre_edit == c).all(-1)    # beard px are skin, not collar
            for x, y in pts:
                blk = (slice(2 * y, 2 * y + 2), slice(2 * x, 2 * x + 2))
                if skin[blk].any(): continue
                trimmed[blk] = True
                col, inside = TRIM_FILL.get(n, (None, lambda x, y: False))
                if inside(x, y): raw[blk + (slice(0, 3),)] = col; raw[blk + (3,)] = 255
                else: raw[blk + (3,)] = 0
    global LAST_FOOTPRINT
    LAST_FOOTPRINT = ((rrgb != pre_edit).any(-1), trimmed, PAD)   # drawn edits only, not the recolour
    rgba = np.zeros((raw.shape[0], raw.shape[1] + 2 * PAD, 4), np.uint8); rgba[:, PAD:PAD + raw.shape[1]] = raw
    rgba = complete_sides(rgba, PAD)
    mask = rgba[..., 3] >= ALPHA; rgb = rgba[..., :3].astype(int)
    pal = palette15(rgb, mask)
    idx = to_index(rgb, mask, pal)
    small = downscale_2x(idx, pal) if NATIVE else downscale_32(idx, pal)
    big = np.full((OUT, OUT), -1, np.int16)
    h, w = small.shape; y0 = OUT - h; x0 = (OUT - w) // 2
    big[y0:y0 + h, x0:x0 + w] = small
    big = crown(big, y0, flat=name.startswith(CROWN_FLAT))
    big = despeckle(outline(big, pal))
    canvas = np.where(big >= 0, big + 1, 0).astype(np.uint8)
    full = np.zeros((16, 3), int); full[0] = (255, 0, 255); full[1:1 + len(pal)] = pal
    return canvas, full.astype(np.uint8)


def protect(path):
    """Drawn edits may change ONLY their own pixels (+ the border the outline step puts on a trimmed
    edge).  Rebuilding re-picks the palette and re-runs despeckle, which nudged untouched pixels next
    to the beard (Baradus's lower lip, 2026-11-16).  Every pixel outside the footprint is restored
    from the unedited build, mapped to the nearest colour of the edited build's palette."""
    base_idx, base_pal = rebuild(path, edits=False)
    idx, pal = rebuild(path, edits=True, _inner=True)
    edited, trimmed, pad = LAST_FOOTPRINT
    H, W = edited.shape
    fp = np.zeros((H, W + 2 * pad), bool)
    fp[:, pad:pad + W] = edited
    tr = np.zeros_like(fp); tr[:, pad:pad + W] = trimmed
    for _ in range(3):                                   # trimmed edge + its new border (master px)
        g = tr.copy(); g[1:] |= tr[:-1]; g[:-1] |= tr[1:]; g[:, 1:] |= tr[:, :-1]; g[:, :-1] |= tr[:, 1:]; tr = g
    fp |= tr
    s = 2.0 if NATIVE else 1.5
    h = int(H / s); w = int((W + 2 * pad) / s); y0 = OUT - h; x0 = (OUT - w) // 2
    out = idx.copy()
    for cy in range(OUT):
        for cx in range(OUT):
            sy, sx = cy - y0, cx - x0
            if 0 <= sy < h and 0 <= sx < w:
                a, b = int(np.floor(sy * s)), int(np.ceil((sy + 1) * s))
                c, d = int(np.floor(sx * s)), int(np.ceil((sx + 1) * s))
                if fp[a:b, c:d].any(): continue
            v = base_idx[cy, cx]
            if v == 0: out[cy, cx] = 0
            else:
                col = base_pal[v].astype(int)
                out[cy, cx] = 1 + int(np.argmin(((pal[1:].astype(int) - col) ** 2).sum(1)))
    return out, pal


if __name__ == '__main__':
    src, od = sys.argv[1], sys.argv[2]; os.makedirs(od, exist_ok=True)
    res = []
    for f in sorted(glob.glob(os.path.join(src, '*.png'))):
        idx, pal = rebuild(f); save(idx, pal, os.path.join(od, os.path.basename(f))); res.append((f, idx, pal))
    if '--preview' in sys.argv:
        from PIL import ImageDraw
        S, cols = 3, 4; CW = 96 * S + 80 * S + 16; H = 96 * S + 16
        sheet = Image.new('RGB', (cols * CW, ((len(res) + cols - 1) // cols) * H), (30, 30, 30)); dr = ImageDraw.Draw(sheet)
        for k, (f, idx, pal) in enumerate(res):
            x = (k % cols) * CW; y = (k // cols) * H
            o = Image.open(f).convert('RGBA'); bg = Image.new('RGBA', o.size, (110, 110, 130, 255)); bg.alpha_composite(o)
            sheet.paste(bg.convert('RGB').resize((96 * S, 96 * S), Image.NEAREST), (x, y + 14))
            rgb = pal[idx]; rgb[idx == 0] = (110, 110, 130)
            sheet.paste(Image.fromarray(rgb).resize((80 * S, 80 * S), Image.NEAREST), (x + 96 * S + 6, y + 14 + 16 * S))
            dr.text((x, y), os.path.basename(f)[:-4], fill=(255, 255, 0))
        sheet.save(sys.argv[sys.argv.index('--preview') + 1])
