"""Cut rectangles out of a FireRed-based ROM's map (Crown, Pokemon Odyssey, Ghost Grey...): the ROM is the one
ODYSSEY_ROM points at (tools/odyssey/frlib.py reads one ROM per process, so each source ROM gets its own run).

cut(L, x0, y0, w, h, mode): 'top' keeps the metatiles' object (top) layer only (RGBA; the piece drops onto any
ground), 'full' keeps both layers (RGB, alpha 255: ground, cliffs, fields).
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'odyssey'))
from frlib import u32, off, layout                     # noqa: E402
from frrender import TS, map_cells                     # noqa: E402

def layers(ts, mid):
    e = ts.ents(mid); out = []
    for layer in range(2):
        img = np.zeros((16, 16, 3), np.uint8); mk = np.zeros((16, 16), bool)
        for q in range(4):
            v = e[layer * 4 + q]; t = ts.tile(v & 0x3FF)
            if v & 0x400: t = t[:, ::-1]
            if v & 0x800: t = t[::-1, :]
            pal = np.array(ts.pal[(v >> 12) & 15], np.uint8); y, x = (q // 2) * 8, (q % 2) * 8
            nz = t != 0 if layer else np.ones((8, 8), bool)
            img[y:y + 8, x:x + 8][nz] = pal[t][nz]; mk[y:y + 8, x:x + 8] |= nz
        out.append((img, mk))
    return out

def cut(L, x0, y0, w, h, mode='top', ref=None):
    """mode 'diff': both layers, keeping only the pixels that differ from the reference ground cell ref (a map
    cell (x, y) of plain ground): for props drawn into the ground layer (fences, crops)."""
    ts = TS(L); cells = map_cells(L); W = L['w']
    if mode == 'diff':
        (rb, _), (rt, rm) = layers(ts, cells[ref[1] * W + ref[0]] & 0x3FF); rimg = rb.copy(); rimg[rm] = rt[rm]
    if mode == 'key':                                  # ref: ground cells; their colours are keyed out
        keyc = set()
        for rx, ry in ref:
            (rb, _), (rt, rm) = layers(ts, cells[ry * W + rx] & 0x3FF); c = rb.copy(); c[rm] = rt[rm]
            keyc |= {tuple(v) for v in c.reshape(-1, 3).tolist()}
    rgba = np.zeros((h * 16, w * 16, 4), np.uint8)
    for dy in range(h):
        for dx in range(w):
            (bot, _), (top, tm) = layers(ts, cells[(y0 + dy) * W + x0 + dx] & 0x3FF)
            sub = rgba[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16]
            if mode in ('full', 'diff', 'key'):
                comp = bot.copy(); comp[tm] = top[tm]; sub[..., :3] = comp; sub[..., 3] = 255
                if mode == 'diff': sub[(comp == rimg).all(-1), 3] = 0
                if mode == 'key':
                    k = np.array([[tuple(v) in keyc for v in row] for row in comp.tolist()]); sub[k, 3] = 0
            else:
                sub[tm, :3] = top[tm]; sub[tm, 3] = 255
    return rgba

def group_layout(groups_ptr, group, num, ngroups=None):
    g = u32(off(groups_ptr) + 4 * group)
    return layout(u32(off(u32(off(g) + 4 * num))))
