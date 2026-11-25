"""MonoMyth's bastion ascent (its map 0x868f4c, the climb inside the bastion castle that leads up to its top, the open
sky; user 2026-11-25: "study the bastion part that leads to the open sky area in monomyth"), cut and made Hollow Hill's.

What makes it work, as a whole design: four flights of stairs on one axis, each narrower than the one below (23, 17,
11, 3 wide), so the climb draws the eye up like a funnel to the arcade at the top; a landing between each two flights;
a pair of round columns and a pair of knight statues flanking every flight; massive stone tiers stepping up either
side, their lit tops and shaded faces in courses; the whole thing shaded on one side; moss and creepers in the joints.
Here: x 16..42, rows 0..27 (its axis x 29 is ours), recoloured onto Hollow Hill's bone and sinister stone (light to
dark by lightness; its moss to Hollow Hill's dead weeds), its walkable cells kept from its own collision.
Credit: MonoMyth (the bastion's art)."""
import os, sys
import numpy as np
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools/art/mt_mirroh'))
X0, Y0, CW, CH = 16, 0, 27, 28
CX = 29 - X0                                   # the axis in the cut (column 13)
ARCADE_ROW = 4                                 # the row of dark arches (the way on, up into the bastion)
BONE_RAMP = [(236, 230, 214), (218, 210, 192), (194, 184, 166), (164, 154, 142), (134, 124, 124), (104, 94, 104),
             (74, 64, 78), (46, 38, 50), (26, 20, 28)]
WEEDS = [(64, 60, 44), (96, 92, 64), (128, 122, 86), (160, 154, 112)]

def lum(c): return 0.3 * c[0] + 0.55 * c[1] + 0.15 * c[2]

def cut(extra=0):
    import mm_render as R
    img, c, ts, L = R.render(0x868f4c); W = L['w']
    rgb = img[Y0 * 16:(Y0 + CH + extra) * 16, X0 * 16:(X0 + CW) * 16].copy()
    walk = np.array([[((c[(Y0 + y) * W + X0 + x] >> 10) & 3) == 0 for x in range(CW)] for y in range(CH)])
    return rgb, walk

def recolour(rgb):
    cols = sorted({tuple(int(v) for v in p) for p in rgb.reshape(-1, 3)}, key=lum, reverse=True)
    green = [c for c in cols if c[1] > c[0] + 10 and c[1] > c[2] + 6]
    stone = [c for c in cols if c not in green]
    m = {}
    ls = [lum(c) for c in stone]; lo, hi = min(ls), max(ls)
    for c in stone:
        t = (hi - lum(c)) / max(1, hi - lo)                      # 0 lightest .. 1 darkest
        m[c] = BONE_RAMP[min(len(BONE_RAMP) - 1, int(t ** 0.72 * len(BONE_RAMP)))]
    if green:
        lg = [lum(c) for c in green]; glo, ghi = min(lg), max(lg)
        for c in green: m[c] = WEEDS[min(3, int((lum(c) - glo) / max(1, ghi - glo + 1) * 4))]
    out = rgb.copy(); flat = out.reshape(-1, 3)
    keys = [tuple(int(v) for v in p) for p in flat]
    for i, k in enumerate(keys): flat[i] = m[k]
    return out

_cache = {}
def bastion():
    """(the bastion's art, its walkable cells, its paving below the last flight: rows 27-28, two cells tall)"""
    if 'b' not in _cache:
        rgb, walk = cut(extra=2); rgb = recolour(rgb)
        _cache['b'] = (rgb[:CH * 16], walk, rgb[(CH - 1) * 16:(CH + 1) * 16])
    return _cache['b'][:2]
def paving(): bastion(); return _cache['b'][2]

if __name__ == '__main__':
    from PIL import Image
    r, w = bastion(); Image.fromarray(r).save('/tmp/summit/bastion_bone.png'); print(r.shape)

def top_mask():
    """the pixels MonoMyth draws on its top layer (entries 8-11 of its triple-layer metatiles): over the player (the
    columns' upper drums, the statues' heads, the tiers' lips the player walks behind)"""
    import mm_render as R
    from romlib import u16, off
    img, c, ts, L = R.render(0x868f4c); W = L['w']
    NPM = 512
    m = np.zeros((CH * 16, CW * 16), bool)
    for y in range(CH):
        for x in range(CW):
            mid = c[(Y0 + y) * W + X0 + x] & 0x3ff
            base = ts.pmt + mid * 24 if mid < NPM else ts.smt + (mid - NPM) * 24
            for q in range(8, 12):
                e = u16(base + q * 2); t = ts.tile(e & 0x3ff)
                if t is None: continue
                if (e >> 10) & 1: t = t[:, ::-1]
                if (e >> 11) & 1: t = t[::-1, :]
                oy, ox = ((q % 4) // 2) * 8, ((q % 4) % 2) * 8
                m[y * 16 + oy:y * 16 + oy + 8, x * 16 + ox:x * 16 + ox + 8] |= t != 0
    return m
