"""Glaive portraits: narrower eyes, spikier hair at the back (user 2026-11-26). Patches drawn as text over the 80x80
portraits (same layout in neutral / positive / negative). Run: python3 portrait_v1.py [--write]"""
import sys, os
import numpy as np
from PIL import Image, ImageDraw
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'codebase', 'graphics', 'portraits')
H = '0123456789ABCDEF'
def patch(a, x0, y0, rows):
    for dy, r in enumerate(rows):
        for dx, ch in enumerate(r):
            if ch == '.': continue
            a[y0 + dy, x0 + dx] = 0 if ch == ' ' else H.index(ch)

def eyes(a):
    # left eye: lid moves down a row (y44 -> brow shade, y45 -> lid), the bottom white row becomes skin
    a[44, 40:48] = 3
    a[45, 41:48] = 2
    a[46, 42] = 11                      # catchlight
    for x in range(45, 48):
        if a[49, x] == 6: a[49, x] = 7
    # right eye: lid down a row
    a[51, 59:63] = 3
    a[52, 59:63] = 2
    a[53, 60] = 11

# Unkempt back (user 2026-11-27: "more unkempt in the back, not a bunch of spikes"): the silhouette at the back of
# the head breaks into uneven clumps, each bulging a pixel or two past the old edge with a small notch between them,
# the clumps hanging down like loose locks. LEFT: per-row offset of the left edge (+ out, - in) from row Y0;
# TOP: per-column offset of the top edge (+ up) from column X0.
Y0 = 18
LEFT = [1, 2, 1, -1, 0, 1, 2, 2, 1, -1, 0, 1, 2, 3, 2, 1, -1, 0, 1, 2, 2, 1, 0, -1, 0, 1, 2, 1, 0]
X0 = 18
TOP = [0, 1, 1, 0, -1, 0, 1, 2, 1, 0, 0, 1, 1, 0]
OUT, MAIN, DARK, SHADE, HI = 13, 4, 10, 14, 12

def hair(a):
    for k, d in enumerate(LEFT):
        y = Y0 + k; x = np.nonzero(a[y])[0][0]
        if d > 0:
            fill = a[y, x + 1] if a[y, x + 1] not in (0, OUT) else MAIN
            a[y, x] = fill if fill != HI else SHADE
            a[y, x - d + 1:x] = SHADE if d > 1 else fill
            a[y, x - d] = OUT
        elif d < 0:
            a[y, x] = 0; a[y, x + 1] = OUT
    for k, d in enumerate(TOP):
        x = X0 + k; ys = np.nonzero(a[:, x])[0]
        if not len(ys): continue
        y = ys[0]
        if d > 0:
            a[y, x] = SHADE
            a[y - d + 1:y, x] = SHADE
            a[y - d, x] = OUT
        elif d < 0:
            a[y, x] = 0; a[y + 1, x] = OUT
    # re-outline the back of the head: hair touching the background is outline, old outline now inside is shade
    HAIR = {2, 4, 10, 12, 14, 13}
    for _ in range(2):
        for y in range(8, 41):
            for x in range(2, 34):
                v = a[y, x]
                if v not in HAIR: continue
                bg = any(a[y + dy, x + dx] == 0 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
                if bg and v != OUT: a[y, x] = OUT
                elif not bg and v == OUT: a[y, x] = SHADE
    # lone outline pixels sticking out (background on three sides) are dropped
    for y in range(8, 41):
        for x in range(2, 34):
            if a[y, x] == OUT and sum(a[y + dy, x + dx] == 0 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))) >= 3:
                a[y, x] = 0
    return a

def render(a, pal, s=6):
    rgb = np.array(pal, np.uint8)[a]; rgb[a == 0] = (210, 228, 210)
    return Image.fromarray(rgb).resize((80 * s, 80 * s), 0)

if __name__ == '__main__':
    write = '--write' in sys.argv
    cells = []
    for n in ('neutral', 'positive', 'negative'):
        p = os.path.join(C, 'glaive_%s.png' % n); im = Image.open(p); a0 = np.array(im)
        pal = [tuple(im.getpalette()[3 * i:3 * i + 3]) for i in range(16)]
        a = a0.copy(); eyes(a); hair(a)
        cells += [render(a0, pal), render(a, pal)]
        if write:
            o = Image.fromarray(a, 'P'); o.putpalette(im.getpalette()); o.save(p)
    S = Image.new('RGB', (480 * 2 + 10, 480 * 3 + 20), (255, 255, 255))
    for k, c in enumerate(cells): S.paste(c, ((k % 2) * 490, (k // 2) * 490))
    S.save('/tmp/gl/portraits_v1.png'); print(S.size)
