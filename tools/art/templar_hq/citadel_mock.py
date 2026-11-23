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

def compose():
    """v3 (user 2026-11-22: study MonoMyth's and Crown's town squares for the vibe and the homes' layout; the homes in
    dark deep grey wood). What those squares share (Watercress Port, Chamomile, Wood Avens, Crown's harbour town): one
    strong axis, built symmetrically; the main building raised on a terrace with a centred stair, its fountain in front;
    the square framed (lamps at its corners and flanking the stair, evergreens in pairs), nothing scattered; the houses
    in mirrored pairs facing the square. Here the axis is column 19 (pixel 312): the church on its terrace, the stair,
    the fountain square and its four statues, the arch, the road down to Route 13, all centred on it."""
    M = mm.Map()
    for y in range(H):
        for x in range(W): M.ground(x, y, PAVE, 'pave')
    # --- the hollow: the mountain above (snow, pines), a tall north face, a face down each side
    top = {(x, y) for y in range(H) for x in range(W) if y <= 1 or x <= 1 or x >= 38 or y >= 35}
    for (x, y) in top: M.ground(x, y, SNOW, 'snow')
    for y in (2, 3, 4):
        for x in range(2, 38): M.ground(x, y, ef(0x105 if x == 2 else 0x107 if x == 37 else 0x106), 'cliff')
    for y in range(5, 35):
        M.ground(2, y, ef(0xfd), 'cliff'); M.ground(37, y, ef(0xff), 'cliff')
    # the cleft east to Route 15 (rows 15-17)
    for y in range(15, 18):
        for x in range(37, W): M.ground(x, y, PAVE, 'pave')
    M.ground(37, 14, ef(0x107), 'cliff')
    for x in range(38, W): M.ground(x, 14, ef(0x106), 'cliff')
    # --- the church's terrace (x 11-27, rows 5-17), its crenellated front wall (rows 18-21) with the stair on the axis
    mm.terrace_wall(M, 11, 27, 18, stairs=(18,))
    M.ground(21, 17, fx(M.g[17][17]), 'wall')                          # (the stair's right pillar: Elderflower's snowy one, mirrored from its left)
    for y in range(5, 18):                                             # (its sides: parapets, the paving shaded inside)
        M.ground(11, y, ef(0x291), 'wall'); M.ground(27, y, fx(ef(0x291)), 'wall')
    # --- the curtain wall across the mouth (rows 31-34), its open arch on the axis (x 18-20)
    mm.city_wall(M, 3, 36, 31)
    for y in range(31, 35):
        for x in range(18, 21): M.ground(x, y, PAVE, 'pave')
    for side, x in ((0, 17), (1, 21)):
        for k, m in enumerate([0x2a3, 0x222, 0x22a, 0x307]):
            t = ef(m); M.ground(x, 31 + k, fx(t) if side == 0 else t, 'wall')
    M.place([[(ef(0x21b), np.ones((16, 16), bool))] * 3, [(ef(0x223), np.ones((16, 16), bool))] * 3], 18, 31, 'lintel', check=False)
    # outside: the road on the axis down through the snow and pines
    for y in range(35, H):
        for x in range(W): M.ground(x, y, PAVE if 18 <= x <= 20 else SNOW, 'pave' if 18 <= x <= 20 else 'snow')
    # --- snow: a few ragged drifts in corners and along walls' feet, mirrored left and right
    cells = {(x, y) for y in range(5, 31) for x in range(3, 37) if M.gtag[y, x] == 'pave'}
    S = set()
    for (cx, cy, rx, ry, sd) in ((4.2, 6.0, 1.6, 1.2, 'd1'), (4.0, 29.4, 1.8, 1.0, 'd5'), (8.5, 21.6, 1.6, 0.8, 'd8')):
        for (ccx, sd2) in ((cx, sd), (38.0 - cx + 0.0, sd + 'm')):
            S |= {(x, y) for y in range(int(cy - ry) - 2, int(cy + ry) + 3) for x in range(int(ccx - rx) - 2, int(ccx + rx) + 3)
                  if (x, y) in cells and ((x - ccx) / (rx + .5)) ** 2 + ((y - cy) / (ry + .5)) ** 2 < 1 + 0.35 * (v3.vnoise(x, y, 1.7, sd2) - 0.5)}
    for (x, y) in [(x, y) for x in (13, 14, 24, 25) for y in (5, 6)]: S.add((x, y))       # (the terrace's back corners)
    S = v3.thick(S)
    v3.snow_on(M, S, lambda x, y: PAVE, cells, 'pave')
    # --- the church on its terrace, its door on the axis at the terrace's front (row 17)
    M.place(block_from_rgba(os.path.join(HERE, 'church', 'front_arceus.png'), 7, 13), 16, 5, 'church', check=False)
    # evergreens in pairs on the terrace's snowy back corners
    for x in (13, 24): mm.pine(M, x, 5, False)
    # --- the fountain square (rows 22-30, x 13-25): Crown 3.0's fountain on the axis, the four worn statues on its
    # corners, the left pair facing left and the right pair right; lamps flanking the stair and the arch
    FT = os.path.join(HERE, 'fountain')
    M.place(block_from_rgba(os.path.join(FT, 'fountain.png'), 5, 4), 17, 24, 'fountain', check=False)
    for (x, y, f) in ((13, 22, 'left'), (13, 27, 'left'), (23, 22, 'right'), (23, 27, 'right')):
        M.place(block_from_rgba(os.path.join(FT, 'statue_%s.png' % f), 3, 3), x, y, 'statue', check=False)
    for (x, y) in ((16, 22), (22, 22), (16, 29), (22, 29)): mm.lamp(M, x, y)       # (the stair's foot; the arch)
    # --- the houses in mirrored pairs facing the square (dark deep grey wood): the Tavern west, the barracks east
    # (the long inn and its mirror), the hall of the Order's guests west and the Braviary mews east up on ledges
    tav = chalet(5, 24, 7, 7)
    M.place(tav, 4, 22, 'house', check=False)
    M.place([row[::-1] for row in [[None if c is None else (c[0][:, ::-1], c[1][:, ::-1]) for c in r] for r in tav]], 28, 22, 'house', check=False)
    small = chalet(11, 14, 5, 6)
    M.place(small, 4, 7, 'house', check=False)
    M.place([row[::-1] for row in [[None if c is None else (c[0][:, ::-1], c[1][:, ::-1]) for c in r] for r in small]], 30, 7, 'house', check=False)
    # the two ledges they stand on (west x 3-10, east x 29-36), a stair down from each toward the square
    for (x0, x1, sx, side) in ((3, 10, 6, 0), (29, 36, 32, 1)):
        for x in range(x0, x1 + 1): M.ground(x, 13, ef(0x106), 'cliff')
        xe = x1 if side == 0 else x0
        for y in range(5, 13): M.ground(xe, y, ef(0xfd if side == 0 else 0xff), 'cliff')
        M.ground(xe, 13, ef(0x107 if side == 0 else 0x105), 'cliff')
        for k, m in enumerate((0x47, 0xe1)): M.ground(sx + k, 13, ef(m), 'stairs')
    # --- pines on the mountain above the walls only
    for (x, y) in sorted(top):
        if M.free(x, y, 1, 2) and all((x, y + k) in top for k in (0, 1)) and rnd('sp', x, y) < 0.8: mm.pine(M, x, y, False)
    return M

def main(out):
    M = compose(); img = Image.fromarray(M.render()).convert('RGBA')
    t = templar()
    for (x, y) in ((16, 35), (22, 35), (18, 23), (20, 23), (12, 26), (26, 26), (38, 16), (19, 18)):
        img.alpha_composite(t, (x * 16, y * 16 + 16 - t.size[1]))
    img.convert('RGB').save(out)
    img.convert('RGB').resize((W * 32, H * 32), Image.NEAREST).save(out.replace('.png', '_2x.png'))
    print('mock', out)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/citadel_mock_v3.png')
