"""Import MonoMyth's Fort Elderflower interior tilesets into Ruination unchanged (both games use
triple-layer 24-byte metatiles, 512/512 tile and metatile splits, palettes 0-5 primary / 6-12
secondary), plus a crop of one interior as a Ruination layout.

The only art change is a palette swap the user asked for (2026-11-16): the interior wood
(primary palette 2) goes from a cool mauve to a warm medieval brown. It is a palette edit, so
every floorboard, table edge and stair in every Elderflower interior turns brown together and no
pixel changes position.

Usage: python3 -I tools/monomyth/import_interior.py codebase
"""
import os, sys, json, struct
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from render import tileset, tiles_of, pals_of, map_cells, off, u16, ROM

PRIMARY = 0x8731254          # Fort Elderflower interiors (192 metatiles, 288 tiles)
SECONDARIES = {'elderflower_study': 0x8730C3C}   # the study / small rooms; the tavern uses 0x8730E4C

# Primary palette 2: the mauve wood -> warm oak. Index: (old) -> new. Greys (rug, sofa) untouched.
WOOD = {
    2:  (62, 44, 34),     # (72,64,64)   dark outline of wood pieces
    3:  (176, 132, 88),   # (152,136,128) light wood
    4:  (142, 96, 58),    # (128,96,96)   floorboard body
    8:  (104, 68, 44),    # (104,80,88)   table edge shadow
    9:  (198, 158, 110),  # (168,152,144) wood highlight
    14: (114, 76, 48),    # (104,80,80)   floorboard grain
    15: (78, 52, 34),     # (88,72,72)    plank seams / darkest wood
}
PAL_OVERRIDES = {2: WOOD}


def gba(c):  # snap to the 5-bit colour the hardware will show
    return tuple((v >> 3) << 3 for v in c)


def write_ts(d, ts_rom, n_meta, slots, is_sec):
    os.makedirs(os.path.join(d, 'palettes'), exist_ok=True)
    tiles = tiles_of(ts_rom)
    pals = pals_of(ts_rom)
    for s, over in PAL_OVERRIDES.items():
        if (s >= 6) == is_sec:
            for i, c in over.items():
                pals[s][i] = gba(c)
    n = max(16, ((len(tiles) + 15) // 16) * 16)
    sheet = np.zeros((n // 16 * 8, 128), np.uint8)
    for i, t in enumerate(tiles):
        sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = t
    im = Image.fromarray(sheet, 'P')
    show = pals[6 if is_sec else 2]
    im.putpalette([v for c in show for v in c] + [0] * (768 - 48)); im.save(os.path.join(d, 'tiles.png'))
    for i in range(16):
        cols = pals[i] if i in slots else [(0, 0, 0)] * 16
        with open(os.path.join(d, 'palettes', f'{i:02d}.pal'), 'w', newline='') as f:
            f.write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join(f'{r} {g} {b}\r\n' for r, g, b in cols))
    mt = ROM[off(ts_rom['mt']):off(ts_rom['mt']) + n_meta * 24]
    at = ROM[off(ts_rom['attr']):off(ts_rom['attr']) + n_meta * 2]
    open(os.path.join(d, 'metatiles.bin'), 'wb').write(mt)
    open(os.path.join(d, 'metatile_attributes.bin'), 'wb').write(at)
    return len(tiles), n_meta


def n_metatiles(ts_rom):
    return (ts_rom['attr'] - ts_rom['mt']) // 24


def main(C):
    P = tileset(PRIMARY)
    print('primary', write_ts(os.path.join(C, 'data/tilesets/primary/elderflower_interior'), P,
                              n_metatiles(P), set(range(6)), False))
    for name, a in SECONDARIES.items():
        S = tileset(a)
        print(name, write_ts(os.path.join(C, f'data/tilesets/secondary/{name}'), S,
                             n_metatiles(S), set(range(6, 13)), True))


if __name__ == '__main__':
    main(sys.argv[1])
