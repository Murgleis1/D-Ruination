import sys, glob, re, os
from PIL import Image, ImageDraw
src, tag, minw = sys.argv[1], sys.argv[2], int(sys.argv[3])
files = []
for f in sorted(glob.glob(src + '/*.png')):
    im = Image.open(f)
    if im.width >= minw * 16 and im.height >= minw * 16: files.append(f)
T = 170; per = 40
for k in range(0, len(files), per):
    S = Image.new('RGB', (8 * (T + 6), 5 * (T + 16)), (24, 24, 30)); d = ImageDraw.Draw(S)
    for i, f in enumerate(files[k:k + per]):
        im = Image.open(f).convert('RGB'); sc = T / max(im.size); im = im.resize((int(im.width * sc), int(im.height * sc)), Image.LANCZOS)
        x, y = (i % 8) * (T + 6), (i // 8) * (T + 16)
        S.paste(im, (x, y + 13)); d.text((x, y), os.path.basename(f)[:-4], fill=(255, 230, 0))
    S.save('/home/claude/scratch/hhruin/sheets/%s_%02d.png' % (tag, k // per))
print(tag, len(files))
