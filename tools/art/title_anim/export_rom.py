"""Export the approved title animation to ROM assets.
Layers (all 8bpp, one shared tile set at char base 0; tile 0 = blank):
  BG3  tail (front)            map @ screenblock 29, 6x6 tile window at tile (6,11); pose tiles swapped at runtime
  BG0  static scene + logo     map @ 28; sky pixels transparent; tail area = repainted background;
                               logo white fill -> palette 128+band (glint), other white -> 66
  BG1/BG2 sky strip 512x48     map @ 30-31 (512x256), alpha-blended one pixel apart
Outputs into OUT (codebase/graphics/title_screen) + a generated C header."""
import numpy as np, pickle, sys, os, math
from PIL import Image
from tail_rig import TAIL
OUT = sys.argv[1]; HDR = sys.argv[2]
im = Image.open('dr_title.png'); a = np.array(im).astype(np.int32)
pal = np.array(im.getpalette()[:768]).reshape(256, 3).astype(np.int32)
for k, r, g, b in np.load('sky_newcols.npy'): pal[k] = (r, g, b)
WHITE_IDX, BAND0 = 66, 128
pal[WHITE_IDX] = (248, 248, 248)
sky_mask = np.load('mask_sky2.npy'); bgf = np.load('bg_filled_tail.npy'); strip = np.load('sky_strip512_light.npy')
logo = np.load('mask_logo_full.npy'); fill = logo & (a == 0)
# --- BG0 (static) --------------------------------------------------------------------------------------
fg = a.copy(); fg[TAIL] = bgf[TAIL]
fy, fx = np.nonzero(fill); U = fx + fy; UMIN, UMAX = int(U.min()), int(U.max())
band = (U - UMIN) // 3; NB = int(band.max()) + 1
assert BAND0 + NB <= 256
fg[fill] = BAND0 + band
fg[(fg == 0) & ~fill] = WHITE_IDX                      # any other white must not be transparent
for b in range(NB): pal[BAND0 + b] = (248, 248, 248)
fg[:48][sky_mask[:48]] = 0                            # sky shows through
assert (strip != 0).all(), 'sky strip must be fully opaque'
# --- tile set ---------------------------------------------------------------------------------------------
tiles = [np.zeros((8, 8), np.uint8)]; index = {tiles[0].tobytes(): 0}
def tid(t):
    k = t.tobytes()
    if k not in index: index[k] = len(tiles); tiles.append(t.copy())
    return index[k]
fgmap = np.zeros((32, 32), np.uint16)
for ty_ in range(20):
    for tx_ in range(30): fgmap[ty_, tx_] = tid(fg[ty_ * 8:ty_ * 8 + 8, tx_ * 8:tx_ * 8 + 8].astype(np.uint8))
skymap = np.zeros((32, 64), np.uint16)
for ty_ in range(6):
    for tx_ in range(64): skymap[ty_, tx_] = tid(strip[ty_ * 8:ty_ * 8 + 8, tx_ * 8:tx_ * 8 + 8].astype(np.uint8))
TAIL_TX, TAIL_TY, TW = 6, 11, 6
TAIL_BASE = len(tiles)
tailmap = np.zeros((32, 32), np.uint16)
for r in range(TW):
    for c in range(TW): tailmap[TAIL_TY + r, TAIL_TX + c] = TAIL_BASE + r * TW + c
for _ in range(TW * TW): tiles.append(np.zeros((8, 8), np.uint8))
NT = len(tiles)
print('tiles: fg+sky unique %d, tail slots %d, total %d (limit 896)' % (TAIL_BASE, TW * TW, NT))
assert NT <= 896
# --- tail poses -------------------------------------------------------------------------------------------
poses, seq = pickle.load(open('tail_poses_l10_idle.pkl', 'rb'))
X0, Y0 = TAIL_TX * 8, TAIL_TY * 8
pose_img = np.zeros((48 * len(poses), 48), np.uint8)
for i, o in enumerate(poses):
    for (x, y), v in o.items():
        assert X0 <= x < X0 + 48 and Y0 <= y < Y0 + 48, (x, y)
        pose_img[i * 48 + (y - Y0), x - X0] = v
# rest pose over the static scene must reproduce the original title exactly (outside sky/logo changes)
comp = fg.copy(); comp[Y0:Y0 + 48, X0:X0 + 48][pose_img[:48] > 0] = pose_img[:48][pose_img[:48] > 0]
chk = (~(np.zeros_like(fill)) & ~fill); chk[:48][sky_mask[:48]] = False
diff = (comp != a) & chk & ~((comp == WHITE_IDX) & (a == 0))
print('rest composite differs from original at', int(diff.sum()), 'pixels (outside sky/logo)')
# --- write files ----------------------------------------------------------------------------------------
def save_p(arr, path):
    p = Image.fromarray(arr.astype(np.uint8), 'P'); p.putpalette([int(v) for v in pal.ravel()]); p.save(path)
cols = 16; rows = (NT + cols - 1) // cols
sheet = np.zeros((rows * 8, cols * 8), np.uint8)
for i, t in enumerate(tiles): sheet[(i // cols) * 8:(i // cols) * 8 + 8, (i % cols) * 8:(i % cols) * 8 + 8] = t
save_p(sheet, os.path.join(OUT, 'dr_title_anim_tiles.png'))
save_p(pose_img, os.path.join(OUT, 'dr_title_tail_poses.png'))
fgmap.astype('<u2').tofile(os.path.join(OUT, 'dr_title_anim_fg.bin'))
np.concatenate([skymap[:, :32].ravel(), skymap[:, 32:].ravel()]).astype('<u2').tofile(os.path.join(OUT, 'dr_title_anim_sky.bin'))
tailmap.astype('<u2').tofile(os.path.join(OUT, 'dr_title_anim_tail.bin'))
# --- glint colour table (same profile as the approved preview) -----------------------------------------
def prof(d): return max(max(0.0, 1 - abs(d) / 7) ** 0.8, max(0.0, 1 - abs(d + 16) / 3.5) ** 0.8)
W5, G5 = np.array([31, 31, 31]), np.array([31, 28, 21])
DMIN, DMAX = -20, 7
glint = []
for d in range(DMIN, DMAX + 1):
    k = prof(d); c = np.round(W5 * (1 - k) + G5 * k).astype(int); glint.append(int(c[0] | (c[1] << 5) | (c[2] << 10)))
with open(HDR, 'w') as h:
    h.write('// Generated by tools/art/title_anim/export_rom.py -- do not edit by hand.\n')
    h.write('#define TITLE_TAIL_TILE_BASE %d\n#define TITLE_TAIL_TILES %d\n' % (TAIL_BASE, TW * TW))
    h.write('#define TITLE_GLINT_PAL_BASE %d\n#define TITLE_GLINT_BANDS %d\n#define TITLE_GLINT_UMIN %d\n#define TITLE_GLINT_UMAX %d\n' % (BAND0, NB, UMIN, UMAX))
    h.write('#define TITLE_GLINT_DMIN (%d)\n#define TITLE_GLINT_DMAX %d\n' % (DMIN, DMAX))
    h.write('static const u16 sTitleGlintColors[] = {' + ', '.join('0x%04X' % c for c in glint) + '};\n')
    h.write('static const u16 sTitleTailSeq[][2] = {\n' + ''.join('    {%d, %d},\n' % (p, n) for p, n in seq) + '};\n')
print('glint bands', NB, 'U', UMIN, UMAX, '| tail sequence entries', len(seq), 'loop %d frames' % sum(n for _, n in seq))
