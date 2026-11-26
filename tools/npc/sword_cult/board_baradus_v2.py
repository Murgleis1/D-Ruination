"""Baradus v2: glasses ice blue (option A), no trim; every asset, now vs new, full and close up."""
import os
from PIL import Image, ImageDraw
import baradus as B
from sword_cult import HERE

REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
BG = (110, 110, 125)
items = []
for name, s, crop, cs in (('front', 4, (22, 4, 38, 14), 16), ('ow', 4, (0, 16, 144, 24), 8),
                          ('positive', 3, (14, 34, 54, 50), 9), ('anger', 3, (14, 34, 54, 50), 9),
                          ('negative', 3, (14, 34, 54, 50), 9)):
    idx, pal = B.load(B.ASSETS[name])
    i2, p2, _ = B.apply(B.ASSETS[name], 'A')
    row = []
    for lab, im in (('now', B.rgba(idx, pal, BG)), ('new', B.rgba(i2, p2, BG))):
        row.append((im.resize((im.width * s, im.height * s), Image.NEAREST), f'{name} {lab}'))
    for lab, im in (('now', B.rgba(idx, pal, BG)), ('new', B.rgba(i2, p2, BG))):
        z = im.crop(crop)
        row.append((z.resize((z.width * cs, z.height * cs), Image.NEAREST), f'{name} {lab}, close'))
    items.append(row)
W = max(sum(im.width + 16 for im, _ in r) for r in items) + 16
H = sum(max(im.height for im, _ in r) + 26 for r in items) + 40
c = Image.new('RGB', (W, H), (36, 36, 44))
d = ImageDraw.Draw(c)
d.text((10, 10), 'Baradus v2: the glass ice blue (A), frames as they are, no trim on his clothes', fill=(240, 220, 120))
y = 34
for r in items:
    x = 10
    for im, lab in r:
        c.paste(im, (x, y))
        d.text((x, y + im.height + 3), lab, fill=(230, 230, 230))
        x += im.width + 16
    y += max(im.height for im, _ in r) + 26
out = os.path.join(REPO, 'assets', 'npc_survey', 'baradus_glasses_v2.png')
c.save(out)
print(out, c.size)
