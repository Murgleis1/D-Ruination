"""Build the monastery hall after Eden's escape blast (LAYOUT_PELLUCA_TEMPLAR_HALL_RUINED) from its approved mock
(blast_mock.py; user 2026-11-19: "This looks fantastic").

The same map (PellucaTemplarHall) gets a second layout; its ON_TRANSITION swaps it in once FLAG_DR_CHURCH_BLASTED is
set (the blast scene, story pass). Cut with the image method (tools/art/academy/imgtiles.py) into its own tileset pair.
Everything the player meets stays as the intact hall has it (read from the intact layout this script leaves alone):
each cell's collision and behaviour (the south exit's arrow warp), and the intact hall's over-the-player pieces
(the side tables' tops) laid in the over layer again. Changed:
  * the split through the medallion: its cells fall through (MB_MT_PYRE_HOLE + a warp to the ice path's landing);
  * the cell doorway: caved in, no longer a door; the fallen stone in front of it solid;
  * hall warp 2: the arrival from the ice path (the ladder and the Templars' rope), just south of the split.
CHURCH_TEST_BLASTED=1 (test builds only) sets the flag on entering, so the ruined hall can be walked in the emulator.
Credits: as build_hall.py and blast_mock.py (the Rejuvenation team's church art; MonoMyth's Old HQ and Mt. Thunder
rubble).
Usage: python3 tools/art/templar/build_ruined.py
"""
import os, sys, json, struct
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'academy'))
import imgtiles as IT
import blast_mock as B
import compose_mock as CM

MB_MT_PYRE_HOLE = 0x0F
NAME, LAYOUT, MAP = 'PellucaTemplarHallRuined', 'LAYOUT_PELLUCA_TEMPLAR_HALL_RUINED', 'MAP_PELLUCA_TEMPLAR_HALL'
PRIM, SEC = ('templar_hall_ruined_tiles', 'TemplarHallRuinedTiles'), ('templar_hall_ruined', 'TemplarHallRuined')
DOOR = (1, CM.WALL - 1)                     # the cell doorway (intact: warp 1 to the monastery)
ARRIVAL = (8, 12)                           # where the ladder and the rope bring the player up: south of the split
SPLIT_MIN, RUBBLE_MIN = 20, 10              # pixels of the gap / of fallen stone that make a cell fall / solid
ICE_PATH, ICE_LANDING = 'MAP_PELLUCA_ICE_PATH', 0

def intact():
    """The intact hall as built: per cell its collision byte, behaviour, and its top layer's pixels (rgb, mask)."""
    d = os.path.join(IT.C, 'data'); W, H = CM.W, CM.H
    g = np.fromfile(os.path.join(d, 'layouts/PellucaTemplarHall/map.bin'), '<u2').reshape(H, W)
    ts = {k: os.path.join(d, 'tilesets', k) for k in ('primary/old_hq_interior', 'secondary/templar_hall')}
    def load(k):
        raw = open(os.path.join(ts[k], 'metatiles.bin'), 'rb').read(); n = len(raw) // 24
        return ([struct.unpack_from('<12H', raw, 24 * i) for i in range(n)],
                list(np.fromfile(os.path.join(ts[k], 'metatile_attributes.bin'), '<u2')),
                np.array(Image.open(os.path.join(ts[k], 'tiles.png'))))
    (pm, pa, pt), (sm, sa, st) = load('primary/old_hq_interior'), load('secondary/templar_hall')
    def pal(i):
        k = 'primary/old_hq_interior' if i < 6 else 'secondary/templar_hall'
        L = open(os.path.join(ts[k], 'palettes', f'{i:02d}.pal')).read().split('\n')[3:19]
        return np.array([[int(v) for v in l.split()] for l in L], np.uint8)
    pals = [pal(i) for i in range(13)]
    def tile(t):
        sheet, t = (pt, t) if t < 512 else (st, t - 512)
        return sheet[(t // 16) * 8:(t // 16) * 8 + 8, (t % 16) * 8:(t % 16) * 8 + 8] & 0xF
    col = (g >> 10).astype(int); beh = np.zeros((H, W), int); top = {}
    for y in range(H):
        for x in range(W):
            m = int(g[y, x] & 0x3FF); e, a = (pm[m], pa[m]) if m < 512 else (sm[m - 512], sa[m - 512])
            beh[y, x] = a & 0xFF
            if not any(v & 0x3FF for v in e[8:]): continue
            rgb = np.zeros((16, 16, 3), np.uint8); mk = np.zeros((16, 16), bool)
            for q, v in enumerate(e[8:]):
                if not v & 0x3FF: continue
                t = tile(v & 0x3FF)
                if v & 0x400: t = t[:, ::-1]
                if v & 0x800: t = t[::-1, :]
                yy, xx = (q // 2) * 8, (q % 2) * 8; nz = t != 0
                rgb[yy:yy + 8, xx:xx + 8][nz] = pals[v >> 12][t][nz]; mk[yy:yy + 8, xx:xx + 8] |= nz
            top[(x, y)] = (rgb, mk)
    return col, beh, top

def cells_of(mask, least):
    H, W = CM.H, CM.W
    return {(x, y) for y in range(H) for x in range(W) if int(mask[y * 16:y * 16 + 16, x * 16:x * 16 + 16].sum()) >= least}

def main():
    img = B.compose(); W, H = CM.W, CM.H
    split, rubble = cells_of(B.LAST['gap'], SPLIT_MIN), cells_of(B.LAST['rubble'], RUBBLE_MIN)
    col0, beh0, top = intact()
    assert ARRIVAL not in split and col0[ARRIVAL[1], ARRIVAL[0]] == IT.FLOOR_E3
    over = np.zeros_like(img); om = np.zeros(img.shape[:2], bool)
    for (x, y), (rgb, mk) in top.items():                 # the intact over-the-player pieces, on the floor's rows only
        if CM.WALL <= y < H - 1:
            om[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = mk; over[y * 16:y * 16 + 16, x * 16:x * 16 + 16][mk] = rgb[mk]
    def col(x, y):
        if (x, y) == DOOR: return IT.WALL
        if (x, y) in rubble and col0[y, x] == IT.FLOOR_E3: return IT.SOLID_E3
        return int(col0[y, x])
    def beh(x, y):
        if (x, y) in split: return MB_MT_PYRE_HOLE
        if (x, y) == DOOR: return 0
        return int(beh0[y, x])
    r = IT.build(img, W, H, over=over, om=om, col=col, beh=beh, merge=16, rare=600, tries=2000)
    bad = IT.check(r)
    r['void'] = int(r['grid'][H - 1, 0] & 0x3FF)          # the black below the room (not the wall's corner)
    # one map, two layouts: the ruined layout and its tilesets only (the hall's map.json keeps its own, warps below)
    mj = os.path.join(IT.C, 'data/maps/PellucaTemplarHall/map.json'); hall = json.load(open(mj))
    IT.write_room(r, NAME, LAYOUT, PRIM, SEC, None, after_layout='LAYOUT_PELLUCA_TEMPLAR_HALL')
    # the hall's warps: 0 Pelluca, 1 the cell door (dead in the ruined layout), 2 the arrival from the ice path,
    # then one per split cell down to the ice path's landing
    ws = hall['warp_events'][:2]
    ws.append({'x': ARRIVAL[0], 'y': ARRIVAL[1], 'elevation': 0, 'dest_map': ICE_PATH, 'dest_warp_id': str(ICE_LANDING)})
    ws += [{'x': x, 'y': y, 'elevation': 0, 'dest_map': ICE_PATH, 'dest_warp_id': str(ICE_LANDING)} for x, y in sorted(split)]
    hall['warp_events'] = ws
    json.dump(hall, open(mj, 'w'), indent=2); open(mj, 'a').write('\n')
    test = bool(os.environ.get('CHURCH_TEST_BLASTED'))
    sp = os.path.join(IT.C, 'data/maps/PellucaTemplarHall/scripts.pory')
    open(sp, 'w').write(SCRIPTS.format(test='        setflag(FLAG_DR_CHURCH_BLASTED) // TEST BUILD ONLY (CHURCH_TEST_BLASTED)\n' if test else ''))
    print(f'ruined hall {W}x{H} tiles {len(r["tiles"])} metatiles {len(r["meta"])} palettes {r["npal"]} mismatches {bad} '
          f'split {sorted(split)} rubble {sorted(rubble)}{"  (TEST: blasted on entry)" if test else ""}')

SCRIPTS = '''// ============ DREAMSTONE RUINATION - Pelluca Valley: the Templar Monastery main hall ============
// The church-like foyer the holding cell's south door opens into (user design 2026-11-19).
// Built by tools/art/templar/build_hall.py (intact) and build_ruined.py (after Eden's escape blast: the split
// floor down to the ice path, the cell room caved in). This file is written by build_ruined.py.
// NPCs and dialogue come with the dialogue pass.

mapscripts PellucaTemplarHall_MapScripts {{
    MAP_SCRIPT_ON_TRANSITION {{
{test}        if (flag(FLAG_DR_CHURCH_BLASTED)) {{
            setmaplayoutindex(LAYOUT_PELLUCA_TEMPLAR_HALL_RUINED)
        }}
    }}
}}
'''

if __name__ == '__main__':
    main()
