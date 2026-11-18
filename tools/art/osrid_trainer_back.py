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
    0x9: (236, 232, 220),   # mask: blank white (seen from behind: no holes, no markings)
    0xE: (214, 158, 120),   # skin (ear, neck, fingers)
    0x7: (160, 104, 76),    # skin shade
    0xF: (58, 60, 72),      # iron dark (pauldrons, gloves): cool grey (MonoMyth greys lean blue)
    0x6: (26, 30, 32),      # jacket shadow: slightly cool (MonoMyth shadows shift toward blue)
    0x2: (50, 58, 56),      # jacket darker grey-green (mid)
    0x3: (84, 96, 74),      # jacket light: warmer, greener (MonoMyth lights shift toward yellow)
    0x8: (92, 64, 44),      # leather strap
    0xB: (198, 192, 180),   # mask shade (slot freed: the cape's darkest green merges into 6 in build())
    0xA: (34, 66, 46),      # cape / scarf dark green
    0xC: (70, 104, 60),     # cape / scarf light: yellow-green
}
HAIR = {0x1, 0x4, 0xD}
SKIN = {0x9, 0xE, 0x7, 0xC, 0xF}          # #4's skin indices (C = its red face paint)
SCARFC = {0xA, 0xB, 0xC}
JACKET = {0x2, 0x3, 0x6, 0x8}
OUT = 0x5
GLOVE = {0x9: 0xE, 0xE: 0xE, 0xF: 0xE, 0x7: 0xF, 0xC: 0x6, 0x8: 0xF}   # fingerless dark gloves, tan fingers
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
HEAD_MODE = 'grid'                              # 'lost' (round 10) | 'grid' (round 9 HEAD_TRACED)
COLLAR_Y = 33                                   # hair at/below this row tucks under the scarf
SCARF = {29: (24, 40), 30: (16, 42), 31: (14, 43), 32: (13, 44), 33: (13, 45), 34: (13, 46),
         35: (13, 46), 36: (13, 46), 37: (14, 45), 38: (15, 44), 39: (17, 42), 40: (20, 38)}
CAPE_TOP = 41
CAPE_FOLD_X = 22                                # #4's own coat fold that becomes the cape's edge
SHOULDER = {38: (13, 19), 39: (11, 20), 40: (10, 21), 41: (10, 21), 42: (10, 20), 43: (10, 19)}
STRAP_PATH = [(44 - i, 41 + i // 2) for i in range(0, 34)]
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


# Round 11 head: built from MonoMyth back 2 (Monty)'s own pixels (user: his hair is the closest style to
# Osrid's, slightly longer; his face and glasses -> the blank white mask; the glasses arm -> the strap round
# the ear). Hair recoloured to the auburn ramp and lengthened 2 px at the nape; the mask is a tall rigid
# plate covering the whole face and forehead (smooth convex front edge, blank), a few lock tips over its
# top; the strap runs from its back edge over the ear to the buckle; the neck goes into the high scarf.
# (Superseded:) Osrid's head seen FROM BEHIND (round 9; user: "the better angle would be where you don't see the mask
# at all, just the back of his hair with the connecting strap"; "hair too thick ... shading and colour
# mixes out of alignment with the simpler MonoMyth mixes"). Hand-drawn pixel by pixel, not generated:
# his short spiky auburn hair (portrait / front: thin pointed locks flaring back) as a jagged cap, three
# hair tones + black outline only (flat mid base, shadow rim on the left and at the nape, one lit
# cluster upper right, two lock partings); the mask strap runs across the back of the skull from ear to
# ear with its buckle off-centre; ears (skin = the glove-finger tan) at strap height; the nape shows
# between the lowest locks and tucks under the scarf.
HEAD_TRACED = [
    "......................................",
    "......................................",
    "............KKKKKK....................",
    "..........KKllllllKK..................",
    "........KKllmmmmmmllK.................",
    ".......KlllmmmmlmmmmlK................",
    "......KlllmmmldmmmmmmlK...............",
    "....KKlllmmmddmmmmmmmmK...............",
    "...KllmlmmmdmmmmmmmmmmlK..............",
    "....KlmmmmmmmmmmmmmlmNdMK.............",
    "....KlmmmmmmmmmmmldmNMNMMK............",
    "...KlmmmmmmmmmmmddmmNMMMMMK...........",
    "...KKlmmmmmmmmddmmmNMMMMMMK...........",
    "..KllmmmmmmmmmmmmmmNMMMMMMMK..........",
    "..KlllmmmmmmmmmmmmmNMMMMMMMK..........",
    "..KllmmmmmmmmmmmmmmNMMMMMMMK..........",
    "..KlmmmmmmmmmmmmmmmNMMMMMMMK..........",
    ".KKlmmmmmmmmmmmmmmmNMMMMMMMK..........",
    "KdddddddduuddddddddNMMMMMMMK..........",
    ".KKdddtttTuttdtttdtNMMMMMMMK..........",
    "...KddddduudddddshdNMMMMMMMK..........",
    "..KKddddddddddddshdNMMMMMMMK..........",
    ".KddddddddddddddshsNMMMMMMMK..........",
    "..KKKddddddddddd8hsNMMMMMMMK..........",
    "....Kddddddddddh8shNMMMMMMMK..........",
    ".....Kdddddddddhh8hNMMMMMMMK..........",
    ".....KdddddddddhhhsNMMMMMMK...........",
    "......KddKddddKAAAANMMMMMMK...........",
    "......KdKKddddAAAAAANMMMMK............",
    ".......K..KddKAAAAAANNNNMK............",
    "...........KdKAKAAKKKNNMK.............",
    "............KAAKKK..KNMK..............",
    ".............KK......KK...............",
]
MASK_SHADE_TMP = 0x11                          # mask shade until build() gives it slot B
HEAD_TRACED_CODE = {'K': 0x5, 'd': 0x4, 'm': 0x1, 'l': 0xD, 't': 0x8, 'T': 0x6, 'u': 0x3,
                    's': 0xE, 'h': 0x7, '8': 0x8, 'M': 0x9, 'N': MASK_SHADE_TMP, 'C': 0xC, 'A': 0xA, 'B': 0xB}
HEAD_TRACED_OX, HEAD_TRACED_OY = 13, 5         # head grid (0,0) in frame-0 coordinates


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


# Round 10 head: MonoMyth #4's OWN head, converted per frame, so the head always sits at the angle its
# body and throwing arm were drawn for (user: "orient his body and head to be in alignment ... a small
# edge of white mask will help you get the angle right so the arm when you throw doesn't look weird").
# The head is turned a little further away than #4's: #4's face becomes hair except a smooth crescent
# at its front edge, which is the white mask (no glyph). #4's hair keeps its own simple MonoMyth shading
# (lit top, shadowed lower half, a few crown strands, part of the outline in the dark hair tone); the
# palette makes it Osrid's auburn. The mask strap runs from a buckle on the back of the skull to the
# mask's edge, above a small ear.
# (x, y, ux, uy, length, tone) in frame-0 coords: three on the crown, four flaring back from the skull
# (angle deg from the hair's centre, 0 = right, 90 = up; length; tone): crown and back of the skull
SPIKES = [(115, 3, 0x1), (88, 3, 0xD), (150, 3, 0x1), (180, 3, 0x1)]
HEM_BELOW_EYE = 5                               # hair hem (lock tips add 0-4 px) below #4's eye row
HEM_TIPS = [2, 0, 3, 1, 4, 2, 0, 1, 3, 4, 1, 0, 2, 3, 1, 4, 0, 2]   # irregular lock lengths (px)
NECK_W = 8                                      # scarf wrap width behind the mask (px)
LOCK_TIPS = [0, 1, 3, 2, 0, 2, 4, 1]               # how far each column's lit lock hangs down (px)
CLEAR = 0x10                                    # head_lost() marker: erase this body pixel
MASK_TOP_ABOVE_EYE = 8                          # mask starts this far above #4's eye row (under the crown)
MASK_W = 3                                      # crescent width (px) at its widest
def head_lost(f, hand, dx_, dy):
    hair = np.isin(f, list(HAIR))
    face = np.isin(f, list(SKIN)) & ~hand
    eye_y = EYE0[1] + dy
    ys8 = [y for y in np.nonzero((f == 0x8) & ~hand)[0] if y > eye_y]   # collar (not the raised cuff)
    ytop8 = min(ys8) if ys8 else 64              # #4's collar top: the head ends here
    face[ytop8:] = False
    L = np.zeros((64, 64), int)
    L[hair] = f[hair]
    rows = [y for y in range(64) if face[y].any()]
    if not rows:
        return L
    # The mask is Osrid's, not #4's face: one unbroken crescent along the head's FRONT edge, from just
    # under the crown to the chin (portrait/front: the mask covers the whole face up to the hairline,
    # the hair sits BEHIND it; no fringe falls over it). Everything behind the crescent is hair, so none
    # of #4's eye / brow / mouth / jaw lines survive (round 10 feedback: "a line like a mouth", "bangs").
    headm = (hair | face).copy()
    headm[ytop8:] = False
    hrows = [y for y in range(64) if headm[y].any()]
    fre = {y: int(np.nonzero(face[y])[0].max()) for y in rows}
    fsm = {y: int(np.median([fre[q] for q in rows if abs(q - y) <= 3])) for y in rows}   # drop nose/lips
    raw = {y: (fsm[y] if y in fsm else int(np.nonzero(headm[y])[0].max())) for y in hrows}
    edge = {y: int(round(np.mean([raw[q] for q in hrows if abs(q - y) <= 2]))) for y in hrows}
    for y in hrows:
        xl = int(np.nonzero(headm[y])[0].min())
        for x in range(xl, 64):
            if x > edge[y]:
                L[y, x] = 0                                  # trimmed: nose, lips, stray fringe tips
            elif L[y, x] == 0:
                # turned-away side of the head = hair, in #4's own scheme: lit locks above, shadow
                # below, the lit locks ending in points that hang into the shadow (not a straight cut)
                L[y, x] = 0x1 if y < eye_y + 1 + LOCK_TIPS[x % len(LOCK_TIPS)] else 0x4
    for y in hrows:                                          # #4's brown face outline left in front of
        for x in range(edge[y] + 2, min(64, edge[y] + 4)):   # the new edge -> cleared in frame()
            if f[y, x] == 0x2:
                L[y, x] = CLEAR
    # Osrid's hair is SHORT (portrait / front): #4's long mop is cut at an irregular hem of lock tips;
    # below it the back of the head is empty space, and only a neck-wide wrap of his scarf runs from
    # under the hair down into the collar, just behind the mask's chin (scarf wrapped high, portrait).
    for y in hrows:
        if y not in edge: continue
        scarf_l = edge[y] - MASK_W - NECK_W
        for x in range(64):
            if L[y, x] not in (0x1, 0x4, 0xD): continue
            hem = eye_y + HEM_BELOW_EYE + HEM_TIPS[x % len(HEM_TIPS)]
            if y < hem: continue
            if x >= scarf_l:
                top = L[y - 1, x] in (0x1, 0x4, 0xD)
                L[y, x] = 0xC if top else (0xB if x <= scarf_l + 1 or y >= ytop8 - 1 else 0xA)
            else:
                L[y, x] = 0                                   # cut: no hair mass below the hem
    mtop, mbot = eye_y - MASK_TOP_ABOVE_EYE, rows[-1]
    for y in range(mtop, mbot + 1):
        if y not in edge:
            continue
        w = min(MASK_W, 1 + (y - mtop), 1 + (mbot - y))      # tapers to 1 px at the top and the chin
        for x in range(edge[y] - w + 1, edge[y] + 1):
            L[y, x] = 0x9
        if w >= 2:
            L[y, edge[y] - w + 1] = 0x7                      # shaded rim where the hair meets it
    # strap: buckle on the back of the skull, band to the mask edge (2 rows: leather, shadow)
    sy = eye_y - 2
    hx = np.nonzero(hair[sy])[0]
    mx = [x for x in range(64) if L[sy, x] in (0x9, 0x7)]
    if len(hx) and mx:
        xl, xr = int(hx.min()) + 1, min(mx)
        for x in range(xl, xr):
            k = (x - xl) * 2 // max(1, xr - xl)          # drops 1 px toward the back (band round a skull)
            yy = sy + 1 - k
            for r, v in ((0, 0x8), (1, 0x6)):
                if L[yy + r, x] in (0x1, 0x4, 0xD): L[yy + r, x] = v
        bx = xl + 4
        for y in range(sy - 1, sy + 3):
            for x in range(bx, bx + 3):
                if L[y, x] in (0x1, 0x4, 0xD, 0x8, 0x6):
                    L[y, x] = 0x3 if (x in (bx, bx + 2) or y in (sy - 1, sy + 2)) else 0x6
    # #4's inner face lines (eye, brow, ear) inside what is now hair: anything not connected to the
    # outside of the head is a hole -> dark hair tone (MonoMyth draws inner hair lines in that tone)
    outside = np.zeros((64, 64), bool)
    q = deque([(y, x) for y in range(64) for x in (0, 63)] + [(y, x) for x in range(64) for y in (0, 63)])
    while q:
        y, x = q.popleft()
        if outside[y, x] or L[y, x] > 0: continue
        outside[y, x] = True
        for dy2, dx2 in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if 0 <= y + dy2 < 64 and 0 <= x + dx2 < 64: q.append((y + dy2, x + dx2))
    hole = (L == 0) & ~outside
    hole[ytop8:] = False
    L[hole] = 0x4
    # Osrid's spiky locks flaring back and up: from the hair's centre, march along each angle to the
    # silhouette and grow a tapering lock there (2 px base, pointed tip)
    hy2, hx2 = np.nonzero(np.isin(L, [0x1, 0x4, 0xD]))
    cy, cx = hy2.mean(), hx2.mean()
    for ang, n, v in SPIKES:
        ux, uy = np.cos(np.radians(ang)), -np.sin(np.radians(ang))
        r = 0.0
        while True:
            px, py = int(round(cx + ux * (r + 1))), int(round(cy + uy * (r + 1)))
            if not (0 <= px < 64 and 0 <= py < 64) or L[py, px] == 0: break
            r += 1
        bx, by = cx + ux * r, cy + uy * r
        for i in range(0, n + 1):
            half = (n - i) / 2.0                                  # triangle: wide at the base, 1 px tip
            pts = [(bx + ux * i + (-uy) * t, by + uy * i + ux * t) for t in np.arange(-half, half + 0.01, 0.5)]
            for fx_, fy_ in pts:
                px, py = int(round(fx_)), int(round(fy_))
                if 0 <= px < 64 and 0 <= py < 64 and L[py, px] == 0 and f[py, px] in (0, OUT):
                    L[py, px] = v
    # outline ring where the head meets empty space; the mask's edge gets black, not #4's brown line
    solid = (L > 0) & (L != CLEAR)
    ring = np.zeros_like(solid)
    ring[1:] |= solid[:-1]; ring[:-1] |= solid[1:]; ring[:, 1:] |= solid[:, :-1]; ring[:, :-1] |= solid[:, 1:]
    near_mask = np.zeros_like(solid)
    m = np.isin(L, [0x9, 0x7])
    L_clear = L == CLEAR
    near_mask[:, :-1] |= m[:, 1:]; near_mask[:, 1:] |= m[:, :-1]; near_mask[1:] |= m[:-1]; near_mask[:-1] |= m[1:]
    body = np.isin(f, [0x2, 0x3, 0x6, 0x8, 0xA, 0xB]) & ~(near_mask & (f == 0x2))   # #4's coat stays
    L[ring & ~solid & ~L_clear & ~(body & ~np.isin(f, list(SKIN)))] = OUT
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
    # --- body = MonoMyth #4's own coat pixels, RECOLOURED (no drawn patterns; round 7, user: "the whole
    #     backsprite looks artificial versus actual monomyth backsprites"):
    #     coat 6/2/3 -> his jacket greens (palette); #4's thick collar (8, and the coat shading
    #     inside its band) -> his wrapped scarf; #4's tie A/B -> the hanging scarf end (palette);
    #     coat behind #4's own fold line -> the cape; #4's near shoulder -> the iron pauldron.
    coat = np.isin(f, [0x2, 0x3, 0x6]) & ~hand
    col8 = (f == 0x8) & ~hand
    ys8 = np.nonzero(col8)[0]
    if len(ys8):
        top8 = ys8.min()
        for y in range(top8, min(64, top8 + 6)):
            xs = np.nonzero(col8[y])[0]
            if len(xs) >= 2:
                for x in range(xs.min(), xs.max() + 1):
                    if coat[y, x]: a[y, x] = {0x3: 0xA, 0x2: 0xB, 0x6: 0xB}[int(f[y, x])]
        a[col8] = 0xC
    # cape: coat pixels behind #4's own fold line (the dark 6 nearest x = CAPE_FOLD_X in each row)
    for y in range(CAPE_TOP + dy, 64):
        xs6 = [x for x in range(64) if f[y, x] == 0x6 and abs(x - (CAPE_FOLD_X + dx)) <= 4]
        if not xs6: continue
        xf = min(xs6, key=lambda x: abs(x - (CAPE_FOLD_X + dx)))
        for x in range(0, xf):
            if coat[y, x]: a[y, x] = {0x2: 0xA, 0x3: 0xC, 0x6: 0xB}[int(f[y, x])]
        a[y, xf] = OUT
    # pauldron: #4's near shoulder cap recoloured to iron, keeping its curved shading
    sh = np.zeros((64, 64), bool)
    for ry_, (x0, x1) in SHOULDER.items():
        for rx_ in range(x0, x1 + 1):
            x, y = rx_ + dx, ry_ + dy
            if 0 <= x < 64 and 0 <= y < 64 and coat[y, x] and a[y, x] not in (0xA, 0xB, 0xC): sh[y, x] = True
    for y, x in zip(*np.nonzero(sh)):
        a[y, x] = {0x2: 0xF, 0x3: 0x3, 0x6: 0x6}[int(f[y, x])]
    for y, x in zip(*np.nonzero(sh)):
        if y > 0 and not sh[y - 1, x] and a[y - 1, x] != 0: a[y, x] = 0x3          # lit upper rim
        if y + 1 < 64 and not sh[y + 1, x]: a[y, x] = OUT                            # lower edge of the plate
    # one leather strap across the back, from the far shoulder toward the near hip (2:1 steps)
    for i, (sx_, sy_) in enumerate(STRAP_PATH):
        x, y = sx_ + dx, sy_ + dy
        for k, v in ((0, 0x8), (1, 0x8), (2, 0x6)):
            if 0 <= y + k < 64 and 0 <= x < 64 and coat[y + k, x] and a[y + k, x] in (0x2, 0x3, 0x6):
                a[y + k, x] = v
    # --- Osrid's head over the scarf and body (never over the gloves)
    L = head_lost(f, hand, dx, dy) if HEAD_MODE == 'lost' else head_layer(H0, dx, dy)
    head = L > 0
    yy = np.arange(64)[:, None]
    under = (L > 0) & ~np.isin(L, list(SCARFC) + [0x9]) & (yy >= COLLAR_Y + dy) & np.isin(a, list(SCARFC))   # hair/nape tuck in
    a[L == CLEAR] = 0
    L[L == CLEAR] = 0
    head = L > 0
    paste = head & ~hand & ~under
    a[paste] = L[paste]
    # bits of #4's old face outline now cut off from the body by the new head: drop them
    labb, nb_ = components((a > 0) & ~paste)
    for k in range(1, nb_ + 1):
        if (labb == k).sum() < 15:
            a[labb == k] = 0
    lab, n = components(a > 0)
    for k in range(1, n + 1):
        if (lab == k).sum() < 20:
            a[lab == k] = 0
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
    out = np.concatenate([frame(frames[j], H0) for j in range(4)], 0)
    out[out == 0xB] = 0x6                       # cape darkest -> the jacket's near-black (frees slot B)
    out[out == MASK_SHADE_TMP] = 0xB            # the mask's soft shade
    return out


def save(a, path):
    img = Image.fromarray(a.astype(np.uint8), 'P')
    flat = []
    for i in range(16):
        flat += list(PAL[i])
    img.putpalette(flat + [0] * (768 - 48))
    img.save(path, transparency=0)


if __name__ == '__main__':
    save(build(pickle.load(open(sys.argv[1], 'rb'))), sys.argv[2])
