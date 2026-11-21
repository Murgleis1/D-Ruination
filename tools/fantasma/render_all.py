"""Render every unique Fantasma map layout and build labelled contact sheets.

Usage: python3 render_all.py HEADERS.pkl OUTDIR
HEADERS.pkl is the pickled list from tools/monomyth/romlib.find_headers run on the Fantasma ROM.
Writes OUTDIR/maps/s{mapsec}_{layoutaddr&0xffff}_{w}x{h}.png and OUTDIR/sheet_NN.png (48 per sheet).
"""
import os, sys, pickle
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fsread as F

def main(hp, out):
    hs = pickle.load(open(hp, 'rb')); os.makedirs(out + '/maps', exist_ok=True)
    seen, names = set(), []
    for h in sorted(hs, key=lambda h: (h['mapsec'], h['layout']['addr'])):
        L = h['layout']
        if L['map'] in seen or not (0 < L['w'] <= 200 and 0 < L['h'] <= 200): continue
        seen.add(L['map'])
        try: img = F.render(L)
        except Exception as e: print('skip', hex(L['addr']), e); continue
        n = 's%03d_%04x' % (h['mapsec'], L['addr'] & 0xffff)
        Image.fromarray(img).save('%s/maps/%s_%dx%d.png' % (out, n, L['w'], L['h'])); names.append((n, img))
    TW, TH, per = 200, 200, 48
    for s in range(0, len(names), per):
        sh = Image.new('RGB', (TW * 8, (TH + 12) * 6), (30, 30, 30)); d = ImageDraw.Draw(sh)
        for k, (n, img) in enumerate(names[s:s + per]):
            im = Image.fromarray(img); im.thumbnail((TW, TH), Image.NEAREST)
            x, y = (k % 8) * TW, (k // 8) * (TH + 12)
            sh.paste(im, (x, y + 12)); d.text((x + 2, y), n, fill=(255, 255, 0))
        sh.save('%s/sheet_%02d.png' % (out, s // per))
    print(len(names), 'layouts')

if __name__ == '__main__': main(*sys.argv[1:3])
