"""Pelluca City's outdoor door animations (user 2026-11-19: "Generate a swing-open").

Two Pelluca doors have real leaves and are MB_ANIMATED_DOOR metatiles with no animation frames yet:
the Umbra Lab door (secondary metatile 0x3E8) and the timber house door (primary 0x05D: the
dormitory, plus two warp-less houses with the same art). The monastery and tavern are open archways
(MB_NON_ANIMATED_DOOR) and stay as they are.

field_door.c draws a size-1 door as the door cell and the cell above it, each 2x2 tiles on the bottom
layer only (the other layers are cleared while it plays), one palette per 8x8 tile. So each frame is
the full 16x32 art of both cells, flattened, and every tile's colours must sit in one palette.

The swing: both knobs are on the left, so the leaves hinge on the right and swing inward. Each frame
narrows the leaf toward the hinge (its columns resampled), shades it one step darker per frame as it
turns from the light, and shows the dark interior where it has opened. Three frames, as the engine
plays them: ajar, half open, open (a sliver of leaf at the hinge).
"""
import os, sys
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import render_layout as R

TS = R.TS('LAYOUT_PELLUCA_CITY')
VOID = (24, 48, 80)                       # the dark interior (palette 6 index 1)

# leaf boxes in the 16x32 strip (cell above = rows 0-15, door cell = rows 16-31): x0..x1, y0..y1 inclusive;
# the jamb outlines around them stay put. shade: one step darker along the tileset's own grey/navy ramp.
DOORS = {
    'umbra_lab': dict(cells=(0x3E2, 0x3E8), metatile=0x3E8, leaf=(1, 14, 17, 29),
                      shade={(120, 120, 128): (88, 88, 96), (88, 88, 96): (64, 72, 104), (64, 72, 104): (48, 56, 80),
                             (48, 56, 80): VOID, (208, 216, 232): (120, 120, 128), (184, 192, 208): (120, 120, 128)}),
    'pelluca_house': dict(cells=(0x322, 0x05D), metatile=0x05D, leaf=(3, 12, 15, 29),
                          shade={(88, 88, 96): (64, 72, 104), (64, 72, 104): (48, 56, 80), (48, 56, 80): VOID,
                                 (208, 216, 232): (120, 120, 128), (152, 168, 184): (120, 120, 128),
                                 (120, 120, 128): (88, 88, 96)}),
}
WIDTHS = (0.70, 0.38, 0.0)                # leaf's projected width per frame (cos of the swing angle)
SHADE_STEPS = (1, 1, 2)                   # how far down the ramp the leaf is shaded per frame (more merges it into the dark)
EDGE = (48, 56, 80)                       # the free edge's outline

def strip(door):
    up, dn = DOORS[door]['cells']
    return np.vstack([TS.metatile(up), TS.metatile(dn)]).astype(np.uint8)

def frame(door, k):
    D = DOORS[door]; a = strip(door); out = a.copy()
    x0, x1, y0, y1 = D['leaf']; w = x1 - x0 + 1
    leaf = a[y0:y1 + 1, x0:x1 + 1]
    for _ in range(SHADE_STEPS[k]):                         # darker as it turns away
        leaf = np.array([[D['shade'].get(tuple(int(v) for v in c), tuple(c)) for c in row] for row in leaf], np.uint8)
    out[y0:y1 + 1, x0:x1 + 1] = VOID
    nw = max(2, int(round(w * WIDTHS[k])))
    cols = [int(i * w / nw) for i in range(nw)]               # resample the leaf, hinged on the right
    out[y0:y1 + 1, x1 + 1 - nw:x1 + 1] = leaf[:, cols]
    out[y0:y1 + 1, x1 + 1 - nw] = EDGE                      # its free edge
    return out

def palette_for(tile_rgb, prefer):
    cs = {tuple(int(v) for v in c) for c in tile_rgb.reshape(-1, 3)}
    for p in prefer + [p for p in range(6, 13) if p not in prefer]:
        if cs <= set(map(tuple, TS.pal[p][1:])): return p
    raise ValueError(f'no palette holds {sorted(cs)}')

def fit(door, frames):
    """One palette per tile position across all frames (the engine's palette list is per door, not per frame)."""
    pals = []
    for q in range(8):
        y, x = (q // 2) * 8, (q % 2) * 8
        stack = np.vstack([f[y:y + 8, x:x + 8] for f in frames])
        pals.append(palette_for(stack, [6, 9]))
    return pals

def indexed(door, frames, pals):
    """16 x (32 * frames) indexed image, each tile's pixels as indices into its palette."""
    out = np.zeros((32 * len(frames), 16), np.uint8)
    for k, f in enumerate(frames):
        for q in range(8):
            y, x = (q // 2) * 8, (q % 2) * 8; pal = [tuple(c) for c in TS.pal[pals[q]]]
            for yy in range(8):
                for xx in range(8):
                    out[k * 32 + y + yy, x + xx] = pal.index(tuple(int(v) for v in f[y + yy, x + xx]), 1)
    return out

if __name__ == '__main__':
    for d in DOORS:
        fr = [frame(d, k) for k in range(3)]; print(d, 'palettes', fit(d, fr))

C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'codebase')
def install():
    """Write graphics/door_anims/<door>.png (16x96: three 16x32 frames, indices into each tile's palette)
    and print each door's palette list for field_door.c."""
    for d in DOORS:
        fr = [frame(d, k) for k in range(3)]; pals = fit(d, fr); idx = indexed(d, fr, pals)
        im = Image.fromarray(idx, 'P'); im.putpalette([v for c in TS.pal[pals[-1]] for v in c] + [0] * (768 - 48))
        im.save(os.path.join(C, 'graphics', 'door_anims', d + '.png')); print(d, pals)

if __name__ == '__main__' and '--install' in sys.argv: install()
