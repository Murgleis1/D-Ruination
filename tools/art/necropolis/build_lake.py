"""Build the Necropolis lake (mock v2, user 2026-11-21) into the game: MAP_NECROPOLIS_LAKE.

The picture is lake_mock.compose() in its game mode (the ice repeating every 4x4 cells, its shades held to whole
and half steps), its colours merged to fit (tilefit), cut into its own tileset pair by academy/imgtiles.py
(primary `necropolis_lake_tiles`: every tile and palettes 0-5; secondary `necropolis_lake`: palettes 6-12 and the
metatiles). Behaviours and collision come from the puzzle grid (lake_puzzle via lake_mock.layout()):
  ice    -> MB_ICE (the engine's sliding ice: field_player_avatar.c ForcedMovement_Slip), walkable;
  soil   -> normal floor, walkable (the islands, the corner platforms, the landing, the door's landing);
  block  -> solid (graves, statues, walls, the bonfires, the sealed arch, the dark).
The four necromancers stand by their bonfires as object events (placeholders: no scripts or teams yet).
The landing's foot (x 20-22, the bottom row) is a south arrow warp up to the grounds' grand entrance; the sealed
arch (21, 4) warps up to Kimaris's chamber (solid until the Trial opens it). The map carries a margin of 2 cells south and east
for the frozen bank. The four bonfires are built unlit; their lit metatiles (the ghost flame, animated by
InitTilesetAnim_NecropolisLake) are listed in data/maps/NecropolisLake/bonfires.json for the Trial's setmetatile.
With DR_LAKE_TEST=1 every bonfire is lit on entry (a test build; rebuild without it).
Usage: python3 tools/art/necropolis/build_lake.py   (then make)
"""
import os, sys, json
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'academy'))
import lake_mock as LM, lake_puzzle as P, imgtiles as IT, tilefit
sys.path.insert(0, os.path.join(HERE, '..'))

C = IT.C
MAP, LAYOUT, MAPID = 'NecropolisLake', 'LAYOUT_NECROPOLIS_LAKE', 'MAP_NECROPOLIS_LAKE'
PRIM, SEC = ('necropolis_lake_tiles', 'NecropolisLakeTiles'), ('necropolis_lake', 'NecropolisLake')
MB_NORMAL, MB_ICE = 0x00, 0x20
TEST = bool(os.environ.get('DR_LAKE_TEST'))

FLAME_TICK = 8                 # a flame frame every 8 frames (as the Battle Pyramid's torch)

def main():
    import mapbuild as MB
    LM.GAME = True
    img, _ = LM.compose(False)
    g, graves, soil = LM.layout()
    h0, w0 = g.shape; H, W = h0 + LM.MARGIN, w0 + LM.MARGIN               # (the bank's margin south and east)
    img = img[:H * 16, :W * 16]
    q, _ = tilefit.reduce_tiles(img, (0, 0, img.shape[1], img.shape[0]), 15)
    trainers = {v['trainer'] for v in P.CORNERS.values()}
    walk = {(x, y) for y in range(h0) for x in range(w0) if g[y, x] != P.BLOCK} | trainers
    mats = [(x, h0 - 1) for x in (20, 21, 22)]                    # the landing's foot: up to the grounds
    ice = lambda x, y: x < w0 and y < h0 and g[y, x] == P.ICE and (x, y) not in trainers
    beh = lambda x, y: MB_ICE if ice(x, y) else 0x65 if (x, y) in mats else MB_NORMAL
    r = MB.build(q, None, None, W, H, walk, beh, max_colours=150)
    # --- the bonfires, lit (user 2026-11-21: real bonfire art, lit and unlit). Unlit in the map; lit, each fire's cell
    # and the cell above it take metatiles of their own whose top layer is the cold ghost flame (lake_mock.flame_frames:
    # the base game's Battle Pyramid torch flame, recoloured), its 8 tiles played by InitTilesetAnim_NecropolisLake.
    frames = LM.flame_frames()
    cols = sorted({tuple(int(v) for v in c) for f in frames for c in f[..., :3][f[..., 3] > 0]}, key=sum)
    slot = next((s for s, p in r['pals'].items() if set(map(tuple, p[1:])) >= set(cols)), None)
    if slot is None:
        slot = next(s for s in range(13) if s not in r['pals'])
        r['pals'][slot] = [(0, 0, 0)] + cols + [(0, 0, 0)] * (15 - len(cols))
    lut = {c: i for i, c in enumerate(r['pals'][slot]) if i and c in cols}
    idx = lambda rgba: np.where(rgba[..., 3] > 0, np.vectorize(lambda a, b_, c: lut.get((int(a), int(b_), int(c)), 0))(
        rgba[..., 0], rgba[..., 1], rgba[..., 2]), 0).astype(np.uint8)
    first = max(r['tiles']) + 1
    order = [(cy, q_) for cy in (0, 1) for q_ in range(4)]                   # (the tip's cell, then the fire's)
    for i, (cy, q_) in enumerate(order):
        r['tiles'][first + i] = idx(frames[0][cy * 16 + (q_ // 2) * 8:cy * 16 + (q_ // 2) * 8 + 8, (q_ % 2) * 8:(q_ % 2) * 8 + 8])
    lit = {}
    nxt = max(r['meta']) + 1
    for k, v in sorted(P.CORNERS.items()):
        fx, fy = v['fire']
        for cy, (x, y) in ((0, (fx, fy - 1)), (1, (fx, fy))):
            base = int(r['grid'][y, x] & 0x3FF); e = list(r['meta'][base])
            # the tip, over the cell above the fire: the top layer (a player there stands behind the fire, its flame before
            # his legs); the fire's own cell: the middle layer, under the sprites (a player south of it stands in front)
            lay = 8 if cy == 0 else 4; assert not any(e[lay:lay + 4])
            for q_ in range(4): e[lay + q_] = (first + cy * 4 + q_) | slot << 12
            r['meta'][nxt] = e; r['attrs'][nxt] = r['attrs'][base]
            lit.setdefault(k, []).append({'x': x, 'y': y, 'unlit': base, 'lit': nxt, 'solid': bool(r['grid'][y, x] & 0xC00)}); nxt += 1
    assert max(r['tiles']) < 1024 and nxt <= 1024
    ad = os.path.join(C, 'data/tilesets/secondary', SEC[0], 'anim', 'flame'); os.makedirs(ad, exist_ok=True)
    pal_flat = [v for c in r['pals'][slot] for v in c] + [0] * (768 - 48)
    for k, f in enumerate(frames):
        col = np.zeros((8 * 8, 8), np.uint8)
        for i, (cy, q_) in enumerate(order):
            col[i * 8:i * 8 + 8] = idx(f[cy * 16 + (q_ // 2) * 8:cy * 16 + (q_ // 2) * 8 + 8, (q_ % 2) * 8:(q_ % 2) * 8 + 8])
        im = Image.fromarray(col, 'P'); im.putpalette(pal_flat); im.save(os.path.join(ad, '%d.png' % k))
    print('flame tiles from', first, 'palette slot', slot, 'lit metatiles', lit)
    objs = []
    for k, v in sorted(P.CORNERS.items()):                       # the necromancers (Dale, Gram, two assistants)
        x, y = v['trainer']
        objs.append({'graphics_id': 'OBJ_EVENT_GFX_HEX_MANIAC', 'x': x, 'y': y, 'elevation': 3,
                     'movement_type': 'MOVEMENT_TYPE_FACE_DOWN', 'movement_range_x': 0, 'movement_range_y': 0,
                     'trainer_type': 'TRAINER_TYPE_NONE', 'trainer_sight_or_berry_tree_id': '0',
                     'script': 'NecropolisLake_EventScript_Necromancer', 'flag': '0'})
    mapj = {'id': MAPID, 'name': MAP, 'layout': LAYOUT, 'music': 'MUS_MT_PYRE',
            'region_map_section': 'MAPSEC_DR_MIRROH_NECROPOLIS', 'requires_flash': False, 'weather': 'WEATHER_NONE',
            'map_type': 'MAP_TYPE_UNDERGROUND', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': True, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
            'object_events': objs,
            'warp_events': [{'x': 21, 'y': 4, 'elevation': 3, 'dest_map': 'MAP_KIMARIS_CHAMBER', 'dest_warp_id': '0'}] +
                           [{'x': x, 'y': y, 'elevation': 3, 'dest_map': 'MAP_NECROPOLIS_GROUNDS', 'dest_warp_id': '4'} for (x, y) in mats],
            'coord_events': [], 'bg_events': []}
    void = int(r['grid'][H - 1, W - 1] & 0x3FF)                       # (the margin's far corner: pure void)
    assert (img[-16:, -16:] == np.array(LM.F.VOID)).all()
    MB.write(r, MAP, LAYOUT, PRIM, SEC, mapj, border=[void] * 4)
    json.dump(lit, open(os.path.join(C, 'data/maps', MAP, 'bonfires.json'), 'w'), indent=1)
    d = os.path.join(C, 'data/maps', MAP)
    pory = 'mapscripts NecropolisLake_MapScripts {\n'
    if TEST:                                                      # (a test build: every bonfire lit on entry)
        pory += '    MAP_SCRIPT_ON_LOAD {\n' + ''.join('        setmetatile(%d, %d, %d, %s)\n' % (c['x'], c['y'], c['lit'], 'TRUE' if c['solid'] else 'FALSE')
                                                       for k in sorted(lit) for c in lit[k]) + '    }\n'
    pory += '}\n\nscript NecropolisLake_EventScript_Necromancer {\n    lock\n    faceplayer\n' \
            '    msgbox("(A necromancer of House Langerin.\\nNo battle yet: the Trial is not written.)")\n    release\n}\n'
    open(os.path.join(d, 'scripts.pory'), 'w').write(pory)
    anim_code(first)

def anim_code(first):
    f = os.path.join(C, 'src/tileset_anims.c'); t = open(f).read()
    start, end = '// --- NecropolisLake bonfires (build_lake.py) ---\n', '// --- end NecropolisLake ---\n'
    if start in t: t = t[:t.index(start)] + t[t.index(end) + len(end):]
    block = start + ''.join('static const u16 sTilesetAnims_NecropolisLake_Flame%d[] = INCBIN_U16("data/tilesets/secondary/necropolis_lake/anim/flame/%d.4bpp");\n' % (k, k) for k in range(3)) \
        + 'static const u16 *const sTilesetAnims_NecropolisLake_Flame[] = {\n' + ''.join('    sTilesetAnims_NecropolisLake_Flame%d,\n' % k for k in range(3)) + '};\n\n' \
        + 'static void TilesetAnim_NecropolisLake(u16 timer)\n{\n    if (timer %% %d == 0)\n' % FLAME_TICK \
        + '        AppendTilesetAnimToBuffer(sTilesetAnims_NecropolisLake_Flame[(timer / %d) %% 3], (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(%d)), 8 * TILE_SIZE_4BPP);\n}\n\n' % (FLAME_TICK, first) \
        + 'void InitTilesetAnim_NecropolisLake(void)\n{\n    sSecondaryTilesetAnimCounter = 0;\n    sSecondaryTilesetAnimCounterMax = %d;\n' % (FLAME_TICK * 3) \
        + '    sSecondaryTilesetAnimCallback = TilesetAnim_NecropolisLake;\n}\n' + end
    open(f, 'w').write(t.rstrip('\n') + '\n\n' + block)
    h = os.path.join(C, 'include/tileset_anims.h'); ht = open(h).read()
    if 'InitTilesetAnim_NecropolisLake' not in ht:
        open(h, 'w').write(ht.replace('void InitTilesetAnim_General(void);', 'void InitTilesetAnim_General(void);\nvoid InitTilesetAnim_NecropolisLake(void);'))
    hd = os.path.join(C, 'src/data/tilesets/headers.h'); s = open(hd).read()
    i = s.index('const struct Tileset gTileset_NecropolisLake ='); j = s.index('};', i)
    open(hd, 'w').write(s[:i] + s[i:j].replace('.callback = NULL', '.callback = InitTilesetAnim_NecropolisLake') + s[j:])

if __name__ == '__main__':
    main()
