"""The church in Arceus's colours (user 2026-11-22: "gold and blue combination; the church HQ echoes the colour of
Arceus itself"): Arceus is cream-white with a golden wheel. The great dome stays blue; gold goes on the ring that
cradles the cross tower (the wheel), the great dome's ribs, the two small dome caps and the cross; the cream walls,
the door and the stained glass stay. Each gilded pixel keeps its lightness (cream ramp -> gold ramp).
Input front.png (cut_front.py); output front_arceus.png."""
import numpy as np
from PIL import Image

a = np.array(Image.open('front.png').convert('RGBA')).astype(int)
H, W = a.shape[:2]
op = a[..., 3] > 0
OUTLINE = (49, 56, 82)
lum = lambda c: .30 * c[0] + .59 * c[1] + .11 * c[2]
def blue(c): return c[2] > c[0] + 25 and c[2] > c[1] + 20 and lum(c) < 110
def cream(c): return not blue(c) and c != OUTLINE and abs(c[0] - c[2]) < 70 and c[0] >= c[2] and lum(c) > 80
C = lambda x, y: tuple(a[y, x, :3])

region = np.zeros((H, W), bool)
def rect(x0, x1, y0, y1): region[y0:y1 + 1, x0:x1 + 1] = True
rect(44, 67, 0, 16)                 # the cross
rect(38, 74, 16, 46)                # the tower's cap (above its window band)
rect(33, 79, 56, 86)                # the ring round the tower's base ...
region[47:69, 41:72] = False        # ... not the tower's own body
rect(34, 78, 112, 149)              # the front tower's cap (above the rose window)
gild = np.zeros((H, W), bool)
for y in range(H):
    for x in range(W):
        if op[y, x] and region[y, x] and cream(C(x, y)): gild[y, x] = True
# the great dome's ribs: thin pale lines with blue (or outline) both sides
for y in range(60, 120):
    for x in range(1, W - 1):
        if not op[y, x] or region[y, x] or not cream(C(x, y)): continue
        nb = lambda dx, dy: op[y + dy, x + dx] and (blue(C(x + dx, y + dy)) or C(x + dx, y + dy) == OUTLINE)
        if (nb(-1, 0) and nb(1, 0)) or (nb(0, -1) and nb(0, 1)) or (nb(-1, -1) and nb(1, 1)) or (nb(1, -1) and nb(-1, 1)):
            gild[y, x] = True
GOLD = [(96, 62, 18), (146, 98, 30), (192, 142, 44), (226, 182, 66), (244, 214, 116), (252, 240, 182)]
cs = sorted({C(x, y) for y in range(H) for x in range(W) if gild[y, x]}, key=lum)
lo, hi = lum(cs[0]), lum(cs[-1])
out = a.copy()
for c in cs:
    g = GOLD[int(round((lum(c) - lo) / (hi - lo) * (len(GOLD) - 1)))]
    m = gild & (a[..., :3] == c).all(-1); out[m, :3] = g
Image.fromarray(out.astype(np.uint8)).save('front_arceus.png')
print('gilded', int(gild.sum()), 'px;', len(cs), 'cream shades ->', len(GOLD), 'golds')
