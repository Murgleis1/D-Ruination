"""Measure the real tile cost of Pelluca's curated terrain set.

Each source REGION contributes every 8x8 tile actually placed in it (both the
merged bottom+middle layer and the top layer), flips deduped, compared by RGB
image so identical art from different source tilesets counts once. Regions are
generous around each approved piece so their transitions are included.
"""
import sys, pickle, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from romlib import *
from render import tiles_of, pals_of
_HP = os.environ.get('MONO_HEADERS', '/home/claude/mono/headers.pkl')
if not os.path.exists(_HP):                      # container wiped: rebuild the map-header index
    os.makedirs(os.path.dirname(_HP), exist_ok=True)
    pickle.dump(find_headers(), open(_HP, 'wb'))
H = {h['addr']: h for h in pickle.load(open(_HP, 'rb'))}
_ctx = {}
MODE = os.environ.get('FLATTEN', 'triple')  # 'merge' = always merge bottom+middle (old count)
def ctx(a):
    if a not in _ctx:
        L = H[a]['layout']; pp = pals_of(L['primary']); sp = pals_of(L['secondary'])
        _ctx[a] = (L, tiles_of(L['primary']), tiles_of(L['secondary']), [pp[i] if i < 6 else sp[i] for i in range(16)])
    return _ctx[a]
def quad(entries, c):
    L, pt, st, pal = c; img = np.full((8, 8, 3), -1, int)
    for e in entries:
        tid, xf, yf, sl = e & 0x3ff, (e >> 10) & 1, (e >> 11) & 1, e >> 12
        if tid == 0: continue
        t = pt[tid] if tid < 512 else st[tid - 512]
        if t is None: continue
        if xf: t = t[:, ::-1]
        if yf: t = t[::-1]
        m = t > 0
        if not m.any(): continue
        img[m] = np.array([pal[sl][v] for v in t[m]])
    return img
def canon(img):
    return min(v.tobytes() for v in (img, img[:, ::-1], img[::-1], img[::-1, ::-1]))
def region_tiles(a, x0, y0, x1, y1, exclude=()):
    c = ctx(a); L = c[0]; mo = off(L['map']); W = L['w']; T = set()
    for y in range(max(0, y0), min(L['h'], y1 + 1)):
        for x in range(max(0, x0), min(W, x1 + 1)):
            if any(ex0 <= x <= ex1 and ey0 <= y <= ey1 for ex0, ey0, ex1, ey1 in exclude): continue
            mid = u16(mo + (y * W + x) * 2) & 0x3ff
            base = off(L['primary']['mt']) + mid * 24 if mid < 512 else off(L['secondary']['mt']) + (mid - 512) * 24
            e = [u16(base + i * 2) for i in range(12)]
            used = [any(e[k * 4 + j] & 0x3ff for j in range(4)) for k in range(3)]
            for q in range(4):
                if MODE == 'triple':
                    # Ruination is triple-layer now (d18a04803): every layer imports as-is.
                    ims = tuple(quad([e[k * 4 + q]], c) for k in range(3) if used[k])
                elif MODE == 'merge' or all(used):
                    # 3 layers in use: two must become one. Merge bottom+middle, keep top.
                    ims = (quad([e[q], e[4 + q]], c), quad([e[8 + q]], c))
                else:
                    # <=2 layers used: they map onto Ruination's two layers unchanged,
                    # so each source tile stays a separate (shareable) tile.
                    ims = tuple(quad([e[k * 4 + q]], c) for k in range(3) if used[k])
                for im in ims:
                    if (im >= 0).any(): T.add(canon(im))
    return T
WA, WC, PG64, PG48, CB, OB12, OB11 = 0x869580, 0x869C10, 0x86DB2C, 0x86D88C, 0x869B84, 0x86DA30, 0x86DA14
WA_BUILDINGS = [(18, 26, 24, 33), (5, 28, 11, 32), (15, 10, 20, 14), (5, 20, 11, 24), (16, 20, 24, 24), (31, 27, 38, 32)]
REGIONS = [  # exact approved crop windows (cells), not generous boxes -- those swept in warehouses
    ('Wood Avens terrain (no snow tier, no buildings)', WA, (0, 9, 49, 45), WA_BUILDINGS),
    ('A Watercress cliff-into-water + rocks', WC, (2, 26, 12, 33), ()),
    ('C Watercress fountain (basin only)', WC, (23, 12, 29, 15), ()),
    ('G Port Ginseng quay', PG64, (35, 37, 44, 44), ()),
    ('I Port Ginseng surf beach', PG48, (3, 15, 13, 21), ()),
    ('F Cascade boardwalk', CB, (2, 26, 12, 32), ()),
    ('J Old Bay river sandbank', OB12, (18, 47, 28, 54), ()),
    ('K Old Bay rock outcrop', OB11, (26, 18, 36, 25), ()),
]
if __name__ == '__main__':
    allT = set()
    for name, a, box, ex in REGIONS:
        T = region_tiles(a, *box, exclude=ex); new = T - allT; allT |= T
        print('%-48s %4d tiles  (%4d new)' % (name, len(T), len(new)))
    print('TERRAIN TOTAL (deduped):', len(allT))
