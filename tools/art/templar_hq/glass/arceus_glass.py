"""The great window's central light: Arceus in true stained glass, from the user's design (2026-11-23: "look at the
original Arceus I shared, look at each color on it, then replace that pixel with the appropriately colored stained
glass cell").
A straight pixel-for-pixel swap, no re-cutting into panes:
1. Empire's glass colours: every glass pixel of Empire's windows (the great window's side lights and its tileset's
   glass), clustered in Lab into ~32 glasses; each glass is its cluster's median, so it is a colour Empire's windows
   really use. Empire's lead is (12, 13, 18).
2. The design (the user's mockup, registered on the nave mock: scale 2.13, offset (32, 12.5)) is sampled at game
   pixels (each the average of its patch).
3. A game pixel is lead where the design is dark there (luminance < 70); every other pixel is the nearest glass (Lab).
   A lone lead pixel (one lead neighbour or none) is a hairline broken by the scaling, so it takes its glass.
4. The region is the central light and the arch above it, filled solid between the frames, so none of the old
   window's lead survives inside it (that leftover lead was what made earlier tries look speckled). The arch is taken
   row by row between its outermost bright glass near the axis; the side lights and mullions stay Empire's.
Usage: python3 arceus_glass.py MOCK.png OUT.png [LEAD_THRESHOLD]"""
import sys, os
import numpy as np
from PIL import Image
from skimage.color import rgb2lab
from scipy.cluster.vq import kmeans2
REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..'))
EMP = os.path.join(REPO, 'assets/templar_hq_reference/empire')
USER = os.path.join(EMP, 'user_arceus_window_mockup.png')
S, OX, OY = 2.13, 32.0, 12.5
X0, X1, Y0, Y1 = 104, 232, 0, 128
CX0, CX1, ARCH = 137, 202, 34
LEAD = np.array((12, 13, 18))
K = 32
STONE = {(182, 172, 146), (192, 182, 156), (196, 186, 160), (200, 190, 164), (112, 104, 86), (132, 105, 66),
         (148, 105, 74), (88, 80, 70), (54, 45, 24), (38, 32, 17), (33, 32, 33), (0, 0, 0)}
lum = lambda a: .30 * a[..., 0] + .59 * a[..., 1] + .11 * a[..., 2]

def main(mock, out, T=70.0):
    m = np.array(Image.open(mock).convert('RGB')).astype(int)
    win = m[Y0:Y1, X0:X1]
    is_stone = np.array([[tuple(p) in STONE for p in r] for r in win])
    glass = np.zeros(win.shape[:2], bool)
    for y in range(win.shape[0]):
        xs = np.nonzero(~is_stone[y])[0]
        if len(xs): glass[y, xs.min():xs.max() + 1] = True
    glass &= ~is_stone
    xx = np.arange(X0, X1)[None]; yy = np.arange(Y0, Y1)[:, None]
    region0 = glass & (((xx >= CX0) & (xx < CX1)) | (yy < ARCH))
    # 1. Empire's glasses
    pix = [win[glass & ~region0]]
    tb = np.array(Image.open(os.path.join(EMP, 'empire_church_tileset_b.png')).convert('RGBA'))[0::2, 0::2].astype(int)[:250, :100]
    ta = np.array(Image.open(os.path.join(EMP, 'empire_church_tileset_a.png')).convert('RGBA'))[0::2, 0::2].astype(int)[75:224]
    for t in (tb, ta): pix.append(t[t[..., 3] > 0][:, :3])
    P = np.concatenate(pix); P = P[lum(P) >= 45]
    _, lab = kmeans2(rgb2lab((P / 255.)[None])[0], K, minit='++', seed=3, iter=50)
    pal = np.array([np.median(P[lab == j], 0) for j in range(K) if (lab == j).sum() > 20]).astype(int)
    pal = pal[lum(pal) >= 70]                      # glass only; everything darker is lead
    PL = rgb2lab((pal / 255.)[None])[0]
    # 4. the region, filled solid between the frames
    region = np.zeros_like(region0)
    for y in range(region0.shape[0]):
        xs = np.nonzero(region0[y])[0]
        if len(xs): region[y, xs.min():xs.max() + 1] = True
    ax = (CX0 + CX1) // 2 - X0
    inside = np.zeros_like(region); bright = lum(win) > 60
    for y in range(ARCH):
        xs = np.nonzero(bright[y])[0]; xs = xs[np.abs(xs - ax) <= 35]
        if len(xs): inside[y, xs.min():xs.max() + 1] = True
    region &= inside | (yy >= ARCH)
    # 2. the design at game pixels
    u = Image.open(USER).convert('RGB'); pad = Image.new('RGB', (u.size[0] + 200, u.size[1] + 200)); pad.paste(u, (100, 100))
    box = tuple(v + 100 for v in (X0 * S - OX, Y0 * S - OY, X1 * S - OX, Y1 * S - OY))
    smp = np.array(pad.resize((X1 - X0, Y1 - Y0), Image.BOX, box=box)).astype(int)
    # 3. each pixel to its glass, or lead
    idx = ((rgb2lab(smp / 255.)[:, :, None, :] - PL[None, None]) ** 2).sum(-1).argmin(-1)
    g = pal[idx]; lead = lum(smp) < T
    g[lead] = LEAD
    H, W = lead.shape
    for y in range(H):
        for x in range(W):
            if lead[y, x] and region[y, x] and lead[max(0, y - 1):y + 2, max(0, x - 1):x + 2].sum() - 1 <= 1:
                g[y, x] = pal[idx[y, x]]
    outw = win.copy(); outw[region] = g[region]
    o = m.copy(); o[Y0:Y1, X0:X1] = outw
    Image.fromarray(o.astype(np.uint8)).save(out)
    Image.fromarray(o.astype(np.uint8)).resize((o.shape[1] * 2, o.shape[0] * 2), Image.NEAREST).save(out.replace('.png', '_2x.png'))
    print(f'{len(pal)} glasses + lead; lead {(g[region] == LEAD).all(-1).mean():.2f} of the light')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 70.0)
