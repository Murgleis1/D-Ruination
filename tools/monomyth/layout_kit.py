"""Terrain classes for every metatile of the new tilesets, from their actual pixels,
plus a neighbourhood dictionary learned from the hand-made MonoMyth source maps.

Classes: W water, S sand, G grass, T tree/forest, P cobble/path, R rock/cliff, O other.
"""
import os, sys, json
from collections import Counter, defaultdict
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from verify_cormoria import load

def tilesets(C):
    pt, ppal, pm = load(os.path.join(C, 'data/tilesets/primary/cormoria'))
    st, spal, sm = load(os.path.join(C, 'data/tilesets/secondary/pelluca_valley'))
    pal = [ppal[i] if i < 6 else spal[i] for i in range(16)]
    def draw(mid):
        e = pm[mid] if mid < 512 else sm[mid - 512]
        img = np.zeros((16, 16, 3), int)
        for q in range(12):
            v = e[q]; tid = v & 0x3FF
            if q >= 4 and tid == 0: continue
            t = pt[tid] if tid < 512 else st[tid - 512]
            if (v >> 10) & 1: t = t[:, ::-1]
            if (v >> 11) & 1: t = t[::-1]
            oy, ox = ((q % 4) // 2) * 8, (q % 2) * 8
            for y in range(8):
                for x in range(8):
                    if t[y, x]: img[oy + y, ox + x] = pal[v >> 12][t[y, x]]
        return img
    return pm, sm, draw

def pixel_class(px):
    r, g, b = px[..., 0], px[..., 1], px[..., 2]
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    cls = np.full(r.shape, 'O', object)
    cls[(b > r + 40) & (b > g + 8)] = 'W'
    cls[(r > 170) & (g > 150) & (b < 160) & (r >= g)] = 'S'
    cls[(np.abs(r - g) < 20) & (np.abs(g - b) < 28) & (lum > 105) & (lum < 215)] = 'P'
    cls[(g > r + 25) & (g >= b) & (lum >= 120)] = 'G'
    cls[(g > r + 10) & (g >= b - 10) & (lum < 120)] = 'T'
    cls[(lum < 95) & (cls == 'O')] = 'R'
    return cls

def metatile_class(img):
    c = Counter(pixel_class(img.reshape(-1, 3)).tolist())
    return c.most_common(1)[0][0]
