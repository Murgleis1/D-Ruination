"""Mock: Pokemon Odyssey pieces in the Pelluca dormitory common room (proposal, 2026-11-19).
Hearth and food plates: Odyssey's brick-fireplace hall (layout 0x8319414). Barrels: its rustic barn
(layout 0x871F950). FireRed metatiles: objects sit on the top layer, so they lift onto our floor/tables."""
import os, sys, pickle
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'monomyth', 'dormitory'))
import numpy as np
from PIL import Image, ImageDraw
import frrender as FR
import compose_mock as CM

def odyssey_layout(addr):
    items = pickle.load(open('/tmp/ody_indoor.pkl', 'rb'))
    return [h for h in items if h['layout']['addr'] == addr][0]['layout']
FIRE, RUST = FR.TS(odyssey_layout(0x8319414)), FR.TS(odyssey_layout(0x871F950))

def fr_layer(ts, mid, layer):
    rgb = np.zeros((16, 16, 3), np.uint8); mask = np.zeros((16, 16), bool); e = ts.ents(mid)
    for q in range(4):
        v = e[layer * 4 + q]; t = ts.tile(v & 0x3FF)
        if v & 0x400: t = t[:, ::-1]
        if v & 0x800: t = t[::-1, :]
        pal = np.array(ts.pal[v >> 12], np.uint8); y, x = (q // 2) * 8, (q % 2) * 8
        rgb[y:y + 8, x:x + 8] = pal[t]; mask[y:y + 8, x:x + 8] = t != 0
    return rgb, mask

_M = CM.M
def M(src, mid):
    if src == 'F': return FIRE.meta(mid)                               # whole Odyssey metatile (the hearth)
    if src in ('Fo', 'Ro'):                                            # Odyssey top layer over one of ours
        ts = FIRE if src == 'Fo' else RUST; oid, under = mid
        out = _M(*under).copy(); rgb, m = fr_layer(ts, oid, 1); out[m] = rgb[m]; return out
    return _M(src, mid)
CM.M = M

def floor1_plus():
    g = CM.floor1()
    hearth = [[668, 669, 670], [676, 677, 678], [684, 685, 686]]
    for dy, r in enumerate(hearth):
        for dx, v in enumerate(r): g[dy][14 + dx] = ('F', v)
    for y, row in enumerate(g):                                         # a plate of food on every dining table
        for x, c in enumerate(row):
            if c == ('s', 176): g[y][x] = ('Fo', (712, ('s', 176)))
    for x in (17, 18):                                                 # barrels in the north-east corner,
        g[4][x], g[5][x] = ('Ro', (648, ('s', 155))), ('Ro', (656, ('s', 155)))   # clear of the door's mat
    return g

if __name__ == '__main__':
    CM.DOORS_1F = (4, 13, 17)
    a = CM.grid(CM.floor1()); b = CM.grid(floor1_plus())
    S = Image.new('RGB', (a.shape[1] * 2 + 16, a.shape[0] + 20), (28, 28, 28)); d = ImageDraw.Draw(S)
    S.paste(Image.fromarray(a), (0, 20)); S.paste(Image.fromarray(b), (a.shape[1] + 16, 20))
    d.text((2, 4), 'Dormitory 1F now', fill=(255, 230, 120)); d.text((a.shape[1] + 18, 4), 'with Odyssey hearth, plates, barrels', fill=(255, 230, 120))
    S.resize((S.width * 2, S.height * 2), Image.NEAREST).save('/tmp/dorm_odyssey_mock.png')
