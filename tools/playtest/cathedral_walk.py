"""The Templar cathedral walked (2026-11-23): Route 13 -> the Citadel -> the church door -> the nave -> each office
and back (the bishops' hall on into the dormitory) -> the sealed Sanctum grille -> out to the courtyard."""
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
def box(): f = g.frame(); return int((f[120:160, 10:230] > 230).all(-1).sum())
ok_all = True
def check(name, cond, info=''):
    global ok_all
    print('%-44s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok_all &= bool(cond)
NAVE = 'TemplarCathedral'
go(g, 'Route13', (33, 1), log=lambda *a: None); press('UP', wait=160)
r = go(g, 'TemplarCitadel', (19, 18), log=lambda *a: None); check('before the church door', r, where(g))
press('UP', wait=180); p = where(g); shot('into the nave'); n0 = p[1]
check('through the church door', p[0] == (10, 35), p)
def enter(name, stand, expect_xy):
    r = go(g, NAVE, stand, log=lambda *a: None)
    press('UP', wait=180); p = where(g); shot(name)
    check('into %s' % name, r and p[1] != n0 and p[0] == expect_xy, p)
    return p
def leave(room_map, mat, back_xy):
    r = go(g, room_map, mat, log=lambda *a: None)
    press('DOWN', wait=180); p = where(g)
    check('  back out to the nave', r and p[1] == n0 and p[0] == back_xy, p)
r = go(g, NAVE, (10, 22), log=lambda *a: None); check('down the aisle', r, where(g)); shot('the nave')
r = go(g, NAVE, (7, 9), log=lambda *a: None); check('up the stairs to the chancel', r, where(g)); shot('the chancel')
enter("Ambrose's study", (18, 8), (6, 10)); leave('TemplarCathedralStudy', (6, 10), (18, 8))
enter("the bishops' hall", (2, 21), (8, 11))
r = go(g, 'TemplarCathedralBishopsHall', (2, 3), log=lambda *a: None); press('UP', wait=180); p = where(g); shot('the dormitory')
check('  through the hall into the dormitory', r and p[0] == (6, 14), p)
r = go(g, 'TemplarCathedralDormitory', (6, 14), log=lambda *a: None); press('DOWN', wait=180); p = where(g)
check('  back to the hall', r and p[0] == (2, 3), p)
leave('TemplarCathedralBishopsHall', (8, 11), (2, 21))
enter('the Braviary registry', (18, 21), (9, 11))
go(g, 'TemplarCathedralRegistry', (8, 9), log=lambda *a: None); shot('the registry, birds about')
leave('TemplarCathedralRegistry', (9, 11), (18, 21))
enter('the kitchen', (1, 22), (8, 11)); leave('TemplarCathedralKitchen', (8, 11), (1, 22))
enter('the storehouse', (19, 22), (7, 10)); leave('TemplarCathedralStorehouse', (7, 10), (19, 22))
r = go(g, NAVE, (2, 8), log=lambda *a: None); press('UP', wait=20); press('A', wait=80); p = where(g); talked = box() > 2000; shot('the Sanctum grille')
for _ in range(4): g.run(6, 'B'); g.run(40)
check('the Sanctum grille stays shut, and says so', r and p[1] == n0 and p[0] == (2, 8) and talked, p)
r = go(g, NAVE, (10, 35), log=lambda *a: None); press('DOWN', wait=180); p = where(g); shot('back in the courtyard')
check('out of the church', p[0] in ((19, 18), (19, 17)), p)
print('ALL OK' if ok_all else 'PROBLEM')
S = Image.new('RGB', (240 * 4, 172 * ((len(shots) + 3) // 4))); dr = ImageDraw.Draw(S)
for i, (n, f) in enumerate(shots):
    S.paste(Image.fromarray(f), ((i % 4) * 240, (i // 4) * 172 + 12)); dr.text(((i % 4) * 240 + 2, (i // 4) * 172), n, fill=(255, 255, 0))
S.save('/home/claude/scratch/r13/cathedral_walk.png')
