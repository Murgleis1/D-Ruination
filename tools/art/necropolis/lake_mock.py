"""The Trial: the frozen lake of the damned, mock v1 (user 2026-11-21).

The great catacomb chamber of Ghost Grey (map 1.93: the user: "the perfect shape and overall layout") frozen over:
its floor a lake of dark silver ice (Heater Forest's sliding ice; v2, user 2026-11-21: silver and ethereal, not
blue), the shapes of the drowned dead under it, gravestones standing up out of it as the stoppers (Dreamstone
Mysteries', Pisces' Zotpyre and village stones, MonoMyth's Speedwell cross), cut cleanly from their old ground
and sunk into the ice with frost frozen up round them; of the chamber's bronze demon heads only the two by the
arch, and one very weathered head centred on the middle island; a small stone gargoyle on the ice right of the
landing (user 2026-11-21); Ghost Grey's islands of
grave-soil (its normal catacomb ground) where you stop and walk; a bonfire of cold ghost flame on a platform of
grave-soil in each corner, a necromancer by it; the sealed arch at the top (the way to Kimaris) opens when all
four burn. The puzzle itself: lake_puzzle.py (solved and checked there).
Credits: Ghost Grey (JoeyZeed), Pisces, MonoMyth, Dreamstone Mysteries.
Usage: python3 tools/art/necropolis/lake_mock.py [outdir] [--lit]
"""
import os, sys, zlib
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'mirroh'))
import lake_puzzle as P
import floor1_mock as F
import mirroh_mock as mm

GRV = os.path.join(HERE, '..', '..', '..', 'assets', 'necropolis_reference', 'graves')
GG = F.GG
rnd = lambda *k: (zlib.crc32(repr(k).encode()) & 0xFFFF) / 65536.0
SEED, NGRAVES = 108, 34
# graves added by hand to the generated layout (user 2026-11-21, the push-off rule: stopped on the ice you can
# only set off away from something solid; under it the door was out of reach until this one went in)
EXTRA_GRAVES = []    # [(18, 7)] restores the door under lake_puzzle.PUSH_OFF
def layout():
    g, graves, soil = P.generate(SEED, n_graves=NGRAVES)
    for (x, y) in EXTRA_GRAVES: g[y, x] = P.BLOCK
    return g, graves + EXTRA_GRAVES, soil

# ------------------------------------------------------------------ the ice of the lake of the damned
# silver, ethereal (user 2026-11-21: the first, blue ice was too blue): near-neutral greys with the faintest cold
# lilac in the shadows, the streaks catching a pale silver light
ICEPAL = [(10, 10, 16), (26, 27, 36), (48, 50, 62), (84, 88, 102), (138, 143, 158), (212, 216, 228)]
_ICE_T = None
GAME = False      # the in-game build (build_lake.py): the ice repeats every 4x4 cells and keeps to its own palette
def lake_ice(x, y):
    """Dark silver ice, its long streaks catching a pale ghost light (Heater Forest's ice, recoloured)."""
    global _ICE_T
    if _ICE_T is None:
        t = mm.full('gg', 0x34b).astype(float).mean(-1) / 255.0
        lo, hi = t.min(), t.max(); _ICE_T = (t - lo) / max(hi - lo, 1e-6)
    t = 0.2 + 0.3 * _ICE_T ** 1.4                                    # the streaks, softened
    yy, xx = np.mgrid[0:16, 0:16]
    gx, gy = (x * 16 + xx) / 56.0, (y * 16 + yy) / 56.0                  # a slow pale sheen drifting over it
    per = None
    if GAME: gx, gy, per = ((x % 4) * 16 + xx) / 32.0, ((y % 4) * 16 + yy) / 32.0, 2   # (repeating: 4x4 cells)
    sheen = np.zeros((16, 16))
    for (sx, sy, w) in (((1, 1, 0.6), (2.3, 1.7, 0.4)) if not GAME else ((1, 1, 0.7), (2, 2, 0.3))):
        X, Y = gx * sx, gy * sy; x0, y0 = np.floor(X).astype(int), np.floor(Y).astype(int); fx, fy = X - x0, Y - y0
        fx, fy = fx * fx * (3 - 2 * fx), fy * fy * (3 - 2 * fy)
        L = per * sx if per else None
        v = lambda i, j: np.vectorize(lambda p, q: rnd('sh', sx, p % L if L else p, q % L if L else q))(x0 + i, y0 + j)
        sheen += w * (v(0, 0) * (1 - fx) * (1 - fy) + v(1, 0) * fx * (1 - fy) + v(0, 1) * (1 - fx) * fy + v(1, 1) * fx * fy)
    t = t + 0.32 * np.clip(sheen - 0.45, 0, 1)
    cols = np.array(ICEPAL, float); q = np.clip(t, 0, 0.999) * (len(cols) - 1)
    if GAME: q = np.round(q * 2) / 2                                    # (whole and half steps: 11 colours)
    i = np.floor(q).astype(int)
    return (cols[i] + (cols[np.minimum(i + 1, len(cols) - 1)] - cols[i]) * (q - i)[..., None]).astype(np.uint8)

SKULL = ["..###..", ".#####.", "#.###.#", "#######", ".##.##.", "..###..", "..#.#.."]
HAND = ["#.#.#..", "#.#.#.#", "#######", ".#####.", "..###..", "..###..", "..###.."]
def drowned(img, x, y):
    """Something under the ice: a skull or a reaching hand, dim, as if a foot down."""
    if GAME: x, y = x % 4, y % 4                                        # (a few kinds, repeating)
    glyph = SKULL if rnd('g', x, y) < 0.55 else HAND
    ox, oy = 3 + int(rnd('ox', x, y) * 5), 3 + int(rnd('oy', x, y) * 5)
    for j, row in enumerate(glyph):
        for i, ch in enumerate(row):
            if ch == '#' and 0 <= oy + j < 16 and 0 <= ox + i < 16:      # pale, faint, under the ice
                p = img[oy + j, ox + i].astype(float); img[oy + j, ox + i] = p * 0.6 + np.array([150, 156, 172]) * 0.4
                if GAME: img[oy + j, ox + i] = (84, 88, 102)
    return img

# ------------------------------------------------------------------ the gravestones
def key(tile, ground):
    return ~(tile == ground).all(-1)
def _l(name): return np.load(os.path.join(GRV, name + '.npy'))

def clean(img, ground, drop=None, tol=0):
    """A grave cut cleanly out of its old tile (user 2026-11-21: no leftover bits of the old ground): everything
    joined to the tile's border through the ground's own colours is background; holes inside the stone are kept
    (filled), crumbs dropped. drop(img, mask) may take off more (a cast shadow)."""
    from scipy.ndimage import label, binary_fill_holes
    gc = np.unique(ground.reshape(-1, 3), axis=0).astype(int)
    dist = np.abs(img.astype(int)[:, :, None, :] - gc[None, None]).sum(-1).min(-1)
    bgc = dist <= tol
    bg = np.zeros((16, 16), bool); st = [(y, x) for y in range(16) for x in (0, 15)] + [(y, x) for x in range(16) for y in (0, 15)]
    while st:
        y, x = st.pop()
        if 0 <= y < 16 and 0 <= x < 16 and not bg[y, x] and bgc[y, x]:
            bg[y, x] = True; st += [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
    a = binary_fill_holes(~bg)
    # stray ground pixels left in its corners: in each corner, colours the stone's own middle never uses go
    core = {tuple(c) for c in img[4:12, 4:12].reshape(-1, 3)}
    for (cy, cx) in ((0, 0), (0, 15), (15, 0), (15, 15)):
        for y in range(16):
            for x in range(16):
                if max(abs(y - cy), abs(x - cx)) <= 3 and tuple(img[y, x]) not in core: a[y, x] = False
    if drop is not None: a &= ~drop(img, a)
    lab, n = label(a); sizes = np.bincount(lab.ravel())
    keep = [i for i in range(1, n + 1) if sizes[i] >= 10]
    return np.isin(lab, keep)

def _shadow(img, a):
    """MonoMyth's cross: its grey cast shadow at the foot."""
    f = img.astype(int); sat = f.max(-1) - f.min(-1)
    m = np.zeros((16, 16), bool); m[11:] = sat[11:] < 24
    return m

def grave_types():
    """Gravestones for the lake: Dreamstone Mysteries' arched stone, Pisces' copper and slate stones (Zotpyre),
    Pisces' frosted stone, MonoMyth's Speedwell cross. (MonoMyth's cross in rubble and Ghost Grey's marker
    were dropped: they did not cut cleanly out of their ground.)"""
    dm = mm.RL.TS('LAYOUT_MIRROH_BASE_CAMP_GRAVEYARD')
    dmg, dms = np.asarray(dm.metatile(0x3A5), np.uint8), np.asarray(dm.metatile(0x1E3), np.uint8)
    t = {'dm_arched': (dmg, dms), 'ps_copper': (_l('ps_324'), _l('ps_1')), 'ps_slate': (_l('ps_325'), _l('ps_1')),
         'pv_frost': (_l('pv_2d2'), _l('pv_239')), 'mm_cross': (_l('mm_39'), _l('mm_209'))}
    return {k: (img, clean(img, gr, _shadow if k == 'mm_cross' else None, tol=40 if k.startswith('ps') else 0))
            for k, (img, gr) in t.items()}

def chill(img):
    """A grave in the lake: its own colours drawn toward cold silver, dimmer."""
    f = img.astype(float); g = f.mean(-1, keepdims=True)
    return np.clip((f * 0.62 + g * 0.38) * 0.84 + np.array([10, 10, 16]), 0, 255).astype(np.uint8)

SINK = 2
def grave_on_ice(base, kind, x, y):
    """A gravestone standing up out of the ice (user 2026-11-21: natural, coming out of the ice): its foot sunk
    SINK pixels under the surface, a ragged collar of frost frozen up round it, hoarfrost on its top edges, and
    its dark shape faintly mirrored in the ice below."""
    img, a = kind
    rows = np.where(a.any(1))[0]; top, bot = rows[0], rows[-1]
    # stand it so its sunk foot sits two pixels above the cell's bottom (room for the collar and the mirror)
    shift = (13 - (bot - SINK)) if bot - SINK < 13 else 0
    shift = max(min(shift, 15 - bot), -top)
    a2 = np.roll(a, shift, 0); im2 = np.roll(chill(img), shift, 0)
    foot = bot + shift - SINK; a2[foot + 1:] = False
    out = base.copy()
    cols = np.where(a2.any(0))[0]; c0, c1 = cols[0], cols[-1]
    for yy in range(foot + 1, 16):                               # its mirror, dim, in the ice under it
        k = yy - foot
        for xx in range(c0, c1 + 1):
            if a2[foot - k + 1 if foot - k + 1 >= 0 else 0, xx] and rnd('mr', x, y, xx, yy) < 0.75:
                out[yy, xx] = (out[yy, xx] * (0.55 + 0.1 * k)).astype(np.uint8)
    out[a2] = im2[a2]
    up = a2 & ~np.vstack([np.zeros((1, 16), bool), a2[:-1]])     # hoarfrost on the edges open to the air above
    for (yy, xx) in zip(*np.where(up)):
        if rnd('hf', x, y, xx) < 0.55: out[yy, xx] = (out[yy, xx] * 0.4 + np.array([224, 228, 238]) * 0.6).astype(np.uint8)
    for xx in range(max(c0 - 1, 0), min(c1 + 2, 16)):             # the collar of frost round its foot
        edge = xx in (c0 - 1, c1 + 1)
        h = 1 + int(rnd('ch', x, y, xx) * (2 if edge else 3))
        for yy in range(foot - h + 1, foot + 2):
            if 0 <= yy < 16:
                lit = yy <= foot - h + 2
                out[yy, xx] = (206, 212, 224) if lit else (150, 156, 172)
        if foot + 2 < 16 and rnd('cs', x, y, xx) < 0.5: out[foot + 2, xx] = (96, 100, 116)
    return out

# ------------------------------------------------------------------ the statues
def weathered_bronze(img, a, seed):
    """A demon head of old bronze, very weathered (user 2026-11-21): tarnished dull and dark, green-grey
    verdigris eaten into it in patches, streaks run down from it, cracks, chips knocked out of its edges and
    corners. img is Ghost Grey's own grey (four levels), so the carving stays readable under the wear."""
    from scipy.ndimage import binary_erosion
    l = img.astype(float).mean(-1); hh, ww = l.shape
    lv = np.unique(l); idx = np.searchsorted(lv, l)
    ramp = np.array([(28, 22, 24), (74, 60, 54), (122, 102, 82), (170, 150, 120)], float)
    ramp = ramp[np.round(np.linspace(0, 3, len(lv))).astype(int)]
    out = ramp[idx] * (1 + 0.16 * np.array([[rnd(seed, 'f', xx // 2, yy // 2) - 0.5 for xx in range(ww)] for yy in range(hh)]))[..., None]
    vg = np.array([[rnd(seed, 'v', xx // 5, yy // 5) * 0.6 + rnd(seed, 'v2', xx // 2, yy // 2) * 0.4
                    for xx in range(ww)] for yy in range(hh)])
    green = (vg > 0.58) & (idx > 0)
    out[green] = out[green] * 0.55 + np.array([84, 116, 104]) * 0.45
    for k in range(6):                                            # verdigris streaks running down
        xx = int(rnd(seed, 'sx', k) * ww); y0 = int(rnd(seed, 'sy', k) * hh * 0.5)
        for yy in range(y0, min(y0 + 5 + int(rnd(seed, 'sl', k) * 9), hh)):
            if idx[yy, xx] > 0: out[yy, xx] = out[yy, xx] * 0.55 + np.array([80, 110, 100]) * 0.45
    for k in range(5):                                            # cracks
        xx, yy = int(rnd(seed, 'cx', k) * ww), int(rnd(seed, 'cy', k) * hh)
        for j in range(5 + int(rnd(seed, 'cl', k) * 6)):
            if 0 <= xx < ww and 0 <= yy < hh: out[yy, xx] = (20, 16, 18)
            xx += 1 if rnd(seed, 'dx', k, j) < 0.5 else -1; yy += 1
    a = a.copy(); yy, xx = np.mgrid[0:hh, 0:ww]
    for (cy, cx, r) in ((0, 0, 3.2), (0, ww - 1, 2.2), (hh - 1, ww - 1, 2.6), (2, int(ww * 0.7), 2.0)):
        a &= ~(((yy - cy) ** 2 + (xx - cx) ** 2) < r * r)          # corners and a bite from the brow knocked off
    edge = a & ~binary_erosion(a, np.ones((3, 3), bool))
    ey, ex = np.where(edge)
    for i in range(len(ey)):                                      # small chips all round its rim
        if rnd(seed, 'chip', int(ey[i]), int(ex[i])) < 0.14: a[ey[i], ex[i]] = False
    edge = a & ~binary_erosion(a, np.ones((3, 3), bool))
    out[edge] = out[edge] * 0.5 + np.array([20, 16, 18]) * 0.5
    return np.clip(out, 0, 255).astype(np.uint8), a

def demon_head():
    """Ghost Grey's bronze demon head (the middle island's 2x2), cut from its floor: (rgb, alpha) 32x32."""
    c = GG['cells']; img = np.zeros((32, 32, 3), np.uint8); a = np.zeros((32, 32), bool)
    for dy in (0, 1):
        for dx in (0, 1):
            m = int(c[19 + dy, 19 + dx]); t = GG['full'][m]; k = key(t, GG['full'][0x3eb])
            img[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16] = t; a[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16] = True
    return img, a

# a small crouching gargoyle on a low plinth, 16 x 22 (drawn for the lake; generic, original): left half, mirrored
_G = ["o.......", "lo....o.", "mlo...lo", "mmlo.ooo", "mddloohh", "mdddoeml", "mdddomdd", "omddoodo",
      ".omdooml", "..omdmll", "..odmdml", "...odmml", "..omldmd", "..omddmo", ".omlo.od", ".oooo.oo",
      ".ooooooo", ".ohhhhhh", ".ollllll", ".omddddd", ".odmmmmm", ".ooooooo"]
_GC = {'o': (26, 24, 32), 'd': (58, 56, 68), 'm': (96, 94, 108), 'l': (140, 138, 152), 'h': (184, 182, 194),
       'e': (150, 230, 236)}
def small_gargoyle():
    rgb = np.zeros((22, 16, 3), np.uint8); a = np.zeros((22, 16), bool)
    for y, row in enumerate(_G):
        full = row + row[::-1]
        for x, ch in enumerate(full):
            if ch in _GC:
                a[y, x] = True; c = np.array(_GC[ch], float)
                if x >= 8 and ch not in 'oe': c = c * 0.86          # the far side a shade darker
                rgb[y, x] = c
    return rgb, a

def weathered_stone_small(rgb, a):
    """The gargoyle's stone, weathered a little: mottle and a few pits."""
    f = rgb.astype(float)
    for (y, x) in zip(*np.where(a)):
        if tuple(rgb[y, x]) in (_GC['o'], _GC['e']): continue
        f[y, x] *= 0.9 + 0.2 * rnd('gm', x // 2, y // 2)
        if rnd('gp', x, y) < 0.08: f[y, x] = (52, 58, 54)
    return np.clip(f, 0, 255).astype(np.uint8), a

def overlay(img, fig, a, px, py):
    h, w = a.shape; sub = img[py:py + h, px:px + w]; sub[a] = fig[a]

# ------------------------------------------------------------------ the bonfires
RING = os.path.join(HERE, '..', '..', '..', 'assets', 'monomyth_reference', 'pieces', 'tarragon_fire_ring.png')
FLAME = ["....#....", "...##....", "...###...", "..####...", "..#####..", ".######..", ".#######.",
         "########.", "#########", ".#######.", "..#####.."]
TORCH = os.path.join(HERE, '..', '..', '..', 'codebase', 'data', 'tilesets', 'secondary', 'battle_pyramid', 'anim', 'torch')
GHOSTFIRE = [(36, 96, 140), (70, 160, 196), (140, 226, 240), (232, 252, 255)]
def flame_frames():
    """The bonfires' cold ghost flame: the base game's Battle Pyramid torch flame (its three frames), lifted out of
    its brazier and recoloured from orange to a spectral cyan-white by lightness. -> three RGBA 16x32 pictures:
    rows 0-15 rise over the cell above the fire, rows 16-31 burn in the fire's own cell."""
    from scipy.ndimage import binary_fill_holes
    out = []
    for k in range(3):
        p = Image.open(os.path.join(TORCH, '%d.png' % k)); idx = np.array(p)
        im = np.array(p.convert('RGB')).astype(int)
        r, b = im[..., 0], im[..., 2]
        warm = (r > b + 60) & (r > 150)
        rows = np.arange(32)[:, None] < 16
        # the flame: its red outline (index 14) and all it encloses, and its tip above the brazier; the
        # brazier's grille (the same orange, outside the outline) left out
        from scipy.ndimage import binary_closing
        shape = binary_fill_holes(binary_closing((idx == 14) | (warm & rows), np.ones((3, 3), bool)) | (idx == 14) | (warm & rows))
        im[shape & ~warm] = (255, 156, 0)                                  # (the brazier's rim crossing it: flame)
        warm = shape
        lum = (im @ [0.3, 0.59, 0.11])
        rgba = np.zeros((32, 16, 4), np.uint8)
        lv = np.digitize(lum, [110, 165, 215])
        col = np.array(GHOSTFIRE, np.uint8)[lv]
        sh = np.zeros_like(warm); sh[1:] = warm[:-1]                        # (down a pixel: its foot in the logs)
        cs = np.zeros_like(col); cs[1:] = col[:-1]
        rgba[sh, :3] = cs[sh]; rgba[sh, 3] = 255
        out.append(rgba)
    return out

LOGS = ["oo....oo", "oLo..oLo", ".oL**Lo.", "..oLLo..", ".oL**Lo.", "oLo..oLo", "oo....oo"]
LOG_COL = {'o': (34, 28, 32), 'L': (88, 70, 62), '*': (176, 182, 196)}   # charcoal, the burnt wood, frost-grey ash
def bonfire(base, lit):
    """A bonfire: MonoMyth's (Tarragon's) stone fire ring, cold-tinted, with charred logs crossed in it and frost on
    their ash (user 2026-11-21: real bonfire art, unlit and lit). Lit, the ghost flame burns up out of the logs."""
    out = base.copy()
    ring = np.array(Image.open(RING).convert('RGBA'))
    rh, rw = ring.shape[:2]; oy, ox = 16 - rh, (16 - rw) // 2
    for j in range(rh):
        for i in range(rw):
            if ring[j, i, 3] > 0 and 0 <= oy + j < 16 and 0 <= ox + i < 16:
                l = float(ring[j, i, :3] @ [0.3, 0.59, 0.11]) * 0.82          # (its stones' own light, frost-cold)
                out[oy + j, ox + i] = np.clip([l * 0.94, l * 0.96, l * 1.08 + 6], 0, 255).astype(np.uint8)
    for j, row in enumerate(LOGS):
        for i, ch in enumerate(row):
            if ch != '.': out[oy + 4 + j, ox + 4 + i] = LOG_COL[ch]
    if lit:                                                              # a cold ghost flame (its foot; its tip
        f = flame_frames()[0][16:]; m = f[..., 3] > 0; out[m] = f[..., :3][m]   # is drawn on the cell above)
    return out

VOIDS = (0x281, 0x3fe)
MARGIN = 2              # rows below and columns right of the old chamber, so its south and east shores can be drawn
def bank(lake, x, y):
    """The lake's shore where the ice meets the dark (user 2026-11-21: slides stopped against nothing to be seen):
    a bank of frozen rock, a ragged lip of frost along each side the ice touches, the rock sinking into the dark
    away from the lake. lake(x, y) -> True for the lake's cells."""
    rock = (F.tone(0x3eb, GG['full'][0x3eb]).astype(float) * 0.5 + np.array([4, 4, 10])).clip(0, 255)
    yy, xx = np.mgrid[0:16, 0:16]
    sides = {(0, -1): 15 - yy, (0, 1): yy, (-1, 0): 15 - xx, (1, 0): xx}   # 15 - (distance to that side)
    near = np.full((16, 16), 99.0)
    for (dx, dy), dd in sides.items():
        if lake(x + dx, y + dy): near = np.minimum(near, (15 - dd).astype(float))
    for dx in (-1, 1):                                                      # corners the ice only touches diagonally
        for dy in (-1, 1):
            if lake(x + dx, y + dy) and not lake(x + dx, y) and not lake(x, y + dy):
                cx, cy = (15 if dx > 0 else 0), (15 if dy > 0 else 0)
                near = np.minimum(near, np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2))
    fade = np.clip(1 - (near - 3) / 12.0, 0.0, 1)[..., None]
    if GAME: fade = np.round(fade * 3) / 3                                  # (a few steps: keeps the colours down)
    out = rock * fade + np.array(F.VOID, float) * (1 - fade)
    if GAME: out = np.round(out / 8) * 8
    for (dx, dy), dd in sides.items():
        if not lake(x + dx, y + dy): continue
        d = 15 - dd                                                         # 0 at the edge the ice touches
        along = xx if dy else yy
        depth = np.vectorize(lambda a: 1 + int(rnd('lip', x if not GAME else x % 4, y if not GAME else y % 4, dx, dy, int(a)) * 3))(along)
        out[d < depth] = (150, 156, 172); out[d == 0] = (206, 212, 224)
        out[(d == depth)] = (26, 26, 36)
    return out.clip(0, 255).astype(np.uint8)

def compose(lit=False):
    g, graves, soil = layout()
    c = GG['cells']; H, W = c.shape
    types = grave_types(); names = sorted(types)
    img = np.zeros(((H + MARGIN) * 16, (W + MARGIN) * 16, 3), np.uint8); img[:] = F.VOID
    isl_soil, isl_block = P.islands()
    isl = set(isl_soil) | set(isl_block)
    demon = {(x + dx, y + dy) for (x, y) in P.DEMONS for dx in (0, 1) for dy in (0, 1)}
    centre = set(P.CENTRE_OLD) | set(P.CENTRE_STATUE)
    fires = {v['fire']: k for k, v in P.CORNERS.items()}; trainers = {v['trainer'] for v in P.CORNERS.values()}
    plats = {cc for v in P.CORNERS.values() for cc in v['plat']}
    for y in range(H):
        for x in range(W):
            m = int(c[y, x]); t = None
            ice = lake_ice(x, y)
            if (x, y) in demon:
                d = GG['full'][m]; a = key(d, GG['full'][0x3eb]); t = ice.copy(); t[a] = F.BRONZE(d)[a]
            elif (x, y) in centre:                                   # plain grave-soil under the one statue
                t = F.tone(0x3eb, GG['full'][0x3eb])
            elif (x, y) in isl:                                      # an island of grave-soil, its edges in ice
                t = F.tone(m, GG['full'][m]); void = (t == np.array(F.VOID)).all(-1); t[void] = ice[void]
            elif (x, y) in plats or (x, y) in P.DOOR_LANDING or (x, y) in set(P.MAT) or (x, y) in soil:
                t = F.tone(0x3eb, GG['full'][0x3eb]) if (x, y) not in set(P.MAT) else F.tone(m, GG['full'][m])
                if (x, y) in fires: t = bonfire(t, lit)
            elif g[y, x] == P.ICE or (x, y) in graves or (x, y) == P.GARGOYLE:
                t = ice
                if (x, y) in graves:
                    t = grave_on_ice(ice, types[names[int(rnd('k', x, y) * len(names))]], x, y)
                elif rnd('dr', x, y) < 0.1: t = drowned(ice, x, y)
            else:
                t = F.tone(m, GG['full'][m])
            img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = t
    d, da = demon_head(); d, da = weathered_bronze(d, da, 'centre')     # one very weathered head, centred on the
    cols = np.where(da.any(0))[0]; rows = np.where(da.any(1))[0]          # middle island to the pixel (x 18-24)
    fw = cols[-1] - cols[0] + 1; px = (18 * 16 + 25 * 16) // 2 - fw // 2 - cols[0]
    py = (19 * 16 + 21 * 16) // 2 - (rows[0] + rows[-1] + 1) // 2
    overlay(img, d, da, px, py)
    gr, ga = small_gargoyle(); gr, ga2 = weathered_stone_small(gr, ga)
    gx, gy = P.GARGOYLE; overlay(img, gr, ga2, gx * 16, gy * 16 + 16 - 22)
    for xx in range(gx * 16, gx * 16 + 16):                             # frost frozen up round its plinth
        h = 1 + int(rnd('gc', xx) * 2)
        for yy in range(gy * 16 + 16 - h, gy * 16 + 16): img[yy, xx] = (206, 212, 224) if yy == gy * 16 + 16 - h else (150, 156, 172)
    # the shore: every dark cell (or cell past the old chamber's edge) beside the lake is frozen bank; under the
    # landing the stair carries on south (the way in)
    lakecell = lambda x, y: 0 <= x < W and 0 <= y < H and (g[y, x] != P.BLOCK or (x, y) in graves or (x, y) == P.GARGOYLE
                                                         or (x, y) in isl or (x, y) in centre or (x, y) in demon)
    for y in range(H + MARGIN):
        for x in range(W + MARGIN):
            inside = 0 <= x < W and 0 <= y < H
            if inside and not (int(c[y, x]) in VOIDS and g[y, x] == P.BLOCK and (x, y) not in isl): continue
            if lakecell(x, y): continue
            if not any(lakecell(x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1)): continue
            if y >= H and P.MAT[0][0] <= x <= P.MAT[-1][0]:
                t = F.tone(int(c[H - 1, x]), GG['full'][int(c[H - 1, x])])
            else: t = bank(lakecell, x, y)
            img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = t
    if lit:                                                          # the flames' tips over the cells above
        tip = flame_frames()[0][:16]; m = tip[..., 3] > 0
        for (fx, fy) in fires: img[(fy - 1) * 16:fy * 16, fx * 16:fx * 16 + 16][m] = tip[..., :3][m]
    if lit:                                                          # each bonfire's cold light on the ice round it
        yy, xx = np.mgrid[0:img.shape[0], 0:img.shape[1]]
        f = img.astype(float)
        for (fx, fy) in fires:
            cx, cy = fx * 16 + 8, fy * 16 + 6
            r = np.sqrt((xx - cx) ** 2 + ((yy - cy) * 1.2) ** 2)
            k = np.clip(1 - r / 72.0, 0, 1) ** 2 * 0.55
            f = f * (1 - k[..., None]) + np.array([110, 230, 240]) * k[..., None] * 0.9 + f * k[..., None] * 0.35
        img = np.clip(f, 0, 255).astype(np.uint8)
    return img, g

def main(outdir, lit):
    os.makedirs(outdir, exist_ok=True)
    img, g = compose(lit)
    tag = '_lit' if lit else ''
    Image.fromarray(img).save(os.path.join(outdir, 'necropolis_lake%s.png' % tag))
    big = Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), 0); d = ImageDraw.Draw(big)
    for k, v in P.CORNERS.items():
        x, y = v['trainer']; cx, cy = x * 32 + 16, y * 32 + 16
        d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], outline=(255, 220, 90), width=3)
    x, y = P.START; d.text((x * 32 + 36, y * 32 + 8), 'in', fill=(255, 220, 90))
    d.text((21 * 32 + 40, 3 * 32 + 8), 'sealed arch (to Kimaris)', fill=(255, 220, 90))
    big.save(os.path.join(outdir, 'necropolis_lake%s_2x.png' % tag))

if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    main(a[0] if a else '/home/claude/scratch/necro', '--lit' in sys.argv)
