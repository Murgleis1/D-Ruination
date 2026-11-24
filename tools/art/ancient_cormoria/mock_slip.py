"""Mock of the Ancient Cormoria slip as the player would see it (240x160 screens at a few places), the ancient
backdrop (backdrop_ancient.py) behind the sky with the Peak's parallax (fixed across, a fraction of the camera's
vertical movement), and a whole-map overview. Usage: python3 mock_slip.py OUTDIR"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import compose_slip as C
import backdrop_ancient as BA

def view(flat, sky_a, bd, px, py, fy=0.15, lift=-8):
    H, W = sky_a.shape
    cx = min(max(px * 16 + 8 - 120, 0), W - 240); cy = min(max(py * 16 + 8 - 80, -8), H - 160)
    scr = np.zeros((160, 240, 3), np.uint8); m = np.zeros((160, 240), bool)
    ys = max(cy, 0)
    scr[ys - cy:] = flat[ys:cy + 160, cx:cx + 240]; m[ys - cy:] = sky_a[ys:cy + 160, cx:cx + 240]; m[:ys - cy] = True
    top = int(round(-(cy + 8) * fy)) - lift
    sky = np.zeros((160, 240, 3), np.uint8)
    for y in range(160):
        by = y - top
        sky[y] = bd[0, 8] if by < 0 else bd[BA.BH - 1, 8] if by >= BA.BH else bd[by, 8:248]
    scr[m] = sky[m]
    return scr

def main(outdir):
    r = C.compose(); bd = BA.backdrop()
    flat = r['bottom'].copy(); flat[r['top_a']] = r['top'][r['top_a']]
    spots = [((24, 11), 'the north altar, on the rim'), ((24, 15), 'up the mesa ladder, the carved panels'),
             ((24, 27), 'the rope bridge below the falls'), ((10, 24), 'the cliff homes, the river'),
             ((24, 44), 'under the ribs'), ((24, 49), 'arrival: the south altar')]
    sh = Image.new('RGB', (3 * 490, 2 * 342), (24, 22, 28)); d = ImageDraw.Draw(sh)
    for i, ((x, y), n) in enumerate(spots):
        s = view(flat, r['sky_a'], bd, x, y)
        sh.paste(Image.fromarray(s).resize((480, 320), Image.NEAREST), ((i % 3) * 490, (i // 3) * 342 + 20))
        d.text(((i % 3) * 490 + 2, (i // 3) * 342 + 4), n, fill=(255, 230, 160))
    sh.save(os.path.join(outdir, 'slip_mock_views_v1.png'))
    ov = flat.copy()                                  # (the overview: the backdrop once, centred above the canyon's rim)
    H, W = r['sky_a'].shape; sk = np.zeros_like(ov); sk[:] = bd[0, 8]
    oy = 14 * 16 - BA.BH; ox = (W - BA.BW) // 2
    sk[max(0, oy):oy + BA.BH, ox:ox + BA.BW] = bd[max(0, -oy):]
    sk[oy + BA.BH:] = bd[BA.BH - 1, 8]
    for x0 in range(ox - BA.BW, -BA.BW, -BA.BW): sk[max(0, oy):oy + BA.BH, max(0, x0):x0 + BA.BW] = bd[max(0, -oy):, max(0, -x0):]
    for x0 in range(ox + BA.BW, W, BA.BW): sk[max(0, oy):oy + BA.BH, x0:min(W, x0 + BA.BW)] = bd[max(0, -oy):, :min(BA.BW, W - x0)]
    ov[r['sky_a']] = sk[r['sky_a']]
    Image.fromarray(ov).save(os.path.join(outdir, 'slip_mock_overview_v1.png'))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/tmp')
