import numpy as np
from PIL import Image
OLD = np.load('monty_head.npy')                 # mask, ear, cheek, strap, buckle, scarf, nape locks
HR = np.load('portrait_hair.npy')               # portrait hair, 26 x 26
HY, HX = 16, 14                                 # where the hair grid sits (Monty-head coordinates)
G = np.full((64, 64), '.', dtype='<U1')
for j in range(HR.shape[0]):
    for i in range(HR.shape[1]):
        if HR[j, i] != '.': G[HY + j, HX + i] = HR[j, i]
for y in range(42, 64):                         # Monty's nape locks below the portrait hair
    for x in range(64):
        if OLD[y, x] in 'lmdK' and x < 30: G[y, x] = OLD[y, x]
# the portrait's upper hair is one flat mid tone with a lit rim: clear downscale speckle above the strap
for y in range(16, 33):
    for x in range(14, 40):
        if G[y, x] == 'd': G[y, x] = 'm'
# everything that is not hair comes back from the current head, on top
for y in range(64):
    for x in range(64):
        if OLD[y, x] in 'tTuMNsh8A': G[y, x] = OLD[y, x]
for y in range(64):                             # nothing of the hair in front of the mask
    xs = [x for x in range(64) if OLD[y, x] in 'MN']
    if xs:
        for x in range(max(xs) + 1, 64): G[y, x] = '.'
# outline: black ring round everything
G[G == 'K'] = '.'
solid = G != '.'
ring = np.zeros_like(solid)
ring[1:] |= solid[:-1]; ring[:-1] |= solid[1:]; ring[:, 1:] |= solid[:, :-1]; ring[:, :-1] |= solid[:, 1:]
G[ring & ~solid] = 'K'
# keep the portrait's inner black lines between locks
for j in range(HR.shape[0]):
    for i in range(HR.shape[1]):
        y, x = HY + j, HX + i
        if HR[j, i] == 'K' and G[y, x] in 'lmd' and x < 30: G[y, x] = 'K'
np.save('osrid_head.npy', G)
CODE = {'K': (10, 10, 12), 'd': (114, 42, 18), 'm': (160, 64, 28), 'l': (206, 104, 52), 't': (92, 64, 44), 'T': (26, 30, 32),
        'u': (84, 96, 74), 's': (214, 158, 120), 'h': (160, 104, 76), '8': (92, 64, 44), 'M': (236, 232, 220), 'N': (198, 192, 180),
        'C': (70, 104, 60), 'A': (34, 66, 46), 'B': (18, 40, 36)}
img = np.full((64, 64, 3), (150, 150, 165), np.uint8)
for y in range(64):
    for x in range(64):
        if G[y, x] in CODE: img[y, x] = CODE[G[y, x]]
P = Image.open('/home/claude/repo/assets/portrait_rework/osrid_round3/portrait_APPROVED_P5.png').convert('RGB')
out = Image.new('RGB', (40 * 10 + 20 + 400, 400), (30, 30, 36))
out.paste(Image.fromarray(img[12:52, 8:48]).resize((400, 400), Image.NEAREST), (0, 0))
out.paste(P.crop((10, 10, 70, 70)).resize((400, 400), Image.NEAREST), (420, 0))
out.save('osrid_head.png')
for y in range(14, 48): print('%2d' % y, ''.join(G[y, 10:44]))
