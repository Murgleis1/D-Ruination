"""Review board v1: the Sword Cult in black with icy sky-blue trim, and Baradus's two glasses options."""
import os
import numpy as np
from PIL import Image, ImageDraw
import baradus as B
from sword_cult import OUT, HERE

BG = (110, 110, 125, 255)
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))


def tile(path, s, label):
    im = Image.open(path).convert('RGBA')
    c = Image.new('RGBA', im.size, BG)
    c.alpha_composite(im)
    return c.resize((im.width * s, im.height * s), Image.NEAREST), label


def rgba_from(idx, pal):
    return B.rgba(idx, pal, BG[:3]).convert('RGBA')


sections = []
sections.append(('Cardinal (your masked villain): front fitted to 64x64, overworld as Emerald\'s 9 frames (32x32)', [
    tile(os.path.join(HERE, 'src_cardinal_front.png'), 3, 'yours'),
    tile(os.path.join(OUT, 'cardinal_front_64.png'), 4, 'front 64'),
    tile(os.path.join(OUT, 'cardinal_ow.png'), 3, 'overworld: S N W, walk S, walk N, walk W')]))
sections.append(('Acolyte (your trainer030): front fitted to 64x64; walking overworld from MonoMyth 217; kneeling from 89/90/84', [
    tile(os.path.join(HERE, 'src_acolyte_front.png'), 3, 'yours'),
    tile(os.path.join(OUT, 'acolyte_front_64.png'), 4, 'front 64'),
    tile(os.path.join(OUT, 'acolyte_ow.png'), 3, 'walking: MonoMyth 217'),
    tile(os.path.join(OUT, 'acolyte_kneel_S.png'), 4, 'kneel S'),
    tile(os.path.join(OUT, 'acolyte_kneel_W.png'), 4, 'W'),
    tile(os.path.join(OUT, 'acolyte_kneel_E.png'), 4, 'E')]))
bar = []
for name, s in (('front', 3), ('positive', 2)):
    idx, pal = B.load(B.ASSETS[name])
    bar.append((rgba_from(idx, pal).resize((idx.shape[1] * s, idx.shape[0] * s), Image.NEAREST), name + ' now'))
    for o, lab in (('A', 'A: ice glass'), ('B', 'B: ice frames')):
        i2, p2, _ = B.apply(B.ASSETS[name], o)
        bar.append((rgba_from(i2, p2).resize((i2.shape[1] * s, i2.shape[0] * s), Image.NEAREST), f'{name} {lab}'))
sections.append(('Baradus: ice collar piping (front also cuffs and hem); glasses A or B. All five assets: see the close-ups', bar))

W = 1500
pad = 14
rows = []
for title, items in sections:
    x, y, line_h, placed = pad, 0, 0, []
    for im, lab in items:
        if x + im.width > W - pad:
            x, y = pad, y + line_h + 22
            line_h = 0
        placed.append((im, lab, x, y))
        x += im.width + pad
        line_h = max(line_h, im.height)
    rows.append((title, placed, y + line_h + 22))
gz = Image.open('/tmp/cult/glasses_zoom.png').convert('RGBA')
gz = gz.resize((W - 2 * pad, round(gz.height * (W - 2 * pad) / gz.width)), Image.NEAREST)
H = sum(h + 40 for _, _, h in rows) + gz.height + 60
c = Image.new('RGBA', (W, H), (36, 36, 44, 255))
d = ImageDraw.Draw(c)
y0 = 10
for title, placed, h in rows:
    d.text((pad, y0), title, fill=(240, 220, 120))
    y0 += 22
    for im, lab, x, y in placed:
        c.alpha_composite(im, (x, y0 + y))
        d.text((x, y0 + y + im.height + 3), lab, fill=(230, 230, 230))
    y0 += h + 18
d.text((pad, y0), 'Baradus close-ups, every asset: now | A ice glass | B ice frames (the black line under his hair stays black)', fill=(240, 220, 120))
c.alpha_composite(gz, (pad, y0 + 22))
out = os.path.join(REPO, 'assets', 'npc_survey', 'sword_cult_v1.png')
c.save(out)
print(out, c.size)
