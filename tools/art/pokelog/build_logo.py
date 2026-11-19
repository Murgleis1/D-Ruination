"""PokéLog list-screen logo, option C (user 2026-11-18): "PokéLog" in the tab bar's blackletter, dark ink on a
vellum plaque, replacing the "POKé DEX" lettering.

    python3 tools/art/pokelog/build_logo.py

The logo sits on BG1 of the list screen (tilemap_list_screen.bin, tile rows 0-2, columns 14-21) and draws from
tileset_menu_list.png (the HGSS_DECAPPED=FALSE set). Each of those 24 tiles is used exactly once, by the logo
and by no other tilemap, so they are redrawn in place and the tilemap is unchanged (the script checks this).
Only the plaque interior is redrawn (filled with palette-0 index 2, vellum, then the lettering in index 7, ink);
the plaque's border and shadow are untouched. The result does not depend on what was there, so it can be rerun."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
HGSS = os.path.join(REPO, 'codebase', 'graphics', 'pokedex', 'hgss')
FONT = os.path.join(HERE, '..', 'trainer_card', 'fonts', 'JacquardaBastarda9-Regular.ttf')
TILESET, TILEMAP = os.path.join(HGSS, 'tileset_menu_list.png'), os.path.join(HGSS, 'tilemap_list_screen.bin')
OTHERS = ['tilemap_list_screen_underlay.bin', 'tilemap_start_menu.bin', 'tilemap_start_menu_search_results.bin']
X0, Y0, W, H = 118, 4, 55, 17          # plaque interior, screen pixels
VELLUM, INK = 2, 7
TEXT, SIZE = 'PokéLog', 13

def lettering():
    f = ImageFont.truetype(FONT, SIZE)
    m = Image.new('L', (96, 32), 0); ImageDraw.Draw(m).text((0, 0), TEXT, font=f, fill=255)
    m = np.asarray(m) > 110; ys, xs = np.where(m)
    return m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]

def main():
    im = Image.open(TILESET); ts = np.array(im); tmap = np.fromfile(TILEMAP, '<u2').reshape(-1, 32)
    cells = [(r, c) for r in range(Y0 // 8, (Y0 + H - 1) // 8 + 1) for c in range(X0 // 8, (X0 + W - 1) // 8 + 1)]
    ids = [int(tmap[r, c]) for r, c in cells]
    assert all(v >> 10 == 0 for v in ids), 'logo tiles are flipped or use another palette'
    ids = [v & 0x3ff for v in ids]
    every = np.concatenate([tmap.flatten()] + [np.fromfile(os.path.join(HGSS, f), '<u2') for f in OTHERS]) & 0x3ff
    assert all((every == t).sum() == 1 for t in ids), 'a logo tile is shared: allocate new tiles instead'
    scr = np.zeros((24, 176), np.uint8)                          # screen rows 0-23, columns 0-175
    def tile(t): r, c = divmod(t, 16); return ts[r * 8:r * 8 + 8, c * 8:c * 8 + 8]
    for (r, c), t in zip(cells, ids): scr[r * 8:r * 8 + 8, c * 8:c * 8 + 8] = tile(t)
    scr[Y0:Y0 + H, X0:X0 + W] = VELLUM
    m = lettering(); h, w = m.shape; y, x = Y0 + (H - h) // 2, X0 + (W - w) // 2
    scr[y:y + h, x:x + w][m] = INK
    for (r, c), t in zip(cells, ids):
        tr, tc = divmod(t, 16); ts[tr * 8:tr * 8 + 8, tc * 8:tc * 8 + 8] = scr[r * 8:r * 8 + 8, c * 8:c * 8 + 8]
    out = Image.fromarray(ts, 'P'); out.putpalette(im.getpalette()); out.save(TILESET)

if __name__ == '__main__':
    main(); print('ok')
