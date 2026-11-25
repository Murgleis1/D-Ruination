"""Hollow Hill's cap of cloud seen in the game (2026-11-25; src/dr_knoll_cloud.c): from the track's end up to ring 2,
round the knoll to the sealed door's forecourt (the cloud over the knoll's top, the door clear below it), waiting there
(the cloud turning slowly), round to the knoll's north side, then back out to Route 11 (the cloud gone) and in again
(the cloud back)."""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image, ImageDraw
ROM = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/repo/codebase/pokeemerald.gba'
OUT = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/scratch/summit/cloud_walk.png'
g = GBA(ROM)
g.restore(gzip.decompress(open('/home/claude/scratch/hh/hh_entry.state', 'rb').read())); g.run(10)
shots = []; ok_all = True
def shot(n): g.run(20); shots.append((n, g.frame().copy()))
def check(name, cond, info=''):
    global ok_all
    print('%-46s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok_all &= bool(cond)
_go = go
def go(g, m, t, tries=4):
    for _ in range(tries):
        if _go(g, m, t, log=lambda *a: None): return True
        for _ in range(60): g.run(6, 'B'); g.run(12)
    return False
HH = 'HollowHill'
shot('entering Hollow Hill (no cloud in view)')
r = go(g, HH, (33, 41)); shot('ring 2, south-east: the cap ahead'); check('up onto ring 2', r, where(g))
r = go(g, HH, (29, 37)); shot("the sealed door's forecourt"); check("to the sealed door's forecourt", r, where(g))
g.run(1200); shot('20 seconds later (an eighth of a turn)')
g.run(1200); shot('40 seconds later (a quarter turn)')
r = go(g, HH, (22, 31)); shot('the knoll, west side'); check('round to the west side', r, where(g))
r = go(g, HH, (30, 21)); shot('the knoll, north side'); check('round to the north side', r, where(g))
r = go(g, HH, (65, 44))
for _ in range(4): g.run(12, 'RIGHT'); g.run(14)
g.run(60); p = where(g); shot('out on Route 11'); check('out to Route 11 (the cloud gone)', r and p and p[1] == (2, 42), p)
for _ in range(5): g.run(12, 'LEFT'); g.run(14)
g.run(40); r = go(g, HH, (33, 41)); r = r and go(g, HH, (22, 31)); shot('back in: the cap again'); check('back in, round to the knoll', r, where(g))
print('ALL OK' if ok_all else 'PROBLEM')
Sh = Image.new('RGB', (240 * 4, 172 * ((len(shots) + 3) // 4))); dr = ImageDraw.Draw(Sh)
for i, (n, f) in enumerate(shots):
    Sh.paste(Image.fromarray(f), ((i % 4) * 240, (i // 4) * 172 + 12)); dr.text(((i % 4) * 240 + 2, (i // 4) * 172), n, fill=(255, 255, 0))
Sh.save(OUT)
