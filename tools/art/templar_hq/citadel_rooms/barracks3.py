"""The Citadel's barracks, mock v3 (user 2026-11-23: "a better basis"; plan v3 approved, plans.py BARRACKS3).
Built from the user's station-barracks reference, its right half (assets/templar_hq_reference/barracks_reference/;
no credit needed, user): the briefing room, the bunk hall, the gear-and-duty room, joined by a corridor. Barracks only
(no jail); the reference's grey stone walls kept, the floor in the houses' cream planks (tavern.py); its modern things
left out (ceiling lights, computers, phone, fridge, microwave, stove, monitor); its red chairs in the Order's blue.
room() returns (picture, solid, exits) as houses.py. Usage: python3 barracks3.py OUT.png"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); TQ = os.path.dirname(HERE)
for d in (HERE, os.path.join(TQ, 'study'), os.path.join(TQ, 'kitchen')): sys.path.insert(0, d)
import tavern, props, cutter
REF = os.path.join(TQ, '..', '..', '..', 'assets', 'templar_hq_reference', 'barracks_reference', 'barracks_half_native.png')
T = 16; W, H = 21, 13
MAT = ((36, 74, 155), (177, 149, 48))
BLACK = [(7, y) for y in range(0, 5)] + [(15, y) for y in range(0, 5)] + [(7, y) for y in range(9, 12)] + [(15, y) for y in range(9, 12)]

def pieces():
    import kitchen_mock as KM
    a = cutter.load(REF); refs = [(1, 6), (1, 1), (1, 2)]
    c = lambda x, y, w, h, **k: cutter.cut(a, x, y, w, h, refs, **k)
    P = {'bed': c(8, 3, 1, 2), 'locker': c(8, 10, 1, 3), 'table': c(2, 8, 4, 3), 'chair_s': c(2, 7, 1, 1),
         'chair_n': c(2, 11, 1, 1), 'chair_e': c(1, 9, 1, 1), 'chair_w': c(17, 6, 1, 1), 'bookshelf': c(3, 2, 2, 2),
         'books_table': c(1, 3, 2, 3), 'side_chair': c(3, 5, 1, 1), 'duty_desk': c(16, 5, 1, 3), 'sack': c(16, 10, 1, 2),
         'crate': c(17, 12, 1, 1), 'chair_n2': c(6, 4, 1, 1)}
    d = c(5, 2, 1, 2); desk = np.concatenate([d, d[:, ::-1]], 1)                 # (the desk without its computer:
    book = P['books_table'][5:22, 1:17].copy()                                       #  its plain half and that half's mirror,
    P['desk'] = desk; P['book'] = book                                             #  a book from the books table on it)
    t = P['table']                                                                 # (the briefing table cleared of its
    t[:41, 0:16] = t[:41, 48:64][:, ::-1]                                          #  screen, tablet and dish: the left from
    t[:17, 32:48] = t[:17, 16:32]                                                  #  the right edge's mirror; a map and a
    m = props.pass_map()[2:20, 4:34]; k = m[..., 3] > 0                            #  book on it instead)
    t[12:30, 17:47][k] = m[k]
    bk = book.copy(); kb = bk[..., 3] > 0; t[8:25, 2:18][kb] = bk[kb]
    stub = np.zeros((32, 16, 4), int); stub[..., :3] = a[6 * T:8 * T, 7 * T:8 * T]; stub[..., 3] = 255
    P['stub'] = stub
    for k in ('chair_s', 'chair_n', 'chair_e', 'chair_w', 'side_chair', 'chair_n2'): KM.blue_cushions(P[k])
    return P, a

def room():
    P, a = pieces(); Q = props.pieces()
    tv, _, _ = tavern.room(); tv = tv.astype(int)
    img = np.zeros((H * T, W * T, 3), int); solid = np.zeros((H, W), bool)
    cell = lambda src, x, y: src[y * T:(y + 1) * T, x * T:(x + 1) * T]
    for x in range(1, W - 1):
        for y in range(2): img[y * T:(y + 1) * T, x * T:(x + 1) * T] = cell(a, 1, 1 + y)        # (plain grey stone)
        for y in range(2, H - 1): img[y * T:(y + 1) * T, x * T:(x + 1) * T] = cell(tv, 8 + x % 2, 2 if y == 2 else 3)
    solid[:2] = True; solid[:, 0] = solid[:, W - 1] = True; solid[H - 1] = True
    for (x, y) in BLACK: img[y * T:(y + 1) * T, x * T:(x + 1) * T] = 0; solid[y, x] = True
    def put(p, px, py, sol=True):
        h, w = p.shape[:2]; m = p[..., 3] > 0
        img[py:py + h, px:px + w][m] = p[..., :3][m]
        if sol:
            cov = np.zeros((H + 4, W + 4)); ys, xs = np.nonzero(m)
            for yy, xx in zip(ys + py, xs + px): cov[yy // T, xx // T] += 1
            solid[:] |= cov[:H, :W] >= 48
    # the briefing room (west)
    put(P['bookshelf'], 3 * T, 1 * T); put(P['desk'], 5 * T, 1 * T); put(P['book'], 5 * T + 10, 1 * T + 4, False)
    put(P['chair_n2'], 6 * T, 3 * T); put(P['books_table'], 1 * T, 2 * T); put(P['side_chair'], 3 * T, 4 * T)
    for x in range(2, 6): put(P['chair_s'], x * T, 6 * T); put(P['chair_n'], x * T, 10 * T)
    put(P['table'], 2 * T, 7 * T); put(P['chair_e'], 1 * T, 8 * T)
    # the bunk hall (centre)
    for x in (7, 15): put(P['stub'], x * T, 5 * T)
    for x in (8, 10, 12, 14):
        for y in (2, 5): put(P['bed'], x * T, y * T)
    put(Q['banner_shield'], 11 * T - 8, 0, False)
    for x in (8, 9, 13, 14): put(P['locker'], x * T, 9 * T)
    # gear and duty (east)
    for y in (4, 16): put(Q['sword'], 16 * T + 1, y, False)
    put(Q['banner_swords'], 18 * T, 0, False)
    put(Q['helmet'], 16 * T, 2 * T); put(Q['helmet'], 18 * T, 2 * T)
    put(P['duty_desk'], 16 * T, 4 * T); put(P['chair_w'], 17 * T, 5 * T)
    put(Q['kegs'], 18 * T, 9 * T); put(P['sack'], 16 * T, 9 * T); put(P['crate'], 17 * T, 11 * T)
    y = (H - 2) * T                                                                            # (the door, three wide)
    img[y + 4:y + 12, 10 * T + 2:13 * T - 2] = MAT[1]; img[y + 5:y + 11, 10 * T + 3:13 * T - 3] = MAT[0]
    ex = [(10, H - 2), (11, H - 2), (12, H - 2)]
    for (x, yy) in ex: solid[yy, x] = False
    return img.astype(np.uint8), solid, ex

if __name__ == '__main__':
    img, solid, ex = room()
    Image.fromarray(img).resize((W * 48, H * 48), Image.NEAREST).save(sys.argv[1]); print(W, H, ex)
    print('\n'.join(''.join('#' if s else '.' for s in r) for r in solid))
