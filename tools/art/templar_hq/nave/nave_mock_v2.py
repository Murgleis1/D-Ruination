"""The Templar cathedral's nave, mock v2 (user 2026-11-23: study other games' churches; re-use Pokemon Empire's
Arceus church interior, with new colours and what was planned). Source: the user's screenshot of Empire's Arceus
church (Starlight City), a 2x upscale, halved to GBA scale: 25x40 (the room x 3-21, rows 1-35). Credit Pokemon
Empire, as for the church outside.
Kept: its plan (the raised chancel behind a balustrade, a stair either side of the low window, the nave of pews down
the blue carpet), its stained glass, its gold candlesticks, the Order's blue banners and carpet, the piano and the
communion table, the altar and the lectern.
Recoloured: the brick floor and the wooden wall tops to the church's own cream stone (so inside matches outside).
Added (user's plan): six doors in the south-facing wall faces where banners hung (GBA doors face south): on the
chancel, west the sealed stair to the Sanctum (a gold grille) and east Ambrose's study; at the head of the nave the
bishops' chambers (west) and the Braviary registry (east), then the kitchen (west) and the storehouse (east). The
stool and two candlesticks that stood before those doors moved aside. Ambrose at the altar, facing down the aisle.
Usage: python3 nave_mock_v2.py [out.png]"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
SRC = os.path.join(REPO, 'assets/templar_hq_reference/empire/empire_church_interior_native.png')

def main(out):
    a = np.array(Image.open(SRC).convert('RGB')).astype(int)
    H, W = a.shape[0] // 16, a.shape[1] // 16
    # floor: brick and mortar (and their wall-shadowed tones) -> cream stone; wall-top wood -> stone
    TABLE = {(175, 123, 84): (208, 200, 180), (132, 91, 62): (166, 156, 130),
             (140, 105, 66): (182, 172, 146), (148, 113, 74): (192, 182, 156), (156, 113, 74): (196, 186, 160),
             (156, 121, 74): (200, 190, 164), (90, 48, 24): (112, 104, 86), (82, 40, 8): (88, 80, 70)}
    # the floor under the walls' shadow: any warm tone darker than the brick in the floor's hue family
    out_a = a.copy()
    for src, dst in TABLE.items():
        m = (a == src).all(-1); out_a[m] = dst
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    shade = (r > g) & (g > b) & (r - b > 50) & (r - b < 110) & (r < 175) & ~np.isin(a.reshape(-1, 3).view([('', int)] * 3).ravel(),
            np.array(list(TABLE.keys())).view([('', int)] * 3).ravel()).reshape(r.shape)
    # (only where a floor cell is: rows 8-12 and 18-35, x 4-20, away from the furniture's own browns)
    floorzone = np.zeros_like(shade); floorzone[8 * 16:13 * 16, 4 * 16:21 * 16] = True; floorzone[18 * 16:36 * 16, 3 * 16:22 * 16] = True
    sm = shade & floorzone & (np.abs((r - b) - 91) < 18)
    k = (.30 * r + .59 * g + .11 * b)[sm] / (.30 * 175 + .59 * 123 + .11 * 84)
    out_a[sm] = np.clip(np.outer(k, (208, 200, 180)), 0, 255).astype(int)
    im = Image.fromarray(out_a.astype(np.uint8)).convert('RGBA'); d = ImageDraw.Draw(im)
    cell = lambda x, y: (x * 16, y * 16, x * 16 + 15, y * 16 + 15)
    floor_px = Image.fromarray(out_a[10 * 16:11 * 16, 9 * 16:10 * 16].astype(np.uint8))      # (a plain floor cell)
    def floor(x, y): im.paste(floor_px, (x * 16, y * 16))
    for (x, y) in ((4, 9), (20, 9), (3, 22), (3, 23), (21, 22), (21, 23)): floor(x, y)         # (the stools, the candlesticks moved)
    for (x, y) in ((5, 9), (19, 9)): floor(x, y)
    # the doors, in the south-facing faces (their lower two rows)
    DK, W1, W2, GD, GL = (28, 22, 20, 255), (96, 64, 40, 255), (82, 54, 34, 255), (192, 142, 44, 255), (244, 214, 116, 255)
    def door(x, y, sealed=False):
        px, py = x * 16, y * 16
        d.rectangle((px + 1, py + 4, px + 14, py + 31), fill=(150, 140, 116, 255))           # (its stone frame)
        d.pieslice((px + 1, py - 2, px + 14, py + 12), 180, 360, fill=(150, 140, 116, 255))
        d.rectangle((px + 3, py + 6, px + 12, py + 31), fill=DK); d.pieslice((px + 3, py + 1, px + 12, py + 12), 180, 360, fill=DK)
        if sealed:                                                                         # (a dark stairwell behind a gold grille)
            for k in range(4, 13, 3): d.line((px + k, py + 4, px + k, py + 31), fill=GD)
            for yy in (py + 12, py + 22): d.line((px + 3, yy, px + 12, yy), fill=GD)
            d.point((px + 7, py + 3), fill=GL); d.point((px + 8, py + 3), fill=GL)
        else:
            d.rectangle((px + 4, py + 7, px + 11, py + 31), fill=W1); d.line((px + 7, py + 6, px + 7, py + 31), fill=DK)
            d.rectangle((px + 8, py + 7, px + 11, py + 31), fill=W2)
            for yy in (py + 14, py + 24): d.line((px + 4, yy, px + 11, yy), fill=(64, 44, 30, 255))
            d.point((px + 6, py + 19), fill=GL); d.point((px + 9, py + 19), fill=GL)
        d.arc((px + 1, py - 2, px + 14, py + 12), 180, 360, fill=GD)
    door(4, 7, sealed=True); door(20, 7)                                                    # (Sanctum stair; Ambrose's study)
    door(4, 19); door(20, 19)                                                               # (bishops' chambers; Braviary registry)
    door(3, 20); door(21, 20)                                                               # (kitchen; storehouse)
    # Ambrose at the altar, facing down the aisle
    am = Image.open(os.path.join(REPO, 'codebase/graphics/object_events/pics/people/ambrose.png'))
    aa = np.array(am.convert('RGBA')); idx = np.array(am); aa[idx == 0, 3] = 0
    fw = 32 if aa.shape[1] % 32 == 0 and aa.shape[1] >= 96 else 16
    spr = Image.fromarray(aa[:, :fw]); im.alpha_composite(spr, (12 * 16 + 8 - fw // 2, 10 * 16 + 16 - spr.size[1]))
    im = im.crop((2 * 16, 0, 23 * 16, 36 * 16))
    im.convert('RGB').save(out); im.convert('RGB').resize((im.size[0] * 2, im.size[1] * 2), Image.NEAREST).save(out.replace('.png', '_2x.png'))
    print('nave mock v2', im.size, 'ambrose frame', fw, aa.shape)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/nave_mock_v2.png')
