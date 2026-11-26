"""Academy dormitory students, one at a time (user 2026-11-26).
  Student A <- MonoMyth 29 (blond boy, white shirt, teal shorts): "use this kid as a dorm student, just make his hair a
               deeper gold". MonoMyth 29's lightest hair tone (10) is also his skin's light: the hair's share of it
               moves to slot 6 (whose three pixels on his shirt go to the gold 2 first), found by facing: south and
               west the crown (rows t..t+6), north the whole back of the head (t..t+11), west the back of the head
               (x 8 and over) down to t+11. Then the hair's ramp deepens: highlight, mid, gold, and its brown outline.
  Student B <- Crown 52 (red feathered beret, red-and-gold doublet) and
  Student C <- Crown 58 (orange hair, purple plaid): the user's picks from youth_cands_v1.png ("i like these guys as
               students"), kept as they are; tools/npc/cr_walker.py extracts Crown's walkers.
  Logan     <- MonoMyth 173 (Logan Orphel, the Academy's youngest teacher, one of Cadmus's first top-honour
               graduates, last son of the minor noble House Orphel; not a student: user 2026-11-26). Spiky blond
               hair, navy coat with gold trim: "needs to be dark blue haired to be more
               interesting". The hair's two darker tones (1, 3) are also the coat's gold trim: below the head (row 22
               on a standing frame) they move to slot 15, which only duplicated 6's navy (its pixels go to 6), and keep
               the gold; then the hair goes dark blue.
Run: python3 students.py -> out/student_{a..c}_ow.png, out/logan_ow.png, /tmp/cult/students.png"""
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


def student_b():
    return load('cr_52')


def student_c():
    return load('cr_58')


def logan():
    idx, pal = load('mm_173')
    idx[idx == 15] = 6                                                         # 15 was 6's twin
    for f in range(9):
        sub = idx[:, f * 16:(f + 1) * 16]
        t = min(y for y in range(32) if sub[y].any())
        # the hair: every 1/2/3 pixel joined to the light hair (2) through 1/2/3; below the head (row 22 on a
        # standing frame), any 1/3 not joined is the trim (the hair's tail down his back stays hair)
        from collections import deque
        hair = np.zeros(sub.shape, bool)
        q = deque(zip(*np.where(sub == 2)))
        while q:
            y, x = q.popleft()
            if not (0 <= y < 32 and 0 <= x < 16) or hair[y, x] or sub[y, x] not in (1, 2, 3):
                continue
            hair[y, x] = True
            q.extend(((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)))
        trim = np.isin(sub, (1, 3)) & ~hair
        trim[:t + 14] = False
        sub[trim] = 15
    pal[15] = (236, 132, 44)                                                   # the coat's trim, orange
    # (user 2026-11-26: his clothes "an orange and light grey mix" on the walker as on the front): the navy coat and
    # trousers (8 light navy, 6 navy) light grey, the trim orange
    pal[8], pal[6] = (208, 208, 214), (150, 150, 160)
    pal[2], pal[3], pal[1] = (92, 108, 184), (56, 70, 140), (30, 38, 86)       # dark blue hair
    return idx, pal


ROWS = [('mm_29', student_a, 'student_a'), ('cr_52', student_b, 'student_b'), ('cr_58', student_c, 'student_c'),
        ('mm_173', logan, 'logan')]

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
