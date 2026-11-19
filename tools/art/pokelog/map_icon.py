"""Region-map "you are here" icon: Rufflet's face, the symbol of Cormorian royalty (user 2026-11-18).

    python3 tools/art/pokelog/map_icon.py     # writes brendan_icon.png / may_icon.png (32x32, 4bpp)

Source: the user's pixel art, assets/region_map/rufflet_face_source.png (a 27x35 sprite shown at ~20.5x).
The art is not redrawn: its pixel grid is sampled back to 27x35, the top 3 px of the crest tip trimmed,
colours reduced to 15 (k-means over the art's own pixels), then box-resampled to 20 px tall (user's
choice of size), outlined with the art's darkest colour, and the two eye pixels set white (user).
It sits centred in a 32x32 sprite (src/region_map.c: sRegionMapPlayerIconOam is 32x32)."""
import os
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SRC = os.path.join(REPO, 'assets', 'region_map', 'rufflet_face_source.png')
CELL, OFF, TRIM_TOP, HEIGHT = 20.5, 19.0, 3, 20
EYES = [(14, 6), (14, 10)]           # (row, col) in the 20-px art: the only black pixels inside the mask

def native():
    im = np.asarray(Image.open(SRC).convert('RGB')).astype(int)
    n = int((im.shape[1] - OFF) // CELL); nat = np.zeros((n, n, 3), np.uint8)
    for j in range(n):
        for i in range(n):
            y = int(OFF + (j + .5) * CELL); x = int(OFF + (i + .5) * CELL)
            nat[j, i] = np.median(im[y - 4:y + 5, x - 4:x + 5].reshape(-1, 3), 0)
    m = np.abs(nat.astype(int) - nat[0, 0].astype(int)).sum(-1) > 40
    ys, xs = np.where(m)
    return nat[ys.min():ys.max() + 1, xs.min():xs.max() + 1], m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]

def palette(art, am):
    px = art[am].reshape(-1, 3).astype(float); rng = np.random.default_rng(1)
    C = px[rng.choice(len(px), 15, replace=False)]
    for _ in range(60):
        a = ((px[:, None] - C[None]) ** 2).sum(-1).argmin(1)
        for k in range(15):
            if (a == k).any(): C[k] = px[a == k].mean(0)
    return np.clip(np.round(C / 8) * 8, 0, 248).astype(np.uint8)

def icon():
    nat, m = native(); art, am = nat[TRIM_TOP:], m[TRIM_TOP:]
    C = palette(art, am)
    w = round(art.shape[1] * HEIGHT / art.shape[0])
    rgba = np.dstack([art, am.astype(np.uint8) * 255])
    sm = np.asarray(Image.fromarray(rgba, 'RGBA').resize((w, HEIGHT), Image.BOX)).astype(float)
    idx = ((sm[..., None, :3] - C[None, None].astype(float)) ** 2).sum(-1).argmin(-1); idx[sm[..., 3] <= 128] = -1
    dark = int(np.argmin(C.astype(int).sum(1))); white = int(np.argmax(C.astype(int).sum(1)))
    f = idx >= 0; p = np.pad(f, 1); edge = f & ~(p[:-2, 1:-1] & p[2:, 1:-1] & p[1:-1, :-2] & p[1:-1, 2:]); idx[edge] = dark
    for r, c in EYES:
        assert idx[r, c] == dark, 'eye pixel moved: re-check EYES'
        idx[r, c] = white
    out = np.zeros((32, 32), np.uint8)                          # 0 = transparent; palette shifted by 1
    y0, x0 = (32 - HEIGHT) // 2, (32 - w) // 2
    out[y0:y0 + HEIGHT, x0:x0 + w] = np.where(idx >= 0, idx + 1, 0)
    return out, C

def save_png(path):
    out, C = icon(); pal = [0, 0, 0] + [int(v) for c in C for v in c]
    im = Image.fromarray(out, 'P'); im.putpalette(pal + [0] * (48 - len(pal))); im.save(path, transparency=0)

if __name__ == '__main__':
    for n in ('brendan_icon', 'may_icon'):
        save_png(os.path.join(REPO, 'codebase', 'graphics', 'pokenav', 'region_map', f'{n}.png'))
    out, C = icon(); pal = np.vstack([[120, 160, 110], C]).astype(np.uint8)
    Image.fromarray(pal[out]).resize((256, 256), Image.NEAREST).save('/tmp/rufflet_icon.png'); print('ok')
