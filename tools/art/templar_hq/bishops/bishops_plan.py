"""The bishops' chambers, floor plans v1 (user 2026-11-23): two rooms.
1. The study hall (entered from the nave's west door at the head of the nave): the bishops' day room, for prayer,
   discussion and day-to-day record keeping; visiting diplomats and notables mingle here (discreet meetings go to
   Ambrose's study instead). 18x13: wall rows 0-2, floor 3-11, the door from the nave at the bottom centre (row 12).
   Prayer at the head (a shrine with kneelers, on the axis from the door); records west (clerks' desks, shelves,
   scroll racks); discussion and mingling east (a long table with chairs, a sitting corner); the dormitory's door in
   the north wall, west end, past the records. One subtle clue (user): on one clerk's desk, a letter the player can
   read, hinting at the cult-aligned bishops (wording in the story stage).
2. The dormitory (through the hall's north-west door): one shared sleeping room. 20x10 (user: six bishops): six beds along the north
   wall (heads to the wall), a bedside stand and a footlocker at each, two wardrobes, a washstand, a small shrine,
   candle stands; the door at the bottom (row 9).
Usage: python3 bishops_plan.py OUT.png"""
import sys
from PIL import Image, ImageDraw
T = 32
HALL = (18, 13, [
 (0, 0, 18, 2, (190, 180, 150), 'back wall (cream stone)'), (0, 2, 18, 1, (150, 120, 90), 'panelling'),
 (2, 1, 1, 2, (60, 45, 35), 'DOOR'), (2, 0, 3, 1, None, 'to dormitory'),
 (8, 1, 2, 3, (220, 210, 170), 'shrine'), (6, 2, 1, 2, (60, 90, 170), 'bnr'), (11, 2, 1, 2, (60, 90, 170), 'bnr'),
 (7, 4, 4, 1, (110, 130, 190), 'kneelers'),
 (4, 2, 2, 2, (120, 80, 50), 'books'), (1, 4, 1, 3, (120, 80, 50), 'scrolls'),
 (3, 6, 2, 1, (150, 110, 70), 'desk'), (3, 5, 2, 1, (170, 150, 120), 'chair'),
 (3, 9, 2, 1, (150, 110, 70), 'desk*'), (3, 8, 2, 1, (170, 150, 120), 'chair'),
 (12, 2, 2, 2, (120, 80, 50), 'books'), (14, 2, 2, 2, (120, 80, 50), 'cabinet'),
 (12, 6, 4, 2, (150, 110, 70), 'long table'),
 (12, 5, 1, 1, (170, 150, 120), 'c'), (13, 5, 1, 1, (170, 150, 120), 'c'), (14, 5, 1, 1, (170, 150, 120), 'c'), (15, 5, 1, 1, (170, 150, 120), 'c'),
 (12, 8, 1, 1, (170, 150, 120), 'c'), (13, 8, 1, 1, (170, 150, 120), 'c'), (14, 8, 1, 1, (170, 150, 120), 'c'), (15, 8, 1, 1, (170, 150, 120), 'c'),
 (14, 10, 2, 1, (90, 110, 170), 'armchairs'), (16, 9, 1, 2, (90, 110, 170), 'sofa'),
 (1, 10, 1, 1, (220, 190, 90), 'cnd'), (16, 3, 1, 1, (220, 190, 90), 'cnd'),
 (6, 10, 1, 1, (150, 150, 150), 'bust'), (11, 10, 1, 1, (150, 150, 150), 'bust'),
 (8, 12, 2, 1, (70, 100, 180), 'door from nave'),
])
DORM = (20, 10, [
 (0, 0, 20, 2, (190, 180, 150), 'back wall'), (0, 2, 20, 1, (150, 120, 90), 'panelling'),
 (2, 2, 1, 2, (200, 200, 220), 'bed'), (3, 3, 1, 1, (160, 140, 100), 'std'), (2, 4, 1, 1, (120, 80, 50), 'ftlk'),
 (5, 2, 1, 2, (200, 200, 220), 'bed'), (6, 3, 1, 1, (160, 140, 100), 'std'), (5, 4, 1, 1, (120, 80, 50), 'ftlk'),
 (8, 2, 1, 2, (200, 200, 220), 'bed'), (9, 3, 1, 1, (160, 140, 100), 'std'), (8, 4, 1, 1, (120, 80, 50), 'ftlk'),
 (11, 2, 1, 2, (200, 200, 220), 'bed'), (12, 3, 1, 1, (160, 140, 100), 'std'), (11, 4, 1, 1, (120, 80, 50), 'ftlk'),
 (14, 2, 1, 2, (200, 200, 220), 'bed'), (15, 3, 1, 1, (160, 140, 100), 'std'), (14, 4, 1, 1, (120, 80, 50), 'ftlk'),
 (17, 2, 1, 2, (200, 200, 220), 'bed'), (18, 3, 1, 1, (160, 140, 100), 'std'), (17, 4, 1, 1, (120, 80, 50), 'ftlk'),
 (1, 6, 1, 2, (120, 80, 50), 'wardrobe'), (18, 6, 1, 2, (120, 80, 50), 'wardrobe'),
 (4, 7, 2, 1, (170, 190, 210), 'washstand'), (14, 7, 2, 1, (220, 210, 170), 'small shrine'),
 (1, 8, 1, 1, (220, 190, 90), 'cnd'), (18, 8, 1, 1, (220, 190, 90), 'cnd'),
 (9, 9, 2, 1, (70, 100, 180), 'door to hall'),
])
def draw(spec, title):
    W, H, Z = spec
    im = Image.new('RGB', (W * T, H * T + 18), (225, 215, 190)); d = ImageDraw.Draw(im)
    d.rectangle((0, H * T, W * T, H * T + 18), fill=(40, 40, 40)); d.text((4, H * T + 3), title, fill=(255, 255, 255))
    for x in (0, W - 1): d.rectangle((x * T, 0, (x + 1) * T - 1, H * T), fill=(20, 20, 20))
    d.rectangle((0, (H - 1) * T, W * T, H * T), fill=(20, 20, 20))
    for x, y, w, h, c, lab in Z:
        if c: d.rectangle((x * T + 1, y * T + 1, (x + w) * T - 2, (y + h) * T - 2), fill=c)
        if lab: d.text((x * T + 2, y * T + 2), lab, fill=(255, 255, 255) if c else (60, 40, 20))
    for x in range(W + 1): d.line((x * T, 0, x * T, H * T), fill=(150, 140, 120))
    for y in range(H + 1): d.line((0, y * T, W * T, y * T), fill=(150, 140, 120))
    return im
def main(out):
    a = draw(HALL, 'STUDY HALL 18x13  (* = the desk with the letter)'); b = draw(DORM, 'DORMITORY 20x10 (six beds)')
    im = Image.new('RGB', (a.size[0] + b.size[0] + 16, max(a.size[1], b.size[1])), (60, 60, 60))
    im.paste(a, (0, 0)); im.paste(b, (a.size[0] + 16, 0)); im.save(out)
if __name__ == '__main__':
    main(sys.argv[1])
