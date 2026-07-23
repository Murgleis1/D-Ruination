#!/usr/bin/env python3
"""
Dreamstone Ruination - reusable tileset/sprite conversion helpers.

This library encodes the process worked out over the Pelluca/Evernahn conversion
and the Osrid sprite work. Read the docstrings before using; several of these
routines exist specifically because the naive approach was TRIED and FAILED.

Nothing here runs on import; import the functions you need.
"""
import struct
import numpy as np
from PIL import Image
from collections import Counter, OrderedDict, deque

# --------------------------------------------------------------------------
# DOWNSCALE  (32px RMXP -> 16px metatile, and hi-res art -> 64px sprite)
# --------------------------------------------------------------------------
# LOCKED FINDING: on flat pixel art use BOX or NEAREST, never a smoothing filter.
# Measured on a 9-colour source tile: BOX and NEAREST both return exactly 9
# colours; HAMMING returns 90-127; LANCZOS explodes to 117. Smoothing invents
# colours the palette budget cannot hold and destroys hard edges.
def downscale_box(rgba_tile, size=16):
    """Colour-lossless 2x downscale for flat pixel art. rgba_tile: HxWx4 uint8."""
    return np.array(Image.fromarray(rgba_tile, 'RGBA').resize((size, size), Image.BOX))

# --------------------------------------------------------------------------
# BACKGROUND KEYING  (strip a checker/solid background, keep warm mask/skin)
# --------------------------------------------------------------------------
# LOCKED FINDING: key by NEUTRALITY, not brightness. A bone-white mask (warm,
# e.g. 235,230,217) and a near-white background (neutral, R=G=B) have similar
# luminance; a brightness threshold deletes the mask along with the background.
# Test R==G==B (within tolerance) AND bright, then FLOOD FILL from the border so
# interior near-neutral pixels are not wrongly cut.
def key_background(rgb, neutral_tol=6, bright=228):
    """rgb: HxWx3 int. Returns bool opaque-mask (True = figure)."""
    H, W, _ = rgb.shape
    mx = rgb.max(2); mn = rgb.min(2)
    lum = 0.299*rgb[:,:,0] + 0.587*rgb[:,:,1] + 0.114*rgb[:,:,2]
    bgish = ((mx-mn) <= neutral_tol) & (lum >= bright)
    bg = np.zeros((H, W), bool); q = deque()
    for x in range(W):
        for y in (0, H-1):
            if bgish[y, x] and not bg[y, x]: bg[y, x] = True; q.append((y, x))
    for y in range(H):
        for x in (0, W-1):
            if bgish[y, x] and not bg[y, x]: bg[y, x] = True; q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny, nx = y+dy, x+dx
            if 0<=ny<H and 0<=nx<W and bgish[ny, nx] and not bg[ny, nx]:
                bg[ny, nx] = True; q.append((ny, nx))
    return ~bg

def largest_component(mask):
    """Keep only the biggest connected blob - drops stray specks left by keying."""
    H, W = mask.shape
    lab = np.zeros((H, W), np.int32); cur = 0; best = (0, 0)
    for sy in range(H):
        for sx in range(W):
            if mask[sy, sx] and lab[sy, sx] == 0:
                cur += 1; n = 0; dq = deque([(sy, sx)]); lab[sy, sx] = cur
                while dq:
                    y, x = dq.popleft(); n += 1
                    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny, nx = y+dy, x+dx
                        if 0<=ny<H and 0<=nx<W and mask[ny, nx] and lab[ny, nx] == 0:
                            lab[ny, nx] = cur; dq.append((ny, nx))
                if n > best[1]: best = (cur, n)
    return lab == best[0]

# --------------------------------------------------------------------------
# PALETTE RECOVERY  (merge resample noise back to the artist's real palette)
# --------------------------------------------------------------------------
# When art arrives as a resampled PNG (tens of thousands of near-duplicate
# colours) the goal is the artist's ORIGINAL ~15 colours, not a fresh
# quantisation. Merge near-duplicates by distance, then fold the rarest into
# their nearest neighbour until <= limit. Preserves hues; a re-quantise mutes them.
def recover_palette(px_rgb, tol=14, limit=15):
    """px_rgb: Nx3 uint8 opaque pixels. Returns (palette Kx3 uint8, raw_count)."""
    cnt = Counter(map(tuple, px_rgb.tolist()))
    centers = []
    for c, n in cnt.most_common():
        hit = False
        for e in centers:
            if sum((a-b)**2 for a, b in zip(c, e[0])) <= tol*tol:
                e[1] += n; hit = True; break
        if not hit: centers.append([list(c), n])
    while len(centers) > limit:
        i = min(range(len(centers)), key=lambda k: centers[k][1])
        j = min((k for k in range(len(centers)) if k != i),
                key=lambda k: sum((a-b)**2 for a, b in zip(centers[i][0], centers[k][0])))
        centers[j][1] += centers[i][1]; centers.pop(i)
    return np.array([c[0] for c in centers], np.uint8), len(cnt)

# QUANTISER CHOICE when a real quantise IS needed (source > 15 colours, no
# original palette to recover): use FASTOCTREE, not MEDIANCUT. MEDIANCUT weights
# by pixel count, so a large dark region dominates and it caps around luminance
# 128 - a bright mask and bright hair get dropped. FASTOCTREE spans the full
# luminance range and keeps them. Also exclude the near-white edge halo from the
# palette source so it doesn't waste a slot.
def quantise_fastoctree(px_rgb, colors=15, drop_halo=True):
    px = px_rgb.astype(np.uint8)
    if drop_halo:
        lum = 0.299*px[:,0] + 0.587*px[:,1] + 0.114*px[:,2]
        neutral = (px.max(1).astype(int) - px.min(1).astype(int)) <= 6
        keep = ~(neutral & (lum >= 235))
        if keep.sum() > 1000: px = px[keep]
    q = Image.fromarray(px.reshape(-1,1,3), 'RGB').quantize(colors=colors, method=Image.FASTOCTREE)
    return np.array(q.getpalette()[:colors*3], np.uint8).reshape(colors, 3)

# --------------------------------------------------------------------------
# MODE DOWNSAMPLE OF AN INDEXED IMAGE  (hi-res indexed -> 64px, no blending)
# --------------------------------------------------------------------------
# After quantising at full res, downsample by taking the MOST COMMON index per
# block, so every output pixel is a real palette colour and never an average of
# outline+fill (which produces mud). Require a block to be >= min_fill opaque to
# be drawn, so the silhouette stays clean.
def mode_downsample(idx_full, opaque_full, out_w, out_h, min_fill=0.40):
    fh, fw = idx_full.shape
    out = np.zeros((out_h, out_w), np.uint8)
    for j in range(out_h):
        ya, yb = int(j*fh/out_h), max(int(j*fh/out_h)+1, int((j+1)*fh/out_h))
        for i in range(out_w):
            xa, xb = int(i*fw/out_w), max(int(i*fw/out_w)+1, int((i+1)*fw/out_w))
            blk = idx_full[ya:yb, xa:xb].ravel()
            nz = blk[blk != 0]
            if len(nz) >= min_fill*len(blk):
                out[j, i] = Counter(nz.tolist()).most_common(1)[0][0]
    return out

# --------------------------------------------------------------------------
# HOUSE-STYLE OUTLINE  (Gen-3 trainer sprites)
# --------------------------------------------------------------------------
# Emerald trainer front pics measured: ~14-15 of 15 palette slots used, darkest
# colour is pure (0,0,0), luminance spans 0-255, silhouette edge is pure black,
# outline share 24-68%. Reserve palette index 1 = black; snap the silhouette
# edge to it. (Only apply when the source art does NOT already have a black
# outline - the user's later art did, so this was skipped for it.)
def snap_edge_to_black(idx, black_index=1):
    o = idx != 0
    edge = np.zeros_like(o)
    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        sh = np.roll(o, (dy, dx), (0, 1))
        if dy == 1: sh[0,:] = False
        if dy == -1: sh[-1,:] = False
        if dx == 1: sh[:,0] = False
        if dx == -1: sh[:,-1] = False
        edge |= o & ~sh
    idx[edge] = black_index
    return idx

# --------------------------------------------------------------------------
# BOUNDED GAP FILL  (repair a porous silhouette WITHOUT blobbing)
# --------------------------------------------------------------------------
# A single 3x3 morphological closing (dilate once, erode once) bridges gaps of
# <=2px and mathematically cannot run away. DO NOT iterate a "fill if >=N
# opaque neighbours" loop with loosening thresholds - that cascades and fills the
# whole bounding box (tried: turned a 1068px sprite into a 2847px diamond).
def close_gaps(mask):
    def dil(m):
        o = m.copy()
        for dy in (-1,0,1):
            for dx in (-1,0,1): o |= np.roll(np.roll(m, dy, 0), dx, 1)
        return o
    def ero(m):
        o = m.copy()
        for dy in (-1,0,1):
            for dx in (-1,0,1): o &= np.roll(np.roll(m, dy, 0), dx, 1)
        return o
    return ero(dil(mask))

# --------------------------------------------------------------------------
# GBA PALETTE I/O
# --------------------------------------------------------------------------
def write_gbapal(path, colors16):
    """colors16: list of 16 (r,g,b). Writes BGR555 .gbapal."""
    with open(path, 'wb') as f:
        for r, g, b in (list(colors16)+[(0,0,0)]*16)[:16]:
            f.write(struct.pack('<H', (r>>3) | ((g>>3)<<5) | ((b>>3)<<10)))

def write_jasc(path, colors16):
    with open(path, 'wb') as f:
        f.write(b'JASC-PAL\r\n0100\r\n16\r\n')
        for r, g, b in (list(colors16)+[(0,0,0)]*16)[:16]:
            f.write(('%d %d %d\r\n' % (r, g, b)).encode())

def read_gbapal(path):
    d = open(path, 'rb').read()
    return [(((v&31)<<3), (((v>>5)&31)<<3), (((v>>10)&31)<<3))
            for v in (struct.unpack_from('<H', d, 2*i)[0] for i in range(16))]

# --------------------------------------------------------------------------
# METATILE ENCODING  (pokeemerald)
# --------------------------------------------------------------------------
# A metatile is 8 u16 tile-entries (16 bytes): entries 0-3 = bottom layer,
# 4-7 = top layer (top drawn transparent over colour 0). Entry bits:
#   0-9  tileId (<512 primary, >=512 secondary-512)
#   10   xflip   11 yflip   12-15 palette slot
# metatile_attributes.bin: one u16 per metatile; bits 0-7 behaviour (MB_*),
# bits 12-13 layer type (use 1). Map cell (map.bin u16):
#   0-9 metatile_id | 10-11 collision | 12-15 elevation.
def metatile_entry(tile_id, palette, xflip=0, yflip=0):
    return struct.pack('<H', (tile_id & 0x3FF) | ((xflip&1)<<10) | ((yflip&1)<<11) | ((palette&15)<<12))

def metatile_attr(behavior, layer_type=1):
    return struct.pack('<H', (behavior & 0xFF) | ((layer_type & 3) << 12))

def split_to_tiles(idx16, tilemap):
    """Split a 16x16 index array into four 8x8 quadrant tile-ids, deduped via
    tilemap (an OrderedDict shared across all metatiles). Returns [tl,tr,bl,br]."""
    quad = []
    for qy in range(2):
        for qx in range(2):
            sub = idx16[qy*8:(qy+1)*8, qx*8:(qx+1)*8]
            key = sub.tobytes()
            if key not in tilemap: tilemap[key] = len(tilemap)
            quad.append(tilemap[key])
    return quad
