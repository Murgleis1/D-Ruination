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


def rebuild(path):
    rgba = np.array(Image.open(path).convert('RGBA'))
    mask = rgba[..., 3] >= ALPHA; rgb = rgba[..., :3].astype(int)
    pal = palette15(rgb, mask)
    idx = to_index(rgb, mask, pal)
    small = despeckle(outline(downscale_32(idx, pal), pal))
    canvas = np.zeros((OUT, OUT), np.uint8)
    h, w = small.shape; y0 = OUT - h; x0 = (OUT - w) // 2
    canvas[y0:y0 + h, x0:x0 + w] = np.where(small >= 0, small + 1, 0)
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
