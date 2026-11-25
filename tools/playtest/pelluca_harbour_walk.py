"""Pelluca Harbour walked (2026-11-25; tools/art/pelluca/build_harbour.py + split_pelluca.py). From the town's west
gate (save state r11/pelluca_west.state): down the main stair (three steps in view, the fade, the harbour's stair,
one step down by itself, on to the quay), out the great pier to its end, the short pier, the east pier, along the quay
to the lab door, down the beach stair to the Tavern's door and into the Tavern and out, across the beach to the sealed
cave door, up the west stair into the town (the fade, one step up by itself), down it again, and up the main stair.
Usage: python3 tools/playtest/pelluca_harbour_walk.py"""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image, ImageDraw
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
g.restore(gzip.decompress(open('/home/claude/scratch/r11/pelluca_west.state', 'rb').read())); g.run(20)
T, HB = 'PellucaCity', 'PellucaHarbour'
TOWN, HARBOUR, TAVERN = (2, 5), (2, 75), None
shots = []; ok_all = True
def shot(n): g.run(10); shots.append((n, g.frame().copy()))
def check(name, cond, info=''):
    global ok_all
    print('%-52s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok_all &= bool(cond)
def step(d, wait=16): g.run(12, d); g.run(wait)
_go = go
def go(g, m, t, tries=4):
    for _ in range(tries):
        if _go(g, m, t, log=lambda *a: None): return True
        for _ in range(40): g.run(6, 'B'); g.run(10)
    return False
for _ in range(4): g.walk('RIGHT', 1); g.run(10)
r = go(g, T, (38, 33)); check('the town: the main stair\'s top', r, where(g)); shot('the town: the top of the main stair')
step('DOWN'); shot('one step down'); step('DOWN'); shot('two steps down')
step('DOWN', 4); shot('the third step: the fade')
g.run(240); p = where(g); shot('the harbour: one step down by itself')
check('down the main stair onto the harbour (38, 7)', p and p[1] == HARBOUR and p[0] == (38, 7), p)
r = go(g, HB, (38, 9)); check('onto the quay', r, where(g))
r = go(g, HB, (38, 26)); shot('the great pier\'s end'); check('out the great pier to its end', r, where(g))
r = go(g, HB, (52, 19)); check('the short pier (the item ball at its end)', r, where(g))
r = go(g, HB, (66, 25)); shot('the east pier\'s end'); check('the east pier to its end', r, where(g))
r = go(g, HB, (47, 14)); step('UP', 200); p = where(g); check('the lab door leads into the lab', p and p[1] == (0, 29), p)
g.walk('DOWN', 1); g.run(200); p = where(g); check('out of the lab onto the harbour (47, 14)', p and p[1] == HARBOUR and p[0] == (47, 14), p)
r = go(g, HB, (33, 13)); shot('the beach stair\'s top'); check('to the beach stair', r, where(g))
r = go(g, HB, (28, 17)); shot('the Tavern\'s door'); check('down the beach stair to the Tavern\'s door', r, where(g))
step('UP', 220); p = where(g); check('into the Tavern', p and p[1] != HARBOUR, p)
for _ in range(3): g.walk('DOWN', 1); g.run(30)
g.run(150); p = where(g); check('out of the Tavern onto the beach (28, 17)', p and p[1] == HARBOUR and p[0] == (28, 17), p)
r = go(g, HB, (10, 9)); g.run(12, 'UP'); g.run(10); g.tap('A'); g.run(40); shot('the sealed cave door'); check('the sealed cave door', r, where(g))
for _ in range(4): g.tap('B'); g.run(20)
r = go(g, HB, (24, 9)); check('the west stair\'s foot', r, where(g))
step('UP'); step('UP'); step('UP', 4); g.run(240); p = where(g); shot('the town after the west stair')
check('up the west stair into the town (24, 35)', p and p[1] == TOWN and p[0] == (24, 35), p)
step('DOWN'); step('DOWN', 4); g.run(240); p = where(g)
check('down the west stair onto the beach (24, 7)', p and p[1] == HARBOUR and p[0] == (24, 7), p)
r = go(g, HB, (38, 9)); step('UP'); step('UP'); step('UP', 4); g.run(240); p = where(g)
check('up the main stair into the town (38, 35)', p and p[1] == TOWN and p[0] == (38, 35), p)
print('ALL OK' if ok_all else 'PROBLEM')
S = Image.new('RGB', (240 * 4, 172 * ((len(shots) + 3) // 4))); d = ImageDraw.Draw(S)
for k, (n, f) in enumerate(shots):
    S.paste(Image.fromarray(f), ((k % 4) * 240, (k // 4) * 172 + 12)); d.text(((k % 4) * 240 + 2, (k // 4) * 172), n, fill=(255, 255, 0))
S.save('/home/claude/scratch/harbour_walk.png')
