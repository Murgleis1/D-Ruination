"""Cut furniture out of a rendered source room (16 px cells). A pixel is see-through where it equals one of the
room's plain reference cells at the same position (its floor, its wall row), or, where given, has one of a set of
background colours (for walls with no plain cell); see-through patches enclosed by the piece are filled back in
(they are the piece's own pixels that happen to match the floor). clear: boxes (x0,y0,x1,y1, piece pixels) forced
see-through. Returns RGBA (int)."""
import numpy as np
from PIL import Image
from scipy.ndimage import label
T = 16

def load(path):
    return np.array(Image.open(path).convert('RGB')).astype(int)

def cell(a, x, y):
    return a[y * T:(y + 1) * T, x * T:(x + 1) * T]

def cut(a, x0, y0, w, h, refs, bgcols=None, clear=(), fill_holes=True):
    out = np.zeros((h * T, w * T, 4), int)
    out[..., :3] = a[y0 * T:(y0 + h) * T, x0 * T:(x0 + w) * T]
    see = np.zeros((h * T, w * T), bool)
    for j in range(h):
        for i in range(w):
            c = out[j * T:(j + 1) * T, i * T:(i + 1) * T, :3]
            for (rx, ry) in refs:
                see[j * T:(j + 1) * T, i * T:(i + 1) * T] |= (c == cell(a, rx, ry)).all(-1)
    if bgcols:
        for (row, cols) in bgcols:            # (source row, set of colours) for walls with no plain cell
            j = row - y0
            if 0 <= j < h:
                band = out[j * T:(j + 1) * T, :, :3]
                see[j * T:(j + 1) * T] |= np.array([[tuple(p) in cols for p in r] for r in band])
    for (cx0, cy0, cx1, cy1) in clear: see[cy0:cy1, cx0:cx1] = True
    out[..., 3] = np.where(see, 0, 255)
    if fill_holes:
        lb, n = label(see)
        edge = set(lb[0]) | set(lb[-1]) | set(lb[:, 0]) | set(lb[:, -1])
        for k in range(1, n + 1):
            if k not in edge and k: out[lb == k, 3] = 255
        for (cx0, cy0, cx1, cy1) in clear: out[cy0:cy1, cx0:cx1, 3] = 0
    return out

def show(pieces, out, scale=4):
    W = sum(p.shape[1] for p in pieces) + 8 * len(pieces); H = max(p.shape[0] for p in pieces)
    im = Image.new('RGBA', (W, H), (255, 0, 255, 255)); x = 0
    for p in pieces:
        im.alpha_composite(Image.fromarray(p.astype(np.uint8)), (x, 0)); x += p.shape[1] + 8
    im.resize((W * scale, H * scale), Image.NEAREST).save(out)
