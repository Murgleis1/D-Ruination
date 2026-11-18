"""Round 16: (1) face turned further toward the opponent -> only a narrow sliver of mask (4 px) with a little
shaded cheek and the ear behind it; (2) the top of the head is no dome: from a low hairline above the mask the
hair line rises gently toward the back, highest at the back-top where small tufts sweep back (portrait/front)."""
import numpy as np
from PIL import Image
G = np.load('osrid_head.npy')                    # round 14 head: hair, strap, ear, scarf (Monty coords)
FRONT = {26: 36, 27: 37, 28: 37, 29: 38, 30: 38, 31: 38, 32: 38, 33: 38, 34: 38, 35: 38, 36: 38, 37: 38, 38: 38,
         39: 38, 40: 38, 41: 37, 42: 37, 43: 36, 44: 36, 45: 35, 46: 34}
BACK = {y: FRONT[y] - (1 if y in (26, 46) else 2 if y in (27, 45) else 3) for y in FRONT}
# clear the old face side (mask, cheek, hair in front of the new edge); scarf stays
for y in range(14, 50):
    for x in range(33, 52):
        if G[y, x] not in 'A': G[y, x] = '.'
# (2) top of the head: swept-back line, low at the front, highest at the back-top
def top(x):                                       # nearly level, a little higher toward the back, no dome
    return 21 + (x - 24) * 0.28 if x >= 24 else 21 + (24 - x) * 0.4
for y in range(14, 34):
    for x in range(10, 40):
        if G[y, x] in 'lmdK' and y < top(x): G[y, x] = '.'
for y in range(14, 34):                          # fill hair down from the new top line to the old hair
    for x in range(14, 33):
        if y >= top(x) and G[y, x] == '.' and any(G[q, x] in 'lmd' for q in range(y + 1, min(y + 6, 64))): G[y, x] = 'm'
# hair continues forward to the mask's back edge above the strap (the side of the head)
for y in range(22, 34):
    for x in range(26, 40):
        if y in BACK and x < BACK[y] and y >= top(x) and G[y, x] == '.': G[y, x] = 'm'
        if y not in BACK and y >= top(x) and x < 36 and G[y, x] == '.' and G[y, x - 1] in 'lmd': G[y, x] = 'm'
# two small tufts at the back-top, swept back
for y in range(14, 46):                          # close 1-px gaps inside the hair (old outline seams)
    for x in range(8, 40):
        if G[y, x] in '.K' and G[y, x - 1] in 'lmd' and G[y, x + 1] in 'lmd': G[y, x] = G[y, x + 1]
for y in range(14, 34):                          # drop loose bits above the new top line
    for x in range(8, 40):
        if G[y, x] in 'lmd' and not any(G[y + q, x + p] in 'lmd' for q, p in ((1, 0), (0, 1), (0, -1))): G[y, x] = '.'
# shading: flat mid above the strap, lit rim along the top line and the back edge
for y in range(14, 33):
    for x in range(10, 40):
        if G[y, x] in 'ld': G[y, x] = 'm'
for y in range(14, 33):
    for x in range(10, 40):
        if G[y, x] == 'm' and (G[y - 1, x] == '.' or (G[y, x - 1] == '.' and y < 30)): G[y, x] = 'l'
for pts in ([(28, 23), (27, 24), (26, 24), (25, 25)], [(33, 27), (32, 28), (31, 28), (30, 29)]):   # lock lines, swept back
    for x, y in pts:
        if G[y, x] in 'ml': G[y, x] = 'd'
for x in (18, 23, 28):                            # small tufts on the top line, swept back (portrait / front)
    ys = [y for y in range(14, 34) if G[y, x] in 'lmd']
    if ys:
        t = min(ys); G[t - 1, x] = 'l'; G[t - 1, x - 1] = 'l'; G[t - 2, x - 1] = 'l'
# (1) cheek (shaded) between the ear and the mask, the mask sliver, nothing in front of it
for y in FRONT:
    for x in range(33, BACK[y]):
        if y >= 35 and G[y, x] in '.': G[y, x] = 'h'
    if y >= 42 and BACK[y] - 1 >= 33: G[y, BACK[y] - 1] = '8'          # jaw line
    for x in range(BACK[y], FRONT[y] + 1): G[y, x] = 'M'
    G[y, BACK[y]] = 'N'
    if y >= 44:
        for x in range(BACK[y], FRONT[y]): G[y, x] = 'N'
G[26, 35] = 'd'                                    # a lock tip over the mask's top
if G[27, 35] == 'M': G[27, 35] = 'N'
for x in range(20, BACK[34]):                      # strap to the mask's back edge
    if G[34, x] in 'lmdh.' and x not in (27, 31): G[34, x] = 't'
# outline
G[G == 'K'] = '.'
solid = G != '.'
ring = np.zeros_like(solid)
ring[1:] |= solid[:-1]; ring[:-1] |= solid[1:]; ring[:, 1:] |= solid[:, :-1]; ring[:, :-1] |= solid[:, 1:]
G[ring & ~solid] = 'K'
np.save('osrid_head_T.npy', G)
CODE = {'K': (10, 10, 12), 'd': (114, 42, 18), 'm': (160, 64, 28), 'l': (206, 104, 52), 't': (92, 64, 44), 'T': (26, 30, 32),
        'u': (84, 96, 74), 's': (214, 158, 120), 'h': (160, 104, 76), '8': (92, 64, 44), 'M': (236, 232, 220), 'N': (198, 192, 180),
        'C': (70, 104, 60), 'A': (34, 66, 46), 'B': (18, 40, 36)}
img = np.full((64, 64, 3), (150, 150, 165), np.uint8)
for y in range(64):
    for x in range(64):
        if G[y, x] in CODE: img[y, x] = CODE[G[y, x]]
P = Image.open('/home/claude/repo/assets/portrait_rework/osrid_round3/portrait_APPROVED_P5.png').convert('RGB')
o = Image.new('RGB', (400 + 20 + 300 + 20 + 300, 400), (30, 30, 36))
o.paste(Image.fromarray(img[12:52, 8:48]).resize((400, 400), Image.NEAREST), (0, 0))
o.paste(P.crop((10, 10, 70, 70)).resize((300, 300), Image.NEAREST), (420, 0))
o.paste(Image.open('/tmp/concept_head.png').crop((0, 0, 460, 460)).resize((300, 300)), (740, 0))
o.save('head_T.png')
for y in range(14, 48): print('%2d' % y, ''.join(G[y, 10:44]))
