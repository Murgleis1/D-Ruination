"""Route 13 mock v1 (zone plan v1 approved by the user 2026-11-22): north from Mirroh's north-west gatehouse up the
slopes of the Mirroh massif; it forks at a plateau with a Templar waystone: the Templars' cobbled pilgrim road runs on
north-east to Templar Headquarters, a rough icy trail breaks off north-west up rock steps to Mt. Mirroh.

Built with Mirroh's composer (tools/art/mirroh/mirroh_mock.py: its Map, its cut-out pieces) so the route reads as the
same massif:
  Fort Elderflower (MonoMyth): snow, snowy pines, buried rocks, the low rock walls that step the snowfield (its outer
    map 0x869C48: the cliff faces 0xff/0xfd, ridges 0x105-0x107), its trodden icy track (0x118-0x12a), its cobbles;
  Ghost Grey (JoeyZeed): Opal Village's reflecting ice (the tarn), as in Mirroh;
  Dreamstone Mysteries: its Mt. Mirroh tall grass (gTileset_Snow 0x0d), cut off its snow and its green cooled to
    Elderflower's pines;
  Pokemon Crown: its signpost; the waystone is new, carved in the ice-path statue's stone (tools/art/icepath).
The foot: Mirroh's north wall (from the built Upper Mirroh) with the passage the road comes out of.
Usage: python3 tools/art/route13/route13_mock.py [out.png]
"""
import os, sys, json
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ART = os.path.join(HERE, '..')
REPO = os.path.abspath(os.path.join(ART, '..', '..')); C = os.path.join(REPO, 'codebase')
sys.path.insert(0, os.path.join(ART, 'mirroh')); sys.path.insert(0, ART); sys.path.insert(0, os.path.join(ART, 'icepath'))
import mirroh_mock as mm
W, H = 40, 64
mm.W, mm.H = W, H                                  # (Mirroh's Map, on this map's size)
import mirroh_v3 as v3
from mirroh_v3 import ef, rnd, vnoise, _seg_dist, thick, snow_on, cobbles
import arceus_statue as AS

EFG = mm.EF_GROUND
def snow(x, y): return ef(0xee) if rnd('r13f', x, y) < 0.035 else ef(0xed)
def rect(x0, y0, x1, y1): return {(x, y) for y in range(y0, y1 + 1) for x in range(x0, x1 + 1)}

def lane(pts, half, seed, wob=0.6):
    out = set()
    for y in range(H):
        for x in range(W):
            w = min(_seg_dist((x, y), a, b) for a, b in zip(pts, pts[1:]))
            if w < half + wob * (vnoise(x, y, 3.0, seed) - 0.5): out.add((x, y))
    return out

# ------------------------------------------------------------------ pieces
def pine(M, x, y, big):
    return M.place(mm.cut_ids('ef', [[0xe9, 0xea], [0xf1, 0xf2], [0xf9, 0xfa]] if big else [[0x109], [0x111]], EFG),
                   x, y, 'tree', check=True)

def rock(M, x, y): return M.place(mm.cut_ids('ef', [[0xe8]], EFG), x, y, 'rock')

def grass_tile():
    """Dreamstone Mysteries' Mt. Mirroh tall grass (gTileset_Snow 0x0d), cut off its own snow and set on
    Elderflower's; its greens cooled to the pines'."""
    big = np.asarray(Image.open('/home/claude/scratch/mirroh/LAYOUT_MT_MIRROH_EXTERIOR.png').convert('RGB'))
    L = [l for l in json.load(open(os.path.join(C, 'data/layouts/layouts.json')))['layouts'] if l.get('id') == 'LAYOUT_MT_MIRROH_EXTERIOR'][0]
    g = np.fromfile(os.path.join(C, L['blockdata_filepath']), '<u2').reshape(L['height'], L['width']) & 0x3FF
    sc = big.shape[1] // L['width']
    cell = lambda x, y: big[y * sc:(y + 1) * sc:sc // 16, x * sc:(x + 1) * sc:sc // 16]
    ys, xs = np.nonzero(g == 0x0d); gr = cell(xs[40], ys[40])
    ids, n = np.unique(g, return_counts=True); plain = None
    for m in ids[np.argsort(-n)]:                                     # (DM's plain snow: the commonest cell
        yy, xx = np.nonzero(g == m); c = cell(xx[0], yy[0])           #  that is nearly flat white)
        if c.mean() > 215 and c.std() < 20: plain = c; break
    tuft = np.abs(gr.astype(int) - plain.astype(int)).sum(-1) > 30
    greens = [(0, 80, 88), (8, 120, 88), (80, 184, 112)]               # (the pines' foliage greens, dark to light)
    out = snow(0, 1).copy(); src = gr[tuft].astype(float)
    l = src @ [0.3, 0.59, 0.11]; lo, hi = l.min(), l.max()
    for i, (p, li) in enumerate(zip(np.argwhere(tuft), l)):
        if src[i][1] > src[i][0] + 12:                                 # (the green: to the pines' ramp)
            out[p[0], p[1]] = greens[int(round((li - lo) / max(1, hi - lo) * (len(greens) - 1)))]
        else: out[p[0], p[1]] = np.clip(src[i] * [0.96, 0.98, 1.0], 0, 255)
    return out

def waystone():
    """The Templars' waystone (new): a slim stele in the ice-path statue's carved, gem-flecked stone, the Order's blue
    gem band and boss, a cap of snow. 16x32 RGBA."""
    w, h = 12, 30; img = np.zeros((32, 16, 3), np.uint8); m = np.zeros((32, 16), bool); ox, oy = 2, 2
    def box(y0, y1, x0, x1, c): img[oy + y0:oy + y1, ox + x0:ox + x1] = c; m[oy + y0:oy + y1, ox + x0:ox + x1] = True
    c = w // 2
    box(0, 4, 0, w, AS.OUT); box(1, 3, 1, w - 1, AS.TOP); box(3, 4, 1, w - 1, AS.LIGHT)              # cap
    box(4, 7, 1, w - 1, AS.OUT); box(5, 6, 2, w - 2, AS.GOLD); box(4, 7, c - 2, c + 2, AS.OUT); box(5, 6, c - 1, c + 1, AS.TEAL)
    box(7, 24, 2, w - 2, AS.OUT); box(7, 24, 3, w - 3, AS.LIGHT); box(7, 8, 3, w - 3, AS.D2)           # shaft
    for x in (4, 7): box(9, 23, x, x + 1, AS.MID)
    box(12, 16, c - 2, c + 2, AS.OUT); box(13, 15, c - 1, c + 1, AS.GOLD_L)                           # gem boss
    box(24, 27, 1, w - 1, AS.OUT); box(24, 26, 2, w - 2, AS.TOP); box(26, 27, 2, w - 2, AS.MID)       # base
    box(27, 30, 0, w, AS.OUT); box(27, 29, 1, w - 1, AS.LIGHT); box(29, 30, 1, w - 1, AS.D1)
    snowcap = (236, 240, 248)
    img[oy:oy + 2, ox + 1:ox + w - 1] = snowcap; img[oy + 2, ox + 2:ox + w - 3] = snowcap; m[oy:oy + 3, ox:ox + w] = True
    img[oy - 1, ox + 3:ox + w - 3] = snowcap; m[oy - 1, ox + 3:ox + w - 3] = True
    return img, m

def place_rgba(M, img, m, x0, y0, tag):
    for cy in range(img.shape[0] // 16):
        for cx in range(img.shape[1] // 16):
            a = m[cy * 16:cy * 16 + 16, cx * 16:cx * 16 + 16]
            if a.any(): M.obj[y0 + cy][x0 + cx].append((img[cy * 16:cy * 16 + 16, cx * 16:cx * 16 + 16].copy(), a)); M.otag[y0 + cy, x0 + cx] = tag

def icy_track(M, cells):
    """Elderflower's trodden icy track (two wide): each vertical run of its cells takes the track's pieces."""
    S = set(cells)
    for (x, y) in sorted(S):
        if (x + 1, y) in S and (x - 1, y) not in S:                     # (the run's left column; its right is x+1)
            top, bot = (x, y - 1) not in S, (x, y + 1) not in S
            l, r = (0x118, 0x11a) if top else (0x128, 0x12a) if bot else (0x120, 0x122)
            M.ground(x, y, ef(l), 'track'); M.ground(x + 1, y, ef(r), 'track')

# ------------------------------------------------------------------ the composition
def compose():
    M = mm.Map()
    for y in range(H):
        for x in range(W): M.ground(x, y, snow(x, y), 'snow')
    walk_extra = set()

    # --- the foot: Mirroh's north wall (its top, from the built Upper Mirroh), the passage the road comes out of,
    # the north-west gatehouse's spires behind it
    sys.path.insert(0, ART); import render_built as RB
    RB.main('MirrohUpper', '/tmp/_r13_upper.png'); U = np.asarray(Image.open('/tmp/_r13_upper.png').convert('RGB'))
    ucell = lambda x, y: U[y * 16:y * 16 + 16, x * 16:x * 16 + 16].copy()
    for x in range(W):
        if x in (19, 20): continue
        sx = 22 + (x % 2)                                               # (a stretch of the wall's top, repeated)
        M.ground(x, 62, ucell(sx, 0), 'wall'); M.ground(x, 63, ucell(sx, 1), 'wall')
    for x in (19, 20):                                                  # (the passage: the gatehouse's dark doorway)
        M.ground(x, 62, ucell(x - 6, 8), 'gate'); M.ground(x, 63, ucell(x - 6, 9), 'gate-in')

    # --- the pinewood flanks (no way round): big pines in two staggered columns, small ones and rocks between
    def wood(x0, x1, y0, y1, seed):
        for y in range(y0, y1 + 1, 3):
            for x in range(x0, x1, 2):
                yy = y + (1 if ((x - x0) // 2) % 2 else 0)
                if yy + 2 <= y1 and M.free(x, yy, 2, 3): pine(M, x, yy, True)
        for y in range(y0, y1 + 1):
            for x in range(x0, x1 + 1):
                if M.free(x, y, 1, 2) and y + 1 <= y1: pine(M, x, y, False)
                elif M.free(x, y, 1, 1): rock(M, x, y)
    wood(0, 3, 0, 61, 'wl'); wood(36, 39, 0, 61, 'wr')
    wood(4, 7, 47, 61, 'wl2'); wood(32, 35, 51, 61, 'wr2'); wood(4, 5, 0, 30, 'wl3'); wood(34, 35, 0, 30, 'wr3')

    # --- the massif's spur between the two branches: a dense stand of pines and rocks on its rising ground (solid),
    # its tip at the fork
    spur = set()
    for y in range(0, 20):
        xl = 14 + int(round(y * 4 / 19)); xr = 26 - int(round(y * 6 / 19))
        for x in range(xl, xr + 1): spur.add((x, y))
    for (x, y) in spur: M.gtag[y, x] = 'spur'
    for y in range(0, 20, 3):
        for x in range(14, 26, 2):
            yy = y + (1 if (x // 2) % 2 else 0)
            if all((xx, yy + k) in spur for xx in (x, x + 1) for k in range(3)) and M.free(x, yy, 2, 3, ground=('spur',)):
                pine(M, x, yy, True)
    for (x, y) in sorted(spur, key=lambda c: (c[1], c[0])):
        if (x, y + 1) in spur and M.free(x, y, 1, 2, ground=('spur',)): pine(M, x, y, False)
        elif M.free(x, y, 1, 1, ground=('spur',)): rock(M, x, y)

    # --- the ledge band (one-way jumps down) for the switchback, a gap where the road climbs through
    for x in range(8, 30):
        if x in (24, 25, 26): continue
        M.ground(x, 44, ef(0x105 if x == 8 or x == 27 else 0x107 if x == 23 or x == 29 else 0x106), 'ledge')

    # --- the frozen tarn (Ghost Grey's reflecting ice, Elderflower's drifts round it)
    icef = lambda x, y: mm.recolour(mm.full('gg', 0x34b), mm.GG_ICE)
    pond = thick({(x, y) for y in range(28, 38) for x in range(4, 18)
                  if ((x - 10.5) / 4.6) ** 2 + ((y - 32.5) / 3.1) ** 2 < 1 + 0.3 * (vnoise(x, y, 1.8, 'tarn') - 0.5)})
    yard = {(x, y) for y in range(26, 40) for x in range(3, 20) if ((x - 10.5) / 6.6) ** 2 + ((y - 32.5) / 4.9) ** 2 < 1.1}
    snow_on(M, thick(yard - pond), icef, yard, 'snow')
    for (x, y) in pond: M.gtag[y, x] = 'ice'

    # --- the roads: the Templars' cobbled pilgrim road from the gate up to the fork and on north-east to their HQ;
    # the rough icy trail breaking off north-west up rock steps to Mt. Mirroh
    road = lane(((19.5, 63), (19.5, 57), (17.5, 52), (17, 48), (22, 46), (25, 45), (25, 41), (21.5, 37), (20.5, 31),
                 (20.5, 26), (22, 23.5), (27, 21), (30, 16), (31.5, 10), (32.5, 4), (33, -1)), 1.25, 'road', 0.4)
    road = thick({c for c in road if M.gtag[c[1], c[0]] in ('snow', 'ledge') and M.otag[c[1], c[0]] is None})
    plateau = {(x, y) for y in range(20, 30) for x in range(13, 28) if ((x - 20.5) / 6.2) ** 2 + ((y - 25) / 3.6) ** 2 < 1}
    cobbles(M, road)
    track = set()
    for (y0, y1, x) in ((22, 25, 13), (17, 21, 11), (11, 15, 9), (4, 9, 8), (0, 2, 8)):     # (staggered, as Elderflower's)
        for y in range(y0, y1 + 1): track |= {(x, y), (x + 1, y)}
    track = {c for c in track if M.gtag[c[1], c[0]] == 'snow' and M.otag[c[1], c[0]] is None}
    icy_track(M, track)
    for y in (16, 10):                                                  # (rock steps across the trail)
        for x in range(6, 13):
            if M.otag[y, x] is None and M.gtag[y, x] in ('snow', 'track'):
                M.ground(x, y, ef(0x105 if x == 6 else 0x107 if x == 12 else 0x106), 'ledge')
        for x in (8, 9): M.ground(x, y, ef(0x121), 'track')            # (its step: a gap in the rock)

    # --- the fork: the Templar waystone and a signpost
    wi, wm = waystone(); place_rgba(M, wi, wm, 19, 22, 'waystone')
    M.place(mm.cut('c31', 23, 20, 1, 1), 23, 26, 'sign')

    # --- snowy tall grass (wild Pokemon, stage 5)
    G = grass_tile()
    for (x0, y0, x1, y1, s) in ((9, 50, 13, 55, 'g1'), (27, 46, 31, 49, 'g2'), (9, 39, 14, 42, 'g3'), (27, 30, 32, 35, 'g4'),
                                (5, 18, 9, 21, 'g5'), (28, 12, 32, 17, 'g6')):
        for (x, y) in rect(x0, y0, x1, y1):
            e = ((x - (x0 + x1) / 2) / ((x1 - x0) / 2 + 0.7)) ** 2 + ((y - (y0 + y1) / 2) / ((y1 - y0) / 2 + 0.7)) ** 2
            if e < 1 + 0.35 * (vnoise(x, y, 1.6, s) - 0.5) and M.gtag[y, x] == 'snow' and M.otag[y, x] is None:
                M.ground(x, y, G, 'grass')

    # --- a few pines and rocks in the open, more uphill
    for (x, y, big) in ((10, 57, False), (28, 55, True), (6, 44, False), (31, 40, False), (14, 46, False), (25, 33, True),
                        (5, 22, True), (11, 25, False), (29, 24, False), (31, 27, False), (26, 9, False), (27, 4, True),
                        (12, 5, False), (5, 8, False)):
        if M.free(x, y, 2 if big else 1, 3 if big else 2): pine(M, x, y, big)
    for (x, y) in ((15, 58), (24, 50), (8, 36), (30, 37), (16, 28), (24, 28), (13, 13), (29, 7), (10, 2)):
        if M.free(x, y, 1, 1): rock(M, x, y)
    return M

def main(out):
    M = compose(); img = M.render(); Image.fromarray(img).save(out)
    big = Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), Image.NEAREST); big.save(out.replace('.png', '_2x.png'))
    print('saved', out, img.shape)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/route13_mock.png')
