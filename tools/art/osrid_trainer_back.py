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

PAL = {                     # same scheme as the front: dark green jacket, iron, sheet browns
    0x0: (255, 0, 255),
    0x5: (10, 10, 12),      # outline / glyph
    0x4: (114, 42, 18),     # hair dark      (portrait)
    0x1: (160, 64, 28),     # hair mid
    0xD: (206, 104, 52),    # hair light
    0x9: (226, 210, 170),   # mask           (portrait)
    0xE: (246, 238, 210),   # mask highlight
    0x7: (178, 152, 112),   # mask shadow / skin (ear, fingers)
    0xF: (58, 58, 58),      # iron dark (pauldrons, gloves)
    0x6: (26, 34, 28),      # green-black (jacket shadow)
    0x2: (56, 64, 54),      # jacket dark green (sheet swatch 58,63,55)
    0x3: (88, 98, 84),      # jacket light / iron highlight / buckle (grey-green light)
    0x8: (92, 64, 44),      # leather strap
    0xB: (22, 44, 30),      # cape / scarf dark
    0xA: (38, 60, 42),      # cape / scarf green
    0xC: (64, 90, 62),      # cape / scarf light
}
HAIR = {0x1, 0x4, 0xD}
SKIN = {0x9, 0xE, 0x7, 0xC, 0xF}          # #4's skin indices (C = its red face paint)
SCARFC = {0xA, 0xB, 0xC}
JACKET = {0x2, 0x3, 0x6, 0x8}
OUT = 0x5
GLOVE = {0x9: 0x7, 0xE: 0x7, 0xF: 0x7, 0x7: 0xF, 0xC: 0x6, 0x8: 0xF}   # fingerless dark gloves, tan fingers
EYE0 = (39, 24)                           # #4's eye glint in frame 0 (x, y): the anchor

# Osrid's head = MonoMyth #4's frame-0 head (the same drawing in every frame, only moved: 98%
# identical, measured), edited at measured frame-0 coordinates:
HEAD_BOX = (7, 37, 13, 48)                      # y0, y1, x0, x1 of #4's head in frame 0
FACE_BOX = (18, 37, 27, 47)                     # #4's face (with ear) in frame 0
EAR_BOX = (24, 28, 28, 31)                      # #4's ear: y0, y1, x0, x1 -> skin
SIDE_X = 34                                     # mask pixels at or left of this: the side plane
# the mask's area in frame 0 (rows: (back edge, profile edge)); profile from #4's own (nose 27-28)
MASK_SPANS = {21: (36, 40), 22: (35, 41), 23: (34, 41), 24: (33, 42), 25: (33, 42), 26: (33, 43),
              27: (33, 44), 28: (34, 44), 29: (34, 42), 30: (35, 42), 31: (36, 41), 32: (38, 40)}
NECK = [(x, y) for y in (29, 30, 31) for x in range(32, 36)]     # nape under the ear: shadowed hair
# tousled strands (lit side = upper right), each a light line with a dark crevice under it
TUFT_ANGLES = [62, 80, 98, 116, 134, 152, 170, 188, 206, 224]   # top and back of the head
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
# iron pauldrons on both shoulders, frame-0 rows: (left, right); they follow the frame offset
PAULDRONS = [{34: (9, 15), 35: (7, 17), 36: (5, 18), 37: (4, 18), 38: (4, 18), 39: (4, 17), 40: (5, 16), 41: (6, 14)},
             {36: (44, 47), 37: (43, 48), 38: (43, 48), 39: (44, 47)}]          # near (his left) | far, peeking
CREASES = [128, 62]                            # two big scarf folds hanging from the neck (deg, y down)


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


# Osrid's head in a MonoMyth back-pic PROFILE (round 6). Studied from MonoMyth's front/back pairs
# (back 2 <-> #80, back 3 <-> #78, back 6 <-> #116, back 8 <-> #88): their back pics are near-profile
# heads facing right, seen slightly from behind (face about 40% of the head's width, ear just
# behind it, hair keeping the front design seen from the side); only the torso turns away.
# Built from the approved portrait: its hair (dominant-vote downscale at natural proportions) keeps
# the crown and the back, with spikes swept up and back; the face becomes the mask in profile
# (forehead under the fringe, brow ridge, eye socket, nose, lips, chin, jaw), carrying the Eye of
# Horus side-on (brow bar, foreshortened eye with its tail back toward the ear, drip, spiral); the
# ear sits behind it; the strap and buckle sit above the ear (his character sheet).
HEAD_TRACED = [
    "..............KKKKKKK............",
    "...........KKKKKKKKKKKK..........",
    "..........KKKKmllKdllKKKK........",
    ".........KKlmmmmmlmmmlmlKK.......",
    ".........KKKmmmmmmmmmmmmmKK......",
    "......KKKKdlmmmmmmmmmmmmmdKK.....",
    "....KKKKllmmmmmmmmmmmmmmmmlKK....",
    "...KKKlllmmmmmmmmmmddmlmdmddK....",
    "..KKllmmmmmmmmmmddddKsdoooKK.....",
    "..KKdmuuummmmmmdddKsKoooowooK....",
    "...KKtuTutttttttttssoooooowooK...",
    "....KluuummmmKssKKssoooKKKKwoK...",
    "...KKlmmmmmmdKssKKssooooooooooK..",
    ".KKllmmmmmmddKsoKssoooooKKKooK...",
    "KKKmlmmmmmmmdKssKssoooKKoKoKoK...",
    "KllmmmmmmmmmmKssKssoooooKKKowoK..",
    "KKKdmmmmddddmdKsKssooooKoKooowoK.",
    ".KKKmmmddddKdddKKssoooKooKooooK..",
    ".KKmmmddddddKdddKssooKoooKoooK...",
    "KKKmmddddddmddddKssooKoooKoooK...",
    "KKlmdddmddmmddddKssoooKooKoooK...",
    "KKKddddddddKdddddKssoooooooooK...",
    "..KKdddddddddKdddKssssssssssK....",
    "..KddddddddKdddddKKsssssssssK....",
    ".KKdddddddddmddddKddKsssssKK.....",
    "..KKKKmdddKKddKKKKKKKKKKKK.......",
    "....KldKKKKKdddK.................",
    "...KKddKKKKKdddK.................",
]
HEAD_TRACED_CODE = {'K': 0x5, 'd': 0x4, 'm': 0x1, 'l': 0xD, 'o': 0x9, 'w': 0xE, 's': 0x7, 'T': 0x6,
                    'u': 0x3, 't': 0x8}
HEAD_TRACED_OX, HEAD_TRACED_OY = 15, 6          # head grid (0,0) in frame-0 coordinates


def make_head(f0):
    L = np.zeros((64, 64), int)
    for y, row in enumerate(HEAD_TRACED):
        for x, ch in enumerate(row):
            if ch in HEAD_TRACED_CODE:
                L[y + HEAD_TRACED_OY, x + HEAD_TRACED_OX] = HEAD_TRACED_CODE[ch]
    return L


def make_head_from_4(f0):
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
                    L[y, x] = 0x7                                # ear (skin tan)
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
    # hair, the way the portrait and the front draw it: clumps with lit tips, dark separations,
    # small swept tufts breaking the outline (2-3 px, not spikes)
    hm = np.isin(L, list(HAIR))
    hy, hx = np.nonzero(hm)
    cy, cx = hy.mean(), hx.mean() + 2
    def ang(x, y): return (np.degrees(np.arctan2(cy - y, x - cx)) + 360) % 360
    def outward(th, r):
        return cx + r * np.cos(np.radians(th)), cy - r * np.sin(np.radians(th))
    rmax = {}
    for y, x in zip(hy, hx):
        k = int(ang(x, y)) // 4
        rmax[k] = max(rmax.get(k, 0), np.hypot(x - cx, y - cy))
    tuft_px = []
    for th in TUFT_ANGLES:
        r0 = rmax.get(int(th) // 4)
        if r0 is None: continue
        for i, (w, ext) in enumerate(((1.0, 1), (0.6, 2), (0.0, 3))):
            ta = th + 9 * (i + 1)                      # swept back (counter-clockwise = toward the nape)
            px, py = outward(ta, r0 + ext - 0.5)
            pts = [(round(px), round(py))]
            if w >= 1.0:
                qx, qy = outward(ta - 8, r0 + ext - 0.5); pts.append((round(qx), round(qy)))
            for (x, y) in pts:
                if 0 <= x < 64 and 0 <= y < 64 and L[y, x] in (0, OUT):
                    L[y, x] = 0x1; tuft_px.append((x, y, i))
    hm = np.isin(L, list(HAIR))
    for y, x in zip(*np.nonzero(hm)):
        th = ang(x, y); r = np.hypot(x - cx, y - cy); rm = rmax.get(int(th) // 4, r)
        v = 0x1
        if 160 <= th <= 300 and r > rm - 3: v = 0x4                    # shadowed back and nape
        if y >= STRAP_Y + 2 and y <= STRAP_Y + 3: v = 0x4               # shadow under the strap
        up = L[y - 1, x] in (0, OUT)
        if up and (20 <= th <= 160): v = 0xD                          # rim light on top edges
        L[y, x] = v
    for (x, y, i) in tuft_px:
        L[y, x] = 0xD if i >= 1 else 0x1                               # lit tuft tips
    for th in TUFT_ANGLES:                                             # dark clump separators
        r0 = rmax.get(int(th) // 4)
        if r0 is None: continue
        for d in (2.0, 3.0, 4.0):
            x, y = outward(th - 4, r0 - d)
            x, y = round(x), round(y)
            if 0 <= x < 64 and 0 <= y < 64 and L[y, x] in HAIR: L[y, x] = 0x4
    hm2 = np.isin(L, list(HAIR))
    ring = nb4(hm2) & (L == 0)
    L[ring] = OUT
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
    # --- anchor: #4's eye glint (index F) nearest where the face sits relative to the hair
    hy_, hx_ = np.nonzero(hair)
    gy, gx = np.nonzero(f == 0xF)
    ty, tx = hy_.mean() + 3, hx_.mean() + 9
    k0 = np.argmin((gy - ty) ** 2 + (gx - tx) ** 2)
    dx, dy = int(gx[k0]) - EYE0[0], int(gy[k0]) - EYE0[1]
    # --- hands: skin regions mostly outside the face box (frame-0 face, shifted) -> gloves
    lab, n = components(skin)
    fy0, fy1, fx0, fx1 = FACE_BOX
    hand = np.zeros_like(skin)
    for k in range(1, n + 1):
        cy_, cx_ = np.nonzero(lab == k)
        inside = ((cy_ >= fy0 + dy) & (cy_ <= fy1 + dy) & (cx_ >= fx0 + dx) & (cx_ <= fx1 + dx)).mean()
        if inside < 0.5:
            hand |= lab == k
    for _ in range(3):
        g2 = hand.copy()
        for y, x in zip(*np.nonzero(hand)):
            sl = (slice(max(0, y - 1), y + 2), slice(max(0, x - 1), x + 2))
            g2[sl] |= (f[sl] == 0x8)
        hand = g2
    for k, v in GLOVE.items():
        a[hand & (f == k)] = v
    # --- clear #4's head: hair, face skin, and the outline that belonged to them
    old = hair | (skin & ~hand)
    grow = old.copy()
    for y, x in zip(*np.nonzero(old)):
        sl = (slice(max(0, y - 1), y + 2), slice(max(0, x - 1), x + 2))
        grow[sl] |= (f[sl] == OUT)
    a[grow & ~hand] = 0
    # --- jacket: #4's own three coat tones, recoloured to his dark green (flat cel shapes; the
    #     palette does it: 6 green-black, 2 dark green, 3 light). The lapel band stays the strap.
    # --- the cape down the near (left) side of the back: #4's coat shading in cape greens, with a
    #     few long vertical folds; ragged right edge
    for y in range(max(0, CAPE_TOP + dy), 64):
        cols = [x for x in range(64) if a[y, x] in JACKET or a[y, x] == OUT]
        if not cols: continue
        left, rgt = min(cols), max(cols)
        right = left + int((rgt - left) * 0.36) + (1 if (y // 3) % 2 else -1)
        for x in range(left, right + 1):
            if a[y, x] in JACKET and not hand[y, x]:
                base = {0x6: 0xB, 0x2: 0xA, 0x3: 0xC, 0x8: 0xA}[int(a[y, x])]
                k = x - left
                if k in (4, 9) and y % 7 != 0: base = 0xB                      # long folds
                elif k in (5, 10) and base == 0xA: base = 0xC                  # lit edge of each fold
                a[y, x] = base
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
            # bunched folds hanging from the neck (portrait): creases at irregular angles, lit
            # ridges beside them, a light rim along the top
            ang_ = (np.degrees(np.arctan2(ry_ - 27, rx_ - 31)) + 360) % 360
            v = 0xA
            for c in CREASES:
                dd = (ang_ - c + 180) % 360 - 180
                if abs(dd) < 6: v = 0xB
                elif 6 <= dd < 14: v = 0xC if v == 0xA else v
            if ry_ == min(rows[rx_]): v = 0xC
            if ry_ >= max(rows[rx_]) - 1: v = 0xB
            a[y, x] = v
    # --- iron pauldrons (dark iron, lit top edge, outlined)
    for P in PAULDRONS:
        pm = np.zeros((64, 64), bool)
        for ry_, (x0, x1) in P.items():
            for rx_ in range(x0, x1 + 1):
                x, y = rx_ + dx, ry_ + dy
                if 0 <= x < 64 and 0 <= y < 64 and not hand[y, x]: pm[y, x] = True
        top, bot = min(P), max(P)
        cxp = (P[top][0] + P[top][1]) / 2
        for y, x in zip(*np.nonzero(pm)):
            ry_, rx_ = y - dy, x - dx
            k = (ry_ - top) % 3                       # overlapping plates (lames), as in the portrait
            v = 0x3 if k == 0 else (0xF if k == 1 else 0x6)
            if ry_ == bot: v = 0x6
            if (rx_, ry_) == (round(cxp), top + 1): v = 0x3              # rivet
            a[y, x] = v
        a[nb4(pm) & ~pm & ~hand] = OUT
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
                if not np.any((nbh != 0) & (nbh != OUT)) and np.any(nbh == 0):   # floating, in the open
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
