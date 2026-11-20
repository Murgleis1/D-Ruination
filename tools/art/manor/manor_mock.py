"""Mock of Cadmus's grand manor (Pelluca; built but locked for now) (user design 2026-11-19).

User brief: two floors; built but locked; Water heraldry, the Jousteel crest and a grand dining hall; a building of
its own (not joined to the lab). Skinned in Pokemon Crown's two-level manor (map group 4 #0; credit: Blah and the
Crown team, used with permission): one map with the upper floor as a gallery behind the lower floor's wall and a
staircase up through it, the way Crown builds its manors (and the Academy hall builds its floors).

Ground floor: the grand dining hall. Crown's stone hearth in the middle of the wall, its two banners in Water
sea blue; the long dining table (Crown's manor table lengthened by its middle columns; two gold candelabras on it)
on a big rug (Water navy with gold, user; maroon with RUG=maroon), one plain chair at each head facing the table, centred
on it (user: no side chairs); against the left wall the Jousteel crest as a stone statue on a fluted plinth (user:
a portrait looked artificial), mirroring the staircase on the right (its runner in the rugs' navy, user); a bookcase in the left
corner, the grandfather clock in the right; maroon banners; a side table, a jug and a coat stand by the door.
Upper floor: Cadmus's private rooms: his bed and dresser on the left, a sea-blue Water banner over his writing
desk (the archive desk, walnut) with his armchair (light violet, user) behind it on a navy rug in the middle, the archive shelves (walnut, as in his Academy office) in a study corner on the right.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/manor/manor_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'crown')); sys.path.insert(0, os.path.join(ROOT, 'tools', 'art', 'academy'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'art', 'academy', 'rooms'))
from crown_pieces import map_layout, TS, cell_layers
import compose_mock as HALL
from office_mock import walnut
from classroom_mock import MAROON_MAT

ASSETS = os.path.join(ROOT, 'assets')
JOUSTEEL = os.path.join(ROOT, 'codebase', 'graphics', 'pokemon', 'jousteel', 'front.png')
TSG = TS(map_layout(4, 0))
UPPER = 4                        # the upper floor's rows (user: room for a proper desk and chair up there)
LW = 2 + UPPER                   # the lower wall's top row
W, H = 22, LW + 11               # x0, x21 void; rows 0-1 upper wall, 2..LW-1 upper floor, LW..LW+2 lower wall, then 7 floor rows, the mat
FLOOR, WALL_TOP, WALL, TRIM, SHADE = 0x01, 0x27, 0x2F, 0x72, 0x93
SCONCE, WINDOW = (0x44, 0x77), 0x7B
HEARTH = ((0x280, 0x5E, 0x52, 0x53, 0x5E, 0x281),
          (0x288, 0x282, 0x5A, 0x5B, 0x282, 0x289),
          (0x290, 0x55, 0x62, 0x63, 0x55, 0x291))
STAIRS = ((0x73, 0x6C, 0x6D, 0x73), (WALL, 0x7C, 0x7D, WALL), (SHADE, 0x74, 0x75, 0x92))
BOOKCASE = ((0x20, 0x21), (0xC0, 0x29)); CLOCK = (0x17, 0x1F)
BED = ((0xCC, 0xC9, 0xC9, 0xD4), (0xD0, 0xD1, 0xD1, 0xD2)); DRESSER = (0x13, 0x1B)
TABLE = ((0x30, 0x32, 0x31), (0x38, 0x3A, 0x39)); CHAIR_L, CHAIR_R = 0x28A, 0x28B   # Crown's plain head chairs
SIDE_TABLE = (0x7E, 0x47, 0x3B, 0x4F); JUG, COAT = 0x3D, 0x1D; MAT = (0xC4, 0xC5)
HEARTH_X, TABLE_X, TABLE_LEN, STAIRS_X = 8, 7, 8, 16
WATER_BANNER = {(160, 64, 104): (52, 96, 168)}
MAROON = {(200, 88, 80): (118, 36, 48), (160, 64, 96): (84, 22, 34), (184, 176, 168): (196, 162, 104),
          (160, 144, 128): (150, 118, 80)}
MAROON_UP = {(216, 112, 104): (118, 36, 48), (200, 88, 80): (96, 26, 40), (160, 64, 104): (84, 22, 34),   # the classroom's
             (104, 56, 88): (64, 18, 28), (208, 216, 104): (196, 162, 104), (192, 160, 56): (186, 150, 100)}  # runner table
NAVY = {(200, 88, 80): (36, 56, 104), (160, 64, 96): (24, 36, 72), (184, 176, 168): (196, 162, 104),
        (160, 144, 128): (150, 118, 80)}
RUG = MAROON if os.environ.get('RUG') == 'maroon' else NAVY        # the dining rug: Water navy (user), or maroon
STAIR_RUNNER = {(168, 112, 200): (36, 56, 104), (136, 88, 168): (24, 36, 72), (96, 88, 152): (16, 24, 52)}   # the rugs' navy (user)
HALL_WATER = {(96, 112, 88): (28, 56, 112), (136, 152, 104): (52, 96, 168), (208, 208, 176): (200, 224, 240)}

def recolour(img, table):
    out = img.copy()
    for a, b in table.items(): out[(img == a).all(-1)] = b
    return out

def cell(m): return TSG.meta(m).copy()
def rug_base(m): return cell_layers(TSG, m)[0][0].copy()       # a cell's bottom layer (the rug under a chair)
def top_on(m, base):
    (_, _), (top, tm) = cell_layers(TSG, m); out = base.copy(); out[tm] = top[tm]; return out

STONE = [(40, 40, 48), (72, 72, 80), (104, 92, 96), (120, 104, 104), (152, 134, 134), (184, 160, 160)]  # the bust's stone
JOUSTEEL_OW = os.path.join(ROOT, 'codebase', 'graphics', 'pokemon', 'jousteel', 'overworld.png')
STATUE_AT = (3, LW)                   # (x, y) of the statue's top-left cell; the plinth below. Against the left wall,
                                       # mirroring the staircase on the right (user)

def statue():
    """Jousteel's overworld sprite (the project's own; its first frame, facing down) turned to stone: its colours ranked
    by brightness and spread over the stone ramp of Crown's library bust, the outline kept dark. 32 x 32."""
    j = Image.open(JOUSTEEL_OW); a = np.array(j.convert('RGB'))[:, :32]; idx = np.array(j)[:, :32]; m = idx != 0
    lum = a @ np.array([0.30, 0.59, 0.11]); out = np.zeros_like(a)
    vals = sorted(np.unique(lum[m])); rest = vals[1:]                 # the darkest is the outline
    out[(lum == vals[0]) & m] = STONE[0]
    for i, v in enumerate(rest):                                     # the rest by rank, spread over the ramp
        out[(lum == v) & m] = STONE[1 + i * (len(STONE) - 1) // len(rest)]
    return out, m

def plinth():
    """A fluted stone plinth for the statue (32 x 16), in the bust pedestal's stone: a cap, the fluted body, a foot."""
    D, K, M, L = STONE[0], STONE[1], STONE[3], STONE[5]; S = STONE[4]
    img = np.zeros((16, 32, 3), np.uint8); m = np.zeros((16, 32), bool)
    def box(y0, y1, x0, x1, c): img[y0:y1, x0:x1] = c; m[y0:y1, x0:x1] = True
    box(0, 4, 1, 31, D); box(1, 2, 2, 30, L); box(2, 3, 2, 30, S)                   # the cap: its top face, its edge
    box(4, 12, 4, 28, D); box(4, 12, 5, 27, M)                                       # the body
    for x in range(7, 26, 4): box(5, 11, x, x + 1, K); box(5, 11, x + 1, x + 2, S)  # fluting
    box(4, 5, 5, 27, K)                                                              # the cap's shadow
    box(12, 16, 2, 30, D); box(13, 14, 3, 29, L); box(14, 15, 3, 29, M)             # the foot
    return img, m

def candelabra():
    """The gold candelabra off the Old HQ table (MonoMyth), its cloth dropped."""
    t = np.array(Image.open(os.path.join(ASSETS, 'monomyth_reference', 'pieces', 'candelabra_table.png')).convert('RGBA'))[:17]
    rgb, m = t[..., :3], t[..., 3] > 0
    cloth = np.zeros(m.shape, bool); cloth[10:] = True
    for c in ((248, 248, 248), (224, 232, 232), (184, 192, 200), (120, 120, 128), (80, 80, 104)): m &= ~(cloth & (rgb == c).all(-1))
    return rgb, m

PAINTINGS = os.path.join(ASSETS, 'monomyth_reference', 'pieces')
# North Edelweiss museum paintings (MonoMyth; tools/monomyth/mm_paintings.py), recoloured to be Cadmus's own (user):
# the starry night's gold swirls and stars turned sea-foam (a starry sea, for the Water house), the portrait's
# orange ground turned the Academy maroon
PAINT_RECOLOUR = {'starry': {(232, 192, 88): (120, 208, 200), (224, 208, 136): (184, 236, 228), (208, 176, 112): (88, 168, 176),
                             (200, 160, 96): (64, 136, 160), (248, 248, 248): (232, 248, 244)},
                  'harbour': {(232, 144, 56): (152, 62, 70), (168, 120, 80): (118, 36, 48), (168, 96, 40): (84, 22, 34),
                              (200, 160, 96): (176, 92, 96), (208, 176, 112): (196, 120, 116), (224, 208, 136): (220, 168, 150)}}

def painting(name):
    """(rgb, mask) of a museum painting, its name plaque cut off, its canvas (inside the 3-px frame) recoloured."""
    a = np.array(Image.open(os.path.join(PAINTINGS, 'painting_%s.png' % name)).convert('RGBA')); m = a[..., 3] > 0
    w = a.shape[1]; bottom = next(y for y in range(4, a.shape[0]) if m[y].sum() < w - 4)
    rgb, m = a[:bottom, :, :3].copy(), m[:bottom]
    canvas = np.zeros(m.shape, bool); canvas[3:-3, 3:-3] = True
    for c, n in PAINT_RECOLOUR.get(name, {}).items(): rgb[canvas & (a[:bottom, :, :3] == c).all(-1)] = n
    return rgb, m

ROYAL_CHAIR = {(152, 152, 168): (216, 204, 236), (128, 136, 144): (188, 172, 220), (104, 112, 120): (160, 144, 200),
               (72, 72, 88): (112, 96, 156), (56, 56, 64): (64, 52, 96), (72, 72, 72): (24, 36, 72)}   # calm light violet
                                                                                               # (user); last: its shadow
def royal_chair():
    """MonoMyth's study armchair (front view) re-upholstered in a calm light violet (user): Cadmus's seat behind his desk."""
    a = np.array(Image.open(os.path.join(PAINTINGS, 'study_armchair.png')).convert('RGBA')); rgb = a[..., :3].copy()
    for c in {tuple(v) for v in rgb[a[..., 3] > 0].tolist()}:
        if c in ROYAL_CHAIR: rgb[(a[..., :3] == c).all(-1)] = ROYAL_CHAIR[c]
    return rgb, a[..., 3] > 0

def ornate_rug(x0, x1, y0, y1, table):
    """Crown's dining rug (corner ornaments, border, plain field) at any size, recoloured."""
    plain = rug_base(CHAIR_L)
    def one(x, y):
        top, bot = y == y0, y == y1
        if x == x0: m = 0x78 if top else 0x88 if bot else 0x90
        elif x == x1: m = 0x7A if top else 0xE4 if bot else 0x84
        elif x == x0 + 1 and (top or bot): m = 0x79 if top else 0x91
        elif x == x1 - 1 and (top or bot): m = 0xA1 if top else 0x89
        elif top: m = 0x98
        elif bot: m = 0x99
        else: return recolour(plain, table)
        return recolour(cell(m), table)
    return one

def compose():
    img = np.zeros((H * 16, W * 16, 3), np.uint8); solid = set()
    def put(x, y, c): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = c
    def paste(rgb, m, px, py): sub = img[py:py + rgb.shape[0], px:px + rgb.shape[1]]; sub[m] = rgb[m]
    # --- the upper floor: Cadmus's rooms
    for x in range(1, W - 1):
        put(x, 0, cell(WALL_TOP)); put(x, 1, cell(WALL))
        for y in range(2, LW): put(x, y, cell(FLOOR))
    for x in (6, 13, 19): put(x, 0, cell(SCONCE[0])); put(x + 1, 0, cell(SCONCE[1]))
    for dy, row in enumerate(BED):
        for dx, m in enumerate(row): put(2 + dx, 2 + dy, cell(m)); solid.add((2 + dx, 2 + dy))
    put(7, 1, cell(DRESSER[0])); put(7, 2, cell(DRESSER[1])); solid.add((7, 2))
    for name, cx in (('starry', 4 * 16), ('harbour', 18 * 16)):   # over the bed; over the stairhead between the shelves
        p, pm = painting(name); paste(p, pm, cx - p.shape[1] // 2, 6)
    rug = ornate_rug(8, 13, 2, LW - 1, NAVY)                   # the study: a Water-navy rug 
    for y in range(2, LW):
        for x in range(8, 14): put(x, y, rug(x, y))
    b, bm = HALL.decor_piece('heraldic_banner.png', HALL_WATER); paste(b[:28], bm[:28], 11 * 16 - b.shape[1] // 2, 1)
    c, cm = royal_chair(); paste(c, cm, 11 * 16 - 16, 2 * 16 - 4)
    d = np.array(Image.open(os.path.join(PAINTINGS, 'arch_desk_clean.png')).convert('RGBA'))
    paste(walnut(d[..., :3]), d[..., 3] > 0, 11 * 16 - 16, 3 * 16 + 4); solid |= {(x, y) for x in (10, 11) for y in (2, 3, 4)}
    shelf = np.array(Image.open(os.path.join(PAINTINGS, 'arch_shelf.png')).convert('RGBA'))
    for x0 in (15, 20 - 1):
        paste(walnut(shelf[..., :3]), shelf[..., 3] > 0, x0 * 16, 16); solid |= {(x0, 2), (x0 + 1, 2)}
    # --- the lower wall: hearth with the crest, bookcase, banners, the stairs, the clock
    for x in range(1, W - 1): put(x, LW, cell(TRIM)); put(x, LW + 1, cell(WALL)); put(x, LW + 2, cell(SHADE))
    for dy in range(2):
        for dx in range(2): put(1 + dx, LW + 1 + dy, cell(BOOKCASE[dy][dx]))
    for x in (6, 14): put(x, LW, top_on(0x5E, cell(TRIM)))        # the Academy's maroon banners (Crown's own colour)
    for dy, row in enumerate(HEARTH):
        for dx, m in enumerate(row):
            c = cell(m)
            if m == 0x5E: c = recolour(c, WATER_BANNER)
            put(HEARTH_X + dx, LW + dy, c)
    solid |= {(HEARTH_X + dx, LW + 2) for dx in range(6)}
    for dy, row in enumerate(STAIRS):
        for dx, m in enumerate(row): put(STAIRS_X + dx, LW + dy, recolour(cell(m), STAIR_RUNNER))
    put(20, LW + 1, cell(CLOCK[0])); put(20, LW + 2, cell(CLOCK[1]))
    # --- the dining hall
    for x in range(1, W - 1):
        for y in range(LW + 3, H - 1): put(x, y, cell(FLOOR))
    rx0, rx1, ry0, ry1 = TABLE_X - 2, TABLE_X + TABLE_LEN + 1, LW + 4, LW + 7   # the rug: two past each head
    plain = rug_base(CHAIR_L)
    def rug(x, y):
        top, bot = y == ry0, y == ry1
        if x == rx0: m = 0x78 if top else 0x88 if bot else 0x90
        elif x == rx1: m = 0x7A if top else 0xE4 if bot else 0x84
        elif x == rx0 + 1 and (top or bot): m = 0x79 if top else 0x91
        elif x == rx1 - 1 and (top or bot): m = 0xA1 if top else 0x89
        elif top: m = 0x98
        elif bot: m = 0x99
        else: return plain.copy()
        return cell(m)
    for y in range(ry0, ry1 + 1):
        for x in range(rx0, rx1 + 1): put(x, y, recolour(rug(x, y), RUG))
    for dy, row in enumerate(TABLE):                           # 30 32.. 31 / 38 3a.. 39 on the rug
        for dx in range(TABLE_LEN):
            m = row[0] if dx == 0 else row[1]
            c = top_on(m, plain)
            if dx == TABLE_LEN - 1: c = top_on(row[0], plain[:, ::-1])[:, ::-1]   # the left end mirrored: Crown's
            x, y = TABLE_X + dx, LW + 5 + dy; put(x, y, recolour(c, RUG)); solid.add((x, y))  # right end carries a jar
    cd, cdm = candelabra()
    for k in (2, 5): paste(cd, cdm, (TABLE_X + k) * 16 + 16 - cd.shape[1] // 2, (LW + 5) * 16 - 4)
    for x, m in ((TABLE_X - 1, CHAIR_L), (TABLE_X + TABLE_LEN, CHAIR_R)):   # one plain chair at each head, facing the
        (_, _), (ct, ctm) = cell_layers(TSG, m)                              # table, centred on its two rows (user)
        paste(ct, ctm, x * 16, (LW + 5) * 16 + 8); solid |= {(x, LW + 5), (x, LW + 6)}
    for y, m in zip(range(LW + 4, LW + 8), SIDE_TABLE): put(20, y, top_on(m, cell(FLOOR))); solid.add((20, y))
    sx, sy = STATUE_AT; pr, pm = plinth(); paste(pr, pm, sx * 16, (sy + 2) * 16)
    st, stm = statue(); paste(st, stm, sx * 16, (sy + 2) * 16 - 31)
    solid |= {(sx, sy + 2), (sx + 1, sy + 2)}
    put(1, LW + 8, top_on(JUG, cell(FLOOR))); put(1, LW + 9, top_on(COAT, cell(FLOOR))); solid |= {(1, LW + 8), (1, LW + 9)}
    put(10, H - 1, recolour(cell(MAT[0]), MAROON_MAT)); put(11, H - 1, recolour(cell(MAT[1]), MAROON_MAT))
    return img, solid

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/manor/manor_mock.png'
    img, _ = compose(); Image.fromarray(img).resize((W * 32, H * 32), 0).save(out); print(out)
