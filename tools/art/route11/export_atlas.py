"""Export a FireRed-hack map's metatiles (both tilesets, ids 0-1023) as an atlas for the mock composers:
<out>.npz with 'full' (1024,16,16,3: both layers) and 'top' (1024,16,16,4: the object layer, RGBA), and 'cells'
(the map's metatile ids, h x w). One ROM per run (ODYSSEY_ROM).
Usage: ODYSSEY_ROM=rom python3 export_atlas.py <groups ptr hex> <group> <num> <out.npz>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import frcut
from frrender import TS, map_cells

def main(gp, g, n, out):
    L = frcut.group_layout(int(gp, 16), int(g), int(n)); ts = TS(L)
    full = np.zeros((1024, 16, 16, 3), np.uint8); top = np.zeros((1024, 16, 16, 4), np.uint8)
    for m in range(1024):
        try: (b, _), (t, tm) = frcut.layers(ts, m)
        except Exception: continue
        c = b.copy(); c[tm] = t[tm]; full[m] = c; top[m][tm, :3] = t[tm]; top[m][tm, 3] = 255
    cells = np.array(map_cells(L), np.uint16).reshape(L['h'], L['w']) & 0x3FF
    np.savez_compressed(out, full=full, top=top, cells=cells)
    print(out, L['w'], L['h'])

if __name__ == '__main__':
    main(*sys.argv[1:5])
