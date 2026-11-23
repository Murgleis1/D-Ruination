"""Floor plans v1 for the Citadel's barracks and armoury (user 2026-11-23: bunks + gear; forge + weapon store; build
from what exists plus the user's prop sheet, assets/templar_hq_reference/user_props/: war banners, a display sword,
helmet stands, iron racks, a workbench, kegs).
Usage: python3 plans.py OUT.png"""
import sys
from PIL import Image, ImageDraw
T = 32
BARRACKS = (16, 14, [      # v2 (user 2026-11-23: v1 "doesn't look right"; split bedrooms, two beds each)
 (0, 0, 16, 2, (190, 180, 150), 'back wall (grey wood)'),
 (1, 2, 6, 1, (90, 90, 100), 'top of the partition'), (9, 2, 6, 1, (90, 90, 100), ''),
 (7, 2, 2, 9, (225, 215, 190), ''),
 (1, 2, 2, 2, (90, 120, 170), 'bed'), (4, 2, 2, 2, (90, 120, 170), 'bed'), (10, 2, 2, 2, (90, 120, 170), 'bed'), (13, 2, 2, 2, (90, 120, 170), 'bed'),
 (3, 2, 1, 1, (120, 80, 50), 'chest'), (12, 2, 1, 1, (120, 80, 50), 'chest'),
 (1, 5, 5, 1, (110, 110, 120), 'PARTITION (doorway at x 6)'), (10, 5, 5, 1, (110, 110, 120), 'PARTITION (doorway at x 9)'),
 (1, 6, 2, 2, (90, 120, 170), 'bed'), (4, 6, 2, 2, (90, 120, 170), 'bed'), (10, 6, 2, 2, (90, 120, 170), 'bed'), (13, 6, 2, 2, (90, 120, 170), 'bed'),
 (3, 6, 1, 1, (120, 80, 50), 'chest'), (12, 6, 1, 1, (120, 80, 50), 'chest'),
 (1, 9, 6, 1, (110, 110, 120), 'PARTITION'), (9, 9, 6, 1, (110, 110, 120), 'PARTITION'),
 (6, 3, 1, 2, (225, 215, 190), 'door-way'), (9, 3, 1, 2, (225, 215, 190), 'door-way'),
 (6, 7, 1, 2, (225, 215, 190), 'door-way'), (9, 7, 1, 2, (225, 215, 190), 'door-way'),
 (7, 3, 2, 6, (210, 200, 175), 'CORRIDOR'),
 (2, 10, 3, 2, (150, 110, 70), 'mess table'), (11, 10, 2, 2, (120, 90, 60), 'weapon wall + kegs'),
 (7, 13, 2, 1, (70, 100, 180), 'door'),
])
ARMOURY = (14, 11, [       # v2 (user 2026-11-23: keep the forge and fireplace; the tree stands, the desk out)
 (0, 0, 14, 2, (190, 180, 150), 'wall (grey wood)'),
 (5, 0, 3, 3, (170, 80, 60), 'THE FORGE (kept)'),
 (1, 0, 2, 2, (200, 200, 210), 'banner'), (11, 0, 2, 2, (200, 200, 210), 'banner'),
 (2, 1, 2, 1, (160, 160, 170), 'swords on the wall'), (9, 1, 2, 1, (160, 160, 170), 'swords on the wall'),
 (6, 3, 1, 1, (60, 60, 70), 'anvil'), (4, 3, 1, 1, (90, 110, 150), 'quench tub'), (8, 3, 2, 1, (120, 90, 60), 'coal kegs'),
 (1, 3, 1, 5, (150, 150, 160), 'helms along the west wall'), (12, 3, 1, 5, (150, 150, 160), 'helms along the east wall'),
 (4, 6, 6, 1, (150, 110, 70), 'WORKBENCHES (finished blades)'),
 (7, 10, 2, 1, (70, 100, 180), 'door'),
])
BARRACKS3 = (21, 13, [     # v3 (user 2026-11-23: built from the user's station barracks reference, right half;
 (0, 0, 21, 2, (190, 180, 150), ''),                 #  no jail; floor in the houses' cream, its grey stone walls kept)
 (7, 0, 1, 7, (20, 20, 20), 'wall'), (15, 0, 1, 7, (20, 20, 20), 'wall'),
 (7, 9, 1, 3, (20, 20, 20), ''), (15, 9, 1, 3, (20, 20, 20), ''),
 (7, 5, 1, 2, (120, 120, 130), 'stub'), (15, 5, 1, 2, (120, 120, 130), 'stub'),
 (1, 0, 6, 2, (175, 170, 160), 'BRIEFING ROOM'),
 (3, 0, 2, 3, (120, 80, 50), 'bookshelf'), (5, 1, 2, 2, (130, 90, 60), 'desk+ledger'), (6, 3, 1, 1, (200, 90, 60), 'chair'),
 (1, 2, 2, 3, (160, 160, 175), 'books table'), (3, 4, 1, 1, (200, 90, 60), 'chair'),
 (2, 6, 4, 1, (200, 90, 60), 'chairs'), (2, 7, 4, 3, (160, 160, 175), 'BRIEFING TABLE'), (2, 10, 4, 1, (200, 90, 60), 'chairs'),
 (1, 8, 1, 1, (200, 90, 60), 'head'),
 (8, 0, 7, 2, (175, 170, 160), 'BUNK HALL   banner'),
 (8, 2, 1, 2, (90, 120, 170), 'bed'), (10, 2, 1, 2, (90, 120, 170), 'bed'), (12, 2, 1, 2, (90, 120, 170), 'bed'), (14, 2, 1, 2, (90, 120, 170), 'bed'),
 (8, 5, 1, 2, (90, 120, 170), 'bed'), (10, 5, 1, 2, (90, 120, 170), 'bed'), (12, 5, 1, 2, (90, 120, 170), 'bed'), (14, 5, 1, 2, (90, 120, 170), 'bed'),
 (8, 9, 2, 3, (150, 110, 70), 'lockers'), (13, 9, 2, 3, (150, 110, 70), 'lockers'),
 (10, 11, 3, 1, (70, 100, 180), 'DOOR (3 wide)'),
 (16, 0, 4, 2, (175, 170, 160), 'GEAR + DUTY'),
 (16, 1, 2, 2, (160, 160, 170), 'swords+banner'), (18, 2, 1, 1, (150, 150, 160), 'helm'), (19, 2, 1, 1, (150, 150, 160), 'helm'),
 (16, 4, 1, 3, (130, 90, 60), 'duty desk'), (17, 5, 1, 1, (200, 90, 60), 'chair'),
 (18, 9, 2, 1, (120, 90, 60), 'kegs'), (16, 9, 1, 3, (170, 140, 90), 'sack'), (17, 11, 1, 1, (200, 170, 60), 'crate'),
])
WATCH = (14, 11, [         # v1 (user 2026-11-23: the east house a watch house, not a second Braviary mews)
 (0, 0, 14, 2, (190, 180, 150), 'wall (grey wood)'),
 (1, 0, 3, 2, (200, 170, 110), 'DISPATCH BOARD'), (6, 0, 2, 2, (200, 200, 210), 'banner'),
 (10, 0, 3, 2, (215, 195, 150), 'MAP OF THE PASS'),
 (1, 2, 2, 1, (120, 80, 50), 'report cabinet'), (3, 2, 1, 1, (150, 120, 80), 'scrolls'),
 (12, 2, 1, 2, (150, 150, 160), 'helms'),
 (6, 3, 2, 1, (60, 90, 160), 'CAPTAIN (stands)'),
 (5, 4, 4, 2, (150, 110, 70), 'MAP TABLE (route 15 laid out)'),
 (1, 5, 2, 1, (130, 90, 60), 'scribe desk'), (1, 6, 1, 1, (60, 90, 160), 'scribe'),
 (11, 5, 2, 2, (110, 100, 90), 'runners bench'), (12, 7, 1, 1, (90, 90, 100), 'horn+lantern'),
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
    if out.endswith('barracks3.png'):
        im = draw(BARRACKS3, 'BARRACKS v3 21x13: briefing room | bunk hall | gear + duty (corridor rows 7-8)')
        d = ImageDraw.Draw(im); d.text((8 * T + 4, 7 * T + 10), 'CORRIDOR: the doorways at x 7 and x 15', fill=(90, 70, 50)); im.save(out); return
    if out.endswith('watch.png'):
        draw(WATCH, 'WATCH HOUSE v1 14x11: the command post for Route 15').save(out); return
    a = draw(BARRACKS, 'BARRACKS v2 16x14: four bedrooms, two beds each'); b = draw(ARMOURY, 'ARMOURY v2 14x11: a working smithy')
    im = Image.new('RGB', (a.size[0] + b.size[0] + 16, max(a.size[1], b.size[1])), (60, 60, 60)); im.paste(a, (0, 0)); im.paste(b, (a.size[0] + 16, 0)); im.save(out)
if __name__ == '__main__':
    main(sys.argv[1])
