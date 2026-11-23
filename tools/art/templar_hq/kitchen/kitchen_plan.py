"""The kitchen, floor plan v1 (behind the nave's west door at its foot; user 2026-11-22: the prime cathedral's
kitchen, where the Templars cook and feed themselves; the storehouse is its own room behind the east door).
References (kitchen_references.png): Odyssey 1.30 (an arched brick oven and a chimney hearth on the back wall, one
big table), MonoMyth 8822718 (a counter with a stove top, plates and pots), MonoMyth's cabin (the user's stove,
firewood beside it), MonoMyth's hut 87f6e98 (long tables set with plates of food).
16x12: wall rows 0-2 (cream), panelling row 3, floor rows 4-10, the door from the nave at the bottom centre (row 11).
- Cooking, the back wall: the user's pot-bellied stove (MonoMyth) with firewood stacked beside it; a brick oven with
  its chimney (Odyssey 1.30); a prep counter with pots and plates (MonoMyth 8822718); shelves of jars.
- Eating, the middle: one long refectory table set with plates of food, benches or stools both sides.
- Work and water, the sides: a chopping block, a water barrel, sacks of flour.
Usage: python3 kitchen_plan.py OUT.png"""
import sys
from PIL import Image, ImageDraw
T, W, H = 36, 16, 12
Z = [
 (0, 0, 16, 3, (190, 180, 150), 'back wall (cream)'), (0, 3, 16, 1, (150, 120, 90), 'panelling'),
 (1, 2, 2, 2, (60, 60, 70), 'STOVE'), (3, 3, 1, 1, (140, 100, 60), 'wood'),
 (5, 0, 3, 4, (170, 80, 60), 'BRICK OVEN + chimney'),
 (9, 2, 4, 2, (150, 110, 70), 'PREP COUNTER (pots, plates)'),
 (13, 1, 2, 3, (120, 80, 50), 'jar shelves'),
 (5, 6, 6, 2, (150, 110, 70), 'LONG TABLE (plates of food)'),
 (5, 5, 6, 1, (170, 150, 120), 'stools'), (5, 8, 6, 1, (170, 150, 120), 'stools'),
 (1, 6, 1, 1, (140, 100, 60), 'block'), (1, 8, 1, 1, (90, 110, 150), 'water'),
 (14, 6, 1, 2, (200, 190, 160), 'flour sacks'), (13, 9, 2, 1, (120, 90, 60), 'barrels'),
 (7, 11, 2, 1, (70, 100, 180), 'door from nave'),
]
def main(out):
    im = Image.new('RGB', (W * T, H * T + 18), (225, 215, 190)); d = ImageDraw.Draw(im)
    d.rectangle((0, H * T, W * T, H * T + 18), fill=(40, 40, 40)); d.text((4, H * T + 3), 'KITCHEN 16x12', fill=(255, 255, 255))
    for x in (0, W - 1): d.rectangle((x * T, 0, (x + 1) * T - 1, H * T), fill=(20, 20, 20))
    d.rectangle((0, (H - 1) * T, W * T, H * T), fill=(20, 20, 20))
    for x, y, w, h, c, lab in Z:
        d.rectangle((x * T + 1, y * T + 1, (x + w) * T - 2, (y + h) * T - 2), fill=c); d.text((x * T + 2, y * T + 2), lab, fill=(255, 255, 255))
    for x in range(W + 1): d.line((x * T, 0, x * T, H * T), fill=(150, 140, 120))
    for y in range(H + 1): d.line((0, y * T, W * T, y * T), fill=(150, 140, 120))
    im.save(out)
if __name__ == '__main__':
    main(sys.argv[1])
