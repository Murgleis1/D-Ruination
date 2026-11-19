import sys, gzip
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go, where, step
from PIL import Image
import numpy as np
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
g.restore(gzip.decompress(open('/home/claude/scratch/pt1/control_v2.state', 'rb').read())); g.run(30)
def burst(name, n=8):
    fr = []
    for i in range(n): fr.append(g.frame().copy()); g.run(8)
    diff = [int((np.abs(fr[i].astype(int) - fr[0]).sum(-1) > 0).sum()) for i in range(n)]
    print(name, where(g), 'pixels differing from first frame:', diff)
    ims = [Image.fromarray(f).resize((480, 320), Image.NEAREST) for f in fr]
    ims[0].save(f'/tmp/{name}.gif', save_all=True, append_images=ims[1:], duration=133, loop=0)
    return fr
assert go(g, 'PellucaUmbraLab', (4, 9)); g.walk('DOWN', 1); g.run(150)
assert go(g, 'PellucaCity', (28, 44)); step(g, 'UP'); g.run(160)
for _ in range(3): step(g, 'UP')
g.run(30); t = burst('tavern_fire_ingame')
assert go(g, 'PellucaCityPokemonCenter', (6, 10)); g.run(10, 'DOWN'); g.run(160)
assert go(g, 'PellucaCity', (11, 9)); step(g, 'UP'); g.run(160)
assert go(g, 'PellucaDormitory1F', (15, 4)); g.run(30); d = burst('dorm_fire_ingame')
S = Image.new('RGB', (480 * 2, 320)); S.paste(Image.fromarray(t[0]).resize((480, 320), Image.NEAREST), (0, 0)); S.paste(Image.fromarray(d[0]).resize((480, 320), Image.NEAREST), (480, 0)); S.save('/tmp/fires_ingame.png')
assert go(g, 'PellucaDormitory1F', (1, 1)); step(g, 'UP'); g.run(150)
for _ in range(1): step(g, 'UP')
for _ in range(12): step(g, 'RIGHT')
g.run(20); Image.fromarray(g.frame()).resize((480, 320), Image.NEAREST).save('/tmp/dorm2f_ingame.png'); print('2F', where(g))
