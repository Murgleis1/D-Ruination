"""Rebuild every source region from gTileset_Cormoria + gTileset_PellucaValley alone
(engine triple-layer semantics) and diff against the MonoMyth original render.

Expected: differences only from the tolerance-16 colour merge (<= 16 per channel).
Anything larger is a conversion error. Dropped cells (None) are excluded.
Usage: python3 -I verify_cormoria.py <codebase> <monomyth_renders_dir> <out_dir>
"""
import sys, os, json, struct
import numpy as np
from PIL import Image

def load_pal(d):
    P = []
    for i in range(16):
        L = open(os.path.join(d, 'palettes', f'{i:02d}.pal')).read().split('\n')[3:19]
        P.append([tuple(int(v) for v in l.split()) for l in L])
    return P

def load(d):
    a = np.array(Image.open(os.path.join(d, 'tiles.png')))
    t = a.reshape(a.shape[0] // 8, 8, 16, 8).transpose(0, 2, 1, 3).reshape(-1, 8, 8)
    mt = open(os.path.join(d, 'metatiles.bin'), 'rb').read()
    return t, load_pal(d), [struct.unpack_from('<12H', mt, i * 24) for i in range(len(mt) // 24)]

def main():
    C, R, O = sys.argv[1:4]
    pt, ppal, pm = load(os.path.join(C, 'data/tilesets/primary/cormoria'))
    st, spal, sm = load(os.path.join(C, 'data/tilesets/secondary/pelluca_valley'))
    pal = [ppal[i] if i < 6 else spal[i] for i in range(16)]
    def draw(mid):
        e = pm[mid] if mid < 512 else sm[mid - 512]
        img = np.zeros((16, 16, 3), int)
        for q in range(12):
            v = e[q]; tid = v & 0x3FF
            if q >= 4 and tid == 0: continue
            t = pt[tid] if tid < 512 else st[tid - 512]
            if (v >> 10) & 1: t = t[:, ::-1]
            if (v >> 11) & 1: t = t[::-1]
            sl = v >> 12; oy, ox = ((q % 4) // 2) * 8, (q % 2) * 8
            for y in range(8):
                for x in range(8):
                    if t[y, x]: img[oy + y, ox + x] = pal[sl][t[y, x]]
        return img
    man = json.load(open(os.path.join(C, 'data/tilesets/secondary/pelluca_valley/assembly_manifest.json')))
    src_png = {'0x869580': 'woodavens.png', '0x86960c': 'elderflower.png', '0x86db2c': 'port_86db2c.png', '0x86da30': 'obi_86da30.png'}
    os.makedirs(O, exist_ok=True); report = {}
    for name, r in man['regions'].items():
        if name == 'church': continue
        g = r['grid']; x0, y0 = r['origin']; H, W = len(g), len(g[0])
        orig = np.array(Image.open(os.path.join(R, src_png[r['source_map']])).convert('RGB')).astype(int)
        orig = orig[y0 * 16:(y0 + H) * 16, x0 * 16:(x0 + W) * 16]
        new = np.zeros_like(orig); mask = np.zeros(orig.shape[:2], bool)
        for y in range(H):
            for x in range(W):
                if g[y][x] is None: continue
                new[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = draw(g[y][x]); mask[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = True
        d = np.abs(new - orig).max(-1)[mask]
        report[name] = dict(cells=int(mask.sum() // 256), exact=round(100 * (d == 0).mean(), 1),
                            within_merge=round(100 * (d <= 16).mean(), 2), worst=int(d.max()))
        side = np.full((orig.shape[0], orig.shape[1] * 2 + 8, 3), 255, np.uint8)
        side[:, :orig.shape[1]] = orig; side[:, orig.shape[1] + 8:] = np.where(mask[..., None], new, 255)
        Image.fromarray(side).save(os.path.join(O, f'{name}.png'))
    # church: render the rebuilt grid on its own
    g = man['regions']['church']['grid']
    ch = np.zeros((len(g) * 16, len(g[0]) * 16, 3), np.uint8)
    for y, row in enumerate(g):
        for x, mid in enumerate(row):
            if mid is not None: ch[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = draw(mid)
    Image.fromarray(ch).save(os.path.join(O, 'church.png'))
    for k, v in report.items(): print(f'{k:12s} {v}')
    bad = [k for k, v in report.items() if v['worst'] > 16]
    print('REGIONS WITH ERRORS BEYOND THE COLOUR MERGE:', bad or 'none')

if __name__ == '__main__':
    main()
