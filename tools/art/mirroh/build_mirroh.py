"""Build Mirroh into the game from its approved mock (mirroh_v3.py; user 2026-11-21 "This is pretty good").

Mirroh's art is more than one map can hold (about 1150 different 8x8 tiles; the engine's limit is 1024), so it is
three maps (user 2026-11-21: "Split it into Lower Mirroh and Upper Mirroh as two maps"), cut along the terrace
walls, each with its own tileset pair (tools/art/mapbuild.py: the ground on the bottom layer, everything standing
on it on the middle layer):
  * MirrohGate: outside the city, below the south gatehouse (mock rows 49-71). Its bottom eight rows are
    Hollow Hill's own blocks (mirroh_mock.hh_seam), and its tileset holds Hollow Hill's 35 seam metatiles, their 90
    tiles and their four palettes (slots 7, 8, 9, 11) at Hollow Hill's own numbers, so its bottom rows show Hollow
    Hill's woods exactly as Hollow Hill draws them in its own
    picture: Hollow Hill's way north leads up to the gatehouse (Mirroh x = Hollow Hill x + 12). The two are linked
    by a short fade at the way north, not joined edge to edge. When the player crosses a joined edge the engine
    reloads only the second tileset, and Mirroh Gate cannot fit under Hollow Hill's first one (it would need six
    more palettes than are free). The seam rows make the fade look continuous: below the gate the snow gives out
    onto Hollow Hill's floor (mirroh_v3.seam_fade).
  * MirrohLower: the lower town inside the walls (mock rows 34-57 walkable; rows 27-33, the square's foot and its
    wall, drawn as scenery above).
  * MirrohUpper: the square and the sacred terrace (mock rows 0-33 walkable; rows 34-38, the lower town's top,
    drawn as scenery below).
The two stairs between the lower town and the square are short arrow warps between Lower and Upper. The south
gatehouse is a walk-through building: its front door (Gate) and its back (Lower) lead into its hallway
(MirrohSouthGatehouse); the north-west gatehouse's door (Upper) into its own (MirrohNWGatehouse), whose far door
is shut until Mt. Mirroh is built. The skull gate (Upper, top) leads to the Necropolis grounds.
Collision: walls, gate stone, roofs, rocks and every cell with something standing on it are solid; snow, paving,
cobbles, the floors, the stairs and the ice are walked on (the reflecting ice as plain floor).
Usage: python3 tools/art/mirroh/build_mirroh.py   (then make)
"""
import os, sys, json, struct, pickle
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import mapbuild as MB
C = MB.C
MB_NORMAL, MB_NORTH_ARROW_WARP, MB_SOUTH_ARROW_WARP, MB_DOOR = 0x00, 0x64, 0x65, 0x60
WALKABLE = {'snow', 'pave', 'cobble', 'floor', 'snow-floor', 'stairs', 'ice', 'warp', 'gate-in'}
NECRO_MAP = os.environ.get('NECRO_MAP', 'MAP_NECROPOLIS_GROUNDS')

def mock():
    p = '/tmp/mirroh_M.pkl'
    if os.path.exists(p) and os.environ.get('MIRROH_CACHE'): return pickle.load(open(p, 'rb'))
    import mirroh_v3 as V
    M = V.compose(); pickle.dump(M, open(p, 'wb')); return M

def layers(M, y0, y1):
    """The mock's rows y0..y1-1 as (bottom, (mid, alpha))."""
    W = M.g[0].__len__(); H = y1 - y0
    bot = np.zeros((H * 16, W * 16, 3), np.uint8); mid = np.zeros_like(bot); ma = np.zeros((H * 16, W * 16), bool)
    for y in range(y0, y1):
        for x in range(W):
            s = (slice((y - y0) * 16, (y - y0) * 16 + 16), slice(x * 16, x * 16 + 16))
            bot[s] = M.g[y][x]
            for img, a in M.obj[y][x]: mid[s][a] = img[a]; ma[s] |= a
    return bot, (mid, ma)

def walkable(M, y0, y1, rows):
    W = len(M.g[0])
    return {(x, y - y0) for y in range(y0, y1) for x in range(W)
            if y in rows and M.gtag[y, x] in WALKABLE and M.otag[y, x] is None}

def snow_cell(r, M, y0):
    """A plain snow cell's metatile (the map's border: beyond the edges, more snow)."""
    for y in range(r['grid'].shape[0]):
        for x in range(r['grid'].shape[1]):
            if M.gtag[y + y0, x] == 'snow' and M.otag[y + y0, x] is None: return int(r['grid'][y, x] & 0x3FF)

def mapj(mid, name, objs=(), warps=(), coords=(), bgs=(), conns=None, music='MUS_DR_HOLLOW_HILL', show=True):
    return {'id': mid, 'name': name, 'layout': 'LAYOUT_' + mid[4:], 'music': music,
            'region_map_section': 'MAPSEC_MIRROH', 'requires_flash': False, 'weather': 'WEATHER_SNOW',
            'map_type': 'MAP_TYPE_TOWN', 'allow_cycling': True, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': show, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': conns,
            'object_events': list(objs), 'warp_events': list(warps), 'coord_events': list(coords), 'bg_events': list(bgs)}
W3 = lambda x, y, dest, wid: {'x': x, 'y': y, 'elevation': 3, 'dest_map': dest, 'dest_warp_id': str(wid)}

# ------------------------------------------------------------------ Hollow Hill's seam (fixed in Mirroh Gate)
def hh_fixed(y0):
    import mirroh_mock as mm
    hm = np.fromfile(os.path.join(C, 'data/layouts/HollowHill/map.bin'), '<u2').reshape(64, 66)
    hd = os.path.join(C, 'data/tilesets/secondary/hollow_hill')
    mt = open(os.path.join(hd, 'metatiles.bin'), 'rb').read(); at = open(os.path.join(hd, 'metatile_attributes.bin'), 'rb').read()
    sheet = np.array(Image.open(os.path.join(hd, 'tiles.png')))
    def pal(i):
        L = open(os.path.join(hd, 'palettes', '%02d.pal' % i)).read().split('\n')[3:19]
        return [tuple(int(v) for v in l.split()) for l in L]
    ids = {int(v) for v in np.unique(hm[:6] & 0x3FF)}
    cells = {}
    for y in range(mm.SEAM, mm.H):
        r = (mm.H - y) % 2
        for x in range(mm.W):
            hx = x - mm.HHX
            if hx < 0: hx = hx % 2
            v = int(hm[r, hx]); cells[(x, y - y0)] = v; ids.add(v & 0x3FF)
    meta, attrs, tiles, slots = {}, {}, {}, set()
    for i in ids:
        e = list(struct.unpack('<12H', mt[(i - 512) * 24:(i - 512) * 24 + 24])); meta[i] = e
        attrs[i] = struct.unpack('<H', at[(i - 512) * 2:(i - 512) * 2 + 2])[0]
        for v in e:
            t = v & 0x3FF
            if t >= 512: tiles[t] = sheet[((t - 512) // 16) * 8:((t - 512) // 16) * 8 + 8, ((t - 512) % 16) * 8:((t - 512) % 16) * 8 + 8].copy()
            if t: slots.add(v >> 12)
    return dict(cells=cells, meta=meta, attrs=attrs, tiles=tiles, pals={s: pal(s) for s in slots})

# ------------------------------------------------------------------ the three maps
def build_gate(M):
    y0, y1 = 49, 72                                   # (from the gatehouse's roof down: the camera at its door shows no higher)
    bot, mid = layers(M, y0, y1)
    walk = walkable(M, y0, y1, range(y0, 64))
    door = {(30, 55 - y0), (31, 55 - y0)}; walk |= door                 # the south gatehouse's front door
    fx = hh_fixed(y0)
    r = MB.build(bot, mid, None, len(M.g[0]), y1 - y0, walk, lambda x, y: MB_DOOR if (x, y) in door else MB_NORMAL, fixed=fx)
    warps = [W3(x, y, 'MAP_MIRROH_SOUTH_GATEHOUSE', 0) for (x, y) in sorted(door)]
    import mirroh_mock as mm
    # down to Hollow Hill: a short fade from the bottom row of the way (the maps cannot be joined edge to edge:
    # crossing a joined edge the engine reloads only the second tileset, and these maps share neither)
    coords = [{'type': 'trigger', 'x': x, 'y': y1 - y0 - 1, 'elevation': 3, 'var': 'VAR_TEMP_1', 'var_value': '0',
               'script': 'MirrohGate_EventScript_ToHollowHill%d' % (x - mm.HHX)} for x in range(28, 32)]
    j = mapj('MAP_MIRROH_GATE', 'MirrohGate', warps=warps, coords=coords)
    # the border: beyond the map's edges, Hollow Hill's bone wood (user 2026-11-21: past the apron's pinewood the
    # camera showed endless snow, as if the land went on). Its fill repeats every 2x2 cells; the engine takes border
    # block (x & 1) + 2 * (y & 1) for map cell (x, y) (fieldmap.c GetBorderBlockAt, coordinates offset by 7), so the
    # wood beyond the edges runs on in step with the wood in the map.
    gb = r['grid'] & 0x3FF; ye = (gb.shape[0] - 1) & ~1                  # (an even row of the wood, at the bottom)
    wood = [int(gb[ye, 0]), int(gb[ye, 1]), int(gb[ye - 1, 0]), int(gb[ye - 1, 1])]
    edges = (0, 1, gb.shape[1] - 2, gb.shape[1] - 1)                    # (the tree pairs that meet the border)
    assert all(int(gb[y, x]) == wood[(x & 1) + 2 * (y & 1)] for y in range(ye - 7, ye + 1) for x in edges), 'the wood is out of step at an edge'
    MB.write(r, 'MirrohGate', 'LAYOUT_MIRROH_GATE', ('mirroh_gate_tiles', 'MirrohGateTiles'),
             ('mirroh_gate', 'MirrohGate'), j, border=wood)
    open(os.path.join(C, 'data/maps/MirrohGate/scripts.pory'), 'w').write('mapscripts MirrohGate_MapScripts {}\n' + ''.join(
        '\nscript MirrohGate_EventScript_ToHollowHill%d {\n    setvar(VAR_TEMP_1, 1)\n    warp(MAP_HOLLOW_HILL, %d, 1)\n}\n' % (hx, hx) for hx in range(16, 20)))
    return r

def build_lower(M):
    y0, y1 = 27, 58
    bot, mid = layers(M, y0, y1)
    walk = walkable(M, y0, y1, range(34, 51))
    back = {(30, 46 - y0), (31, 46 - y0)}                                # the south gatehouse's back
    up = {(x, 34 - y0) for x in (14, 15, 16, 43, 44, 45)}                # the stairs' tops: up to the square
    beh = lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) in back else MB_NORTH_ARROW_WARP if (x, y) in up else MB_NORMAL
    r = MB.build(bot, mid, None, len(M.g[0]), y1 - y0, walk, beh)
    warps = [W3(x, y, 'MAP_MIRROH_SOUTH_GATEHOUSE', 2) for (x, y) in sorted(back)]
    warps += [W3(x, y, 'MAP_MIRROH_UPPER', 2 + i) for i, (x, y) in enumerate(sorted(up))]
    j = mapj('MAP_MIRROH_LOWER', 'MirrohLower', warps=warps)
    s = snow_cell(r, M, y0)
    MB.write(r, 'MirrohLower', 'LAYOUT_MIRROH_LOWER', ('mirroh_lower_tiles', 'MirrohLowerTiles'), ('mirroh_lower', 'MirrohLower'), j, border=[s] * 4)
    return r

def build_upper(M):
    y0, y1 = 0, 39
    bot, mid = layers(M, y0, y1)
    walk = walkable(M, y0, y1, range(0, 34))
    nw = {(13, 10), (14, 10)}                 # (the gate's last row, as the south one's)
    necro = {(43, 9), (44, 9), (45, 9)}; walk |= nw | necro
    down = {(x, 33) for x in (14, 15, 16, 43, 44, 45)}
    beh = lambda x, y: MB_DOOR if (x, y) in nw | necro else MB_SOUTH_ARROW_WARP if (x, y) in down else MB_NORMAL
    r = MB.build(bot, mid, None, len(M.g[0]), y1 - y0, walk, beh)
    warps = [W3(x, y, 'MAP_MIRROH_NW_GATEHOUSE', 0) for (x, y) in sorted(nw)]
    warps += [W3(x, y, 'MAP_MIRROH_LOWER', 2 + i) for i, (x, y) in enumerate(sorted(down))]
    warps += [W3(x, y, NECRO_MAP, i) for i, (x, y) in enumerate(sorted(necro))]      # (to the grounds' foot, x 20-22)
    j = mapj('MAP_MIRROH_UPPER', 'MirrohUpper', warps=warps)
    s = snow_cell(r, M, y0)
    MB.write(r, 'MirrohUpper', 'LAYOUT_MIRROH_UPPER', ('mirroh_upper_tiles', 'MirrohUpperTiles'), ('mirroh_upper', 'MirrohUpper'), j, border=[s] * 4)
    return r

# ------------------------------------------------------------------ the gatehouse hallways
def build_halls():
    import gate_hall as GH
    rows = GH.hall(); img = np.vstack([np.hstack(r) for r in rows]); H, W = len(rows), len(rows[0])
    solid = {(x, y) for y in (0, 1) for x in range(W)} | {(x, y) for y in range(4, 10) for x in (0, 1, 2, 7, 8, 9)}
    solid |= {(1, 2), (8, 2), (0, 11), (9, 11), (0, 16), (9, 16), (1, 12), (1, 13), (8, 12), (8, 13)}
    solid |= {(x, 17) for x in range(W)}
    top, mat = {(4, 1), (5, 1)}, {(4, 16), (5, 16)}
    walk = {(x, y) for y in range(H) for x in range(W) if (x, y) not in solid} | top
    beh = lambda x, y: MB_DOOR if (x, y) in top else MB_SOUTH_ARROW_WARP if (x, y) in mat else MB_NORMAL
    r = MB.build(img, None, None, W, H, walk, beh)
    void = max(r['meta']) + 1; r['meta'][void] = [0] * 12; r['attrs'][void] = 0       # (black beyond its walls)
    guards = [{'graphics_id': 'OBJ_EVENT_GFX_MAN_3', 'x': gx, 'y': 6, 'elevation': 3,
               'movement_type': 'MOVEMENT_TYPE_FACE_' + ('RIGHT' if gx == 0 else 'LEFT'), 'movement_range_x': 0,
               'movement_range_y': 0, 'trainer_type': 'TRAINER_TYPE_NONE', 'trainer_sight_or_berry_tree_id': '0',
               'script': 'MirrohGatehouse_EventScript_Guard', 'flag': '0'} for gx in (0, 9)]
    hall = lambda mid, name, out_south, out_north, north_open: {
        'id': mid, 'name': name, 'layout': 'LAYOUT_MIRROH_GATEHOUSE', 'music': 'MUS_DR_HOLLOW_HILL',
        'region_map_section': 'MAPSEC_MIRROH', 'requires_flash': False, 'weather': 'WEATHER_NONE',
        'map_type': 'MAP_TYPE_INDOOR', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
        'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
        'object_events': guards,
        'warp_events': [W3(4, 16, out_south[0], out_south[1]), W3(5, 16, out_south[0], out_south[1] + 1)] +
                       ([W3(4, 1, out_north[0], out_north[1]), W3(5, 1, out_north[0], out_north[1] + 1)] if north_open else []),
        'coord_events': [] if north_open else
        [{'type': 'trigger', 'x': x, 'y': 1, 'elevation': 3, 'var': 'VAR_TEMP_1', 'var_value': '0',
          'script': 'MirrohNWGatehouse_EventScript_RoadClosed'} for x in (4, 5)], 'bg_events': []}
    MB.write(r, 'MirrohSouthGatehouse', 'LAYOUT_MIRROH_GATEHOUSE', ('mirroh_gatehouse_tiles', 'MirrohGatehouseTiles'),
             ('mirroh_gatehouse', 'MirrohGatehouse'), border=[void] * 4, mapj=
             hall('MAP_MIRROH_SOUTH_GATEHOUSE', 'MirrohSouthGatehouse', ('MAP_MIRROH_GATE', 0), ('MAP_MIRROH_LOWER', 0), True))
    j = hall('MAP_MIRROH_NW_GATEHOUSE', 'MirrohNWGatehouse', ('MAP_MIRROH_UPPER', 0), None, False)
    md = os.path.join(C, 'data/maps/MirrohNWGatehouse'); os.makedirs(md, exist_ok=True)
    json.dump(j, open(os.path.join(md, 'map.json'), 'w'), indent=2); open(os.path.join(md, 'map.json'), 'a').write('\n')
    import imgtiles as IT
    IT._add('data/event_scripts.s', '\t.include "data/maps/PellucaAcademyHall/scripts.inc"\n', '\t.include "data/maps/MirrohNWGatehouse/scripts.inc"\n')
    gj = os.path.join(C, 'data/maps/map_groups.json'); G = json.load(open(gj))
    if 'MirrohNWGatehouse' not in G['gMapGroup_Phase3']:
        G['gMapGroup_Phase3'].append('MirrohNWGatehouse'); json.dump(G, open(gj, 'w'), indent=2); open(gj, 'a').write('\n')
    open(os.path.join(C, 'data/maps/MirrohSouthGatehouse/scripts.pory'), 'w').write(
        'mapscripts MirrohSouthGatehouse_MapScripts {}\n\n'
        'script MirrohGatehouse_EventScript_Guard {\n    lock\n    faceplayer\n'
        '    msgbox("Mirroh\'s gate. Keep to the road, traveller.")\n    release\n}\n')
    open(os.path.join(md, 'scripts.pory'), 'w').write(
        'mapscripts MirrohNWGatehouse_MapScripts {}\n\n'
        'script MirrohNWGatehouse_EventScript_RoadClosed {\n    lock\n'
        '    msgbox("The road beyond is snowed in.\\n(Mt. Mirroh is not built yet.)")\n'
        '    applymovement(OBJ_EVENT_ID_PLAYER, MirrohNWGatehouse_Movement_StepBack)\n    waitmovement(0)\n    release\n}\n\n'
        'movement MirrohNWGatehouse_Movement_StepBack {\n    walk_down\n}\n')
    return r

def hh_connection():
    """Hollow Hill's way north (its top row, x 16-19): a short fade up to Mirroh Gate's bottom row but one."""
    import mirroh_mock as mm
    j = os.path.join(C, 'data/maps/HollowHill/map.json'); m = json.load(open(j))
    m['connections'] = [c for c in m['connections'] if c['map'] != 'MAP_MIRROH_GATE']
    m['coord_events'] = [e for e in m['coord_events'] if not e.get('script', '').startswith('HollowHill_EventScript_ToMirroh')] + \
        [{'type': 'trigger', 'x': hx, 'y': 0, 'elevation': 3, 'var': 'VAR_TEMP_1', 'var_value': '0',
          'script': 'HollowHill_EventScript_ToMirroh%d' % hx} for hx in range(16, 20)]
    json.dump(m, open(j, 'w'), indent=2); open(j, 'a').write('\n')
    p = os.path.join(C, 'data/maps/HollowHill/scripts.pory'); s = open(p).read()
    i = s.find('\n\nscript HollowHill_EventScript_ToMirroh'); s = (s if i < 0 else s[:i]).rstrip('\n') + '\n'
    gh = 72 - 49 - 2                                   # Mirroh Gate: the row above its bottom one
    s += ''.join('\nscript HollowHill_EventScript_ToMirroh%d {\n    setvar(VAR_TEMP_1, 1)          # (else the trigger fires again every frame of the fade)\n    warp(MAP_MIRROH_GATE, %d, %d)\n}\n' % (hx, hx + mm.HHX, gh) for hx in range(16, 20))
    open(p, 'w').write(s)

def main():
    M = mock()
    out = {}
    for name, fn in (('approach', build_gate), ('lower', build_lower), ('upper', build_upper)):
        r = fn(M); out[name] = MB.render(r)
        Image.fromarray(out[name]).save('/home/claude/scratch/mirroh/built_%s.png' % name)
    r = build_halls(); Image.fromarray(MB.render(r)).save('/home/claude/scratch/mirroh/built_hall.png')
    hh_connection()

if __name__ == '__main__':
    main()
