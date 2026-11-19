"""16x16 region-map "you are here" icon: a small white falcon head in outline (user 2026-11-18),
in profile facing right -- hooked beak, eye, the falcon's malar 'tear' stripe -- with a 1-px dark edge
so the white line reads on any terrain. Drawn into graphics/pokenav/region_map/brendan_icon / may_icon."""
import numpy as np
from PIL import Image
LINE = [   # W = white line; eye + malar stripe inside; hooked beak at right
 "................",
 "................",
 ".....WWWWW......",
 "....W.....W.....",
 "...W.......W....",
 "...W.....W..W...",
 "..W..........W..",
 "..W......W...WWW",
 "..W......W..W..W",
 "...W.......W..W.",
 "...W......W.....",
 "....W.....W.....",
 "....W.....W.....",
 "....WWWWWWW.....",
 "................",
 "................"]
def _line_mask():
    return np.array([[c == 'W' for c in r] for r in LINE])
PAL = [(0, 0, 0), (248, 248, 248), (32, 24, 24)]          # 0 transparent, 1 white line, 2 dark edge
def icon():
    w = _line_mask()
    p = np.pad(w, 1)
    edge = (p[:-2, 1:-1] | p[2:, 1:-1] | p[1:-1, :-2] | p[1:-1, 2:]) & ~w
    return np.where(w, 1, np.where(edge, 2, 0)).astype(np.uint8)
def save_png(path):
    im = Image.fromarray(icon(), 'P'); pal = [v for c in PAL for v in c]; im.putpalette(pal + [0] * (48 - len(pal)))
    im.save(path, transparency=0)
if __name__ == '__main__':
    a = np.array(PAL, np.uint8)[icon()]; a[icon() == 0] = (120, 160, 110)
    Image.fromarray(a).resize((128, 128), Image.NEAREST).save('/tmp/falcon_icon.png')
