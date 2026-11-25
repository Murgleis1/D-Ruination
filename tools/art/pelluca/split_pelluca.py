"""Split Pelluca Valley into the town (PellucaCity, cut to 80 x 42) and the harbour (PellucaHarbour, build_harbour.py)
(user 2026-11-25). Run after build_harbour.py. Idempotent on a clean checkout of PellucaCity (it reads the 80 x 60 map
from git at PRE_SPLIT, rows 0-35 as built before the split).

The town: rows 0-33 unchanged; rows 34-39 the retaining wall six courses high (its top course, then its second five
times; the cave door gone from this side: it is at the wall's foot on the harbour), both stairs its full height; row 36
of each stair is a new metatile (a copy of the stair's, MB_DEEP_SOUTH_WARP): stepping onto it going down fades to the
harbour; arriving on it from the harbour the player faces north and takes one step up. Rows 40-41: what lies below the
wall's foot, seen only from the stairs (the Tavern's and the lab's roofs, sand, quay stone), all solid.
Warps: 1 and 2 (the lab and the Tavern before) become the west stair's (24, 36) and (25, 36); 10-12 the main stair's
(37-39, 36); the others keep their numbers (other maps point at them). The waterfront's people, ships, shrine and
signs move to the harbour, its arrival scene too.
Usage: python3 tools/art/pelluca/split_pelluca.py"""
import os, sys, json, struct, subprocess, re
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..')); C = os.path.join(ROOT, 'codebase')
W, OLD_H, H = 80, 60, 42
DY = 27
STAIRS = {24: 204, 25: 205, 37: 208, 38: 209, 39: 209}
MB_DEEP_SOUTH_WARP = 0x6E
PRIM = os.path.join(C, 'data/tilesets/primary/cormoria')

PRE_SPLIT = 'b1b53ecde~1'                    # (the last commit with the 80 x 60 Pelluca)
def git_bytes(path):
    return subprocess.run(['git', 'show', PRE_SPLIT + ':codebase/' + path], cwd=ROOT, capture_output=True, check=True).stdout

def warp_metatiles():
    """copies of the stair metatiles 204, 205, 208, 209 with the warp behaviour, appended to the Cormoria primary
    (kept if already there)"""
    mt = bytearray(open(os.path.join(PRIM, 'metatiles.bin'), 'rb').read())
    at = bytearray(open(os.path.join(PRIM, 'metatile_attributes.bin'), 'rb').read())
    n = len(at) // 2; out = {}
    for src in (204, 205, 208, 209):
        ent = mt[src * 24:(src + 1) * 24]; a = (struct.unpack_from('<H', at, src * 2)[0] & 0xFF00) | MB_DEEP_SOUTH_WARP
        found = None
        for m in range(n):
            if mt[m * 24:(m + 1) * 24] == ent and struct.unpack_from('<H', at, m * 2)[0] == a: found = m; break
        if found is None:
            found = n; mt += ent; at += struct.pack('<H', a); n += 1
        out[src] = found
    assert n <= 512
    open(os.path.join(PRIM, 'metatiles.bin'), 'wb').write(mt); open(os.path.join(PRIM, 'metatile_attributes.bin'), 'wb').write(at)
    return out

def town_grid(warp_m):
    old = np.frombuffer(git_bytes('data/layouts/PellucaCity/map.bin'), '<u2').reshape(OLD_H, W).copy()
    g = np.zeros((H, W), np.uint16)
    g[:34] = old[:34]
    ID = lambda v: int(v) & 0x3FF
    for r, y in enumerate(range(34, 40)):
        src = old[34] if r == 0 else old[35]
        for x in range(W):
            m = ID(src[x])
            if x in (10, 11): m = ID(old[34 if r == 0 else 35, 14])          # (plain wall: the cave door is below)
            stair = x in STAIRS
            if stair and y == 36: m = warp_m[STAIRS[x]]
            if stair and y <= 36: col, el = 0, (0 if y == 34 else 3)
            elif x < 8 or x >= 72: col, el = (int(src[x]) >> 10) & 3, int(src[x]) >> 12
            else: col, el = 1, 0
            g[y, x] = m | col << 10 | el << 12
    # the foot: the Tavern's roof (old rows 36-37), the lab's (old rows 40-41: it moved up four), sand, quay stone
    sand, stone = ID(old[36, 14]), ID(old[38, 40])
    for r, y in enumerate((40, 41)):
        for x in range(W):
            if x < 8 or x >= 72: m = ID(old[36 + r, x])
            elif 25 <= x <= 31: m = ID(old[36 + r, x])
            elif 44 <= x <= 49: m = ID(old[40 + r, x])
            elif x < 32: m = sand
            else: m = stone
            g[y, x] = m | 1 << 10
    return g

def town_events():
    p = os.path.join(C, 'data/maps/PellucaCity/map.json')
    j = json.loads(git_bytes('data/maps/PellucaCity/map.json'))
    moved = [o for o in j['object_events'] if o['y'] >= 32]
    j['object_events'] = [o for o in j['object_events'] if o['y'] < 32]
    j['bg_events'] = [e for e in j['bg_events'] if e['y'] < 32]
    w = j['warp_events']
    w[1] = {'x': 24, 'y': 36, 'elevation': 3, 'dest_map': 'MAP_PELLUCA_HARBOUR', 'dest_warp_id': '2'}
    w[2] = {'x': 25, 'y': 36, 'elevation': 3, 'dest_map': 'MAP_PELLUCA_HARBOUR', 'dest_warp_id': '3'}
    for k, x in enumerate((37, 38, 39)):
        w.append({'x': x, 'y': 36, 'elevation': 3, 'dest_map': 'MAP_PELLUCA_HARBOUR', 'dest_warp_id': str(4 + k)})
    json.dump(j, open(p, 'w'), indent=2); open(p, 'a').write('\n')
    return moved

def harbour_events():
    p = os.path.join(C, 'data/maps/PellucaHarbour/map.json'); j = json.load(open(p))
    def obj(gfx, x, y, script='NULL', flag='0', move='MOVEMENT_TYPE_NONE', rx=0, ry=0, extra='0'):
        return {'graphics_id': gfx, 'x': x, 'y': y, 'elevation': 3, 'movement_type': move, 'movement_range_x': rx,
                'movement_range_y': ry, 'trainer_type': 'TRAINER_TYPE_NONE', 'trainer_sight_or_berry_tree_id': extra,
                'script': script, 'flag': flag}
    j['object_events'] = [
        obj('OBJ_EVENT_GFX_PALE_VELUZA', 46, 23, flag='FLAG_UNUSED_0x884'),                         # 1 the Pale Veluza
        obj('OBJ_EVENT_GFX_CADMUS', 40, 15, flag='FLAG_UNUSED_0x884', move='MOVEMENT_TYPE_FACE_DOWN'),   # 2
        obj('OBJ_EVENT_GFX_DR_SHRINE', 38, 11, 'DR_PellucaCity_Shrine', move='MOVEMENT_TYPE_FACE_DOWN'),  # 3
        obj('OBJ_EVENT_GFX_OLD_WOMAN', 36, 11, 'DR_PellucaCity_ShrineKeeper', move='MOVEMENT_TYPE_FACE_RIGHT'),  # 4
        obj('OBJ_EVENT_GFX_MERCHANTMAN', 60, 24),                                                    # 5
        obj('OBJ_EVENT_GFX_FISHING_SLOOP', 57, 19),                                                  # 6
        obj('OBJ_EVENT_GFX_WOODEN_ROWBOAT', 32, 21),                                                 # 7
        obj('OBJ_EVENT_GFX_WOODEN_ROWBOAT', 70, 18),                                                 # 8
        obj('OBJ_EVENT_GFX_BOY_2', 52, 11, 'PellucaCity_NPC7', move='MOVEMENT_TYPE_WANDER_AROUND', rx=1, ry=1),
        obj('OBJ_EVENT_GFX_MAN_1', 12, 15, 'PellucaCity_NPC6', move='MOVEMENT_TYPE_WANDER_AROUND', rx=2, ry=1),
        obj('OBJ_EVENT_GFX_TUBER_M', 20, 15, 'PellucaCity_NPC1', move='MOVEMENT_TYPE_WANDER_AROUND', rx=2, ry=1),
        obj('OBJ_EVENT_GFX_SPECIES(LYCANROC)', 13, 16, 'PellucaCity_Lycanroc', move='MOVEMENT_TYPE_WANDER_AROUND', rx=1, ry=1),
        obj('OBJ_EVENT_GFX_SPECIES(SEALEO)', 22, 18, 'PellucaCity_Sealeo', move='MOVEMENT_TYPE_FACE_RIGHT'),
        obj('OBJ_EVENT_GFX_WOMAN_2', 53, 13, 'PellucaCity_NPC10', move='MOVEMENT_TYPE_FACE_DOWN'),
        obj('OBJ_EVENT_GFX_TMHM_BALL', 52, 20, 'Common_EventScript_FindItem', flag='FLAG_ITEM_PELLUCA_CITY_B',
            move='MOVEMENT_TYPE_LOOK_AROUND', extra='ITEM_TM40'),
    ]
    j['warp_events'] = [
        {'x': 28, 'y': 16, 'elevation': 3, 'dest_map': 'MAP_PELLUCA_CITY_POKEMON_CENTER', 'dest_warp_id': '0'},
        {'x': 47, 'y': 12, 'elevation': 3, 'dest_map': 'MAP_PELLUCA_UMBRA_LAB', 'dest_warp_id': '0'},
        {'x': 24, 'y': 6, 'elevation': 3, 'dest_map': 'MAP_PELLUCA_CITY', 'dest_warp_id': '1'},
        {'x': 25, 'y': 6, 'elevation': 3, 'dest_map': 'MAP_PELLUCA_CITY', 'dest_warp_id': '2'},
        {'x': 37, 'y': 6, 'elevation': 3, 'dest_map': 'MAP_PELLUCA_CITY', 'dest_warp_id': '10'},
        {'x': 38, 'y': 6, 'elevation': 3, 'dest_map': 'MAP_PELLUCA_CITY', 'dest_warp_id': '11'},
        {'x': 39, 'y': 6, 'elevation': 3, 'dest_map': 'MAP_PELLUCA_CITY', 'dest_warp_id': '12'}]
    sign = lambda x, y, s, f='BG_EVENT_PLAYER_FACING_ANY': {'type': 'sign', 'x': x, 'y': y, 'elevation': 0,
                                                            'player_facing_dir': f, 'script': s}
    j['bg_events'] = [sign(23, 17, 'DR_PellucaCity_SignInn'), sign(24, 17, 'DR_PellucaCity_SignInn'),
                      sign(10, 8, 'DR_PellucaCity_CaveSealed', 'BG_EVENT_PLAYER_FACING_NORTH'),
                      sign(11, 8, 'DR_PellucaCity_CaveSealed', 'BG_EVENT_PLAYER_FACING_NORTH')]
    j['coord_events'] = []
    j['show_map_name'] = False
    json.dump(j, open(p, 'w'), indent=2); open(p, 'a').write('\n')

HARBOUR_SCRIPTS = r'''mapscripts PellucaHarbour_MapScripts {
    MAP_SCRIPT_ON_TRANSITION {
        setflag(FLAG_VISITED_PELLUCA_CITY)
    }
    MAP_SCRIPT_ON_FRAME_TABLE [
        VAR_UNUSED_0x404E, 1: PellucaHarbour_Arrival
    ]
}

const LOCALID_HB_VELUZA = 1
const LOCALID_HB_CADMUS = 2

// The cold open's arrival (moved from PellucaCity with the waterfront, user 2026-11-25). Osrid lands at (40, 21) off
// the Pale Veluza; Cadmus comes down the great pier from (40, 15); both walk up it; Osrid stops at the shrine to the
// lost prince (38, 11) while Cadmus goes on along the kerb (row 14) and up to the lab door (47, 12). The walk is kept clear
// (tools/art/pelluca/waterfront_mock.py check_walk).
script PellucaHarbour_Arrival {
    lockall
    setvar(VAR_UNUSED_0x404E, 2)
    applymovement(OBJ_EVENT_ID_PLAYER, moves(face_up))
    waitmovement(0)
    delay(20)
    speakername("Dockhand")
    msgbox(format("A Rainhawk, in a mask? Like something out of the old stories."))
    speakername("Sailor")
    msgbox(format("That's the one who held the beach at Sevii. Burned for it, they say."))
    closemessage
    delay(30)
    applymovement(LOCALID_HB_CADMUS, moves(walk_down * 5))
    waitmovement(0)
    delay(12)
    showportrait(PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE)
    msgbox(format("Rainhawk Alban. Welcome to Pelluca Valley."))
    closemessage
    delay(40)
    showportrait(PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL)
    msgbox(format("And the burns? Are they healing?"))
    showportrait(PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL)
    speakername("“Nomad”")
    msgbox(format("Slowly. The mask helps."))
    showportrait(PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL)
    msgbox(format("Good. Walk with me. We will talk somewhere quieter."))
    hideportrait
    closemessage
    release
    delay(12)
    applymovement(LOCALID_HB_CADMUS, moves(walk_up * 6 walk_right * 7 face_left))
    applymovement(OBJ_EVENT_ID_PLAYER, moves(walk_up * 7 walk_left * 2 walk_up * 2 face_up))
    waitmovement(0)
    waitmovement(LOCALID_HB_CADMUS)
    delay(30)
    msgbox(format("For Prince {PLAYER}, Keerin's Chosen. Wherever you are, come home."), MSGBOX_SIGN)
    closemessage
    delay(40)
    showportrait(PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL)
    msgbox(format("Rainhawk."))
    hideportrait
    closemessage
    applymovement(LOCALID_HB_CADMUS, moves(walk_up face_up))
    waitmovement(0)
    delay(12)
    playse(SE_EXIT)
    removeobject(LOCALID_HB_CADMUS)
    delay(16)
    applymovement(OBJ_EVENT_ID_PLAYER, moves(walk_down * 2 walk_right * 9 walk_up face_up))
    waitmovement(0)
    delay(12)
    setflag(FLAG_UNUSED_0x884)
    warp(MAP_PELLUCA_UMBRA_LAB, 0)
    waitstate
    end
}
'''

def scripts():
    open(os.path.join(C, 'data/maps/PellucaHarbour/scripts.pory'), 'w').write(HARBOUR_SCRIPTS)
    sp = os.path.join(C, 'data/maps/PellucaCity/scripts.pory'); s = open(sp).read()
    s = s.replace("    MAP_SCRIPT_ON_FRAME_TABLE [\n        VAR_UNUSED_0x404E, 1: DR_PellucaCity_Arrival\n    ]    \n", "")
    open(sp, 'w').write(s)
    rp = os.path.join(C, 'data/maps/PellucaReflection/scripts.pory'); r = open(rp).read()
    r = r.replace('warp(MAP_PELLUCA_CITY, 44, 52)', 'warp(MAP_PELLUCA_HARBOUR, 40, 21)'); open(rp, 'w').write(r)
    hp = os.path.join(C, 'src/data/heal_locations.h'); h = open(hp).read()
    h = h.replace('[HEAL_LOCATION_PELLUCA_CITY - 1] = {MAP_GROUP(PELLUCA_CITY), MAP_NUM(PELLUCA_CITY), 28, 44}',
                  '[HEAL_LOCATION_PELLUCA_CITY - 1] = {MAP_GROUP(PELLUCA_HARBOUR), MAP_NUM(PELLUCA_HARBOUR), 28, 17}')
    open(hp, 'w').write(h)
    for m, wid in (('PellucaCityPokemonCenter', '0'), ('PellucaUmbraLab', '1')):
        p = os.path.join(C, 'data/maps', m, 'map.json'); j = json.load(open(p))
        for w in j['warp_events']:
            if w['dest_map'] == 'MAP_PELLUCA_CITY': w['dest_map'] = 'MAP_PELLUCA_HARBOUR'; w['dest_warp_id'] = wid
        json.dump(j, open(p, 'w'), indent=2); open(p, 'a').write('\n')

def main():
    wm = warp_metatiles(); print('warp metatiles', wm)
    g = town_grid(wm)
    g.astype('<u2').tofile(os.path.join(C, 'data/layouts/PellucaCity/map.bin'))
    lj = os.path.join(C, 'data/layouts/layouts.json'); L = json.load(open(lj))
    for l in L['layouts']:
        if l.get('id') == 'LAYOUT_PELLUCA_CITY': l['height'] = H
    json.dump(L, open(lj, 'w'), indent=2); open(lj, 'a').write('\n')
    moved = town_events(); print('moved off the town:', len(moved), 'objects')
    harbour_events(); scripts()

if __name__ == '__main__':
    main()
