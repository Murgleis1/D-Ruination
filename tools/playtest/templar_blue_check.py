"""The Templar's overworld in the Order's blue, seen in the game (2026-11-25): from Pelluca's west gate (save state
r11/pelluca_west.state) to the north road guard at (38, 3); matches her frames on screen against the PNG.
Usage: python3 tools/playtest/templar_blue_check.py [OUT.png]"""
import sys, gzip
import numpy as np
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/templar_blue_check.png'
CB = '/home/claude/repo/codebase/'
im = Image.open(CB + 'graphics/object_events/pics/people/templar.png')
IDX = np.array(im); PAL = np.array(im.getpalette()[:48]).reshape(16, 3).astype(int) // 8 * 8


def match(f):
    a = f.astype(int) // 8 * 8
    best = None
    for k in range(9):
        idx = IDX[:, k * 16:(k + 1) * 16]; m = idx != 0
        ys, xs = np.nonzero(m); w = PAL[idx][ys, xs]
        oy, ox = np.mgrid[0:160 - 32 + 1, 0:240 - 16 + 1]
        bad = (np.abs(a[oy[..., None] + ys, ox[..., None] + xs] - w).max(-1) > 8).sum(-1)
        y, x = np.unravel_index(bad.argmin(), bad.shape)
        if best is None or bad[y, x] < best[0]:
            best = (int(bad[y, x]), int(x), int(y), k, int(m.sum()))
    return best


g = GBA(CB + 'pokeemerald.gba')
g.restore(gzip.decompress(open('/home/claude/scratch/r11/pelluca_west.state', 'rb').read())); g.run(20)
for _ in range(4): g.walk('RIGHT', 1); g.run(10)
ok = False
for tgt in ((38, 6), (38, 7), (37, 6)):
    for _ in range(4):
        if go(g, 'PellucaCity', tgt, log=lambda *a: None):
            ok = True; break
        for _ in range(40): g.run(6, 'B'); g.run(10)
    if ok: break
g.run(30)
f = g.frame()
b = match(f)
print('walked near the north road guard:', ok, where(g))
print('Templar on screen: frame %d at (%d, %d), %d of %d pixels differ' % (b[3], b[1], b[2], b[0], b[4]))
print('ALL OK' if ok and b[0] == 0 else 'PROBLEM')
x, y = b[1], b[2]
Image.fromarray(f).resize((480, 320), Image.NEAREST).save(OUT)
Image.fromarray(f).crop((max(0, x - 24), max(0, y - 16), x + 40, y + 48)).resize((256, 256), Image.NEAREST).save(OUT.replace('.png', '_crop.png'))
