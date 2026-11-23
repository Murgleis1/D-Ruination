"""The registry's wall map: the user's illustrated map of the Cormorian Empire
(assets/region_map/cormorian_empire_illustrated.png; user 2026-11-23: "make it more like parchment and make the map
look cleaner ... or take the original high fidelity version I gave you ... as the basis") redrawn as a clean
parchment map: light paper, the land shaded from the painting's own light and dark in a few parchment tones, the sea
a pale wash, the desert a warmer tan, a dark-brown ink line wherever land meets sea, the rivers in thin blue ink.
Usage: python3 parchment_map.py OUT.png [W H]"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..', 'assets', 'region_map', 'cormorian_empire_illustrated.png'))
INK = (74, 48, 28); RIVER = (86, 112, 126)
LAND = [(150, 122, 84), (184, 156, 112), (210, 186, 140), (230, 212, 170), (244, 232, 198)]   # dark -> light
SEA = [(170, 190, 180), (194, 208, 196)]
SAND = (226, 196, 140)

def parchment(w=84, h=56):
    src = Image.open(SRC).convert('RGB')
    W0, H0 = src.size
    src = src.crop((int(W0 * .02), int(H0 * .03), int(W0 * .98), int(H0 * .97)))   # (the painting's dark border off)
    big = np.array(src.filter(ImageFilter.GaussianBlur(3)).resize((w * 4, h * 4), Image.BOX)).astype(float)
    r, g, b = big[..., 0], big[..., 1], big[..., 2]
    sea4 = (b > r + 25) & (b > g + 5)
    cw, ch = big.shape[1], big.shape[0]
    title = np.zeros(sea4.shape, bool); title[:int(ch * .09), int(cw * .34):int(cw * .64)] = True
    sea4 &= ~title                                            # (the title cartouche is land, not a lake)
    sand4 = (r > 150) & (r > b + 60) & (g > 110) & (r - g < 70) & ~sea4
    a = np.array(src.resize((w, h), Image.BOX)).astype(float)
    # each game pixel: the class most of its 4x4 patch has
    sea = sea4.reshape(h, 4, w, 4).mean((1, 3)) > 0.5
    sand = sand4.reshape(h, 4, w, 4).mean((1, 3)) > 0.5
    sm = np.array(src.filter(ImageFilter.GaussianBlur(12)).resize((w, h), Image.BOX)).astype(float)
    L = (.3 * sm[..., 0] + .59 * sm[..., 1] + .11 * sm[..., 2])   # (shaded from a smoothed painting: no speckle)
    land = ~sea
    out = np.zeros((h, w, 3), int)
    q = np.quantile(L[land], [0.3, 0.7]) if land.any() else [0, 0]
    k = np.searchsorted(q, L) + 1                              # (three tones: LAND[1..3])
    out[land] = np.array(LAND)[np.clip(k, 1, 3)][land]
    out[sand & land] = SAND
    sq = np.quantile(L[sea], [0.5]) if sea.any() else [0]
    out[sea] = np.where((L[sea] < sq[0])[:, None], SEA[0], SEA[1])
    # the painting's details, in ink: roads (its gold lines), towns (its grey stone knots), peaks (rocky, rough ground)
    from skimage.morphology import skeletonize
    from scipy.ndimage import maximum_filter, uniform_filter
    A = np.array(src).astype(int); R, G, B = A[..., 0], A[..., 1], A[..., 2]
    def down(m):
        Hh, Ww = m.shape; hh, ww = Hh // h, Ww // w
        return m[:hh * h, :ww * w].reshape(h, hh, w, ww).mean((1, 3))
    rd = down((R > 170) & (G > 130) & (B < 90) & (R - G < 70))
    gr = down((abs(R - G) < 18) & (abs(G - B) < 22) & (R > 90) & (R < 200))
    Lf = (.3 * R + .59 * G + .11 * B).astype(float)
    rough = down(np.abs(Lf - uniform_filter(Lf, 9)) > 28)
    from scipy.ndimage import binary_dilation
    roads = skeletonize(binary_dilation((rd > 0.045) & land & ~sand)) & land & ~sand
    gs = uniform_filter(gr, 3)
    towns = (gs == maximum_filter(gs, 7)) & (gs > 0.16) & land
    towns[:3] = towns[-3:] = False; towns[:, :3] = towns[:, -3:] = False   # (no marks on the margin)
    peaks = (uniform_filter(rough, 5) > 0.26) & (uniform_filter(gr, 5) > 0.06) & land & ~sand   # (rough AND grey rock: not forest)
    print('roads', int(roads.sum()), 'towns', int(towns.sum()), 'peaks', int(peaks.sum()))
    ROAD, TOWN, TOWNC = (150, 72, 46), (74, 48, 28), (176, 60, 44)
    for y in range(h):
        for x in range(w):
            if roads[y, x] and (x + y) % 2 == 0: out[y, x] = ROAD          # (dotted)
    for y in range(1, h - 2, 4):                                           # (peak marks on a loose grid)
        for x in range(2 + (y // 4) % 2 * 2, w - 2, 4):
            if peaks[y, x] and not roads[y, x]:
                out[y + 1, x - 1] = INK; out[y, x] = INK; out[y + 1, x + 1] = INK
    for y, x in zip(*np.nonzero(towns)):
        y0, x0 = max(0, y - 1), max(0, x - 1)
        out[y0:y0 + 3, x0:x0 + 3] = TOWN; out[y0 + 1, x0 + 1] = TOWNC
    # rivers: thin blue runs inside the land (a sea pixel with land on both sides across it)
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            if sea[y, x] and ((land[y, x - 1] and land[y, x + 1]) or (land[y - 1, x] and land[y + 1, x])):
                out[y, x] = RIVER
    # coast: ink on land pixels that touch the sea
    for y in range(h):
        for x in range(w):
            if land[y, x] and tuple(out[y, x]) != RIVER:
                nb = sea[max(0, y - 1):y + 2, max(0, x - 1):x + 2]
                if nb.any(): out[y, x] = INK
    return out

def scroll(w=84, h=56):
    """The map hung as a scroll: a paper margin, a scorched rim, a wooden rod top and bottom."""
    m = parchment(w, h)
    W, H = w + 6, h + 10
    out = np.zeros((H, W, 4), int)
    out[3:H - 3, 1:W - 1, :3] = (236, 222, 186); out[3:H - 3, 1:W - 1, 3] = 255
    out[3:H - 3, 1, :3] = (168, 136, 96); out[3:H - 3, W - 2, :3] = (168, 136, 96)   # (the rim, scorched)
    out[5:5 + h, 3:3 + w, :3] = m
    for y in (0, H - 3):                                       # the rods
        out[y:y + 3, 0:W, 3] = 255
        out[y, :, :3] = (128, 80, 56); out[y + 1, :, :3] = (96, 60, 44); out[y + 2, :, :3] = (64, 40, 32)
        out[y:y + 3, 0, :3] = (40, 40, 48); out[y:y + 3, W - 1, :3] = (40, 40, 48)
    return out

if __name__ == '__main__':
    w, h = (int(sys.argv[2]), int(sys.argv[3])) if len(sys.argv) > 3 else (84, 56)
    s = scroll(w, h); Image.fromarray(s[..., :3].astype(np.uint8)).resize((s.shape[1] * 5, s.shape[0] * 5), Image.NEAREST).save(sys.argv[1])
