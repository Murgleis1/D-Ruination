"""Mirroh: zone plan (before any pixel art), user brief 2026-11-20: a walled city climbing the slope of the Mirroh
massif, a mix of a Crown village and MonoMyth's Fort Elderflower; light snow in the lower town, deeper uphill;
gothic, gloomy and wintry; the Necropolis on its own map uphill.
Usage: python3 tools/art/mirroh/layout_sketch.py out.png"""
import sys
from PIL import Image, ImageDraw, ImageFont
S = 14
C = dict(snow=(232, 236, 244), snow2=(214, 222, 236), snow3=(196, 206, 224), cobble=(150, 150, 165),
         wall=(92, 92, 112), wallhi=(120, 120, 140), stairs=(200, 200, 205), house=(70, 70, 92), roofthatch=(120, 105, 90),
         tavern=(150, 60, 60), shop=(60, 90, 150), chapel=(50, 45, 70), grave=(110, 110, 120), garden=(120, 140, 110),
         bone=(186, 176, 152), pine=(60, 90, 80), mtn=(170, 180, 200), road=(176, 170, 160), lantern=(240, 200, 90),
         fog=(200, 205, 215), keep=(60, 60, 80), water=(150, 180, 210), banner=(90, 40, 90))

def box(d, x0, y0, x1, y1, col, outline=None):
    d.rectangle([10 + x0 * S, 30 + y0 * S, 10 + (x1 + 1) * S - 1, 30 + (y1 + 1) * S - 1], fill=col, outline=outline)

def label(d, x, y, t, f, col=(0, 0, 0)):
    d.text((10 + x * S, 30 + y * S), t, fill=col, font=f)

def main(out):
    W, H = 60, 60
    im = Image.new('RGB', (W * S + 20, H * S + 40), (30, 30, 36)); d = ImageDraw.Draw(im)
    try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
    except Exception: f = ImageFont.load_default()
    d.text((10, 8), 'MIRROH (about 60x60): a walled city climbing the massif; light snow below, deep snow above; '
           'gothic, gloomy, wintry', fill=(230, 230, 230), font=f)
    # the mountain all round, snow deepening upward
    box(d, 0, 0, W - 1, H - 1, C['snow3'])
    box(d, 0, 20, W - 1, H - 1, C['snow2']); box(d, 0, 38, W - 1, H - 1, C['snow'])
    # outside the south gate: Hollow Hill's bone woods (the seam), thinning into snowy pines
    box(d, 0, 52, W - 1, H - 1, C['bone']); box(d, 0, 52, 22, H - 1, C['pine']); box(d, 37, 52, W - 1, H - 1, C['pine'])
    box(d, 26, 52, 33, H - 1, C['road']); label(d, 24, 57, 'from Hollow Hill', f)
    # the city walls (Elderflower): crenellated terrace walls that jog with the slope, stairs staggered so the way
    # winds up through the town; the gatehouse south
    box(d, 5, 49, 53, 51, C['wall']); box(d, 27, 49, 32, 51, C['keep']); label(d, 27, 50, 'south gate', f, (255, 255, 255))
    box(d, 24, 49, 25, 49, C['banner']); box(d, 34, 49, 35, 49, C['banner'])
    box(d, 5, 22, 6, 49, C['wall']); box(d, 53, 12, 54, 49, C['wall']); box(d, 7, 12, 8, 21, C['wall'])
    # lower town (light snow): cottages with fenced gardens (Crown village), a well, lanterns; the street bends east
    box(d, 7, 37, 52, 48, C['snow'])
    for x0, y0 in ((9, 39), (16, 41), (43, 39), (47, 43), (22, 44)): box(d, x0, y0, x0 + 4, y0 + 3, C['roofthatch'])
    for x0, y0 in ((9, 44), (16, 46), (42, 45)): box(d, x0, y0, x0 + 4, y0 + 1, C['garden'], outline=(90, 70, 50))
    box(d, 28, 40, 31, 48, C['cobble']); box(d, 28, 38, 41, 40, C['cobble']); box(d, 33, 43, 34, 44, C['water']); label(d, 35, 43, 'well', f)
    label(d, 8, 37, 'cottages + gardens', f)
    # terrace wall (jogging) with the stairs at its east end
    box(d, 7, 35, 30, 36, C['wall']); box(d, 31, 34, 52, 35, C['wall']); box(d, 40, 34, 41, 35, C['stairs'])
    # middle terrace: the square west of the stairs: the Tavern (Pokemon Center), the market hall, stalls, a frozen fountain
    box(d, 9, 20, 52, 34, C['snow2']); box(d, 16, 23, 41, 33, C['cobble'])
    box(d, 9, 22, 15, 27, C['tavern']); label(d, 9, 28, 'Tavern', f)
    box(d, 44, 22, 51, 27, C['shop']); label(d, 44, 28, 'market hall', f)
    for x0 in (18, 22, 34, 38): box(d, x0, 30, x0 + 1, 31, (160, 120, 80))
    box(d, 26, 25, 29, 28, C['water']); label(d, 24, 24, 'frozen fountain', f)
    box(d, 9, 30, 14, 33, C['house']); box(d, 45, 30, 51, 33, C['house'])
    # terrace wall with the stairs at its west end
    box(d, 9, 18, 31, 19, C['wall']); box(d, 32, 19, 52, 20, C['wall']); box(d, 17, 18, 18, 19, C['stairs'])
    # upper terrace (deep snow): the gothic chapel and its graveyard; a tall manor (House Langerin's town house?)
    box(d, 9, 9, 52, 17, C['snow3'])
    box(d, 10, 10, 17, 16, C['chapel']); label(d, 10, 9, 'gothic chapel', f, (40, 40, 60))
    box(d, 19, 12, 26, 16, C['grave']); label(d, 19, 11, 'graveyard', f, (40, 40, 60))
    box(d, 40, 10, 50, 16, C['house']); label(d, 40, 9, 'Langerin town house?', f, (40, 40, 60))
    # the keep gate north (east of centre): the road up to the Necropolis (its own map) and the mountain
    box(d, 7, 6, 54, 8, C['wall']); box(d, 31, 6, 36, 8, C['keep']); label(d, 31, 7, 'north gate', f, (255, 255, 255))
    box(d, 32, 0, 35, 5, C['road']); label(d, 37, 1, 'up to the Necropolis, the Templar Citadel, Mt. Mirroh', f)
    # the way through: south gate -> street bending east -> stairs -> the square -> west stairs -> past the chapel
    for (x0, y0, x1, y1) in ((30, 52, 30, 39), (30, 39, 40, 39), (40, 39, 40, 33), (40, 33, 18, 29), (18, 29, 18, 17),
                             (18, 17, 33, 13), (33, 13, 33, 6)):
        d.line([10 + x0 * S + 7, 30 + y0 * S + 7, 10 + x1 * S + 7, 30 + y1 * S + 7], fill=(200, 40, 40), width=2)
    label(d, 42, 37, 'the way up', f, (200, 40, 40))
    # lanterns along the streets
    for x, y in ((27, 41), (32, 46), (37, 38), (16, 24), (41, 24), (16, 32), (41, 32), (27, 14), (36, 12)):
        box(d, x, y, x, y, C['lantern'])
    # fog low over the lower town
    im.save(out); print(out)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/mirroh/mirroh_sketch.png')
