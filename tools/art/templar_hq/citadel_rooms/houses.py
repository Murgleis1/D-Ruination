"""The Citadel's barracks and armoury, mocks v1 (floor plans v1, plans.py; user 2026-11-23: barracks "build the mock",
with the prop sheet's sword banners and Crown's wall swords; armoury approved). Both on the Citadel Tavern's shell
(tavern.py: the cream plank floor, the dark grey wood walls), so the courtyard's houses match inside.
Each room() returns (picture, solid, exits): the exit mat on the last floor row, as everywhere.
Pieces: the user's prop sheet (props.py: banners, helmet stands, iron stands, kegs, the display sword, the anvil drawn
here), Odyssey's bed (the bishops' dormitory's), MonoMyth's writing desk and Crown's chair (Ambrose's study's), the
Tavern's brick hearth as the forge. Usage: python3 houses.py (renders both to the scratch folder)."""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); TQ = os.path.dirname(HERE)
for d in (HERE, os.path.join(TQ, 'study'), os.path.join(TQ, 'bishops')): sys.path.insert(0, d)
import tavern, props
T = 16
MAT = ((36, 74, 155), (177, 149, 48))

class Room:
    def __init__(self, W, H):
        self.W, self.H = W, H
        tv, _, _ = tavern.room(); self.tv = tv.astype(int)
        self.img = np.zeros((H * T, W * T, 3), int); self.solid = np.zeros((H, W), bool)
        cell = lambda x, y: self.tv[y * T:(y + 1) * T, x * T:(x + 1) * T]
        for x in range(1, W - 1):
            for y in range(2):
                self.img[y * T:(y + 1) * T, x * T:(x + 1) * T] = cell(2 + x % 2, y)            # (the grey wood wall)
            for y in range(2, H - 1):
                self.img[y * T:(y + 1) * T, x * T:(x + 1) * T] = cell(8 + x % 2, 2 if y == 2 else 3)   # (planks)
        self.solid[:2] = True; self.solid[:, 0] = True; self.solid[:, W - 1] = True; self.solid[H - 1] = True
    def put(self, p, px, py, solid=True):
        h, w = p.shape[:2]; m = p[..., 3] > 0
        self.img[py:py + h, px:px + w][m] = p[..., :3][m]
        if solid:
            cov = np.zeros((self.H + 4, self.W + 4))
            ys, xs = np.nonzero(m)
            for y, x in zip(ys + py, xs + px):
                if 0 <= y < self.H * T and 0 <= x < self.W * T: cov[y // T, x // T] += 1
            self.solid |= cov[:self.H, :self.W] >= 48
    def wall(self, p, px, py): self.put(p, px, py, solid=False)                       # (on the wall: solid anyway)
    def mat(self, x0):
        y = (self.H - 2) * T
        self.img[y + 4:y + 12, x0 * T + 2:(x0 + 2) * T - 2] = MAT[1]; self.img[y + 5:y + 11, x0 * T + 3:(x0 + 2) * T - 3] = MAT[0]
        return [(x0, self.H - 2), (x0 + 1, self.H - 2)]

def common():
    import study_mock as SM, dorm_mock as DM
    P, _ = DM.pieces(); Q = props.pieces()
    st = Q.pop('rack'); l = st[:, :20].copy()
    l[28:, 14:, 3] = 0                                          # (the bench beside it off: the stand alone)
    Q['stand_l'] = l; Q['stand_r'] = l[:, ::-1].copy()          # (the right one: its mirror)
    b = Q['board']; Q['board'] = b[4:] if b.shape[0] > 12 else b
    return P, Q

def barracks():
    P, Q = common(); R = Room(16, 13)
    R.wall(Q['banner_swords'], 4 * T + 2, 0); R.wall(Q['banner_shield'], 7 * T + 2, 0); R.wall(Q['banner_swords'], 10 * T + 2, 0)
    R.wall(Q['banner_swords'], 1 * T + 2, 0); R.wall(Q['banner_swords'], 13 * T + 2, 0)
    for y in (2, 5, 8):                                           # (three beds down each side, heads north)
        R.put(P['bed'], 1 * T, y * T + 4); R.put(P['bed'], 13 * T, y * T + 4)
    R.put(Q['helmet'], 4 * T, 2 * T + 4); R.put(Q['helmet'], 11 * T, 2 * T + 4)
    R.put(Q['stand_l'], 6 * T, 2 * T); R.put(Q['stand_r'], 9 * T - 6, 2 * T)        # (the weapon stands, at the head)
    R.put(Q['sword'], 7 * T, 4 * T)                                                  # (a sword laid across them)
    R.put(Q['board'], 6 * T + 8, 6 * T + 8)                                          # (the drill table)
    R.put(Q['kegs'], 4 * T, 9 * T); R.put(Q['kegs'], 11 * T - 6, 9 * T)
    R.put(P['desk'], 8 * T, 8 * T); R.put(P['chairL'], 9 * T, 10 * T)               # (the sergeant's desk)
    ex = R.mat(7)
    for c in ex: R.solid[c[1], c[0]] = False
    return R.img.astype(np.uint8), R.solid, ex

def armoury():
    P, Q = common(); R = Room(14, 11)
    hearth = R.tv[0:3 * T, 4 * T:7 * T]                                              # (the Tavern's hearth: the forge)
    R.img[0:3 * T, 5 * T:8 * T] = hearth; R.solid[0:3, 5:8] = True
    R.wall(Q['banner_swords'], 1 * T + 2, 0); R.wall(Q['banner_shield'], 11 * T + 2, 0)
    R.put(Q['anvil'], 6 * T, 3 * T + 4)                                               # (before the forge)
    R.put(Q['board'], 9 * T, 3 * T + 6); R.put(Q['sword'], 9 * T + 6, 3 * T + 2, solid=False)   # (the workbench)
    R.put(Q['kegs'], 2 * T, 3 * T)                                                    # (coal)
    for x in (3, 5, 8, 10): R.put(Q['helmet'], x * T, 5 * T + 4)                      # (a row of helmet stands)
    R.put(Q['stand_l'], 1 * T, 4 * T); R.put(Q['stand_r'], 12 * T - 6, 4 * T)        # (clear of the desk)
    R.put(P['desk'], 1 * T, 7 * T); R.put(P['chairL'], 2 * T, 9 * T)                 # (the quartermaster)
    ex = R.mat(6)
    for c in ex: R.solid[c[1], c[0]] = False
    return R.img.astype(np.uint8), R.solid, ex

if __name__ == '__main__':
    for n, f in (('barracks', barracks), ('armoury', armoury)):
        img, solid, ex = f(); H, W = solid.shape
        Image.fromarray(img).resize((W * 48, H * 48), Image.NEAREST).save('/home/claude/scratch/%s_v1.png' % n)
        print(n, W, H, ex)
