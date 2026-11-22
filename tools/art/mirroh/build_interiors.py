"""Build Mirroh's seven interiors (approved by the user 2026-11-22, mock v3) as maps of their own, each with its own
tileset pair, from tools/art/mirroh/interiors.py's rooms; wire their exits to the doors build_mirroh.py puts on the
town's buildings (DOORS below, shared with it).

The Tavern carries the core staff every Tavern has (bible §4; shared scripts data/scripts/dr_tavern.pory): healer,
barkeep (Mirroh's own stock, a first pass), the Sage, the Caretaker; standing where Pelluca's stand (the same room).
Whiteout and flying bring the player back to its door (HEAL_LOCATION_MIRROH).
Usage: python3 tools/art/mirroh/build_interiors.py   (after build_mirroh.py; then make)
"""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import mapbuild as MB, interiors as I
C = I.C
MB_NORMAL, MB_SOUTH_ARROW_WARP, MB_COUNTER = 0x00, 0x65, 0x80
# the bar you talk to the staff across (Pelluca's Tavern's row 4, behaviour 0x80; the shop's counters come with its
# shopkeepers in stage 2)
COUNTERS = {'tavern': {(x, 4) for x in range(13)},
            'shop': {(1, 4), (2, 4), (3, 4), (8, 3), (9, 3), (10, 3)}}   # (its two keepers' counters)

# room: (map name, map id, exterior map, the exterior door cells, the interior exit each door brings you to)
DOORS = {
    'tavern':    ('MirrohTavern', 'MAP_MIRROH_TAVERN', 'MAP_MIRROH_UPPER', [(12, 29), (13, 29)], [0, 1]),
    'langerin':  ('MirrohLangerinHall', 'MAP_MIRROH_LANGERIN_HALL', 'MAP_MIRROH_UPPER', [(44, 26)], [1]),
    'chapel':    ('MirrohChapel', 'MAP_MIRROH_CHAPEL', 'MAP_MIRROH_UPPER', [(30, 13), (31, 13)], [1, 2]),
    'snowy':     ('MirrohSnowyHouse', 'MAP_MIRROH_SNOWY_HOUSE', 'MAP_MIRROH_LOWER', [(9, 16)], [0]),
    'cottage':   ('MirrohCottage', 'MAP_MIRROH_COTTAGE', 'MAP_MIRROH_LOWER', [(21, 16)], [0]),
    'townhouse': ('MirrohTownhouse', 'MAP_MIRROH_TOWNHOUSE', 'MAP_MIRROH_LOWER', [(28, 16)], [0]),
    'shop':      ('MirrohSpecialtyShop', 'MAP_MIRROH_SPECIALTY_SHOP', 'MAP_MIRROH_LOWER', [(39, 16)], [0]),
}
UPPER_BASE, LOWER_BASE = 11, 8
# which door each exit leads back out of (default: the door of the same index, the last for any extra exit): you leave
# by the door you came in at
EXIT_DOOR = {'chapel': [0, 0, 1], 'langerin': [0, 0, 0]}          # (the exteriors' own warps come first: build_mirroh appends the doors after them)

def door_warp_ids():
    """{room: [the exterior warp id of each of its doors]}, in the order build_mirroh appends them."""
    out, nu, nl = {}, UPPER_BASE, LOWER_BASE
    for k, (_, _, ext, cells, _) in DOORS.items():
        if ext == 'MAP_MIRROH_UPPER': out[k] = list(range(nu, nu + len(cells))); nu += len(cells)
        else: out[k] = list(range(nl, nl + len(cells))); nl += len(cells)
    return out

TAVERN_STAFF = [('OBJ_EVENT_GFX_WOMAN_5', 4, 3, 'DR_Tavern_Healer'), ('OBJ_EVENT_GFX_COOK', 9, 3, 'MirrohTavern_EventScript_Barkeep'),
                ('OBJ_EVENT_GFX_EXPERT_M', 3, 7, 'DR_Tavern_Sage'), ('OBJ_EVENT_GFX_WOMAN_3', 13, 4, 'DR_Tavern_Caretaker')]
TAVERN_PORY = '''// Mirroh's Tavern (Pelluca's Seaside Tavern room, recoloured to Mirroh's colder palette; build_interiors.py).
// Core staff (bible Section 4): healer, barkeep (Mirroh's stock below, a first pass: [OPEN]), Sage, Caretaker.

mapscripts MirrohTavern_MapScripts {
    MAP_SCRIPT_ON_TRANSITION {
        setrespawn(HEAL_LOCATION_MIRROH)
    }
}

script MirrohTavern_EventScript_Barkeep {
    lock
    faceplayer
    speakername("Barkeep")
    message(format("Cold out there. Stock up before you go."))
    waitmessage
    pokemart(MirrohTavern_Stock)
    speakername("Barkeep")
    msgbox(format("Keep warm."))
    closemessage
    release
    end
}

mart MirrohTavern_Stock {
    ITEM_POTION
    ITEM_SUPER_POTION
    ITEM_POKE_BALL
    ITEM_ANTIDOTE
    ITEM_PARALYZE_HEAL
    ITEM_BURN_HEAL
    ITEM_ICE_HEAL
    ITEM_AWAKENING
}
'''

def obj(gfx, x, y, script):
    return {'graphics_id': gfx, 'x': x, 'y': y, 'elevation': 3, 'movement_type': 'MOVEMENT_TYPE_FACE_DOWN',
            'movement_range_x': 0, 'movement_range_y': 0, 'trainer_type': 'TRAINER_TYPE_NONE',
            'trainer_sight_or_berry_tree_id': '0', 'script': script, 'flag': '0'}

def build_room(k, ids):
    name, mid, ext, cells, _ = DOORS[k]
    img, solid, exits = I.ROOMS[k]()
    H, W = solid.shape
    black = {(x, y) for y in range(H) for x in range(W) if img[y * 16:y * 16 + 16, x * 16:x * 16 + 16].max() < 12}
    walk = ({(x, y) for y in range(H) for x in range(W) if not solid[y, x]} - black) | set(exits)
    ctr = COUNTERS.get(k, set())
    beh = lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) in exits else MB_COUNTER if (x, y) in ctr else MB_NORMAL
    r = MB.build(img, None, None, W, H, walk, beh)
    ed = EXIT_DOOR.get(k, [min(i, len(ids) - 1) for i in range(len(exits))])
    warps = [{'x': x, 'y': y, 'elevation': 3, 'dest_map': ext, 'dest_warp_id': str(ids[ed[i]])}
             for i, (x, y) in enumerate(exits)]
    objs = [obj(*s) for s in TAVERN_STAFF] if k == 'tavern' else []
    j = {'id': mid, 'name': name, 'layout': 'LAYOUT_' + mid[4:], 'music': 'MUS_DEWFORD' if k == 'tavern' else 'MUS_LILYCOVE_MUSEUM',
         'region_map_section': 'MAPSEC_MIRROH', 'requires_flash': False, 'weather': 'WEATHER_NONE',
         'map_type': 'MAP_TYPE_INDOOR', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': k != 'tavern',
         'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
         'object_events': objs, 'warp_events': warps, 'coord_events': [], 'bg_events': []}
    bk = next((int(r['grid'][y, x] & 0x3FF) for (x, y) in sorted(black)), int(r['grid'][0, 0] & 0x3FF))
    low = 'mirroh_int_' + k
    MB.write(r, name, 'LAYOUT_' + mid[4:], (low + '_tiles', ''.join(w.capitalize() for w in low.split('_')) + 'Tiles'),
             (low, ''.join(w.capitalize() for w in low.split('_'))), j, border=[bk] * 4)
    if k == 'tavern': open(os.path.join(C, 'data/maps', name, 'scripts.pory'), 'w').write(TAVERN_PORY)
    return r

def heal_location():
    """HEAL_LOCATION_MIRROH (41): outside the Tavern's door; flying to Mirroh lands there too."""
    h = os.path.join(C, 'include/constants/heal_locations.h'); t = open(h).read()
    if 'HEAL_LOCATION_MIRROH ' not in t:
        t = t.replace('#define HEAL_LOCATION_CHAMPIONSHIP_CORRIDOR 40\n',
                      '#define HEAL_LOCATION_CHAMPIONSHIP_CORRIDOR 40\n#define HEAL_LOCATION_MIRROH 41\n'); open(h, 'w').write(t)
    d = os.path.join(C, 'src/data/heal_locations.h'); t = open(d).read()
    line = '    [HEAL_LOCATION_MIRROH - 1] = {MAP_GROUP(MIRROH_UPPER), MAP_NUM(MIRROH_UPPER), 12, 30},\n'
    if 'HEAL_LOCATION_MIRROH - 1' not in t:
        i = t.rindex('};'); t = t[:i] + line + t[i:]; open(d, 'w').write(t)
    rm = os.path.join(C, 'src/region_map.c'); t = open(rm).read()
    t = t.replace('[MAPSEC_MIRROH] = {MAP_GROUP(MIRROH_BASE_CAMP), MAP_NUM(MIRROH_BASE_CAMP), HEAL_LOCATION_MIRROH_BASE_CAMP},',
                  '[MAPSEC_MIRROH] = {MAP_GROUP(MIRROH_UPPER), MAP_NUM(MIRROH_UPPER), HEAL_LOCATION_MIRROH},')
    open(rm, 'w').write(t)

def main():
    ids = door_warp_ids()
    for k in DOORS:
        r = build_room(k, ids[k]); print(k, DOORS[k][0], "ok")
    heal_location()

if __name__ == '__main__':
    main()
