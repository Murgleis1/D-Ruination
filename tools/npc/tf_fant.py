import sys, struct, numpy as np
sys.path.insert(0, '/home/claude/repo/tools/fantasma')
import fsread as F
from PIL import Image, ImageDraw
d = F.ROM; isp = lambda v: 0x08000000 <= v < 0x0A000000
# CompressedSpriteSheet {ptr, u16 0x800, u16 tag=k} at a fixed stride, k = 0,1,2,...
best = (0, 0, 0)
cands = [a for a in range(0, len(d) - 8, 4) if struct.unpack_from('<HH', d, a + 4) == (0x800, 0) and isp(struct.unpack_from('<I', d, a)[0])]
for a in cands:
    for stride in range(8, 80, 4):
        n = 0
        while True:
            p, sz, t = struct.unpack_from('<IHH', d, a + stride * n)
            if sz != 0x800 or t != n or not isp(p): break
            n += 1
        if n > best[0]: best = (n, a, stride)
n, a, stride = best; print('fronts', n, hex(a), stride)
# palette: look inside the struct after frontPic for {ptr, u16 tag=k}
for po in range(8, stride, 4):
    ok = all(struct.unpack_from('<IH', d, a + stride * k + po)[1] == k and isp(struct.unpack_from('<I', d, a + stride * k + po)[0]) for k in range(5))
    if ok: break
print('pal at +', po)
cols = 12; S = 2; W, H = 64 * S + 6, 64 * S + 14
img = Image.new('RGB', (cols * W, ((n + cols - 1) // cols) * H + 20), (40, 40, 48)); dr = ImageDraw.Draw(img)
dr.text((4, 4), 'Fantasma trainer fronts (%d)' % n, fill=(255, 255, 255))
for i in range(n):
    p = struct.unpack_from('<I', d, a + stride * i)[0]; pp = struct.unpack_from('<I', d, a + stride * i + po)[0]
    try:
        o = F.off(p); b = F.lz77(o) if d[o] == 0x10 else F.unsmol(o)
        q = F.off(pp); raw = F.lz77(q)[:32] if d[q] == 0x10 else d[q:q + 32]
    except Exception as e: continue
    if len(b) < 2048: continue
    c = struct.unpack('<16H', raw); pal = np.array([((v & 31) << 3, ((v >> 5) & 31) << 3, ((v >> 10) & 31) << 3) for v in c], np.uint8)
    px = np.zeros((64, 64), np.uint8)
    for t in range(64):
        tb = np.frombuffer(b[t * 32:(t + 1) * 32], np.uint8); tile = np.zeros((8, 8), np.uint8)
        tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
        px[(t // 8) * 8:(t // 8) * 8 + 8, (t % 8) * 8:(t % 8) * 8 + 8] = tile
    rgb = pal[px]; rgb[px == 0] = (70, 70, 86)
    x, y = (i % cols) * W, (i // cols) * H + 20; dr.text((x + 2, y), str(i), fill=(255, 230, 0))
    img.paste(Image.fromarray(rgb).resize((64 * S, 64 * S), Image.NEAREST), (x, y + 12))
img.save('tf_fantasma.png'); print(img.size)
