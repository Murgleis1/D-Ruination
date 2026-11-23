"""The Citadel's two pockets (user 2026-11-22): the sparring ground (west) and the Braviary landing ground (east).
pad.png: a round stone landing pad, 80x80 (5x5 cells), Elderflower's stone greys, inlaid with Arceus's golden wheel (a
ring and four spokes, the church's gold); drawn here, plain geometry.
braviary_*.png: the expansion's Braviary follower sprite (its down and side frames), for placing (stage 2 objects)."""
import numpy as np
from PIL import Image, ImageDraw
R = 40; S = 80
img = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
OUT, D, M, L, T = (40, 40, 54, 255), (78, 78, 94, 255), (104, 104, 120, 255), (130, 130, 144, 255), (156, 156, 168, 255)
G0, G1, G2 = (112, 76, 28, 255), (192, 142, 44, 255), (244, 214, 116, 255)
d.ellipse((0, 4, S - 1, S - 1), fill=OUT)                    # (its rim's shadow side, the disc seen a little from above)
d.ellipse((1, 1, S - 2, S - 5), fill=OUT); d.ellipse((2, 2, S - 3, S - 6), fill=M)
d.ellipse((5, 5, S - 6, S - 9), fill=L)                      # (the paving within its kerb)
for k in range(0, 360, 30):                                  # (flagstone joints radiating)
    a = np.radians(k); d.line((S / 2, (S - 4) / 2, S / 2 + 33 * np.cos(a), (S - 4) / 2 + 31 * np.sin(a)), fill=M, width=1)
cx, cy = S / 2 - 0.5, (S - 4) / 2 - 0.5
d.ellipse((cx - 22, cy - 21, cx + 22, cy + 21), outline=G0, width=4)        # the golden wheel: its ring
d.ellipse((cx - 21, cy - 20, cx + 21, cy + 20), outline=G1, width=2)
d.ellipse((cx - 20, cy - 19, cx + 20, cy + 19), outline=G2, width=1)
for (dx, dy) in ((0, -1), (0, 1), (-1, 0), (1, 0)):                       # its four spokes, to a hub
    d.line((cx + dx * 6, cy + dy * 6, cx + dx * 20, cy + dy * 19), fill=G1, width=3)
    d.line((cx + dx * 6, cy + dy * 6, cx + dx * 20, cy + dy * 19), fill=G2, width=1)
d.ellipse((cx - 6, cy - 6, cx + 6, cy + 6), fill=G1, outline=G0); d.ellipse((cx - 3, cy - 3, cx + 3, cy + 3), fill=G2)
img.save('pad.png')
b = Image.open('/home/claude/repo/codebase/graphics/pokemon/braviary/overworld.png')
a = np.array(b.convert('RGBA')); idx = np.array(b); a[idx == 0, 3] = 0
Image.fromarray(a[:, 0:32]).save('braviary_down.png'); Image.fromarray(a[:, 128:160]).save('braviary_left.png')
print('pad', img.size)
