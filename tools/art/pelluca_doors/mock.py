"""Mock: each door in place on Pelluca City, closed then the three swing frames (+ GIFs)."""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import doors as D
city = np.array(Image.open(sys.argv[1]).convert('RGB'))[::3, ::3]       # render_layout's 3x render
AT = {'umbra_lab': (47, 44), 'pelluca_house': (11, 8)}
LABEL = {'umbra_lab': 'Umbra Lab door', 'pelluca_house': 'Timber house door (dormitory)'}
rows = []; gifs = []
for d, (x, y) in AT.items():
    states = [('closed', None)] + [(n, D.frame(d, k)) for k, n in enumerate(('frame 1: ajar', 'frame 2: half', 'frame 3: open'))]
    imgs = []
    for n, f in states:
        c = city.copy()
        if f is not None: c[(y - 1) * 16:(y + 1) * 16, x * 16:(x + 1) * 16] = f
        imgs.append((n, c[(y - 3) * 16:(y + 2) * 16, (x - 2) * 16:(x + 3) * 16]))
    rows.append((LABEL[d], imgs))
    seq = [imgs[0][1]] * 3 + [i for _, i in imgs[1:]] + [imgs[3][1]] * 4 + [i for _, i in imgs[1:][::-1]] + [imgs[0][1]] * 3
    Image.fromarray(seq[0]).resize((240, 240), 0).save(f'{sys.argv[2]}_{d}.gif', save_all=True,
        append_images=[Image.fromarray(s).resize((240, 240), 0) for s in seq[1:]], duration=133, loop=0)
cw, ch = 80, 80; S = Image.new('RGB', (4 * (cw + 6), len(rows) * (ch + 24)), (28, 28, 28)); dr = ImageDraw.Draw(S)
for r, (lab, imgs) in enumerate(rows):
    y0 = r * (ch + 24); dr.text((2, y0 + 1), lab, fill=(255, 230, 120))
    for k, (n, im) in enumerate(imgs):
        S.paste(Image.fromarray(im), (k * (cw + 6), y0 + 12)); dr.text((k * (cw + 6) + 2, y0 + ch + 12), n, fill=(200, 200, 200))
S.resize((S.width * 3, S.height * 3), 0).save(sys.argv[2] + '.png')
