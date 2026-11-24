"""The ancient sky over the slip's mesa (user 2026-11-24): MonoMyth's bastion-top backdrop (the user's export, flipped
by them; the Peak's sky ages later) reworked: "more clouds, a deep sunset, and even larger mountains that are very
ominous against the blood red ancient sky".
  * its 14 colours turned colour by colour: the sky blood red, deep maroon at the top to a burning orange-red at the
    horizon; its clouds dark crimson with fire-lit edges; the sun sinking, a pale ember in an orange halo; the near
    range near-black crimson, its lit ridges dark red; the far range a smoky maroon;
  * more clouds: long streaks of dark cloud across the upper sky, their undersides lit by the sun;
  * larger mountains: a great range rising behind the old one, its peaks reaching high into the sky (the tallest on
    the right, as the user's flip puts the mountain), dark, lit on their sun-facing slopes, the sun half sunk behind
    them.
Stays within one palette (15 colours). Usage: python3 backdrop_ancient.py [OUT.png]"""
import os, sys, random
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
SRC = os.path.join(REPO, 'assets', 'mt_mirroh_reference', 'backdrop_bastion_flipped_src.png')
BH, BW = 136, 256
SKY_TOP, SKY_UP, SKY_HI, SKY, SKY_LOW = (52, 6, 14), (84, 12, 20), (122, 20, 24), (164, 30, 28), (204, 56, 34)
CLOUD_LIT, CLOUD_HI, HALO, SUN = (232, 92, 44), (248, 136, 66), (255, 188, 108), (255, 234, 188)
NEAR, NEAR_DARK, RIDGE, FAR, FAR_EDGE = (30, 8, 14), (20, 4, 10), (72, 18, 24), (56, 14, 22), (88, 22, 28)
RECOLOUR = {
    (148, 140, 99): SKY_TOP, (173, 140, 99): SKY_UP, (198, 148, 90): SKY_HI, (222, 148, 90): SKY,
    (247, 156, 90): SKY_LOW, (255, 173, 90): CLOUD_LIT, (255, 189, 90): CLOUD_HI, (255, 222, 123): HALO,
    (255, 255, 206): SUN, (132, 107, 74): NEAR, (132, 99, 66): NEAR_DARK, (148, 115, 74): RIDGE,
    (206, 123, 82): FAR_EDGE, (173, 115, 82): FAR}
SKYCOLS = {SKY_TOP, SKY_UP, SKY_HI, SKY, SKY_LOW, CLOUD_LIT, CLOUD_HI, HALO, SUN}

def ridge(rng, n, peaks):
    """a mountain skyline: heights (rows from the top) across n columns, from a few great peaks and jagged noise"""
    h = np.full(n, 140.0)
    for (px, py, w) in peaks:
        x = np.arange(n); h = np.minimum(h, py + np.abs(x - px) * (BH - py) / w)
    # jag it: midpoint-displaced noise, steeper where high
    noise = np.zeros(n); step = 32; amp = 7.0
    pts = {0: 0.0, n - 1: 0.0}
    while step >= 1:
        for s in range(0, n - 1, step * 2 if step > 1 else 1):
            m = min(s + step, n - 1); a, b = pts.get(s, 0.0), pts.get(min(s + 2 * step, n - 1), 0.0)
            pts[m] = (a + b) / 2 + rng.uniform(-amp, amp)
        step //= 2; amp *= 0.6
    for x in range(n): noise[x] = pts.get(x, 0.0)
    return h + noise

def backdrop():
    a = np.array(Image.open(SRC).convert('RGB'))[:BH]
    out = a.copy()
    for k, v in RECOLOUR.items(): out[(a == k).all(-1)] = v
    sky = np.zeros((BH, BW), bool)
    for c in SKYCOLS - {SUN, HALO}: sky |= (out == c).all(-1)
    rng = random.Random(7)
    yy, xx = np.mgrid[0:BH, 0:BW]
    # more clouds: long dark streaks across the upper sky, lit from below
    for (cx, cy, rx, ry) in ((40, 14, 46, 3.2), (150, 9, 60, 2.6), (220, 22, 40, 3.0), (96, 28, 34, 2.4), (20, 36, 30, 2.2),
                             (190, 40, 36, 2.6), (128, 18, 26, 2.0)):
        wob = np.sin(xx / 7.0 + cx) * 1.2 + np.sin(xx / 3.1 + cy) * 0.6
        m = (((xx - cx) / rx) ** 2 + ((yy - cy - wob) / ry) ** 2 <= 1) & sky
        out[m] = SKY_UP
        lit = m & ~np.roll(m, -1, 0); out[lit] = CLOUD_LIT                        # (its sunlit underside)
        rim = m & ~np.roll(m, 1, 0); out[rim] = SKY_HI                            # (its dark crown)
    # the great range behind: its peaks reaching high, the tallest on the right; dark, lit on the sun's side (the
    # slope edges toward the sun, and a ridge line running down from each peak toward it)
    sm = (a == (255, 255, 206)).all(-1)
    sunx = float(np.mean(np.where(sm)[1])) if sm.any() else 110.0
    PEAKS = [(206, 4, 64), (150, 30, 46), (92, 38, 50), (30, 32, 40), (244, 20, 28), (176, 22, 30)]
    h = ridge(rng, BW, PEAKS)
    for k in range(3):                                                           # (extra fine jags)
        h += np.array([rng.uniform(-1.2, 1.2) for _ in range(BW)])
    top = np.clip(h, 0, BH).astype(int)
    behind = (yy >= top[None, :]) & (sky | (out == SUN).all(-1) | (out == HALO).all(-1))
    out[behind] = FAR
    for x in range(1, BW - 1):
        toward = -1 if x > sunx else 1                                           # (the neighbour on the sun's side)
        if top[x + toward] > top[x]:                                             # (a slope facing the sun)
            for y in range(top[x], min(BH, top[x] + 2 + (top[x + toward] - top[x]) // 2)):
                if behind[y, x]: out[y, x] = FAR_EDGE
        elif 0 <= top[x] < BH and behind[top[x], x]: out[top[x], x] = FAR_EDGE
    for (px, py, w) in PEAKS:                                                    # (ridge lines down from the peaks)
        x = px; y = int(top[px]) + 1; d = -1 if px > sunx else 1
        while y < BH - 1 and 0 < x < BW - 1:
            if behind[y, x]: out[y, x] = FAR_EDGE
            if behind[y, x - d]: out[y, x - d] = NEAR
            y += 1
            if rng.random() < 0.55: x += d
    cols = {tuple(int(v) for v in c) for c in out.reshape(-1, 3)}
    assert len(cols) <= 15, len(cols)
    return out

if __name__ == '__main__':
    b = backdrop()
    Image.fromarray(b).resize((BW * 3, BH * 3), Image.NEAREST).save(sys.argv[1] if len(sys.argv) > 1 else '/tmp/anc_sky.png')
