"""The Templar cathedral's interior: floor plan v1 (user 2026-11-22: two levels; on the first floor the cathedral is the
central room with several offices around it; a stair from the cathedral room up to the Sanctum, the cross tower's top;
Loulan leads the player to Ambrose at the altar; the Sanctum sealed until Ambrose is beaten).
Usage: python3 tools/art/templar_hq/interior_sketch.py out.png"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'route13'))
from PIL import Image, ImageDraw, ImageFont
from layout_sketch import S, box, ell, path, label

def main(out):
    W, H = 32, 24
    im = Image.new('RGB', (W * S + 20 + 60 + 16 * S + 300, H * S + 40), (30, 30, 36)); d = ImageDraw.Draw(im)
    try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
    except Exception: f = ImageFont.load_default()
    d.text((10, 8), 'TEMPLAR CATHEDRAL, 1F (32x24)                                                  THE SANCTUM, 2F (16x14)', fill=(230, 230, 230), font=f)
    wall, floor, nave, pew, gold, office, door = (70, 70, 86), (196, 188, 168), (214, 206, 184), (150, 120, 70), (220, 180, 70), (176, 150, 120), (20, 20, 26)
    blue, carpet, seal = (60, 74, 150), (64, 80, 170), (160, 60, 60)
    box(d, 0, 0, W - 1, H - 1, wall)
    # the offices: two each side, off a cloister walk
    for (x0, y0, n) in ((1, 1, 'OFFICE 1'), (1, 12, 'OFFICE 2'), (24, 1, 'OFFICE 3'), (24, 12, 'OFFICE 4')):
        box(d, x0, y0, x0 + 6, y0 + 8, office); label(d, x0 + 0.6, y0 + 3.5, n, f)
    for (x, y) in ((4, 10), (4, 21), (27, 10), (27, 21)):
        box(d, x, y, x, y, door)
    box(d, 1, 10, 7, 11, floor); box(d, 1, 21, 7, 22, floor); box(d, 24, 10, 30, 11, floor); box(d, 24, 21, 30, 22, floor)
    box(d, 8, 2, 8, 22, floor); box(d, 23, 2, 23, 22, floor)                     # (the cloister walks either side)
    # the round nave (Crown 1.94's shape), pews in rows either side of the aisle, the altar at its head
    ell(d, 9, 1, 22, 21, nave)
    path(d, [(15.5, 22), (15.5, 4.5)], carpet, 2)
    for y in (8, 10, 12, 14, 16, 18):
        box(d, 11, y, 14, y, pew); box(d, 17, y, 20, y, pew)
    box(d, 13, 2, 18, 4, gold); label(d, 13.3, 2.6, 'ALTAR', f, (40, 30, 10))
    box(d, 15, 5, 16, 5, (240, 240, 240)); label(d, 16.6, 4.8, 'Ambrose', f, (40, 30, 10))
    box(d, 12, 3, 12, 4, (236, 232, 214)); box(d, 19, 3, 19, 4, (236, 232, 214))
    # the stair up to the Sanctum: behind the altar, a doorway in the apse, sealed
    box(d, 15, 0, 16, 1, seal); label(d, 17.2, 0.5, 'stair to the Sanctum (sealed)', f, (240, 200, 200))
    # the doors: an archway from the nave into each cloister
    for (x, y) in ((9, 11), (22, 11)): box(d, x, y, x, y, floor)
    box(d, 14, H - 1, 17, H - 1, (120, 60, 50)); label(d, 18, H - 0.9, 'entrance (the door at the church\'s foot)', f, (240, 240, 240))
    # the Sanctum: Crown 1.79's octagonal chamber, the three stained windows behind its dais
    ox = W + 4
    box(d, ox, 0, ox + 15, 13, wall); ell(d, ox + 1, 1, ox + 14, 13, (190, 200, 216))
    box(d, ox + 6, 1, ox + 9, 3, gold); label(d, ox + 5.7, 1.6, 'dais', f, (40, 30, 10))
    for k in (0, 1, 2): box(d, ox + 5 + k * 2.2, 0, ox + 5.8 + k * 2.2, 0, (120, 170, 240))
    box(d, ox + 7, 7, ox + 8, 8, (30, 30, 36)); label(d, ox + 4.5, 9, 'the shadow self', f)
    box(d, ox + 7, 13, ox + 8, 13, (120, 60, 50)); label(d, ox + 2, 12, 'stair down', f)
    label(d, ox, 15, 'three stained windows + the cross above', f, (230, 230, 230))
    label(d, ox, 16, 'unlocked after the Ambrose fight', f, (230, 230, 230))
    im.save(out)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/cathedral_plan_v1.png')
