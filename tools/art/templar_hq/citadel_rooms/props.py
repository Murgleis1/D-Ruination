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
            'sword': _cut(34, 54, 64, 70), 'board': _cut(176, 113, 224, 128), 'anvil': anvil(), 'tub': tub(), 'bench': bench(), 'board_d': dispatch_board(), 'pass_map': pass_map(), 'map_table': map_table(), 'lantern_horn': lantern_horn()}

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

def _canvas(h, w):
    a = np.zeros((h, w, 4), int)
    def px(x, y, c):
        if 0 <= y < h and 0 <= x < w: a[y, x, :3] = c; a[y, x, 3] = 255
    def rect(x0, y0, x1, y1, c):
        for y in range(y0, y1):
            for x in range(x0, x1): px(x, y, c)
    return a, px, rect

INK, PAPER, PAPER2, PIN, PIN2 = (52, 40, 32), (236, 224, 192), (214, 198, 160), (184, 48, 40), (48, 80, 160)

def dispatch_board():
    """The watch's dispatch board, 48x28, for the wall: a dark grey-wood frame, cork, orders and reports pinned up (drawn here)."""
    a, px, rect = _canvas(28, 48)
    rect(0, 0, 48, 28, (40, 40, 48)); rect(2, 2, 46, 26, (150, 112, 72))
    for y in range(2, 26):
        for x in range(2, 46):
            if (x * 7 + y * 13) % 11 == 0: px(x, y, (128, 94, 60))
    for x0, y0, w, h in ((4, 4, 10, 12), (16, 3, 12, 9), (30, 5, 13, 10), (6, 17, 12, 7), (21, 14, 9, 11), (33, 17, 10, 7)):
        rect(x0, y0, x0 + w, y0 + h, PAPER); rect(x0, y0 + h - 1, x0 + w, y0 + h, PAPER2)
        for ly in range(y0 + 3, y0 + h - 2, 2): rect(x0 + 2, ly, x0 + w - 2 - (ly % 3), ly + 1, INK)
        px(x0 + w // 2, y0 + 1, PIN if (x0 // 3) % 2 else PIN2)
    return a

def pass_map():
    """A sketched map of the pass to Route 15, 44x28, pinned to the wall: paper, ink peaks, the trail, a red mark (drawn here)."""
    a, px, rect = _canvas(28, 44)
    rect(0, 0, 44, 28, PAPER); rect(0, 26, 44, 28, PAPER2); rect(42, 0, 44, 28, PAPER2)
    for x in range(44): px(x, 0, PAPER2)
    for cx, cy in ((7, 8), (13, 6), (30, 7), (36, 10), (9, 19), (34, 20), (19, 5)):      # (peaks, as in the registry map's ink)
        for d in range(4): px(cx - d, cy + d, INK); px(cx + d, cy + d, INK)
    path = [(2, 14), (6, 14), (10, 13), (14, 14), (18, 15), (22, 14), (26, 13), (30, 14), (34, 15), (38, 14), (41, 13)]
    for (x0, y0), (x1, y1) in zip(path, path[1:]):
        for t in range(0, 8):
            x = x0 + (x1 - x0) * t // 8; y = y0 + (y1 - y0) * t // 8
            if t % 2 == 0: px(x, y, (120, 70, 40))
    for d in range(-2, 3): px(30 + d, 13 + d, PIN); px(30 + d, 13 - d, PIN)           # (where the trouble is)
    rect(1, 1, 3, 3, INK); px(2, 2, PAPER)                                                # (the Citadel, west)
    px(21, 1, PIN); px(4, 24, PIN2)
    return a

def map_table():
    """The watch's map table, 64x32: a long plank table with Route 15 spread across it, markers on it (drawn here)."""
    a, px, rect = _canvas(32, 64)
    O, T1, T2, T3, L = (40, 28, 20), (150, 104, 64), (128, 86, 52), (176, 128, 80), (96, 64, 40)
    rect(1, 1, 63, 23, T1)
    for y in range(1, 23, 4): rect(1, y, 63, y + 1, T2)
    rect(1, 1, 63, 2, T3); rect(0, 0, 64, 1, O); rect(0, 23, 64, 25, O); rect(0, 0, 1, 25, O); rect(63, 0, 64, 25, O)
    rect(1, 21, 63, 23, T2)
    for x0 in (3, 58):
        rect(x0, 25, x0 + 3, 31, L); rect(x0, 25, x0 + 1, 31, O); rect(x0 + 2, 25, x0 + 3, 31, O); rect(x0, 31, x0 + 3, 32, O)
    m = pass_map()                                                                          # (the sheet spread on it)
    sheet = m[2:22, 2:42]; sh, sw = sheet.shape[:2]
    a[2:2 + sh, 12:12 + sw][sheet[..., 3] > 0] = sheet[sheet[..., 3] > 0]
    rect(13, 22, 12 + sw + 1, 23, PAPER2)
    for x, y, c in ((18, 6, PIN2), (24, 9, PIN2), (40, 12, PIN), (44, 8, PIN), (30, 16, PIN2)):   # (markers: the watch's posts)
        rect(x, y, x + 2, y + 3, c); px(x, y + 3, O); px(x + 1, y + 3, O)
    rect(54, 5, 61, 13, PAPER); rect(55, 7, 60, 8, INK); rect(55, 9, 59, 10, INK); rect(55, 11, 60, 12, INK)   # (a report)
    rect(4, 8, 9, 9, (200, 190, 170)); rect(5, 5, 6, 9, (90, 70, 50))                                    # (a quill)
    return a

def lantern_horn():
    """A signal horn and a lantern, 32x16, set on the runners' bench (drawn here)."""
    a, px, rect = _canvas(16, 32)
    O, IR, GL, GL2 = (32, 32, 40), (72, 72, 84), (248, 208, 96), (232, 152, 48)
    rect(4, 2, 12, 3, O); rect(7, 0, 9, 2, O)                                                 # (the lantern)
    rect(4, 3, 12, 12, O); rect(5, 4, 11, 11, GL); rect(7, 5, 9, 9, (255, 240, 176)); rect(5, 9, 11, 11, GL2)
    rect(7, 4, 9, 11, IR) if False else None
    rect(3, 12, 13, 14, O)
    HC, HC2, HB = (226, 210, 170), (190, 168, 120), (120, 84, 48)                             # (the horn, lying on its side)
    for i, x in enumerate(range(16, 31)):
        r = 1 + i // 4
        for y in range(10 - r, 11 + r): px(x, y, HC if y < 10 else HC2)
        px(x, 10 - r - 1, O); px(x, 11 + r, O)
    rect(30, 5, 31, 16, O); rect(19, 8, 21, 13, HB); rect(25, 6, 27, 15, HB); rect(15, 9, 16, 12, O)
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
