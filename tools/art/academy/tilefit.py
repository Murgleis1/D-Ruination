"""Fit a picture's 8x8 tiles to the GBA's 15 colours a tile (a helper for imgtiles builds).

reduce_tiles(img, box): inside box (x0, y0, x1, y1, pixels), merge the closest pair of colours (the rarer into the
commoner; distance scaled by the rarer's count, so rare stray shades go first and a hue that carries the picture,
like the statue's sapphire, survives) until no 8x8 tile in the box has more than `limit` colours. Applied to the
whole box at once, so neighbouring tiles keep sharing colours (and so palettes).
"""
import collections
import numpy as np

def reduce_tiles(img, box, limit=15):
    x0, y0, x1, y1 = box; out = (img >> 3) << 3; sub = out[y0:y1, x0:x1]
    def worst():
        m = 0
        for ty in range(y0 // 8 * 8, y1, 8):
            for tx in range(x0 // 8 * 8, x1, 8):
                m = max(m, len(set(map(tuple, out[ty:ty + 8, tx:tx + 8].reshape(-1, 3).tolist()))))
        return m
    merges = 0
    while worst() > limit:
        cnt = collections.Counter(map(tuple, sub.reshape(-1, 3).tolist())); cols = list(cnt)
        best = None
        for i, a in enumerate(cols):
            for b in cols[i + 1:]:
                d = sum((p - q) ** 2 for p, q in zip(a, b)) ** 0.5 * min(cnt[a], cnt[b]) ** 0.5
                if best is None or d < best[0]: best = (d, a, b)
        _, a, b = best; keep, drop = (a, b) if cnt[a] >= cnt[b] else (b, a)
        flat = sub.reshape(-1, 3); flat[(flat == drop).all(1)] = keep; sub[:] = flat.reshape(sub.shape); merges += 1
    return out, merges
