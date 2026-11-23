"""The Templar Citadel (Templar Headquarters), mock v1, from zone plan v2 (user 2026-11-22).

A courtyard in a stone hollow of the Mirroh mountains: the hollow's rock walls step up on three sides (MonoMyth
Fort Elderflower's cliff pieces, snowy pines on top), a crenellated curtain wall closes its mouth with an open arch
(Elderflower's city wall, round towers either side of the arch, its crenels running over the arch as a lintel you
walk under), the pilgrim road climbs in from Route 13 below. Inside, the ground is stone with touches of snow
(Elderflower's paving, light drifts against the walls; user: less snowy than Mirroh). The church (Pokemon Empire's
Arceus church, its front building, Arceus's gold and blue: church/) stands on a narrow frozen moat at the head of
the courtyard, a causeway to its door; the Arceus statue (Pokemon Rejuvenation's figure) on a plinth in a cobbled
round before it; Templars standing about (the in-game Templar sprite, stage 2, shown for placing). West: the Tavern
(Crown 3.2's green-roofed inn) and the barracks (a Crown 3.2 timber chalet). East: the Braviary roost on a ledge up a
stair (a chalet, the mews), the training yard below (fenced). East wall: the cleft to Route 15 (closed: a Templar).
Usage: python3 tools/art/templar_hq/citadel_mock.py [out.png]
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, '..'); REPO = os.path.normpath(os.path.join(ART, '..', '..'))
sys.path.insert(0, os.path.join(ART, 'mirroh')); sys.path.insert(0, ART)
import mirroh_mock as mm
import mirroh_v3 as v3

W, H = 40, 40
for mod in (mm, v3): mod.W, mod.H = W, H
ef = v3.ef; fx = v3.fx; rnd = v3.rnd
PAVE = ef(0x275); SNOW = ef(0xed)
GROUND = mm.EF_GROUND

def block_from_rgba(path_or_img, cw, ch, pad_top=True):
    """An RGBA picture as a placeable block of cells (img, alpha), padded to whole cells (at the top: it stands)."""
    im = path_or_img if isinstance(path_or_img, Image.Image) else Image.open(path_or_img)
    a = np.array(im.convert('RGBA'))
    h, w = a.shape[:2]; Hc, Wc = ch * 16, cw * 16
    out = np.zeros((Hc, Wc, 4), np.uint8)
    oy = Hc - h if pad_top else 0; ox = (Wc - w) // 2
    out[oy:oy + h, ox:ox + w] = a
    return [[(out[y * 16:y * 16 + 16, x * 16:x * 16 + 16, :3].copy(), out[y * 16:y * 16 + 16, x * 16:x * 16 + 16, 3] > 0)
             for x in range(cw)] for y in range(ch)]

def templar():
    """The in-game Templar overworld sprite, facing down (its first frame), as RGBA."""
    im = Image.open(os.path.join(REPO, 'codebase/graphics/object_events/pics/people/templar.png'))
    a = np.array(im.convert('RGBA')); fw = 16; fh = a.shape[0]
    fr = a[:, :fw].copy()
    pal = im.getpalette() if im.mode == 'P' else None
    if im.mode == 'P':
        idx = np.array(im)[:, :fw]; fr[idx == 0, 3] = 0
    return Image.fromarray(fr)

def statue_block():
    """The Arceus figure (Rejuvenation's, its own white and gold) on a plinth of Elderflower stone: 3x4 cells."""
    fig = Image.open(os.path.join(REPO, 'assets/arceus_statue/arceus_figure.png')).convert('RGBA')
    can = Image.new('RGBA', (48, 64), (0, 0, 0, 0))
    d = ImageDraw.Draw(can)
    # the plinth: a stepped base, a shaft, a cap (plain geometry in Elderflower's stone greys)
    OUT, D, M_, L, T = (40, 40, 56, 255), (88, 88, 108, 255), (122, 122, 140, 255), (160, 160, 176, 255), (200, 200, 212, 255)
    d.rectangle((2, 52, 45, 63), fill=OUT); d.rectangle((3, 53, 44, 61), fill=M_); d.rectangle((3, 53, 44, 54), fill=L)
    d.rectangle((3, 60, 44, 61), fill=D)
    d.rectangle((8, 44, 39, 53), fill=OUT); d.rectangle((9, 45, 38, 52), fill=M_); d.rectangle((9, 45, 38, 46), fill=T)
    d.rectangle((9, 51, 38, 52), fill=D)
    can.alpha_composite(fig, ((48 - fig.size[0]) // 2, 47 - fig.size[1]))
    return block_from_rgba(can, 3, 4)

GREY_WOOD = [(22, 22, 26), (34, 34, 40), (46, 46, 52), (60, 60, 66), (76, 76, 82), (94, 94, 98), (114, 113, 116)]
def grey_wood(img):
    """(user 2026-11-22: the homes in a dark, deep grey wood, so they stand out) Crown's timber, its shingles and its
    climbing vines to a deep grey ramp by lightness; glass, plaster, lanterns and stone keep their colours."""
    a = img.astype(int); r, g, b = a[..., 0], a[..., 1], a[..., 2]
    lum = .30 * r + .59 * g + .11 * b
    wood = ((r > b + 6) & (r >= g - 6) & (lum < 175)) | ((g > r + 8) & (g > b + 8))      # (browns, the darkest too; the vines' greens)
    t = np.clip(lum / 160.0, 0, 1)
    ramp = np.array(GREY_WOOD)
    out = a.copy(); out[wood] = ramp[np.clip((t[wood] * (len(ramp) - 1)).round().astype(int), 0, len(ramp) - 1)]
    return out.astype(np.uint8)

def chalet(sx, sy, w, h):
    b = mm.cut('c32', sx, sy, w, h)
    return [[None if c is None else (grey_wood(c[0]), c[1]) for c in row] for row in b]

def house_rgba(block):
    """A placed block of cells (img, alpha) back into one RGBA picture."""
    h, w = len(block), len(block[0]); out = np.zeros((h * 16, w * 16, 4), np.uint8)
    for y, row in enumerate(block):
        for x, c in enumerate(row):
            if c is None: continue
            t, m = c; sub = out[y * 16:y * 16 + 16, x * 16:x * 16 + 16]; sub[m, :3] = t[m]; sub[m, 3] = 255
    return Image.fromarray(out)

AXIS = 19                     # (the axis: the middle of column 19, pixel 312; x mirrors to 38 - x)
def mirror_cells(cells): return {(2 * AXIS - x, y) for (x, y) in cells}

def compose():
    """v4 (user 2026-11-22): the snow and the little trees inside looked placed, not natural -- study how these
    environments use them; and the ledge houses' stairs were not centred on their doors.
    Fort Elderflower (MonoMyth's walled winter city, the same paving) shows the way: no trees inside the paved
    courts at all (pines grow on the snow outside the walls, in loose clusters of big and small with gaps, never in
    rows); snow lies on the paving in broad patches with stepped edges, in the open stone where nobody walks, the odd
    ice crystal on it; the walking lines (between doors, stairs and gates) bare.
    The stairs: the house's door is centred in it (its opening spans pixels 32-46 of 80), so on the tile grid it is
    centred on a tile, and the two-tile stair can never sit under it. Each ledge house is set half a tile over (the
    tiles are rebuilt from the picture, so this costs nothing), its door's centre on a tile edge, the stair right
    under it. And the whole map now mirrors about one line: the hollow's east wall was half a tile off the axis the
    church, the fountain and the arch are centred on (x 37 for the mirror of x 2: now x 36)."""
    M = mm.Map()
    for y in range(H):
        for x in range(W): M.ground(x, y, PAVE, 'pave')
    # --- the hollow: the mountain above (snow, pines), a tall north face, a face down each side (x 2 and 36)
    top = {(x, y) for y in range(H) for x in range(W) if y <= 1 or x <= 1 or x >= 37 or y >= 35}
    for (x, y) in top: M.ground(x, y, SNOW, 'snow')
    for y in (2, 3, 4):
        for x in range(2, 37): M.ground(x, y, ef(0x105 if x == 2 else 0x107 if x == 36 else 0x106), 'cliff')
    for y in range(5, 35):
        M.ground(2, y, ef(0xfd), 'cliff'); M.ground(36, y, ef(0xff), 'cliff')
    for x in range(37, W):
        for y in range(5, 35): M.ground(x, y, SNOW, 'snow')
    # the cleft east to Route 15 (rows 15-17)
    for y in range(15, 18):
        for x in range(36, W): M.ground(x, y, PAVE, 'pave')
    M.ground(36, 14, ef(0x107), 'cliff')
    for x in range(37, W): M.ground(x, 14, ef(0x106), 'cliff')
    for x in range(37, W): M.ground(x, 18, ef(0x106), 'cliff')
    # --- the church's terrace (x 11-27), its crenellated front wall (rows 18-21), the stair on the axis (x 18-20)
    mm.terrace_wall(M, 11, 27, 18, stairs=(18,))
    M.ground(21, 17, fx(M.g[17][17]), 'wall')
    for y in range(5, 18):
        M.ground(11, y, ef(0x291), 'wall'); M.ground(27, y, fx(ef(0x291)), 'wall')
    # --- the curtain wall (x 3-35, rows 31-34), its open arch on the axis
    mm.city_wall(M, 3, 35, 31)
    for y in range(31, 35):
        for x in range(18, 21): M.ground(x, y, PAVE, 'pave')
    for side, x in ((0, 17), (1, 21)):
        for k, m in enumerate([0x2a3, 0x222, 0x22a, 0x307]):
            t = ef(m); M.ground(x, 31 + k, fx(t) if side == 0 else t, 'wall')
    M.place([[(ef(0x21b), np.ones((16, 16), bool))] * 3, [(ef(0x223), np.ones((16, 16), bool))] * 3], 18, 31, 'lintel', check=False)
    for y in range(35, H):
        for x in range(W): M.ground(x, y, PAVE if 18 <= x <= 20 else SNOW, 'pave' if 18 <= x <= 20 else 'snow')
    # --- the ledges (west x 3-10, east x 28-35), their faces on row 13, their inner sides x 11 / 27
    for (x0, x1, xe, side) in ((3, 10, 11, 0), (28, 35, 27, 1)):
        for x in range(x0, x1 + 1): M.ground(x, 13, ef(0x106), 'cliff')
        for y in range(5, 13): M.ground(xe, y, ef(0xfd if side == 0 else 0xff), 'cliff')
        M.ground(xe, 13, ef(0x107 if side == 0 else 0x105), 'cliff')
    # (the terrace's side parapets stand where the ledges' inner faces are: the ledge faces win above row 13)
    for k, m in enumerate((0x47, 0xe1)): M.ground(6 + k, 13, ef(m), 'stairs')          # (under the west door: x 6-7)
    for k, m in enumerate((0x47, 0xe1)): M.ground(31 + k, 13, ef(m), 'stairs')         # (under the east door: x 31-32)
    # --- snow: broad patches with stepped edges in the open stone, Elderflower's way; never on a walking line
    ways = set()
    ways |= {(x, y) for x in range(17, 22) for y in range(16, 31)}                       # (the axis, the stair)
    ways |= {(x, y) for x in range(12, 27) for y in range(22, 31)}                       # (the fountain square)
    ways |= {(x, y) for x in range(5, 10) for y in range(11, 21)} | mirror_cells({(x, y) for x in range(5, 10) for y in range(11, 21)})   # (ledge doors, stairs, down to the square)
    ways |= {(x, y) for x in range(6, 9) for y in range(28, 31)} | mirror_cells({(x, y) for x in range(6, 9) for y in range(28, 31)})    # (the Tavern's door and its twin's)
    ways |= {(x, y) for x in range(9, 18) for y in range(19, 22)} | mirror_cells({(x, y) for x in range(9, 18) for y in range(19, 22)})
    ways |= {(x, y) for x in range(22, 37) for y in range(14, 19)}                       # (to the cleft)
    ways |= {(x, y) for x in range(15, 24) for y in range(15, 18)}                       # (before the church door)
    def patch(rects):
        return {(x, y) for (x0, y0, x1, y1) in rects for y in range(y0, y1 + 1) for x in range(x0, x1 + 1)}
    S = set()
    S |= patch([(12, 6, 15, 8), (12, 9, 14, 12), (13, 13, 15, 15)])                       # (the terrace, west of the church)
    S |= patch([(23, 5, 26, 7), (24, 8, 26, 11), (23, 12, 25, 13)])                       # (the terrace, east: not a mirror)
    S |= patch([(3, 5, 4, 9), (9, 5, 10, 7)]) | patch([(34, 5, 35, 8), (28, 9, 29, 12), (28, 5, 30, 6)])   # (the ledges round the houses)
    S |= patch([(3, 14, 6, 17), (3, 18, 4, 20)])                                         # (under the west ledge)
    S |= patch([(32, 19, 35, 21), (34, 22, 35, 23)])                                     # (east, above the Tavern's twin)
    S |= patch([(3, 29, 5, 30), (9, 29, 15, 30)]) | patch([(23, 29, 28, 30), (33, 29, 35, 30)])   # (along the curtain wall's foot)
    cells = {(x, y) for y in range(5, 31) for x in range(3, 36) if M.gtag[y, x] == 'pave'}
    S = v3.thick({c for c in S if c in cells and c not in ways})
    v3.snow_on(M, S, lambda x, y: PAVE, cells, 'pave')
    # --- the church on its terrace
    M.place(block_from_rgba(os.path.join(HERE, 'church', 'front_arceus.png'), 7, 13), 16, 5, 'church', check=False)
    # --- the fountain square
    FT = os.path.join(HERE, 'fountain')
    M.place(block_from_rgba(os.path.join(FT, 'fountain.png'), 5, 4), 17, 24, 'fountain', check=False)
    for (x, y, f) in ((13, 22, 'left'), (13, 27, 'left'), (23, 22, 'right'), (23, 27, 'right')):
        M.place(block_from_rgba(os.path.join(FT, 'statue_%s.png' % f), 3, 3), x, y, 'statue', check=False)
    for (x, y) in ((16, 22), (22, 22), (16, 29), (22, 29)): mm.lamp(M, x, y)
    # --- the houses (dark deep grey wood), mirrored pairs: the Tavern and its twin; the ledge houses, half a tile over
    tav = chalet(5, 24, 7, 7)
    flip = lambda b: [[None if c is None else (c[0][:, ::-1], c[1][:, ::-1]) for c in r][::-1] for r in b]
    M.place(tav, 4, 22, 'house', check=False); M.place(flip(tav), 28, 22, 'house', check=False)
    small = house_rgba(chalet(11, 14, 5, 6))
    M.place(block_from_rgba(small, 6, 6), 4, 7, 'house', check=False)                      # (pixels 72-152: door centred on x 7.0)
    M.place(block_from_rgba(small.transpose(Image.FLIP_LEFT_RIGHT), 6, 6), 29, 7, 'house', check=False)   # (472-552: door on 32.0)
    # --- pines outside the walls only: loose clusters of big and small with gaps (Elderflower), never rows
    for (x, y) in sorted(top, key=lambda c: (c[1], c[0])):
        if rnd('bp', x, y) < 0.42 and M.free(x, y, 2, 3) and all((x + i, y + j) in top for i in (0, 1) for j in (0, 1, 2)):
            mm.pine(M, x, y, True)
    for (x, y) in sorted(top, key=lambda c: (c[1], c[0])):
        if rnd('lp', x, y) < 0.35 and M.free(x, y, 1, 2) and all((x, y + k) in top for k in (0, 1)):
            mm.pine(M, x, y, False)
    return M

def main(out):
    M = compose(); img = Image.fromarray(M.render()).convert('RGBA')
    t = templar()
    for (x, y) in ((16, 35), (22, 35), (18, 23), (20, 23), (12, 26), (26, 26), (37, 16), (19, 18)):
        img.alpha_composite(t, (x * 16, y * 16 + 16 - t.size[1]))
    img.convert('RGB').save(out)
    img.convert('RGB').resize((W * 32, H * 32), Image.NEAREST).save(out.replace('.png', '_2x.png'))
    print('mock', out)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/citadel_mock_v4.png')
