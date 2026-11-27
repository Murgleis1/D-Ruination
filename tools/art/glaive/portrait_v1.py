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

# Spikes, after MonoMyth's #109 (the user's pick, 2026-11-27): a few big tufts, thick at the root and tapering to a
# point, curving; a black outline (13) where they meet the background, the very tip in dark brown (2) instead of
# black, a highlight streak (12) along the upper side and a dark band (10) along the underside.
# Each tuft: a centreline from inside the hair out to the tip, (x, y) points, and its root half-width.
TUFTS = [([(27, 18), (25, 14), (24, 11), (24, 9), (25, 8)], 3.4),     # crown, standing up and curling over
         ([(21, 25), (17, 23), (14, 22), (11, 22)], 3.2),             # back, out to the left
         ([(18, 35), (15, 35), (12, 37)], 2.6)]                       # lower back, a short flick down
OUT, TIP, MAIN, DARK, SHADE, HI = 13, 2, 4, 10, 14, 12

def hair(a):
    for line, w0 in TUFTS:
        seg = []                                   # sample the centreline densely
        for (x0, y0), (x1, y1) in zip(line, line[1:]):
            n = int(max(abs(x1 - x0), abs(y1 - y0)) * 4) + 1
            seg += [(x0 + (x1 - x0) * t / n, y0 + (y1 - y0) * t / n) for t in range(n)]
        seg.append(line[-1]); N = len(seg)
        R = [max(0.6, w0 * (1 - k / (N - 1)) ** 0.55) for k in range(N)]
        mask = set()
        for k, (cx, cy) in enumerate(seg):
            r = R[k]
            for y in range(int(cy - r) - 1, int(cy + r) + 2):
                for x in range(int(cx - r) - 1, int(cx + r) + 2):
                    if (x + 0.5 - cx) ** 2 + (y + 0.5 - cy) ** 2 <= r * r: mask.add((x, y))
        new = [(x, y) for (x, y) in mask if a[y, x] in (0, OUT)]
        for x, y in new:
            k = min(range(N), key=lambda i: (seg[i][0] - x - 0.5) ** 2 + (seg[i][1] - y - 0.5) ** 2)
            k2 = min(k + 1, N - 1); k1 = max(k - 1, 0)
            tx, ty = seg[k2][0] - seg[k1][0], seg[k2][1] - seg[k1][1]; L = max(1e-6, (tx * tx + ty * ty) ** 0.5)
            nx, ny = -ty / L, tx / L
            if ny > 0: nx, ny = -nx, -ny               # the normal that points up: the upper side
            side = (x + 0.5 - seg[k][0]) * nx + (y + 0.5 - seg[k][1]) * ny
            a[y, x] = HI if side > 0.25 * R[k] else DARK if side < -0.45 * R[k] else MAIN
        for x, y in new:
            if any(a[y + ddy, x + ddx] == 0 for ddx, ddy in ((1, 0), (-1, 0), (0, 1), (0, -1))): a[y, x] = OUT
        tx, ty = line[-1]
        for x, y in new:                           # the tip: dark brown, not black
            if abs(x + 0.5 - tx) <= 1.2 and abs(y + 0.5 - ty) <= 1.2 and a[y, x] == OUT: a[y, x] = TIP

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
