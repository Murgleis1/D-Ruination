"""Osrid's back-pic hair from the APPROVED PORTRAIT's own hair (dominant-vote downscale, the method that made
the approved front head). Portrait hair: smooth top swept straight back off the mask, spiky locks flaring
off the back edge in groups, lit rim along top/back, flat mid, darker underneath toward ear and nape."""
import numpy as np
from PIL import Image
P = np.array(Image.open('/home/claude/repo/assets/portrait_rework/osrid_round3/portrait_APPROVED_P5.png').convert('RGB'))
CL = {(74, 26, 12): 'd', (114, 42, 18): 'd', (160, 64, 28): 'm', (206, 104, 52): 'l', (10, 10, 12): 'K', (255, 0, 255): '.'}
y0, y1, x0, x1 = 17, 50, 16, 60                  # portrait hair box (the face inside it -> back of the skull)
src = np.array([[CL.get(tuple(P[y, x]), 'o') for x in range(x0, x1)] for y in range(y0, y1)])
# face / mask / skin inside the hair box = the back of the head in the back view: shadowed hair
for r in range(src.shape[0]):                     # everything from the face's back edge rightwards
    xs = np.nonzero(src[r] == 'o')[0]                 # (incl. the glyph's black lines) = back of skull
    if len(xs):
        for c in range(xs.min(), src.shape[1]):
            if src[r, c] in 'oK' and not (c > xs.max()): src[r, c] = 'D'
src[src == 'o'] = 'D'
TW, TH = 26, 26                                    # target size of the hair (Monty-head scale)
sy, sx = src.shape[0] / TH, src.shape[1] / TW
out = np.full((TH, TW), '.', dtype='<U1')
for j in range(TH):
    for i in range(TW):
        win = src[int(j * sy):max(int((j + 1) * sy), int(j * sy) + 1), int(i * sx):max(int((i + 1) * sx), int(i * sx) + 1)].ravel()
        solid = [c for c in win if c != '.']
        if len(solid) * 2 < len(win): continue        # mostly background -> background (keeps spikes pointed)
        hair = [c for c in solid if c in 'lmdD']
        if not hair: out[j, i] = 'K'; continue
        if 'l' in hair and hair.count('l') * 3 >= len(hair): out[j, i] = 'l'      # lit rim survives
        else:
            v = max(set(hair), key=hair.count)
            out[j, i] = ('m' if j < 15 else 'd') if v == 'D' else v
np.save('portrait_hair.npy', out)
print('\n'.join(''.join(r) for r in out))
