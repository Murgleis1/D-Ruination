"""The Trial: the frozen lake of the damned, mock v1 (user 2026-11-21).

The great catacomb chamber of Ghost Grey (map 1.93: the user: "the perfect shape and overall layout") frozen over:
its floor a lake of dark ice (Heater Forest's sliding ice, recoloured cold and deep), the shapes of the drowned
dead under it, gravestones of every kind standing up out of it as the stoppers (Ghost Grey's, Dreamstone
Mysteries', Pisces' Zotpyre shrine and village stones, MonoMyth's Speedwell crosses), Ghost Grey's islands of
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

# ------------------------------------------------------------------ the ice of the lake of the damned
ICEPAL = [(6, 10, 22), (14, 26, 46), (24, 46, 72), (44, 80, 108), (92, 148, 176), (190, 230, 244)]
_ICE_T = None
def lake_ice(x, y):
    """Deep black-blue ice, its long streaks catching the ghost light (Heater Forest's ice, darkened)."""
    global _ICE_T
    if _ICE_T is None:
        t = mm.full('gg', 0x34b).astype(float).mean(-1) / 255.0
        lo, hi = t.min(), t.max(); _ICE_T = (t - lo) / max(hi - lo, 1e-6)
    t = 0.12 + 0.5 * _ICE_T ** 1.6
    t = t - 0.06 * (rnd('d', x // 3, y // 3) - 0.5)
    cols = np.array(ICEPAL, float); q = np.clip(t, 0, 0.999) * (len(cols) - 1); i = np.floor(q).astype(int)
    return (cols[i] + (cols[np.minimum(i + 1, len(cols) - 1)] - cols[i]) * (q - i)[..., None]).astype(np.uint8)

SKULL = ["..###..", ".#####.", "#.###.#", "#######", ".##.##.", "..###..", "..#.#.."]
HAND = ["#.#.#..", "#.#.#.#", "#######", ".#####.", "..###..", "..###..", "..###.."]
def drowned(img, x, y):
    """Something under the ice: a skull or a reaching hand, dim, as if a foot down."""
    glyph = SKULL if rnd('g', x, y) < 0.55 else HAND
    ox, oy = 3 + int(rnd('ox', x, y) * 5), 3 + int(rnd('oy', x, y) * 5)
    for j, row in enumerate(glyph):
        for i, ch in enumerate(row):
            if ch == '#' and 0 <= oy + j < 16 and 0 <= ox + i < 16:      # pale, faint, under the ice
                p = img[oy + j, ox + i].astype(float); img[oy + j, ox + i] = p * 0.6 + np.array([110, 160, 180]) * 0.4
    return img

# ------------------------------------------------------------------ the gravestones
def key(tile, ground):
    return ~(tile == ground).all(-1)
def _l(name): return np.load(os.path.join(GRV, name + '.npy'))
def grave_types():
    dm = mm.RL.TS('LAYOUT_MIRROH_BASE_CAMP_GRAVEYARD')
    dmg, dms = np.asarray(dm.metatile(0x3A5), np.uint8), np.asarray(dm.metatile(0x1E3), np.uint8)
    out = {
        'dm_arched': (dmg, key(dmg, dms)),
        'ps_copper': (_l('ps_324'), key(_l('ps_324'), _l('ps_1'))),
        'ps_slate': (_l('ps_325'), key(_l('ps_325'), _l('ps_1'))),
        'pv_frost': (_l('pv_2d2'), key(_l('pv_2d2'), _l('pv_239'))),
        'mm_cross': (_l('mm_39'), key(_l('mm_39'), _l('mm_209'))),
        'mm_cross2': (_l('mm_a6'), key(_l('mm_a6'), _l('mm_209'))),
    }
    g = GG['full'][0x3d7]; r = GG['full'][0x3eb]
    a = key(g, r); a[:3] = False
    out['gg_marker'] = (F.BONE(g), a)
    return out

def chill(img):
    """A grave in the lake: its own colours a shade colder and dimmer."""
    f = img.astype(float); g = f.mean(-1, keepdims=True)
    return np.clip((f * 0.75 + g * 0.25) * 0.86 + np.array([6, 10, 20]), 0, 255).astype(np.uint8)

def grave_on_ice(base, kind, x, y):
    img, a = kind
    out = base.copy(); out[a] = chill(img)[a]
    cols = np.where(a.any(0))[0]; foot = np.where(a.any(1))[0][-1]
    for xx in range(max(cols[0] - 1, 0), min(cols[-1] + 2, 16)):      # the ice frozen up round its foot
        for yy in (foot - 1, foot):
            if 0 <= yy < 16 and (rnd('r', x, y, xx, yy) < 0.7): out[yy, xx] = (196, 228, 244) if yy == foot else (150, 196, 220)
    return out

# ------------------------------------------------------------------ the bonfires
RING = os.path.join(HERE, '..', '..', '..', 'assets', 'monomyth_reference', 'pieces', 'tarragon_fire_ring.png')
FLAME = ["....#....", "...##....", "...###...", "..####...", "..#####..", ".######..", ".#######.",
         "########.", "#########", ".#######.", "..#####.."]
def bonfire(base, lit):
    out = base.copy()
    ring = np.array(Image.open(RING).convert('RGBA'))
    rh, rw = ring.shape[:2]; oy, ox = 16 - rh, (16 - rw) // 2
    for j in range(rh):
        for i in range(rw):
            if ring[j, i, 3] > 0 and 0 <= oy + j < 16 and 0 <= ox + i < 16:
                out[oy + j, ox + i] = mm.gloom(ring[j:j + 1, i:i + 1, :3], 0.3)[0, 0]
    if lit:                                                              # a cold ghost flame
        for j, row in enumerate(FLAME):
            for i, ch in enumerate(row):
                y, x = j + 1, i + 3
                if ch == '#' and 0 <= y < 16 and 0 <= x < 16:
                    core = abs(i - 4) <= 1 and j > 4
                    out[y, x] = (236, 252, 255) if core else (120, 230, 240) if abs(i - 4) <= 2 else (60, 170, 200)
    return out

def compose(lit=False):
    g, graves, soil = P.generate(SEED, n_graves=NGRAVES)
    c = GG['cells']; H, W = c.shape
    types = grave_types(); names = sorted(types)
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    isl_soil, isl_block = P.islands()
    isl = set(isl_soil) | set(isl_block)
    demon = {(x + dx, y + dy) for (x, y) in P.DEMONS for dx in (0, 1) for dy in (0, 1)}
    fires = {v['fire']: k for k, v in P.CORNERS.items()}; trainers = {v['trainer'] for v in P.CORNERS.values()}
    plats = {cc for v in P.CORNERS.values() for cc in v['plat']}
    for y in range(H):
        for x in range(W):
            m = int(c[y, x]); t = None
            ice = lake_ice(x, y)
            if (x, y) in demon:
                d = GG['full'][m]; a = key(d, GG['full'][0x3eb]); t = ice.copy(); t[a] = F.BRONZE(d)[a]
            elif (x, y) in isl:                                      # an island of grave-soil, its edges in ice
                t = F.tone(m, GG['full'][m]); void = (t == np.array(F.VOID)).all(-1); t[void] = ice[void]
            elif (x, y) in plats or (x, y) in P.DOOR_LANDING or (x, y) in set(P.MAT) or (x, y) in soil:
                t = F.tone(0x3eb, GG['full'][0x3eb]) if (x, y) not in set(P.MAT) else F.tone(m, GG['full'][m])
                if (x, y) in fires: t = bonfire(t, lit)
            elif g[y, x] == P.ICE or (x, y) in graves:
                t = ice
                if (x, y) in graves:
                    t = grave_on_ice(ice, types[names[int(rnd('k', x, y) * len(names))]], x, y)
                elif rnd('dr', x, y) < 0.1: t = drowned(ice, x, y)
            else:
                t = F.tone(m, GG['full'][m])
            img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = t
    if lit:                                                          # each bonfire's cold light on the ice round it
        yy, xx = np.mgrid[0:H * 16, 0:W * 16]
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
