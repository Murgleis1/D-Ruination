"""Build Mt. Mirroh B1F into the game: the Blast Crater, mock v3 (compose_b1f5.py on plan_b1f5.py; user 2026-11-24:
"this looks correct"). Keeps the map id and name (MAP_MIRROH_INTERIOR_B1F); Dreamstone Mysteries' 60x80 icy hall is
replaced by the 40x40 crater, on its own tileset pair (tools/art/mapbuild.py).

Cells: plan_b1f5.SOLID solid (rock, the temple's faces, the pit, the altar's stones, pillars and stumps, the fallen
shafts, rubble, the camp); everything else walkable, one level (elevation 3). The pillars' and crystals' upper parts are
on the top layer (the player walks behind them).
Warp 0: the ladder (20, 37), MB_LADDER, up to the exterior's secret ladder (MAP_MT_MIRROH_EXTERIOR warp 1, under its
Rock Smash rock; its warp already points here, warp 0).
Events: none yet. Dreamstone Mysteries had a Sneasler (its tunnel to Winterlily Hollow, a later area) and an item
ball (ITEM_SAPPHIRE, FLAG_ITEM_MIRROH_B1F_A): left for later stages (the script stays in Winterlily Hollow's file).
Winterlily Hollow's own warp into B1F (16, 68) pointed past the new map's edge: it now lands at the ladder's foot
(20, 36) until that area is designed. DM's wild encounters here (levels 33-35) removed: stage 5's job.
Usage: python3 tools/art/mt_mirroh/b1f/build_b1f.py   (then make)"""
import os, sys, json, re
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import compose_b1f5 as CB
import plan_b1f5 as P
import mapbuild as MB
import tilequant as TQN
C = MB.C
NAME, LAYOUT = 'MirrohInterior_B1F', 'LAYOUT_MIRROH_INTERIOR_B1F'
W, H = P.W, P.H
LADDER = (20, 37)
MB_LADDER = 0x61

def main():
    r = CB.compose(); cv = r['cv']
    under = cv.img.copy(); under[cv.mid_a] = cv.mid[cv.mid_a]                     # (ground + props under the player)
    flat = cv.flat()
    both = np.concatenate([flat, under], 0).astype(int)
    q, _ = TQN.quantise(both, n=13); q = q.astype(np.uint8)
    flat_q, under_q = q[:H * 16], q[H * 16:]
    solid = np.isin(P.G, list(P.SOLID))
    walk = {(x, y) for y in range(H) for x in range(W) if not solid[y, x]}
    beh = lambda x, y: MB_LADDER if (x, y) == LADDER else 0
    b = MB.build(under_q, None, (flat_q, cv.top_a), W, H, walk, beh)
    g = b['grid']
    for y in range(H):
        for x in range(W):
            g[y, x] = (g[y, x] & 0x3FF) | ((1 if solid[y, x] else 0) << 10) | (3 << 12)
    border = int(g[0, 0] & 0x3FF)
    MB.write(b, NAME, LAYOUT, ('mt_mirroh_b1f_tiles', 'MtMirrohB1FTiles'), ('mt_mirroh_b1f', 'MtMirrohB1F'), None,
             border=[border] * 4)
    p = os.path.join(C, 'data/maps', NAME, 'map.json'); j = json.load(open(p))
    j['warp_events'] = [{'x': LADDER[0], 'y': LADDER[1], 'elevation': 3, 'dest_map': 'MAP_MT_MIRROH_EXTERIOR', 'dest_warp_id': '1'}]
    j['object_events'] = []; j['coord_events'] = []; j['bg_events'] = []
    json.dump(j, open(p, 'w'), indent=2); open(p, 'a').write('\n')
    # Winterlily Hollow's Sneasler tunnel: land inside the new map (the ladder's foot) until that area is designed
    for f in ('scripts.pory', 'scripts.inc'):
        sp = os.path.join(C, 'data/maps/WinterlilyHollow', f); s = open(sp).read()
        s = s.replace('warp(MAP_MIRROH_INTERIOR_B1F, 16, 68)', 'warp(MAP_MIRROH_INTERIOR_B1F, 20, 36)')
        s = s.replace('warp MAP_MIRROH_INTERIOR_B1F, 16, 68', 'warp MAP_MIRROH_INTERIOR_B1F, 20, 36')
        open(sp, 'w').write(s)
    # Dreamstone Mysteries' encounters (33-35): gone until stage 5
    wp = os.path.join(C, 'src/data/wild_encounters.json'); wj = json.load(open(wp))
    for grp in wj['wild_encounter_groups']:
        grp['encounters'] = [e for e in grp['encounters'] if e.get('map') != 'MAP_MIRROH_INTERIOR_B1F']
    json.dump(wj, open(wp, 'w'), indent=2); open(wp, 'a').write('\n')
    print('B1F built: tiles', len(b['tiles']), 'metatiles', len(b['meta']), 'palettes', len(b['pals']))

if __name__ == '__main__':
    main()
