"""Sword Cult outfits: black with icy sky-blue trim (user 2026-11-25).

Sources (the user's, 2026-11-25), halved to native scale by extract():
  src_cardinal_front.png  masked villain front (Cardinals, the unit bosses under Baradus)
  src_cardinal_ow.png     masked villain 4x4 overworld sheet (32x32 cells)
  src_acolyte_front.png   trainer030, the hooded robe (rank-and-file acolytes)
MonoMyth overworld 84 (deep blue hood) is the acolyte overworld base.

Run: python3 sword_cult.py   -> out/*.png and /tmp/cult/mock_v1.png
"""
import os
from collections import deque

import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out')
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

# Black cloth ramp, light to dark (cool, so black reads as cloth, not a hole).
BLACK = [(70, 74, 94), (46, 48, 64), (30, 32, 44), (19, 20, 29), (10, 10, 16)]
# Icy sky-blue trim, light to dark.
ICE = [(216, 244, 255), (160, 216, 248), (104, 168, 224), (64, 112, 176)]
# Charcoal for the cardinal's trousers, so they part from the cloak.
SLATE = [(78, 86, 104), (52, 58, 74), (34, 38, 50), (20, 22, 30)]


def load(name):
    return np.array(Image.open(os.path.join(HERE, name)).convert('RGBA'))


def lum(c):
    return 0.299 * c[0] + 0.587 * c[1] + 0.114 * c[2]


def ramp_map(colours, ramp):
    """Map a set of source colours onto a ramp by brightness rank."""
    cs = sorted(set(colours), key=lum, reverse=True)
    if len(cs) == 1:
        return {cs[0]: ramp[len(ramp) // 2]}
    out = {}
    for k, c in enumerate(cs):
        out[c] = ramp[round(k * (len(ramp) - 1) / (len(cs) - 1))]
    return out


def ramp_by_lum(colours, ramp, lo, hi):
    """Map colours onto a ramp by absolute brightness between hi (ramp[0]) and lo (ramp[-1])."""
    out = {}
    for c in set(colours):
        t = (hi - lum(c)) / max(1e-6, hi - lo)
        out[c] = ramp[int(round(min(1, max(0, t)) * (len(ramp) - 1)))]
    return out


def is_cloak(c):            # the masked villain's lavender-white cloth
    r, g, b = c
    return b >= r and b >= g and (b - min(r, g)) <= 40 and lum(c) > 60 or c in [(26, 26, 43), (40, 40, 56)]


def is_gold(c):
    r, g, b = c
    return r > 200 and g > 140 and b < 160 and r - b > 60


def is_green(c):
    r, g, b = c
    return g > r and g > b and g - max(r, b) >= 8 and lum(c) < 110


def is_red(c):
    r, g, b = c
    return r > 150 and g < 120 and r - g > 60 and r - b > 60


def flood(a, seeds, ok):
    h, w = a.shape[:2]
    seen = np.zeros((h, w), bool)
    q = deque(s for s in seeds if ok(s))
    for s in q:
        seen[s[1], s[0]] = True
    while q:
        x, y = q.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < w and 0 <= ny < h and not seen[ny, nx] and ok((nx, ny)):
                seen[ny, nx] = True
                q.append((nx, ny))
    return seen


def recolour_cardinal(a):
    """Cloak -> black, gold rim -> ice, trousers -> slate; the mask (inside the gold ring) stays pale."""
    a = a.copy()
    h, w = a.shape[:2]
    col = lambda x, y: tuple(int(v) for v in a[y, x, :3])
    opaque = a[..., 3] > 0
    # the mask: pale cloth connected to a red eye without crossing gold or dark outline
    reds = [(x, y) for y in range(h) for x in range(w) if opaque[y, x] and is_red(col(x, y))]
    mask = flood(a, reds, lambda p: opaque[p[1], p[0]] and (is_red(col(*p)) or (is_cloak(col(*p)) and lum(col(*p)) > 120)))
    cloth = [col(x, y) for y in range(h) for x in range(w) if opaque[y, x] and not mask[y, x] and is_cloak(col(x, y))]
    golds = [col(x, y) for y in range(h) for x in range(w) if opaque[y, x] and is_gold(col(x, y))]
    greens = [col(x, y) for y in range(h) for x in range(w) if opaque[y, x] and is_green(col(x, y))]
    m_cloth = ramp_by_lum(cloth, BLACK, 30, 235)
    m_gold = ramp_map(golds, ICE[:3])
    m_green = ramp_map(greens, SLATE)
    for y in range(h):
        for x in range(w):
            if not opaque[y, x] or mask[y, x]:
                continue
            c = col(x, y)
            for m in (m_gold, m_green, m_cloth):
                if c in m:
                    a[y, x, :3] = m[c]
                    break
    return a, mask


ACO_ROBE = [(241, 222, 198), (214, 182, 143), (158, 121, 87), (106, 81, 57), (63, 48, 34)]
# trainer030's layout (native px): face and hand above row 29, belt rows 34-40, boots from row 60.
SKIN_MAX_Y, BELT_Y, BOOTS_Y = 29, (34, 40), 60
ACO_SKIN = [(255, 213, 189), (222, 164, 123), (189, 123, 98), (176, 116, 94)]


def recolour_acolyte(a, boots_from=None):
    """Robe -> black; trim of ice at the hood rim, the cuff and the hem; boots and belt -> black leather."""
    a = a.copy()
    h, w = a.shape[:2]
    col = lambda x, y: tuple(int(v) for v in a[y, x, :3])
    opaque = a[..., 3] > 0
    robe = np.zeros((h, w), bool)
    skin = np.zeros((h, w), bool)
    for y in range(h):
        for x in range(w):
            if opaque[y, x]:
                c = col(x, y)
                robe[y, x] = c in ACO_ROBE
                skin[y, x] = c in ACO_SKIN and y < SKIN_MAX_Y
    ys = np.nonzero(robe)[0]
    boots_from = BOOTS_Y
    src = a.copy()
    rm = dict(zip(ACO_ROBE, BLACK))
    for y in range(h):
        for x in range(w):
            if not opaque[y, x]:
                continue
            c = tuple(int(v) for v in src[y, x, :3])
            if robe[y, x]:
                a[y, x, :3] = rm[c]
            elif c in ((153, 78, 51), (176, 116, 94)):
                if y >= BOOTS_Y:                                    # boots -> black leather
                    a[y, x, :3] = BLACK[3] if c == (153, 78, 51) else BLACK[1]
                elif BELT_Y[0] <= y <= BELT_Y[1]:                   # belt -> ice
                    a[y, x, :3] = ICE[2]
                else:                                               # wrist and back shading -> robe shadow
                    a[y, x, :3] = BLACK[3]
            elif c == (197, 172, 82):                               # buckle
                a[y, x, :3] = ICE[0]
    trim = np.zeros((h, w), bool)
    # the hood rim and the cuffs: robe pixels touching skin
    for y in range(h):
        for x in range(w):
            if robe[y, x]:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < w and 0 <= ny < h and skin[ny, nx]:
                        trim[y, x] = True
    # the hem: the lowest robe pixel of each column above the boots
    for x in range(w):
        col_ys = [y for y in range(h) if robe[y, x]]
        if col_ys and col_ys[-1] >= boots_from - 6:
            trim[col_ys[-1], x] = True
    for y in range(h):
        for x in range(w):
            if trim[y, x]:
                light = lum(tuple(int(v) for v in src[y, x, :3])) > 150
                a[y, x, :3] = ICE[1] if light else ICE[2]
    return a


def extract():
    up = '/mnt/user-data/uploads'
    srcs = {'cardinal_front': ('44c3f187', 1), 'cardinal_ow': ('a9ee4127', 0), 'acolyte_front': ('bc5c47da', 0)}
    for k, (p, o) in srcs.items():
        a = np.array(Image.open(f'{up}/{p}-image.png').convert('RGBA'))[o::2, o::2]
        Image.fromarray(a).save(os.path.join(HERE, f'src_{k}.png'))


def fit64(a):
    """Crop to the figure and scale to fit 64x64 whole (user: 'the shrinking works'), bottom-aligned."""
    ys, xs = np.nonzero(a[..., 3])
    a = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    h, w = a.shape[:2]
    s = min(64 / h, 64 / w, 1.0)
    im = Image.fromarray(a)
    if s < 1:
        im = im.resize((max(1, round(w * s)), max(1, round(h * s))), Image.NEAREST)
    c = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    c.alpha_composite(im, ((64 - im.width) // 2, 64 - im.height))
    return np.array(c)


def board(items, path, scale=3):
    pad = 12
    ims = [Image.fromarray(a) for a, _ in items]
    W = sum(i.width * scale + pad for i in ims) + pad
    H = max(i.height * scale for i in ims) + 2 * pad + 14
    from PIL import ImageDraw
    c = Image.new('RGBA', (W, H), (110, 110, 125, 255))
    d = ImageDraw.Draw(c)
    x = pad
    for i, (_, label) in zip(ims, items):
        c.alpha_composite(i.resize((i.width * scale, i.height * scale), Image.NEAREST), (x, pad))
        d.text((x, H - pad - 10), label, fill=(240, 240, 240, 255))
        x += i.width * scale + pad
    c.save(path)
    return c


def ow9(a, cw, ch):
    """Essentials 4x4 (rows down, left, right, up; columns stand, step, stand, step) -> Emerald's 9 frames:
    S, N, W, walk S x2, walk N x2, walk W x2."""
    f = lambda r, c: a[r * ch:(r + 1) * ch, c * cw:(c + 1) * cw]
    order = [f(0, 0), f(3, 0), f(1, 0), f(0, 1), f(0, 3), f(3, 1), f(3, 3), f(1, 1), f(1, 3)]
    return np.concatenate(order, axis=1)


MM = os.path.join(REPO, 'assets', 'npc_survey', 'mm_frames')
NAVY_217 = [(104, 104, 136), (72, 72, 112), (48, 48, 88), (32, 24, 48), (0, 0, 16)]
GOLD_217 = {(240, 192, 72): ICE[1], (208, 168, 80): ICE[2], (72, 48, 24): ICE[3]}
NAVY_HOOD = {(72, 72, 128): BLACK[1], (48, 48, 88): BLACK[2], (24, 24, 48): BLACK[3], (0, 0, 0): BLACK[4]}
HOOD_SKIN = [(208, 152, 128), (200, 128, 96), (120, 64, 64), (216, 184, 160)]


def acolyte_walker():
    """MonoMyth 217 (navy hooded robe, gold band and face plate; all 9 frames) -> black with ice."""
    a = np.array(Image.open(os.path.join(MM, '217.png')).convert('RGBA'))
    m = dict(zip(NAVY_217, [BLACK[0], BLACK[1], BLACK[2], BLACK[3], (0, 0, 0)]))
    m.update(GOLD_217)
    for y, x in zip(*np.nonzero(a[..., 3])):
        c = tuple(int(v) for v in a[y, x, :3])
        if c in m:
            a[y, x, :3] = m[c]
    return a


def acolyte_kneeler():
    """MonoMyth 84/89/90: one hunched hooded figure in three facings (east, south, west), no north and no
    walk. -> black hood, ice piping round the face opening. Returns S, W, E (static frames)."""
    out = []
    for n in ('89', '90', '84'):
        a = np.array(Image.open(os.path.join(MM, n + '.png')).convert('RGBA'))[:, 32:48].copy()   # frame 2: face showing
        h, w = a.shape[:2]
        skin = np.zeros((h, w), bool)
        hood = np.zeros((h, w), bool)
        for y, x in zip(*np.nonzero(a[..., 3])):
            c = tuple(int(v) for v in a[y, x, :3])
            skin[y, x] = c in HOOD_SKIN
            hood[y, x] = c in NAVY_HOOD and c != (0, 0, 0)
        src = a.copy()
        for y, x in zip(*np.nonzero(a[..., 3])):
            c = tuple(int(v) for v in src[y, x, :3])
            if c in NAVY_HOOD:
                a[y, x, :3] = NAVY_HOOD[c]
        # the face's own black outline, then the hood pixels touching that outline: the opening's rim
        n4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
        near = lambda m, y, x: any(0 <= y + dy < h and 0 <= x + dx < w and m[y + dy, x + dx] for dx, dy in n4)
        dark = (a[..., 3] > 0) & (src[..., :3].max(-1) < 30)
        ring = np.zeros((h, w), bool)
        for y, x in zip(*np.nonzero(dark)):
            ring[y, x] = near(skin, y, x)
        for y, x in zip(*np.nonzero(hood)):
            if (near(skin, y, x) or near(ring, y, x)) and y < 24:
                a[y, x, :3] = ICE[1] if lum(tuple(int(v) for v in src[y, x, :3])) > 60 else ICE[2]
        out.append(a)
    return out


def fit64_snap(a):
    """Shrink to fit 64x64 by area averaging, then snap every pixel back to the sprite's own colours, so
    one-pixel trim lines survive better than with nearest-neighbour. Bottom-aligned, centred."""
    ys, xs = np.nonzero(a[..., 3])
    a = a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    h, w = a.shape[:2]
    s = min(64 / h, 64 / w, 1.0)
    cols = np.array(sorted(set(tuple(int(v) for v in p[:3]) for p in a.reshape(-1, 4) if p[3] > 0)), float)
    if s < 1:
        nw, nh = max(1, round(w * s)), max(1, round(h * s))
        pm = a.astype(float)
        pm[..., :3] *= pm[..., 3:4] / 255.0                 # premultiply so transparency doesn't grey edges
        sm = np.array(Image.fromarray(pm.astype(np.uint8)).resize((nw, nh), Image.BOX)).astype(float)
        al = sm[..., 3]
        rgb = np.where(al[..., None] > 0, sm[..., :3] * 255.0 / np.maximum(al[..., None], 1), 0)
        out = np.zeros((nh, nw, 4), np.uint8)
        for y in range(nh):
            for x in range(nw):
                if al[y, x] >= 128:
                    d = ((cols - rgb[y, x]) ** 2).sum(1)
                    out[y, x, :3] = cols[d.argmin()]
                    out[y, x, 3] = 255
        a = out
    c = np.zeros((64, 64, 4), np.uint8)
    h, w = a.shape[:2]
    c[64 - h:, (64 - w) // 2:(64 - w) // 2 + w] = a
    return c


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    os.makedirs('/tmp/cult', exist_ok=True)
    cf = load('src_cardinal_front.png')
    cf2, _ = recolour_cardinal(cf)
    co = load('src_cardinal_ow.png')
    co2, _ = recolour_cardinal(co)
    af = load('src_acolyte_front.png')
    af2 = recolour_acolyte(af)
    for n, a in (('cardinal_front', cf2), ('cardinal_ow_sheet', co2), ('acolyte_front', af2)):
        Image.fromarray(a).save(os.path.join(OUT, n + '.png'))
    board([(cf, 'cardinal (yours)'), (cf2, 'cardinal v1'), (af, 'acolyte (yours)'), (af2, 'acolyte v1')],
          '/tmp/cult/fronts_v1.png', 4)
    board([(co, 'yours'), (co2, 'v1')], '/tmp/cult/ow_v1.png', 3)
    card9 = ow9(co2, 32, 32)
    walker = acolyte_walker()
    kneel = acolyte_kneeler()
    for n, a in (('cardinal_ow', card9), ('acolyte_ow', walker)):
        Image.fromarray(a).save(os.path.join(OUT, n + '.png'))
    for n, a in zip(('S', 'W', 'E'), kneel):
        Image.fromarray(a).save(os.path.join(OUT, 'acolyte_kneel_%s.png' % n))
    mm217 = np.array(Image.open(os.path.join(MM, '217.png')).convert('RGBA'))
    fits = []
    for n, a in (('cardinal', cf2), ('acolyte', af2)):
        nn, sn = fit64(a), fit64_snap(a)
        Image.fromarray(nn).save(os.path.join(OUT, n + '_front_64.png'))   # nearest keeps the trim lines whole
        fits += [(nn, n + ' nearest'), (sn, n + ' area+snap')]
    board(fits, '/tmp/cult/fit64_v1.png', 5)
    board([(mm217, 'MonoMyth 217'), (walker, 'acolyte walker')], '/tmp/cult/walker_v1.png', 4)
    board([(card9, 'cardinal, Emerald 9 frames')], '/tmp/cult/card9_v1.png', 3)
    board([(k, l) for k, l in zip(kneel, ('kneel S', 'kneel W', 'kneel E'))], '/tmp/cult/kneel_v1.png', 5)
