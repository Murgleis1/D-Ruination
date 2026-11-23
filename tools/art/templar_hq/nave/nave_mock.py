"""The Templar cathedral's first floor, the nave: mock v1 (user 2026-11-22: floor plan v1 approved; the offices are
Ambrose's study, the Braviary registry, the bishops' chambers and the kitchen and storehouse).
Crown's round hall (map 1.94; credit Blah and the Crown team, with permission): its stepped round walls, its floor,
its two gilded pillars at the head. Its seats taken out (the floor laid back in the same phase) and Crown's church
pews (map 6.2) set in rows either side of the aisle; Crown's church altar at the head between the pillars; a blue
carpet with a gold edge up the aisle. Recoloured to the church's own: the purple wall panels to the Order's blue, the
white wall tops and the green floor to the church's cream.
The offices open off the round's stepped wall faces as radiating chapels open off an apse: four double doors, two
each side (x 7-8 and 5-6 west, 14-15 and 16-17 east), each office its own room behind. The stair up to the Sanctum is
cut into the apse wall behind the altar (the Sanctum's own stair, its steps turned to climb), sealed by a gold grille.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 nave_mock.py [out.png]"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'mirroh'))
os.environ.setdefault('ODYSSEY_ROM', '/home/claude/crown/Crown.gba')
import interiors as I

AXIS_PX = 11 * 16 + 8                                   # (the aisle's middle: x 9-13)
SEATS = None

def lum(a): return .30 * a[..., 0] + .59 * a[..., 1] + .11 * a[..., 2]

def main(out):
    img, solid = I._crown(1, 94); img = img.astype(int)
    H, W = solid.shape
    cell = lambda im, x, y: im[y * 16:y * 16 + 16, x * 16:x * 16 + 16]
    src = img.copy()
    # 1. the seats out: every cell holding a seat (its gold or violet cushion) takes the aisle's floor of the same column
    # parity and row
    def is_seat(x, y):
        c = cell(src, x, y); r, g, b = c[..., 0], c[..., 1], c[..., 2]
        gold = (r > 180) & (g > 140) & (b < 120); vio = (b > 170) & (r > 140) & (g < r)
        return (gold | vio).sum() > 20
    for y in range(H):
        for x in range(W):
            if x in (9, 13) and y < 5: continue                       # (the gilded pillars)
            if is_seat(x, y): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cell(src, 10 + x % 2, 10 + y % 2)   # (the aisle's floor, same phase)
    for (x, y) in [(9, 15), (10, 15), (9, 16), (10, 16), (9, 17), (10, 17), (11, 15)]:   # (its stair down: floor)
        img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = cell(src, 10 + x % 2, 10 + y % 2)
    # 2. recolour: purple panels -> the Order's blue; white tops and the green floor -> the church's cream
    r, g, b = img[..., 0], img[..., 1], img[..., 2]; L = lum(img)
    purple = (b > g + 15) & (r > g - 5) & ~((r > 180) & (g > 140) & (b < 120))
    green = (g > r + 6) & (g >= b - 4)
    white = (np.abs(r - b) < 20) & (np.abs(r - g) < 20) & (L > 150)
    BLUE = np.array([(22, 24, 50), (34, 40, 89), (51, 60, 128), (62, 74, 163), (96, 112, 190), (150, 166, 220)])
    CREAM = np.array([(120, 108, 86), (146, 134, 108), (170, 158, 130), (190, 180, 154), (208, 200, 180), (226, 221, 211)])
    q = lambda m, ramp, lo, hi: ramp[np.clip(((L[m] - lo) / (hi - lo) * (len(ramp) - 1)).round().astype(int), 0, len(ramp) - 1)]
    out_img = img.copy()
    out_img[purple] = q(purple, BLUE, 30, 200); out_img[green] = q(green, CREAM, 50, 170); out_img[white] = q(white, CREAM, 120, 255)
    img = out_img
    im = Image.fromarray(img.astype(np.uint8)).convert('RGBA'); d = ImageDraw.Draw(im)
    # 3. the carpet up the aisle (x 10-12, rows 5-17): the Order's blue, a gold edge
    d.rectangle((10 * 16 + 2, 5 * 16, 13 * 16 - 3, 18 * 16 - 1), fill=(51, 60, 128, 255))
    d.line((10 * 16 + 2, 5 * 16, 10 * 16 + 2, 18 * 16 - 1), fill=(192, 142, 44, 255)); d.line((13 * 16 - 3, 5 * 16, 13 * 16 - 3, 18 * 16 - 1), fill=(192, 142, 44, 255))
    d.line((10 * 16 + 4, 5 * 16, 10 * 16 + 4, 18 * 16 - 1), fill=(62, 74, 163, 255)); d.line((13 * 16 - 5, 5 * 16, 13 * 16 - 5, 18 * 16 - 1), fill=(34, 40, 89, 255))
    # 4. Crown's church pieces (6.2): pews (x 2-4, rows 10-11), the altar (x 6-9, rows 6-7)
    ch, _ = I._crown(6, 2)
    def piece(x0, y0, w, h, bgref):
        p = ch[y0 * 16:(y0 + h) * 16, x0 * 16:(x0 + w) * 16].astype(int)
        bg = ch[bgref[1] * 16:bgref[1] * 16 + 16, bgref[0] * 16:bgref[0] * 16 + 16].astype(int)
        m = np.zeros(p.shape[:2], bool)
        for yy in range(h):
            for xx in range(w):
                c = p[yy * 16:yy * 16 + 16, xx * 16:xx * 16 + 16]; m[yy * 16:yy * 16 + 16, xx * 16:xx * 16 + 16] = np.abs(c - bg).sum(-1) > 30
        a = np.dstack([p, m * 255]).astype(np.uint8); return Image.fromarray(a)
    pew = piece(2, 10, 3, 2, (1, 12))
    altar = piece(6, 6, 4, 2, (5, 5))
    # (pews follow the round: the inner rank down the aisle, the outer only where the round is widest, clear of its walls)
    for (x, y) in [(5, 7), (5, 10), (5, 13), (2, 9), (2, 12)] if False else [(5, 7), (5, 10), (5, 13), (2, 10)]:
        im.alpha_composite(pew, (x * 16, y * 16))
        im.alpha_composite(pew.transpose(Image.FLIP_LEFT_RIGHT), ((22 - x - 3 + 1) * 16, y * 16))
    im.alpha_composite(altar, (AXIS_PX - altar.size[0] // 2, 3 * 16 + 4))
    # 5. the Sanctum's stair, cut into the apse wall behind the altar (x 10-12, rows 0-1), sealed by a gold grille
    sm = Image.open(os.path.join(HERE, '..', 'sanctum', 'sanctum_mock.png')).convert('RGBA') if os.path.exists(os.path.join(HERE, '..', 'sanctum', 'sanctum_mock.png')) else None
    if sm is None:
        import subprocess; subprocess.run([sys.executable, '-I', 'sanctum_mock.py', 'sanctum_mock.png'], cwd=os.path.join(HERE, '..', 'sanctum'))
        sm = Image.open(os.path.join(HERE, '..', 'sanctum', 'sanctum_mock.png')).convert('RGBA')
    stair = sm.crop((7 * 16, 12 * 16, 10 * 16, 14 * 16))
    im.alpha_composite(stair, (10 * 16, 0))
    for k in range(10 * 16 + 2, 13 * 16 - 1, 5): d.line((k, 2, k, 2 * 16 - 1), fill=(192, 142, 44, 255))
    d.line((10 * 16, 2, 13 * 16 - 1, 2), fill=(244, 214, 116, 255)); d.line((10 * 16, 2 * 16 - 2, 13 * 16 - 1, 2 * 16 - 2), fill=(112, 76, 28, 255))
    # 6. the four office doors: an arched double door of dark wood in each stepped face (lower row: the doors; upper: the arch)
    def door(x0, ytop):
        px, py = x0 * 16, ytop * 16
        d.rectangle((px + 3, py + 6, px + 28, py + 31), fill=(34, 26, 22, 255))
        d.pieslice((px + 3, py + 1, px + 28, py + 13), 180, 360, fill=(34, 26, 22, 255))
        d.rectangle((px + 5, py + 8, px + 15, py + 31), fill=(92, 62, 40, 255)); d.rectangle((px + 16, py + 8, px + 26, py + 31), fill=(80, 54, 36, 255))
        d.pieslice((px + 5, py + 3, px + 26, py + 15), 180, 360, fill=(92, 62, 40, 255))
        d.line((px + 15, py + 5, px + 15, py + 31), fill=(34, 26, 22, 255))
        for yy in (py + 14, py + 24): d.line((px + 6, yy, px + 25, yy), fill=(60, 42, 30, 255))
        d.arc((px + 2, py + 0, px + 29, py + 14), 180, 360, fill=(192, 142, 44, 255))
        d.point((px + 13, py + 20), fill=(244, 214, 116, 255)); d.point((px + 18, py + 20), fill=(244, 214, 116, 255))
    for (x0, ytop) in ((7, 1), (5, 2), (14, 1), (16, 2)): door(x0, ytop)
    # 7. the exit mat at the foot (x 10-12, row 17): the Order's blue, gold-edged
    d.rectangle((10 * 16 + 2, 17 * 16 + 6, 13 * 16 - 3, 17 * 16 + 15), fill=(34, 40, 89, 255), outline=(192, 142, 44, 255))
    im = im.crop((1 * 16, 0, 22 * 16, 18 * 16))
    im.convert('RGB').save(out)
    im.convert('RGB').resize((im.size[0] * 3, im.size[1] * 3), Image.NEAREST).save(out.replace('.png', '_3x.png'))
    print('nave mock', im.size)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/nave_mock_v1.png')
