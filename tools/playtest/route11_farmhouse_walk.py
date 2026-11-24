"""Route 11's farmhouse walked (2026-11-24; tools/art/route11/build_farmhouse.py, variant B): from Route 11's road up
to the cottage's door, in, round the room (the table, the beds, the hay corner), back out by the mat onto Route 11."""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image, ImageDraw
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
g.restore(gzip.decompress(open('/home/claude/scratch/r11/r11_entry.state', 'rb').read())); g.run(10)
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
R, F = 'Route11', 'Route11Farmhouse'
r = go(g, R, (55, 15)); shot('before the farmhouse door'); check('to the farmhouse door', r, where(g)); m0 = where(g)[1]
press('UP', wait=200); g.run(60); p = where(g); shot('inside'); check('in through the door, on the mat', p and p[1] != m0 and p[0][1] == 8, p)
r = go(g, F, (6, 6)); shot('by the table'); check('by the table', r, where(g))
r = go(g, F, (8, 5)); press('UP', wait=30); shot('by the beds'); check('at the foot of the beds', r, where(g))
r = go(g, F, (9, 8)); shot('the hay corner'); check('by the hay corner', r, where(g))
r = go(g, F, (6, 8)); press('DOWN', wait=200); g.run(60); p = where(g); shot('back out'); check('out by the mat onto Route 11', r and p and p[1] == m0 and p[0] == (55, 15), p)
print('ALL OK' if ok_all else 'PROBLEM')
S = Image.new('RGB', (240 * 3, 172 * ((len(shots) + 2) // 3))); dr = ImageDraw.Draw(S)
for i, (n, f) in enumerate(shots):
    S.paste(Image.fromarray(f), ((i % 3) * 240, (i // 3) * 172 + 12)); dr.text(((i % 3) * 240 + 2, (i // 3) * 172), n, fill=(255, 255, 0))
S.save('/home/claude/scratch/route11/farmhouse_walk.png')
