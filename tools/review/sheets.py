import sys, os, subprocess
sys.path.insert(0, '/home/claude/scratch/review')
from maps import CH1
from PIL import Image, ImageDraw, ImageFont
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)
O = '/home/claude/scratch/review/r'; os.makedirs(O, exist_ok=True)
sys.path.insert(0, '/home/claude/repo/tools/art')
import render_own_map as R
from PIL import Image as I
for k, (area, ms) in enumerate(CH1.items()):
    ims = []
    for m in ms:
        p = f'{O}/{m}.png'
        if not os.path.exists(p): I.fromarray(R.render(m)).save(p)
        ims.append((m, Image.open(p)))
    T = 330 if len(ms) > 6 else 640
    thumbs = []
    for m, im in ims:
        sc = min(1.0, T / max(im.size)); thumbs.append((m, im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)))
    W = 1400; x = y = 0; rowh = 0; pos = []
    for m, im in thumbs:
        if x + im.width > W: x = 0; y += rowh + 22; rowh = 0
        pos.append((x, y, m, im)); x += im.width + 8; rowh = max(rowh, im.height)
    S = Image.new('RGB', (W, y + rowh + 50), (22, 22, 28)); d = ImageDraw.Draw(S)
    d.text((6, 4), area, font=F, fill=(255, 255, 255))
    for x, y, m, im in pos: S.paste(im, (x, y + 46)); d.text((x, y + 28), m, font=F, fill=(255, 230, 120))
    S.save(f'/home/claude/scratch/review/sheet_{k}.png'); print(k, area, S.size)
