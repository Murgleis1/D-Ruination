"""The Citadel's four houses walked (2026-11-23): Route 13 -> the Citadel -> into each house and back out of the same
door; the Tavern's healer heals; the Tavern's barkeep's shop opens."""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image, ImageDraw
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
g.restore(gzip.decompress(open('/home/claude/scratch/r13/route13_entry.state', 'rb').read())); g.run(10)
shots = []
def shot(n): g.run(20); shots.append((n, g.frame().copy()))
def press(d, n=1, wait=40):
    for _ in range(n): g.run(12, d); g.run(14)
    g.run(wait)
def box(): f = g.frame(); return int((f[120:160, 10:230].astype(int).sum(-1) > 600).sum())
ok_all = True
def check(name, cond, info=''):
    global ok_all
    print('%-46s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok_all &= bool(cond)
CIT = 'TemplarCitadel'
go(g, 'Route13', (33, 1), log=lambda *a: None); press('UP', wait=160)
c0 = where(g)[1]; check('into the Citadel', c0 is not None, where(g))
HOUSES = [('the Tavern', (4, 29), 'TemplarCitadelTavern', (7, 10), (4, 29)),
          ('the barracks', (35, 29), 'TemplarCitadelBarracks', (11, 11), (35, 29)),
          ('the armoury (west door)', (6, 13), 'TemplarCitadelArmoury', (6, 9), (6, 13)),
          ('the armoury (east door)', (7, 13), 'TemplarCitadelArmoury', (7, 9), (7, 13)),
          ('the watch house (west door)', (31, 13), 'TemplarCitadelWatchHouse', (6, 9), (31, 13)),
          ('the watch house (east door)', (32, 13), 'TemplarCitadelWatchHouse', (7, 9), (32, 13))]
for name, front, room, mat, back in HOUSES:
    r = go(g, CIT, front, log=lambda *a: None)
    press('UP', wait=180); p = where(g); shot(name)
    check('into %s' % name, r and p[1] != c0 and p[0] == mat, p)
    if name == 'the Tavern':
        go(g, room, (4, 5), log=lambda *a: None); press('UP', wait=20); press('A', wait=90); talked = box() > 2000; shot('the Tavern healer')
        for _ in range(3): g.run(6, 'A'); g.run(50)
        for _ in range(10): g.run(6, 'B'); g.run(40)
        check('  the healer speaks', talked)
        go(g, room, (9, 5), log=lambda *a: None); press('UP', wait=20); press('A', wait=90); shot('the barkeep')
        g.run(6, 'A'); g.run(120); shot('the barkeep\'s shop'); f = g.frame()
        menu = int((f[0:80, 0:120].astype(int).sum(-1) > 600).sum())
        for _ in range(10): g.run(6, 'B'); g.run(40)
        check('  the barkeep opens a shop', menu > 1500, menu)
    if name == 'the barracks':
        go(g, room, (11, 7), log=lambda *a: None); shot('the barracks corridor')
        r2 = go(g, room, (3, 11), log=lambda *a: None); check('  the briefing room reached', r2, where(g))
        r2 = go(g, room, (19, 4), log=lambda *a: None); check('  the gear room reached', r2, where(g))
    r = go(g, room, mat, log=lambda *a: None)
    press('DOWN', wait=180); p = where(g)
    check('  back out of the same door', r and p[1] == c0 and p[0] == back, p)
shot('back in the courtyard')
print('ALL OK' if ok_all else 'PROBLEM')
S = Image.new('RGB', (240 * 4, 172 * ((len(shots) + 3) // 4))); dr = ImageDraw.Draw(S)
for i, (n, f) in enumerate(shots):
    S.paste(Image.fromarray(f), ((i % 4) * 240, (i // 4) * 172 + 12)); dr.text(((i % 4) * 240 + 2, (i // 4) * 172), n, fill=(255, 255, 0))
S.save('/home/claude/scratch/r13/houses_walk.png')
