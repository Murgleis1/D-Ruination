"""The Mirroh Necropolis grounds, mock v1 (2026-11-21).

The user: the grounds are an expanded version of Dreamstone Mysteries' graveyard in modern Mirroh
(LAYOUT_MIRROH_BASE_CAMP_GRAVEYARD, 20x38), with the rest of the plan added. That graveyard's shape, kept and
enlarged: snowy round trees closing it on every side; the great cross of trees in its middle (a band across, a
column down through it), headstones in rows in its four quarters, the cluster of winter roses at its head, an open
grave in a lower quarter, the way in at its foot between hedges and a fence. Added for the Necropolis of House
Langerin, centuries before it decayed into that graveyard: the grand entrance down into the catacombs at its head
(Crown's palisade gate, charred and gloomed, set into the fortress wall of Mirroh's copper-shaded stone), its two
dragon statues as gargoyles, a mausoleum at each end of the cross (Elderflower's skull door), lamps. The way in at
the foot comes up from Mirroh's skull gate (the bottom edge is the warp back).
Usage: python3 tools/art/necropolis/grounds_mock.py [outdir]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'mirroh'))
import mirroh_mock as mm
import mirroh_v3 as v3

W, H = 44, 50
for mod in (mm, v3): mod.W, mod.H = W, H
ef = v3.ef; fx = v3.fx; rnd = v3.rnd
DM = mm.RL.TS('LAYOUT_MIRROH_BASE_CAMP_GRAVEYARD')
_DMSNOW = np.asarray(DM.metatile(0x1E3), np.uint8)

def dm(rows, tone=None):
    """Dreamstone Mysteries' graveyard pieces, its snow dropped (pixel for pixel), on our snow."""
    out = []
    for r in rows:
        line = []
        for m in r:
            if m is None: line.append(None); continue
            t = np.asarray(DM.metatile(m), np.uint8); a = ~(t == _DMSNOW).all(-1)
            line.append((tone(t) if tone else t, a))
        out.append(line)
    return out

def ancient(img):
    """The Necropolis's trees: Dreamstone Mysteries' snowy greens, older and colder."""
    return mm.gloom(img, 0.3, (30, 40, 50))

def treerow(n):                                     # a column of n round trees, its tip above
    rows = [[0x1ce, 0x1cf]]
    for k in range(n): rows += [[0x1d4, 0x1d5], [0x1dc, 0x1dd] if k < n - 1 else [0x1e6, 0x1e7]]
    return rows

def trees(M, x, y, n, tip=True):
    rows = treerow(n)
    if not tip: rows = rows[1:]; y += 0
    M.place(dm(rows, ancient), x, y - (1 if tip else 0), 'tree', check=False)
    for dy in range(len(rows)):
        for dx in (0, 1):
            yy = y - (1 if tip else 0) + dy
            if 0 <= yy < H and dy > 0: M.gtag[yy, x + dx] = 'treeblock'

def mausoleum(M, x0, y0):
    """A Langerin mausoleum, 7 x 6: Elderflower's skull door between round towers, a crenellated top."""
    c = v3.EFC
    top = [0x2a3] + [0x272] * 5 + [None]
    for dx, m in enumerate(top[:-1]): M.ground(x0 + dx, y0, ef(m), 'wall')
    M.ground(x0 + 6, y0, fx(ef(0x2a3)), 'wall')
    M.ground(x0, y0 + 1, ef(0x222), 'wall'); M.ground(x0 + 6, y0 + 1, fx(ef(0x222)), 'wall')
    for dx in range(1, 6): M.ground(x0 + dx, y0 + 1, ef(0x20e), 'wall')
    for dy in range(4):
        M.ground(x0, y0 + 2 + dy, ef((0x222, 0x222, 0x22a, 0x307)[dy]), 'wall')
        M.ground(x0 + 6, y0 + 2 + dy, fx(ef((0x222, 0x222, 0x22a, 0x307)[dy])), 'wall')
        for dx in range(5): M.ground(x0 + 1 + dx, y0 + 2 + dy, ef(int(c[14 + dy, 28 + dx])), 'wall')
    M.gtag[y0 + 5, x0 + 3] = 'door'

DRUDDIGHUL = os.path.join(HERE, '..', '..', '..', 'assets', 'monomyth_reference', 'pieces', 'druddighul_ow.png')
def stone(img, x0=0, y0=0):
    """A grey, weathered stone from head to toe: lightness onto a cold grey ramp, mottled."""
    f = img.astype(float); l = v3._lum(f) / 255.0
    lo, hi = np.array([40, 40, 46], float), np.array([206, 206, 212], float)
    out = lo + (hi - lo) * np.clip((l - 0.08) / 0.8, 0, 1)[..., None]
    hh, ww = l.shape
    for y in range(hh):
        for x in range(ww):
            out[y, x] += (rnd('st', x0 + x, y0 + y) - 0.5) * 18
    return np.clip(out, 0, 255).astype(np.uint8)

def druddighul_statue(M, x0, y0):
    """A stone Druddighul (user 2026-11-21): MonoMyth's Druddighul, the decrepit dragon of the Apocryphal
    Bastion's ruined castle (its overworld sprite, graphics 0x128, 32x32), turned to grey stone head to toe,
    on a plinth (Crown's statue plinth, greyed). 2 x 3."""
    im = np.array(Image.open(DRUDDIGHUL).convert('RGBA'))
    rgb, a = im[..., :3], im[..., 3] > 0
    st = stone(rgb, x0 * 16, y0 * 16)
    blk = [[(st[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16], a[dy * 16:dy * 16 + 16, dx * 16:dx * 16 + 16])
            for dx in range(2)] for dy in range(2)]
    plinth = mm.cut('c33', 22, 10, 2, 1)
    blk.append([(stone(c[0], x0 * 16 + 16 * i, y0 * 16 + 32), c[1]) if c else None for i, c in enumerate(plinth[0])])
    M.place(blk, x0, y0, 'statue', check=False)

def palisade(M, x0, y0):
    """The grand entrance: Crown's palisade gate (its walled capital, cells 43-55 x 5-14), charred: its timber
    burnt dark, its stone the fortress stone, its green lanterns a ghostly cold flame; the dark within is the way
    down. Crown's dragon statues (darkened, as in Mirroh) stand before it as gargoyles."""
    b = mm.cut('c33', 43, 5, 13, 8, ground=(0x8, 0x9, 0x4, 0x5, 0xa, 0xb, 0x1, 0x13, 0x12, 0x19, 0x2e0, 0x2e1),
               ring=False)                              # (its own stone shares the wall's colours: grass only)
    def tone(i):
        f = i.astype(int); r, g, bl = f[..., 0], f[..., 1], f[..., 2]
        out = v3.to_ef(i)
        wood = (r > bl + 25) & (r > g)                   # timber: charred
        out[wood] = mm.gloom(i, 0.62, (26, 18, 20), keep_snow=False)[wood]
        glow = (g > r + 25) & (g > bl + 10)              # the lanterns' green: a cold ghost flame
        gl = v3._lum(f.astype(float))[..., None] / 255.0
        out[glow] = (np.array([70, 150, 170]) * 0.4 + np.array([150, 230, 240]) * 0.6 * gl[glow]).astype(np.uint8)
        return v3.cstone(out)
    M.place(b, x0, y0, 'gate', fn=tone, check=False)
    for dy in range(8):
        for dx in range(13):
            if b[dy][dx] is not None: M.gtag[y0 + dy, x0 + dx] = 'gatebody'
    mm.gargoyle(M, x0 + 2, y0 + 8); mm.gargoyle(M, x0 + 9, y0 + 8)
    M.gtag[y0 + 7, x0 + 6] = 'door'

def compose():
    M = mm.Map()
    for y in range(H):
        for x in range(W): M.ground(x, y, v3.snow_tile(x, y), 'snow')
    O = 4                                               # (everything below the fortress wall: four rows down)
    # --- the fortress wall across the top (the mountain's foot): crenels on row 8, its face, its foot on row 11;
    # the grand entrance stands out from it (its back against the wall, as in Crown), the dark within the way down
    v3.L = np.zeros((H, W), int); v3.L[0:9, 2:42] = 1; v3.FACES = {1: 2}
    v3.walls(M)
    palisade(M, 15, 8)
    # the slope above the wall: closed by trees
    for x in range(2, 42, 2): trees(M, x, 1, 3)
    # --- the trees closing it round: the two sides (columns), the foot (blocks either side of the way in)
    for x in (0, 42):
        for y in range(0, H - 2, 4): trees(M, x, y + 1, 2)
    for x in list(range(2, 19, 2)) + list(range(25, 42, 2)):
        for y in (37 + O, 41 + O): trees(M, x, y + 1, 2)
    # --- the cross: the band across, the column down through it
    for x in range(10, 34, 2):
        if x in (20, 22): continue
        trees(M, x, 23 + O, 2)
    for y in (17, 21, 25, 29):
        if y == 17: continue                            # (its head starts below the roses)
        trees(M, 20, y + O, 2, tip=(y == 21)); trees(M, 22, y + O, 2, tip=(y == 21))
    trees(M, 21, 33 + O, 1)
    # --- headstones in rows in the four quarters (every other cell, as in Dreamstone Mysteries)
    for (x0, x1, y0, y1) in ((5, 17, 15, 21), (26, 38, 15, 21), (5, 17, 29, 35), (26, 38, 29, 35)):
        for y in range(y0 + O, y1 + O + 1, 2):
            for x in range(x0, x1 + 1, 2):
                if M.free(x, y, 1, 1) and not (35 <= x <= 37 and 31 + O <= y <= 33 + O): mm.headstone(M, x, y)
    # the open grave (Dreamstone Mysteries' dug earth), lower right
    M.place(dm([[0x103, 0x104, 0x105], [0x10b, 0x10c, 0x10d], [0x113, 0x114, 0x115]]), 35, 31 + O, 'grave', check=False)
    # --- the winter roses at the head, between the gargoyles
    for x, y in ((21, 17), (20, 18), (22, 18), (21, 19)):
        M.place(dm([[0x4]], ancient), x, y, 'flowers', check=False)
    # --- a stone Druddighul either side of the cross (user: in place of the mausoleums)
    druddighul_statue(M, 6, 27); druddighul_statue(M, 36, 27)
    # --- the way in at the foot: the fence, the hedges, the way down to Mirroh
    M.place(dm([[0x149, 0x149, 0x13a, None, None, 0x138, 0x149, 0x149]]), 18, 37 + O, 'fence', check=False)
    for y in range(39 + O, H):
        M.place(dm([[0xc7]], ancient), 19, y, 'hedge', check=False); M.place(dm([[0xc7]], ancient), 24, y, 'hedge', check=False)
    v3.stone_pass(M)
    for x in (20, 21, 22, 23): M.gtag[H - 1, x] = 'warp'
    return M

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    M = compose(); img = M.render()
    Image.fromarray(img).save(os.path.join(outdir, 'necropolis_grounds.png'))
    Image.fromarray(img).resize((W * 32, H * 32), 0).save(os.path.join(outdir, 'necropolis_grounds_2x.png'))
    return M

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/necro')
