"""Paint the empire-era region map (240x160, the full region-map screen) in MonoMyth's style.
Palette: MonoMyth's 48 region-map colours (indices below are into that palette, see MM_PAL).
Inputs: the terrain class map (classify.py) and the grid layout (layout.py).
Output: an indexed image whose pixel values are palette indices 0..47."""
import numpy as np
from PIL import Image
from layout import LAYOUT

# MonoMyth region-map palette (RGB555 expanded), read from its ROM at 0xA124F0
MM_PAL = [(0,0,0),(248,248,248),(88,136,136),(0,0,0),(80,96,48),(192,224,224),(48,64,24),(80,104,128),
 (104,168,160),(56,96,64),(120,136,64),(144,192,176),(56,88,96),(136,128,80),(80,88,96),(0,0,0),
 (192,176,152),(0,0,0),(16,112,48),(208,216,168),(224,232,216),(192,176,160),(64,136,120),(208,120,56),
 (88,88,136),(248,88,56),(112,96,64),(128,168,120),(200,176,80),(216,216,136),(152,120,72),(168,168,48),
 (152,112,40),(112,136,80),(192,184,128),(184,192,104),(152,160,120),(192,200,160),(120,160,104),(168,184,128),
 (152,160,104),(152,152,136),(136,152,104),(184,168,112),(216,200,128),(208,216,152),(0,0,0),(0,0,0)]
# colours MonoMyth's map does not need but ours does (slots that are empty in its palette)
MM_PAL[3]  = (56, 40, 40)     # ash: dark basalt
MM_PAL[15] = (104, 64, 48)    # ash: warm rock
MM_PAL[17] = (248, 152, 40)   # lava glow
DEEP, SHALLOW, GRASS, FOREST, MOUNTAIN, SNOW, SAND, ASH, MARSH = range(9)
rng = np.random.default_rng(7)

def bayer(h, w):
    b = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]) / 16.0
    return np.tile(b, (h // 4 + 1, w // 4 + 1))[:h, :w]

def dist_to(mask, maxd=6):
    """Chebyshev distance (pixels) from each pixel to the nearest True in mask, capped."""
    H, W = mask.shape; d = np.full((H, W), maxd, np.int32); cur = mask.copy()
    d[cur] = 0
    for k in range(1, maxd):
        p = np.pad(cur, 1)
        grow = p[1:-1, 1:-1] | p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:] | p[:-2, :-2] | p[:-2, 2:] | p[2:, :-2] | p[2:, 2:]
        d[grow & ~cur] = k; cur = grow
    return d

def noise(h, w, scale, seed):
    r = np.random.default_rng(seed); g = r.random((h // scale + 2, w // scale + 2))
    img = Image.fromarray((g * 255).astype(np.uint8)).resize(((w // scale + 2) * scale, (h // scale + 2) * scale), Image.BICUBIC)
    return np.asarray(img)[:h, :w] / 255.0

# ---- terrain ----
def soften_snow(cls):
    cls = cls.copy(); sn = cls == SNOW
    d = dist_to(~sn, 4); n = noise(*cls.shape, 3, 9)
    cls[sn & (d <= 2) & (n < 0.5)] = MOUNTAIN
    return cls

def paint_terrain(cls):
    H, W = cls.shape; out = np.zeros((H, W), np.uint8); B = bayer(H, W)
    water = cls <= SHALLOW; land = ~water
    dl = dist_to(land, 8)                                   # distance from water to land
    # sea: teal near land, blue-grey offshore, dithered band between
    t = np.clip((dl - 3) / 4.0, 0, 1)
    out[water] = np.where(t[water] > B[water], 7, 2)
    # foam: broken white line 2 px off the coast, light cyan wavelets just outside it
    n = noise(H, W, 3, 1)
    foam = water & (dl == 2) & (n > 0.35)
    out[foam] = 1
    out[water & (dl == 4) & (n > 0.72)] = 5
    # inland water (rivers / lakes): teal with a light edge
    # land base colours
    g = noise(H, W, 6, 2)
    m = land & (cls == GRASS); out[m] = np.where(g[m] > 0.62, 31, np.where(g[m] > 0.38, 27, 38))
    out[m & (B < 0.12) & (g > 0.5)] = 33
    m = land & (cls == SAND); out[m] = np.where(B[m] < 0.15, 28, 29)
    dn = noise(H, W, 6, 12); yy, xx = np.mgrid[0:H, 0:W]
    ph = (yy * 0.55 + np.sin(xx * 0.35 + dn * 5) * 1.6 + dn * 4) % 4.0
    out[m & (ph < 0.55)] = 28; out[m & (ph > 0.55) & (ph < 1.0)] = 44     # dune crest + lit face
    m = land & (cls == SNOW); out[m] = np.where(B[m] < 0.18, 5, 1)
    m = land & (cls == MARSH)
    out[m] = np.where(B[m] < 0.45, 22, 38)
    ch = noise(H, W, 3, 3); out[m & (np.abs(ch - 0.5) < 0.09)] = 2
    out[m & (np.abs(ch - 0.5) < 0.07) & (B < 0.2)] = 22
    out[m & (B > 0.88)] = 9                                   # reed tufts
    m = land & (cls == ASH)
    an = noise(H, W, 4, 4); out[m] = np.where(an[m] > 0.58, 15, 3)
    v1 = noise(H, W, 5, 5); v2 = noise(H, W, 7, 11)
    vein = m & (np.abs(v1 - 0.5) < 0.022) & (v2 > 0.45)
    out[vein] = 17; out[vein & (B < 0.3)] = 25
    # mountains: earth base; the peaks are stamped afterwards (stamp_peaks)
    m = land & (cls == MOUNTAIN)
    out[m] = np.where(B[m] < 0.25, 26, 30)
    s_ = land & (cls == SNOW); out[s_] = np.where(B[s_] < 0.08, 5, 1)
    # coast rim: a darker earth line where land meets water
    dw = dist_to(water, 2)
    rim = land & (dw == 1) & (cls != SNOW)
    out[rim] = np.where(cls[rim] == SAND, 28, 13)
    # forest floor then trees
    f = land & (cls == FOREST); out[f] = 6
    return out

TREE = ["..a..",
        ".aba.",
        ".abc.",
        "abbca",
        "abbbc",
        "..t.."]
TREE_COL = {'a': 4, 'b': 9, 'c': 10, 't': 26}
SNOWTREE = {'a': 4, 'b': 1, 'c': 5, 't': 26}

PEAK = ["...a...",
        "..aab..",
        ".aaabb.",
        "aaaabbb",
        "ddddddd"]
PEAK_COL = {'a': 16, 'b': 32, 'd': 26}
SNOWPEAK_ROWS = 2
SMALL_PEAK = [".......","...a...","..aab..",".aaabb.","ddddddd"]

def stamp_peaks(out, cls):
    H, W = cls.shape
    for y0 in range(-3, H, 4):
        for x0 in range(-3, W, 6):
            x = x0 + (3 if (y0 // 4) % 2 else 0) + rng.integers(-1, 2); y = y0 + rng.integers(-1, 1)
            cx, cy = x + 3, y + 3
            if not (0 <= cx < W and 0 <= cy < H): continue
            if cls[cy, cx] not in (MOUNTAIN, SNOW): continue
            snowy = cls[cy, cx] == SNOW
            if rng.random() < 0.12: continue                   # gaps break up the grid
            art = PEAK if rng.random() < 0.7 else SMALL_PEAK
            for j, row in enumerate(art):
                for i, ch in enumerate(row):
                    yy, xx = y + j, x + i
                    if ch == '.' or not (0 <= yy < H and 0 <= xx < W) or cls[yy, xx] <= SHALLOW: continue
                    c = PEAK_COL[ch]
                    if snowy and j < SNOWPEAK_ROWS + 1 and ch in 'ab': c = 1 if ch == 'a' else 5
                    out[yy, xx] = c

def stamp_trees(out, cls):
    H, W = cls.shape
    for y0 in range(-2, H, 4):
        for x0 in range(-2, W, 5):
            x = x0 + (2 if (y0 // 4) % 2 else 0) + rng.integers(-1, 2); y = y0 + rng.integers(-1, 2)
            cx, cy = x + 2, y + 3
            if not (0 <= cx < W and 0 <= cy < H): continue
            kind = cls[cy, cx]
            if kind == FOREST: col = TREE_COL
            elif kind == GRASS and rng.random() < 0.06: col = TREE_COL
            else: continue
            for j, row in enumerate(TREE):
                for i, ch in enumerate(row):
                    if ch == '.': continue
                    yy, xx = y + j, x + i
                    if 0 <= yy < H and 0 <= xx < W and cls[yy, xx] > SHALLOW:
                        out[yy, xx] = col[ch]

# ---- roads and markers ----
def cell_px(gx, gy): return 8 + 8 * gx + 4, 16 + 8 * gy + 4
ROADS = [  # waypoints in grid cells; drawn orthogonally between consecutive points
 [(4,0),(4,4)], [(4,4),(4,8)], [(4,8),(4,9)], [(3,8),(9,8)], [(6,7),(6,8)],
 [(4,3),(7,3),(7,2)], [(7,3),(8,3)], [(4,4),(9,4),(9,5)],
 [(8,8),(8,13)], [(9,8),(13,8)],
 [(13,2),(13,3)], [(12,3),(20,3)], [(12,3),(12,8),(13,8)], [(14,7),(13,7),(13,8)],
 [(14,7),(16,7),(16,8)], [(13,8),(16,8)], [(16,8),(20,8)],
 [(20,3),(20,8)], [(22,7),(22,8)], [(20,8),(24,8)],
 [(20,8),(20,10),(21,10),(21,13)],
 [(24,8),(24,0)],
]
WATER_MASK = None
def draw_roads(out):
    H, W = out.shape; fill = np.zeros((H, W), bool)
    for pts in ROADS:
        for (ax, ay), (bx, by) in zip(pts, pts[1:]):
            (x0, y0), (x1, y1) = cell_px(ax, ay), cell_px(bx, by)
            xs, xe = sorted((x0, x1)); ys, ye = sorted((y0, y1))
            fill[ys - 1:ye + 1, xs - 1:xe + 1] = True     # 2-px pale fill; the outline makes it 4 px
    p = np.pad(fill, 1); edge = (p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:]) & ~fill
    wet = WATER_MASK if WATER_MASK is not None else np.zeros_like(fill)
    out[edge] = np.where(wet[edge], 26, 18); out[fill] = np.where(wet[fill], 16, 19)   # over water: a bridge

def draw_marker(out, x, y, w, h, centre):
    """MonoMyth marker: dark-green outline, white ring, coloured centre; covers w x h cells."""
    x0, y0 = 8 + 8 * x + 1, 16 + 8 * y + 1; x1, y1 = 8 + 8 * (x + w) - 2, 16 + 8 * (y + h) - 2
    out[y0:y1 + 1, x0:x1 + 1] = 18
    out[y0 + 1:y1, x0 + 1:x1] = 20
    out[y0 + 2:y1 - 1, x0 + 2:x1 - 1] = centre

BIG_PEAK = [  # 17 x 10 landmark mountain, lit from the left; s/t = snow
 "........s........",
 ".......sst.......",
 "......sssbt......",
 ".....sssbbbt.....",
 "....asssabbbt....",
 "...aaasaabbbbt...",
 "..aaaaaaabbbbbt..",
 ".aaaaaaaabbbbbbt.",
 "aaaaaaaaabbbbbbbb",
 "ddddddddddddddddd"]
PEAK_COLOURS = {'Mt. Mirroh Peak': {'s': 1, 't': 5, 'a': 16, 'b': 32, 'd': 26},
                'Mt. Ceram':       {'s': 1, 't': 5, 'a': 41, 'b': 14, 'd': 3}}
LANDMARK_PEAKS = {'Mt. Mirroh Peak': BIG_PEAK, 'Mt. Ceram': BIG_PEAK}
def stamp_big_peak(out, name, x, y, w, h):
    art = LANDMARK_PEAKS[name]; ih, iw = len(art), len(art[0])
    cx = 8 + 8 * x + 4 * w; by = 16 + 8 * y + 8 * h - 1
    ox, oy = cx - iw // 2, by - ih + 1
    for j, row in enumerate(art):
        for i, ch in enumerate(row):
            if ch != '.' and 0 <= oy + j < out.shape[0] and 0 <= ox + i < out.shape[1]:
                out[oy + j, ox + i] = PEAK_COLOURS[name][ch]

def city_icon(name):
    """16 x 14 painted city, transparent = 255. Walls along the bottom, corner towers, roofs and a keep."""
    roof, dark = {'Silversun City': (24, 12), 'Pelluca Valley': (25, 26), 'Mirroh': (14, 12), 'Fennilahl': (24, 12),
                  'Rivetshore City': (23, 26), 'Galecrest City': (25, 26), 'Victory Cape': (25, 26)}.get(name, (25, 26))
    wall, shade, edge = (41, 14, 12) if name == 'Mirroh' else (21, 41, 26)
    a = np.full((14, 16), 255, np.uint8)
    a[9:13, 1:15] = wall; a[9:13, 10:15] = np.where(np.arange(5) >= 2, shade, wall)[None, :]
    a[13, 1:15] = edge; a[9:13, 1] = edge; a[9:13, 14] = edge
    a[8, 1:15:2] = wall                                           # crenellations
    a[11:13, 7:9] = 12; a[10, 7:9] = edge                         # gate
    for tx in (0, 13):                                            # corner towers with conical roofs
        a[5:13, tx:tx + 3] = wall; a[5:13, tx + 2] = shade; a[13, tx:tx + 3] = edge
        a[4, tx:tx + 3] = roof; a[3, tx:tx + 3] = roof; a[2, tx + 1] = roof; a[3:5, tx + 2] = dark
    for hx in (3, 9):                                             # gabled house roofs over the wall
        a[8, hx:hx + 5] = roof; a[7, hx + 1:hx + 4] = roof; a[6, hx + 2] = roof
        a[8, hx + 3:hx + 5] = dark; a[7, hx + 3] = dark
    if name in ('Silversun City', 'Mirroh', 'Fennilahl'):         # tall keep / cathedral spire
        a[3:9, 6:10] = wall; a[3:9, 9] = shade; a[5, 7] = 12
        a[2, 6:10] = roof; a[1, 7:9] = roof; a[0, 7] = roof; a[2, 9] = dark
    if name == 'Silversun City':                                  # the palace rising to the right, white with blue spires
        a[0:9, 10:13] = 20; a[0:9, 12] = 21; a[0, 11] = 24; a[1, 10:13] = 24; a[3, 11] = 12
    if name == 'Victory Cape':                                    # the lighthouse
        a[0:13, 12:15] = 1; a[0:13, 14] = 5; a[0, 12:15] = 25; a[1, 13] = 17; a[5, 12:15] = 25; a[9, 12:15] = 25
    return a

CITY_MARKER_CENTRE = 25      # red centre: large cities; towns/landmarks use teal (22)
def draw_city(out, name, x, y, w, h):
    """MonoMyth-style rectangle marker across the city's cells, with the painted city standing on it."""
    x0, y0 = 8 + 8 * x, 16 + 8 * y
    mx0, mx1, my0, my1 = x0 + 1, x0 + 8 * w - 2, y0 + 2, y0 + 8 * h - 1      # marker sits low in the cell
    out[my0:my1 + 1, mx0:mx1 + 1] = 18
    out[my0 + 1:my1, mx0 + 1:mx1] = 20
    out[my0 + 2:my1 - 1, mx0 + 2:mx1 - 1] = CITY_MARKER_CENTRE
    icon = city_icon(name)[:-1]                                   # the marker is the city's ground line
    ih, iw = icon.shape
    oy = my0 - ih; ox = x0 + (8 * w - iw) // 2
    for j in range(ih):
        for i in range(iw):
            if icon[j, i] != 255 and 0 <= oy + j < out.shape[0]: out[oy + j, ox + i] = icon[j, i]

def paint(cls):
    global WATER_MASK
    WATER_MASK = cls <= SHALLOW
    cls = soften_snow(cls)
    out = paint_terrain(cls)
    stamp_peaks(out, cls)
    stamp_trees(out, cls)
    draw_roads(out)
    for name, kind, x, y, w, h in LAYOUT:
        if name in LANDMARK_PEAKS: stamp_big_peak(out, name, x, y, w, h)
    for name, kind, x, y, w, h in LAYOUT:
        if kind == 'town' and name != 'Silversun Palace' and name not in LANDMARK_PEAKS: draw_marker(out, x, y, 1, 1, 22)
    for name, kind, x, y, w, h in LAYOUT:                          # cities last: their icons stand over the cell above
        if kind == 'city': draw_city(out, name, x, y, w, h)
    return out

def to_rgb(idx):
    return np.array(MM_PAL, np.uint8)[idx]
