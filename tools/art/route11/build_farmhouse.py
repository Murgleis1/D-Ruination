"""Build Route 11's farmhouse interior from mock v1, variant B (user 2026-11-24: "second one is better probably"):
farmhouse_mock.farmhouse('B'), as Pelluca's houses are built (tools/art/houses/build_houses.py): the picture cut into
its own tileset pair with the Academy's image method (tools/art/academy/imgtiles.py); collision from the mock (every
piece solid, the floor and the loose straw walkable); the mat lifted onto the floor (matlift) and its cells south-arrow
exits to Route 11.
Route 11: the cottage's doorway (55, 14) becomes a door (MB_NON_ANIMATED_DOOR, walkable: build_route11.py's DOOR) with
warp 0 into the farmhouse.
Map: Route11Farmhouse (MAP_ROUTE11_FARMHOUSE, LAYOUT_ROUTE11_FARMHOUSE), its own tilesets route11_farmhouse(_tiles).
Usage: ODYSSEY_ROM=/home/claude/crown/Crown.gba python3 tools/art/route11/build_farmhouse.py   (then build_route11.py, make)"""
import os, sys, json
import numpy as np
os.environ.setdefault('ODYSSEY_ROM', '/home/claude/crown/Crown.gba')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'academy')); sys.path.insert(0, os.path.join(HERE, '..', 'houses'))
import imgtiles as IT
import matlift as ML
import build_houses as BH
import farmhouse_mock as FM

MB_SOUTH_ARROW_WARP = 0x65
PRIM, SEC = ('route11_farmhouse_tiles', 'Route11FarmhouseTiles'), ('route11_farmhouse', 'Route11Farmhouse')
NAME, LAYOUT, MAPID = 'Route11Farmhouse', 'LAYOUT_ROUTE11_FARMHOUSE', 'MAP_ROUTE11_FARMHOUSE'
DOOR = (55, 14)                       # Route 11: the cottage's doorway
ROUTE_WARP = 0                        # Route 11's warp into the farmhouse

def main():
    r = FM.farmhouse('B'); img = r.render()
    solid = BH.solid_of(r)
    walk = {(x, y) for y in range(3, r.H - 1) for x in range(1, r.W - 1) if (x, y) not in solid}
    mats = [(x, r.H - 1) for x in range(r.W) if r.g[r.H - 1][x]]
    mats, walk = ML.lift(img, walk, mats, 0, r.W); mats = sorted(mats)
    R = IT.build(img, r.W, r.H, walk=walk, beh=lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) in mats else 0)
    print('farmhouse: tiles %d metatiles %d palettes %d mismatches %s' % (len(R['tiles']), len(R['meta']), R['npal'], IT.check(R)))
    m = [mats[len(mats) // 2]] + [c for c in mats if c != mats[len(mats) // 2]]      # (warp 0: the mat's middle)
    warps = [{'x': x, 'y': y, 'elevation': 0, 'dest_map': 'MAP_ROUTE11', 'dest_warp_id': str(ROUTE_WARP)} for x, y in m]
    mapj = {'id': MAPID, 'name': NAME, 'layout': LAYOUT, 'music': 'MUS_LILYCOVE_MUSEUM',
            'region_map_section': 'MAPSEC_DR_ROUTE_11', 'requires_flash': False, 'weather': 'WEATHER_NONE',
            'map_type': 'MAP_TYPE_INDOOR', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
            'object_events': [], 'warp_events': warps, 'coord_events': [], 'bg_events': []}
    old = os.path.join(IT.C, 'data/maps', NAME, 'map.json')
    if os.path.exists(old):                                  # (keep the people later stages add)
        prev = json.load(open(old))
        for k in ('object_events', 'coord_events', 'bg_events'): mapj[k] = prev.get(k, [])
    IT.write_room(R, NAME, LAYOUT, PRIM, SEC, mapj, after_layout='LAYOUT_PELLUCA_HOUSE_5', after_map='PellucaHouse5')
    sp = os.path.join(IT.C, 'data/maps', NAME, 'scripts.pory')
    if not os.path.exists(sp):
        open(sp, 'w').write('// ============ DREAMSTONE RUINATION - Route 11: the farmhouse ============\n'
                            '// Built by tools/art/route11/build_farmhouse.py from farmhouse_mock.py, variant B (user 2026-11-24).\n'
                            '// Stage 1 (the look). Who lives here, NPCs and dialogue come in stage 2.\n\n'
                            'mapscripts Route11Farmhouse_MapScripts {}\n')
    # Route 11: the door's warp (its cell made a door by build_route11.py)
    rj = os.path.join(IT.C, 'data/maps/Route11/map.json'); rt = json.load(open(rj))
    w = {'x': DOOR[0], 'y': DOOR[1], 'elevation': 3, 'dest_map': MAPID, 'dest_warp_id': '0'}
    ws = rt['warp_events']; hit = [j for j, v in enumerate(ws) if (v['x'], v['y']) == DOOR]
    if hit: ws[hit[0]] = w
    else: ws.append(w)
    assert ws.index(w) == ROUTE_WARP, ws
    json.dump(rt, open(rj, 'w'), indent=2); open(rj, 'a').write('\n')
    print('mats', mats, 'Route 11 warp', ROUTE_WARP)

if __name__ == '__main__':
    main()
