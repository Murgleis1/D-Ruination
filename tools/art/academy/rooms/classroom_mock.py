"""Mock of the Academy classroom (M3, the active one) (user design 2026-11-19): the layout of MonoMyth's
Cascade City clown academy classroom (a window wall with a wide chalkboard between two windows, desks in a
chevron facing it), skinned with Pokemon Crown's classroom tileset (map group 5 #2; credit: Blah and the Crown
team, used with permission): its cream wall with the dark trim, heraldic shields, chalkboard, bookcases, plank
floor, red runner, and its two-seat desks and chairs (user: the desks and tables from the Crown classroom too).
Crown has no windows, so the two windows are the Academy hall's own cleaned ones (they match the hall outside).
The chalkboard is widened from 2 to 4 tiles (Cascade's is 4) by repeating its middle columns.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/academy/rooms/classroom_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'crown'))
from crown_pieces import map_layout, TS, cell_layers

L = map_layout(5, 2); TSC = TS(L)
W, H = 16, 14                                  # x0 and x15 are the void sides; rows 0-2 wall, 3-12 floor, 13 the mat
TRIM, SHIELD, WALL, FLOOR, FLOOR_SHADE = 0x72, 0x73, 0x2F, 0x01, 0x93
BOARD = ((0x281, 0x282), (0x289, 0x28A))
SHELF = ((0x20, 0x21), (0xC0, 0x29))
DESKS = [(0x05, 0x06), (0x290, 0x291)]; CHAIR = 0x288
RUNNER, MAT = (0x85, 0x86), (0xC4, 0xC5)
AISLE = (7, 8)
LEFT = [(6, 1), (6, 4), (8, 2), (8, 5), (10, 3)]                 # (row, left column) of each 2-seat desk: a chevron
DESKS_AT = LEFT + [(r, 15 - x - 1) for r, x in LEFT]              # mirrored about the aisle
WINDOWS = [3, 11]                                                  # left column of each window (2 wide)

def grid():
    g = [[0] * W for _ in range(H)]
    for x in range(1, W - 1):
        g[0][x], g[1][x], g[2][x] = TRIM, WALL, WALL
        g[3][x] = FLOOR_SHADE
        for y in range(4, H - 1): g[y][x] = FLOOR
    for x in (5, 10): g[0][x] = SHIELD
    for x0 in (1, 13):
        for dy in range(2):
            for dx in range(2): g[1 + dy][x0 + dx] = SHELF[dy][dx]
    g[4][7], g[4][8] = DESKS[0]                                    # the teacher's desk, before the board
    for y in range(5, H - 1): g[y][7], g[y][8] = RUNNER
    g[H - 1][7], g[H - 1][8] = MAT
    for k, (r, x) in enumerate(DESKS_AT):
        g[r][x], g[r][x + 1] = DESKS[k % 2]; g[r + 1][x] = g[r + 1][x + 1] = CHAIR
    return g

def board():
    """Crown's 2x2 chalkboard widened to 4 tiles: its left 16 px, its middle twice, its right 16 px."""
    b = np.vstack([np.hstack([TSC.meta(m) for m in row]) for row in BOARD])
    return np.hstack([b[:, :16], b[:, 6:22], b[:, 10:26], b[:, 16:]])

def compose():
    g = grid(); img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            if g[y][x]: img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = TSC.meta(g[y][x])
    b = board(); img[0:32, 6 * 16:10 * 16] = b
    win = np.load(os.path.join(HERE, 'hall_window.npy')); wrgb, wm = win[..., :3], win[..., 3] > 0
    ys, xs = np.where(wm); wrgb, wm = wrgb[ys.min():ys.max() + 1, xs.min():xs.max() + 1], wm[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    for x0 in WINDOWS:
        px, py = x0 * 16 + 16 - wm.shape[1] // 2, 12
        sub = img[py:py + wm.shape[0], px:px + wm.shape[1]]; sub[wm] = wrgb[wm]
    return img, g

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/rooms/classroom_mock.png'
    img, _ = compose(); Image.fromarray(img).resize((W * 32, H * 32), 0).save(out); print(out)
