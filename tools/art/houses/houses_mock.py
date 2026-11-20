"""Mocks of Pelluca's five houses (stage 1: the look only; who lives there comes later) (user design 2026-11-19).

User: Crown's medieval cottages, with MonoMyth pieces where they make sense; H1 (the two-winged timber townhouse at
(59,8)) larger, the four purple-roof cottages (H2 (54,23), H3 (64,23), H4 (54,30), H5 (64,30)) small, each laid out
differently; MonoMyth's tree-stump lodge table for H1 (user).
Kit: Pokemon Crown's cottage pair (map group 4 #1; credit: Blah and the Crown team, with permission): stone walls
with small windows, plank floor, the stone chimney breast with its hearth, bed, wardrobe, bookcases, table and
chairs, candelabras, coat stand, barrels, the door mat. MonoMyth: the stump table and stools, the braided oval and
round rugs (Wood Avens cabins 0x8868E9C / 0x8869490).
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/houses/houses_mock.py [outdir]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'crown')); sys.path.insert(0, os.path.join(ROOT, 'tools', 'monomyth'))
from crown_pieces import map_layout, TS, cell_layers

TSH = TS(map_layout(4, 1))
STONE, WINDOW, WALL_FOOT, FLOOR, SHADE, SHADE_L, EDGE_L = 0x4, 0x3, 0x57, 0x1, 0x93, 0x92, 0x9A
BED = ((0xCC, 0xC9, 0xCA), (0xD0, 0xD1, 0xD2))
WARDROBE = ((0x9D, 0x95), (0x1C, 0x1B))
BOOKCASE = ((0x9E, 0x9F), (0xC0, 0x29))
HEARTH = ((0x18E, 0x4, 0x4, 0x18F), (0x18A, 0x96, 0x97, 0x18C), (0x186, 0x8E, 0x8F, 0x1A4), (SHADE, 0x62, 0x63, SHADE))
TABLE = ((0xA5, 0x8, 0x9, 0xA6), (0xA5, 0x10, 0x11, 0xA6))
ARMCHAIR, COAT, CANDLE, BARREL = (0x16, 0x1E), (0x15, 0x1D), (0xAE, 0xC7), 0xC
MAT = (0xD8, 0xD9, 0xDA)

MM_FLOOR = 0x50                    # the Wood Avens cabins' plain plank floor (the pieces are cut against it)

def mm_piece(header, x0, y0, w, h, ref):
    """A MonoMyth piece cut against its floor; then every pixel in the floor's own colours dropped too (its planks
    vary by cell), holes filled again, so only the piece itself is left."""
    import mm_pieces
    from scipy.ndimage import binary_fill_holes
    from romlib import u32, off, layout
    a = mm_pieces.cut_diff(header, x0, y0, w, h, ref); rgb, m = a[..., :3], a[..., 3] > 0
    L = layout(u32(off(header))); fl = mm_pieces.comp(L, mm_pieces.TS(L), ref).reshape(-1, 3)
    floor = np.zeros(m.shape, bool)
    for c in {tuple(v) for v in fl.tolist()}: floor |= (rgb == c).all(-1)
    m = binary_fill_holes(m & ~floor)
    return rgb, m

def stump():          # the tree-stump table with its four stools (user: for H1)
    return mm_piece(0x08868E9C, 3, 4, 4, 3, MM_FLOOR)       # its own pale wood: it reads clearly on Crown's planks
def oval_rug():
    return mm_piece(0x08868E9C, 1, 4, 2, 5, MM_FLOOR)
def round_rug():
    return mm_piece(0x08869490, 7, 3, 2, 2, MM_FLOOR)

class Room:
    """A Crown cottage room: x0 and x W-1 void; wall rows 0-2 (stone, the window row, the wall's foot); floor rows
    3..H-2 (row 3 in the wall's shade, the left column's edge); the mat row H-1."""
    def __init__(s, W, H, windows, mat_x):
        s.W, s.H = W, H; s.g = [[0] * W for _ in range(H)]; s.over = []; s.solid = set()
        for x in range(1, W - 1):
            s.g[0][x] = STONE; s.g[1][x] = WINDOW if x in windows else STONE; s.g[2][x] = WALL_FOOT
            s.g[3][x] = SHADE_L if x == 1 else SHADE
            for y in range(4, H - 1): s.g[y][x] = EDGE_L if x == 1 else FLOOR
        for i, m in enumerate(MAT): s.g[H - 1][mat_x + i] = m
    def block(s, rows, x, y, solid_rows=None):
        for dy, row in enumerate(rows):
            for dx, m in enumerate(row):
                s.g[y + dy][x + dx] = m
                if solid_rows is None or dy in solid_rows: s.solid.add((x + dx, y + dy))
    def paste(s, piece, px, py, solid=()):
        s.over.append((piece, px, py)); s.solid |= set(solid)
    def render(s):
        img = np.zeros((s.H * 16, s.W * 16, 3), np.uint8)
        for y in range(s.H):
            for x in range(s.W):
                if s.g[y][x]: img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = TSH.meta(s.g[y][x])
        for (rgb, m), px, py in s.over:
            sub = img[py:py + rgb.shape[0], px:px + rgb.shape[1]]; sub[m] = rgb[m]
        return img

def h2():
    """A hearth cottage: the chimney breast in the middle, the bed on the left, wardrobe and bookcase on the right,
    the table below them; a round rug before the fire."""
    r = Room(13, 10, windows={2, 3, 9, 10}, mat_x=5)
    r.block(BED, 1, 3); r.block(HEARTH, 4, 3, solid_rows={0, 1, 2, 3})
    r.block(WARDROBE, 8, 2, solid_rows={1}); r.block(BOOKCASE, 10, 2, solid_rows={1})
    r.block(TABLE, 8, 5); r.block((CANDLE[:1], CANDLE[1:]), 1, 7); r.block((COAT[:1], COAT[1:]), 11, 7)
    r.paste(round_rug(), 5 * 16, 7 * 16)
    return r

def h3():
    """A family cottage: two beds against the back wall, the table and chairs in the middle on an oval rug, the
    hearth in the corner, barrels by the door."""
    r = Room(13, 10, windows={4, 8}, mat_x=5)
    r.block(BED, 1, 3); r.block(BED, 9, 3); r.block(BOOKCASE, 5, 2, solid_rows={1})
    r.block(TABLE, 4, 5); r.block(((BARREL, BARREL), (BARREL, BARREL)), 10, 7)
    r.block((CANDLE[:1], CANDLE[1:]), 1, 7)
    return r

def h4():
    """A scholar's cottage: bookcases along the back wall, the hearth with an armchair beside it and a round rug
    before it, the bed in the corner, a table on the left."""
    r = Room(13, 10, windows={6, 7}, mat_x=5)
    r.block(BOOKCASE, 1, 2, solid_rows={1}); r.block(BOOKCASE, 3, 2, solid_rows={1})
    r.block(HEARTH, 5, 3, solid_rows={0, 1, 2, 3}); r.block(BED, 9, 3)
    r.block((ARMCHAIR[:1], ARMCHAIR[1:]), 9, 5); r.block(TABLE, 1, 5); r.block((COAT[:1], COAT[1:]), 11, 7)
    r.paste(round_rug(), 6 * 16, 7 * 16)
    return r

def h5():
    """A small cottage: one bed and wardrobe, a table by the window, barrels and the coat stand."""
    r = Room(11, 9, windows={3, 7}, mat_x=4)
    r.block(BED, 7, 3); r.block(WARDROBE, 1, 2, solid_rows={1}); r.block(TABLE, 2, 5)
    r.block(((BARREL,), (BARREL,)), 9, 6); r.block((COAT[:1], COAT[1:]), 1, 6)
    r.paste(round_rug(), 5 * 16, 6 * 16)
    return r

def h1():
    """The townhouse (larger): Crown's two-room plan, the chimney breast dividing a living room on the left from the
    bedroom on the right; MonoMyth's stump table with its stools in the living room (user), a round rug before the fire."""
    r = Room(19, 11, windows={2, 3, 5, 13, 15, 16}, mat_x=8)
    r.block(BOOKCASE, 1, 2, solid_rows={1}); r.block(BOOKCASE, 3, 2, solid_rows={1})
    r.block(HEARTH, 7, 3, solid_rows={0, 1, 2, 3})
    r.block(WARDROBE, 12, 2, solid_rows={1}); r.block(BED, 15, 3); r.block(TABLE, 13, 6)
    st = stump(); r.paste(st, 2 * 16, 5 * 16, solid={(3, 6), (4, 6)})
    r.paste(round_rug(), 8 * 16, 7 * 16)
    r.block((CANDLE[:1], CANDLE[1:]), 1, 8); r.block((CANDLE[:1], CANDLE[1:]), 17, 8)
    r.block((ARMCHAIR[:1], ARMCHAIR[1:]), 11, 6)
    return r

HOUSES = {'H1': h1, 'H2': h2, 'H3': h3, 'H4': h4, 'H5': h5}

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/houses'
    for k, f in HOUSES.items():
        r = f(); Image.fromarray(r.render()).resize((r.W * 32, r.H * 32), 0).save(os.path.join(out, f'{k}_mock.png')); print(k)
