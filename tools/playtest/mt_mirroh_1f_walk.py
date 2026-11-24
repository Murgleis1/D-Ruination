"""Mt. Mirroh 1F walked (2026-11-23), re-drawn in Glittering Grotto's grammar (plan_1f.py): in from the exterior at the
way in; the rest stop; bridge 2, the middle cave, bridge 1, the west cave; stair A onto the upper level; stair B into
the top band; the rubble's text; the torture chamber; out onto the Peak and back; the ledge down; out to the exterior."""
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
X = 'MtMirrohExterior'; F = 'MirrohInterior_1F'
# Dreamstone Mysteries' nurse quest (its trigger at x 47, rows 44-46) still starts on the way in (a stage-3 question):
# the walk talks through it (B moves its text on) and tries again
_go = go
def go(g, m, t, log=None, tries=4):
    for _ in range(tries):
        if _go(g, m, t, log=log): return True
        for _ in range(60): g.run(6, 'B'); g.run(12)
    return False
# Dreamstone Mysteries' two Magma grunts by the old Peak exit (6, 8-9; their trigger at x 8) stand in the way of the
# rubble until stage 2 replaces them: the walk treats them as already beaten (their flag set: they are hidden)
# SaveBlock1's flags sit at +5260 (offsetof with the build's own -mabi=apcs-gnu; the 5220 used before was wrong)
FLAGS = 5260
def get_flag(g, f):
    st = g.state(); sb1 = struct.unpack_from('<I', st, walklib.IW + (0x03006A08 - 0x03000000))[0]
    return (st[walklib.EW + (sb1 - 0x02000000) + FLAGS + f // 8] >> (f % 8)) & 1, hex(sb1)
def set_flag(g, f):
    st = bytearray(g.state()); sb1 = struct.unpack_from('<I', st, walklib.IW + (0x03006A08 - 0x03000000))[0]
    o = walklib.EW + (sb1 - 0x02000000) + FLAGS + f // 8; st[o] |= 1 << (f % 8); g.restore(bytes(st)); g.run(2)
_Grid = walklib.Grid
class Grid(_Grid):
    def __init__(self, m):
        _Grid.__init__(self, m)
        if m == 'MirrohInterior_1F': self.objs -= {(6, 8), (6, 9)}
walklib.Grid = Grid
go(g, 'Route13', (8, 1), log=lambda *a: None); press('UP', wait=200)
r = go(g, X, (13, 11), log=lambda *a: None); press('UP', wait=200); g.run(120); p = where(g); shot('the way in'); m1 = p[1]
check('into 1F at the way in', r and p[0] in ((55, 58), (55, 57)), p)
r = go(g, F, (41, 41), log=lambda *a: None); shot('the rest stop'); check('the rest stop', r, where(g))
r = go(g, F, (33, 30), log=lambda *a: None); shot('over bridge 2, the middle cave'); check('over bridge 2', r, where(g))
r = go(g, F, (17, 26), log=lambda *a: None); shot('over bridge 1, the west cave'); check('over bridge 1', r, where(g))
r = go(g, F, (10, 15), log=lambda *a: None); shot('up stair A'); check('up stair A onto the upper level', r, where(g))
r = go(g, F, (38, 7), log=lambda *a: None); shot('up stair B'); check('up stair B into the top band', r, where(g))
r = go(g, F, (4, 3), log=lambda *a: None); press('UP', wait=10); g.run(6, 'A'); g.run(90); shot('the rubble'); g.run(6, 'A'); g.run(90); shot('the rubble, 2')
check('west along the top band to the rubble', r, where(g))
for _ in range(4): g.run(6, 'B'); g.run(30)
r = go(g, F, (50, 6), log=lambda *a: None); shot('the torture chamber'); check('east to the torture chamber', r, where(g))
r = go(g, F, (54, 2), log=lambda *a: None); press('UP', wait=30); press('UP', wait=200); p = where(g); shot('onto the Peak')
check('the exit leads onto the Peak', r and p[1] != m1, p); mp = p[1]
press('UP', wait=200); p = where(g)
if p[1] == mp: press('UP', wait=200); p = where(g)
g.run(120); shot('back into 1F'); check('the Peak leads back to 1F', mp != m1 and p[1] == m1 and p[0] in ((54, 1), (54, 2)), p)
press('DOWN', wait=40)
r = go(g, F, (52, 9), log=lambda *a: None); press('DOWN', wait=60); p = where(g); shot('the ledge down')
check('the ledge hops down to the east passage', r and p[0] == (52, 11), p)
r = go(g, F, (55, 57), log=lambda *a: None); press('DOWN', wait=60); p = where(g)
if p[1] == m1: press('DOWN', wait=200); p = where(g)
shot('out to the exterior'); check('out to the exterior cave mouth', p[1] != m1 and p[0][0] == 13, p)
print('ALL OK' if ok_all else 'PROBLEM')
S = Image.new('RGB', (240 * 4, 172 * ((len(shots) + 3) // 4))); dr = ImageDraw.Draw(S)
for i, (n, f) in enumerate(shots):
    S.paste(Image.fromarray(f), ((i % 4) * 240, (i // 4) * 172 + 12)); dr.text(((i % 4) * 240 + 2, (i // 4) * 172), n, fill=(255, 255, 0))
S.save('/home/claude/scratch/r13/m1f_walk.png')
