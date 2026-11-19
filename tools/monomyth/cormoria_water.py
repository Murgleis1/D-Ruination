"""Animate Pelluca's water and shoreline with MonoMyth's own water animation (user 2026-11-19: "doesn't MonoMyth
have water textures you can use"; "the water is animated but the foam isn't": study MonoMyth's shorelines).

What MonoMyth does (measured, Old Bay / Port Ginseng): its terrain primary animates a 32-tile strip, 8 frames
(frame list 0x894DB34), copied over primary tiles 416-447. The strip holds the open water (416-419), the foam
pieces of the shoreline (424-429, 446) and the shallow water under the foam (440-443): the whole shore moves
together. (Its tileset ships those tiles from mixed frames, which is why they first looked like other art.)

gTileset_Cormoria took the quay water and Old Bay's sandbank from those maps, so our tiles 182-185, 196-199 and
202-210 are copies of strip tiles. The Cormoria build's assembly manifest says which MonoMyth metatile each of
our metatiles came from; lining up their entries gives, for each of our tiles, its strip tile and flip.
One fix: the build had merged MonoMyth's 424 and 425 (identical in the shipped frame, different in the others)
into our tile 206, so 425's uses get a tile of their own (FOAM_SPLIT, a free primary tile).
Colours: the remap the build actually applied (it merged some shallow-water tones), read off our tiles against
MonoMyth's shipped tiles; colours that only appear in other frames go to the nearest colour of our palette 5.

Run after build_cormoria.py (it rewrites the Cormoria tiles and metatiles).
Usage: python3 tools/monomyth/cormoria_water.py [--mock out_prefix]
"""
import os, sys, json, struct
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from romlib import ROM, u32, off, layout
from render import map_cells, pals_of, tiles_of
C = os.path.normpath(os.path.join(HERE, '..', '..', 'codebase'))
D = os.path.join(C, 'data/tilesets/primary/cormoria')
MAN = os.path.join(C, 'data/tilesets/secondary/pelluca_valley/assembly_manifest.json')
FRAMES, STRIP0, NSTRIP = 0x894DB34, 416, 32          # MonoMyth's terrain water: frame list, dest tile, tiles
FOAM_SPLIT = 506                                     # our new tile for MonoMyth's 425 (first free primary tile)

def mm_tile(addr):
    a = np.frombuffer(ROM[off(addr):off(addr) + 32], np.uint8); t = np.zeros((8, 8), np.uint8)
    t[:, 0::2] = (a & 15).reshape(8, 4); t[:, 1::2] = (a >> 4).reshape(8, 4); return t
FR = [u32(off(FRAMES) + 4 * i) for i in range(8)]
STRIP = [[mm_tile(FR[f] + 32 * k) for k in range(NSTRIP)] for f in range(8)]
def flip(t, fl): return t[:, ::-1] if fl & 1 else t if not fl & 2 else t[::-1] if not fl & 1 else t
def flipt(t, fl):
    if fl & 1: t = t[:, ::-1]
    if fl & 2: t = t[::-1]
    return t

# ---- our tiles <- strip tiles, from the manifest ----
def sources():
    """{(our metatile, entry index): (strip k, flip delta, MonoMyth palette, source map)} for strip entries."""
    man = json.load(open(MAN)); pm = open(os.path.join(D, 'metatiles.bin'), 'rb').read(); out = {}
    for r in man['regions'].values():
        if not r.get('source_map'): continue
        s = int(r['source_map'], 16); x0, y0 = r['origin']; L = layout(u32(s)); W = L['w']; cells = map_cells(L)
        for y, row in enumerate(r['grid']):
            for x, nid in enumerate(row):
                if nid is None or nid >= 512: continue
                mm = cells[(y0 + y) * W + (x0 + x)] & 0x3FF
                base = off(L['primary']['mt']) + 24 * mm if mm < 512 else off(L['secondary']['mt']) + 24 * (mm - 512)
                e = struct.unpack_from('<12H', ROM, base); o = struct.unpack_from('<12H', pm, nid * 24)
                for q, (v, w) in enumerate(zip(o, e)):
                    if STRIP0 <= (w & 0x3FF) < STRIP0 + NSTRIP and v & 0x3FF:
                        out[(nid, q)] = ((w & 0x3FF) - STRIP0, ((v >> 10) & 3) ^ ((w >> 10) & 3), w >> 12, s)
    return out

def pal5():
    L = open(os.path.join(D, 'palettes', '05.pal')).read().split('\n')[3:19]
    return np.array([tuple(int(v) for v in l.split()) for l in L])
def lut(mm_pal):
    P5 = pal5(); return np.array([int(np.argmin(np.abs(P5[1:] - np.array(c)).sum(1))) + 1 if i else 0
                                  for i, c in enumerate(mm_pal)], np.uint8)

def plan():
    """{our tile: (k, flip, palette lut)} for every animated tile, after the 424/425 split (applied if needed)."""
    src = sources(); pm = bytearray(open(os.path.join(D, 'metatiles.bin'), 'rb').read())
    pals = {}
    def key(s, p):
        if (s, p) not in pals: pals[(s, p)] = lut(pals_of(layout(u32(s))['primary'])[p])
        return pals[(s, p)]
    by_tile = {}
    for (nid, q), (k, fl, p, s) in src.items():
        v = struct.unpack_from('<H', pm, nid * 24 + 2 * q)[0]; t = v & 0x3FF
        by_tile.setdefault(t, {}).setdefault((k, fl), []).append((nid, q, p, s))
    changed = False
    for t, uses in list(by_tile.items()):
        seqs = {}
        for (k, fl) in uses: seqs.setdefault(tuple(flipt(STRIP[f][k], fl).tobytes() for f in range(8)), []).append((k, fl))
        if len(seqs) == 1: continue
        assert t == 206 and len(seqs) == 2, f'tile {t}: {len(seqs)} different animations'
        # MonoMyth 425 (strip 9) gets FOAM_SPLIT; the shipped pixels are the same as 206's
        for (k, fl) in [kf for kf in uses if kf[0] == 9]:
            for nid, q, p, s in uses.pop((k, fl)):
                v = struct.unpack_from('<H', pm, nid * 24 + 2 * q)[0]
                struct.pack_into('<H', pm, nid * 24 + 2 * q, (v & ~0x3FF) | FOAM_SPLIT); changed = True
            by_tile.setdefault(FOAM_SPLIT, {})[(k, fl)] = [(0, 0, 3, 0x86DA30)]
    # the build's own colour remap, per source palette: our tile vs MonoMyth's shipped tile (416+k of the source
    # map's primary), pixel by pixel; colours never shipped fall back to the nearest colour
    sheet = np.array(Image.open(os.path.join(D, 'tiles.png'))) & 15
    pairs = {}
    for t, uses in by_tile.items():
        if t == FOAM_SPLIT: continue
        (k, fl), lst = next(iter(uses.items())); _, _, p, s = lst[0]
        shipped = flipt(tiles_of(layout(u32(s))['primary'])[STRIP0 + k], fl)
        ours = sheet[(t // 16) * 8:(t // 16) * 8 + 8, (t % 16) * 8:(t % 16) * 8 + 8]
        for a, b in zip(shipped.ravel(), ours.ravel()): pairs.setdefault((s, p), {}).setdefault(int(a), {}).setdefault(int(b), 0); pairs[(s, p)][int(a)][int(b)] += 1
    luts = {}
    for sp, m in pairs.items():
        lt = key(*sp).copy()
        for a, bs in m.items(): lt[a] = max(bs, key=bs.get)
        luts[sp] = lt
    out = {}
    for t, uses in by_tile.items():
        (k, fl), lst = next(iter(uses.items())); _, _, p, s = lst[0]; out[t] = (k, fl, luts.get((s, p), key(s, p)))
    return out, pm, changed

def frame_tiles(pl, f):
    return {t: lt[flipt(STRIP[f][k], fl)] for t, (k, fl, lt) in pl.items()}

def runs(tiles):
    r = []
    for t in sorted(tiles):
        if r and r[-1][0] + r[-1][1] == t: r[-1][1] += 1
        else: r.append([t, 1])
    return r

def write():
    pl, pm, changed = plan()
    sheet = np.array(Image.open(os.path.join(D, 'tiles.png'))); im0 = Image.open(os.path.join(D, 'tiles.png'))
    if changed or FOAM_SPLIT in pl:
        ty, tx = FOAM_SPLIT // 16, FOAM_SPLIT % 16
        assert not (sheet[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8] & 15).any() or not changed, f'tile {FOAM_SPLIT} is in use'
        sheet[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8] = frame_tiles(pl, 0)[FOAM_SPLIT]
        im = Image.fromarray(sheet, 'P'); im.putpalette(im0.getpalette()); im.save(os.path.join(D, 'tiles.png'))
        open(os.path.join(D, 'metatiles.bin'), 'wb').write(bytes(pm))
    R = runs(pl); d = os.path.join(D, 'anim', 'water'); os.makedirs(d, exist_ok=True)
    P5 = [tuple(int(v) for v in c) for c in pal5()]
    for f in range(8):
        ft = frame_tiles(pl, f); strip = np.hstack([ft[t] for t in sorted(pl)])
        im = Image.fromarray(strip, 'P'); im.putpalette([v for c in P5 for v in c] + [0] * (768 - 48))
        im.save(os.path.join(d, f'{f}.png'))
    print('animated tiles (runs: first, count):', R)
    return R

def mock(prefix):
    """Pelluca's south shore with the frames applied, as a GIF."""
    sys.path.insert(0, os.path.join(HERE, '..'))
    import render_layout as R
    pl, pm, changed = plan()
    ts = R.TS('LAYOUT_PELLUCA_CITY'); W = 80
    ts.pm = np.frombuffer(bytes(pm), '<u2').reshape(-1, 12)
    while len(ts.pt) <= FOAM_SPLIT: ts.pt.append(np.zeros((8, 8), np.uint8))
    cells = struct.unpack('<4800H', open(os.path.join(C, 'data/layouts/PellucaCity/map.bin'), 'rb').read())
    box = (4, 36, 40, 60); imgs = []
    for f in range(8):
        for t, tile in frame_tiles(pl, f).items(): ts.pt[t] = tile
        img = np.zeros(((box[3] - box[1]) * 16, (box[2] - box[0]) * 16, 3), np.uint8)
        for y in range(box[1], box[3]):
            for x in range(box[0], box[2]):
                img[(y - box[1]) * 16:(y - box[1] + 1) * 16, (x - box[0]) * 16:(x - box[0] + 1) * 16] = ts.metatile(cells[y * W + x] & 0x3FF)
        imgs.append(Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), Image.NEAREST))
    imgs[0].save(prefix + '.gif', save_all=True, append_images=imgs[1:], duration=267, loop=0)
    print(prefix + '.gif', 'animated tiles', sorted(pl))

if __name__ == '__main__':
    if '--mock' in sys.argv: mock(sys.argv[sys.argv.index('--mock') + 1])
    else: write()
