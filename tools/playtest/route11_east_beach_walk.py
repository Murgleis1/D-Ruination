"""Route 11's east beach walked (2026-11-25; tools/art/route11/east_beach_stairs.py): from the road east of the bridge
through the tall grass to the new stairs, down onto the east beach, along it to the stream and to the cove wall, back
up the stairs to the road."""
import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image, ImageDraw
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
g.restore(gzip.decompress(open('/home/claude/scratch/r11/r11_entry.state', 'rb').read())); g.run(10)
shots = []; ok_all = True
def shot(n): g.run(20); shots.append((n, g.frame().copy()))
def check(name, cond, info=''):
    global ok_all
    print('%-46s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok_all &= bool(cond)
_go = go
def go(g, m, t, tries=6):
    for _ in range(tries):
        if _go(g, m, t, log=lambda *a: None): return True
        for _ in range(60): g.run(6, 'B'); g.run(12)            # (out of any wild battle in the grass)
    return False
R = 'Route11'
r = go(g, R, (78, 21)); shot('the road east of the bridge'); check('to the road east of the bridge', r, where(g))
r = go(g, R, (78, 24)); shot('through the tall grass to the stairs'); check('through the grass to the stairs', r, where(g))
r = go(g, R, (78, 28)); shot('down onto the east beach'); check('down the stairs onto the beach', r, where(g))
r = go(g, R, (70, 29)); shot('along the beach to the stream'); check('along the beach to the stream', r, where(g))
r = go(g, R, (79, 30)); shot('to the cove wall'); check('to the cove wall', r, where(g))
r = go(g, R, (78, 21)); shot('back up to the road'); check('back up the stairs to the road', r, where(g))
print('ALL OK' if ok_all else 'PROBLEM')
Sh = Image.new('RGB', (240 * 3, 172 * ((len(shots) + 2) // 3))); dr = ImageDraw.Draw(Sh)
for i, (n, f) in enumerate(shots):
    Sh.paste(Image.fromarray(f), ((i % 3) * 240, (i // 3) * 172 + 12)); dr.text(((i % 3) * 240 + 2, (i // 3) * 172), n, fill=(255, 255, 0))
Sh.save('/home/claude/repo/assets/route11_reference/ingame_east_beach_walk.png')
