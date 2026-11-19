"""PokéLog re-tint, option B "vellum + leather" (user 2026-11-18).

    python3 tools/art/pokelog/retint.py

The game runs the HGSS PokéLog in HGSS_DARK colour mode (src/pokedex_plus_hgss.c). Its pages draw from BG
palette 0: indices 1-9 are the grey interface ramp and 15 the text colour; 10-14 are the parchment tab bar
(build_tab_bar.py) and are left alone. This rewrites, in place and keeping every file's size and layout:
  - palette_{default,national,search_results}_dark.pal: palette 0 indices 1-9 and 15 -> RAMP;
  - palette_search_menu_dark.pal: its neutral greys -> the same ramp by brightness, its green/orange/red
    highlights -> gold, tan and leather (SEARCH_HI);
  - cry_screen_bg.png / cry_meter.png (the Cry page): the blue waveform strip and grey dial -> the ramp.
Type badges and Pokémon sprites keep their colours. Safe to rerun (gives the same files). The mockup this matches was
rendered in the emulator from the same RAMP and tone() (session scratch retint_mock.py)."""
import os
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
DEX = os.path.join(REPO, 'codebase', 'graphics', 'pokedex')

RAMP = {1: (248, 236, 208), 2: (232, 214, 174), 3: (208, 184, 140), 4: (160, 108, 64), 5: (126, 80, 44),
        6: (96, 60, 32), 7: (44, 26, 14), 8: (96, 60, 32), 9: (32, 18, 8), 15: (48, 30, 16)}
GOLD = (176, 136, 64)
CRY_WAVE_GREYS = [148, 156, 172, 189, 205, 222, 238, 255]       # original lavender ramp (red channel), indices 8-15
# Search-menu highlights (user 2026-11-18): green/orange/red -> gold, tan and leather. Keys are the original
# colours at GBA precision; values never match a key, so a rerun leaves them alone.
SEARCH_HI = {(152, 224, 0): (216, 176, 88), (56, 112, 0): (120, 84, 36), (248, 168, 0): (208, 168, 108),
             (80, 184, 88): (176, 140, 72), (24, 128, 32): (110, 76, 36), (40, 112, 0): (100, 70, 30),
             (176, 104, 0): (140, 92, 48), (248, 32, 32): (152, 40, 32), (128, 32, 32): (104, 40, 24)}

def tone(v):
    """Grey level 0..248 -> a colour along RAMP (darkest to lightest)."""
    pts = sorted((sum(c) / 3, c) for c in RAMP.values())
    xs = [p[0] for p in pts]; v = xs[0] + (xs[-1] - xs[0]) * v / 248
    return tuple(int(np.interp(v, xs, [p[1][k] for p in pts])) for k in range(3))

def q(c): return tuple((int(v) >> 3) << 3 for v in c)          # GBA 5-bit channel, as gbagfx stores it

def read_pal(path):
    lines = open(path).read().split('\n'); n = int(lines[2])
    return [tuple(int(x) for x in l.split()) for l in lines[3:3 + n]]

def write_pal(path, cols):
    with open(path, 'w', newline='\r\n') as f:
        f.write('JASC-PAL\n0100\n%d\n' % len(cols))
        for r, g, b in cols: f.write(f'{r} {g} {b}\n')

def neutral(c): return max(c) - min(c) <= 20

def main():
    for name in ('palette_default_dark', 'palette_national_dark', 'palette_search_results_dark'):
        p = os.path.join(DEX, 'hgss', name + '.pal'); cols = read_pal(p)
        for i, c in RAMP.items(): cols[i] = c
        write_pal(p, cols)
    p = os.path.join(DEX, 'hgss', 'palette_search_menu_dark.pal'); cols = read_pal(p)
    for i, c in enumerate(cols):
        if not i % 16: continue                                    # index 0 of each line is the backdrop
        if q(c) in SEARCH_HI: cols[i] = SEARCH_HI[q(c)]
        elif neutral(c): cols[i] = tone(sum(c) / 3)
    write_pal(p, cols)
    im = Image.open(os.path.join(DEX, 'cry_screen_bg.png')); pal = im.getpalette()[:48]
    cols = [tuple(pal[i:i + 3]) for i in range(0, 48, 3)]
    cols[1] = tone(60); cols[2] = GOLD                             # the strip and its line
    for i, v in zip(range(8, 16), CRY_WAVE_GREYS): cols[i] = tone(v)  # lavender waveform ramp
    im.putpalette([v for c in cols for v in q(c)]); im.save(os.path.join(DEX, 'cry_screen_bg.png'))
    im = Image.open(os.path.join(DEX, 'cry_meter.png')); pal = im.getpalette()[:48]
    cols = [tuple(pal[i:i + 3]) for i in range(0, 48, 3)]
    cols = [tone(c[0]) if c[0] == c[1] == c[2] and i else c for i, c in enumerate(cols)]
    im.putpalette([v for c in cols for v in q(c)]); im.save(os.path.join(DEX, 'cry_meter.png'))

if __name__ == '__main__':
    main(); print('ok')
