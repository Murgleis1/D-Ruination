"""The older noblewoman class (user 2026-11-25): three of the user's designs ('socialite' fronts 1-3), each in three
colourways (outfit, hair, skin), fronts fitted to 64x64; overworlds from MonoMyth bodies at our cast's size (the
user's own overworld sheets are Gen 4 size, a head taller than MonoMyth's people): design 1 = MonoMyth 24 with a
brimmed hat drawn on (no MonoMyth old woman wears one), design 2 = MonoMyth 16 (grey bun, lilac dress), design 3 =
MonoMyth 24 (long white hair).

Run: python3 dowager.py  -> out/*.png, /tmp/cult/dowager_v1.png"""
import colorsys
import os
import sys

import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
sys.path.insert(0, os.path.join(HERE, '..', 'sword_cult'))
from sword_cult import fit64      # crop to the figure, nearest-shrink to fit 64x64, bottom-aligned


def lum(c):
    return 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]


def ramp_to(colours, hue, sat, vscale=1.0, vlift=0.0):
    """Recolour a part: each source colour keeps its brightness (HSV value, scaled), takes the target hue, and a
    saturation that follows the source's own (darker shades a little richer)."""
    out = {}
    vs = [colorsys.rgb_to_hsv(*[x / 255 for x in c])[2] for c in colours]
    vmax = max(vs) if vs else 1
    for c, v in zip(colours, vs):
        t = v / vmax if vmax else 1
        s = min(1.0, sat * (1.25 - 0.35 * t))
        nv = min(1.0, max(0.0, v * vscale + vlift))
        r, g, b = colorsys.hsv_to_rgb(hue / 360, s, nv)
        out[c] = (round(r * 255), round(g * 255), round(b * 255))
    return out


def ramp_exact(colours, targets):
    """Map source colours (by brightness rank) onto an explicit ramp, light to dark."""
    cs = sorted(colours, key=lum, reverse=True)
    if len(cs) == 1:
        return {cs[0]: targets[len(targets) // 2]}
    return {c: targets[round(k * (len(targets) - 1) / (len(cs) - 1))] for k, c in enumerate(cs)}


SKIN = {
    'fair': None,                                                        # as drawn
    'medium': [(240, 196, 156), (214, 156, 112), (176, 116, 82), (132, 82, 58)],
    'bronzed': [(206, 148, 102), (166, 110, 72), (128, 80, 52), (92, 56, 38)],   # the Yo'aki tone (Baradus)
}
HAIR = {
    'as drawn': None,
    'white': [(252, 252, 252), (226, 228, 236), (190, 192, 204), (140, 142, 156)],
    'silver': [(232, 234, 244), (200, 204, 218), (156, 160, 178), (108, 110, 126)],
    'iron grey': [(196, 196, 200), (156, 156, 162), (116, 116, 124), (76, 76, 84)],
}


# Each design: the colours of each part in the user's front (some limited to a band of rows, where the same colour
# is used twice: design 2's white bag shares the hair's whites).
FRONTS = {
    1: {'src': 'src_front1.png',
        'outfit': [(205, 164, 106), (148, 123, 98), (98, 82, 74)],
        'accent': [(255, 139, 156), (180, 90, 106), (123, 74, 90), (82, 57, 65)],
        'hair': [(238, 238, 255), (213, 205, 213), (156, 156, 148), (106, 98, 98)], 'hair_rows': (0, 34),
        'skin': [(255, 213, 189), (222, 164, 123), (189, 123, 98)]},
    2: {'src': 'src_front2.png',
        'outfit': [(208, 152, 168), (160, 104, 120), (120, 72, 88)],
        'accent': [(128, 104, 176), (72, 72, 112)],
        'hair': [(248, 248, 248), (200, 200, 200), (120, 120, 144)], 'hair_rows': (0, 26),
        'skin': [(248, 208, 184), (216, 160, 120), (184, 120, 96)]},
    3: {'src': 'src_front3.png',
        'outfit': [(188, 194, 233), (168, 168, 185), (137, 144, 180), (61, 68, 95)],
        'accent': [],
        'hair': [(255, 255, 255), (225, 224, 227), (206, 206, 206)], 'hair_rows': (0, 22),
        'skin': [(255, 214, 189), (222, 164, 123), (222, 165, 123), (189, 123, 98)]},
}

# Colourways: (label, outfit (hue, sat, vscale, vlift) or None = as drawn, accent likewise, hair, skin).
# House palettes are suggestions only: just Umbra navy-and-gold and Langerin copper are on record.
VARIANTS = {
    1: [('a', 'tan and rose (as drawn)', None, None, 'as drawn', 'fair'),
        ('b', 'navy and gold', (222, 0.55, 0.78, 0.0), (44, 0.70, 1.0, 0.0), 'white', 'medium'),
        ('c', 'burgundy and cream', (348, 0.55, 0.80, 0.0), (38, 0.22, 1.0, 0.05), 'iron grey', 'bronzed')],
    2: [('a', 'mauve and violet (as drawn)', None, None, 'as drawn', 'fair'),
        ('b', 'forest green and gold', (138, 0.40, 0.85, 0.0), (44, 0.65, 1.15, 0.0), 'white', 'bronzed'),
        ('c', 'slate blue and plum', (212, 0.28, 0.95, 0.0), (318, 0.40, 1.1, 0.0), 'silver', 'medium')],
    3: [('a', 'periwinkle (as drawn)', None, None, 'as drawn', 'fair'),
        ('b', 'crimson', (354, 0.50, 0.85, 0.0), None, 'silver', 'medium'),
        ('c', 'charcoal', (228, 0.10, 0.55, 0.0), None, 'white', 'bronzed')],
}


def recolour(a, parts, var, rows_for=None):
    """parts: {'outfit': [...], 'accent': [...], 'hair': [...], 'skin': [...], 'hair_rows': (y0, y1)}."""
    _, _, outfit, accent, hair, skin = var
    maps = {}
    if outfit:
        maps['outfit'] = ramp_to(parts['outfit'], *outfit)
    if accent and parts['accent']:
        maps['accent'] = ramp_to(parts['accent'], *accent)
    if HAIR[hair]:
        maps['hair'] = ramp_exact(parts['hair'], HAIR[hair])
    if SKIN[skin]:
        maps['skin'] = ramp_exact(parts['skin'], SKIN[skin])
    out = a.copy()
    h = a.shape[0]
    y0, y1 = parts.get('hair_rows', (0, h))
    for y, x in zip(*np.nonzero(a[..., 3])):
        c = tuple(int(v) for v in a[y, x, :3])
        for part in ('hair', 'skin', 'accent', 'outfit'):
            if part in maps and c in maps[part]:
                if part == 'hair' and not (y0 <= y < y1):
                    continue
                out[y, x, :3] = maps[part][c]
                break
    return out


# ---- overworlds: MonoMyth bodies, by palette index ----
MM = {
    16: {'outfit': None, 'accent': None, 'hair': None, 'skin': None},   # filled in from its palette below
    24: {},
}


def mm_load(n):
    im = Image.open(os.path.join(HERE, 'mm_%d.png' % n))
    return np.array(im), [tuple(im.getpalette()[k:k + 3]) for k in range(0, 48, 3)]


MM_PARTS = {      # by palette index, read from each body's palette (2026-11-25)
    16: {'hair': [9, 10, 11], 'skin': [1, 2, 3, 4, 5], 'outfit': [6, 7, 8]},
    24: {'hair': [2, 3, 1], 'skin': [5, 4, 7, 6], 'outfit': [11, 10, 9]},
}


def mm_parts(n):
    return MM_PARTS[n]


def hat(idx, frame, facing, top, x0, x1, light, mid, dark, rose, rose_dark):
    """Draw a small brimmed hat (the user's design 1) on one 16x32 frame of a MonoMyth woman: crown two rows above
    the head, band and flower, brim a pixel wider than the head; the hair still shows below the brim."""
    f = idx[:, frame * 16:(frame + 1) * 16]
    O = 8
    cx0, cx1 = x0 + 2, x1 - 2                     # the crown, narrower than the head
    if facing == 'W':
        cx0, cx1 = x0 + 2, x1 - 3
    for x in range(cx0 + 1, cx1):
        f[top - 2, x] = O
    for y in (top - 1, top):
        f[y, cx0] = O
        f[y, cx1] = O
        for x in range(cx0 + 1, cx1):
            f[y, x] = light if y == top - 1 else mid
    # the band and the flower (on the viewer's right for south, at the back for west, hidden from behind)
    if facing == 'S':
        f[top, cx1 - 2] = rose
        f[top, cx1 - 1] = rose_dark
    elif facing == 'W':
        f[top, cx1 - 1] = rose
        f[top - 1, cx1 - 1] = rose_dark
    # the brim
    bx0, bx1 = x0 - 1, x1 + 1
    if facing == 'W':
        bx0, bx1 = x0 - 2, x1
    bx0, bx1 = max(0, bx0), min(15, bx1)            # never past the frame's edge (it would wrap)
    f[top + 1, bx0] = O
    f[top + 1, bx1] = O
    for x in range(bx0 + 1, bx1):
        f[top + 1, x] = mid if facing != 'N' else light
    for x in range(bx0, bx1 + 1):
        f[top + 2, x] = O if x in (bx0, bx1) else dark
    idx[:, frame * 16:(frame + 1) * 16] = f


FACING = {0: 'S', 1: 'N', 2: 'W', 3: 'S', 4: 'S', 5: 'N', 6: 'N', 7: 'W', 8: 'W'}


def head_box(f):
    ys, xs = np.nonzero(f)
    top = ys.min()
    band = f[top:top + 4]
    bx = np.nonzero(band.any(0))[0]
    return top, bx.min(), bx.max()


def overworld(design, var):
    n = {1: 24, 2: 16, 3: 24}[design]
    idx, pal = mm_load(n)
    pal = list(pal)
    parts = mm_parts(n)
    _, _, outfit, accent, hair, skin = var
    if design == 1:
        # the coat and the hat in the front's tan; the rose in two free slots
        tan = [(205, 164, 106), (148, 123, 98), (98, 82, 74)]
        o = sorted(parts['outfit'], key=lambda k: lum(pal[k]), reverse=True)
        for k, c in zip(o, tan):
            pal[k] = c
        free = [k for k in range(1, 16) if not (idx == k).any()]
        rose, rose_dark = free[0], free[1]
        pal[rose], pal[rose_dark] = (255, 139, 156), (180, 90, 106)
        light, mid, dark = o[0], o[1], o[2]
        skin_k = parts['skin']
        for fr in range(9):
            sub = idx[:, fr * 16:(fr + 1) * 16]
            top, x0, x1 = head_box(sub)
            # the front's rose scarf at her neck: coat pixels touching her face or neck, high on the body (on the
            # tan coat the bare collar under the chin read as a beard)
            sk = np.isin(sub, skin_k)
            near = np.zeros_like(sk)
            near[1:] |= sk[:-1]; near[:-1] |= sk[1:]; near[:, 1:] |= sk[:, :-1]; near[:, :-1] |= sk[:, 1:]
            for y, x in zip(*np.nonzero(np.isin(sub, o) & near)):
                if y < top + 13 and FACING[fr] != 'N' and x0 < x < x1:   # the neck, not the hands
                    sub[y, x] = rose if sub[y, x] != o[2] else rose_dark
            idx[:, fr * 16:(fr + 1) * 16] = sub
            hat(idx, fr, FACING[fr], top + 1, x0, x1, light, mid, dark, rose, rose_dark)
        if outfit:
            m = ramp_to([pal[k] for k in o], *outfit)
            for k in o:
                pal[k] = m[pal[k]]
        if accent:
            m = ramp_to([pal[rose], pal[rose_dark]], *accent)
            pal[rose], pal[rose_dark] = m[pal[rose]], m[pal[rose_dark]]
    elif outfit:
        cols = [pal[k] for k in parts['outfit']]
        m = ramp_to(cols, *outfit)
        for k in parts['outfit']:
            pal[k] = m[pal[k]]
    elif design == 3:
        # as drawn: the front's periwinkle suit on MonoMyth 24's green dress
        o = sorted(parts['outfit'], key=lambda k: lum(pal[k]), reverse=True)
        for k, c in zip(o, [(188, 194, 233), (137, 144, 180), (61, 68, 95)]):
            pal[k] = c
    elif design == 2:
        o = sorted(parts['outfit'], key=lambda k: lum(pal[k]), reverse=True)
        for k, c in zip(o, [(208, 152, 168), (160, 104, 120), (120, 72, 88)]):
            pal[k] = c
    if design == 3 and outfit:
        pass
    if HAIR[hair]:
        hs = sorted(parts['hair'], key=lambda k: lum(pal[k]), reverse=True)
        m = ramp_exact([pal[k] for k in hs], HAIR[hair])
        for k in hs:
            pal[k] = m[pal[k]]
    sk = SKIN[skin] or ([(255, 213, 189), (222, 164, 123), (189, 123, 98)] if design == 2 else None)
    if sk:
        ss = sorted(parts['skin'], key=lambda k: lum(pal[k]), reverse=True)
        m = ramp_exact([pal[k] for k in ss], sk)
        for k in ss:
            pal[k] = m[pal[k]]
    a = np.zeros(idx.shape + (4,), np.uint8)
    for k in range(1, 16):
        a[idx == k, :3] = pal[k]
        a[idx == k, 3] = 255
    return a


def board(rows, path):
    pad = 12
    W = 1500
    H = sum(r[0].height for r in rows) + 40 * len(rows) + 50
    c = Image.new('RGBA', (W, H), (36, 36, 44, 255))
    d = ImageDraw.Draw(c)
    d.text((pad, 10), 'Older noblewoman class v1: your three designs x three colourways. Overworlds from MonoMyth at our cast\'s size.', fill=(240, 220, 120))
    y = 36
    for im, label in rows:
        d.text((pad, y), label, fill=(240, 220, 120))
        c.alpha_composite(im, (pad, y + 16))
        y += im.height + 40
    c.save(path)


def tile(a, s, bg=(110, 110, 125, 255)):
    im = Image.fromarray(a)
    c = Image.new('RGBA', im.size, bg)
    c.alpha_composite(im)
    return c.resize((im.width * s, im.height * s), Image.NEAREST)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for d in (1, 2, 3):
        parts = FRONTS[d]
        src = np.array(Image.open(os.path.join(HERE, parts['src'])).convert('RGBA'))
        strip = []
        for var in VARIANTS[d]:
            fr = fit64(recolour(src, parts, var))
            ow = overworld(d, var)
            Image.fromarray(fr).save(os.path.join(OUT, 'design%d%s_front.png' % (d, var[0])))
            Image.fromarray(ow).save(os.path.join(OUT, 'design%d%s_ow.png' % (d, var[0])))
            strip.append((tile(fr, 3), tile(ow[:, :16 * 9], 3), '%d%s %s; hair %s, skin %s' % (d, var[0], var[1], var[4], var[5])))
        W = sum(max(f.width, 16 * 9 * 3 // 2) + 30 for f, _, _ in strip)
        H = max(f.height for f, _, _ in strip) + 32 * 3 + 40
        c = Image.new('RGBA', (1470, H), (36, 36, 44, 255))
        dr = ImageDraw.Draw(c)
        x = 0
        for f, o, lab in strip:
            c.alpha_composite(f, (x, 0))
            c.alpha_composite(o.crop((0, 0, 16 * 3 * 5, 96)), (x + f.width + 6, f.height - 96))
            dr.text((x, f.height + 6), lab, fill=(230, 230, 230))
            x += 490
        rows.append((c, 'Design %d' % d))
    board(rows, '/tmp/cult/dowager_v1.png')
    print('ok')
