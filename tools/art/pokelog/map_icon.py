"""16x16 region-map player icon: a heraldic eagle head in profile (bronze and gold), Cormoria's symbol. Replaces Brendan's face (graphics/pokenav/region_map/brendan_icon / may_icon)."""
import os
import numpy as np
from PIL import Image
ART = [  # heraldic eagle head in profile, Cormoria's symbol (user 2026-11-18)
 "................",
 "....ooooo.......",
 "..ooLLLFFoo.....",
 ".oLLFFFFffffoo..",
 ".oLFFFFFwoFFFoo.",
 "oLFFFFFFooffBBBo",
 "oLFFFFFFFffBBBBo",
 "oFFFFFFFFfoBBbbo",
 "oFFfFFFFFfo.obbo",
 "oFFffFFFfo...obo",
 ".oFFffFFfo....o.",
 ".oFfFffFFfo.....",
 "..oFfoFffFfo....",
 "..ofo.ofo.ofo...",
 "...o...o...o....",
 "................"]
PAL = [(0, 0, 0), (40, 24, 16), (136, 88, 32), (192, 136, 48), (232, 192, 96), (240, 208, 64),
       (184, 136, 24), (248, 240, 200)]
KEY = {'.': 0, 'o': 1, 'f': 2, 'F': 3, 'L': 4, 'B': 5, 'b': 6, 'w': 7}
def icon():
    return np.array([[KEY[c] for c in row] for row in ART], np.uint8)
def save_png(path):
    im = Image.fromarray(icon(), 'P'); pal = [v for c in PAL for v in c]; im.putpalette(pal + [0] * (48 - len(pal)))
    im.save(path, transparency=0)
if __name__ == '__main__':
    a = np.array(PAL, np.uint8)[icon()]; a[icon() == 0] = (120, 160, 110)
    Image.fromarray(a).resize((128, 128), Image.NEAREST).save('/tmp/osrid_icon.png')
