"""Build the Mirroh Necropolis grounds into the game from their approved mock (grounds_mock.py; user 2026-11-21
"Looks good overall"): MAP_NECROPOLIS_GROUNDS, its own tileset pair (tools/art/mapbuild.py: ground on the bottom
layer, everything standing on it on the middle layer).

Ways: the way in runs down off the mock's foot between the skull gate's spires (Upper Mirroh as built, nine rows
below the mock: see UPPER_DX); its last row of snow above the gate's top (x 20-24) is a south arrow warp back to
Mirroh's skull gate; the grand entrance's dark doorway (21, 15) is a door down to the frozen lake's landing. Walls, the
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

# (user 2026-11-22: make sure the other gatehouses and entrances don't show what Route 13's foot did.) The grounds' way
# back to Mirroh ran off the bottom edge between the hedges into open snow (the border), and you came out before a
# skull gate you never saw. Now, as at Route 13's foot and by MonoMyth's convention for a building entered from its
# north, the grounds end on Upper Mirroh as built: its rows 0-8 (the city wall-walk, the skull gate's spired towers
# and crenellated top, the city behind them), its x 42-46 (the notch between the gate's spires) under the grounds'
# x 20-24, so the road runs on down between the spires; the warp is the road's last row of snow above the gate's top.
UPPER_DX, EXTRA = 22, 9
NOTCH = range(20, 25)                     # (the grounds' x of Upper's 42-46: between the spires, snow, walked on)

def main():
    import grounds_mock as G
    M = G.compose(); H0, W = G.H, G.W; H = H0 + EXTRA
    bot = np.zeros((H * 16, W * 16, 3), np.uint8); mid = np.zeros_like(bot); ma = np.zeros((H * 16, W * 16), bool)
    for y in range(H0):
        for x in range(W):
            s = (slice(y * 16, y * 16 + 16), slice(x * 16, x * 16 + 16)); bot[s] = M.g[y][x]
            for img, a in M.obj[y][x]: mid[s][a] = img[a]; ma[s] |= a
    sys.path.insert(0, os.path.join(HERE, '..')); import render_built as RB
    RB.main('MirrohUpper', '/tmp/_ng_upper.png'); U = np.asarray(Image.open('/tmp/_ng_upper.png').convert('RGB'))
    for y in range(EXTRA):
        for x in range(W):
            ux = x + UPPER_DX
            if ux > 59: ux = 57 + (ux - 57) % 3                       # (past Upper's edge: its flank pines carry on)
            bot[(H0 + y) * 16:(H0 + y + 1) * 16, x * 16:(x + 1) * 16] = U[y * 16:(y + 1) * 16, ux * 16:(ux + 1) * 16]
    # the half cell of snow between each end of the wall-walk and the gate's spired tower: the walk runs on to the
    # tower, behind its spire (as at Route 13's foot): where those cells show plain snow, the wall-walk's pixels
    cell = lambda ux, uy: U[uy * 16:(uy + 1) * 16, ux * 16:(ux + 1) * 16]
    snow_ref = cell(43, 2)
    for gx, ux_wall in ((17, 37), (27, 51)):
        for y in (0, 1):
            t = bot[(H0 + y) * 16:(H0 + y + 1) * 16, gx * 16:(gx + 1) * 16]
            m = (t == snow_ref).all(-1); t[m] = cell(ux_wall, y)[m]
    walk = {(x, y) for y in range(H0) for x in range(W) if M.gtag[y, x] in WALK_G and M.otag[y, x] in WALK_O}
    walk |= {(x, H0 - 1) for x in range(W) if M.gtag[H0 - 1, x] == 'warp'}      # (the old foot row: the road, walked on)
    walk |= {(x, y) for x in NOTCH for y in range(H0, H0 + 4)}
    # the warps: Upper's skull-gate warps (its x 43, 44, 45) lead to these in order, so they come first, x for x
    foot = [(21, H0 + 3), (22, H0 + 3), (23, H0 + 3), (20, H0 + 3), (24, H0 + 3)]
    door = [(x, y) for y in range(H0) for x in range(W) if M.gtag[y, x] == 'door']
    walk |= set(foot) | set(door)
    beh = lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) in foot else MB_DOOR if (x, y) in door else MB_NORMAL
    r = MB.build(bot, (mid, ma), None, W, H, walk, beh)
    up = {21: 0, 22: 1, 23: 2, 20: 0, 24: 2}
    warps = [W3(x, y, 'MAP_MIRROH_UPPER', UPPER_NECRO_WARP + up[x]) for (x, y) in foot]
    warps += [W3(x, y, 'MAP_NECROPOLIS_LAKE', 1) for (x, y) in door]
    j = {'id': 'MAP_NECROPOLIS_GROUNDS', 'name': 'NecropolisGrounds', 'layout': 'LAYOUT_NECROPOLIS_GROUNDS',
         'music': 'MUS_MT_PYRE', 'region_map_section': 'MAPSEC_DR_MIRROH_NECROPOLIS', 'requires_flash': False,
         'weather': 'WEATHER_SNOW', 'map_type': 'MAP_TYPE_ROUTE', 'allow_cycling': True, 'allow_escaping': False,
         'allow_running': True, 'show_map_name': True, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
         'object_events': [], 'warp_events': warps, 'coord_events': [], 'bg_events': []}
    snow = next(int(r['grid'][y, x] & 0x3FF) for y in range(H0) for x in range(W) if (x, y) in walk and M.gtag[y, x] == 'snow')
    MB.write(r, 'NecropolisGrounds', 'LAYOUT_NECROPOLIS_GROUNDS', ('necropolis_grounds_tiles', 'NecropolisGroundsTiles'),
             ('necropolis_grounds', 'NecropolisGrounds'), j, border=[snow] * 4)
    Image.fromarray(MB.render(r)).save('/home/claude/scratch/necro/built_grounds.png')
    print('foot', foot, 'door', door)

if __name__ == '__main__':
    main()
