"""Build the Necropolis lake (mock v2, user 2026-11-21) into the game: MAP_NECROPOLIS_LAKE.

The picture is lake_mock.compose() in its game mode (the ice repeating every 4x4 cells, its shades held to whole
and half steps), its colours merged to fit (tilefit), cut into its own tileset pair by academy/imgtiles.py
(primary `necropolis_lake_tiles`: every tile and palettes 0-5; secondary `necropolis_lake`: palettes 6-12 and the
metatiles). Behaviours and collision come from the puzzle grid (lake_puzzle via lake_mock.layout()):
  ice    -> MB_ICE (the engine's sliding ice: field_player_avatar.c ForcedMovement_Slip), walkable;
  soil   -> normal floor, walkable (the islands, the corner platforms, the landing, the door's landing);
  block  -> solid (graves, statues, walls, the bonfires, the sealed arch, the dark).
The four necromancers stand by their bonfires as object events (placeholders: no scripts or teams yet).
The landing's foot (x 20-22, the bottom row) is a south arrow warp up to the grounds' grand entrance; the sealed
arch (21, 4) warps up to Kimaris's chamber (solid until the Trial opens it). With DR_LAKE_TEST=1 a test way in is added:
a trigger on Hollow Hill's way north warps to the landing (one way); rebuild without it
to take it out.
Usage: python3 tools/art/necropolis/build_lake.py   (then make)
"""
import os, sys, json
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'academy'))
import lake_mock as LM, lake_puzzle as P, imgtiles as IT, tilefit

C = IT.C
MAP, LAYOUT, MAPID = 'NecropolisLake', 'LAYOUT_NECROPOLIS_LAKE', 'MAP_NECROPOLIS_LAKE'
PRIM, SEC = ('necropolis_lake_tiles', 'NecropolisLakeTiles'), ('necropolis_lake', 'NecropolisLake')
MB_NORMAL, MB_ICE = 0x00, 0x20
TEST = bool(os.environ.get('DR_LAKE_TEST'))
HH_TEST_CELL = (17, 6)                                          # Hollow Hill's way north (tools: hh/walk_hh.py)

def main():
    LM.GAME = True
    img, _ = LM.compose(False)
    g, graves, soil = LM.layout()
    H, W = g.shape
    img = img[:H * 16, :W * 16]
    q, _ = tilefit.reduce_joint([img], (0, 0, img.shape[1], img.shape[0]), 110); q = q[0]
    q, _ = tilefit.reduce_tiles(q, (0, 0, q.shape[1], q.shape[0]), 15)
    trainers = {v['trainer'] for v in P.CORNERS.values()}
    walk = {(x, y) for y in range(H) for x in range(W) if g[y, x] != P.BLOCK} | trainers
    mats = [(x, P.H - 1) for x in (20, 21, 22)]                  # the landing's foot: up to the grounds
    beh = lambda x, y: MB_ICE if g[y, x] == P.ICE and (x, y) not in trainers else 0x65 if (x, y) in mats else MB_NORMAL
    r = IT.build(q, W, H, walk=walk, beh=beh, tries=400)
    print('palettes', r['npal'], 'tiles', len(r['tiles']), 'metatiles', len(r['meta']), 'check', IT.check(r))
    objs = []
    for k, v in sorted(P.CORNERS.items()):                       # the necromancers (Dale, Gram, two assistants)
        x, y = v['trainer']
        objs.append({'graphics_id': 'OBJ_EVENT_GFX_HEX_MANIAC', 'x': x, 'y': y, 'elevation': 3,
                     'movement_type': 'MOVEMENT_TYPE_FACE_DOWN', 'movement_range_x': 0, 'movement_range_y': 0,
                     'trainer_type': 'TRAINER_TYPE_NONE', 'trainer_sight_or_berry_tree_id': '0',
                     'script': 'NecropolisLake_EventScript_Necromancer', 'flag': '0'})
    mapj = {'id': MAPID, 'name': MAP, 'layout': LAYOUT, 'music': 'MUS_MT_PYRE',
            'region_map_section': 'MAPSEC_DR_MIRROH_NECROPOLIS', 'requires_flash': False, 'weather': 'WEATHER_NONE',
            'map_type': 'MAP_TYPE_UNDERGROUND', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': True, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
            'object_events': objs,
            'warp_events': [{'x': 21, 'y': 4, 'elevation': 3, 'dest_map': 'MAP_KIMARIS_CHAMBER', 'dest_warp_id': '0'}] +
                           [{'x': x, 'y': y, 'elevation': 3, 'dest_map': 'MAP_NECROPOLIS_GROUNDS', 'dest_warp_id': '4'} for (x, y) in mats],
            'coord_events': [], 'bg_events': []}
    IT.write_room(r, MAP, LAYOUT, PRIM, SEC, mapj)
    d = os.path.join(C, 'data/maps', MAP)
    pory = ('mapscripts NecropolisLake_MapScripts {}\n\n'
            'script NecropolisLake_EventScript_Necromancer {\n    lock\n    faceplayer\n'
            '    msgbox("(A necromancer of House Langerin.\\nNo battle yet: the Trial is not written.)")\n    release\n}\n')
    open(os.path.join(d, 'scripts.pory'), 'w').write(pory)
    # the test way in, on Hollow Hill (added or taken out)
    hj = os.path.join(C, 'data/maps/HollowHill/map.json'); hm = json.load(open(hj))
    hm['coord_events'] = [e for e in hm['coord_events'] if e.get('script') != 'HollowHill_EventScript_LakeTest']
    hp = os.path.join(C, 'data/maps/HollowHill/scripts.pory'); hs = open(hp).read()
    i = hs.find('\n\nscript HollowHill_EventScript_LakeTest'); hs = hs if i < 0 else hs[:i] + '\n'
    if TEST:
        x, y = HH_TEST_CELL
        hm['coord_events'].append({'type': 'trigger', 'x': x, 'y': y, 'elevation': 3, 'var': 'VAR_TEMP_1', 'var_value': '0',
                                   'script': 'HollowHill_EventScript_LakeTest'})
        hs = hs.rstrip('\n') + '\n\nscript HollowHill_EventScript_LakeTest {\n    setvar(VAR_TEMP_1, 1)\n' \
             '    warp(MAP_NECROPOLIS_LAKE, %d, %d)\n}\n' % P.START
    json.dump(hm, open(hj, 'w'), indent=2); open(hj, 'a').write('\n'); open(hp, 'w').write(hs)

if __name__ == '__main__':
    main()
