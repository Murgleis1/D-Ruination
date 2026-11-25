"""Overworld sprite catalogue for a GBA Pokemon hack (FireRed or Emerald base): finds the graphics-info structs
(tileTag 0xFFFF, 16x32 or 32x32), their palettes by tag, and decodes frame 0 (south) of each, raw or LZ77."""
import sys, re, struct
import numpy as np
from PIL import Image, ImageDraw
isp = lambda v: 0x08000000 <= v < 0x0A000000
def lz77(d, o):
    if d[o] != 0x10: return None
    n = d[o + 1] | d[o + 2] << 8 | d[o + 3] << 16; out = bytearray(); i = o + 4
    while len(out) < n:
        f = d[i]; i += 1
        for b in range(8):
            if len(out) >= n: break
            if f & (0x80 >> b):
                x = d[i] << 8 | d[i + 1]; i += 2; ln = (x >> 12) + 3; dist = (x & 0xFFF) + 1
                for _ in range(ln): out.append(out[-dist])
            else: out.append(d[i]); i += 1
    return bytes(out)
def scan(d):
    infos = []
    for m in re.finditer(re.escape(b'\xff\xff'), d):
        a = m.start()
        if a % 4 or a > len(d) - 64: continue
        tag, pal, refl, size, w, h = struct.unpack_from('<HHHHhh', d, a)
        if (w, h, size) not in ((16, 32, 256), (32, 32, 512)): continue
        ptrs = [struct.unpack_from('<I', d, a + o)[0] for o in range(16, 36, 4)]
        if sum(isp(p) for p in ptrs) < 4 or not isp(ptrs[3]): continue
        infos.append((a, pal, ptrs[3], w, h, size))
    tags = {i[1] for i in infos}; pals = {}
    for a in range(0, len(d) - 8, 4):
        p, t, z = struct.unpack_from('<IHH', d, a)
        if t in tags and t not in pals and isp(p) and z == 0:
            q = p - 0x08000000
            raw = d[q:q + 32] if d[q] != 0x10 else (lz77(d, q) or b'')[:32]
            if len(raw) < 32: continue
            cols = struct.unpack('<16H', raw)
            if all(c < 0x8000 for c in cols):
                pals[t] = np.array([((c & 31) << 3, ((c >> 5) & 31) << 3, ((c >> 10) & 31) << 3) for c in cols], np.uint8)
    return infos, pals
def frame(d, images, w, h, size):
    p, sz = struct.unpack_from('<IH', d, images - 0x08000000)
    if not isp(p): return None
    q = p - 0x08000000
    b = d[q:q + size] if d[q] != 0x10 or sz == size and False else None
    if d[q] == 0x10:
        try: b = lz77(d, q)[:size]
        except Exception: b = d[q:q + size]
    if b is None or len(b) < size: b = d[q:q + size]
    tw, th = w // 8, h // 8; px = np.zeros((h, w), np.uint8)
    for t in range(tw * th):
        tb = np.frombuffer(b[t * 32:(t + 1) * 32], np.uint8); tile = np.zeros((8, 8), np.uint8)
        tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
        px[(t // tw) * 8:(t // tw) * 8 + 8, (t % tw) * 8:(t % tw) * 8 + 8] = tile
    return px
def catalogue(rom, out, label):
    d = open(rom, 'rb').read(); infos, pals = scan(d)
    S, cols = 3, 16; W, H = 32 * S + 8, 32 * S + 14
    img = Image.new('RGB', (cols * W, ((len(infos) + cols - 1) // cols) * H + 20), (40, 40, 48)); dr = ImageDraw.Draw(img)
    dr.text((4, 4), label + ' (%d sprites)' % len(infos), fill=(255, 255, 255))
    for i, (a, tag, images, w, h, size) in enumerate(infos):
        px = frame(d, images, w, h, size); x, y = (i % cols) * W, (i // cols) * H + 20
        dr.text((x + 2, y), str(i), fill=(255, 230, 0))
        if px is None: continue
        rgb = pals[tag][px] if tag in pals else np.stack([px * 17] * 3, -1).astype(np.uint8); rgb[px == 0] = (70, 70, 86)
        img.paste(Image.fromarray(rgb).resize((w * S, h * S), Image.NEAREST), (x + (32 - w) * S // 2, y + 12))
    img.save(out); print(label, len(infos), 'sprites,', len(pals), 'palettes')
    return infos
if __name__ == '__main__':
    catalogue(sys.argv[1], sys.argv[2], sys.argv[3])
