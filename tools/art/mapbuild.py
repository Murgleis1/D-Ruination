"""Layered picture -> a map's own tileset pair (primary + secondary), up to the engine's full budget.

academy/imgtiles.py flattens a picture into one layer and keeps every tile in the primary (512). Towns need more:
here the picture comes in three layers per cell (bottom: the ground, opaque; middle: what stands on it, drawn
under the player; top: what the player walks behind), so an object's tiles are shared whatever ground it stands
on, and the tiles fill both tilesets (1024 in all: 0-511 primary, 512-1023 secondary).

  * Colours on GBA 5-bit, those within one GBA step per channel merged into the commoner.
  * Each 8x8 tile of each layer gets one of up to 13 palettes (packed greedily over randomised orders, as imgtiles).
  * Seams with a neighbour (fixed=): metatiles, tiles and palette slots that must sit at given numbers, so the
    neighbour's own blocks draw right from here (a connected map is drawn with the tilesets of the map the player
    stands in); cells given as fixed take those metatiles and their own collision.
  * Metatiles: deduplicated, ids from 512 up (secondary), then 1-511 (primary) if more are needed.

build() -> dict(tiles, pals, meta, attrs, grid); write() writes the tilesets, the layout, the map and registers
them (via academy/imgtiles.py's registration).
"""
import os, sys, json, struct, random, collections
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'academy'))
import imgtiles as IT
C = IT.C
FLOOR_E3, SOLID_E3 = 3 << 2, 1 | 3 << 2

def _q(a): return (a >> 3) << 3

def build(bottom, mid, top, W, H, walk, beh=None, fixed=None, seed=7, tries=600, max_colours=None):
    """bottom: (H*16, W*16, 3); mid, top: ((H*16, W*16, 3), alpha) or None. walk: walkable cells;
    beh(x, y) -> metatile behaviour. fixed: dict(cells={(x, y): grid value}, tiles={n: 8x8 index array},
    pals={slot: [16 colours]}, meta={id: [12 entries]}, attrs={id: attr})."""
    fixed = fixed or {}
    fcells, ftiles, fpals = fixed.get('cells', {}), fixed.get('tiles', {}), fixed.get('pals', {})
    fmeta, fattrs = fixed.get('meta', {}), fixed.get('attrs', {})
    zero = np.zeros(bottom.shape[:2], bool)
    L = [(_q(bottom), ~zero)]
    for lay in (mid, top):
        L.append((_q(lay[0]), lay[1]) if lay is not None else (np.zeros_like(bottom), zero))
    live = lambda x, y: (x, y) not in fcells
    # colours: merge those within one GBA step into the commoner
    pix = collections.Counter()
    for y in range(H):
        for x in range(W):
            if not live(x, y): continue
            for img, a in L:
                s = (slice(y * 16, y * 16 + 16), slice(x * 16, x * 16 + 16))
                pix.update(map(tuple, img[s][a[s]].tolist()))
    rep = {}
    for c, _ in pix.most_common():
        if c in rep: continue
        rep[c] = c
        for d in pix:
            if d not in rep and max(abs(p - q) for p, q in zip(c, d)) <= 8: rep[d] = c
    if max_colours:                                    # merge further, nearest and rarest first, to fit the palettes
        cnt = collections.Counter()
        for c, n in pix.items(): cnt[rep[c]] += n
        fixed_c = {tuple(c) for p in fpals.values() for c in p[1:]}
        while len([c for c in cnt if c not in fixed_c]) > max_colours:
            cols = list(cnt); best = None
            for i, a in enumerate(cols):
                for b in cols[i + 1:]:
                    if a in fixed_c and b in fixed_c: continue
                    d = sum((p - q) ** 2 for p, q in zip(a, b)) ** 0.5 * min(cnt[a], cnt[b]) ** 0.5
                    if best is None or d < best[0]: best = (d, a, b)
            _, a, b = best
            keep, drop = (a, b) if (a in fixed_c or (cnt[a] >= cnt[b] and b not in fixed_c)) else (b, a)
            cnt[keep] += cnt.pop(drop)
            for k, v in rep.items():
                if v == drop: rep[k] = keep
    lut = {k: v for k, v in rep.items() if k != v}
    for img, a in L:
        if lut:
            flat = img.reshape(-1, 3); keys = [tuple(p) for p in flat.tolist()]
            for i, k in enumerate(keys):
                if k in lut: flat[i] = lut[k]
    # the tiles of every layer, their colour sets
    def blocks():
        for y in range(H):
            for x in range(W):
                if not live(x, y): continue
                for li, (img, a) in enumerate(L):
                    for q in range(4):
                        yy, xx = y * 16 + (q // 2) * 8, x * 16 + (q % 2) * 8
                        m = a[yy:yy + 8, xx:xx + 8]
                        if li and not m.any(): continue
                        yield x, y, li, q, img[yy:yy + 8, xx:xx + 8], (None if li == 0 else m)
    sets = set()
    for *_, t, m in blocks():
        cols = frozenset(map(tuple, (t[m] if m is not None else t.reshape(-1, 3)).tolist()))
        assert len(cols) <= 15, 'an 8x8 tile has %d colours' % len(cols)
        sets.add(cols)
    red = []
    for s in sorted(sets, key=len, reverse=True):
        if not any(s <= r for r in red): red.append(s)
    free_slots = [s for s in range(13) if s not in fpals]
    fixed_sets = [set(map(tuple, fpals[s][1:])) for s in sorted(fpals)]
    def greedy(order):
        pals = []
        for s in order:
            if any(s <= f for f in fixed_sets): continue
            best = None
            for i, p in enumerate(pals):
                n = len(p | s)
                if n <= 15 and (best is None or n - len(p) < best[0]): best = (n - len(p), i)
            if best is None: pals.append(set(s))
            else: pals[best[1]] |= s
        return pals
    def improve(groups):
        """Try to empty the smallest palette by moving each of its tile sets into another that still fits."""
        changed = True
        while changed and len(groups) > 1:
            changed = False
            groups.sort(key=lambda g: len(set().union(*g)))
            src = groups[0]; rest = groups[1:]; moved = []
            for s in sorted(src, key=len, reverse=True):
                for g in sorted(rest, key=lambda g: len(set().union(*g) | s) - len(set().union(*g))):
                    if len(set().union(*g) | s) <= 15: g.append(s); moved.append(s); break
                else: break
            if len(moved) == len(src): groups = rest; changed = True
            else:
                for s in moved:
                    for g in rest:
                        if s in g and g is not src: g.remove(s); break
        return groups
    rng = random.Random(seed); PALS = None
    for _ in range(tries):
        o = [s for s in red if not any(s <= f for f in fixed_sets)]; rng.shuffle(o); o.sort(key=lambda s: -len(s) + rng.random() * 4)
        groups = []
        for s in o:
            best = None
            for i, g in enumerate(groups):
                u = set().union(*g); n = len(u | s)
                if n <= 15 and (best is None or n - len(u) < best[0]): best = (n - len(u), i)
            if best is None: groups.append([s])
            else: groups[best[1]].append(s)
        groups = improve(groups)
        p = [set().union(*g) for g in groups]
        if PALS is None or len(p) < len(PALS): PALS = p
        if len(PALS) <= len(free_slots) and _ > tries // 4: break
    if len(PALS) > len(free_slots):
        allc = set().union(*red)
        print('packing failed: %d tile colour sets, %d colours, sizes %s, palette sizes %s' % (
            len(red), len(allc), sorted((len(s) for s in red), reverse=True)[:12], [len(p) for p in PALS]))
    assert len(PALS) <= len(free_slots), '%d palettes, %d free slots' % (len(PALS), len(free_slots))
    pal_cols = {}
    for slot, p in zip(free_slots, sorted(PALS, key=len, reverse=True)):
        pal_cols[slot] = [(0, 0, 0)] + sorted(p, key=sum)
    for slot, p in fpals.items(): pal_cols[slot] = list(p)
    slot_sets = {s: set(map(tuple, c[1:])) for s, c in pal_cols.items()}
    # tiles
    tiles = {0: np.zeros((8, 8), np.uint8)}; tiles.update(ftiles)
    tid = {}
    for n, t in tiles.items():
        if n == 0: tid.setdefault(t.tobytes(), (0, 0))
    free_tile = iter([n for n in range(1, 1024) if n not in tiles and n != 512])
    def add_tile(idx):
        for f, t in ((0, idx), (1, idx[:, ::-1]), (2, idx[::-1, :]), (3, idx[::-1, ::-1])):
            k = np.ascontiguousarray(t).tobytes()
            if k in tid: t0, f0 = tid[k]; return t0, f ^ f0
        n = next(free_tile); tiles[n] = idx.copy(); tid[idx.tobytes()] = (n, 0); return n, 0
    def entry(rgb, mask):
        cols = frozenset(map(tuple, (rgb[mask] if mask is not None else rgb.reshape(-1, 3)).tolist()))
        slot = min(s for s, ss in slot_sets.items() if cols <= ss)
        lk = {c: i for i, c in enumerate(pal_cols[slot]) if i}
        idx = np.zeros((8, 8), np.uint8)
        for yy in range(8):
            for xx in range(8):
                if mask is None or mask[yy, xx]: idx[yy, xx] = lk[tuple(rgb[yy, xx].tolist())]
        t, f = add_tile(idx); return t | f << 10 | slot << 12
    cell_e = {}
    for x, y, li, q, t, m in blocks():
        cell_e.setdefault((x, y), [0] * 12)[li * 4 + q] = entry(t, m)
    assert max(tiles) < 1024, '%d tiles' % len(tiles)
    # metatiles
    meta, attrs = dict(fmeta), dict(fattrs)
    free_mid = iter([m for m in list(range(512, 1024)) + list(range(1, 512)) if m not in meta])
    mid_of = {}
    grid = np.zeros((H, W), np.uint16); walk = set(walk)
    for y in range(H):
        for x in range(W):
            if not live(x, y): grid[y, x] = fcells[(x, y)]; continue
            a = beh(x, y) if beh else 0; k = (tuple(cell_e[(x, y)]), a)
            if k not in mid_of:
                m = next(free_mid); mid_of[k] = m; meta[m] = list(cell_e[(x, y)]); attrs[m] = a
            grid[y, x] = mid_of[k] | (FLOOR_E3 if (x, y) in walk else SOLID_E3) << 10
    print('palettes %d (+%d fixed), tiles %d (max no. %d), metatiles %d' % (len(PALS), len(fpals), len(tiles), max(tiles), len(meta)))
    return dict(tiles=tiles, pals=pal_cols, meta=meta, attrs=attrs, grid=grid)

def render(r, H=None, W=None):
    """Draw the result back from its tiles (a check)."""
    grid = r['grid']; H, W = grid.shape; out = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            for k, v in enumerate(r['meta'][int(grid[y, x] & 0x3FF)]):
                if k >= 4 and not v: continue
                t = r['tiles'].get(v & 0x3FF, np.zeros((8, 8), np.uint8))
                if v & 0x400: t = t[:, ::-1]
                if v & 0x800: t = t[::-1, :]
                q = k % 4; yy, xx = y * 16 + (q // 2) * 8, x * 16 + (q % 2) * 8
                mk = t != 0 if k >= 4 else np.ones((8, 8), bool)
                P = np.array((list(r['pals'].get(v >> 12, [(0, 0, 0)] * 16)) + [(0, 0, 0)] * 16)[:16], np.uint8)
                out[yy:yy + 8, xx:xx + 8][mk] = P[t][mk]
    return out

def _tileset_files(d, tiles, pals, meta, attrs, show):
    os.makedirs(os.path.join(d, 'palettes'), exist_ok=True)
    n = max(16, (max(tiles) + 1 + 15) // 16 * 16) if tiles else 16
    sheet = np.zeros((n // 16 * 8, 128), np.uint8)
    for i, t in tiles.items(): sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = t
    im = Image.fromarray(sheet, 'P'); im.putpalette([v for c in pals[show] for v in c] + [0] * (768 - 48))
    im.save(os.path.join(d, 'tiles.png'))
    for i, cols in enumerate(pals):
        with open(os.path.join(d, 'palettes', '%02d.pal' % i), 'w', newline='') as f:
            f.write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join('%d %d %d\r\n' % c for c in cols))
    with open(os.path.join(d, 'metatiles.bin'), 'wb') as f:
        for e in meta: f.write(struct.pack('<12H', *e))
    with open(os.path.join(d, 'metatile_attributes.bin'), 'wb') as f:
        for a in attrs: f.write(struct.pack('<H', a))

def write(r, map_name, layout_id, prim, sec, mapj, border=None, after_layout='LAYOUT_PELLUCA_ACADEMY_HALL',
          after_map='PellucaAcademyHall'):
    """prim/sec: (dir, Name). Writes both tilesets, the layout (+ layouts.json), the map (mapj; None: layout only),
    registers the tilesets, the map's group entry and its scripts include."""
    blank = [(0, 0, 0)] * 16
    pals = [(list(r['pals'][i]) + blank)[:16] if i in r['pals'] else blank for i in range(16)]
    pt = {n: t for n, t in r['tiles'].items() if n < 512}
    st = {n - 512: t for n, t in r['tiles'].items() if n >= 512}
    pm = [r['meta'].get(i, [0] * 12) for i in range(max([i for i in r['meta'] if i < 512] + [0]) + 1)]
    pa = [r['attrs'].get(i, 0) for i in range(len(pm))]
    sm = [r['meta'].get(i, [0] * 12) for i in range(512, max([i for i in r['meta'] if i >= 512] + [512]) + 1)]
    sa = [r['attrs'].get(i, 0) for i in range(512, 512 + len(sm))]
    _tileset_files(os.path.join(C, 'data/tilesets/primary', prim[0]), pt, [p if i < 6 else blank for i, p in enumerate(pals)], pm, pa, 0)
    _tileset_files(os.path.join(C, 'data/tilesets/secondary', sec[0]), st or {0: np.zeros((8, 8), np.uint8)},
                   [p if 6 <= i < 13 else blank for i, p in enumerate(pals)], sm, sa, 6)
    H, W = r['grid'].shape
    d = os.path.join(C, 'data/layouts', map_name); os.makedirs(d, exist_ok=True)
    r['grid'].astype('<u2').tofile(os.path.join(d, 'map.bin'))
    b = border if border is not None else [int(r['grid'][0, 0] & 0x3FF)] * 4
    open(os.path.join(d, 'border.bin'), 'wb').write(struct.pack('<4H', *b))
    lj = os.path.join(C, 'data/layouts/layouts.json'); Lj = json.load(open(lj)); lays = Lj['layouts']
    entry = {'id': layout_id, 'name': map_name + '_Layout', 'width': W, 'height': H,
             'primary_tileset': 'gTileset_' + prim[1], 'secondary_tileset': 'gTileset_' + sec[1],
             'border_filepath': 'data/layouts/%s/border.bin' % map_name, 'blockdata_filepath': 'data/layouts/%s/map.bin' % map_name}
    old = [i for i, l in enumerate(lays) if l.get('id') == layout_id]
    if old: lays[old[0]] = entry
    else: lays.insert([i for i, l in enumerate(lays) if l.get('id') == after_layout][0] + 1, entry)
    json.dump(Lj, open(lj, 'w'), indent=2); open(lj, 'a').write('\n')
    IT.register_tilesets([('primary', prim[0], prim[1]), ('secondary', sec[0], sec[1])])
    if mapj is None: return
    md = os.path.join(C, 'data/maps', map_name); os.makedirs(md, exist_ok=True)
    json.dump(mapj, open(os.path.join(md, 'map.json'), 'w'), indent=2); open(os.path.join(md, 'map.json'), 'a').write('\n')
    IT._add('data/event_scripts.s', '\t.include "data/maps/%s/scripts.inc"\n' % after_map, '\t.include "data/maps/%s/scripts.inc"\n' % map_name)
    gj = os.path.join(C, 'data/maps/map_groups.json'); G = json.load(open(gj))
    if map_name not in G['gMapGroup_Phase3']:
        G['gMapGroup_Phase3'].append(map_name); json.dump(G, open(gj, 'w'), indent=2); open(gj, 'a').write('\n')
    sp = os.path.join(md, 'scripts.pory')
    if not os.path.exists(sp): open(sp, 'w').write('mapscripts %s_MapScripts {}\n' % map_name)
