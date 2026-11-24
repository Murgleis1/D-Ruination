"""Mirroh Peak's sky backdrop (user 2026-11-24): the moving backdrop from the top of MonoMyth's bastion castle (a sunset
over mountains), exported by the user from MonoMyth and flipped by them so the tallest mountain is on the right
(assets/mt_mirroh_reference/backdrop_bastion_flipped_src.png, 256x136 used), recoloured as asked: "the sky to more of a
light blue and the sun to a white pale to go against the dark mountains in the distance".

Recolour, colour by colour (each of its 14 colours keeps its role): the sky's bands become light blues, palest toward the
horizon; its clouds paler still; the sun and its halo pale white; the mountains dark cold slate, their lit ridges a
step lighter, the far range behind them a hazy blue-grey.
Mock (before any engine work): what the player would see at a few places on the summit, the backdrop showing wherever
the sky does. Movement as MonoMyth's: the backdrop stays put across (distant), and slides up as the player climbs
down / down as they come up toward the summit (a fraction of the camera's own movement), so the mountains rise into
the gaps between the ledges lower down and the peak and sun crown the plateau.
Usage: python3 backdrop.py OUTDIR"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
SRC = os.path.join(REPO, 'assets', 'mt_mirroh_reference', 'backdrop_bastion_flipped_src.png')
BH = 136
RECOLOUR = {
    (148, 140, 99): (112, 164, 222),   # the sky's top (deepest blue)
    (173, 140, 99): (128, 178, 230),   # its upper cloud band
    (198, 148, 90): (146, 192, 238),   # upper sky
    (222, 148, 90): (166, 206, 244),   # the main sky
    (247, 156, 90): (188, 220, 248),   # lower sky, clouds
    (255, 173, 90): (208, 232, 252),   # bright clouds near the horizon
    (255, 189, 90): (224, 240, 254),   # cloud highlights
    (255, 222, 123): (238, 246, 255),  # the sun's halo
    (255, 255, 206): (252, 254, 255),  # the sun: pale white
    (132, 107, 74): (54, 64, 90),      # the mountains (dark, cold)
    (132, 99, 66): (44, 52, 76),       # their darkest bits
    (148, 115, 74): (84, 98, 130),     # their lit ridges
    (206, 123, 82): (96, 112, 148),    # the far range's edge, the path
    (173, 115, 82): (116, 134, 170),   # the far range behind (haze)
}

def backdrop():
    a = np.array(Image.open(SRC).convert('RGB'))[:BH]
    out = a.copy()
    for k, v in RECOLOUR.items(): out[(a == k).all(-1)] = v
    left = {tuple(c) for c in a.reshape(-1, 3)} - set(RECOLOUR)
    assert not left, left
    return out

def view(full, sky_a, bd, px, py, fy=0.15, y0=-8):
    """the 240x160 screen centred on the player at cell (px, py), the backdrop behind the sky"""
    H, W = sky_a.shape
    cx = min(max(px * 16 + 8 - 120, 0), W - 240); cy = min(max(py * 16 + 8 - 80, -8), H - 160)
    scr = np.zeros((160, 240, 3), np.uint8); m = np.zeros((160, 240), bool)
    ys, ye = max(cy, 0), cy + 160
    scr[ys - cy:, :] = full[ys:ye, cx:cx + 240]; m[ys - cy:, :] = sky_a[ys:ye, cx:cx + 240]
    m[:ys - cy, :] = True                                             # (above the map's top edge: sky too)
    top = int(round(-(cy - y0) * fy))                                  # (the backdrop's top on screen)
    sky = np.zeros((160, 240, 3), np.uint8)
    for y in range(160):
        by = y - top
        if by < 0: sky[y] = bd[0, 8]
        elif by >= BH: sky[y] = bd[BH - 1, 8]
        else: sky[y] = bd[by, 8:248]
    scr[m] = sky[m]
    return scr

def main(outdir):
    sys.path.insert(0, HERE)
    import compose_peak as CP
    bd = backdrop(); Image.fromarray(bd).save(os.path.join(outdir, 'peak_backdrop_v1.png'))
    r = CP.compose()
    spots = [((20, 4), 'top of the plateau, by the huts'), ((15, 9), 'the plateau, its west side'), ((12, 17), 'the first ledge, west'),
             ((37, 21), 'the second ledge, east'), ((8, 27), 'the third ledge, west'), ((40, 33), 'the last ledge, east')]
    sh = Image.new('RGB', (3 * 480 + 20, 2 * (320 + 22)), (24, 24, 30)); d = ImageDraw.Draw(sh)
    for i, ((x, y), n) in enumerate(spots):
        s = view(r['flat'], r['sky_a'], bd, x, y)
        sh.paste(Image.fromarray(s).resize((480, 320), Image.NEAREST), ((i % 3) * 490, (i // 3) * 342 + 20))
        d.text(((i % 3) * 490 + 2, (i // 3) * 342 + 4), n, fill=(255, 230, 120))
    sh.save(os.path.join(outdir, 'peak_backdrop_mock_v1.png'))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/tmp')
