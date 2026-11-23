import sys, numpy as np
from PIL import Image
def glyphs(buf, n, order=0):
    out = np.zeros((16 * ((n + 15) // 16), 256), np.uint8)
    for g in range(n):
        b = buf[g * 64:(g + 1) * 64]
        if len(b) < 64: break
        im = np.zeros((16, 16), np.uint8)
        for t, (tx, ty) in enumerate(((0, 0), (8, 0), (0, 8), (8, 8))):
            for r in range(8):
                w = b[t * 16 + r * 2] | (b[t * 16 + r * 2 + 1] << 8)
                for i in range(8):
                    v = (w >> (2 * i)) & 3 if order == 0 else (w >> (14 - 2 * i)) & 3
                    im[ty + r, tx + i] = v
        gx, gy = g % 16, g // 16
        out[gy * 16:(gy + 1) * 16, gx * 16:(gx + 1) * 16] = im
    return out
if __name__ == '__main__':
    rom = open(sys.argv[1], 'rb').read(); off = int(sys.argv[2], 16); n = int(sys.argv[3]); order = int(sys.argv[5]) if len(sys.argv) > 5 else 0
    g = glyphs(rom[off:off + n * 64], n, order)
    pal = np.array([(255, 255, 255), (40, 40, 40), (160, 160, 160), (255, 0, 0)], np.uint8)
    Image.fromarray(pal[g]).resize((g.shape[1] * 2, g.shape[0] * 2), Image.NEAREST).save(sys.argv[4])
