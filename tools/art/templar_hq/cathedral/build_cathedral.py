"""Build the Templar cathedral's interior into the game (user 2026-11-23: the approved mocks; "Lets proceed").

MAP_TEMPLAR_CATHEDRAL, the nave (nave_mock_v2 without Ambrose, the stained-glass Arceus over it; collision in
nave_grid.py): its exit (the carpet's last row) leads out to the courtyard's church door (build_citadel.py makes that
door, warp 0 there); its five doors lead to the offices; the Sanctum's grille is sealed (a sign).
Each room has its own tileset pair (tools/art/mapbuild.py).
Usage: python3 tools/art/templar_hq/cathedral/build_cathedral.py [rooms...]   (then build_citadel.py; then make)
"""
import os, sys, json, subprocess
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); TQ = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(TQ, '..'))
for d in ('nave', 'study', 'bishops', 'registry', 'kitchen', 'storehouse', 'glass'): sys.path.insert(0, os.path.join(TQ, d))
import mapbuild as MB
import nave_grid as NG
C = MB.C
MB_NORMAL, MB_SOUTH_ARROW_WARP, MB_DOOR = 0x00, 0x65, 0x60
SCR = '/tmp/cathedral_build'; os.makedirs(SCR, exist_ok=True)

# room key: (map name, map id)
ROOMS = {'nave': ('TemplarCathedral', 'MAP_TEMPLAR_CATHEDRAL'),
         'study': ('TemplarCathedralStudy', 'MAP_TEMPLAR_CATHEDRAL_STUDY'),
         'bishops': ('TemplarCathedralBishopsHall', 'MAP_TEMPLAR_CATHEDRAL_BISHOPS_HALL'),
         'dorm': ('TemplarCathedralDormitory', 'MAP_TEMPLAR_CATHEDRAL_DORMITORY'),
         'registry': ('TemplarCathedralRegistry', 'MAP_TEMPLAR_CATHEDRAL_REGISTRY'),
         'kitchen': ('TemplarCathedralKitchen', 'MAP_TEMPLAR_CATHEDRAL_KITCHEN'),
         'storehouse': ('TemplarCathedralStorehouse', 'MAP_TEMPLAR_CATHEDRAL_STOREHOUSE')}
OFFICES = ['study', 'bishops', 'registry', 'kitchen', 'storehouse']
NAVE_EXITS = [(x, y) for y, row in enumerate(NG.GRID) for x, c in enumerate(row) if c == 'E']
# the nave's warps: its exits first (0..), then a door per office, in OFFICES order
NAVE_DOOR_WARP = {k: len(NAVE_EXITS) + i for i, k in enumerate(OFFICES)}

def mapj(key, warps, objs=(), bgs=(), music='MUS_DR_MM_ROUTE15'):
    name, mid = ROOMS[key]
    return {'id': mid, 'name': name, 'layout': 'LAYOUT_' + mid[4:], 'music': music,
            'region_map_section': 'MAPSEC_DR_TEMPLAR_HQ', 'requires_flash': False, 'weather': 'WEATHER_NONE',
            'map_type': 'MAP_TYPE_INDOOR', 'allow_cycling': False, 'allow_escaping': False, 'allow_running': True,
            'show_map_name': False, 'battle_scene': 'MAP_BATTLE_SCENE_NORMAL', 'connections': None,
            'object_events': list(objs), 'warp_events': warps, 'coord_events': [], 'bg_events': list(bgs)}

def W3(x, y, dest, wid): return {'x': x, 'y': y, 'elevation': 3, 'dest_map': dest, 'dest_warp_id': str(wid)}

def write_room(key, img, walk, beh, j, pory):
    name, mid = ROOMS[key]
    H, W = img.shape[0] // 16, img.shape[1] // 16
    r = MB.build(img.astype(np.uint8), None, None, W, H, walk, beh)
    black = [(x, y) for y in range(H) for x in range(W) if img[y * 16:y * 16 + 16, x * 16:x * 16 + 16].max() < 12]
    bk = int(r['grid'][black[0][1], black[0][0]] & 0x3FF) if black else int(r['grid'][0, 0] & 0x3FF)
    low = 'templar_cath_' + key
    cam = ''.join(w.capitalize() for w in low.split('_'))
    MB.write(r, name, 'LAYOUT_' + mid[4:], (low + '_tiles', cam + 'Tiles'), (low, cam), j, border=[bk] * 4,
             after_layout='LAYOUT_TEMPLAR_CITADEL', after_map='TemplarCitadel')
    open(os.path.join(C, 'data/maps', name, 'scripts.pory'), 'w').write(pory)
    Image.fromarray(MB.render(r)).save(os.path.join(SCR, key + '_built.png'))
    print(key, name, W, 'x', H, 'ok')
    return r

def nave_picture():
    import nave_mock_v2 as N
    N.main(os.path.join(SCR, 'nave_base.png'), with_ambrose=False)
    subprocess.run([sys.executable, os.path.join(TQ, 'glass', 'arceus_glass.py'), os.path.join(SCR, 'nave_base.png'),
                    os.path.join(SCR, 'nave_game.png')], check=True, capture_output=True)
    return np.array(Image.open(os.path.join(SCR, 'nave_game.png')).convert('RGB')).astype(int)

def gba_legal(img, keep=(), n=60):
    """Make a picture fit the GBA's colour rules: every colour in keep stays exactly (the stained-glass Arceus's
    glasses and lead); everything else is reduced to n shared colours (median cut, no dither); then any 8x8 tile
    still over 15 colours has its closest colours merged until it fits."""
    img = img.copy(); H, W = img.shape[:2]
    keep = {tuple(c) for c in keep}
    flat = img.reshape(-1, 3); is_keep = np.array([tuple(p) in keep for p in flat.tolist()])
    rest = flat[~is_keep]
    q = Image.fromarray(rest.reshape(1, -1, 3).astype(np.uint8)).quantize(n, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    pal = np.array(q.getpalette()[:n * 3]).reshape(-1, 3)
    flat[~is_keep] = pal[np.array(q).ravel()]
    img = flat.reshape(H, W, 3)
    for y in range(0, H, 8):
        for x in range(0, W, 8):
            t = img[y:y + 8, x:x + 8]
            while True:
                cols, cnt = np.unique(t.reshape(-1, 3), axis=0, return_counts=True)
                if len(cols) <= 15: break
                d = ((cols[:, None, :] - cols[None, :, :]) ** 2).sum(-1) + np.eye(len(cols)) * 1e9
                i, j = np.unravel_index(d.argmin(), d.shape)
                a_, b_ = (i, j) if cnt[i] >= cnt[j] else (j, i)          # (the rarer takes the commoner)
                if tuple(cols[b_]) in keep and tuple(cols[a_]) not in keep: a_, b_ = b_, a_
                m = (t == cols[b_]).all(-1); t[m] = cols[a_]
    return img

def build_nave():
    img = nave_picture()
    src = open(os.path.join(TQ, 'glass', 'arceus_glass.py')).read()           # (its glasses: kept exact; the
    i = src.index('FAM={'); FAM = eval(src[i + 4:src.index('\n}', i) + 2])     #  script runs on import, so read its table)
    glass = {(12, 13, 18)}
    for fam in FAM.values(): glass |= set(fam)
    import tilequant as TQN
    img, _ = TQN.quantise(img, n=13, snap=glass)                # (GBA-legal by construction; the glass kept exact)
    Image.fromarray(img.astype(np.uint8)).save(os.path.join(SCR, 'nave_legal.png'))
    G = NG.GRID; H, W = len(G), len(G[0])
    walk = {(x, y) for y in range(H) for x in range(W) if G[y][x] in '.DE'}
    doors = {v: k for k, v in NG.DOORS.items()}
    beh = lambda x, y: MB_SOUTH_ARROW_WARP if G[y][x] == 'E' else MB_DOOR if G[y][x] == 'D' else MB_NORMAL
    warps = [W3(x, y, 'MAP_TEMPLAR_CITADEL', 0) for (x, y) in NAVE_EXITS]
    warps += [W3(*NG.DOORS[k], ROOMS[k][1], 0) for k in OFFICES]
    gx, gy = NG.SANCTUM_GRILLE
    bgs = [{'type': 'sign', 'x': gx, 'y': gy, 'elevation': 3, 'player_facing_dir': 'BG_EVENT_PLAYER_FACING_NORTH',
            'script': 'TemplarCathedral_EventScript_SanctumGrille'}]
    pory = '''mapscripts TemplarCathedral_MapScripts {}

// The gold grille over the stair up to the Sanctum (sealed until Ambrose is beaten; the Sanctum is built, unreached).
script TemplarCathedral_EventScript_SanctumGrille {
    msgbox(format("A gilded grille bars a narrow stair leading up.\\pIt is locked."), MSGBOX_SIGN)
    end
}
'''
    return write_room('nave', img, walk, beh, mapj('nave', warps, bgs=bgs), pory)

def main(which):
    if 'nave' in which: build_nave()

if __name__ == '__main__':
    main(sys.argv[1:] or ['nave'])
