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

def chalet(sx, sy, w, h):
    return mm.cut('c32', sx, sy, w, h)

def compose():
    M = mm.Map()
    for y in range(H):
        for x in range(W): M.ground(x, y, PAVE, 'pave')
    # --- the hollow's rock walls (user: a stone hollow): the mountain above (snow, pines) and its faces dropping into the
    # hollow, tall on the north (three rows of Elderflower's cliff face stacked, as MonoMyth's Route 22 builds its high
    # walls), one column on each side; boulders along their feet
    top = {(x, y) for y in range(H) for x in range(W) if y <= 1 or x <= 1 or x >= 38 or y >= 35}
    for (x, y) in top: M.ground(x, y, SNOW, 'snow')
    for y in (2, 3, 4):
        for x in range(2, 38):
            m = 0x106
            if x == 2: m = 0x105
            if x == 37: m = 0x107
            M.ground(x, y, ef(m), 'cliff')
    for y in range(5, 35):                                             # (down to the curtain wall's foot)
        M.ground(2, y, ef(0xfd), 'cliff'); M.ground(37, y, ef(0xff), 'cliff')
    # the cleft east to Route 15 (rows 15-17): the east wall broken through, the stone out to the edge
    for y in range(15, 18):
        for x in range(37, W): M.ground(x, y, PAVE, 'pave')
    M.ground(37, 14, ef(0x107), 'cliff')
    for x in range(38, W): M.ground(x, 14, ef(0x106), 'cliff')
    # --- the curtain wall across the mouth (rows 31-34) with its open arch (x 18-21)
    mm.city_wall(M, 3, 36, 31)
    for y in range(31, 35):
        for x in range(18, 22): M.ground(x, y, PAVE, 'pave')
    for side, x in ((0, 17), (1, 22)):                                  # (round towers either side of the arch)
        for k, m in enumerate([0x2a3, 0x222, 0x22a, 0x307]):
            t = ef(m); M.ground(x, 31 + k, fx(t) if side == 0 else t, 'wall')
    lintel = [[(ef(m), np.ones((16, 16), bool)) for m in (0x21b,) * 4], [(ef(0x223), np.ones((16, 16), bool))] * 4]
    M.place(lintel, 18, 31, 'lintel', check=False)
    # --- the pilgrim road: up from Route 13 through the arch to the church
    road = {(x, y) for x in range(18, 22) for y in range(18, H)}
    # (user 2026-11-22: the stone-on-stone mix looked unnatural: one stone surface, the way is the paving itself)
    for y in range(35, H):
        for x in range(W):
            if (x, y) not in road: M.ground(x, y, SNOW, 'snow')
            elif y >= 35: M.ground(x, y, PAVE, 'pave')
    # snow (user: stone with touches of snow, less than Mirroh): Mirroh's own pass, lighter (base 0.0 to Mirroh's
    # 0.2): ragged drifts a little deeper toward the walls, the ways swept (the processional way, every door), the
    # paving round the drifts dusted so they fade into the stone
    cells = {(x, y) for y in range(5, 31) for x in range(3, 37) if M.gtag[y, x] == 'pave'}
    ways = [((19.5, 34), (19.5, 17)), ((12, 24.5), (27, 24.5)), ((8, 28), (16, 28)), ((8.5, 13), (8.5, 20), (16, 22)), ((32.5, 13), (32.5, 20)),
            ((24, 25), (31, 22)), ((36, 16), (24, 16), (22, 17)), ((7, 21), (7, 14))]
    # (user 2026-11-22: touches of winter, not a second stone: a few ragged drifts, each in a corner or along a wall's
    # foot where snow gathers; none in the open, none on the ways)
    S = set()
    for (cx, cy, rx, ry, sd) in ((4.2, 6.0, 1.8, 1.3, 'd1'), (11.5, 5.6, 2.2, 0.9, 'd2'), (26.0, 5.6, 1.6, 0.9, 'd3'),
                                 (35.4, 21.0, 1.1, 2.2, 'd4'), (4.0, 29.4, 2.0, 1.0, 'd5'), (34.8, 29.4, 1.8, 1.0, 'd6'),
                                 (3.8, 17.5, 0.9, 1.8, 'd7')):
        S |= {(x, y) for y in range(int(cy - ry) - 2, int(cy + ry) + 3) for x in range(int(cx - rx) - 2, int(cx + rx) + 3)
              if (x, y) in cells and ((x - cx) / (rx + .5)) ** 2 + ((y - cy) / (ry + .5)) ** 2 < 1 + 0.35 * (v3.vnoise(x, y, 1.7, sd) - 0.5)}
    S = v3.thick(S)
    v3.snow_on(M, S, lambda x, y: PAVE, cells, 'pave')
    # (no dusting: user 2026-11-22, the specks read as a second stone)
    # --- the church at the courtyard's head, on the stone (no moat: user's courtyard; 7 wide it needs none)
    M.place(block_from_rgba(os.path.join(HERE, 'church', 'front_arceus.png'), 7, 13), 16, 5, 'church', check=False)
    # --- the fountain square (user 2026-11-22: a fountain in place of the big statue; Arceus's overworld sprite
    # reskinned as worn stone statues on the square's four corners, the left pair facing left, the right pair right):
    # Crown 3.0's tiered fountain in the middle (x 18-21, rows 23-26), the statues on plinths at the corners
    FT = os.path.join(HERE, 'fountain')
    M.place(block_from_rgba(os.path.join(FT, 'fountain.png'), 4, 4), 18, 23, 'fountain', check=False)
    for (x, y, f) in ((14, 20, 'left'), (14, 27, 'left'), (23, 20, 'right'), (23, 27, 'right')):
        M.place(block_from_rgba(os.path.join(FT, 'statue_%s.png' % f), 3, 3), x, y, 'statue', check=False)
    # --- west: the Tavern (Crown 3.2's green-roofed inn) and the barracks (a timber chalet); east: the roost's mews
    M.place(chalet(5, 24, 7, 7), 5, 21, 'house', check=False)
    M.place(chalet(11, 14, 5, 6), 6, 7, 'house', check=False)
    M.place(chalet(28, 25, 5, 7), 30, 5, 'house', check=False)
    # the roost's ledge: a step up (its face on row 12, a stair at x 32-33; its west side at x 28)
    for x in range(28, 37): M.ground(x, 12, ef(0x106), 'cliff')
    for y in range(5, 12): M.ground(28, y, ef(0xff), 'cliff')
    M.ground(28, 12, ef(0x105), 'cliff')
    for k, m in enumerate((0x47, 0xe1)): M.ground(32 + k, 12, ef(m), 'stairs')
    # (the training yard: open stone east of the square, no fences: user 2026-11-22, too many random things)
    # --- lamps along the way, snow drifting against the walls
    for (x, y) in ((17, 18), (22, 18)): mm.lamp(M, x, y)
    # --- pines on the mountain above the walls only (whole trees; never in the courtyard)
    for (x, y) in sorted(top):
        if M.free(x, y, 1, 2) and all((x, y + k) in top for k in (0, 1)) and rnd('sp', x, y) < 0.8: mm.pine(M, x, y, False)
    # boulders at the walls' feet, here and there
    for (x, y) in ((3, 11), (36, 9), (3, 24), (36, 22), (10, 5), (27, 5)): mm.M_rock(M, x, y) if hasattr(mm, 'M_rock') else v3.rock(M, x, y)
    return M

def main(out):
    M = compose(); img = Image.fromarray(M.render()).convert('RGBA')
    t = templar()
    for (x, y) in ((17, 35), (22, 35), (12, 23), (27, 23), (12, 28), (28, 27), (38, 16), (19, 19)):
        img.alpha_composite(t, (x * 16, y * 16 + 16 - t.size[1]))
    img.convert('RGB').save(out)
    img.convert('RGB').resize((W * 32, H * 32), Image.NEAREST).save(out.replace('.png', '_2x.png'))
    print('mock', out)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/citadel_mock_v2.png')
