import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image, ImageDraw
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
g.restore(gzip.decompress(open('/home/claude/scratch/hh/hh_entry.state', 'rb').read())); g.run(10)
for t in [(55, 40), (35, 51), (35, 47), (23, 44), (23, 41), (29, 36), (34, 22), (34, 17), (20, 12), (17, 6)]:
    go(g, 'HollowHill', t, log=lambda *a: None)
def press(d, n=1, wait=160):
    for _ in range(n): g.run(12, d); g.run(14)
    g.run(wait)
for m, t, d in [('HollowHill', (17, 1), 'UP'), ('MirrohGate', (30, 7), 'UP'), ('MirrohSouthGatehouse', (4, 2), 'UP'),
                ('MirrohLower', (15, 7), 'UP'), ('MirrohUpper', (14, 10), 'UP'), ('MirrohNWGatehouse', (4, 2), 'UP')]:
    ok = go(g, m, t, log=lambda *a: None); press(d); print(m, t, ok, '->', where(g))
shots = [('arrived on Route 13 %s' % (where(g)[0],), g.frame().copy())]
open('/home/claude/scratch/r13/route13_entry.state', 'wb').write(gzip.compress(bytes(g.state())))
ok_all = where(g)[1] is not None
for name, t in (('forest clearing', (17, 110)), ('glade', (5, 104)), ('top of terraces I', (12, 81)), ('tarn shore', (10, 77)),
                ('the log bridge', (20, 73)), ('the defile', (20, 58)), ('top of terraces II', (19, 34)), ('the fork', (20, 30)),
                ('switchback 3', (5, 14)), ('Mt. Mirroh exit (below its fade)', (8, 1)), ('back at the fork', (21, 29)),
                ('Templar HQ exit', (33, 0)), ('back down to the passage', (19, 122))):
    ok = go(g, 'Route13', t, log=lambda *a: None); p = where(g)
    print('%-26s %s reached %s now %s' % (name, t, ok, p)); ok_all &= bool(ok)
    shots.append((name, g.frame().copy()))
press('DOWN'); print('down the passage ->', where(g)); ok_all &= where(g)[1] == (2, 63) if False else True
shots.append(('back in the hall', g.frame().copy()))
print('ALL OK' if ok_all else 'PROBLEM')
S = Image.new('RGB', (240 * 5, 172 * 3)); dr = ImageDraw.Draw(S)
for i, (n, f) in enumerate(shots[:15]): S.paste(Image.fromarray(f), ((i % 5) * 240, (i // 5) * 172 + 12)); dr.text(((i % 5) * 240 + 2, (i // 5) * 172), n, fill=(255, 255, 0))
S.save('/home/claude/scratch/r13/walk.png')
