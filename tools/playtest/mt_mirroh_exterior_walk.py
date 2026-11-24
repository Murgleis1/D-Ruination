"""Mt. Mirroh's exterior walked (2026-11-23): Route 13's Mt. Mirroh exit fades onto its foot; up the stair back past
the ledge; the plateau path to the cave mouth; into 1F and back out; the bridge over the lower river; the ledge jumped
down from the foot; the secret ladder's rock in place; back down to Route 13."""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
import walklib, struct, re
# wild battles: the mountain keeps Dreamstone Mysteries' encounters until stage 5; the walk runs from them (B moves
# the text on and backs out of any submenu; RIGHT, DOWN is RUN in the action menu)
MAPTXT = open('/home/claude/repo/codebase/pokeemerald.map').read()
sym = lambda n: int(re.search(r'\s+0x([0-9a-f]+)\s+' + n + r'\n', MAPTXT).group(1), 16)
GMAIN, BCB2, OWCB2 = sym('gMain'), sym('BattleMainCB2'), sym('CB2_Overworld')
def cb2(g): st = bytes(g.state()); return struct.unpack_from('<I', st, 0x19000 + GMAIN - 0x03000000 + 4)[0] & ~1
BATTLES = [0]
def flee(g):
    for _ in range(30):                                   # (a battle's intro runs on other callbacks: wait it out)
        if cb2(g) in (OWCB2, BCB2): break
        g.run(10)
    if cb2(g) != BCB2: return
    BATTLES[0] += 1
    for _ in range(30):
        if cb2(g) == OWCB2: break
        for b_ in ('B', 'B', 'B', 'B', 'RIGHT', 'DOWN', 'A', 'B', 'B', 'B', 'B'): g.run(6, b_); g.run(30)
    for _ in range(30):
        if cb2(g) == OWCB2: break
        g.run(10)
    g.run(40)
_step = walklib.step
def step(g, d): _step(g, d); flee(g)
walklib.step = step
from PIL import Image, ImageDraw
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
g.restore(gzip.decompress(open('/home/claude/scratch/r13/route13_entry.state', 'rb').read())); g.run(10)
shots = []; ok_all = True
def shot(n): g.run(20); shots.append((n, g.frame().copy()))
def press(d, n=1, wait=40):
    for _ in range(n): g.run(12, d); g.run(14)
    g.run(wait)
def check(name, cond, info=''):
    global ok_all
    print('%-46s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok_all &= bool(cond)
X = 'MtMirrohExterior'
go(g, 'Route13', (8, 1), log=lambda *a: None); press('UP', wait=200); p = where(g); shot('arrived at the foot')
check('Route 13 fades onto the foot', p[0][0] in (38, 39) and p[0][1] >= 77, p); mx = p[1]

r = go(g, X, (37, 44), log=lambda *a: None); check('up the stair past the ledge', r, where(g)); shot('the stair up')
r = go(g, X, (13, 11), log=lambda *a: None); check('to the cave mouth', r, where(g)); shot('the cave mouth')
press('UP', wait=200); p = where(g); shot('into 1F')
check('into 1F', p[1] != mx, p); m1 = p[1]
press('DOWN', wait=200); p = where(g)
if p[1] == m1: press('DOWN', wait=200); p = where(g)
check('back out of 1F to the cave mouth', p[1] == mx and p[0] in ((13, 11), (13, 10)), p)
r = go(g, X, (10, 13), log=lambda *a: None); press('LEFT', wait=30); shot('the rock on the ladder'); p = where(g)
check('the Rock Smash rock blocks the ladder', r and p[0] == (10, 13), p)
r = go(g, X, (15, 55), log=lambda *a: None); r2 = go(g, X, (21, 55), log=lambda *a: None); shot('across the bridge')
check('across the new bridge', r and r2, where(g))
r = go(g, X, (32, 51), log=lambda *a: None); press('DOWN', wait=60); p = where(g)
check('down the ledge from the foot side', r and p[0][1] >= 53, p)
r = go(g, X, (38, 78), log=lambda *a: None); press('DOWN', wait=200); p = where(g); shot('back on Route 13')
check('back down to Route 13', p[1] != mx and p[0] in ((8, 1), (9, 1)), p)
print('wild battles run from:', BATTLES[0]); print('ALL OK' if ok_all else 'PROBLEM')
S = Image.new('RGB', (240 * 4, 172 * ((len(shots) + 3) // 4))); dr = ImageDraw.Draw(S)
for i, (n, f) in enumerate(shots):
    S.paste(Image.fromarray(f), ((i % 4) * 240, (i // 4) * 172 + 12)); dr.text(((i % 4) * 240 + 2, (i // 4) * 172), n, fill=(255, 255, 0))
S.save('/home/claude/scratch/r13/mtx_walk.png')
