"""Pelluca City: fixes from the 2026-11-22 review pass (user: "check everything going back to Pelluca Valley").

Applied to the built map (codebase/data/layouts/PellucaCity/map.bin), not by rebuilding it: the map was installed
from layout draft 19 (tools/monomyth/pelluca_layout.py) and then edited in place by later steps (the houses' doors,
the Academy's door, the water animation), which a rebuild would lose. Every cell written here is a copy of a cell
the map already has (metatile, collision and elevation together), so no new metatile is needed.

1. The coast at the map's sides (user choice: "woods end at the surf"). The east and west forest belts ran straight
   down into the sea to the map's bottom edge: pines standing in the water. Now each belt ends in its own base row
   (copied from the base row its top part already ends in, at the gap for the road), and below it is open sea
   (copied from the nearest sea columns, x parity kept for the water's tiling):
     west: base row 45 (the beach's wet sand row at x 8-12), sea from row 46, x 0-7;
     east: base row 41 (level with the quay's wall), sea from row 42, x 72-79.
   Nothing walkable reaches the map's edge there: the sea needs Surf.
2. The canal's basin ("where it goes underground", the dive spot) had stone banks on three sides and its south
   edge ran straight from water to grass. It takes a stone rim on that side: the pier's own rim pieces (its north
   rim, and its inner corners where the stem meets the head).

Usage: python3 tools/art/pelluca_review_fixes.py   (idempotent; then make)
"""
import os, json
import numpy as np

C = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'codebase'))
P = os.path.join(C, 'data/layouts/PellucaCity/map.bin')
W, H = 80, 60


def main():
    g = np.fromfile(P, '<u2').reshape(H, W)
    src = g.copy()                                    # (every copy reads the map as it was)
    # 1. west belt: base row 45 from the top part's base row 27; sea below from x 8/9
    for x in range(0, 8):
        g[45, x] = src[27, x]
        for y in range(46, H):
            g[y, x] = src[y, 8 + x % 2]
    # 1. east belt: base row 41 from its top part's base row 23; harbour sea below from x 70/71 (rows 43 on: plain
    #    open water; row 42 is the shadow under the quay's wall there, so row 42 takes row 44's piece)
    for x in range(72, 80):
        g[41, x] = src[23, x]
        for y in range(42, H):
            g[y, x] = src[y if y >= 43 else y + 2, 70 + x % 2]
    # 2. the basin's south rim: corners from the pier's inner corners, the run from its north rim (x parity kept)
    g[12, 16] = src[49, 45]                           # (water to the north-east only: the inner corner)
    g[12, 23] = src[49, 43]                           # (water to the north-west only)
    for x in range(17, 23):
        g[12, x] = src[49, 42 if x % 2 == 0 else 41]
    g.astype('<u2').tofile(P)
    print('Pelluca review fixes written')


if __name__ == '__main__':
    main()
