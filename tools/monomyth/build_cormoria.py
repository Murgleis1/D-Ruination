"""Build gTileset_Cormoria (shared primary) + gTileset_PellucaValley (secondary).

Sources (decisions + measurements: assets/pelluca_dock_spec/PELLUCA_DESIGN.md):
  primary   = Wood Avens terrain (trimmed), Port Ginseng quay G, Old Bay sandbank J,
              + the residence model's tiles (shared art)
  secondary = Academy, Cadmus house, Lab tower, Residence (metatiles), Wood Avens;
              Tavern (lodge G) + Guardhouse (keep gate), Fort Elderflower;
              Arceus church, Evernahn r17-26 c0-c6 minus 6 junk cells.

Ruination is TRIPLE-LAYER (tools/metatile_format.py), so every MonoMyth layer is
copied as-is: entries 0-3 bottom, 4-7 middle, 8-11 top. Nothing is baked.

Colour: one tolerance-16 merge (approved on screen, palette_tolerance_compare.png #2),
then palettes packed: terrain into primary slots 0-5, buildings into 6-12 (a building
tile whose colours already fit a terrain palette uses it).

Tiles: deduplicated by INDEX pattern incl. h/v flips; secondary metatiles reuse
primary tiles where identical. Tile 0 of the primary stays blank (entry 0 = empty).

Writes nothing outside the two new tileset directories + build/ manifest.
Usage: MONOMYTH_ROM=... python3 -I build_cormoria.py <codebase dir>
"""
import sys, os, json, struct
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from romlib import *
import budget_terrain as bt
import palette_pack as pp

WA, FE = 0x869580, 0x86960C
PG64, OB12 = 0x86DB2C, 0x86DA30
# Wood Avens terrain drops (wa_rare.json badge numbers; see PELLUCA_DESIGN.md)
DROP_BADGES = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 31, 35, 36, 51, 52, 58, 49, 50, 48,
               45, 46, 56, 57, 59, 60, 14, 15, 16, 28, 29, 30, 32, 33, 34]
BUILDINGS = [  # name, source map, box (x0,y0,x1,y1) in source cells
    ('academy', WA, (18, 26, 24, 33)), ('cadmus_house', WA, (5, 28, 11, 32)),
    ('lab_tower', WA, (15, 10, 20, 14)), ('residence', WA, (5, 20, 11, 24)),
    ('tavern', FE, (38, 40, 43, 47)), ('guardhouse', FE, (27, 12, 34, 18)),   # tavern x37/x44 = town wall
]
TERRAIN_EXTRA = [('quay', PG64, (35, 37, 44, 44)), ('sandbank', OB12, (18, 47, 28, 54))]
CHURCH_ROWS, CHURCH_COLS = range(17, 27), range(0, 7)
CHURCH_JUNK = {(17, 0), (17, 1), (17, 5), (17, 6), (18, 0), (18, 6)}
TOL = 16


def src_metatile(a, mid):
    L = bt.ctx(a)[0]
    base = off(L['primary']['mt']) + mid * 24 if mid < 512 else off(L['secondary']['mt']) + (mid - 512) * 24
    abase = off(L['primary']['attr']) + mid * 2 if mid < 512 else off(L['secondary']['attr']) + (mid - 512) * 2
    return [u16(base + i * 2) for i in range(12)], u16(abase)


def cell(a, x, y):
    L = bt.ctx(a)[0]
    return u16(off(L['map']) + (y * L['w'] + x) * 2) & 0x3FF


def quad_img(a, e):
    """Entry -> 8x8 RGB image (-1 = transparent), source flips applied."""
    if (e & 0x3FF) == 0:
        return None
    im = bt.quad([e], bt.ctx(a))
    return im if (im >= 0).any() else None


def is_snow_ground(a, mid):
    """True only for cells that RENDER as snow: bright, near-colourless, uniform.
    (A frequency filter wrongly dropped Elderflower's stone wall fill too.)"""
    e, _ = src_metatile(a, mid)
    ims = [quad_img(a, v) for v in e]
    px = np.concatenate([im.reshape(-1, 3) for im in ims if im is not None]) if any(im is not None for im in ims) else None
    if px is None: return False
    px = px[(px >= 0).all(1)]
    bright = px.mean(1) > 185
    grey = (px.max(1) - px.min(1)) < 48
    return (bright & grey).mean() > 0.9


def select():
    rare = {i: m for i, m, _ in json.load(open(os.environ.get('WA_RARE', '/home/claude/scratch/wa_rare.json')))}
    drop = {rare[b] for b in DROP_BADGES}
    L = bt.ctx(WA)[0]
    prim, regions = [], {}
    seen = set()
    def add(lst, a, mid):
        if (a, mid) not in seen:
            seen.add((a, mid)); lst.append((a, mid))
    grid = []
    for y in range(9, 46):
        row = []
        for x in range(L['w']):
            mid = cell(WA, x, y)
            inb = any(x0 <= x <= x1 and y0 <= y <= y1 for _, aa, (x0, y0, x1, y1) in BUILDINGS if aa == WA)
            if inb or mid in drop:
                row.append(None); continue
            add(prim, WA, mid); row.append((WA, mid))
        grid.append(row)
    regions['wa_terrain'] = (WA, (0, 9), grid)
    for name, a, (x0, y0, x1, y1) in TERRAIN_EXTRA:
        g = []
        for y in range(y0, y1 + 1):
            g.append([]);
            for x in range(x0, x1 + 1):
                mid = cell(a, x, y); add(prim, a, mid); g[-1].append((a, mid))
        regions[name] = (a, (x0, y0), g)
    sec = []
    from collections import Counter
    for name, a, (x0, y0, x1, y1) in BUILDINGS:
        g = []
        for y in range(y0, y1 + 1):
            g.append([])
            for x in range(x0, x1 + 1):
                mid = cell(a, x, y)
                if (a, mid) in seen:
                    g[-1].append((a, mid)); continue
                if a == FE and is_snow_ground(a, mid):  # Elderflower snow ground: not imported
                    g[-1].append(None); continue
                add(sec, a, mid); g[-1].append((a, mid))
        regions[name] = (a, (x0, y0), g)
    return prim, sec, regions


def church_quads(grass_bottom):
    ev = np.array(Image.open(os.path.join(HERE, '../../assets/pelluca_tileset_source/Evernahn.png')).convert('RGBA'))
    cells = {}
    for r in CHURCH_ROWS:
        for c in CHURCH_COLS:
            if (r, c) in CHURCH_JUNK:
                continue
            a = ev[r * 32:(r + 1) * 32, c * 32:(c + 1) * 32]
            small = np.full((16, 16, 3), -1, int)
            for y in range(16):
                for x in range(16):
                    blk = a[y * 2:y * 2 + 2, x * 2:x * 2 + 2].reshape(-1, 4); op = blk[blk[:, 3] > 0]
                    if len(op) >= 2:
                        u, k = np.unique(op[:, :3], axis=0, return_counts=True)
                        small[y, x] = (u[k.argmax()] >> 3) << 3
            mids = [small[qy:qy + 8, qx:qx + 8] for qy in (0, 8) for qx in (0, 8)]
            cells[(r, c)] = mids
    return cells


# Tavern finish (user decisions 2026-11-15): snow removed with roof fill + ivy on the
# ledges (option 3), right lower roof repaired from real shingles above, roof
# recoloured DUSK PLUM. Reproducible from source: no hand-edited files.
def _plum():
    """The EXACT ramp the user approved (tavern_roof_colours.png panel 4), read from
    the file it was rendered from -- never retyped (a retyped copy was wrong once)."""
    import json
    p = os.path.join(HERE, '../../assets/pelluca_dock_spec/tavern_roof_ramps.json')
    return {tuple(k): tuple(v) for k, v in json.load(open(p))['C dusk plum']}
PLUM = _plum()


def tavern_finished():
    import desnow as ds
    a = FE; (x0, y0, x1, y1) = [bx for n, _, bx in BUILDINGS if n == 'tavern'][0]
    W, H = x1 - x0 + 1, y1 - y0 + 1
    lay = [np.full((H * 16, W * 16, 3), -1, int) for _ in range(3)]
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            e, _ = src_metatile(a, cell(a, x, y))
            for L in range(3):
                for q in range(4):
                    im = quad_img(a, e[L * 4 + q])
                    if im is None: continue
                    oy, ox = (y - y0) * 16 + (q // 2) * 8, (x - x0) * 16 + (q % 2) * 8
                    m = (im >= 0).all(-1); lay[L][oy:oy + 8, ox:ox + 8][m] = im[m]
    protect = np.zeros(lay[1].shape[:2], bool); protect[6 * 16:8 * 16, 4 * 16:5 * 16] = True   # lamp post
    wa = np.zeros((1, 1, 3))
    from render import render_map  # noqa: F401  (render util lives beside this file)
    import pickle
    wa_png = os.environ.get('WA_RENDER', '/home/claude/mono/woodavens.png')
    wa = np.array(Image.open(wa_png).convert('RGB')).astype(int)
    leaves, _ = ds.leaf_patch(wa)
    mid, top = ds.desnow_building(lay[1], lay[2], (56, 56, 88), protect, 88, 110, facade_leaves=leaves)
    mid = ds.patch_from_above(mid, top, lay[1], lay[2], (62, 64, 96, 83), 16, protect)
    for img in (mid, top):
        for src, dst in PLUM.items():
            img[(img == np.array(src)).all(-1)] = dst
    return (x0, y0, W, H), mid, top


def main():
    C = sys.argv[1]
    prim, sec, regions = select()
    # ---- gather every layer quad image, keyed so metatiles can be rebuilt
    Q = {}            # (kind, key, entry index) -> image
    meta_src = {}     # (kind, key) -> (12 entries, attr)
    for kind, lst in (('p', prim), ('s', sec)):
        for a, mid in lst:
            e, attr = src_metatile(a, mid)
            meta_src[(kind, (a, mid))] = (e, attr)
            for i in range(12):
                im = quad_img(a, e[i])
                if im is not None:
                    Q[(kind, (a, mid), i)] = im
    # church: bottom = Wood Avens base grass (most common WA ground metatile), middle = church art
    from collections import Counter
    wa_grid = regions['wa_terrain'][2]
    base_grass = Counter(c for row in wa_grid for c in row if c).most_common(1)[0][0]
    ge, _ = src_metatile(*base_grass)
    # Wood Avens keeps ground on whichever layer it likes (often the MIDDLE): take the
    # first non-empty layer of the base grass metatile as the church's ground.
    glayer = next(L for L in range(3) if any(ge[L * 4 + q] & 0x3FF for q in range(4)))
    gq = ge[glayer * 4:glayer * 4 + 4]
    church = church_quads(gq)
    for (r, c), mids in church.items():
        meta_src[('s', ('church', r, c))] = (None, 0)
        for q in range(4):
            gi = quad_img(base_grass[0], gq[q])
            if gi is not None: Q[('s', ('church', r, c), q)] = gi
            if (mids[q] >= 0).any(): Q[('s', ('church', r, c), 4 + q)] = mids[q]
    # ---- tavern: replace its metatiles' layers with the finished (snow-free) art
    (tx0, ty0, TW, TH), tmid, ttop = tavern_finished()
    done_mt = set()
    for yy in range(TH):
        for xx in range(TW):
            key = (FE, cell(FE, tx0 + xx, ty0 + yy))
            if ('s', key) not in meta_src or key in done_mt:
                continue
            done_mt.add(key)
            for i in range(12):
                Q.pop(('s', key, i), None)
            for L, img in ((1, tmid), (2, ttop)):
                for q in range(4):
                    sub = img[yy * 16 + (q // 2) * 8: yy * 16 + (q // 2) * 8 + 8, xx * 16 + (q % 2) * 8: xx * 16 + (q % 2) * 8 + 8]
                    if (sub >= 0).all(-1).any():
                        Q[('s', key, L * 4 + q)] = sub.copy()
            for q in range(4):                                   # ground: Wood Avens grass
                gi = quad_img(base_grass[0], gq[q])
                if gi is not None: Q[('s', key, q)] = gi
    # ---- colour merge (one map over everything)
    allbytes = {im.tobytes() for im in Q.values()}
    cmap, ncol = pp.merge_map(allbytes, TOL)
    def remap(im):
        out = im.copy(); f = out.reshape(-1, 3)
        for k, c in enumerate(map(tuple, f)):
            if c[0] >= 0: f[k] = cmap[c]
        return out
    Q = {k: remap(v) for k, v in Q.items()}
    cs = lambda im: frozenset(map(tuple, im.reshape(-1, 3)[(im.reshape(-1, 3) >= 0).all(1)]))
    # ---- palettes. Measured: Wood Avens terrain packs into 4; the coastal pieces
    # (quay, sandbank) need 3 more. Shared slots 0-5 = WA terrain + as many coastal
    # palettes as fit; remaining coastal palette(s) lead the secondary (6-12):
    # shore colours are regional, provided by each coastal town's secondary.
    def keyset(k): return cs(Q[k])
    wa_k = [k for k in Q if k[0] == 'p' and k[1][0] == WA]
    co_k = [k for k in Q if k[0] == 'p' and k[1][0] != WA]
    pw = pp.pack_best([keyset(k) for k in wa_k], tries=300)
    co_left = [keyset(k) for k in co_k if not any(keyset(k) <= p for p in pw)]
    pc = pp.pack_best(co_left, tries=300) if co_left else []
    ppals = (pw + pc)[:6]
    spill = (pw + pc)[6:]
    all_terr = ppals + spill
    b_left = [cs(v) for k, v in Q.items() if k[0] == 's' and not any(cs(v) <= p for p in all_terr)]
    bp = pp.pack_best(b_left, tries=300) if b_left else []
    spals = spill + bp
    assert len(ppals) <= 6 and len(spals) <= 7, f'palettes: primary {len(ppals)}/6, secondary {len(spals)}/7'
    print(f'palettes: WA terrain {len(pw)}, coastal {len(pc)}, buildings {len(bp)} -> primary {len(ppals)}, secondary {len(spals)}')
    slots = {i: sorted(p, key=lambda c: (0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2])) for i, p in enumerate(ppals)}
    slots.update({6 + i: sorted(p, key=lambda c: (0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2])) for i, p in enumerate(spals)})
    def slot_for(im, kind):
        s = cs(im)
        for i in sorted(slots):            # terrain may use a spilled coastal slot (>= 6)
            if s <= set(slots[i]): return i
        raise AssertionError('no palette holds a tile')
    # ---- tiles (dedupe by index pattern incl. flips)
    ptiles = [np.zeros((8, 8), np.uint8)]; stiles = []
    pidx, sidx = {ptiles[0].tobytes(): (0, 0, 0)}, {}
    def to_idx(im, sl):
        lut = {c: i + 1 for i, c in enumerate(slots[sl])}
        out = np.zeros((8, 8), np.uint8)
        for y in range(8):
            for x in range(8):
                c = tuple(im[y, x])
                if c[0] >= 0: out[y, x] = lut[c]
        return out
    def place(idx, kind):
        for hf in (0, 1):
            for vf in (0, 1):
                v = idx[:, ::-1] if hf else idx
                v = v[::-1] if vf else v
                k = v.tobytes()
                if k in pidx: return pidx[k][0], hf, vf
                if kind == 's' and k in sidx: return sidx[k][0], hf, vf
        if kind == 'p':
            ptiles.append(idx); tid = len(ptiles) - 1; pidx[idx.tobytes()] = (tid, 0, 0)
        else:
            stiles.append(idx); tid = 512 + len(stiles) - 1; sidx[idx.tobytes()] = (tid, 0, 0)
        return tid, 0, 0
    # The residence is the SHARED house model: its tile art lives in the primary
    # (every town reuses it); its metatiles stay in each town's secondary so the
    # roof palette can differ per town.
    # Tavern too: every Cormorian town has one (bible), so its art is shared as well.
    res_keys = {c for name in ('residence', 'tavern') for row in regions[name][2] for c in row if c}
    entries = {}
    for k, im in sorted(Q.items(), key=lambda kv: (kv[0][0] != 'p', kv[0][1] not in res_keys)):
        sl = slot_for(im, k[0])
        tile_kind = 'p' if (k[0] == 'p' or k[1] in res_keys) else 's'
        tid, hf, vf = place(to_idx(im, sl), tile_kind)
        entries[k] = tid | (hf << 10) | (vf << 11) | (sl << 12)
    print(f'tiles: primary {len(ptiles)}/512, secondary {len(stiles)}/512')
    assert len(ptiles) <= 512, f'primary tiles {len(ptiles)} > 512'
    assert len(stiles) <= 512, f'secondary tiles {len(stiles)} > 512'
    assert all(t >= 512 for t in sidx.values() for t in [t[0]]), 'secondary tile id below 512'
    # ---- metatiles + attributes
    pmeta, smeta, newid = [], [], {}
    pmeta.append(([0] * 12, 0)); # metatile 0 = empty
    for kind, key in [k for k in meta_src]:
        e = [entries.get((kind, key, i), 0) for i in range(12)]
        src_e, src_attr = meta_src[(kind, key)]
        beh = src_attr & 0xFF
        layer = 0 if any(e[8:12]) else 1     # NORMAL if top layer used, else COVERED (gameplay meaning)
        attr = beh | (layer << 12)
        if kind == 'p':
            newid[key] = len(pmeta); pmeta.append((e, attr))
        else:
            newid[key] = 512 + len(smeta); smeta.append((e, attr))
    assert len(pmeta) <= 512 and len(smeta) <= 512
    # ---- write
    def write_ts(d, tiles, metas, pal_slots, is_sec):
        os.makedirs(os.path.join(d, 'palettes'), exist_ok=True)
        n = max(16, ((len(tiles) + 15) // 16) * 16)
        sheet = np.zeros((n // 16 * 8, 128), np.uint8)
        for i, t in enumerate(tiles):
            sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = t
        im = Image.fromarray(sheet, 'P')
        show = slots.get(6 if is_sec else 0, [])
        flat = [0, 0, 0] + [v for c in show for v in c]
        im.putpalette(flat + [0] * (768 - len(flat))); im.save(os.path.join(d, 'tiles.png'))
        for i in range(16):
            cols = [(0, 0, 0)] + list(pal_slots.get(i, []))
            cols += [(0, 0, 0)] * (16 - len(cols))
            with open(os.path.join(d, 'palettes', f'{i:02d}.pal'), 'w', newline='') as f:
                f.write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join(f'{r} {g} {b}\r\n' for r, g, b in cols))
        open(os.path.join(d, 'metatiles.bin'), 'wb').write(b''.join(struct.pack('<12H', *e) for e, _ in metas))
        open(os.path.join(d, 'metatile_attributes.bin'), 'wb').write(b''.join(struct.pack('<H', a) for _, a in metas))
    P = os.path.join(C, 'data/tilesets/primary/cormoria'); S = os.path.join(C, 'data/tilesets/secondary/pelluca_valley')
    write_ts(P, ptiles, pmeta, {i: slots[i] for i in slots if i < 6}, False)
    write_ts(S, stiles, smeta, {i: slots[i] for i in slots if i >= 6}, True)
    # manifest: how to rebuild each source region from the new metatiles (used by verify)
    man = {'colours_after_merge': ncol, 'primary_palettes': len(ppals), 'secondary_palettes': len(spals),
           'primary_tiles': len(ptiles), 'secondary_tiles': len(stiles),
           'primary_metatiles': len(pmeta), 'secondary_metatiles': len(smeta), 'regions': {}}
    for name, (a, (x0, y0), g) in regions.items():
        man['regions'][name] = {'source_map': hex(a), 'origin': [x0, y0],
                                'grid': [[newid.get(c) if c else None for c in row] for row in g]}
    man['regions']['church'] = {'source': 'Evernahn r17-26 c0-c6', 'grid': [[newid.get(('church', r, c)) for c in CHURCH_COLS] for r in CHURCH_ROWS]}
    json.dump(man, open(os.path.join(S, 'assembly_manifest.json'), 'w'), indent=1)
    print(json.dumps({k: v for k, v in man.items() if k != 'regions'}, indent=1))


if __name__ == '__main__':
    main()
