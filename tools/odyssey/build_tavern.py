"""Seaside Tavern with Pokemon Odyssey pieces (user-approved mockup 2026-11-19, tools/odyssey/pelluca_odyssey_mock.py).

    python3 -I tools/odyssey/build_tavern.py

Always starts from the original files saved in tools/odyssey/base/tavern/ (so reruns do not stack), and writes:
  - data/layouts/PellucaTavern/map.bin: one floor row added under the back wall (user: the space behind the bar
    was "really tight"; two rows moved the bar "too much"). The bar and everything below move down one row.
    The behind-the-bar row keeps the bar's back edge but loses its baked-in wall shadow (user: "this shadow
    on the ground needs to go away"); the new row under the wall carries the wall's shadow instead.
  - the brick hearth on the back wall (cols 4-6), lit (MonoMyth's fire, animated: anim/fire, palette 9),
    plates on the two round tables, barrels in the front corners.
  - data/tilesets/secondary/elderflower_tavern: new tiles from 229, new metatiles from 562, palettes 10-12.
  - data/maps/PellucaCityPokemonCenter/map.json: NPCs and the exit moved down with the room.
The tavern secondary is used by this map only; its placed art uses palette slot 2 only (checked).
"""
import os, sys, struct, json, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
from PIL import Image
import pieces

REPO = os.path.abspath(os.path.join(HERE, '..', '..')); C = os.path.join(REPO, 'codebase')
BASE = os.path.join(HERE, 'base', 'tavern')
TS_DIR = os.path.join(C, 'data/tilesets/secondary/elderflower_tavern')
PRIM = os.path.join(C, 'data/tilesets/primary/elderflower_interior')
W, H0 = 14, 11
HEARTH_SLOT, PLATE_SLOT, RUSTIC_SLOT, FIRE_SLOT = 10, 11, 12, 9
FIRST_TILE, FIRST_META = 229, 562
SOLID = 1 | 3 << 2

base = np.fromfile(os.path.join(BASE, 'map.bin'), '<u2').reshape(H0, W)
pm = open(os.path.join(PRIM, 'metatiles.bin'), 'rb').read()
sm = bytearray(open(os.path.join(BASE, 'metatiles.bin'), 'rb').read())
sa = bytearray(open(os.path.join(BASE, 'metatile_attributes.bin'), 'rb').read())
sheet = np.array(Image.open(os.path.join(BASE, 'tiles.png'))); sheet_pal = Image.open(os.path.join(BASE, 'tiles.png')).getpalette()
assert not sheet[FIRST_TILE // 16 * 8:].any() or not any(sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8].any() for i in range(FIRST_TILE, 512))
assert (base & 0x3FF).max() < FIRST_META

def ents(m): return list(struct.unpack_from('<12H', pm if m < 512 else sm, (m % 512) * 24))
def attr(m): return struct.unpack_from('<H', sa, (m - 512) * 2)[0] if m >= 512 else 0
EMPTY_TILES = (0, 1, 2)                                    # blank in the Elderflower primary (checked)
def is_empty(v): return (v & 0x3FF) in EMPTY_TILES

n_tiles = FIRST_TILE; tile_ids = {}
def add_tile(t):
    global n_tiles
    k = t.tobytes()
    if k not in tile_ids:
        assert n_tiles < 512
        i = n_tiles; sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = t
        tile_ids[k] = 512 + i; n_tiles += 1
    return tile_ids[k]
n_meta = FIRST_META; meta_ids = {}
def add_meta(e, a=0):
    global n_meta
    k = (tuple(e), a)
    if k not in meta_ids:
        assert n_meta < 1024
        struct.pack_into('<12H', sm, (n_meta - 512) * 24, *e); struct.pack_into('<H', sa, (n_meta - 512) * 2, a)
        meta_ids[k] = n_meta; n_meta += 1
    return meta_ids[k]
def quad(tiles, slot): return [add_tile(t) | slot << 12 for t in tiles]
def over(under, q): return add_meta(pieces.overlay(ents(under), q, is_empty), attr(under))

# the hearth fire's 4 animated tiles come first (fixed id: src/tileset_anims.c DR_HEARTH_FIRE_TILE)
assert n_tiles == pieces.FIRE_TILE
for t in pieces.as_quad(pieces.lit_firebox()[0]):                  # frame 0; not deduplicated
    i = n_tiles; sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = t; n_tiles += 1
FIRE_Q = [(512 + pieces.FIRE_TILE + i) | FIRE_SLOT << 12 for i in range(4)]
HEARTH = {(dx, dy): quad(pieces.hearth(dx, dy), HEARTH_SLOT) for dy in range(3) for dx in range(3)}
PLATE = quad(pieces.plate(), PLATE_SLOT)
BARREL_TOP, BARREL_BOTTOM = quad(pieces.rustic(648), RUSTIC_SLOT), quad(pieces.rustic(656), RUSTIC_SLOT)

def no_shadow(m):
    """The behind-the-bar floor without the wall's shadow: its bottom quad becomes plain floor (metatile 66)."""
    e = ents(m); e[0:4] = ents(66)[0:4]; return add_meta(e, attr(m))

def build():
    g = np.zeros((H0 + 1, W), np.uint16)
    g[0:2] = base[0:2]
    under_wall = [23] + [119] * (W - 1)                    # the floor under the wall, with its shadow
    for x in range(W): g[2, x] = under_wall[x] | (base[2, x] & 0xFC00)
    row = base[2].copy()                                   # the old behind-the-bar row, shadow removed
    for x in range(1, W):
        m = row[x] & 0x3FF
        if m in (113, 114): row[x] = no_shadow(m) | (row[x] & 0xFC00)
        elif m == 119: row[x] = 66 | (row[x] & 0xFC00)
    g[3] = row
    g[4:] = base[3:]
    def put(x, y, m, coll=None):
        g[y, x] = m | ((coll if coll is not None else g[y, x] >> 10) << 10)
    for dy in range(3):                                     # hearth on the back wall, cols 4-6, lit
        for dx in range(3):
            x, y = 4 + dx, dy; under = int(g[y, x] & 0x3FF)
            if (dx, dy) == pieces.CM.FIREBOX:
                e = pieces.compact(ents(under), is_empty)
                e = pieces.overlay(pieces.overlay(e, HEARTH[(dx, dy)], is_empty), FIRE_Q, is_empty)
                put(x, y, add_meta(e, attr(under)), SOLID)
            else: put(x, y, over(under, HEARTH[(dx, dy)]), SOLID if dy == 2 else None)
    for x, y in ((1, 7), (2, 8), (11, 7), (12, 8)):        # plates on the round tables
        put(x, y, over(g[y, x] & 0x3FF, PLATE))
    for x in (0, 1, 12, 13):                                # barrels in the front corners
        put(x, 9, over(g[9, x] & 0x3FF, BARREL_TOP), SOLID); put(x, 10, over(g[10, x] & 0x3FF, BARREL_BOTTOM), SOLID)
    return g

def main():
    g = build()
    g.astype('<u2').tofile(os.path.join(C, 'data/layouts/PellucaTavern/map.bin'))
    lj = os.path.join(C, 'data/layouts/layouts.json'); L = json.load(open(lj))
    for l in L['layouts']:
        if l.get('id') == 'LAYOUT_PELLUCA_TAVERN': l['height'] = int(g.shape[0])
    json.dump(L, open(lj, 'w'), indent=2); open(lj, 'a').write('\n')
    open(os.path.join(TS_DIR, 'metatiles.bin'), 'wb').write(sm)
    open(os.path.join(TS_DIR, 'metatile_attributes.bin'), 'wb').write(sa)
    im = Image.fromarray(sheet, 'P'); im.putpalette(sheet_pal); im.save(os.path.join(TS_DIR, 'tiles.png'))
    pals = {HEARTH_SLOT: pieces.HEARTH_PAL, PLATE_SLOT: pieces.PLATE_PAL, RUSTIC_SLOT: pieces.RUSTIC_PAL, FIRE_SLOT: pieces.FIRE_ANIM_PAL}
    pieces.write_fire_frames(os.path.join(TS_DIR, 'anim', 'fire'))
    for i in range(16):
        src = os.path.join(BASE, 'palettes', f'{i:02d}.pal'); dst = os.path.join(TS_DIR, 'palettes', f'{i:02d}.pal')
        if i in pals:
            with open(dst, 'w', newline='') as f:
                f.write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join(f'{(r >> 3) << 3} {(gg >> 3) << 3} {(b >> 3) << 3}\r\n' for r, gg, b in pals[i]))
        else: shutil.copy(src, dst)
    m = json.load(open(os.path.join(BASE, 'map.json')))      # NPCs and exit move down with the room
    for k in ('object_events', 'warp_events', 'bg_events', 'coord_events'):
        for e in m.get(k, []):
            if e['y'] >= 2: e['y'] += 1
    with open(os.path.join(C, 'data/maps/PellucaCityPokemonCenter/map.json'), 'w') as f: json.dump(m, f, indent=2); f.write('\n')
    print('tavern', g.shape, 'tiles', n_tiles, 'metatiles', n_meta)

if __name__ == '__main__':
    main()
