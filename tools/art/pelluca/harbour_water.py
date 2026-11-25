"""Pelluca Harbour's water animated with MonoMyth's own water (as the old Pelluca shore was: tools/monomyth/
cormoria_water.py), called by build_harbour.py between mapbuild's build and write.

MonoMyth's terrain primary (0x86135EA, Watercress' and Cascade's) animates a 32-tile strip, 8 frames, over its tiles
416-447; Watercress' water metatiles are the strip's 416-419 in their four quarters (0x6C pale with palette 5, 0xE0
deep with palette 0), and its quay, pier and shore pieces lay their stone and sand over the same four tiles. So in
the harbour's picture every 8x8 block of the waterfront has, under whatever lies on it, strip tile 416 + quarter as
shipped; its water pixels are the pixels equal to that tile (pale or deep, whichever matches more). Each frame
replaces those pixels with the strip's frame, in the nearest colours of the block's own palette; whatever lies over
the water stays. The animated tiles are moved to the front of each tileset (after tile 0 / at 512) so each is one run.
Writes data/tilesets/primary/pelluca_harbour_tiles/anim/water/{0..7}.png, the C (tileset_anims.c, its header's
callback), and returns the runs."""
import os, sys, re
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'monomyth'))
from romlib import ROM, u32, off, layout
from render import pals_of, tiles_of
C = os.path.normpath(os.path.join(HERE, '..', '..', '..', 'codebase'))
FRAMES, STRIP0 = 0x894DB34, 416
S = 16

def mm_tile(addr):
    a = np.frombuffer(ROM[off(addr):off(addr) + 32], np.uint8); t = np.zeros((8, 8), np.uint8)
    t[:, 0::2] = (a & 15).reshape(8, 4); t[:, 1::2] = (a >> 4).reshape(8, 4); return t
def strip():
    FR = [u32(off(FRAMES) + 4 * i) for i in range(8)]
    return [[mm_tile(FR[f] + 32 * k) for k in range(4)] for f in range(8)]

def plan(under, grid, meta, tiles, pals, rows):
    """{tile: (palette, mask in the tile's own orientation, [8 frames of rgb])} for the waterfront's blocks"""
    L = layout(u32(0x869C10)); P = pals_of(L['primary']); shipped = tiles_of(L['primary'])
    ST = strip()
    cand = {}
    for q in range(4):
        cand[q] = [(np.array(P[p], np.uint8)[shipped[STRIP0 + q]], [np.array(P[p], np.uint8)[ST[f][q]] for f in range(8)]) for p in (5, 0)]
    plan_ = {}; conflicts = 0
    H, W = grid.shape
    for y in rows:
        for x in range(W):
            m = meta[int(grid[y, x] & 0x3FF)]
            for q in range(4):
                blk = under[y * S + (q // 2) * 8:y * S + (q // 2) * 8 + 8, x * S + (q % 2) * 8:x * S + (q % 2) * 8 + 8]
                best = None
                for ship, frames in cand[q]:
                    mk = (blk == ship).all(-1)
                    if best is None or mk.sum() > best[0].sum(): best = (mk, frames)
                mk, frames = best
                if mk.sum() < 6: continue
                e = m[q]; t, xf, yf, p = e & 0x3FF, bool(e & 0x400), bool(e & 0x800), e >> 12
                def orient(a):
                    if xf: a = a[:, ::-1]
                    if yf: a = a[::-1]
                    return a
                rec = (p, orient(mk).copy(), [orient(fr).copy() for fr in frames])
                if t in plan_:
                    if plan_[t][0] != p or not (plan_[t][1] == rec[1]).all(): conflicts += 1
                    continue
                plan_[t] = rec
    return plan_, conflicts

def frames_of(plan_, tiles, pals):
    out = {}
    for t, (p, mk, frs) in plan_.items():
        P = np.array((list(pals[p]) + [(0, 0, 0)] * 16)[:16], float)
        seq = []
        for fr in frs:
            tile = tiles[t].copy()
            near = ((fr.reshape(-1, 1, 3).astype(float) - P[None, 1:]) ** 2).sum(-1).argmin(1).reshape(8, 8) + 1
            tile[mk] = near[mk]; seq.append(tile)
        out[t] = seq
    return out

def permute(b, animated):
    """animated tiles to the front of each tileset: primary from 1, secondary from 512; meta entries rewritten"""
    tiles = b['tiles']; mp = {}
    for lo, hi, start in ((1, 512, 1), (512, 1024, 512)):
        keys = sorted(k for k in tiles if lo <= k < hi)
        anim = [k for k in keys if k in animated]; rest = [k for k in keys if k not in animated]
        for i, k in enumerate(anim + rest): mp[k] = start + i
    mp[0] = 0
    b['tiles'] = {mp[k]: v for k, v in tiles.items()}
    b['meta'] = {i: [(v & ~0x3FF) | mp.get(v & 0x3FF, v & 0x3FF) if v else v for v in m] for i, m in b['meta'].items()}
    return mp

def install(b, under, rows):
    pl, conflicts = plan(under, b['grid'], b['meta'], b['tiles'], b['pals'], rows)
    fr = frames_of(pl, b['tiles'], b['pals'])
    mp = permute(b, set(fr))
    fr = {mp[t]: v for t, v in fr.items()}
    prim = sorted(t for t in fr if t < 512); sec = sorted(t for t in fr if t >= 512)
    assert prim == list(range(1, 1 + len(prim))) and sec == list(range(512, 512 + len(sec)))
    d = os.path.join(C, 'data/tilesets/primary/pelluca_harbour_tiles/anim/water'); os.makedirs(d, exist_ok=True)
    for f in range(8):
        row = np.hstack([fr[t][f] for t in prim + sec]).astype(np.uint8)
        im = Image.fromarray(row, 'P'); im.putpalette([v for i in range(16) for v in (i * 16, i * 16, i * 16)] + [0] * (768 - 48))
        im.save(os.path.join(d, '%d.png' % f))
    runs = [(1, len(prim))] + ([(512, len(sec))] if sec else [])
    print('water: %d animated tiles (primary %d, secondary %d), %d blocks skipped (shared tile, other water)' % (len(fr), len(prim), len(sec), conflicts))
    return runs

C_CODE = '''
// DR: Pelluca Harbour's water (tools/art/pelluca/harbour_water.py): MonoMyth's 8-frame terrain water over every water
// pixel of the waterfront (the open water, the basin, the water under the piers' and quay's edges and the beach's
// shore), as on the old Pelluca shore; a new frame every 32 game frames (user: slower waves).
static const u16 gTilesetAnims_PellucaHarbour_Water_Frame0[] = INCBIN_U16("data/tilesets/primary/pelluca_harbour_tiles/anim/water/0.4bpp");
static const u16 gTilesetAnims_PellucaHarbour_Water_Frame1[] = INCBIN_U16("data/tilesets/primary/pelluca_harbour_tiles/anim/water/1.4bpp");
static const u16 gTilesetAnims_PellucaHarbour_Water_Frame2[] = INCBIN_U16("data/tilesets/primary/pelluca_harbour_tiles/anim/water/2.4bpp");
static const u16 gTilesetAnims_PellucaHarbour_Water_Frame3[] = INCBIN_U16("data/tilesets/primary/pelluca_harbour_tiles/anim/water/3.4bpp");
static const u16 gTilesetAnims_PellucaHarbour_Water_Frame4[] = INCBIN_U16("data/tilesets/primary/pelluca_harbour_tiles/anim/water/4.4bpp");
static const u16 gTilesetAnims_PellucaHarbour_Water_Frame5[] = INCBIN_U16("data/tilesets/primary/pelluca_harbour_tiles/anim/water/5.4bpp");
static const u16 gTilesetAnims_PellucaHarbour_Water_Frame6[] = INCBIN_U16("data/tilesets/primary/pelluca_harbour_tiles/anim/water/6.4bpp");
static const u16 gTilesetAnims_PellucaHarbour_Water_Frame7[] = INCBIN_U16("data/tilesets/primary/pelluca_harbour_tiles/anim/water/7.4bpp");
static const u16 *const gTilesetAnims_PellucaHarbour_Water[] = {
    gTilesetAnims_PellucaHarbour_Water_Frame0, gTilesetAnims_PellucaHarbour_Water_Frame1,
    gTilesetAnims_PellucaHarbour_Water_Frame2, gTilesetAnims_PellucaHarbour_Water_Frame3,
    gTilesetAnims_PellucaHarbour_Water_Frame4, gTilesetAnims_PellucaHarbour_Water_Frame5,
    gTilesetAnims_PellucaHarbour_Water_Frame6, gTilesetAnims_PellucaHarbour_Water_Frame7,
};
static const u16 sPellucaHarbourWaterRuns[][2] = {RUNS};

static void QueueAnimTiles_PellucaHarbour_Water(u16 timer)
{
    const u8 *src = (const u8 *)gTilesetAnims_PellucaHarbour_Water[timer % ARRAY_COUNT(gTilesetAnims_PellucaHarbour_Water)];
    u32 i;

    for (i = 0; i < ARRAY_COUNT(sPellucaHarbourWaterRuns); i++)
    {
        AppendTilesetAnimToBuffer((const u16 *)src, (u16 *)(BG_VRAM + TILE_OFFSET_4BPP(sPellucaHarbourWaterRuns[i][0])), sPellucaHarbourWaterRuns[i][1] * TILE_SIZE_4BPP);
        src += sPellucaHarbourWaterRuns[i][1] * TILE_SIZE_4BPP;
    }
}

static void TilesetAnim_PellucaHarbour(u16 timer)
{
    if (timer % 32 == 0)
        QueueAnimTiles_PellucaHarbour_Water(timer / 32);
}

void InitTilesetAnim_PellucaHarbour(void)
{
    sPrimaryTilesetAnimCounter = 0;
    sPrimaryTilesetAnimCounterMax = 256;
    sPrimaryTilesetAnimCallback = TilesetAnim_PellucaHarbour;
}
// DR: end Pelluca Harbour's water
'''

def wire(runs):
    p = os.path.join(C, 'src/tileset_anims.c'); s = open(p).read()
    code = C_CODE.replace('RUNS', ', '.join('{%d, %d}' % r for r in runs))
    s = re.sub(r'\n// DR: Pelluca Harbour\'s water \(tools.*?// DR: end Pelluca Harbour\'s water\n', '\n', s, flags=re.S)
    s = s.rstrip('\n') + '\n' + code
    open(p, 'w').write(s)
    h = os.path.join(C, 'include/tileset_anims.h'); t = open(h).read()
    if 'InitTilesetAnim_PellucaHarbour' not in t:
        t = t.replace('void InitTilesetAnim_General(void);', 'void InitTilesetAnim_General(void);\nvoid InitTilesetAnim_PellucaHarbour(void);')
        open(h, 'w').write(t)
    hp = os.path.join(C, 'src/data/tilesets/headers.h'); t = open(hp).read()
    i = t.index('const struct Tileset gTileset_PellucaHarbourTiles ='); j = t.index('};', i)
    blk = re.sub(r'\.callback\s*=\s*[^,]+,', '.callback = InitTilesetAnim_PellucaHarbour,', t[i:j])
    if '.callback' not in blk: blk = blk.rstrip() + '\n    .callback = InitTilesetAnim_PellucaHarbour,\n'
    t = t[:i] + blk + t[j:]; open(hp, 'w').write(t)
