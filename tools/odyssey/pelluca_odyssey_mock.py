"""Proposal mockups (2026-11-19): Pokemon Odyssey pieces in Osrid's room, the Seaside Tavern and the Templar
holding cell. Odyssey objects sit on the top layer of its FireRed metatiles, so they are pasted over what is
there (exactly how the build would layer them); the hearth is pasted whole."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(REPO, 'tools', 'monomyth', 'dormitory'))
import numpy as np
from PIL import Image, ImageDraw
import frlib, frrender as FR
import compose_mock as CM
FIRE, RUST = FR.TS(frlib.layout(0x08319414)), FR.TS(frlib.layout(0x0871F950))
TS = {'F': FIRE, 'R': RUST}

def ours(layout_id):
    out = f'/tmp/{layout_id}.png'
    subprocess.run([sys.executable, os.path.join(REPO, 'tools', 'render_layout.py'), 'layout', layout_id, out], check=True)
    im = Image.open(out).convert('RGB'); return np.array(im.resize((im.width // 3, im.height // 3), Image.NEAREST))

def put(img, x, y, src, mid, whole=False):
    ts = TS[src]
    if whole: img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = ts.meta(mid); return
    rgb, m = CM.fr_layer(ts, mid, 1); blk = img[y * 16:y * 16 + 16, x * 16:x * 16 + 16]; blk[m] = rgb[m]

def hearth(img, x0, y0):
    """The hearth as an object over what is there (compose_mock.hearth_piece: top layer + firebox, recoloured)."""
    for dy in range(3):
        for dx in range(3):
            rgb, m = CM.hearth_piece(dx, dy); blk = img[(y0 + dy) * 16:(y0 + dy) * 16 + 16, (x0 + dx) * 16:(x0 + dx) * 16 + 16]; blk[m] = rgb[m]

EXTRA = 1                                               # one floor row added behind the bar (user: 2 was too much)
def tavern(hx=4):
    a = ours('LAYOUT_PELLUCA_TAVERN')
    floor = a[5 * 16:6 * 16]                            # a plain floor row (row 5) for the new space
    b = np.vstack([a[:2 * 16]] + [floor] * EXTRA + [a[2 * 16:]])   # under the wall; row 2 carries the bar's back edge
    hearth(b, hx, 0)                                    # the cooking hearth, standing on the floor behind the bar
    for x, y in ((1, 6), (2, 7), (11, 6), (12, 7)): put(b, x, y + EXTRA, 'F', 712)   # plates on the round tables
    for x in (0, 1, 12, 13): put(b, x, 8 + EXTRA, 'R', 648); put(b, x, 9 + EXTRA, 'R', 656)   # barrels, front corners
    return a, b

def cell():
    a = ours('LAYOUT_PELLUCA_TEMPLAR_MONASTERY'); b = a.copy()
    # the cell doubles as a storeroom (user: prisoners are rare, there is very little crime in Pelluca)
    for x, y in ((2, 3), (3, 3), (2, 4)): put(b, x, y, 'R', 642)            # hay bales
    for x, y in ((4, 4), (6, 3), (7, 4)): put(b, x, y, 'R', 649)            # loose straw
    for x in (9, 10): put(b, x, 3, 'R', 648); put(b, x, 4, 'R', 656)        # stored barrels
    for (x, y), m in {(8, 8): 643, (9, 8): 644, (8, 9): 651, (9, 9): 652}.items(): put(b, x, y, 'R', m)  # guards' table
    for x, y in ((7, 9), (10, 9)): put(b, x, y, 'R', 650)                    # stools
    return a, b

def osrid_room():
    a = CM.grid(CM.osrid_room())
    g = CM.osrid_room()
    W = len(g[0])
    for y in range(2, 8):                                # clear the furniture rows
        for x in range(1, W):
            if y >= 4: g[y][x] = ('s', 155)
            elif g[y][x] not in (('s', 216), ('s', 217), ('s', 218), ('s', 224), ('s', 225), ('s', 226)): g[y][x] = ('s', 168 if y == 2 else 155)
    for dy, r in enumerate([[216, 217, 218], [224, 225, 226], [232, 233, 234]]):
        for dx, v in enumerate(r): g[2 + dy][1 + dx] = ('s', v)
    CM.put_hearth(g, 4)
    for dx, v in enumerate((181, 182, 183)): g[2][7 + dx] = ('s', v)
    for dx, v in enumerate((189, 190, 191)): g[3][7 + dx] = ('s', v)
    g[6][6], g[6][7], g[6][8] = ('s', 167), ('s', 176), ('s', 159)
    g[5][9] = ('s', 203)
    b = CM.grid(g)
    for x in (4, 5):                                     # rug in front of the hearth (Odyssey green rug)
        rgb, m = CM.fr_layer(FIRE, 699 if x == 4 else 700, 1)
        if not m.any(): rgb, m = FIRE.meta(699 if x == 4 else 700), np.ones((16, 16), bool)
        blk = b[3 * 16:4 * 16, x * 16 + 8:x * 16 + 24] if False else b[3 * 16:4 * 16, x * 16:x * 16 + 16]; blk[m] = rgb[m]
    return a, b

if __name__ == '__main__':
    rows = [('Seaside Tavern', *tavern()), ('Templar holding cell', *cell())]
    W = max(a.shape[1] + b.shape[1] + 24 for _, a, b in rows); H = sum(max(a.shape[0], b.shape[0]) + 24 for _, a, b in rows)
    S = Image.new('RGB', (W, H), (28, 28, 28)); d = ImageDraw.Draw(S); y = 0
    for name, a, b in rows:
        d.text((2, y + 4), f'{name}: now', fill=(255, 230, 120)); d.text((a.shape[1] + 26, y + 4), 'with Odyssey pieces', fill=(255, 230, 120))
        S.paste(Image.fromarray(a), (0, y + 20)); S.paste(Image.fromarray(b), (a.shape[1] + 24, y + 20)); y += max(a.shape[0], b.shape[0]) + 24
    S.resize((S.width * 2, S.height * 2), Image.NEAREST).save('/tmp/pelluca_odyssey_mock.png'); print(S.size)
