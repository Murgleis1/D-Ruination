"""Osrid's back-pic head from MonoMyth back 2 (Monty)'s own pixels (user: his hair is the closest style;
face + glasses -> the blank white mask; glasses arm -> the mask strap round the ear)."""
import numpy as np
from PIL import Image
A = np.array(Image.open('/home/claude/repo/assets/monomyth_reference/trainer_backs/back_02.png'))[:64].astype(int)
HAIRI = {0xf: 'l', 0x2: 'm', 0x4: 'm', 0x1: 'd', 0x3: 'd'}
SKINI = {0x6: 's', 0x9: 's', 0x7: 'h', 0x8: '8'}
G = np.full((64, 64), '.', dtype='<U1')
for y in range(14, 46):
    for x in range(14, 50):
        v = A[y, x]
        if v == 0x5: G[y, x] = 'K'
        elif v in HAIRI: G[y, x] = HAIRI[v]
        elif v in SKINI: G[y, x] = SKINI[v]
# 1. hair a little longer at the back of the nape: rows 37-38 repeated below themselves (x <= 28)
for x in range(14, 29):
    col = G[:, x].copy()
    G[39:62, x] = col[37:60]
# 2. the mask: a tall rigid plate over the whole face and forehead (taller than wide, like the portrait),
#    smooth convex front edge, blank white. Its top edge is the hairline (row 27); only a few short lock
#    tips fall over it.
# the trace's mask (user: "the tallness and how it's thinner ... is closer to being correct"): a 4 px plate
# from the upper head to below the chin, front edge 3 px further back than Monty's face (head turned a little
# more away), so the ear sits just behind it with only a sliver of shaded cheek
FRONT = {24: 36, 25: 37, 26: 38, 27: 38, 28: 39, 29: 39, 30: 39, 31: 40, 32: 40, 33: 40, 34: 40,
         35: 40, 36: 40, 37: 40, 38: 40, 39: 40, 40: 40, 41: 39, 42: 39, 43: 38, 44: 38, 45: 37, 46: 36}
BACK = {y: FRONT[y] - (1 if y in (24, 46) else 2 if y in (25, 45) else 3) for y in FRONT}
for y in range(16, 52):
    for x in range(30, 52):
        if y in FRONT and BACK[y] <= x <= FRONT[y]: G[y, x] = 'M'
        elif y in FRONT and x > FRONT[y]: G[y, x] = '.'
        elif y > 46 and x >= 30: G[y, x] = '.'
for y in range(33, 46):
    for x in range(33, 44):
        if y in BACK and x < BACK[y] and (G[y, x] in 's' or (G[y, x] in 'K.' and A[y, x] in (0x5, 0xa, 0xb, 0xc, 0xd, 0xe, 0x6, 0x9, 0x7, 0x8))):
            G[y, x] = 'h'                       # cheek / jaw in the mask's shadow (no eye, no lit face)
for y in range(33, 46):
    if y in BACK:
        xs = [x for x in range(33, BACK[y]) if G[y, x] == 'h']
        if y >= 42 and xs: G[y, xs[-1]] = '8'      # jaw line under the cheek
# the hair cap above the mask rounds into the mask's top instead of overhanging it (no fringe)
HAIR_FRONT = {16: 33, 17: 34, 18: 35, 19: 36, 20: 36, 21: 36, 22: 36, 23: 35}
for y, xf in HAIR_FRONT.items():
    for x in range(xf + 1, 52):
        G[y, x] = '.'
# a few short lock tips falling over the mask's top edge
for y in range(16, 24):                       # the cap's front edge above the mask: hair, not mask
    for x in range(30, 40):
        if G[y, x] in 'MN.' and x <= HAIR_FRONT.get(y, 0) and G[y, x - 1] in 'lmd': G[y, x] = 'd'
for (x, y, c) in [(34, 24, 'd'), (34, 25, 'd'), (36, 25, 'd')]:     # two pointed locks over the mask's top
    G[y, x] = c
# mask volume (still blank): one soft shade along its back edge, its chin, and under the lock tips
for y in FRONT:
    xs = [x for x in range(64) if G[y, x] == 'M']
    if not xs: continue
    G[y, min(xs)] = 'N'
    if y >= 44:
        for x in xs[:-1]: G[y, x] = 'N'
for (x, y) in ((34, 26), (36, 26)):            # the lock tips' soft shadow on the mask
    if G[y, x] == 'M': G[y, x] = 'N'
# 3. the glasses arm -> the mask strap: from the mask's back edge over the top of the ear, across the back
#    of the head to the buckle (two rows: leather, shadow)
for x in range(21, BACK[34]):
    if G[34, x] != '.': G[34, x] = 't'
    if G[35, x] != '.': G[35, x] = 'T'
for y in range(33, 37):
    for x in range(23, 26):
        G[y, x] = 'u' if (x in (23, 25) or y in (33, 36)) else 'T'
# 4. neck under the ear -> the scarf, wrapped high
for y in range(42, 52):
    for x in range(14, 34):
        if G[y, x] in 'sh8': G[y, x] = 'A'
for y in range(47, 64):
    for x in range(14, 52):
        if G[y, x] not in 'lmd': G[y, x] = '.'
# 5. outline: Monty's black kept inside; black ring round the whole head and the mask
solid = (G != '.') & (G != 'K')
ring = np.zeros_like(solid)
ring[1:] |= solid[:-1]; ring[:-1] |= solid[1:]; ring[:, 1:] |= solid[:, :-1]; ring[:, :-1] |= solid[:, 1:]
G[ring & (G == '.')] = 'K'
for y in range(64):                          # drop black left floating in the open
    for x in range(64):
        if G[y, x] == 'K':
            nb = G[max(0, y - 1):y + 2, max(0, x - 1):x + 2]
            if not np.isin(nb, list('lmdtTusMNh8ACB')).any(): G[y, x] = '.'
np.save('monty_head.npy', G)
CODE = {'K': (10, 10, 12), 'd': (114, 42, 18), 'm': (160, 64, 28), 'l': (206, 104, 52), 't': (92, 64, 44), 'T': (26, 30, 32),
        'u': (84, 96, 74), 's': (214, 158, 120), 'h': (160, 104, 76), '8': (92, 64, 44), 'M': (236, 232, 220), 'N': (198, 192, 180),
        'C': (70, 104, 60), 'A': (34, 66, 46), 'B': (18, 40, 36)}
img = np.full((64, 64, 3), (150, 150, 165), np.uint8)
for y in range(64):
    for x in range(64):
        if G[y, x] in CODE: img[y, x] = CODE[G[y, x]]
S = 10
out = Image.new('RGB', (40 * S * 2 + 20, 40 * S), (30, 30, 36))
out.paste(Image.fromarray(img[12:52, 12:52]).resize((40 * S, 40 * S), Image.NEAREST), (0, 0))
m = np.array(Image.open('/home/claude/repo/assets/monomyth_reference/trainer_backs/back_02.png').convert('RGB'))[:64]; m[A == 0] = (150, 150, 165)
out.paste(Image.fromarray(m[12:52, 12:52].astype(np.uint8)).resize((40 * S, 40 * S), Image.NEAREST), (40 * S + 20, 0))
out.save('monty_head.png')
for y in range(14, 50): print('%2d' % y, ''.join(G[y, 14:52]))
