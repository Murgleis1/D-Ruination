"""Build the Templar Citadel (Templar Headquarters) into the game from its approved mock (citadel_mock.py, v7; user
2026-11-22 "Perfect. Proceed"): MAP_TEMPLAR_CITADEL, its own tileset pair (tools/art/mapbuild.py: ground on the bottom
layer, everything standing on it on the middle layer), connected to Route 13's north-east exit.

The seam: Route 13's road to the Citadel leaves its top edge at x 32-34; the Citadel's road enters its bottom edge at
x 18-20. A map connection would not do: the engine reloads only the new map's secondary tileset when you cross one
(connected maps are meant to share a primary, and the strip of the neighbour you can see is drawn with the current
map's tiles), and the Citadel has its own primary (in the game it came up scrambled). So the road fades across, as
Hollow Hill's way north fades into Mirroh Gate: triggers on Route 13's top row (x 32-34) warp to the Citadel's row 38
(x 18-20), and on the Citadel's bottom row back to Route 13's row 1.
Collision: paving and stairs walked on (the landing pad too); cliffs, walls, parapets, buildings, statues, the
fountain, lamps, fences and targets solid; outside the curtain wall only the road and the guards' apron are walked on
(the snow and pines beyond are the mountain). The church door (19,17) leads into the nave (MAP_TEMPLAR_CATHEDRAL, cathedral/build_cathedral.py); the four
houses' doors (2026-11-23) into the Tavern, the barracks, the armoury and the watch house (citadel_rooms/build_houses.py,
whose HOUSES holds their door cells; their warps follow the church's, in that order).
The line of Templar guards across the cleft to Route 15 (user 2026-11-22) goes in now as objects, since they are the
barrier: "an incident on Route 15 ... nobody is allowed in or out". The courtyard's other Templars are stage 2.
Usage: python3 tools/art/templar_hq/build_citadel.py   (then rebuild Route 13: build_route13.py; then make)
"""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import citadel_mock as CM
sys.path.insert(0, os.path.join(HERE, 'citadel_rooms'))
import build_houses as BH
import mapbuild as MB
C = MB.C
NAME, LAYOUT, MAPID = 'TemplarCitadel', 'LAYOUT_TEMPLAR_CITADEL', 'MAP_TEMPLAR_CITADEL'
ROUTE13_OFFSET = 14
GUARDS = [(36, 15), (36, 16), (36, 17)]
CHURCH_DOOR = (19, 17)          # (the church front's doorway; into the nave, user 2026-11-23: build the interiors)
MB_DOOR = 0x60

def main():
    M = CM.compose(); W, H = CM.W, CM.H
    bot = np.zeros((H * 16, W * 16, 3), np.uint8); mid = np.zeros_like(bot); ma = np.zeros((H * 16, W * 16), bool)
    for y in range(H):
        for x in range(W):
            s = (slice(y * 16, y * 16 + 16), slice(x * 16, x * 16 + 16)); bot[s] = M.g[y][x]
            for img, a in M.obj[y][x]: mid[s][a] = img[a]; ma[s] |= a
    walk = {(x, y) for y in range(H) for x in range(W)
            if M.gtag[y, x] in ('pave', 'stairs') and M.otag[y, x] in (None, 'pad')}
    house_doors = [(c, BH.HOUSES[k][1], BH.entry_warp(k)[i]) for k in BH.HOUSES for i, c in enumerate(BH.HOUSES[k][2])]
    doors = {CHURCH_DOOR} | {c for c, _, _ in house_doors}
    walk |= doors
    beh = lambda x, y: MB_DOOR if (x, y) in doors else 0
    r = MB.build(bot, (mid, ma), None, W, H, walk, beh)
    # the border: Elderflower's small pines (top on even rows, foot on odd), as Route 13's, so the mountain goes on
    def find(m):
        t = CM.ef(m)
        for y in range(H):
            for x in range(W):
                if (bot[y * 16:y * 16 + 16, x * 16:x * 16 + 16] == t).all() and not ma[y * 16:y * 16 + 16, x * 16:x * 16 + 16].any():
                    return int(r['grid'][y, x] & 0x3FF)
    snow = find(0xed)
    T = lambda x, y, scr, mv: {'graphics_id': 'OBJ_EVENT_GFX_TEMPLAR', 'x': x, 'y': y, 'elevation': 3, 'movement_type': mv,
                               'movement_range_x': 0, 'movement_range_y': 0, 'trainer_type': 'TRAINER_TYPE_NONE',
                               'trainer_sight_or_berry_tree_id': '0', 'script': scr, 'flag': '0'}
    mapj = {'id': MAPID, 'name': NAME, 'layout': LAYOUT, 'music': 'MUS_DR_MM_ROUTE15',
            'region_map_section': 'MAPSEC_DR_TEMPLAR_HQ', 'requires_flash': False, 'weather': 'WEATHER_SNOW',
            'map_type': 'MAP_TYPE_TOWN', 'allow_cycling': True, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': True, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL',
            'connections': None,
            'object_events': [T(x, y, 'TemplarCitadel_EventScript_Route15Guard', 'MOVEMENT_TYPE_FACE_LEFT') for (x, y) in GUARDS],
            'warp_events': [{'x': CHURCH_DOOR[0], 'y': CHURCH_DOOR[1], 'elevation': 3, 'dest_map': 'MAP_TEMPLAR_CATHEDRAL',
                             'dest_warp_id': '1'}]                  # (warp 0; into the nave, onto the middle of its mat)
                           + [{'x': c[0], 'y': c[1], 'elevation': 3, 'dest_map': mid, 'dest_warp_id': str(w)}
                              for c, mid, w in house_doors],        # (warps 1..: the houses, build_houses.HOUSES order)
            'coord_events': [{'type': 'trigger', 'x': x, 'y': H - 1, 'elevation': 3, 'var': 'VAR_TEMP_1', 'var_value': '0',
                              'script': 'TemplarCitadel_EventScript_ToRoute13_%d' % x} for x in (18, 19, 20)],
            'bg_events': []}
    MB.write(r, NAME, LAYOUT, ('templar_citadel_tiles', 'TemplarCitadelTiles'), ('templar_citadel', 'TemplarCitadel'), mapj,
             border=[snow] * 4, after_layout='LAYOUT_ROUTE13', after_map='Route13')
    down = ''.join('\nscript TemplarCitadel_EventScript_ToRoute13_%d {\n    setvar(VAR_TEMP_1, 1)          # (else the trigger fires again every frame of the fade)\n    warp(MAP_ROUTE13, %d, 1)\n}\n' % (x, x + ROUTE13_OFFSET) for x in (18, 19, 20))
    open(os.path.join(C, 'data/maps', NAME, 'scripts.pory'), 'w').write('''mapscripts TemplarCitadel_MapScripts {}
''' + down + '''
// The line of Templar guards across the cleft east to Route 15 (user 2026-11-22). Route 15's chapter opens it.
script TemplarCitadel_EventScript_Route15Guard {
    speakername("Templar")
    msgbox(format("There's been an incident on Route 15. We're observing the situation.\\pUntil something changes, nobody is allowed in or out that way."), MSGBOX_NPC)
    end
}
''')
    print('Templar Citadel built:', W, 'x', H)

if __name__ == '__main__':
    main()
