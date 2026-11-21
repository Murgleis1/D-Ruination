"""Build Kimaris's Trial chamber (user 2026-11-21) into the game: MAP_KIMARIS_CHAMBER.

The room is Fantasma's summoning room (its mapsec 1, layout s001_b8b0, 17x15; the user: "actually perfect for the
Kimaris fight"), drawn by tools/fantasma/fsread.py and cut into its own tileset pair by academy/imgtiles.py.
Credit: Fantasma (permission to be asked).

On its left side stands **the boiling cauldron from Rinri's house in MonoMyth's Wood Avens** (user 2026-11-21),
its brew turned a ghostly white. In MonoMyth it is the hut tileset 0x87310D4's metatiles 0x2A0-0x2B2 (the brew,
the splashes and the rim, all on the top layer, animated) over the hut's cauldron legs (metatiles 0x282-0x284).
The animation: every 8 frames the hut's tileset callback (0x809B901 -> 0x809B918) copies frame (timer / 8) % 9
of the list at 0x89691C0 (9 frames, 24 tiles) to VRAM tile 0x320. Here the same 9 frames, recoloured, are
redrawn as the cauldron's 3x3 top layer (36 tiles of their own) and played by InitTilesetAnim_KimarisChamber
(src/tileset_anims.c) the same way: a frame every 8 frames.
Credit: MonoMyth (the cauldron and its animation).

Placement (the chamber's cells): the cauldron's top layer on x 3-5, y 3-5 (its splashes above, the brew on
row 5), its legs on row 6; rows 5-6 solid, rows 3-4 walked behind.
Warps: the stair foot (8, 14) is a south arrow warp down to the lake's sealed arch (lake warp 0, at (21, 4));
the lake's arch warps up here. The arch stays solid until the Trial is scripted (all four bonfires lit).
The barred door behind Kimaris (the secret way down to the Distortion gate and the Necropolis Dreamstone) stays
shut: no warp (late game).
With DR_KIMARIS_TEST=1, a test way in: Hollow Hill's way north warps straight here (rebuild without it).
Usage: python3 tools/art/necropolis/build_kimaris.py   (then make)
"""
import os, sys, json, pickle
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'academy'))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'fantasma')); sys.path.insert(0, os.path.join(HERE, '..', '..', 'monomyth'))
import imgtiles as IT

C = IT.C
MAP, LAYOUT, MAPID = 'KimarisChamber', 'LAYOUT_KIMARIS_CHAMBER', 'MAP_KIMARIS_CHAMBER'
PRIM, SEC = ('kimaris_chamber_tiles', 'KimarisChamberTiles'), ('kimaris_chamber', 'KimarisChamber')
MB_NORMAL, MB_SOUTH_ARROW_WARP = 0x00, 0x65
CX, CY = 3, 3                        # the cauldron's top-left cell (its 3x3 top layer), legs on CY + 3
STAIR = (8, 14)
TEST = bool(os.environ.get('DR_KIMARIS_TEST'))
FANT_HEADERS = os.environ.get('FANTASMA_HEADERS', '/tmp/fant_hs.pkl')

# ------------------------------------------------------------------ the room (Fantasma)
def room():
    import fsread as F
    hs = pickle.load(open(FANT_HEADERS, 'rb'))
    L = [h for h in hs if h['mapsec'] == 1 and (h['layout']['addr'] & 0xffff) == 0xb8b0][0]['layout']
    img = F.render(L); o = F.off(L['map'])
    raw = np.frombuffer(F.ROM[o:o + L['w'] * L['h'] * 2], '<u2').reshape(L['h'], L['w'])
    return img, (raw >> 10) & 3

# ------------------------------------------------------------------ the cauldron (MonoMyth)
GHOST = np.array([(150, 160, 184), (200, 210, 226), (236, 242, 252)], float)
# MonoMyth's iron is lit green by its brew; here a cold, neutral iron (darkest to lightest)
IRON = {(88, 80, 104): (30, 28, 40), (96, 112, 104): (58, 58, 74), (136, 128, 152): (92, 92, 112),
        (160, 168, 144): (150, 152, 170)}
def ghostly(rgba):
    """The brew and its splashes from MonoMyth's swamp green to a ghostly white (by their own lightness, so the
    small splashes stay bright); the iron to a cold grey."""
    out = rgba.copy(); f = rgba[..., :3].astype(int); a = rgba[..., 3] > 0
    q = (f >> 3) << 3
    iron = np.zeros(a.shape, bool)
    for src, dst in IRON.items():
        m = a & (q == src).all(-1); out[..., :3][m] = dst; iron |= m
    green = a & ~iron & (f[..., 1] > f[..., 0] + 16) & (f[..., 1] > f[..., 2] + 8)
    g = f[..., 1][green]
    out[..., :3][green] = GHOST[np.digitize(g, [150, 200])].astype(np.uint8)
    return out

def cauldron():
    """-> (frames: 9 RGBA 48x48 top layers, legs: RGBA 48x16)."""
    import romlib, render
    from romlib import ROM, u16, off, u32
    hs = romlib.find_headers(); L = [h for h in hs if h['addr'] == 0x86ac94][0]['layout']
    FR = [u32(off(0x89691c0) + 4 * i) for i in range(9)]
    def ts_frame(k):
        ts = render.TS(L); a = np.frombuffer(ROM[off(FR[k]):off(FR[k]) + 768], np.uint8).reshape(24, 32)
        t = np.zeros((24, 8, 8), np.uint8); t[:, :, 0::2] = (a & 15).reshape(24, 8, 4); t[:, :, 1::2] = (a >> 4).reshape(24, 8, 4)
        st = list(ts.st)
        while len(st) < 0x140: st.append(np.zeros((8, 8), np.uint8))
        for i in range(24): st[0x120 + i] = t[i]
        ts.st = st; return ts
    def layers(ts, m, which):
        base = ts.pmt + m * 24 if m < 512 else ts.smt + (m - 512) * 24
        img = np.zeros((16, 16, 4), np.uint8)
        for q in range(12):
            if q // 4 not in which: continue
            e = u16(base + 2 * q); t = ts.tile(e & 0x3ff)
            if t is None: continue
            if (e >> 10) & 1: t = t[:, ::-1]
            if (e >> 11) & 1: t = t[::-1, :]
            oy, ox = ((q % 4) // 2) * 8, ((q % 4) % 2) * 8; pal = np.array(ts.pal[e >> 12], np.uint8)
            m_ = t != 0; blk = img[oy:oy + 8, ox:ox + 8]; blk[..., :3][m_] = pal[t][m_]; blk[..., 3][m_] = 255
        return img
    frames = []
    for k in range(9):
        ts = ts_frame(k)
        frames.append(ghostly(np.concatenate([np.concatenate([layers(ts, m, [2]) for m in r], 1)
                                              for r in ([0x2a0, 0x2a1, 0x2a2], [0x2a8, 0x2a9, 0x2aa], [0x2b0, 0x2b1, 0x2b2])], 0)))
    ts = ts_frame(0)
    legs = np.concatenate([layers(ts, m, [1, 2]) for m in (0x282, 0x283, 0x284)], 1)
    floor = layers(ts, 0x28b, [0, 1, 2])                          # the hut's planks: flooded out from the row's
    fl = {tuple(c) for c in floor[..., :3].reshape(-1, 3)}          # edges, stopping at the legs' dark outline
    bg = np.zeros((16, 48), bool); st = [(y, x) for y in range(16) for x in (0, 47)] + [(15, x) for x in range(48)]
    while st:
        y, x = st.pop()
        if 0 <= y < 16 and 0 <= x < 48 and not bg[y, x] and (not legs[y, x, 3] or tuple(legs[y, x, :3]) in fl) \
                and tuple(legs[y, x, :3]) != (88, 80, 104):
            bg[y, x] = True; st += [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    legs[bg, 3] = 0
    f = legs[..., :3].astype(int); legs[(f[..., 0] > f[..., 2] + 20), 3] = 0     # the planks seen between the legs
    for y in range(16):                                            # plank seams running in from the row's ends
        for xs in (range(48), range(47, -1, -1)):
            for x in xs:
                if not legs[y, x, 3]: continue
                up = y > 0 and legs[y - 1, x, 3]; dn = y < 15 and legs[y + 1, x, 3]
                if up or dn: break
                legs[y, x, 3] = 0
    return frames, ghostly(legs)

def quantize(frames, legs, n=15):
    """One palette for the cauldron (its animated top layer must keep to one): all frames and the legs together."""
    allpx = np.concatenate([f[..., :3][f[..., 3] > 0] for f in frames] + [legs[..., :3][legs[..., 3] > 0]])
    cols = np.unique((allpx >> 3) << 3, axis=0)
    if len(cols) > n:
        im = Image.fromarray(allpx.reshape(1, -1, 3).astype(np.uint8)).quantize(colors=n, method=Image.Quantize.MAXCOVERAGE, dither=Image.Dither.NONE)
        pal = np.array(im.getpalette()[:n * 3]).reshape(n, 3)
    else: pal = cols
    pal = (pal >> 3) << 3
    def snap(img):
        out = img.copy(); m = img[..., 3] > 0; px = img[..., :3][m].astype(int)
        out[..., :3][m] = pal[((px[:, None, :] - pal[None]) ** 2).sum(-1).argmin(1)]
        return out
    return [snap(f) for f in frames], snap(legs), [tuple(int(v) for v in c) for c in pal]

def main():
    img, coll = room(); H, W = coll.shape
    frames, legs, cpal = quantize(*cauldron())
    under = img.copy()
    ly = (CY + 3) * 16; lx = CX * 16                            # a soft shadow on the floor, then the legs
    yy, xx = np.mgrid[0:16, 0:48]; sh = ((xx - 24) / 22.0) ** 2 + ((yy - 12) / 5.0) ** 2 < 1
    sub = under[ly:ly + 16, lx:lx + 48]; sub[sh] = (sub[sh] * 0.55).astype(np.uint8)
    a = legs[..., 3] > 0; sub[a] = legs[..., :3][a]
    walk = set()
    for y in range(H):
        for x in range(W):
            if coll[y, x] == 0: walk.add((x, y))
    walk |= {(x, y) for x in (7, 8, 9) for y in (12, 13, 14)}            # the stair down
    for x in range(CX, CX + 3):
        for y in (CY + 2, CY + 3): walk.discard((x, y))                   # the cauldron's bowl and legs
    beh = lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) == STAIR else MB_NORMAL
    r = IT.build(under, W, H, walk=walk, beh=beh, tries=400)
    # the cauldron's top layer: 36 tiles of its own (so its frames can be copied over them), one palette
    assert r['npal'] < 13, r['npal']
    slot = len(r['pals']); r['pals'].append([(0, 0, 0)] + cpal + [(0, 0, 0)] * (15 - len(cpal)))
    lut = {c: i + 1 for i, c in enumerate(cpal)}
    def idx(rgba):
        t = np.zeros(rgba.shape[:2], np.uint8)
        for (y, x) in zip(*np.where(rgba[..., 3] > 0)): t[y, x] = lut[tuple(int(v) for v in rgba[y, x, :3])]
        return t
    first = len(r['tiles']); order = []
    for cy in range(3):
        for cx in range(3):
            g = int(r['grid'][CY + cy, CX + cx]); e = list(r['meta'][(g & 0x3FF) - 512])
            for q in range(4):
                n = len(r['tiles']); order.append((cy, cx, q))
                tq = idx(frames[0][cy * 16 + (q // 2) * 8:cy * 16 + (q // 2) * 8 + 8, cx * 16 + (q % 2) * 8:cx * 16 + (q % 2) * 8 + 8])
                r['tiles'].append(tq); e[8 + q] = n | slot << 12
            r['meta'].append(e); r['attrs'].append(r['attrs'][(g & 0x3FF) - 512])
            r['grid'][CY + cy, CX + cx] = (512 + len(r['meta']) - 1) | (g & 0xFC00)
    assert len(r['tiles']) <= 512 and len(r['meta']) <= 512, (len(r['tiles']), len(r['meta']))
    print('palettes', len(r['pals']), 'tiles', len(r['tiles']), 'metatiles', len(r['meta']), 'cauldron tiles from', first)
    # the frames, as the animation's pictures (8 px wide: its 36 tiles in order)
    ad = os.path.join(C, 'data/tilesets/secondary', SEC[0], 'anim', 'cauldron'); os.makedirs(ad, exist_ok=True)
    pal_flat = [v for c in r['pals'][slot] for v in c] + [0] * (768 - 48)
    for k, f in enumerate(frames):
        col = np.zeros((36 * 8, 8), np.uint8)
        for i, (cy, cx, q) in enumerate(order):
            col[i * 8:i * 8 + 8] = idx(f[cy * 16 + (q // 2) * 8:cy * 16 + (q // 2) * 8 + 8, cx * 16 + (q % 2) * 8:cx * 16 + (q % 2) * 8 + 8])
        im = Image.fromarray(col, 'P'); im.putpalette(pal_flat); im.save(os.path.join(ad, '%d.png' % k))
    open(os.path.join(ad, 'FIRST_TILE'), 'w').write('%d\n' % first)
    objs = [{'graphics_id': 'OBJ_EVENT_GFX_KIMARIS', 'x': 8, 'y': 8, 'elevation': 3,
             'movement_type': 'MOVEMENT_TYPE_FACE_DOWN', 'movement_range_x': 0, 'movement_range_y': 0,
             'trainer_type': 'TRAINER_TYPE_NONE', 'trainer_sight_or_berry_tree_id': '0',
             'script': 'KimarisChamber_EventScript_Kimaris', 'flag': '0'}]
    mapj = {'id': MAPID, 'name': MAP, 'layout': LAYOUT, 'music': 'MUS_MT_PYRE',
            'region_map_section': 'MAPSEC_DR_MIRROH_NECROPOLIS', 'requires_flash': False, 'weather': 'WEATHER_NONE',
            'map_type': 'MAP_TYPE_INDOOR', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
            'object_events': objs,
            'warp_events': [{'x': STAIR[0], 'y': STAIR[1], 'elevation': 3, 'dest_map': 'MAP_NECROPOLIS_LAKE', 'dest_warp_id': '0'}],
            'coord_events': [], 'bg_events': []}
    IT.write_room(r, MAP, LAYOUT, PRIM, SEC, mapj)
    d = os.path.join(C, 'data/maps', MAP)
    open(os.path.join(d, 'scripts.pory'), 'w').write(
        'mapscripts KimarisChamber_MapScripts {}\n\n'
        'script KimarisChamber_EventScript_Kimaris {\n    lock\n    faceplayer\n'
        '    msgbox("(Kimaris Langerin waits on the sigil.\\nThe Trial is not written yet.)")\n    release\n}\n')
    anim_code()
    lake_warp()
    test_entrance()

def anim_code():
    """The cauldron's animation in src/tileset_anims.c and its callback on the chamber's secondary tileset."""
    first = int(open(os.path.join(C, 'data/tilesets/secondary', SEC[0], 'anim/cauldron/FIRST_TILE')).read())
    f = os.path.join(C, 'src/tileset_anims.c'); t = open(f).read()
    start, end = '// --- KimarisChamber cauldron (build_kimaris.py) ---\n', '// --- end KimarisChamber ---\n'
    if start in t: t = t[:t.index(start)] + t[t.index(end) + len(end):]
    block = start + ''.join('static const u16 sTilesetAnims_KimarisChamber_Cauldron_Frame%d[] = INCBIN_U16("data/tilesets/secondary/kimaris_chamber/anim/cauldron/%d.4bpp");\n' % (k, k) for k in range(9)) \
        + 'static const u16 *const sTilesetAnims_KimarisChamber_Cauldron[] = {\n' + ''.join('    sTilesetAnims_KimarisChamber_Cauldron_Frame%d,\n' % k for k in range(9)) + '};\n\n' \
        + 'static void TilesetAnim_KimarisChamber(u16 timer)\n{\n    if (timer % 8 == 0)\n' \
        + '        AppendTilesetAnimToBuffer(sTilesetAnims_KimarisChamber_Cauldron[(timer / 8) % ARRAY_COUNT(sTilesetAnims_KimarisChamber_Cauldron)],\n' \
        + '                                  (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(%d)), 36 * TILE_SIZE_4BPP);\n}\n\n' % first \
        + 'void InitTilesetAnim_KimarisChamber(void)\n{\n    sSecondaryTilesetAnimCounter = 0;\n    sSecondaryTilesetAnimCounterMax = 72;\n' \
        + '    sSecondaryTilesetAnimCallback = TilesetAnim_KimarisChamber;\n}\n' + end
    t = t.rstrip('\n') + '\n\n' + block
    open(f, 'w').write(t)
    h = os.path.join(C, 'include/tileset_anims.h'); ht = open(h).read()
    if 'InitTilesetAnim_KimarisChamber' not in ht:
        ht = ht.replace('void InitTilesetAnim_General(void);', 'void InitTilesetAnim_General(void);\nvoid InitTilesetAnim_KimarisChamber(void);')
        open(h, 'w').write(ht)
    hd = os.path.join(C, 'src/data/tilesets/headers.h'); s = open(hd).read()
    i = s.index('const struct Tileset gTileset_KimarisChamber ='); j = s.index('};', i)
    s = s[:i] + s[i:j].replace('.callback = NULL', '.callback = InitTilesetAnim_KimarisChamber') + s[j:]
    open(hd, 'w').write(s)

def lake_warp():
    """The lake's sealed arch: a warp up to the chamber (the arch's cell stays solid until the Trial opens it)."""
    j = os.path.join(C, 'data/maps/NecropolisLake/map.json'); m = json.load(open(j))
    m['warp_events'] = [{'x': 21, 'y': 4, 'elevation': 3, 'dest_map': MAPID, 'dest_warp_id': '0'}]
    json.dump(m, open(j, 'w'), indent=2); open(j, 'a').write('\n')

def test_entrance():
    hj = os.path.join(C, 'data/maps/HollowHill/map.json'); hm = json.load(open(hj))
    hm['coord_events'] = [e for e in hm['coord_events'] if e.get('script') != 'HollowHill_EventScript_KimarisTest']
    hp = os.path.join(C, 'data/maps/HollowHill/scripts.pory'); hs = open(hp).read()
    i = hs.find('\n\nscript HollowHill_EventScript_KimarisTest'); hs = hs if i < 0 else hs[:i] + '\n'
    if TEST:
        hm['coord_events'].append({'type': 'trigger', 'x': 17, 'y': 6, 'elevation': 3, 'var': 'VAR_TEMP_1', 'var_value': '0',
                                   'script': 'HollowHill_EventScript_KimarisTest'})
        hs = hs.rstrip('\n') + '\n\nscript HollowHill_EventScript_KimarisTest {\n    setvar(VAR_TEMP_1, 1)\n' \
             '    warp(%s, 8, 13)\n}\n' % MAPID
    json.dump(hm, open(hj, 'w'), indent=2); open(hj, 'a').write('\n'); open(hp, 'w').write(hs)

if __name__ == '__main__':
    main()
