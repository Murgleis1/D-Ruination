"""Roof selection by SHAPE + COLOUR: the same slate greys appear in foundations,
chimneys and window frames, so a colour swap alone would recolour those too.

roof = pixels in the roof colour set that are 4-connected (through roof-colour
pixels) to roof-colour pixels in the building's top `seed_rows` rows.
"""
import numpy as np
from collections import deque

def roof_mask(img, colours, seed_rows):
    H, W = img.shape[:2]
    cand = np.zeros((H, W), bool)
    for c in colours:
        cand |= (img == np.array(c)).all(-1)
    m = np.zeros_like(cand)
    q = deque((y, x) for y in range(min(seed_rows, H)) for x in range(W) if cand[y, x])
    for y, x in q: m[y, x] = True
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            yy, xx = y + dy, x + dx
            if 0 <= yy < H and 0 <= xx < W and cand[yy, xx] and not m[yy, xx]:
                m[yy, xx] = True; q.append((yy, xx))
    return m
