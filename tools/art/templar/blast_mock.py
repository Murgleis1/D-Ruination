"""Mock: the monastery hall after Eden's escape blast (user story 2026-11-19, bible 20_chapter1_build.md 16.2).

Eden blows her way out of the holding cell (its door on the north wall, west of the altar) with a small explosive;
the blast cracks the church floor open in front of the cell door, down into the frozen hollow below (the ice path,
tools/art/icepath/). Drawn over the approved hall (compose_mock.compose('pews')): a jagged hole in the nave carpet,
its torn and scorched rim, cracks running out across the carpet, rubble and soot thrown towards the nave, and a cold
blue glow of ice down inside. Plain geometry and noise only (no borrowed art).
Usage: python3 tools/art/templar/blast_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import compose_mock as CM

HOLE_C = (4 * 16 + 8, 9 * 16 + 8)          # the hole's centre (px): in the open floor below the cell door, clear of the stand, pillar and table
HOLE_R = (19, 13)                            # its half-width, half-height (an oval, then roughened)
VOID = [(8, 10, 18), (16, 22, 36), (26, 38, 58), (40, 64, 92)]
ICE = [(84, 140, 180), (140, 200, 232), (200, 236, 250)]
RUBBLE = [(52, 52, 58), (88, 88, 96), (126, 126, 134), (160, 160, 166)]
SOOT = (40, 36, 34)

def hole_mask(H, W, rng):
    yy, xx = np.mgrid[0:H, 0:W]; cx, cy = HOLE_C; rx, ry = HOLE_R
    ang = np.arctan2(yy - cy, xx - cx); wob = np.zeros_like(ang)
    for k, a in ((3, 0.10), (5, 0.08), (9, 0.06), (14, 0.05)):                # jagged: a few angular harmonics
        wob += a * np.sin(k * ang + rng.uniform(0, 6.28))
    d = np.sqrt(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2)
    return d, wob

def compose():
    img = CM.compose('pews').copy(); H, W = img.shape[:2]; rng = np.random.default_rng(13)
    d, wob = hole_mask(H, W, rng); cx, cy = HOLE_C
    yy, xx = np.mgrid[0:H, 0:W]
    hole = d < 1 + wob
    rim = (d < 1.32 + wob * 1.3) & ~hole
    scorch = (d < 2.1 + wob * 2 + rng.random((H, W)) * 0.35) & ~hole & ~rim & (yy > CM.WALL * 16 - 4)
    # scorched carpet: darkened towards the hole, patchy
    f = np.clip((2.1 - d) / 0.8, 0, 1)                 # in three dithered steps (a GBA palette, not a smooth blur)
    bayer = np.array([[0, 2], [3, 1]]) / 4.0; th = np.tile(bayer, (H // 2 + 1, W // 2 + 1))[:H, :W]
    lvl = np.floor(f * 3 + th).clip(0, 3).astype(int)
    for L, k in ((1, 0.30), (2, 0.55), (3, 0.80)):
        sel = scorch & (lvl == L); img[sel] = (img[sel] * (1 - k) + np.array(SOOT) * k).astype(np.uint8)
    # the torn rim: broken flagstone under the carpet, light on the far side, dark on the near side
    lit = (yy < cy)
    img[rim & lit] = RUBBLE[2]; img[rim & ~lit] = RUBBLE[1]
    edge = rim & (d < 1.08 + wob)
    img[edge] = RUBBLE[0]
    # the void: dark, deeper towards the near (lower) wall; the far inner wall catches a cold blue glow of ice
    depth = np.clip((yy - (cy - HOLE_R[1])) / (2 * HOLE_R[1]), 0, 1)
    for i, c in enumerate(VOID):
        img[hole & (depth >= i / 4) & (depth < (i + 1) / 4)] = VOID[3 - i]
    glint = hole & (d > 0.55 + wob) & (yy > cy) & ((xx + yy) % 3 == 0)
    img[glint] = ICE[0]
    low = hole & (d > 0.75 + wob) & (yy > cy + 3)
    img[low] = ICE[1]; img[low & ((xx * 7 + yy) % 5 == 0)] = ICE[2]
    # cracks running out from the rim across the carpet
    for k in range(9):
        a = rng.uniform(0, 2 * np.pi); r = 1.25
        x = cx + np.cos(a) * HOLE_R[0] * r; y = cy + np.sin(a) * HOLE_R[1] * r
        for _ in range(int(rng.integers(8, 20))):
            xi, yi = int(round(x)), int(round(y))
            if CM.WALL * 16 <= yi < H and 0 <= xi < W: img[yi, xi] = (30, 30, 34)
            a += rng.uniform(-0.5, 0.5); x += np.cos(a); y += np.sin(a) * 0.8
    # rubble thrown out, mostly towards the nave (south and east)
    for _ in range(26):
        a = rng.uniform(-0.6, 2.2); r = rng.uniform(1.4, 3.2)
        x = int(cx + np.cos(a) * HOLE_R[0] * r); y = int(cy + np.sin(a) * HOLE_R[1] * r * 1.2)
        s = int(rng.integers(1, 4))
        if y < CM.WALL * 16 or y + s >= H: continue
        img[y:y + s, x:x + s] = RUBBLE[int(rng.integers(1, 4))]; img[y + s - 1, x:x + s] = RUBBLE[0]
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/arceus/church_blast.png'
    img = compose(); Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), 0).save(out)
    Image.fromarray(img[: 14 * 16, : 9 * 16]).resize((9 * 16 * 4, 14 * 16 * 4), 0).save(out.replace('.png', '_zoom.png')); print(out)
