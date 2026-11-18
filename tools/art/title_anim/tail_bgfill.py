"""Background behind the tail: nearest surrounding LIGHT background pixel (never Chien-Pao, never dark shadow),
then a 3x3 mode pass inside the region to break up streaks."""
import numpy as np
from PIL import Image
from scipy import ndimage
from tail_rig import TAIL
im = Image.open('dr_title.png'); a = np.array(im); tp = np.array(im.getpalette()[:768]).reshape(256, 3)
cp = np.load('mask_cp.npy'); bgf = np.load('bg_filled.npy')
lum = tp[a].astype(float) @ [0.3, 0.59, 0.11]
R = ndimage.binary_dilation(TAIL, iterations=1) & ~(cp & ~TAIL)          # tail area (+1 px), never the body
cand = ~cp & ~R & (lum > 150)
_, (iy, ix) = ndimage.distance_transform_edt(~cand, return_indices=True)
fill = a.copy(); fill[R] = a[iy[R], ix[R]]
for _ in range(2):
    nxt = fill.copy()
    for y, x in zip(*np.nonzero(R)):
        win = fill[y - 1:y + 2, x - 1:x + 2].ravel(); v, c = np.unique(win, return_counts=True); nxt[y, x] = v[c.argmax()]
    fill = nxt
out = bgf.copy(); out[R] = fill[R]
out[~R] = bgf[~R]
np.save('bg_filled_tail.npy', out)
scene = a.copy(); scene[TAIL] = out[TAIL]; scene[R & ~TAIL] = a[R & ~TAIL]
Image.fromarray(tp[scene][96:128, 56:104].astype(np.uint8)).resize((384, 256), Image.NEAREST).save('/tmp/bgtail.png')
print('filled', int(R.sum()))
