"""Install the parchment tab bar into the HGSS PokéLog (user 2026-11-18).

    python3 tools/art/pokelog/build_tab_bar.py

For every info page the bar is rows 0-1 of a page tilemap drawn with one of three menu tilesets:
    menu1: INFO (tilemap_info_screen), AREA (SelectBar, drawn over menu1 on BG1), STATS (tilemap_stats_screen)
    menu2: EVO (tilemap_evo_screen_PE, tilemap_evo_screen), FORMS (tilemap_forms_screen: EVO lit)
    menu3: CRY (tilemap_cry_screen), SIZE (tilemap_size_screen)
Bar tiles go into indices that only bar rows used before (never a tile any page body uses), then into the
tileset's spare room (the game loads 0x2000 bytes = 256 tiles per tileset). Tiles are de-duplicated with
flips. The bar's colours are palette-0 indices 10-14, set in every HGSS palette file (unused elsewhere).
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from tab_bar import render_bar, COLOURS
HG = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'codebase', 'graphics', 'pokedex', 'hgss'))
INFO, AREA, STATS, EVO, CRY, SIZE = range(6)
GROUPS = {
    'menu1': [('tilemap_info_screen', INFO), ('SelectBar', AREA), ('tilemap_stats_screen', STATS)],
    'menu2': [('tilemap_evo_screen_PE', EVO), ('tilemap_evo_screen', EVO), ('tilemap_forms_screen', EVO)],
    'menu3': [('tilemap_cry_screen', CRY), ('tilemap_size_screen', SIZE)],
}
MAX_TILES = 256
PAL_FILES = [f'palette_{a}{b}.pal' for a in ('default', 'national', 'search_results') for b in ('', '_dark', '_darkest')]

def load_tileset(name):
    im = Image.open(os.path.join(HG, f'tileset_{name}.png')); a = np.asarray(im).copy()
    n = (a.shape[0] // 8) * 16
    tiles = [a[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8].copy() for i in range(n)]
    return im, tiles

def save_tileset(name, im, tiles):
    rows = (len(tiles) + 15) // 16; a = np.zeros((rows * 8, 128), np.uint8)
    for i, t in enumerate(tiles): a[(i // 16) * 8:(i // 16) * 8 + 8, (i % 16) * 8:(i % 16) * 8 + 8] = t
    out = Image.fromarray(a, 'P'); out.putpalette(im.getpalette()); out.save(os.path.join(HG, f'tileset_{name}.png'))

def build_group(name, pages):
    im, tiles = load_tileset(name)
    maps = {m: np.fromfile(os.path.join(HG, f'{m}.bin'), '<u2').copy() for m, _ in pages}
    body = set(); bar_old = set()
    for m, tm in maps.items():
        bar_old |= {int(v & 0x3FF) for v in tm[:64]}
        body |= {int(v & 0x3FF) for v in tm[64:]}
    free = sorted(bar_old - body - {0}) + list(range(len(tiles), MAX_TILES))
    lookup = {}
    def place(t):
        for flip, v in ((0, t), (1, t[:, ::-1]), (2, t[::-1, :]), (3, t[::-1, ::-1])):
            if v.tobytes() in lookup: return lookup[v.tobytes()] | ((flip & 1) << 10) | ((flip >> 1) << 11)
        idx = free.pop(0)
        while idx >= len(tiles): tiles.append(np.zeros((8, 8), np.uint8))
        tiles[idx] = t.copy(); lookup[t.tobytes()] = idx
        return idx
    for m, sel in pages:
        bar = render_bar(sel); tm = maps[m]
        for ty in range(2):
            for tx in range(32):
                if tx >= 30: tm[ty * 32 + tx] = 0; continue
                tm[ty * 32 + tx] = place(bar[ty * 8:ty * 8 + 8, tx * 8:tx * 8 + 8])      # palette bits 0
        tm.astype('<u2').tofile(os.path.join(HG, f'{m}.bin'))
    if len(tiles) > MAX_TILES: raise SystemExit(f'{name}: {len(tiles)} tiles')
    save_tileset(name, im, tiles)
    return len(lookup), len(tiles)

def set_palettes():
    for f in PAL_FILES:
        p = os.path.join(HG, f); lines = open(p).read().splitlines()
        for idx, (r, g, b) in COLOURS.items(): lines[3 + idx] = f'{r} {g} {b}'
        open(p, 'w', newline='\r\n').write('\n'.join(lines) + '\n')

if __name__ == '__main__':
    for name, pages in GROUPS.items(): print(name, 'bar tiles %d, tileset now %d tiles' % build_group(name, pages))
    set_palettes(); print('palettes', len(PAL_FILES))
