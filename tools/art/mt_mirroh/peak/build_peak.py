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
The sky: the backdrop (user 2026-11-24: MonoMyth's bastion-top backdrop, recoloured; backdrop.py) on BG3 behind the
map, its parallax in src/field_camera.c (sMapBackdrops): the map's art is built into the middle layer with its sky
transparent; the backdrop's tiles and palette (slot 12) are fixed in the tileset; its BG3 tilemap is written to
data/tilesets/secondary/mt_mirroh_peak/backdrop.bin.
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

BD_SLOT = 12                                    # (the backdrop's palette: the tileset's last slot)

def backdrop_tiles():
    """The recoloured backdrop (backdrop.py) as 8x8 tiles in its own palette (BD_SLOT), deduplicated with flips, at
    tile numbers counted down from 1023; and its 32x32 BG3 tilemap: rows 0-16 the backdrop (256x136), rows 17-29 its
    mountains' own colour (below it, as the camera climbs down), rows 30-31 its sky's top colour (above it)."""
    import backdrop as BD
    bd = BD.backdrop()
    cols = sorted({tuple(int(v) for v in c) for c in bd.reshape(-1, 3)}, key=sum)
    assert len(cols) <= 15
    pal = [(0, 0, 0)] + cols + [(0, 0, 0)] * (15 - len(cols))
    lk = {c: i + 1 for i, c in enumerate(cols)}
    I = np.zeros(bd.shape[:2], np.uint8)
    for c, i in lk.items(): I[(bd == c).all(-1)] = i
    body, skytop = lk[tuple(int(v) for v in bd[BD.BH - 1, 8])], lk[tuple(int(v) for v in bd[0, 8])]
    rows = [I[ty * 8:ty * 8 + 8] for ty in range(17)] + [np.full((8, 256), body, np.uint8)] * 13 + [np.full((8, 256), skytop, np.uint8)] * 2
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

def main():
    r = CP.compose()
    both = np.concatenate([r['flat'], r['bottom']], 0).astype(int)
    q, _ = TQN.quantise(both, n=13); q = q.astype(np.uint8)
    flat_q, under_q = q[:H * 16], q[H * 16:]
    walk = {(x, y) for y in range(H) for x in range(W) if not r['solid'][y, x]}
    beh = lambda x, y: int(r['beh'][y, x])
    # the map's art in the middle layer (BG2), its sky transparent; the bottom layer (never drawn on a map with a
    # backdrop) one plain colour; the backdrop's tiles and palette fixed in the tileset
    bt, bpal, btm = backdrop_tiles()
    plain = np.zeros_like(under_q); plain[:] = under_q[0, 0]
    b = MB.build(plain, (under_q, ~r['sky_a']), (flat_q, r['top_a']), W, H, walk, beh,
                 fixed=dict(tiles=bt, pals={BD_SLOT: bpal}))
    g = b['grid']
    for y in range(H):
        for x in range(W):
            col = 1 if r['solid'][y, x] else 0
            g[y, x] = (g[y, x] & 0x3FF) | (col << 10) | (int(r['elev'][y, x]) << 12)
    border = int(g[H - 1, 0] & 0x3FF)
    btm.astype('<u2').tofile(os.path.join(C, 'data/tilesets/secondary/mt_mirroh_peak/backdrop.bin'))
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
    print('Peak built: tiles', len(b['tiles']), '(backdrop %d)' % len(bt), 'metatiles', len(b['meta']), 'palettes', len(b['pals']))

if __name__ == '__main__':
    main()
