"""Children walkers (user 2026-11-26, of MonoMyth 192, 94, 134, 50 and 193: "These kids are all great, just change all
their hair colors and clothes colors to new ones"). Skin kept on every one; hair and clothes new. Where a slot is
shared between the hair and the clothes it is split by row (from each frame's own top; walking frames bob a row) and
the body's half moved to a free slot.
  Kid A <- MonoMyth 192 (boy; black hair, white shirt, red tie, dark shorts): chestnut hair; pale-blue shirt,
           mustard tie, dark green shorts
  Kid B <- MonoMyth 94  (girl; slate hair with a green sheen, green dress, purple trim): auburn hair; navy dress,
           light-blue skirt, gold trim
  Kid C <- MonoMyth 134 (boy; brown hair, lavender and blue tunic, purple trim): black hair; green tunic, cream,
           maroon trim
  Kid D <- MonoMyth 50  (boy in a swim ring, floating; blonde, teal ring): ginger hair; mustard ring. WATER ONLY
           (user: "a kid who floats in the water, so we can't use him in town")
  Kid E <- MonoMyth 193 (girl; black hair in buns, red dress): light brown hair; blue dress
Run: python3 kids.py -> out/kid_{a..e}_ow.png, /tmp/cult/kids.png"""
import os
import sys
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'walkers'))
from seafolk import save          # noqa: E402
sys.path.insert(0, HERE)
from women import load            # noqa: E402  (this folder's women.py)


def head_split(idx, row, m):
    """Remap slots above `row` (a standing frame's row; follows each frame's top) with m."""
    t0 = None
    for f in range(9):
        sub = idx[:, f * 16:(f + 1) * 16]
        t = min(y for y in range(32) if sub[y].any())
        t0 = t if t0 is None else t0
        head = sub[:row + t - t0]
        src = head.copy()
        for a, b in m.items():
            head[src == a] = b


def body_split(idx, row, m):
    """Remap slots below `row` (a standing frame's row; follows each frame's top) with m."""
    t0 = None
    for f in range(9):
        sub = idx[:, f * 16:(f + 1) * 16]
        t = min(y for y in range(32) if sub[y].any())
        t0 = t if t0 is None else t0
        body = sub[row + t - t0:]
        src = body.copy()
        for a, b in m.items():
            body[src == a] = b


def kid_a():
    idx, pal = load('mm_192')
    body_split(idx, 25, {3: 13})                                           # shorts off the hair's dark
    pal[2], pal[3] = (128, 84, 50), (86, 56, 36)                           # chestnut hair
    pal[9], pal[7], pal[10] = (196, 214, 232), (150, 172, 200), (96, 112, 140)   # pale-blue shirt
    pal[11], pal[12] = (214, 168, 64), (150, 110, 40)                      # mustard tie
    pal[13] = (46, 72, 52)                                                 # dark green shorts
    return idx, pal


def kid_b():
    idx, pal = load('mm_94')
    body_split(idx, 24, {4: 14})                                           # the skirt off the hair's sheen
    pal[2], pal[3], pal[4] = (110, 46, 36), (160, 78, 56), (206, 124, 86)  # auburn hair
    pal[6], pal[13] = (56, 74, 128), (92, 116, 176)                        # navy dress
    pal[14] = (150, 176, 220)                                              # light-blue skirt
    pal[12] = (204, 156, 60)                                               # gold trim
    return idx, pal


def kid_c():
    idx, pal = load('mm_134')
    head_split(idx, 24, {4: 3})                                            # the hair's sheen with the hair
    pal[1], pal[2], pal[3] = (30, 28, 34), (60, 56, 68), (96, 90, 108)    # black hair
    pal[4], pal[10] = (168, 210, 150), (78, 128, 80)                       # green tunic
    pal[11] = (232, 222, 192)                                              # cream
    pal[12] = (132, 40, 52)                                                # maroon trim
    return idx, pal


def kid_d():
    idx, pal = load('mm_50')
    pal[1], pal[2], pal[3] = (130, 50, 30), (200, 92, 48), (236, 142, 82)  # ginger hair
    pal[9], pal[10], pal[11] = (76, 54, 20), (190, 142, 52), (232, 202, 112)   # mustard smock
    return idx, pal


def kid_e():
    idx, pal = load('mm_193')
    body_split(idx, 25, {4: 13})                                           # the sleeves off the hair's sheen
    head_split(idx, 21, {9: 4})                                            # the buns' grey shine to the hair's light
    pal[2], pal[3], pal[4] = (142, 98, 58), (98, 64, 40), (184, 136, 84)   # light brown hair
    pal[5], pal[6] = (40, 58, 126), (72, 110, 190)                         # blue dress
    pal[13] = (96, 116, 160)                                               # sleeves
    return idx, pal


ROWS = [('mm_192', kid_a, 'kid_a'), ('mm_94', kid_b, 'kid_b'), ('mm_134', kid_c, 'kid_c'), ('mm_50', kid_d, 'kid_d'),
        ('mm_193', kid_e, 'kid_e')]

if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    S = 5
    sheet = Image.new('RGB', (2 * (3 * (16 * S + 6)) + 40, len(ROWS) * (32 * S + 10) + 10), (110, 110, 125))
    for r, (src, fn, name) in enumerate(ROWS):
        idx, pal = fn()
        save(idx, pal, os.path.join(HERE, 'out', name + '_ow.png'))
        for c, (ii, pp) in enumerate((load(src), (idx, pal))):
            P = np.array(pp, np.uint8)
            for f in range(3):
                sub = ii[:, f * 16:(f + 1) * 16]
                o = np.zeros((32, 16, 3), np.uint8); o[:] = (110, 110, 125)
                for k in range(1, 16):
                    o[sub == k] = P[k]
                sheet.paste(Image.fromarray(o).resize((16 * S, 32 * S), Image.NEAREST),
                            (10 + c * (3 * (16 * S + 6) + 20) + f * (16 * S + 6), 5 + r * (32 * S + 10)))
    sheet.save('/tmp/cult/kids.png'); print(sheet.size)
