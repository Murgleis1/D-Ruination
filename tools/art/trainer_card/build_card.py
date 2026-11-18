"""Dreamstone Ruination parchment Trainer Card (layout A, approved 2026-11-18) -> ROM assets.
Outputs (OUT = codebase/graphics/trainer_card/dr):
  card_bg.png + card_bg.bin   parchment sheet, name/labels/frame/boxes baked in (4bpp tiles + 32x32 map)
  stamps.png                  9 Trial stamps, 2x2 tiles each, transparent background
  digits.png                  Jacquarda Bastarda 9 digits 0-9 and ':' in 8x16 cells
and HDR (src/data/dr_trainer_card.h): tile counts, digit advances, layout constants.
Fonts (OFL): Jacquard 12 (name), Jacquarda Bastarda 9 (labels, digits)."""
import os, sys, pickle, numpy as np
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
OUT, HDR = sys.argv[1], sys.argv[2]
FB = ImageFont.truetype(os.path.join(HERE, 'fonts/JacquardaBastarda9-Regular.ttf'), 13)
FJ = ImageFont.truetype(os.path.join(HERE, 'fonts/Jacquard12-Regular.ttf'), 21)
# ---- the one 16-colour palette (GBA 5-bit values) -----------------------------------------------
TONES = [(232, 208, 168), (216, 192, 144), (200, 168, 128), (176, 144, 104), (144, 112, 80)]
INK, INK2 = (64, 40, 24), (120, 88, 56)
STAMP_ORDER = ['Wraith', 'Smelt', 'Haywire', 'Nonpareil', 'Firmament', 'Verdant', 'Gloaming', 'Glamour', 'Upheaval']
STAMP_INK = {'Wraith': (96, 56, 128), 'Smelt': (192, 88, 32), 'Haywire': (176, 128, 16), 'Nonpareil': (112, 96, 80),
             'Firmament': (64, 112, 168), 'Verdant': (56, 120, 56), 'Gloaming': (48, 40, 88), 'Glamour': (192, 80, 128), 'Upheaval': (128, 80, 40)}
PAL = TONES + [INK, INK2] + [STAMP_INK[n] for n in STAMP_ORDER]
assert len(PAL) == 16
I_INK, I_INK2, I_STAMP0 = 5, 6, 7
# ---- parchment (same recipe as the approved mockup; deterministic) -------------------------------
rng = np.random.default_rng(7)
W, H = 240, 160
yy, xx = np.mgrid[0:H, 0:W]
edge = np.minimum.reduce([xx, yy, W - 1 - xx, H - 1 - yy]).astype(float)
shade = np.clip(1 - edge / 14, 0, 1) ** 1.6 * 46
blot = np.zeros((H, W))
for _ in range(9):
    cx, cy, r = rng.uniform(0, W), rng.uniform(0, H), rng.uniform(10, 34)
    blot += np.exp(-(((xx - cx) ** 2 + (yy - cy) ** 2) / (2 * r * r))) * rng.uniform(4, 10)
v = np.array([226, 208, 166], float)[None, None] - (shade + blot)[..., None] * np.array([1.0, 1.1, 1.3])
tones_ref = np.array([[230, 212, 170], [214, 192, 148], [196, 170, 126], [172, 144, 102], [142, 112, 76]], float)
B4 = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]) / 16 - 0.5
lum = v.mean(-1) + B4[yy % 4, xx % 4] * 14
idx = np.abs(lum[..., None] - tones_ref.mean(-1)[None, None]).argmin(-1).astype(np.uint8)
# ---- ink layer: draw in an RGB scratch then stamp ink indices ------------------------------------
L = {'name': (12, 8), 'rule': (12, 30, 150), 'labels_x': 14, 'rows_y': (38, 55, 72), 'values_right': 128,
     'frame': (158, 14, 225, 81), 'pic_tile': (20, 2), 'trials': (14, 98), 'box0': (14, 118), 'box_step': 24, 'box': 20}
def ink(draw_fn, index):
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m); d.fontmode = '1'; draw_fn(d)
    idx[np.array(m) > 0] = index
ink(lambda d: d.rectangle([5, 5, 234, 154], outline=255), I_INK2)
ink(lambda d: d.text(L['name'], 'Rainhawk Alban', font=FJ, fill=255), I_INK)
ink(lambda d: d.line([L['rule'][0], L['rule'][1], L['rule'][2], L['rule'][1]], fill=255), I_INK2)
for k, y in zip(('Money', 'PokeLog', 'Time'), L['rows_y']):
    ink(lambda d, k=k, y=y: d.text((L['labels_x'], y), k, font=FB, fill=255), I_INK)
ink(lambda d: d.rectangle(list(L['frame']), outline=255), I_INK2)
ink(lambda d: d.text(L['trials'], 'Trials', font=FB, fill=255), I_INK2)
for i in range(9):
    x = L['box0'][0] + i * L['box_step']
    ink(lambda d, x=x: d.rectangle([x, L['box0'][1], x + L['box'] - 1, L['box0'][1] + L['box'] - 1], outline=255), I_INK2)
# ---- tiles + map ----------------------------------------------------------------------------------
full = np.zeros((256, 256), np.uint8); full[:H, :W] = idx
# tile 0 must be blank: BG2 (stamps) shares this tile set and its empty cells point at tile 0
tiles, index, tmap = [np.zeros((8, 8), np.uint8)], {np.zeros((8, 8), np.uint8).tobytes(): 0}, np.zeros((32, 32), np.uint16)
for ty in range(32):
    for tx in range(32):
        t = full[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8]
        if ty >= 20 or tx >= 30: t = np.zeros((8, 8), np.uint8)
        k = t.tobytes()
        if k not in index: index[k] = len(tiles); tiles.append(t.copy())
        tmap[ty, tx] = index[k]
def save(arr, path):
    im = Image.fromarray(arr.astype(np.uint8), 'P'); im.putpalette([c for rgb in PAL for c in rgb] + [0] * (768 - 48)); im.save(path)
cols = 16; rows = (len(tiles) + cols - 1) // cols
sheet = np.zeros((rows * 8, cols * 8), np.uint8)
for i, t in enumerate(tiles): sheet[(i // cols) * 8:(i // cols) * 8 + 8, (i % cols) * 8:(i % cols) * 8 + 8] = t
save(sheet, os.path.join(OUT, 'card_bg.png')); tmap.astype('<u2').tofile(os.path.join(OUT, 'card_bg.bin'))
NBG = rows * cols                                     # tiles occupied after gbagfx (whole sheet rows)
# ---- stamps ----------------------------------------------------------------------------------------
sys.path.insert(0, HERE)
src = open(os.path.join(HERE, 'stamps_src.py')).read().split("PAPER, BOX")[0]
ns = {'np': np}; exec(src, ns)
st = np.zeros((16 * 9, 16), np.uint8)
for i, n in enumerate(STAMP_ORDER):
    st[i * 16:(i + 1) * 16][ns['stamp'](n)] = I_STAMP0 + i
save(st, os.path.join(OUT, 'stamps.png'))
# ---- digits ----------------------------------------------------------------------------------------
GLYPHS = '0123456789:'
dg = np.zeros((16, 8 * len(GLYPHS)), np.uint8); adv = []
for i, ch in enumerate(GLYPHS):
    m = Image.new('L', (8, 16), 0); d = ImageDraw.Draw(m); d.fontmode = '1'; d.text((0, 0), ch, font=FB, fill=255)
    a = np.array(m) > 0
    big = Image.new('L', (32, 32), 0); ImageDraw.Draw(big).text((0, 0), ch, font=FB, fill=255)
    assert not (np.array(big)[16:, :].any() or np.array(big)[:, 8:].any()), 'glyph %r does not fit 8x16' % ch
    dg[:, i * 8:(i + 1) * 8][a] = I_INK; adv.append(int(round(FB.getlength(ch))))
save(dg, os.path.join(OUT, 'digits.png'))
with open(HDR, 'w') as h:
    h.write('// Generated by tools/art/trainer_card/build_card.py -- do not edit.\n')
    h.write('#define DR_CARD_BG_TILES %d\n#define DR_CARD_STAMP_TILE_BASE %d\n' % (NBG, NBG))
    h.write('#define DR_CARD_VALUES_RIGHT %d\n' % L['values_right'])
    h.write('static const u8 sDrCardRowY[3] = {%s};\n' % ', '.join(str(y) for y in L['rows_y']))
    h.write('static const u8 sDrCardDigitAdvance[%d] = {%s}; // "%s"\n' % (len(GLYPHS), ', '.join(map(str, adv)), GLYPHS))
    h.write('#define DR_CARD_DIGITS_WIDTH %d\n' % (8 * len(GLYPHS)))
    h.write('#define DR_CARD_PIC_TILE_X %d\n#define DR_CARD_PIC_TILE_Y %d\n' % L['pic_tile'])
    h.write('#define DR_CARD_STAMP_TILE_X0 %d\n#define DR_CARD_STAMP_TILE_STEP %d\n#define DR_CARD_STAMP_TILE_Y %d\n' % ((L['box0'][0] + 2) // 8, L['box_step'] // 8, (L['box0'][1] + 2) // 8))
assert (L['box0'][0] + 2) % 8 == 0 and L['box_step'] % 8 == 0 and (L['box0'][1] + 2) % 8 == 0
print('bg tiles', len(tiles), 'sheet tiles', NBG, 'digit advances', adv)
