"""Build Hollow Hill in the game from its composer (hh_mock.py, mock v8 approved by the user 2026-11-20): its own
secondary tileset under Pelluca's primary (gTileset_Cormoria, as Route 11), the layout, the map, its connection with
Route 11.

The seam: a connected map is drawn with the tilesets of the map the player stands in. Hollow Hill's columns 58-65 are
Route 11's own columns 1-8 (the same blocks), and Route 11's columns 0-8 use a few of Route 11's own metatiles; so
Hollow Hill's tileset holds those metatiles at the same ids, with the same tiles at the same tile numbers and Route
11's two palettes they use (its grass, slot 6, and its broadleaf woods, slot 7) in the same slots. Everything else is
Hollow Hill's own, round them.

The tiles: every cell not of the seam is a new metatile, its bottom layer the cell's ground, cliffs, pieces and blood,
its top layer what the player walks behind or under (tree crowns, the webs). Each 8x8 tile reuses Pelluca's or the
seam's if the same picture is there, takes an existing palette if its colours are all in one, else goes into one of
Hollow Hill's five: G the woods' floor (bone, the shades toward Route 11's olive, tall grass, weeds), T the pines,
dead trees, stumps and logs, S the cliffs, stairs, blood, rocks, slabs and burrows, C Crown's woods paled toward the
bone, D the sealed door and the red mushrooms. Each kind's colours are merged, nearest and rarest first, to fifteen.

Usage: python3 tools/art/hollowhill/build_hollowhill.py [--dry]   (then make)
"""
import os, sys, json, struct, collections
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'academy')); sys.path.insert(0, os.path.join(HERE, '..', 'route11'))
import hh_mock as HM, kit, imgtiles as IT
from kit import RL

C = RL.C
NAME, LAYOUT, MAPID = 'HollowHill', 'LAYOUT_HOLLOW_HILL', 'MAP_HOLLOW_HILL'
TSDIR, TSNAME = 'hollow_hill', 'HollowHill'
GROUPS = ('G', 'T', 'S', 'C', 'D')
MB_NORMAL, MB_TALL_GRASS, MB_ROCK_STAIRS = 0x00, 0x02, 0x4F
WALK, SOLID = 3 << 2, 1 | 3 << 2
W, H = HM.W, HM.H

def q5(img): return (img >> 3) << 3

# ------------------------------------------------------------------ Pelluca's primary, Route 11's tileset
_cor = kit._cor
PPAL = [[tuple(int(v) >> 3 << 3 for v in c) for c in _cor.pal[i]] for i in range(6)]
PTILES = [_cor.pt[i] for i in range(512)]
R11 = os.path.join(C, 'data/tilesets/secondary/route11')
def _read_pal(p):
    L = open(p).read().split('\n')[3:19]
    return [tuple(int(v) >> 3 << 3 for v in l.split()) for l in L]
R11PAL = [_read_pal(os.path.join(R11, 'palettes', f'{i:02d}.pal')) for i in range(16)]
_sheet = np.array(Image.open(os.path.join(R11, 'tiles.png')))
R11TILES = [_sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8].copy() for i in range(_sheet.shape[0] // 8 * 16)]
_mt = open(os.path.join(R11, 'metatiles.bin'), 'rb').read()
R11META = [list(struct.unpack('<12H', _mt[i * 24:i * 24 + 24])) for i in range(len(_mt) // 24)]
_at = open(os.path.join(R11, 'metatile_attributes.bin'), 'rb').read()
R11ATTR = list(struct.unpack('<%dH' % (len(_at) // 2), _at))
SEAM_SLOTS = (6, 7)

# ------------------------------------------------------------------ what each cell is
def classify(M):
    col = np.zeros((H, W), int); beh = np.zeros((H, W), int); grp = {}
    for y in range(H):
        for x in range(W):
            if (x, y) in M.seam: continue
            u = M.used[y, x] or ''; tag = u.split(':')[0]
            top = any(t for _, t in M.over[y][x])
            if (x, y) in M.face:
                v = abs(M.face[x, y])
                if u == 'stairs': c, b = WALK, MB_ROCK_STAIRS
                else: c, b = SOLID, MB_NORMAL
                g = 'D' if u == 'door' else 'S'
            elif tag in ('', 'road', 'soft'):
                c = WALK; b = MB_TALL_GRASS if u == 'soft:grass' else MB_NORMAL
                g = 'D' if u == 'soft:mush' else 'S' if u == 'soft:slab' else 'G'
            elif tag in ('woods', 'tree'):
                c = WALK if top else SOLID; b = MB_NORMAL       # (a crown's row: walked behind)
                g = 'C' if (tag == 'woods' and x >= 54) or u.startswith('tree:broad') else 'T'
            elif tag == 'thing':
                c, b = SOLID, MB_NORMAL
                g = 'S' if u in ('thing:rock', 'thing:burrow') else 'T'
            else:
                c, b, g = SOLID, MB_NORMAL, 'S'
            col[y, x] = c; beh[y, x] = b; grp[x, y] = g
    return col, beh, grp

# ------------------------------------------------------------------ the tiles
def build(M):
    col, beh, grp = classify(M)
    Uf, Of, OMf = HM.layers(M)
    U, O, OM = {}, {}, {}
    own = sorted(grp, key=lambda k: (k[1], k[0]))
    for x, y in own:
        sl = (slice(y * 16, y * 16 + 16), slice(x * 16, x * 16 + 16))
        U[x, y] = q5(Uf[sl].copy()); O[x, y] = q5(Of[sl].copy()); OM[x, y] = OMf[sl].copy()
    # the seam's reserved metatiles, tiles and palettes
    rmeta = sorted({v & 0x3FF for v in M.seam.values() if v & 0x3FF >= 512})
    # (and every Route 11 metatile its own columns 0-8 use, which Hollow Hill shows of Route 11)
    r11 = struct.unpack('<%dH' % (90 * 40), open(os.path.join(C, 'data/layouts/Route11/map.bin'), 'rb').read())
    rmeta = sorted(set(rmeta) | {r11[y * 90 + x] & 0x3FF for y in range(40) for x in range(9) if r11[y * 90 + x] & 0x3FF >= 512})
    rtiles = sorted({v & 0x3FF for m in rmeta for k, v in enumerate(R11META[m - 512]) if (k < 4 or v) and v & 0x3FF >= 512})
    rslots = sorted({v >> 12 for m in rmeta for k, v in enumerate(R11META[m - 512]) if k < 4 or v})
    assert set(rslots) <= set(range(6)) | set(SEAM_SLOTS), rslots
    print(f'seam: {len(rmeta)} of Route 11\'s metatiles, {len(rtiles)} tiles, palettes {rslots}')

    def tiles_of(rgb, mask=None):
        for q in range(4):
            yy, xx = (q // 2) * 8, (q % 2) * 8
            t = rgb[yy:yy + 8, xx:xx + 8]; mk = None if mask is None else mask[yy:yy + 8, xx:xx + 8]
            if mk is not None and not mk.any(): yield q, None, None; continue
            yield q, t, mk
    def cset(t, mk): return frozenset(map(tuple, (t[mk] if mk is not None else t.reshape(-1, 3)).tolist()))
    fixed = PPAL + [R11PAL[s] for s in SEAM_SLOTS]                       # slots 0-5, 6, 7
    fsets = [set(p[1:]) for p in fixed]
    def fits_fixed(s): return any(s <= p for p in fsets)
    by = collections.defaultdict(list)
    for k in own: by[grp[k]].append(k)
    pals, merges = [], 0
    for g in GROUPS:
        cells = by.get(g, [])
        def need():
            cnt = collections.Counter()
            for k in cells:
                for q, t, mk in tiles_of(U[k]):
                    s_ = cset(t, None)
                    if not fits_fixed(s_): cnt.update({c: 1 for c in s_})
                for q, t, mk in tiles_of(O[k], OM[k]):
                    if t is not None:
                        s_ = cset(t, mk)
                        if not fits_fixed(s_): cnt.update({c: 1 for c in s_})
            return cnt
        cnt = need(); n0 = len(cnt)
        while len(cnt) > 15:
            cols = list(cnt); best = None
            for i, a in enumerate(cols):
                for b_ in cols[i + 1:]:
                    d = sum((p - q) ** 2 for p, q in zip(a, b_)) ** 0.5 * min(cnt[a], cnt[b_]) ** 0.5
                    if best is None or d < best[0]: best = (d, a, b_)
            _, a, b_ = best
            drop, keep = (a, b_) if cnt[a] <= cnt[b_] else (b_, a)
            if '-v' in sys.argv: print(f'    {g}: {drop} -> {keep}')
            for k in cells:
                for img in (U[k], O[k]):
                    f = img.reshape(-1, 3); f[(f == drop).all(1)] = keep
            merges += 1; cnt = need()
        print(f'  {g}: {len(cells)} cells, {n0} colours -> {len(cnt)}')
        pals.append(set(cnt))
    SP = [[(0, 0, 0)] + sorted(p, key=sum) for p in pals]
    assert len(SP) <= 5
    allp = fixed + SP                                                     # slots 0-12
    pset_all = [set(p[1:]) for p in allp]
    # tiles: Pelluca's or the seam's (any flip), or new ones in the free tile numbers
    tiles = {i: R11TILES[i - 512] for i in rtiles}
    pidx = {}
    for i, t in enumerate(PTILES):
        for f, tt in ((0, t), (1, t[:, ::-1]), (2, t[::-1, :]), (3, t[::-1, ::-1])):
            pidx.setdefault((np.ascontiguousarray(tt).tobytes(), 'p'), (i, f))
    nidx = {}
    def index_tile(i, t, slot_ok):
        for f, tt in ((0, t), (1, t[:, ::-1]), (2, t[::-1, :]), (3, t[::-1, ::-1])):
            nidx.setdefault(np.ascontiguousarray(tt).tobytes(), (i, f))
    for i in rtiles: index_tile(i, tiles[i], None)
    free_t = [i for i in range(512, 1024) if i not in tiles]
    def add(idx):
        k = np.ascontiguousarray(idx).tobytes()
        if k in nidx: return nidx[k]
        if not free_t:
            assert '--dry' in sys.argv, 'out of tile numbers'
            add.over = getattr(add, 'over', 0) + 1; free_t.append(2000 + add.over)   # (a dry run counts how far over)
        i = free_t.pop(0); tiles[i] = idx.copy(); index_tile(i, idx, None); return nidx[k]
    if 512 not in tiles: tiles[512] = np.zeros((8, 8), np.uint8); index_tile(512, tiles[512], None); free_t.remove(512)
    reused = 0
    def entry(t, mk):
        nonlocal reused
        s = cset(t, mk)
        slots = [i for i, p in enumerate(pset_all) if s <= p]
        assert slots, ('a tile with no palette', s)
        best = None
        for slot in slots:
            lut = {c: i for i, c in enumerate(allp[slot]) if i}
            idx = np.zeros((8, 8), np.uint8)
            for yy in range(8):
                for xx in range(8):
                    if mk is None or mk[yy, xx]: idx[yy, xx] = lut[tuple(t[yy, xx].tolist())]
            k = idx.tobytes()
            if slot < 6 and (k, 'p') in pidx: i, f = pidx[(k, 'p')]; reused += 1; return i | f << 10 | slot << 12
            if k in nidx: i, f = nidx[k]; return i | f << 10 | slot << 12
            if best is None: best = (slot, idx)
        slot, idx = best
        i, f = add(idx); return i | f << 10 | slot << 12
    meta = {m: R11META[m - 512] for m in rmeta}; attrs = {m: R11ATTR[m - 512] for m in rmeta}
    free_m = [m for m in range(512, 1024) if m not in meta]
    mid = {}
    grid = np.zeros((H, W), np.uint16)
    for (x, y), v in M.seam.items(): grid[y, x] = v
    for x, y in own:
        e = [0] * 12
        for q, t, mk in tiles_of(U[x, y]): e[q] = entry(t, None)
        for q, t, mk in tiles_of(O[x, y], OM[x, y]):
            if t is not None: e[8 + q] = entry(t, mk)
        a = int(beh[y, x]); k = (tuple(e), a)
        if k not in mid:
            assert free_m, 'out of metatiles'
            m = free_m.pop(0); mid[k] = m; meta[m] = e; attrs[m] = a
        grid[y, x] = mid[k] | int(col[y, x]) << 10
    n_tiles = max(tiles) - 511; n_meta = max(meta) - 511
    print(f'Hollow Hill: {len(mid)} metatiles of its own (+{len(rmeta)} of Route 11\'s), {len(tiles) - len(rtiles)} tiles '
          f'of its own (+{reused} of Pelluca\'s reused), {len(SP)} palettes, {merges} colour merges; '
          f'tile numbers used to {511 + n_tiles}, metatile ids to {511 + n_meta}')
    return dict(tiles=tiles, pals=SP, meta=meta, attrs=attrs, grid=grid, U=U, O=O, OM=OM, n_tiles=n_tiles, n_meta=n_meta,
                allp=allp)

# ------------------------------------------------------------------ writing it
def write(r):
    blank = [(0, 0, 0)] * 16
    pals = [blank] * 6 + [R11PAL[s] for s in SEAM_SLOTS] + [(p + [(0, 0, 0)] * 16)[:16] for p in r['pals']]
    pals += [blank] * (16 - len(pals))
    tl = [r['tiles'].get(512 + i, np.zeros((8, 8), np.uint8)) for i in range(r['n_tiles'])]
    ml = [r['meta'].get(512 + i, [0] * 12) for i in range(r['n_meta'])]
    al = [r['attrs'].get(512 + i, 0) for i in range(r['n_meta'])]
    IT.write_tileset(os.path.join(C, 'data/tilesets/secondary', TSDIR), tl, pals, ml, al, 8)
    d = os.path.join(C, 'data/layouts', NAME); os.makedirs(d, exist_ok=True)
    r['grid'].astype('<u2').tofile(os.path.join(d, 'map.bin'))
    # the border (past the map's edge, seen only beyond the woods): the bone pines' wall, as at the west edge
    g = r['grid']; wall = [int(g[10, 0]) & 0x3FF, int(g[10, 1]) & 0x3FF, int(g[11, 0]) & 0x3FF, int(g[11, 1]) & 0x3FF]
    open(os.path.join(d, 'border.bin'), 'wb').write(struct.pack('<4H', *[v | 1 << 10 | 3 << 12 for v in wall]))
    lj = os.path.join(C, 'data/layouts/layouts.json'); L = json.load(open(lj)); lays = L['layouts']
    entry = {'id': LAYOUT, 'name': NAME + '_Layout', 'width': W, 'height': H,
             'primary_tileset': 'gTileset_Cormoria', 'secondary_tileset': 'gTileset_' + TSNAME,
             'border_filepath': f'data/layouts/{NAME}/border.bin', 'blockdata_filepath': f'data/layouts/{NAME}/map.bin'}
    old = [i for i, l in enumerate(lays) if l.get('id') == LAYOUT]
    if old: lays[old[0]] = entry
    else: lays.insert([i for i, l in enumerate(lays) if l.get('id') == 'LAYOUT_ROUTE11'][0] + 1, entry)
    json.dump(L, open(lj, 'w'), indent=2); open(lj, 'a').write('\n')
    IT.register_tilesets([('secondary', TSDIR, TSNAME)])

MUSIC = 'MUS_DR_HOLLOW_HILL'

def write_map():
    """Hollow Hill's map (no people yet: stage 2), its connection with Route 11 both ways. The way north to Mirroh
    runs off the top edge: no map there yet (the Mirroh area is next)."""
    md = os.path.join(C, 'data/maps', NAME); os.makedirs(md, exist_ok=True)
    mapj = {'id': MAPID, 'name': NAME, 'layout': LAYOUT, 'music': MUSIC, 'region_map_section': 'MAPSEC_DR_HOLLOW_HILL',
            'requires_flash': False, 'weather': 'WEATHER_FOG_HORIZONTAL', 'map_type': 'MAP_TYPE_ROUTE', 'allow_cycling': True,
            'allow_escaping': False, 'allow_running': True, 'show_map_name': True,
            'battle_scene': 'MAP_BATTLE_SCENE_NORMAL',
            'connections': [{'map': 'MAP_ROUTE11', 'offset': HM.OFF, 'direction': 'right'}],
            'object_events': [], 'warp_events': [], 'coord_events': [], 'bg_events': []}
    old = os.path.join(md, 'map.json')
    if os.path.exists(old):
        prev = json.load(open(old))
        for k in ('object_events', 'warp_events', 'coord_events', 'bg_events'): mapj[k] = prev.get(k, [])
    json.dump(mapj, open(old, 'w'), indent=2); open(old, 'a').write('\n')
    sp = os.path.join(md, 'scripts.pory')
    if not os.path.exists(sp): open(sp, 'w').write('mapscripts HollowHill_MapScripts {}\n')
    IT._add('data/event_scripts.s', '\t.include "data/maps/Route11/scripts.inc"\n', '\t.include "data/maps/HollowHill/scripts.inc"\n')
    gj = os.path.join(C, 'data/maps/map_groups.json'); G = json.load(open(gj))
    if NAME not in G['gMapGroup_Phase3']:
        G['gMapGroup_Phase3'].insert(G['gMapGroup_Phase3'].index('Route11') + 1, NAME)
        json.dump(G, open(gj, 'w'), indent=2); open(gj, 'a').write('\n')
    rj = os.path.join(C, 'data/maps/Route11/map.json'); R = json.load(open(rj))
    R['connections'] = [c for c in (R.get('connections') or []) if c['map'] != MAPID] + \
        [{'map': MAPID, 'offset': -HM.OFF, 'direction': 'left'}]
    json.dump(R, open(rj, 'w'), indent=2); open(rj, 'a').write('\n')

def render_check(r):
    out = np.zeros((H * 16, W * 16, 3), np.uint8); allp = r['allp']
    R11TS = RL.TS('LAYOUT_ROUTE11')
    def tile(v):
        i = v & 0x3FF; t = PTILES[i] if i < 512 else r['tiles'][i]
        if v & 0x400: t = t[:, ::-1]
        if v & 0x800: t = t[::-1, :]
        return t, allp[v >> 12] + [(0, 0, 0)] * 16
    bad = 0
    for y in range(H):
        for x in range(W):
            m = int(r['grid'][y, x]) & 0x3FF
            if m < 512: out[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = kit.cor_full(m); continue
            e = r['meta'][m]; cell = np.zeros((16, 16, 3), np.uint8)
            for k, v in enumerate(e):
                if k >= 4 and not v: continue
                t, P = tile(v); P = np.array(P[:16], np.uint8); q = k % 4; yy, xx = (q // 2) * 8, (q % 2) * 8
                mk = t != 0 if k >= 4 else np.ones((8, 8), bool)
                cell[yy:yy + 8, xx:xx + 8][mk] = P[t][mk]
            if (x, y) in r['U']:
                ref = r['U'][x, y].copy(); ref[r['OM'][x, y]] = r['O'][x, y][r['OM'][x, y]]
            else:
                ref = q5(np.asarray(R11TS.metatile(m), np.uint8))
            bad += int((cell != ref).any(-1).sum())
            out[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cell
    return out, bad

def main():
    M = HM.compose(); r = build(M)
    img, bad = render_check(r)
    Image.fromarray(img).save('/home/claude/scratch/hollowhill/hollow_hill_built.png')
    print(f'render check: {bad} pixels differ from the picture')
    if '--dry' in sys.argv: return
    write(r); write_map(); print('written')

if __name__ == '__main__':
    main()
