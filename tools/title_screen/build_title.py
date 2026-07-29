#!/usr/bin/env python3
"""
Build graphics/title_screen/dr_title.png from the high-resolution sources.

WHY THIS EXISTS
---------------
The previous dr_title.png was a 240x160 image carrying 253 of 256 colours with
heavy error-diffusion dithering -- an 8x8 patch of plain SKY used 24 distinct
colours, and the mean horizontal run of identical pixels was 1.27px. On real
hardware that dither blends optically and looks like a smooth gradient; at 6x on
a modern LCD it magnifies into noise, and mGBA's default bilinear filter then
averages the noise into mush. That is the "blurry title screen".

The fix is not a better filter. It is to stop dithering. Measured on the new
source, 256 colours reproduce the downscaled art with a mean error of only 1.85
per channel, so dithering buys nothing at all and costs all the crispness.

PIPELINE
--------
1. Crop the 1376x768 (1.79:1) source to 3:2 for the GBA. Only the WIDTH can be
   cut, so 224px come off -- taken entirely from the RIGHT, which centres
   Chien-Pao (detected at x=530 by its dark body in the mid-ground band) at 46%
   across and preserves the left cliff whole.
2. Downscale 1152x768 -> 240x160 with a BOX filter. This is area-averaging: each
   output pixel is the mean of ~23 source pixels. The source is NOT on a clean
   pixel grid (81,220 unique colours, 1.30px runs -- pixel-art styled but noisy),
   so this averaging is what removes the per-pixel noise.
3. Quantise to 64 colours with NO dithering. 64 was chosen over 256 from a
   measured tradeoff: run length 2.28px vs 1.78px, at an error cost of 3.49 vs
   1.85. Fewer colours force flat regions, and flat regions are what "crisp"
   actually means at this size.
4. Composite the logo and subtitle as flat-tone hard-edged shapes. Because
   nothing is dithered, these stay perfectly crisp baked into the 8bpp
   background -- no sprite layer is needed for them.

The subtitle is rendered at 6x the target point size and then thresholded, which
gives clean letterforms; rendering straight at 25px would produce antialiased
grey fringes that the quantiser would then scatter.

Both subtitle lines use ONE point size. An earlier revision fitted each line to
its own target width, which silently made "Ruination" 28pt against
"Dreamstone" at 27pt -- the words should differ in width because they differ in
length, not because the type is a different size.

OUTPUT CONTRACT
---------------
dr_title.png must be mode P with a full 256-entry palette, because
src/title_screen.c:607 does LoadPalette(sDrTitlePal, BG_PLTT_ID(0),
16 * PLTT_SIZE_4BPP) -- it copies a fixed 512 bytes. A short palette would
under-fill it. The image must also stay 240x160 so gbagfx emits exactly 600
undeduplicated 8bpp tiles (38400 bytes) and the committed dr_title.bin tilemap,
which is a plain linear 0..599 map, remains valid.

Usage: python3 tools/title_screen/build_title.py [--pt N] [--colors N]
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"
OUT = HERE.parents[1] / "codebase" / "graphics" / "title_screen" / "dr_title.png"

SCREEN = (240, 160)
LOGO_W = 112
LOGO_Y = 5
FILL = (248, 248, 248)
INK = (16, 16, 24)
SS = 6                       # supersample factor for text rendering


def build_background(colors):
    im = Image.open(SRC / "ruination_widescreen.png").convert("RGB")
    w, h = im.size
    keep = int(round(h * SCREEN[0] / SCREEN[1]))      # 1152
    im = im.crop((0, 0, keep, h))                     # trim from the RIGHT
    im = im.resize(SCREEN, Image.BOX)
    return im.quantize(colors=colors, dither=Image.Dither.NONE).convert("RGB")


def build_logo():
    lg = Image.open(SRC / "pokemon_logo_mono.png").convert("LA")
    a = np.array(lg)
    ys, xs = np.where(a[:, :, 1] > 0)
    lg = lg.crop((xs.min(), ys.min(), xs.max() + 1, ys.max() + 1))
    h = round(lg.size[1] * LOGO_W / lg.size[0])
    lg = lg.resize((LOGO_W, h), Image.LANCZOS)
    a = np.array(lg).astype(int)
    lum, alpha = a[:, :, 0], a[:, :, 1]
    rgb = np.zeros((h, LOGO_W, 3), np.uint8)
    rgb[lum > 140] = FILL
    rgb[lum <= 140] = INK
    return rgb, alpha > 128


def hard_text(text, pt):
    """Render at SS x size then threshold, for hard edges at native resolution."""
    f = ImageFont.truetype(str(SRC / "MAGIC.TTF"), pt * SS)
    b = f.getbbox(text)
    im = Image.new("L", (b[2] - b[0] + SS * 4, b[3] - b[1] + SS * 4), 0)
    ImageDraw.Draw(im).text((SS * 2 - b[0], SS * 2 - b[1]), text, font=f, fill=255)
    im = im.resize((im.size[0] // SS, im.size[1] // SS), Image.BOX)
    m = np.array(im) > 110
    ys, xs = np.where(m)
    return m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def stamp(canvas, mask, ox, oy):
    """Draw mask in FILL with a 1px INK outline."""
    d = np.zeros_like(mask)
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            d |= np.roll(np.roll(mask, dy, 0), dx, 1)
    h, w = mask.shape
    reg = canvas[oy:oy + h, ox:ox + w]
    reg[d & ~mask] = INK
    reg[mask] = FILL


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pt", type=int, default=25)
    ap.add_argument("--colors", type=int, default=64)
    ap.add_argument("--byline", default=None,
                    help='optional bottom line, e.g. "A PREQUEL BY MURGLEIS"')
    ap.add_argument("--byline-pt", type=int, default=13)
    a = ap.parse_args()

    canvas = np.array(build_background(a.colors)).copy()
    logo, opaque = build_logo()
    lx = (SCREEN[0] - LOGO_W) // 2
    reg = canvas[LOGO_Y:LOGO_Y + logo.shape[0], lx:lx + LOGO_W]
    reg[opaque] = logo[opaque]

    l1, l2 = hard_text("Dreamstone", a.pt), hard_text("Ruination", a.pt)
    y = LOGO_Y + logo.shape[0] + 4
    stamp(canvas, l1, (SCREEN[0] - l1.shape[1]) // 2, y)
    y2 = y + l1.shape[0] + 2
    stamp(canvas, l2, (SCREEN[0] - l2.shape[1]) // 2, y2)
    bottom = y2 + l2.shape[0]

    if a.byline:
        bl = hard_text(a.byline, a.byline_pt)
        by = SCREEN[1] - bl.shape[0] - 3
        stamp(canvas, bl, (SCREEN[0] - bl.shape[1]) // 2, by)

    img = Image.fromarray(canvas)
    n = len(np.unique(canvas.reshape(-1, 3), axis=0))
    assert n <= 256, f"{n} colours exceeds the 8bpp budget"
    img = img.quantize(colors=256, dither=Image.Dither.NONE)

    # pad to a full 256-entry palette; title_screen.c copies a fixed 512 bytes
    pal = img.getpalette() or []
    pal = list(pal) + [0] * (768 - len(pal))
    img.putpalette(pal[:768])

    img.save(OUT)
    print(f"wrote {OUT}")
    print(f"  mode={img.mode} size={img.size} palette entries={len(img.getpalette())//3}")
    print(f"  distinct colours used: {n}")
    print(f"  logo {LOGO_W}x{logo.shape[0]} at y={LOGO_Y}; subtitle {a.pt}pt ends y={bottom}")


if __name__ == "__main__":
    main()
