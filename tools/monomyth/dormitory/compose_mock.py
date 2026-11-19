"""(user-approved 2026-11-19) Mock the Pelluca dormitory (1F common room, 2F hallway, Osrid's room) from real MonoMyth metatiles:
saloon (Speedwell, recoloured), apartment door (South Edelweiss), pedestal lectern (Wood Avens)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE)); sys.path.insert(0, HERE)
import numpy as np
from render import TS
from PIL import Image, ImageDraw
from headers import load
H, names = load()
def ts_of(a):
    return TS([h for h in H if h['addr'] + 0x08000000 == a][0]['layout'])
SAL, APT, WA = ts_of(0x886a39c), ts_of(0x886a188), ts_of(0x886acb0)
RECOLOUR = {
 4: {10: (176, 132, 88), 2: (150, 106, 66), 3: (120, 80, 50), 11: (168, 124, 80),
     6: (190, 156, 116), 7: (208, 178, 138), 8: (172, 138, 100), 4: (176, 140, 98), 5: (110, 74, 48), 12: (138, 98, 62)},
 3: {1: (156, 108, 66), 3: (92, 60, 36), 5: (120, 80, 48), 6: (176, 132, 86), 11: (170, 128, 92)}}
for s, m in RECOLOUR.items():
    for i, c in m.items(): SAL.pal[s][i] = c
DOOR_RECOLOUR = {2: (72, 48, 32), 7: (200, 160, 112), 10: (168, 124, 84), 4: (136, 96, 60)}
WALL_RECOLOUR = {3: (236, 222, 190), 9: (212, 188, 150), 6: (200, 182, 150), 4: (110, 84, 62), 2: (72, 48, 32)}
for i, c in WALL_RECOLOUR.items(): APT.pal[1][i] = c
for i, c in DOOR_RECOLOUR.items(): APT.pal[3][i] = c

def wa_floor():
    t = [WA.tile(i) for i in (130, 131, 146, 147)]
    img = np.zeros((16, 16, 3), np.uint8)
    for q, tt in enumerate(t):
        oy, ox = (q // 2) * 8, (q % 2) * 8
        img[oy:oy+8, ox:ox+8] = np.array(WA.pal[2], np.uint8)[tt]
    return img
def lectern(part, under):
    """Wood Avens pedestal over one of our metatiles: pixels that differ from the WA floor are the pedestal."""
    src = WA.meta({0: 106, 1: 122}[part]); fl = wa_floor(); out = SAL.meta(under).copy()
    m = np.abs(src.astype(int) - fl).sum(-1) > 0; out[m] = src[m]; return out
def mat(under):
    """South Edelweiss doormat (metatile 189) laid on one of our floor metatiles."""
    src, fl = APT.meta(189), APT.meta(279); out = SAL.meta(under).copy()
    m = np.abs(src.astype(int) - fl).sum(-1) > 0; out[m] = src[m]; return out
def lift(mid, old_bg, new_bg):
    """A saloon object lifted off the wall piece it was drawn on (old_bg) onto our wall (new_bg)."""
    src, old = SAL.meta(mid), SAL.meta(old_bg); out = M(*new_bg).copy()
    m = np.abs(src.astype(int) - old).sum(-1) > 0; out[m] = src[m]; return out
def M(src, mid):
    if src == 'P': return lift(mid, 168, ('a', 177))
    if src == 'Q': return lift(mid, 160, ('a', 184))
    if src == 'R': return lift(mid, 153, ('s', 155))
    if src == 'T': return lift(mid, 154, ('s', 155))
    if src == 'L': return lectern(*mid)
    if src == 'm': return mat(mid)
    return {'s': SAL, 'a': APT, 'w': WA}[src].meta(mid)
VOID = np.zeros((16, 16, 3), np.uint8)
PLAIN = True
def plain(rows):
    """The approved wall/floor treatment: apartment wall instead of the saloon's panelling and plaster,
    one even oak floor (no baked-in wall-shadow strips). Objects keep their art; only their background
    layer changes ('P' onto the lower wall, 'Q' onto the upper wall, 'R'/'T' onto plain floor)."""
    def fix(c, y):
        if c in (('s', 168), ('s', 240), ('s', 161)): return ('a', 177)
        if c == ('s', 160): return ('a', 184)
        if c in (('s', 153), ('s', 248), ('s', 163)) and y == 3: return ('s', 155)
        if c is not None and c[0] == 's' and y == 4 and c[1] in (162, 231, 179): return ('T', c[1])
        if c is not None and c[0] == 's' and y >= 3 and c[1] in (175, 184, 186): return ('R', c[1])
        if c in (('s', 153), ('s', 154)) and y >= 4: return ('s', 155)
        if c is not None and c[0] == 's' and y >= 4 and c[1] in (232, 233, 234): return ('R', c[1])
        if c is not None and c[0] == 's' and y == 3 and c[1] in (224, 225, 226, 189, 190, 191, 208, 210): return ('R', c[1])
        if c is not None and c[0] == 's' and c[1] in (221, 222, 223, 227, 228): return ('Q', c[1])
        if c is not None and c[0] == 's' and c[1] in (216, 217, 218, 181, 182, 183, 200, 202): return ('P', c[1])
        return c
    return [[fix(c, y) for c in r] for y, r in enumerate(rows)]
def grid(rows):
    """rows: list of lists of (src, id) or None."""
    if PLAIN: rows = plain(rows)
    h, w = len(rows), max(len(r) for r in rows)
    img = np.zeros((h * 16, w * 16, 3), np.uint8)
    for y, r in enumerate(rows):
        for x, c in enumerate(r):
            img[y*16:y*16+16, x*16:x*16+16] = VOID if c is None else M(*c)
    return img

SALOON = [  # rows 9..23 of the Speedwell saloon (the ground floor), 19 wide
 [192,193,194,247,247,247,247,247,247,247,247,254,152,152,152,152,152,152,152],
 [227,185,228,160,160,160,160,160,221,222,223,160,160,160,160,160,160,160,160],
 [200,201,202,240,168,168,161,168,181,182,183,168,161,168,168,168,168,168,240],
 [208,209,210,248,153,153,163,153,189,190,191,175,163,153,153,153,153,153,248],
 [153,154,154,154,154,231,177,162,162,179,162,162,178,231,154,154,154,154,154],
 [153,155,155,155,155,155,169,170,170,187,170,170,171,155,155,155,155,155,155],
 [153,155,155,155,155,155,155,215,155,215,155,215,155,155,156,157,157,157,158],
 [153,155,155,155,155,155,155,155,155,155,155,155,155,155,164,197,198,199,166],
 [153,167,176,159,155,155,155,155,155,155,167,176,159,155,164,205,206,207,235],
 [175,155,155,155,155,167,176,159,155,155,155,155,155,155,164,165,239,165,166],
 [153,155,155,155,155,155,155,155,155,155,155,155,155,155,164,165,165,165,166],
 [153,167,176,159,155,155,155,155,155,155,167,176,159,155,172,173,173,173,174],
 [153,155,155,155,155,195,155,155,155,155,155,155,155,155,155,155,195,155,155],
 [153,155,155,155,155,203,155,155,196,204,212,155,155,155,155,155,203,155,155],
 [  0,  0,  0,  0,  0,  0,  0,  0,211,214,213,  0,  0,  0,  0,  0,  0,  0,  0]]

DOORS_1F = (4, 13, 17)          # Osrid's door first
DOORS_2F = (4, 9, 14, 19)
def floor1():
    g = [[('s', v) if v else None for v in r] for r in SALOON]
    # back-wall doors (wall face row 2): Osrid's is the one by the stairs (user 2026-11-19), two locked
    # student rooms spread out to the east
    for x in DOORS_1F: g[2][x] = ('a', 289); g[3][x] = ('m', 155)
    # small speaking stage: 5 wide x 4 tall in the south-east corner, a pedestal lectern in the middle
    for y in range(6, 12):
        for x in range(14, 19): g[y][x] = ('s', 155)
    stage = [[156,157,157,157,158],[164,165,165,165,166],[164,165,165,165,166],[172,173,173,173,174]]
    for dy, r in enumerate(stage):
        for dx, v in enumerate(r): g[8 + dy][14 + dx] = ('s', v)
    g[9][15] = ('L', (1, 165))                  # the pedestal is one metatile; the speaker stands east of it, facing the chairs
    g[11][18] = ('s', 155)
    # audience benches facing the stage (west of it), replacing the two right-hand dining sets
    for y in (8, 11):
        for x in (10, 11, 12): g[y][x] = ('s', 155)
    for y in (8, 9, 10, 11):                     # two columns of chairs facing east, toward the speaker
        g[y][11] = ('s', 167); g[y][12] = ('s', 167)
    return g

def floor2():
    W = 22
    top = [('s', 152)] * W
    band = [('s', 160)] * W
    face = [('s', 240)] + [('s', 168)] * (W - 2) + [('s', 240)]
    base = [('s', 248)] + [('s', 153)] * (W - 2) + [('s', 248)]
    fl = lambda: [('s', 153)] + [('s', 155)] * (W - 1)
    g = [top, band, face, base, fl(), fl(), fl()]
    for x in DOORS_2F: g[2][x] = ('a', 289); g[3][x] = ('m', 155)
    g[4][3] = ('s', 203)                          # a plant by the stairs
    # stairs down at the west end (the top of the saloon staircase)
    g[4][0], g[4][1], g[4][2] = ('s', 184), ('s', 155), ('s', 186)
    g[5][0], g[5][1], g[5][2] = ('s', 192), ('s', 193), ('s', 194)
    g[6][0], g[6][1], g[6][2] = ('s', 227), ('s', 185), ('s', 228)
    return g

def osrid_room():
    W = 11
    g = [[('s', 152)] * W, [('s', 160)] * W,
         [('s', 240)] + [('s', 168)] * (W - 2) + [('s', 240)],
         [('s', 248)] + [('s', 153)] * (W - 2) + [('s', 248)]]
    for _ in range(4): g.append([('s', 153)] + [('s', 155)] * (W - 1))
    bed = [[216, 217, 218], [224, 225, 226], [232, 233, 234]]
    for dy, r in enumerate(bed):
        for dx, v in enumerate(r): g[2 + dy][1 + dx] = ('s', v)
    for dx, v in enumerate((181, 182, 183)): g[2][5 + dx] = ('s', v)      # bookshelf
    g[3][5], g[3][6], g[3][7] = ('s', 189), ('s', 190), ('s', 191)
    for dx, v in enumerate((181, 182, 183)): g[2][5 + dx] = ('s', v)
    g[4][9] = ('s', 203)                                                   # plant in the corner
    g[5][6], g[5][7], g[5][8] = ('s', 167), ('s', 176), ('s', 159)        # writing table and two chairs
    g.append([('s', 153)] + [('s', 155)] * (W - 1))
    g[8][4], g[8][5], g[8][6] = ('s', 196), ('s', 204), ('s', 212)        # the way out (saloon entrance)
    g.append([None] * 4 + [('s', 211), ('s', 214), ('s', 213)] + [None] * 4)
    return g

if __name__ == '__main__':
    a, b, c = grid(floor1()), grid(floor2()), grid(osrid_room())
    pad = 16
    Wd = a.shape[1] + pad + max(b.shape[1], c.shape[1]); Hd = max(a.shape[0], b.shape[0] + c.shape[0] + pad) + 20
    S = Image.new('RGB', (Wd, Hd), (28, 28, 28)); d = ImageDraw.Draw(S)
    S.paste(Image.fromarray(a), (0, 20)); d.text((2, 4), 'Dormitory 1F: common room', fill=(255, 230, 120))
    x2 = a.shape[1] + pad
    S.paste(Image.fromarray(b), (x2, 20)); d.text((x2 + 2, 4), '2F hallway', fill=(255, 230, 120))
    S.paste(Image.fromarray(c), (x2, 20 + b.shape[0] + pad)); d.text((x2 + 2, 8 + b.shape[0] + pad), "Osrid's room", fill=(255, 230, 120))
    S.resize((S.width * 2, S.height * 2), Image.NEAREST).save('/tmp/dorm_mock.png')
