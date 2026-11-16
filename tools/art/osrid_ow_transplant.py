"""Osrid's overworld sprite: Osrid's ENTIRE head from his existing sheet on KAKUGO's body
(user 2026-11-16, 14:15: "why not just take Osrid's entire headsprite on the overworld and put it
on Kakugo's overworld sprite body as a starting point"; clothes in his dark green tunic).

Per frame (standard order S, N, W, walk S x2, walk N x2, walk W x2 in both sheets):
  * neck line = first row of the frame that is mostly clothing (>= 2 tunic/coat pixels) -- measured
    separately in each sheet, so each walk frame's bob is respected
  * Kakugo's frame above its neck line is cleared; Osrid's head (his rows above HIS neck line) is
    placed so the two neck lines meet -- head pixels exactly as Osrid's artist drew them
  * Kakugo's body is recoloured to Osrid's tunic greens (coat 4-tone ramp -> his 4 greens, scarf ->
    his light greens); leftover helmet-brown at the collar -> the tunic's darkest green
  * output palette = the exact colours used (<= 15 + transparent), no quantisation
Run: python3 -I osrid_ow_transplant.py KAKUGO.png OSRID_OLD.png OUT.png
"""
import sys
import numpy as np
from PIL import Image

KAK_COAT = {9: 0, 11: 1, 10: 2, 12: 3}          # Kakugo coat index -> tone 0 (dark) .. 3 (light)
OSR_GREENS = [(24, 42, 30), (35, 61, 43), (46, 80, 56), (72, 106, 78)]
KAK_SCARF = {13: 2, 14: 3}
KAK_BROWN = (1, 2, 3, 4, 6, 8)                   # helmet / visor colours (gold 6, ruby 8)
KAK_GOLD = 7                                     # gold buttons -> lightest green
OSR_BODY = (4, 6, 15, 8, 9)                      # Osrid's tunic greens + armour greys


def rgba(path):
    im = Image.open(path); px = np.array(im)
    pal = np.array(im.getpalette()[:48]).reshape(16, 3)
    return px, pal


def neck(frame, body_idx):
    for y in range(32):
        if np.isin(frame[y], body_idx).sum() >= 2: return y
    return 32


def build(kak_path, osr_path):
    kp, kpal = rgba(kak_path); op, opal = rgba(osr_path)
    # Anchor per DIRECTION on its standing frame (neck lines of walk frames are unreliable:
    # measured, Osrid's collar row jumps 21->23 between frames 0 and 3); walk frames then move the
    # head by exactly the bob of each sheet (difference of the frame's top row to the standing one).
    STAND = {0: 0, 3: 0, 4: 0, 1: 1, 5: 1, 6: 1, 2: 2, 7: 2, 8: 2}
    top = lambda f: min(y for y in range(32) if f[y].any())
    fr = lambda a, i: a[:, i * 16:(i + 1) * 16]
    frames = []
    for fi in range(9):
        kf, of = fr(kp, fi), fr(op, fi)
        st = STAND[fi]; ks, os_ = fr(kp, st), fr(op, st)
        kn0 = neck(ks, tuple(KAK_COAT) + tuple(KAK_SCARF)); on0 = neck(os_, OSR_BODY)
        kb = top(kf) - top(ks); ob = top(of) - top(os_)          # this frame's bob in each sheet
        kn = kn0 + kb                                            # Kakugo's neck in this frame
        on = on0 + ob                                            # Osrid's head ends here
        out = np.zeros((32, 16, 4), np.uint8)
        for y in range(kn, 32):
            for x in range(16):
                v = int(kf[y, x])
                if v == 0: continue
                if v in KAK_COAT: c = OSR_GREENS[KAK_COAT[v]]
                elif v in KAK_SCARF: c = OSR_GREENS[KAK_SCARF[v]]
                elif v == KAK_GOLD: c = OSR_GREENS[3]
                elif v in KAK_BROWN: c = OSR_GREENS[0]
                else: c = tuple(int(t) for t in kpal[v])
                out[y, x] = (*c, 255)
        dy = kn - on
        for y in range(0, on):
            for x in range(16):
                v = int(of[y, x])
                if v == 0 or not (0 <= y + dy < 32): continue
                out[y + dy, x] = (*[int(t) for t in opal[v]], 255)
        frames.append(out)
    sheet = np.concatenate(frames, 1)
    cols = sorted({tuple(c[:3]) for c in sheet.reshape(-1, 4) if c[3]}, key=lambda c: int(c[0]) + int(c[1]) + int(c[2]))
    assert len(cols) <= 15, f'{len(cols)} colours'
    lut = {c: i + 1 for i, c in enumerate(cols)}
    idx = np.zeros(sheet.shape[:2], np.uint8)
    for y in range(sheet.shape[0]):
        for x in range(sheet.shape[1]):
            if sheet[y, x, 3]: idx[y, x] = lut[tuple(sheet[y, x, :3])]
    pal = [(115, 197, 164)] + cols + [(0, 0, 0)] * (15 - len(cols))
    o = Image.fromarray(idx, 'P'); o.putpalette([v for c in pal for v in c] + [0] * (768 - 48))
    return o


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2]).save(sys.argv[3], transparency=0)
