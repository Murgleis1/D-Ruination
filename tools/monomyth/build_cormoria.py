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
    ('tavern', FE, (38, 40, 43, 47)),   # tavern x37/x44 = town wall
    # guardhouse (FE keep gate 27,12-34,18) DEFERRED with the north gate (user); re-add then.
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
    rare = {i: m for i, m, _ in json.load(open(os.environ.get('WA_RARE', os.path.join(HERE, 'data/wa_rare.json'))))}
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
    wa_png = os.environ.get('WA_RENDER', os.path.join(HERE, '../../assets/monomyth_reference/woodavens.png'))
    wa = np.array(Image.open(wa_png).convert('RGB')).astype(int)
    leaves, _ = ds.leaf_patch(wa)
    mid, top = ds.desnow_building(lay[1], lay[2], (56, 56, 88), protect, 88, 110, facade_leaves=leaves)
    mid = ds.patch_from_above(mid, top, lay[1], lay[2], (62, 64, 96, 83), 16, protect)
    for img in (mid, top):
        for src, dst in PLUM.items():
            img[(img == np.array(src)).all(-1)] = dst
    return (x0, y0, W, H), mid, top


# Roof colours decided by the user 2026-11-15 (roof_colour_options.png); the exact
# ramps are read from roof_ramps.json, never retyped.
SLATE = [(72, 72, 80), (88, 88, 96), (120, 120, 128), (144, 144, 152), (168, 168, 176)]
CHURCH_ROOF = [(64, 56, 80), (80, 72, 112), (112, 96, 152), (152, 128, 192), (192, 168, 224)]
RECOLOUR = {'academy': '1B', 'cadmus_house': '3C', 'residence': '5B'}   # per-cell metatiles (de-shared)
# Residence: ALL Pelluca residences blue (5B). Keeping slate AND blue in one town needs
# one palette more than the GBA has (measured 14/13 even with packing reserved); the
# palette-swap path below stays for a town that can afford it.
RESIDENCE_PALETTE_SWAP = False
CHURCH_RAMP, RESIDENCE_VARIANT = '2B', '5B'           # church + holes patched; residence = palette swap


def _ramps():
    import json
    p = os.path.join(HERE, '../../assets/pelluca_dock_spec/roof_ramps.json')
    return {k: {tuple(a): tuple(b) for a, b in v['map']} for k, v in json.load(open(p)).items()}


def region_layers(a, box):
    x0, y0, x1, y1 = box; W, H = x1 - x0 + 1, y1 - y0 + 1
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
    comp = np.full_like(lay[0], -1)
    for L in lay:
        m = (L >= 0).all(-1); comp[m] = L[m]
    return lay, comp


def church_image(cells):
    H, W = len(CHURCH_ROWS), len(CHURCH_COLS)
    ch = np.full((H * 16, W * 16, 3), -1, int)
    for (r, c), mids in cells.items():
        y, x = (r - CHURCH_ROWS[0]) * 16, c * 16
        for q, m in enumerate(mids):
            oy, ox = y + (q // 2) * 8, x + (q % 2) * 8; k = (m >= 0).all(-1); ch[oy:oy + 8, ox:ox + 8][k] = m[k]
    return ch


def church_finished(cells):
    """Crimson (2B) roof; dark patches enclosed by the roof filled as roof (user)."""
    import roof_mask as rm, roof_recolour as rr
    from scipy import ndimage
    img = church_image(cells); H, W = img.shape[:2]
    roof = rm.roof_mask(img, CHURCH_ROOF, int(H * 0.4))
    lab, n = ndimage.label(~roof); holes = np.zeros_like(roof)
    for i in range(1, n + 1):
        comp = lab == i; ys, xs = np.nonzero(comp)
        if ys.min() == 0 or xs.min() == 0 or ys.max() == H - 1 or xs.max() == W - 1: continue
        ring = ndimage.binary_dilation(comp) & ~comp
        if roof[ring].mean() > 0.85 and comp.sum() < 400: holes |= comp
    out = rr.patch_roof_holes(img, roof, holes)
    return rr.apply(out, roof | holes, _ramps()[CHURCH_RAMP])


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
    cf = church_finished(church)
    for (r, c), mids in church.items():
        y, x = (r - CHURCH_ROWS[0]) * 16, c * 16
        mids = [cf[y + qy:y + qy + 8, x + qx:x + qx + 8] for qy in (0, 8) for qx in (0, 8)]
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
    # ---- roof recolours: per-cell metatiles so shared roof pieces elsewhere keep slate
    import roof_mask as rm, roof_recolour as rr
    ramps = _ramps()
    for name, label in RECOLOUR.items():
        a, box = [(aa, bx) for n, aa, bx in BUILDINGS if n == name][0]
        lay, comp = region_layers(a, box)
        roof = rm.roof_mask(comp, SLATE, int(comp.shape[0] * 0.4))
        new = [rr.apply(L, roof, ramps[label]) for L in lay]
        g = regions[name][2]; x0, y0 = box[0], box[1]
        for cy in range(len(g)):
            for cx in range(len(g[0])):
                if not roof[cy * 16:cy * 16 + 16, cx * 16:cx * 16 + 16].any():
                    continue
                key = ('recol', name, cx, cy)
                e, attr = src_metatile(a, cell(a, x0 + cx, y0 + cy))
                meta_src[('s', key)] = (e, attr)
                for L in range(3):
                    for q in range(4):
                        sub = new[L][cy * 16 + (q // 2) * 8: cy * 16 + (q // 2) * 8 + 8, cx * 16 + (q % 2) * 8: cx * 16 + (q % 2) * 8 + 8]
                        if (sub >= 0).all(-1).any():
                            Q[('s', key, L * 4 + q)] = sub.copy()
                g[cy][cx] = key
    # ---- colour merge (one map over everything)
    allbytes = {im.tobytes() for im in Q.values()}
    cmap, ncol = pp.merge_map(allbytes, TOL)
    def remap(im):
        out = im.copy(); f = out.reshape(-1, 3)
        for k, c in enumerate(map(tuple, f)):
            if c[0] >= 0: f[k] = cmap[c]
        return out
    Q = {k: remap(v) for k, v in Q.items()}
    # Coastal pieces (quay, sandbank) took 3 whole palettes for two small features.
    # A tolerance-24 merge on their sand/stone/foliage tones only (water PROTECTED:
    # the same strength flattened grass before) packs them into 2 -- checked on screen
    # (coastal_merge_check.png) and numerically (0 of 38 water tiles changed).
    co = {k: v for k, v in Q.items() if k[0] == 'p' and k[1][0] in (PG64, OB12)}
    cmap2, _ = pp.merge_map({v.tobytes() for v in co.values()}, 24)
    is_water = lambda c: c[2] > c[0] + 40 and c[2] > c[1] + 8
    for k, v in co.items():
        f = v.copy().reshape(-1, 3)
        for i, c in enumerate(map(tuple, f)):
            if c[0] >= 0 and not is_water(c) and not is_water(cmap2[c]): f[i] = cmap2[c]
        Q[k] = f.reshape(v.shape)
    cs = lambda im: frozenset(map(tuple, im.reshape(-1, 3)[(im.reshape(-1, 3) >= 0).all(1)]))
    # ---- palettes. Measured: Wood Avens terrain packs into 4; the coastal pieces
    # (quay, sandbank) need 3 more. Shared slots 0-5 = WA terrain + as many coastal
    # palettes as fit; remaining coastal palette(s) lead the secondary (6-12):
    # shore colours are regional, provided by each coastal town's secondary.
    def keyset(k): return cs(Q[k])
    if not RESIDENCE_PALETTE_SWAP:
        res_roof_keys, res_roof_mask, RES_PACK, SENT, wall_dups, MS = set(), {}, frozenset(), [], [], set()
    # Residence roof quads must share ONE palette, so the blue residence (palette swap)
    # needs one copy, not one per palette they happened to be packed into.
    import roof_mask as rm
    rbox = [bx for n, _, bx in BUILDINGS if n == 'residence'][0]
    _, rcomp = region_layers(WA, rbox) if RESIDENCE_PALETTE_SWAP else (None, np.zeros((16, 16, 3)))
    rroof = rm.roof_mask(rcomp, SLATE, int(rcomp.shape[0] * 0.4))
    res_roof_keys = set(); res_roof_mask = {}
    MS = {cmap[c] for c in SLATE if c in cmap}       # slate after the colour merge
    rg = regions['residence'][2]
    for cy in range(len(rg)):
        for cx in range(len(rg[0])):
            k = rg[cy][cx]
            if k is None: continue
            kind = 'p' if ('p', k) in meta_src else 's'
            for L in range(3):
                for q in range(4):
                    oy, ox = cy * 16 + (q // 2) * 8, cx * 16 + (q % 2) * 8
                    key3 = (kind, k, L * 4 + q)
                    if key3 not in Q: continue
                    # the QUAD ITSELF must carry slate inside the roof outline: matching by
                    # position alone also caught the grass tiles beneath the eaves (18 colours)
                    img = Q[key3]; mk = rroof[oy:oy + 8, ox:ox + 8]
                    if any(tuple(img[yy, xx]) in MS for yy, xx in zip(*np.nonzero(mk))):
                        res_roof_keys.add(key3); res_roof_mask[key3] = mk.copy()
    RES_U = frozenset().union(*[keyset(k) for k in res_roof_keys])
    wall_dups = []
    for k3 in res_roof_keys:
        img = Q[k3]; mk = res_roof_mask[k3]
        for yy in range(8):
            for xx in range(8):
                c = tuple(img[yy, xx])
                if c[0] >= 0 and c in MS and not mk[yy, xx] and c not in wall_dups:
                    wall_dups.append(c)
    SENT = [(-2, -2, -2 - i) for i in range(len(wall_dups))]   # placeholders: never real colours
    RES_PACK = RES_U | frozenset(SENT)
    print(f'residence roof: {len(res_roof_keys)} quads, {len(RES_U)} colours + {len(wall_dups)} reserved wall-siding slot(s)')
    assert len(RES_PACK) <= 15
    wa_k = [k for k in Q if k[0] == 'p' and k[1][0] == WA]
    co_k = [k for k in Q if k[0] == 'p' and k[1][0] != WA]
    pw = pp.pack_best([keyset(k) for k in wa_k] + [RES_PACK], tries=300)
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
    assert sum(1 for p in ppals for c in p if c in SENT) == len(SENT), 'sentinels spread over palettes'
    slots.update({6 + i: sorted(p, key=lambda c: (0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2])) for i, p in enumerate(spals)})
    res_slot = next(i for i in sorted(slots) if RES_U <= set(slots[i]))
    # Wall siding under the gables uses the SAME grey as the roof slate inside the same
    # 8x8 tiles; a palette swap would turn it blue. Those wall pixels get their own
    # palette entries (same RGB, later index; room reserved during packing) so the
    # blue copy changes roof slots only.
    slots[res_slot] = [c for c in slots[res_slot] if c not in SENT] + wall_dups
    WALL_IDX = {c: len(slots[res_slot]) - len(wall_dups) + i + 1 for i, c in enumerate(wall_dups)}
    assert len(slots[res_slot]) <= 15, f'residence palette {len(slots[res_slot])} > 15'
    print(f'residence palette: {len(slots[res_slot])} colours incl. {len(wall_dups)} wall-siding duplicate(s)')
    def slot_for(im, kind, key=None):
        if key in res_roof_keys:
            return res_slot
        s = cs(im)
        for i in sorted(slots):            # terrain may use a spilled coastal slot (>= 6)
            if s <= set(slots[i]): return i
        raise AssertionError('no palette holds a tile')
    # ---- tiles (dedupe by index pattern incl. flips)
    ptiles = [np.zeros((8, 8), np.uint8)]; stiles = []
    pidx, sidx = {ptiles[0].tobytes(): (0, 0, 0)}, {}
    def to_idx(im, sl, key=None):
        lut = {}
        for i, c in enumerate(slots[sl]):
            lut.setdefault(c, i + 1)              # first occurrence: duplicates are reserved
        mk = res_roof_mask.get(key) if key in res_roof_keys else None
        out = np.zeros((8, 8), np.uint8)
        for y in range(8):
            for x in range(8):
                c = tuple(im[y, x])
                if c[0] < 0: continue
                out[y, x] = WALL_IDX[c] if (mk is not None and c in WALL_IDX and not mk[y, x]) else lut[c]
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
        sl = slot_for(im, k[0], k)
        tile_kind = 'p' if (k[0] == 'p' or k[1] in res_keys) else 's'
        tid, hf, vf = place(to_idx(im, sl, k), tile_kind)
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
    if RESIDENCE_PALETTE_SWAP:
        # ---- residence second colour (5B blue) by PALETTE SWAP: same tiles, roof quads point
        # at a copy of their palette with the (merged) slate entries -> blue at the SAME
        # indices. Costs one palette per distinct roof palette, no tiles.
        blue = ramps[RESIDENCE_VARIANT]
        merged_blue = {}
        for sc in SLATE:
            mc = cmap.get(sc)
            if mc is not None and mc not in merged_blue: merged_blue[mc] = blue[sc]
        rbox = [bx for n, _, bx in BUILDINGS if n == 'residence'][0]
        _, rcomp = region_layers(WA, rbox)
        rroof = rm.roof_mask(rcomp, SLATE, int(rcomp.shape[0] * 0.4))
        variant, next_slot = {}, 6 + len(spals)
        g = regions['residence'][2]; bg = []
        for cy in range(len(g)):
            bg.append([])
            for cx in range(len(g[0])):
                k = g[cy][cx]
                if k is None: bg[-1].append(None); continue
                kind = 'p' if ('p', k) in meta_src else 's'
                e = [entries.get((kind, k, i), 0) for i in range(12)]
                for L in range(3):
                    for q in range(4):
                        v = e[L * 4 + q]
                        if not v: continue
                        if (kind, k, L * 4 + q) not in res_roof_keys: continue   # same set the packer used
                        sl = v >> 12
                        if sl not in variant:
                            variant[sl] = next_slot; next_slot += 1
                            seen_c = set(); newp = []
                            for c in slots[sl]:
                                newp.append(merged_blue.get(c, c) if c not in seen_c else c)  # duplicates = wall: keep
                                seen_c.add(c)
                            slots[variant[sl]] = newp
                        e[L * 4 + q] = (v & 0x0FFF) | (variant[sl] << 12)
                key = ('resblue', cx, cy)
                src_attr = meta_src[(kind, k)][1]
                attr = (src_attr & 0xFF) | ((0 if any(e[8:12]) else 1) << 12)
                newid[key] = 512 + len(smeta); smeta.append((e, attr)); bg[-1].append(key)
        regions['residence_blue'] = (WA, (rbox[0], rbox[1]), bg)
        print(f'residence blue: {len(variant)} variant palette(s) -> slots {sorted(variant.values())}; total secondary slots used {next_slot - 6}/7')
        assert next_slot <= 13, f'palette slots exceeded: {next_slot}'
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
