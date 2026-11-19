"""Mock of Cadmus's office (G1, off the hall's ground floor) (user design 2026-11-19: desk and bookshelves, the
Academy banner and a maroon rug, and a Water-type touch for the Vizier who masters Water).

Pokemon Crown pieces (credit: Blah and the Crown team, used with permission), in the classroom's finish so the
rooms read as one building: Crown's trim wall and plank floor, its bookcases along the back wall, the purple
Academy banner from the hall behind the desk, Crown's desk with two visitors' chairs before it on a maroon rug
(Crown's rug set: corners, edges and middle, in the Academy maroon with gold trim), and in front, greeting whoever
comes in, the harbour town's round stone fountain (Crown map group 3 #0), cut off its grass, between the manor
room's two tall iron candle stands.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/academy/rooms/office_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'crown')); sys.path.insert(0, HERE)
from crown_pieces import map_layout, TS
from classroom_mock import TSC, TRIM, WALL, FLOOR, FLOOR_SHADE, SHELF, CHAIR, MAT, MAROON_RUG, MAROON_MAT, recolour
PIECES = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'assets', 'crown_reference', 'pieces'))
sys.path.insert(0, os.path.join(HERE, '..'))
import compose_mock as HALL                                       # the hall's banner, in its purple

TSM = TS(map_layout(17, 0))                                       # the manor room's set: its rug pieces
W, H = 14, 14                                                     # x0, x13 void; rows 0-1 wall, 2-12 floor, 13 the mat
DESK = (0x05, 0x06)
RUG = {'tl': 0x40, 't': 0x326, 'tr': 0x41, 'l': 0x85, 'm': 0xDC, 'r': 0x86, 'bl': 0x48, 'b': 0x8D, 'br': 0x49}
RUG_BOX = (4, 4, 9, 6)                                            # x0, y0, x1, y1 (inclusive)
VISITORS = [(5, 4), (8, 4)]                                       # chairs facing the desk, either side of the gap
FOUNTAIN = (5, 8)                                                 # its top-left cell (4 x 4)
SHELVES = [1, 3, 9, 11]
CANDLES = [(3, 9), (10, 9)]                                       # the manor's tall iron candle stands, either side

def compose():
    img = np.zeros((H * 16, W * 16, 3), np.uint8); solid = set()
    def put(x, y, cell): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cell
    def paste(rgba, px, py):
        a = np.array(rgba); m = a[..., 3] > 0; sub = img[py:py + a.shape[0], px:px + a.shape[1]]; sub[m] = a[..., :3][m]
    for x in range(1, W - 1):
        put(x, 0, TSC.meta(TRIM)); put(x, 1, TSC.meta(WALL)); put(x, 2, TSC.meta(FLOOR_SHADE))
        for y in range(3, H - 1): put(x, y, TSC.meta(FLOOR))
    for x0 in SHELVES:
        for dy in range(2):
            for dx in range(2): put(x0 + dx, 1 + dy, TSC.meta(SHELF[dy][dx])); solid.add((x0 + dx, 1 + dy))
    b, bm = HALL.decor_piece('heraldic_banner.png', HALL.BANNER_RECOLOUR)
    sub = img[3:3 + b.shape[0], 6 * 16 + 8:6 * 16 + 8 + b.shape[1]]; sub[bm[:sub.shape[0]]] = b[:sub.shape[0]][bm[:sub.shape[0]]]
    x0, y0, x1, y1 = RUG_BOX
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            v = 't' if y == y0 else 'b' if y == y1 else ''; h = 'l' if x == x0 else 'r' if x == x1 else ''
            put(x, y, recolour(TSM.meta(RUG[v + h if v + h else 'm']), MAROON_RUG))
    for x, y in VISITORS:
        cell = recolour(TSM.meta(RUG['t']), MAROON_RUG); chair = TSC.meta(CHAIR)
        floor = TSC.meta(FLOOR); keep = (chair != floor).any(-1); cell[keep] = chair[keep]; put(x, y, cell); solid.add((x, y))
    put(6, 3, TSC.meta(DESK[0])); put(7, 3, TSC.meta(DESK[1])); solid |= {(6, 3), (7, 3)}
    paste(Image.open(os.path.join(PIECES, 'fountain.png')).convert('RGBA'), FOUNTAIN[0] * 16, FOUNTAIN[1] * 16)
    solid |= {(FOUNTAIN[0] + dx, FOUNTAIN[1] + dy) for dx in range(4) for dy in range(4)}
    for x, y in CANDLES:
        for dy, m in enumerate((0xA7, 0xAF)):
            c = TSM.meta(m); f = TSC.meta(FLOOR).copy(); keep = (c != TSM.meta(0x1)).any(-1); f[keep] = c[keep]; put(x, y + dy, f)
        solid.add((x, y + 1))
    put(6, H - 1, recolour(TSC.meta(MAT[0]), MAROON_MAT)); put(7, H - 1, recolour(TSC.meta(MAT[1]), MAROON_MAT))
    return img, solid

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/rooms/office_mock.png'
    img, _ = compose(); Image.fromarray(img).resize((W * 32, H * 32), 0).save(out); print(out)
