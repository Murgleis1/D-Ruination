"""Mock of the Academy library (M1) (user design 2026-11-19: a grand reading room).

Pokemon Crown's library (map group 7 #9; credit: Blah and the Crown team, used with permission) enlarged: its
cornice and panelled back wall lined with bookshelves, the dark lattice cabinet in the middle of it (a locked
case), two freestanding stacks of shelves either side of a central reading area with two reading tables on rugs,
and the two stone busts flanking the door. Crown's marble floor. The rugs and the door mat take the Academy's
maroon with gold trim (user: maroon is the Academy's motif), as the classroom's runner.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/academy/rooms/library_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'crown'))
from crown_pieces import map_layout, TS, cell_layers
sys.path.insert(0, HERE)
from classroom_mock import MAROON_RUG, MAROON_MAT, recolour

L = map_layout(7, 9); TSL = TS(L)
W, H = 18, 15                                   # x0 and x17 void; rows 0-1 wall, 2-3 back shelves, 4-13 floor, 14 the mat
CORNICE, PANEL = (0x2C5, 0x2C6), (0x2AA, 0x2AB, 0x2AA)
SHELF = ((0x2DC, 0x2DD), (0x27C, 0x27D))
LATTICE = ((0x2BA,) * 4, (0x2E0, 0x2CA, 0x2CA, 0x2AF))
FLOOR, FLOOR_EDGE = 0x2AE, 0x2CB
BUST_L, BUST_R = (0x2CC, 0x2D4), (0x2CD, 0x27B)
RUG = ((0x40, 0x2A6, 0x2A7, 0x41), (0x48, 0x0E, 0x0E, 0x49))     # a reading table and two chairs on its rug
MAT = (0xC4, 0xC5)
STACKS = [(x, y) for y in (6, 10) for x in (1, 3, 5, 11, 13, 15)]  # top-left cells of the freestanding shelves
TABLES = [(7, 6), (7, 10)]
BUSTS = [(7, 12, BUST_L), (10, 12, BUST_R)]                       # flanking the door
RUG_IDS = {m for row in RUG for m in row}

def on_floor(m):
    """A piece whose bottom layer is wall (a shelf) or the room's edge (a bust): its top layer over plain floor."""
    (_, _), (top, tm) = cell_layers(TSL, m); img = TSL.meta(FLOOR).copy(); img[tm] = top[tm]; return img

def compose():
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    def put(x, y, cell): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cell
    for x in range(1, W - 1):
        put(x, 0, TSL.meta(CORNICE[(x - 1) % 2])); put(x, 1, TSL.meta(PANEL[(x - 1) % 3]))
        for y in range(4, H - 1): put(x, y, TSL.meta(FLOOR_EDGE if x == 1 else FLOOR))
    for x0 in (1, 3, 5, 11, 13, 15):                                # the back wall's shelves
        for dy in range(2):
            for dx in range(2): put(x0 + dx, 2 + dy, TSL.meta(SHELF[dy][dx]))
    for dy in range(2):
        for dx in range(4): put(7 + dx, 2 + dy, TSL.meta(LATTICE[dy][dx]))
    for x0, y0 in STACKS:                                           # freestanding: shelf over floor
        for dy in range(2):
            for dx in range(2): put(x0 + dx, y0 + dy, on_floor(SHELF[dy][dx]) if dy == 0 or dx == 1 else TSL.meta(SHELF[dy][dx]))
    for x0, y0 in TABLES:
        for dy in range(2):
            for dx in range(4): put(x0 + dx, y0 + dy, recolour(TSL.meta(RUG[dy][dx]), MAROON_RUG))
    for x, y, (a, b) in BUSTS: put(x, y, on_floor(a)); put(x, y + 1, on_floor(b))
    put(8, H - 1, recolour(TSL.meta(MAT[0]), MAROON_MAT)); put(9, H - 1, recolour(TSL.meta(MAT[1]), MAROON_MAT))
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/rooms/library_mock.png'
    Image.fromarray(compose()).resize((W * 32, H * 32), 0).save(out); print(out)
