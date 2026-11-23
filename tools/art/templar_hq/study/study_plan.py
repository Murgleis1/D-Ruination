"""Ambrose's study, floor plan v2 (after user review 2026-11-23: v1 did not read as an office: no chair behind the
desk, no chairs facing it, nowhere to rest overnight, a stray bureau behind the desk). Grid: 14x11 tiles; wall
rows 0-1, floor rows 2-9, the door (from the nave) at the bottom centre, row 10.
Usage: python3 study_plan.py OUT.png"""
import sys
from PIL import Image, ImageDraw
W, H, T = 14, 11, 40
ZONES = [  # (x, y, w, h, colour, label)
 (0, 0, 14, 2, (190, 180, 150), 'back wall (cream stone)'),
 (6, 0, 2, 2, (60, 90, 170), 'Arceus banner'),
 (1, 2, 2, 2, (120, 80, 50), 'books'), (3, 2, 2, 2, (120, 80, 50), 'books'),
 (4, 3, 6, 4, (70, 100, 180), ''),                      # the rug
 (6, 3, 2, 1, (150, 110, 70), 'his chair'),
 (6, 4, 2, 1, (170, 120, 70), 'DESK'),
 (6, 5, 1, 1, (150, 110, 70), 'chair'), (7, 5, 1, 1, (150, 110, 70), 'chair'),
 (9, 2, 1, 2, (120, 80, 50), 'robes'),
 (10, 2, 1, 1, (160, 140, 100), 'stand'),
 (11, 2, 2, 2, (200, 200, 220), 'BED'),
 (11, 4, 2, 1, (140, 120, 100), 'screen'),
 (1, 6, 2, 2, (90, 110, 170), 'armchair'), (3, 6, 1, 1, (160, 140, 100), 'table'),
 (1, 8, 1, 1, (220, 190, 90), 'candles'), (12, 8, 1, 1, (220, 190, 90), 'candles'),
 (4, 8, 1, 2, (150, 150, 150), 'bust'), (9, 8, 1, 2, (150, 150, 150), 'bust'),
 (6, 10, 2, 1, (70, 100, 180), 'door'),
]
def main(out):
    im = Image.new('RGB', (W * T, H * T), (225, 215, 190)); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, T - 1, H * T), fill=(20, 20, 20)); d.rectangle(((W - 1) * T, 0, W * T, H * T), fill=(20, 20, 20))
    d.rectangle((0, 10 * T, W * T, H * T), fill=(20, 20, 20))
    for x, y, w, h, c, lab in ZONES:
        d.rectangle((x * T + 1, y * T + 1, (x + w) * T - 2, (y + h) * T - 2), fill=c)
        if lab: d.text((x * T + 3, y * T + 3), lab, fill=(255, 255, 255))
    for x in range(W + 1): d.line((x * T, 0, x * T, H * T), fill=(150, 140, 120))
    for y in range(H + 1): d.line((0, y * T, W * T, y * T), fill=(150, 140, 120))
    d.text((4 * T + 3, 6 * T + 26), 'rug (Order blue + gold)', fill=(255, 255, 255))
    for y in (6, 7, 8, 9): d.text((6 * T + 14, y * T + 12), '|', fill=(200, 40, 40)); d.text((7 * T + 14, y * T + 12), '|', fill=(200, 40, 40))
    d.text((5 * T - 30, 9 * T + 12), 'walkway', fill=(200, 40, 40))
    im.save(out)
if __name__ == '__main__':
    main(sys.argv[1])
