"""16x16 region-map player icon: Osrid's mask -- a cream oval with the Eye of Horus at its centre. Replaces Brendan's face (graphics/pokenav/region_map/brendan_icon / may_icon)."""
import os
import numpy as np
from PIL import Image
ART = [  # Osrid's mask: an oval with the Eye of Horus (user 2026-11-18)
 ".....oooooo.....",
 "...ooMMMMMMoo...",
 "..oMMMMMMMMMmo..",
 "..oMeeeeeeeemo..",
 ".oMMMMMMMMMMMmo.",
 ".oMMMMeeeeMMMmo.",
 ".oMMMeMeeMeMMmo.",
 ".oMMeMMeeMMeeeo.",
 ".oMMMeMMMMeMMmo.",
 ".oMMMMeeeeMMMmo.",
 ".oMMMMMeMMeMMmo.",
 "..oMMMMeMMMeMo..",
 "..oMMMMeMMeeMo..",
 "...oMMMMMMMmo...",
 "....oMMMMMmo....",
 ".....oooooo....."]
PAL = [(0, 0, 0), (24, 16, 16), (128, 48, 24), (200, 88, 40), (240, 144, 80), (248, 240, 224),
       (208, 192, 168), (24, 24, 24), (40, 72, 48), (72, 120, 80)]
KEY = {'.': 0, 'o': 1, 'd': 2, 'h': 3, 'H': 4, 'M': 5, 'm': 6, 'e': 7, 'E': 7, 'G': 8, 'g': 9}
def icon():
    return np.array([[KEY[c] for c in row] for row in ART], np.uint8)
def save_png(path):
    im = Image.fromarray(icon(), 'P'); pal = [v for c in PAL for v in c]; im.putpalette(pal + [0] * (48 - len(pal)))
    im.save(path, transparency=0)
if __name__ == '__main__':
    a = np.array(PAL, np.uint8)[icon()]; a[icon() == 0] = (120, 160, 110)
    Image.fromarray(a).resize((128, 128), Image.NEAREST).save('/tmp/osrid_icon.png')
