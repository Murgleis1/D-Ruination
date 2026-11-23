"""Floor plans v1 for the Citadel's barracks and armoury (user 2026-11-23: bunks + gear; forge + weapon store; build
from what exists plus the user's prop sheet, assets/templar_hq_reference/user_props/: war banners, a display sword,
helmet stands, iron racks, a workbench, kegs).
Usage: python3 plans.py OUT.png"""
import sys
from PIL import Image, ImageDraw
T = 32
BARRACKS = (16, 13, [
 (0, 0, 16, 2, (190, 180, 150), 'wall (cream)'), (0, 2, 16, 1, (110, 110, 120), 'panelling (grey wood)'),
 (4, 0, 2, 2, (200, 200, 210), 'swords banner'), (7, 0, 2, 2, (200, 200, 210), 'shield banner'), (10, 0, 2, 2, (200, 200, 210), 'swords banner'),
 (1, 3, 2, 3, (90, 120, 170), 'bed'), (1, 6, 2, 3, (90, 120, 170), 'bed'), (1, 9, 2, 3, (90, 120, 170), 'bed'),
 (13, 3, 2, 3, (90, 120, 170), 'bed'), (13, 6, 2, 3, (90, 120, 170), 'bed'), (13, 9, 2, 3, (90, 120, 170), 'bed'),
 (4, 3, 1, 2, (150, 150, 160), 'helmet'), (11, 3, 1, 2, (150, 150, 160), 'helmet'),
 (6, 3, 4, 2, (130, 100, 70), 'weapon rack (iron stands)'),
 (6, 6, 4, 2, (150, 110, 70), 'drill table'), (4, 9, 1, 1, (120, 90, 60), 'kegs'), (11, 9, 1, 1, (120, 90, 60), 'kegs'),
 (9, 10, 2, 1, (150, 110, 70), "sergeant's desk"),
 (7, 12, 2, 1, (70, 100, 180), 'door'),
])
ARMOURY = (14, 11, [
 (0, 0, 14, 2, (190, 180, 150), 'wall (cream)'), (0, 2, 14, 1, (110, 110, 120), 'panelling'),
 (5, 0, 4, 3, (170, 80, 60), 'THE FORGE (hearth + fire)'),
 (1, 0, 2, 2, (200, 200, 210), 'banner'), (11, 0, 2, 2, (200, 200, 210), 'banner'),
 (1, 3, 1, 3, (130, 100, 70), 'swords (wall)'), (12, 3, 1, 3, (130, 100, 70), 'swords (wall)'),
 (5, 4, 3, 1, (150, 110, 70), 'workbench + sword'), (9, 3, 2, 2, (120, 90, 60), 'kegs, coal'),
 (3, 6, 1, 2, (150, 150, 160), 'helm'), (5, 6, 1, 2, (150, 150, 160), 'helm'), (8, 6, 1, 2, (150, 150, 160), 'helm'), (10, 6, 1, 2, (150, 150, 160), 'helm'),
 (1, 8, 2, 1, (150, 110, 70), 'quartermaster'),
 (11, 8, 2, 1, (130, 100, 70), 'iron rack'),
 (6, 10, 2, 1, (70, 100, 180), 'door'),
])
def draw(spec, title):
    W, H, Z = spec
    im = Image.new('RGB', (W * T, H * T + 18), (225, 215, 190)); d = ImageDraw.Draw(im)
    d.rectangle((0, H * T, W * T, H * T + 18), fill=(40, 40, 40)); d.text((4, H * T + 3), title, fill=(255, 255, 255))
    for x in (0, W - 1): d.rectangle((x * T, 0, (x + 1) * T - 1, H * T), fill=(20, 20, 20))
    d.rectangle((0, (H - 1) * T, W * T, H * T), fill=(20, 20, 20))
    for x, y, w, h, c, lab in Z:
        d.rectangle((x * T + 1, y * T + 1, (x + w) * T - 2, (y + h) * T - 2), fill=c); d.text((x * T + 2, y * T + 2), lab, fill=(255, 255, 255))
    for x in range(W + 1): d.line((x * T, 0, x * T, H * T), fill=(150, 140, 120))
    for y in range(H + 1): d.line((0, y * T, W * T, y * T), fill=(150, 140, 120))
    return im
def main(out):
    a = draw(BARRACKS, 'BARRACKS 16x13'); b = draw(ARMOURY, 'ARMOURY 14x11')
    im = Image.new('RGB', (a.size[0] + b.size[0] + 16, max(a.size[1], b.size[1])), (60, 60, 60)); im.paste(a, (0, 0)); im.paste(b, (a.size[0] + 16, 0)); im.save(out)
if __name__ == '__main__':
    main(sys.argv[1])
