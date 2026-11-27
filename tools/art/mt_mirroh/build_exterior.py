"""Build Mt. Mirroh's exterior into the game (user 2026-11-23: mock v1, "keep both"): MAP_MT_MIRROH_EXTERIOR, redrawn
on its own tileset pair (tools/art/mapbuild.py) from exterior_mock.py; Dreamstone Mysteries' layout, its map id and
name kept (the expansion keeps DM's maps).

Ways in and out:
  - the foot path (x 38-39, the bottom row) fades to Route 13's Mt. Mirroh exit (its stair's top, x 8-9), and back
    (Route 13's own triggers: tools/art/route13/build_route13.py); no map connection (each has its own primary);
  - warp 0: the cave mouth (13, 10) into 1F (its warp 3; 1F's way out (55, 57) points back here, warp 0);
  - warp 1: the secret ladder (9, 13) down to B1F (its warp 0; B1F's way up points back here), under a Rock Smash rock.
Objects: the Rock Smash rock on the ladder (Dreamstone Mysteries' Strength boulders by the cave mouth removed, user). Its other
people and items are stage 2 and 6 (left out here). Signs: the one by the cave mouth.
Usage: python3 tools/art/mt_mirroh/build_exterior.py   (then build_route13.py; then make)
"""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import exterior_mock as E
import mapbuild as MB
C = MB.C
NAME, LAYOUT, MAPID = 'MtMirrohExterior', 'LAYOUT_MT_MIRROH_EXTERIOR', 'MAP_MT_MIRROH_EXTERIOR'
MB_OCEAN_WATER, MB_WATERFALL, MB_NON_ANIMATED_DOOR, MB_LADDER = 0x15, 0x13, 0x60, 0x61
FOOT = [(38, E.H - 1), (39, E.H - 1)]

def main():
    import tilequant as TQN
    img, solid, beh = E.compose()
    img, _ = TQN.quantise(img.astype(int), n=13); img = img.astype(np.uint8)
    W, H = E.W, E.H
    walk = {(x, y) for y in range(H) for x in range(W) if not solid[y, x] and (x, y) not in E.WATER or (x, y) in E.BRIDGE}
    walk |= {E.CAVE, E.SECRET}
    D = E.D['cells']
    def b(x, y):
        if (x, y) == E.CAVE: return MB_NON_ANIMATED_DOOR
        if (x, y) == E.SECRET: return MB_LADDER
        if (x, y) in E.WATER and (x, y) not in E.BRIDGE:
            return MB_WATERFALL if D['%d,%d' % (x, y)][2] == 'MB_WATERFALL' else MB_OCEAN_WATER
        return int(beh[y, x])
    r = MB.build(img, None, None, W, H, walk, b)
    # the river is real water (user 2026-11-27: "you should be able to fish in the water leading up to the cave
    # entrance"): its cells sit a level below the banks with no collision, so the Old Rod works from the bank (and a
    # later Surf could ride it); the waterfalls stay solid
    for y in range(H):
        for x in range(W):
            if b(x, y) == MB_OCEAN_WATER:
                r['grid'][y, x] = (r['grid'][y, x] & 0x3FF) | (0 << 10) | (1 << 12)
    j = json.load(open(os.path.join(C, 'data/maps', NAME, 'map.json')))
    keep_objs = []                       # (DM's Strength boulders by the mouth: gone, user 2026-11-23)
    rock = {'graphics_id': 'OBJ_EVENT_GFX_BREAKABLE_ROCK', 'x': E.SECRET[0], 'y': E.SECRET[1], 'elevation': 3,
            'movement_type': 'MOVEMENT_TYPE_LOOK_AROUND', 'movement_range_x': 0, 'movement_range_y': 0,
            'trainer_type': 'TRAINER_TYPE_NONE', 'trainer_sight_or_berry_tree_id': '0', 'script': 'EventScript_RockSmash', 'flag': '0'}
    j.update({'weather': 'WEATHER_SNOW', 'connections': None, 'object_events': keep_objs + [rock],
              'warp_events': [{'x': E.CAVE[0], 'y': E.CAVE[1], 'elevation': 3, 'dest_map': 'MAP_MIRROH_INTERIOR_1F', 'dest_warp_id': '0'},
                              {'x': E.SECRET[0], 'y': E.SECRET[1], 'elevation': 3, 'dest_map': 'MAP_MIRROH_INTERIOR_B1F', 'dest_warp_id': '0'}],
              'coord_events': [{'type': 'trigger', 'x': x, 'y': y, 'elevation': 3, 'var': 'VAR_TEMP_1', 'var_value': '0',
                                'script': 'MtMirrohExterior_EventScript_ToRoute13_%d' % x} for (x, y) in FOOT],
              'bg_events': [e for e in j['bg_events'] if (e['x'], e['y']) == (12, 11)]})
    # the border: a pine of the woods (the camera shows woods past the edges)
    border = int(r['grid'][E.H - 1, 0] & 0x3FF)
    MB.write(r, NAME, LAYOUT, ('mt_mirroh_ext_tiles', 'MtMirrohExtTiles'), ('mt_mirroh_ext', 'MtMirrohExt'), None,
             border=[border] * 4)
    json.dump(j, open(os.path.join(C, 'data/maps', NAME, 'map.json'), 'w'), indent=2); open(os.path.join(C, 'data/maps', NAME, 'map.json'), 'a').write('\n')
    sp = os.path.join(C, 'data/maps', NAME, 'scripts.pory'); sc = open(sp).read()
    if 'ToRoute13_' not in sc:
        sc += '\n// The foot path fades down to Route 13 (its Mt. Mirroh exit, the stair\'s top; 2026-11-23)\n'
        for (x, y) in FOOT:
            sc += 'script MtMirrohExterior_EventScript_ToRoute13_%d {\n    setvar(VAR_TEMP_1, 1)\n    warp(MAP_ROUTE13, %d, 1)\n}\n' % (x, x - 30)
        open(sp, 'w').write(sc)
    # 1F's way out (55, 57) and B1F's way up lead back to the cave mouth (warp 0) and the ladder (warp 1)
    for m, idx, wid in (('MirrohInterior_1F', 0, '0'), ('MirrohInterior_B1F', 0, '1')):
        p = os.path.join(C, 'data/maps', m, 'map.json'); mj = json.load(open(p))
        mj['warp_events'][idx]['dest_warp_id'] = wid; mj['warp_events'][idx]['dest_map'] = MAPID
        json.dump(mj, open(p, 'w'), indent=2); open(p, 'a').write('\n')
    print('Mt. Mirroh exterior built:', W, 'x', H)

if __name__ == '__main__':
    main()
