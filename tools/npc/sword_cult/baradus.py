"""Baradus in Sword Cult colours: icy sky-blue glasses and trim on his black coat (user 2026-11-25).

One set of rules for every asset, so they agree:
  * glasses: option A tints the lenses ice (frames as they are); option B makes the frames ice (lenses dark)
  * collar and cuffs: coat pixels touching neck or hand skin become ice piping
  * the battle front also gets an ice hem line where the coat ends
Each palette frees three slots for the ice by merging near-duplicate blacks (differences of a few levels).

Mock only: writes out/baradus_*_{A,B}.png and /tmp/cult/baradus_mock.png. Nothing in codebase/ is touched.
"""
import os

import numpy as np
from PIL import Image, ImageDraw

from sword_cult import ICE, HERE, OUT

CB = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'codebase'))
ASSETS = {
    'front': 'graphics/trainers/front_pics/baradus.png',
    'ow': 'graphics/object_events/pics/people/baradus.png',
    'positive': 'graphics/portraits/baradus_positive.png',
    'anger': 'graphics/portraits/baradus_anger.png',
    'negative': 'graphics/portraits/baradus_negative.png',
}
ICE3 = ICE[:3]          # light, mid, shade


def load(rel):
    im = Image.open(os.path.join(CB, rel))
    assert im.mode == 'P'
    pal = im.getpalette()[:48]
    pal += [0] * (48 - len(pal))
    return np.array(im), [tuple(pal[k:k + 3]) for k in range(0, 48, 3)]


def free_slots(idx, pal, n, keep):
    """Merge the closest pairs of colours (by count-weighted distance) until n indices are unused."""
    idx = idx.copy()
    pal = list(pal)
    counts = lambda: {k: int((idx == k).sum()) for k in range(16)}
    merges = []
    while True:
        c = counts()
        free = [k for k in range(1, 16) if c[k] == 0]
        if len(free) >= n:
            return idx, pal, free[:n], merges
        best = None
        for a in range(1, 16):
            if c[a] == 0 or a in keep:
                continue
            for b in range(1, 16):
                if b == a or c[b] == 0:
                    continue
                d = sum((x - y) ** 2 for x, y in zip(pal[a], pal[b])) ** 0.5
                cost = d * c[a] ** 0.5
                if best is None or cost < best[0]:
                    best = (cost, a, b, d)
        _, a, b, d = best
        idx[idx == a] = b
        merges.append((a, pal[a], b, pal[b], round(d, 1)))


def neighbours(mask):
    out = np.zeros_like(mask)
    out[1:] |= mask[:-1]
    out[:-1] |= mask[1:]
    out[:, 1:] |= mask[:, :-1]
    out[:, :-1] |= mask[:, 1:]
    return out


def lens_shade(pts):
    """Glass, per lens: a thin diagonal highlight (light), the upper half mid, the lower half shade."""
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    x0, y0, y1 = min(xs), min(ys), max(ys)
    h = y1 - y0 + 1
    out = {}
    for x, y in pts:
        d = (x - x0) + (y - y0)
        if len(pts) == 1:
            out[(x, y)] = 1
        elif h >= 4 and d in (2, 3) or h < 4 and d == 0:
            out[(x, y)] = 0
        elif (y - y0) < h / 2:
            out[(x, y)] = 1
        else:
            out[(x, y)] = 2
    return out


def split_lenses(pts):
    """Two lenses: split the lens pixels at the widest empty column gap."""
    xs = sorted(set(p[0] for p in pts))
    gaps = [(xs[k + 1] - xs[k], xs[k]) for k in range(len(xs) - 1)]
    if not gaps:
        return [pts]
    g, at = max(gaps)
    if g < 2:
        return [pts]
    return [[p for p in pts if p[0] <= at], [p for p in pts if p[0] > at]]


# ---- per-asset geometry (read from the index dumps, 2026-11-25) ----

def glasses_front(idx):
    """64x64 front: the glasses are the dark band at rows 8-9. Row 8 is the black top line (as on the
    portraits: the rim under his hair stays black); the glass is row 9 (x 26-27 and 30-32). The frame is the
    bridge (28-29, 8) and the temple ends (25, 8), (33, 8). Returns (glass, frame)."""
    glass = [(26, 9), (27, 9), (30, 9), (31, 9), (32, 9)]
    frame = [(25, 8), (28, 8), (29, 8), (33, 8)]
    return glass, frame


def glasses_ow(idx):
    """Overworld, each face frame: the glasses are two rows holding F (15, black) over A (10). The F row is the
    black top line; the glass is the A pixels; the frame is the index-3 pixels on those two rows."""
    glass, frame = [], []
    for f in range(9):
        sub = idx[:, f * 16:(f + 1) * 16]
        top = [y for y in range(16, 25) if (sub[y, 2:14] == 15).any()]
        if not top:
            continue
        rows = (top[0], top[0] + 1)
        for y in rows:
            for x in range(2, 14):
                v = sub[y, x]
                if v == 10 and y == rows[1]:
                    glass.append((f * 16 + x, y))
                elif v == 3:
                    frame.append((f * 16 + x, y))
    return glass, frame


PORTRAIT_FRAME = ((104, 104, 128), (72, 72, 97))


def glasses_portrait(idx, pal):
    """Frames are the two grey-blues. Glass is black inside the glasses band that touches only black or frame:
    a black pixel touching anything else (hair, skin, transparency) is a line, the rim drawn in black where
    the grey frame is absent or the face outline (user 2026-11-25: the top row under his hair is a black
    line, not glass), so it stays black. Returns (glass, frame)."""
    fi = [k for k in range(16) if pal[k] in PORTRAIT_FRAME]
    black = pal.index((0, 0, 0))
    fm = np.isin(idx, fi)
    fm[:30] = False
    fm[52:] = False
    ys, xs = np.nonzero(fm)
    y0, y1, x0, x1 = ys.min(), ys.max(), xs.min(), xs.max()          # the glasses band
    h, w = idx.shape
    glass = []
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if idx[y, x] != black:
                continue
            ok = True
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                v = idx[ny, nx] if 0 <= nx < w and 0 <= ny < h else 0
                if v != black and v not in fi:
                    ok = False
            if ok:
                glass.append((x, y))
    frame = list(zip(xs.tolist(), ys.tolist()))
    return glass, frame


def trim_mask(idx, pal, skin, coat, top):
    """Coat pixels touching skin below row `top` (collar V and cuffs)."""
    sk = np.isin(idx, skin)
    sk[:top] = False
    co = np.isin(idx, coat)
    co[:top] = False
    return co & neighbours(sk)


def shade_trim(idx, mask, pal):
    """Ice piping: light on pixels whose coat colour is lighter, shade on the darker ones."""
    out = {}
    for y, x in zip(*np.nonzero(mask)):
        l = sum(pal[idx[y, x]])
        out[(x, y)] = 1 if l >= 105 else 2
    return out


def apply(rel, option):
    idx, pal = load(rel)
    name = [k for k, v in ASSETS.items() if v == rel][0]
    black_like = lambda c: max(c) < 60 and max(c) - min(c) < 10
    coat = [k for k in range(1, 16) if black_like(pal[k]) and pal[k] != (0, 0, 0)]
    if name == 'front':
        lens, frame = glasses_front(idx)
        skin, top = [1, 14], 12
    elif name == 'ow':
        lens, frame = glasses_ow(idx)
        skin, top = [1, 2], 22
    else:
        lens, frame = glasses_portrait(idx, pal)
        skin, top = [k for k in range(16) if pal[k][0] > 90 and pal[k][0] - pal[k][2] > 40], 64
    tm = trim_mask(idx, pal, skin, coat, top)
    if name == 'ow':                                        # per frame: the collar starts below the neck
        tm[:] = False
        for f in range(9):
            sub = idx[:, f * 16:(f + 1) * 16]
            g = [y for y in range(16, 25) if (sub[y, 2:14] == 15).any()]
            t = g[0] + 3 if g else 23
            m = trim_mask(sub, pal, skin, coat, t)
            m[t + 2:] = False                               # collar only: cuffs at 16 px read as gloves
            m[:, :4] = False
            m[:, 12:] = False                               # the neck's columns, not a swinging hand
            tm[:, f * 16:(f + 1) * 16] = m
    if name == 'front':                                     # the hem where the coat ends
        for x in range(25, 36):
            if idx[38, x] in coat:
                tm[38, x] = True
    paint = {}
    paint.update(shade_trim(idx, tm, pal))
    if option == 'A':
        if name == 'ow':
            for f in range(9):
                fl = [p for p in lens if f * 16 <= p[0] < f * 16 + 16]
                for one in split_lenses(fl):
                    if one:
                        paint.update(lens_shade(one))
        else:
            for one in split_lenses(lens):
                paint.update(lens_shade(one))
    else:
        lit = {p: sum(pal[idx[p[1], p[0]]]) for p in frame}
        cut = (max(lit.values()) + min(lit.values())) / 2 if lit else 0
        for p in frame:                                      # keep the frame's own two-tone shading
            paint[p] = 1 if lit[p] > cut or len(set(lit.values())) == 1 else 2
    keep = set(int(idx[y, x]) for (x, y) in lens + frame)   # don't merge away what the glasses use
    idx2, pal2, slots, merges = free_slots(idx, pal, 3, keep=set())
    for k, c in zip(slots, ICE3):
        pal2[k] = c
    for (x, y), t in paint.items():
        idx2[y, x] = slots[t]
    return idx2, pal2, merges


def to_image(idx, pal):
    im = Image.fromarray(idx.astype(np.uint8), 'P')
    flat = [v for c in pal for v in c]
    im.putpalette(flat + [0] * (768 - len(flat)))
    return im


def rgba(idx, pal, bg=(110, 110, 125)):
    a = np.zeros(idx.shape + (4,), np.uint8)
    for k in range(16):
        m = idx == k
        a[m, :3] = pal[k] if k else bg
    a[..., 3] = 255
    return Image.fromarray(a)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    rows = []
    for name, rel in ASSETS.items():
        idx, pal = load(rel)
        row = [('now', rgba(idx, pal))]
        for opt in 'AB':
            i2, p2, merges = apply(rel, opt)
            to_image(i2, p2).save(os.path.join(OUT, f'baradus_{name}_{opt}.png'))
            row.append((opt, rgba(i2, p2)))
            if opt == 'A':
                print(name, 'merged:', merges)
        rows.append((name, row))
    # board: each asset at a scale that fills ~240 px
    s_for = {'front': 4, 'ow': 3, 'positive': 3, 'anger': 3, 'negative': 3}
    W = 1500
    H = 0
    for name, row in rows:
        H += max(im.height for _, im in row) * s_for[name] + 30
    c = Image.new('RGB', (W, H + 40), (36, 36, 44))
    d = ImageDraw.Draw(c)
    d.text((10, 10), 'Baradus: now | A ice lenses | B ice frames   (collar and cuffs piped ice; front also a hem)', fill=(240, 220, 120))
    y = 40
    for name, row in rows:
        s = s_for[name]
        x = 10
        for lab, im in row:
            z = im.resize((im.width * s, im.height * s), Image.NEAREST)
            if x + z.width > W:
                break
            c.paste(z, (x, y))
            d.text((x, y + z.height + 2), f'{name} {lab}', fill=(230, 230, 230))
            x += z.width + 20
        y += max(im.height for _, im in row) * s + 30
    c.save('/tmp/cult/baradus_mock.png')
    print(c.size)
