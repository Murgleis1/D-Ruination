"""Full logo mask (POKeMON + Dreamstone Ruination): white fill + near-black outline, connected to the white
letters, inside the logo box; plus enclosed counters."""
from PIL import Image
import numpy as np
from collections import deque
a = np.array(Image.open('dr_title.png'))
LX0, LX1, LY1 = 60, 182, 86
LET = {0}; OUTL = {64, 65, 63}
m = np.zeros_like(a, bool)
q = deque([(y, x) for y in range(LY1) for x in range(LX0, LX1) if a[y, x] in LET])
while q:
    y, x = q.popleft()
    if not (0 <= y < LY1 and LX0 <= x < LX1) or m[y, x] or a[y, x] not in LET | OUTL: continue
    m[y, x] = True; q.extend([(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)])
# counters (holes) enclosed by the letters
out = np.zeros_like(m); q = deque([(y, x) for y in (0, LY1 - 1) for x in range(LX0, LX1)] + [(y, x) for y in range(LY1) for x in (LX0, LX1 - 1)])
while q:
    y, x = q.popleft()
    if not (0 <= y < LY1 and LX0 <= x < LX1) or out[y, x] or m[y, x]: continue
    out[y, x] = True; q.extend([(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)])
holes = np.zeros_like(m); holes[:LY1, LX0:LX1] = ~out[:LY1, LX0:LX1] & ~m[:LY1, LX0:LX1]
small = holes.sum() < 3000
print('logo px', m.sum(), 'enclosed px', holes.sum())
np.save('mask_logo_full.npy', m)
rgb = np.array(Image.open('dr_title.png').convert('RGB')); ov = rgb.copy(); ov[m] = (ov[m] * 0.4 + np.array([0, 255, 0]) * 0.6).astype(np.uint8)
Image.fromarray(ov[:100]).resize((720, 300), Image.NEAREST).save('/tmp/logo_mask.png')
