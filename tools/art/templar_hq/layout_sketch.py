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

def main_v2(out):
    """v2 (user 2026-11-22): the Citadel stands in a STONE HOLLOW of the Mirroh mountains, an open courtyard before
    the church with Templars standing in it; the ground stony with touches of snow (Fort Elderflower's paving); the
    church is Pokemon Empire's Arceus church, its front building only, 7x13 at native size, drawn here as it is."""
    W, H = 40, 40
    im = Image.new('RGB', (W * S + 20 + 330, H * S + 40), (30, 30, 36)); d = ImageDraw.Draw(im)
    try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
    except Exception: f = ImageFont.load_default()
    d.text((10, 8), 'TEMPLAR CITADEL (40x40), zone plan v2: a courtyard in a stone hollow', fill=(230, 230, 230), font=f)
    stone = (128, 128, 140); stone2 = (110, 110, 124); rockc = (84, 82, 92); wood = (150, 105, 70); roost = (170, 150, 120)
    yard = (150, 150, 162); tmpl = (230, 200, 80)
    box(d, 0, 0, W - 1, H - 1, stone)
    for (x0, y0, x1, y1) in ((4, 30, 6, 31), (31, 18, 34, 19), (9, 16, 11, 17), (25, 27, 27, 28), (13, 29, 14, 30)):
        box(d, x0, y0, x1, y1, C['snow'])                                  # (touches of snow on the stone)
    # the hollow's rock walls (terraced cliffs), the massif rising behind
    box(d, 0, 0, W - 1, 2, rockc); box(d, 0, 0, 3, H - 1, rockc); box(d, W - 4, 0, W - 1, H - 1, rockc)
    box(d, 4, 3, 7, 5, stone2); box(d, 32, 3, 35, 5, stone2)               # (a ledge step at the back corners)
    label(d, 12, 0.8, 'the massif: the hollow\'s rock walls rise all round', f, (230, 230, 230))
    # the mouth: curtain wall with its open arch, two guards; the pilgrim road down to Route 13
    box(d, 4, 33, W - 5, 34, C['wall']); box(d, 17, 32, 22, 35, C['gate']); box(d, 18, 33, 21, 34, (20, 20, 26))
    for gx in (16, 23): box(d, gx, 35, gx, 35, tmpl)
    box(d, 0, 35, 16, H - 1, rockc); box(d, 23, 35, W - 1, H - 1, rockc)
    path(d, [(19.5, H), (19.5, 35)], C['cobble'], 4); box(d, 18, H - 1, 21, H - 1, C['exitc'])
    label(d, 23.5, 36.2, 'curtain wall, open arch, 2 guards', f, (240, 240, 240)); label(d, 23.5, 38.2, 'from Route 13 (pilgrim road)', f, (240, 240, 240))
    # the courtyard: the cobbled way to the church door, the Arceus statue, Templars standing about
    path(d, [(19.5, 32), (19.5, 19)], C['cobble'], 3)
    box(d, 17, 24, 22, 27, yard); box(d, 19, 25, 20, 26, (236, 232, 214)); label(d, 13.2, 23.0, 'Arceus statue', f)
    for (tx, ty) in ((15, 22), (24, 22), (14, 28), (25, 29), (11, 25)): box(d, tx, ty, tx, ty, tmpl)
    label(d, W + 0.3, 9.4, 'gold squares: Templars standing', f, (240, 240, 240)); label(d, W + 0.3, 10.4, 'in the courtyard (stage 2)', f, (240, 240, 240))
    # the church, as drawn, on a narrow frozen moat with a causeway to its door
    box(d, 14, 3, 25, 17, C['ice']); box(d, 18, 16, 21, 18, C['cobble'])
    ch = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'church', 'front_arceus.png')).convert('RGBA')
    ch = ch.resize((ch.size[0] * S // 16, ch.size[1] * S // 16), Image.LANCZOS)
    im.paste(ch, (10 + 16 * S, 30 + 3 * S + S // 2), ch)
    label(d, W + 0.3, 4.4, 'the church (7x13), on a frozen', f, (240, 240, 240)); label(d, W + 0.3, 5.4, 'moat; its door at the foot.', f, (240, 240, 240)); label(d, W + 0.3, 6.4, 'Inside, Loulan leads you', f, (240, 240, 240)); label(d, W + 0.3, 7.4, 'to Ambrose at its heart.', f, (240, 240, 240))
    # west: the Tavern and the barracks, doors onto the courtyard
    box(d, 5, 19, 10, 23, wood); box(d, 7, 23, 8, 23, (20, 20, 26)); label(d, 5.6, 20.6, 'Tavern', f, (240, 240, 240))
    box(d, 5, 8, 10, 12, wood); box(d, 7, 12, 8, 12, (20, 20, 26)); label(d, 5.3, 9.6, 'barracks', f, (240, 240, 240))
    path(d, [(7.5, 24), (7.5, 30), (17, 30)], C['cobble'], 2); path(d, [(7.5, 13), (7.5, 24)], C['cobble'], 2)
    # east: the Braviary roost up on a ledge (stairs), the training yard below
    box(d, 28, 6, 35, 12, stone2); box(d, 29, 7, 34, 11, roost); box(d, 30, 13, 31, 13, C['trail'])
    label(d, 29.3, 8.2, 'Braviary', f); label(d, 29.3, 9.2, 'roost', f); label(d, 29.3, 10.2, '(on a ledge)', f)
    box(d, 27, 21, 34, 28, yard); label(d, 27.6, 22.2, 'training yard', f)
    path(d, [(22, 30), (30.5, 30), (30.5, 28.5)], C['cobble'], 2); path(d, [(30.5, 21), (30.5, 13.5)], C['cobble'], 2)
    # east: the cleft to Route 15 (a later chapter: a Templar turns you back)
    box(d, W - 4, 15, W - 1, 17, stone); path(d, [(35, 16), (W, 16)], C['cobble'], 2); box(d, W - 1, 15, W - 1, 17, C['exitc'])
    box(d, 35, 15, 35, 15, tmpl); label(d, W + 0.3, 15.4, '-> Route 15 (later chapter:', f, (240, 240, 240)); label(d, W + 0.3, 16.4, '   a Templar turns you back)', f, (240, 240, 240))
    lx = W + 0.6
    for i, (n, c) in enumerate((('stone paving', stone), ('snow touches', C['snow']), ('rock (hollow walls)', rockc), ('ledge', stone2),
                                ('cobbled way', C['cobble']), ('frozen moat', C['ice']), ('curtain wall / gate', C['wall']),
                                ('timber building', wood), ('Braviary roost', roost), ('yard', yard), ('Templar', tmpl), ('exit', C['exitc']))):
        box(d, lx, 21 + i * 1.4, lx + 1, 21 + i * 1.4 + 0.9, c); label(d, lx + 1.6, 21 + i * 1.4 - 0.05, n, f, (230, 230, 230))
    im.save(out)

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[2] == 'v2': main_v2(sys.argv[1]); sys.exit()
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/templar_hq_sketch_v1.png')
