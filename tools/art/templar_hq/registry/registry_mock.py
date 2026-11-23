"""The Braviary registry, mock v1, to floor plan v1 (registry_plan.py; user 2026-11-23 with additions: Rufflet chicks
and eggs, "to show that new Rufflets and Braviaries are often born or evolve here"; the clerk's desk is House
Raptora's liaison's).  16x12 tiles: wall rows 0-1 (cream), panelling row 2, cream marble rows 3-10, the door from the
nave at the bottom centre (row 11, x 7-8). The study's room materials.
- Back wall: the map of Cormoria (the game's own parchment region map, tools/region_map, scaled into a wooden frame)
  in the middle; ledger shelves either side (Crown 7.9's bookcases); at the west end the dispatch cabinets, two tall
  cabinets of pigeonholed orders for every Tavern (Odyssey 11.8's).
- The registrar's counter across the room (MonoMyth's bar counter, shortened, in Crown's wood): behind it, staff only.
- West: House Raptora's liaison's desk (MonoMyth's writing desk, a chair before it), watching the logs.
- East, the nursery, their place (user: more of them): three Braviaries each resting on a bed of straw, two straw
  nests with five eggs, Rufflet chicks among them, straw for feed (MonoMyth's stable straw; the game's own Rufflet and Braviary overworld sprites and the Egg's
  icon). No candle on this side (hay).
- By the door: three stools where Templars wait their turn (MonoMyth's bar stools); a candelabra in the south-west
  corner.
(Plan changes: the dispatch rack stands against the back wall instead of along the west side, so nothing stands
loose in the room; no source has a bird perch, so the Braviary rests on straw.)
Credits: Pokemon Crown, MonoMyth, Odyssey.  Usage: python3 registry_mock.py OUT.png"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(HERE, '..', 'study')); sys.path.insert(0, os.path.join(HERE, '..', 'bishops'))
from cutter import load, cell, cut, T
import study_mock as SM
import hall_mock as HM
W, H = 16, 13
GFX = os.path.join(REPO, 'codebase', 'graphics', 'pokemon')

def sprite(path, frame=0, size=32):
    im = Image.open(path); idx = np.array(im); a = np.array(im.convert('RGBA')).astype(int)
    f = a[:size, frame * size:(frame + 1) * size].copy()
    f[..., 3] = np.where(idx[:size, frame * size:(frame + 1) * size] == 0, 0, 255)
    return f

def wall_map(w=70, h=44):
    """The game's parchment region map, scaled into a dark-wood frame (w x h inside, +2 px frame)."""
    sys.path.insert(0, os.path.join(REPO, 'tools', 'region_map'))
    import export, paint
    idx, pal = export.painted()
    a = paint.to_rgb(idx, pal)
    m = Image.fromarray(a.astype(np.uint8)).crop((6, 6, 234, 150)).resize((w, h), Image.BOX)
    m = m.quantize(15, dither=Image.Dither.NONE).convert('RGB')
    out = np.zeros((h + 4, w + 4, 4), int); out[..., 3] = 255
    out[..., :3] = (64, 40, 32); out[1:-1, 1:-1, :3] = (128, 80, 56)
    out[2:-2, 2:-2, :3] = np.array(m)
    return out

def pieces():
    P, c79 = HM.pieces()
    st = load(os.path.join(HERE, 'mm_stable.png')); bar = load(os.path.join(HERE, 'mm_bar.png'))
    o = load(os.path.join(HERE, 'ody_118.png'))
    stfl = [(x, y) for x in (5, 6, 8, 9, 10) for y in (6, 7, 8)] + [(3, 3), (4, 3), (14, 5)]
    P['strawbed'] = cut(st, 1, 5, 2, 2, stfl)
    P['nest'] = cut(st, 13, 7, 2, 2, stfl)
    P['strawsmall'] = cut(st, 2, 3, 1, 1, stfl)
    barfl = [(x, y) for x in (8, 9, 10, 11) for y in (5, 6, 7)] + [(x, 2) for x in (8, 9, 10)]
    c = cut(bar, 4, 2, 14, 3, barfl)[14:42]                  # (its top and front face; the stools left out)
    c = c[:, list(range(0, 20)) + [100] * (10 * T - 40) + list(range(204, 224))]  # (shortened to 10 tiles)
    HM.tone(c); P['counter'] = c
    warm = {tuple(p) for x, y in barfl for p in cell(bar, x, y).reshape(-1, 3) if p[0] > p[2] + 6}
    P['stool'] = cut(bar, 4, 6, 1, 1, barfl, bgcols=[(6, warm)])   # (grey stool; the bar's floor is warm brown)
    ofl = [(x, y) for x in (1, 2, 3, 4, 5, 6) for y in (7, 8)]
    owall = {tuple(p) for p in o[0:32, 96:112].reshape(-1, 3)} | {tuple(p) for p in o[0:32, 64:80].reshape(-1, 3)}
    cab = cut(o, 5, 0, 1, 3, ofl + [(6, 2), (4, 2)], bgcols=[(0, owall), (1, owall)])
    ofloor = {tuple(p) for x, y in ofl for p in cell(o, x, y).reshape(-1, 3)}
    cab[37:, :, 3] = 0                                        # (its feet end at y 36; below is Odyssey's floor)
    P['cabinet'] = cab
    P['rufflet'] = sprite(os.path.join(GFX, 'rufflet', 'overworld.png'), 0)
    rl = sprite(os.path.join(GFX, 'rufflet', 'overworld.png'), 4)   # (frames: 0-1 down, 2-3 up, 4-5 left)
    P['rufflet_l'] = rl; P['rufflet_r'] = rl[:, ::-1].copy()
    P['egg'] = sprite(os.path.join(GFX, 'egg', 'icon.png'), 0)
    P['braviary_l'] = np.array(Image.open(os.path.join(HERE, '..', 'yard', 'braviary_left.png')).convert('RGBA')).astype(int)
    P['braviary'] = np.array(Image.open(os.path.join(HERE, '..', 'yard', 'braviary_down.png')).convert('RGBA')).astype(int)
    import parchment_map as PMAP
    P['map'] = PMAP.scroll(80, 53)                            # (user's illustrated map, as parchment, hung as a scroll)
    return P, c79

def put(img, p, x, y):
    """Paste at pixel position."""
    h, w = p.shape[:2]; m = p[..., 3] > 0
    img[y:y + h, x:x + w][m] = p[..., :3][m]

def centre(p):
    ys, xs = np.nonzero(p[..., 3] > 0); return (ys.min() + ys.max()) / 2, (xs.min() + xs.max()) / 2

def main(out):
    P, c79 = pieces()
    img = np.zeros((H * T, W * T, 3), int)
    for x in range(1, W - 1):                                 # wall: wallpaper rows 0-2, panelling row 3
        img[0:2 * T, x * T:(x + 1) * T] = c79[0:2 * T, 3 * T:4 * T]
        img[2 * T:3 * T, x * T:(x + 1) * T] = c79[T:2 * T, 3 * T:4 * T]
        img[3 * T:4 * T, x * T:(x + 1) * T] = cell(c79, 3, 2)
        for y in range(4, H - 1):
            src = (5, 3) if y == 4 else (1, 4) if x == 1 else (3, 6)
            img[y * T:(y + 1) * T, x * T:(x + 1) * T] = cell(c79, *src)
    rows = np.arange(H * T)[:, None].repeat(W * T, 1)
    SM.recolour(img, SM.WALL, rows < 3 * T)
    img[(H - 1) * T:H * T, 7 * T:9 * T] = c79[8 * T:9 * T, 4 * T:6 * T]
    SM.recolour(img, SM.MAT, rows >= (H - 1) * T)
    # the staff wall: the map between two ledger bookcases, the counter before them
    mp = P['map']; put(img, mp, 8 * T - mp.shape[1] // 2, 1)
    SM.paste(img, P['bookcase'], 3, 3); SM.paste(img, P['bookcase'], 11, 3)
    put(img, P['counter'], 3 * T, 6 * T - 6)
    # west corner: House Raptora's liaison, at a desk against the wall
    SM.paste(img, P['desk'], 1, 3); SM.paste(img, P['chairL'], 1, 5)
    # east: the nursery, their place (user 2026-11-23: more of them): three Braviaries each on a bed of straw, two
    # nests with five eggs, Rufflet chicks among them, feed straw; the walkway from the door (x 7-8) left clear
    def bed(x, y, bird):
        SM.paste(img, P['strawbed'], x, y); put(img, bird, x * T, y * T - 10)
    def nest(x, y, n):
        SM.paste(img, P['nest'], x, y)
        ny, nx = centre(P['nest']); ey, ex = centre(P['egg'])
        offs = {2: [(-5, 0), (5, 0)], 3: [(-7, 1), (0, -3), (7, 1)]}[n]
        for dx, dy in offs: put(img, P['egg'], int(x * T + nx - ex + dx), int(y * T + ny - ey - 3 + dy))
    bed(13, 4, P['braviary'])
    nest(11, 7, 3); nest(13, 7, 2)
    bed(10, 9, P['braviary_l'])
    bed(13, 10, P['braviary'])
    SM.paste(img, P['strawsmall'], 9, 8); SM.paste(img, P['strawsmall'], 12, 11)
    put(img, P['rufflet_l'], 12 * T + 2, 5 * T + 6)
    put(img, P['rufflet_r'], 9 * T + 2, 7 * T - 10)
    put(img, P['rufflet_r'], 11 * T - 6, 11 * T - 10)                   # (by the feed straw, clear of the birds)
    # by the door
    for x in (3, 4, 5): SM.paste(img, P['stool'], x, 11)
    SM.paste(img, P['candelabra'], 1, 10)
    o = Image.fromarray(img.astype(np.uint8)); o.save(out)
    o.resize((W * T * 3, H * T * 3), Image.NEAREST).save(out.replace('.png', '_3x.png'))

if __name__ == '__main__':
    main(sys.argv[1])
