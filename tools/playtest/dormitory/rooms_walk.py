import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where, step
from PIL import Image
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
g.restore(gzip.decompress(open('/home/claude/scratch/pt1/control_v2.state', 'rb').read())); g.run(30)
shots = []
def snap(label): shots.append((label, g.frame().copy())); print(label, where(g))
def close():
    for _ in range(6): g.tap('B'); g.run(25)
assert go(g, 'PellucaUmbraLab', (4, 9)); g.walk('DOWN', 1); g.run(150)
# tavern
assert go(g, 'PellucaCity', (28, 44)); step(g, 'UP'); g.run(160)
for _ in range(3): step(g, 'UP')
g.run(20); snap('tavern')
assert go(g, 'PellucaCityPokemonCenter', (4, 5)); g.tap('UP'); g.run(10); g.tap('A'); g.run(90); snap('bartender across the counter'); close()
for _ in range(3): step(g, 'UP')
g.run(10); snap('tavern back')
assert go(g, 'PellucaCityPokemonCenter', (6, 10)); g.run(10, 'DOWN'); g.run(160)
# monastery cell
assert go(g, 'PellucaCity', (22, 28)); step(g, 'UP'); g.run(160)
for _ in range(4): step(g, 'UP')
g.run(20); snap('templar cell')
assert go(g, 'PellucaTemplarMonastery', (6, 13)); g.run(10, 'DOWN'); g.run(160)
# dormitory
assert go(g, 'PellucaCity', (11, 9)); step(g, 'UP'); g.run(160)
assert go(g, 'PellucaDormitory1F', (15, 4)); g.run(20); snap('dormitory hearth')
S = Image.new('RGB', (240 * 3, 160 * ((len(shots) + 2) // 3)))
for i, (l, f) in enumerate(shots): S.paste(Image.fromarray(f), ((i % 3) * 240, (i // 3) * 160))
S.save('/tmp/rooms_ingame.png'); print([l for l, _ in shots])
