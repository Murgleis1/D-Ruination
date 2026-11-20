"""Shared art kit for the Route 11 / Hollow Hill composers (user design 2026-11-20).

Pieces from:
  Pelluca's Cormoria tiles (via tools/render_layout.py), split into ground (bottom layer) and object (middle + top)
  so the pines can stand on any shade of grass;
  Pokemon Crown (credit Blah and the Crown team, used with permission): broadleaf woods, the worn-path and patch
  edge shapes, tall grass, farm props;
  Pokemon Odyssey: farm crops, the sown field, hay;
  MonoMyth: the river, its falls and pools, ledges, the bridge.
Atlases: export_atlas.py / export_atlas_mm.py into ATLAS.

The grass: four shades, mint (Pelluca) -> sage -> spring -> olive (Crown's woods). Where two shades meet, the edge
follows Crown's own patch-edge shapes (its lighter-grass patches in the dark woods, ids 8b-9f): a corner autotile
(each cell's four corners inside or outside the patch), the two shades' own textures either side and a one-pixel
shadow on the darker side.
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..'))
import render_layout as RL
ATLAS = os.environ.get('ROUTE11_ATLAS', '/home/claude/scratch/route11/atlas')
_cor = RL.TS('LAYOUT_PELLUCA_CITY')
_at = {}

def atlas(name):
    if name not in _at: _at[name] = np.load(os.path.join(ATLAS, name + '.npz'))
    return _at[name]

# ------------------------------------------------------------------ Cormoria (Pelluca) cells
# Pelluca's metatiles are drawn whole in their middle layer, the pines with their grass, so a pine on another shade
# is the pine with Pelluca's mint pixels swapped (kit.overlay).
def cor_full(m): return np.asarray(_cor.metatile(m), np.uint8)

# ------------------------------------------------------------------ the grass shades
MINT = [(112, 208, 160), (136, 216, 176), (160, 224, 176)]            # Pelluca's metatile 6, dark to light
SAGE = [(104, 190, 140), (124, 202, 152), (146, 214, 162)]
SPRING = [(92, 162, 98), (110, 174, 108), (126, 186, 120)]
OLIVE = [(80, 136, 64), (96, 148, 76), (108, 160, 88)]                   # Crown's woods grass, its three main greens
OLIVE4 = [(80, 136, 64), (96, 144, 80), (104, 160, 88), (112, 168, 80)]   # Crown's woods grass (its metatile 1)
SHADES = [MINT, SAGE, SPRING, OLIVE]

def _recolour(img, src, dst):
    out = img.copy(); flat = out.reshape(-1, 3)
    for a, b in zip(src, dst): flat[(flat == a).all(1)] = b
    return out

_plain = {}
def plain(k):
    """A plain cell of shade k: Pelluca's own grass, recoloured for the darker shades, so only the colour changes
    across the route (the pieces from other games leave their own grass out)."""
    if k not in _plain: _plain[k] = _recolour(cor_full(6), MINT, SHADES[k])
    return _plain[k]

# Crown's patch-edge pieces: which corners of the cell lie inside the patch (TL, TR, BL, BR)
_PIECES = {(0, 0, 0, 1): 0x8b, (0, 0, 1, 1): 0x8c, (0, 0, 1, 0): 0x8d, (0, 1, 0, 1): 0x93, (1, 1, 1, 1): 0x94,
           (1, 0, 1, 0): 0x95, (0, 1, 0, 0): 0x9b, (1, 1, 0, 0): 0x9c, (1, 0, 0, 0): 0x9d, (0, 1, 1, 1): 0x96,
           (1, 0, 1, 1): 0x97, (1, 1, 0, 1): 0x9e, (1, 1, 1, 0): 0x9f}
_LIGHT = {(120, 192, 104), (104, 184, 96), (136, 200, 120)}
_masks = {}
def patch_mask(corners):
    """The patch's pixels in a cell with these corners inside (Crown's own edge shapes)."""
    corners = tuple(int(c) for c in corners)
    if corners in _masks: return _masks[corners]
    if corners == (0, 0, 0, 0): m = np.zeros((16, 16), bool)
    elif corners in _PIECES:
        f = atlas('crown325')['full'][_PIECES[corners]]
        m = np.array([[tuple(p) in _LIGHT for p in row] for row in f.tolist()])
    else:                                                  # the two diagonal cases: the union of two corners
        parts = [patch_mask(tuple(1 if i == j else 0 for i in range(4))) for j in range(4) if corners[j]]
        m = np.zeros((16, 16), bool)
        for p in parts: m |= p
    _masks[corners] = m; return m

def grass_cell(v):
    """v: the four corner shades (TL, TR, BL, BR), at most two adjacent shades. The darker shade's patch drawn
    into the lighter with Crown's edge shapes, a one-pixel shadow round the patch."""
    ks = sorted(set(v))
    if len(ks) == 1: return plain(ks[0]).copy()
    assert len(ks) == 2 and ks[1] == ks[0] + 1, v
    lo, hi = ks
    m = patch_mask(tuple(1 if c == hi else 0 for c in v))
    img = plain(lo).copy(); d = plain(hi); img[m] = d[m]
    from scipy.ndimage import binary_dilation
    rim = binary_dilation(m) & ~m                          # the lighter side's pixels touching the patch: a shadow
    img[rim] = SHADES[hi][0]                               # in the darker shade's own darkest green (no new colour)
    return img

def recolour_grass(img, src_shade, k):
    """Move a cell drawn on one shade's grass to shade k's (the grass colours swapped by rank)."""
    src = SHADES[src_shade]; dst = SHADES[k]
    if len(src) == 4 and len(dst) == 3: dst = [dst[0]] + list(dst)
    if len(src) == 3 and len(dst) == 4: dst = dst[1:]
    return _recolour(img, src, dst)

def edge_cell(lo, hi, corners, rim_lo=None, rim_hi=None):
    """Any two grounds meeting with Crown's patch-edge shapes: hi (the patch) where the corners are set, over lo; a
    one-pixel rim either side of the edge (rim_lo on lo's side, rim_hi on hi's), when given."""
    from scipy.ndimage import binary_dilation
    m = patch_mask(tuple(int(bool(c)) for c in corners))
    img = lo.copy(); img[m] = hi[m]
    if rim_lo is not None: img[binary_dilation(m) & ~m] = rim_lo
    if rim_hi is not None: img[m & binary_dilation(~m)] = rim_hi
    return img
