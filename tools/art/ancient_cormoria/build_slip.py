"""Build the Ancient Cormoria slip (Beat 8e) into the game from mock v3 (approved 2026-11-24: "Everything looks
absolutely fantastic now"): compose_slip.py's art on its own tileset pair (tools/art/mapbuild.py), as a new map
(user 2026-11-24: a new map; Dreamstone Mysteries' AncientMirroh, its caves and tower left as they are).

Map: AncientCormoriaSlip (MAP_ANCIENT_CORMORIA_SLIP, LAYOUT_ANCIENT_CORMORIA_SLIP), 50x56, in gMapGroup_Phase3.
Cells: rock, water, the bones, obelisks, altars, palms, cacti and the solid props solid (plan_slip.solid()); one level
(3): the stairs pass straight through the walls (as the Peak's); sand and dunes MB_SAND (footprints); river, pool and
spring MB_POND_WATER (a later Surf); the falls MB_WATERFALL.
Warps: 0 at the arrival (24, 50), the slip's landing (it is reached by script, stage 3: from Kimaris's chamber after
the Trial; the way home is the north altar's script, back to the chamber). No warp tile is stepped on here.
Events: none yet (Kimaris, the altars' scripts: stages 2-3).
The sky: the ancient backdrop (backdrop_ancient.py) on BG3, as the Peak's (src/field_camera.c, sMapBackdrops): the
map's art in the middle layer with the sky transparent; the backdrop's tiles and palette (slot 12) fixed in the
tileset; its tilemap in data/tilesets/secondary/ancient_cormoria_slip/backdrop.bin. The mock drew the backdrop 8 px
lower than the Peak's formula puts it, so 8 rows of its top colour head the tilemap (the engine's formula unchanged).
Usage: python3 tools/art/ancient_cormoria/build_slip.py   (then make)"""
import os, sys, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import compose_slip as CS
import plan_slip as P
import backdrop_ancient as BA
import mapbuild as MB
import tilequant as TQN
C = MB.C
NAME, LAYOUT, MAPID = 'AncientCormoriaSlip', 'LAYOUT_ANCIENT_CORMORIA_SLIP', 'MAP_ANCIENT_CORMORIA_SLIP'
TS_PRI, TS_SEC = ('ancient_cormoria_slip_tiles', 'AncientCormoriaSlipTiles'), ('ancient_cormoria_slip', 'AncientCormoriaSlip')
W, H = P.W, P.H
BD_SLOT = 12
LOWER = 8                                       # (px: the mock's backdrop sits this much under the engine's formula)

def backdrop_tiles():
    """the ancient backdrop as 8x8 tiles in its own palette (BD_SLOT), deduplicated with flips, numbered down from
    1023; its 32x32 BG3 tilemap: LOWER px of the sky's top colour, the backdrop (256 x BA.BH), the mountains' colour
    below it, the sky's top colour in the last two rows (above it when the camera climbs)"""
    bd = BA.backdrop()
    top_c = tuple(int(v) for v in bd[0, 8])
    bd = np.concatenate([np.tile(np.array(top_c, np.uint8), (LOWER, BA.BW, 1)), bd], 0)
    rows_n = bd.shape[0] // 8; assert bd.shape[0] % 8 == 0 and rows_n <= 30
    cols = sorted({tuple(int(v) for v in c) for c in bd.reshape(-1, 3)}, key=sum)
    assert len(cols) <= 15, len(cols)
    pal = [(0, 0, 0)] + cols + [(0, 0, 0)] * (15 - len(cols))
    lk = {c: i + 1 for i, c in enumerate(cols)}
    I = np.zeros(bd.shape[:2], np.uint8)
    for c, i in lk.items(): I[(bd == c).all(-1)] = i
    body, skytop = lk[tuple(int(v) for v in bd[-1, 8])], lk[top_c]
    I = I.copy()
    rows = [I[ty * 8:ty * 8 + 8] for ty in range(rows_n)] + [np.full((8, 256), body, np.uint8)] * (30 - rows_n) + \
           [np.full((8, 256), skytop, np.uint8)] * 2
    for R in rows: R[:, 0:8] = R[:, 8:16]; R[:, 248:256] = R[:, 240:248]   # (columns 0 and 31 never show: BG3HOFS = 8)
    tiles, seen, free = {}, {}, iter([n for n in range(1023, 0, -1) if n != 512])
    tm = np.zeros((32, 32), np.uint16)
    for ty, R in enumerate(rows):
        for tx in range(32):
            t = R[:, tx * 8:tx * 8 + 8]
            for f, v in ((0, t), (1, t[:, ::-1]), (2, t[::-1]), (3, t[::-1, ::-1])):
                k = np.ascontiguousarray(v).tobytes()
                if k in seen: n, f0 = seen[k]; tm[ty, tx] = n | (f ^ f0) << 10 | BD_SLOT << 12; break
            else:
                n = next(free); tiles[n] = t.copy(); seen[t.tobytes()] = (n, 0); tm[ty, tx] = n | BD_SLOT << 12
    return tiles, pal, tm

def cells(r):
    """collision and behaviour per cell"""
    solid = P.solid()
    beh = np.zeros((H, W), int)
    for y in range(H):
        for x in range(W):
            ch = P.G[y, x]
            if ch == '~': beh[y, x] = 0x10                                     # MB_POND_WATER
            elif ch in '.r' and not solid[y, x]: beh[y, x] = 0x21              # MB_SAND
    F = P.FALLS
    for x in range(F['x0'], F['x1'] + 1):
        for y in range(F['top'], F['top'] + F['rows']): beh[y, x] = 0x13; solid[y, x] = True   # MB_WATERFALL
    for y in range(P.BRIDGE['y0'], P.BRIDGE['y1'] + 1):                          # (the rope bridge: walked, not swum)
        for x in (P.BRIDGE['x'], P.BRIDGE['x'] + 1): beh[y, x] = 0; solid[y, x] = False
    for L in P.LADDERS:                                                         # (the stairs: plain stone)
        for x in (L['x'], L['x'] + 1):
            for y in range(H):
                if not solid[y, x] and P.G[y, x] == '#': beh[y, x] = 0
    return solid, beh

def main():
    r = CS.compose()
    solid, beh = cells(r)
    flat = r['bottom'].copy(); flat[r['top_a']] = r['top'][r['top_a']]
    both = np.concatenate([flat, r['bottom']], 0).astype(int)
    q, _ = TQN.quantise(both, n=12); q = q.astype(np.uint8)
    flat_q, under_q = q[:H * 16], q[H * 16:]
    walk = {(x, y) for y in range(H) for x in range(W) if not solid[y, x]}
    bt, bpal, btm = backdrop_tiles()
    plain = np.zeros_like(under_q); plain[:] = under_q[H * 16 - 1, 0]
    b = MB.build(plain, (under_q, ~r['sky_a']), (flat_q, r['top_a']), W, H, walk, lambda x, y: int(beh[y, x]),
                 fixed=dict(tiles=bt, pals={BD_SLOT: bpal}))
    g = b['grid']
    for y in range(H):
        for x in range(W):
            g[y, x] = (g[y, x] & 0x3FF) | ((1 if solid[y, x] else 0) << 10) | (3 << 12)
    border = int(g[H - 1, 0] & 0x3FF)
    os.makedirs(os.path.join(C, 'data/tilesets/secondary', TS_SEC[0]), exist_ok=True)
    btm.astype('<u2').tofile(os.path.join(C, 'data/tilesets/secondary', TS_SEC[0], 'backdrop.bin'))
    mapj = {
        'id': MAPID, 'name': NAME, 'layout': LAYOUT, 'music': 'MUS_ROUTE113',
        'region_map_section': 'MAPSEC_ANCIENT_CERAM', 'requires_flash': False, 'weather': 'WEATHER_NONE',
        'map_type': 'MAP_TYPE_ROUTE', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
        'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
        'object_events': [],
        'warp_events': [{'x': P.ARRIVE[0], 'y': P.ARRIVE[1], 'elevation': 3, 'dest_map': MAPID, 'dest_warp_id': '0'}],
        'coord_events': [], 'bg_events': []}
    MB.write(b, NAME, LAYOUT, TS_PRI, TS_SEC, mapj, border=[border] * 4)
    print('slip built: tiles', len(b['tiles']), '(backdrop %d)' % len(bt), 'metatiles', len(b['meta']), 'palettes', len(b['pals']))

if __name__ == '__main__':
    main()
