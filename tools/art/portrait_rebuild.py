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


def crown(img, top):
    """The masters' hair runs off the top of their frame (16-56 opaque px on row 0, all but Osrid).
    v4 capped each cut segment with its own dome, v5 one elliptical dome per head: both read as a
    LUMP (user, twice) -- an ellipse leaves its base with VERTICAL sides, so where it meets the
    head's sloping outline the silhouette pinches in. Now the cap CONTINUES the outline: each side
    keeps the slope the head's edge has over the rows below the cut, plus a gentle quadratic
    rounding that closes the top -- the outline is smooth (no pinch, no shoulder) by construction.
    Fill: the hair rows mirrored upward, the cut's dominant hair colours only; existing art is never
    overwritten."""
    out = img.copy()
    H, W = img.shape
    def edges(y):
        xs = np.nonzero(img[y] >= 0)[0]
        return (int(xs.min()), int(xs.max())) if len(xs) else None
    e0 = edges(top)
    if e0 is None or e0[1] - e0[0] < 2: return out
    k = 4
    ek = edges(top + k) or e0
    dl = max(0.0, (e0[0] - ek[0]) / k)      # going up, the left edge moves right by dl per row
    dr = max(0.0, (ek[1] - e0[1]) / k)      # ... and the right edge moves left by dr per row
    w0 = e0[1] - e0[0] + 1
    h = int(min(top, max(2, round(0.45 * w0 / 2))))
    a = max(0.08, (w0 - (dl + dr) * h) / (2.0 * h * h))
    band = img[top:top + 4, e0[0]:e0[1] + 1].ravel(); band = band[band >= 0]
    vals, cnt = np.unique(band, return_counts=True)
    hair = [int(v) for v, c in sorted(zip(vals, cnt), key=lambda t: -t[1]) if c >= 0.10 * cnt.sum()]
    for r in range(1, top + 1):
        left = e0[0] + dl * r + a * r * r; right = e0[1] - dr * r - a * r * r
        if right < left: break
        y = top - r
        for x in range(int(np.ceil(left - 0.25)), int(np.floor(right + 0.25)) + 1):
            if out[y, x] >= 0: continue
            src = img[min(top + r - 1, H - 1), x]
            if src < 0 or src not in hair:
                src = img[top, x] if img[top, x] in hair else hair[0]
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


def rebuild(path):
    rgba = np.array(Image.open(path).convert('RGBA'))
    mask = rgba[..., 3] >= ALPHA; rgb = rgba[..., :3].astype(int)
    for name, table in RECOLOUR.items():
        if os.path.basename(path).startswith(name):
            for a, b in table.items(): rgb[(rgb == a).all(-1)] = b
    pal = palette15(rgb, mask)
    idx = to_index(rgb, mask, pal)
    small = downscale_32(idx, pal)
    big = np.full((OUT, OUT), -1, np.int16)
    h, w = small.shape; y0 = OUT - h; x0 = (OUT - w) // 2
    big[y0:y0 + h, x0:x0 + w] = small
    big = crown(big, y0)
    big = despeckle(outline(big, pal))
    canvas = np.where(big >= 0, big + 1, 0).astype(np.uint8)
    full = np.zeros((16, 3), int); full[0] = (255, 0, 255); full[1:1 + len(pal)] = pal
    return canvas, full.astype(np.uint8)


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
