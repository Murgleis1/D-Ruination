"""Image -> tileset pair + layout, the method build_hall.py uses for the Academy hall, made reusable for its rooms.

An approved mock (one RGB image, optionally an over-the-player layer with its mask) is cut into 8x8 tiles:
  * colours on GBA 5-bit; colours within one GBA step per channel merged into the more common one;
  * the tiles' colour sets packed into <= 13 palettes of 15 (randomised greedy, fixed seed);
  * primary tileset = all tiles + palettes 0-5 (the most used), secondary = palettes 6-12 + the metatiles
    ([under | empty | over] per cell), metatile attributes from a behaviour function.
write_room() writes the tilesets, the layout (+ layouts.json entry), map.json, and registers the tilesets in the
C tables, the map in its group and its script include.
"""
import os, json, struct, random, collections
import numpy as np
from PIL import Image
C = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'codebase'))
WALL, FLOOR_E3, SOLID_E3, WARP_E0 = 1, 3 << 2, 1 | 3 << 2, 0

def build(under, W, H, over=None, om=None, walk=(), beh=None, col=None, seed=7, merge=8, tries=1500, rare=None):
    """-> dict(tiles, pals, meta, attrs, grid, void): `walk` = walkable cells; beh(x, y) -> behaviour;
    col(x, y) -> collision byte or None for the default (walkable: FLOOR_E3, else SOLID_E3); `merge`: colours this
    close per channel are merged (8 = one GBA step; past 8 only colours under `rare` pixels, if given); `tries`: randomised palette packings tried."""
    under = (under >> 3) << 3
    if over is None: over, om = np.zeros_like(under), np.zeros(under.shape[:2], bool)
    over = (over >> 3) << 3
    pix = collections.Counter(map(tuple, under.reshape(-1, 3).tolist())) + collections.Counter(map(tuple, over[om].tolist()))
    rep = {}
    for c, _ in pix.most_common():
        if c in rep: continue
        rep[c] = c
        for d in pix:
            if d in rep: continue
            dist = max(abs(a - b) for a, b in zip(c, d))
            if dist <= 8 or (dist <= merge and (rare is None or pix[d] < rare)): rep[d] = c
    def remap(img):
        out = img.copy(); flat = out.reshape(-1, 3)
        for k, v in rep.items():
            if k != v: flat[(flat == k).all(1)] = v
        return out
    under, over = remap(under), remap(over)
    def blocks():
        for ty in range(H * 2):
            for tx in range(W * 2):
                yield tx, ty, under[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8], over[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8], om[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8]
    sets = set()
    for _, _, u, o, mk in blocks():
        sets.add(frozenset(map(tuple, u.reshape(-1, 3).tolist())))
        if mk.any(): sets.add(frozenset(map(tuple, o[mk].tolist())))
    red = []
    for s in sorted(sets, key=len, reverse=True):
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
    rng = random.Random(seed); PALS = None
    for _ in range(tries):
        o = list(red); rng.shuffle(o); o.sort(key=lambda s: -len(s) + rng.random() * 4)
        p = greedy(o)
        if PALS is None or len(p) < len(PALS): PALS = p
    assert len(PALS) <= 13, f'{len(PALS)} palettes'
    use = collections.Counter()
    for _, _, u, _, _ in blocks():
        s = frozenset(map(tuple, u.reshape(-1, 3).tolist())); use[[i for i, p in enumerate(PALS) if s <= p][0]] += 1
    order = sorted(range(len(PALS)), key=lambda i: -use[i])
    pal_cols = [[(0, 0, 0)] + sorted(PALS[i], key=lambda c: sum(c)) for i in order]; slot_sets = [set(PALS[i]) for i in order]
    tiles = [np.zeros((8, 8), np.uint8)]; tid = {tiles[0].tobytes(): (0, 0)}
    def add_tile(idx):
        for f, t in ((0, idx), (1, idx[:, ::-1]), (2, idx[::-1, :]), (3, idx[::-1, ::-1])):
            k = np.ascontiguousarray(t).tobytes()
            if k in tid: t0, f0 = tid[k]; return t0, f ^ f0
        n = len(tiles); tiles.append(idx.copy()); tid[idx.tobytes()] = (n, 0); return n, 0
    def entry(rgb, mask=None):
        cols = frozenset(map(tuple, (rgb[mask] if mask is not None else rgb.reshape(-1, 3)).tolist()))
        slot = [k for k, s in enumerate(slot_sets) if cols <= s][0]; lut = {c: i for i, c in enumerate(pal_cols[slot]) if i}
        idx = np.zeros((8, 8), np.uint8)
        for yy in range(8):
            for xx in range(8):
                if mask is None or mask[yy, xx]: idx[yy, xx] = lut[tuple(rgb[yy, xx].tolist())]
        t, f = add_tile(idx); return t | f << 10 | slot << 12
    cell_e = {}
    for tx, ty, u, o, mk in blocks():
        e = cell_e.setdefault((tx // 2, ty // 2), [0] * 12); q = (ty % 2) * 2 + tx % 2
        e[q] = entry(u)
        if mk.any(): e[8 + q] = entry(o, mk)
    assert len(tiles) <= 512, f'{len(tiles)} tiles'
    meta, attrs, mid = [], [], {}
    grid = np.zeros((H, W), np.uint16); walk = set(walk)
    for y in range(H):
        for x in range(W):
            a = beh(x, y) if beh else 0
            k = (tuple(cell_e[(x, y)]), a)
            if k not in mid:
                assert len(meta) < 512, 'secondary metatile budget'
                mid[k] = 512 + len(meta); meta.append(list(cell_e[(x, y)])); attrs.append(a)
            c = col(x, y) if col else None
            if c is None: c = FLOOR_E3 if (x, y) in walk else SOLID_E3
            grid[y, x] = mid[k] | c << 10
    return dict(tiles=tiles, pals=pal_cols, meta=meta, attrs=attrs, grid=grid, void=int(grid[0, 0] & 0x3FF), npal=len(PALS),
                under=under, over=over, om=om)

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

def _add(path, after, text):
    f = os.path.join(C, path); t = open(f).read()
    if text.strip().splitlines()[0] in t: return
    i = t.index(after) + len(after); open(f, 'w').write(t[:i] + text + t[i:])

def register_tilesets(pairs):
    """pairs: [(kind, dir, Name)]; appended after the Academy hall's own entries."""
    for kind, dirn, name in pairs:
        pal = ''.join(f'    INCBIN_U16("data/tilesets/{kind}/{dirn}/palettes/{i:02d}.gbapal"),\n' for i in range(16))
        _add('src/data/tilesets/graphics.h', 'gTilesetTiles_AcademyHall[] = INCBIN_U32("data/tilesets/secondary/academy_hall/tiles.4bpp.lz");\n',
             f'\nconst u16 gTilesetPalettes_{name}[][16] =\n{{\n{pal}}};\n\n'
             f'const u32 gTilesetTiles_{name}[] = INCBIN_U32("data/tilesets/{kind}/{dirn}/tiles.4bpp.lz");\n')
        _add('src/data/tilesets/metatiles.h', 'gMetatileAttributes_AcademyHall[] = INCBIN_U16("data/tilesets/secondary/academy_hall/metatile_attributes.bin");\n',
             f'const u16 gMetatiles_{name}[] = INCBIN_U16("data/tilesets/{kind}/{dirn}/metatiles.bin");\n'
             f'const u16 gMetatileAttributes_{name}[] = INCBIN_U16("data/tilesets/{kind}/{dirn}/metatile_attributes.bin");\n')
        hdr = open(os.path.join(C, 'src/data/tilesets/headers.h')).read(); i = hdr.index('const struct Tileset gTileset_AcademyHall =')
        _add('src/data/tilesets/headers.h', hdr[i:hdr.index('};', i) + 3],
             f'\nconst struct Tileset gTileset_{name} =\n{{\n    .isCompressed = TRUE,\n    .isSecondary = {"TRUE" if kind == "secondary" else "FALSE"},\n'
             f'    .tiles = gTilesetTiles_{name},\n    .palettes = gTilesetPalettes_{name},\n    .metatiles = gMetatiles_{name},\n'
             f'    .metatileAttributes = gMetatileAttributes_{name},\n    .callback = NULL,\n}};\n')

def write_room(r, map_name, layout_id, prim, sec, mapj, after_layout='LAYOUT_PELLUCA_ACADEMY_HALL', after_map='PellucaAcademyHall'):
    """prim/sec: (dir, Name). Writes everything for one room."""
    blank = [(0, 0, 0)] * 16; P = r['pals']
    pals = [(P[i] + [(0, 0, 0)] * 16)[:16] if i < len(P) else blank for i in range(16)]
    write_tileset(os.path.join(C, 'data/tilesets/primary', prim[0]), r['tiles'], [p if i < 6 else blank for i, p in enumerate(pals)], [[0] * 12], [0], 0)
    write_tileset(os.path.join(C, 'data/tilesets/secondary', sec[0]), [np.zeros((8, 8), np.uint8)],
                  [p if 6 <= i < 13 else blank for i, p in enumerate(pals)], r['meta'], r['attrs'], 6)
    H, W = r['grid'].shape
    d = os.path.join(C, 'data/layouts', map_name); os.makedirs(d, exist_ok=True)
    r['grid'].astype('<u2').tofile(os.path.join(d, 'map.bin'))
    open(os.path.join(d, 'border.bin'), 'wb').write(struct.pack('<4H', *[r['void']] * 4))
    lj = os.path.join(C, 'data/layouts/layouts.json'); L = json.load(open(lj)); lays = L['layouts']
    entry = {'id': layout_id, 'name': map_name + '_Layout', 'width': W, 'height': H,
             'primary_tileset': 'gTileset_' + prim[1], 'secondary_tileset': 'gTileset_' + sec[1],
             'border_filepath': f'data/layouts/{map_name}/border.bin', 'blockdata_filepath': f'data/layouts/{map_name}/map.bin'}
    old = [i for i, l in enumerate(lays) if l.get('id') == layout_id]
    if old: lays[old[0]] = entry
    else: lays.insert([i for i, l in enumerate(lays) if l.get('id') == after_layout][0] + 1, entry)
    json.dump(L, open(lj, 'w'), indent=2); open(lj, 'a').write('\n')
    md = os.path.join(C, 'data/maps', map_name); os.makedirs(md, exist_ok=True)
    json.dump(mapj, open(os.path.join(md, 'map.json'), 'w'), indent=2); open(os.path.join(md, 'map.json'), 'a').write('\n')
    register_tilesets([('primary', prim[0], prim[1]), ('secondary', sec[0], sec[1])])
    _add('data/event_scripts.s', f'\t.include "data/maps/{after_map}/scripts.inc"\n', f'\t.include "data/maps/{map_name}/scripts.inc"\n')
    gj = os.path.join(C, 'data/maps/map_groups.json'); G = json.load(open(gj))
    if map_name not in G['gMapGroup_Phase3']:
        G['gMapGroup_Phase3'].append(map_name); json.dump(G, open(gj, 'w'), indent=2); open(gj, 'a').write('\n')

def check(r):
    """Re-render the built tiles/palettes/metatiles and compare with the (colour-merged) image; -> mismatches."""
    tiles, pals = r['tiles'], r['pals']; H, W = r['grid'].shape; out = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            e = r['meta'][int(r['grid'][y, x] & 0x3FF) - 512]
            for k, v in enumerate(e):
                if k >= 4 and not v: continue
                t = tiles[v & 0x3FF]
                if v & 0x400: t = t[:, ::-1]
                if v & 0x800: t = t[::-1, :]
                q = k % 4; yy, xx = y * 16 + (q // 2) * 8, x * 16 + (q % 2) * 8; mk = t != 0 if k >= 4 else np.ones((8, 8), bool)
                P = np.array((pals[v >> 12] + [(0, 0, 0)] * 16)[:16], np.uint8); out[yy:yy + 8, xx:xx + 8][mk] = P[t][mk]
    ref = r['under'].copy(); ref[r['om']] = r['over'][r['om']]
    return int((np.abs(out.astype(int) - ref.astype(int)).sum(-1) > 0).sum())
