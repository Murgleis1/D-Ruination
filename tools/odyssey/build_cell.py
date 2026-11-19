"""Templar Monastery holding cell with Pokemon Odyssey rustic pieces (user-approved mockup 2026-11-19).

    python3 -I tools/odyssey/build_cell.py

The cell doubles as a storeroom (user: prisoners are rare, there is very little crime in Pelluca Valley): hay
bales and loose straw on the prisoner's side, two stored barrels, and a plank table with two stools for the
guards. Starts from the original files in tools/odyssey/base/cell/ (reruns do not stack).
The templar_monastery secondary is used by this map only. Its palette slots are all taken, but the map's
placed art uses only 0, 3, 6 and 12; slot 7 is used only by leftover metatiles placed nowhere, so the
rustic palette goes there. New tiles take blank, unreferenced tile slots; new metatiles are appended.
Straw is walkable; hay, barrels, table and stools are solid. Eden stands at (6,4) in the scene: kept clear.
"""
import os, sys, struct, json, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from PIL import Image
import pieces

REPO = os.path.abspath(os.path.join(HERE, '..', '..')); C = os.path.join(REPO, 'codebase')
BASE = os.path.join(HERE, 'base', 'cell')
TS_DIR = os.path.join(C, 'data/tilesets/secondary/templar_monastery')
PRIM = os.path.join(C, 'data/tilesets/primary/building')
W, H = 13, 14
RUSTIC_SLOT = 7

g = np.fromfile(os.path.join(BASE, 'map.bin'), '<u2').reshape(H, W)
pm = open(os.path.join(PRIM, 'metatiles.bin'), 'rb').read()
sm = bytearray(open(os.path.join(BASE, 'metatiles.bin'), 'rb').read())
sa = bytearray(open(os.path.join(BASE, 'metatile_attributes.bin'), 'rb').read())
base_png = Image.open(os.path.join(BASE, 'tiles.png')); sheet = np.array(base_png)
prim_sheet = np.array(Image.open(os.path.join(PRIM, 'tiles.png')))
def tile_of(a, i): return a[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8]

n_base = len(sm) // 24
placed = set((g & 0x3FF).flatten().tolist())
for m in placed:
    if m >= 512:
        assert all(v >> 12 != RUSTIC_SLOT for v in struct.unpack_from('<12H', sm, (m - 512) * 24) if v & 0x3FF), 'slot 7 is in use'
ref = {(v & 0x3FF) - 512 for m in range(n_base) for v in struct.unpack_from('<12H', sm, m * 24) if v & 0x3FF >= 512}
FREE_TILES = [i for i in range(1, 512) if i not in ref and not tile_of(sheet, i).any()]
BLANK_PRIM = {i for i in range(prim_sheet.shape[0] // 8 * 16) if not tile_of(prim_sheet, i).any()}

def ents(m): return list(struct.unpack_from('<12H', pm if m < 512 else sm, (m % 512) * 24))
def attr(m):
    if m < 512: return struct.unpack_from('<H', open(os.path.join(PRIM, 'metatile_attributes.bin'), 'rb').read(), m * 2)[0]
    return struct.unpack_from('<H', sa, (m - 512) * 2)[0]
def is_empty(v):
    t = v & 0x3FF
    return t in BLANK_PRIM if t < 512 else not tile_of(sheet, t - 512).any()

tile_ids = {}
def add_tile(t):
    k = t.tobytes()
    if k not in tile_ids:
        i = FREE_TILES.pop(0); sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = t
        tile_ids[k] = 512 + i
    return tile_ids[k]
meta_ids = {}
def add_meta(e, a):
    global sm, sa
    k = (tuple(e), a)
    if k not in meta_ids:
        n = len(sm) // 24; assert n < 512
        sm += struct.pack('<12H', *e); sa += struct.pack('<H', a); meta_ids[k] = 512 + n
    return meta_ids[k]
def quad(mid): return [add_tile(t) | RUSTIC_SLOT << 12 for t in pieces.rustic(mid)]

PIECES = {   # (x, y): (rustic metatile, solid)
    (2, 3): (642, True), (3, 3): (642, True), (2, 4): (642, True),             # hay bales
    (4, 4): (649, False), (6, 3): (649, False), (7, 4): (649, False),           # loose straw
    (9, 3): (648, True), (10, 3): (648, True), (9, 4): (656, True), (10, 4): (656, True),   # stored barrels
    (8, 8): (643, True), (9, 8): (644, True), (8, 9): (651, True), (9, 9): (652, True),     # guards' table
    (7, 9): (650, True), (10, 9): (650, True),                                  # stools
}
assert (6, 4) not in PIECES                                                     # Eden's spot

def main():
    for (x, y), (mid, solid) in PIECES.items():
        under = int(g[y, x] & 0x3FF); e = pieces.overlay(ents(under), quad(mid), is_empty)
        coll = (g[y, x] >> 10) | (1 if solid else 0)
        g[y, x] = add_meta(e, attr(under)) | (coll << 10)
    g.astype('<u2').tofile(os.path.join(C, 'data/layouts/PellucaTemplarMonastery/map.bin'))
    open(os.path.join(TS_DIR, 'metatiles.bin'), 'wb').write(sm)
    open(os.path.join(TS_DIR, 'metatile_attributes.bin'), 'wb').write(sa)
    im = Image.fromarray(sheet, 'P'); im.putpalette(base_png.getpalette()); im.save(os.path.join(TS_DIR, 'tiles.png'))
    for i in range(16):
        dst = os.path.join(TS_DIR, 'palettes', f'{i:02d}.pal')
        if i == RUSTIC_SLOT:
            with open(dst, 'w', newline='') as f:
                f.write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join(f'{(r >> 3) << 3} {(gg >> 3) << 3} {(b >> 3) << 3}\r\n' for r, gg, b in pieces.RUSTIC_PAL))
        else: shutil.copy(os.path.join(BASE, 'palettes', f'{i:02d}.pal'), dst)
    print('cell: metatiles', len(sm) // 24, 'new tiles', len(tile_ids))

if __name__ == '__main__':
    main()
