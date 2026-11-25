"""Cut sprites (with transparency) out of Lazarus maps, layer by layer (credit the Lazarus team).

Lazarus' metatiles have three layers of four tiles (MS=24): bottom, middle, top. A prop drawn over ground sits in the
middle/top layers, so rendering only those layers, colour 0 transparent, gives the prop alone; where a prop was drawn
into the bottom layer, `ground` (a metatile id of the plain ground under it) is diffed away instead.
API: cells(header_off) -> (W, H, ids, ts); cut(header_off, x0, y0, w, h, ground=None) -> (rgb, alpha) at 16 px/cell.
The ROM is at /home/claude/lazarus/Lazarus.gba (romlib), readers in /home/claude/lazlib."""
import sys, numpy as np
sys.path.insert(0, '/home/claude/lazlib')
from romlib import u16, u32, off, layout
import render as LR

_ts = {}
def header(h_off):
    lp = u32(h_off)
    return layout(lp)

def cells(h_off):
    L = header(h_off); key = L['addr']
    if key not in _ts: _ts[key] = LR.TS(L)
    ts = _ts[key]; W, H = L['w'], L['h']; mo = off(L['map'])
    ids = np.array([[u16(mo + (y * W + x) * 2) & 0x3ff for x in range(W)] for y in range(H)])
    return W, H, ids, ts

def layer_img(ts, mid, layers=(1, 2)):
    """the metatile's chosen layers only: (rgb 16x16x3, alpha 16x16)"""
    base = ts.pmt + mid * LR.MS if mid < LR.NPM else ts.smt + (mid - LR.NPM) * LR.MS
    rgb = np.zeros((16, 16, 3), np.uint8); a = np.zeros((16, 16), bool)
    for q in range(LR.MS // 2):
        if q // 4 not in layers: continue
        e = u16(base + q * 2); tid, xf, yf, sl = e & 0x3ff, (e >> 10) & 1, (e >> 11) & 1, e >> 12
        t = ts.tile(tid)
        if t is None: continue
        if xf: t = t[:, ::-1]
        if yf: t = t[::-1, :]
        oy, ox = ((q % 4) // 2) * 8, ((q % 4) % 2) * 8
        m = t != 0
        rgb[oy:oy + 8, ox:ox + 8][m] = np.array([ts.pal[sl][v] for v in t[m]], np.uint8).reshape(-1, 3)
        a[oy:oy + 8, ox:ox + 8] |= m
    return rgb, a

def cut(h_off, x0, y0, w, h, ground=None, layers=(1, 2)):
    W, H, ids, ts = cells(h_off)
    rgb = np.zeros((h * 16, w * 16, 3), np.uint8); a = np.zeros((h * 16, w * 16), bool)
    for y in range(h):
        for x in range(w):
            mid = int(ids[y0 + y, x0 + x])
            r_, a_ = layer_img(ts, mid, layers)
            if ground is not None:
                full = ts.meta(mid); g = ts.meta(ground)
                diff = (full != g).any(-1)
                r_ = np.where(a_[..., None], r_, full); a_ = a_ | diff
            rgb[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = r_; a[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = a_
    return rgb, a

def cut_on(h_off, x0, y0, w, h, ground_ids):
    """a prop drawn into its ground: every pixel whose colour is not one of the ground's (the metatiles ground_ids)"""
    W, H, ids, ts = cells(h_off)
    gc = set()
    for g in ground_ids: gc |= {tuple(c) for c in ts.meta(g).reshape(-1, 3)}
    rgb = np.zeros((h * 16, w * 16, 3), np.uint8)
    for y in range(h):
        for x in range(w): rgb[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = ts.meta(int(ids[y0 + y, x0 + x]))
    a = np.array([[tuple(c) not in gc for c in row] for row in rgb])
    return rgb, a
