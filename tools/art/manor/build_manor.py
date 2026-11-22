"""Build Cadmus's manor (Vizier Umbra's residence, Pelluca) from its approved mock (user design 2026-11-19).

manor_mock.py is the picture; this cuts it into its own tileset pair with the Academy's image method
(tools/art/academy/imgtiles.py: all of it in the bottom layer; nothing in the room stands where the player can walk
behind it) and sets collision by hand: one elevation, the stairs walkable, the furniture solid.
Built but locked (user): the manor's door mat warps to Pelluca warp 10, but the city has no warp at the residence
door (13,23) in a normal build, so its "locked" sign answers. MANOR_TEST_OPEN=1 (test builds only) adds that warp
so the manor can be walked in the emulator. The unlock (story) adds the same warp, as warp 10.
Credits: Pokemon Crown (Blah and the Crown team, with permission): the manor set; MonoMyth: the museum paintings,
the study armchair, the archive desk and shelves, the Old HQ candelabras; the Jousteel statue from the project's own
overworld sprite.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/manor/build_manor.py
"""
import os, sys, json
os.environ.setdefault('ODYSSEY_ROM', '/home/claude/crown/Crown.gba')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'academy'))
import imgtiles as IT
import manor_mock as MM
import matlift as ML                                   # (the exit mat onto the floor: user 2026-11-22)

MB_SOUTH_ARROW_WARP = 0x65
NAME, LAYOUT, MAP = 'PellucaUmbraManor', 'LAYOUT_PELLUCA_UMBRA_MANOR', 'MAP_PELLUCA_UMBRA_MANOR'
PRIM, SEC = ('umbra_manor_tiles', 'UmbraManorTiles'), ('umbra_manor', 'UmbraManor')
CITY_DOOR, CITY_WARP = (13, 23), 10                    # (5-9: the five houses)

def rect(x0, x1, y0, y1): return {(x, y) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)}

def cells():
    W, H, LW = MM.W, MM.H, MM.LW
    mats = {(10, H - 1), (11, H - 1)}
    floor = rect(1, W - 2, 2, LW - 1)                                  # the upper floor
    floor |= rect(MM.STAIRS_X + 1, MM.STAIRS_X + 2, LW, LW + 1)          # the stairs (their runner; the posts solid)
    floor |= rect(1, W - 2, LW + 2, H - 2)                               # the wall's foot row and the hall
    solid = rect(2, 5, 2, 3) | {(7, 2)} | rect(10, 11, 2, 4) | rect(15, 16, 2, 2) | rect(19, 20, 2, 2)   # bed, dresser,
    #                                                                     chair and desk, shelves
    solid |= {(1, LW + 2), (2, LW + 2)}                                  # bookcase
    sx, sy = MM.STATUE_AT; solid |= {(sx, sy + 2), (sx + 1, sy + 2)}      # the statue's plinth
    solid |= rect(MM.HEARTH_X, MM.HEARTH_X + 5, LW + 2, LW + 2)          # hearth and its candelabras
    solid |= {(20, LW + 2)}                                              # clock
    solid |= rect(MM.TABLE_X - 1, MM.TABLE_X + MM.TABLE_LEN, LW + 5, LW + 6)   # the table and its two chairs
    solid |= rect(20, 20, LW + 4, LW + 7) | {(1, LW + 8), (1, LW + 9)}   # side table; jug, coat stand
    return (floor - solid) | mats, mats

def main():
    img, _ = MM.compose(); W, H = MM.W, MM.H
    walk, mats = cells()
    mats, walk = ML.lift(img, walk, mats)                                 # (mat and warps under the floor: up onto it)
    # 109 colours: merging only one GBA step left 15 palettes; rare colours (under 300 px: the paintings, the desk,
    # the hearth stone's flecks) also merge at two steps -> 12 (the change is not visible)
    r = IT.build(img, W, H, walk=walk, beh=lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) in mats else 0, merge=16, rare=300, tries=2000)
    bad = IT.check(r)
    warps = [{'x': x, 'y': y, 'elevation': 0, 'dest_map': 'MAP_PELLUCA_CITY', 'dest_warp_id': str(CITY_WARP)} for x, y in sorted(mats)]
    mapj = {'id': MAP, 'name': NAME, 'layout': LAYOUT, 'music': 'MUS_LILYCOVE_MUSEUM',
            'region_map_section': 'MAPSEC_PELLUCA_VALLEY', 'requires_flash': False, 'weather': 'WEATHER_NONE',
            'map_type': 'MAP_TYPE_INDOOR', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None, 'object_events': [],
            'warp_events': warps, 'coord_events': [], 'bg_events': []}
    IT.write_room(r, NAME, LAYOUT, PRIM, SEC, mapj, after_layout='LAYOUT_PELLUCA_ACADEMY_LOUNGE', after_map='PellucaAcademyLounge')
    sp = os.path.join(IT.C, 'data/maps', NAME, 'scripts.pory')
    if not os.path.exists(sp):
        open(sp, 'w').write('// ============ DREAMSTONE RUINATION - Pelluca: Cadmus\'s manor (Vizier Umbra\'s residence) ============\n'
                            '// Built by tools/art/manor/build_manor.py from manor_mock.py (user design 2026-11-19).\n'
                            '// Built but locked: the city door keeps its sign. NPCs and dialogue come with the story.\n\n'
                            f'mapscripts {NAME}_MapScripts {{}}\n')
    # Pelluca: the residence door (13,23) is already a door metatile, and a door warps on a step north into it whatever
    # its collision. So "locked" = no city warp there (its sign answers instead); MANOR_TEST_OPEN adds the warp (as
    # Pelluca warp 10, the manor's door mat's destination).
    cj = os.path.join(IT.C, 'data/maps/PellucaCity/map.json'); city = json.load(open(cj))
    ws = [v for v in city['warp_events'] if (v['x'], v['y']) != CITY_DOOR]
    if os.environ.get('MANOR_TEST_OPEN'):
        assert len(ws) == CITY_WARP, len(ws)
        ws.append({'x': CITY_DOOR[0], 'y': CITY_DOOR[1], 'elevation': 0, 'dest_map': MAP, 'dest_warp_id': '0'})
    city['warp_events'] = ws
    json.dump(city, open(cj, 'w'), indent=2); open(cj, 'a').write('\n')
    print(f'manor {W}x{H} tiles {len(r["tiles"])} metatiles {len(r["meta"])} palettes {r["npal"]} mismatches {bad}'
          f'{"  (TEST: city door open)" if os.environ.get("MANOR_TEST_OPEN") else ""}')

if __name__ == '__main__':
    main()
