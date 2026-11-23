"""Build the Templar Citadel's four courtyard houses into the game (user 2026-11-23: "proceed with putting them all
into the game"), each a map with its own tileset pair (tools/art/mapbuild.py), from the approved mocks:

  the Tavern     tavern.room()        Pelluca's Tavern room in the Citadel's colours; the core staff every Tavern has
                                      (healer, barkeep, Sage, Caretaker; data/scripts/dr_tavern.pory), standing where
                                      Mirroh's stand; whiteout comes back to its door (HEAL_LOCATION_TEMPLAR_HQ).
  the barracks   barracks3.room()     mock v3, from the user's station-barracks reference.
  the armoury    houses.armoury()     mock v2, a working smithy.
  the watch house houses.watch()      mock v1, the command post for the Route 15 incident.

The courtyard's doors (build_citadel.py HOUSE_DOORS) follow the church's warp 0, in HOUSES order; each house's exit
mat (its last floor row) leads back out of the door you came in at. The barracks', armoury's and watch house's people
are stage 2. Usage: python3 tools/art/templar_hq/citadel_rooms/build_houses.py   (then build_citadel.py; then make)
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); TQ = os.path.dirname(HERE)
for d in (HERE, TQ, os.path.join(TQ, '..'), os.path.join(TQ, '..', 'mirroh')): sys.path.insert(0, d)
import mapbuild as MB
C = MB.C
MB_NORMAL, MB_SOUTH_ARROW_WARP, MB_COUNTER = 0x00, 0x65, 0x80
SCR = '/tmp/citadel_houses'; os.makedirs(SCR, exist_ok=True)

# key: (map name, map id, the courtyard's door cells (shared with build_citadel.py), music)
HOUSES = {
    'tavern':   ('TemplarCitadelTavern', 'MAP_TEMPLAR_CITADEL_TAVERN', [(4, 28)], 'MUS_DEWFORD'),
    'barracks': ('TemplarCitadelBarracks', 'MAP_TEMPLAR_CITADEL_BARRACKS', [(35, 28)], 'MUS_DR_MM_ROUTE15'),
    'armoury':  ('TemplarCitadelArmoury', 'MAP_TEMPLAR_CITADEL_ARMOURY', [(6, 12), (7, 12)], 'MUS_DR_MM_ROUTE15'),
    'watch':    ('TemplarCitadelWatchHouse', 'MAP_TEMPLAR_CITADEL_WATCH_HOUSE', [(31, 12), (32, 12)], 'MUS_DR_MM_ROUTE15'),
}
FIRST_DOOR_WARP = 1                       # (the courtyard's warp 0 is the church door)

def door_warp_ids():
    """{house: [the courtyard warp id of each of its doors]}, in the order build_citadel.py appends them."""
    out, n = {}, FIRST_DOOR_WARP
    for k, (_, _, cells, _) in HOUSES.items():
        out[k] = list(range(n, n + len(cells))); n += len(cells)
    return out

def entry_warp(k):
    """The interior warp each courtyard door brings you to: the matching mat cell, or the mat's middle."""
    n_exits = {'tavern': 2, 'barracks': 3, 'armoury': 2, 'watch': 2}[k]
    cells = HOUSES[k][2]
    return [i for i in range(len(cells))] if len(cells) == n_exits else [n_exits // 2] * len(cells)

def picture(k):
    if k == 'tavern':
        import tavern; return tavern.room()
    if k == 'barracks':
        import barracks3; return barracks3.room()
    import houses
    return {'armoury': houses.armoury, 'watch': houses.watch}[k]()

TAVERN_STAFF = [('OBJ_EVENT_GFX_WOMAN_5', 4, 3, 'DR_Tavern_Healer'), ('OBJ_EVENT_GFX_COOK', 9, 3, 'TemplarCitadelTavern_EventScript_Barkeep'),
                ('OBJ_EVENT_GFX_EXPERT_M', 3, 7, 'DR_Tavern_Sage'), ('OBJ_EVENT_GFX_WOMAN_3', 13, 4, 'DR_Tavern_Caretaker')]
TAVERN_PORY = '''// The Citadel's Tavern (Pelluca's Seaside Tavern room in the Citadel's colours; citadel_rooms/build_houses.py).
// Core staff (bible Section 4): healer, barkeep (the Citadel's stock below, a first pass: [OPEN]), Sage, Caretaker.

mapscripts TemplarCitadelTavern_MapScripts {
    MAP_SCRIPT_ON_TRANSITION {
        setrespawn(HEAL_LOCATION_TEMPLAR_HQ)
    }
}

script TemplarCitadelTavern_EventScript_Barkeep {
    lock
    faceplayer
    speakername("Barkeep")
    message(format("Mountain air works up a hunger. Need anything for the road?"))
    waitmessage
    pokemart(TemplarCitadelTavern_Stock)
    speakername("Barkeep")
    msgbox(format("Arceus keep you."))
    closemessage
    release
    end
}

mart TemplarCitadelTavern_Stock {
    ITEM_POTION
    ITEM_SUPER_POTION
    ITEM_POKE_BALL
    ITEM_GREAT_BALL
    ITEM_ANTIDOTE
    ITEM_PARALYZE_HEAL
    ITEM_BURN_HEAL
    ITEM_ICE_HEAL
    ITEM_AWAKENING
    ITEM_REPEL
}
'''

def obj(gfx, x, y, script):
    return {'graphics_id': gfx, 'x': x, 'y': y, 'elevation': 3, 'movement_type': 'MOVEMENT_TYPE_FACE_DOWN',
            'movement_range_x': 0, 'movement_range_y': 0, 'trainer_type': 'TRAINER_TYPE_NONE',
            'trainer_sight_or_berry_tree_id': '0', 'script': script, 'flag': '0'}

def build(k, ids):
    import tilequant as TQN
    name, mid, cells, music = HOUSES[k]
    img, solid, exits = picture(k)
    img = np.asarray(img).astype(int); H, W = solid.shape
    img, _ = TQN.quantise(img, n=13)
    img = img.astype(np.uint8)
    black = {(x, y) for y in range(H) for x in range(W) if img[y * 16:y * 16 + 16, x * 16:x * 16 + 16].max() < 12}
    walk = ({(x, y) for y in range(H) for x in range(W) if not solid[y, x]} - black) | set(exits)
    ctr = {(x, 4) for x in range(13)} if k == 'tavern' else set()        # (the bar you talk to the staff across)
    beh = lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) in exits else MB_COUNTER if (x, y) in ctr else MB_NORMAL
    r = MB.build(img, None, None, W, H, walk, beh)
    out = [i if len(ids) == len(exits) else 0 for i in range(len(exits))]   # (a one-door house: every mat cell to it)
    warps = [{'x': x, 'y': y, 'elevation': 3, 'dest_map': 'MAP_TEMPLAR_CITADEL', 'dest_warp_id': str(ids[out[i]])}
             for i, (x, y) in enumerate(exits)]
    objs = [obj(*s) for s in TAVERN_STAFF] if k == 'tavern' else []
    j = {'id': mid, 'name': name, 'layout': 'LAYOUT_' + mid[4:], 'music': music,
         'region_map_section': 'MAPSEC_DR_TEMPLAR_HQ', 'requires_flash': False, 'weather': 'WEATHER_NONE',
         'map_type': 'MAP_TYPE_INDOOR', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': k != 'tavern',
         'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
         'object_events': objs, 'warp_events': warps, 'coord_events': [], 'bg_events': []}
    bk = next((int(r['grid'][y, x] & 0x3FF) for (x, y) in sorted(black)), int(r['grid'][0, 0] & 0x3FF))
    low = 'templar_cit_' + k
    cam = ''.join(w.capitalize() for w in low.split('_'))
    MB.write(r, name, 'LAYOUT_' + mid[4:], (low + '_tiles', cam + 'Tiles'), (low, cam), j, border=[bk] * 4,
             after_layout='LAYOUT_TEMPLAR_CITADEL', after_map='TemplarCitadel')
    pory = TAVERN_PORY if k == 'tavern' else ('// %s (citadel_rooms/build_houses.py). Its people are stage 2.\n\nmapscripts %s_MapScripts {}\n' % (name, name))
    open(os.path.join(C, 'data/maps', name, 'scripts.pory'), 'w').write(pory)
    Image.fromarray(MB.render(r)).save(os.path.join(SCR, k + '_built.png'))
    print(k, name, W, 'x', H, 'exits', exits, '->', [w['dest_warp_id'] for w in warps])

def heal_location():
    """HEAL_LOCATION_TEMPLAR_HQ (42): outside the Tavern's door, (4, 29); flying to the Citadel lands there too."""
    h = os.path.join(C, 'include/constants/heal_locations.h'); t = open(h).read()
    if 'HEAL_LOCATION_TEMPLAR_HQ ' not in t:
        t = t.replace('#define HEAL_LOCATION_MIRROH 41\n', '#define HEAL_LOCATION_MIRROH 41\n#define HEAL_LOCATION_TEMPLAR_HQ 42\n'); open(h, 'w').write(t)
    d = os.path.join(C, 'src/data/heal_locations.h'); t = open(d).read()
    line = '    [HEAL_LOCATION_TEMPLAR_HQ - 1] = {MAP_GROUP(TEMPLAR_CITADEL), MAP_NUM(TEMPLAR_CITADEL), 4, 29},\n'
    if 'HEAL_LOCATION_TEMPLAR_HQ - 1' not in t:
        i = t.rindex('};'); t = t[:i] + line + t[i:]; open(d, 'w').write(t)
    rm = os.path.join(C, 'src/region_map.c'); t = open(rm).read()
    if '[MAPSEC_DR_TEMPLAR_HQ]' not in t:
        a = '    [MAPSEC_MIRROH] = {MAP_GROUP(MIRROH_UPPER), MAP_NUM(MIRROH_UPPER), HEAL_LOCATION_MIRROH},\n'
        t = t.replace(a, a + '    [MAPSEC_DR_TEMPLAR_HQ] = {MAP_GROUP(TEMPLAR_CITADEL), MAP_NUM(TEMPLAR_CITADEL), HEAL_LOCATION_TEMPLAR_HQ},\n'); open(rm, 'w').write(t)

def main():
    ids = door_warp_ids()
    for k in HOUSES: build(k, ids[k])
    heal_location()

if __name__ == '__main__':
    main()
