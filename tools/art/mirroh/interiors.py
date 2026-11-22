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

def room_shop():
    img, solid = SOURCES['shop'](); img, solid = crop(img, solid, 18, 5, 29, 14)
    return img, solid, [(24 - 18, 14 - 5)]

def room_townhouse():
    img, solid = SOURCES['townhouse'](); img = exact_map(img, WOOD); img, solid = crop(img, solid, 5, 4, 19, 14)
    return img, solid, [(10 - 5, 13 - 4)]

def room_cottage():
    img, solid = SOURCES['cottage'](); img, solid = crop(img, solid, 1, 0, 12, 8)
    return img, solid, [(6 - 1, 7)]

def room_snowy():
    img, solid = SOURCES['snowy'](); img = exact_map(img, WOOD)
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
