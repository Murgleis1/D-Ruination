"""Pelluca's townsfolk (user 2026-11-26: proceed with the commoners, children, students and tavern staff). None of
Pelluca's townsfolk battle, so these are walkers only. Candidates from Fantasma's own townsfolk (its period
villagers: tunics, aprons, bonnets), the same style as the walkers already made.
Run: python3 cands.py -> /tmp/cult/townsfolk_cands_v1.png"""
import sys
sys.path.insert(0, '/home/claude/repo/tools/npc')
import fa_walker, ow_scan, numpy as np
from PIL import Image, ImageDraw

GROUPS = [
    ('Commoner man (Man 1, Man 3, the Black Belt; pick 2-3)', [113, 150, 156, 115, 155, 268, 270, 102]),
    ('Commoner woman (Woman 1-4, the Triathlete; pick 3-4)', [48, 49, 51, 123, 125, 60, 61, 120]),
    ('Children (Boy, Tuber; pick a boy and a girl)', [36, 37, 104, 42, 44, 56, 58]),
    ('Academy students (School Kid, Lass, Youngster)', [108, 109, 110, 111]),
    ('Cook / barkeep (the dorm cook, the tavern barkeep)', [254, 255, 256]),
    ('Healer (the tavern healer)', [137, 138, 139, 140]),
]
PICKS = {113, 150, 156, 48, 49, 123, 125, 36, 42, 108, 254, 138}

d = open(fa_walker.ROMP, 'rb').read(); infos, pals = ow_scan.scan(d)
S = 4; cw = 3 * 16 * S + 22; cols = 8; rh = 32 * S + 24
H = 30 + sum(22 + ((len(g) + cols - 1) // cols) * rh for _, g in GROUPS)
sh = Image.new('RGBA', (cols * cw + 10, H), (40, 40, 48, 255)); dr = ImageDraw.Draw(sh)
dr.text((6, 6), 'Townsfolk walker candidates (Fantasma; standing S, N, W; * = my pick)', fill=(255, 220, 120))
y0 = 28
for title, ns in GROUPS:
    dr.text((6, y0), title, fill=(200, 200, 255)); y0 += 20
    for i, n in enumerate(ns):
        a, tag, images, w, h, size = infos[n]
        b = fa_walker.sheet_bytes(d, images, size, 3); P = np.array(pals[tag], np.uint8)
        x0 = 6 + (i % cols) * cw; y = y0 + (i // cols) * rh
        bg = Image.new('RGBA', (3 * 16 * S + 8, 32 * S), (110, 110, 125, 255))
        for k in range(3):
            px = fa_walker.tiles(b[k * size:(k + 1) * size], w, h)
            o = np.zeros((32, 16, 4), np.uint8); o[..., :3] = P[px]; o[..., 3] = (px != 0) * 255
            bg.alpha_composite(Image.fromarray(o).resize((16 * S, 32 * S), Image.NEAREST), (k * (16 * S + 4), 0))
        sh.alpha_composite(bg, (x0, y + 14))
        dr.text((x0, y), 'FA %d%s' % (n, '  *' if n in PICKS else ''), fill=(255, 255, 0))
    y0 += ((len(ns) + cols - 1) // cols) * rh
sh.save('/tmp/cult/townsfolk_cands_v1.png'); print(sh.size)
