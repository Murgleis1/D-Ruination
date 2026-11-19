"""Cut furniture out of MonoMyth maps by layer: a MonoMyth metatile is triple-layer and its furniture sits on the
middle/top layers over a floor (or wall) on the bottom layer, so a piece = layers 1-2 of a rectangle of cells.
Usage: python3 tools/monomyth/mm_pieces.py  (writes assets/monomyth_reference/pieces/<name>.png, RGBA)
"""
import os, sys, struct
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from romlib import u32, off, layout
from render import TS, map_cells, ROM

def cut(header, x0, y0, w, h, layers=(1, 2)):
    L = layout(u32(off(header))); ts = TS(L); c = map_cells(L); W = L['w']
    rgba = np.zeros((h * 16, w * 16, 4), np.uint8)
    for dy in range(h):
        for dx in range(w):
            m = c[(y0 + dy) * W + x0 + dx] & 0x3FF
            base = off(L['primary']['mt']) + 24 * m if m < 512 else off(L['secondary']['mt']) + 24 * (m - 512)
            e = struct.unpack_from('<12H', ROM, base)
            for layer in layers:
                for q in range(4):
                    v = e[layer * 4 + q]; t = ts.tile(v & 0x3FF)
                    if t is None or not v & 0x3FF: continue
                    if v & 0x400: t = t[:, ::-1]
                    if v & 0x800: t = t[::-1, :]
                    y, x = dy * 16 + (q // 2) * 8, dx * 16 + (q % 2) * 8; mk = t != 0
                    rgba[y:y + 8, x:x + 8, :3][mk] = np.array(ts.pal[v >> 12], np.uint8)[t][mk]
                    rgba[y:y + 8, x:x + 8, 3][mk] = 255
    return rgba

def comp(L, ts, m):
    """All three layers of a metatile, composited (opaque bottom)."""
    base = off(L['primary']['mt']) + 24 * m if m < 512 else off(L['secondary']['mt']) + 24 * (m - 512)
    e = struct.unpack_from('<12H', ROM, base); img = np.zeros((16, 16, 3), np.uint8)
    for k, v in enumerate(e):
        t = ts.tile(v & 0x3FF)
        if t is None: continue
        if v & 0x400: t = t[:, ::-1]
        if v & 0x800: t = t[::-1, :]
        q = k % 4; y, x = (q // 2) * 8, (q % 2) * 8; mk = np.ones((8, 8), bool) if k < 4 else t != 0
        img[y:y + 8, x:x + 8][mk] = np.array(ts.pal[v >> 12], np.uint8)[t][mk]
    return img

def cut_diff(header, x0, y0, w, h, ref):
    """Furniture drawn into the bottom layer too: keep the pixels that differ from a plain reference metatile
    (ref: one id for all cells, or {(x, y): id}); holes filled."""
    from scipy.ndimage import binary_fill_holes
    L = layout(u32(off(header))); ts = TS(L); c = map_cells(L); W = L['w']
    rgba = np.zeros((h * 16, w * 16, 4), np.uint8)
    for dy in range(h):
        for dx in range(w):
            x, y = x0 + dx, y0 + dy; a = comp(L, ts, c[y * W + x] & 0x3FF)
            r = comp(L, ts, ref[(x, y)] if isinstance(ref, dict) else ref)
            mk = np.abs(a.astype(int) - r.astype(int)).sum(-1) > 0
            sub = rgba[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16]; sub[..., :3] = a; sub[..., 3] = mk * 255
    m = binary_fill_holes(rgba[..., 3] > 0); rgba[..., 3] = m * 255
    return rgba

PIECES = {
    # the dark study (0x886B2D0): its writing desk with lamp and papers, its big armchair: Cadmus's office
    'study_desk': (0x0886B2D0, 15, 5, 2, 3),
    'study_armchair': (0x0886B2D0, 13, 5, 2, 2),
    # North Edelweiss lounge (0x886A9A0): the two-seat sofa and the two side couches facing in
    'lounge_sofa': (0x0886A9A0, 10, 2, 2, 2),
    'lounge_couch_left': (0x0886A9A0, 9, 4, 1, 2),
    'lounge_couch_right': (0x0886A9A0, 12, 4, 1, 2),
}

def l_couch():
    """La Costa Nostra's L-shaped red velvet couch (North Edelweiss restaurant, 0x886A984, cells 9-13 x 11-14). Its seat
    shares the restaurant carpet's salmon and part of it sits in the bottom layer, so it is cut by its outline: the
    back run (pixels 8-79 x 2-27 of the 5x4-cell block) and the side run (59-79 x 2-56, its end cap included)."""
    a = cut(0x0886A984, 9, 11, 5, 4, layers=(0, 1, 2)); m = np.zeros(a.shape[:2], bool)
    m[2:28, 8:80] = True; m[2:57, 59:80] = True
    a[..., 3] = m * 255; ys, xs = np.where(m)
    return a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]

def card_table():
    """The same restaurant's octagonal card table (green felt, cards and chips) from inside the couch's corner."""
    a = cut(0x0886A984, 9, 11, 5, 4, layers=(0, 1, 2)); m = np.zeros(a.shape[:2], bool)
    sub = a[32:63, 26:54].copy(); carpet = (sub[..., :3] == (200, 120, 120)).all(-1)
    from scipy.ndimage import binary_fill_holes
    mm = binary_fill_holes(~carpet & ~((sub[..., :3] == (208, 208, 216)).all(-1)))
    sub[..., 3] = mm * 255; return sub

if __name__ == '__main__':
    out0 = os.path.normpath(os.path.join(HERE, '..', '..', 'assets', 'monomyth_reference', 'pieces'))
    Image.fromarray(l_couch()).save(os.path.join(out0, 'l_couch.png')); Image.fromarray(card_table()).save(os.path.join(out0, 'card_table.png'))
    out = os.path.normpath(os.path.join(HERE, '..', '..', 'assets', 'monomyth_reference', 'pieces')); os.makedirs(out, exist_ok=True)
    for name, spec in PIECES.items():
        Image.fromarray(cut(*spec)).save(os.path.join(out, name + '.png')); print(name)
