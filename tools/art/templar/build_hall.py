"""Build the Templar Monastery main hall (user design 2026-11-19; mock: compose_mock.py).

The hall the holding cell's south door opens into: a church-like foyer with pews, entered from Pelluca.
  * Primary tileset `old_hq_interior`: MonoMyth's "Old Headquarters" primary (0x8730F84), unchanged except
    that its carpet's indoor-encounter behaviour becomes plain floor (that room has wild battles; ours not).
  * Secondary tileset `templar_hall`: only the Old HQ secondary tiles the hall uses (its secondary is full)
    in its palette slots 8 (wall) and 12 (carpet), plus our pieces:
      - Pokemon Rejuvenation (credit: the Rejuvenation team): ArceusRuins sheet, halved exactly (the art is
        pixel-doubled): the white Arceus statue, two matching tall statue-pillars (user), the altar rug, the
        gold medallion, the four crystals (user), the cell doorway; Church sheet: the great stained-glass
        window (the figure's hair re-dyed gold blonde with silver: user) and the two gothic lancets,
        resampled from the JPEG the user supplied (the original PNG was unavailable: user said go ahead).
      - pews drawn in the saloon's warm wood (user picked pews over chairs).
  * Each 8x8 tile takes one palette; where two pieces of different palettes share a tile they are split
    across the middle and top layers (later piece on top).
Usage: python3 tools/art/templar/build_hall.py
"""
import os, sys, json, struct
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'codebase'))
sys.path.insert(0, HERE)
import compose_mock as CM                                    # the approved pieces (one source of truth)
from romlib import u32, off, layout
from render import ROM, tiles_of, pals_of

MB_NORMAL, MB_INDOOR_ENCOUNTER, MB_NON_ANIMATED_DOOR, MB_SOUTH_ARROW_WARP = 0x00, 0x02, 0x60, 0x65
WALL, FLOOR_E3, SOLID_E3, WARP_E0 = 1, 3 << 2, 1 | 3 << 2, 0          # collision | elevation << 2

HQ_L = layout(u32(off(0x0886DEC8))); P, S = HQ_L['primary'], HQ_L['secondary']
assert P['addr'] == 0x8730F84
PT, ST = tiles_of(P), tiles_of(S); PP, SP = pals_of(P), pals_of(S)
def hq_ents(m): return list(struct.unpack_from('<12H', ROM, off(P['mt']) + 24 * m))
def hq_attr(m): return struct.unpack_from('<H', ROM, off(P['attr']) + 2 * m)[0]
def hq_tile(t): return PT[t] if t < 512 else ST[t - 512]
def gba(c): return tuple((int(v) >> 3) << 3 for v in c)

# ---------------- secondary tiles ----------------
s_tiles = [np.zeros((8, 8), np.uint8)]; _tid = {s_tiles[0].tobytes(): 0}
def add_tile(t):
    k = t.astype(np.uint8).tobytes()
    if k not in _tid:
        assert len(s_tiles) < 512, 'secondary tile budget'
        _tid[k] = len(s_tiles); s_tiles.append(t.astype(np.uint8).copy())
    return 512 + _tid[k]
def hq_entries(m):
    """An Old HQ metatile's entries in our tilesets: primary tiles keep their ids, its secondary tiles are
    copied into ours; blank filler entries become 0."""
    out = []
    for v in hq_ents(m):
        t = v & 0x3FF
        if not hq_tile(t).any(): out.append(0); continue
        out.append((add_tile(ST[t - 512]) | (v & 0xFC00)) if t >= 512 else v)
    return out
def empty(v): return not (v & 0x3FF)

# the wall made taller: the face metatile's rows 1-8 repeated (no bottom trim), as in the mock
def mid_wall(m):
    e = hq_ents(m); idx = np.zeros((16, 16), np.uint8); slot = e[0] >> 12
    for q in range(4):
        v = e[q]; t = hq_tile(v & 0x3FF)
        if v & 0x400: t = t[:, ::-1]
        if v & 0x800: t = t[::-1, :]
        assert v >> 12 == slot; idx[(q // 2) * 8:(q // 2) * 8 + 8, (q % 2) * 8:(q % 2) * 8 + 8] = t
    band = idx[1:9]; img = np.vstack([band, band])
    return [add_tile(img[(q // 2) * 8:(q // 2) * 8 + 8, (q % 2) * 8:(q % 2) * 8 + 8]) | slot << 12 for q in range(4)] + [0] * 8

# ---------------- the room (17 x 22, as the mock) ----------------
W, H, WALL_ROWS = CM.W, CM.H, CM.WALL
VOID_M = 0x14                                                  # Old HQ's black void
floor = [[None] * W for _ in range(H)]                         # ('hq', id) or ('mid', id)
for x in range(W):
    l, r = x == 0, x == W - 1
    floor[0][x] = ('hq', 0xCE if l else 0xCF if r else 0xCA)
    for y in range(1, WALL_ROWS - 1): floor[y][x] = ('mid', 0xD6 if l else 0xD7 if r else 0xD2)
    floor[WALL_ROWS - 1][x] = ('hq', 0xD6 if l else 0xD7 if r else 0xD2)
    floor[WALL_ROWS][x] = ('hq', 0xC9)                         # the carpet's shadow row under the wall
    for y in range(WALL_ROWS + 1, H - 1): floor[y][x] = ('hq', CM.lattice(x, y))
    floor[H - 1][x] = ('hq', VOID_M)
for dx, (a, b) in enumerate(((0x120, 0xBD), (0x121, 0xBE), (0x122, 0xBF))):
    floor[H - 2][7 + dx] = ('hq', a); floor[H - 1][7 + dx] = ('hq', b)
TABLE = [[0x133, 0x131, 0x134], [0x123, 0x128, 0x125], [0x12B, 0x12C, 0x12D]]
TABLES = [(x0, y0) for y0 in (WALL_ROWS + 3, WALL_ROWS + 7, WALL_ROWS + 11) for x0 in (0, 14)]
for x0, y0 in TABLES:
    for dy in range(3):
        for dx in range(3): floor[y0 + dy][x0 + dx] = ('hq', TABLE[dy][dx])

# ---------------- object pieces (pixels) and their palette slots ----------------
GREAT, LANCET, STATUE, CRYS_A, CRYS_B, WALLSLOT, CARPET = 6, 7, 9, 10, 11, 8, 12
placed = []                                                     # (rgb, mask, px, py, slot), in drawing order
def place(rgb, m, px, py, slot): placed.append((rgb.astype(np.uint8), m, px, py, slot))
g, gm = CM.ch_window((4, 7352, 146, 7512), 80); g = CM.blonde(g, gm); place(g, gm, 8 * 16 + 8 - 40, 4, GREAT)
l, lm = CM.ch_window((150, 7392, 210, 7512), 32); place(l, lm, 3 * 16, 14, LANCET); place(l, lm, 12 * 16, 14, LANCET)
a, m = CM.ar((16, 34, 33, 64)); DOOR_PX = (1 * 16, WALL_ROWS * 16 - m.shape[0]); place(a, m, *DOOR_PX, STATUE)
a, m = CM.ar(CM.BOX[11]); place(a, m, 7 * 16, WALL_ROWS * 16, STATUE)                       # altar rug
a, m = CM.ar(CM.BOX[5]); place(a, m, 8 * 16 + 8 - m.shape[1] // 2, WALL_ROWS * 16 + 30 - m.shape[0], STATUE)
x0, y0, x1, y1 = CM.BOX[36]; a, m = CM.ar((x0, y0, x0 + 16, y1))
PILLAR_Y = (WALL_ROWS + 2) * 16 - m.shape[0] + 4
place(a, m, 5 * 16, PILLAR_Y, STATUE); place(a[:, ::-1], m[:, ::-1], 11 * 16, PILLAR_Y, STATUE)
x0, y0, x1, y1 = CM.BOX[63]
for k, px, slot in ((0, 3 * 16, CRYS_A), (1, 4 * 16, CRYS_A), (2, 12 * 16, CRYS_B), (3, 13 * 16, CRYS_B)):
    a, m = CM.ar((x0 + 16 * k, y0, x0 + 16 * k + 16, y1)); place(a, m, px, (WALL_ROWS + 2) * 16 - m.shape[0] + 2, slot)
x0, y0, x1, y1 = CM.BOX[1]; a, m = CM.ar((x0, y1 - 48, x1, y1)); place(a, m, 8 * 16 + 8 - 24, (WALL_ROWS + 3) * 16 + 4, CARPET)
PEWS = [(sx, sy) for sy in range(WALL_ROWS + 6, H - 3, 2) for sx in (4, 10)]
for sx, sy in PEWS:
    a, m = CM.pew(); place(a, m, sx * 16, sy * 16, WALLSLOT)

# ---------------- palettes ----------------
prim_pals = [[gba(c) for c in PP[i]] if i < 6 else [(0, 0, 0)] * 16 for i in range(16)]
sec_pals = [[(0, 0, 0)] * 16 for _ in range(16)]
reserved = {s: {0} for s in range(16)}
for s in (WALLSLOT, CARPET): sec_pals[s] = [gba(c) for c in SP[s]]
# which indices the Old HQ pieces we use draw with (they stay put)
USED_HQ = {0xCE, 0xCA, 0xCF, 0xD6, 0xD2, 0xD7, 0xC9, 0xC8, 0xD0, 0xE0, VOID_M, 0x120, 0x121, 0x122, 0xBD, 0xBE, 0xBF} | {m for r in TABLE for m in r}
for mm in USED_HQ:
    for v in hq_ents(mm):
        t = v & 0x3FF
        if t and hq_tile(t).any() and v >> 12 >= 6: reserved[v >> 12] |= set(np.unique(hq_tile(t)).tolist())
def allocate(slot, colours):
    """Map each colour to an index of the slot: an exact match, else a free index."""
    pal = sec_pals[slot]; out = {}
    for c in colours:
        c = gba(c); hit = [i for i in range(1, 16) if pal[i] == c and (i in reserved[slot] or i in out.values())]
        if hit: out[c] = hit[0]; continue
        free = [i for i in range(1, 16) if i not in reserved[slot] and i not in out.values()]
        assert free, f'slot {slot} is full'
        pal[free[0]] = c; out[c] = free[0]
    reserved[slot] |= set(out.values()); return out
def reduce(slot, n):
    """Quantize every piece of a slot together to at most n colours (the statue alone has 43 shades)."""
    group = [k for k, p in enumerate(placed) if p[4] == slot]
    px = np.concatenate([placed[k][0][placed[k][1]] for k in group]).reshape(1, -1, 3)
    q = Image.fromarray(px).quantize(n, method=Image.Quantize.MEDIANCUT)
    pal = np.array(q.getpalette()[:3 * n], np.uint8).reshape(-1, 3); idx = np.array(q)[0]; at = 0
    for k in group:
        rgb, m, x, y, s = placed[k]; cnt = int(m.sum()); new = rgb.copy(); new[m] = pal[idx[at:at + cnt]]; at += cnt
        placed[k] = (new, m, x, y, s)
LUT = {}
for slot in sorted({p[4] for p in placed}):
    cap = 15 - (len(reserved[slot]) - 1)
    cols = {gba(c) for k, p in enumerate(placed) if p[4] == slot for c in p[0][p[1]]}
    fresh = [c for c in cols if c not in sec_pals[slot]]
    if len(fresh) > cap: reduce(slot, cap); cols = {gba(c) for p in placed if p[4] == slot for c in p[0][p[1]]}
    LUT[slot] = allocate(slot, sorted(cols))

# ---------------- object layers: per 8x8 tile, one palette per layer ----------------
TOP = np.full((H * 16, W * 16), -1, np.int32)                  # which placement shows at each pixel
for k, (rgb, m, px, py, s) in enumerate(placed):
    h, w = m.shape; sub = TOP[py:py + h, px:px + w]; sub[m[:sub.shape[0], :sub.shape[1]]] = k
OBJ = {}                                                       # (cx, cy) -> [quad of layer A, quad of layer B]
for ty in range(H * 2):
    for tx in range(W * 2):
        blk = TOP[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8]; ks = sorted(set(blk[blk >= 0].tolist()))
        if not ks: continue
        by_slot = {}
        for k in ks: by_slot.setdefault(placed[k][4], []).append(k)
        order = sorted(by_slot, key=lambda s: min(by_slot[s]))  # the slot drawn first goes underneath
        assert len(order) <= 2, f'tile {tx},{ty}: three palettes'
        cx, cy, q = tx // 2, ty // 2, (ty % 2) * 2 + tx % 2
        for layer, slot in enumerate(order):
            t = np.zeros((8, 8), np.uint8)
            for k in by_slot[slot]:
                rgb, m, px, py, s = placed[k]
                for yy in range(8):
                    for xx in range(8):
                        if blk[yy, xx] == k:
                            Y, X = ty * 8 + yy - py, tx * 8 + xx - px; t[yy, xx] = LUT[slot][gba(rgb[Y, X])]
            OBJ.setdefault((cx, cy), [[0] * 4, [0] * 4])[layer][q] = add_tile(t) | slot << 12

# ---------------- metatiles and the layout ----------------
s_meta, s_attr, _mid = [], [], {}
def add_meta(e, a):
    k = (tuple(e), a)
    if k not in _mid:
        assert len(s_meta) < 512, 'secondary metatile budget'
        _mid[k] = 512 + len(s_meta); s_meta.append(list(e)); s_attr.append(a)
    return _mid[k]
def compact(e):
    layers = [e[k * 4:k * 4 + 4] for k in range(3) if not all(empty(v) for v in e[k * 4:k * 4 + 4])]
    while len(layers) < 3: layers.append([0] * 4)
    return [v for l in layers for v in l]
def overlay(e, q):
    used = [k for k in range(3) if not all(empty(v) for v in e[k * 4:k * 4 + 4])]
    k = max(used) + 1 if used else 0; assert k < 3, 'no free layer'
    e = list(e); e[k * 4:k * 4 + 4] = q; return e
SOLID = set()
for x0, y0 in TABLES: SOLID |= {(x0 + dx, y0 + dy) for dx in range(3) for dy in (1, 2)}
for sx, sy in PEWS: SOLID |= {(sx + dx, sy) for dx in range(3)}
SOLID |= {(x, y) for x in (7, 8, 9) for y in (WALL_ROWS, WALL_ROWS + 1)}                    # the altar
SOLID |= {(x, y) for x in (3, 4, 5, 11, 12, 13) for y in (WALL_ROWS, WALL_ROWS + 1)}        # crystals, pillars
DOOR = (1, WALL_ROWS - 1); EXIT = (8, H - 2)
grid = np.zeros((H, W), np.uint16)
for y in range(H):
    for x in range(W):
        kind, m = floor[y][x]
        e = mid_wall(m) if kind == 'mid' else hq_entries(m)
        a = hq_attr(m) if kind == 'hq' else MB_NORMAL
        if a & 0xFF == MB_INDOOR_ENCOUNTER: a = (a & ~0xFF) | MB_NORMAL
        if (x, y) in OBJ:
            e = compact(e)
            for q in OBJ[(x, y)]:
                if any(q): e = overlay(e, q)
        if (x, y) == DOOR: a = (a & ~0xFF) | MB_NON_ANIMATED_DOOR
        mid = add_meta(e, a)
        if (x, y) == DOOR or (x, y) == EXIT: col = WARP_E0 if (x, y) == DOOR else FLOOR_E3
        elif y < WALL_ROWS or y == H - 1 or (x, y) in SOLID: col = SOLID_E3 if y >= WALL_ROWS and y < H - 1 else WALL
        else: col = FLOOR_E3
        grid[y, x] = mid | col << 10
assert hq_attr(0x121) & 0xFF == MB_SOUTH_ARROW_WARP
VOID_ID = int(grid[H - 1, 0] & 0x3FF)                          # the black void (border)

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

def main():
    p_attr = []
    for i in range(512):
        a = hq_attr(i); p_attr.append((a & ~0xFF) | MB_NORMAL if a & 0xFF == MB_INDOOR_ENCOUNTER else a)
    write_tileset(os.path.join(C, 'data/tilesets/primary/old_hq_interior'), list(PT), prim_pals,
                  [hq_ents(i) for i in range(512)], p_attr, 1)
    write_tileset(os.path.join(C, 'data/tilesets/secondary/templar_hall'), s_tiles, sec_pals, s_meta, s_attr, GREAT)
    d = os.path.join(C, 'data/layouts/PellucaTemplarHall'); os.makedirs(d, exist_ok=True)
    grid.astype('<u2').tofile(os.path.join(d, 'map.bin'))
    open(os.path.join(d, 'border.bin'), 'wb').write(struct.pack('<4H', *[VOID_ID] * 4))
    lj = os.path.join(C, 'data/layouts/layouts.json'); L = json.load(open(lj)); lays = L['layouts']
    entry = {'id': 'LAYOUT_PELLUCA_TEMPLAR_HALL', 'name': 'PellucaTemplarHall_Layout', 'width': W, 'height': H,
             'primary_tileset': 'gTileset_OldHqInterior', 'secondary_tileset': 'gTileset_TemplarHall',
             'border_filepath': 'data/layouts/PellucaTemplarHall/border.bin',
             'blockdata_filepath': 'data/layouts/PellucaTemplarHall/map.bin'}
    old = [i for i, l in enumerate(lays) if l.get('id') == entry['id']]
    if old: lays[old[0]] = entry
    else: lays.insert([i for i, l in enumerate(lays) if l.get('id') == 'LAYOUT_PELLUCA_TEMPLAR_MONASTERY'][0] + 1, entry)
    json.dump(L, open(lj, 'w'), indent=2); open(lj, 'a').write('\n')
    print('secondary tiles', len(s_tiles), 'metatiles', len(s_meta), 'palettes',
          {s: 16 - sum(1 for i in range(1, 16) if i not in reserved[s]) for s in range(6, 13)})

if __name__ == '__main__':
    main()
