"""Build the ice path under Pelluca's church (PellucaIcePath) from its approved mock (user design 2026-11-19).

icepath_mock.py is the picture; this cuts it into its own tileset pair with the image method
(tools/art/academy/imgtiles.py), plus one extra row of variant cells only for their metatiles:
  thin ice -> cracked -> broken (the Sootopolis gym's own three looks), the gate's opening (bare floor), and
  "safe" ice: the thin ice's look with no behaviour (the solved field refreezes solid).
Their ids go to include/constants/metatile_labels.h (METATILE_PellucaIcePath_*) for src/field_tasks.c (the
Sootopolis step callback, made to use them on this layout) and the map scripts.
Collision by hand: the ice and the shrine floor walkable; the boulders, the ice wall and its gate, the statue, fire
rings, logs and flowers, and the ribs' feet solid; the rest of the three ribs over the player (he walks under
and between them).
Warps: 0 the landing (where the split drops you), 1 the ladder in the shrine's corner and 2 the Templars' rope
beside the landing, both up to the church hall (its arrival warp, written by tools/art/templar/build_ruined.py).
Credits as icepath_mock.py.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/icepath/build_icepath.py
"""
import os, sys, re
os.environ.setdefault('ODYSSEY_ROM', '/home/claude/crown/Crown.gba')
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'academy'))
import numpy as np
import imgtiles as IT, tilefit
import icepath_mock as M

MB_THIN_ICE, MB_CRACKED_ICE, MB_LADDER = 0x26, 0x27, 0x61
NAME, LAYOUT, MAP = 'PellucaIcePath', 'LAYOUT_PELLUCA_ICE_PATH', 'MAP_PELLUCA_ICE_PATH'
PRIM, SEC = ('pelluca_ice_path_tiles', 'PellucaIcePathTiles'), ('pelluca_ice_path', 'PellucaIcePath')
HALL, HALL_ARRIVAL = 'MAP_PELLUCA_TEMPLAR_HALL', 2          # the hall's warp 2: beside the split (build_ruined.py)
TOTAL = None                                                  # ice cells (set in main; the scripts' target is 1 + it)
VARIANTS = ['thin', 'cracked', 'broken', 'gate_open', 'safe']  # the extra row, left to right

MELT = (0.15, 0.4, 0.62, 0.84, 1.0)                                  # the awakening's melt frames (awaken_mock.py)
FIRE_FRAMES = 4
JOINT = 26                                                    # colours left in the statue's cells, all frames

def box_cells():
    """The cells the melt can touch: the statue's three columns and the next on each side (the ice block is wider
    than the statue), from its head's wall row to the meltwater row."""
    return [(x, y) for y in range(1, M.STATUE_BASE + 2) for x in range(M.STATUE_CX - 2, M.STATUE_CX + 3)]

def fit(img):
    x0, x1 = (M.STATUE_CX - 2) * 16, (M.STATUE_CX + 3) * 16
    return tilefit.reduce_tiles(img, (x0, 16, x1, (M.STATUE_BASE + 2) * 16))[0]

def cell(img, x, y): return img[y * 16:y * 16 + 16, x * 16:x * 16 + 16]

def main():
    import awaken_mock as A
    img, cells = M.compose(); W, H = M.W, M.H
    # the statue in its ice block has up to 19 colours in an 8x8 tile; merge its rarest near-shades until each tile
    # fits one palette (38 merges, no visible change; the sapphire ring kept)
    img, _ = tilefit.reduce_tiles(img, ((M.STATUE_CX - 1) * 16, 16, (M.STATUE_CX + 2) * 16, (M.STATUE_BASE + 1) * 16))
    ice, ladder_foot, rope, landing = cells['ice'], (M.LADDER[0], M.LADDER[1] + 1), M.ROPE, M.LANDING
    arch, arch_m = cells['arch']
    legs = cells['feet']
    # the ribs: free-standing, so the player can pass under them and between them: each leg's foot solid, every
    # other pixel of them in the over layer (he walks behind a rib north of its feet)
    om0 = arch_m.copy(); over0 = np.zeros_like(img); over0[arch_m] = arch[arch_m]
    for x, y in legs: om0[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = False    # (the feet in the bottom layer)
    # ---- the variant cells (their own rows under the map, only for their metatiles) ----
    rock = M.TSI.meta(M.ROCK)
    var = []                                                     # (key, under 16x16, over 16x16, mask 16x16, behaviour)
    blank_o, blank_m = np.zeros((16, 16, 3), np.uint8), np.zeros((16, 16), bool)
    looks = {'thin': M.SOOT.metatile(M.THIN), 'cracked': M.SOOT.metatile(M.CRACKED), 'broken': M.SOOT.metatile(M.BROKEN),
             'gate_open': rock, 'safe': M.SOOT.metatile(M.THIN)}
    for k in VARIANTS:
        var.append((k, looks[k], blank_o, blank_m, {'thin': MB_THIN_ICE, 'cracked': MB_CRACKED_ICE}.get(k, 0)))
    # the awakening (user 2026-11-20): the melt frames, each cell that differs from the statue as found
    sb = A.shrine_base()
    melt = [fit(A.scene(sb, A.melted(f), puddle_f=f)) for f in MELT]
    # the frames' blends of stone and thinning ice make new shades on every frame (58 colours in the statue's cells
    # across the frames: 17 palettes): merge them across all the frames together (the statue as found included, so
    # its cells stay the same picture in every frame) down to JOINT colours
    x0, x1, y1 = (M.STATUE_CX - 2) * 16, (M.STATUE_CX + 3) * 16, (M.STATUE_BASE + 2) * 16
    joint, merges = tilefit.reduce_joint([img] + melt, (x0, 16, x1, y1), JOINT)
    img, melt = joint[0], joint[1:]
    for i, fr in enumerate(melt):
        for x, y in box_cells():
            if (cell(fr, x, y) != cell(img, x, y)).any():
                var.append((('melt', i, (x, y)), cell(fr, x, y), cell(over0, x, y), cell(om0, x, y), 0))
    # the lit fire rings (holy sapphire flame, user): FIRE_FRAMES frames per ring, animated in game on dedicated tiles;
    # plus a "carrier" cell per ring whose four tiles hold every colour each quarter shows across the frames, so the
    # palette packing keeps those colours together in one palette per quarter
    lit = [A.scene(sb, A.melted(1.0), fire_scheme='holy', fire_k=k, puddle_f=1.0) for k in range(FIRE_FRAMES)]
    rings = {}                                                   # one lit metatile per distinct ring picture
    for x, y in sorted(cells['fires']):
        key = b''.join(cell(l, x, y).tobytes() for l in lit); rings.setdefault(key, []).append((x, y))
    union = set()
    for n_, cs in enumerate(rings.values()):
        x, y = cs[0]
        for k in range(FIRE_FRAMES):
            f = cell(lit[k], x, y); var.append((('fire', n_, k), f, blank_o, blank_m, 0))
            union |= {tuple(c) for c in ((f >> 3) << 3).reshape(-1, 3).tolist()}
    union = sorted(union); assert len(union) <= 15, f'fire colours {len(union)}'
    car = np.array([union[i % len(union)] for i in range(256)], np.uint8).reshape(16, 16, 3)
    var.append(('carrier', car, blank_o, blank_m, 0))
    nrows = (len(var) + W - 1) // W
    under = np.vstack([img, np.zeros((nrows * 16, W * 16, 3), np.uint8)])
    over = np.vstack([over0, np.zeros((nrows * 16, W * 16, 3), np.uint8)]); om = np.vstack([om0, np.zeros((nrows * 16, W * 16), bool)])
    for yy in range(nrows):
        for xx in range(W): cell(under, xx, H + yy)[:] = rock
    pos, vbeh = {}, {}
    for i, (k, u, o, m, b) in enumerate(var):
        x, y = i % W, H + i // W; pos[k] = (x, y); vbeh[(x, y)] = b
        cell(under, x, y)[:] = u; cell(over, x, y)[:] = o; cell(om, x, y)[:] = m
    solid = cells['statue'] | cells['fires'] | cells['flowers'] | cells['logs'] | legs
    shrine = cells['shrine'] - solid
    walk = ice | shrine | {ladder_foot, rope, landing}
    def beh(x, y):
        if y >= H: return vbeh.get((x, y), 0)
        if (x, y) in ice: return MB_THIN_ICE
        if (x, y) in (ladder_foot, rope): return MB_LADDER
        return 0
    r = IT.build(under, W, H + nrows, over=over, om=om, walk=walk, beh=beh, merge=16, rare=300, tries=2000)
    bad = IT.check(r)
    mid = lambda k: int(r['grid'][pos[k][1], pos[k][0]] & 0x3FF)
    ids = {k: mid(k) for k in VARIANTS}
    field_ids = {int(r['grid'][y, x] & 0x3FF) for x, y in ice}
    assert field_ids == {ids['thin']}, (field_ids, ids)             # every field cell is the one thin-ice metatile
    assert len(set(ids.values())) == len(ids), ids
    melt_ids = [{c: mid(('melt', i, c)) for c in box_cells() if ('melt', i, c) in pos} for i in range(len(MELT))]
    # the lit rings: dedicated tiles (frame 0), their metatile, and the animation frames
    anim, fire_ids = [], {}
    pals = [[tuple(c) for c in p] for p in r['pals']]
    for n_, cs in enumerate(rings.values()):
        frs = [cell(r['under'], *pos[('fire', n_, k)]) for k in range(FIRE_FRAMES)]       # (colour-merged)
        ent = []
        for q in range(4):
            qy, qx = (q // 2) * 8, (q % 2) * 8
            cols = {tuple(c) for f in frs for c in f[qy:qy + 8, qx:qx + 8].reshape(-1, 3).tolist()}
            slot = [s_ for s_, p in enumerate(pals) if cols <= set(p[1:])][0]
            lut = {c: i for i, c in enumerate(pals[slot]) if i}
            tiles = [np.array([[lut[tuple(f[qy + yy, qx + xx].tolist())] for xx in range(8)] for yy in range(8)], np.uint8) for f in frs]
            t = len(r['tiles']); r['tiles'].append(tiles[0]); ent.append(t | slot << 12)
            anim.append((t, tiles))
        r['meta'].append(ent + [0] * 8); r['attrs'].append(0)
        for c in cs: fire_ids[c] = 512 + len(r['meta']) - 1
    assert len(r['tiles']) <= 512 and len(r['meta']) <= 512, (len(r['tiles']), len(r['meta']))
    t0 = anim[0][0]; assert [a[0] for a in anim] == list(range(t0, t0 + len(anim)))     # one run of tiles
    r['grid'] = r['grid'][:H]
    warps = [{'x': x, 'y': y, 'elevation': 0, 'dest_map': HALL, 'dest_warp_id': str(HALL_ARRIVAL)}
             for x, y in (landing, ladder_foot, rope)]
    signs = [{'type': 'sign', 'x': x, 'y': M.STATUE_BASE, 'elevation': 0, 'player_facing_dir': 'BG_EVENT_PLAYER_FACING_NORTH',
              'script': 'PellucaIcePath_EventScript_Statue'} for x in (M.STATUE_CX - 1, M.STATUE_CX, M.STATUE_CX + 1)]
    mapj = {'id': MAP, 'name': NAME, 'layout': LAYOUT, 'music': 'MUS_DR_OLD_HQ',
            'region_map_section': 'MAPSEC_PELLUCA_VALLEY', 'requires_flash': False, 'weather': 'WEATHER_NONE',
            'map_type': 'MAP_TYPE_UNDERGROUND', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None, 'object_events': [],
            'warp_events': warps, 'coord_events': [], 'bg_events': signs}
    IT.write_room(r, NAME, LAYOUT, PRIM, SEC, mapj, after_layout='LAYOUT_PELLUCA_TEMPLAR_HALL', after_map='PellucaTemplarHall')
    # the flame animation: FIRE_FRAMES pictures of the run of dedicated tiles (gbagfx makes the .4bpp)
    from PIL import Image
    ad = os.path.join(IT.C, 'data/tilesets/primary', PRIM[0], 'anim', 'fire'); os.makedirs(ad, exist_ok=True)
    for k in range(FIRE_FRAMES):
        strip = np.hstack([tiles[k] for _, tiles in anim])
        im = Image.fromarray(strip, 'P'); im.putpalette([v for i in range(16) for v in (i * 17,) * 3] + [0] * (768 - 48))
        im.save(os.path.join(ad, f'{k}.png'))
    install_anim()
    # the metatile ids and the flame tiles for C and the scripts (secondary metatiles start at 512)
    lab = os.path.join(IT.C, 'include/constants/metatile_labels.h'); t = open(lab).read()
    block = ('// gTileset_PellucaIcePath (written by tools/art/icepath/build_icepath.py)\n' +
             ''.join(f'#define {"METATILE_PellucaIcePath_" + k.title().replace("_", ""):<38} 0x{ids[k]:03X}\n' for k in VARIANTS) +
             f'#define {"DR_ICE_PATH_FIRE_TILE":<38} {t0}\n#define {"DR_ICE_PATH_FIRE_TILES":<38} {len(anim)}\n'
             f'#define {"DR_ICE_PATH_FIRE_FRAMES":<38} {FIRE_FRAMES}\n')
    t = re.sub(r'// gTileset_PellucaIcePath \(written by[^\n]*\n(#define (METATILE_PellucaIcePath_|DR_ICE_PATH_)[^\n]*\n)*', '', t)
    t = t.replace('\n#endif // GUARD_METATILE_LABELS_H', block + '\n#endif // GUARD_METATILE_LABELS_H')
    open(lab, 'w').write(t)
    n = len(ice); gx, gy = M.GATE
    def sets(d): return ''.join(f'    setmetatile({x}, {y}, 0x{v:03X}, {"FALSE" if (x, y) in walk else "TRUE"})\n' for (x, y), v in sorted(d.items()))
    subs = ''.join(f'script PellucaIcePath_EventScript_Melt{i} {{\n{sets(d)}    return\n}}\n\n' for i, d in enumerate(melt_ids))
    fl, fr_ = [sorted(fire_ids.items())[0]], [sorted(fire_ids.items())[1]]
    subs += f'script PellucaIcePath_EventScript_LightLeftFire {{\n{sets(dict(fl))}    return\n}}\n\n'
    subs += f'script PellucaIcePath_EventScript_LightRightFire {{\n{sets(dict(fr_))}    return\n}}\n\n'
    melt_calls = ''.join(f'    call(PellucaIcePath_EventScript_Melt{i})\n    special(DrawWholeMapView)\n    delay(24)\n' for i in range(len(MELT)))
    sp = os.path.join(IT.C, 'data/maps', NAME, 'scripts.pory')
    open(sp, 'w').write(SCRIPTS.format(target=1 + n, n=n, gx=gx, gy=gy, last=len(MELT) - 1) +
                       AWAKEN.format(melt_calls=melt_calls) + subs)
    write_opal_icon(A)
    print(f'ice path {W}x{H} tiles {len(r["tiles"])} metatiles {len(r["meta"])} palettes {r["npal"]} mismatches {bad} '
          f'ice cells {n} melt cells {[len(d) for d in melt_ids]} fire tiles {t0}+{len(anim)} '
          f'ids {", ".join(f"{k}=0x{v:03X}" for k, v in ids.items())}')

def write_opal_icon(A):
    """The Sparkling Opal's bag icon (awaken_mock.opal_icon), as the item graphics want it: 24x24 4bpp + palette."""
    from PIL import Image
    rgb, m = A.opal_icon(); rgb = (rgb >> 3) << 3
    cols = sorted({tuple(c) for c in rgb[m].tolist()}, key=sum)
    if len(cols) > 15:
        q = Image.fromarray(rgb[m].reshape(1, -1, 3)).quantize(15, method=Image.Quantize.MEDIANCUT)
        pal = np.array(q.getpalette()[:45], np.uint8).reshape(-1, 3); rgb[m] = pal[np.array(q)[0]]
        cols = sorted({tuple(c) for c in rgb[m].tolist()}, key=sum)
    lut = {c: i + 1 for i, c in enumerate(cols)}
    idx = np.zeros((24, 24), np.uint8)
    for y, x in zip(*np.nonzero(m)): idx[y, x] = lut[tuple(rgb[y, x].tolist())]
    P = [(0, 0, 0)] + cols + [(0, 0, 0)] * (15 - len(cols))
    im = Image.fromarray(idx, 'P'); im.putpalette([v for c in P for v in c] + [0] * (768 - 48))
    im.save(os.path.join(IT.C, 'graphics/items/icons/sparkling_opal.png'))
    with open(os.path.join(IT.C, 'graphics/items/icon_palettes/sparkling_opal.pal'), 'w', newline='') as f:
        f.write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join(f'{r} {g} {b}\r\n' for r, g, b in P))

ANIM_C = """
// DR: the ice path's lit fire rings (tools/art/icepath/build_icepath.py): DR_ICE_PATH_FIRE_FRAMES frames of the
// holy sapphire flame on a run of DR_ICE_PATH_FIRE_TILES dedicated primary tiles from DR_ICE_PATH_FIRE_TILE (only
// the lit-ring metatile uses them, so the flames show once the shrine has awakened). A new frame every 8 game frames.
static const u16 gTilesetAnims_PellucaIcePath_Fire_Frame0[] = INCBIN_U16("data/tilesets/primary/pelluca_ice_path_tiles/anim/fire/0.4bpp");
static const u16 gTilesetAnims_PellucaIcePath_Fire_Frame1[] = INCBIN_U16("data/tilesets/primary/pelluca_ice_path_tiles/anim/fire/1.4bpp");
static const u16 gTilesetAnims_PellucaIcePath_Fire_Frame2[] = INCBIN_U16("data/tilesets/primary/pelluca_ice_path_tiles/anim/fire/2.4bpp");
static const u16 gTilesetAnims_PellucaIcePath_Fire_Frame3[] = INCBIN_U16("data/tilesets/primary/pelluca_ice_path_tiles/anim/fire/3.4bpp");
static const u16 *const gTilesetAnims_PellucaIcePath_Fire[] = {
    gTilesetAnims_PellucaIcePath_Fire_Frame0, gTilesetAnims_PellucaIcePath_Fire_Frame1,
    gTilesetAnims_PellucaIcePath_Fire_Frame2, gTilesetAnims_PellucaIcePath_Fire_Frame3,
};

static void TilesetAnim_PellucaIcePath(u16 timer)
{
    if (timer % 8 == 0)
        AppendTilesetAnimToBuffer(gTilesetAnims_PellucaIcePath_Fire[(timer / 8) % DR_ICE_PATH_FIRE_FRAMES],
                                  (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(DR_ICE_PATH_FIRE_TILE)),
                                  DR_ICE_PATH_FIRE_TILES * TILE_SIZE_4BPP);
}

void InitTilesetAnim_PellucaIcePath(void)
{
    sPrimaryTilesetAnimCounter = 0;
    sPrimaryTilesetAnimCounterMax = 256;
    sPrimaryTilesetAnimCallback = TilesetAnim_PellucaIcePath;
}
"""

def install_anim():
    """Once: the animation code, its declaration, and the primary tileset's callback."""
    assert FIRE_FRAMES == 4                                     # (ANIM_C lists four frames)
    f = os.path.join(IT.C, 'src/tileset_anims.c'); t = open(f).read()
    if 'TilesetAnim_PellucaIcePath' not in t:
        if '#include "constants/metatile_labels.h"' not in t:
            t = t.replace('#include "global.h"\n', '#include "global.h"\n#include "constants/metatile_labels.h"\n', 1)
        open(f, 'w').write(t.rstrip('\n') + '\n' + ANIM_C)
    f = os.path.join(IT.C, 'include/tileset_anims.h'); t = open(f).read()
    if 'InitTilesetAnim_PellucaIcePath' not in t:
        t = t.replace('void InitTilesetAnim_Cormoria(void);\n', 'void InitTilesetAnim_Cormoria(void);\nvoid InitTilesetAnim_PellucaIcePath(void);\n')
        open(f, 'w').write(t)
    f = os.path.join(IT.C, 'src/data/tilesets/headers.h'); t = open(f).read()
    i = t.index('const struct Tileset gTileset_PellucaIcePathTiles ='); j = t.index('};', i)
    open(f, 'w').write(t[:i] + t[i:j].replace('.callback = NULL', '.callback = InitTilesetAnim_PellucaIcePath') + t[j:])

SCRIPTS = '''// ============ DREAMSTONE RUINATION - Pelluca: the ice path under the church ============
// Written by tools/art/icepath/build_icepath.py (user design 2026-11-19; bible 20_chapter1_build.md).
// The thin-ice field (after Pokemon Pisces' Sootopolis gym): every one of its {n} ice cells must crack exactly once.
// The Sootopolis step callback counts VAR_ICE_STEP_COUNT up from 1 per fresh cell and sets it to 0 on a cracked one.
//   {target} (all cracked): the gate in the ice wall gives way, the field refreezes solid (DrIcePathFreeze), solved.
//   0 (a second step on a cracked cell): the ice breaks; black out, back on the landing with a fresh field.
// NPCs and dialogue (the Templar, the discovery) come with the story pass.

mapscripts PellucaIcePath_MapScripts {{
    MAP_SCRIPT_ON_LOAD {{
        if (flag(FLAG_DR_ICE_PATH_SOLVED)) {{
            setvar(VAR_ICE_STEP_COUNT, 999)
            call(PellucaIcePath_EventScript_SetSolved)
            if (flag(FLAG_DR_STATUE_AWAKENED)) {{
                call(PellucaIcePath_EventScript_SetAwakened)
            }}
        }} else {{
            special(DrIcePathReset)
        }}
    }}
    MAP_SCRIPT_ON_RESUME {{
        setstepcallback(STEP_CB_SOOTOPOLIS_ICE)
    }}
    MAP_SCRIPT_ON_FRAME_TABLE [
        VAR_ICE_STEP_COUNT, {target}: PellucaIcePath_EventScript_Solved
        VAR_ICE_STEP_COUNT, 0: PellucaIcePath_EventScript_FallThroughIce
    ]
}}

script PellucaIcePath_EventScript_SetSolved {{
    setmetatile({gx}, {gy}, METATILE_PellucaIcePath_GateOpen, FALSE)
    special(DrIcePathFreeze)
    return
}}

script PellucaIcePath_EventScript_Solved {{
    lockall
    setvar(VAR_ICE_STEP_COUNT, 999)
    delay(40)
    playse(SE_ICE_STAIRS)
    call(PellucaIcePath_EventScript_SetSolved)
    special(DrawWholeMapView)
    setflag(FLAG_DR_ICE_PATH_SOLVED)
    releaseall
    end
}}

script PellucaIcePath_EventScript_FallThroughIce {{
    lockall
    delay(20)
    applymovement(OBJ_EVENT_ID_PLAYER, PellucaIcePath_Movement_FallThroughIce)
    waitmovement(0)
    playse(SE_FALL)
    delay(60)
    warpsilent(MAP_PELLUCA_ICE_PATH, 0)
    waitstate
    end
}}

movement PellucaIcePath_Movement_FallThroughIce {{
    set_invisible
}}

script PellucaIcePath_EventScript_SetAwakened {{
    call(PellucaIcePath_EventScript_Melt{last})
    call(PellucaIcePath_EventScript_LightLeftFire)
    call(PellucaIcePath_EventScript_LightRightFire)
    return
}}
'''

AWAKEN = '''
// ---- The awakening (user 2026-11-20): with the field solved, A on the statue: dramatic music (Rayquaza Appears) from
// the touch, a rumble, the ice melts off it, the seal breaks in a holy light with Arceus's cry echoing, the fire rings
// light (holy sapphire flame, animated), the music ends; something falls out of the ice: the Sparkling Opal. (Later, stage 4: the Opal goes to Archbishop Ambrose up in the church, for the Warding Ring.)
script PellucaIcePath_EventScript_Statue {{
    if (flag(FLAG_DR_STATUE_AWAKENED)) {{
        end
    }}
    lockall
    playbgm(MUS_RAYQUAZA_APPEARS, FALSE)
    delay(16)
    playse(SE_M_EARTHQUAKE)
    setvar(VAR_0x8004, 1)
    setvar(VAR_0x8005, 1)
    setvar(VAR_0x8006, 12)
    setvar(VAR_0x8007, 4)
    special(ShakeCamera)
    waitstate
    delay(20)
    playse(SE_M_MORNING_SUN)
{melt_calls}    waitse
    fadescreenspeed(FADE_TO_WHITE, 4)
    special(DrPlayEchoCry)
    delay(30)
    fadescreenspeed(FADE_FROM_WHITE, 4)
    waitmoncry
    special(DrEndEchoCry)
    delay(20)
    call(PellucaIcePath_EventScript_LightLeftFire)
    special(DrawWholeMapView)
    playse(SE_M_SACRED_FIRE)
    delay(30)
    call(PellucaIcePath_EventScript_LightRightFire)
    special(DrawWholeMapView)
    playse(SE_M_SACRED_FIRE)
    waitse
    delay(30)
    fadedefaultbgm
    delay(40)
    showportrait(PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL)
    special(DrSetPrinceNameplate)
    msgbox(format("Something fell down out of the ice... Could this be...!!"))
    hideportrait
    closemessage
    setvar(VAR_0x8004, ITEM_SPARKLING_OPAL)
    setvar(VAR_0x8005, 1)
    setvar(VAR_0x8006, ITEM_SPARKLING_OPAL)
    setvar(VAR_0x8007, TRUE)
    additem(ITEM_SPARKLING_OPAL)
    bufferitemname(STR_VAR_2, ITEM_SPARKLING_OPAL)
    checkitemtype(ITEM_SPARKLING_OPAL)
    call(EventScript_BufferPocketNameAndTryFanfare)
    message(format("{{PLAYER}} found the Sparkling Opal!"))
    showitemdescription
    waitfanfare
    waitmessage
    msgbox(gText_PutItemInPocket, MSGBOX_DEFAULT)
    hideitemdescription
    setflag(FLAG_DR_STATUE_AWAKENED)
    releaseall
    end
}}

'''

if __name__ == '__main__':
    main()
