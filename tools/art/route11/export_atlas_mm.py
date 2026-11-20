"""Export a MonoMyth map's metatiles as an atlas (same format as export_atlas.py: 'full', 'top', 'cells'), for the
mock composers. MonoMyth's metatiles are triple-layer (12 entries).
Usage: python3 export_atlas_mm.py <layout addr hex> <out.npz>"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'monomyth'))
import numpy as np
import romlib, render
from romlib import u16

def main(addr, out):
    a = int(addr, 16); L = [h for h in romlib.find_headers() if h['layout']['addr'] == a][0]['layout']
    ts = render.TS(L); NPM = render.NPM
    full = np.zeros((1024, 16, 16, 3), np.uint8); top = np.zeros((1024, 16, 16, 4), np.uint8)
    for m in range(1024):
        base = ts.pmt + m * 24 if m < NPM else ts.smt + (m - NPM) * 24
        img = np.zeros((16, 16, 3), np.uint8); tm = np.zeros((16, 16), bool); timg = np.zeros((16, 16, 3), np.uint8)
        try:
            for q in range(12):
                e = u16(base + q * 2); tid, xf, yf, sl = e & 0x3ff, (e >> 10) & 1, (e >> 11) & 1, e >> 12
                t = ts.tile(tid)
                if t is None: continue
                if xf: t = t[:, ::-1]
                if yf: t = t[::-1, :]
                oy, ox = ((q % 4) // 2) * 8, ((q % 4) % 2) * 8
                pal = np.array(ts.pal[sl], np.uint8); nz = t != 0
                blk = img[oy:oy + 8, ox:ox + 8]
                if q < 4: blk[:] = pal[t]
                else:
                    blk[nz] = pal[t][nz]; timg[oy:oy + 8, ox:ox + 8][nz] = pal[t][nz]; tm[oy:oy + 8, ox:ox + 8] |= nz
        except Exception: continue
        full[m] = img; top[m][tm, :3] = timg[tm]; top[m][tm, 3] = 255
    cells = np.array(render.map_cells(L), np.uint16).reshape(L['h'], L['w']) & 0x3FF
    np.savez_compressed(out, full=full, top=top, cells=cells); print(out, L['w'], L['h'])

if __name__ == '__main__':
    main(*sys.argv[1:3])
