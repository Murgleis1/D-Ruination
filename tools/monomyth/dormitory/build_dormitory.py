"""Build the Pelluca dormitory: two tilesets and three layouts, from the user-approved mockup
(compose_mock.py, assets/monomyth_reference/interiors/dormitory_mock_approved.png, 2026-11-19).

    python3 -I tools/monomyth/dormitory/build_dormitory.py          # needs MONOMYTH_ROM (see ../README.md)

Tilesets
  primary   speedwell_interior  MonoMyth's building primary (0x8730CCC) unchanged, palettes 3-4 recoloured
                                (compose_mock.RECOLOUR: oak floor, warm plaster, warm wood).
  secondary pelluca_dormitory   MonoMyth's tavern secondary (0x8730E4C, the one the Speedwell saloon pairs
                                with: its first 229 tiles and metatiles 512-561 are kept at the same ids,
                                because the primary's metatiles point into them), plus new pieces:
                                  - South Edelweiss apartment wall (upper/lower), door and doormat
                                    (palettes in slots 9 and 7, warmed: compose_mock.WALL_/DOOR_RECOLOUR;
                                    slot 6 stays the tavern secondary's own, the saloon beds use it),
                                  - the Wood Avens pedestal as the stage lectern (slot 8),
                                  - Pokemon Odyssey's brick hearth (slot 10) and food plates on the
                                    dining tables (slot 11), from its fireplace hall (layout 0x8319414),
                                  - saloon furniture re-based onto the new wall / plain oak floor: only the
                                    background layer entry changes, the object layers are untouched,
                                  - warp copies: stair tops (MB_NON_ANIMATED_DOOR), exit mats
                                    (MB_SOUTH_ARROW_WARP). Doors are MB_ANIMATED_DOOR.
Layouts  LAYOUT_PELLUCA_DORMITORY_1F (19x15), _2F (16x7), LAYOUT_PELLUCA_DORMITORY_OSRID_ROOM (11x10).
Collision: each saloon metatile keeps the collision/elevation it has in the saloon map; walls 1, floor 3,
doors and the lectern solid at elevation 3 (the player walks into a door to use it, as in a Pokemon Center).
"""
import os, sys, struct, json
HERE = os.path.dirname(os.path.abspath(__file__)); MM = os.path.dirname(HERE)
sys.path.insert(0, MM); sys.path.insert(0, HERE)
import numpy as np
from PIL import Image
from render import ROM, off, tiles_of, map_cells
import compose_mock as CM

REPO = os.path.abspath(os.path.join(MM, '..', '..')); C = os.path.join(REPO, 'codebase')
MB_NON_ANIMATED_DOOR, MB_SOUTH_ARROW_WARP, MB_ANIMATED_DOOR = 0x60, 0x65, 0x69
WALL, FLOOR_E3, SOLID_E3, WARP_E0 = 1, 3 << 2, 1 | 3 << 2, 0          # collision | elevation << 2

def layout(a): return [h for h in CM.H if h['addr'] + 0x08000000 == a][0]['layout']
SAL_L, APT_L, WA_L = layout(0x886A39C), layout(0x886A188), layout(0x886ACB0)
SP, SS = SAL_L['primary'], SAL_L['secondary']
assert SP['addr'] == 0x8730CCC and SS['addr'] == 0x8730E4C
AP, WP = APT_L['primary'], WA_L['primary']

def ents(ts, i): return list(struct.unpack_from('<12H', ROM, off(ts['mt']) + i * 24))
def attr(ts, i): return struct.unpack_from('<H', ROM, off(ts['attr']) + i * 2)[0]
def sal_ents(mid): return ents(SP, mid) if mid < 512 else ents(SS, mid - 512)
def sal_attr(mid): return attr(SP, mid) if mid < 512 else attr(SS, mid - 512)
def gba(c): return tuple((int(v) >> 3) << 3 for v in c)

# ---------------- tiles ----------------
P_TILES, S_TILES = tiles_of(SP), tiles_of(SS)
assert not P_TILES[0].any(), 'primary tile 0 must be blank'
FIRST_FREE_TILE = 229
assert not S_TILES[FIRST_FREE_TILE:].any(), 'secondary tiles past 228 must be unused'
s_tiles = [t.copy() for t in S_TILES[:FIRST_FREE_TILE]]
_tile_ids = {}
def add_tile(t):
    k = t.tobytes()
    if k not in _tile_ids:
        assert len(s_tiles) < 512, 'secondary tile budget'
        _tile_ids[k] = len(s_tiles); s_tiles.append(t.copy())
    return 512 + _tile_ids[k]
FOREIGN_TILES = {id(AP): tiles_of(AP), id(WP): tiles_of(WP)}
def import_fr_quad(ts, quad, slot_map):
    """Pokemon Odyssey (FireRed) metatile entries -> ours: FireRed tile ids (primary < 640) resolved by the
    FireRed tileset, tile copied into our secondary, palette slot remapped, flips kept."""
    out = []
    for v in quad:
        t, flips, slot = v & 0x3FF, v & 0xC00, v >> 12
        out.append(add_tile(ts.tile(t)) | flips | (slot_map[slot] << 12))
    return out
def import_quad(ts, quad, slot_map):
    """Foreign metatile entries -> ours: tile copied into the secondary, palette slot remapped, flips kept."""
    out = []
    for v in quad:
        tid, flips, slot = v & 0x3FF, v & 0xC00, v >> 12
        assert tid < 512, 'foreign pieces come from their primary tilesets'
        out.append(add_tile(FOREIGN_TILES[id(ts)][tid]) | flips | (slot_map[slot] << 12))
    return out

WALL_SLOT, DOOR_SLOT, PED_SLOT = 9, 7, 8        # free: the saloon pieces use 0, 3-5 and the tavern's 6 (the bed)
W_UP = import_quad(AP, ents(AP, 184)[8:12], {1: WALL_SLOT})
W_LO = import_quad(AP, ents(AP, 177)[4:8], {1: WALL_SLOT})
DOOR = import_quad(AP, ents(AP, 289)[0:4], {3: DOOR_SLOT})
MAT = import_quad(AP, ents(AP, 189)[4:8], {1: WALL_SLOT})
PED = import_quad(WP, ents(WP, 122)[4:8], {2: PED_SLOT})
# Pokemon Odyssey brick hearth (its palette 7 -> our 10) and food plates (its palette 8 -> our 11)
HEARTH_SLOT, PLATE_SLOT = 10, 11
FIRE = CM.FIRE
def fr_ents(mid): return list(FIRE.ents(mid))
HEARTH_META = {m: import_fr_quad(FIRE, fr_ents(m)[0:4], {7: HEARTH_SLOT}) + import_fr_quad(FIRE, fr_ents(m)[4:8], {7: HEARTH_SLOT})
               for row in CM.HEARTH for m in row}
PLATE = import_fr_quad(FIRE, fr_ents(CM.PLATE)[4:8], {8: PLATE_SLOT})
FLOOR = sal_ents(155)[4:8]
EMPTY = [0, 0, 0, 0]

# ---------------- secondary metatiles ----------------
REAL_SEC_METATILES = 50                                   # 512-561: what MonoMyth's maps use
s_meta = [sal_ents(512 + i) for i in range(REAL_SEC_METATILES)]
s_attr = [sal_attr(512 + i) for i in range(REAL_SEC_METATILES)]
_meta_ids = {}
def add_meta(e, a=0):
    k = (tuple(e), a)
    if k not in _meta_ids:
        assert len(s_meta) < 512, 'secondary metatile budget'
        _meta_ids[k] = 512 + len(s_meta); s_meta.append(list(e)); s_attr.append(a)
    return _meta_ids[k]

# the door is always the first new metatile, so its id (= METATILE_PellucaDormitory_Door, which the door
# animation table is keyed on) does not move when pieces are added
DOOR_ID = add_meta(DOOR + EMPTY + EMPTY, MB_ANIMATED_DOOR)
BG = {(514, 514, 530, 530): FLOOR, (514, 514, 531, 531): FLOOR,          # wall-shadow floor strips -> oak
      (560, 513, 576, 529): W_LO,                                          # panelled wainscot -> lower wall
      (544, 544, 544, 544): W_UP}                                          # plaster band -> upper wall
def rebase(mid):
    """A saloon metatile with its background layer swapped (P/Q/R/T in the mockup)."""
    e = sal_ents(mid)
    for k in range(3):
        q = e[k * 4:k * 4 + 4]
        key = tuple(v & 0x3FF for v in q)
        if key in BG and all(v >> 12 == 4 for v in q): e[k * 4:k * 4 + 4] = BG[key]
    return add_meta(e, sal_attr(mid))

# collision/elevation each saloon metatile has in the saloon map (first occurrence)
COLL = {}
for v in map_cells(SAL_L): COLL.setdefault(v & 0x3FF, v >> 10)

def cell(c):
    if c is None: return 0, WALL
    src, mid = c
    if src == 's': return mid, COLL.get(mid, WALL)
    if src == 'a' and mid == 184: return add_meta(EMPTY + W_UP + EMPTY), WALL
    if src == 'a' and mid == 177: return add_meta(EMPTY + W_LO + EMPTY), WALL
    if src == 'a' and mid == 289: return add_meta(DOOR + EMPTY + EMPTY, MB_ANIMATED_DOOR), SOLID_E3
    if src == 'm': return add_meta(EMPTY + FLOOR + MAT), FLOOR_E3
    if src == 'L': return add_meta(EMPTY + sal_ents(165)[4:8] + PED), SOLID_E3
    if src in 'PQRT': return rebase(mid), COLL.get(mid, WALL)
    if src == 'F': return add_meta(EMPTY + HEARTH_META[mid]), WALL               # in the wall rows
    if src == 'Fo':                                                             # a plate on a table
        oid, (usrc, umid) = mid; assert usrc == 's'
        e = sal_ents(umid); free = [k for k in range(3) if not any(v & 0x3FF for v in e[k * 4:k * 4 + 4])]
        assert free and free[-1] > max(k for k in range(3) if any(v & 0x3FF for v in e[k * 4:k * 4 + 4])), 'no layer above the table'
        e[free[-1] * 4:free[-1] * 4 + 4] = PLATE
        return add_meta(e, sal_attr(umid)), COLL.get(umid, WALL)
    raise ValueError(c)

def warp_copy(mid, behaviour):
    return add_meta(sal_ents(mid), behaviour)

def build(rows, warps):
    rows = CM.plain(rows)
    h, w = len(rows), max(len(r) for r in rows)
    out = np.zeros((h, w), np.uint16)
    for y, r in enumerate(rows):
        for x in range(w):
            m, col = cell(r[x] if x < len(r) else None)
            out[y, x] = m | (col << 10)
    for (x, y), (mid, beh, col) in warps.items():
        out[y, x] = warp_copy(mid, beh) | (col << 10)
    return out

ROOMS = {
    'PellucaDormitory1F': build(CM.floor1(), {(1, 0): (193, MB_NON_ANIMATED_DOOR, WARP_E0),
                                              (9, 14): (214, MB_SOUTH_ARROW_WARP, FLOOR_E3)}),
    # the upstairs flight descends southward: an arrow warp (press Down on it). A stair-top
    # MB_NON_ANIMATED_DOOR would walk an arriving player one tile south, straight back down the stairs.
    'PellucaDormitory2F': build(CM.floor2(), {(1, 5): (193, MB_SOUTH_ARROW_WARP, FLOOR_E3)}),
    'PellucaDormitoryOsridRoom': build(CM.osrid_room(), {(5, 9): (214, MB_SOUTH_ARROW_WARP, FLOOR_E3)}),
}
# the stair below the 2F warp leads off the map: keep the player on the landing
ROOMS['PellucaDormitory2F'][6, 1] = (ROOMS['PellucaDormitory2F'][6, 1] & 0x3FF) | (WALL << 10)

# ---------------- palettes ----------------
prim_pals = [[gba(c) for c in CM.SAL.pal[i]] if i < 6 else [(0, 0, 0)] * 16 for i in range(16)]
sec_pals = [[(0, 0, 0)] * 16 for _ in range(16)]
sec_pals[6] = [gba(c) for c in CM.SAL.pal[6]]               # the tavern secondary's own slot 6 (beds)
sec_pals[WALL_SLOT] = [gba(c) for c in CM.APT.pal[1]]        # apartment wall + doormat, warmed
sec_pals[DOOR_SLOT] = [gba(c) for c in CM.APT.pal[3]]        # apartment door, warm wood
sec_pals[PED_SLOT] = [gba(c) for c in CM.WA.pal[2]]          # Wood Avens pedestal
sec_pals[HEARTH_SLOT] = [gba(c) for c in FIRE.pal[7]]        # Odyssey brick hearth
sec_pals[PLATE_SLOT] = [gba(c) for c in FIRE.pal[8]]         # Odyssey food plates

# ---------------- write ----------------
def write_tileset(d, tiles, pals, meta, attrs, show):
    os.makedirs(os.path.join(d, 'palettes'), exist_ok=True)
    n = max(16, (len(tiles) + 15) // 16 * 16)
    sheet = np.zeros((n // 16 * 8, 128), np.uint8)
    for i, t in enumerate(tiles): sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = t
    im = Image.fromarray(sheet, 'P'); im.putpalette([v for c in pals[show] for v in c] + [0] * (768 - 48))
    im.save(os.path.join(d, 'tiles.png'))
    for i, cols in enumerate(pals):
        with open(os.path.join(d, 'palettes', f'{i:02d}.pal'), 'w', newline='') as f:
            f.write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join(f'{r} {g} {b}\r\n' for r, g, b in cols))
    with open(os.path.join(d, 'metatiles.bin'), 'wb') as f:
        for e in meta: f.write(struct.pack('<12H', *e))
    with open(os.path.join(d, 'metatile_attributes.bin'), 'wb') as f:
        for a in attrs: f.write(struct.pack('<H', a))

# ---------------- door animation ----------------
# MonoMyth animates this door as a 1x1 door (its table entry for metatile 289: tiles 0x8873DA8, three
# 16x16 frames, palette slot 3). Our engine draws 1x2 doors (the door and the metatile above it), so each
# frame is the upper-wall art over MonoMyth's frame; palettes: top = wall slot, bottom = door slot.
DOOR_METATILE = 0x232                                    # = METATILE_PellucaDormitory_Door (metatile_labels.h)
MM_DOOR_FRAMES = 0x873DA8
def frame_tile(i):
    a = np.frombuffer(ROM[MM_DOOR_FRAMES + 32 * i: MM_DOOR_FRAMES + 32 * i + 32], np.uint8)
    t = np.zeros((8, 8), np.uint8); t[:, 0::2] = (a & 15).reshape(8, 4); t[:, 1::2] = (a >> 4).reshape(8, 4); return t
def quad_pixels(quad):
    img = np.zeros((16, 16), np.uint8)
    for q, v in enumerate(quad):
        t = s_tiles[(v & 0x3FF) - 512]
        if v & 0x400: t = t[:, ::-1]
        if v & 0x800: t = t[::-1, :]
        img[(q // 2) * 8:(q // 2) * 8 + 8, (q % 2) * 8:(q % 2) * 8 + 8] = t
    return img
def write_door_anim():
    img = np.zeros((96, 16), np.uint8)
    for f in range(3):
        img[f * 32:f * 32 + 16] = quad_pixels(W_UP)
        for q in range(4):
            y, x = f * 32 + 16 + (q // 2) * 8, (q % 2) * 8; img[y:y + 8, x:x + 8] = frame_tile(f * 4 + q)
    im = Image.fromarray(img, 'P'); im.putpalette([v for c in sec_pals[DOOR_SLOT] for v in c] + [0] * (768 - 48))
    im.save(os.path.join(C, 'graphics/door_anims/pelluca_dormitory.png'))

def main():
    write_tileset(os.path.join(C, 'data/tilesets/primary/speedwell_interior'), list(P_TILES), prim_pals,
                  [ents(SP, i) for i in range(512)], [attr(SP, i) for i in range(512)], 4)
    write_tileset(os.path.join(C, 'data/tilesets/secondary/pelluca_dormitory'), s_tiles, sec_pals,
                  s_meta, s_attr, 6)
    lj = os.path.join(C, 'data/layouts/layouts.json'); L = json.load(open(lj))
    ids = {'PellucaDormitory1F': 'LAYOUT_PELLUCA_DORMITORY_1F', 'PellucaDormitory2F': 'LAYOUT_PELLUCA_DORMITORY_2F',
           'PellucaDormitoryOsridRoom': 'LAYOUT_PELLUCA_DORMITORY_OSRID_ROOM'}
    for name, grid in ROOMS.items():
        d = os.path.join(C, 'data/layouts', name); os.makedirs(d, exist_ok=True)
        grid.astype('<u2').tofile(os.path.join(d, 'map.bin'))
        open(os.path.join(d, 'border.bin'), 'wb').write(bytes(8))
        entry = {'id': ids[name], 'name': name + '_Layout', 'width': int(grid.shape[1]), 'height': int(grid.shape[0]),
                 'primary_tileset': 'gTileset_SpeedwellInterior', 'secondary_tileset': 'gTileset_PellucaDormitory',
                 'border_filepath': f'data/layouts/{name}/border.bin', 'blockdata_filepath': f'data/layouts/{name}/map.bin'}
        lays = L['layouts']; old = [i for i, l in enumerate(lays) if l.get('id') == ids[name]]
        if old: lays[old[0]] = entry
        else:
            at = [i for i, l in enumerate(lays) if l.get('id') == 'LAYOUT_PELLUCA_TAVERN'][0] + 1 + len(
                [1 for l in lays if l.get('id', '').startswith('LAYOUT_PELLUCA_DORMITORY')])
            lays.insert(at, entry)
    json.dump(L, open(lj, 'w'), indent=2); open(lj, 'a').write('\n')
    door_ids = [512 + i for i, a in enumerate(s_attr) if a & 0xFF == MB_ANIMATED_DOOR]
    assert door_ids == [DOOR_METATILE], f'door metatile moved to {door_ids}: update DOOR_METATILE and metatile_labels.h'
    write_door_anim()
    print('secondary tiles', len(s_tiles), 'secondary metatiles', len(s_meta), {k: v.shape for k, v in ROOMS.items()})

if __name__ == '__main__':
    main()
