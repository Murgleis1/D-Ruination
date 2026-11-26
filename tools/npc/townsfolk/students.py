"""Academy dormitory students, one at a time (user 2026-11-26).
  Student A <- MonoMyth 29 (blond boy, white shirt, teal shorts): "use this kid as a dorm student, just make his hair a
               deeper gold". MonoMyth 29's lightest hair tone (10) is also his skin's light: the hair's share of it
               moves to slot 6 (whose three pixels on his shirt go to the gold 2 first), found by facing: south and
               west the crown (rows t..t+6), north the whole back of the head (t..t+11), west the back of the head
               (x 8 and over) down to t+11. Then the hair's ramp deepens: highlight, mid, gold, and its brown outline.
Run: python3 students.py -> out/student_a_ow.png, /tmp/cult/students.png"""
import os
import sys
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'walkers'))
from seafolk import save          # noqa: E402
sys.path.insert(0, HERE)
from women import load            # noqa: E402  (this folder's women.py)

FACE = {0: 'S', 1: 'N', 2: 'W', 3: 'S', 4: 'S', 5: 'N', 6: 'N', 7: 'W', 8: 'W'}


def student_a():
    idx, pal = load('mm_29')
    idx[idx == 6] = 2
    for f in range(9):
        sub = idx[:, f * 16:(f + 1) * 16]
        t = min(y for y in range(32) if sub[y].any())
        fac = FACE[f]
        for y in range(t, t + 12):
            for x in range(16):
                if sub[y, x] != 10:
                    continue
                k = y - t
                if k <= 6 or (fac == 'N') or (fac == 'W' and x >= 8):
                    sub[y, x] = 6
    pal[11], pal[6], pal[2] = (240, 196, 96), (214, 160, 52), (168, 116, 28)     # deeper gold
    pal[14] = (112, 74, 40)                                                       # its outline
    return idx, pal


ROWS = [('mm_29', student_a, 'student_a')]

if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    S = 6
    sheet = Image.new('RGB', (9 * (16 * S + 8) + 8, 2 * len(ROWS) * (32 * S + 12) + 8), (110, 110, 125))
    r = 0
    for src, fn, name in ROWS:
        idx, pal = fn()
        save(idx, pal, os.path.join(HERE, 'out', name + '_ow.png'))
        for ii, pp in (load(src), (idx, pal)):
            P = np.array(pp, np.uint8)
            for f in range(9):
                sub = ii[:, f * 16:(f + 1) * 16]
                o = np.zeros((32, 16, 3), np.uint8); o[:] = (110, 110, 125)
                for k in range(1, 16):
                    o[sub == k] = P[k]
                sheet.paste(Image.fromarray(o).resize((16 * S, 32 * S), Image.NEAREST),
                            (8 + f * (16 * S + 8), 8 + r * (32 * S + 12)))
            r += 1
    sheet.save('/tmp/cult/students.png'); print(sheet.size)
