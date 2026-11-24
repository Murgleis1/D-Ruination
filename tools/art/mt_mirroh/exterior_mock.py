"""Mt. Mirroh's exterior, mock v1 (user 2026-11-23: an expansion of Dreamstone Mysteries' own Mt. Mirroh; plan
assets/mt_mirroh_reference/exterior_plan_v1.png; "go ahead and start building"; the look a combination of Route 13,
MonoMyth's mountains, Dreamstone Mysteries' snowy and icy mountain terrain, and Crown's).

Dreamstone Mysteries' own picture and collision are the base (its river valley, its blue ice cliffs and plateaus,
stairs, bridges, meadows, the cave mouth at the head), so the layout stays exactly; what changes:
  - its pines become Route 13's (MonoMyth's Fort Elderflower pines, snow-laden), laid as whole trees, staggered;
  - its tall grass becomes Route 13's ice grass;
  - the dojo is gone (pinewood), the lower cave mouth into B1F is rock (B1F is reached only from 1F later), the top
    edge is closed (pinewood);
  - the way in is the foot path (x 38-39) from Route 13.
Usage: python3 tools/art/mt_mirroh/exterior_mock.py [out.png]
"""
import os, sys, json, struct
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ART = os.path.join(HERE, '..'); REPO = os.path.abspath(os.path.join(ART, '..', '..'))
sys.path.insert(0, os.path.join(ART, 'mirroh')); sys.path.insert(0, os.path.join(ART, 'route13'))
import mirroh_mock as mm
W, H = 60, 80
D = json.load(open(os.path.join(HERE, 'dm_exterior_cells.json')))
BASE = os.path.join(REPO, 'assets', 'mt_mirroh_reference', 'dm_exterior.png')
DOJO = {(x, y) for x in range(33, 49) for y in range(4, 12)}
LOWER_MOUTH = [(11, 64), (11, 65)]
CAVE = (13, 10)
# the secret way down to B1F, Alaric's ritual site (user 2026-11-23: right by the main entrance into the mountain): a
# ladder hole in the ice west of the cave mouth, above two rocks, under a Rock Smash rock (an object, placed by the build;
# Rock Smash comes later in the game, so in Chapter 1 the rock stays)
SECRET = (9, 13)        # (user 2026-11-23, marked on a screenshot: the open ice above the two rocks, west of the mouth)
DRILL = [(15, 10), (16, 10), (15, 11), (16, 11)]   # (Dreamstone Mysteries' drilling machine by the mouth: gone, user)
MB_TALL_GRASS = 0x02
EFG = mm.EF_GROUND
BIG, SMALL, ROCK = [[0xe9, 0xea], [0xf1, 0xf2], [0xf9, 0xfa]], [[0x109], [0x111]], [[0xe8]]

def rnd(s, x, y):
    h = (x * 73856093) ^ (y * 19349663) ^ (sum(map(ord, s)) * 83492791)
    return (h % 10007) / 10007.0

def cell_of(dm, x, y): return dm[y * 16:y * 16 + 16, x * 16:x * 16 + 16]

def compose():
    dm = np.array(Image.open(BASE).convert('RGB'))
    img = dm.copy()
    cells = {tuple(map(int, k.split(','))): v for k, v in D['cells'].items()}
    solid = np.array([[cells[(x, y)][0] != 0 for x in range(W)] for y in range(H)])
    beh = np.zeros((H, W), np.uint8)
    for (x, y), (col, el, b, r, g, bl) in cells.items():
        if b == 'MB_TALL_GRASS': beh[y, x] = MB_TALL_GRASS
    # the ground under DM's trees: its plain snow (or its plain ice, where the trees stand on the ice plateaus)
    SNOW = cell_of(dm, 0, 79).copy() if False else None
    snow_cells = [(x, y) for (x, y), v in cells.items() if v[0] == 0 and v[2] == 'MB_NORMAL' and v[3] > 230 and v[5] > 230]
    ice_cells = [(x, y) for (x, y), v in cells.items() if v[0] == 0 and v[2] == 'MB_MOUNTAIN_TOP']
    # (the plainest of each: the cell closest to that kind's median picture)
    def plain(cs):
        st = np.stack([cell_of(dm, x, y).astype(int) for x, y in cs]); med = np.median(st, 0)
        return st[np.argmin(((st - med) ** 2).sum((1, 2, 3)))].astype(np.uint8)
    SNOW, ICE = plain(snow_cells), plain(ice_cells)
    def greens(x, y):
        c = cell_of(dm, x, y).astype(int); return int(((c[..., 1] - c[..., 0] > 20) & (c[..., 1] >= c[..., 2] - 10)).sum())
    tree = {(x, y) for (x, y), v in cells.items() if v[0] != 0 and (v[4] - v[5] > 5 or greens(x, y) >= 24)}   # (a pine's snowy top too)
    def nearest_ground_kind(x, y):
        for r in range(1, 8):
            for n in ((x, y + r), (x - r, y), (x + r, y), (x, y - r)):
                v = cells.get(n)
                if v and v[0] == 0 and n not in tree: return v[2]
        return 'MB_NORMAL'
    def ice_bg(x, y):                                       # (what DM drew round its tree: light-blue ice or white snow)
        c = cell_of(dm, x, y).astype(int)
        blue = ((c[..., 2] - c[..., 0] > 30) & (c.sum(-1) > 450)).sum(); white = (c.min(-1) > 230).sum()
        return blue > white
    def corner_ice(x, y):                                  # (DM's ground at the cell's top corners: ice or snow)
        c = cell_of(dm, x, y).astype(int); k = np.concatenate([c[:3, :3].reshape(-1, 3), c[:3, -3:].reshape(-1, 3)])
        return ((k[:, 2] - k[:, 0] > 30) & (k.sum(-1) > 450)).mean() > 0.5
    base = {(x, y) for (x, y) in tree if cells[(x, y)][2] == 'MB_MOUNTAIN_TOP'}
    on_ice = base | {(x, y) for (x, y) in tree if (x, y + 1) in base}                       # (a pine's top over its foot)
    on_ice |= {(x, y) for (x, y) in tree if corner_ice(x, y) and cells[(x, y)][2] != 'MB_MOUNTAIN_TOP' and
               any(cells.get(n, [1, 0, ''])[2] == 'MB_MOUNTAIN_TOP' for n in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)))}
    tree |= DOJO
    for x in range(W):                                              # (the top edge closed: pinewood)
        if not solid[0, x]: tree |= {(x, 0)}
    plain_snow = {(x, y) for (x, y) in snow_cells if min(cells[(x, y)][3:6]) > 225 and max(cells[(x, y)][3:6]) - min(cells[(x, y)][3:6]) < 20}
    plain_ice = {(x, y) for (x, y) in ice_cells if not (cells[(x, y)][4] - cells[(x, y)][3] > 10)}
    def ground_near(x, y, pool, default):
        for r in range(1, 12):                                  # (the nearest plain ground of that kind: DM's own texture)
            for n in ((x - r, y), (x + r, y), (x, y - r), (x, y + r)):
                if n in pool: return cell_of(dm, *n)
        return default
    for (x, y) in tree:
        img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = ground_near(x, y, plain_ice, ICE) if (x, y) in on_ice else SNOW if (x, y) in DOJO else ground_near(x, y, plain_snow, SNOW)
        solid[y, x] = True; beh[y, x] = 0
    # Route 13's pinewood over them: big pines staggered, small pines, rocks in the gaps (whole trees only)
    used = set()
    snowcols = {tuple(c) for m in (0xed, 0xee) for c in mm.full('ef', m).reshape(-1, 3)}   # (Elderflower's snow: never drawn on DM's)
    from scipy.ndimage import label
    def place(rows, x, y):
        pc = mm.cut_ids('ef', rows, EFG)
        hh, ww = len(pc), len(pc[0])
        big = np.zeros((hh * 16, ww * 16, 3), np.uint8); keep = np.zeros((hh * 16, ww * 16), bool)
        for dy, r in enumerate(pc):
            for dx, p in enumerate(r):
                if p is not None: big[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16] = p[0]; keep[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16] = p[1]
        for dy in range(hh):
            for dx in range(ww):
                if pc[dy][dx] is None: continue
                a = keep[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16]; rgb = big[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16]
                reg = img[(y + dy) * 16:(y + dy) * 16 + 16, (x + dx) * 16:(x + dx) * 16 + 16]; reg[a] = rgb[a]
                used.add((x + dx, y + dy))
    for (x, y) in sorted(tree, key=lambda c: (c[1], c[0])):
        if (x + y * 3) % 2 == 0 and all((x + i, y + j) in tree and (x + i, y + j) not in used for i in (0, 1) for j in (0, 1, 2)):
            place(BIG, x, y)
    for (x, y) in sorted(tree, key=lambda c: (c[1], c[0])):
        if (x, y) in used: continue
        if (x, y + 1) in tree and (x, y + 1) not in used: place(SMALL, x, y)
        else: place(ROCK, x, y)                                         # (no bare cells in a wood: they read as ground)
    # trees standing on DM's ice: Elderflower's plain snow left round them (its two commonest colours) shows the ice
    from scipy.ndimage import label as _label
    t0 = mm.full('ef', 0xed).reshape(-1, 3); cols_, cnt_ = np.unique(t0, axis=0, return_counts=True)
    efsnow = {tuple(c) for c in cols_[np.argsort(-cnt_)[:2]]}     # (its plain snow's two colours only)
    for (x, y) in on_ice:
        reg = img[y * 16:y * 16 + 16, x * 16:x * 16 + 16]
        icec = ground_near(x, y, plain_ice, ICE)
        sn = np.array([[tuple(c) in efsnow for c in row] for row in reg])
        lb, n = _label(sn)                                          # (the snow round the tree: it reaches the cell's
        edge = set(lb[0]) | set(lb[:, 0]) | set(lb[:, -1]); edge.discard(0)   #  top or sides; the tree's own snow does not)
        for k in edge: reg[lb == k] = icec[lb == k]
    # DM's little green shrubs on open ground: gone (Route 13's woods have none); its plain ground under them
    for (x, y), (col, el, b, r, g, bl) in cells.items():
        if col == 0 and g - bl > 5 and g - r > 10 and b != 'MB_TALL_GRASS' and (x, y) not in tree:
            fill = ICE if b == 'MB_MOUNTAIN_TOP' else SNOW
            for n in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1), (x - 2, y), (x + 2, y)):   # (the ground beside it)
                v = cells.get(n)
                if v and v[0] == 0 and v[2] == b and not (v[4] - v[5] > 5 and v[4] - v[3] > 10):
                    fill = cell_of(dm, *n); break
            img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = fill
    # DM's pine tops peeking over its cliffs (green in rock cells): the ice they stand on instead
    for (x, y), (col, el, b, r, g, bl) in cells.items():
        if col != 0 and (x, y) not in tree:
            reg = img[y * 16:y * 16 + 16, x * 16:x * 16 + 16]; rr = reg.astype(int)
            gm = (rr[..., 1] - rr[..., 0] > 20) & (rr[..., 1] >= rr[..., 2] - 10)
            if not gm.any(): continue
            from scipy.ndimage import binary_dilation                     # (a pine's tip: its green and the snow on it)
            gm = gm | (binary_dilation(gm, iterations=2) & (rr.sum(-1) > 600))
            for dx in (1, -1, 2, -2, 3, -3):                   # (the rock beside it, same pixel: the band's texture runs on)
                n = (x + dx, y)
                if n in cells and cells[n][0] != 0 and n not in tree:
                    nb = dm[y * 16:y * 16 + 16, n[0] * 16:n[0] * 16 + 16].astype(int)
                    if not ((nb[..., 1] - nb[..., 0] > 20) & (nb[..., 1] >= nb[..., 2] - 10)).any():
                        reg[gm] = nb[gm]; break
            else: reg[gm] = ICE[gm]
    # its tall grass: Route 13's ice grass, on DM's snow
    grass = mm.cut_ids('ef', [[0xf0]], EFG)[0][0]
    for y in range(H):
        for x in range(W):
            if beh[y, x] == MB_TALL_GRASS:
                reg = img[y * 16:y * 16 + 16, x * 16:x * 16 + 16]; reg[:] = SNOW
                if grass: reg[grass[1]] = grass[0][grass[1]]
    # the lower cave mouth into B1F: rock (DM's own cliff, from the cells beside it)
    for (x, y) in LOWER_MOUTH:
        for d in (-1, 1, -2, 2, -3, 3, -4, 4, -5, 5, -6, 6):      # (the nearest plain cliff of the same band row)
            n = (x + d, y); v = cells.get(n)
            if v and v[0] == 1 and n not in tree and n not in LOWER_MOUTH and v[2] == 'MB_MOUNTAIN_TOP' and v[5] - v[3] > 40: break
        img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cell_of(dm, *n); solid[y, x] = True; beh[y, x] = 0
    # the drilling machine: gone; the band and the ice beside it carry on (DM's own cells, and their collision)
    for (x, y) in DRILL:
        n = (14, y); img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cell_of(dm, *n); solid[y, x] = cells[n][0] != 0; beh[y, x] = 0
    # the ladder hole: Dreamstone Mysteries' own (its 1F's ladder at (38, 45)), cut from its cave floor onto the ice
    one = np.array(Image.open(os.path.join(REPO, 'assets', 'mt_mirroh_reference', 'dm_1f.png')).convert('RGB'))
    lad = cell_of(one, 38, 45).astype(int); flo = cell_of(one, 37, 45).astype(int)
    m = (np.abs(lad - flo).sum(-1) > 24)
    from scipy.ndimage import binary_fill_holes
    m = binary_fill_holes(m)
    x, y = SECRET; reg = img[y * 16:y * 16 + 16, x * 16:x * 16 + 16]; reg[m] = lad[m]
    return img, solid, beh

def reach(solid, start):
    from collections import deque
    seen = {start}; q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n = (x + dx, y + dy)
            if 0 <= n[0] < W and 0 <= n[1] < H and n not in seen and not solid[n[1], n[0]]: seen.add(n); q.append(n)
    return seen

def main(out):
    img, solid, beh = compose()
    R0 = reach(solid, (38, H - 1))
    print('cave mouth reached', any((CAVE[0] + dx, CAVE[1] + dy) in R0 for dx in (-1, 0, 1) for dy in (0, 1)), '| cells reached', len(R0))
    Image.fromarray(img).save(out)
    np.savez_compressed(out.replace('.png', '.npz'), solid=solid, beh=beh)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/mt_ext_v1.png')
