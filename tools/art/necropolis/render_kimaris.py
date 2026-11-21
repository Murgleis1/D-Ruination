"""Render Kimaris's chamber as built (its tilesets, metatiles and layout in the codebase), with the cauldrons'
animation: a 9-frame GIF and a still. Usage: python3 render_kimaris.py OUT.gif OUT.png"""
import os, sys, json, struct
import numpy as np
from PIL import Image
C = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'codebase'))
P, S = C + '/data/tilesets/primary/kimaris_chamber_tiles', C + '/data/tilesets/secondary/kimaris_chamber'
def pal(path):
    L = open(path).read().split('\n')[3:19]; return np.array([[int(v) for v in l.split()] for l in L], np.uint8)
def main(gif, png):
    sheet = np.array(Image.open(P + '/tiles.png')); n = sheet.shape[0] // 8 * 16
    tiles = [sheet[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] for i in range(n)]
    pals = [pal(P + '/palettes/%02d.pal' % i) if i < 6 else pal(S + '/palettes/%02d.pal' % i) for i in range(16)]
    mt = open(S + '/metatiles.bin', 'rb').read(); meta = [struct.unpack('<12H', mt[i * 24:i * 24 + 24]) for i in range(len(mt) // 24)]
    grid = np.fromfile(C + '/data/layouts/KimarisChamber/map.bin', '<u2').reshape(15, 17)
    pots = json.load(open(S + '/anim/cauldrons.json')); frames = []
    for k in range(9):
        T = list(tiles)
        for p in pots:
            a = np.array(Image.open(S + '/anim/cauldron_%s/%d.png' % (p['name'], (k + p['phase']) % 9)))
            for i in range(p['n']): T[p['first'] + i] = a[i * 8:i * 8 + 8]
        img = np.zeros((240, 272, 3), np.uint8)
        for y in range(15):
            for x in range(17):
                for q, v in enumerate(meta[(grid[y, x] & 0x3ff) - 512]):
                    if q >= 4 and not (v & 0x3ff): continue
                    t = T[v & 0x3ff]
                    if v & 0x400: t = t[:, ::-1]
                    if v & 0x800: t = t[::-1]
                    qq = q % 4; yy, xx = y * 16 + (qq // 2) * 8, x * 16 + (qq % 2) * 8
                    m = t != 0 if q >= 4 else np.ones((8, 8), bool); img[yy:yy + 8, xx:xx + 8][m] = pals[v >> 12][t][m]
        frames.append(Image.fromarray(img).resize((544, 480), 0))
    frames[0].save(gif, save_all=True, append_images=frames[1:], duration=133, loop=0); frames[2].save(png)
if __name__ == '__main__': main(*sys.argv[1:3])
