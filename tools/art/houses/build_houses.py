"""Build Pelluca's five houses from their approved mocks (houses_mock.py; user approved 2026-11-19) and open their doors.

All five share one tileset pair (houses_tiles / houses): the mocks are laid side by side into one picture and cut
with the Academy's image method (tools/art/academy/imgtiles.py), then each house's cells become its own layout.
Collision from the mocks (every piece solid, the floor walkable); the door mat's three cells are south-arrow exits.
Pelluca: the five "The door is locked." signs go, the five door cells become walkable (as the dormitory's) and get
warps 5-9. (Cadmus's manor, locked, takes warp 10 when it opens.)
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/houses/build_houses.py
"""
import os, sys, json, struct
import numpy as np
os.environ.setdefault('ODYSSEY_ROM', '/home/claude/crown/Crown.gba')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'academy'))
import imgtiles as IT
import houses_mock as HM
import matlift as ML                                   # (the exit mat onto the floor: user 2026-11-22)

MB_SOUTH_ARROW_WARP = 0x65
PRIM, SEC = ('pelluca_houses_tiles', 'PellucaHousesTiles'), ('pelluca_houses', 'PellucaHouses')
# key, city door, map name
HOUSES = [('H1', (59, 8), 'PellucaHouse1'), ('H2', (54, 23), 'PellucaHouse2'), ('H3', (64, 23), 'PellucaHouse3'),
          ('H4', (54, 30), 'PellucaHouse4'), ('H5', (64, 30), 'PellucaHouse5')]
FIRST_CITY_WARP = 5

def solid_of(r):
    """The mock's solid cells, plus every cell a pasted piece covers by a third or more (the stump table, the
    cauldron, the alchemy desk and shelf)."""
    s = set(r.solid)
    for (rgb, m), px, py in r.over:
        for y in range(py // 16, (py + m.shape[0] + 15) // 16):
            for x in range(px // 16, (px + m.shape[1] + 15) // 16):
                sub = m[max(0, y * 16 - py):y * 16 + 16 - py, max(0, x * 16 - px):x * 16 + 16 - px]
                if sub.size and sub.sum() >= 86: s.add((x, y))
    return s

def main():
    rooms = [(k, door, name, getattr(HM, k.lower())()) for k, door, name in HOUSES]
    Hmax = max(r.H for *_, r in rooms); x0s, x = [], 0
    for *_, r in rooms: x0s.append(x); x += r.W
    img = np.zeros((Hmax * 16, x * 16, 3), np.uint8); walk, mats = set(), {}
    for (k, door, name, r), ox in zip(rooms, x0s):
        img[:r.H * 16, ox * 16:(ox + r.W) * 16] = r.render()
        solid = solid_of(r)
        for y in range(3, r.H - 1):
            for xx in range(1, r.W - 1):
                if (xx, y) not in solid: walk.add((ox + xx, y))
        mx = [xx for xx in range(r.W) if r.g[r.H - 1][xx]]
        mats[k] = [(ox + xx, r.H - 1) for xx in mx]
        lifted, walk = ML.lift(img, walk, mats[k], ox, ox + r.W); mats[k] = sorted(lifted)
    allmats = {c for v in mats.values() for c in v}
    R = IT.build(img, x, Hmax, walk=walk, beh=lambda cx, cy: MB_SOUTH_ARROW_WARP if (cx, cy) in allmats else 0)
    bad = IT.check(R)
    print(f'shared tiles {len(R["tiles"])} metatiles {len(R["meta"])} palettes {R["npal"]} mismatches {bad}')
    after_l, after_m = 'LAYOUT_PELLUCA_UMBRA_MANOR', 'PellucaUmbraManor'
    cj = os.path.join(IT.C, 'data/maps/PellucaCity/map.json'); city = json.load(open(cj))
    for i, ((k, door, name, r), ox) in enumerate(zip(rooms, x0s)):
        sub = dict(R, grid=R['grid'][:r.H, ox:ox + r.W].copy())
        lid = 'LAYOUT_PELLUCA_HOUSE_' + name[-1]; mid = 'MAP_PELLUCA_HOUSE_' + name[-1]
        m = sorted(mats[k]); m = [m[len(m) // 2]] + [c for c in m if c != m[len(m) // 2]]   # warp 0: the mat's middle
        warps = [{'x': cx - ox, 'y': cy, 'elevation': 0, 'dest_map': 'MAP_PELLUCA_CITY',
                  'dest_warp_id': str(FIRST_CITY_WARP + i)} for cx, cy in m]
        mapj = {'id': mid, 'name': name, 'layout': lid, 'music': 'MUS_LILYCOVE_MUSEUM',
                'region_map_section': 'MAPSEC_PELLUCA_VALLEY', 'requires_flash': False, 'weather': 'WEATHER_NONE',
                'map_type': 'MAP_TYPE_INDOOR', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
                'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
                'object_events': [], 'warp_events': warps, 'coord_events': [], 'bg_events': []}
        IT.write_room(sub, name, lid, PRIM, SEC, mapj, after_layout=after_l, after_map=after_m)
        sp = os.path.join(IT.C, 'data/maps', name, 'scripts.pory')
        if not os.path.exists(sp):
            open(sp, 'w').write(f'// ============ DREAMSTONE RUINATION - Pelluca: house {k} (door {door}) ============\n'
                                f'// Built by tools/art/houses/build_houses.py from houses_mock.py (user design 2026-11-19).\n'
                                f'// Stage 1 (the look). Who lives here, NPCs and dialogue come in stage 2.\n\n'
                                f'mapscripts {name}_MapScripts {{}}\n')
        after_l, after_m = lid, name
        # Pelluca: warp FIRST_CITY_WARP + i at the door, its locked sign gone
        w = {'x': door[0], 'y': door[1], 'elevation': 0, 'dest_map': mid, 'dest_warp_id': '0'}
        ws = city['warp_events']; hit = [j for j, v in enumerate(ws) if (v['x'], v['y']) == door]
        if hit: ws[hit[0]] = w
        else: ws.append(w)
        assert ws.index(w) == FIRST_CITY_WARP + i, (k, ws.index(w))
        city['bg_events'] = [b for b in city['bg_events'] if not ((b['x'], b['y']) == door and b['script'] == 'DR_PellucaCity_DoorLocked')]
        print(f'{k} {name} {r.W}x{r.H} city warp {FIRST_CITY_WARP + i}')
    json.dump(city, open(cj, 'w'), indent=2); open(cj, 'a').write('\n')
    lj = json.load(open(os.path.join(IT.C, 'data/layouts/layouts.json')))
    cl = [l for l in lj['layouts'] if l.get('id') == city['layout']][0]
    cb = os.path.join(IT.C, cl['blockdata_filepath']); data = bytearray(open(cb, 'rb').read())
    for _, door, _ in HOUSES:                                  # the door cells walkable, as the dormitory's
        o = 2 * (door[1] * cl['width'] + door[0]); v = struct.unpack_from('<H', data, o)[0]
        struct.pack_into('<H', data, o, (v & 0x3FF) | IT.FLOOR_E3 << 10)
    open(cb, 'wb').write(data)

if __name__ == '__main__':
    main()
