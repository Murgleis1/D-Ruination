"""A cap of cloud over Hollow Hill's knoll (user 2026-11-25: "put some kind of animated cloud formation above the
entrance ... it makes sense when you enter and climb up to the ruins. Right now when you look at the map from above,
it's a small flat peak"; "is it possible to obscure the peak from the outside?").
The cloud that sits on a hill's top: it hides the knoll's small flat top, so the hill reads as rising up into cloud
(the summit beyond the sealed door, much larger, is somewhere up in it). Its lowest edge stays above the sealed door's
band: the door and its forecourt stay clear.
Made from the game's own top-down cloud (Emerald's weather cloud, graphics/weather/cloud.png, 64x64), recoloured to
the fog's greys (a little violet in the shade): copies of it, some mirrored or flipped, overlapping into one mass, each
drifting slowly to and fro on its own phase, so the cap churns while it stays put. In the game: object sprites sharing
that one picture (2 KB of sprite memory), drawn under the fog, the player always in front of it.
Usage: python3 knoll_cloud.py OUTDIR [hollow_hill_render.png]"""
import sys, os, math
import numpy as np
from PIL import Image
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
FOG = {5: (222, 224, 232), 1: (204, 206, 218), 3: (182, 184, 200), 2: (160, 160, 182), 4: (134, 132, 158)}

def cloud_indices():
    """the picture as palette indices: Emerald's cloud over its own copy turned half round, so the gaps between its
    billows fill and the cap can close completely (user 2026-11-25: "make sure the clouds directly above completely
    obscure the peak")"""
    a = np.array(Image.open(os.path.join(ROOT, 'codebase/graphics/weather/cloud.png')))
    b = a[::-1, ::-1].copy(); b[a != 0] = a[a != 0]
    return b

def lens_indices():
    """the picture the game uses, 64x32 (user 2026-11-25: "make sure the clouds directly above completely obscure the
    peak"): a billow's outline (a low lens with rounded lobes along its top) filled with Emerald's cloud texture (its
    gaps filled from the nearest shade), lit along the top of each lobe and shaded along its underside; 64x32 so few
    cross any one scanline (the GBA draws only so many sprite pixels per line, the fog's included)"""
    from scipy.ndimage import distance_transform_edt
    tex = cloud_indices()[16:48].copy(); m = tex != 0
    _, (iy, ix) = distance_transform_edt(~m, return_indices=True); tex = tex[iy, ix]
    yy, xx = np.mgrid[0:32, 0:64].astype(float)
    body = ((xx - 32) / 32.5) ** 2 + ((yy - 18) / 14.0) ** 2 <= 1
    lobes = np.zeros_like(body)
    for cx, cy, r in ((12, 15, 11), (30, 11, 12), (49, 14, 11), (22, 19, 13), (42, 19, 13)):
        lobes |= (xx - cx) ** 2 + (yy - cy) ** 2 <= r * r
    shape = (body | lobes) & (yy <= 30)
    d = np.where(shape, tex, 0)
    up = shape & ~np.roll(shape, 1, 0); up[0] = shape[0]
    d[up] = 5; d[shape & ~np.roll(shape, -1, 0)] = 4                                # (lit top edge, shaded underside)
    edge = shape & ~(np.roll(shape, 1, 1) & np.roll(shape, -1, 1))
    d[edge & (yy > 16)] = 2
    return d

def to_rgba(a):
    out = np.zeros(a.shape + (4,), np.uint8)
    for i, c in FOG.items(): out[a == i, :3] = c; out[a == i, 3] = 255
    return out

def cloud(): return to_rgba(lens_indices())

def write_game_picture():
    """graphics/field_effects/pics/dr_knoll_cloud.png: the lens, indexed (0 clear, 1-5 the fog greys)"""
    a = lens_indices(); pal = [(65, 148, 255)] + [FOG[i] for i in range(1, 6)] + [(0, 0, 0)] * 10
    im = Image.fromarray(a.astype(np.uint8), 'P'); im.putpalette([v for c in pal for v in c])
    im.save(os.path.join(ROOT, 'codebase/graphics/field_effects/pics/dr_knoll_cloud.png'))

# packed close (user 2026-11-25: "bring the clouds more packed together and swirl extremely slowly in a circular
# pattern"): a still heart, an inner ring of 4 turning one way, an outer ring of 8 turning the other, on ellipses (the
# hill seen from above and in front). Each ring's copies alternate two flips, so after a quarter turn the cap looks
# as it began: the swirl loops seamlessly. Its speed in the game: a quarter turn in about 40 seconds.
# (checked over a whole turn by knoll_cloud_check(): the knoll's flat top never shows, the low door never covered;
# at most 7 of them cross any scanline)
RINGS = [(0, 0, 1, [0], 0),                                   # (x radius, y radius, turn direction, flips, start/1024)
         (30, 26, 1, [1, 2], 0),
         (52, 40, -1, [0, 3], 65)]
COUNTS = [1, 4, 8]
CY = 3                                                        # (the cap's heart below the centre point)

def placements(phase):
    """(x, y, flip) of each copy at phase 0..1 (one loop: a quarter turn)"""
    out = []
    for (rx, ry, d, flips, st), n in zip(RINGS, COUNTS):
        for j in range(n):
            a = 2 * math.pi * (st / 1024 + j / n) + d * (math.pi / 2) * phase
            out.append((rx * math.cos(a), CY + ry * math.sin(a), flips[j % len(flips)], math.sin(a)))
    return sorted(out, key=lambda p: p[3])                    # (the far side drawn first)

def compose(base, k, n, cx, cy):
    c = cloud(); out = base.copy()
    pics = [Image.fromarray(c), Image.fromarray(c[:, ::-1].copy()), Image.fromarray(c[::-1].copy()), Image.fromarray(c[::-1, ::-1].copy())]
    for x, y, fl, _ in placements(4 * k / n):              # (a whole turn over the loop)
        out.alpha_composite(pics[fl], (int(round(cx + x - 32)), int(round(cy + y - 16))))
    return out

def main(outdir, hh=None):
    os.makedirs(outdir, exist_ok=True); write_game_picture()
    Image.fromarray(cloud()).save(os.path.join(outdir, 'cloud_fog.png'))
    if hh:
        base = Image.open(hh).convert('RGBA')
        cx, cy = 29 * 16 + 8, 29 * 16 + 7                     # (as src/dr_knoll_cloud.c places it)                              # the knoll's top; the cap's foot ends above row 33
        crop = (16 * 16, 16 * 16, 44 * 16, 42 * 16)
        n = 48; seq = [compose(base, k, n, cx, cy).crop(crop) for k in range(n)]
        seq = [s.resize((s.width * 2, s.height * 2), Image.NEAREST).convert('RGB') for s in seq]
        seq[0].save(os.path.join(outdir, 'knoll_cloud.gif'), save_all=True, append_images=seq[1:], duration=200, loop=0)
        seq[0].save(os.path.join(outdir, 'knoll_cloud_still.png'))
        compose(base, 0, n, cx, cy).convert('RGB').save(os.path.join(outdir, 'knoll_cloud_full.png'))
    print(outdir)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)

# ------------------------------------------------------------------ v3: the whole top of the knoll (user 2026-11-25:
# "the WHOLE top area of the hill peak needs clouds"). Two parts, both checked over a whole lap by conveyor_check():
#  * under: every cell of the knoll above the door's band (its top and all its upper bands, the slab's top row apart)
#    is cloud in the map itself (UNDER_TEX, a cell of this cloud's texture in two greys), so no part of the peak can
#    ever show, whatever the sprites do;
#  * over: 20 billows travel slowly clockwise round that cloud's outline (a lap in 160 seconds), always covering its
#    hard cell edge with their soft outline: the cap's rim turns round the hill top. Spaced by their size (64 wide, 32
#    tall: twice as far apart along the top and bottom as down the sides), so at most 8 cross any scanline.
N_RIM = 20
LAP_FRAMES = 9600
UNDER_COLS = {0: (182, 184, 200), 1: (160, 160, 182)}

def under_cells():
    import hh_mock as HM
    E, (P1, P2, P3) = HM.rings()
    return [(x, y) for y in range(HM.H) for x in range(HM.W) if P3[y, x] and y <= 32 and not (28 <= x <= 30 and y == 32)]

def under_tex():
    """one 16x16 cell of the cloud's texture in two greys (its lighter and darker billows), tiling seamlessly"""
    a = cloud_indices()[24:40, 24:40]
    out = np.zeros((16, 16, 3), np.uint8)
    light = np.isin(a, (5, 1)); out[light] = UNDER_COLS[0]; out[~light] = UNDER_COLS[1]
    return out

def rim_path(npts=1024):
    """the billows' track: the cloud's outline brought in 4 px and smoothed, as (dx, dy) from the knoll's centre point,
    respaced so equal steps are equal in billow-widths (horizontal distance counts half); never below dy 50 (the low
    door stays clear)"""
    from scipy.ndimage import distance_transform_edt, gaussian_filter
    from skimage import measure
    H, W = 64 * 16, 66 * 16
    t = np.zeros((H, W), bool)
    for x, y in under_cells(): t[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = True
    f = gaussian_filter(distance_transform_edt(t) - 4.0, 6)
    c = max(measure.find_contours(f, 0.0), key=len)
    P = np.stack([c[:, 1] - (29 * 16 + 8), c[:, 0] - (29 * 16 + 7)], 1)
    d = np.diff(np.vstack([P, P[:1]]), axis=0); s = np.concatenate([[0], np.cumsum(np.hypot(d[:, 0] / 2, d[:, 1]))])
    q = np.linspace(0, s[-1], npts, endpoint=False); Pc = np.vstack([P, P[:1]])
    P = np.stack([np.interp(q, s, Pc[:, 0]), np.interp(q, s, Pc[:, 1])], 1)
    if np.arctan2(P[10, 1], P[10, 0]) < np.arctan2(P[0, 1], P[0, 0]): P = P[::-1]          # (clockwise on screen)
    P[:, 1] = np.minimum(P[:, 1], 50)
    side = np.abs(P[:, 0]) > 60; P[side, 0] -= np.sign(P[side, 0]) * 6       # (down the sides, 6 px in: less spills off)
    return np.rint(P).astype(int)

def write_c_path():
    P = rim_path()
    rows = ['    {%d, %d},' % (x, y) for x, y in P]
    open(os.path.join(ROOT, 'codebase/src/data/dr_knoll_cloud_path.h'), 'w').write(
        '// generated by tools/art/hollowhill/knoll_cloud.py (rim_path): the knoll cloud\'s rim billows\' track, clockwise\n'
        'static const s8 sKnollCloudPath[%d][2] = {\n%s\n};\n' % (len(P), '\n'.join(rows)))

N_INNER, INNER = 6, (48, 20, -16)

def rim_positions(frame, inner=True):
    """(dx, dy) and flip of every billow at a frame, as src/dr_knoll_cloud.c places them: the rim's 20, the inner 6"""
    P = rim_path() if not hasattr(rim_positions, 'P') else rim_positions.P
    rim_positions.P = P
    out = [(P[(i * len(P) // N_RIM + frame * len(P) // LAP_FRAMES) % len(P)], i % 4) for i in range(N_RIM)]
    if inner:
        rx, ry, cy = INNER
        for j in range(N_INNER):
            a = 2 * math.pi * (j / N_INNER + frame / LAP_FRAMES)
            out.append(((int(rx * math.cos(a)), cy + int(ry * math.sin(a))), (N_RIM + j) % 4))
    return out

def conveyor_check(n=96):
    """the whole lap: the underlay's edge always covered, the low door never, at most how many billows on a line"""
    from scipy.ndimage import distance_transform_edt
    H, W = 64 * 16, 66 * 16; t = np.zeros((H, W), bool)
    for x, y in under_cells(): t[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = True
    need = t & (distance_transform_edt(t) <= 6)
    low = np.zeros((H, W), bool); low[34 * 16:36 * 16, 28 * 16:31 * 16] = True
    A = lens_indices() != 0; F = [A, A[:, ::-1], A[::-1], A[::-1, ::-1]]
    wb = dw = lines = 0
    for k in range(n):
        m = np.zeros((H, W), bool); ys = []
        for (dx, dy), f in rim_positions(k * LAP_FRAMES // n // N_RIM):
            x, y = 29 * 16 + 8 + dx, 29 * 16 + 7 + dy; m[y - 16:y + 16, x - 32:x + 32] |= F[f]; ys.append(y)
        wb = max(wb, (need & ~m).sum()); dw = max(dw, (low & m).sum())
        for line in range(min(ys) - 16, max(ys) + 16): lines = max(lines, sum(1 for y in ys if y - 16 <= line < y + 16))
    return dict(edge_gap_px=int(wb), low_door_px=int(dw), max_per_line=lines)

def mock_v3(base_png, outdir, n=48):
    """the knoll with its underlay (from the built map or the mock with hh_door.install) and the rim turning"""
    base = Image.open(base_png).convert('RGBA'); A = to_rgba(lens_indices())
    pics = [Image.fromarray(A), Image.fromarray(A[:, ::-1].copy()), Image.fromarray(A[::-1].copy()), Image.fromarray(A[::-1, ::-1].copy())]
    crop = (16 * 16, 16 * 16, 44 * 16, 42 * 16); seq = []
    for k in range(n):
        im = base.copy()
        for (dx, dy), f in sorted(rim_positions(k * LAP_FRAMES // n), key=lambda p: p[0][1]):
            im.alpha_composite(pics[f], (29 * 16 + 8 + dx - 32, 29 * 16 + 7 + dy - 16))
        seq.append(im.crop(crop).resize(((crop[2] - crop[0]) * 2, (crop[3] - crop[1]) * 2), Image.NEAREST).convert('RGB'))
    seq[0].save(os.path.join(outdir, 'knoll_cloud_v3.gif'), save_all=True, append_images=seq[1:], duration=200, loop=0)
    seq[0].save(os.path.join(outdir, 'knoll_cloud_v3.png'))
