"""256 x 48 seamless sky strip for the animated title (BG1), painted in the title's own sky style and colours.
Rules read from the original sky (dr_title.png rows 0-42):
  rows 0-13  dark purple base (40); clouds = long horizontal streaks: body 31, lit top 30 (28 at the centre),
             thin underside 32/33, stair-stepped ends in 36/38, a few grey-teal flecks 45/46 at the edges
  rows 14-20 a slightly lighter purple band (38) with a ragged top; row 21 a 36 transition line
  rows 22-42 light-blue bands (18 -> 17/16/15 -> 9/8) with faint streaks and 13 specks; the wisp, once
Everything is placed modulo 256, so the strip wraps seamlessly."""
from PIL import Image
import numpy as np
im = Image.open('dr_title.png'); a = np.array(im)
import sys
W = int(sys.argv[1]) if len(sys.argv) > 1 else 256
R = 48
rng = np.random.default_rng(29)
S = np.zeros((R, W), np.uint8)
def put(y, x, v):
    if 0 <= y < R: S[y, x % W] = v
# --- bands
S[0:14] = 40
S[14:21] = 38
x = 0                                                # ragged top of the 38 band, in clumps (runs), like the original
while x < W:
    run = int(rng.integers(3, 14)); gap = int(rng.integers(6, 30))
    for k in range(run): S[14, (x + k) % W] = 40
    if rng.random() < 0.4:
        for k in range(1, max(2, run - 3)): S[15, (x + k) % W] = 40
    x += run + gap
S[21] = 36
src_rows = {y: a[y, 176:240] for y in range(22, 43)}
for y in range(22, 43):
    vals, cnt = np.unique(src_rows[y], return_counts=True); S[y] = vals[np.argmax(cnt)]
# faint streaks in the blue (neighbouring tones, as in the original)
STREAK = {27: 17, 28: 17, 29: 17, 30: 16, 31: 17, 32: 15, 33: 16, 34: 15, 37: 8, 39: 8, 40: 9}
for y, v in STREAK.items():
    for _ in range(3 * W // 256):
        x0 = int(rng.integers(0, W)); ln = int(rng.integers(10, 38))
        for x in range(x0, x0 + ln): put(y, x, v)
for _ in range(14 * W // 256):                                  # specks in the lowest rows
    put(int(rng.integers(39, 43)), int(rng.integers(0, W)), 13)
# --- clouds: long, thin, wind-swept streaks (as in the original): each streak 1 row, 30-85 px, layered in
#     groups with long steps on the left; shaded along the length -- trailing left tail 38 -> 36, body 31,
#     lit toward the right end 30 (28 on the uppermost streak), thin 32 underside under the lowest one
def streak(y, x0, ln, top=False):
    for k in range(ln):
        f = k / max(1, ln - 1)
        v = 38 if f < 0.12 else 36 if f < 0.24 else 31 if f < 0.62 else 30
        if top and 0.7 < f < 0.92: v = 28
        put(y, x0 + k, v)
    if rng.random() < 0.4: put(y, x0 - 1, 45 if rng.random() < 0.5 else 46)
def group(xr, y0, lens):
    """Right ends roughly aligned at xr (the lit side, jitter +-3); each row's length in lens, so the left starts
    step out further as the rows go down and trail darker tails -- as in the original's big cloud."""
    for i, ln in enumerate(lens):
        jit = int(rng.integers(-3, 4))
        streak(y0 + i, xr + jit - ln, ln, top=(i == 0))
    ln = lens[-1]
    for k in range(int(ln * 0.35), int(ln * 0.9)): put(y0 + len(lens), xr - ln + k, 32)
GROUPS = [
    (70,  1, [22, 38, 52, 64, 70, 46]),
    (124, 6, [18, 34, 44, 30]),
    (150, 0, [16, 26]),
    (246, 2, [26, 44, 60, 78, 92, 98, 84, 56, 30]),
    (300, 9, [14, 30, 40]),
]
if W == 512:
    GROUPS = GROUPS[:-1] + [
        (292, 9, [14, 30, 40]),
        (352, 3, [20, 36, 50, 44, 26]),
        (398, 0, [12, 22]),
        (470, 1, [22, 40, 56, 70, 80, 72, 50, 28]),
        (528, 8, [16, 28, 36]),                      # wraps past 512 into the start
    ]
for (xr, y0, lens) in GROUPS: group(xr, y0, lens)
# --- the original wisp, copied once (rows 22-33, x 170-192 where it is not plain blue)
for y in range(22, 34):
    for x in range(170, 193):
        v = a[y, x]
        if v not in (17, 18, 15, 16, 9, 8, 13, 0, 64, 65, 63):
            put(y, 120 + (x - 170), v)
S[43:48] = S[42]
np.save('sky_strip.npy' if W == 256 else 'sky_strip%d.npy' % W, S)
two = np.concatenate([S, S], 1)
t = Image.fromarray(two, 'P'); t.putpalette(im.getpalette()[:768])
t.convert('RGB').resize((W * 4, 192), Image.NEAREST).save('/tmp/sky_strip.png')
