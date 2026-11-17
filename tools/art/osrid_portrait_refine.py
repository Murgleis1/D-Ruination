"""Osrid portrait refinement (user 2026-11-17): "refine the existing portrait into something less
overtly layered/AI colored looking that fits the monomyth/ruination GBA aesthetic".

The same drawing, re-shaded the MonoMyth way (tools/art/MONOMYTH_TRAINER_STYLE.md and
assets/portrait_rework/PORTRAIT_REWORK.md). Measured faults of the current 80x80 portrait:
  * hair: 5 close tones (51,18,8 / 80,37,17 / 109,46,18 / 146,61,23 / 149,84,49) stacked in bands
    down every spike -> the "layered" look. Now 3 flat tones plus rim light on upper edges.
  * scarf/armour: 3 near-black greens (18,22,18 / 34,39,34 / 40,52,39) interleaved pixel by pixel
    -> noise and mud. Now mode-filtered into flat cel shapes on a ramp with real value steps.
  * glyph: anti-aliased with mid tones -> soft. Now crisp black line art.
  * mask: 4 creams -> 3 (shadow / base / highlight).
Usage: python3 -I osrid_portrait_refine.py IN.png OUT.png
"""
import sys
import numpy as np
from PIL import Image

# old index -> material, by the portrait's own palette (see the docstring)
BLACK = 6
HAIR = {10: 0, 7: 1, 9: 2, 3: 2, 11: 3}          # tone rank: 0 outline-dark, 1 dark, 2 mid, 3 skin
MASK = {4: 0, 2: 1, 14: 1, 13: 2}
CLOTH = {8: 0, 15: 1, 1: 2, 5: 3, 12: 4}         # 4 = strap brown

NEW = [
    (255, 0, 255),   # 0 transparent
    (10, 10, 12),    # 1 outline / glyph
    (74, 26, 12),    # 2 hair darkest (line inside the hair)
    (114, 42, 18),   # 3 hair dark
    (160, 64, 28),   # 4 hair mid
    (206, 104, 52),  # 5 hair light (rim)
    (176, 112, 78),  # 6 skin (ear)
    (178, 152, 112), # 7 mask shadow
    (226, 210, 170), # 8 mask
    (246, 238, 210), # 9 mask highlight
    (24, 34, 28),    # 10 cloth darkest
    (40, 58, 44),    # 11 scarf dark
    (62, 88, 62),    # 12 scarf mid
    (104, 96, 82),   # 13 armour light
    (92, 58, 36),    # 14 strap
    (70, 66, 60),    # 15 armour mid
]


def mode_filter(idx, sel, passes=2):
    out = idx.copy(); H, W = idx.shape
    for _ in range(passes):
        src = out.copy()
        for y in range(1, H - 1):
            for x in range(1, W - 1):
                if not sel[y, x]: continue
                win = src[y - 1:y + 2, x - 1:x + 2][sel[y - 1:y + 2, x - 1:x + 2]]
                vals, cnt = np.unique(win, return_counts=True)
                if cnt.max() >= 5:
                    out[y, x] = vals[np.argmax(cnt)]
    return out


def refine(a):
    H, W = a.shape
    out = np.zeros_like(a)
    # regions: the mask is the cream blob; the glyph is the dark pixels enclosed by it
    cream = np.isin(a, list(MASK))
    ys, xs = np.nonzero(cream)
    my0, my1, mx0, mx1 = ys.min(), ys.max(), xs.min(), xs.max()
    in_mask_box = np.zeros_like(cream)
    for y in range(my0, my1 + 1):
        row = np.nonzero(cream[y])[0]
        if len(row): in_mask_box[y, row.min():row.max() + 1] = True
    body = np.zeros_like(cream); body[54:] = True
    for y in range(H):
        for x in range(W):
            v = a[y, x]
            if v == 0: continue
            if v == BLACK: out[y, x] = 1; continue
            if in_mask_box[y, x] and not cream[y, x] and v not in HAIR:
                if v in (8, 15, 1):
                    # glyph strokes keep their two weights: core black, soft edge very dark
                    out[y, x] = 1 if v == 8 else 10
                else:                                        # anti-aliasing: black only on a stroke
                    nb = [a[y + dy, x + dx] for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1))]
                    n_dark = sum(n in (6, 8, 15, 1) for n in nb)
                    out[y, x] = 1 if n_dark >= 2 else 10 if n_dark == 1 else 7
                continue
            if v in MASK:
                t = MASK[v]
                if t == 2 and y >= my0 + 6:
                    t = 1                                    # highlight only on the brow plane
                out[y, x] = 7 + t; continue
            if v in HAIR and not body[y, x]:
                r = HAIR[v]
                out[y, x] = 6 if r == 3 else 2 + r
                continue
            if v in CLOTH or v in HAIR:
                r = CLOTH.get(v, 4)
                out[y, x] = {0: 10, 1: 11, 2: 12, 3: 13, 4: 14}[r]
                continue
            out[y, x] = 1
    # cloth: flatten the interleaved noise into cel shapes
    cloth = np.isin(out, [10, 11, 12, 13, 14, 15])
    out = mode_filter(out, cloth, passes=2)
    # armour plate (right of the scarf, where #5/#15 dominated): its dark green -> armour mid
    for y in range(54, H):
        for x in range(52, W):
            if out[y, x] == 11 and np.count_nonzero(out[max(54, y - 3):y + 4, max(0, x - 3):x + 4] == 13) >= 3:
                out[y, x] = 15
    # hair: flatten bands, then rim light on upper edges of mid-tone hair
    hair = np.isin(out, [2, 3, 4])
    out = mode_filter(out, hair, passes=1)
    for y in range(1, H):
        for x in range(W):
            if out[y, x] == 4 and out[y - 1, x] in (0, 1):
                out[y, x] = 5
                if y + 1 < H and out[y + 1, x] == 4 and x % 2 == 0:
                    out[y + 1, x] = 5
    # isolated pixels inside a material -> the material's majority (MonoMyth: no specks)
    for y in range(1, H - 1):
        for x in range(1, W - 1):
            v = out[y, x]
            if v in (0, 1): continue
            nb = [out[y - 1, x], out[y + 1, x], out[y, x - 1], out[y, x + 1]]
            if all(n != v for n in nb) and v not in (5, 9):
                vals, cnt = np.unique([n for n in nb if n not in (0, 1)], return_counts=True)
                if len(vals) and cnt.max() >= 3:
                    out[y, x] = vals[np.argmax(cnt)]
    # silhouette: every coloured pixel touching transparency becomes outline
    edge = np.zeros_like(cream)
    for y in range(H):
        for x in range(W):
            if out[y, x] not in (0, 1):
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < H and 0 <= nx < W and out[ny, nx] == 0:
                        edge[y, x] = True
    out[edge & (np.arange(H)[:, None] < H - 1)] = 1
    return out


if __name__ == '__main__':
    a = np.array(Image.open(sys.argv[1]))
    o = refine(a)
    img = Image.fromarray(o.astype(np.uint8), 'P')
    flat = [c for rgb in NEW for c in rgb]
    img.putpalette(flat + [0] * (768 - 48))
    img.save(sys.argv[2], transparency=0)
