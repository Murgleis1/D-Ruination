"""Osrid's overworld sprite = KAKUGO's sprite (MonoMyth gid 0xCD) wearing OSRID's own mask
(user 2026-11-16, 14:12): "take Osrid's white mask with the horus pattern from the existing
overworld sprite and place it on Kakugo's instead of Kakugo's current mask ..., then fix the back so
it matches Osrid's auburn hair and the clothes to match his dark green tunic".

  * mask: the white mask + black Horus glyph pixels of Osrid's existing frames (rows 15-20) are
    pasted over Kakugo's visor (bottom of the mask on the row below Kakugo's eyes, so it bobs with
    the walk); front frames take the front mask, profile frames the profile mask
  * hair: Kakugo's helmet ramp -> Osrid's own auburn ramp (from his existing sheet)
  * clothes: Kakugo's coat and scarf -> Osrid's own dark green tunic ramp
Frame order is the standard 9 (S, N, W, walk S x2, walk N x2, walk W x2) in both sheets; Kakugo's
10th frame is dropped. Run: python3 -I osrid_ow.py KAKUGO.png OSRID_OLD.png OUT.png
"""
import sys
import numpy as np
from PIL import Image

# Kakugo index -> colour (Osrid's own colours, sampled from his existing sheet)
PAL = {
    4: (60, 38, 24),     # helmet darkest  -> hair dark
    1: (96, 58, 34),     # helmet mid-dark -> hair
    3: (120, 72, 42),    # helmet mid      -> hair mid
    2: (172, 110, 64),   # helmet light    -> hair light
    6: (172, 110, 64),   # gold highlight  -> hair light
    7: (72, 106, 78),    # gold buttons    -> tunic light
    9: (24, 42, 30),     # coat darkest    -> tunic darkest
    11: (35, 61, 43),    # coat dark       -> tunic dark
    10: (46, 80, 56),    # coat mid        -> tunic
    12: (72, 106, 78),   # coat light      -> tunic light
    13: (46, 80, 56),    # scarf shade     -> tunic
    14: (72, 106, 78),   # scarf           -> tunic light
    15: (255, 255, 255), # (free slot)     -> mask white
}
OLD_WHITE, OLD_BLACK = 5, 1
MASK_ROWS = range(15, 21)


def mask_of(oframe):
    """The mask pixels of one of Osrid's frames: white + the black glyph/outline enclosed by it."""
    m = {}
    for y in MASK_ROWS:
        xs = [x for x in range(16) if oframe[y, x] == OLD_WHITE]
        if not xs: continue
        for x in range(min(xs), max(xs) + 1):
            v = oframe[y, x]
            if v == OLD_WHITE: m[(y, x)] = 15
            elif v == OLD_BLACK: m[(y, x)] = 5
    return m


def build(kak_path, old_path):
    k = Image.open(kak_path); kp = np.array(k).copy(); pal = np.array(k.getpalette()[:48]).reshape(16, 3)
    op = np.array(Image.open(old_path))
    out = []
    for fi in range(9):
        f = kp[:, fi * 16:(fi + 1) * 16].copy(); o = op[:, fi * 16:(fi + 1) * 16]
        m = mask_of(o)
        ye = np.nonzero(f == 8)[0]
        if m and len(ye):
            dy = (ye.max() + 1) - max(y for y, _ in m)        # mask bottom -> row under the eyes
            for (y, x), v in m.items(): f[y + dy, x] = v
        f[f == 8] = 5                                          # any ruby left -> dark
        out.append(f)
    px = np.concatenate(out, 1)
    for i, c in PAL.items(): pal[i] = c
    o = Image.fromarray(px, 'P'); o.putpalette([int(v) for c in pal for v in c] + [0] * (768 - 48))
    return o


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2]).save(sys.argv[3], transparency=0)
