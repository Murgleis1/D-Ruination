"""Children walker candidates (user 2026-11-26: "If you need any children overworld sprites, there's a ton in
MonoMyth and the other games"). MonoMyth's short walkers (figure under 20 px tall in its catalogue, the non-children
dropped by eye) and Fantasma's youngsters. Pelluca needs a boy (Emerald's Boy 2) and a small child (the Tuber).
Run: python3 children_cands.py -> /tmp/cult/children_cands_v1.png"""
import sys
sys.path.insert(0, '/home/claude/repo/tools/npc')
import fa_walker, ow_scan, numpy as np
from PIL import Image, ImageDraw
cat = Image.open('/home/claude/repo/assets/monomyth_ow/catalogue_ow16x32.png').convert('RGB')
MM = [192, 94, 134, 50, 193, 29, 59, 237, 48]
FA = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59]
d = open(fa_walker.ROMP, 'rb').read(); infos, pals = ow_scan.scan(d)
S = 3; cw = 4 * 16 * S + 14; rh = 32 * S + 22; cols = 7
H = 40 + ((len(MM) + cols - 1) // cols) * rh + 30 + ((len(FA) + cols - 1) // cols) * rh
sh = Image.new('RGB', (cols * cw + 10, H), (40, 40, 48)); dr = ImageDraw.Draw(sh)
dr.text((6, 4), 'Children: MonoMyth (S, S, N, W as catalogued)', fill=(255, 220, 120))
y0 = 22
for i, n in enumerate(MM):
    r, c = divmod(n, 10); cell = cat.crop((c * 202, r * 110 + 12, c * 202 + 192, r * 110 + 108))
    x = 6 + (i % cols) * cw; y = y0 + (i // cols) * rh
    dr.text((x, y), 'MM %d' % n, fill=(255, 255, 0)); sh.paste(cell, (x, y + 14))
y0 += ((len(MM) + cols - 1) // cols) * rh + 8
dr.text((6, y0), 'Children: Fantasma (S, N, W)', fill=(255, 220, 120)); y0 += 18
for i, n in enumerate(FA):
    a, tag, images, w, h, size = infos[n]; b = fa_walker.sheet_bytes(d, images, size, 3); P = np.array(pals[tag], np.uint8)
    x = 6 + (i % cols) * cw; y = y0 + (i // cols) * rh
    dr.text((x, y), 'FA %d' % n, fill=(255, 255, 0))
    bg = Image.new('RGB', (3 * 16 * S + 8, 32 * S), (110, 110, 125))
    for k in range(3):
        px = fa_walker.tiles(b[k * size:(k + 1) * size], w, h); o = np.zeros((32, 16, 3), np.uint8); o[:] = (110, 110, 125)
        for v in range(1, 16):
            o[px == v] = P[v]
        bg.paste(Image.fromarray(o).resize((16 * S, 32 * S), Image.NEAREST), (k * (16 * S + 4), 0))
    sh.paste(bg, (x, y + 14))
sh.save('/tmp/cult/children_cands_v1.png'); print(sh.size)
