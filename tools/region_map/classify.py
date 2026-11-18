"""Classify the illustrated empire map into terrain classes on the 240x160 region-map screen.
Grid cell (gx, gy) of the 28x15 region-map grid covers screen pixels x 8+8gx.., y 16+8gy..
and maps to the painting crop (25..1515, 25..975)."""
import numpy as np
from PIL import Image
CLASSES = ['deep', 'shallow', 'grass', 'forest', 'mountain', 'snow', 'sand', 'ash', 'marsh']
X0, X1, Y0, Y1 = 25, 1515, 25, 975
def painting_xy(sx, sy):
    return X0 + (sx - 8) * (X1 - X0) / 224.0, Y0 + (sy - 16) * (Y1 - Y0) / 120.0
def classify_pixels(rgb):
    r, g, b = [rgb[..., i].astype(float) for i in range(3)]
    mx = np.maximum(np.maximum(r, g), b); mn = np.minimum(np.minimum(r, g), b)
    sat = (mx - mn) / np.maximum(mx, 1); v = mx; lum = 0.3*r + 0.59*g + 0.11*b
    c = np.full(r.shape, 2, np.uint8)                                   # grass by default
    water = (b > r + 8) & (b >= g - 6)
    c[water & (lum < 95)] = 0; c[water & (lum >= 95)] = 1
    c[(g > r) & (g > b) & (lum < 70)] = 3                               # dark green = forest
    c[(sat < 0.22) & (lum >= 70) & ~water] = 4                          # grey rock
    c[(lum > 185) & (sat < 0.18)] = 5                                   # snow
    c[(r > g) & (g > b) & (r > 150) & (sat > 0.25) & (lum > 120)] = 6   # tan sand / desert
    c[(lum < 60) & (r >= g) & (r >= b)] = 7                             # dark ash
    c[(r > 170) & (g < 120) & (b < 80)] = 7                             # lava glow
    return c
def class_map(src_path, W=240, H=160, ss=4):
    src = np.asarray(Image.open(src_path).convert('RGB'))
    out = np.zeros((H, W), np.uint8)
    ys, xs = np.mgrid[0:H*ss, 0:W*ss] / ss
    px, py = painting_xy(xs, ys)
    inside = (px >= 0) & (px < src.shape[1]) & (py >= 0) & (py < src.shape[0])
    samp = np.zeros(xs.shape + (3,), np.uint8)
    samp[inside] = src[py[inside].astype(int), px[inside].astype(int)]
    cls = classify_pixels(samp); cls[~inside] = 0
    votes = np.zeros((H, W, len(CLASSES)), np.int32)
    for k in range(len(CLASSES)):
        votes[..., k] = (cls == k).reshape(H, ss, W, ss).sum((1, 3))
    return votes.argmax(-1).astype(np.uint8)

# ---- v2: biome outlines in PAINTING coordinates override the colour classifier on land ----
from PIL import ImageDraw
BIOMES = [  # (class, polygon) -- painted in this order, later wins
 ('mountain', [(20,30),(345,30),(352,120),(305,200),(330,300),(300,420),(262,470),(150,482),(60,452),(20,420)]),
 ('snow',     [(190,25),(330,25),(318,90),(280,135),(225,128),(195,80)]),
 ('snow',     [(40,60),(110,40),(150,90),(120,160),(70,170),(40,120)]),
 ('mountain', [(1262,236),(1332,232),(1392,330),(1362,425),(1290,432),(1250,360)]),
 ('snow',     [(1300,250),(1340,248),(1352,290),(1310,296)]),
 ('sand',     [(1180,25),(1510,25),(1510,250),(1400,245),(1335,232),(1235,200),(1180,120)]),
 ('ash',      [(1392,240),(1510,200),(1510,650),(1440,660),(1385,530),(1362,430),(1392,330)]),
 ('marsh',    [(505,545),(565,522),(700,540),(760,585),(705,640),(565,660),(512,612)]),
]
FORCE_SEA = [(540,0,995,72), (15,760,200,960)]   # title cartouche, compass rose
def _majority(a, k, n):
    from numpy.lib.stride_tricks import sliding_window_view
    p = np.pad(a, k//2, mode='edge'); w = sliding_window_view(p, (k, k))
    counts = np.stack([(w == c).sum((-1, -2)) for c in range(n)], -1)
    return counts.argmax(-1).astype(a.dtype)
def _small_components(mask, minsize):
    from collections import deque
    H, W = mask.shape; seen = np.zeros_like(mask, bool); out = []
    for y in range(H):
        for x in range(W):
            if mask[y, x] and not seen[y, x]:
                q = deque([(y, x)]); seen[y, x] = True; comp = []
                while q:
                    cy, cx = q.popleft(); comp.append((cy, cx))
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = cy+dy, cx+dx
                        if 0 <= ny < H and 0 <= nx < W and mask[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True; q.append((ny, nx))
                if len(comp) < minsize: out += comp
    return out
def class_map_v2(src_path, W=240, H=160):
    raw = class_map(src_path, W, H)
    # biome layer, rasterised on the screen grid via the painting->screen transform
    def to_screen(pt): return (8 + (pt[0]-X0)*224.0/(X1-X0), 16 + (pt[1]-Y0)*120.0/(Y1-Y0))
    biome = Image.new('L', (W, H), 255); d = ImageDraw.Draw(biome)
    for name, poly in BIOMES: d.polygon([to_screen(p) for p in poly], fill=CLASSES.index(name))
    for x0, y0, x1, y1 in FORCE_SEA:
        a, b = to_screen((x0, y0)), to_screen((x1, y1)); d.rectangle([a, b], fill=254)
    biome = np.asarray(biome)
    water = (raw <= 1) | (biome == 254)
    # outside the painting is open sea
    ys, xs = np.mgrid[0:H, 0:W]; px, py = painting_xy(xs + .5, ys + .5)
    water |= (px < X0 + 4) | (px > X1 - 4) | (py < Y0 + 4) | (py > Y1 - 4)
    water = _majority(water.astype(np.uint8), 3, 2).astype(bool)
    for y, x in _small_components(water, 5): water[y, x] = False      # specks of "water" in land (labels)
    for y, x in _small_components(~water, 4): water[y, x] = True      # specks of land at sea
    land = np.where(raw == 3, 3, 2).astype(np.uint8)                   # forest vs grass only
    land = _majority(land, 5, 4)
    out = np.where(water, 0, land).astype(np.uint8)
    on = (biome < 254) & ~water
    out[on] = biome[on]
    # shallow band: water within 2 px of land; inland water (rivers, lakes) is all shallow
    from numpy.lib.stride_tricks import sliding_window_view
    landm = np.pad(~water, 2, mode='edge'); near = sliding_window_view(landm, (5, 5)).any((-1, -2))
    out[water & near] = 1
    return out

# ---- v3: land runs off-screen (no forced sea at the painting's border) + explicit rivers ----
RIVERS = [  # polylines in painting coordinates, drawn 1 px wide as shallow water
 [(485,185),(445,240),(465,300),(450,345),(475,410),(460,470),(450,545)],      # Ivy River, west branch
 [(650,165),(640,180),(610,280),(580,330),(550,420),(520,480),(480,545)],      # Ivy River, east branch
 [(1240,290),(1210,380),(1180,450),(1155,530),(1160,570),(1195,620),(1190,712)],  # eastern river
]
def class_map_v3(src_path, W=240, H=160):
    global painting_xy
    _orig = painting_xy
    def clamped(sx, sy):
        px, py = _orig(sx, sy)
        return np.clip(px, 32, 1503), np.clip(py, 32, 965)
    painting_xy = clamped
    try:
        raw = class_map(src_path, W, H)
    finally:
        painting_xy = _orig
    def to_screen(pt): return (8 + (pt[0]-X0)*224.0/(X1-X0), 16 + (pt[1]-Y0)*120.0/(Y1-Y0))
    biome = Image.new('L', (W, H), 255); d = ImageDraw.Draw(biome)
    for name, poly in BIOMES: d.polygon([to_screen(p) for p in poly], fill=CLASSES.index(name))
    for x0, y0, x1, y1 in FORCE_SEA:
        a, b = to_screen((x0, y0)), to_screen((x1, y1)); d.rectangle([a, b], fill=254)
    # the biome polygons that touch the painting border continue off-screen too
    biome = np.asarray(biome).copy()
    water = (raw <= 1) | (biome == 254)
    water = _majority(water.astype(np.uint8), 3, 2).astype(bool)
    for y, x in _small_components(water, 5): water[y, x] = False
    for y, x in _small_components(~water, 4): water[y, x] = True
    land = _majority(np.where(raw == 3, 3, 2).astype(np.uint8), 5, 4)
    out = np.where(water, 0, land).astype(np.uint8)
    # extend edge-touching biome polygons to the screen edge by clamping the lookup
    ys, xs = np.mgrid[0:H, 0:W]
    bx = np.clip(xs, 8, 231); by = np.clip(ys, 16, 135)
    bext = biome[by, bx]
    on = (bext < 254) & ~water
    out[on] = bext[on]
    from numpy.lib.stride_tricks import sliding_window_view
    landm = np.pad(~water, 2, mode='edge'); near = sliding_window_view(landm, (5, 5)).any((-1, -2))
    out[water & near] = 1
    riv = Image.new('L', (W, H), 0); dr = ImageDraw.Draw(riv)
    for line in RIVERS: dr.line([to_screen(p) for p in line], fill=1, width=1)
    out[np.asarray(riv) == 1] = 1
    return out

# ---- v4: classify the grid area only, then grow the margins from a smoothed copy of its edge ----
def _smooth_line(v, k=11, n=len(CLASSES)):
    p = np.pad(v, k//2, mode='edge'); out = v.copy()
    for i in range(len(v)): out[i] = np.bincount(p[i:i+k], minlength=n).argmax()
    return out
def class_map_v4(src_path, W=240, H=160):
    full = class_map_v2(src_path, W, H)          # v2 forces sea outside the painting; we only keep the grid part
    gx0, gx1, gy0, gy1 = 8, 232, 16, 136
    g = full[gy0:gy1, gx0:gx1].copy()
    # v2's border-sea ring sits on the grid edge: re-read the first 3 px from 3 px further in
    for k in range(3):
        g[k, :] = g[3, :]; g[-1-k, :] = g[-4, :]; g[:, k] = g[:, 3]; g[:, -1-k] = g[:, -4]
    out = np.zeros((H, W), np.uint8)
    out[gy0:gy1, gx0:gx1] = g
    top, bot = _smooth_line(g[3, :]), _smooth_line(g[-4, :])
    left, right = _smooth_line(g[:, 3]), _smooth_line(g[:, -4])
    out[:gy0, gx0:gx1] = top; out[gy1:, gx0:gx1] = bot
    out[gy0:gy1, :gx0] = left[:, None]; out[gy0:gy1, gx1:] = right[:, None]
    out[:gy0, :gx0] = top[0]; out[:gy0, gx1:] = top[-1]; out[gy1:, :gx0] = bot[0]; out[gy1:, gx1:] = bot[-1]
    out[gy1:, :] = 0                              # south of the map is open sea
    water = out <= 1
    from numpy.lib.stride_tricks import sliding_window_view
    landm = np.pad(~water, 2, mode='edge'); near = sliding_window_view(landm, (5, 5)).any((-1, -2))
    out[water] = 0; out[water & near] = 1
    def to_screen(pt): return (8 + (pt[0]-X0)*224.0/(X1-X0), 16 + (pt[1]-Y0)*120.0/(Y1-Y0))
    riv = Image.new('L', (W, H), 0); dr = ImageDraw.Draw(riv)
    for line in RIVERS: dr.line([to_screen(p) for p in line], fill=1, width=1)
    out[np.asarray(riv) == 1] = 1
    return out
