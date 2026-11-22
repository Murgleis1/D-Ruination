"""Mirroh's interiors (step 4, user 2026-11-21): each room lifted from a source hack's interior as a picture
plus its collision, recoloured and edited for Mirroh, then built with tools/art/mapbuild.py as a map of its own.

Rooms (user choices 2026-11-21):
  tavern    Pelluca's Seaside Tavern (MonoMyth's Elderflower tavern), recoloured to Mirroh's colder palette
  chapel    Crown's church nave (Crown map 6.2), restoned in Mirroh's stone, the runner in copper
  langerin  House Langerin's reception hall: MonoMyth's Elderflower long hall (0x86B260), copper banners
  shop      the specialty shop (rare held items, the Egg salesman): Crown's stocked room (map 7.5, its right room)
  townhouse a wealthier home: MonoMyth's Elderflower study (0x86B2D0)
  cottage   a home: Crown's herbalist room (map 18.1)
  snowy     a home: MonoMyth's Elderflower room (0x86B1F0), the source of the snowy house's outside too

Credits: Crown (Blah and the Crown team, used with permission), MonoMyth (permission pending before release).
Usage: python3 tools/art/mirroh/interiors.py sheet   (the source rooms with their collision, for cropping)
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
C = os.path.join(REPO, 'codebase')
CROWN_ROM = '/home/claude/crown/Crown.gba'

def _crown(group, num):
    os.environ.setdefault('ODYSSEY_ROM', CROWN_ROM)
    sys.path.insert(0, os.path.join(REPO, 'tools', 'crown')); sys.path.insert(0, os.path.join(REPO, 'tools', 'odyssey'))
    import crown_pieces as CP
    from frrender import render, map_cells
    L = CP.map_layout(group, num); img = np.asarray(render(L).convert('RGB') if hasattr(render(L), 'convert') else render(L))
    cells = np.array(map_cells(L), np.uint16).reshape(L['h'], L['w'])
    return img[..., :3].copy(), ((cells >> 10) & 3) != 0

def _monomyth(header):
    sys.path.insert(0, os.path.join(REPO, 'tools', 'monomyth'))
    import render as R, romlib as RL
    L = RL.layout(RL.u32(header)); ts = R.TS(L); W, H = L['w'], L['h']          # (header: a ROM offset)
    cells = np.array(R.map_cells(L), np.uint16).reshape(H, W)
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = ts.meta(int(cells[y, x]) & 0x3FF)
    return img, ((cells >> 10) & 3) != 0

def _ours(map_name):
    sys.path.insert(0, os.path.join(REPO, 'tools', 'art'))
    import render_built as RB, json
    p = '/tmp/_ours_%s.png' % map_name; RB.main(map_name, p)
    mj = json.load(open(os.path.join(C, 'data/maps', map_name, 'map.json')))
    L = [l for l in json.load(open(os.path.join(C, 'data/layouts/layouts.json')))['layouts'] if l.get('id') == mj['layout']][0]
    g = np.fromfile(os.path.join(C, L['blockdata_filepath']), '<u2').reshape(L['height'], L['width'])
    return np.asarray(Image.open(p).convert('RGB')).copy(), ((g >> 10) & 3) != 0

SOURCES = {
    'tavern': lambda: _ours('PellucaCityPokemonCenter'),
    'chapel': lambda: _crown(6, 2),
    'langerin': lambda: _monomyth(0x86B260),
    'shop': lambda: _crown(7, 5),
    'townhouse': lambda: _monomyth(0x86B2D0),
    'cottage': lambda: _crown(18, 1),
    'snowy': lambda: _monomyth(0x86B1F0),
}

# ------------------------------------------------------------------ colours
WOOD = {(72, 64, 64): (62, 44, 34), (152, 136, 128): (176, 132, 88), (128, 96, 96): (142, 96, 58),
        (104, 80, 88): (104, 68, 44), (168, 152, 144): (198, 158, 110), (104, 80, 80): (114, 76, 48),
        (88, 72, 72): (78, 52, 34)}          # (Pelluca's import: MonoMyth's mauve wood -> warm oak, import_interior.py)
COPPER = [(44, 22, 20), (74, 36, 26), (112, 58, 36), (150, 82, 48), (186, 112, 66), (222, 160, 108)]   # (Kimaris's)
STONE = [(34, 34, 42), (58, 58, 68), (84, 84, 94), (112, 110, 118), (142, 138, 142), (176, 170, 170), (206, 200, 198)]

def lum(c): return 0.30 * c[0] + 0.59 * c[1] + 0.11 * c[2]

def ramp_map(img, colours, ramp, lo=None, hi=None):
    """Each listed colour to a ramp by its lightness (the darkest listed to the ramp's foot, the lightest to its top)."""
    out = img.copy(); ls = [lum(c) for c in colours]; lo = min(ls) if lo is None else lo; hi = max(ls) if hi is None else hi
    for c, l in zip(colours, ls):
        t = 0 if hi == lo else (l - lo) / (hi - lo); r = ramp[int(round(t * (len(ramp) - 1)))]
        out[(img == np.array(c, np.uint8)).all(-1)] = r
    return out

def exact_map(img, table):
    out = img.copy()
    for a, b in table.items(): out[(img == np.array(a, np.uint8)).all(-1)] = b
    return out

def colder(img, keep=None, k=0.5, dark=0.86):
    """Mirroh's colder interior: warm browns pulled toward a cold grey of their own lightness and darkened
    (keep: a mask left as it is, e.g. a fire)."""
    f = img.astype(float); l = (f @ [0.30, 0.59, 0.11])[..., None]
    cold = l * np.array([0.92, 0.96, 1.08])
    warm = (f[..., 0] > f[..., 2] + 12)[..., None]
    out = np.where(warm, (f * (1 - k) + cold * k) * dark, f)
    if keep is not None: out[keep] = f[keep]
    return np.clip(out, 0, 255).astype(np.uint8)

def ramp_colours(colours, ramp):
    """The ramp colour each of these colours takes by its lightness (as ramp_map)."""
    ls = [lum(c) for c in colours]; lo, hi = min(ls), max(ls)
    return [ramp[int(round((0 if hi == lo else (l - lo) / (hi - lo)) * (len(ramp) - 1)))] for l in ls]

def region_map(img, cells, table):
    """exact_map only inside a block of cells (x0, y0, x1, y1), for colours the rest of the room shares."""
    x0, y0, x1, y1 = cells; out = img.copy()
    out[y0 * 16:(y1 + 1) * 16, x0 * 16:(x1 + 1) * 16] = exact_map(img[y0 * 16:(y1 + 1) * 16, x0 * 16:(x1 + 1) * 16], table)
    return out

WALNUT = {(142, 96, 58): (104, 62, 42), (114, 76, 48): (84, 48, 34), (78, 52, 34): (56, 32, 26), (104, 68, 44): (74, 42, 30),
          (62, 44, 34): (44, 26, 22), (176, 132, 88): (140, 92, 64), (198, 158, 110): (168, 120, 86)}   # (Pelluca's oak, darker)

def crop(img, solid, x0, y0, x1, y1):
    return img[y0 * 16:(y1 + 1) * 16, x0 * 16:(x1 + 1) * 16].copy(), solid[y0:y1 + 1, x0:x1 + 1].copy()

def paste_cells(dst, src, sx, sy, w, h, dx, dy):
    dst[dy * 16:(dy + h) * 16, dx * 16:(dx + w) * 16] = src[sy * 16:(sy + h) * 16, sx * 16:(sx + w) * 16]

def banner():
    """House Langerin's copper banner (16x32 RGBA), lifted off Kimaris's chamber's back wall by its copper."""
    sys.path.insert(0, os.path.join(REPO, 'tools', 'art')); import render_built as RB
    RB.main('KimarisChamber', '/tmp/_kim.png'); k = np.asarray(Image.open('/tmp/_kim.png').convert('RGB'))
    cell = k[0:32, 96:112].astype(int)
    cop = np.array(COPPER); d = np.abs(cell[:, :, None, :] - cop[None, None]).sum(-1).min(-1)
    m = d < 40
    from scipy.ndimage import binary_fill_holes, binary_closing
    m = binary_fill_holes(binary_closing(m, np.ones((3, 3), bool)))
    out = np.zeros((32, 16, 4), np.uint8); out[..., :3] = cell; out[..., 3] = np.where(m, 255, 0); return out

BED = os.path.join(REPO, 'assets', 'crown_reference', 'pieces', 'bed_inn.png')
# (Crown's inn, map 7.8, its bed at (5, 4-5): crown_pieces.cut(7, 8, 4, 4, 3, 2, full=floor 676), trimmed to its frame)

def floor_from(img, solid, cells, src):
    """Clear furniture off cells: each (x, y) takes the floor of src(x, y) (a cell with the same plank/tile phase)."""
    for (x, y) in cells:
        sx, sy = src(x, y); paste_cells(img, img.copy(), sx, sy, 1, 1, x, y); solid[y, x] = False

def bed(img, solid, px, cy):
    """A bed (user 2026-11-22: homes need beds), head up, its frame's left edge at pixel px, rows cy..cy+1; the cells
    it covers solid."""
    b = np.asarray(Image.open(BED).convert('RGBA'))
    put(img, b, px, cy * 16)
    for x in range(px // 16, (px + b.shape[1] - 1) // 16 + 1): solid[cy:cy + 2, x] = True

def put(dst, rgba, px, py):
    h, w = rgba.shape[:2]; a = rgba[..., 3] > 0
    dst[py:py + h, px:px + w][a] = rgba[..., :3][a]

# ------------------------------------------------------------------ the rooms: (image, solid, exits)
def room_tavern():
    img, solid = SOURCES['tavern']()
    fire = np.zeros(img.shape[:2], bool); fire[2 * 16 + 2:3 * 16, 5 * 16 + 1:6 * 16 - 1] = True   # (its fire stays warm)
    return colder(img, keep=fire), solid, [(6, 10), (7, 10)]

CH_FLOOR = [(176, 128, 112), (152, 136, 104), (152, 104, 88), (200, 168, 144), (128, 112, 80), (104, 96, 80),
            (120, 120, 96), (176, 160, 128), (88, 80, 64), (96, 96, 72), (168, 144, 120), (152, 88, 88), (128, 72, 72)]
CH_RUNNER = [(192, 80, 80), (208, 104, 96)]   # ((128,72,72) is the floor's outline too: stone)
CH_CUSHION = [(104, 56, 80), (152, 64, 96)]
def room_chapel():
    img, solid = SOURCES['chapel'](); img, solid = crop(img, solid, 0, 0, 16, 20)
    img = ramp_map(img, CH_FLOOR, STONE[1:])
    img = ramp_map(img, CH_RUNNER, COPPER[3:5])                    # (the runner: mid copper, its highlight above)
    img = ramp_map(img, CH_CUSHION, COPPER[:3])
    return img, solid, [(7, 19), (8, 19), (9, 19)]

def room_langerin():
    img, solid = SOURCES['langerin'](); img = exact_map(img, WOOD)
    tav, tsol = SOURCES['tavern']()
    paste_cells(img, tav, 4, 0, 3, 3, 4, 0)                         # the hearth (the Tavern's), lit
    solid[0:3, 4:7] = True
    b = banner()
    for x in (3, 7): put(img, b, x * 16, 0)                          # Langerin's copper banners either side of it
    floor = [(142, 96, 58), (114, 76, 48), (78, 52, 34), (176, 132, 88), (104, 68, 44), (198, 158, 110), (62, 44, 34)]
    img = exact_map(img, {c: tuple(int(v * 0.72) for v in c) for c in floor})   # (a darker, stately oak)
    return img, solid, [(4, 16), (5, 16), (6, 16)]

def move_mat(img, solid, row, to_row, dx_px=0):
    """The exit mat off the black below the floor onto the floor's bottom row (user 2026-11-22 review: in the Crown rooms
    it sat out on the black, where the other rooms lay it on the floor). Its pixels (the non-black ones in its row)
    move up, shifted dx_px across; the row it leaves is black and solid."""
    strip = img[row * 16:row * 16 + 16].copy(); m = strip.any(-1)
    img[row * 16:row * 16 + 16] = 0; solid[row, :] = True
    ys, xs = np.nonzero(m); dst = img[to_row * 16:to_row * 16 + 16]
    dst[ys, xs + dx_px] = strip[ys, xs]

def counter(img, solid, x0, y, w, wood=None):
    """A free-standing run of the Mirroh Tavern's bar, w cells at row y from x0: its end piece at both ends (the left
    one mirrored), its plain middle between, and its lip (the shadow under the front edge) on the row below. The
    cells are solid; build_interiors marks them MB_COUNTER, so a keeper behind it is spoken to across it."""
    tav, _ = room_tavern()[:2]
    cell = lambda cx, cy: tav[cy * 16:cy * 16 + 16, cx * 16:cx * 16 + 16]
    end, mid, bg = cell(12, 4).astype(int), cell(6, 4), cell(13, 4).astype(int)
    keep = np.abs(end - bg).sum(-1).max(0) > 24                          # (the end piece's counter columns, not its floor)
    lip = cell(7, 5)[:5].copy()
    if wood:                                                         # (in the room's own wood, by lightness)
        cols = sorted({tuple(int(v) for v in c) for a in (end[:, keep], mid, lip) for c in np.asarray(a).reshape(-1, 3)}, key=lum)
        tab = dict(zip(cols, [tuple(c) for c in ramp_colours(cols, wood)]))
        end, mid, lip = (exact_map(np.asarray(a, np.uint8), tab).astype(int) for a in (end, mid, lip))
    for i in range(w):
        x = x0 + i; c = img[y * 16:y * 16 + 16, x * 16:x * 16 + 16]
        if i == w - 1: c[:, keep] = end[:, keep]
        elif i == 0: c[:, keep[::-1]] = end[:, ::-1][:, keep[::-1]]
        else: c[:] = mid
        img[(y + 1) * 16:(y + 1) * 16 + 5, x * 16:x * 16 + 16] = lip
        solid[y, x] = True

def room_shop():
    img, solid = SOURCES['shop'](); img, solid = crop(img, solid, 18, 5, 29, 14)
    img = region_map(img, (4, 4, 8, 6), {(104, 56, 88): COPPER[1], (160, 64, 104): COPPER[2], (200, 88, 80): COPPER[3],
                                        (216, 112, 104): COPPER[4]})     # (its rug in copper; user 2026-11-21)
    # the counters for the specialty shop's two keepers (stage 2: the dealer, the Egg salesman), runs of the Tavern's
    # bar in place of the two writing desks: the dealer's at row 4 (x 1-3, he stands at row 3), the Egg salesman's at
    # row 3 (x 8-10, he stands at row 2); the desks' floor laid back first (the marble's own phase)
    d = img[4 * 16:6 * 16, 1 * 16:4 * 16].reshape(-1, 3)              # (the desks' wood, warm browns, for the counters)
    wood = sorted({tuple(int(v) for v in c) for c in d if int(c[0]) > int(c[1]) > int(c[2]) and int(c[0]) - int(c[2]) > 40}, key=lum)
    floor_from(img, solid, [(x, y) for x in (1, 2, 3) for y in (4, 5)], lambda x, y: (x, 6 if y == 4 else 3))
    floor_from(img, solid, [(x, y) for x in (9, 10) for y in (2, 3)], lambda x, y: (3 if x % 2 else 2, 3 if y == 3 else 5))
    counter(img, solid, 1, 4, 3, wood); counter(img, solid, 8, 3, 3, wood)
    paste_cells(img, img.copy(), 10, 7, 1, 2, 4, 2); solid[2:4, 4] = True   # (a bust closes the way round behind the dealer)
    move_mat(img, solid, 9, 8)                                       # (onto the floor, between the candelabra)
    return img, solid, [(6, 8)]

def room_townhouse():
    # (user 2026-11-21: make it unlike the snowy house inside) the wealthier home: a lit hearth on the back wall in
    # place of the sofa, the rug under the big table in copper, the whole room in dark walnut
    img, solid = SOURCES['townhouse'](); img = exact_map(img, WOOD); img, solid = crop(img, solid, 5, 4, 19, 14)
    tav, _ = SOURCES['tavern'](); paste_cells(img, tav, 4, 0, 3, 3, 7, 0); solid[0:3, 7:10] = True
    floor_from(img, solid, [(x, y) for x in (1, 2, 3) for y in (5, 6)], lambda x, y: (3 if x % 2 else 2, 8 + y % 2))   # (same plank phase)
    bed(img, solid, 17, 5)                                           # (the bed, against the left wall)
    rug = sorted({tuple(int(v) for v in c) for c in img[4 * 16 + 8:8 * 16 - 8, 4 * 16 + 8:8 * 16 - 8].reshape(-1, 3)
                  if abs(int(c[0]) - int(c[2])) < 30 and int(c[2]) >= int(c[0])}, key=lum)    # (its greys, not the oak)
    img = region_map(img, (4, 4, 7, 7), dict(zip(rug, [tuple(c) for c in ramp_colours(rug, COPPER[1:5])])))
    img = exact_map(img, WALNUT)
    return img, solid, [(10 - 5, 13 - 4)]

def room_cottage():
    img, solid = SOURCES['cottage'](); img, solid = crop(img, solid, 1, 0, 12, 8)
    floor_from(img, solid, [(4, 5), (4, 6), (6, 5), (6, 6)], lambda x, y: (2, y))   # (no candelabra; user 2026-11-22)
    bed(img, solid, 17, 4)                                           # (the bed, against the left wall)
    move_mat(img, solid, 7, 6)
    return img, solid, [(5, 6)]

def room_snowy():
    img, solid = SOURCES['snowy'](); img = exact_map(img, WOOD)
    bed(img, solid, 10 * 16 - 2 - 24, 5)                            # (the bed on the open right side, flush to its wall,
                                                                     #  clear of the desk's stool; user 2026-11-22)
    solid[:, 0] = True; solid[:, -1] = True                          # (the walls' edges: never walkable)
    return img, solid, [(5, 9)]

ROOMS = {'tavern': room_tavern, 'chapel': room_chapel, 'langerin': room_langerin, 'shop': room_shop,
         'townhouse': room_townhouse, 'cottage': room_cottage, 'snowy': room_snowy}

def mock(out):
    ims = []
    for k, f in ROOMS.items():
        img, solid, ex = f(); im = Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), Image.NEAREST)
        d = ImageDraw.Draw(im, 'RGBA')
        for (x, y) in ex: d.rectangle((x * 32 + 4, y * 32 + 4, x * 32 + 27, y * 32 + 27), outline=(80, 255, 80, 200), width=2)
        ims.append((k, im))
    Wd = 2000; x = y = rh = 0; pos = []
    for k, im in ims:
        if x + im.width > Wd: x = 0; y += rh + 20; rh = 0
        pos.append((k, im, x, y)); x += im.width + 14; rh = max(rh, im.height)
    S = Image.new('RGB', (Wd, y + rh + 20), (24, 24, 24)); d = ImageDraw.Draw(S)
    for k, im, x, y in pos: S.paste(im, (x, y + 16)); d.text((x, y), k, fill=(255, 255, 255))
    S.save(out)

def overlay(img, solid, scale=2):
    H, W = solid.shape
    im = Image.fromarray(img).resize((W * 16 * scale, H * 16 * scale), Image.NEAREST); d = ImageDraw.Draw(im, 'RGBA')
    c = 16 * scale
    for y in range(H):
        for x in range(W):
            if solid[y, x]: d.rectangle((x * c + 2, y * c + 2, x * c + c - 3, y * c + c - 3), outline=(255, 40, 40, 150))
    for x in range(W): d.text((x * c + 2, 0), str(x), fill=(255, 255, 0))
    for y in range(H): d.text((0, y * c + 2), str(y), fill=(0, 255, 255))
    return im

def sheet(out):
    ims = []
    for k, f in SOURCES.items():
        img, solid = f(); print(k, solid.shape[::-1]); ims.append((k, overlay(img, solid)))
    Wd = 2200; x = y = rh = 0; pos = []
    for k, im in ims:
        if x + im.width > Wd: x = 0; y += rh + 18; rh = 0
        pos.append((k, im, x, y)); x += im.width + 12; rh = max(rh, im.height)
    S = Image.new('RGB', (Wd, y + rh + 18), (24, 24, 24)); d = ImageDraw.Draw(S)
    for k, im, x, y in pos: S.paste(im, (x, y + 14)); d.text((x, y), k, fill=(255, 255, 255))
    S.save(out)

if __name__ == '__main__':
    if sys.argv[1:2] == ['sheet']: sheet(sys.argv[2] if len(sys.argv) > 2 else '/home/claude/scratch/mirint/sources.png')
    if sys.argv[1:2] == ['mock']: mock(sys.argv[2] if len(sys.argv) > 2 else '/home/claude/scratch/mirint/mock.png')
