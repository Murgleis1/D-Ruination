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
            'sword': _cut(34, 54, 64, 70), 'board': _cut(176, 113, 224, 128), 'anvil': anvil(), 'tub': tub(), 'bench': bench()}

def tub():
    """A smith's quench tub, wooden staves and dark water, 16x16 (drawn here)."""
    a = np.zeros((16, 16, 4), int)
    O, W1, W2, H = (40, 28, 20), (96, 60, 44), (128, 80, 56), (168, 120, 72)
    B1, B2, B3 = (24, 48, 88), (40, 74, 124), (96, 140, 180)
    def px(x, y, c): a[y, x, :3] = c; a[y, x, 3] = 255
    for y in range(1, 16):                                        # (the staves: a barrel-like body, the full tile)
        for x in range(0, 16):
            if (x - 7.5) ** 2 / 64 + (y - 8.5) ** 2 / 56 <= 1: px(x, y, W1 if x % 3 else W2)
    for y in range(1, 16):
        for x in range(0, 16):
            if a[y, x, 3] and (x - 7.5) ** 2 / 64 + (y - 8.5) ** 2 / 56 > 0.8: px(x, y, O)
    for y in range(2, 9):                                         # (the water's surface, seen from above)
        for x in range(1, 15):
            if (x - 7.5) ** 2 / 42 + (y - 5) ** 2 / 7 <= 1: px(x, y, B2)
    for x in range(4, 9): px(x, 3, B3)
    px(11, 6, B1); px(3, 6, B1); px(12, 5, B1)
    for x in range(1, 15):                                        # (an iron hoop)
        if a[11, x, 3]: px(x, 11, O)
    return a

def partition(w):
    """A low interior wall, w tiles long, 16 tall: a dark cap over grey-wood boards (drawn here, in the houses' wood)."""
    a = np.zeros((16, w * 16, 4), int); a[..., 3] = 255
    a[0, :, :3] = (32, 32, 40); a[1:3, :, :3] = (96, 96, 108); a[3, :, :3] = (64, 64, 76)
    for y in range(4, 16):
        for x in range(w * 16):
            a[y, x, :3] = (40, 40, 48) if x % 8 == 0 else (72, 72, 84) if y < 6 else (84, 84, 96) if (x // 8) % 2 else (78, 78, 90)
    a[15, :, :3] = (40, 40, 48)
    return a

def bench(w=2):
    """A smith's workbench, w tiles wide, 16 tall: a plank top over two trestle legs (drawn here)."""
    a = np.zeros((16, w * 16, 4), int); W = w * 16
    O, T1, T2, T3, L = (40, 28, 20), (150, 104, 64), (128, 86, 52), (176, 128, 80), (96, 64, 40)
    def px(x, y, c): a[y, x, :3] = c; a[y, x, 3] = 255
    for y in range(2, 10):
        for x in range(1, W - 1): px(x, y, T3 if y == 2 else T1 if (y // 3) % 2 else T2)
    for x in range(1, W - 1): px(x, 1, O); px(x, 10, O)
    for y in range(1, 11): px(0, y, O); px(W - 1, y, O)
    for x0 in (2, W - 5):
        for y in range(11, 16):
            for x in range(x0, x0 + 3): px(x, y, O if x in (x0, x0 + 2) or y == 15 else L)
    return a

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
