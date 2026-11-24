"""Build Mirroh Peak into the game from plan v2 (plan_peak.py) and its art (compose_peak.py, Mt. Thunder style; user
2026-11-24), on its own tileset pair (tools/art/mapbuild.py). Keeps the map id, name and layout (50x110).

Cells: rock, pines, ruins, mouths, water and the solid dressing solid; one level (3): the bands are walls and the
stairs pass straight through them; the ice grass is tall grass (stage 5 gives it its encounters); the stream and pond
are water (a later Surf). The pines' crowns on the climb are on the top layer (the player walks behind them).
Warps (ids kept): 0 Winterlily Hollow's mouth (40, 78), blocked in Chapter 1 (solid: its warp is never stepped on);
1 the cave mouth into 1F (26, 101) <-> 1F's exit to the Peak (1F's warp 1).
Events: none for now. Dreamstone Mysteries' people (Maxie and the Magma grunts, Viniel, Wally, its hiker), its
cutscene and save triggers, its signs and its items (a TM, two hidden items) are left for stages 2-3 and 6: their
scripts stay in scripts.pory.
Usage: python3 tools/art/mt_mirroh/peak/build_peak.py   (then make)"""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..'))
import compose_peak as CP
import mapbuild as MB
import tilequant as TQN
C = MB.C
NAME, LAYOUT = 'MirrohPeak', 'LAYOUT_MIRROH_PEAK'
W, H = CP.W, CP.H

def main():
    r = CP.compose()
    both = np.concatenate([r['flat'], r['bottom']], 0).astype(int)
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
    MB.write(b, NAME, LAYOUT, ('mt_mirroh_peak_tiles', 'MtMirrohPeakTiles'), ('mt_mirroh_peak', 'MtMirrohPeak'), None,
             border=[border] * 4)
    p = os.path.join(C, 'data/maps', NAME, 'map.json'); j = json.load(open(p))
    j['warp_events'] = [
        {'x': CP.MOUTH_WL[0], 'y': CP.MOUTH_WL[1], 'elevation': 3, 'dest_map': 'MAP_WINTERLILY_HOLLOW', 'dest_warp_id': '1'},
        {'x': CP.MOUTH_1F[0], 'y': CP.MOUTH_1F[1], 'elevation': 3, 'dest_map': 'MAP_MIRROH_INTERIOR_1F', 'dest_warp_id': '1'}]
    j['object_events'] = []
    j['coord_events'] = []
    j['bg_events'] = []
    json.dump(j, open(p, 'w'), indent=2); open(p, 'a').write('\n')
    print('Peak built: tiles', len(b['tiles']), 'metatiles', len(b['meta']), 'palettes', len(b['pals']))

if __name__ == '__main__':
    main()
