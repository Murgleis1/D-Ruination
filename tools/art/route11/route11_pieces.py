"""Cut Route 11's borrowed pieces out of their source ROMs into assets/route11_reference/pieces/ (RGBA PNGs).

Sources (each its own run: frlib reads one ROM per process):
  crown    Pokemon Crown (credit: Blah and the Crown team, used with permission): the seaside farm village
           (map 3.1: thatched cottage, wooden fences, flower rows, soil mounds, stumps, scarecrow post, tan cliffs)
           and the dark forest (map 3.25: broadleaf trees, dark grass, tall grass, cobwebs).
  odyssey  Pokemon Odyssey: the farm (map 0.232: cabbage rows, the sown field, hay bales, pitchfork).
Usage: python3 tools/art/route11/route11_pieces.py crown|odyssey
"""
import os, sys
SRC = sys.argv[1] if len(sys.argv) > 1 else 'crown'
os.environ['ODYSSEY_ROM'] = {'crown': '/home/claude/crown/Crown.gba', 'odyssey': '/home/claude/odyssey/odyssey.gba'}[SRC]
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from PIL import Image
import frcut
OUT = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'assets', 'route11_reference', 'pieces'))
GROUPS = {'crown': 0x8711468, 'odyssey': 0x83526A8}[SRC]

PIECES = {
  'crown': {   # name: (group, num, x0, y0, w, h, mode)
    'cottage': (3, 1, 12, 9, 7, 4, 'top'),
    'fence_row': (3, 1, 12, 23, 6, 1, 'key', [(3, 18), (2, 18), (5, 15), (13, 15)]),
    'fence_col': (3, 1, 17, 23, 1, 5, 'key', [(3, 18), (2, 18), (5, 15), (13, 15), (18, 24), (18, 26)]),
    'flower_rows': (3, 1, 12, 24, 5, 4, 'top'),
    'soil_mounds': (3, 1, 44, 24, 2, 1, 'top'),
    'stumps': (3, 1, 6, 16, 2, 2, 'top'),
    'scarecrow': (3, 1, 8, 16, 1, 2, 'top'),
    'axe_stump': (3, 1, 14, 21, 1, 1, 'top'),
    'hedge': (3, 1, 22, 15, 5, 6, 'top'),
    'sign': (3, 1, 23, 20, 1, 1, 'top'),
    'cliffs': (3, 1, 0, 0, 13, 14, 'full'),
    'pines': (3, 1, 0, 21, 12, 9, 'full'),
    'dark_forest': (3, 25, 0, 0, 42, 30, 'full'),
    'dark_tree': (3, 25, 12, 15, 3, 4, 'key', [(16, 10), (3, 8), (6, 9), (1, 8), (15, 17), (16, 18), (11, 18), (11, 17)]),
    'dark_tree_b': (3, 25, 3, 5, 3, 3, 'key', [(16, 10), (3, 8), (6, 9), (1, 8), (2, 8), (6, 7)]),
    'dark_trees_top': (3, 25, 0, 0, 42, 30, 'top'),
  },
  'odyssey': {
    'cabbages': (0, 232, 17, 7, 8, 3, 'key', [(6, 13), (7, 13), (13, 12), (12, 15), (20, 11), (5, 9)]),
    'field': (0, 232, 17, 12, 9, 4, 'full'),
    'hay_big': (0, 232, 9, 9, 2, 2, 'top'),
    'hay_small': (0, 232, 15, 10, 2, 3, 'top'),
    'pitchfork': (0, 232, 8, 10, 1, 2, 'top'),
    'grass': (0, 232, 6, 13, 1, 1, 'full'),
  },
}[SRC]

def main():
    os.makedirs(OUT, exist_ok=True)
    for name, (g, n, x0, y0, w, h, mode, *ref) in PIECES.items():
        L = frcut.group_layout(GROUPS, g, n)
        a = frcut.cut(L, x0, y0, w, h, mode, ref[0] if ref else None)
        Image.fromarray(a, 'RGBA').save(os.path.join(OUT, f'{SRC}_{name}.png'))
        print(name, a.shape)

if __name__ == '__main__':
    main()
