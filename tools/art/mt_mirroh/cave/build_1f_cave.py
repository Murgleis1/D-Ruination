"""Build Mt. Mirroh 1F into the game from the approved plan and its art (plan_1f.py, compose_1f.py; user 2026-11-23):
MonoMyth's Glittering Grotto made icy, on its own tileset pair (tools/art/mapbuild.py). Keeps the map id and name.

Cells: rock solid; three levels (3 lower caves, 4 upper level, 5 top band), stairs at level 0; the frozen streams are
water (a later Surf crosses them; the bridges are the way in Chapter 1); the ledge jumps south; the great ice
crystals, the small ice chunks and the rubble are solid. The crystals' tips are on the top layer (the player walks
behind them).
Warps: 0 the way in/out (55, 58) <-> the exterior's cave mouth; 1 the exit to the Peak (54, 1) <-> the Peak.
Events: the rubble's sign (the Shard: items / story stage). Dreamstone Mysteries' people, items and its nurse quest
triggers are left for stages 2-3 and 6 (their scripts stay in the file, unhooked).
Usage: python3 tools/art/mt_mirroh/cave/build_1f_cave.py   (then make)"""
import os, sys, json, re
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import compose_1f as CF
import mapbuild as MB
import tilequant as TQN
C = MB.C
NAME, LAYOUT = 'MirrohInterior_1F', 'LAYOUT_MIRROH_INTERIOR_1F'
W = H = 60

def main():
    r = CF.compose()
    under = r['bottom'].copy(); under[r['mid_a']] = r['mid'][r['mid_a']]          # ground + props (under the player)
    both = np.concatenate([r['flat'], under], 0).astype(int)
    q, _ = TQN.quantise(both, n=13); q = q.astype(np.uint8)
    flat_q, under_q = q[:H * 16], q[H * 16:]
    walk = {(x, y) for y in range(H) for x in range(W) if not r['solid'][y, x]}
    beh = lambda x, y: int(r['beh'][y, x])
    b = MB.build(under_q, None, (flat_q, r['top_a']), W, H, walk, beh)
    g = b['grid']
    for y in range(H):
        for x in range(W):
            col = 1 if r['solid'][y, x] else 0
            g[y, x] = (g[y, x] & 0x3FF) | (col << 10) | (int(r['elev'][y, x]) << 12)
    border = int(g[H - 1, 0] & 0x3FF)
    MB.write(b, NAME, LAYOUT, ('mt_mirroh_cave_tiles', 'MtMirrohCaveTiles'), ('mt_mirroh_cave', 'MtMirrohCave'), None,
             border=[border] * 4)
    p = os.path.join(C, 'data/maps', NAME, 'map.json'); j = json.load(open(p))
    j['warp_events'] = [
        {'x': CF.EXIT_S[0], 'y': CF.EXIT_S[1], 'elevation': 3, 'dest_map': 'MAP_MT_MIRROH_EXTERIOR', 'dest_warp_id': '0'},
        {'x': CF.EXIT_N[0], 'y': CF.EXIT_N[1], 'elevation': 5, 'dest_map': 'MAP_MIRROH_PEAK', 'dest_warp_id': '1'}]
    j['object_events'] = []
    j['coord_events'] = []
    j['bg_events'] = [{'type': 'sign', 'x': CF.RUBBLE[0], 'y': CF.RUBBLE[1], 'elevation': 5,
                       'player_facing_dir': 'BG_EVENT_PLAYER_FACING_ANY', 'script': 'MirrohInterior_1F_EventScript_Rubble'}]
    j['weather'] = 'WEATHER_NONE'
    json.dump(j, open(p, 'w'), indent=2); open(p, 'a').write('\n')
    # unhook Dreamstone Mysteries' on-frame nurse-quest script (its people are gone until stage 2-3)
    sp = os.path.join(C, 'data/maps', NAME, 'scripts.pory'); s = open(sp).read()
    s = re.sub(r'mapscripts MirrohInterior_1F_MapScripts\s*\{.*?\n\}', 'mapscripts MirrohInterior_1F_MapScripts {}', s, count=1, flags=re.S)
    open(sp, 'w').write(s)
    print('1F built: tiles', len(b['tiles']), 'metatiles', len(b['meta']), 'palettes', len(b['pals']))

if __name__ == '__main__':
    main()
