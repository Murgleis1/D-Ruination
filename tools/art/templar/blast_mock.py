"""Mock: the monastery hall after Eden's escape blast (user story 2026-11-19, bible 20_chapter1_build.md 16.2).

Eden blows her way out of the holding cell with a small explosive; the shock splits the church floor down into the
frozen hollow below (the ice path, tools/art/icepath/). User: the split runs through the gold medallion at the centre
of the nave. No natural split-floor tiles turned up in Crown or MonoMyth (searched), so it is drawn here as pixel art
over the approved hall (compose_mock.compose('pews')): a stepped, crisp-edged fissure through the medallion (widest
at its centre, closing at its rim), the far slab's broken face showing under a lit lip and the near lip a dark edge, the lower half of the slab sunk a shade,
two small patches of pale ice far down in the dark, short stepped hairline cracks branching into the carpet,
frost (user: the sudden cold the Templar remarks on) creeping out from the split, thickest at its lips; and the
old foundation fault the blast exposed (user): Old HQ's cracked wall pieces, faint old cracks in the carpet; and the
cell room caved in (user): its doorway choked with fallen stone, fresh cracks running from it to the split.
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
    # frost (user: the Templar there notes the sudden drop in temperature; ice must lie right below): a band of solid
    # rime along the split with a ragged edge, a dithered fringe beyond it, and a few small star crystals further out
    from scipy.ndimage import distance_transform_edt, zoom
    d = distance_transform_edt(~gap); rng = np.random.default_rng(8)
    RIME, FRINGE, STAR = (236, 248, 255), (196, 228, 244), (214, 238, 250)
    blot = zoom(rng.random((H // 4 + 1, W // 4 + 1)), 4, order=1)[:H, :W]          # low-frequency: a ragged edge
    band = (d >= 1) & (d <= 1.5 + 3.0 * blot) & (yy >= CM.WALL * 16)
    fringe = (d > 1.5 + 3.0 * blot) & (d <= 3.5 + 5.0 * blot) & ((xx + yy) % 2 == 0) & (yy >= CM.WALL * 16)
    img[fringe] = FRINGE; img[band] = RIME
    stars = 0
    for _ in range(400):
        y, x = int(rng.integers(0, H)), int(rng.integers(0, W))
        if not (7 <= d[y, x] <= 16) or y < CM.WALL * 16 + 1 or y >= H - 1 or x < 1 or x >= W - 1: continue
        img[y, x] = RIME
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)): img[y + dy, x + dx] = STAR
        stars += 1
        if stars >= 9: break
    old_fault(img)
    rubble = cave_in(img)
    glass_cracks(img)
    LAST.update(gap=gap, rubble=rubble)                  # (for build_ruined.py: the fall cells, the blocked cells)
    return img

LAST = {}

# the old foundation fault (user: the blast only exposed it; the church was always at risk): MonoMyth Old
# Headquarters' own cracked wall and trim pieces laid over a few stretches of clear wall, and faint old hairline cracks in the carpet (a shade darker than the carpet, not black like
# the fresh split) running from the walls towards the medallion
OLD_WALL = [(2, 0, 0xCC, 0xCA), (2, 2, 0xD4, 0xD2), (14, 0, 0xCD, 0xCA), (15, 1, 0xD4, 0xD2), (14, 3, 0xD5, 0xD2),
            (0, 3, 0xD5, 0xD2)]                         # (x, wall row, cracked piece, the clean piece it is drawn on)
OLD_CRACKS = [((1 * 16 + 4, CM.WALL * 16), [(3, 4), (2, 5), (4, 3), (3, 6), (5, 4)]),
              ((15 * 16 + 6, CM.WALL * 16), [(-3, 5), (-4, 3), (-2, 6), (-5, 4)]),
              ((3 * 16 + 2, 14 * 16), [(5, -3), (6, -2), (4, -4)]),
              ((14 * 16 + 8, 13 * 16), [(-5, -2), (-4, -4), (-6, -1)])]

def old_fault(img):
    H, W = img.shape[:2]
    for x, row, cracked, clean in OLD_WALL:                 # only the crack's own pixels, over our wall
        a, b = CM.hq(cracked), CM.hq(clean); m = np.abs(a.astype(int) - b.astype(int)).sum(-1) > 0
        sub = img[row * 16:row * 16 + 16, x * 16:x * 16 + 16]; sub[m] = a[m]
    for (x, y), steps in OLD_CRACKS:
        for dx, dy in steps:
            for px, py in line((x, y), (x + dx, y + dy)):
                if 0 <= py < H and 0 <= px < W: img[py, px] = (img[py, px].astype(int) * 0.62).astype(np.uint8)
            x, y = x + dx, y + dy

# the cell room caved in (user: the blast let Eden out of the cell but brought part of that room down, and the
# collapse set off the chain of cracks that split the chapel floor): the cell doorway on the north wall choked with
# fallen stone (MonoMyth's rubble piles from Mt. Thunder, map 0x886D608, turned to the church's grey; user: the Crown
# rocks looked unnatural), and fresh cracks running from the doorway across the floor to the split
ROCKS = os.path.join(HERE, '..', '..', '..', 'assets', 'monomyth_reference', 'pieces')
DOOR_X = 1 * 16                                          # the cell doorway (compose_mock: x 1, on the wall's foot)
PILE = [('rubble_pile_a', 1 * 16 - 3, CM.WALL * 16 - 30), ('rubble_pile_a', 1 * 16 - 6, CM.WALL * 16 - 12),
        ('rubble_stone', 0 * 16 + 1, CM.WALL * 16 + 4), ('rubble_stone', 2 * 16 - 2, CM.WALL * 16 + 8)]   # clear of the stand
# from the foot of the choked doorway, under the candle stand, to where the split's own crack begins
CHAIN = [(1 * 16 + 10, CM.WALL * 16 + 12), (2 * 16 + 2, CM.WALL * 16 + 22), (2 * 16 + 12, CM.WALL * 16 + 34),
         (3 * 16 + 12, CM.WALL * 16 + 40), (4 * 16 + 14, CM.WALL * 16 + 49), (6 * 16 + 4, CM.WALL * 16 + 57)]
GREY = [(40, 40, 46), (66, 66, 72), (94, 94, 100), (122, 122, 128), (150, 150, 156), (178, 178, 182)]

def rock(name):
    a = np.array(Image.open(os.path.join(ROCKS, name + '.png')).convert('RGBA')); rgb, m = a[..., :3].copy(), a[..., 3] > 0
    lum = rgb.astype(int).sum(-1); lo, hi = lum[m].min(), lum[m].max()
    for y, x in zip(*np.nonzero(m)): rgb[y, x] = GREY[min(5, int((lum[y, x] - lo) / max(1, hi - lo + 1) * 6))]
    return rgb, m

def cave_in(img):
    H, W = img.shape[:2]
    img[CM.WALL * 16 - 32:CM.WALL * 16, DOOR_X:DOOR_X + 18] = GREY[0]          # the doorway's dark, now dust and stone
    rubble = np.zeros((H, W), bool)
    for name, px, py in PILE:
        rgb, m = rock(name); sub = img[py:py + m.shape[0], px:px + m.shape[1]]
        mm = m[:sub.shape[0], :sub.shape[1]]; sub[mm] = rgb[:sub.shape[0], :sub.shape[1]][mm]
        rubble[py:py + mm.shape[0], px:px + mm.shape[1]] |= mm
    pts = CHAIN
    for p, q in zip(pts, pts[1:]):                         # the chain of fresh cracks, doorway to split, with spurs
        for x, y in line(p, q): img[y, x] = CRACK_FRESH
    for (x, y), (dx, dy) in zip(pts[1:-1], ((4, -2), (-3, 4), (2, 4), (3, -3))):
        for px, py in line((x, y), (x + dx, y + dy)): img[py, px] = CRACK_FRESH
    return rubble

CRACK_FRESH = (30, 30, 36)

# cracked stained glass (user: two or three minor cracks in each of the three windows, one even across the face of
# the girl in the great window behind the statue): small star fractures, pale fracture lines with a dark pit at the
# point of impact, drawn only on the glass (never on the wall round it)
GLASS = [  # (centre, rays as (dx, dy) steps, the window's box x0, y0, x1, y1)
    ((123, 45), [(-5, -4), (6, -3), (4, 6), (-3, 7), (-7, 2)], (98, 4, 170, 92)),        # across the girl's face
    ((152, 70), [(5, -5), (-6, -2), (2, 7)], (98, 4, 170, 92)),
    ((109, 26), [(-4, 5), (5, 3)], (98, 4, 170, 92)),
    ((58, 40), [(-5, -6), (6, -4), (-3, 7), (5, 6)], (48, 14, 81, 79)),                    # the west lancet
    ((70, 66), [(-4, 4), (4, -3)], (48, 14, 81, 79)),
    ((210, 54), [(5, -6), (-6, -3), (-2, 7), (6, 5)], (192, 14, 225, 79)),                 # the east lancet
    ((200, 30), [(4, -4), (-3, 5)], (192, 14, 225, 79)),
]
FRACTURE, PIT = (232, 238, 244), (36, 36, 44)

def glass_cracks(img):
    wall = tuple(img[60, 40]); wall2 = tuple(img[60, 90])               # the wall's own greys round the windows
    def glass(x, y, box):
        x0, y0, x1, y1 = box
        return x0 <= x < x1 and y0 <= y < y1 and tuple(img[y, x]) not in (wall, wall2)
    for (cx, cy), rays, box in GLASS:
        for dx, dy in rays:
            for i, (x, y) in enumerate(line((cx, cy), (cx + dx, cy + dy))):
                if glass(x, y, box) and i:                     # pale on dark glass, dark on pale glass
                    img[y, x] = FRACTURE if int(img[y, x].astype(int).sum()) < 480 else (64, 64, 78)
        if glass(cx, cy, box): img[cy, cx] = PIT

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/arceus/church_blast.png'
    img = compose(); Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), 0).save(out)
    cx, cy = MED_C
    Image.fromarray(img[cy - 48:cy + 48, cx - 64:cx + 64]).resize((128 * 5, 96 * 5), 0).save(out.replace('.png', '_zoom.png')); print(out)
