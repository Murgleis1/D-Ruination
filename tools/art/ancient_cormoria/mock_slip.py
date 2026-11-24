"""Mock v2 of the Ancient Cormoria slip as the player sees it: 240x160 screens at the places along the way, the ancient
backdrop (backdrop_ancient.py) behind the sky as the game draws it (pinned across the screen, sliding a fraction of the
camera's vertical movement: field_camera.c's backdrop), and a whole-map overview. In the overview the sky is left a
plain colour: the backdrop is pinned to the screen, so no one picture of the whole map can show it truly (mock v1's
overview tiled it, which read as a cut-off band and three suns); the screens along the rim show it as it is.
Usage: python3 mock_slip.py OUTDIR"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import compose_slip as C
import backdrop_ancient as BA
import tilesolve as T

def view(flat, sky_a, bd, px, py):
    """the screen with the player at cell (px, py), as field_camera.c draws it: camera clamped to the map (8 px of
    border above), the backdrop's top at 8 - (camY + 8) * 3 / 20 (+ the Peak's lift), its rows past the bottom the
    mountains' colour, above its top the sky's top colour"""
    H, W = sky_a.shape
    cx = min(max(px * 16 + 8 - 120, 0), W - 240); cy = min(max(py * 16 + 8 - 80, -8), H - 160)
    scr = np.zeros((160, 240, 3), np.uint8); m = np.zeros((160, 240), bool)
    ys = max(cy, 0)
    scr[ys - cy:] = flat[ys:cy + 160, cx:cx + 240]; m[ys - cy:] = sky_a[ys:cy + 160, cx:cx + 240]; m[:ys - cy] = True
    top = 8 - (cy + 8) * 3 // 20 + 8
    sky = np.zeros((160, 240, 3), np.uint8)
    for y in range(160):
        by = y - top
        sky[y] = bd[0, 8] if by < 0 else bd[BA.BH - 1, 8] if by >= BA.BH else bd[by, 8:248]
    scr[m] = sky[m]
    return scr

SPOTS = [((24, 50), 'arrival: the south altar'), ((24, 45), 'under the ribs'), ((35, 43), 'the skull and the spine'),
         ((24, 37), 'up the step'), ((37, 27), 'the oasis'), ((24, 25), 'the rope bridge'),
         ((39, 21), 'the falls'), ((7, 23), 'the cliff homes'), ((24, 18), 'the mesa ladder'),
         ((24, 12), 'up the neck to the summit'), ((24, 6), 'the north altar'), ((20, 7), 'the summit, west rim')]

def main(outdir, tag='v2'):
    r = C.compose(); bd = BA.backdrop()
    flat = r['bottom'].copy(); flat[r['top_a']] = r['top'][r['top_a']]
    cols = 3; rows = (len(SPOTS) + cols - 1) // cols
    sh = Image.new('RGB', (cols * 490, rows * 342), (24, 22, 28)); d = ImageDraw.Draw(sh)
    for i, ((x, y), n) in enumerate(SPOTS):
        s = view(flat, r['sky_a'], bd, x, y)
        sh.paste(Image.fromarray(s).resize((480, 320), Image.NEAREST), ((i % cols) * 490, (i // cols) * 342 + 20))
        d.text(((i % cols) * 490 + 2, (i // cols) * 342 + 4), n, fill=(255, 230, 160))
    sh.save(os.path.join(outdir, 'slip_mock_views_%s.png' % tag))
    ov = flat.copy(); ov[r['sky_a']] = (110, 22, 26)
    Image.fromarray(ov).save(os.path.join(outdir, 'slip_mock_overview_%s.png' % tag))
    Image.fromarray(T.seam_map(T.render(r['grid']), r['seams'])).save(os.path.join(outdir, 'slip_seams_%s.png' % tag))
    print('seams:', len(r['seams']), '| props:', len(r['props']))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/tmp')
