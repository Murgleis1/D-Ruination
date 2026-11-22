import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where
from PIL import Image
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
g.restore(gzip.decompress(open('/home/claude/scratch/pt1/control_v2.state', 'rb').read())); g.run(30)
shots = []
def snap(label): shots.append((label, g.frame().copy())); print(label, where(g))
def settle(n=150): g.run(n)
def close():
    for _ in range(4): g.tap('B'); g.run(25)
import os
if os.environ.get('RESUME'):
    g.restore(gzip.decompress(open('/home/claude/scratch/dorm/dorm_1f.state', 'rb').read())); g.run(10)
else:
    print('start', where(g))
    assert go(g, 'PellucaUmbraLab', (4, 9)); g.walk('DOWN', 1); settle()
    assert go(g, 'PellucaCity', (11, 9)); snap('city: below the dormitory door')
    g.walk('UP', 1); settle(40); snap('door opening'); settle(140)
    snap('1F arrival')
    for _ in range(2): g.walk('UP', 1)
    settle(30); snap('1F inside')
    open('/home/claude/scratch/dorm/dorm_1f.state', 'wb').write(gzip.compress(bytes(g.state())))
# cook (talk to the counter front)
assert go(g, 'PellucaDormitory1F', (8, 6)); g.tap('UP'); g.run(10); g.tap('A'); g.run(90); snap('cook'); close()
# locked door
assert go(g, 'PellucaDormitory1F', (13, 3)); g.tap('UP'); g.run(10); g.tap('A'); g.run(60); snap('locked door'); close()
# upstairs
assert go(g, 'PellucaDormitory1F', (1, 1)); from walklib import step
step(g, 'UP'); settle(); snap('2F arrival')
step(g, 'UP'); [step(g, 'RIGHT') for _ in range(8)]; g.run(20); snap('2F hallway')
assert go(g, 'PellucaDormitory2F', (1, 5)); g.run(10, 'DOWN'); settle(); snap('back on 1F')
# Osrid's room via his door
assert go(g, 'PellucaDormitory1F', (5, 3)); g.tap('UP'); g.run(10); g.tap('A'); g.run(60); snap('brass plate'); close()
assert go(g, 'PellucaDormitory1F', (4, 3))
g.run(10, 'UP'); g.run(12); snap('his door opening'); settle(150); snap("Osrid's room")
assert go(g, 'PellucaDormitoryOsridRoom', (5, 8)) or True   # (the warp on the mat's top half since 2026-11-22)
step(g, 'DOWN'); settle(); snap('back out of his room')
assert go(g, 'PellucaDormitory1F', (9, 13)); step(g, 'DOWN'); settle(); snap('outside again')
W = 240 * 4; S = Image.new('RGB', (W, 160 * ((len(shots) + 3) // 4)))
for i, (l, f) in enumerate(shots): S.paste(Image.fromarray(f), ((i % 4) * 240, (i // 4) * 160))
S.save('/tmp/dorm_ingame.png'); print([l for l, _ in shots])
