"""Mock of the Academy classroom (M3, the active one) (user design 2026-11-19): the layout of MonoMyth's
Cascade City clown academy classroom (a window wall with a wide chalkboard between two windows, desks in a
chevron facing it), skinned with Pokemon Crown's classroom tileset (map group 5 #2; credit: Blah and the Crown
team, used with permission): its cream wall with the dark trim, heraldic shields, chalkboard, bookcases, plank
floor, red runner, and its two-seat desks and chairs (user: the desks and tables from the Crown classroom too).
Crown has no windows; the hall's windows looked wrong on Crown's wall (user), so Cascade's windows become Crown's
bookcases (exactly what Crown's own classroom has beside its board), with Crown's grandfather clock in one corner.
The wall is Crown's own two rows (trim, then the lower wall that meets the floor): a third row stacked another
lower-wall piece and showed its floor edge as a pale band (user). The chalkboard is widened from 2 to 4 tiles
(Cascade's is 4) by repeating its middle columns.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/academy/rooms/classroom_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'crown'))
from crown_pieces import map_layout, TS, cell_layers

L = map_layout(5, 2); TSC = TS(L)
W, H = 16, 13                                  # x0 and x15 are the void sides; rows 0-1 wall, 2-11 floor, 12 the mat
TRIM, SHIELD, WALL, FLOOR, FLOOR_SHADE = 0x72, 0x73, 0x2F, 0x01, 0x93
BOARD = ((0x281, 0x282), (0x289, 0x28A))
SHELF = ((0x20, 0x21), (0xC0, 0x29)); CLOCK = (0x17, 0x1F)      # the clock stands on the floor, its face on the wall
DESKS = [(0x05, 0x06), (0x290, 0x291)]; CHAIR = 0x288
RUNNER, MAT = (0x85, 0x86), (0xC4, 0xC5)
# the runner and the door mat in the Academy's maroon (user), with the hall carpets' gold trim and cream
MAROON_RUG = {(216, 112, 104): (118, 36, 48), (200, 88, 80): (96, 26, 40), (160, 64, 104): (84, 22, 34),
              (104, 56, 88): (64, 18, 28), (208, 216, 104): (186, 150, 100)}
MAROON_MAT = {(160, 64, 104): (118, 36, 48), (200, 88, 80): (148, 58, 64), (192, 168, 168): (230, 210, 182)}
def recolour(cell, table):
    out = cell.copy()
    for a, b in table.items(): out[(cell == a).all(-1)] = b
    return out
AISLE = (7, 8)
LEFT = [(5, 1), (5, 4), (7, 2), (7, 5), (9, 3)]                  # (row, left column) of each 2-seat desk: a chevron
DESKS_AT = LEFT + [(r, 15 - x - 1) for r, x in LEFT]              # mirrored about the aisle
SHELVES = [3, 11]                                                  # Cascade's window places (2 wide)

def grid():
    g = [[0] * W for _ in range(H)]
    for x in range(1, W - 1):
        g[0][x], g[1][x] = TRIM, WALL
        g[2][x] = FLOOR_SHADE
        for y in range(3, H - 1): g[y][x] = FLOOR
    for x in (5, 10): g[0][x] = SHIELD
    for x0 in SHELVES:
        for dy in range(2):
            for dx in range(2): g[1 + dy][x0 + dx] = SHELF[dy][dx]
    g[1][14], g[2][14] = CLOCK                                     # one grandfather clock, in the corner (user: not two)
    g[3][7], g[3][8] = DESKS[0]                                    # the teacher's desk, before the board
    for y in range(4, H - 1): g[y][7], g[y][8] = RUNNER
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
            if not g[y][x]: continue
            c = TSC.meta(g[y][x])
            if g[y][x] in RUNNER: c = recolour(c, MAROON_RUG)
            if g[y][x] in MAT: c = recolour(c, MAROON_MAT)
            img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = c
    b = board(); img[0:32, 6 * 16:10 * 16] = b
    return img, g

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/rooms/classroom_mock.png'
    img, _ = compose(); Image.fromarray(img).resize((W * 32, H * 32), 0).save(out); print(out)
