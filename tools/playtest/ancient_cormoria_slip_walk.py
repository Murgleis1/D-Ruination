"""The Ancient Cormoria slip walked (2026-11-24; mock v3, built by tools/art/ancient_cormoria/build_slip.py). The slip
is reached by script (stage 3), so this walk runs on a test ROM whose Mt. Mirroh exterior door (warp 0) is pointed at
the slip's landing for the test only (made, then the door restored, by the build session; ROM path below).
From the landing at the south altar: under the ribs, by the skull, up the stairs in the step, to the oasis, over the
rope bridge, up the stairs in the north wall, up the neck to the north altar, to the summit's west rim; the falls and
the river are not walked into."""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image, ImageDraw
ROM = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/anc2/slip_test.gba'
g = GBA(ROM)
g.restore(gzip.decompress(open('/home/claude/scratch/r13/route13_entry.state', 'rb').read())); g.run(10)
shots = []; ok_all = True
def shot(n): g.run(20); shots.append((n, g.frame().copy()))
def press(d, n=1, wait=40):
    for _ in range(n): g.run(12, d); g.run(14)
    g.run(wait)
def check(name, cond, info=''):
    global ok_all
    print('%-46s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok_all &= bool(cond)
_go = go
def go(g, m, t, tries=4):
    for _ in range(tries):
        if _go(g, m, t, log=lambda *a: None): return True
        for _ in range(60): g.run(6, 'B'); g.run(12)
    return False
X, S = 'MtMirrohExterior', 'AncientCormoriaSlip'
go(g, 'Route13', (8, 1)); press('UP', wait=200)
go(g, X, (13, 11)); press('UP', wait=260); g.run(120); p = where(g)
shot('the landing: the south altar'); check('lands at the south altar', p and p[0] == (24, 50), p)
r = go(g, S, (24, 45)); shot('under the ribs'); check('north under the ribs', r, where(g))
r = go(g, S, (38, 44)); shot('by the skull'); check('east to the skull', r, where(g))
r = go(g, S, (24, 36)); shot('below the step'); check('to the foot of the step', r, where(g))
r = go(g, S, (24, 30)); shot('up the stairs in the step'); check('up the stairs onto the plain', r, where(g))
r = go(g, S, (39, 30)); shot('the oasis'); check('to the oasis', r, where(g))
r = go(g, S, (24, 28)); r2 = go(g, S, (24, 22)); shot('over the rope bridge'); check('over the rope bridge', r and r2, where(g))
r = go(g, S, (11, 20)); shot('below the Tyrantrum'); check('west under the Tyrantrum', r, where(g))
r = go(g, S, (24, 19)); shot('below the north wall'); check('to the foot of the north wall', r, where(g))
r = go(g, S, (24, 14)); shot('up the stairs in the north wall'); check('up the stairs', r, where(g))
r = go(g, S, (24, 10)); shot('up the neck'); check('up the neck', r, where(g))
r = go(g, S, (24, 6)); press('UP', wait=30); shot('the north altar'); check('before the north altar', r, where(g))
r = go(g, S, (20, 7)); press('LEFT', wait=30); shot('the summit, west rim'); check('the west rim', r, where(g))
before = where(g); press('LEFT', 3, wait=30); check('the rim holds (no walking into the sky)', where(g) == before, where(g))
r = go(g, S, (29, 7)); press('RIGHT', wait=30); shot('the summit, east rim'); check('the east rim', r, where(g))
print('ALL OK' if ok_all else 'PROBLEM')
Sh = Image.new('RGB', (240 * 4, 172 * ((len(shots) + 3) // 4))); dr = ImageDraw.Draw(Sh)
for i, (n, f) in enumerate(shots):
    Sh.paste(Image.fromarray(f), ((i % 4) * 240, (i // 4) * 172 + 12)); dr.text(((i % 4) * 240 + 2, (i // 4) * 172), n, fill=(255, 255, 0))
Sh.save('/home/claude/scratch/slipwalk/slip_walk.png')
