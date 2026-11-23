"""Props for the Citadel's courtyard houses: the user's prop sheet (assets/templar_hq_reference/user_props/,
halved to native; user 2026-11-23) and pieces drawn here where nothing exists (user 2026-11-23: "you may also need to
build some of your own assets": the anvil)."""
import os
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
SHEET = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'assets', 'templar_hq_reference', 'user_props', 'user_props_native.png'))

def _cut(x0, y0, x1, y1):
    a = np.array(Image.open(SHEET).convert('RGBA')).astype(int)[y0:y1, x0:x1].copy()
    a[a[..., 3] < 128, 3] = 0; a[a[..., 3] >= 128, 3] = 255
    ys, xs = np.nonzero(a[..., 3]); return a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]

def pieces():
    return {'banner_swords': _cut(96, 0, 128, 36), 'banner_shield': _cut(96, 46, 128, 80),
            'helmet': _cut(0, 48, 32, 80), 'rack': _cut(160, 64, 224, 112), 'kegs': _cut(224, 64, 256, 96),
            'sword': _cut(34, 54, 64, 70), 'board': _cut(176, 113, 224, 128), 'anvil': anvil()}

def anvil():
    """A plain smith's anvil on a wooden stump, 16x16 (drawn here: no source has one)."""
    a = np.zeros((16, 16, 4), int)
    K, D, M, L = (32, 32, 40), (64, 64, 76), (100, 100, 112), (150, 150, 164)     # (iron: outline, dark, mid, light)
    W0, W1, W2 = (64, 40, 32), (96, 60, 44), (128, 80, 56)                       # (the stump's wood)
    def px(x, y, c): a[y, x, :3] = c; a[y, x, 3] = 255
    for x in range(1, 15): px(x, 3, K); px(x, 6, K)                             # the face, horn to heel
    for x in range(2, 14): px(x, 4, L); px(x, 5, M)
    px(1, 4, K); px(1, 5, K); px(0, 4, K); px(14, 4, K); px(14, 5, K)
    px(2, 4, M); px(13, 4, M)
    for y in (7, 8):                                                            # the waist
        for x in range(5, 11): px(x, y, D if x > 5 else K)
        px(4, y, K); px(11, y, K)
    for x in range(3, 13): px(x, 9, K)                                          # the foot
    for x in range(4, 12): px(x, 10, D)
    for y in range(11, 15):                                                     # the stump
        for x in range(3, 13): px(x, y, W1 if (x + y) % 3 else W2)
        px(3, y, W0); px(12, y, W0)
    for x in range(3, 13): px(x, 15, W0)
    return a

if __name__ == '__main__':
    P = pieces(); W = sum(p.shape[1] for p in P.values()) + 8 * len(P); Hh = max(p.shape[0] for p in P.values())
    im = Image.new('RGBA', (W, Hh), (255, 0, 255, 255)); x = 0
    for p in P.values(): im.alpha_composite(Image.fromarray(p.astype(np.uint8)), (x, 0)); x += p.shape[1] + 8
    im.resize((W * 4, Hh * 4), Image.NEAREST).save('/home/claude/scratch/props_cut.png')
