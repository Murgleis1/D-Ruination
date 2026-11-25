"""Find and dump every large overworld sprite (an object-event graphics info 48 px or wider) in a GBA ROM whose
sprites are stored raw (FireRed/Emerald layout: tileTag 0xFFFF, paletteTag, reflection tag, size, width, height, then
five pointers, images at +28; each image a {data pointer, size} pair; palettes a {data pointer, tag} table).
Used to look for ships in Crown, Odyssey and Lazarus (user 2026-11-24: "re-examine the main games... pick a fitting ship
for the Pale Veluza... put two other ships for each of the other docks").
Usage: python3 scan_big_sprites.py ROM OUTDIR"""
import os, sys, struct, re
import numpy as np
from PIL import Image, ImageDraw

def main(rom, out):
    d = open(rom, 'rb').read(); N = len(d)
    isp = lambda p: 0x08000000 <= p < 0x08000000 + N
    os.makedirs(out, exist_ok=True)
    found = []
    for m in re.finditer(re.escape(b'\xff\xff'), d):
        a = m.start()
        if a % 4 or a > N - 40: continue
        tag, pal, refl, size, w, h = struct.unpack_from('<HHHHhh', d, a)
        if not (48 <= w <= 128 and 32 <= h <= 128 and w % 8 == 0 and h % 8 == 0): continue
        if size != w * h // 2: continue
        ptrs = [struct.unpack_from('<I', d, a + o)[0] for o in range(16, 36, 4)]
        if not isp(ptrs[3]): continue
        img0 = ptrs[3] - 0x08000000
        dp, sz = struct.unpack_from('<II', d, img0)
        if not isp(dp) or (sz & 0xFFFF) != size: continue
        found.append((a, pal, w, h, dp - 0x08000000))
    pals = {}
    tags = {f[1] for f in found}
    for a in range(0, N - 8, 4):
        p, t, z = struct.unpack_from('<IHH', d, a)
        if t in tags and t not in pals and isp(p) and z == 0:
            q = p - 0x08000000
            cols = struct.unpack_from('<16H', d, q)
            if all(c < 0x8000 for c in cols):
                pals[t] = np.array([((c & 31) << 3, ((c >> 5) & 31) << 3, ((c >> 10) & 31) << 3) for c in cols], np.uint8)
    shots = []
    seen = set()
    for (a, pal, w, h, dp) in found:
        if dp in seen: continue
        seen.add(dp)
        tw = w // 8; n = tw * (h // 8); px = np.zeros((h, w), np.uint8)
        for t in range(n):
            tb = np.frombuffer(d[dp + t * 32:dp + t * 32 + 32], np.uint8); tile = np.zeros((8, 8), np.uint8)
            tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
            px[(t // tw) * 8:(t // tw) * 8 + 8, (t % tw) * 8:(t % tw) * 8 + 8] = tile
        P = pals.get(pal)
        if P is None: P = np.array([(i * 16, i * 16, i * 16) for i in range(16)], np.uint8)
        rgba = np.zeros((h, w, 4), np.uint8); rgba[..., :3] = P[px]; rgba[..., 3] = (px != 0) * 255
        name = '%06x_%dx%d' % (a, w, h); Image.fromarray(rgba).save(os.path.join(out, name + '.png')); shots.append((name, rgba))
    print(len(shots), 'big sprites')
    if not shots: return
    cols = 8; cw = 136; ch = 150
    S = Image.new('RGBA', (cols * cw, ((len(shots) + cols - 1) // cols) * ch), (60, 60, 80, 255)); dr = ImageDraw.Draw(S)
    for i, (n, r) in enumerate(shots):
        x, y = (i % cols) * cw, (i // cols) * ch
        S.alpha_composite(Image.fromarray(r), (x, y + 14)); dr.text((x, y), n, fill=(255, 255, 0))
    S.save(os.path.join(out, 'sheet.png'))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
