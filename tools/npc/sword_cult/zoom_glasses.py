"""Close-up check of Baradus's glasses on every asset: now | A (ice glass) | B (ice frames)."""
import sys
from PIL import Image, ImageDraw
import baradus as B

CROPS = {'front': ((22, 4, 38, 20), 14), 'ow': ((0, 14, 64, 30), 10), 'positive': ((14, 34, 54, 80), 7),
         'anger': ((14, 34, 54, 80), 7), 'negative': ((14, 34, 54, 80), 7)}
rows = []
for name, (box, s) in CROPS.items():
    idx, pal = B.load(B.ASSETS[name])
    ims = [('now', B.rgba(idx, pal))]
    for o in 'AB':
        i2, p2, _ = B.apply(B.ASSETS[name], o)
        ims.append((o, B.rgba(i2, p2)))
    rows.append((name, [(l, im.crop(box).resize(((box[2] - box[0]) * s, (box[3] - box[1]) * s), Image.NEAREST)) for l, im in ims]))
W = max(sum(z.width + 16 for _, z in r) + 10 for _, r in rows)
H = sum(max(z.height for _, z in r) + 24 for _, r in rows) + 10
c = Image.new('RGB', (W, H), (36, 36, 44))
d = ImageDraw.Draw(c)
y = 6
for name, r in rows:
    x = 8
    for l, z in r:
        c.paste(z, (x, y))
        d.text((x, y + z.height + 2), f'{name} {l}', fill=(230, 230, 230))
        x += z.width + 16
    y += max(z.height for _, z in r) + 24
c.save(sys.argv[1] if len(sys.argv) > 1 else '/tmp/cult/glasses_zoom.png')
print(c.size)
