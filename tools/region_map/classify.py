"""Classify the illustrated empire map (assets/region_map/cormorian_empire_illustrated.png) into terrain
classes on the 240x160 region-map screen.

Geometry: grid cell (gx, gy) of the 28x15 region-map grid covers screen pixels x 8+8gx.., y 16+8gy..
and the grid as a whole maps to the painting crop (25..1515, 25..975). Outside the grid the map is
continued from a smoothed copy of its edge (south of the map is always sea).

Method (v5, 2026-11-18, after the user's topography review):
- From colour, only water / grass / forest are trusted. Everything else the painting draws on top of
  the land -- roads, bridges, labels, route plaques, city drawings -- is UNKNOWN and is filled from the
  surrounding known terrain. (v1-v4 read a stone bridge as land and fused Rivetshore to Windrunner.)
- Biomes (mountain, snow, sand, ash, marsh) come from outlines traced on the painting, not colour.
- Rivers are explicit 1-px lines; the sea gets a shallow band within 2 px of land.
"""
import numpy as np
from PIL import Image, ImageDraw
from numpy.lib.stride_tricks import sliding_window_view

CLASSES = ['deep', 'shallow', 'grass', 'forest', 'mountain', 'snow', 'sand', 'ash', 'marsh']
DEEP, SHALLOW, GRASS, FOREST, MOUNTAIN, SNOW, SAND, ASH, MARSH = range(9)
UNKNOWN = 255
X0, X1, Y0, Y1 = 25, 1515, 25, 975          # painting crop that the 28x15 grid covers
GX0, GX1, GY0, GY1 = 8, 232, 16, 136        # the grid on the 240x160 screen

def painting_xy(sx, sy):
    return X0 + (sx - GX0) * (X1 - X0) / (GX1 - GX0), Y0 + (sy - GY0) * (Y1 - Y0) / (GY1 - GY0)
def to_screen(pt):
    return (GX0 + (pt[0] - X0) * (GX1 - GX0) / (X1 - X0), GY0 + (pt[1] - Y0) * (GY1 - GY0) / (Y1 - Y0))

# ---- traced outlines (painting coordinates); later entries win ----
BIOMES = [
 ('mountain', [(40,0),(370,0),(365,140),(330,200),(365,300),(330,400),(320,470),(300,520),(200,560),(140,620),(90,680),(40,660)]),
 ('mountain', [(290,462),(380,452),(392,522),(322,545)]),                       # Necropolis foothills
 ('snow',     [(195,0),(335,0),(325,80),(290,130),(230,125),(195,70)]),          # Mt. Mirroh Peak
 ('snow',     [(80,40),(160,30),(190,90),(150,150),(100,140)]),
 ('sand',     [(1175,0),(1510,0),(1510,140),(1420,150),(1380,250),(1360,400),(1355,560),(1300,580),
               (1230,540),(1215,420),(1225,300),(1235,210),(1195,120)]),         # Seregmorn + dry foothills
 ('ash',      [(1420,140),(1510,130),(1510,690),(1440,690),(1360,600),(1352,480),(1365,380),(1385,250)]),
 ('mountain', [(1245,250),(1300,240),(1352,300),(1345,370),(1290,380),(1240,340)]),   # Mt. Ceram
 ('snow',     [(1285,248),(1312,246),(1322,272),(1290,276)]),
 ('marsh',    [(505,545),(565,522),(700,540),(760,585),(705,640),(565,660),(512,612)]),
]
FORCE_SEA = [(540, 0, 995, 72), (15, 760, 200, 960),       # title cartouche, compass rose
             (330, 815, 560, 858)]                          # the strait under the Riptide Bridge: Windrunner is an island
FORCE_LAND = [  # (polygon in painting coords) land the painting draws too thin for the grid
 [(1135,700),(1275,700),(1290,800),(1240,830),(1160,830),(1120,800)],   # Victory Cape is a broad cape, not an island
]
RIVERS = [
 [(485,185),(445,240),(465,300),(450,345),(475,410),(460,470),(450,545)],          # Ivy River, west branch
 [(650,165),(640,180),(610,280),(580,330),(550,420),(520,480),(480,545)],          # Ivy River, east branch
 [(1240,290),(1210,380),(1180,450),(1155,530),(1160,570),(1195,620),(1190,712)],   # eastern river to the sea
]

def colour_class(rgb):
    r, g, b = [rgb[..., i].astype(float) for i in range(3)]
    mx = np.maximum(np.maximum(r, g), b); mn = np.minimum(np.minimum(r, g), b)
    sat = (mx - mn) / np.maximum(mx, 1); lum = 0.3*r + 0.59*g + 0.11*b
    c = np.full(r.shape, UNKNOWN, np.uint8)
    water = (b > r + 8) & (b >= g - 6) & (lum > 25)
    c[water] = DEEP
    greenish = (g >= r - 4) & (g > b + 4) & (sat > 0.12) & ~water
    c[greenish & (lum < 72)] = FOREST
    c[greenish & (lum >= 72) & (lum < 175)] = GRASS
    # olive / dry-grass tones of the painted fields
    c[(r > g) & (r - g < 18) & (g > b + 20) & (lum > 70) & (lum < 160) & ~water] = GRASS
    return c

def _vote(cls, H, W, ss):
    votes = np.zeros((H, W, 4), np.int32)
    for k, c in enumerate((DEEP, GRASS, FOREST, UNKNOWN)):
        votes[..., k] = (cls == c).reshape(H, ss, W, ss).sum((1, 3))
    known = votes[..., :3]
    out = np.array([DEEP, GRASS, FOREST], np.uint8)[known.argmax(-1)]
    # a pixel is unknown if most of it was drawn-over (road, label, icon)
    out[known.sum(-1) < votes[..., 3] * 0.6] = UNKNOWN
    return out

def _fill_unknown(a):
    a = a.copy()
    for _ in range(40):
        u = a == UNKNOWN
        if not u.any(): break
        p = np.pad(a, 1, mode='edge'); w = sliding_window_view(p, (3, 3)).reshape(*a.shape, 9)
        for c in (DEEP, GRASS, FOREST):
            pass
        cnt = np.stack([(w == c).sum(-1) for c in (DEEP, GRASS, FOREST)], -1)
        best = np.array([DEEP, GRASS, FOREST], np.uint8)[cnt.argmax(-1)]
        a[u & (cnt.sum(-1) > 0)] = best[u & (cnt.sum(-1) > 0)]
    return a

def _majority(a, k, values):
    p = np.pad(a, k // 2, mode='edge'); w = sliding_window_view(p, (k, k))
    cnt = np.stack([(w == v).sum((-1, -2)) for v in values], -1)
    return np.array(values, a.dtype)[cnt.argmax(-1)]

def _components(mask):
    from collections import deque
    H, W = mask.shape; lab = np.zeros(mask.shape, np.int32); n = 0; sizes = [0]
    for y in range(H):
        for x in range(W):
            if mask[y, x] and not lab[y, x]:
                n += 1; q = deque([(y, x)]); lab[y, x] = n; s = 0
                while q:
                    cy, cx = q.popleft(); s += 1
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = n; q.append((ny, nx))
                sizes.append(s)
    return lab, np.array(sizes)

def _smooth_line(v, k=11):
    p = np.pad(v, k // 2, mode='edge'); out = v.copy()
    for i in range(len(v)): out[i] = np.bincount(p[i:i + k], minlength=len(CLASSES)).argmax()
    return out

def class_map(src_path, W=240, H=160, ss=4):
    src = np.asarray(Image.open(src_path).convert('RGB'))
    ys, xs = np.mgrid[0:H * ss, 0:W * ss] / ss
    px, py = painting_xy(xs, ys)
    px = np.clip(px, 0, src.shape[1] - 1).astype(int); py = np.clip(py, 0, src.shape[0] - 1).astype(int)
    base = _fill_unknown(_vote(colour_class(src[py, px]), H, W, ss))
    # traced outlines and forced sea
    lay = Image.new('L', (W, H), 255); d = ImageDraw.Draw(lay)
    for name, poly in BIOMES: d.polygon([to_screen(p) for p in poly], fill=CLASSES.index(name))
    for x0, y0, x1, y1 in FORCE_SEA: d.rectangle([to_screen((x0, y0)), to_screen((x1, y1))], fill=254)
    lay = np.asarray(lay)
    fl = Image.new('L', (W, H), 0); df = ImageDraw.Draw(fl)
    for poly in FORCE_LAND: df.polygon([to_screen(p) for p in poly], fill=1)
    base = np.where((np.asarray(fl) == 1) & (base == DEEP), GRASS, base)
    water = (base == DEEP) | (lay == 254)
    water = _majority(water.astype(np.uint8), 3, [0, 1]).astype(bool)
    lab, sz = _components(water);  water[(sz[lab] < 5) & water] = False      # specks of water in land
    lab, sz = _components(~water); water[(sz[lab] < 4) & ~water] = True       # specks of land at sea
    land = _majority(np.where(base == FOREST, FOREST, GRASS).astype(np.uint8), 5, [GRASS, FOREST])
    out = np.where(water, DEEP, land).astype(np.uint8)
    on = (lay < 254) & ~water; out[on] = lay[on]
    # continue the map past the grid from a smoothed copy of its edge; south is sea
    g = out[GY0:GY1, GX0:GX1].copy()
    top, left, right = _smooth_line(g[0, :]), _smooth_line(g[:, 0]), _smooth_line(g[:, -1])
    full = np.zeros((H, W), np.uint8); full[GY0:GY1, GX0:GX1] = g
    full[:GY0, GX0:GX1] = top; full[GY0:GY1, :GX0] = left[:, None]; full[GY0:GY1, GX1:] = right[:, None]
    full[:GY0, :GX0] = top[0]; full[:GY0, GX1:] = top[-1]; full[GY1:, :] = DEEP
    water = full <= SHALLOW
    near = sliding_window_view(np.pad(~water, 2, mode='edge'), (5, 5)).any((-1, -2))
    full[water] = DEEP; full[water & near] = SHALLOW
    riv = Image.new('L', (W, H), 0); dr = ImageDraw.Draw(riv)
    for line in RIVERS: dr.line([to_screen(p) for p in line], fill=1, width=1)
    full[np.asarray(riv) == 1] = SHALLOW
    return full

def land_components(cls):
    """Label separate landmasses (for topology checks: Windrunner must be its own island)."""
    return _components(cls > SHALLOW)
