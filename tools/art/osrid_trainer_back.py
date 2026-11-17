"""Osrid trainer BACK pic (2026-11-17, round 3).

Design source: his character sheet, assets/osrid_reference/osrid_character_sheet.png (back view),
and the approved portrait. User, round 2: "the head is a giant blobby huge swollen monstrosity with
red spikes ... make the backsprite actually work in alignment with the portrait and front sprite".
Measured from the sheet's back view and built by hand (row spans plus placed strands, not generated):
  * head about 23 px wide (MonoMyth #4's own is 30): tousled wavy auburn hair with curls at the
    nape, not spikes
  * the mask's leather strap round the back of the head above the ear, with the square buckle
  * ear under the strap; the mask's side and profile (brow, nose, chin) at the right, with the
    end of the eye glyph, the drip and the start of the spiral at the front edge
  * scarf bunched round the neck and left shoulder; the tattered green cape down the left half of
    the back; quilted charcoal jacket and the diagonal brown strap on the right half
  * fingerless dark gloves; colours from the sheet's swatches and the approved portrait
Base: MonoMyth back #4 for body, arm and the 4-frame throw ONLY (its head is removed).

Usage: python3 -I osrid_trainer_back.py BACKS_PKL OUT.png   (64x256, 4 frames)
"""
import sys, pickle
import numpy as np
from PIL import Image
from collections import deque

PAL = {
    0x0: (255, 0, 255),
    0x5: (10, 10, 12),      # outline / glyph
    0x4: (114, 42, 18),     # hair dark      (portrait)
    0x1: (160, 64, 28),     # hair mid
    0xD: (206, 104, 52),    # hair light
    0x9: (226, 210, 170),   # mask           (portrait)
    0xE: (246, 238, 210),   # mask highlight
    0x7: (178, 152, 112),   # mask shadow / skin
    0xF: (176, 112, 78),    # ear
    0x6: (30, 30, 32),      # charcoal dark  (sheet swatch 49,48,46 as the mid)
    0x2: (50, 49, 48),      # charcoal mid
    0x3: (82, 80, 76),      # charcoal light / buckle metal
    0x8: (92, 64, 44),      # leather strap  (sheet browns)
    0xB: (24, 34, 28),      # green dark     (portrait / sheet)
    0xA: (40, 58, 44),      # green mid
    0xC: (66, 84, 62),      # green light
}
HAIR = {0x1, 0x4, 0xD}
SKIN = {0x9, 0xE, 0x7, 0xC, 0xF}          # #4's skin indices (C = its red face paint)
SCARFC = {0xA, 0xB, 0xC}
JACKET = {0x2, 0x3, 0x6, 0x8}
OUT = 0x5
GLOVE = {0x9: 0x7, 0xE: 0x7, 0xF: 0x7, 0x7: 0x2, 0xC: 0x6, 0x8: 0x2}   # fingerless dark gloves
EYE0 = (39, 24)                           # #4's eye glint in frame 0 (x, y): the anchor

# Osrid's head = MonoMyth #4's frame-0 head (the same drawing in every frame, only moved: 98%
# identical, measured), edited at measured frame-0 coordinates:
HEAD_BOX = (7, 37, 13, 48)                      # y0, y1, x0, x1 of #4's head in frame 0
EAR_BOX = (24, 28, 28, 31)                      # #4's ear: y0, y1, x0, x1 -> skin
SIDE_X = 34                                     # mask pixels at or left of this: the side plane
# the mask's area in frame 0 (rows: (back edge, profile edge)); profile from #4's own (nose 27-28)
MASK_SPANS = {21: (36, 40), 22: (35, 41), 23: (34, 41), 24: (33, 42), 25: (33, 42), 26: (33, 43),
              27: (33, 44), 28: (34, 44), 29: (34, 42), 30: (35, 42), 31: (36, 41), 32: (38, 40)}
NECK = [(x, y) for y in (29, 30, 31) for x in range(32, 36)]     # nape under the ear: shadowed hair
# tousled strands (lit side = upper right), each a light line with a dark crevice under it
STRANDS = [[(34, 10), (31, 12), (28, 14), (25, 17)], [(38, 11), (36, 13), (34, 16), (32, 19)],
           [(42, 14), (41, 16), (40, 18)], [(29, 10), (25, 12), (22, 14), (19, 17)],
           [(24, 18), (21, 19), (18, 20)]]
TUFTS = [(27, 9), (28, 8), (33, 8), (34, 7)]
MASK_HI = [(39, 22), (40, 22), (43, 27), (42, 26)]
GLYPH = [(39, 23), (40, 23),                    # brow bar (foreshortened at the front edge)
         (40, 24), (41, 24), (41, 25),          # eye
         (40, 26), (40, 27), (40, 28),          # drip
         (39, 29), (38, 29), (38, 28)]          # start of the spiral
STRAP_Y, STRAP_X = 22, (15, 33)                 # strap rows 22 (light) and 23 (dark), above the ear
BUCKLE = (19, 21, 22, 24)                       # x0, y0, x1, y1
COLLAR_Y = 30                                   # hair at/below this row tucks under the scarf
SCARF = {29: (24, 40), 30: (16, 42), 31: (14, 43), 32: (13, 44), 33: (13, 45), 34: (13, 46),
         35: (13, 46), 36: (13, 46), 37: (14, 45), 38: (15, 44), 39: (17, 42), 40: (20, 38)}
CAPE_TOP = 41


def components(mask):
    h, w = mask.shape; lab = np.zeros((h, w), int); n = 0
    for y in range(h):
        for x in range(w):
            if mask[y, x] and not lab[y, x]:
                n += 1; q = deque([(y, x)]); lab[y, x] = n
                while q:
                    cy, cx = q.popleft()
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < h and 0 <= nx < w and mask[ny, nx] and not lab[ny, nx]:
                            lab[ny, nx] = n; q.append((ny, nx))
    return lab, n


def nb4(m):
    out = np.zeros_like(m)
    out[1:] |= m[:-1]; out[:-1] |= m[1:]; out[:, 1:] |= m[:, :-1]; out[:, :-1] |= m[:, 1:]
    return out


def make_head(f0):
    """Osrid's head as a frame-0 layer (index array, 0 = empty) built on #4's own head."""
    y0, y1, x0, x1 = HEAD_BOX
    L = np.zeros((64, 64), int)
    src = f0
    hairm = np.isin(src, list(HAIR))
    skinm = np.isin(src, list(SKIN))
    region = np.zeros((64, 64), bool); region[y0:y1, x0:x1] = True
    # face span per row (skin plus #4's brown profile outline inside the face)
    for y in range(y0, y1):
        for x in range(x0, x1):
            v = src[y, x]
            if hairm[y, x]:
                L[y, x] = v
            elif skinm[y, x]:
                ey0, ey1, ex0, ex1 = EAR_BOX
                if ey0 <= y <= ey1 and ex0 <= x <= ex1:
                    L[y, x] = 0xF if v != 0x7 else 0x7          # ear skin, its shadow kept
                elif x <= SIDE_X:
                    L[y, x] = 0x7                                # mask side plane
                else:
                    L[y, x] = 0xE if v == 0xE else 0x9           # mask front: cream, paint gone
            elif v == OUT:
                L[y, x] = OUT
            elif v == 0x2 and y <= 35 and x >= 38:               # #4's soft brown profile edge
                L[y, x] = OUT
    # the mask: explicit area (clears #4's hair and lines from in front of the face), crisp profile
    for y, (mx0, mx1) in MASK_SPANS.items():
        for x in range(mx0, mx1 + 1):
            if not (EAR_BOX[0] <= y <= EAR_BOX[1] and EAR_BOX[2] <= x <= EAR_BOX[3]):
                L[y, x] = 0x7 if x <= mx0 + 1 else 0x9
        L[y, mx1 + 1] = OUT
        for x in range(mx1 + 2, x1):
            if L[y, x] != 0 and y >= 21: L[y, x] = 0
        if mx0 - 1 > EAR_BOX[3] and L[y, mx0 - 1] in HAIR: L[y, mx0 - 1] = OUT
    for (x, y) in NECK:
        L[y, x] = 0x4
    for y, (mx0, mx1) in MASK_SPANS.items():      # underside of jaw and chin
        for x in range(mx0, mx1 + 1):
            if y + 1 not in MASK_SPANS or not (MASK_SPANS[y + 1][0] <= x <= MASK_SPANS[y + 1][1]):
                if L[y + 1, x] not in (0xF,): L[y + 1, x] = OUT

    for y in range(max(MASK_SPANS) + 1, y1):        # #4's longer chin below ours: removed
        for x in range(30, x1):
            if L[y, x] in SKIN and not (y == max(MASK_SPANS) + 1 and L[y, x] == OUT): L[y, x] = 0
    for y in range(y0, min(MASK_SPANS)):             # #4's skin showing through the hair above
        for x in range(x0, x1):
            if L[y, x] in (0x9, 0xE, 0x7) and src[y, x] in SKIN: L[y, x] = 0x4
    for (x, y) in MASK_HI:
        L[y, x] = 0xE
    # strands and tufts
    def seg(p, q):
        n = max(abs(q[0] - p[0]), abs(q[1] - p[1]), 1)
        return [(round(p[0] + (q[0] - p[0]) * i / n), round(p[1] + (q[1] - p[1]) * i / n)) for i in range(n + 1)]
    for st in STRANDS:
        for p, q in zip(st, st[1:]):
            for (x, y) in seg(p, q):
                if L[y, x] in HAIR:
                    L[y, x] = 0xD
                    if L[y + 1, x] in HAIR and (x, y + 1) not in seg(p, q): L[y + 1, x] = 0x4
    for (x, y) in TUFTS:
        if L[y, x] == 0 or L[y, x] == OUT:
            L[y, x] = 0x1
    for (x, y) in TUFTS:
        for a, b in ((0, -1), (-1, 0), (1, 0)):
            if L[y + b, x + a] == 0: L[y + b, x + a] = OUT
    # the fringe edge over the mask's brow: a dark line under the hair
    y = min(MASK_SPANS)
    for x in range(MASK_SPANS[y][0], MASK_SPANS[y][1] + 1):
        if L[y - 1, x] in HAIR: L[y - 1, x] = 0x4
    # strap round the back of the head, above the ear, to the mask edge; square buckle
    sx0, sx1 = STRAP_X
    for x in range(sx0, sx1 + 1):
        for y, v in ((STRAP_Y, 0x8), (STRAP_Y + 1, 0x6)):
            if L[y, x] != 0: L[y, x] = v
        if L[STRAP_Y - 1, x] in HAIR: L[STRAP_Y - 1, x] = OUT
        if L[STRAP_Y + 2, x] in HAIR: L[STRAP_Y + 2, x] = 0x4
    bx0, by0, bx1, by1 = BUCKLE
    for y in range(by0 - 1, by1 + 2):
        for x in range(bx0 - 1, bx1 + 2):
            if bx0 <= x <= bx1 and by0 <= y <= by1:
                border = x in (bx0, bx1) or y in (by0, by1)
                L[y, x] = 0x3 if border else (0x8 if y == STRAP_Y else 0x6)
            elif L[y, x] in HAIR:
                L[y, x] = OUT
    for (x, y) in GLYPH:
        L[y, x] = OUT
    return L


def head_layer(H0, dx, dy):
    L = np.zeros((64, 64), int)
    ys, xs = np.nonzero(H0)
    for y, x in zip(ys, xs):
        Y, X = y + dy, x + dx
        if 0 <= Y < 64 and 0 <= X < 64: L[Y, X] = H0[y, x]
    return L


def frame(f, H0):
    a = f.copy()
    hair = np.isin(f, list(HAIR))
    skin = np.isin(f, list(SKIN))
    # --- hands: skin components away from the hair -> gloves (grown into #4's index-8 hand light)
    lab, n = components(skin)
    near_hair = np.zeros_like(hair)
    for y, x in zip(*np.nonzero(hair)):
        near_hair[max(0, y - 2):y + 3, max(0, x - 2):x + 3] = True
    hand = np.zeros_like(skin)
    for k in range(1, n + 1):
        comp = lab == k
        if not np.any(comp & near_hair):
            hand |= comp
    for _ in range(3):
        g2 = hand.copy()
        for y, x in zip(*np.nonzero(hand)):
            sl = (slice(max(0, y - 1), y + 2), slice(max(0, x - 1), x + 2))
            g2[sl] |= (f[sl] == 0x8)
        hand = g2
    for k, v in GLOVE.items():
        a[hand & (f == k)] = v
    # --- this frame's offset from frame 0 (#4's eye glint)
    ey, ex = np.nonzero((f == 0xF) & ~hand)
    k0 = np.argmin(ey * 64 + ex)
    dx, dy = int(ex[k0]) - EYE0[0], int(ey[k0]) - EYE0[1]
    # --- clear #4's head: hair, face skin, and the outline that belonged to them
    old = hair | (skin & ~hand)
    grow = old.copy()
    for y, x in zip(*np.nonzero(old)):
        sl = (slice(max(0, y - 1), y + 2), slice(max(0, x - 1), x + 2))
        grow[sl] |= (f[sl] == OUT)
    a[grow & ~hand] = 0
    # --- jacket: #4's coat -> quilted charcoal; the lapel band stays the brown strap
    for y in range(64):
        for x in range(64):
            if a[y, x] in (0x2, 0x3) and not hand[y, x] and ((x + y) % 6 == 0 or (x - y) % 6 == 0):
                a[y, x] = 0x6 if a[y, x] == 0x2 else 0x2
    # --- the cape over the left ~40% of the back (ragged right edge), over the jacket only
    for y in range(max(0, CAPE_TOP + dy), 64):
        cols = [x for x in range(64) if a[y, x] in JACKET or a[y, x] == OUT]
        if not cols: continue
        left, rgt = min(cols), max(cols)
        right = left + int((rgt - left) * 0.34) + (1 if (y // 3) % 2 else -1)
        for x in range(left, right + 1):
            if a[y, x] in JACKET and not hand[y, x]:
                fold = (x + 2 * y) % 9 == 0
                a[y, x] = 0xB if (fold or x <= left + 2) else 0xA
        if 0 <= right + 1 < 64 and a[y, right + 1] in JACKET:
            a[y, right + 1] = OUT
    # --- scarf bunched round the neck and left shoulder
    rows = {}
    for ry_, (x0, x1) in SCARF.items():
        for rx_ in range(x0, x1 + 1):
            rows.setdefault(rx_, []).append(ry_)
    for ry_, (x0, x1) in SCARF.items():
        for rx_ in range(x0, x1 + 1):
            x, y = rx_ + dx, ry_ + dy
            if not (0 <= x < 64 and 0 <= y < 64) or hand[y, x]:
                continue
            top = ry_ == min(rows[rx_]); bot = ry_ >= max(rows[rx_]) - 1
            fold = (rx_ - ry_) % 9 == 0
            a[y, x] = 0xC if top else 0xB if (bot or fold) else 0xA
    # --- Osrid's head over the scarf and body (never over the gloves)
    L = head_layer(H0, dx, dy)
    head = L > 0
    yy = np.arange(64)[:, None]
    under = np.isin(L, list(HAIR)) & (yy >= COLLAR_Y + dy) & np.isin(a, list(SCARFC))   # tucked in
    paste = head & ~hand & ~under
    a[paste] = L[paste]
    # --- outline round the scarf and the cape; fill enclosed holes; drop floating outline
    for y in range(64):
        for x in range(64):
            if a[y, x] == 0:
                nb = [a[y + q, x + p] for q, p in ((1, 0), (-1, 0), (0, 1), (0, -1))
                      if 0 <= y + q < 64 and 0 <= x + p < 64]
                if any(v in SCARFC for v in nb):
                    a[y, x] = OUT
    for y in range(1, 63):
        for x in range(1, 63):
            if a[y, x] == 0:
                nb = [a[y + q, x + p] for q, p in ((1, 0), (-1, 0), (0, 1), (0, -1))]
                if all(v != 0 for v in nb):
                    body = [v for v in nb if v != OUT]
                    a[y, x] = max(set(body), key=body.count) if body else OUT
    for y in range(64):
        for x in range(64):
            if a[y, x] == OUT:
                nbh = a[max(0, y - 1):y + 2, max(0, x - 1):x + 2]
                if not np.any((nbh != 0) & (nbh != OUT)):
                    a[y, x] = 0
    return a


def build(B):
    frames, _, _ = B[4]
    H0 = make_head(frames[0])
    return np.concatenate([frame(frames[j], H0) for j in range(4)], 0)


def save(a, path):
    img = Image.fromarray(a.astype(np.uint8), 'P')
    flat = []
    for i in range(16):
        flat += list(PAL[i])
    img.putpalette(flat + [0] * (768 - 48))
    img.save(path, transparency=0)


if __name__ == '__main__':
    save(build(pickle.load(open(sys.argv[1], 'rb'))), sys.argv[2])
