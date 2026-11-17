"""Osrid trainer BACK pic (2026-11-17, round 2).

Base: MonoMyth back #4 (an adult rear bust facing right with a full 4-frame throw), used for body,
arm and animation ONLY. Round 1 kept #4's head, which gave too much hair and a face-like profile.
User: "make his backsprite more accurate to the actual design of Osrid". #4's head is now cleared,
and Osrid's head is built from explicit shapes with his portrait's balance:
  * hair: skull mass plus six spikes swept up and back, a fringe falling over the mask, dark
    strand lines separating the spikes, rim light on the top right (the side toward the light)
  * mask: side-on (3/4 from behind): a smooth front edge (a mask, no nose), side-plane shadow,
    and only the outer edge of the eye glyph (brow end, lid, pupil) plus the drip at the front
  * ear just behind the mask
  * scarf: his thick dark green wrap round the neck and shoulders (portrait), over the nape
  * hands: tan leather gloves; coat: his armour brown-grey; lapel band: his brown strap
Shapes are in frame-0 coordinates and follow the head through the throw (offset = #4's eye glint).

Usage: python3 -I osrid_trainer_back.py BACKS_PKL OUT.png   (64x256, 4 frames)
"""
import sys, pickle
import numpy as np
from PIL import Image
from collections import deque

PAL = {
    0x0: (255, 0, 255),
    0x5: (8, 8, 10),        # outline / glyph
    0x4: (90, 34, 18),      # hair dark
    0x1: (156, 62, 26),     # hair mid
    0xD: (210, 104, 50),    # hair light
    0x9: (230, 214, 172),   # mask
    0xE: (248, 240, 212),   # mask highlight
    0x7: (184, 158, 118),   # mask shadow / glove light
    0xF: (176, 112, 78),    # ear (skin)
    0x6: (44, 40, 42),      # coat dark
    0x2: (82, 74, 66),      # coat mid
    0x3: (112, 100, 86),    # coat light
    0x8: (126, 84, 52),     # leather strap / glove
    0xB: (30, 48, 34),      # scarf dark
    0xA: (50, 78, 54),      # scarf mid
    0xC: (78, 110, 72),     # scarf light
}
HAIR = {0x1, 0x4, 0xD}
SKIN = {0x9, 0xE, 0x7, 0xC, 0xF}          # #4's skin indices (C = its red face paint)
COAT = {0x2, 0x3, 0x6, 0x8, 0xA, 0xB}     # #4's coat, lapel and tie
SCARFC = {0xA, 0xB, 0xC}
OUT = 0x5
GLOVE = {0x9: 0x7, 0xE: 0x7, 0xF: 0x7, 0x7: 0x8, 0xC: 0x8, 0x8: 0x7}
EYE0 = (39, 24)                           # #4's eye glint in frame 0 (x, y): the anchor

# Osrid's head from behind, frame-0 coordinates
SKULL = (28.0, 21.5, 10.0, 10.5)          # centre x, centre y, rx, ry
SPIKES = [((25, 12), (31, 11), (21, 3)),  # (base a, base b, tip): crown, swept back
          ((30, 11), (36, 13), (33, 5)),
          ((20, 14), (25, 12), (12, 7)),
          ((17, 19), (20, 14), (8, 14)),
          ((17, 25), (18, 19), (9, 24)),
          ((20, 30), (17, 25), (12, 31)), # nape
          ((26, 11), (30, 11), (27, 6)),  # short crown tuft
          ((34, 15), (39, 15), (36, 20))] # fringe over the mask (last)
STRAND_FROM = (30, 21)
MASK = {18: (37, 40), 19: (36, 42), 20: (35, 43), 21: (35, 44), 22: (35, 44), 23: (35, 44),
        24: (35, 44), 25: (35, 44), 26: (35, 43), 27: (35, 43), 28: (35, 43), 29: (35, 42),
        30: (36, 42), 31: (36, 41), 32: (37, 41), 33: (38, 40), 34: (39, 39)}
EAR = [(x, y) for x in (33, 34) for y in range(23, 28)]
GLYPH = [(42, 23), (43, 23), (44, 23),        # upper lid (outer corner)
         (43, 24), (44, 24),                  # pupil at the profile edge
         (43, 25),                            # lower lid
         (42, 26), (42, 27), (42, 28)]        # drip
HILITE = [(41, 19), (42, 20), (43, 21)]
SCARF = {33: (31, 41), 34: (28, 43), 35: (25, 44), 36: (22, 45), 37: (20, 46), 38: (18, 46),
         39: (17, 45), 40: (17, 43), 41: (18, 40), 42: (21, 36)}


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


def line(x0, y0, x1, y1, start=0.0):
    n = int(max(abs(x1 - x0), abs(y1 - y0), 1))
    for i in range(int(n * start), n + 1):
        yield int(round(x0 + (x1 - x0) * i / n)), int(round(y0 + (y1 - y0) * i / n))


def head_layer(dx, dy):
    L = np.zeros((64, 64), int)
    yy, xx = np.mgrid[0:64, 0:64]
    cx, cy, rx, ry = SKULL
    cx += dx; cy += dy
    hair = ((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2 <= 1
    fringe = np.zeros_like(hair)
    for k, (p0, p1, tp) in enumerate(SPIKES):
        (x0, y0), (x1, y1), (x2, y2) = [(p[0] + dx, p[1] + dy) for p in (p0, p1, tp)]
        d1 = (xx - x1) * (y0 - y1) - (x0 - x1) * (yy - y1)
        d2 = (xx - x2) * (y1 - y2) - (x1 - x2) * (yy - y2)
        d3 = (xx - x0) * (y2 - y0) - (x2 - x0) * (yy - y0)
        tri = ~(((d1 < 0) | (d2 < 0) | (d3 < 0)) & ((d1 > 0) | (d2 > 0) | (d3 > 0)))
        hair |= tri
        if k == len(SPIKES) - 1:
            fringe = tri
    ang = (np.degrees(np.arctan2(cy - yy, xx - cx)) + 360) % 360
    edge = hair & ~nb4(~hair)
    edge = hair & nb4(~hair)
    dist = np.where(edge, 0, 99)
    for k in range(1, 4):
        dist[hair & nb4(dist == k - 1) & (dist == 99)] = k
    L[hair] = 0x1
    L[hair & (dist <= 1) & (ang >= 25) & (ang <= 125)] = 0xD
    L[hair & (dist <= 2) & (ang >= 160) & (ang <= 300)] = 0x4
    # spike undersides dark (one px below the spine)
    for (p0, p1, tp) in SPIKES[:-1]:
        mx, my = (p0[0] + p1[0]) / 2 + dx, (p0[1] + p1[1]) / 2 + dy
        for x, y in line(mx, my, tp[0] + dx, tp[1] + dy):
            if 0 <= y + 1 < 64 and 0 <= x < 64 and hair[y + 1, x] and not edge[y + 1, x]:
                L[y + 1, x] = 0x4
    # strand lines toward the spike bases (outer half only)
    sx, sy = STRAND_FROM[0] + dx, STRAND_FROM[1] + dy
    for (p0, p1, tp) in SPIKES[:-1]:
        for (bx, by) in (p0, p1):
            for x, y in line(sx, sy, bx + dx, by + dy, start=0.55):
                if 0 <= x < 64 and 0 <= y < 64 and hair[y, x] and not edge[y, x]:
                    L[y, x] = 0x4
    # mask (side-on)
    inmask = np.zeros((64, 64), bool)
    for ry_, (x0, x1) in MASK.items():
        for rx_ in range(x0, x1 + 1):
            x, y = rx_ + dx, ry_ + dy
            if 0 <= x < 64 and 0 <= y < 64:
                inmask[y, x] = True
                L[y, x] = 0x7 if (rx_ - x0 < 2 or (ry_ >= 31 and rx_ - x0 < 3)) else 0x9
    L[fringe & inmask] = 0x1                                  # the fringe lies over the mask
    for (rx_, ry_) in HILITE:
        L[ry_ + dy, rx_ + dx] = 0xE
    for ry_, (x0, x1) in MASK.items():                        # seam: hair-dark behind the mask
        y, x = ry_ + dy, x0 - 1 + dx
        if L[y, x] in HAIR: L[y, x] = 0x4
    for (rx_, ry_) in EAR:
        if not inmask[ry_ + dy, rx_ + dx]: L[ry_ + dy, rx_ + dx] = 0xF
    earm = L == 0xF
    L[nb4(earm) & ~earm & (L != 0) & ~inmask] = OUT
    for (rx_, ry_) in GLYPH:
        L[ry_ + dy, rx_ + dx] = OUT
    return L, inmask


def frame(f):
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
    # --- Osrid's head
    L, inmask = head_layer(dx, dy)
    head = L > 0
    a[head & ~hand] = L[head & ~hand]
    ring = nb4(head) & ~head & ~hand
    a[ring & ((a == 0) | np.isin(a, list(COAT)))] = OUT
    # --- scarf wrap over the nape, neck and collar (never over the mask, ear or gloves)
    rows = {}
    for ry_, (x0, x1) in SCARF.items():
        for rx_ in range(x0, x1 + 1):
            rows.setdefault(rx_, []).append(ry_)
    for ry_, (x0, x1) in SCARF.items():
        for rx_ in range(x0, x1 + 1):
            x, y = rx_ + dx, ry_ + dy
            if not (0 <= x < 64 and 0 <= y < 64) or hand[y, x] or inmask[y, x] or a[y, x] == 0xF:
                continue
            top = ry_ == min(rows[rx_]); bot = ry_ >= max(rows[rx_]) - 1
            fold = (rx_ - ry_) % 9 == 0
            a[y, x] = 0xC if top else 0xB if (bot or fold) else 0xA
    # --- outline round hair and scarf; fill enclosed holes; drop floating outline
    for y in range(64):
        for x in range(64):
            if a[y, x] == 0:
                nb = [a[y + q, x + p] for q, p in ((1, 0), (-1, 0), (0, 1), (0, -1))
                      if 0 <= y + q < 64 and 0 <= x + p < 64]
                if any(v in HAIR or v in SCARFC or v in (0x9, 0x7, 0xE) for v in nb):
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
    return np.concatenate([frame(frames[j]) for j in range(4)], 0)


def save(a, path):
    img = Image.fromarray(a.astype(np.uint8), 'P')
    flat = []
    for i in range(16):
        flat += list(PAL[i])
    img.putpalette(flat + [0] * (768 - 48))
    img.save(path, transparency=0)


if __name__ == '__main__':
    save(build(pickle.load(open(sys.argv[1], 'rb'))), sys.argv[2])
