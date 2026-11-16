"""Town props for Pelluca (user 2026-11-16: "I'd like all that stuff" -- benches, signposts, a well,
barrels and crates).

Every prop is MonoMyth art that already sits in the MIDDLE/TOP layers of its source map with plain
ground in the bottom layer, so it lifts cleanly and goes onto Pelluca's own ground (grass, harbour
stone) by swapping the bottom layer -- the palm's technique.

  bench    Chamomile park bench, cells 29-30 y25 (2x1)          -> Academy yard, plaza lawn
  sign     Farmstead wooden signpost, cell 19,6 (1x1)           -> town entrances
  well     Mandrake covered well, cells 25 y40-41 (1x2)         -> dorm garden
  barrel   Mandrake barrel, cell 46,19 (1x1)                    -> harbour
  produce  Mandrake crate (greens -> its own dark wood: goods), cell 48,23 (1x1)           -> harbour
  crate    Mandrake tall crate, cells 46 y23-24 (1x2)           -> harbour
  inn      Wood Avens INN signboard, cells 16-17 y32-33 (2x2)  -> the tavern (user 2026-11-16).
           Its top row (post caps) was already in the terrain crop as 114/115 without the board
           row -- the half-sign that read as 'incomplete posts'; now imported whole.

prop_layers(name) -> (mid, top): RGB images (h*16, w*16, 3), -1 = transparent. Any opaque pixel of
the source's ground (sand / grass) left in the mid/top layers is cut, so only the object remains.
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_cormoria as b

CHAMOMILE, FARMSTEAD, MANDRAKE, WOOD_AVENS = 0x8694d8, 0x869a18, 0x869548, 0x869580
PROPS = {
    'bench':   (CHAMOMILE, (29, 25, 30, 25)),
    'sign':    (FARMSTEAD, (19, 6, 19, 6)),
    'well':    (MANDRAKE, (25, 40, 25, 41)),
    'barrel':  (MANDRAKE, (46, 19, 46, 19)),
    'produce': (MANDRAKE, (48, 23, 48, 23)),
    'crate':   (MANDRAKE, (46, 23, 46, 24)),
    'inn':     (WOOD_AVENS, (16, 32, 17, 33)),
}


# Measured on the fitted build: the sign's lettering (104,72,80) and the crate's greens (96,200,8)
# have no near colour in the palette that holds their wood, and snapped to grey / noise. Lettering
# takes the sign's own outline; the crate's greens take its own dark wood (a crate of goods).
RECOLOUR = {
    'sign': [((104, 72, 80), (72, 56, 72)), ((192, 168, 144), (176, 136, 112))],   # its bevel tan snapped to grey
    'produce': [((96, 200, 8), (128, 96, 64))],
}


def _ground_cols(bottom):
    return {tuple(v) for v in bottom.reshape(-1, 3) if v[0] >= 0}


def prop_layers(name):
    a, box = PROPS[name]
    lay, _ = b.region_layers(a, box)
    ground = _ground_cols(lay[0])
    out = []
    for L in (lay[1], lay[2]):
        img = L.copy()
        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                if img[y, x, 0] >= 0 and tuple(img[y, x]) in ground: img[y, x] = -1
        for src, dst in RECOLOUR.get(name, ()):          # colours no palette pairs with the prop's own woods
            img[(img == src).all(-1)] = dst
        out.append(img)
    return tuple(out)


if __name__ == '__main__':
    from PIL import Image, ImageDraw
    S = 6; tiles = []
    for n in PROPS:
        mid, top = prop_layers(n)
        img = np.zeros(mid.shape, int); img[:] = (120, 200, 120)
        for L in (mid, top):
            m = (L >= 0).all(-1); img[m] = L[m]
        tiles.append((n, img))
    W = sum(t.shape[1] + 8 for _, t in tiles) * S; Hh = max(t.shape[0] for _, t in tiles) * S + 20
    sheet = Image.new('RGB', (W, Hh), (40, 40, 40)); d = ImageDraw.Draw(sheet); x = 0
    for i, (n, t) in enumerate(tiles):
        sheet.paste(Image.fromarray(t.astype(np.uint8)).resize((t.shape[1] * S, t.shape[0] * S), Image.NEAREST), (x, 20))
        d.text((x, 4), f'{i + 1} {n}', fill=(255, 255, 0)); x += (t.shape[1] + 8) * S
    sheet.save(sys.argv[1] if len(sys.argv) > 1 else '/tmp/props.png')
