"""The great window's central light, Arceus in stained glass (user 2026-11-23: replace the man in Empire's great window
with an Arceus in stained glass; the user's mockup gives the design, "every pixel of it replaced with appropriately
coloured pixels already in the stained glass").
1. The user's mockup (a screenshot of the nave mock with their Arceus pasted in, at about 2.13x) is registered on the
   mock (fitted on the chancel below the window: scale 2.13, offset (32, 12.5)) and sampled at each GBA pixel.
2. The region replaced: the great window's glass inside its central light (x 137-201 of the mock) and the pointed
   arch above the lights (rows 0-33); its mullions and the side lights stay Empire's.
3. Every pixel there takes the nearest colour of a palette drawn from Empire's own glass (k-means over the window's
   glass), so nothing new is coloured in.
4. Leading: the design's own dark lines (between its rays and panes, round the figure) become the glass's
   near-black lead, with a one-pixel rim round the body; stray single lead pixels dropped. (A pane mosaic cut over
   it was tried and broke the halo up: the design is already cut into panes.)
Usage: python3 arceus_window.py MOCK.png OUT.png"""
import sys, os
import numpy as np
from PIL import Image
REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
USER = os.path.join(REPO, 'assets/templar_hq_reference/empire/user_arceus_window_mockup.png')
S, OX, OY = 2.13, 32.0, 12.5
X0, X1, Y0, Y1 = 104, 232, 0, 128                 # (the great window's box in the mock)
CX0, CX1, ARCH = 137, 202, 34                      # (the central light; the arch above the lights)
LEAD = np.array((12, 13, 18))
STONE = {(182, 172, 146), (192, 182, 156), (196, 186, 160), (200, 190, 164), (112, 104, 86), (132, 105, 66),
         (148, 105, 74), (88, 80, 70), (54, 45, 24), (38, 32, 17), (33, 32, 33), (0, 0, 0)}

def kmeans(X, k, it=25, seed=3):
    rng = np.random.default_rng(seed); C = X[rng.choice(len(X), k, replace=False)].astype(float)
    for _ in range(it):
        lab = ((X[:, None, :] - C[None]) ** 2).sum(-1).argmin(1)
        for j in range(k):
            if (lab == j).any(): C[j] = X[lab == j].mean(0)
    return C

def main(mock, out):
    m = np.array(Image.open(mock).convert('RGB')).astype(int)
    u = np.array(Image.open(USER).convert('RGB')).astype(int)
    win = m[Y0:Y1, X0:X1]
    is_stone = np.array([[tuple(p) in STONE for p in row] for row in win])
    # the glass: per row, between the first and last non-stone pixel (the arch's silhouette)
    glass = np.zeros(win.shape[:2], bool)
    for y in range(win.shape[0]):
        xs = np.nonzero(~is_stone[y])[0]
        if len(xs): glass[y, xs.min():xs.max() + 1] = True
    glass &= ~is_stone
    region = glass.copy(); xx = np.arange(X0, X1)[None, :]; yy = np.arange(Y0, Y1)[:, None]
    region &= ((xx >= CX0) & (xx < CX1)) | (yy < ARCH)
    # the palette: every colour in Empire's stained glass (its tileset's windows, halved to GBA scale), plus its lead
    tb = np.array(Image.open(os.path.join(REPO, 'assets/templar_hq_reference/empire/empire_church_tileset_b.png')).convert('RGBA'))[0::2, 0::2]
    gl = tb[:250, :96]; gl = gl[gl[..., 3] > 0][:, :3].astype(int)
    P = np.unique(np.vstack([gl, win[glass & ~region].reshape(-1, 3)]), axis=0)
    P = P[(np.abs(P - LEAD).sum(-1) > 40) & (P.sum(-1) > 60)]          # (no near-blacks: the sheet's own black ground, and lead is laid separately)
    P = np.vstack([P, LEAD[None]])
    # the user's design at GBA pixels
    # (each GBA pixel the average of its whole patch of the screenshot: the screenshot is blurred, a point sample
    # picks up its noise)
    box = (X0 * S - OX, Y0 * S - OY, X1 * S - OX, Y1 * S - OY)
    uim = Image.open(USER).convert('RGB')
    pad = Image.new('RGB', (uim.size[0] + 200, uim.size[1] + 200)); pad.paste(uim, (100, 100))
    smp = np.array(pad.resize((X1 - X0, Y1 - Y0), Image.BOX, box=tuple(v + 100 for v in box))).astype(int)
    H, W = smp.shape[:2]
    flat = smp.reshape(-1, 3)
    lab = np.empty(len(flat), int)
    for i in range(0, len(flat), 2048):
        lab[i:i + 2048] = ((flat[i:i + 2048, None, :] - P[None]) ** 2).sum(-1).argmin(-1)
    lab = lab.reshape(H, W)
    L = .30 * smp[..., 0] + .59 * smp[..., 1] + .11 * smp[..., 2]
    sat = smp.max(-1) - smp.min(-1)
    body = (sat < 40) & (L > 95) & (L < 214)                         # (Arceus's greys: the halo's whites are field)
    # (only the silhouette: grey specks in the halo's light are not the body; its own holes filled)
    from scipy.ndimage import label as _lab, binary_fill_holes, binary_opening
    body = binary_opening(body, np.ones((2, 2), bool))
    bl, nb_ = _lab(body); bs = np.bincount(bl.ravel()); bs[0] = 0
    body = np.isin(bl, np.nonzero(bs >= 60)[0]); body = binary_fill_holes(body)
    # leading: (a) the design's own outlines (its darks); (b) panes: Voronoi cells, large on the body, small in the
    # field, cut only between pixels of the same kind (body/field), so the body's edge is the outline's
    lead = (L < 48)
    # (no added pane mosaic: the design already has its own leading, the dark lines between its rays and panes)
    # the body's rim against the field: lead (one pixel, on the field's side)
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nb = np.roll(body, (dy, dx), axis=(0, 1))
        lead |= nb & ~body & (L >= 48) & (sat >= 40)               # (only against coloured glass: never its own white highlights)
    lead &= region
    # stray lead dots inside the body (shading in the design, not outline): gone unless they join a line
    from scipy.ndimage import convolve
    for _ in range(2):
        n = convolve(lead.astype(int), np.ones((3, 3), int), mode='constant') - lead
        lead &= ~(n <= 1)
    from scipy.ndimage import label
    lb, nl = label(lead, structure=np.ones((3, 3)))
    sizes = np.bincount(lb.ravel()); small = sizes < 12; small[0] = False
    lead &= ~small[lb]                                              # (lead fragments under twelve pixels: the rays' fine lines break into dashes at this scale)
    res = win.copy()
    col = P[lab]
    # dark pixels that are not part of a lead line (the screenshot's blur specks, snapped to the glass's near-blacks):
    # each takes the commonest colour of its non-dark neighbours
    dk = (.30 * col[..., 0] + .59 * col[..., 1] + .11 * col[..., 2] < 48) & ~lead & region
    for _ in range(3):
        ys_, xs_ = np.nonzero(dk)
        for y, x in zip(ys_, xs_):
            nb = [tuple(col[yy, xx]) for yy in range(max(0, y - 1), min(H, y + 2)) for xx in range(max(0, x - 1), min(W, x + 2))
                  if (yy, xx) != (y, x) and not dk[yy, xx] and not lead[yy, xx]]
            if nb:
                from collections import Counter
                col[y, x] = Counter(nb).most_common(1)[0][0]; dk[y, x] = False
    res[region] = col[region]
    if os.environ.get('NOLEAD') is None: res[lead] = LEAD
    # the lead around the replaced region's edge (where it meets the mullions and the arch), and the eye kept bright
    m2 = m.copy(); m2[Y0:Y1, X0:X1] = res
    Image.fromarray(m2.astype(np.uint8)).save(out)
    Image.fromarray(res.astype(np.uint8)).resize(((X1 - X0) * 4, (Y1 - Y0) * 4), Image.NEAREST).save(out.replace('.png', '_window4x.png'))
    print('replaced', int(region.sum()), 'px; palette', len(P), 'colours; lead', int(lead.sum()), round(lead.sum() / region.sum(), 2))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
