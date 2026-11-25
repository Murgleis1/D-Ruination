"""Hollow Hill's summit walked (2026-11-25; mock v2, built by tools/art/hollowhill/ruin/build_summit.py). Nothing leads
up yet (Hollow Hill's sealed door stays shut in Chapter 1), so this walk runs on a test ROM whose Route 11 farmhouse
door (Route 11 warp 0) is pointed at the summit's arrival (warp 1) for the test only (made, then restored, by the build
session; ROM path below).
Arrival on the sunk stair (the player steps up onto the summit), the court round the stele and the plinths, both
colonnades, up the four flights of the bastion to the landing under the burst arch (the arch holds: the lair is shut),
back down, and down the sunk stair to Hollow Hill's sealed door's forecourt."""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image, ImageDraw
ROM = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/summit/summit_test.gba'
OUT = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/scratch/summit/summit_walk.png'
g = GBA(ROM)
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
R, SM = 'Route11', 'HollowHillSummit'
r = go(g, R, (55, 15)); check('to the (test) door', r, where(g))
press('UP', wait=260); g.run(120); p = where(g)
shot('arrival: up out of the sunk stair'); check('arrives and steps up onto the summit (21, 41)', p and p[0] == (21, 41), p)
r = go(g, SM, (21, 36)); shot('before the stele'); check('to the stele', r, where(g))
press('UP', 2, wait=30); check('the stele holds', where(g)[0] == (21, 36), where(g))
r = go(g, SM, (14, 34)); shot('the court, west plinths'); check('round the west plinths', r, where(g))
r = go(g, SM, (11, 35)); shot('the west colonnade'); check('the west colonnade', r, where(g))
r = go(g, SM, (31, 35)); shot('the east colonnade'); check('the east colonnade', r, where(g))
r = go(g, SM, (21, 27)); shot('the foot of the bastion'); check('the foot of the bastion', r, where(g))
r = go(g, SM, (21, 21)); shot('up the first flights'); check('up flights 4 and 3', r, where(g))
r = go(g, SM, (21, 12)); shot('up flight 2'); check('up flight 2', r, where(g))
r = go(g, SM, (21, 6)); shot('under the burst arch'); check('up the last flight, under the arch', r, where(g))
press('UP', 3, wait=30); shot('the lair is shut'); check('the arch holds (lair shut in Chapter 1)', where(g)[0] == (21, 6), where(g))
r = go(g, SM, (16, 7)); shot('the top landing, west'); check('the top landing west', r, where(g))
r = go(g, SM, (21, 41)); press('DOWN', wait=260); g.run(120); p = where(g)
shot('down the sunk stair'); check('down to Hollow Hill (29, 36)', p and p[1] == 'HollowHill' and p[0] == (29, 36), p) if p and isinstance(p[1], str) else check('down to Hollow Hill (29, 36)', p and p[0] == (29, 36), p)
print('ALL OK' if ok_all else 'PROBLEM')
Sh = Image.new('RGB', (240 * 4, 172 * ((len(shots) + 3) // 4))); dr = ImageDraw.Draw(Sh)
for i, (n, f) in enumerate(shots):
    Sh.paste(Image.fromarray(f), ((i % 4) * 240, (i // 4) * 172 + 12)); dr.text(((i % 4) * 240 + 2, (i // 4) * 172), n, fill=(255, 255, 0))
Sh.save(OUT)
