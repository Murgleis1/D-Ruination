"""Mock of the abandoned, haunted teachers' lounge (T4, top floor) (user design 2026-11-19: MonoMyth's Ironbark
Cabin back room, kept dingy, with lounge furniture).

The cabin's back room (0x886B394) in the cabin's own old colours: stained walls, the boarded window, the stopped
wall clock, the cluttered desk and bookshelf, the grey tea table and stool. The bed and the PC go; in their place
the cabin's sofa (against the left wall, under the clock) and its armchair (by the tea table). Cobwebs in the two
top corners (Pokemon Crown's sewers, map group 7 #11; credit: Blah and the Crown team, used with permission).
Usage: python3 tools/art/academy/rooms/lounge_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import compose_mock as HALL
from romlib import u32, off, layout
from render import TS, map_cells

ROOM = layout(u32(off(0x0886B394))); RW = ROOM['w']; RC = map_cells(ROOM)
X0, X1, Y0, Y1 = 9, 20, 7, 16                                    # the room in its layout (with a void margin)
OLD = TS(HALL.CABIN)                                             # the cabin's original, dingy colours
EDITS = {(10, 10): 0x183, (11, 10): 0x183, (10, 11): 0x188, (11, 11): 0x188, (10, 12): 0x18B, (11, 12): 0x18B,   # the bed
         (18, 10): 0x183, (18, 11): 0x188}                                                                    # the PC
MOVED = {(10, 11): 0x18E, (11, 11): 0x18F, (10, 12): 0x196, (11, 12): 0x197,                                  # the sofa
         (18, 12): 0x1E0, (18, 13): 0x1E8}                                                                    # the armchair
PIECES = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'assets', 'crown_reference', 'pieces'))
WEBS = [(10, 8, False), (17, 8, True)]                           # cell, mirrored

def compose():
    W, H = X1 - X0, Y1 - Y0; img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(Y0, Y1):
        for x in range(X0, X1):
            m = EDITS.get((x, y), RC[y * RW + x] & 0x3FF)
            if (x, y) in MOVED: u, o, om = HALL.meta_layers(OLD, MOVED[(x, y)], clean=False, floor=m)
            else: u, o, om = HALL.meta_layers(OLD, m, clean=False)
            u = u.copy(); u[om] = o[om]; img[(y - Y0) * 16:(y - Y0 + 1) * 16, (x - X0) * 16:(x - X0 + 1) * 16] = u
    web = np.array(Image.open(os.path.join(PIECES, 'cobweb.png')).convert('RGBA'))
    for x, y, flip in WEBS:
        w = web[:, ::-1] if flip else web; m = w[..., 3] > 0
        sub = img[(y - Y0) * 16:(y - Y0) * 16 + w.shape[0], (x - X0) * 16:(x - X0) * 16 + w.shape[1]]; sub[m] = w[..., :3][m]
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/rooms/lounge_mock.png'
    img = compose(); Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), 0).save(out); print(out)
