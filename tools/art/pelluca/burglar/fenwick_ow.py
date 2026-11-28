"""Burglar Fenwick's overworld sprite (2026-11-27): no reference game has a walking sprite for Odyssey's ragged hooded
thief, so it is built from Ruination's own commoner man B (dr_commoner_man_b, 9 frames) recoloured to his battle
picture: the hair blue-black, the shirt the darker beige of his tunic, the trousers the grey-blue of his leg wraps.
Usage: python3 tools/art/pelluca/burglar/fenwick_ow.py [--write]"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
PEOPLE = os.path.join(HERE, '..', '..', '..', '..', 'codebase/graphics/object_events/pics/people')
SRC, OUT = os.path.join(PEOPLE, 'dr_commoner_man_b.png'), os.path.join(PEOPLE, 'dr_burglar.png')
NEW = {11: (62, 78, 104), 12: (40, 52, 76), 13: (26, 32, 50),       # hair (and boots): blue-black, as his picture
       5: (146, 128, 94), 6: (112, 98, 74), 7: (84, 72, 56),           # shirt: the darker beige tunic
       8: (88, 100, 110), 9: (62, 70, 82), 10: (42, 48, 58)}           # trousers: the grey-blue leg wraps

def build():
    im = Image.open(SRC); P = im.getpalette()[:48]
    for i, c in NEW.items(): P[i * 3:i * 3 + 3] = list(c)
    out = im.copy(); out.putpalette(P); return out

if __name__ == '__main__':
    out = build()
    if '--write' in sys.argv: out.save(os.path.abspath(OUT)); print('written', os.path.abspath(OUT))
    out.convert('RGBA').resize((out.width * 5, out.height * 5), 0).save('/tmp/fenwick_ow_x5.png')
