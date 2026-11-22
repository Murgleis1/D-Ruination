"""Route 13: zone plan (before any pixel art). User 2026-11-22: Route 13 runs north from Mirroh's north-west gatehouse
and FORKS: one branch climbs to Mt. Mirroh, a side branch leads to Templar Headquarters ("Templar Citadel").
On the slopes of the Mirroh massif: snowy pinewood, rock, snow deepening uphill.
Usage: python3 tools/art/route13/layout_sketch.py out.png"""
import sys
from PIL import Image, ImageDraw, ImageFont
S = 14
C = dict(snow=(232, 236, 244), snow2=(214, 222, 236), snow3=(196, 206, 224), pine=(60, 90, 80), rock=(118, 116, 124),
         cliff=(84, 82, 92), ledge=(150, 140, 120), trail=(176, 166, 150), cobble=(150, 150, 165), grass=(120, 150, 130),
         ice=(170, 200, 230), wall=(92, 92, 112), gate=(70, 70, 92), shrine=(220, 200, 120), sign=(150, 110, 70),
         exitc=(240, 120, 90))

def box(d, x0, y0, x1, y1, col, outline=None):
    d.rectangle([10 + x0 * S, 30 + y0 * S, 10 + (x1 + 1) * S - 1, 30 + (y1 + 1) * S - 1], fill=col, outline=outline)

def ell(d, x0, y0, x1, y1, col):
    d.ellipse([10 + x0 * S, 30 + y0 * S, 10 + (x1 + 1) * S - 1, 30 + (y1 + 1) * S - 1], fill=col)

def path(d, pts, col, w):
    d.line([(10 + x * S + S // 2, 30 + y * S + S // 2) for x, y in pts], fill=col, width=w * S, joint='curve')

def label(d, x, y, t, f, col=(0, 0, 0)):
    d.text((10 + x * S, 30 + y * S), t, fill=col, font=f)

def main(out):
    W, H = 40, 64
    im = Image.new('RGB', (W * S + 20 + 300, H * S + 40), (30, 30, 36)); d = ImageDraw.Draw(im)
    try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
    except Exception: f = ImageFont.load_default()
    d.text((10, 8), 'ROUTE 13 (40x64): north from Mirroh; forks to Mt. Mirroh (NW) and Templar HQ (NE)', fill=(230, 230, 230), font=f)
    # snow deepening uphill
    box(d, 0, 0, W - 1, H - 1, C['snow3']); box(d, 0, 22, W - 1, H - 1, C['snow2']); box(d, 0, 44, W - 1, H - 1, C['snow'])
    # pinewood flanks all the way (no way round), thicker low down
    box(d, 0, 0, 3, H - 1, C['pine']); box(d, W - 4, 0, W - 1, H - 1, C['pine'])
    box(d, 4, 46, 7, 57, C['pine']); box(d, 32, 50, 35, 57, C['pine'])
    # Mirroh's north wall and the NW gatehouse's north face (you step out of its north door)
    box(d, 0, 59, W - 1, H - 1, C['wall']); box(d, 13, 56, 26, H - 1, C['gate'])
    box(d, 19, 61, 20, 62, (20, 20, 26)); label(d, 13.4, 57.2, 'NW gatehouse', f, (230, 230, 230)); label(d, 13.4, 58.1, '(north face)', f, (230, 230, 230))
    # the massif's spur between the branches (impassable): rock and cliffs, deep snow
    pts = [(14, 0), (26, 0), (25, 8), (22, 15), (19, 20)]
    d.polygon([(10 + x * S, 30 + y * S) for x, y in pts], fill=C['cliff'])
    box(d, 15, 0, 24, 5, C['rock']); label(d, 15.2, 2, 'the massif\'s spur', f, (230, 230, 230))
    # rock ledge band (one-way jumps down) for the switchback
    for x in range(8, 30): box(d, x, 44, x, 44, C['ledge'])
    box(d, 24, 44, 26, 44, C['trail'])                                   # (the trail's gap up through it)
    # snowy tall grass (wild encounters, stage 5)
    for (x0, y0, x1, y1) in ((8, 50, 13, 55), (27, 46, 31, 49), (9, 38, 13, 42), (28, 31, 33, 36), (6, 12, 10, 17), (29, 14, 33, 18)):
        box(d, x0, y0, x1, y1, C['grass'])
    # the frozen tarn (reflecting ice, Ghost Grey's)
    ell(d, 5, 28, 15, 36, C['ice']); label(d, 7, 31.5, 'frozen tarn', f)
    # the road: out of the gate, switchback round the ledges, up the tarn's east shore to the fork
    path(d, [(19.5, 58), (19.5, 52), (16, 48), (25, 45.5), (25, 42), (20, 38), (19, 32), (19.5, 26)], C['trail'], 2)
    # the fork plateau: Templar waystone + signpost
    ell(d, 14, 21, 25, 28, C['snow'])
    box(d, 19, 23, 20, 24, C['shrine']); box(d, 22, 25, 22, 25, C['sign'])
    label(d, 26, 22.3, 'THE FORK: Templar waystone', f, (240, 240, 240)); label(d, 26, 23.3, '(Arceus marker) + signpost', f, (240, 240, 240))
    # NE branch: the Templars' cobbled pilgrim road to Templar HQ
    path(d, [(21, 24), (27, 21), (30, 16), (32, 10), (33, 4), (33.5, 0)], C['cobble'], 2)
    box(d, 32, 0, 35, 0, C['exitc']); label(d, 24.5, 6.5, 'cobbled pilgrim road', f, (240, 240, 240))
    label(d, 30.5, 1.2, '-> Templar HQ', f, (30, 30, 30))
    # NW branch: the rough mountain trail up rocky steps to Mt. Mirroh
    path(d, [(18, 24), (13, 21), (10, 16), (8, 10), (9, 5), (8.5, 0)], C['trail'], 2)
    for y in (17, 9): box(d, 8, y, 11, y, C['ledge'])                     # (rock steps)
    box(d, 7, 0, 10, 0, C['exitc']); label(d, 4, 6.5, 'rough trail,', f); label(d, 4, 7.4, 'rock steps', f)
    label(d, 4.3, 1.2, '-> Mt. Mirroh', f, (30, 30, 30))
    # legend
    lx = W * S + 30; ly = 40
    for i, (k, t) in enumerate((('snow', 'light snow (low)'), ('snow2', 'snow'), ('snow3', 'deep snow (high)'), ('pine', 'snowy pinewood (solid)'),
                                ('cliff', 'cliff / massif (solid)'), ('rock', 'rock'), ('ledge', 'rock ledges / steps (jump down)'),
                                ('grass', 'snowy tall grass'), ('ice', 'frozen tarn (reflecting)'), ('trail', 'rough trail'),
                                ('cobble', 'Templar cobbled road'), ('shrine', 'Templar waystone'), ('exitc', 'exit (closed for now)'))):
        d.rectangle([lx, ly + i * 20, lx + 14, ly + i * 20 + 14], fill=C[k]); d.text((lx + 22, ly + i * 20), t, fill=(230, 230, 230), font=f)
    im.save(out)

def main_v2(out):
    """v2 (user 2026-11-22: too short; flesh it out after MonoMyth's northern routes): about 40x104, terraced climbs
    with stone stairs, real pine forests with clearings, a high meadow with the tarn, more mountain clutter."""
    W, H = 40, 104
    im = Image.new('RGB', (W * S + 20 + 330, H * S + 40), (30, 30, 36)); d = ImageDraw.Draw(im)
    try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
    except Exception: f = ImageFont.load_default()
    d.text((10, 8), 'ROUTE 13 v2 (40x104): terraces + stairs, forests + clearings, after MonoMyth Routes 17/20/22/23', fill=(230, 230, 230), font=f)
    box(d, 0, 0, W - 1, H - 1, C['snow3']); box(d, 0, 40, W - 1, H - 1, C['snow2']); box(d, 0, 76, W - 1, H - 1, C['snow'])
    def terr(y0, n, x0, x1, gap, step=1):                            # (contour walls stepping up, a stair through)
        for k in range(n):
            y = y0 - k * 2 * step
            for x in range(x0, x1 + 1):
                if not (gap[0] <= x <= gap[1]): box(d, x, y, x, y, C['cliff'])
            box(d, gap[0], y, gap[1], y, (200, 200, 205))
    # foot + the first forest
    box(d, 0, 101, W - 1, H - 1, C['wall']); box(d, 19, 102, 20, 103, (20, 20, 26))
    box(d, 0, 78, 13, 100, C['pine']); box(d, 27, 76, W - 1, 100, C['pine']); box(d, 14, 92, 17, 97, C['pine'])
    box(d, 16, 84, 23, 90, C['snow']); box(d, 18, 85, 22, 89, C['grass']); label(d, 15.5, 82.6, 'forest clearing', f, (230, 230, 230))
    box(d, 4, 86, 8, 89, C['snow']); label(d, 3.2, 85.0, 'glade', f, (230, 230, 230))
    # first terraces
    terr(75, 4, 0, W - 1, (18, 20)); label(d, 22, 69.2, 'terraces I: 4 tiers, stone stair', f, (240, 240, 240))
    box(d, 2, 66, 8, 69, C['grass']); box(d, 30, 64, 35, 68, C['grass'])
    # the high meadow and the tarn
    ell(d, 5, 52, 16, 60, C['ice']); label(d, 7.5, 55.5, 'frozen tarn', f)
    box(d, 24, 50, 30, 55, C['grass']); box(d, 20, 58, 22, 59, C['rock']); box(d, 31, 58, 33, 59, C['rock'])
    label(d, 22, 60.3, 'high meadow: boulders, rock arches,', f); label(d, 22, 61.3, 'frozen puddles', f)
    box(d, 0, 44, 3, 63, C['pine']); box(d, 35, 44, W - 1, 63, C['pine'])
    # second terraces (switchback stairs)
    terr(43, 3, 0, 23, (6, 8)); terr(43, 3, 24, W - 1, (30, 32), step=1)
    label(d, 9.5, 37.3, 'terraces II: switchback stairs', f, (240, 240, 240))
    # the fork plateau
    ell(d, 12, 26, 28, 34, C['snow']); box(d, 19, 28, 19, 29, C['shrine']); box(d, 22, 31, 22, 31, C['sign'])
    label(d, 26.5, 26.4, 'THE FORK: waystone + sign', f, (240, 240, 240))
    # branches
    path(d, [(21, 30), (27, 25), (30, 18), (32, 10), (33, 3), (33, 0)], C['cobble'], 2)
    box(d, 27, 12, 36, 20, C['pine']); box(d, 36, 0, W - 1, 30, C['pine']); box(d, 28, 4, 31, 8, C['grass'])
    label(d, 24, 21.5, 'pilgrim road through', f, (240, 240, 240)); label(d, 24, 22.5, 'a pinewood to HQ', f, (240, 240, 240))
    path(d, [(18, 30), (13, 26), (10, 20), (8, 12), (8, 0)], C['trail'], 2)
    terr(22, 6, 0, 12, (7, 9)); box(d, 0, 0, 2, 30, C['pine'])
    label(d, 0.5, 4, 'steep terraces,', f, (240, 240, 240)); label(d, 0.5, 5, 'stairs: Mt. Mirroh', f, (240, 240, 240))
    pts = [(14, 0), (27, 0), (24, 10), (20, 22)]
    d.polygon([(10 + x * S, 30 + y * S) for x, y in pts], fill=C['pine']); label(d, 16, 6, 'the spur', f, (230, 230, 230))
    box(d, 7, 0, 10, 0, C['exitc']); box(d, 32, 0, 35, 0, C['exitc'])
    lx = W * S + 30; ly = 40
    for i, (k, t) in enumerate((('snow', 'light snow (low)'), ('snow2', 'snow'), ('snow3', 'deep snow (high)'), ('pine', 'pine forest (solid)'),
                                ('cliff', 'terrace rock walls (tiers)'), ('rock', 'boulders / rock arches'),
                                ('grass', "tall grass (MonoMyth's ice grass)"), ('ice', 'frozen tarn'), ('trail', 'rough trail'),
                                ('cobble', 'Templar pilgrim road'), ('shrine', 'Templar waystone'), ('exitc', 'exit (closed for now)'))):
        d.rectangle([lx, ly + i * 20, lx + 14, ly + i * 20 + 14], fill=C[k]); d.text((lx + 22, ly + i * 20), t, fill=(230, 230, 230), font=f)
    d.rectangle([lx, ly + 260, lx + 14, ly + 274], fill=(200, 200, 205)); d.text((lx + 22, ly + 260), 'stone stairs', fill=(230, 230, 230), font=f)
    im.save(out)

if __name__ == '__main__':
    if sys.argv[1:2] == ['v2']: main_v2(sys.argv[2])
    else: main(sys.argv[1] if len(sys.argv) > 1 else '/tmp/route13_sketch.png')
