"""The dock shrine (user 2026-11-27): MonoMyth's small wayside shrine from the Mt. Thunder climb (map header
0x86D73C, cells 15-16 x 19-21, its upper layers: a 32x48 wooden shrine with purple drapes and gold offerings, built
against the rock wall), recoloured for Pelluca / House Umbra, mocked on Pelluca Harbour's stair plaza.
Usage: python3 tools/art/pelluca/shrine/shrine_mock.py OUTDIR"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools/monomyth'))
from romlib import u32, layout
from render import TS, map_cells, NPM
from romlib import u16

def cut():
    L = layout(u32(0x86D73C)); c = map_cells(L); W = L['w']; ts = TS(L)
    out = np.zeros((48, 32, 4), np.uint8)
    for j in range(3):
        for i in range(2):
            mid = c[(19 + j) * W + 15 + i] & 0x3FF
            base = ts.pmt + mid * 24 if mid < NPM else ts.smt + (mid - NPM) * 24
            for q in range(4, 12):                       # middle and top layers: the shrine, not the wall behind
                e = u16(base + q * 2); tid, xf, yf, sl = e & 0x3FF, (e >> 10) & 1, (e >> 11) & 1, e >> 12
                t = ts.tile(tid)
                if t is None: continue
                if xf: t = t[:, ::-1]
                if yf: t = t[::-1, :]
                oy, ox = j * 16 + ((q % 4) // 2) * 8, i * 16 + ((q % 4) % 2) * 8
                m = t > 0
                blk = out[oy:oy + 8, ox:ox + 8]
                blk[m, :3] = np.array(ts.pal[sl])[t[m]]; blk[m, 3] = 255
    # the wall tapestry hanging behind the roof's left side (cell 15,19) is not part of the shrine
    WOOD = {(88, 72, 56), (112, 96, 80), (136, 128, 112), (176, 160, 136), (56, 64, 88), (72, 56, 80)}
    for y in range(13):
        for x in range(14):
            if out[y, x, 3] and tuple(int(v) for v in out[y, x, :3]) not in WOOD: out[y, x] = 0
    return out

ROOF_ROWS = 25          # rows above this are the roof
def recolour(src, scheme):
    out = src.copy(); a = src[..., 3] > 0
    for y in range(48):
        for x in range(32):
            if not a[y, x]: continue
            k = tuple(int(v) for v in src[y, x, :3])
            m = scheme['roof' if y < ROOF_ROWS else 'body'].get(k) or scheme['all'].get(k)
            if m: out[y, x, :3] = m
    return out

BROWNS = [(88, 72, 56), (112, 96, 80), (136, 128, 112), (176, 160, 136)]          # MonoMyth's wood, dark to light
SCHEMES = {
    # Pelluca's purple-slate roofs (sampled from the harbour's houses), walnut posts, Umbra violet drapes, gold kept
    'A_pelluca_slate': dict(
        roof=dict(zip(BROWNS, [(72, 56, 80), (120, 88, 128), (144, 104, 152), (168, 128, 176)])),
        body=dict(zip(BROWNS, [(64, 44, 40), (96, 64, 52), (128, 92, 68), (160, 124, 92)])),
        all={(56, 64, 88): (40, 32, 48), (72, 56, 80): (48, 36, 56)}),
    # House Umbra: a black roof with a violet sheen, black-lacquered posts, the same drapes and gold
    'B_umbra_black': dict(
        roof=dict(zip(BROWNS, [(40, 36, 52), (64, 56, 80), (88, 76, 108), (120, 104, 144)])),
        body=dict(zip(BROWNS, [(36, 32, 44), (56, 48, 64), (80, 68, 92), (108, 96, 124)])),
        all={(56, 64, 88): (24, 20, 32), (72, 56, 80): (32, 28, 40)}),
}

def candles():
    """MonoMyth's purple candle cluster beside the shrine (cell 17,21; cell 18,21 the single pair): both layers,
    keyed off the icy brick by colour (the candles are purple, their flames orange and yellow)."""
    L = layout(u32(0x86D73C)); c = map_cells(L); W = L['w']; ts = TS(L)
    out = np.zeros((16, 32, 4), np.uint8)
    for i in range(2):
        t = ts.meta(c[21 * W + 17 + i] & 0x3FF)
        for y in range(16):
            for x in range(16):
                r, g, b = (int(v) for v in t[y, x])
                purple = b > g + 30 and r > g          # the wax
                flame = r > 200 and b < 90             # the flame
                if purple or flame: out[y, i * 16 + x, :3] = (r, g, b); out[y, i * 16 + x, 3] = 255
    return out

def paste(img, spr, tx, ty_bottom):
    """spr's bottom-left on tile (tx, ty_bottom)."""
    h, w = spr.shape[:2]; y0 = (ty_bottom + 1) * 16 - h; x0 = tx * 16
    m = spr[..., 3] > 0; img[y0:y0 + h, x0:x0 + w][m] = spr[..., :3][m]

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    src = cut()
    Image.fromarray(src).save(os.path.join(outdir, 'mm_shrine_cut.png'))
    vs = {k: recolour(src, s) for k, s in SCHEMES.items()}
    for k, v in vs.items(): Image.fromarray(v).save(os.path.join(outdir, 'shrine_%s.png' % k))
    # 1: the options side by side, 4x, on Pelluca's dock brick
    harb = np.array(Image.open(os.path.join(outdir, 'harbour.png')).convert('RGB'))
    floor = harb[12 * 16:12 * 16 + 16, 34 * 16:34 * 16 + 16]
    S = np.tile(floor, (4, 3 * 3 + 1, 1))[:64, :16 * 10].copy()
    for i, s in enumerate([src] + list(vs.values())):
        m = s[..., 3] > 0; S[8:56, 8 + i * 52:8 + i * 52 + 32][m] = s[..., :3][m]
    im = Image.fromarray(S).resize((S.shape[1] * 4, S.shape[0] * 4), 0); d = ImageDraw.Draw(im)
    for i, n in enumerate(['MonoMyth original', 'A: Pelluca slate', 'B: Umbra black']): d.text((32 + i * 208, 2), n, fill=(255, 255, 0))
    im.save(os.path.join(outdir, 'shrine_options.png'))
    # 2: on the dock. The old shrine and its candelabras are cleared with the brick floor; two placements.
    for k, v in vs.items():
        panels = []
        for label, (tx, tyb) in [('in its old place, below the stairs', (37, 12)), ('against the cliff, right of the stairs', (40, 10))]:
            img = harb.copy()
            for y in (10, 11):
                for x in (36, 37, 38, 39, 40): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = floor
            if tx == 40: img[9 * 16:10 * 16, 40 * 16:42 * 16] = np.tile(floor, (1, 2, 1))   # the right planter moves
            paste(img, v, tx, tyb); cd = candles()
            paste(img, cd[:, :16], tx - 1, tyb); paste(img, cd[:, 16:], tx + 2, tyb)
            p = Image.fromarray(img[3 * 16:17 * 16, 30 * 16:47 * 16]).resize((17 * 32, 14 * 32), 0)
            ImageDraw.Draw(p).text((4, 4), '%s: %s' % (k[0], label), fill=(255, 255, 0)); panels.append(p)
        S2 = Image.new('RGB', (panels[0].width * 2 + 8, panels[0].height))
        for i, p in enumerate(panels): S2.paste(p, (i * (p.width + 8), 0))
        S2.save(os.path.join(outdir, 'dock_mock_%s.png' % k))

if __name__ == '__main__':
    main(sys.argv[1])
