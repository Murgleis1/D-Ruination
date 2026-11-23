"""The Citadel's barracks and armoury, mocks v2 (v1 rejected by the user 2026-11-23); originally v1 (floor plans v1, plans.py; user 2026-11-23: barracks "build the mock",
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
    """v2 (user 2026-11-23: four small bedrooms, two beds each, off a central corridor; a common room by the door)."""
    import study_mock as SM
    P, Q = common(); R = Room(16, 14)
    SP, _ = SM.pieces(); bed, chest = SP['bed'], SP['chest']          # (the compact bed: white sheets, a blue frame)
    for x0, x1 in ((1, 6), (9, 14)):                                   # (the partitions: between the bedrooms, and
        for row in (5, 9):                                             #  between them and the common room)
            R.put(props.partition(x1 - x0 + 1), x0 * T, row * T)
    for y in (2, 6):                                                   # (the bedrooms: two beds, a chest between)
        for bx, cx in ((2, 3), (11, 12)):
            R.put(bed, bx * T, y * T); R.put(chest, cx * T, y * T); R.put(bed, (bx + 2) * T, y * T)
    R.wall(Q['banner_swords'], 7 * T + 2, 0)                          # (over the corridor's head)
    tv = R.tv
    R.img[10 * T:12 * T, 1 * T:5 * T] = tv[7 * T:9 * T, 0:4 * T]     # (the common room: the Tavern's table and stools)
    R.solid[10:12, 1:5] = True
    R.put(Q['helmet'], 11 * T, 10 * T); R.put(Q['kegs'], 13 * T, 10 * T)
    for x in (10, 12): R.wall(Q['sword'], x * T + 2, 9 * T + 6)         # (the weapon wall: blades on the partition)
    ex = R.mat(7)
    for c in ex: R.solid[c[1], c[0]] = False
    return R.img.astype(np.uint8), R.solid, ex

def armoury():
    """v2 (user 2026-11-23: keep the forge and fireplace; a working smithy, no desk, no tree stands)."""
    P, Q = common(); R = Room(14, 11)
    hearth = R.tv[0:3 * T, 4 * T:7 * T]                                              # (the Tavern's hearth: the forge)
    R.img[0:3 * T, 5 * T:8 * T] = hearth; R.solid[0:3, 5:8] = True
    R.wall(Q['banner_swords'], 1 * T + 2, 0); R.wall(Q['banner_shield'], 11 * T + 2, 0)
    for x in (3, 8):                                                                   # (swords mounted either side)
        for y in (6, 17): R.wall(Q['sword'], x * T + 2, y)
    R.put(Q['anvil'], 6 * T, 3 * T); R.put(Q['tub'], 4 * T, 3 * T); R.put(Q['kegs'], 8 * T, 3 * T)
    for y in (3, 5, 7):                                                                # (helms along both side walls)
        R.put(Q['helmet'], 1 * T - 2, y * T); R.put(Q['helmet'], 11 * T + 4, y * T)
    for x in (3, 8):                                                                   # (workbenches of finished blades)
        R.put(Q['bench'], x * T, 6 * T); R.wall(Q['sword'], x * T + 2, 6 * T + 1)
    ex = R.mat(6)
    for c in ex: R.solid[c[1], c[0]] = False
    return R.img.astype(np.uint8), R.solid, ex

def watch():
    """v1 (user 2026-11-23: the upper-east house is a watch house, the command post for the Route 15 incident; plan v1)."""
    import study_mock as SM, hall_mock as HM
    P, Q = common(); R = Room(14, 11)
    SP, _ = SM.pieces(); HP, _ = HM.pieces()
    R.wall(Q['board_d'], 1 * T + 4, 2); R.wall(Q['banner_shield'], 6 * T + 2, 0); R.wall(Q['pass_map'], 10 * T + 2, 3)
    R.put(SP['bureau'], 1 * T, 2 * T); R.put(HP['scrolls'], 3 * T, 2 * T)             # (the reports: a cabinet, scrolls)
    R.put(Q['helmet'], 12 * T - 4, 2 * T); R.put(Q['helmet'], 12 * T - 4, 4 * T)
    R.put(Q['map_table'], 5 * T, 4 * T)                                                 # (the captain stands at (6-7,3))
    R.put(SP['desk'], 1 * T, 5 * T - 4); R.put(HP['chairE'], 3 * T, 6 * T)              # (the scribe's desk, a chair beside)
    R.put(Q['bench'], 10 * T + 8, 7 * T); R.wall(Q['lantern_horn'], 10 * T + 8, 7 * T)          # (the runners' bench, horn and lantern)
    ex = R.mat(6)
    for c in ex: R.solid[c[1], c[0]] = False
    return R.img.astype(np.uint8), R.solid, ex

if __name__ == '__main__':
    for n, f in (('barracks', barracks), ('armoury', armoury), ('watch', watch)):
        img, solid, ex = f(); H, W = solid.shape
        Image.fromarray(img).resize((W * 48, H * 48), Image.NEAREST).save('/home/claude/scratch/%s_v1.png' % n)
        print(n, W, H, ex)
