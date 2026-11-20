"""Build the ice path under Pelluca's church (PellucaIcePath) from its approved mock (user design 2026-11-19).

icepath_mock.py is the picture; this cuts it into its own tileset pair with the image method
(tools/art/academy/imgtiles.py), plus one extra row of variant cells only for their metatiles:
  thin ice -> cracked -> broken (the Sootopolis gym's own three looks), the gate's opening (bare floor), and
  "safe" ice: the thin ice's look with no behaviour (the solved field refreezes solid).
Their ids go to include/constants/metatile_labels.h (METATILE_PellucaIcePath_*) for src/field_tasks.c (the
Sootopolis step callback, made to use them on this layout) and the map scripts.
Collision by hand: the ice and the shrine floor walkable; the boulders, the ice wall and its gate, the statue, fire
rings, logs and flowers, and the ribs' feet solid; the rest of the three ribs over the player (he walks under
and between them).
Warps: 0 the landing (where the split drops you), 1 the ladder in the shrine's corner and 2 the Templars' rope
beside the landing, both up to the church hall (its arrival warp, written by tools/art/templar/build_ruined.py).
Credits as icepath_mock.py.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/icepath/build_icepath.py
"""
import os, sys, re
os.environ.setdefault('ODYSSEY_ROM', '/home/claude/crown/Crown.gba')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'academy'))
import numpy as np
import imgtiles as IT, tilefit
import icepath_mock as M

MB_THIN_ICE, MB_CRACKED_ICE, MB_LADDER = 0x26, 0x27, 0x61
NAME, LAYOUT, MAP = 'PellucaIcePath', 'LAYOUT_PELLUCA_ICE_PATH', 'MAP_PELLUCA_ICE_PATH'
PRIM, SEC = ('pelluca_ice_path_tiles', 'PellucaIcePathTiles'), ('pelluca_ice_path', 'PellucaIcePath')
HALL, HALL_ARRIVAL = 'MAP_PELLUCA_TEMPLAR_HALL', 2          # the hall's warp 2: beside the split (build_ruined.py)
TOTAL = None                                                  # ice cells (set in main; the scripts' target is 1 + it)
VARIANTS = ['thin', 'cracked', 'broken', 'gate_open', 'safe']  # the extra row, left to right

def main():
    img, cells = M.compose(); W, H = M.W, M.H
    # the statue in its ice block has up to 19 colours in an 8x8 tile; merge its rarest near-shades until each tile
    # fits one palette (38 merges, no visible change; the sapphire ring kept)
    img, _ = tilefit.reduce_tiles(img, ((M.STATUE_CX - 1) * 16, 16, (M.STATUE_CX + 2) * 16, (M.STATUE_BASE + 1) * 16))
    ice, ladder_foot, rope, landing = cells['ice'], (M.LADDER[0], M.LADDER[1] + 1), M.ROPE, M.LANDING
    arch, arch_m = cells['arch']
    # the extra row: the variant cells, the rest of the row plain rock
    rock = M.TSI.meta(M.ROCK); row = np.zeros((16, W * 16, 3), np.uint8)
    for x in range(W): row[:, x * 16:x * 16 + 16] = rock
    looks = {'thin': M.SOOT.metatile(M.THIN), 'cracked': M.SOOT.metatile(M.CRACKED), 'broken': M.SOOT.metatile(M.BROKEN),
             'gate_open': rock, 'safe': M.SOOT.metatile(M.THIN)}
    for i, k in enumerate(VARIANTS): row[:, i * 16:i * 16 + 16] = looks[k]
    under = np.vstack([img, row])
    # the ribs: free-standing, so the player can pass under them and between them: each leg's foot solid, every
    # other pixel of them in the over layer (he walks behind a rib north of its feet)
    legs = cells['feet']
    om = np.zeros(under.shape[:2], bool); om[:H * 16] = arch_m; over = np.zeros_like(under); over[:H * 16][arch_m] = arch[arch_m]
    for x, y in legs: om[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = False    # (the feet in the bottom layer)
    solid = cells['statue'] | cells['fires'] | cells['flowers'] | cells['logs'] | legs
    shrine = cells['shrine'] - solid
    walk = ice | shrine | {ladder_foot, rope, landing}
    def beh(x, y):
        if y == H:                                                   # the variant row
            k = VARIANTS[x] if x < len(VARIANTS) else None
            return {'thin': MB_THIN_ICE, 'cracked': MB_CRACKED_ICE}.get(k, 0)
        if (x, y) in ice: return MB_THIN_ICE
        if (x, y) in (ladder_foot, rope): return MB_LADDER
        return 0
    r = IT.build(under, W, H + 1, over=over, om=om, walk=walk, beh=beh, merge=16, rare=300, tries=2000)
    bad = IT.check(r)
    ids = {k: int(r['grid'][H, i] & 0x3FF) for i, k in enumerate(VARIANTS)}
    field_ids = {int(r['grid'][y, x] & 0x3FF) for x, y in ice}
    assert field_ids == {ids['thin']}, (field_ids, ids)             # every field cell is the one thin-ice metatile
    assert len(set(ids.values())) == len(ids), ids
    r['grid'] = r['grid'][:H]
    warps = [{'x': x, 'y': y, 'elevation': 0, 'dest_map': HALL, 'dest_warp_id': str(HALL_ARRIVAL)}
             for x, y in (landing, ladder_foot, rope)]
    mapj = {'id': MAP, 'name': NAME, 'layout': LAYOUT, 'music': 'MUS_SEALED_CHAMBER',
            'region_map_section': 'MAPSEC_PELLUCA_VALLEY', 'requires_flash': False, 'weather': 'WEATHER_NONE',
            'map_type': 'MAP_TYPE_UNDERGROUND', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None, 'object_events': [],
            'warp_events': warps, 'coord_events': [], 'bg_events': []}
    IT.write_room(r, NAME, LAYOUT, PRIM, SEC, mapj, after_layout='LAYOUT_PELLUCA_TEMPLAR_HALL', after_map='PellucaTemplarHall')
    # the metatile ids for C and the scripts (secondary metatiles start at 512)
    lab = os.path.join(IT.C, 'include/constants/metatile_labels.h'); t = open(lab).read()
    block = ('// gTileset_PellucaIcePath (written by tools/art/icepath/build_icepath.py)\n' +
             ''.join(f'#define {"METATILE_PellucaIcePath_" + k.title().replace("_", ""):<38} 0x{ids[k]:03X}\n' for k in VARIANTS))
    t = re.sub(r'// gTileset_PellucaIcePath \(written by[^\n]*\n(#define METATILE_PellucaIcePath_[^\n]*\n)*', '', t)
    t = t.replace('\n#endif // GUARD_METATILE_LABELS_H', block + '\n#endif // GUARD_METATILE_LABELS_H')
    open(lab, 'w').write(t)
    n = len(ice); gx, gy = M.GATE
    sp = os.path.join(IT.C, 'data/maps', NAME, 'scripts.pory')
    open(sp, 'w').write(SCRIPTS.format(target=1 + n, n=n, gx=gx, gy=gy))
    print(f'ice path {W}x{H} tiles {len(r["tiles"])} metatiles {len(r["meta"])} palettes {r["npal"]} mismatches {bad} '
          f'ice cells {n} ids {", ".join(f"{k}=0x{v:03X}" for k, v in ids.items())}')

SCRIPTS = '''// ============ DREAMSTONE RUINATION - Pelluca: the ice path under the church ============
// Written by tools/art/icepath/build_icepath.py (user design 2026-11-19; bible 20_chapter1_build.md).
// The thin-ice field (after Pokemon Pisces' Sootopolis gym): every one of its {n} ice cells must crack exactly once.
// The Sootopolis step callback counts VAR_ICE_STEP_COUNT up from 1 per fresh cell and sets it to 0 on a cracked one.
//   {target} (all cracked): the gate in the ice wall gives way, the field refreezes solid (DrIcePathFreeze), solved.
//   0 (a second step on a cracked cell): the ice breaks; black out, back on the landing with a fresh field.
// NPCs and dialogue (the Templar, the discovery) come with the story pass.

mapscripts PellucaIcePath_MapScripts {{
    MAP_SCRIPT_ON_LOAD {{
        if (flag(FLAG_DR_ICE_PATH_SOLVED)) {{
            setvar(VAR_ICE_STEP_COUNT, 999)
            call(PellucaIcePath_EventScript_SetSolved)
        }} else {{
            special(DrIcePathReset)
        }}
    }}
    MAP_SCRIPT_ON_RESUME {{
        setstepcallback(STEP_CB_SOOTOPOLIS_ICE)
    }}
    MAP_SCRIPT_ON_FRAME_TABLE [
        VAR_ICE_STEP_COUNT, {target}: PellucaIcePath_EventScript_Solved
        VAR_ICE_STEP_COUNT, 0: PellucaIcePath_EventScript_FallThroughIce
    ]
}}

script PellucaIcePath_EventScript_SetSolved {{
    setmetatile({gx}, {gy}, METATILE_PellucaIcePath_GateOpen, FALSE)
    special(DrIcePathFreeze)
    return
}}

script PellucaIcePath_EventScript_Solved {{
    lockall
    setvar(VAR_ICE_STEP_COUNT, 999)
    delay(40)
    playse(SE_ICE_STAIRS)
    call(PellucaIcePath_EventScript_SetSolved)
    special(DrawWholeMapView)
    setflag(FLAG_DR_ICE_PATH_SOLVED)
    releaseall
    end
}}

script PellucaIcePath_EventScript_FallThroughIce {{
    lockall
    delay(20)
    applymovement(OBJ_EVENT_ID_PLAYER, PellucaIcePath_Movement_FallThroughIce)
    waitmovement(0)
    playse(SE_FALL)
    delay(60)
    warpsilent(MAP_PELLUCA_ICE_PATH, 0)
    waitstate
    end
}}

movement PellucaIcePath_Movement_FallThroughIce {{
    set_invisible
}}
'''

if __name__ == '__main__':
    main()
