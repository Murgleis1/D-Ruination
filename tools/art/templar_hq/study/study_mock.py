"""Ambrose's study (user 2026-11-23: Crown's office 7.9 as the base, with MonoMyth's writing desk and bureau).
Base: Crown 7.9 (crown79.png, an 11x9 render; the room is columns 1-8, the exit mat at columns 4-5 on row 8): its
bookcases, busts on plinths and cream marble floor kept. Changes:
- the wallpaper (rows 0-1) recoloured to the cathedral's cream stone;
- the rug recoloured to the Order's blue with a gold trim (the nave carpet's colours);
- Crown's desk and two chairs taken out (the rug rebuilt beneath them) and MonoMyth's writing desk (paper, quill
  and inkwell; from its dark-wood office, layout 0x87ffdfc, mm_office.png) set on the rug, centred, its stool and
  the wall picture above it left out;
- MonoMyth's bureau set against the back panelling right of centre, over Crown's small chest;
- the exit mat in the same blue and gold;
- MonoMyth's mauve wood re-toned to the brown of Crown's bookcases.
Pieces are cut from the render cell by cell: a pixel is see-through where it equals a plain floor or wall cell of
the source room at the same position; enclosed see-through patches are part of the furniture.
Credits: Pokemon Crown, MonoMyth.  Usage: python3 study_mock.py OUT.png"""
import os, sys
import numpy as np
from PIL import Image
from scipy.ndimage import label
HERE = os.path.dirname(os.path.abspath(__file__)); T = 16
WOOD = {(56, 56, 64): (40, 40, 48), (72, 64, 64): (64, 40, 32), (88, 72, 72): (96, 60, 44), (104, 80, 88): (128, 80, 56),
        (104, 80, 80): (128, 80, 56), (128, 96, 96): (168, 120, 72), (152, 136, 128): (200, 152, 96),
        (168, 152, 144): (224, 184, 128)}
WALL = {(152, 136, 104): (208, 200, 180), (120, 104, 96): (166, 156, 130), (184, 184, 160): (230, 224, 208),
        (96, 80, 72): (140, 132, 110)}
RUG = {(216, 112, 104): (36, 74, 155), (200, 88, 80): (28, 60, 130), (160, 64, 104): (0, 40, 82),
       (104, 56, 88): (0, 30, 64), (208, 216, 104): (177, 149, 48)}

def recolour(a, table, mask):
    for s, d in table.items():
        a[mask & (a[..., :3] == s).all(-1)] = d

def mm_piece(x0, y0, w, h):
    a = np.array(Image.open(os.path.join(HERE, 'mm_office.png')).convert('RGB')).astype(int)
    cell = lambda x, y: a[y * T:(y + 1) * T, x * T:(x + 1) * T]
    floors = [cell(x, y) for y in (4, 5, 6, 7) for x in range(3, 9)]
    refs = {0: [cell(3, 0), cell(4, 0)], 1: [cell(3, 1), cell(4, 1), cell(1, 1)]}
    out = np.zeros((h * T, w * T, 4), int)
    for j in range(h):
        for i in range(w):
            c = cell(x0 + i, y0 + j); same = np.zeros((T, T), bool)
            for r in refs.get(y0 + j, []) + floors: same |= (c == r).all(-1)
            out[j * T:(j + 1) * T, i * T:(i + 1) * T, :3] = c
            out[j * T:(j + 1) * T, i * T:(i + 1) * T, 3] = np.where(same, 0, 255)
    lb, n = label(out[..., 3] == 0)
    edge = set(lb[0]) | set(lb[-1]) | set(lb[:, 0]) | set(lb[:, -1])
    for k in range(1, n + 1):
        if k not in edge: out[lb == k, 3] = 255
    recolour(out[..., :3], WOOD, out[..., 3] > 0)
    return out

def paste(img, p, x, y):
    h, w = p.shape[:2]; m = p[..., 3] > 0
    img[y:y + h, x:x + w][m] = p[..., :3][m]

def main(out):
    img = np.array(Image.open(os.path.join(HERE, 'crown79.png')).convert('RGB')).astype(int)
    H, W = img.shape[:2]; yy, xx = np.mgrid[0:H, 0:W]
    recolour(img, WALL, (yy < 2 * T) & (xx >= T) & (xx < 9 * T))
    # the rug beneath Crown's desk and chairs: its own column x=60 carried across x 64-95
    img[4 * T:6 * T, 4 * T:6 * T] = img[4 * T:6 * T, 60:61]
    recolour(img, RUG, (yy >= 4 * T) & (yy < 6 * T) & (xx >= 3 * T) & (xx < 7 * T))
    # the exit mat in the same blue and gold
    recolour(img, {(160, 64, 104): (36, 74, 155), (200, 88, 80): (0, 40, 82), (192, 168, 168): (177, 149, 48)},
             (yy >= 8 * T) & (xx >= 4 * T) & (xx < 6 * T))
    # Crown's small chest at (6,3) cleared to floor (the bureau stands there)
    img[3 * T:4 * T, 6 * T:7 * T] = img[3 * T:4 * T, 5 * T:6 * T]
    # MonoMyth's bureau, cols 5-6 rows 2-3
    paste(img, mm_piece(5, 1, 2, 2), 5 * T, 2 * T)
    # MonoMyth's desk: its rows 1-2 and the top of row 3 (the leg rail), the wall picture cleared
    d = mm_piece(7, 1, 2, 3)[:2 * T + 4]
    d[0:12, T:2 * T, 3] = 0
    rail = d[2 * T:, :, :3]; d[2 * T:, :, 3] = np.where(rail.sum(-1) < 200, 255, 0)
    paste(img, d, 4 * T, 3 * T)
    o = Image.fromarray(img.astype(np.uint8)); o.save(out)
    o.resize((W * 3, H * 3), Image.NEAREST).save(out.replace('.png', '_3x.png'))

if __name__ == '__main__':
    main(sys.argv[1])
