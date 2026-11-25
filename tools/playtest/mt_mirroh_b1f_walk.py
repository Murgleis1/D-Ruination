"""Mt. Mirroh B1F walked (2026-11-24; the Blast Crater, mock v3, built by tools/art/mt_mirroh/b1f/build_b1f.py). B1F's
only way in is the exterior's secret ladder under a Rock Smash rock (shut in Chapter 1), so this walk runs on a test
ROM whose exterior cave mouth (warp 0) is pointed at B1F's ladder for the test only (made, then the mouth restored, by
the build session; ROM path below).
From the ladder: up the passage, the sinkhole's south lip (the pit holds), round its west side past the pillar ring,
under the temple, up its central stair onto the terrace, along the terrace both ways, the camp, the east side, back to
the ladder and up it to the exterior."""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image, ImageDraw
ROM = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/b1f/b1f_test.gba'
OUT = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/scratch/b1f/b1f_walk.png'
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
X, B = 'MtMirrohExterior', 'MirrohInterior_B1F'
go(g, 'Route13', (8, 1)); press('UP', wait=200)
go(g, X, (13, 11)); press('UP', wait=260); g.run(120); p = where(g)
shot('the landing: the ladder'); check('lands on the ladder', p and p[0] == (20, 37), p)
r = go(g, B, (20, 32)); shot('up the passage'); check('up the passage', r, where(g))
r = go(g, B, (20, 25)); shot("the sinkhole's south lip"); check("to the sinkhole's south lip", r, where(g))
r = go(g, B, (20, 24)); before = where(g); press('UP', 3, wait=30)
check('the pit holds (no walking into it)', r and where(g) == before, where(g))
r = go(g, B, (7, 21)); shot('west of the pit, the pillar ring'); check('round the west side', r, where(g))
r = go(g, B, (12, 11)); shot('under the temple, west'); check('under the temple', r, where(g))
r = go(g, B, (20, 10)); shot('the foot of the stair'); check('to the foot of the stair', r, where(g))
r = go(g, B, (20, 6)); shot('up the stair onto the terrace'); check('up the stair onto the terrace', r, where(g))
r = go(g, B, (10, 6)); shot('the terrace, west end'); check('the terrace west', r, where(g))
r = go(g, B, (30, 6)); shot('the terrace, east end'); check('the terrace east', r, where(g))
press('UP', 4, wait=30); shot('under the back face'); check('the back face holds (stops at row 4)', where(g)[0] == (30, 4), where(g))
r = go(g, B, (7, 31)); shot('the camp'); check('to the camp', r, where(g))
r = go(g, B, (33, 21)); shot('east of the pit'); check('round to the east side', r, where(g))
r = go(g, B, (20, 36)); press('DOWN', wait=260); g.run(120); p = where(g)
shot('up the ladder'); check('the ladder leads up to the exterior (9, 13)', p and p[0] == (9, 13), p)
print('ALL OK' if ok_all else 'PROBLEM')
Sh = Image.new('RGB', (240 * 4, 172 * ((len(shots) + 3) // 4))); dr = ImageDraw.Draw(Sh)
for i, (n, f) in enumerate(shots):
    Sh.paste(Image.fromarray(f), ((i % 4) * 240, (i // 4) * 172 + 12)); dr.text(((i % 4) * 240 + 2, (i // 4) * 172), n, fill=(255, 255, 0))
Sh.save(OUT)
