import sys, os
sys.path.insert(0, '/home/claude/repo/tools/monomyth')
import numpy as np
from PIL import Image
import build_cormoria as b, desnow as ds

def layers(a, box):
    x0, y0, x1, y1 = box; W, H = x1 - x0 + 1, y1 - y0 + 1
    lay = [np.full((H * 16, W * 16, 3), -1, int) for _ in range(3)]
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            e, _ = b.src_metatile(a, b.cell(a, x, y))
            for L in range(3):
                for q in range(4):
                    im = b.quad_img(a, e[L * 4 + q])
                    if im is None: continue
                    oy, ox = (y - y0) * 16 + (q // 2) * 8, (x - x0) * 16 + (q % 2) * 8
                    m = (im >= 0).all(-1); lay[L][oy:oy + 8, ox:ox + 8][m] = im[m]
    return lay

def comp(lay, ground=(184, 216, 168)):
    out = np.zeros(lay[1].shape, int); out[:] = ground
    for L in lay[1:]:
        m = (L >= 0).all(-1); out[m] = L[m]
    return out.clip(0, 255).astype(np.uint8)

wa = np.array(Image.open('/home/claude/repo/assets/monomyth_reference/woodavens.png').convert('RGB')).astype(int)
leaves, _ = ds.leaf_patch(wa)
HOUSES = {'H cottage': ((24, 50, 28, 53), 34), 'D cottage': ((5, 41, 9, 44), 34),
          'E steep-roof': ((17, 39, 21, 44), 70), 'B steep-roof': ((37, 25, 41, 30), 70)}
res = {}
for name, (box, roof_until) in HOUSES.items():
    lay = layers(b.FE, box); Hp = lay[1].shape[0]
    snowset = np.array(ds.SNOW)
    for cy in range(Hp // 16):
        for cx in range(lay[1].shape[1] // 16):
            sl = (slice(cy * 16, cy * 16 + 16), slice(cx * 16, cx * 16 + 16))
            b0 = lay[0][sl]
            if not (b0 >= 0).all(-1).any(): continue
            snowy = (b0[..., None, :] == snowset).all(-1).any(-1).mean()
            edge = cy == 0 or cx == 0 or cy == Hp // 16 - 1 or cx == lay[1].shape[1] // 16 - 1
            bottom = cy == Hp // 16 - 1
            if edge and not bottom: continue             # top/side rim: bottom layer is wall, never house
            if bottom and snowy > 0.6: continue          # bottom rim: snowy ground stays ground
            m = ~(lay[1][sl] >= 0).all(-1) & (b0 >= 0).all(-1)
            lay[1][sl][m] = b0[m]
    prot = np.zeros(lay[1].shape[:2], bool)
    if name.startswith('E'):                     # castle wall behind the steep roof's top corners
        wallc = np.unique(lay[1][0:16, 0:16].reshape(-1, 3), axis=0)
        wallc = wallc[(wallc >= 0).all(-1)]
        for cx in (0, 1, 3, 4):
            for L in (1, 2):
                c = lay[L][0:16, cx * 16:cx * 16 + 16]
                m = (c[..., None, :] == wallc).all(-1).any(-1); c[m] = -1
    mid, top = ds.desnow_building(lay[1], lay[2], (56, 56, 88), prot, roof_until, Hp, facade_leaves=leaves)
    was = ds.snow_mask(lay[1], prot) | ds.snow_mask(lay[2], prot)
    if name.startswith('E'):                     # centre stripe: copy the real shingles from 16px beside it
        cx0, cx1 = 26, 54
        for y in range(4, roof_until):
            for x in range(cx0, cx1):
                if not was[y, x] or (top[y, x] >= 0).all(): continue
                sx = x - 16 if x < 40 else x + 16
                src = top[y, sx] if (top[y, sx] >= 0).all() else mid[y, sx]
                if (src >= 0).all() and not was[y, sx]: mid[y, x] = src
    if name.startswith('D'):                     # ice ground left in the bottom-right rim cell
        c = mid[48:64, 64:80]
        lum = c.sum(-1) / 3
        c[(lum > 170) & (c[..., 2] >= c[..., 0])] = -1
    res[name] = (comp([None, lay[1], lay[2]]), comp([None, mid, top]))
S = 4; tiles = []
for name, (before, after) in res.items():
    h, w = before.shape[:2]
    c = Image.new('RGB', (w * S * 2 + 12, h * S), 'white')
    c.paste(Image.fromarray(before).resize((w * S, h * S), Image.NEAREST), (0, 0))
    c.paste(Image.fromarray(after).resize((w * S, h * S), Image.NEAREST), (w * S + 12, 0)); tiles.append((name, c))
Wt = max(c.width for _, c in tiles); Ht = sum(c.height + 30 for _, c in tiles)
from PIL import ImageDraw, ImageFont
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
s = Image.new('RGB', (Wt, Ht), 'white'); d = ImageDraw.Draw(s); y = 0
for name, c in tiles:
    d.text((4, y + 4), name + '   (source | snow -> shingles + ivy)', fill='black', font=F); s.paste(c, (0, y + 28)); y += c.height + 30
s.save('os.environ.get('OUT', '/tmp/fe_houses_desnow.png')'); print(s.size)
