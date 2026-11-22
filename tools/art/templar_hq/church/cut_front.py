"""The Arceus church (user 2026-11-22, Arceus_Church_Starlight_City.png): keep the front building with the cross
tower on its roof, shed the domed hall behind it. Works at the GBA's scale (the source is a 2x upscale)."""
import numpy as np
from collections import deque
from PIL import Image

n = np.array(Image.open('native.png').convert('RGBA')).astype(int)
H, W = n.shape[:2]
C = lambda x, y: tuple(n[y, x, :3])
BLUES = {(51, 60, 128), (67, 79, 168), (62, 74, 163), (34, 40, 89), (66, 73, 107)}
OUTLINE = (49, 56, 82)
RIM = {(237, 234, 228), (247, 247, 247)}
TX0, TX1 = 38, 74                      # (the cross tower's box: x 38-73)
TOP = 46

keep = np.zeros((H, W), bool)
# 1. the front building: everything from the crescent rim down (left half, then mirrored)
for x in range(0, 56):
    if TX0 <= x < TX1: continue
    rim = [y for y in range(112 if x < 16 else 100, 135) if C(x, y) in RIM and n[y, x, 3]]   # (by the walls, the hall's window whites come first)
    if rim:
        y0 = rim[0]
        if C(x, y0 - 1) == OUTLINE: y0 -= 1                       # (its dark outline above it: one pixel, not a whole wall's edge)
    else:
        y0 = 118                                                  # (the side walls: the waist)
    keep[y0:, x] = True
# the tower's column below the tower itself
keep[118:, TX0:TX1] = True
# 2. the cross tower: in its box, flood the back dome's blues (and outline) in from the box's edges; what the flood
#    does not reach is the tower and its cross; then its outline pixels come back
box = np.zeros((H, W), bool); box[TOP:118, TX0:TX1] = True
seen = np.zeros((H, W), bool); q = deque()
for y in range(TOP, 118):
    for x in (TX0, TX1 - 1): q.append((x, y))
for x in range(TX0, TX1): q.append((x, TOP))
while q:
    x, y = q.popleft()
    if not box[y, x] or seen[y, x]: continue
    c = C(x, y)
    if n[y, x, 3] and c not in BLUES and c != OUTLINE: continue
    seen[y, x] = True
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)): q.append((x + dx, y + dy))
tower = box & ~seen & (n[..., 3] > 0)
for y in range(TOP, 118):
    for x in range(TX0, TX1):
        if seen[y, x] and C(x, y) == OUTLINE and any(0 <= y + dy < H and tower[y + dy, x + dx] for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
            tower[y, x] = True
# only the tower's own piece (the hall's lantern top also falls in the box)
lab = np.zeros((H, W), int); k = 0; sizes = {}
for y0 in range(H):
    for x0 in range(W):
        if tower[y0, x0] and not lab[y0, x0]:
            k += 1; q = deque([(x0, y0)]); lab[y0, x0] = k; sizes[k] = 0
            while q:
                x, y = q.popleft(); sizes[k] += 1
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
                    a, b = x + dx, y + dy
                    if 0 <= a < W and 0 <= b < H and tower[b, a] and not lab[b, a]: lab[b, a] = k; q.append((a, b))
tower = lab == max(sizes, key=sizes.get)
keep |= tower
# the ring cradling the tower's base is a U: inside it (rows 106-117, either side of the tower) is the front dome's
# own blue, which the flood took with the hall's
keep[106:118, TX0:TX1] |= n[106:118, TX0:TX1, 3] > 0
# mirror the left half's decisions onto the right (the art is symmetrical about x 56)
keep[:, 56:] = keep[:, :56][:, ::-1] | keep[:, 56:] & tower[:, 56:]
keep[:, 56:] |= tower[:, 56:]
# the hall's last thin lines (one-pixel spurs) at the dome's top corners: pruned, line end by line end
while True:
    k4 = np.zeros_like(keep, int)
    k4[1:] += keep[:-1]; k4[:-1] += keep[1:]; k4[:, 1:] += keep[:, :-1]; k4[:, :-1] += keep[:, 1:]
    spur = keep & (k4 <= 1); spur[:96] = False; spur[121:] = False
    if not spur.any(): break
    keep &= ~spur
out = n.copy(); out[~keep] = 0
ys = np.nonzero(out[..., 3])[0]
out = out[ys.min():ys.max() + 1]
# hand fixes (front-image coordinates, left side; mirrored): the hall's last tick above the rim's start, and the
# rim's dark top outline where a step of it went with the hall
OUTL = np.array([*OUTLINE, 255]); RIMC = np.array([237, 234, 228, 255])
fix = {(7, 65): None, (8, 65): None, (7, 66): None, (8, 66): None, (7, 67): None, (8, 67): OUTL,
       (25, 62): OUTL, (26, 62): OUTL, (27, 62): OUTL, (28, 62): OUTL, (28, 63): RIMC}
Wf = out.shape[1]
for (x, y), v in fix.items():
    for xx in (x, Wf - 1 - x):
        out[y, xx] = 0 if v is None else v
# pinholes: a transparent pixel walled in on three or more sides takes its neighbours' commonest colour
from collections import Counter
for _ in range(3):
    Hf = out.shape[0]
    for y in range(1, Hf - 1):
        for x in range(1, Wf - 1):
            if out[y, x, 3]: continue
            nb = [tuple(out[y + dy, x + dx]) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if out[y + dy, x + dx, 3]]
            if len(nb) >= 3: out[y, x] = Counter(nb).most_common(1)[0][0]
Image.fromarray(out.astype(np.uint8)).save('front.png')
print('front building', out.shape[1], 'x', out.shape[0], 'px =', out.shape[1] / 16, 'x', out.shape[0] / 16, 'tiles')
