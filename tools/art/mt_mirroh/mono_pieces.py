"""Cut sprites (with transparency) out of MonoMyth maps (credit the MonoMyth team).

A prop drawn into its ground: every pixel whose colour is not one of the ground's (the metatiles ground_ids), and
not green (grass, moss: green_drop), is the prop.  cut_on(addr, x0, y0, w, h, ground_ids) -> (rgb, alpha).
Renders through mm_render (MonoMyth's blockdata may be LZ77-compressed)."""
import os, sys, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mm_render as M

_cache = {}
def grid(addr):
    if addr not in _cache:
        img, c, ts, L = M.render(addr)
        _cache[addr] = (img, np.array(c).reshape(L['h'], L['w']) & 0x3ff, ts)
    return _cache[addr]

def cut_on(addr, x0, y0, w, h, ground_ids, green_drop=True):
    img, g, ts = grid(addr)
    gc = set()
    for m in ground_ids: gc |= {tuple(c) for c in ts.meta(m).reshape(-1, 3)}
    rgb = img[y0 * 16:(y0 + h) * 16, x0 * 16:(x0 + w) * 16].copy()
    a = np.array([[tuple(c) not in gc for c in row] for row in rgb])
    if green_drop:
        r_, g_, b_ = [rgb[..., i].astype(int) for i in range(3)]
        a &= ~((g_ > r_ + 12) & (g_ > b_ - 10))
    return rgb, a
