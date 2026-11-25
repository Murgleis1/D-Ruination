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

def cloud():
    im = Image.open(os.path.join(ROOT, 'codebase/graphics/weather/cloud.png')); a = np.array(im)
    out = np.zeros(a.shape + (4,), np.uint8)
    for i, c in FOG.items(): out[a == i, :3] = c; out[a == i, 3] = 255
    return out

# packed close (user 2026-11-25: "bring the clouds more packed together and swirl extremely slowly in a circular
# pattern"): a still heart, an inner ring of 4 turning one way, an outer ring of 8 turning the other, on ellipses (the
# hill seen from above and in front). Each ring's copies alternate two flips, so after a quarter turn the cap looks
# as it began: the swirl loops seamlessly. Its speed in the game: a quarter turn in about 40 seconds.
RINGS = [(0, 0, 1, [0]),                                      # (x radius, y radius, turn direction, flips round it)
         (22, 14, 1, [1, 2]),
         (46, 33, -1, [0, 3])]
CY = 8                                                        # (the cap's heart, below the knoll's top centre)

def placements(phase):
    """(x, y, flip) of each copy at phase 0..1 (one loop: a quarter turn)"""
    out = []
    for rx, ry, d, flips in RINGS:
        n = 1 if rx == 0 else (4 if rx < 30 else 8)
        for j in range(n):
            a = 2 * math.pi * j / n + d * (math.pi / 2) * phase + (0.4 if n == 8 else 0)
            out.append((rx * math.cos(a), CY + ry * math.sin(a), flips[j % len(flips)], math.sin(a)))
    return sorted(out, key=lambda p: p[3])                    # (the far side drawn first)

def compose(base, k, n, cx, cy):
    c = cloud(); out = base.copy()
    pics = [Image.fromarray(c), Image.fromarray(c[:, ::-1].copy()), Image.fromarray(c[::-1].copy()), Image.fromarray(c[::-1, ::-1].copy())]
    for x, y, fl, _ in placements(k / n):
        out.alpha_composite(pics[fl], (int(round(cx + x - 32)), int(round(cy + y - 32))))
    return out

def main(outdir, hh=None):
    os.makedirs(outdir, exist_ok=True)
    Image.fromarray(cloud()).save(os.path.join(outdir, 'cloud_fog.png'))
    if hh:
        base = Image.open(hh).convert('RGBA')
        cx, cy = int(29.5 * 16), 444                              # the knoll's top; the cap's foot ends above row 33
        crop = (16 * 16, 16 * 16, 44 * 16, 42 * 16)
        n = 24; seq = [compose(base, k, n, cx, cy).crop(crop) for k in range(n)]
        seq = [s.resize((s.width * 2, s.height * 2), Image.NEAREST).convert('RGB') for s in seq]
        seq[0].save(os.path.join(outdir, 'knoll_cloud.gif'), save_all=True, append_images=seq[1:], duration=300, loop=0)
        seq[0].save(os.path.join(outdir, 'knoll_cloud_still.png'))
        compose(base, 0, n, cx, cy).convert('RGB').save(os.path.join(outdir, 'knoll_cloud_full.png'))
    print(outdir)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
