"""Osrid trainer BACK pic, candidate (2026-11-17).

Base: MonoMyth back pic #4 (a 3/4 rear bust facing right with a full 4-frame throw), used for
anatomy and animation only. The MonoMyth spec (tools/art/MONOMYTH_TRAINER_STYLE.md) says a back pic
is a right-facing rear bust, and #4 is the closest structure to Osrid (coat, scarf, shaggy hair).
Repainted to Osrid, consistent with the front candidate:
  * hair: his red-orange, plus swept-back spikes added to the silhouette (#4 has a shaggy bob)
  * face: his cream mask in profile (#4's skin and red face paint)
  * hands: tan leather gloves (skin regions that do not touch the hair)
  * coat: his dark armour brown-grey; the light lapel band: his brown leather strap
  * scarf: his green

Usage: python3 -I osrid_trainer_back.py BACKS_PKL OUT.png   (64x256, 4 frames)
"""
import sys, pickle
import numpy as np
from PIL import Image
from collections import deque

# #4 index -> role: 5 outline; 1/4/D hair; 9/E/7/C/F skin (C = red face paint); 2/3/6 coat;
# 8 lapel (also hand light); A/B scarf.
PAL = {
    0x0: (255, 0, 255),
    0x5: (8, 8, 10),
    0x4: (90, 34, 18),      # hair dark
    0x1: (156, 62, 26),     # hair mid
    0xD: (210, 104, 50),    # hair light
    0x9: (230, 214, 172),   # mask
    0xE: (248, 240, 212),   # mask highlight
    0xF: (248, 240, 212),   # (eye glints in #4) -> mask highlight
    0x7: (184, 158, 118),   # mask shadow
    0xC: (152, 128, 96),    # mask deep shadow (was face paint)
    0x6: (44, 40, 42),      # coat dark
    0x2: (82, 74, 66),      # coat mid
    0x3: (112, 100, 86),    # coat light
    0x8: (126, 84, 52),     # leather strap
    0xA: (62, 94, 62),      # scarf
    0xB: (40, 64, 44),      # scarf dark
}
HAIR = {0x1, 0x4, 0xD}
SKIN = {0x9, 0xE, 0x7, 0xC, 0xF}
OUT = 0x5
# glove: two tones from the existing slots (mask shadow as the glove light, strap as the leather)
GLOVE = {0x9: 0x7, 0xE: 0x7, 0xF: 0x7, 0x7: 0x8, 0xC: 0x8, 0x8: 0x7}

# Spikes: the hair's outline in polar form round the head centre, modulated by a sawtooth on the
# back and top (angles in degrees, 0 = right/face, 90 = up, 180 = back): valleys are carved,
# tips pushed out, so the spikes grow from the hair mass instead of being stuck on.
SPIKE_FROM, SPIKE_TO, SPIKE_PERIOD = 60, 250, 30     # degrees
TIP, VALLEY = 3.0, -2.5                               # px added at a tip / removed in a valley
SPIKE_PHASE = 8


def saw(theta):
    t = ((theta - SPIKE_FROM + SPIKE_PHASE) % SPIKE_PERIOD) / SPIKE_PERIOD   # 0..1
    tri = 1 - abs(2 * t - 1)                                                   # 0 valley, 1 tip
    return VALLEY + (TIP - VALLEY) * tri ** 1.6


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


def tri_fill(a, p0, p1, p2, val):
    (x0, y0), (x1, y1), (x2, y2) = p0, p1, p2
    ys = range(max(0, min(y0, y1, y2)), min(63, max(y0, y1, y2)) + 1)
    for y in ys:
        for x in range(64):
            d1 = (x - x1) * (y0 - y1) - (x0 - x1) * (y - y1)
            d2 = (x - x2) * (y1 - y2) - (x1 - x2) * (y - y2)
            d3 = (x - x0) * (y2 - y0) - (x2 - x0) * (y - y0)
            neg = d1 < 0 or d2 < 0 or d3 < 0; pos = d1 > 0 or d2 > 0 or d3 > 0
            if not (neg and pos) and a[y, x] in (0, OUT):
                a[y, x] = val


def frame(f):
    a = f.copy()
    hair = np.isin(a, list(HAIR))
    skin = np.isin(a, list(SKIN))
    # hands = skin components that do not touch the hair (8-neighbourhood)
    lab, n = components(skin)
    near_hair = np.zeros_like(hair)
    ys, xs = np.nonzero(hair)
    for y, x in zip(ys, xs):
        near_hair[max(0, y - 2):y + 3, max(0, x - 2):x + 3] = True
    hand = np.zeros_like(skin)
    for k in range(1, n + 1):
        comp = lab == k
        if not np.any(comp & near_hair):
            hand |= comp
    # grow the hand into adjacent lapel-light pixels (#4 lights hands with index 8)
    grown = hand.copy()
    for _ in range(3):
        g2 = grown.copy()
        for y, x in zip(*np.nonzero(grown)):
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < 64 and 0 <= nx < 64 and a[ny, nx] == 0x8 and not g2[ny, nx]:
                        g2[ny, nx] = True
        grown = g2
    src = a.copy()
    for k, v in GLOVE.items():
        a[grown & (src == k)] = v
    # --- spikes by polar modulation of the hair outline
    head = hair | (skin & near_hair & ~grown)
    hy, hx = np.nonzero(head)
    cy, cx = hy.mean() + 2, hx.mean()
    yy, xx = np.mgrid[0:64, 0:64]
    ang = (np.degrees(np.arctan2(cy - yy, xx - cx)) + 360) % 360
    rad = np.hypot(xx - cx, yy - cy)
    rmax = np.zeros(360)
    for y, x in zip(*np.nonzero(hair)):
        k = int(ang[y, x]); rmax[k] = max(rmax[k], rad[y, x])
    for k in range(360):            # fill empty bins from neighbours
        if rmax[k] == 0:
            rmax[k] = max(rmax[(k - 1) % 360], rmax[(k + 1) % 360])
    inside = np.zeros((64, 64), bool); band = np.zeros((64, 64), bool)
    for y in range(64):
        for x in range(64):
            th = ang[y, x]
            if SPIKE_FROM <= th <= SPIKE_TO:
                band[y, x] = True
                inside[y, x] = rad[y, x] <= rmax[int(th)] + saw(th)
    # carve: band hair pixels outside the new outline (and their old outline) -> background
    carve = band & ~inside & (hair | (a == OUT)) & (rad > rmax[ang.astype(int)] - 4)
    a[carve] = 0
    # extend: band pixels inside the new outline that are background -> hair
    ext = band & inside & (a == 0)
    for y, x in zip(*np.nonzero(ext)):
        th = ang[y, x]
        a[y, x] = 0xD if (60 <= th <= 150 and rad[y, x] > rmax[int(th)]) else 0x1
    # spike shading: light on upper faces, dark on lower faces
    hair2 = np.isin(a, list(HAIR))
    for y, x in zip(*np.nonzero(hair2 & band & (rad > rmax[ang.astype(int)] - 3))):
        up = y > 0 and a[y - 1, x] in (0, OUT)
        dn = y < 63 and a[y + 1, x] in (0, OUT)
        if up and not dn:
            a[y, x] = 0xD
        elif dn and not up:
            a[y, x] = 0x4
    # --- mask profile: smooth the face's right edge (no nose notch: a mask, not a face)
    face = np.isin(a, list(SKIN)) & near_hair & ~grown
    fy = np.nonzero(face)[0]
    if len(fy):
        right = {}
        for y in range(fy.min(), fy.max() + 1):
            xs_ = np.nonzero(face[y])[0]
            if len(xs_): right[y] = xs_.max()
        rows = sorted(right)
        for i, y in enumerate(rows):
            win = [right[r] for r in rows[max(0, i - 2):i + 3]]
            target = int(round(max(win)))
            for x in range(right[y] + 1, target + 1):
                a[y, x] = 0x9
            if target + 1 < 64 and a[y, target + 1] != OUT:
                a[y, target + 1] = OUT
        # eye glyph: where #4's eye glint was (index F inside the face) + the drip below it
        ey = np.nonzero((f == 0xF) & face)
        if len(ey[0]):
            y0, x0 = int(ey[0].min()), int(ey[1].min())
            for dy, dx in ((0, 0), (0, 1), (-1, 0), (1, 1), (2, 1), (3, 1), (4, 1)):
                yy0, xx0 = y0 + dy, x0 + dx
                if 0 <= yy0 < 64 and 0 <= xx0 < 64 and a[yy0, xx0] in SKIN:
                    a[yy0, xx0] = OUT
    # --- fresh outline round the hair and the mask
    for y in range(64):
        for x in range(64):
            if a[y, x] == 0:
                nb = [a[y + dy, x + dx] for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1))
                      if 0 <= y + dy < 64 and 0 <= x + dx < 64]
                if any(v in HAIR for v in nb):
                    a[y, x] = OUT
    # enclosed transparent pixels left by the carve -> the surrounding colour
    for y in range(1, 63):
        for x in range(1, 63):
            if a[y, x] == 0:
                nb = [a[y + dy, x + dx] for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1))]
                if all(v != 0 for v in nb):
                    body = [v for v in nb if v != OUT]
                    a[y, x] = max(set(body), key=body.count) if body else OUT
    # drop stray outline pixels left floating by the carve
    for y in range(64):
        for x in range(64):
            if a[y, x] == OUT:
                nb = a[max(0, y - 1):y + 2, max(0, x - 1):x + 2]
                if not np.any((nb != 0) & (nb != OUT)):
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
