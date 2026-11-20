"""Mocks of Pelluca's five houses (stage 1: the look only; who lives there comes later) (user design 2026-11-19).

User: Crown's medieval cottages, with MonoMyth pieces where they make sense; H1 (the two-winged timber townhouse at
(59,8)) larger, the four purple-roof cottages (H2 (54,23), H3 (64,23), H4 (54,30), H5 (64,30)) small, each laid out
differently; MonoMyth's tree-stump lodge table for H1 (user).
Kit: Pokemon Crown's cottage pair (map group 4 #1; credit: Blah and the Crown team, with permission): stone walls
with small windows, plank floor, the stone chimney breast with its hearth, bed, wardrobe, bookcases, table and
chairs, candelabras, coat stand, barrels, the door mat; the manor's upright organ (group 4 #0); the alchemist's
desk, potion shelf and cauldron (group 18 #1). MonoMyth: the stump table and stools (Wood Avens cabin 0x8868E9C).
User: no hearths in these houses, no round rugs.
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
TABLE = ((0xA5, 0x8, 0x9, 0xA6), (0xA5, 0x10, 0x11, 0xA6))
COAT, CANDLE, BARREL = (0x15, 0x1D), (0xAE, 0xC7), 0xC   # (user: no free-standing chair-and-harp piece mid-floor)
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
TSM = TS(map_layout(4, 0))          # Crown's manor (same primary): its upright organ on its rug
ORGAN_TOP, ORGAN_RUG = (0x58, 0x59), ((0x40, 0x60, 0x61, 0x41), (0x48, 0x8D, 0x8D, 0x49))

def crown_cut(x0, y0, w, h):
    from crown_pieces import cut
    a = cut(18, 1, x0, y0, w, h); return a[..., :3], a[..., 3] > 0
def alchemy_desk(): return crown_cut(2, 1, 2, 2)      # Crown's alchemist's room (group 18 #1): the cluttered desk,
def potion_shelf(): return crown_cut(5, 1, 2, 2)      # the potion shelf,
def cauldron(): return crown_cut(8, 1, 2, 2)          # the cauldron

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
    def organ(s, x):
        """Crown's upright organ against the back wall at columns x+1..x+2, on its rug (x..x+3, two rows)."""
        s.g[2][x + 1], s.g[2][x + 2] = ('top', ORGAN_TOP[0]), ('top', ORGAN_TOP[1])
        for dy, row in enumerate(ORGAN_RUG):
            for dx, m in enumerate(row): s.g[3 + dy][x + dx] = 0x10000 + m
        s.solid |= {(x + 1, 3), (x + 2, 3)}
    def paste(s, piece, px, py, solid=()):
        s.over.append((piece, px, py)); s.solid |= set(solid)
    def render(s):
        img = np.zeros((s.H * 16, s.W * 16, 3), np.uint8)
        for y in range(s.H):
            for x in range(s.W):
                v = s.g[y][x]
                if isinstance(v, tuple):                                  # ('organ top', id): its top layer on the wall
                    c = TSH.meta(WALL_FOOT).copy(); (_, _), (tp, tm) = cell_layers(TSM, v[1]); c[tm] = tp[tm]
                    img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = c
                elif v >= 0x10000: img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = TSM.meta(v - 0x10000)
                elif v: img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = TSH.meta(v)
        for (rgb, m), px, py in s.over:
            sub = img[py:py + rgb.shape[0], px:px + rgb.shape[1]]; sub[m] = rgb[m]
        return img

def h2():
    """The cauldron cottage: Crown's iron cauldron against the back wall (user: no hearths; something no other house
    has), the bed on the left, wardrobe and bookcase on the right, the table below them."""
    r = Room(13, 10, windows={2, 3, 9, 10}, mat_x=5)
    r.block(BED, 1, 3); r.paste(cauldron(), 5 * 16, 2 * 16, solid={(5, 3), (6, 3)})
    r.block(WARDROBE, 8, 2, solid_rows={1}); r.block(BOOKCASE, 10, 2, solid_rows={1})
    r.block(TABLE, 8, 5); r.block((CANDLE[:1], CANDLE[1:]), 1, 7); r.block((COAT[:1], COAT[1:]), 11, 7)
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
    """The alchemist's cottage: bookcases, then Crown's cluttered alchemy desk and potion shelf against the back wall
    (user: no hearth; something unique), the bed in the corner, a table on the left."""
    r = Room(13, 10, windows={6, 7}, mat_x=5)
    r.block(BOOKCASE, 1, 2, solid_rows={1}); r.block(BOOKCASE, 3, 2, solid_rows={1})
    r.paste(alchemy_desk(), 5 * 16, 2 * 16, solid={(5, 3), (6, 3)}); r.paste(potion_shelf(), 7 * 16, 2 * 16, solid={(7, 3), (8, 3)})
    r.block(BED, 9, 3)
    r.block(TABLE, 1, 5); r.block((COAT[:1], COAT[1:]), 11, 7)
    return r

def h5():
    """A small cottage: one bed and wardrobe, a table by the window, barrels and the coat stand."""
    r = Room(11, 9, windows={3, 7}, mat_x=4)
    r.block(BED, 7, 3); r.block(WARDROBE, 1, 2, solid_rows={1}); r.block(TABLE, 2, 5)
    r.block(((BARREL,), (BARREL,)), 9, 6); r.block((COAT[:1], COAT[1:]), 1, 6)
    return r

def h1():
    """The townhouse (larger): bookcases and MonoMyth's stump table with its stools on the left (user), Crown's upright
    organ on its rug in the middle (user: no hearth; something unique), the bedroom end on the right."""
    r = Room(19, 11, windows={2, 3, 5, 13, 15, 16}, mat_x=8)
    r.block(BOOKCASE, 1, 2, solid_rows={1}); r.block(BOOKCASE, 3, 2, solid_rows={1})
    r.organ(7)
    r.block(WARDROBE, 12, 2, solid_rows={1}); r.block(BED, 15, 3); r.block(TABLE, 13, 6)
    st = stump(); r.paste(st, 2 * 16, 5 * 16, solid={(3, 6), (4, 6)})
    r.block((CANDLE[:1], CANDLE[1:]), 1, 8); r.block((CANDLE[:1], CANDLE[1:]), 17, 8)
    return r

HOUSES = {'H1': h1, 'H2': h2, 'H3': h3, 'H4': h4, 'H5': h5}

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/houses'
    for k, f in HOUSES.items():
        r = f(); Image.fromarray(r.render()).resize((r.W * 32, r.H * 32), 0).save(os.path.join(out, f'{k}_mock.png')); print(k)
