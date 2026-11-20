"""The half-thawed Arceus statue for the ice path's shrine (user 2026-11-19: reform the supplied statue, which is stuck
on its platform, into a more compelling statue for the ice cave).

Source: the user's statue sheet (assets/arceus_statue/arceus_statue_on_platform.png: 2x RPG Maker art halved to GBA
scale). The figure was cut off its platform (the platform is mirror-symmetric, so pixels that differ from their mirror
image are figure or its shadow; the shadow and the platform corner the figure hid were dropped):
assets/arceus_statue/arceus_figure.png. Here it is stood on a new pedestal (plain geometry: a slab, a band of
blue gemstone with a bright gem, a fluted shaft with a gem boss, stepped base); statue and pedestal in stony greys and
blues flecked with gems (user: ancient, carved from gem-laden cave stone; the platform's gold triangle seen through
the ring removed) and its legs and pedestal are
locked in a faceted block of clear ice (the half-thawed relic the Templar hails as pre-imperial evidence).
Usage: python3 tools/art/icepath/arceus_statue.py [out_preview.png]
"""
import os, sys
import numpy as np
from PIL import Image
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
FIG = os.path.join(ROOT, 'assets', 'arceus_statue', 'arceus_figure.png')

# user: stony greys and blues, an ancient statue carved from gem-laden cave stone (no gold): the stone darker and bluer
# in its shadows, greyer in its lights; the ring, hooves and inlays deep blue gemstone
OUT, D1, D2, MID, LIGHT, TOP = (24, 30, 44), (44, 52, 74), (56, 66, 90), (86, 100, 124), (108, 118, 136), (142, 148, 158)
GOLD_D, GOLD, GOLD_L = (28, 56, 112), (48, 104, 176), (88, 152, 216)            # (named for what they replace)
TEAL_D, TEAL = (60, 150, 200), (150, 226, 248)
FIG_RECOLOUR = {(31, 32, 35): OUT, (38, 38, 38): OUT, (65, 68, 72): D2, (85, 87, 94): (72, 84, 108),
                (87, 90, 96): (76, 88, 112), (92, 95, 102): MID, (94, 98, 104): MID, (111, 115, 123): LIGHT,
                (126, 130, 139): (128, 136, 150), (132, 136, 144): TOP, (133, 135, 142): TOP,
                (80, 72, 24): GOLD_D, (128, 112, 32): GOLD, (159, 136, 56): GOLD_L, (193, 168, 78): (150, 206, 240),
                (177, 151, 62): GOLD_L, (48, 80, 75): (40, 96, 150), (107, 118, 107): TEAL_D}
GEMS = [(150, 226, 248), (96, 176, 240), (200, 240, 255)]

def figure():
    """The cut figure recoloured to gem-laden cave stone, a scatter of gem flecks in its mid tones."""
    f = np.array(Image.open(FIG).convert('RGBA')); rgb, m = f[..., :3].copy(), f[..., 3] > 0
    src = f[..., :3]
    for a, b in FIG_RECOLOUR.items(): rgb[(src == a).all(-1) & m] = b
    rng = np.random.default_rng(7)
    mid = m & ((src == (85, 87, 94)).all(-1) | (src == (87, 90, 96)).all(-1) | (src == (111, 115, 123)).all(-1))
    ys, xs = np.nonzero(mid)
    for i in rng.choice(len(ys), size=max(1, len(ys) // 22), replace=False): rgb[ys[i], xs[i]] = GEMS[i % 3]
    return rgb, m
ICE = [(70, 120, 160), (104, 160, 200), (140, 196, 226), (176, 222, 242), (214, 240, 250), (244, 252, 255)]

def pedestal(w=40):
    """The new pedestal, w px wide: (rgb, mask), 26 px tall."""
    h = 26; img = np.zeros((h, w, 3), np.uint8); m = np.zeros((h, w), bool)
    def box(y0, y1, x0, x1, c): img[y0:y1, x0:x1] = c; m[y0:y1, x0:x1] = True
    c = w // 2
    box(0, 4, 0, w, OUT); box(1, 3, 1, w - 1, TOP); box(3, 4, 1, w - 1, LIGHT)                 # the top slab
    box(4, 7, 2, w - 2, OUT); box(4, 6, 3, w - 3, GOLD); box(5, 6, 3, w - 3, GOLD_D)          # the gold band
    box(4, 7, c - 3, c + 3, OUT); box(5, 6, c - 2, c + 2, TEAL); img[4, c - 1:c + 1] = TEAL; img[6, c - 1:c + 1] = TEAL_D
    box(7, 19, 4, w - 4, OUT); box(7, 19, 5, w - 5, LIGHT)                                     # the fluted shaft
    for x in range(8, w - 7, 4): box(8, 18, x, x + 1, MID); box(8, 18, x + 1, x + 2, TOP)
    box(7, 8, 5, w - 5, D2)
    box(11, 15, c - 2, c + 2, GOLD); img[11, c - 2] = img[11, c + 1] = img[14, c - 2] = img[14, c + 1] = GOLD_D   # gold boss
    box(19, 22, 2, w - 2, OUT); box(19, 21, 3, w - 3, TOP); box(21, 22, 3, w - 3, MID)        # the stepped base
    box(22, 26, 0, w, OUT); box(22, 25, 1, w - 1, LIGHT); box(25, 26, 1, w - 1, D1)
    rng = np.random.default_rng(9)                              # gem flecks in the carved stone
    ys, xs = np.nonzero(m & ((img == LIGHT).all(-1) | (img == TOP).all(-1)))
    for i in rng.choice(len(ys), size=len(ys) // 25, replace=False): img[ys[i], xs[i]] = GEMS[i % 3]
    return img, m

def statue(ice=True, ice_top=0.72):
    """(rgb, mask): the figure on the pedestal; with ice, everything below ice_top of the figure in a block of ice."""
    fr, fm = figure()
    p, pm = pedestal(); fh, fw = fm.shape; ph, pw = pm.shape
    W = max(fw, pw) + 10; H = fh + ph - 3 + 2
    img = np.zeros((H, W, 3), np.uint8); m = np.zeros((H, W), bool)
    px = (W - pw) // 2; py = fh - 3
    img[py:py + ph, px:px + pw][pm] = p[pm]; m[py:py + ph, px:px + pw] |= pm
    fx = (W - fw) // 2; sub = img[0:fh, fx:fx + fw]; sub[fm] = fr[fm]; m[0:fh, fx:fx + fw] |= fm
    if not ice: return img, m
    # the ice: crystal points rising round the hooves, the block flaring out over the pedestal; the stone seen through
    # it (blended, not hidden), faceted in two tones, a bright rim and a darker outline
    top = int(fh * ice_top); rng = np.random.default_rng(11)
    edge = np.full(W, top + 6)
    for _ in range(9):                                      # crystal points
        cx = int(rng.integers(2, W - 2)); hgt = int(rng.integers(4, 11)); half = int(rng.integers(2, 5))
        for x in range(max(0, cx - half), min(W, cx + half + 1)):
            edge[x] = min(edge[x], top + 6 - hgt + abs(x - cx) * hgt // (half + 1))
    out = img.astype(float).copy(); om = m.copy(); ice = np.zeros(m.shape, bool)
    for x in range(W):
        for y in range(max(0, edge[x]), H):
            flare = (y - top) // 6                            # the block widens downwards
            if x < max(0, 4 - flare) or x > W - 1 - max(0, 4 - flare): continue
            ice[y, x] = True
    facet = ((np.arange(W)[None, :] + np.arange(H)[:, None] // 2) // 4) % 2
    for y, x in zip(*np.nonzero(ice)):
        tone = np.array(ICE[3] if facet[y, x] else ICE[4], float)
        out[y, x] = out[y, x] * 0.5 + tone * 0.5 if m[y, x] else tone
        om[y, x] = True
    for y, x in zip(*np.nonzero(ice)):                         # rim and outline
        up = y == 0 or not ice[y - 1, x]
        side = x == 0 or x == W - 1 or not ice[y, x - 1] or not ice[y, x + 1]
        if up: out[y, x] = ICE[5]
        elif side or y == H - 1: out[y, x] = ICE[1]
    return out.astype(np.uint8), om

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/arceus/statue_preview.png'
    a, am = statue(ice=False); b, bm = statue(ice=True)
    bg = (176, 196, 210)
    def onbg(r, mm):
        o = np.zeros(r.shape, np.uint8); o[:] = bg; o[mm] = r[mm]; return o
    S = np.hstack([onbg(a, am), np.zeros((a.shape[0], 6, 3), np.uint8) + 60, onbg(b, bm)])
    Image.fromarray(S).resize((S.shape[1] * 5, S.shape[0] * 5), 0).save(path); print(path, a.shape)
