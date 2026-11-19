"""Cut props out of Pokemon Crown maps (credit: Blah and the Crown team; used with permission).

Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/crown/crown_pieces.py
Each piece is a rectangle of a Crown map (map group, map number, columns, rows); only the metatiles' object
(top) layer is kept, so the piece drops onto any floor or wall. Pieces whose bottom layer is part of the prop
(a counter built into the floor) list those cells in `full` with a plain reference metatile for each (the wall or
floor the prop stands on): the bottom layer is kept where it differs from the reference, holes filled.
Output: assets/crown_reference/pieces/<name>.png (RGBA).
"""
import os, sys, struct
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'odyssey'))
from frlib import ROM, u32, off, layout
from frrender import TS, map_cells

MAP_GROUPS = 0x8711468               # 43 groups (README)

def map_layout(group, num):
    starts = [u32(off(MAP_GROUPS) + 4 * g) for g in range(43)]
    return layout(u32(off(u32(off(starts[group]) + 4 * num))))

def cell_layers(ts, mid):
    """(bottom RGB, top RGB, top mask) of one metatile."""
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

def cut(group, num, x0, y0, w, h, full=None, crop=None, clear=()):
    from scipy.ndimage import binary_fill_holes
    full = full or {}
    L = map_layout(group, num); ts = TS(L); cells = map_cells(L); W = L['w']
    rgba = np.zeros((h * 16, w * 16, 4), np.uint8); bmask = np.zeros((h * 16, w * 16), bool)
    for dy in range(h):
        for dx in range(w):
            x, y = x0 + dx, y0 + dy; (bot, _), (top, tm) = cell_layers(ts, cells[y * W + x] & 0x3FF)
            sub = rgba[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16]
            if (x, y) in full:                             # both layers composited, against the reference's
                comp = bot.copy(); comp[tm] = top[tm]
                if full[(x, y)] < 0: ref = bot                 # -1: against its own bottom layer
                else: (rb, _), (rt, rm) = cell_layers(ts, full[(x, y)]); ref = rb.copy(); ref[rm] = rt[rm]
                bm = np.abs(comp.astype(int) - ref.astype(int)).sum(-1) > 0
                sub[bm, :3] = comp[bm]; sub[bm, 3] = 255; bmask[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16] = bm
                continue
            sub[tm, :3] = top[tm]; sub[tm, 3] = 255
    if full:                                             # the bottom-layer part: diff mask with its holes filled
        b = binary_fill_holes(bmask); fill = b & (rgba[..., 3] == 0)
        for dy in range(h):
            for dx in range(w):
                x, y = x0 + dx, y0 + dy
                if (x, y) not in full: continue
                (bot, _), (top, tm) = cell_layers(ts, cells[y * W + x] & 0x3FF); comp = bot.copy(); comp[tm] = top[tm]
                s = (slice(dy * 16, dy * 16 + 16), slice(dx * 16, dx * 16 + 16)); f = fill[s]
                rgba[s][f, :3] = comp[f]; rgba[s][f, 3] = 255
        from scipy.ndimage import label                  # stray pixels (floor-plank variation): keep the prop itself
        lab, n = label(rgba[..., 3] > 0, structure=np.ones((3, 3)))
        if n > 1:
            keep = 1 + int(np.argmax([(lab == k).sum() for k in range(1, n + 1)])); rgba[lab != keep] = 0
    for (a, b, c, d) in clear: rgba[b:d, a:c] = 0      # boxes (x0, y0, x1, y1) of leftovers to drop
    if crop: x0, y0, x1, y1 = crop; rgba = rgba[y0:y1, x0:x1]
    return rgba

PIECES = {
    # name: (group, num, x0, y0, w, h, {full cell: plain reference metatile}, crop box or None[, clear boxes])
    # the inn's U-shaped counter with its flowers and ledger (g7.8); reception desk, Academy ground floor
    # (the cells inside the U are listed against themselves: nothing of them is kept)
    'reception_counter': (7, 8, 8, 14, 4, 4, {(8, 14): 0x57, (11, 14): 0x57, (8, 15): 0x29D, (11, 15): 0x29D,
                          (9, 14): 0x57, (10, 14): 0x57, (9, 15): 0x29D, (10, 15): 0x29D,
                          (8, 16): 0x78, (9, 16): 0x78, (10, 16): 0x78, (11, 16): 0x78,
                          (8, 17): 0x78, (9, 17): 0x78, (10, 17): 0x78, (11, 17): 0x78}, None,
                          [(62, 61, 64, 64), (0, 63, 64, 64)]),          # a floor plank's seam under its corner
    # the notice board with pinned papers on its ledge (g4.3), without the scraps on the floor
    'notice_board': (4, 3, 12, 3, 3, 2, None, None),
    # a wooden crate (the witch's hut, g20.1) and the step ladder (the sewers, g7.11): construction props
    'crate': (20, 1, 10, 4, 1, 1, None, None),
    'step_ladder': (7, 11, 25, 14, 1, 2, {(25, 15): 0x289}, None),
    # the park's signboard on two posts (the harbour market town, g3.0): the standing notice board's frame
    'park_sign': (3, 0, 17, 19, 2, 2, None, None),
    # the grand piano of the manor room (g17.0), drawn over its wall and floor: kept where it differs from them
    'grand_piano': (17, 0, 4, 1, 2, 3, {(x, y): -1 for x in (4, 5) for y in (1, 2, 3)}, None),
}

if __name__ == '__main__':
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'crown_reference', 'pieces')
    for name, spec in PIECES.items():
        Image.fromarray(cut(*spec)).save(os.path.join(out, name + '.png')); print(name)
