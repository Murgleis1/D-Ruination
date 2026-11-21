"""The Mirroh Necropolis catacombs, floor 1 (Dale Langerin), mock v1 (2026-11-21).

Ghost Grey's Lavender Town catacombs are the primary reference (user): this floor is its great chamber (map
1.93, 41x32) taken as it stands: the brick back wall with the demon-faced arch (the way down), the rubble floor
of grave markers on the upper ledge, the chasm across the middle with its islands, the lower ledge with the
landing (the stairs up to the grounds), stone demon heads standing about. Ghost Grey crosses its chasm by an
invisible path; here it is crossed by Crown's plank bridges (its underground halls, map 6.8), two of them,
straight up through the middle island, where Dale stands between the island's demon heads: the only way on.
Colours (Ghost Grey is greyscale): the rubble a cold grey-violet, the graves bone, the bricks the fortress's
copper-shaded stone in shadow, the demon heads and the arch bronze (House Langerin's copper), the landing slate,
the chasm a blue-black.
Credits: Ghost Grey (JoeyZeed), Crown (its team). Usage: python3 tools/art/necropolis/floor1_mock.py [outdir]
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = '/home/claude/scratch/necro/f1'
GG = np.load(os.path.join(SRC, 'gg_1_93.npz')); CR = np.load(os.path.join(SRC, 'cr_6_8.npz'))

RUBBLE = {0x3eb, 0x3dc, 0x3c8, 0x3c9, 0x3d0, 0x3d1, 0x3db, 0x3df, 0x3e7}
GRAVE = {0x3d7, 0x3d4, 0x3d3}
DEMON = {0x3f3, 0x3f4, 0x3fb, 0x3fc, 0x3ed, 0x3ee, 0x3ef, 0x3f5, 0x3f6, 0x3f7}
BRICK = {0x3f0, 0x3f1, 0x3f2, 0x3f8, 0x3f9, 0x3fa}
MAT = {0x3d8, 0x3d9, 0x3da, 0x3e0, 0x3e1, 0x3e2, 0x3e8, 0x3e9, 0x3ea}
VOID = (12, 11, 22)

def ramp(cols):
    cols = np.array(cols, float)
    def f(img):
        l = img.astype(float).mean(-1) / 255.0
        q = np.clip(l, 0, 0.999) * (len(cols) - 1); i = np.floor(q).astype(int)
        return (cols[i] + (cols[np.minimum(i + 1, len(cols) - 1)] - cols[i]) * (q - i)[..., None]).astype(np.uint8)
    return f
STONE = ramp([VOID, (54, 50, 68), (104, 98, 120), (156, 150, 168), (198, 194, 206)])
BONE = ramp([VOID, (70, 64, 66), (150, 142, 132), (206, 198, 182), (232, 226, 210)])
BRONZE = ramp([VOID, (52, 30, 24), (120, 70, 42), (184, 116, 66), (228, 172, 112)])
BRICKS = ramp([VOID, (44, 36, 40), (86, 70, 68), (128, 108, 100), (168, 150, 140)])
SLATE = ramp([VOID, (40, 44, 58), (78, 86, 106), (118, 128, 148), (160, 168, 184)])

def tone(m, img):
    if m in (0x281, 0x3fe): return np.full((16, 16, 3), VOID, np.uint8)
    if m in GRAVE:                                     # the marker bone, the rubble round it stone
        b, s = BONE(img), STONE(img)
        out = s.copy(); out[4:15, 2:14] = b[4:15, 2:14]
        return out
    for group, fn in ((DEMON, BRONZE), (BRICK, BRICKS), (MAT, SLATE)):
        if m in group:
            out = fn(img); dark = img.astype(int).sum(-1) < 40
            out[dark] = VOID if group is not DEMON else (30, 16, 14)
            return out
    return STONE(img)

def compose():
    c = GG['cells'].copy(); H, W = c.shape
    c[c == 0x3fe] = 0x281                              # (Ghost Grey's invisible path: here the bridges)
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W):
            img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = tone(int(c[y, x]), GG['full'][c[y, x]])
    # Crown's plank bridges: down the middle, ledge to island to ledge
    def wood(t):
        f = t.astype(float); return np.clip(f * np.array([0.92, 0.84, 0.8]) * 0.9, 0, 255).astype(np.uint8)
    for (y0, y1) in ((13, 17), (22, 26)):
        for y in range(y0, y1 + 1):
            for dx, m in enumerate((0x30a, 0x30b, 0x30c)):
                t = wood(CR['full'][m]); dark = CR['full'][m].astype(int).sum(-1) < 60
                t[dark] = VOID
                img[y * 16:y * 16 + 16, (20 + dx) * 16:(21 + dx) * 16] = t
    return img, c

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    img, c = compose()
    Image.fromarray(img).save(os.path.join(outdir, 'necropolis_f1.png'))
    big = Image.fromarray(img).resize((img.shape[1] * 2, img.shape[0] * 2), 0)
    d = ImageDraw.Draw(big)
    for (x, y), t in (((21, 19), 'Dale'), ((21, 30), 'stairs up (grounds)'), ((21, 3), 'way down (floor 2)')):
        cx, cy = x * 32 + 16, y * 32 + 16
        d.ellipse([cx - 13, cy - 13, cx + 13, cy + 13], outline=(255, 220, 90), width=3)
        d.text((cx + 16, cy - 6), t, fill=(255, 220, 90))
    big.save(os.path.join(outdir, 'necropolis_f1_2x.png'))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/necro')
