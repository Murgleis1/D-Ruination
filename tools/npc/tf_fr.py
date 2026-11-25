import sys, struct, numpy as np
from PIL import Image, ImageDraw
from ow_scan import lz77, isp
def runs(d):
    out = []; a = 0
    while a < len(d) - 8:
        p, sz, t = struct.unpack_from('<IHH', d, a)
        if sz in (0x800, 0x1000) and t == 0 and isp(p):
            n = 0
            while True:
                p, sz, t = struct.unpack_from('<IHH', d, a + 8 * n)
                if sz not in (0x800, 0x1000) or t != n or not isp(p): break
                n += 1
            if n > 60: out.append((a, n))
            a += 8 * max(n, 1); continue
        a += 4
    return out
def palrun(d, n, avoid):
    best = None
    for a in range(0, len(d) - 8, 4):
        p, t, z = struct.unpack_from('<IHH', d, a)
        if t != 0 or z != 0 or not isp(p) or a in avoid: continue
        k = 0
        while k < n:
            p, t, z = struct.unpack_from('<IHH', d, a + 8 * k)
            if t != k or z != 0 or not isp(p): break
            k += 1
        if k >= n - 2 and (best is None): best = a
    return best
def decode(d, p, sz):
    q = p - 0x08000000
    b = lz77(d, q) if d[q] == 0x10 else d[q:q + sz]
    b = b[:2048]; px = np.zeros((64, 64), np.uint8)
    for t in range(64):
        tb = np.frombuffer(b[t * 32:(t + 1) * 32], np.uint8); tile = np.zeros((8, 8), np.uint8)
        tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
        px[(t // 8) * 8:(t // 8) * 8 + 8, (t % 8) * 8:(t % 8) * 8 + 8] = tile
    return px
def pal(d, p):
    q = p - 0x08000000; raw = lz77(d, q)[:32] if d[q] == 0x10 else d[q:q + 32]
    c = struct.unpack('<16H', raw); return np.array([((v & 31) << 3, ((v >> 5) & 31) << 3, ((v >> 10) & 31) << 3) for v in c], np.uint8)
if __name__ == '__main__':
    d = open(sys.argv[1], 'rb').read(); R = runs(d); print([(hex(a), n) for a, n in R])
    a, n = [r for r in R if r[1] not in (440,)][int(sys.argv[4]) if len(sys.argv) > 4 else 0]
    pa = palrun(d, n, set())
    print('table', hex(a), n, 'pals', hex(pa) if pa else None)
    cols = 12; S = 2; W, H = 64 * S + 6, 64 * S + 14
    img = Image.new('RGB', (cols * W, ((n + cols - 1) // cols) * H + 20), (40, 40, 48)); dr = ImageDraw.Draw(img)
    dr.text((4, 4), '%s trainer fronts (%d)' % (sys.argv[3], n), fill=(255, 255, 255)); bad = 0
    for i in range(n):
        p, sz, _ = struct.unpack_from('<IHH', d, a + 8 * i)
        try:
            px = decode(d, p, sz); pl = pal(d, struct.unpack_from('<I', d, pa + 8 * i)[0]) if pa else None
        except Exception: bad += 1; continue
        rgb = pl[px] if pl is not None else np.stack([px * 17] * 3, -1).astype(np.uint8); rgb[px == 0] = (70, 70, 86)
        x, y = (i % cols) * W, (i // cols) * H + 20; dr.text((x + 2, y), str(i), fill=(255, 230, 0))
        img.paste(Image.fromarray(rgb).resize((64 * S, 64 * S), Image.NEAREST), (x, y + 12))
    img.save(sys.argv[2]); print('bad', bad)
