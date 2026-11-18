"""Sky mask v2: original sky mask + letter counters (holes inside the logo) + the old dark-sky transition
line on row 21 next to the cliff, so the new light sky shows through all of them."""
import numpy as np
from PIL import Image
from collections import deque
a = np.array(Image.open('dr_title.png')); sky = np.load('mask_sky.npy'); logo = np.load('mask_logo_full.npy')
LX0, LX1, LY1 = 60, 182, 86
out = np.zeros_like(logo); q = deque([(y, x) for y in (0, LY1 - 1) for x in range(LX0, LX1)] + [(y, x) for y in range(LY1) for x in (LX0, LX1 - 1)])
while q:
    y, x = q.popleft()
    if not (0 <= y < LY1 and LX0 <= x < LX1) or out[y, x] or logo[y, x]: continue
    out[y, x] = True; q.extend([(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)])
holes = np.zeros_like(logo); holes[:LY1, LX0:LX1] = ~out[:LY1, LX0:LX1] & ~logo[:LY1, LX0:LX1]; holes[43:] = False
line = np.zeros_like(sky); line[21, 20:42] = (a[21, 20:42] == 36)
np.save('mask_sky2.npy', sky | holes | line)
