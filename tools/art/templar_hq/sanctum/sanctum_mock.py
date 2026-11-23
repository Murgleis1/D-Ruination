"""The Sanctum (user 2026-11-22: a holy library at the top of the cathedral's cross tower, a lost repository of
knowledge and secret tomes, where the player communes with Arceus and faces their shadow self; unlocked by defeating
Ambrose). Source: Fantasma's castle library (its mapsec 1, layout s001_b68c, 17x15; credit the Fantasma team, with
permission before release): three arched alcoves of books along the back wall, chests of drawers, lecterns with
open tomes, a writing desk, candelabras, and a glowing circle in the floor (where the shadow self rises); the stair
down at its foot. Recoloured to the cathedral's own: its violet stone to the church's cream ramp by lightness, its
skull banners to the Order's blue with Arceus's golden wheel, the circle's cold cyan to the church's gold and glass
blue. The cobwebs stay: it is a lost repository.
Usage: python3 sanctum_mock.py [out.png]"""
import sys
import numpy as np
from PIL import Image, ImageDraw
a = np.array(Image.open('source_fantasma_b68c.png').convert('RGB')).astype(int)
r, g, b = a[..., 0], a[..., 1], a[..., 2]
lum = .30 * r + .59 * g + .11 * b
out = a.copy()
# the violet stone (grey with blue over red, little saturation) -> the church's stone, dark outline to cream lights
stone = (b >= r) & (b - r <= 32) & (np.abs(r - g) <= 20) & (lum > 3)
RAMP = np.array([(22, 24, 38), (40, 44, 64), (70, 64, 60), (102, 92, 74), (128, 116, 92), (152, 140, 112),
                 (174, 162, 134), (194, 184, 158), (212, 205, 186), (230, 226, 214)])
t = np.clip(lum / 190.0, 0, 1)
out[stone] = RAMP[np.clip((t[stone] * (len(RAMP) - 1)).round().astype(int), 0, len(RAMP) - 1)]
# the cyan glow -> glass blue (the church's), its brightest to white-gold
cyan = (b > r + 40) & (g > r + 30)
GLOW = np.array([(34, 40, 89), (62, 74, 163), (0, 128, 255), (108, 182, 255), (236, 238, 250)])
t2 = np.clip((lum - 60) / 190.0, 0, 1)
out[cyan] = GLOW[np.clip((t2[cyan] * (len(GLOW) - 1)).round().astype(int), 0, len(GLOW) - 1)]
# the banners' violet -> the Order's blue; their skulls -> plain gold, over which Arceus's wheel is drawn
purple = (r > g + 25) & (b > g + 30)
out[purple] = np.array([(34, 40, 89), (51, 60, 128), (62, 74, 163)])[np.clip(((lum[purple] - 30) / 30).astype(int), 0, 2)]
img = Image.fromarray(out.astype(np.uint8)); d = ImageDraw.Draw(img)
G0, G1, G2 = (112, 76, 28), (192, 142, 44), (244, 214, 116)
for bx in (80, 176):                                   # (the two banners, x bx..bx+15, rows 8-46: repainted whole)
    x0, x1, y0, y1 = bx + 2, bx + 13, 9, 43
    for y in range(6, 47):                                # (clear the old banner back to the wall behind it)
        for x in range(bx, bx + 16):
            if purple[y, x] or (r[y, x] > 150 and g[y, x] > 110 and b[y, x] < 140) or (lum[y, x] < 30 and x0 <= x <= x1 and y0 - 1 <= y <= y1 + 2):
                img.putpixel((x, y), tuple(int(v) for v in RAMP[3]))
    d.rectangle((x0 - 1, y0 - 2, x1 + 1, y0 - 1), fill=G0)                     # (its rod)
    d.polygon([(x0, y0), (x1, y0), (x1, y1), ((x0 + x1) / 2, y1 + 3), (x0, y1)], fill=(51, 60, 128), outline=(22, 24, 38))
    d.line((x0 + 1, y0 + 1, x0 + 1, y1 - 1), fill=(62, 74, 163))
    cx, cy = (x0 + x1) / 2, 25
    d.ellipse((cx - 4.5, cy - 4.5, cx + 4.5, cy + 4.5), outline=G1)
    for (dx, dy) in ((0, -1), (0, 1), (-1, 0), (1, 0)): d.line((cx, cy, cx + dx * 4, cy + dy * 4), fill=G2)
    d.line((x0 + 1, y1 - 3, x1 - 1, y1 - 3), fill=G1)                        # (a gold hem)
# the two narrow windows (x 101-107 and 165-171, rows 18-35): stained glass, the church's own colours (blue at the
# heart, rose and magenta at the edges, lead lines between), echoing the tower's windows outside
GL = {0: (0, 128, 255), 1: (108, 182, 255), 2: (255, 117, 186), 3: (255, 0, 255), 4: (236, 238, 250)}
for wx in (101, 165):
    for y in range(18, 36):
        for x in range(wx, wx + 7):
            if lum[y, x] >= 30: continue
            dx = x - wx; band = (y - 18) // 4
            if dx in (0, 6) or (y - 18) % 4 == 3: c = (40, 44, 64)                  # (the lead)
            elif dx in (1, 5): c = GL[3 if band % 2 else 2]
            elif dx == 3 and band == 1: c = GL[4]
            else: c = GL[1 if band % 2 else 0]
            img.putpixel((x, y), c)
img.save(sys.argv[1] if len(sys.argv) > 1 else 'sanctum_mock.png')
