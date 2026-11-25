"""Build Hollow Hill's summit into the game (mock v2, compose_summit.py; user 2026-11-25: "looks really awesome").
A new map, MAP_HOLLOW_HILL_SUMMIT (HollowHillSummit, 43x49), on its own tileset pair (tools/art/mapbuild.py).

Cells: walkable = what the mock's walk check reaches (the court, the bastion's own walkable cells from MonoMyth's
collision, the sunk stair); everything else solid, one level (elevation 3). The lair's door (the burst arch, (21, 5))
is solid for now: the guardian's quest (stage 3, post-midgame) opens it. Top layer: the bastion's columns (MonoMyth's
own top layer), the plinths' and trees' upper parts, the webs.
Warps: 0-2, the sunk stair's lower step (20-22, 42), MB_DEEP_SOUTH_WARP, down to Hollow Hill warp 0 (the sealed door's
forecourt, (29, 36): a landing only, no trigger). Arriving on warp 1 the player faces north and steps up onto the
summit. Nothing leads up yet: Hollow Hill's sealed door stays shut in Chapter 1 (the tunnel is a later map).
Weather and music as Hollow Hill's; its map section too, so it gets Hollow Hill's thinned fog (field_weather_effect.c
picks it by map section).
Usage: python3 tools/art/hollowhill/ruin/build_summit.py   (then make)"""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import compose_summit as CS
import mapbuild as MB
import tilequant as TQN
C = MB.C
NAME, LAYOUT, MAPID = 'HollowHillSummit', 'LAYOUT_HOLLOW_HILL_SUMMIT', 'MAP_HOLLOW_HILL_SUMMIT'
W, H, S = CS.W, CS.H, CS.S
MB_DEEP_SOUTH_WARP = 0x6E
STEP = [(CS.AX - 1, CS.ARRIVE[1] + 1), (CS.AX, CS.ARRIVE[1] + 1), (CS.AX + 1, CS.ARRIVE[1] + 1)]

def main():
    cv, E, F, used, door, fm = CS.compose()
    miss, seen = CS.walk_check(E, used, door); assert not miss, miss
    under = cv.img.copy(); under[cv.mid_a] = cv.mid[cv.mid_a]
    flat = cv.flat()
    both = np.concatenate([flat, under], 0).astype(int)
    q, _ = TQN.quantise(both, n=13); q = q.astype(np.uint8)
    flat_q, under_q = q[:H * S], q[H * S:]
    walk = set(seen) - {door}
    for c in STEP: assert c in walk, ('the stair step is not walkable', c)
    beh = lambda x, y: MB_DEEP_SOUTH_WARP if (x, y) in STEP else 0
    b = MB.build(under_q, None, (flat_q, cv.top_a), W, H, walk, beh)
    g = b['grid']
    for y in range(H):
        for x in range(W):
            g[y, x] = (g[y, x] & 0x3FF) | ((0 if (x, y) in walk else 1) << 10) | (3 << 12)
    border = int(g[H - 1, 0] & 0x3FF)
    mapj = {'id': MAPID, 'name': NAME, 'layout': LAYOUT, 'music': 'MUS_DR_HOLLOW_HILL',
            'region_map_section': 'MAPSEC_DR_HOLLOW_HILL', 'requires_flash': False, 'weather': 'WEATHER_FOG_HORIZONTAL',
            'map_type': 'MAP_TYPE_ROUTE', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
            'object_events': [], 'coord_events': [], 'bg_events': [],
            'warp_events': [{'x': x, 'y': y, 'elevation': 3, 'dest_map': 'MAP_HOLLOW_HILL', 'dest_warp_id': '0'} for x, y in STEP]}
    MB.write(b, NAME, LAYOUT, ('hollow_hill_summit_tiles', 'HollowHillSummitTiles'), ('hollow_hill_summit', 'HollowHillSummit'),
             mapj, border=[border] * 4, after_layout='LAYOUT_HOLLOW_HILL', after_map='HollowHill')
    # Hollow Hill: warp 0, the sealed door's forecourt (a landing for the way down; no trigger: plain ground)
    p = os.path.join(C, 'data/maps/HollowHill/map.json'); j = json.load(open(p))
    j['warp_events'] = [{'x': 29, 'y': 36, 'elevation': 3, 'dest_map': MAPID, 'dest_warp_id': '1'}]
    json.dump(j, open(p, 'w'), indent=2); open(p, 'a').write('\n')
    print('summit built: tiles', len(b['tiles']), 'metatiles', len(b['meta']), 'palettes', len(b['pals']), 'walkable', len(walk))
    from PIL import Image
    Image.fromarray(MB.render(b)).save('/tmp/summit/summit_built.png')

if __name__ == '__main__':
    main()
