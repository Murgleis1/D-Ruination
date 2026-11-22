"""Build Route 13 (mock v2 approved by the user 2026-11-22) into the game from tools/art/route13/route13_v2.py's
composition: its pixels, collision and behaviours go to tools/art/mapbuild.py as a map with its own tileset pair.

Connections: its foot's passage (x 19-20, row 122, the road's last cells at the gatehouse roof's peak: south arrow warps) leads down into Mirroh's north-west gatehouse
hall, whose top doorway (4-5, 1) now leads up here (tools/art/mirroh/build_mirroh.py, the NW hall's north_open).
Its two top exits (Mt. Mirroh, x 7-10; Templar HQ, x 32-34) stay closed until those maps exist.
The border: Elderflower's small pines (1x2) repeated, so the camera shows woods past the edges, never open snow.
Usage: python3 tools/art/route13/build_route13.py   (then rebuild Mirroh's halls: build_mirroh.py; then make)
"""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import route13_v2 as V
import mapbuild as MB
C = V.C
MB_SOUTH_ARROW_WARP = 0x65
PASSAGE = [(19, 122), (20, 122)]   # (the road's last two cells at the roof's peak: MonoMyth's north-door convention)

def main():
    K, _ = V.compose()
    W, H = V.W, V.H
    walk = {(x, y) for y in range(H) for x in range(W) if not K.solid[y, x]}
    beh = lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) in PASSAGE else int(K.beh[y, x])
    r = MB.build(K.img, None, None, W, H, walk, beh)
    # the border: a small pine's top and foot (Elderflower 0x109/0x111), so map cell (x, y) shows the top on even rows
    ef = lambda m: V.mm.full('ef', m)
    def find(m):
        t = ef(m)
        for y in range(H):
            for x in range(W):
                if (K.img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] == t).all(): return int(r['grid'][y, x] & 0x3FF)
    top, foot = find(0x109), find(0x111)
    assert top is not None and foot is not None
    mapj = {'id': 'MAP_ROUTE13', 'name': 'Route13', 'layout': 'LAYOUT_ROUTE13', 'music': 'MUS_DR_MM_ROUTE15',
            'region_map_section': 'MAPSEC_DR_ROUTE_13', 'requires_flash': False, 'weather': 'WEATHER_SNOW',
            'map_type': 'MAP_TYPE_ROUTE', 'allow_cycling': True, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': True, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
            'object_events': [],
            'warp_events': [{'x': x, 'y': y, 'elevation': 3, 'dest_map': 'MAP_MIRROH_NW_GATEHOUSE', 'dest_warp_id': str(2 + i)}
                            for i, (x, y) in enumerate(PASSAGE)],
            'coord_events': [], 'bg_events': []}
    MB.write(r, 'Route13', 'LAYOUT_ROUTE13', ('route13_tiles', 'Route13Tiles'), ('route13', 'Route13'), mapj,
             border=[top, top, foot, foot])
    d = os.path.join(C, 'data/maps/Route13')
    open(os.path.join(d, 'scripts.pory'), 'w').write('mapscripts Route13_MapScripts {}\n')
    print('Route 13 built:', W, 'x', H)

if __name__ == '__main__':
    main()
