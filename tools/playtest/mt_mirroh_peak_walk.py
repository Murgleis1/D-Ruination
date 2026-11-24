"""Mirroh Peak walked (2026-11-24; plan v2, Mt. Thunder style): out of 1F's exit onto the Peak at the cave mouth;
across Dreamstone Mysteries' foot and up its stairs; Winterlily Hollow's mouth is closed (nothing happens walking at
it); up the band onto the middle climb, up its three stairs, past the stream; up the summit's four ledges by their
switchback stairs; onto the summit: the stage, the shrine, the lookout on its rim; the two ruined huts on the ledge below; back down to the mouth and into 1F."""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
import walklib
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
_go = go
def go(g, m, t, log=None, tries=4):
    for _ in range(tries):
        if _go(g, m, t, log=log): return True
        for _ in range(60): g.run(6, 'B'); g.run(12)
    return False
X, F, P = 'MtMirrohExterior', 'MirrohInterior_1F', 'MirrohPeak'
_Grid = walklib.Grid
class Grid(_Grid):
    def __init__(self, m):
        _Grid.__init__(self, m)
        if m == F: self.objs -= {(6, 8), (6, 9)}
walklib.Grid = Grid
go(g, 'Route13', (8, 1), log=lambda *a: None); press('UP', wait=200)
go(g, X, (13, 11), log=lambda *a: None); press('UP', wait=200); g.run(120); m1 = where(g)[1]
r = go(g, F, (54, 2), log=lambda *a: None); press('UP', wait=30); press('UP', wait=200); g.run(60); p = where(g); mp = p[1]
shot('onto the Peak'); check("1F's exit onto the Peak, at the cave mouth", r and mp != m1 and p[0] == (26, 102), p)
r = go(g, P, (29, 79), log=lambda *a: None); shot('the foot, below its stairs'); check("across Dreamstone Mysteries' foot", r, where(g))
r = go(g, P, (40, 79), log=lambda *a: None); before = where(g); press('UP', wait=120); p = where(g); shot("Winterlily Hollow's mouth")
check("Winterlily Hollow's mouth is closed", r and p == before, p)
r = go(g, P, (22, 69), log=lambda *a: None); shot('up the foot'); check('up the foot to the band', r, where(g))
r = go(g, P, (22, 66), log=lambda *a: None); shot('onto the middle climb'); check('up the band onto the middle climb', r, where(g))
r = go(g, P, (40, 50), log=lambda *a: None); shot('the middle climb'); check('up the middle climb', r, where(g))
r = go(g, P, (40, 35), log=lambda *a: None); shot('the top of the climb'); check('to the foot of the summit', r, where(g))
r = go(g, P, (8, 31), log=lambda *a: None); shot('the summit ledges'); check('up the summit ledges', r, where(g))
r = go(g, P, (24, 15), log=lambda *a: None); shot('onto the plateau'); check('onto the plateau', r, where(g))
r = go(g, P, (25, 14), log=lambda *a: None); shot('the stage'); check('the stage (8b-8c)', r, where(g))
r = go(g, P, (25, 12), log=lambda *a: None); press('UP', wait=30); shot('the shrine'); check('before the shrine (the cardinal)', r, where(g))
r = go(g, P, (21, 9), log=lambda *a: None); press('UP', wait=30); shot('the lookout'); check('the north edge, a lookout', r, where(g))
r = go(g, P, (18, 22), log=lambda *a: None); press('UP', wait=30); shot('a ruined hut'); check('before the west hut', r, where(g))
r = go(g, P, (31, 22), log=lambda *a: None); press('UP', wait=30); shot('the other hut'); check('before the east hut', r, where(g))
r = go(g, P, (26, 102), log=lambda *a: None); press('UP', wait=200); g.run(120); p = where(g); shot('back into 1F')
check('back down to the mouth and into 1F', r and p[1] == m1 and p[0] in ((54, 1), (54, 2)), p)
print('ALL OK' if ok_all else 'PROBLEM')
S = Image.new('RGB', (240 * 4, 172 * ((len(shots) + 3) // 4))); dr = ImageDraw.Draw(S)
for i, (n, f) in enumerate(shots):
    S.paste(Image.fromarray(f), ((i % 4) * 240, (i // 4) * 172 + 12)); dr.text(((i % 4) * 240 + 2, (i // 4) * 172), n, fill=(255, 255, 0))
S.save('/home/claude/scratch/peak/peak_walk.png')
