"""The storehouse, floor plan v1 (behind the nave's east door at its foot; user 2026-11-22: the prime cathedral's
stores, where the Templars stock food). Reference: MonoMyth's warehouse 87f254c (rows of stacked wooden crates
forming aisles; monomyth_warehouse_87f254c.png), with the kitchen's barrels and bottles.
16x12: wall rows 0-1 (cream), panelling row 2, floor rows 3-10, the door from the nave at the bottom centre (row 11).
- Back wall: shelves of preserves and bottles; crates stacked against it at the ends.
- The middle: two rows of crate stacks (MonoMyth's) running east-west, three aisles between and around them.
- East wall: barrels (water, wine, oil). West corner: sacks of grain and flour.
- By the door: the quartermaster's small desk with the stores ledger.
Usage: python3 store_plan.py OUT.png"""
import sys
from PIL import Image, ImageDraw
T, W, H = 36, 16, 12
Z = [
 (0, 0, 16, 2, (190, 180, 150), 'back wall (cream)'), (0, 2, 16, 1, (150, 120, 90), 'panelling'),
 (4, 0, 2, 2, (120, 80, 50), 'preserves'), (10, 0, 2, 2, (120, 80, 50), 'bottles'),
 (1, 2, 2, 2, (170, 120, 70), 'crates'), (13, 2, 2, 2, (170, 120, 70), 'crates'),
 (3, 5, 4, 1, (170, 120, 70), 'CRATE ROW'), (9, 5, 4, 1, (170, 120, 70), 'CRATE ROW'),
 (3, 8, 4, 1, (170, 120, 70), 'CRATE ROW'), (9, 8, 4, 1, (170, 120, 70), 'CRATE ROW'),
 (14, 4, 1, 5, (120, 90, 60), 'barrels'),
 (1, 5, 1, 4, (210, 200, 170), 'sacks'),
 (10, 10, 2, 1, (150, 110, 70), 'quartermaster'),
 (7, 11, 2, 1, (70, 100, 180), 'door from nave'),
]
def main(out):
    im = Image.new('RGB', (W * T, H * T + 18), (225, 215, 190)); d = ImageDraw.Draw(im)
    d.rectangle((0, H * T, W * T, H * T + 18), fill=(40, 40, 40)); d.text((4, H * T + 3), 'STOREHOUSE 16x12', fill=(255, 255, 255))
    for x in (0, W - 1): d.rectangle((x * T, 0, (x + 1) * T - 1, H * T), fill=(20, 20, 20))
    d.rectangle((0, (H - 1) * T, W * T, H * T), fill=(20, 20, 20))
    for x, y, w, h, c, lab in Z:
        d.rectangle((x * T + 1, y * T + 1, (x + w) * T - 2, (y + h) * T - 2), fill=c); d.text((x * T + 2, y * T + 2), lab, fill=(255, 255, 255))
    for x in range(W + 1): d.line((x * T, 0, x * T, H * T), fill=(150, 140, 120))
    for y in range(H + 1): d.line((0, y * T, W * T, y * T), fill=(150, 140, 120))
    im.save(out)
if __name__ == '__main__':
    main(sys.argv[1])
