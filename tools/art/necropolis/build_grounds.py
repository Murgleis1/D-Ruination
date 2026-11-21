"""Build the Mirroh Necropolis grounds into the game from their approved mock (grounds_mock.py; user 2026-11-21
"Looks good overall"): MAP_NECROPOLIS_GROUNDS, its own tileset pair (tools/art/mapbuild.py: ground on the bottom
layer, everything standing on it on the middle layer).

Ways: the foot of the way in (x 20-23, the bottom row) is a south arrow warp back to Mirroh's skull gate (Upper
Mirroh); the grand entrance's dark doorway (21, 15) is a door down to the frozen lake's landing. Walls, the
entrance's body, trees, hedges, the fence, graves and statues are solid; the snow and the snow flowers are walked
on. The look above ground (Mirroh's family, darker and older) is as the mock: the user has not changed it.
Usage: python3 tools/art/necropolis/build_grounds.py   (then make)
"""
import os, sys, json
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..')); sys.path.insert(0, os.path.join(HERE, '..', 'mirroh'))
import mapbuild as MB
C = MB.C
MB_NORMAL, MB_SOUTH_ARROW_WARP, MB_DOOR = 0x00, 0x65, 0x60
WALK_G = {'snow', 'pave', 'warp', 'door'}
WALK_O = {None, 'flowers'}
W3 = lambda x, y, dest, wid: {'x': x, 'y': y, 'elevation': 3, 'dest_map': dest, 'dest_warp_id': str(wid)}
UPPER_NECRO_WARP = 8            # Upper Mirroh's warps: 2 to the north-west gatehouse, 6 down the stairs, then the skull gate's

def main():
    import grounds_mock as G
    M = G.compose(); H, W = G.H, G.W
    bot = np.zeros((H * 16, W * 16, 3), np.uint8); mid = np.zeros_like(bot); ma = np.zeros((H * 16, W * 16), bool)
    for y in range(H):
        for x in range(W):
            s = (slice(y * 16, y * 16 + 16), slice(x * 16, x * 16 + 16)); bot[s] = M.g[y][x]
            for img, a in M.obj[y][x]: mid[s][a] = img[a]; ma[s] |= a
    walk = {(x, y) for y in range(H) for x in range(W) if M.gtag[y, x] in WALK_G and M.otag[y, x] in WALK_O}
    foot = [(x, H - 1) for x in range(W) if M.gtag[H - 1, x] == 'warp']
    door = [(x, y) for y in range(H) for x in range(W) if M.gtag[y, x] == 'door']
    walk |= set(foot) | set(door)
    beh = lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) in foot else MB_DOOR if (x, y) in door else MB_NORMAL
    r = MB.build(bot, (mid, ma), None, W, H, walk, beh)
    warps = [W3(x, y, 'MAP_MIRROH_UPPER', UPPER_NECRO_WARP + min(i, 2)) for i, (x, y) in enumerate(foot)]
    warps += [W3(x, y, 'MAP_NECROPOLIS_LAKE', 1) for (x, y) in door]
    j = {'id': 'MAP_NECROPOLIS_GROUNDS', 'name': 'NecropolisGrounds', 'layout': 'LAYOUT_NECROPOLIS_GROUNDS',
         'music': 'MUS_MT_PYRE', 'region_map_section': 'MAPSEC_DR_MIRROH_NECROPOLIS', 'requires_flash': False,
         'weather': 'WEATHER_SNOW', 'map_type': 'MAP_TYPE_ROUTE', 'allow_cycling': True, 'allow_escaping': False,
         'allow_running': True, 'show_map_name': True, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
         'object_events': [], 'warp_events': warps, 'coord_events': [], 'bg_events': []}
    snow = next(int(r['grid'][y, x] & 0x3FF) for y in range(H) for x in range(W) if (x, y) in walk and M.gtag[y, x] == 'snow')
    MB.write(r, 'NecropolisGrounds', 'LAYOUT_NECROPOLIS_GROUNDS', ('necropolis_grounds_tiles', 'NecropolisGroundsTiles'),
             ('necropolis_grounds', 'NecropolisGrounds'), j, border=[snow] * 4)
    Image.fromarray(MB.render(r)).save('/home/claude/scratch/necro/built_grounds.png')
    print('foot', foot, 'door', door)

if __name__ == '__main__':
    main()
