"""Build the Pelluca Academy main hall (user design 2026-11-19; mock: compose_mock.py, approved).

The image-based build: compose_mock.compose_layers() gives the hall exactly as approved, split into what is
drawn under the player (the cabin's bottom and middle layers plus every new piece) and over the player (the
cabin's top layer: railing tops, lamp shades, the sofa's back, the hearth glow). Both are cut into 8x8 tiles;
every metatile is [under tiles | empty | over tiles].
  * Colours: GBA 5-bit; colours within one GBA step per channel (8 in 8-bit) are merged into the more common
    one (invisible; it keeps the palette count down), then the tiles' colour sets are packed into 16-colour
    palettes (index 0 transparent). The hall needs about eleven, so it gets its own tileset pair:
      - primary `academy_interior`: all the tiles, palettes 0-5;
      - secondary `academy_hall`: palettes 6-12 and the metatiles.
    (Future Academy rooms can share the primary: its first palettes are the most used ones, the walls and floors.)
  * Collision and behaviours are set by hand below (the cabin's own collision assumed object events).
  * Doors: in this build every room is closed (signs): the rooms are designed next.
Sources: MonoMyth's Ironbark Cabin (reskinned), its Speedwell saloon staircase, Pokemon Crown pieces (credit: Blah
and the Crown team; used with permission): banner, pendulum clock, reception counter, notice board, crates, ladder.
Usage: python3 tools/art/academy/build_hall.py
"""
import os, sys, json, struct, random, collections
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'codebase'))
sys.path.insert(0, HERE)
import compose_mock as CM

MB_NORMAL, MB_SOUTH_ARROW_WARP, MB_COUNTER = 0x00, 0x65, 0x80
WALL, FLOOR_E3, SOLID_E3 = 1, 3 << 2, 1 | 3 << 2                   # collision | elevation << 2
X0, Y0 = CM.X0, CM.Y0
W, H = CM.X1 - CM.X0, CM.Y1 - CM.Y0                                # 17 x 23
def m(x, y): return (x - X0, y - Y0)                              # cabin coordinates -> map coordinates

# ---------------- the picture ----------------
UNDER, OVER, OM = CM.compose_layers('A ivory plaster')
UNDER, OVER = (UNDER >> 3) << 3, (OVER >> 3) << 3
pix = collections.Counter(map(tuple, UNDER.reshape(-1, 3).tolist())) + collections.Counter(map(tuple, OVER[OM].tolist()))
REP = {}
for c, _ in pix.most_common():                                     # merge colours one GBA step apart
    if c in REP: continue
    REP[c] = c
    for d in pix:
        if d not in REP and max(abs(a - b) for a, b in zip(c, d)) <= 8: REP[d] = c
def remap(img):
    out = img.copy(); flat = out.reshape(-1, 3)
    for k, v in REP.items():
        if k != v: flat[(flat == k).all(1)] = v
    return out
UNDER, OVER = remap(UNDER), remap(OVER)

# ---------------- palettes: pack the 8x8 tiles' colour sets ----------------
def blocks():
    for ty in range(H * 2):
        for tx in range(W * 2):
            u = UNDER[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8]; o = OVER[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8]
            mk = OM[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8]
            yield tx, ty, u, o, mk
SETS = set()
for tx, ty, u, o, mk in blocks():
    SETS.add(frozenset(map(tuple, u.reshape(-1, 3).tolist())))
    if mk.any(): SETS.add(frozenset(map(tuple, o[mk].tolist())))
red = []
for s in sorted(SETS, key=len, reverse=True):
    if not any(s <= r for r in red): red.append(s)
def greedy(order):
    pals = []
    for s in order:
        best = None
        for i, p in enumerate(pals):
            n = len(p | s)
            if n <= 15 and (best is None or n - len(p) < best[0]): best = (n - len(p), i)
        if best is None: pals.append(set(s))
        else: pals[best[1]] |= s
    return pals
rng = random.Random(7); PALS = None
for it in range(1500):                                             # randomised greedy, deterministic seed
    o = list(red); rng.shuffle(o); o.sort(key=lambda s: -len(s) + rng.random() * 4)
    p = greedy(o)
    if PALS is None or len(p) < len(PALS): PALS = p
assert len(PALS) <= 13, f'{len(PALS)} palettes'
def pal_of(s): return [i for i, p in enumerate(PALS) if s <= p]
use = collections.Counter()
for tx, ty, u, o, mk in blocks():
    use[pal_of(frozenset(map(tuple, u.reshape(-1, 3).tolist())))[0]] += 1
ORDER = sorted(range(len(PALS)), key=lambda i: -use[i])           # slots 0-5 (primary) = the most used
PAL_COLS = [[(0, 0, 0)] + sorted(PALS[i], key=lambda c: sum(c)) for i in ORDER]
SLOT_SETS = [set(PALS[i]) for i in ORDER]

# ---------------- tiles ----------------
TILES = [np.zeros((8, 8), np.uint8)]; _tid = {TILES[0].tobytes(): (0, 0)}   # tile 0: blank (empty layers)
def add_tile(idx):
    """-> (tile id, flip bits) with h/v flips deduplicated."""
    for f, t in ((0, idx), (1, idx[:, ::-1]), (2, idx[::-1, :]), (3, idx[::-1, ::-1])):
        k = np.ascontiguousarray(t).tobytes()
        if k in _tid: tid, f0 = _tid[k]; return tid, f ^ f0
    tid = len(TILES); TILES.append(idx.copy()); _tid[idx.tobytes()] = (tid, 0); return tid, 0
def entry(rgb, mask=None):
    cols = frozenset(map(tuple, (rgb[mask] if mask is not None else rgb.reshape(-1, 3)).tolist()))
    slot = [k for k, s in enumerate(SLOT_SETS) if cols <= s][0]; P = PAL_COLS[slot]
    lut = {c: i for i, c in enumerate(P) if i}; idx = np.zeros((8, 8), np.uint8)
    for yy in range(8):
        for xx in range(8):
            if mask is None or mask[yy, xx]: idx[yy, xx] = lut[tuple(rgb[yy, xx].tolist())]
    tid, f = add_tile(idx); return tid | f << 10 | slot << 12
CELL_E = {}
for tx, ty, u, o, mk in blocks():
    cx, cy, q = tx // 2, ty // 2, (ty % 2) * 2 + tx % 2
    e = CELL_E.setdefault((cx, cy), [0] * 12)
    e[q] = entry(u)
    if mk.any(): e[8 + q] = entry(o, mk)
assert len(TILES) <= 512, f'{len(TILES)} tiles: spill into the secondary'

# ---------------- collision and behaviour (cabin coordinates) ----------------
WALK = set()
for y in (9, 10, 14, 15): WALK |= {(x, y) for x in range(7, 22)}             # the two galleries
for y in range(19, 26): WALK |= {(x, y) for x in range(7, 22)}               # the ground floor
for fx, fy in CM.FLIGHTS:                                                    # stairs: up the centre column
    WALK |= {(fx + 1, fy + d) for d in range(4)}; WALK -= {(fx, fy), (fx + 2, fy)}   # newel posts at the top
SOLID = set(CM.CRATES) | {(CM.LADDER[0], CM.LADDER[1] + 1), (14, 9), (14, 14)}   # crates, ladder feet, chimney bases
SOLID |= {(x, 19) for x in (8, 9, 10, 13, 14, 15)}                          # lamp + piano, hearth
SOLID |= {(9, 20), (10, 20), (12, 21), (16, 21)}                             # piano bench, armchairs
SOLID |= {(x, y) for x in (9, 10, 11) for y in (22, 23)}                     # the sofa set
SOLID |= {(x, 24) for x in (8, 9, 10, 11)} | {(12, 25), (16, 25)}            # table and stools, lamp stands
dx0, dy0 = CM.DESK
SOLID |= {(dx0, dy0 + d) for d in range(3)} | {(dx0 + 3, dy0 + d) for d in range(3)} | {(dx0 + k, dy0 + 3) for k in range(4)}
COUNTER = {(dx0 + 1, dy0 + 3), (dx0 + 2, dy0 + 3)}                           # talk across to whoever stands inside
EXIT = (14, 25)
WALK -= SOLID

# ---------------- metatiles and the layout ----------------
s_meta, s_attr, _mid = [], [], {}
def add_meta(e, a):
    k = (tuple(e), a)
    if k not in _mid:
        assert len(s_meta) < 512, 'secondary metatile budget'
        _mid[k] = 512 + len(s_meta); s_meta.append(list(e)); s_attr.append(a)
    return _mid[k]
grid = np.zeros((H, W), np.uint16)
for my in range(H):
    for mx in range(W):
        x, y = mx + X0, my + Y0
        a = MB_SOUTH_ARROW_WARP if (x, y) == EXIT else MB_COUNTER if (x, y) in COUNTER else MB_NORMAL
        col = FLOOR_E3 if (x, y) in WALK else SOLID_E3
        grid[my, mx] = add_meta(CELL_E[(mx, my)], a) | col << 10
VOID_ID = int(grid[0, 0] & 0x3FF)                                            # the black void (border)

# ---------------- events (map coordinates) ----------------
DOORS = {  # bottom cell of each door (cabin coordinates) -> script
    (20, 18): 'DR_Academy_OfficeDoor',     # G1 Cadmus's office
    (8, 13): 'DR_Academy_LibraryDoor',     # M1 library
    (17, 13): 'DR_Academy_ClassroomDoor',  # M3 classroom (top of the first stairs)
    (20, 8): 'DR_Academy_LoungeDoor',      # T4 the haunted teachers' lounge (rusted key after the second badge)
    (20, 13): 'DR_Academy_RenovationDoor', (8, 8): 'DR_Academy_RenovationDoor', (17, 8): 'DR_Academy_RenovationDoor',
}
def sign(x, y, script):
    mx, my = m(x, y)
    return {'type': 'sign', 'x': mx, 'y': my, 'elevation': 0, 'player_facing_dir': 'BG_EVENT_PLAYER_FACING_NORTH', 'script': script}
BG = [sign(x, y, s) for (x, y), s in DOORS.items()]
BG += [sign(CM.BOARD[0] + k, CM.BOARD[1] + 1, 'DR_Academy_NoticeBoard') for k in (0, 1)]
EX, EY = m(*EXIT)
MAP = {
    'id': 'MAP_PELLUCA_ACADEMY_HALL', 'name': 'PellucaAcademyHall', 'layout': 'LAYOUT_PELLUCA_ACADEMY_HALL',
    'music': 'MUS_LILYCOVE_MUSEUM', 'region_map_section': 'MAPSEC_PELLUCA_VALLEY', 'requires_flash': False,
    'weather': 'WEATHER_NONE', 'map_type': 'MAP_TYPE_INDOOR', 'allow_cycling': False, 'allow_escaping': False,
    'allow_running': True, 'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
    'object_events': [],
    'warp_events': [{'x': EX, 'y': EY, 'elevation': 0, 'dest_map': 'MAP_PELLUCA_CITY', 'dest_warp_id': '4'}],
    'coord_events': [], 'bg_events': BG}
CITY_DOOR = (27, 12)                                                         # Pelluca: the Academy's front door

# ---------------- write ----------------
def write_tileset(d, tiles, pals, meta, attrs, show):
    os.makedirs(os.path.join(d, 'palettes'), exist_ok=True)
    n = max(16, (len(tiles) + 15) // 16 * 16); sheet = np.zeros((n // 16 * 8, 128), np.uint8)
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

def register():
    """The tilesets in the C tables, the map in its group and the script include (each once)."""
    def add(path, after, text):
        f = os.path.join(C, path); t = open(f).read()
        if text.strip().splitlines()[0] in t: return
        i = t.index(after) + len(after); open(f, 'w').write(t[:i] + text + t[i:])
    for kind, dirn, name in (('primary', 'academy_interior', 'AcademyInterior'), ('secondary', 'academy_hall', 'AcademyHall')):
        pal = ''.join(f'    INCBIN_U16("data/tilesets/{kind}/{dirn}/palettes/{i:02d}.gbapal"),\n' for i in range(16))
        add('src/data/tilesets/graphics.h', 'gTilesetTiles_TemplarHall[] = INCBIN_U32("data/tilesets/secondary/templar_hall/tiles.4bpp.lz");\n',
            f'\nconst u16 gTilesetPalettes_{name}[][16] =\n{{\n{pal}}};\n\n'
            f'const u32 gTilesetTiles_{name}[] = INCBIN_U32("data/tilesets/{kind}/{dirn}/tiles.4bpp.lz");\n')
        add('src/data/tilesets/metatiles.h', 'gMetatileAttributes_TemplarHall[] = INCBIN_U16("data/tilesets/secondary/templar_hall/metatile_attributes.bin");\n',
            f'const u16 gMetatiles_{name}[] = INCBIN_U16("data/tilesets/{kind}/{dirn}/metatiles.bin");\n'
            f'const u16 gMetatileAttributes_{name}[] = INCBIN_U16("data/tilesets/{kind}/{dirn}/metatile_attributes.bin");\n')
        hdr = open(os.path.join(C, 'src/data/tilesets/headers.h')).read(); i = hdr.index('const struct Tileset gTileset_TemplarHall')
        add('src/data/tilesets/headers.h', hdr[i:hdr.index('};', i) + 3],
            f'\nconst struct Tileset gTileset_{name} =\n{{\n    .isCompressed = TRUE,\n    .isSecondary = {"TRUE" if kind == "secondary" else "FALSE"},\n'
            f'    .tiles = gTilesetTiles_{name},\n    .palettes = gTilesetPalettes_{name},\n    .metatiles = gMetatiles_{name},\n'
            f'    .metatileAttributes = gMetatileAttributes_{name},\n    .callback = NULL,\n}};\n')
    add('data/event_scripts.s', '\t.include "data/maps/PellucaTemplarHall/scripts.inc"\n', '\t.include "data/maps/PellucaAcademyHall/scripts.inc"\n')
    gj = os.path.join(C, 'data/maps/map_groups.json'); G = json.load(open(gj))
    if 'PellucaAcademyHall' not in G['gMapGroup_Phase3']:
        G['gMapGroup_Phase3'].append('PellucaAcademyHall'); json.dump(G, open(gj, 'w'), indent=2); open(gj, 'a').write('\n')

def main():
    blank = [(0, 0, 0)] * 16
    pals = [(PAL_COLS[i] + [(0, 0, 0)] * 16)[:16] if i < len(PAL_COLS) else blank for i in range(16)]
    write_tileset(os.path.join(C, 'data/tilesets/primary/academy_interior'), TILES,
                  [p if i < 6 else blank for i, p in enumerate(pals)], [[0] * 12], [MB_NORMAL], 0)
    write_tileset(os.path.join(C, 'data/tilesets/secondary/academy_hall'), [np.zeros((8, 8), np.uint8)],
                  [p if 6 <= i < 13 else blank for i, p in enumerate(pals)], s_meta, s_attr, 6)
    d = os.path.join(C, 'data/layouts/PellucaAcademyHall'); os.makedirs(d, exist_ok=True)
    grid.astype('<u2').tofile(os.path.join(d, 'map.bin'))
    open(os.path.join(d, 'border.bin'), 'wb').write(struct.pack('<4H', *[VOID_ID] * 4))
    lj = os.path.join(C, 'data/layouts/layouts.json'); L = json.load(open(lj)); lays = L['layouts']
    entry_ = {'id': 'LAYOUT_PELLUCA_ACADEMY_HALL', 'name': 'PellucaAcademyHall_Layout', 'width': W, 'height': H,
              'primary_tileset': 'gTileset_AcademyInterior', 'secondary_tileset': 'gTileset_AcademyHall',
              'border_filepath': 'data/layouts/PellucaAcademyHall/border.bin',
              'blockdata_filepath': 'data/layouts/PellucaAcademyHall/map.bin'}
    old = [i for i, l in enumerate(lays) if l.get('id') == entry_['id']]
    if old: lays[old[0]] = entry_
    else: lays.insert([i for i, l in enumerate(lays) if l.get('id') == 'LAYOUT_PELLUCA_TEMPLAR_HALL'][0] + 1, entry_)
    json.dump(L, open(lj, 'w'), indent=2); open(lj, 'a').write('\n')
    md = os.path.join(C, 'data/maps/PellucaAcademyHall'); os.makedirs(md, exist_ok=True)
    json.dump(MAP, open(os.path.join(md, 'map.json'), 'w'), indent=2); open(os.path.join(md, 'map.json'), 'a').write('\n')
    # Pelluca: the Academy's front door becomes a warp into the hall (its "locked" sign goes)
    cj = os.path.join(C, 'data/maps/PellucaCity/map.json'); city = json.load(open(cj))
    w = {'x': CITY_DOOR[0], 'y': CITY_DOOR[1], 'elevation': 0, 'dest_map': 'MAP_PELLUCA_ACADEMY_HALL', 'dest_warp_id': '0'}
    ws = city['warp_events']; hit = [i for i, v in enumerate(ws) if (v['x'], v['y']) == CITY_DOOR]
    if hit: ws[hit[0]] = w
    else: ws.append(w)
    assert ws.index(w) == 4, ws.index(w)
    city['bg_events'] = [b for b in city['bg_events'] if b.get('script') != 'DR_PellucaCity_DoorAcademy']
    json.dump(city, open(cj, 'w'), indent=2); open(cj, 'a').write('\n')
    cl = json.load(open(lj)); cl = [l for l in cl['layouts'] if l.get('id') == city['layout']][0]
    cb = os.path.join(C, cl['blockdata_filepath']); data = bytearray(open(cb, 'rb').read())
    o = 2 * (CITY_DOOR[1] * cl['width'] + CITY_DOOR[0]); v = struct.unpack_from('<H', data, o)[0]
    assert v & 0x3FF == 0x05D, hex(v)                                        # the door metatile (as the dormitory's)
    struct.pack_into('<H', data, o, 0x05D | FLOOR_E3 << 10); open(cb, 'wb').write(data)
    register()
    print('tiles', len(TILES), 'metatiles', len(s_meta), 'palettes', len(PALS), 'merged colours', sum(k != v for k, v in REP.items()))

if __name__ == '__main__':
    main()
