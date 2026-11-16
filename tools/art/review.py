#!/usr/bin/env python3
"""review.py -- the measurable half of tools/art/REVIEW_CHECKLIST.md, run on EVERY sprite before
it is shown to the user.  GBA rules + pixel-art-studio's validations/sharp_edges + codixel's
"count what each step changed, and where".

    python3 tools/art/review.py CANDIDATE.png --mode portrait|battle|overworld
        [--prev PREVIOUS.png]          # the version before this change (or the original art)
        [--allow x0,y0,x1,y1 ...]      # boxes the change was MEANT to touch (inclusive)
        [--ref REF.png ...]            # references to put on the sheet (MonoMyth, original art)
        [--sheet OUT.png]              # 1x + zoom sheet: refs | prev | candidate | diff

Exit status 1 when a hard rule fails (palette over budget, art cut by the frame, changes outside
--allow).  Everything else is reported for the written critique.
"""
import argparse, sys
import numpy as np
from PIL import Image, ImageDraw

MODES = {'portrait': ((80, 80), 'bottom'),      # 80x80 bust, may be cut by the BOTTOM edge only
         'battle': ((64, 64), 'bottom'),
         'overworld': ((16, 32), 'bottom')}     # sheet of 16x32 frames; feet stand on the bottom edge


def load(path):
    im = Image.open(path)
    if im.mode == 'P':
        idx = np.array(im).astype(int)
        pal = np.array((im.getpalette() + [0] * 768)[:768]).reshape(256, 3)
        tr = im.info.get('transparency', 0)
        op = idx != (tr if isinstance(tr, int) else 0)
        rgb = pal[idx]
        return rgb, op, idx, pal[:max(16, idx.max() + 1)]
    a = np.array(im.convert('RGBA')).astype(int)
    return a[..., :3], a[..., 3] >= 128, None, None


def frames(shape, mode):
    (fw, fh), _ = MODES[mode]
    H, W = shape
    if (W, H) == (fw, fh) or mode != 'overworld': return [(0, 0, W, H)]
    return [(x, 0, x + fw, fh) for x in range(0, W, fw)]


def lum(c): return 0.299 * c[..., 0] + 0.587 * c[..., 1] + 0.114 * c[..., 2]


def check(path, mode, prev=None, allow=()):
    rgb, op, idx, pal = load(path)
    H, W = op.shape
    hard, notes = [], []
    (fw, fh), cut_ok = MODES[mode]
    if mode != 'overworld' and (W, H) != (fw, fh): hard.append('size %dx%d, expected %dx%d' % (W, H, fw, fh))
    if mode == 'overworld' and (H != fh or W % fw): hard.append('sheet %dx%d is not N x 16x32 frames' % (W, H))
    # palette ---------------------------------------------------------------------------------
    cols = sorted({tuple(c) for c in rgb[op].tolist()})
    if len(cols) > 15: hard.append('%d opaque colours (4bpp budget is 15 + transparent)' % len(cols))
    g555 = {}
    for c in cols: g555.setdefault(tuple(v >> 3 for v in c), []).append(c)
    coll = [v for v in g555.values() if len(v) > 1]
    if coll: notes.append('colours that become IDENTICAL on GBA (15-bit): %s -- wasted slots' % coll)
    near = [(a, b) for i, a in enumerate(cols) for b in cols[i + 1:]
            if np.sqrt(sum((x - y) ** 2 for x, y in zip(a, b))) < 20 and (a, b) not in coll]
    if near: notes.append('near-duplicate colours (<20 apart, each must earn its slot): %s' % near[:8])
    if idx is not None:
        used = set(np.unique(idx[op]).tolist()); notes.append('palette slots used: %d' % len(used))
    # silhouette / frame edges ----------------------------------------------------------------
    pop_ = load(prev)[1] if prev else None
    for (x0, y0, x1, y1) in frames(op.shape, mode):
        def cut(m):
            f = m[y0:y1, x0:x1]
            e = {'top': f[0].any(), 'left': f[:, 0].any(), 'right': f[:, -1].any(), 'bottom': f[-1].any()}
            return {k for k, v in e.items() if v and not (k == 'bottom' and cut_ok == 'bottom')}
        bad = cut(op); old = cut(pop_) if pop_ is not None and pop_.shape == op.shape else set()
        if bad - old: hard.append('frame @x%d: art touches the %s edge (cut off)' % (x0, '/'.join(sorted(bad - old))))
        if bad & old: notes.append('frame @x%d: touches the %s edge in the previous version too (pre-existing)' % (x0, '/'.join(sorted(bad & old))))
    P = np.pad(op, 1)
    n4 = P[:-2, 1:-1].astype(int) + P[2:, 1:-1] + P[1:-1, :-2] + P[1:-1, 2:]
    nubs = np.argwhere(op & (n4 <= 1))
    holes = np.argwhere(~op & (n4 == 4))
    if len(nubs): notes.append('1-px nubs on the silhouette (x,y): %s' % [tuple(int(v) for v in p[::-1]) for p in nubs[:12]])
    if len(holes): notes.append('enclosed 1-px holes (x,y): %s' % [tuple(int(v) for v in p[::-1]) for p in holes[:12]])
    # outline: silhouette pixels must be dark (no light pixel bleeding to transparency)
    edge = op & (n4 < 4)
    if cut_ok == 'bottom': edge[-1] = False         # the bust meets the frame bottom by design
    L = lum(rgb.astype(float))
    light_edge = np.argwhere(edge & (L > 90))
    if len(light_edge): notes.append('outline holes -- light px on the silhouette edge (x,y): %s' % [tuple(int(v) for v in p[::-1]) for p in light_edge[:12]])
    # isolated pixels (pixel-art-studio's definition): opaque specks with no opaque 8-neighbour
    n8 = sum(P[1 + dy:H + 1 + dy, 1 + dx:W + 1 + dx].astype(int) for dy in (-1, 0, 1) for dx in (-1, 0, 1) if dy or dx)
    iso = [tuple(int(v) for v in p[::-1]) for p in np.argwhere(op & (n8 == 0))]
    if iso: notes.append('%d floating specks (dirt at 1x unless deliberate): %s' % (len(iso), iso[:15]))
    # change vs previous ----------------------------------------------------------------------
    diff = None
    if prev:
        prgb, pop, _, _ = load(prev)
        if prgb.shape != rgb.shape: hard.append('prev is %s, candidate %s' % (prgb.shape[:2], rgb.shape[:2]))
        else:
            diff = (op != pop) | (op & pop & (np.abs(rgb - prgb).max(-1) > 8))
            ys, xs = np.nonzero(diff)
            if len(ys):
                notes.append('changed vs prev: %d px, bbox x%d-%d y%d-%d, rows %s' % (
                    len(ys), xs.min(), xs.max(), ys.min(), ys.max(), sorted(set(ys.tolist()))))
                if allow:
                    ok = np.zeros_like(diff)
                    for (a, b, c, d) in allow: ok[b:d + 1, a:c + 1] = True
                    out = np.argwhere(diff & ~ok)
                    if len(out): hard.append('%d px changed OUTSIDE the intended area (x,y): %s' % (len(out), [tuple(int(v) for v in p[::-1]) for p in out[:12]]))
            else: notes.append('changed vs prev: 0 px -- the step did nothing')
    return hard, notes, (rgb, op, diff)


def to_img(path, bg=(110, 110, 132)):
    rgb, op, _, _ = load(path)
    a = np.zeros(op.shape + (3,), np.uint8); a[:] = bg; a[op] = rgb[op]
    return Image.fromarray(a)


def sheet(out, cand, prev, refs, diff):
    items = [(r, to_img(r)) for r in refs] + ([('prev', to_img(prev))] if prev else []) + [('candidate', to_img(cand))]
    if diff is not None:
        d = np.array(to_img(cand)).copy(); d[diff] = (255, 40, 40); items.append(('changed px', Image.fromarray(d)))
    h = max(i.height for _, i in items); Z = max(1, min(6, 480 // h))
    W = sum(i.width * Z + i.width + 12 for _, i in items)
    S = Image.new('RGB', (W, h * Z + 20), (30, 30, 36)); dr = ImageDraw.Draw(S); x = 0
    for lab, im in items:
        S.paste(im.resize((im.width * Z, im.height * Z), Image.NEAREST), (x, 16))
        S.paste(im, (x + im.width * Z + 4, 16))                      # true 1x beside the zoom
        dr.text((x, 2), lab.split('/')[-1][:28], fill=(255, 255, 120)); x += im.width * Z + im.width + 12
    S.save(out)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('png'); ap.add_argument('--mode', required=True, choices=MODES)
    ap.add_argument('--prev'); ap.add_argument('--ref', nargs='*', default=[]); ap.add_argument('--sheet')
    ap.add_argument('--allow', nargs='*', default=[])
    a = ap.parse_args()
    allow = [tuple(int(v) for v in s.split(',')) for s in a.allow]
    hard, notes, (_, _, diff) = check(a.png, a.mode, a.prev, allow)
    print('REVIEW', a.png, '[%s]' % a.mode)
    for h in hard: print('  FAIL ', h)
    for n in notes: print('  note ', n)
    print('  verdict (measured):', 'FIX' if hard else 'pass -- now do the written critique (REVIEW_CHECKLIST.md)')
    if a.sheet: sheet(a.sheet, a.png, a.prev, a.ref, diff); print('  sheet ->', a.sheet)
    sys.exit(1 if hard else 0)
