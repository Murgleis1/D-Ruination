"""Templar Headquarters ("Templar Citadel"): zone plan v1 (before any pixel art).
Reached from Route 13's north-east branch (the Templars' cobbled pilgrim road, its exit at x 32-34). Seat of the
Templar Arceus order (Archbishop Ambrose Caymen): runs the Taverns and the Braviary mount system. Chapter 1: a side
branch the player may visit or skip (Loulan recurs here); later chapters stage the bishops' coup here.
Art plan (bible 20 §16.10): Crown's gothic cathedral on its moat island with timber chalets (Crown map 3.2), alpine
snow, perhaps an outer wall.
Usage: python3 tools/art/templar_hq/layout_sketch.py out.png"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'route13'))
from PIL import Image, ImageDraw, ImageFont
from layout_sketch import S, C, box, ell, path, label

def main(out):
    W, H = 48, 48
    im = Image.new('RGB', (W * S + 20 + 330, H * S + 40), (30, 30, 36)); d = ImageDraw.Draw(im)
    try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
    except Exception: f = ImageFont.load_default()
    d.text((10, 8), 'TEMPLAR CITADEL (48x48), zone plan v1: north-east of Route 13\'s fork', fill=(230, 230, 230), font=f)
    white = (236, 232, 214); gold = (214, 180, 90); wood = (150, 105, 70); roost = (170, 150, 120); yard = (200, 196, 180)
    box(d, 0, 0, W - 1, H - 1, C['snow'])
    # the massif's pinewood all round (no way round), the cliff behind the cathedral to the north
    box(d, 0, 0, 3, H - 1, C['pine']); box(d, W - 4, 0, W - 1, H - 1, C['pine']); box(d, 0, 0, W - 1, 3, C['cliff'])
    label(d, 14, 1.2, 'the massif rises behind (cliff, deep snow)', f, (230, 230, 230))
    # the approach from Route 13: the pilgrim road up through the pines
    box(d, 4, 38, 18, H - 1, C['pine']); box(d, 29, 38, 43, H - 1, C['pine'])
    path(d, [(23.5, H), (23.5, 42), (23.5, 36)], C['cobble'], 3)
    box(d, 22, H - 1, 25, H - 1, C['exitc']); label(d, 26, 45.3, 'from Route 13 (pilgrim road)', f)
    # the curtain wall with an open gate arch (guards, no hallway map)
    box(d, 4, 35, W - 5, 36, C['wall']); box(d, 21, 34, 26, 37, C['gate'])
    box(d, 23, 35, 24, 36, (20, 20, 26)); label(d, 27.5, 37.3, 'curtain wall: open gate arch, 2 guards', f, (20, 20, 20))
    # forecourt: Arceus statue
    box(d, 16, 27, 31, 33, yard); box(d, 22, 29, 25, 31, white); label(d, 16.3, 32.2, 'forecourt: Arceus statue', f)
    # the cathedral on its frozen moat island (white stone, gold: Arceus's colours, unlike Mirroh's dark chapel)
    box(d, 12, 5, 35, 24, C['ice']); box(d, 16, 6, 31, 21, C['snow2'])
    box(d, 18, 7, 29, 17, white); box(d, 18, 7, 29, 9, gold); box(d, 23, 17, 24, 17, (20, 20, 26))
    box(d, 22, 21, 25, 26, C['cobble']); label(d, 18.4, 12, 'CATHEDRAL', f); label(d, 18.4, 13, '(white & gold)', f)
    label(d, 12.3, 22.6, 'frozen moat', f); label(d, 26, 22.6, 'causeway', f)
    # west: the Tavern (the order runs them) and the barracks
    box(d, 5, 24, 10, 28, wood); box(d, 7, 28, 8, 28, (20, 20, 26)); label(d, 5.3, 25, 'TAVERN', f, (240, 240, 240))
    box(d, 5, 13, 10, 17, wood); box(d, 7, 17, 8, 17, (20, 20, 26)); label(d, 5.3, 14, 'barracks', f, (240, 240, 240))
    path(d, [(7.5, 29), (7.5, 31), (16, 31)], C['cobble'], 2); path(d, [(7.5, 18), (7.5, 29)], C['cobble'], 2)
    # east: the Braviary roost (the mount system): a tower and a landing yard
    box(d, 37, 11, 42, 16, roost); box(d, 38, 6, 41, 11, (130, 110, 90)); label(d, 37.3, 12.5, 'Braviary', f)
    label(d, 37.3, 13.5, 'roost +', f); label(d, 37.3, 14.5, 'landing', f)
    box(d, 37, 24, 42, 30, yard); label(d, 37.3, 26, 'training', f); label(d, 37.3, 27, 'yard', f)
    path(d, [(31, 30), (36.5, 30)], C['cobble'], 2); path(d, [(39.5, 17.5), (39.5, 24)], C['cobble'], 2)
    # east exit: Route 15 (a later chapter: closed by a Templar guard)
    path(d, [(42, 20), (W, 20)], C['cobble'], 2); box(d, W - 1, 19, W - 1, 21, C['exitc'])
    label(d, W + 0.3, 19.4, '-> Route 15 (later chapter:', f, (240, 240, 240)); label(d, W + 0.3, 20.4, '   a Templar guard turns you back)', f, (240, 240, 240))
    # legend
    lx = W + 0.6
    for i, (n, c) in enumerate((('snow', C['snow']), ('pinewood', C['pine']), ('cliff / massif', C['cliff']), ('cobbled road', C['cobble']),
                                ('frozen moat (ice)', C['ice']), ('curtain wall / gate', C['wall']), ('cathedral', white), ('timber chalet', wood),
                                ('Braviary roost', roost), ('yard / forecourt', yard), ('exit', C['exitc']))):
        box(d, lx, 26 + i * 1.4, lx + 1, 26 + i * 1.4 + 0.9, c); label(d, lx + 1.6, 26 + i * 1.4 - 0.05, n, f, (230, 230, 230))
    im.save(out)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/templar_hq_sketch_v1.png')
