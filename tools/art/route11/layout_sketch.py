"""Layout sketches (zone plans, before any pixel art) for Route 11 and Hollow Hill (user brief 2026-11-20).
Usage: python3 tools/art/route11/layout_sketch.py out.png"""
import sys
from PIL import Image, ImageDraw, ImageFont
S = 14                                                   # px per cell
C = dict(grass=(150, 214, 170), pine=(40, 120, 80), road=(170, 170, 175), dirt=(214, 190, 130),
         field=(150, 110, 70), crops=(110, 170, 60), flowers=(240, 200, 90), tall=(70, 160, 70),
         cliff=(190, 130, 80), cliff_hi=(222, 170, 110), sand=(240, 220, 160), sea=(70, 120, 200),
         dark=(70, 110, 60), darkgrass=(110, 150, 90), house=(140, 110, 80), t1=(120, 150, 100),
         t2=(100, 135, 90), t3=(85, 120, 80), rock=(130, 130, 140), door=(40, 30, 40), fog=(200, 205, 215))

def box(d, ox, oy, x0, y0, x1, y1, col, outline=None):
    d.rectangle([ox + x0 * S, oy + y0 * S, ox + (x1 + 1) * S - 1, oy + (y1 + 1) * S - 1], fill=col, outline=outline)

def label(d, ox, oy, x, y, t, f, col=(0, 0, 0)):
    d.text((ox + x * S, oy + y * S), t, fill=col, font=f)

def route11(d, ox, oy, f):
    W, H = 45, 30
    box(d, ox, oy, 0, 0, W - 1, H - 1, C['grass'])
    # the dark forest to the west (Hollow Hill's woods reaching out), with its dark grass
    box(d, ox, oy, 0, 0, 13, H - 1, C['darkgrass'])
    for (a, b, c, e) in [(0, 0, 13, 10), (0, 18, 13, 29), (11, 0, 16, 6), (11, 22, 15, 29), (14, 7, 16, 11)]:
        box(d, ox, oy, a, b, c, e, C['dark'])
    box(d, ox, oy, 3, 11, 7, 12, C['tall']); box(d, ox, oy, 2, 17, 6, 17, C['tall'])
    # Pelluca's pines on the east edge (the seam: Cormoria tiles only, cols 37-44)
    box(d, ox, oy, 37, 0, 44, 13, C['pine']); box(d, ox, oy, 37, 17, 44, 29, C['pine'])
    # the road: Pelluca's cobbles west to the farm, then a dirt track into the woods
    box(d, ox, oy, 24, 14, 44, 16, C['road']); box(d, ox, oy, 0, 13, 23, 15, C['dirt'])
    # north: tan cliffs, stepping down to the fields (the "cliff elements")
    for (a, b, c, e) in [(15, 0, 36, 2), (17, 3, 25, 4), (30, 3, 36, 4)]:
        box(d, ox, oy, a, b, c, e, C['cliff'])
    box(d, ox, oy, 18, 0, 24, 1, C['cliff_hi']); box(d, ox, oy, 31, 0, 35, 1, C['cliff_hi'])
    # the farm north of the road: a thatched farmhouse, its fenced yard, cabbage rows, a sown field, hay
    box(d, ox, oy, 27, 6, 33, 9, C['house']); box(d, ox, oy, 26, 10, 34, 11, (200, 200, 150), outline=(120, 80, 40))
    box(d, ox, oy, 18, 6, 24, 8, C['crops']); box(d, ox, oy, 18, 9, 24, 11, C['field'])
    box(d, ox, oy, 35, 9, 36, 10, C['flowers'])
    # south of the road: flower rows (fenced), tall grass, then the cliff drop to a little cove
    box(d, ox, oy, 28, 18, 34, 20, C['flowers'], outline=(120, 80, 40))
    box(d, ox, oy, 18, 18, 25, 21, C['tall']); box(d, ox, oy, 35, 19, 36, 21, C['tall'])
    for (a, b, c, e) in [(14, 22, 21, 23), (30, 22, 36, 23), (14, 24, 16, 29), (34, 24, 36, 29)]:
        box(d, ox, oy, a, b, c, e, C['cliff'])
    box(d, ox, oy, 22, 22, 29, 23, C['grass']); box(d, ox, oy, 17, 24, 33, 25, C['sand'])
    box(d, ox, oy, 17, 26, 33, 29, C['sea'])
    for x, y, t in [(1, 14, 'to Hollow Hill'), (38, 14, 'Pelluca'), (27, 7, 'farmhouse'), (18, 6, 'cabbages'),
                    (18, 9, 'sown field'), (28, 18, 'flower rows'), (18, 18, 'tall grass'), (20, 26, 'cove'),
                    (19, 0, 'tan cliffs'), (1, 3, 'dark woods'), (38, 3, 'pines'), (11, 13, 'Eiscue scene')]:
        label(d, ox, oy, x, y, t, f, (255, 255, 255) if t in ('dark woods', 'pines', 'cove', 'to Hollow Hill') else (0, 0, 0))
    d.ellipse([ox + 12 * S, oy + 14 * S, ox + 14 * S, oy + 16 * S], outline=(255, 0, 0), width=2)
    for y in range(H): d.line([ox, oy + y * S, ox + W * S, oy + y * S], fill=(0, 0, 0, 40))

def hollow(d, ox, oy, f):
    W, H = 50, 50
    box(d, ox, oy, 0, 0, W - 1, H - 1, C['dark'])
    # concentric terraces rising to the centre: each ring a cliff step up, the forest thinning
    rings = [(4, 4, 45, 45, C['t1']), (10, 10, 39, 39, C['t2']), (16, 16, 33, 33, C['t3'])]
    for (a, b, c, e, col) in rings: box(d, ox, oy, a, b, c, e, col, outline=(60, 40, 30))
    box(d, ox, oy, 21, 21, 28, 28, C['rock'], outline=(40, 40, 40))
    box(d, ox, oy, 24, 28, 25, 28, C['door'])
    # the climbing path: in from the east, round each ring to its stairs
    path = [((49, 30), (42, 30)), ((42, 30), (42, 42)), ((42, 42), (7, 42)), ((7, 42), (7, 7)),   # first ring
            ((7, 7), (22, 7)), ((22, 7), (22, 0)),                                                      # north exit
            ((7, 25), (13, 25)), ((13, 25), (13, 36)), ((13, 36), (36, 36)), ((36, 36), (36, 13)),       # up to the 2nd
            ((36, 13), (25, 13)), ((25, 13), (25, 19)), ((25, 19), (19, 19)), ((19, 19), (19, 30)),      # up to the 3rd
            ((19, 30), (24, 30)), ((24, 30), (24, 29))]                                                  # the sealed door
    for (a, b) in path:
        d.line([ox + a[0] * S + S // 2, oy + a[1] * S + S // 2, ox + b[0] * S + S // 2, oy + b[1] * S + S // 2],
               fill=C['dirt'], width=S - 4)
    for (x, y) in [(10, 25), (13, 24), (36, 12), (25, 16), (19, 18)]:                                  # stairs
        box(d, ox, oy, x, y, x, y, (240, 240, 240))
    for x, y, t, c in [(41, 29, 'from Route 11', (255, 255, 255)), (24, 1, 'north exit to Mirroh: Glaive', (255, 255, 255)),
                       (17, 17, 'third ring', (0, 0, 0)), (11, 11, 'second ring', (0, 0, 0)), (5, 5, 'first ring', (0, 0, 0)),
                       (21, 24, 'rock knoll', (255, 255, 255)), (18, 29, 'SEALED tunnel door', (255, 0, 0)),
                       (2, 43, 'Eiscue + the 1v2', (255, 255, 0)), (1, 47, 'fog (weather), Ghost-drawing woods', (255, 255, 255))]:
        label(d, ox, oy, x, y, t, f, c)
    d.ellipse([ox + 4 * S, oy + 39 * S, ox + 10 * S, oy + 45 * S], outline=(255, 255, 0), width=2)
    d.ellipse([ox + 20 * S, oy + 0 * S, ox + 25 * S, oy + 4 * S], outline=(255, 255, 255), width=2)

def main(out):
    f = ImageFont.load_default()
    img = Image.new('RGB', (45 * S + 50 * S + 60, 50 * S + 70), (30, 30, 34)); d = ImageDraw.Draw(img, 'RGBA')
    d.text((10, 8), 'ROUTE 11 (45x30): Pelluca -> west. Farmland, tan cliffs, a little cove; cooler dark woods at the west end', fill=(255, 255, 255), font=f)
    route11(d, 10, 30, f)
    ox = 45 * S + 40
    d.text((ox, 8), 'HOLLOW HILL (about 50x50): forest rising in rings to the centre; the tunnel up to the summit is sealed', fill=(255, 255, 255), font=f)
    hollow(d, ox, 30, f)
    img.save(out)

if __name__ == '__main__':
    main(sys.argv[1])

def route11_v2(d, ox, oy, f):
    """Revision 2 (user 2026-11-20): twice as long (90x30); the Ivy River's thin western branch comes down from the
    north (as on the illustrated region map, just west of Pelluca), under a bridge on the road, to the sea at the
    cove; the grass darkens in bands, each band reaching into the next in patches."""
    W, H = 90, 30
    shades = [(150, 214, 170), (128, 196, 140), (122, 188, 108), (100, 150, 84)]     # mint, sage, spring, olive
    bands = [(66, 89, 0), (44, 65, 1), (22, 43, 2), (0, 21, 3)]
    for a, b, k in bands: box(d, ox, oy, a, 0, b, H - 1, shades[k])
    import random; rnd = random.Random(3)
    for a, b, k in bands[:-1]:                                  # the next band's patches reaching in
        for _ in range(6):
            px = rnd.randint(a - 4, a + 6); py = rnd.randint(0, H - 3)
            box(d, ox, oy, px, py, px + rnd.randint(1, 3), py + rnd.randint(1, 2), shades[k + 1])
    box(d, ox, oy, 82, 0, 89, 13, C['pine']); box(d, ox, oy, 82, 17, 89, 29, C['pine'])
    for (a, b, c, e) in [(64, 0, 71, 3), (70, 4, 72, 6), (48, 19, 52, 22)]: box(d, ox, oy, a, b, c, e, C['pine'])
    for (a, b, c, e) in [(30, 2, 38, 6), (36, 20, 41, 24), (24, 24, 30, 29)]: box(d, ox, oy, a, b, c, e, (60, 120, 70))
    box(d, ox, oy, 0, 0, 19, 10, C['dark']); box(d, ox, oy, 0, 19, 21, 29, C['dark']); box(d, ox, oy, 12, 0, 26, 5, C['dark'])
    for (a, b, c, e) in [(72, 0, 81, 2), (73, 3, 80, 4)]: box(d, ox, oy, a, b, c, e, C['cliff'])
    box(d, ox, oy, 73, 6, 79, 9, C['house']); box(d, ox, oy, 72, 10, 80, 11, (200, 200, 150), outline=(120, 80, 40))
    box(d, ox, oy, 66, 6, 71, 8, C['crops']); box(d, ox, oy, 66, 9, 71, 11, C['field'])
    box(d, ox, oy, 74, 18, 80, 20, C['flowers'], outline=(120, 80, 40)); box(d, ox, oy, 66, 18, 71, 20, C['tall'])
    # the river: from the north edge, a fall over the cliff step, under the bridge, out to the cove
    river = [(59, 0, 62, 5), (60, 6, 62, 8), (59, 9, 62, 13), (59, 17, 62, 21), (58, 22, 63, 23)]
    for (a, b, c, e) in river: box(d, ox, oy, a, b, c, e, C['sea'])
    box(d, ox, oy, 59, 6, 62, 7, (220, 235, 250))                # the fall
    box(d, ox, oy, 58, 14, 63, 16, (150, 100, 60))               # the bridge
    box(d, ox, oy, 63, 21, 81, 22, (60, 60, 70)); box(d, ox, oy, 52, 21, 57, 22, (60, 60, 70))    # sea wall
    box(d, ox, oy, 52, 23, 81, 24, C['sand']); box(d, ox, oy, 52, 25, 81, 29, C['sea'])
    box(d, ox, oy, 64, 14, 89, 16, C['road']); box(d, ox, oy, 0, 14, 57, 16, C['dirt'])
    for a, b, c, e in [(30, 12, 35, 13), (8, 11, 13, 12), (40, 17, 45, 18), (16, 17, 20, 18), (50, 10, 54, 12)]:
        box(d, ox, oy, a, b, c, e, C['tall'])
    for x, y, t, c in [(83, 14, 'Pelluca', (0, 0, 0)), (1, 14, 'to Hollow Hill', (0, 0, 0)), (73, 6, 'farm', (255, 255, 255)),
                       (55, 0, 'river (from the Ivy, N)', (0, 0, 0)), (58, 13, 'bridge', (0, 0, 0)), (60, 26, 'cove', (255, 255, 255)),
                       (66, 0, 'pines', (255, 255, 255)), (31, 3, 'mixed', (255, 255, 255)), (2, 3, 'dark woods', (255, 255, 255)),
                       (74, 0, 'tan cliffs', (0, 0, 0)), (14, 13, 'Eiscue', (200, 0, 0)),
                       (67, 27, 'mint', (255, 255, 255)), (46, 27, 'sage', (0, 0, 0)), (24, 27, '', (0, 0, 0)),
                       (44, 0, 'sage band', (0, 0, 0)), (23, 7, 'spring band', (0, 0, 0)), (2, 13, '', (0, 0, 0))]:
        label(d, ox, oy, x, y, t, f, c)

def main_v2(out):
    f = ImageFont.load_default()
    img = Image.new('RGB', (90 * S + 20, 30 * S + 50), (30, 30, 34)); d = ImageDraw.Draw(img, 'RGBA')
    d.text((10, 8), 'ROUTE 11 rev. 2 (90x30): mint -> sage -> spring -> olive grass in bands (patches of the next reaching in); pines -> mixed -> dark woods; the river and bridge near Pelluca', fill=(255, 255, 255), font=f)
    route11_v2(d, 10, 30, f); img.save(out)

def route11_v3(d, ox, oy, f):
    """Revision 3 (user 2026-11-20): the river comes in from the north-east (from the Ivy, north of Pelluca) and
    runs down south-west to the sea in a terraced gorge with falls (MonoMyth's Route 7 as the model); the road
    bridges the gorge; the beach is only the river mouth's, so nothing crosses the river's way."""
    W, H = 90, 30
    shades = [(150, 214, 170), (128, 196, 140), (122, 188, 108), (100, 150, 84)]
    for a, b, k in [(60, 89, 0), (40, 59, 1), (20, 39, 2), (0, 19, 3)]: box(d, ox, oy, a, 0, b, H - 1, shades[k])
    import random; rnd = random.Random(5)
    for a, k in [(60, 1), (40, 2), (20, 3)]:
        for _ in range(6):
            px = rnd.randint(a - 3, a + 6); py = rnd.randint(0, H - 3)
            if not (13 <= py <= 17): box(d, ox, oy, px, py, px + rnd.randint(1, 3), py + rnd.randint(1, 2), shades[k])
    box(d, ox, oy, 82, 0, 89, 13, C['pine']); box(d, ox, oy, 82, 17, 89, 29, C['pine'])
    # the gorge: terraced cliffs either side of the river, falls at each step
    gorge = [(71, 0, 80, 4), (68, 5, 78, 9), (65, 10, 76, 13), (63, 17, 74, 20), (59, 21, 70, 24)]
    for (a, b, c, e) in gorge: box(d, ox, oy, a, b, c, e, C['cliff'])
    river = [(74, 0, 77, 4), (71, 5, 74, 9), (68, 10, 72, 13), (66, 17, 71, 20), (61, 21, 66, 24), (60, 25, 66, 26)]
    for (a, b, c, e) in river: box(d, ox, oy, a, b, c, e, C['sea'])
    for (a, b, c, e) in [(74, 4, 77, 4), (71, 9, 74, 9), (66, 20, 71, 20)]: box(d, ox, oy, a, b, c, e, (225, 238, 250))
    box(d, ox, oy, 64, 14, 75, 16, (150, 100, 60))                 # the bridge
    box(d, ox, oy, 46, 27, 80, 29, C['sea']); box(d, ox, oy, 52, 25, 59, 26, C['sand']); box(d, ox, oy, 67, 25, 74, 26, C['sand'])
    box(d, ox, oy, 46, 25, 51, 26, C['cliff']); box(d, ox, oy, 75, 21, 81, 26, C['cliff'])
    # the farm west of the gorge; the road
    box(d, ox, oy, 52, 5, 58, 8, C['house']); box(d, ox, oy, 51, 9, 59, 10, (200, 200, 150), outline=(120, 80, 40))
    box(d, ox, oy, 44, 4, 49, 6, C['crops']); box(d, ox, oy, 44, 7, 49, 10, C['field'])
    box(d, ox, oy, 50, 18, 56, 20, C['flowers'], outline=(120, 80, 40)); box(d, ox, oy, 76, 18, 80, 20, C['tall'])
    box(d, ox, oy, 76, 14, 89, 16, C['road']); box(d, ox, oy, 0, 14, 63, 16, C['dirt'])
    for (a, b, c, e) in [(30, 2, 38, 6), (34, 20, 40, 24), (24, 23, 30, 29), (40, 0, 46, 2)]: box(d, ox, oy, a, b, c, e, (60, 120, 70))
    box(d, ox, oy, 0, 0, 19, 10, C['dark']); box(d, ox, oy, 0, 19, 21, 29, C['dark']); box(d, ox, oy, 12, 0, 26, 5, C['dark'])
    for a, b, c, e in [(30, 11, 35, 12), (8, 11, 13, 12), (40, 18, 45, 19), (16, 17, 20, 18)]: box(d, ox, oy, a, b, c, e, C['tall'])
    for x, y, t, c in [(83, 14, 'Pelluca', (0, 0, 0)), (1, 14, 'to Hollow Hill', (0, 0, 0)), (52, 5, 'farm', (255, 255, 255)),
                       (72, 1, 'river from the Ivy (NE)', (0, 0, 0)), (66, 13, 'bridge', (0, 0, 0)), (60, 28, 'the river mouth', (255, 255, 255)),
                       (31, 3, 'mixed', (255, 255, 255)), (2, 3, 'dark woods', (255, 255, 255)), (14, 13, 'Eiscue', (200, 0, 0)),
                       (62, 22, 'gorge', (0, 0, 0)), (61, 1, 'mint', (0, 0, 0)), (41, 3, 'sage', (0, 0, 0)), (21, 7, 'spring', (0, 0, 0))]:
        label(d, ox, oy, x, y, t, f, c)

def main_v3(out):
    f = ImageFont.load_default()
    img = Image.new('RGB', (90 * S + 20, 30 * S + 50), (30, 30, 34)); d = ImageDraw.Draw(img, 'RGBA')
    d.text((10, 8), 'ROUTE 11 rev. 3 (90x30): the river from the north-east down a terraced gorge (falls) under the bridge to its mouth; beach only at the mouth', fill=(255, 255, 255), font=f)
    route11_v3(d, 10, 30, f); img.save(out)
