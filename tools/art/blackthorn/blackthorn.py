"""The Bagon line's new shiny colours: black and crimson (user 2026-11-26; Glaive's Blackthorn, bible §7).
Writes graphics/pokemon/{bagon,shelgon,salamence}/shiny.pal and overworld_shiny.pal from the normal palettes' roles,
and a comparison sheet (normal / old shiny / new shiny; front, back, overworld).
Run: python3 tools/art/blackthorn/blackthorn.py [--write] [sheet.png]"""
import sys, os
import numpy as np
from PIL import Image, ImageDraw
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'codebase')
G = lambda m, f: os.path.join(C, 'graphics', 'pokemon', m, f)

# index -> new colour (indices not listed keep the normal colour)
FRONT = {
 'bagon': {1: (46, 44, 54), 2: (38, 22, 28), 3: (128, 122, 140), 4: (92, 88, 104), 6: (66, 62, 76),
           7: (28, 26, 32), 10: (44, 42, 50), 11: (64, 60, 72),
           8: (204, 40, 56), 9: (150, 26, 42), 12: (232, 232, 236), 13: (248, 248, 248), 14: (110, 30, 44), 15: (226, 110, 120)},
 'shelgon': {1: (40, 38, 46), 3: (104, 98, 114), 4: (72, 68, 82), 5: (54, 50, 62), 10: (60, 56, 66),
             6: (110, 24, 36), 7: (70, 16, 26), 8: (224, 224, 216), 9: (248, 248, 244),
             11: (220, 40, 56), 12: (100, 14, 28), 13: (248, 88, 96)},
 'salamence': {1: (70, 10, 20), 2: (220, 64, 76), 3: (176, 30, 46), 4: (126, 18, 34),
               6: (34, 32, 40), 7: (52, 48, 60), 8: (100, 94, 112), 9: (72, 68, 82),
               10: (78, 74, 88), 15: (108, 102, 120), 14: (54, 50, 62), 12: (60, 20, 28), 13: (120, 40, 56)},
}
OW = {
 'bagon': {1: (40, 38, 46), 2: (128, 122, 140), 3: (92, 88, 104), 5: (66, 62, 76), 6: (108, 102, 120),
           7: (204, 40, 56), 12: (120, 20, 34), 8: (44, 42, 50), 10: (58, 54, 66), 11: (72, 68, 82), 13: (28, 26, 32)},
 'shelgon': {1: (40, 38, 46), 3: (72, 68, 82), 4: (104, 98, 114), 5: (86, 80, 96), 6: (96, 90, 106),
             7: (54, 50, 62), 8: (46, 44, 54), 9: (200, 200, 204), 10: (240, 240, 236), 11: (200, 40, 56)},
 'salamence': {1: (70, 10, 20), 2: (220, 64, 76), 4: (150, 24, 40), 8: (180, 32, 48),
               5: (34, 32, 40), 7: (58, 54, 66), 9: (80, 76, 92), 6: (100, 94, 112),
               10: (78, 74, 88), 13: (54, 50, 62), 11: (108, 102, 120), 12: (40, 14, 22)},
}

# Bagon's eyes are drawn in the head plate's own whites (3, 4), so the shiny's dark head plate turned them grey:
#  - front: the small white patches under the head plate beside the black pupil;
#  - back: the light vertical strip at x 45-46, rows 21-26 (user 2026-11-26), and the light pixel at (48, 24) ringed
#    in black, at the head plate's edge.
# The yellow ring further down the back sprite, like the yellow patch on the front, is the PATTERN on the side of its
# face: crimson in the shiny (user 2026-11-26; it must not be white). The back sprite's fang is white in both.
# The eyes and fang get their own indices: 13 = white (normal: index 3's colour), 12 = light grey (normal: index 4's);
# the belly's few darkest pixels (old 12) merge into 9. The normal Bagon looks the same but for a few pixels.
# Boxes: (frame y offset, (x0, y0, x1, y1)).
FRONT_EYES = [(0, (26, 22, 31, 26)), (64, (20, 26, 25, 29))]
BACK_FANG, BACK_EYE, BACK_STRIP = (44, 29, 48, 33), (48, 24, 49, 25), (45, 21, 47, 27)
NORMAL_EYE = {12: (208, 200, 216), 13: (240, 240, 248)}

def box(shape, boxes):
    m = np.zeros(shape, bool)
    for y0, (x0, ya, x1, yb) in boxes: m[y0 + ya:y0 + yb, x0:x1] = True
    return m

def bagon_eyes(write):
    for f in ('anim_front.png', 'back.png'):
        p = G('bagon', f); im = Image.open(p); a = np.array(im); pal = im.getpalette()
        if not (a == 13).any():          # not yet done
            a[a == 12] = 9
            boxes = FRONT_EYES if f == 'anim_front.png' else [(0, BACK_FANG), (0, BACK_EYE), (0, BACK_STRIP)]
            m = box(a.shape, boxes)
            if f == 'back.png':
                a[box(a.shape, [(0, BACK_EYE)]) & (a == 4)] = 3          # the eye pixel: white
            white, grey = m & (a == 3), m & (a == 4)
            a[white] = 13; a[grey] = 12
        for i, c in NORMAL_EYE.items(): pal[3 * i:3 * i + 3] = list(c)
        if write:
            o = Image.fromarray(a, 'P'); o.putpalette(pal); o.save(p)
    if write:
        n = rd(G('bagon', 'normal.pal'))
        for i, c in NORMAL_EYE.items(): n[i] = c
        wr(G('bagon', 'normal.pal'), n)

def rd(p):
    L = open(p).read().split('\n'); return [tuple(int(v) for v in l.split()) for l in L[3:19] if l.strip()]
def wr(p, pal):
    open(p, 'w', newline='').write('JASC-PAL\r\n0100\r\n16\r\n' + ''.join('%d %d %d\r\n' % c for c in pal))
def newpal(base, m):
    return [m.get(i, c) for i, c in enumerate(base)]
def render(path, pal, crop=None, scale=3):
    a = np.array(Image.open(path))
    if crop: a = a[crop[1]:crop[3], crop[0]:crop[2]]
    rgb = np.array(pal, np.uint8)[a]; rgb[a == 0] = (236, 236, 228)
    return Image.fromarray(rgb).resize((a.shape[1] * scale, a.shape[0] * scale), 0)

if __name__ == '__main__':
    write = '--write' in sys.argv
    bagon_eyes(write)
    out = [x for x in sys.argv[1:] if x.endswith('.png')]
    rows = []
    for m in ('bagon', 'shelgon', 'salamence'):
        n, s0 = rd(G(m, 'normal.pal')), rd(G(m, 'shiny.pal'))
        on, os0 = rd(G(m, 'overworld_normal.pal')), rd(G(m, 'overworld_shiny.pal'))
        s1, os1 = newpal(n, FRONT[m]), newpal(on, OW[m])
        if write:
            wr(G(m, 'shiny.pal'), s1); wr(G(m, 'overworld_shiny.pal'), os1)
        cells = []
        for lab, P, OP in (('normal', n, on), ('old shiny', s0, os0), ('NEW shiny', s1, os1)):
            f = render(G(m, 'anim_front.png'), P, (0, 0, 64, 64)); b = render(G(m, 'back.png'), P)
            o = render(G(m, 'overworld.png'), OP, (0, 0, 32, 32), 3)
            c = Image.new('RGB', (192 * 2 + 100, 200), (236, 236, 228)); c.paste(f, (0, 8)); c.paste(b, (192, 8)); c.paste(o, (384, 40))
            ImageDraw.Draw(c).text((4, 0), '%s %s' % (m, lab), fill=(0, 0, 0)); cells.append(c)
        row = Image.new('RGB', (sum(c.width for c in cells), 200), (236, 236, 228))
        x = 0
        for c in cells: row.paste(c, (x, 0)); x += c.width
        rows.append(row)
    S = Image.new('RGB', (rows[0].width, 200 * len(rows)), (236, 236, 228))
    for k, r in enumerate(rows): S.paste(r, (0, 200 * k))
    S.save(out[0] if out else '/tmp/bt/blackthorn_v1.png'); print('sheet', S.size, 'written' if write else '')
