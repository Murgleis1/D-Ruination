"""(user 2026-11-19) Mock of the Templar Monastery main hall ("foyer with seating, church-esque",
between intimate and grand), entered from the holding cell's south door; the front door leads to Pelluca.

Sources:
  * MonoMyth "Old Headquarters" (map 0x886DEC8): the candelabra tables, the teal-and-gold diamond carpet,
    the stone wall (its clean pieces: no cracks, no worn diamonds, this is a living church).
  * Pokemon Rejuvenation (by the user's friends on its team): ArceusRuins sheet (pixel-doubled 32px art,
    halved exactly) for the Arceus statues, pillar statues, wheel plaques, crystals, gold medallion, doorway;
    Church sheet for the stained glass. The Church sheet arrived as a resized JPEG, so its windows here are a
    PROVISIONAL resample until the original PNG is supplied.
Image-level mock only (no tileset yet): every piece is composited as pixels.
"""
import os, sys, json
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, '/home/claude/repo/tools/monomyth')
from romlib import u32, off, layout
from render import TS, map_cells
import importlib.util as _ilu                                    # the dormitory mock (the saloon), loaded by path:
_spec = _ilu.spec_from_file_location('dorm_compose_mock', '/home/claude/repo/tools/monomyth/dormitory/compose_mock.py')
DORM = _ilu.module_from_spec(_spec); _spec.loader.exec_module(DORM)     # it shares this module's file name

UP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'assets', 'rejuvenation') + os.sep   # the user's sheets
AR = np.array(Image.open(UP + 'ArceusRuins.png').convert('RGBA'))[::2, ::2]   # ArceusRuins, halved exactly
CH = Image.open(UP + 'Church.jpg').convert('RGB')                         # Church (JPEG, provisional)
HQ_L = layout(u32(off(0x0886DEC8))); HQ = TS(HQ_L); HQ_W = HQ_L['w']; HQ_C = map_cells(HQ_L)

def hq(mid): return HQ.meta(mid).astype(np.uint8)
def lattice(x, y):
    """The Old HQ carpet: teal diamonds on (even, even), gold on (odd, odd), plain between."""
    return 0xD0 if x % 2 == 0 and y % 2 == 0 else (0xE0 if x % 2 and y % 2 else 0xC8)

# ---- a candelabra table lifted off the Old HQ carpet: pixels that differ from the carpet under it ----
TABLE_AT = (13, 8)                     # an isolated whole table in the Old HQ map (133 131 134 / 123 128 125 / 12b 12c 12d)
def table_object():
    rgb = np.zeros((48, 48, 3), np.uint8); m = np.zeros((48, 48), bool); x0, y0 = TABLE_AT
    for dy in range(3):
        for dx in range(3):
            x, y = x0 + dx, y0 + dy; src = hq(HQ_C[y * HQ_W + x] & 0x3FF); bg = hq(lattice(x, y))
            d = np.abs(src.astype(int) - bg).sum(-1) > 0
            rgb[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16] = src; m[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16] = d
    return rgb, m

# ---- the wall: Old HQ's clean stone wall, made taller for the windows (its plain middle repeated) ----
def wall_rows(W, rows):
    top = [hq(0xCE)] + [hq(0xCA)] * (W - 2) + [hq(0xCF)]
    face = [hq(0xD6)] + [hq(0xD2)] * (W - 2) + [hq(0xD7)]
    def mid(t):                                     # the face without its bottom trim: its rows 1-8 repeated
        o = t.copy(); band = t[1:9]; o[:8] = band; o[8:] = band; return o
    out = [np.hstack(top)] + [np.hstack([mid(t) for t in face])] * (rows - 2) + [np.hstack(face)]
    return np.vstack(out)

def ar(box):
    x0, y0, x1, y1 = box; a = AR[y0:y1, x0:x1]; return a[..., :3], a[..., 3] > 0
def ch_window(box, w_gba):
    """PROVISIONAL: a Church-sheet window resampled from the JPEG to GBA scale, quantized to 15 colours."""
    im = CH.crop(box); h = round(im.height * w_gba / im.width)
    im = im.resize((w_gba, h), Image.LANCZOS).quantize(15, method=Image.Quantize.MEDIANCUT).convert('RGB')
    a = np.array(im); m = (a.astype(int).sum(-1) < 720)          # drop the white sheet background
    return a, m

import colorsys
# the great window's figure: her cyan hair re-dyed gold blonde with tinges of silver (user 2026-11-19).
# Hair = the window's cyan/teal pixels; each takes a colour on a gold ramp by its brightness, and the
# brightest strands turn silver.
HAIR_RAMP = [(96, 64, 32), (144, 104, 40), (192, 148, 56), (224, 184, 88), (240, 212, 136)]
HAIR_SILVER = [(200, 204, 216), (232, 236, 244)]
HAIR_SHADES = [(120, 84, 32), (184, 140, 52), (228, 192, 96), (212, 216, 228)]   # deep gold, gold, pale gold, silver
def is_hair(c):
    h, l, s = colorsys.rgb_to_hls(*(v / 255 for v in c)); return 0.43 <= h <= 0.56 and s > 0.25
def blonde(rgb, m):
    """The window has four hair shades (after quantizing): darkest to lightest -> deep gold, gold, pale gold,
    silver (the lightest strands: the silver tinge)."""
    out = rgb.copy(); px = {tuple(int(v) for v in c) for c in rgb[m]}
    hair = sorted((c for c in px if is_hair(c)), key=lambda c: colorsys.rgb_to_hls(*(v / 255 for v in c))[1])
    ramp = HAIR_SHADES[-len(hair):] if len(hair) <= len(HAIR_SHADES) else None
    assert ramp, f'{len(hair)} hair shades'
    for c, new in zip(hair, ramp): out[(rgb == c).all(-1) & m] = new
    return out

# ---- tall iron candle stands (user 2026-11-19: replace the "gaudy" crystals) ----
# Rejuvenation's Church-sheet stand (three lit candles on dark iron), resampled from the JPEG; its muddied
# colours mapped to a clean ramp (iron, wax, flame), and the JPEG's cream halo along the stem (below the
# candles) dropped.
STAND_MAP = {(46, 43, 53): (40, 40, 56), (63, 62, 74): (64, 64, 80), (91, 89, 102): (104, 104, 120),
             (148, 103, 75): (216, 96, 32), (142, 147, 149): (168, 168, 176), (191, 157, 126): (248, 168, 56),
             (197, 178, 153): (224, 216, 200), (229, 222, 208): (248, 240, 200)}
STAND_HALO_FROM = 17                           # rows from here down are stem: light pixels there are halo
def candle_stand():
    st, sm = ch_window((112, 4758, 138, 4836), 15); out = st.copy(); m = sm.copy()
    for k, v in STAND_MAP.items(): out[(st == k).all(-1) & sm] = v
    halo = np.isin(st.reshape(-1, 3).view([('', st.dtype)] * 3), np.array([(197, 178, 153), (229, 222, 208)], st.dtype).view([('', st.dtype)] * 3)).reshape(st.shape[:2])
    m[STAND_HALO_FROM:] &= ~halo[STAND_HALO_FROM:]
    return out, m

def pew():
    """Option B: a three-tile pew seen from behind, in the saloon's warm wood (generic furniture, drawn)."""
    W = (DORM.SAL.pal[4][5], DORM.SAL.pal[4][3], DORM.SAL.pal[4][2], DORM.SAL.pal[4][10], DORM.SAL.pal[4][7])
    dk, md, mid, lt, hi = [np.array(c, np.uint8) for c in W]
    a = np.zeros((16, 48, 3), np.uint8); m = np.zeros((16, 48), bool)
    a[1:7, 1:47] = mid; a[1, 1:47] = hi; a[2, 1:47] = lt; a[6, 1:47] = md         # back rest
    a[7:11, 2:46] = lt; a[7, 2:46] = hi; a[10, 2:46] = md                          # seat
    for x in (1, 2, 45, 46): a[1:14, x] = mid                                     # end posts
    a[1:14, 1] = dk; a[1:14, 46] = dk; a[0, 1:47] = dk; a[11:14, 3:45] = 0
    for x in (6, 24, 41): a[11:14, x] = dk                                        # legs
    m[0:14, 1:47] = True; m[11:14, 3:45] = False
    for x in (6, 24, 41): m[11:14, x] = True
    a[14:16, 2:46] = (0, 0, 0); m[14:16, 2:46] = False
    return a, m

def chair():
    src = DORM.SAL.meta(175); fl = DORM.SAL.meta(155)
    return src, np.abs(src.astype(int) - fl).sum(-1) > 0

BOX = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ar_boxes.json')))   # objects in the halved ArceusRuins sheet
W, H, WALL = 17, 22, 6                   # 17 x 22 cells; the north wall is 6 rows (room for the stained glass)

def compose(seating):
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    img[:WALL * 16] = wall_rows(W, WALL)
    for y in range(WALL, H - 1):
        for x in range(W): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = hq(lattice(x, y))
    def put(rgb, m, px, py):
        h, w = m.shape; sub = img[py:py + h, px:px + w]; sub[m[:sub.shape[0], :sub.shape[1]]] = rgb[:sub.shape[0], :sub.shape[1]][m[:sub.shape[0], :sub.shape[1]]]
    # the exit at the bottom: Old HQ's mat and threshold, centred
    for dx, (a, b) in enumerate(((0x120, 0xBD), (0x121, 0xBE), (0x122, 0xBF))):
        img[(H - 2) * 16:(H - 1) * 16, (7 + dx) * 16:(8 + dx) * 16] = hq(a); img[(H - 1) * 16:H * 16, (7 + dx) * 16:(8 + dx) * 16] = hq(b)
    # stained glass: the great window centred, the two gothic lancets either side (PROVISIONAL, from the JPEG)
    g, gm = ch_window((4, 7352, 146, 7512), 80); g = blonde(g, gm); put(g, gm, 8 * 16 + 8 - 40, 4)
    l, lm = ch_window((150, 7392, 210, 7512), 32)
    put(l, lm, 3 * 16, 14); put(l, lm, 12 * 16, 14)
    # the cell door (Rejuvenation's dark doorway) in the wall west of the altar
    a, m = ar((16, 34, 33, 64)); put(a, m, 1 * 16, WALL * 16 - m.shape[0])
    # altar: Rejuvenation's white-and-blue rug as the altar cloth, the white Arceus statue on it,
    # statue-pillars flanking
    a, m = ar(BOX[11]); put(a, m, 7 * 16, WALL * 16)
    a, m = ar(BOX[5]); put(a, m, 8 * 16 + 8 - m.shape[1] // 2, WALL * 16 + 30 - m.shape[0])
    # the same tall fluted statue-pillar either side (user: they must match), the right one mirrored
    x0, y0, x1, y1 = BOX[36]; a, m = ar((x0, y0, x0 + 16, y1))
    put(a, m, 5 * 16, (WALL + 2) * 16 - m.shape[0] + 4); put(a[:, ::-1], m[:, ::-1], 11 * 16, (WALL + 2) * 16 - m.shape[0] + 4)
    # tall iron candle stands either side of the altar (they replaced the crystals: user)
    a, m = candle_stand()
    for px in (3 * 16 + 8, 12 * 16 + 8): put(a, m, px, (WALL + 2) * 16 - m.shape[0] + 2)
    # the gold medallion set in the floor before the altar
    x0, y0, x1, y1 = BOX[1]; a, m = ar((x0, y1 - 48, x1, y1)); put(a, m, 8 * 16 + 8 - 24, (WALL + 3) * 16 + 4)
    # candelabra tables down both side walls
    t, tm = table_object()
    for ty in (WALL + 3, WALL + 7, WALL + 11):
        put(t, tm, 0, ty * 16); put(t, tm, 14 * 16, ty * 16)
    # seating either side of the aisle
    for sy in range(WALL + 6, H - 3, 2):
        for sx in (4, 10):
            if seating == 'pews':
                a, m = pew(); put(a, m, sx * 16, sy * 16)
            else:
                a, m = chair()
                for k in range(3): put(a, m, (sx + k) * 16, sy * 16)
    return img

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/templar_mock'
    A, B = compose('chairs'), compose('pews')
    S = Image.new('RGB', (W * 16 * 2 + 16, H * 16 + 14), (28, 28, 28)); d = ImageDraw.Draw(S)
    S.paste(Image.fromarray(A), (0, 14)); S.paste(Image.fromarray(B), (W * 16 + 16, 14))
    d.text((2, 2), 'A: saloon chairs', fill=(255, 230, 120)); d.text((W * 16 + 18, 2), 'B: pews', fill=(255, 230, 120))
    S.resize((S.width * 2, S.height * 2), 0).save(out + '.png'); print(out + '.png')
