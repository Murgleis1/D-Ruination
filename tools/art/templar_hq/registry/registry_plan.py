"""The Braviary registry, floor plan v1 (behind the nave's east door at its head). The office that keeps the empire's
Braviary travel running (bible: every city's Tavern Templar flies paying travellers, fares by distance; House Raptora
bred the line and watches every flight). 16x12: wall rows 0-1, panelling row 2, floor rows 3-10, the door from the
nave at the bottom centre (row 11).
- Back wall: a great map of Cormoria with the flight routes, centred; ledger shelves either side (every Braviary and
  its Templar, the flight logs, the fare tables).
- The registrar's counter across the room: the registrar behind it logs flights and assigns birds; Templars come to
  it from the door side.
- West: the dispatch rack (pigeonholes for orders to every Tavern) and a clerk's desk.
- East: a perch with a Braviary resting on it (a messenger bird between flights), a feed basket.
- By the door: a bench where Templars wait their turn.
- Optional lore hook: a House Raptora liaison at the clerk's desk, watching the logs.
Usage: python3 registry_plan.py OUT.png"""
import sys
from PIL import Image, ImageDraw
T = 36
W, H = 16, 12
Z = [
 (0, 0, 16, 2, (190, 180, 150), 'back wall (cream)'), (0, 2, 16, 1, (150, 120, 90), 'panelling'),
 (5, 0, 6, 2, (120, 150, 110), 'MAP OF CORMORIA (routes)'),
 (1, 2, 2, 2, (120, 80, 50), 'ledgers'), (3, 2, 2, 2, (120, 80, 50), 'ledgers'),
 (11, 2, 2, 2, (120, 80, 50), 'ledgers'), (13, 2, 2, 2, (120, 80, 50), 'ledgers'),
 (7, 4, 2, 1, (170, 150, 120), 'registrar'),
 (4, 5, 8, 1, (150, 110, 70), "REGISTRAR'S COUNTER"),
 (1, 5, 1, 3, (120, 80, 50), 'dispatch rack'),
 (2, 8, 2, 1, (150, 110, 70), 'desk'), (2, 7, 2, 1, (170, 150, 120), 'clerk (Raptora?)'),
 (13, 6, 2, 2, (200, 170, 110), 'PERCH + Braviary'), (14, 8, 1, 1, (160, 140, 100), 'feed'),
 (10, 9, 3, 1, (150, 120, 90), 'bench'),
 (1, 10, 1, 1, (220, 190, 90), 'cnd'), (14, 10, 1, 1, (220, 190, 90), 'cnd'),
 (7, 11, 2, 1, (70, 100, 180), 'door from nave'),
]
def main(out):
    im = Image.new('RGB', (W * T, H * T + 18), (225, 215, 190)); d = ImageDraw.Draw(im)
    d.rectangle((0, H * T, W * T, H * T + 18), fill=(40, 40, 40)); d.text((4, H * T + 3), 'BRAVIARY REGISTRY 16x12', fill=(255, 255, 255))
    for x in (0, W - 1): d.rectangle((x * T, 0, (x + 1) * T - 1, H * T), fill=(20, 20, 20))
    d.rectangle((0, (H - 1) * T, W * T, H * T), fill=(20, 20, 20))
    for x, y, w, h, c, lab in Z:
        d.rectangle((x * T + 1, y * T + 1, (x + w) * T - 2, (y + h) * T - 2), fill=c)
        d.text((x * T + 2, y * T + 2), lab, fill=(255, 255, 255))
    for x in range(W + 1): d.line((x * T, 0, x * T, H * T), fill=(150, 140, 120))
    for y in range(H + 1): d.line((0, y * T, W * T, y * T), fill=(150, 140, 120))
    for y in (6, 7, 8, 9, 10): d.text((7 * T + 14, y * T + 12), '|  |', fill=(200, 40, 40))
    im.save(out)
if __name__ == '__main__':
    main(sys.argv[1])
