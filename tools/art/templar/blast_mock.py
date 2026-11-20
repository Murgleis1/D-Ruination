"""Mock: the monastery hall after Eden's escape blast (user story 2026-11-19, bible 20_chapter1_build.md 16.2).

Eden blows her way out of the holding cell with a small explosive; the shock splits the church floor down into the
frozen hollow below (the ice path, tools/art/icepath/). User: the split runs through the gold medallion at the centre
of the nave. No natural split-floor tiles turned up in Crown or MonoMyth (searched), so it is drawn here as pixel art
over the approved hall (compose_mock.compose('pews')): a stepped, crisp-edged fissure through the medallion (widest
at its centre, closing at its rim), the far slab's broken face showing under a lit lip and the near lip a dark edge, the lower half of the slab sunk a shade,
two small patches of pale ice far down in the dark, and short stepped hairline cracks branching into the carpet.
Usage: python3 tools/art/templar/blast_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import compose_mock as CM

MED_C = (8 * 16 + 8, (CM.WALL + 3) * 16 + 4 + 24)      # the medallion's centre (as compose_mock places it)
MED_R = 23
# the fissure's centre line, pixel waypoints relative to the medallion's centre (stepped: 45-degree and straight runs)
PATH = [(-24, -12), (-17, -9), (-12, -9), (-6, -4), (-3, -4), (2, 1), (7, 1), (11, 5), (16, 7), (24, 12)]
VOID, VOID_DEEP = (22, 26, 38), (10, 12, 20)
ICE, ICE_HI = (110, 170, 206), (190, 230, 248)
CRACK = (58, 66, 70)

def line(p, q):
    (x0, y0), (x1, y1) = p, q; pts = []; dx, dy = abs(x1 - x0), -abs(y1 - y0)
    sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1); err = dx + dy
    while True:
        pts.append((x0, y0))
        if (x0, y0) == (x1, y1): return pts
        e2 = 2 * err
        if e2 >= dy: err += dy; x0 += sx
        if e2 <= dx: err += dx; y0 += sy

def compose():
    img = CM.compose('pews').copy(); H, W = img.shape[:2]; cx, cy = MED_C
    yy, xx = np.mgrid[0:H, 0:W]; r = np.hypot(xx - cx, yy - cy); med = r <= MED_R
    centre = []
    for a, b in zip(PATH, PATH[1:]): centre += line((cx + a[0], cy + a[1]), (cx + b[0], cy + b[1]))
    centre = list(dict.fromkeys(centre))
    gap = np.zeros((H, W), bool)
    for x, y in centre:                                  # square brush, wider towards the medallion's centre
        w = 0 if r[y, x] > MED_R - 3 else (1 if r[y, x] > 15 else (2 if r[y, x] > 8 else 3))
        gap[y - w:y + w + 1, x - w:x + w + 1] = True
    gap &= r <= MED_R + 1
    below = np.zeros((H, W), bool)                       # the near (lower) side of the split
    for x, y in centre: below[y + 1:, x] = True
    below &= ~gap
    sunk = med & below                                   # the lower slab sunk a shade
    img[sunk] = (img[sunk].astype(int) * 0.9).astype(np.uint8)
    img[gap] = VOID                                      # the fissure, deepest along its centre line
    for x, y in centre:
        if gap[y, x] and r[y, x] < MED_R - 4: img[y, x] = VOID_DEEP
    for k in (len(centre) // 2 - 3, len(centre) // 2 + 4):          # two small patches of ice far down
        x, y = centre[k]; img[y + 1, x - 1:x + 1] = ICE; img[y + 1, x] = ICE_HI
    # seen from the south, the far (upper) slab's broken face shows inside the top of the gap: a strip of cut stone
    # under a lit lip; the near (lower) lip is a dark edge
    face = gap & ~np.roll(gap, 1, 0)                     # the gap's top pixel in each column
    face2 = gap & np.roll(face, 1, 0) & (r < MED_R - 6)  # and the one below it where the gap is wide
    img[face] = (150, 118, 66); img[face2] = (104, 80, 44)
    lip_far = np.roll(gap, -1, 0) & ~gap & med           # the pixel above the gap
    lip_near = np.roll(gap, 1, 0) & ~gap & med           # the pixel below the gap
    img[lip_far] = (232, 206, 136); img[lip_near] = (64, 48, 30)
    for (ax, ay), steps in (((-24, -12), [(-5, -3), (-4, -4), (-3, 0)]), ((24, 12), [(5, 2), (3, 4), (4, 1)]),
                            ((-17, -9), [(-2, -5), (-3, -2)]), ((16, 7), [(3, 5), (1, 4)])):
        x, y = cx + ax, cy + ay                          # short stepped hairline cracks into the carpet
        for dx, dy in steps:
            for px, py in line((x, y), (x + dx, y + dy)):
                if r[py, px] > MED_R and CM.WALL * 16 <= py < H: img[py, px] = CRACK
            x, y = x + dx, y + dy
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/arceus/church_blast.png'
    img = compose(); Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), 0).save(out)
    cx, cy = MED_C
    Image.fromarray(img[cy - 48:cy + 48, cx - 64:cx + 64]).resize((128 * 5, 96 * 5), 0).save(out.replace('.png', '_zoom.png')); print(out)
