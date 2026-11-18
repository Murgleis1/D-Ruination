"""Round 15: the mask covers most of the face and its top (the upper forehead) reaches the hairline.
Variant A: mask meets the hairline. Variant B: a 1-px sliver of forehead skin between hairline and mask."""
import numpy as np, sys
from PIL import Image
G = np.load('osrid_head.npy')                    # round 14 head (Monty coords)
variant = sys.argv[1]
FRONT = {24: 37, 25: 38, 26: 39, 27: 39, 28: 40, 29: 40, 30: 40, 31: 40, 32: 40, 33: 40, 34: 40, 35: 40,
         36: 40, 37: 40, 38: 40, 39: 40, 40: 40, 41: 39, 42: 39, 43: 38, 44: 38, 45: 37, 46: 36}
BACK = {24: 35, 25: 34, 26: 34, 27: 33, 28: 33, 29: 33, 30: 33, 31: 33, 32: 33, 33: 33, 34: 33, 35: 33,
        36: 33, 37: 33, 38: 33, 39: 33, 40: 33, 41: 33, 42: 33, 43: 34, 44: 34, 45: 35, 46: 35}
for y in range(14, 50):                          # clear the old mask / cheek / hair in front of the new back edge
    for x in range(30, 50):
        if y in BACK and x >= BACK[y] and G[y, x] != 'A': G[y, x] = '.'
for y in FRONT:
    for x in range(BACK[y], FRONT[y] + 1):
        if G[y, x] != 'A' or y <= 44: G[y, x] = 'M'
# soft shade: along the back edge (where hair and ear meet it), the chin, and under the hairline
for y in FRONT:
    G[y, BACK[y]] = 'N'
    if y >= 44:
        for x in range(BACK[y], FRONT[y]): G[y, x] = 'N'
for (x, y) in ((36, 24),):
    G[y, x] = 'd'                                                # a lock tip over the forehead
    if G[y + 1, x] == 'M': G[y + 1, x] = 'N'
# hairline: hair rows above / behind the mask top stay; restore hair where clearing left a gap at the crown
for y in range(17, 24):                       # hair cap above the forehead edge reaches the front of the head
    xs = [x for x in range(64) if G[y, x] in 'lmd']
    if xs:
        for x in range(max(xs) + 1, min(37, 31 + (y - 17))):
            if G[y, x] == '.': G[y, x] = 'm'
# the strap meets the new back edge
for x in range(20, BACK[34]):
    if G[34, x] in 'lmd' and x not in (27, 31): G[34, x] = 't'
# outline
G[G == 'K'] = '.'
solid = G != '.'
ring = np.zeros_like(solid)
ring[1:] |= solid[:-1]; ring[:-1] |= solid[1:]; ring[:, 1:] |= solid[:, :-1]; ring[:, :-1] |= solid[:, 1:]
G[ring & ~solid] = 'K'
np.save('osrid_head_%s.npy' % variant, G)
CODE = {'K': (10, 10, 12), 'd': (114, 42, 18), 'm': (160, 64, 28), 'l': (206, 104, 52), 't': (92, 64, 44), 'T': (26, 30, 32),
        'u': (84, 96, 74), 's': (214, 158, 120), 'h': (160, 104, 76), '8': (92, 64, 44), 'M': (236, 232, 220), 'N': (198, 192, 180),
        'C': (70, 104, 60), 'A': (34, 66, 46), 'B': (18, 40, 36)}
img = np.full((64, 64, 3), (150, 150, 165), np.uint8)
for y in range(64):
    for x in range(64):
        if G[y, x] in CODE: img[y, x] = CODE[G[y, x]]
Image.fromarray(img[12:52, 8:48]).resize((400, 400), Image.NEAREST).save('head_%s.png' % variant)
for y in range(15, 48): print('%2d' % y, ''.join(G[y, 10:44]))
