"""The slip's set pieces: cut from MonoMyth (the canyon's falls, rope bridge, rope ladder, adobe houses and carved
panels; Santana's canyon's skull and stone spikes, the spikes turned to bone) or painted (the dreamstone obelisks, the
two altars, the spine's vertebrae, the rib arches, the pink crystal sand). Each returns (rgb, alpha) in pixels."""
import os, sys, random, collections
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'mt_mirroh')); sys.path.insert(0, '/home/claude/mono')
import mm_render as MR
S = 16
_R = {}
def src(addr):
    if addr not in _R:
        img, c, ts, L = MR.render(addr); _R[addr] = (img, c, L['w'], L['h'])
    return _R[addr]
def block(addr, x0, y0, x1, y1):
    img = src(addr)[0]; return img[y0 * S:(y1 + 1) * S, x0 * S:(x1 + 1) * S].copy()

def ground_cut(addr, x0, y0, x1, y1, n_ground=4):
    """a prop standing on a map's ground: its pixels that are not the ground's colours (the map's commonest tiles),
    holes filled, specks dropped"""
    from scipy.ndimage import binary_fill_holes, label
    img, c, W, H = src(addr)
    cnt = collections.Counter(v & 0x3FF for v in c)
    gcols = set()
    for m, _ in cnt.most_common(n_ground):
        ys, xs = [(i // W, i % W) for i, v in enumerate(c) if v & 0x3FF == m][0]
        gcols |= {tuple(p) for p in img[ys * S:ys * S + S, xs * S:xs * S + S].reshape(-1, 3)}
    rgb = block(addr, x0, y0, x1, y1)
    a = ~np.array([[tuple(p) in gcols for p in row] for row in rgb])
    a = binary_fill_holes(a)
    lab, n = label(a)
    if n > 1:
        sz = np.bincount(lab.ravel()); keep = [i for i in range(1, n + 1) if sz[i] >= 12]
        a = np.isin(lab, keep)
    return rgb, a

BONE = [(255, 250, 232), (236, 226, 196), (204, 188, 154), (160, 140, 110), (104, 86, 70), (58, 44, 40)]
def to_bone(rgb, a):
    """stone to bone: each pixel's lightness onto the bone ramp"""
    out = rgb.copy(); lum = rgb.astype(int).mean(-1)
    lv = np.clip(((235 - lum) / 190.0 * (len(BONE) - 0.01)).astype(int), 0, len(BONE) - 1)
    for i, c in enumerate(BONE): out[a & (lv == i)] = c
    return out

# ---- MonoMyth pieces (map, cells)
CANYON, SANTANA, DESERT, AMPHI = 0x86daf4, 0x8699c4, 0x869708, 0x86c028
def falls(rows):
    """the canyon's falls, two wide (its middle columns), `rows` tall, its foam row last"""
    body = [block(CANYON, 14, 25 + min(k, 3), 15, 25 + min(k, 3)) for k in range(rows - 1)]
    return np.concatenate(body + [block(CANYON, 14, 29, 15, 29)], 0)
def bridge(rows):
    """the canyon's rope bridge running north-south, two wide: its north end, deck, south end"""
    if rows <= 1: return block(CANYON, 51, 35, 52, 35)
    mids = [block(CANYON, 51, 35 + (k % 2), 52, 35 + (k % 2)) for k in range(rows - 2)]
    return np.concatenate([block(CANYON, 51, 34, 52, 34)] + mids + [block(CANYON, 51, 37, 52, 37)], 0)
def ladder(rows, cols=2):
    """the canyon's rope ladder down a cliff face: its top, rungs, foot"""
    x0, x1 = (43, 44) if cols == 2 else (43, 43)
    if rows == 1: return block(CANYON, x0, 46, x1, 46)
    mids = [block(CANYON, x0, 42 + (k % 3), x1, 42 + (k % 3)) for k in range(rows - 2)]
    return np.concatenate([block(CANYON, x0, 41, x1, 41)] + mids + [block(CANYON, x0, 46, x1, 46)], 0)
def house(which):
    """an adobe house of the canyon's village (4x5), its doorway walled up (the wall beside it carried across)"""
    if which == 0:
        b = block(CANYON, 39, 0, 42, 4); b[4 * S:5 * S, 1 * S:2 * S] = block(CANYON, 41, 4, 41, 4)
    else:
        b = block(CANYON, 39, 7, 42, 11)
    return b
def panel(k):
    """a carved alcove of the amphitheatre's wall (2x2): the old people's figures"""
    x = (8, 11, 14)[k % 3]; return block(AMPHI, x, 13, x + 1, 14)
def _nogreen(rgb, a):
    f = rgb.astype(int); g = (f[..., 1] > f[..., 0] + 10) & (f[..., 1] > f[..., 2] + 10); return rgb, a & ~g
def skull():
    """Santana's canyon's great skull (5x5 cells), only its own body (the stone spike beside it left out)"""
    from scipy.ndimage import label
    rgb, a = _nogreen(*ground_cut(SANTANA, 14, 42, 19, 46))
    lab, n = label(a, structure=np.ones((3, 3), int))
    if n > 1: a = lab == 1 + int(np.argmax(np.bincount(lab.ravel())[1:]))
    return rgb, a
SPIKES = [(8, 35, 8, 36), (9, 34, 9, 35), (10, 40, 10, 41)]
SMALL_SPIKES = [(10, 34, 10, 34), (7, 37, 7, 37)]
def spike(k, tall=True):
    box = SPIKES[k % len(SPIKES)] if tall else SMALL_SPIKES[k % len(SMALL_SPIKES)]
    rgb, a = _nogreen(*ground_cut(SANTANA, *box)); return to_bone(rgb, a), a

# ---- painted
PINK = [(70, 22, 74), (132, 46, 140), (196, 88, 200), (238, 150, 236), (255, 226, 252)]
def obelisk():
    """a dreamstone obelisk, 16x32 (its upper half on the top layer): a broad faceted crystal shaft tapering to a
    point, set in a sandstone socket, lit from the west (its west facet pale, its east facet deep), a glow at its foot"""
    rgb = np.zeros((32, 16, 3), np.uint8); a = np.zeros((32, 16), bool)
    for y in range(1, 26):
        half = min(6, 1 + (y - 1) * 6 // 14)
        x0, x1 = 8 - half, 7 + half
        for x in range(x0, x1 + 1):
            a[y, x] = True
            rgb[y, x] = PINK[3] if x < 6 else PINK[2] if x < 8 else PINK[1] if x < 10 else (100, 36, 110)
        rgb[y, x0] = PINK[0]; rgb[y, x1] = PINK[0]
        if y > 3 and x0 + 1 < 8: rgb[y, x0 + 1] = PINK[4] if (y // 3) % 2 else PINK[3]
    for y in range(6, 25, 6): rgb[y, 3:13][a[y, 3:13]] = PINK[0]                        # (its facet bands)
    rgb[1, 7:9] = PINK[4]
    for y in range(24, 31):                                  # its socket
        for x in range(1, 15):
            a[y, x] = True; rgb[y, x] = (186, 100, 72) if y < 26 else (148, 70, 52)
        rgb[y, 1] = rgb[y, 14] = (74, 30, 26)
    rgb[24, 1:15] = (226, 150, 110); rgb[30, 1:15] = (74, 30, 26)
    rgb[26, 4:12] = (250, 190, 240)                          # (its glow on the socket's lip)
    return rgb, a
def altar(north=False):
    """an ancient altar, 32x32: a round sandstone dais of two tiers seen from above and in front, a ring carved in its
    top, a dreamstone shard floating over a socket at its heart; the north one with a stone horn either side"""
    rgb = np.zeros((32, 32, 3), np.uint8); a = np.zeros((32, 32), bool)
    yy, xx = np.mgrid[0:32, 0:32]
    def disc(cy, rx, ry, h, top, side, rim):
        topm = ((xx - 15.5) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1
        sidem = np.zeros_like(topm)
        for d in range(1, h + 1): sidem |= np.roll(topm, d, 0)
        sidem &= ~topm
        rgb[sidem] = side; a[sidem] = True
        rgb[sidem & (yy > cy + ry + h - 2)] = (70, 30, 26)
        rgb[topm] = top; a[topm] = True
        edge = topm & ~(((xx - 15.5) / (rx - 1)) ** 2 + ((yy - cy) / (ry - 1)) ** 2 <= 1)
        rgb[edge & (yy < cy)] = (240, 176, 130); rgb[edge & (yy >= cy)] = rim
        return topm
    disc(21, 15.5, 7, 4, (196, 112, 78), (150, 70, 52), (110, 50, 40))
    t2 = disc(17 if north else 18, 10, 4.6, 4, (214, 132, 92), (164, 80, 58), (118, 54, 42))
    cy2 = 17 if north else 18
    ring = (((xx - 15.5) / 7.5) ** 2 + ((yy - cy2) / 3.2) ** 2 <= 1) & ~(((xx - 15.5) / 6.5) ** 2 + ((yy - cy2) / 2.4) ** 2 <= 1)
    rgb[ring & t2] = (142, 62, 50)
    sock = ((xx - 15.5) / 3) ** 2 + ((yy - cy2) / 1.6) ** 2 <= 1; rgb[sock] = (60, 20, 40)
    # the floating shard (a small crystal over the socket) and its glow
    sh = (abs(xx - 15.5) <= (yy - (cy2 - 12)) * 0.4) & (yy >= cy2 - 12) & (yy <= cy2 - 6) | \
         (abs(xx - 15.5) <= (cy2 - 1 - yy) * 0.6) & (yy > cy2 - 6) & (yy <= cy2 - 3)
    rgb[sh] = PINK[2]; rgb[sh & (xx < 16)] = PINK[3]; rgb[sh & (xx < 15) & (yy < cy2 - 7)] = PINK[4]; a |= sh
    glow = sock & (yy <= cy2); rgb[glow] = PINK[1]
    if north:
        for hx, d in ((4, 1), (27, -1)):
            for y in range(2, 20):
                w = 1 if y < 8 else 2
                cx_ = hx + d * (y // 7)
                a[y, cx_ - w:cx_ + w + 1] = True; rgb[y, cx_ - w:cx_ + w + 1] = (176, 92, 66)
                rgb[y, cx_ - w] = (226, 150, 110); rgb[y, cx_ + w] = (84, 36, 30)
    return rgb, a
def vertebra(seed):
    r = random.Random(seed); rgb = np.zeros((16, 16, 3), np.uint8); a = np.zeros((16, 16), bool)
    yy, xx = np.mgrid[0:16, 0:16]
    body = ((xx - 8) / 6.5) ** 2 + ((yy - 9) / 4.2) ** 2 <= 1
    spine_ = (abs(xx - 8 + (yy - 4) * 0.3) <= 1.2) & (yy >= 1) & (yy <= 7)
    m = body | spine_; a |= m
    rgb[m] = BONE[1]; rgb[m & (yy < 8) & (xx < 8)] = BONE[0]
    rgb[m & (yy > 11)] = BONE[2]
    edge = m & ~np.roll(m, 1, 1) | m & ~np.roll(m, -1, 1) | m & ~np.roll(m, -1, 0); rgb[edge] = BONE[4]
    rgb[(abs(xx - 8 - r.randint(-2, 2)) < 1) & (abs(yy - 9) < 2) & body] = BONE[3]
    return rgb, a
def arch(width_cells):
    """a rib arching over the way, 3 cells tall: a thick band of bone rising from a foot in the sand either side (the
    outer cells) over the path (the cells between); the upper two rows go on the top layer (walked under)"""
    Wp = (width_cells + 2) * S; Hp = 3 * S
    rgb = np.zeros((Hp, Wp, 3), np.uint8); a = np.zeros((Hp, Wp), bool)
    yy, xx = np.mgrid[0:Hp, 0:Wp]
    cx = Wp / 2.0; rx, ry = Wp / 2.0 - 2, Hp - 3
    outer = ((xx - cx) / rx) ** 2 + ((yy - Hp) / ry) ** 2 <= 1
    inner = ((xx - cx) / (rx - 9)) ** 2 + ((yy - Hp) / (ry - 9)) ** 2 <= 1
    m = outer & ~inner; a |= m
    rgb[m] = BONE[1]
    hi = m & ~(((xx - cx) / (rx - 3)) ** 2 + ((yy - Hp) / (ry - 3)) ** 2 <= 1); rgb[hi] = BONE[0]
    lo = m & (((xx - cx) / (rx - 7)) ** 2 + ((yy - Hp) / (ry - 7)) ** 2 <= 1); rgb[lo] = BONE[2]
    edge = m & (~np.roll(m, 1, 0) | ~np.roll(m, -1, 0) | ~np.roll(m, 1, 1) | ~np.roll(m, -1, 1)); rgb[edge] = BONE[4]
    for k in range(6, Wp - 6, 11): rgb[m & ~edge & (abs(xx - k) < 1)] = BONE[3]          # (its grain, cracks)
    feet = m & (yy > Hp - 5); rgb[feet] = BONE[3]
    return rgb, a
def spine(points, seed=3):
    """the spine's vertebrae along a curve of pixel points: a chain of bone knuckles, each with a dorsal spike rising
    north (its length varying); returns (rgb, a) over the whole map's pixel size given by the caller"""
    return points
def pink_sand(sand):
    """the sand the obelisks' power has soaked into: each sand pixel's lightness onto a pink ramp"""
    ramp = [(250, 214, 222), (238, 186, 204), (220, 156, 184), (190, 120, 156)]
    lum = sand.astype(int).mean(-1); out = sand.copy()
    lv = np.clip(((240 - lum) / 70.0 * 3.99).astype(int), 0, 3)
    for i, c in enumerate(ramp): out[lv == i] = c
    return out
GEMS = [[(3, 4), (11, 9)], [(7, 3), (2, 12), (12, 13)], [(9, 6)], [(4, 9), (13, 3)]]
def gem(img, ox, oy):
    img[oy, ox] = (255, 255, 255); img[oy - 1, ox] = img[oy + 1, ox] = (190, 240, 255)
    img[oy, ox - 1] = img[oy, ox + 1] = (150, 220, 250)
