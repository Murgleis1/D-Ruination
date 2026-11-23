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

# ------------------------------------------------------------------ the offices
# room: (mock module, wall rows, the mat's columns on the black bottom row, extra doors {cell: (dest map, warp id)})
OFFICE_SPEC = {
    'study':      ('study_mock', 3, (6, 7), {}),
    'bishops':    ('hall_mock', 3, (8, 9), {(2, 2): ('MAP_TEMPLAR_CATHEDRAL_DORMITORY', 0)}),
    'dorm':       ('dorm_mock', 3, (6, 7), {}),
    'registry':   ('registry_mock', 4, (9, 10), {}),
    'kitchen':    ('kitchen_mock', 3, (8, 9), {}),
    'storehouse': ('store_mock', 3, (7, 8), {}),
}
COVER = 48                               # (a piece covering this many pixels of a cell makes it solid)

def bird_sprites():
    """The registry's birds (they become objects): {key: array} as registry_mock draws them."""
    import registry_mock as R
    from PIL import Image as I_
    rl = R.sprite(os.path.join(R.GFX, 'rufflet', 'overworld.png'), 4)
    return {'braviary': np.array(I_.open(os.path.join(TQ, 'yard', 'braviary_down.png')).convert('RGBA')).astype(int),
            'braviary_l': np.array(I_.open(os.path.join(TQ, 'yard', 'braviary_left.png')).convert('RGBA')).astype(int),
            'rufflet': R.sprite(os.path.join(R.GFX, 'rufflet', 'overworld.png'), 0), 'rufflet_l': rl, 'rufflet_r': rl[:, ::-1].copy()}

def capture(key):
    """Run a room's mock, recording every piece it places (and keeping the birds out of the picture)."""
    import importlib, study_mock as SM
    modname = OFFICE_SPEC[key][0]; mod = importlib.import_module(modname)
    rec, birds = [], []
    sprites = bird_sprites() if key == 'registry' else {}
    o_paste = SM.paste
    def paste(img, p, tx, ty, dy=0):
        rec.append((p, tx * 16, ty * 16 + dy)); o_paste(img, p, tx, ty, dy)
    SM.paste = paste
    o_put = getattr(mod, 'put', None)
    if o_put:
        def put(img, p, x, y):
            for k, sp in sprites.items():
                if p.shape == sp.shape and np.array_equal(p, sp): birds.append((k, x, y)); return
            rec.append((p, x, y)); o_put(img, p, x, y)
        mod.put = put
    try:
        out = os.path.join(SCR, key + '_mock.png'); mod.main(out)
    finally:
        SM.paste = o_paste
        if o_put: mod.put = o_put
    # which recorded pieces are walkable: compare to the module's own pieces by identity of content
    P = None
    return np.array(Image.open(out).convert('RGB')).astype(int), rec, birds

def office(key):
    modname, wall_rows, matcols, extra = OFFICE_SPEC[key]
    img, rec, birds = capture(key)
    H, W = img.shape[0] // 16, img.shape[1] // 16
    # the mat: off the black bottom row onto the last floor row; the black row dropped
    strip = img[(H - 1) * 16:H * 16].copy(); m = strip.any(-1)
    ys, xs = np.nonzero(m); img[(H - 2) * 16 + ys, xs] = strip[ys, xs]
    img = img[:(H - 1) * 16]; H -= 1
    solid = np.zeros((H, W), bool); solid[:wall_rows] = True; solid[:, 0] = True; solid[:, W - 1] = True
    import study_mock as SM
    walk_arrays = []
    if key == 'registry':                                         # (the loose straw piles are walked over)
        import registry_mock as R
        walk_arrays.append(R.pieces()[0]['strawsmall'])
    for p, x, y in rec:
        a = p[..., 3] > 0
        if any(p.shape == w.shape and np.array_equal(p, w) for w in walk_arrays): continue
        cov = np.zeros((H + 4, W + 4))
        ys_, xs_ = np.nonzero(a)
        for yy, xx in zip(ys_ + y, xs_ + x):
            if 0 <= yy < H * 16 and 0 <= xx < W * 16: cov[yy // 16, xx // 16] += 1
        solid |= cov[:H, :W] >= COVER
    exits = [(x, H - 1) for x in matcols]
    for c in exits: solid[c[1], c[0]] = False
    for (x, y) in extra: solid[y, x] = False
    walk = {(x, y) for y in range(H) for x in range(W) if not solid[y, x]}
    beh = lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) in exits else MB_DOOR if (x, y) in extra else MB_NORMAL
    if key == 'dorm':
        warps = [W3(x, y, ROOMS['bishops'][1], 2) for (x, y) in exits]          # (back to the hall's door: its warp 2)
    else:
        warps = [W3(x, y, 'MAP_TEMPLAR_CATHEDRAL', NAVE_DOOR_WARP[key]) for (x, y) in exits]
    warps += [W3(x, y, d, wid) for (x, y), (d, wid) in extra.items()]
    objs = []
    for k, x, y in birds:
        cx, cy = (x + 8) // 16, (y + 31) // 16
        sp = 'BRAVIARY' if k.startswith('braviary') else 'RUFFLET'
        mv = ('MOVEMENT_TYPE_FACE_LEFT' if k.endswith('_l') else 'MOVEMENT_TYPE_FACE_RIGHT' if k.endswith('_r') else 'MOVEMENT_TYPE_FACE_DOWN') \
            if sp == 'BRAVIARY' else 'MOVEMENT_TYPE_WANDER_AROUND'
        objs.append({'graphics_id': 'OBJ_EVENT_GFX_SPECIES(%s)' % sp, 'x': int(cx), 'y': int(cy), 'elevation': 3,
                     'movement_type': mv, 'movement_range_x': 1 if sp == 'RUFFLET' else 0,
                     'movement_range_y': 1 if sp == 'RUFFLET' else 0, 'trainer_type': 'TRAINER_TYPE_NONE',
                     'trainer_sight_or_berry_tree_id': '0', 'script': 'TemplarCathedralRegistry_EventScript_' + sp.capitalize(),
                     'flag': '0'})
    name = ROOMS[key][0]
    pory = 'mapscripts %s_MapScripts {}\n' % name
    if key == 'registry':
        pory += """
script TemplarCathedralRegistry_EventScript_Braviary {
    lock
    faceplayer
    playmoncry(SPECIES_BRAVIARY, CRY_MODE_NORMAL)
    msgbox(format("Braviary: Kreeaw!"))
    waitmoncry
    release
    end
}

script TemplarCathedralRegistry_EventScript_Rufflet {
    lock
    faceplayer
    playmoncry(SPECIES_RUFFLET, CRY_MODE_NORMAL)
    msgbox(format("Rufflet: Ruff!"))
    waitmoncry
    release
    end
}
"""
    np.save(os.path.join(SCR, key + '_solid.npy'), solid)
    import tilequant as TQN
    img, _ = TQN.quantise(img, n=13)
    return write_room(key, img, walk, beh, mapj(key, warps, objs), pory)

def main(which):
    if 'nave' in which: build_nave()
    for k in OFFICE_SPEC:
        if k in which or 'offices' in which: office(k)

if __name__ == '__main__':
    main(sys.argv[1:] or ['nave', 'offices'])
