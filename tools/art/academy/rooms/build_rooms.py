"""Build the Academy's four rooms from their approved mocks (user design 2026-11-19), and wire them to the hall.

  classroom (M3): classroom_mock.py   office (G1): office_mock.py   library (M1): library_mock.py
  haunted teachers' lounge (T4): lounge_mock.py; its door stays locked (rusted key after the second badge), so the
  room is built and its warps wired, but the hall's T4 door stays solid with its sign.
Each room: its own tileset pair (imgtiles.build: all furniture in the bottom layer and solid), a south-arrow exit on
its door mat (both mat cells), warps to the hall's door. The hall's G1/M1/M3 door cells become open doors
(build_hall.py: ROOM_DOORS). Credits: MonoMyth (cabin, Fort Elderflower archive, Old HQ, La Costa Nostra, Webbed
Woods, Watercress/New Old Bay pieces), Pokemon Crown (Blah and the Crown team, with permission).
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/academy/rooms/build_rooms.py
"""
import os, sys
os.environ.setdefault('ODYSSEY_ROM', '/home/claude/crown/Crown.gba')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import imgtiles as IT
import classroom_mock, office_mock, library_mock, lounge_mock
import matlift as ML                                   # (the exit mat onto the floor: user 2026-11-22)

MB_SOUTH_ARROW_WARP = 0x65
HALL = 'MAP_PELLUCA_ACADEMY_HALL'
# the hall's warp ids for the rooms' doors (build_hall.py ROOM_DOORS keeps the same order)
HALL_WARP = {'office': 1, 'library': 2, 'classroom': 3, 'lounge': 4}

def rect(x0, x1, y0, y1): return {(x, y) for x in range(x0, x1 + 1) for y in range(y0, y1 + 1)}

def classroom():
    img, _ = classroom_mock.compose(); W, H = classroom_mock.W, classroom_mock.H
    floor = rect(1, 14, 2, H - 2); mats = {(7, H - 1), (8, H - 1)}
    solid = rect(1, 4, 2, 2) | {(11, 2), (12, 2), (14, 2), (7, 3), (8, 3)}
    for r, x in classroom_mock.DESKS_AT: solid |= rect(x, x + 1, r, r + 1)
    return img, W, H, (floor - solid) | mats, mats

def office():
    img, _ = office_mock.compose(); W, H = office_mock.W, office_mock.H
    floor = rect(1, 10, 2, H - 2); mats = {(5, H - 1), (6, H - 1)}
    solid = rect(1, 4, 2, 2) | rect(6, 10, 2, 3) | {(10, 4), (10, 5)} | rect(7, 9, 4, 5)      # shelves, couch, table
    for x, y in office_mock.CANDLES: solid |= {(x, y), (x, y - 1)}
    return img, W, H, (floor - solid) | mats, mats

def library():
    img = library_mock.compose(); W, H = library_mock.W, library_mock.H
    floor = rect(1, 16, 4, H - 2) | rect(7, 9, 3, 3); mats = {(8, H - 1), (9, H - 1)}
    solid = set()
    for x0, y0 in library_mock.STACKS: solid |= rect(x0, x0 + 1, y0, y0 + 1)
    for x0, y in library_mock.NOOKS: solid |= rect(x0, x0 + 2, y, y)
    for x, y, _ in library_mock.CHAIRS: solid.add((x, y))
    return img, W, H, (floor - solid) | mats, mats

def lounge():
    img = lounge_mock.compose(); X0, Y0 = lounge_mock.X0, lounge_mock.Y0
    W, H = lounge_mock.X1 - X0, lounge_mock.Y1 - Y0
    m = lambda cells: {(x - X0, y - Y0) for x, y in cells}
    floor = m(rect(10, 18, 11, 14)); mats = m({(12, 14), (13, 14)})
    solid = m(rect(10, 11, 11, 12) | {(15, 11), (16, 11), (16, 12), (15, 13), (16, 13), (18, 12), (18, 13)})
    return img, W, H, floor - solid, mats

ROOMS = [  # key, map name, layout id, (primary dir, Name), (secondary dir, Name), builder
    ('office', 'PellucaAcademyOffice', 'LAYOUT_PELLUCA_ACADEMY_OFFICE', ('academy_office_tiles', 'AcademyOfficeTiles'), ('academy_office', 'AcademyOffice'), office),
    ('library', 'PellucaAcademyLibrary', 'LAYOUT_PELLUCA_ACADEMY_LIBRARY', ('academy_library_tiles', 'AcademyLibraryTiles'), ('academy_library', 'AcademyLibrary'), library),
    ('classroom', 'PellucaAcademyClassroom', 'LAYOUT_PELLUCA_ACADEMY_CLASSROOM', ('academy_classroom_tiles', 'AcademyClassroomTiles'), ('academy_classroom', 'AcademyClassroom'), classroom),
    ('lounge', 'PellucaAcademyLounge', 'LAYOUT_PELLUCA_ACADEMY_LOUNGE', ('academy_lounge_tiles', 'AcademyLoungeTiles'), ('academy_lounge', 'AcademyLounge'), lounge),
]

def main():
    after_l, after_m = 'LAYOUT_PELLUCA_ACADEMY_HALL', 'PellucaAcademyHall'
    for key, name, lid, prim, sec, fn in ROOMS:
        img, W, H, walk, mats = fn()
        my = max(y for _, y in mats)
        if my == H - 1: mats, walk = ML.lift(img, walk, mats)              # (mat and warps under the floor: up onto it)
        else: ML.move_row(img, my + 1, my)                                 # (the lounge: its warps on the floor, its mat drawn under)
        r = IT.build(img, W, H, walk=walk, beh=lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) in mats else 0)
        bad = IT.check(r)
        warps = [{'x': x, 'y': y, 'elevation': 0, 'dest_map': HALL, 'dest_warp_id': str(HALL_WARP[key])} for x, y in sorted(mats)]
        mapj = {'id': 'MAP_' + lid[len('LAYOUT_'):], 'name': name, 'layout': lid, 'music': 'MUS_LILYCOVE_MUSEUM',
                'region_map_section': 'MAPSEC_PELLUCA_VALLEY', 'requires_flash': False, 'weather': 'WEATHER_NONE',
                'map_type': 'MAP_TYPE_INDOOR', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
                'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None, 'object_events': [],
                'warp_events': warps, 'coord_events': [], 'bg_events': []}
        IT.write_room(r, name, lid, prim, sec, mapj, after_layout=after_l, after_map=after_m)
        sp = os.path.join(IT.C, 'data/maps', name, 'scripts.pory')
        if not os.path.exists(sp):
            open(sp, 'w').write(f'// ============ DREAMSTONE RUINATION - Pelluca Valley: the Academy, {key} ============\n'
                                f'// Built by tools/art/academy/rooms/build_rooms.py from {key}_mock.py (user design 2026-11-19).\n'
                                f'// NPCs and dialogue come with the dialogue pass.\n\nmapscripts {name}_MapScripts {{}}\n')
        after_l, after_m = lid, name
        print(f'{key:9s} {W}x{H} tiles {len(r["tiles"])} metatiles {len(r["meta"])} palettes {r["npal"]} mismatches {bad}')

if __name__ == '__main__':
    main()
