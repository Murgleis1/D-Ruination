import numpy as np
from PIL import Image
g = np.load('blackletter_glyphs.npy'); W = open('blackletter_widths.bin', 'rb').read()
def code(c):
    if c == ' ': return 0
    if 'A' <= c <= 'Z': return 0xBB + ord(c) - 65
    if 'a' <= c <= 'z': return 0xD5 + ord(c) - 97
    if '0' <= c <= '9': return 0xA1 + ord(c) - 48
    return {'.': 0xAD, ',': 0xB8, "'": 0xB4, '!': 0xAB, '?': 0xAC, '-': 0xAE, 'é': 0x1B}[c]
def glyph(c): k = code(c); return g[(k // 16) * 16:(k // 16) * 16 + 16, (k % 16) * 16:(k % 16) * 16 + 16], W[k]
def width(s): return sum(glyph(c)[1] for c in s)
def wrap(text, maxw):
    lines, cur = [], ''
    for w in text.split(' '):
        t = (cur + ' ' + w).strip()
        if width(t) <= maxw: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]
INK, SHADOW = (58, 38, 22), (196, 164, 112)
def box(img, lines, y0=112):
    H, Wd = 48, 240
    rng = np.random.default_rng(3)
    for y in range(y0, y0 + H):
        for x in range(0, Wd):
            dx, dy = min(x, Wd - 1 - x), min(y - y0, y0 + H - 1 - y)
            e = min(dx, dy)
            base = np.array((238, 224, 186)) if e > 5 else np.array((228, 208, 160)) if e > 2 else np.array((206, 178, 124))
            n = rng.integers(-6, 7)
            img[y, x] = np.clip(base + n if e > 2 else base, 0, 255)
    img[y0, 2:Wd - 2] = img[y0 + H - 1, 2:Wd - 2] = (120, 84, 48); img[y0 + 2:y0 + H - 2, 0] = img[y0 + 2:y0 + H - 2, Wd - 1] = (120, 84, 48)
    for (cx, cy) in ((1, y0 + 1), (Wd - 2, y0 + 1), (1, y0 + H - 2), (Wd - 2, y0 + H - 2)): img[cy, cx] = (120, 84, 48)
    for li, line in enumerate(lines):
        x = 12; y = y0 + 8 + 16 * li
        for c in line:
            gl, w = glyph(c)
            for yy in range(16):
                for xx in range(16):
                    v = gl[yy, xx]
                    if v == 1: img[y + yy, x + xx] = INK
                    elif v == 2: img[y + yy, x + xx] = SHADOW
            x += w
def frame(lines):
    img = np.zeros((160, 240, 3), int); img[:] = (16, 20, 34)
    img[60:100, 100:140] = (40, 48, 70)
    box(img, lines); return img
text1 = "Nomad Alban,"
text2 = "The surgeon's report from Sevii reached my desk a week before your commander's did. A commander proud of his decisions does not take a week to report them."
pages = [[text1]] + [wrap(text2, 214)[i:i + 2] for i in range(0, 6, 2)]
pages = [p for p in pages if p and p[0]]
ims = [frame(p) for p in pages[:3]]
sheet = np.concatenate([np.pad(i, ((0, 0), (0, 6), (0, 0))) for i in ims], 1).astype(np.uint8)
Image.fromarray(sheet).resize((sheet.shape[1] * 3, 160 * 3), Image.NEAREST).save('letter_preview.png')
print(pages)
