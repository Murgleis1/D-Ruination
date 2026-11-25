"""Pelluca's closed exits in Chapter 1 (2026-11-25, the stage-1 exits check): every way off the town's map is either
the west road to Route 11 (closed until the shrine is awakened) or a later chapter's road (closed). Tries each: the
west road on all five of its rows (rows 31-32 were open past the gate's triggers until today), the canal's two banks
north (they ran to the map's edge and stopped), the north road and the east road; each must turn the player back."""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image, ImageDraw
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
st = gzip.decompress(open('/home/claude/scratch/r11/pelluca_west.state', 'rb').read())
shots = []; ok_all = True
def check(name, cond, info=''):
    global ok_all
    print('%-46s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok_all &= bool(cond)
def attempt(name, stand, d, n=3, back_ok=lambda p: True):
    g.restore(st); g.run(10)
    r = go(g, 'PellucaCity', stand, log=lambda *a: None)
    for _ in range(n):
        g.run(12, d); g.run(14)
        shots.append((name, g.frame().copy())) if _ == 0 else None
        for _ in range(8): g.tap('A'); g.run(25)
    g.run(60); p = where(g)
    check(name, r and p and p[1] == (2, 5) and back_ok(p[0]), (stand, p))
for y in (28, 29, 30, 31, 32):
    attempt('west road, row %d: turned back' % y, (1, y), 'LEFT', back_ok=lambda q: q[0] >= 1)
# (the canal's banks, x 18 and 21, look like they run north off the map but cannot be entered: their cells only let
# a surfer onto the canal; and Surf comes in a later chapter)
g.restore(st); g.run(10); go(g, 'PellucaCity', (16, 7), log=lambda *a: None)
for d in ('RIGHT', 'UP', 'RIGHT'): g.run(12, d); g.run(16)
check("the canal's west bank cannot be entered", where(g)[0][0] <= 16, where(g))
attempt('north road: turned back', (37, 5), 'UP', back_ok=lambda q: q[1] >= 4)
attempt('east road: turned back', (72, 26), 'RIGHT', back_ok=lambda q: q[0] <= 73)
print('ALL OK' if ok_all else 'PROBLEM')
Sh = Image.new('RGB', (240 * 3, 172 * ((len(shots) + 2) // 3))); dr = ImageDraw.Draw(Sh)
for i, (n, f) in enumerate(shots):
    Sh.paste(Image.fromarray(f), ((i % 3) * 240, (i // 3) * 172 + 12)); dr.text(((i % 3) * 240 + 2, (i // 3) * 172), n, fill=(255, 255, 0))
Sh.save('/home/claude/repo/assets/pelluca_reference/ingame_closed_exits.png')
