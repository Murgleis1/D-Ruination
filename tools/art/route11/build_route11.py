"""Build Route 11 in the game from the composer (route11_v2.py): its own secondary tileset under Pelluca's primary
(gTileset_Cormoria), the layout, the map, its connection with Pelluca Valley.

Why Pelluca's primary: a connected map is drawn with the tilesets of the map the player stands in, so the columns of
each map the other can see (Route 11's 82-89, Pelluca's 0-7) are Pelluca's own primary metatiles on both sides.

The tiles:
  * a cell that is one of Pelluca's metatiles as it stands (its grass, pines, cobbles, sand, sea) is that metatile;
  * every other cell is a new metatile, its bottom layer the cell's ground and pieces, its top layer the pieces the
    player walks behind (tree crowns); each 8x8 tile reuses one of Pelluca's tiles if the same picture is there,
    takes one of Pelluca's six palettes if its colours are all in one, else goes into Route 11's seven;
  * Route 11's seven palettes are one per kind of thing (grass, broadleaf woods, farm, cottage, bridge, cliffs, river
    and the pines on sage); each kind's colours are merged, nearest and rarest first, until its palette holds them.
Collision and behaviour come from what the composer put in each cell (route11_v2 tags).

Usage: python3 tools/art/route11/build_route11.py [--dry]   (then make; tools/render_layout.py to look)
"""
import os, sys, json, struct, random, collections
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'academy'))
import route11_v2 as R, kit, imgtiles as IT
from kit import RL

C = RL.C
NAME, LAYOUT, MAPID = 'Route11', 'LAYOUT_ROUTE11', 'MAP_ROUTE11'
TSDIR, TSNAME = 'route11', 'Route11'
GROUPS = (('G', ('', 'road', 'tall', 'flower', 'sea')), ('T', ('tree', 'canopy', 'tuft')), ('F', ('farm',)),
          ('H', ('house',)), ('B', ('bridge',)), ('C', ('cliff', 'stairs')), ('W', ('water', 'stream', 'ptree', 'pcanopy')))   # (W: the river's blues and Pelluca's pines on sage)

MB_NORMAL, MB_TALL_GRASS, MB_POND_WATER, MB_SAND, MB_ROCK_STAIRS = 0x00, 0x02, 0x10, 0x21, 0x4F
WALK, SOLID, WATER = 3 << 2, 1 | 3 << 2, 1 << 2          # collision | elevation << 2

def q5(img): return (img >> 3) << 3

# ------------------------------------------------------------------ Pelluca's primary
_cor = kit._cor
PPAL = [[tuple(int(v) >> 3 << 3 for v in c) for c in _cor.pal[i]] for i in range(6)]
PTILES = [_cor.pt[i] for i in range(512)]
def _pelluca_collision():
    g = np.fromfile(os.path.join(C, 'data/layouts/PellucaCity/map.bin'), '<u2')
    d = collections.defaultdict(collections.Counter)
    for v in g: d[int(v) & 0x3FF][int(v) >> 10] += 1
    return {m: c.most_common(1)[0][0] for m, c in d.items()}
PCOL = _pelluca_collision()

# ------------------------------------------------------------------ what each cell is
def classify(M):
    """-> grid of (primary id or None), collision byte, behaviour."""
    H, W = R.H, R.W
    prim = [[M.primary(x, y) for x in range(W)] for y in range(H)]
    col = np.zeros((H, W), int); beh = np.zeros((H, W), int)
    for y in range(H):
        for x in range(W):
            u = M.used[y, x] or ''; tag = u.split(':')[0]; g = M.ground[y][x]
            p = prim[y][x]
            if p is not None and tag not in ('canopy', 'pcanopy'):
                col[y, x] = PCOL.get(p, SOLID); continue
            if tag in ('', 'road', 'flower', 'tuft', 'canopy', 'pcanopy', 'tall', 'stairs'):
                c = WALK
                if (x, y) in M.wet and M.wet[(x, y)]: c = WATER
            elif tag == 'bridge': c = WALK if y == R.ROAD + 1 else SOLID
            elif tag == 'stream': c = WATER
            elif tag == 'sea':
                if isinstance(g, tuple) and g[0] == 'cor' and not M.over[y][x]: c = PCOL.get(g[1], WATER)
                else: c = WATER if M.wet.get((x, y), True) else WALK
            else: c = SOLID
            if p is not None and tag in ('canopy', 'pcanopy'): c = PCOL.get(p, WALK)
            col[y, x] = c
            if tag == 'tall': beh[y, x] = MB_TALL_GRASS
            elif tag == 'stairs': beh[y, x] = MB_ROCK_STAIRS
            elif c == WATER: beh[y, x] = MB_POND_WATER
            elif c == WALK and (g == 'sand' or (isinstance(g, tuple) and g[0] == 'img')): beh[y, x] = MB_SAND
    return prim, col, beh

# ------------------------------------------------------------------ the tiles
def build(M, dry=False):
    H, W = R.H, R.W
    prim, col, beh = classify(M)
    own = [(x, y) for y in range(H) for x in range(W) if prim[y][x] is None]
    U = {}; O = {}; OM = {}
    for x, y in own:
        u, o, m = M.layers(x, y); U[(x, y)] = q5(u); O[(x, y)] = q5(o); OM[(x, y)] = m
    def tiles_of(rgb, mask=None):
        for q in range(4):
            yy, xx = (q // 2) * 8, (q % 2) * 8
            t = rgb[yy:yy + 8, xx:xx + 8]; mk = None if mask is None else mask[yy:yy + 8, xx:xx + 8]
            if mk is not None and not mk.any(): yield q, None, None; continue
            yield q, t, mk
    def cset(t, mk): return frozenset(map(tuple, (t[mk] if mk is not None else t.reshape(-1, 3)).tolist()))
    psets = [set(p[1:]) for p in PPAL]
    def fits_primary(s): return [i for i, p in enumerate(psets) if s <= p]
    # Route 11's seven palettes, one for each kind of thing: G grass (the four shades, the dirt road, the tall grass),
    # T Crown's broadleaf woods, F the farm, H the cottage (and hay), B the bridge, C the cliffs, W the river in the
    # chasm and Pelluca's pines on sage.
    # A tile whose colours are all in one of Pelluca's palettes uses that palette instead. Each kind's colours (its
    # pieces come from four games, each shaded its own way) are merged, nearest and rarest first, until its palette
    # holds them; the grass shades themselves never move.
    shades = {tuple(v >> 3 << 3 for v in c) for sh in kit.SHADES for c in sh}
    def group(k):
        if M.used[k[1], k[0]] == 'farm:hay': return 'H'         # (the hay's yellows with the cottage's thatch)
        t = (M.used[k[1], k[0]] or '').split(':')[0]
        for g, tags in GROUPS:
            if t in tags: return g
        return 'G'
    by = collections.defaultdict(list)
    for k in own: by[group(k)].append(k)
    pals, merges = [], 0
    for g, _ in GROUPS:
        cells = by.get(g, [])
        def need():
            cnt = collections.Counter()
            for k in cells:
                for q, t, mk in tiles_of(U[k]):
                    s_ = cset(t, None)
                    if not fits_primary(s_): cnt.update({c: 1 for c in s_})
                for q, t, mk in tiles_of(O[k], OM[k]):
                    if t is not None:
                        s_ = cset(t, mk)
                        if not fits_primary(s_): cnt.update({c: 1 for c in s_})
            return cnt
        cnt = need(); n0 = len(cnt)
        while len(cnt) > 15:
            cols = list(cnt); best = None
            for i, a in enumerate(cols):
                for b_ in cols[i + 1:]:
                    if a in shades and b_ in shades: continue
                    d = sum((p - q) ** 2 for p, q in zip(a, b_)) ** 0.5 * min(cnt[a], cnt[b_]) ** 0.5
                    if a in shades or b_ in shades: d *= 3           # a piece's own colour into the grass: last
                    if best is None or d < best[0]: best = (d, a, b_)
            _, a, b_ = best
            drop, keep = (a, b_) if (a not in shades and (b_ in shades or cnt[a] <= cnt[b_])) else (b_, a)
            if '-v' in sys.argv: print(f'    {g}: {drop} -> {keep}')
            for k in cells:
                for img in (U[k], O[k]):
                    f = img.reshape(-1, 3); f[(f == drop).all(1)] = keep
            merges += 1; cnt = need()
        print(f'  {g}: {len(cells)} cells, {n0} colours -> {len(cnt)}')
        pals.append(set(cnt))
    # palettes: slots 6.. for Route 11's own
    SP = [[(0, 0, 0)] + sorted(p, key=sum) for p in pals]
    merges_total = merges
    allp = PPAL + SP
    pset_all = [set(p[1:]) for p in allp]
    # tiles: Pelluca's (any flip) or new
    pidx = {}
    for i, t in enumerate(PTILES):
        for f, tt in ((0, t), (1, t[:, ::-1]), (2, t[::-1, :]), (3, t[::-1, ::-1])):
            pidx.setdefault(np.ascontiguousarray(tt).tobytes(), (i, f))
    new = [np.zeros((8, 8), np.uint8)]; nidx = {new[0].tobytes(): (0, 0)}
    def add(idx):
        for f, tt in ((0, idx), (1, idx[:, ::-1]), (2, idx[::-1, :]), (3, idx[::-1, ::-1])):
            k = np.ascontiguousarray(tt).tobytes()
            if k in nidx: return 512 + nidx[k][0], nidx[k][1] ^ f
        nidx[idx.tobytes()] = (len(new), 0); new.append(idx.copy()); return 512 + len(new) - 1, 0
    reused = 0
    def entry(t, mk, under):
        nonlocal reused
        s = cset(t, mk)
        slots = [i for i, p in enumerate(pset_all) if s <= p]
        assert slots, 'a tile with no palette'
        for slot in slots:                                   # Pelluca's tile itself, if it is there
            lut = {c: i for i, c in enumerate(allp[slot]) if i}
            idx = np.zeros((8, 8), np.uint8)
            for yy in range(8):
                for xx in range(8):
                    if mk is None or mk[yy, xx]: idx[yy, xx] = lut[tuple(t[yy, xx].tolist())]
            k = idx.tobytes()
            if k in pidx and slot < 6: i, f = pidx[k]; reused += 1; return i | f << 10 | slot << 12
        slot = slots[0]; lut = {c: i for i, c in enumerate(allp[slot]) if i}
        idx = np.zeros((8, 8), np.uint8)
        for yy in range(8):
            for xx in range(8):
                if mk is None or mk[yy, xx]: idx[yy, xx] = lut[tuple(t[yy, xx].tolist())]
        i, f = add(idx); return i | f << 10 | slot << 12
    meta, attrs, mid = [], [], {}
    grid = np.zeros((H, W), np.uint16)
    for y in range(H):
        for x in range(W):
            if prim[y][x] is not None:
                grid[y, x] = prim[y][x] | int(col[y, x]) << 10; continue
            e = [0] * 12
            for q, t, mk in tiles_of(U[(x, y)]): e[q] = entry(t, None, True)
            for q, t, mk in tiles_of(O[(x, y)], OM[(x, y)]):
                if t is not None: e[8 + q] = entry(t, mk, False)
            a = int(beh[y, x])
            k = (tuple(e), a)
            if k not in mid:
                mid[k] = 512 + len(meta); meta.append(e); attrs.append(a)
            grid[y, x] = mid[k] | int(col[y, x]) << 10
    print(f'Route 11: {len(meta)} metatiles, {len(new)} tiles of its own (+{reused} of Pelluca\'s reused), '
          f'{len(SP)} palettes, {merges} colour merges')
    assert len(meta) <= 512 and len(new) <= 512 and len(SP) <= 7
    r = dict(tiles=new, pals=SP, meta=meta, attrs=attrs, grid=grid, U=U, O=O, OM=OM, prim=prim)
    return r

# ------------------------------------------------------------------ writing it
def write(r):
    blank = [(0, 0, 0)] * 16
    pals = [blank] * 6 + [(p + [(0, 0, 0)] * 16)[:16] for p in r['pals']]
    pals += [blank] * (16 - len(pals))
    IT.write_tileset(os.path.join(C, 'data/tilesets/secondary', TSDIR), r['tiles'], pals, r['meta'], r['attrs'], 6)
    d = os.path.join(C, 'data/layouts', NAME); os.makedirs(d, exist_ok=True)
    r['grid'].astype('<u2').tofile(os.path.join(d, 'map.bin'))
    # the border (seen only past the woods): Pelluca's pine forest
    open(os.path.join(d, 'border.bin'), 'wb').write(struct.pack('<4H', *[v | 1 << 10 | 3 << 12 for v in (31, 30, 24, 23)]))
    lj = os.path.join(C, 'data/layouts/layouts.json'); L = json.load(open(lj)); lays = L['layouts']
    entry = {'id': LAYOUT, 'name': NAME + '_Layout', 'width': R.W, 'height': R.H,
             'primary_tileset': 'gTileset_Cormoria', 'secondary_tileset': 'gTileset_' + TSNAME,
             'border_filepath': f'data/layouts/{NAME}/border.bin', 'blockdata_filepath': f'data/layouts/{NAME}/map.bin'}
    old = [i for i, l in enumerate(lays) if l.get('id') == LAYOUT]
    if old: lays[old[0]] = entry
    else: lays.insert([i for i, l in enumerate(lays) if l.get('id') == 'LAYOUT_PELLUCA_CITY'][0] + 1, entry)
    json.dump(L, open(lj, 'w'), indent=2); open(lj, 'a').write('\n')
    IT.register_tilesets([('secondary', TSDIR, TSNAME)])

MUSIC = 'MUS_ROUTE104'          # a placeholder until the user picks (kept from map.json once set)
GATE_TEXT = {
    'church': "Cadmus told me to meet him at the church.\pI shouldn't leave the Valley yet.",
    'early': "I still have things to take care of here in the Valley.\pI shouldn't leave just yet.",
}

def write_map():
    """Route 11's map (no people yet: stage 2), its connection with Pelluca Valley both ways, and the story gate at
    Pelluca's west road (bible 20: leaving the Valley is stopped until the story sends the player west)."""
    md = os.path.join(C, 'data/maps', NAME); os.makedirs(md, exist_ok=True)
    mapj = {'id': MAPID, 'name': NAME, 'layout': LAYOUT, 'music': MUSIC, 'region_map_section': 'MAPSEC_DR_ROUTE_11',
            'requires_flash': False, 'weather': 'WEATHER_NONE', 'map_type': 'MAP_TYPE_ROUTE', 'allow_cycling': True,
            'allow_escaping': False, 'allow_running': True, 'show_map_name': True,
            'battle_scene': 'MAP_BATTLE_SCENE_NORMAL',
            'connections': [{'map': 'MAP_PELLUCA_CITY', 'offset': -R.PEL, 'direction': 'right'}],
            'object_events': [], 'warp_events': [], 'coord_events': [], 'bg_events': []}
    old = os.path.join(md, 'map.json')
    if os.path.exists(old):                                  # (keep whatever events later stages have added)
        prev = json.load(open(old))
        for k in ('object_events', 'warp_events', 'coord_events', 'bg_events'): mapj[k] = prev.get(k, [])
        mapj['music'] = prev.get('music', MUSIC)
    json.dump(mapj, open(old, 'w'), indent=2); open(old, 'a').write('\n')
    sp = os.path.join(md, 'scripts.pory')
    if not os.path.exists(sp): open(sp, 'w').write('mapscripts Route11_MapScripts {}\n')
    IT._add('data/event_scripts.s', '\t.include "data/maps/PellucaIcePath/scripts.inc"\n', '\t.include "data/maps/Route11/scripts.inc"\n')
    gj = os.path.join(C, 'data/maps/map_groups.json'); G = json.load(open(gj))
    if NAME not in G['gMapGroup_Phase3']:
        G['gMapGroup_Phase3'].append(NAME); json.dump(G, open(gj, 'w'), indent=2); open(gj, 'a').write('\n')
    # Pelluca: the connection back, and the gate on its west road (its column 0, the road's three rows)
    pj = os.path.join(C, 'data/maps/PellucaCity/map.json'); P = json.load(open(pj))
    P['connections'] = [c for c in (P.get('connections') or []) if c['map'] != MAPID] + \
        [{'map': MAPID, 'offset': R.PEL, 'direction': 'left'}]
    P['coord_events'] = [c for c in P['coord_events'] if c.get('script') != 'PellucaCity_EventScript_DrWestGate'] + \
        [{'type': 'trigger', 'x': 0, 'y': 28 + i, 'elevation': 0, 'var': 'VAR_TEMP_1', 'var_value': '0',
          'script': 'PellucaCity_EventScript_DrWestGate'} for i in range(3)]
    json.dump(P, open(pj, 'w'), indent=2); open(pj, 'a').write('\n')
    pp = os.path.join(C, 'data/maps/PellucaCity/scripts.pory'); t = open(pp).read()
    i = t.find('// DR: the west gate')
    if i >= 0: t = t[:i].rstrip('\n') + '\n'
    t += f'''
// DR: the west gate (tools/art/route11/build_route11.py). Leaving the Valley for Route 11 is stopped until the story
// sends Osrid west (bible 20). For now the way opens once the shrine under the church is awakened; stage 4 (the
// main story) puts the real condition here.
script PellucaCity_EventScript_DrWestGate {{
    if (flag(FLAG_DR_STATUE_AWAKENED)) {{
        setvar(VAR_TEMP_1, 1)
        end
    }}
    lockall
    showportrait(PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL)
    special(DrSetPrinceNameplate)
    if (flag(FLAG_DR_CHURCH_BLASTED)) {{
        msgbox(format("{GATE_TEXT['church']}"))
    }} else {{
        msgbox(format("{GATE_TEXT['early']}"))
    }}
    hideportrait
    closemessage
    applymovement(OBJ_EVENT_ID_PLAYER, PellucaCity_Movement_DrWestGateBack)
    waitmovement(0)
    releaseall
}}

movement PellucaCity_Movement_DrWestGateBack {{
    walk_right
}}
'''
    open(pp, 'w').write(t)

def render_check(r):
    """Draw the built map back from its tiles and compare with the composer's (colour-merged) picture."""
    H, W = R.H, R.W; out = np.zeros((H * 16, W * 16, 3), np.uint8)
    allp = PPAL + r['pals']
    def tile(v):
        i = v & 0x3FF; t = PTILES[i] if i < 512 else r['tiles'][i - 512]
        if v & 0x400: t = t[:, ::-1]
        if v & 0x800: t = t[::-1, :]
        return t, allp[v >> 12] + [(0, 0, 0)] * 16
    bad = 0
    for y in range(H):
        for x in range(W):
            m = int(r['grid'][y, x]) & 0x3FF
            if m < 512: out[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = kit.cor_full(m); continue
            e = r['meta'][m - 512]; cell = np.zeros((16, 16, 3), np.uint8)
            for k, v in enumerate(e):
                if k >= 4 and not v: continue
                t, P = tile(v); P = np.array(P[:16], np.uint8); q = k % 4; yy, xx = (q // 2) * 8, (q % 2) * 8
                mk = t != 0 if k >= 4 else np.ones((8, 8), bool)
                cell[yy:yy + 8, xx:xx + 8][mk] = P[t][mk]
            ref = r['U'][(x, y)].copy(); ref[r['OM'][(x, y)]] = r['O'][(x, y)][r['OM'][(x, y)]]
            bad += int((cell != ref).any(-1).sum())
            out[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cell
    return out, bad

def main():
    M = R.compose(); r = build(M)
    img, bad = render_check(r)
    Image.fromarray(img).save('/home/claude/scratch/route11/route11_built.png')
    print(f'render check: {bad} pixels differ from the picture')
    if '--dry' in sys.argv: return
    write(r); write_map(); print('written')

if __name__ == '__main__':
    main()
