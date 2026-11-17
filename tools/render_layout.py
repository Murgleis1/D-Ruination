"""Render a Ruination layout (or a tileset's metatiles) from the source files, no ROM needed.
Triple-layer metatiles: 12 u16 entries (bottom, middle, top x 4 tiles). Tile ids < 512 are in the
primary tileset, >= 512 in the secondary; palettes 0-5 primary, 6-12 secondary.
Usage:
  render_layout.py layout LAYOUT_ID out.png [--grid]
  render_layout.py sheet LAYOUT_ID out.png        # every metatile of both tilesets, numbered
"""
import sys, os, json, re
import numpy as np
from PIL import Image, ImageDraw
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'codebase')

def ts_dir(sym):
    hdr = open(os.path.join(C, 'src/data/tilesets/headers.h')).read()
    m = re.search(r'const struct Tileset ' + sym + r'\s*=\s*\{(.*?)\};', hdr, re.S)
    tiles = re.search(r'\.tiles = (\w+)', m.group(1)).group(1)
    g = open(os.path.join(C, 'src/data/tilesets/graphics.h')).read()
    path = re.search(tiles + r'\[\] = INCBIN_U32\("([^"]+)"', g).group(1)
    return os.path.join(C, os.path.dirname(path))

def load_ts(d):
    im = Image.open(os.path.join(d, 'tiles.png')); a = np.array(im)
    if im.mode != 'P': raise SystemExit('tiles.png not indexed: ' + d)
    a = a & 15
    tiles = [a[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] for i in range((a.shape[0] // 8) * 16)]
    pals = []
    for i in range(16):
        p = os.path.join(d, 'palettes', f'{i:02d}.pal')
        L = open(p).read().split('\n')[3:19] if os.path.exists(p) else []
        pals.append([tuple(int(v) for v in l.split()) for l in L if l.strip()] or [(0, 0, 0)] * 16)
    mt = np.frombuffer(open(os.path.join(d, 'metatiles.bin'), 'rb').read(), '<u2')
    return tiles, pals, mt.reshape(-1, 12)

class TS:
    def __init__(self, layout):
        L = [l for l in json.load(open(os.path.join(C, 'data/layouts/layouts.json')))['layouts'] if l.get('id') == layout][0]
        self.L = L
        self.pt, self.pp, self.pm = load_ts(ts_dir(L['primary_tileset']))
        self.st, self.sp, self.sm = load_ts(ts_dir(L['secondary_tileset']))
        self.pal = self.pp[:6] + self.sp[6:13] + self.pp[13:]
    def tile(self, t):
        return self.pt[t] if t < 512 else (self.st[t - 512] if t - 512 < len(self.st) else None)
    def metatile(self, m):
        ent = self.pm[m] if m < 512 else self.sm[m - 512]
        img = np.zeros((16, 16, 3), np.uint8); img[:] = (0, 0, 0)
        for layer in range(3):
            for q in range(4):
                v = int(ent[layer * 4 + q]); t = self.tile(v & 0x3FF)
                if t is None: continue
                if v & 0x400: t = t[:, ::-1]
                if v & 0x800: t = t[::-1, :]
                pal = self.pal[v >> 12]
                y, x = (q // 2) * 8, (q % 2) * 8
                for yy in range(8):
                    for xx in range(8):
                        c = t[yy, xx]
                        if c or layer == 0: img[y + yy, x + xx] = pal[c] if c < len(pal) else (0, 0, 0)
        return img

def main():
    mode, layout, out = sys.argv[1:4]
    ts = TS(layout)
    if mode == 'layout':
        W, H = ts.L['width'], ts.L['height']
        cells = np.frombuffer(open(os.path.join(C, ts.L['blockdata_filepath']), 'rb').read(), '<u2').reshape(H, W)
        img = np.zeros((H * 16, W * 16, 3), np.uint8)
        for y in range(H):
            for x in range(W):
                img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = ts.metatile(int(cells[y, x]) & 0x3FF)
        im = Image.fromarray(img).resize((W * 48, H * 48), 0)
        if '--grid' in sys.argv:
            d = ImageDraw.Draw(im)
            for x in range(W): d.text((x * 48 + 2, 2), str(x), fill=(255, 255, 0))
            for y in range(H): d.text((2, y * 48 + 2), str(y), fill=(0, 255, 255))
        im.save(out)
    else:
        ids = list(range(len(ts.pm))) + [512 + i for i in range(len(ts.sm))]
        cols = 16; rows = (len(ids) + cols - 1) // cols
        im = Image.new('RGB', (cols * 52, rows * 62), (40, 40, 40)); d = ImageDraw.Draw(im)
        for k, m in enumerate(ids):
            x, y = (k % cols) * 52, (k // cols) * 62
            im.paste(Image.fromarray(ts.metatile(m)).resize((48, 48), 0), (x + 2, y + 12)); d.text((x + 2, y), str(m), fill=(255, 255, 0))
        im.save(out)

if __name__ == '__main__':
    main()
