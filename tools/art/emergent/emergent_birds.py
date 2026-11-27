"""Emergent Rufflet / Emergent Braviary art (bible §16.6 item 12; user 2026-11-27: copy the real sprites and recolour
them to a striking black and white).

Design
  * Rufflet: the head fluff, crest and tail go white; the face mask and body ruff go black, so the white head carries a
    black bandit mask (Dark type); the crest's red stripe becomes a black slash on a white feather.
  * Braviary: patterned on the Steller's sea eagle: a black body and wings with the red parts (the wing's leading
    edge and the shoulders) turned to bold white flashes, the head white; the blue tail band a steel grey.
  * Both keep the yellow beak and talons: the only colour on the bird, so it reads at a glance.
  * The whites are shaded cool (lavender-grey), the blacks lifted with a steel-blue highlight, so neither reads flat.
  * Shiny (user 2026-11-27): silver and dark blue (the first idea, black and white swapped, looked strange).

Every original palette index is given a role: ('W', k) white ramp level k, ('B', k) black ramp level k, or a fixed
colour (yellow, outline, eye white). The pixel data is copied unchanged, except where one index has to be split
(Rufflet's index 4 is both the crest and the eye whites: the eyes move to a free index that stays white in the shiny).
Run: python3 emergent_birds.py [--write]   (preview to /tmp/ef/emergent_preview.png)
"""
import os, sys
import numpy as np
from PIL import Image

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'codebase', 'graphics', 'pokemon')

W = [(244, 244, 250), (206, 208, 224), (156, 158, 182), (100, 102, 126)]     # white: base, shade, deep, edge
B = [(98, 106, 136), (50, 52, 68), (32, 34, 46), (20, 20, 28)]               # black: steel highlight, base, shade, deep
# Shiny (user 2026-11-27, replacing the black/white swap, which looked strange): silver and dark blue. The whites
# become a metallic silver (a brighter top and a harder step to the shade than the matte white), the blacks a deep
# navy with a cornflower highlight; the yellow beak and talons stay.
SILVER = [(200, 208, 222), (150, 160, 182), (106, 114, 140), (66, 72, 96)]
NAVY = [(88, 122, 196), (38, 60, 124), (24, 38, 88), (12, 20, 52)]
SHINY_OF = {('W', k): SILVER[k] for k in range(4)}
SHINY_OF.update({('B', k): NAVY[k] for k in range(4)})

def col(role, shiny=False):
    if isinstance(role, tuple) and len(role) == 2 and role[0] in ('W', 'B'):
        return SHINY_OF[role] if shiny else (W if role[0] == 'W' else B)[role[1]]
    return role                                                              # fixed RGB

YEL, YEL_S, YEL_D = (232, 200, 88), (184, 152, 56), (120, 96, 40)
BLACK = (0, 0, 0); OUTL = (16, 16, 16); EYE = (248, 248, 248)

# ---- role tables (index -> role), per palette ----------------------------------------------------------------
RUF = {1: ('B', 1), 2: BLACK, 3: ('W', 2), 4: ('W', 0), 5: ('W', 3), 6: ('W', 0), 7: ('W', 1), 8: ('B', 2),
       9: ('B', 1), 10: ('B', 2), 11: ('B', 3), 12: YEL, 13: YEL_S, 14: ('B', 0), 15: EYE}
RUF_OW = {1: ('B', 3), 2: BLACK, 3: ('W', 0), 4: ('W', 3), 5: ('W', 0), 6: ('W', 1), 7: ('B', 1), 8: ('B', 2),
          9: ('B', 1), 10: YEL, 11: ('W', 0), 12: YEL_S, 13: ('W', 0), 14: ('B', 2), 15: YEL_D}
BRA = {1: ('W', 3), 2: ('W', 2), 3: ('W', 0), 4: OUTL, 5: ('B', 3), 6: ('B', 1), 7: ('W', 2), 8: ('W', 0),
       9: ('W', 1), 10: YEL_D, 11: ('W', 2), 12: ('B', 2), 13: YEL_S, 14: YEL, 15: ('B', 0)}
BRA_OW = {1: ('B', 1), 2: ('B', 2), 3: ('W', 1), 4: OUTL, 5: YEL, 6: ('W', 3), 7: ('W', 2), 8: BLACK,
          9: ('W', 0), 10: ('B', 0), 11: YEL_D, 12: BLACK, 13: BLACK, 14: BLACK, 15: BLACK}

def rufflet_eyes(a):
    """Index 4 below the crest is the eye whites: move them to 15 (always white)."""
    a = a.copy()
    for y, x in np.argwhere(a == 4):
        if y % 64 >= 23: a[y, x] = 15
    return a

def braviary_back(a):
    """On the back sprite the red is the bird's upper back, not the wing's leading edge: move it onto the black
    entries (red main 3 -> 6, shade 2 -> 12, deep 1 -> 5) so the white head sits on a black body."""
    a = a.copy(); m3, m2, m1 = a == 3, a == 2, a == 1
    a[m3], a[m2], a[m1] = 6, 12, 5
    return a

def braviary_front(a):
    """The red streaks in the head crest turn black (the wing and tail red stays white), so the white crest carries
    black slashes like the Rufflet's, and the head stands out from the white wing edge behind it."""
    a = a.copy()
    for (y0, y1, x1) in ((28, 48, 16), (64 + 18, 64 + 40, 16)):          # head box per frame: rows y0..y1, x < x1
        sub = a[y0:y1, :x1]
        m3, m2, m1 = sub == 3, sub == 2, sub == 1
        sub[m3], sub[m2], sub[m1] = 6, 12, 5
    return a

# species dir -> (front file, battle role table, ow role table, pixel fix)
SPECIES = {
    'rufflet':  ('anim_front.png', RUF, RUF_OW, (rufflet_eyes, rufflet_eyes)),
    'braviary': ('anim_front.png', BRA, BRA_OW, (braviary_front, braviary_back)),
}
BG = (152, 208, 160)

def palette(roles, shiny):
    return [BG] + [col(roles[i], shiny) for i in range(1, 16)]

def write_pal(path, pal):
    with open(path, 'w', newline='\r\n') as f:
        f.write('JASC-PAL\n0100\n16\n' + ''.join('%d %d %d\n' % c for c in pal))

def read_pal(path):
    L = [l.strip() for l in open(path).read().splitlines()][3:19]
    return [tuple(int(v) for v in l.split()) for l in L]

def save_png(a, pal, path):
    im = Image.fromarray(a.astype(np.uint8), 'P'); flat = [v for c in pal for v in c]
    im.putpalette(flat + [0] * (768 - len(flat))); im.save(path)

# Icons share fixed palettes, so they are redrawn onto palette 0 (1 grey 131, 2 grey 189, 3 white, 4 dark yellow,
# 5 yellow, 14 grey 98, 15 grey 65) index by index from the original icon (its own palette 2 / 0 colours).
ICON_MAP = {
    'rufflet':  {1: 1, 2: 2, 3: 3, 4: 15, 11: 14, 8: 4, 9: 5, 10: 15, 14: 14, 15: 15},   # mask/body dark, crest black
    'braviary': {1: 14, 2: 2, 3: 3, 4: 4, 5: 5, 6: 3, 7: 14, 8: 2, 9: 2, 14: 15, 15: 15},  # wing black, red edges white
}

def icon(sp, roles_front=None):
    a = np.array(Image.open(os.path.join(ROOT, sp, 'icon.png'))); out = np.zeros_like(a)
    for i, j in ICON_MAP[sp].items(): out[a == i] = j
    assert not ((a > 0) & (out == 0)).any(), sp
    return out

def build(write=False):
    res = {}
    for sp, (front, roles, ow_roles, fix) in SPECIES.items():
        d = os.path.join(ROOT, sp); od = os.path.join(d, 'emergent')
        fr = np.array(Image.open(os.path.join(d, front))); bk = np.array(Image.open(os.path.join(d, 'back.png')))
        ow = np.array(Image.open(os.path.join(d, 'overworld.png')))
        if fix[0]: fr = fix[0](fr)
        if fix[1]: bk = fix[1](bk)
        pn, ps = palette(roles, False), palette(roles, True)
        on, osh = palette(ow_roles, False), palette(ow_roles, True)
        ic = icon(sp, roles)
        res[sp] = dict(front=fr, back=bk, ow=ow, pn=pn, ps=ps, on=on, os=osh, icon=ic)
        if write:
            os.makedirs(od, exist_ok=True)
            save_png(fr, pn, os.path.join(od, 'anim_front.png')); save_png(bk, pn, os.path.join(od, 'back.png'))
            save_png(ow, on, os.path.join(od, 'overworld.png'))
            save_png(ic, read_pal(os.path.join(ROOT, 'icon_palettes', 'pal0.pal')), os.path.join(od, 'icon.png'))
            write_pal(os.path.join(od, 'normal.pal'), pn); write_pal(os.path.join(od, 'shiny.pal'), ps)
            write_pal(os.path.join(od, 'overworld_normal.pal'), on); write_pal(os.path.join(od, 'overworld_shiny.pal'), osh)
    return res

def preview(res, out='/tmp/ef/emergent_preview.png', s=3):
    def rgb(a, pal, bg=(200, 215, 200)):
        p = np.array(pal, np.uint8); r = p[a]; r[a == 0] = bg; return Image.fromarray(r)
    ip = read_pal(os.path.join(ROOT, 'icon_palettes', 'pal0.pal'))
    rows = []
    for sp in SPECIES:
        r = res[sp]; d = os.path.join(ROOT, sp)
        on = read_pal(os.path.join(d, 'normal.pal')); oo = read_pal(os.path.join(d, 'overworld_normal.pal'))
        orig_f = np.array(Image.open(os.path.join(d, SPECIES[sp][0])))
        for label, pal, opal, src in (('original', on, oo, None), ('E. normal', r['pn'], r['on'], 1), ('E. shiny', r['ps'], r['os'], 1)):
            fr = orig_f if src is None else r['front']
            bk = np.array(Image.open(os.path.join(d, 'back.png'))) if src is None else r['back']
            cells = [rgb(fr[:64], pal), rgb(fr[64:], pal), rgb(bk, pal), rgb(r['ow'][:, :96], opal)]
            if label == 'E. normal': cells.append(rgb(r['icon'][:32], ip))
            rows.append((sp + ' ' + label, cells))
    W = 4 * (64 * s + 8) + 96 * s + 32 * s + 40; H = len(rows) * (64 * s + 18)
    S = Image.new('RGB', (W, H), (255, 255, 255))
    from PIL import ImageDraw
    dr = ImageDraw.Draw(S)
    for k, (label, cells) in enumerate(rows):
        x = 0; y = k * (64 * s + 18)
        dr.text((2, y), label, fill=(0, 0, 0))
        for c in cells:
            c = c.resize((c.width * s, c.height * s), Image.NEAREST); S.paste(c, (x, y + 14)); x += c.width + 8
    os.makedirs(os.path.dirname(out), exist_ok=True); S.save(out); return out

if __name__ == '__main__':
    r = build('--write' in sys.argv)
    print(preview(r))
