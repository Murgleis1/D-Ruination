"""The shared Cormorian gabled cottage (user, 2026-11-15): Fort Elderflower small house D
(source cells x5-9, y41-44, 5x4), snow -> shingles on the roof and ivy on the eaves, the
same pipeline as the tavern. Approved look: houses_and_monument_options.png #1.

Fort Elderflower keeps some house art in the BOTTOM layer: interior cells and the door row
take it (unless the bottom-row cell is snowy ground); top/side rim cells never do (there
the bottom layer is the town wall).

cottage_finished() -> (W, H, mid, top): RGB layer images, -1 = transparent.
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_cormoria as b
import desnow as ds

BOX = (5, 41, 9, 44)
ROOF_UNTIL = 34


def cottage_finished():
    lay, _ = b.region_layers(b.FE, BOX)
    H, W = lay[1].shape[:2]
    snowset = np.array(ds.SNOW)
    for cy in range(H // 16):
        for cx in range(W // 16):
            sl = (slice(cy * 16, cy * 16 + 16), slice(cx * 16, cx * 16 + 16))
            b0 = lay[0][sl]
            if not (b0 >= 0).all(-1).any(): continue
            snowy = (b0[..., None, :] == snowset).all(-1).any(-1).mean()
            edge = cy == 0 or cx == 0 or cy == H // 16 - 1 or cx == W // 16 - 1
            bottom = cy == H // 16 - 1
            if edge and not bottom: continue
            if bottom and snowy > 0.6: continue
            m = ~(lay[1][sl] >= 0).all(-1) & (b0 >= 0).all(-1)
            lay[1][sl][m] = b0[m]
    wa_png = os.environ.get('WA_RENDER', os.path.join(HERE, '../../assets/monomyth_reference/woodavens.png'))
    leaves, _ = ds.leaf_patch(np.array(Image.open(wa_png).convert('RGB')).astype(int))
    prot = np.zeros((H, W), bool)
    mid, top = ds.desnow_building(lay[1], lay[2], (56, 56, 88), prot, ROOF_UNTIL, H, facade_leaves=leaves)
    c = mid[48:64, 64:80]                         # ice ground left in the bottom-right rim cell
    lum = c.sum(-1) / 3
    c[(lum > 170) & (c[..., 2] >= c[..., 0])] = -1
    for img in (mid, top):                        # roof = the tavern's dusk plum (same FE roof art ->
        for src, dst in b.PLUM.items():           # same colours -> shares the tavern's palettes)
            img[(img == np.array(src)).all(-1)] = dst
    return W // 16, H // 16, mid, top


if __name__ == '__main__':
    w, h, mid, top = cottage_finished()
    img = np.zeros(mid.shape, int); img[:] = (152, 208, 160)
    for L in (mid, top):
        m = (L >= 0).all(-1); img[m] = L[m]
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp/cottage.png'
    Image.fromarray(img.astype(np.uint8)).resize((w * 64, h * 64), Image.NEAREST).save(out)
    print(w, h)
