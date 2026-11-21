"""Build Kimaris's Trial chamber (user 2026-11-21) into the game: MAP_KIMARIS_CHAMBER.

The room is Fantasma's summoning room (its mapsec 1, layout s001_b8b0, 17x15; the user: "actually perfect for the
Kimaris fight"), drawn by tools/fantasma/fsread.py and cut into its own tileset pair by academy/imgtiles.py.
Credit: Fantasma (permission to be asked).

Round the summoning circle stand **four boiling cauldrons** (user 2026-11-21), on the corners of a square about
the circle's centre, each brew and its smoke its own colour: upper left white/grey, upper right bloody crimson,
lower left dark blue, lower right MonoMyth's own green. The cauldron is **the one from Rinri's house in
MonoMyth's Wood Avens**: the hut tileset 0x87310D4's metatiles 0x2A0-0x2B2 (the brew, the smoke and the rim,
all on the top layer, animated) over the hut's cauldron legs (metatiles 0x282-0x284); its iron here a cold grey.
The animation: every 8 frames the hut's tileset callback (0x809B901 -> 0x809B918) copies frame (timer / 8) % 9
of the list at 0x89691C0 (9 frames, 24 tiles) to VRAM tile 0x320. Here each cauldron's top layer has tiles of
its own and InitTilesetAnim_KimarisChamber (src/tileset_anims.c) plays its 9 frames the same way, each cauldron
a few frames out of step with the others. Credit: MonoMyth (the cauldron and its animation).
House Langerin's copper (user 2026-11-21): the banners and the circle's ring in copper, and at the circle's
centre the Wraith badge's symbol (the Trial 1 stamp on the Trainer Card) inlaid in copper, in place of
Fantasma's old sigil.
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
    return langerin(img), (raw >> 10) & 3

# ------------------------------------------------------------------ House Langerin's copper (user 2026-11-21)
COPPER = np.array([(44, 22, 20), (74, 36, 26), (112, 58, 36), (150, 82, 48), (186, 112, 66), (222, 160, 108)], float)
CENTRE, RING_IN = (136, 120), 30                 # the summoning circle's centre (pixels) and its inside radius
def _copper(px, lo, hi):
    l = px.astype(float) @ [0.3, 0.59, 0.11] / 255.0
    t = np.clip((l - l.min()) / max(l.max() - l.min(), 1e-6), 0, 1)
    return COPPER[np.round(lo + (hi - lo) * t).astype(int)].astype(np.uint8)
def langerin(img):
    """Fantasma's gold and violet in House Langerin's copper: the two banners (cloth dark copper, skull and trim
    bright), the circle's ring; the circle's old sigil (a skull over a bowl between crescents) taken out and the
    Wraith badge's symbol (the Trial's stamp on the Trainer Card, tools/art/trainer_card/stamps_src.py) inlaid in
    copper at its centre."""
    out = img.copy(); f = img.astype(int)
    gold = (f[..., 0] > 140) & (f[..., 0] > f[..., 2] + 60) & (f[..., 1] > 70)
    purple = (f[..., 2] > f[..., 1] + 25) & (f[..., 0] > f[..., 1] + 10)
    for x0 in (96, 160):                                                  # the banners (cells 6 and 10, rows 0-1)
        box = (slice(0, 32), slice(x0, x0 + 16))
        sub, g, p = out[box], gold[box], purple[box]
        if p.any(): sub[p] = _copper(img[box][p], 0, 2)
        if g.any(): sub[g] = _copper(img[box][g], 4, 5)
    yy, xx = np.mgrid[0:img.shape[0], 0:img.shape[1]]
    d = np.hypot(xx - CENTRE[0], yy - CENTRE[1])
    inside = d < RING_IN                                                  # the old sigil out: the circle's upper
    low = inside & (yy > CENTRE[1])                                       # half mirrored onto its lower half
    out[low] = out[2 * CENTRE[1] - yy[low], xx[low]]
    ring = (d >= RING_IN) & (d < 40) & gold
    out[ring] = _copper(img[ring], 1, 5)
    import re
    src = open(os.path.join(HERE, '..', 'trainer_card', 'stamps_src.py')).read()     # (read, not imported: it
    rows = re.search(r"'Wraith': \"\"\"(.*?)\"\"\"", src, re.S).group(1).strip('\n').split('\n')  # loads fonts)
    glyph = np.array([[c == '#' for c in row] for row in rows])
    glyph = glyph.repeat(2, 0).repeat(2, 1); gh, gw = glyph.shape
    oy, ox = CENTRE[1] - gh // 2, CENTRE[0] - gw // 2
    from scipy.ndimage import binary_dilation
    rim = binary_dilation(glyph) & ~glyph
    reg = out[oy - 1:oy + gh + 1, ox - 1:ox + gw + 1]
    g2 = np.pad(glyph, 1); r2 = np.pad(rim, 1)
    reg[r2 & ~binary_dilation(np.zeros_like(g2))] = COPPER[0]             # a dark edge round the inlay
    reg[g2] = COPPER[4]
    up = g2 & ~np.vstack([np.zeros((1, g2.shape[1]), bool), g2[:-1]])     # light catching its top edges
    reg[up] = COPPER[5]
    dn = g2 & ~np.vstack([g2[1:], np.zeros((1, g2.shape[1]), bool)])      # and shade under them
    reg[dn] = COPPER[3]
    return out

# ------------------------------------------------------------------ the cauldron (MonoMyth)
# the four brews (user 2026-11-21): their colour, dark to light; None keeps MonoMyth's own swamp green
BREWS = {'white': [(150, 160, 184), (200, 210, 226), (236, 242, 252)],
         'crimson': [(104, 16, 28), (164, 28, 40), (216, 72, 80)],
         'blue': [(24, 36, 104), (40, 68, 164), (96, 132, 216)],
         'green': None}
# MonoMyth's iron is lit green by its brew; here a cold, neutral iron (darkest to lightest)
IRON = {(88, 80, 104): (30, 28, 40), (96, 112, 104): (58, 58, 74), (136, 128, 152): (92, 92, 112),
        (160, 168, 144): (150, 152, 170)}
def brew(rgba, ramp):
    """The brew and its smoke from MonoMyth's swamp green to the given colour (by their own lightness, so the
    small splashes keep their brightness); the iron to a cold grey."""
    out = rgba.copy(); f = rgba[..., :3].astype(int); a = rgba[..., 3] > 0
    q = (f >> 3) << 3
    iron = np.zeros(a.shape, bool)
    for src, dst in IRON.items():
        m = a & (q == src).all(-1); out[..., :3][m] = dst; iron |= m
    if ramp is None: return out
    green = a & ~iron & (f[..., 1] > f[..., 0] + 16) & (f[..., 1] > f[..., 2] + 8)
    g = f[..., 1][green]
    out[..., :3][green] = np.array(ramp)[np.digitize(g, [150, 200])].astype(np.uint8)
    return out

def cauldron(ramp):
    """-> (frames: 9 RGBA 48x48 top layers, legs: RGBA 48x16), the brew in the given colour."""
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
        frames.append(brew(np.concatenate([np.concatenate([layers(ts, m, [2]) for m in r], 1)
                                           for r in ([0x2a0, 0x2a1, 0x2a2], [0x2a8, 0x2a9, 0x2aa], [0x2b0, 0x2b1, 0x2b2])], 0), ramp))
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
    return frames, brew(legs, ramp)

# the four cauldrons (user 2026-11-21): a square round the circle's centre, each brew and its smoke its own colour;
# (name, brew, the bowl's centre as an offset from the circle's centre in pixels, animation phase in frames)
# (name, brew, which corner (x, y signs), animation phase in frames). Each stands out along its diagonal until the
# nearest pixel of its bowl, legs or shadow is GAP pixels outside the ring (user 2026-11-21: all four the same
# distance from the circle; centring the bowls alone left the upper pair's legs 1.4 px from the ring and the
# lower pair's rims 4.2 px, the cauldron not being the same shape top and bottom).
CAULDRONS = [('ul', 'white', (-1, -1), 0), ('ur', 'crimson', (1, -1), 2),
             ('ll', 'blue', (-1, 1), 4), ('lr', 'green', (1, 1), 6)]
RING_OUT, GAP = 37.5, 6
# Kimaris stands on the very top of the Wraith skull at the circle's centre (user 2026-11-21): cell (8, 6), his
# feet on the skull's crown; the player meets him on the skull itself, (8, 7)
KIMARIS = (8, 6)

def main():
    img, coll = room(); H, W = coll.shape
    under = img.copy()
    walk = {(x, y) for y in range(H) for x in range(W) if coll[y, x] == 0}
    walk |= {(x, y) for x in (7, 8, 9) for y in (12, 13, 14)}            # the stair down
    walk |= {(7, 7), (8, 7), (9, 7), (7, 6), (9, 6)}                       # the old sigil's block, the skull now
    walk.discard(KIMARIS)                                                  # (Kimaris stands on its crown)
    pots = []
    for name, brw, (sx, sy), phase in CAULDRONS:
        frames, legs = cauldron(BREWS[brw])
        body = np.concatenate([frames[0][32:], legs], 0)[..., 3] > 0       # the bowl and legs (rows 32-63)
        ys, xs = np.where(body); bcx, bcy = (xs.min() + xs.max() + 1) / 2, 32 + (ys.min() + ys.max() + 1) / 2
        yy, xx = np.mgrid[0:16, 0:48]; sh = ((xx - 24) / 22.0) ** 2 + ((yy - 12) / 5.0) ** 2 < 1
        foot = np.zeros((64, 48), bool); foot[32:] = body; foot[48:] |= sh     # what you see of it on the floor
        FY, FX = np.where(foot)
        def gap(tx, ty):
            px, py = int(CENTRE[0] + sx * tx - bcx + 0.5), int(CENTRE[1] + sy * ty - bcy + 0.5)
            return px, py, np.hypot(FX + px + 0.5 - CENTRE[0], FY + py + 0.5 - CENTRE[1]).min() - RING_OUT
        # whole-pixel offsets, the same out sideways as up or down (within a pixel), the gap closest to GAP
        best = min(((abs(gap(tx, ty)[2] - GAP), abs(tx - ty), tx, ty) for tx in range(30, 70) for ty in range(30, 70)
                    if abs(tx - ty) <= 1))
        px, py, near = gap(best[2], best[3]); near += RING_OUT
        sub = under[py + 48:py + 64, px:px + 48]; sub[sh] = (sub[sh] * 0.55).astype(np.uint8)   # a soft shadow
        a = legs[..., 3] > 0; sub[a] = legs[..., :3][a]                    # the legs (static, under the player)
        x0, x1, y0, y1 = px + xs.min(), px + xs.max() + 1, py + 32 + ys.min(), py + 32 + ys.max() + 1
        for cy in range(y0 // 16, (y1 - 1) // 16 + 1):                   # the bowl and legs are solid where they
            for cx in range(x0 // 16, (x1 - 1) // 16 + 1):                # cover more than a sliver of a cell
                ox = min(x1, cx * 16 + 16) - max(x0, cx * 16); oy = min(y1, cy * 16 + 16) - max(y0, cy * 16)
                if ox >= 5 and oy >= 5: walk.discard((cx, cy))
        pots.append(dict(name=name, brew=brw, frames=frames, px=px, py=py, phase=phase))
        print(name, brw, 'picture at', (px, py), 'bowl centre', (px + bcx, py + bcy), 'gap %.1f' % (near - RING_OUT))
    stairs = (8, 13); seen = {stairs}; q = [stairs]                       # Kimaris must still be reachable
    while q:
        x, y = q.pop()
        for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (x + d[0], y + d[1])
            if n in walk and n not in seen: seen.add(n); q.append(n)
    assert (KIMARIS[0], KIMARIS[1] + 1) in seen, 'the way from the stair to Kimaris is blocked'
    assert (8, 3) in seen, 'the way to the barred door behind Kimaris is blocked'
    cut = sorted(walk - seen); assert not cut, 'floor cut off by the cauldrons: %s' % cut
    beh = lambda x, y: MB_SOUTH_ARROW_WARP if (x, y) == STAIR else MB_NORMAL
    r = IT.build(under, W, H, walk=walk, beh=beh, tries=400)
    # their top layers (brew, rim and smoke): tiles of their own so each frame can be copied over them; two
    # palettes shared two cauldrons apiece
    groups = [('ul', 'ur'), ('ll', 'lr')]
    slots = {}
    for grp in groups:
        cols = set()
        for p in pots:
            if p['name'] in grp:
                for f in p['frames']: cols |= {tuple(int(v) for v in c) for c in ((f[..., :3][f[..., 3] > 0] >> 3) << 3)}
        cols = sorted(cols, key=sum); assert len(cols) <= 15, (grp, len(cols))
        slot = len(r['pals']); r['pals'].append([(0, 0, 0)] + cols + [(0, 0, 0)] * (15 - len(cols)))
        for n in grp: slots[n] = (slot, {c: i + 1 for i, c in enumerate(cols)})
    assert len(r['pals']) <= 13, len(r['pals'])
    def idx(rgba, lut):
        t = np.zeros(rgba.shape[:2], np.uint8)
        for (y, x) in zip(*np.where(rgba[..., 3] > 0)): t[y, x] = lut[tuple(int(v) >> 3 << 3 for v in rgba[y, x, :3])]
        return t
    newmeta = {}                                                           # cell -> its own new metatile
    ad = os.path.join(C, 'data/tilesets/secondary', SEC[0], 'anim'); os.makedirs(ad, exist_ok=True)
    for p in pots:
        slot, lut = slots[p['name']]
        canv = [np.zeros((H * 16, W * 16, 4), np.uint8) for _ in range(9)]
        for k, f in enumerate(p['frames']):
            c = canv[k][p['py']:p['py'] + 48, p['px']:p['px'] + 48]; m = f[..., 3] > 0; c[m] = f[m]
        anyp = np.any([c[..., 3] > 0 for c in canv], 0)
        tiles_here = [(tx, ty) for ty in range(H * 2) for tx in range(W * 2) if anyp[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8].any()]
        p['first'] = len(r['tiles']); p['n'] = len(tiles_here)
        for (tx, ty) in tiles_here:
            cell = (tx // 2, ty // 2)
            if cell not in newmeta:
                g = int(r['grid'][cell[1], cell[0]]); e = list(r['meta'][(g & 0x3FF) - 512])
                r['meta'].append(e); r['attrs'].append(r['attrs'][(g & 0x3FF) - 512])
                newmeta[cell] = len(r['meta']) - 1; r['grid'][cell[1], cell[0]] = (512 + newmeta[cell]) | (g & 0xFC00)
            n = len(r['tiles']); r['tiles'].append(idx(canv[0][ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8], lut))
            r['meta'][newmeta[cell]][8 + (ty % 2) * 2 + tx % 2] = n | slot << 12
        pal_flat = [v for c in r['pals'][slot] for v in c] + [0] * (768 - 48)
        d = os.path.join(ad, 'cauldron_' + p['name']); os.makedirs(d, exist_ok=True)
        for k in range(9):
            col = np.zeros((len(tiles_here) * 8, 8), np.uint8)
            for i, (tx, ty) in enumerate(tiles_here): col[i * 8:i * 8 + 8] = idx(canv[k][ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8], lut)
            im = Image.fromarray(col, 'P'); im.putpalette(pal_flat); im.save(os.path.join(d, '%d.png' % k))
    assert len(r['tiles']) <= 512 and len(r['meta']) <= 512, (len(r['tiles']), len(r['meta']))
    print('palettes', len(r['pals']), 'tiles', len(r['tiles']), 'metatiles', len(r['meta']),
          'cauldron tiles', [(p['name'], p['first'], p['n']) for p in pots])
    old = os.path.join(ad, 'cauldron')
    if os.path.isdir(old):
        import shutil; shutil.rmtree(old)
    json.dump([{k: p[k] for k in ('name', 'first', 'n', 'phase')} for p in pots], open(os.path.join(ad, 'cauldrons.json'), 'w'), indent=1)
    objs = [{'graphics_id': 'OBJ_EVENT_GFX_KIMARIS', 'x': KIMARIS[0], 'y': KIMARIS[1], 'elevation': 3,
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
        '    msgbox("(Kimaris Langerin waits atop the skull.\\nThe Trial is not written yet.)")\n    release\n}\n')
    anim_code()
    lake_warp()
    test_entrance()

def anim_code():
    """The cauldrons' animation in src/tileset_anims.c and its callback on the chamber's secondary tileset: every 8
    frames each cauldron's next frame (its own phase, so they do not boil in step)."""
    pots = json.load(open(os.path.join(C, 'data/tilesets/secondary', SEC[0], 'anim/cauldrons.json')))
    f = os.path.join(C, 'src/tileset_anims.c'); t = open(f).read()
    start, end = '// --- KimarisChamber cauldron (build_kimaris.py) ---\n', '// --- end KimarisChamber ---\n'
    if start in t: t = t[:t.index(start)] + t[t.index(end) + len(end):]
    block = start
    for p in pots:
        nm = p['name'].upper()
        block += ''.join('static const u16 sTilesetAnims_KimarisChamber_%s_Frame%d[] = INCBIN_U16("data/tilesets/secondary/kimaris_chamber/anim/cauldron_%s/%d.4bpp");\n'
                         % (nm, k, p['name'], k) for k in range(9))
        block += 'static const u16 *const sTilesetAnims_KimarisChamber_%s[] = {\n' % nm + \
                 ''.join('    sTilesetAnims_KimarisChamber_%s_Frame%d,\n' % (nm, k) for k in range(9)) + '};\n'
    block += '\nstatic void TilesetAnim_KimarisChamber(u16 timer)\n{\n    if (timer % 8 == 0)\n    {\n'
    for p in pots:
        nm = p['name'].upper()
        block += ('        AppendTilesetAnimToBuffer(sTilesetAnims_KimarisChamber_%s[(timer / 8 + %d) %% 9],\n'
                  '                                  (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(%d)), %d * TILE_SIZE_4BPP);\n') % (nm, p['phase'], p['first'], p['n'])
    block += '    }\n}\n\nvoid InitTilesetAnim_KimarisChamber(void)\n{\n    sSecondaryTilesetAnimCounter = 0;\n' \
             '    sSecondaryTilesetAnimCounterMax = 72;\n    sSecondaryTilesetAnimCallback = TilesetAnim_KimarisChamber;\n}\n' + end
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
