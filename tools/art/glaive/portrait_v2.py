"""Glaive portraits v2: narrower eyes (approved 2026-11-26), unkempt hair at the back (no spikes: a few loose
clumps of uneven size that follow the existing lock bands and droop past the silhouette), light scarring on the
cheek facing the viewer (2026-11-27). Run: python3 portrait_v2.py [--write]"""
import sys, os
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from portrait_v1 import eyes, C

OUT, MAIN, DARK, SHADE, HI, DEEP = 13, 4, 10, 14, 12, 2
HAIR = {2, 4, 10, 12, 14, 13}

# (base, control, tip, half-width at base). Bezier centreline from inside the hair out past the back edge.
LOCKS = [
    ((22, 26), (16, 25), (15, 29), 3.4),   # upper band (highlight streak y24-28)
    ((21, 33), (14, 32), (12, 36), 3.8),   # middle band, the biggest clump
    ((20, 41), (15, 41), (15, 45), 3.2),   # lower band, droops by the ear
]

def bez(p0, p1, p2, t):
    return ((1 - t) ** 2 * np.array(p0) + 2 * (1 - t) * t * np.array(p1) + t * t * np.array(p2))

def hair(a):
    orig = a.copy()
    for p0, p1, p2, w in LOCKS:
        ts = np.linspace(0, 1, 200); pts = np.array([bez(p0, p1, p2, t) for t in ts])
        tang = np.gradient(pts, axis=0); tang /= np.linalg.norm(tang, axis=1)[:, None]
        nrm = np.stack([tang[:, 1], -tang[:, 0]], 1)          # points "up" for a lock heading left
        if nrm[0, 1] > 0: nrm = -nrm
        for y in range(8, 60):
            for x in range(2, 40):
                if orig[y, x] not in (0, OUT): continue
                c = np.array([x + .5, y + .5]); d = np.linalg.norm(pts - c, axis=1); i = d.argmin()
                t = ts[i]; hw = w * (1 - t) ** 0.6 + 1.3 * t
                if d[i] > hw: continue
                side = np.dot(c - pts[i], nrm[i]) / hw            # +1 top edge .. -1 bottom edge
                a[y, x] = HI if (side > .35 and t < .55) else MAIN if side > -.2 else SHADE if side > -.65 else DARK
    # outline: hair next to background is outline; old outline swallowed by a lock becomes dark strand line
    for y in range(8, 60):
        for x in range(2, 40):
            v = a[y, x]
            if v not in HAIR: continue
            bg = any(a[y + dy, x + dx] == 0 for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            if bg: a[y, x] = OUT
            elif v == OUT: a[y, x] = DARK
    # tidy the pixel clusters: lone nubs (background on 3 sides) go, 1-px pits (hair on 3 sides) close up
    N4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for y in range(8, 60):
        for x in range(2, 40):
            nb = sum(a[y + dy, x + dx] == 0 for dx, dy in N4)
            if a[y, x] == OUT and nb >= 3: a[y, x] = 0
            elif a[y, x] == 0 and nb <= 1: a[y, x] = OUT
    return a

# Light scarring on the near cheek: one healed slash running down toward the jaw and a short nick under it.
SCAR = [(40, 53, 7), (41, 54, 7), (41, 55, 3), (42, 56, 7), (43, 57, 7), (44, 58, 7),
        (39, 58, 7), (40, 59, 7)]

def scar(a):
    for x, y, c in SCAR:
        if a[y, x] == 1: a[y, x] = c
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
        a = a0.copy(); eyes(a); hair(a); scar(a)
        cells += [render(a0, pal), render(a, pal)]
        if write:
            o = Image.fromarray(a, 'P'); o.putpalette(im.getpalette()); o.save(p)
    S = Image.new('RGB', (480 * 2 + 10, 480 * 3 + 20), (255, 255, 255))
    for k, c in enumerate(cells): S.paste(c, ((k % 2) * 490, (k // 2) * 490))
    S.save('/tmp/gl/portraits_v2.png'); print(S.size)
