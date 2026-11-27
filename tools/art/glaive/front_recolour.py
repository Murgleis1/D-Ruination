"""Glaive battle front pic: hair and skin recoloured to the portrait / overworld palette (user 2026-11-27: "the
front sprite's hair colour doesn't match his portrait or overworld sprites"). Works from the committed source
(b12db3cd7) so it can be re-run. Run: python3 front_recolour.py [--write]"""
import os, subprocess, sys, io
import numpy as np
from PIL import Image
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
PNG = os.path.join(ROOT, 'codebase', 'graphics', 'trainers', 'front_pics', 'glaive.png')
SRC = 'b12db3cd7:codebase/graphics/trainers/front_pics/glaive.png'

# Portrait colours: hair main 4 (148,56,44), highlight 12 (181,69,54), darkest 2 (64,24,19); skin 1 / 7.
NEW = {1: (243, 197, 172), 2: (209, 155, 123), 6: (148, 56, 44), 10: (64, 24, 19),
       14: (181, 69, 54),                     # new: hair highlight
       15: (160, 146, 143),                   # new: shoe / buckle grey that used to borrow the skin entries
       3: (77, 157, 70)}                      # eye green (portrait idx 8); its old grey merges into 4 (7 apart)
NONSKIN = [(32, 33), (33, 33), (34, 33), (32, 34), (33, 34),                         # belt buckle
           (24, 61), (39, 59), (40, 59), (23, 60), (24, 60), (38, 60), (39, 60), (40, 60), (41, 60),
           (22, 61), (23, 61), (25, 61)]                                             # shoes
WRIST = [(24, 34), (40, 34)]                  # the two hair-index px under the hands are skin shadow

# Face on the warm skin: the grey feature index (3, shared with the suit) read as smudges. Eyes go green like the
# portrait (user 2026-11-27), the mouth to skin shadow, the ear top to hair dark and the px under the right eye to skin shadow.
FACE = {(30, 9): 3, (35, 9): 3, (34, 10): 2, (32, 13): 2, (26, 8): 10}
MOUTH = [(31, 13)]                            # mouth widened to 2 px of skin shadow, like the portrait's soft mouth
# Hair highlight streaks on the top-left of each clump, the way the portrait and overworld are lit.
HILITE = [(28, 2), (29, 2), (27, 3), (28, 3), (33, 2), (34, 2), (32, 3), (27, 6), (26, 7), (36, 4)]
# Scar at the spot the user picked (cells x30-31, y11-12): soft diagonal in skin shadow.
SCAR = [(30, 11), (31, 12)]

def source():
    raw = subprocess.run(['git', '-C', ROOT, 'show', SRC], capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(raw))

def recolour(hilite=HILITE, face=True, scar=True):
    im = source(); a = np.array(im); pal = list(im.getpalette()[:48])
    for i, c in NEW.items(): pal[3 * i:3 * i + 3] = c
    face_px = set(FACE)
    for y, x in np.argwhere(a == 3):
        if (x, y) not in face_px: a[y, x] = 4          # suit grey (102,94,99) -> (95,87,92)
    for x, y in NONSKIN:
        assert a[y, x] in (1, 2), (x, y, a[y, x]); a[y, x] = 15
    for x, y in WRIST:
        assert a[y, x] == 6; a[y, x] = 2
    for x, y in hilite:
        assert a[y, x] == 6, (x, y, a[y, x]); a[y, x] = 14
    if face:
        for (x, y), c in FACE.items():
            assert a[y, x] == 3, (x, y, a[y, x]); a[y, x] = c if c != 3 else 3
        for x, y in MOUTH:
            assert a[y, x] == 1; a[y, x] = 2
    if scar:
        for x, y in SCAR:
            assert a[y, x] == 1; a[y, x] = 2
    return a, pal

def save(a, pal, path=PNG):
    o = Image.fromarray(a.astype(np.uint8), 'P'); o.putpalette(pal + [0] * (768 - len(pal))); o.save(path, transparency=0)

if __name__ == '__main__':
    a, pal = recolour()
    if '--write' in sys.argv: save(a, pal)
