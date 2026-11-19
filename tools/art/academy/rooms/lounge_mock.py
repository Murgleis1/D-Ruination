"""Mock of the abandoned, haunted teachers' lounge (T4, top floor) (user design 2026-11-19: MonoMyth's Ironbark
Cabin back room, kept dingy, with lounge furniture).

The cabin's back room (0x886B394) in the cabin's own old colours: stained walls, the boarded window, the stopped
wall clock, the cluttered desk and bookshelf, the grey tea table and stool. The bed and the PC go; in their place
the cabin's sofa (against the left wall, under the clock) and its armchair (by the tea table). Cobwebs in the two
top corners (Pokemon Crown's sewers, map group 7 #11; credit: Blah and the Crown team, used with permission).
Then (user): greyer furniture, even more decrepit walls, more webs and creepiness: the furniture drained towards grey;
the walls' own damp stains spread (grown from the stains already there, patchily) and darkened, the whole room
dimmed; the Webbed Woods' webbing (user: better than Crown's cobwebs): a sagging web net under the ceiling over the
stopped clock, zig-zag strands along the rest of the ceiling and across the desk's shelf; then (user: the strands looked
weird) the big net tilted to slant from the corner towards the window, and small webs (a corner of the same net) on
the armchair, the sofa's arm, the shelf, the top right corner and under the tea table; loose papers strewn on the
floor (Fort Elderflower archive).
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
# the webs (user: the Webbed Woods' webbing, not Crown's): (piece, x px, y px) in room pixels
WEBS = [('web_net_tilted', 16, 16, False),                               # the big net, slanting from the corner towards the window
        ('web_small', 138, 80, True),                                          # small webs: on the armchair's back,
        ('web_small', 17, 66, False),                                          # the sofa's arm,
        ('web_small', 99, 30, True),                                           # the desk's shelf,
        ('web_small', 160 - 22, 16, True),                                     # the top right corner,
        ('web_small', 94, 95, False)]                                          # the tea table's corner
PAPERS = [(13, 12), (17, 14), (11, 13)]
FURNITURE = {(x, y) for x in (10, 11) for y in (11, 12)} | {(18, 12), (18, 13), (15, 12), (16, 12), (15, 13), (16, 13)} | \
            {(x, y) for x in (15, 16) for y in (9, 10, 11)}

def compose():
    W, H = X1 - X0, Y1 - Y0; img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(Y0, Y1):
        for x in range(X0, X1):
            m = EDITS.get((x, y), RC[y * RW + x] & 0x3FF)
            if (x, y) in MOVED: u, o, om = HALL.meta_layers(OLD, MOVED[(x, y)], clean=False, floor=m)
            else: u, o, om = HALL.meta_layers(OLD, m, clean=False)
            u = u.copy(); u[om] = o[om]; img[(y - Y0) * 16:(y - Y0 + 1) * 16, (x - X0) * 16:(x - X0 + 1) * 16] = u
    import colorsys
    rng = np.random.RandomState(13)
    # the furniture drained towards grey (its own pixels: not the floor's or the wall's)
    cset = lambda ms: {tuple(c) for m in ms for c in HALL.meta_layers(OLD, m, clean=False)[0].reshape(-1, 3).tolist()}
    keep, keep_wall = cset((0x18B, 0x188, 0x183, 0x17B)), cset((0x183, 0x17B, 0x179))
    for (x, y) in FURNITURE:
        sub = img[(y - Y0) * 16:(y - Y0 + 1) * 16, (x - X0) * 16:(x - X0 + 1) * 16]
        kk = keep_wall if y <= 10 else keep                       # on the wall rows the wood is furniture too
        mk = np.array([[tuple(c) not in kk for c in row] for row in sub.tolist()])
        g = sub.mean(-1, keepdims=True); grey = (sub * 0.3 + g * 0.7).astype(np.uint8); sub[mk] = grey[mk]
    my, mx = 14 - Y0, 12 - X0                                     # the faded door mat (its own pixels)
    mat = img[my * 16:(my + 2) * 16, mx * 16:(mx + 2) * 16]
    mk = np.array([[tuple(c) not in keep for c in row] for row in mat.tolist()])
    g = mat.mean(-1, keepdims=True); faded = (mat * 0.45 + g * 0.4).astype(np.uint8); mat[mk] = faded[mk]
    # the walls (rows 8-10): grow the damp stains (the wall's darker teal) patchily, then darken the wall
    wall = img[(8 - Y0) * 16:(11 - Y0) * 16]
    cols = {tuple(c) for c in wall.reshape(-1, 3).tolist()}
    lum = lambda c: 0.3 * c[0] + 0.59 * c[1] + 0.11 * c[2]
    teal = [c for c in cols if c[1] >= c[0] and c[2] >= c[0] - 8 and 40 < lum(c) < 140]
    if teal:
        stain = min(teal, key=lum); base = (wall == stain).all(-1)
        from scipy.ndimage import binary_dilation
        grown = binary_dilation(base, iterations=3) & (rng.rand(*base.shape) < 0.55)
        grown &= np.array([[lum(c) > lum(stain) and c[1] >= c[0] for c in row] for row in wall.tolist()])
        wall[grown] = stain
    wall[:] = (wall.astype(int) * 0.82).astype(np.uint8)
    # the whole room a shade dimmer and colder
    img[:] = np.clip(img.astype(int) * np.array([0.84, 0.9, 0.95]), 0, 255).astype(np.uint8)
    MP = os.path.join(HERE, '..', '..', '..', '..', 'assets', 'monomyth_reference', 'pieces')
    for name, px, py, flip in WEBS:
        w = np.array(Image.open(os.path.join(MP, name + '.png')).convert('RGBA'))
        if flip: w = w[:, ::-1]
        m = w[..., 3] > 0
        sub = img[py:py + w.shape[0], px:px + w.shape[1]]; sub[m[:sub.shape[0], :sub.shape[1]]] = w[..., :3][:sub.shape[0], :sub.shape[1]][m[:sub.shape[0], :sub.shape[1]]]
    pp = np.array(Image.open(os.path.join(HERE, '..', '..', '..', '..', 'assets', 'monomyth_reference', 'pieces', 'papers.png')).convert('RGBA'))
    pm = pp[..., 3] > 0; prgb = (pp[..., :3].astype(int) * 0.85).astype(np.uint8)
    for x, y in PAPERS:
        sub = img[(y - Y0) * 16 + 3:(y - Y0) * 16 + 3 + pp.shape[0], (x - X0) * 16 + 2:(x - X0) * 16 + 2 + pp.shape[1]]; sub[pm] = prgb[pm]
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/rooms/lounge_mock.png'
    img = compose(); Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), 0).save(out); print(out)
