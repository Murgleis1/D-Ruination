"""Open light sky, 512 x 48 seamless strip: gradient upward from the original clear-sky blues, scattered light
wind-swept clouds in the original wisp's colours.  New colours at palette indices 100-102 (GBA 15-bit)."""
import numpy as np
from PIL import Image
im = Image.open('dr_title.png'); a = np.array(im)
W, R = 512, 48
NEW = {100: (104, 144, 184), 101: (120, 160, 192), 102: (136, 176, 200)}      # zenith -> toward the clear band
rng = np.random.default_rng(41)
S = np.zeros((R, W), np.uint8)
def put(y, x, v):
    if 0 <= y < R: S[y, x % W] = v
# --- gradient: rows 0-6 = 100, 7-13 = 101, 14-21 = 102, 22-42 original clear-sky rows; 2-row checker dither seams
for y in range(R): S[y] = 100 if y < 7 else 101 if y < 14 else 102 if y < 22 else 0
for y in range(22, 43):
    vals, cnt = np.unique(a[y, 176:240], return_counts=True); S[y] = vals[np.argmax(cnt)]
S[43:] = S[42]
B4 = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]])
def dither(y0, upper, lower):                       # rows y0-2 .. y0: 25 / 50 / 75 % of the lower colour (Bayer 4x4)
    for dy, frac in ((-2, 0.25), (-1, 0.5), (0, 0.75)):
        y = y0 + dy
        for x in range(W): S[y, x] = lower if B4[y % 4, x % 4] < frac * 16 else upper
dither(7, 100, 101); dither(14, 101, 102); dither(22, 102, int(S[22, 0]))
STREAK = {27: 17, 28: 17, 29: 17, 30: 16, 31: 17, 32: 15, 33: 16, 34: 15, 37: 8, 39: 8, 40: 9}
for y, v in STREAK.items():                         # faint streaks in the clear band, as in the original
    for _ in range(6):
        x0 = int(rng.integers(0, W)); ln = int(rng.integers(10, 38))
        for x in range(x0, x0 + ln): put(y, x, v)
# --- light clouds: streak stacks, right ends lit; colours from the wisp
def streak(y, x0, ln, top=False):
    for k in range(ln):
        f = k / max(1, ln - 1)
        v = 21 if f < 0.10 else 14 if f < 0.25 else 7 if f < 0.70 else 3
        if top and 0.72 < f < 0.94: v = 10                                   # dusk-pink glint on the top edge
        put(y, x0 + k, v)
def cloud(xr, y0, lens):
    for i, ln in enumerate(lens):
        streak(y0 + i, xr + int(rng.integers(-3, 4)) - ln, ln, top=(i == 0))
    ln = lens[-1]
    for k in range(int(ln * 0.25), int(ln * 0.85)): put(y0 + len(lens), xr - ln + k, 19)      # soft underside
CLOUDS = [(64, 3, [16, 30, 40, 34, 18]), (118, 14, [12, 20]), (178, 6, [20, 36, 50, 56, 44, 24]),
          (232, 25, [10, 18, 14]), (300, 1, [14, 24, 20]), (372, 10, [18, 34, 48, 52, 36, 16]),
          (430, 2, [10, 16]), (500, 17, [16, 28, 34, 22]), (556, 4, [12, 22, 26, 14])]       # last wraps
for c in CLOUDS: cloud(*c)
# the original wisp, once
for y in range(22, 34):
    for x in range(170, 193):
        v = a[y, x]
        if v not in (17, 18, 15, 16, 9, 8, 13, 0, 64, 65, 63): put(y, 140 + (x - 170), v)
np.save('sky_strip512_light.npy', S); np.save('sky_newcols.npy', np.array([[k, *v] for k, v in NEW.items()]))
pal = np.array(im.getpalette()[:768]).reshape(256, 3)
for k, v in NEW.items(): pal[k] = v
Image.fromarray(pal[S].astype(np.uint8)).resize((W * 3, R * 3), Image.NEAREST).save('/tmp/sky_light.png')
