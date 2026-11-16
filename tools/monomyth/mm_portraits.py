"""MonoMyth dialogue portraits: extract + catalogue (user 2026-11-16: "I want MonoMyth's portrait
system ... exactly what I want for our portraits").

Measured on Pokemon_MonoMyth.gba (scan of every LZ77 blob, then every word pointing at one):
  * a portrait is ONE 80x80 4bpp image (10x10 tiles, 3200 bytes) LZ77-compressed, with ONE raw
    16-colour palette (32 bytes, index 0 = transparent background). No frame, no window border:
    a head-and-shoulders bust, right-aligned in the 80px canvas, cut flat at the bottom.
  * 495 portraits in four pointer tables of {gfx*, pal*} pairs (8 bytes each). Expressions,
    hand gestures and emote marks ("?", hearts, sweat) are separate full images, not overlays.

Usage:
  python3 -I mm_portraits.py ROM OUT_DIR            -> OUT_DIR/mm_NNN.png (indexed, idx 0 transparent)
                                                       + OUT_DIR/catalogue_NNN.png sheets (numbered)
  from mm_portraits import load(rom) -> list of (index, pixels[80,80] uint8, palette[16,3] uint8)
"""
import os, sys, struct
import numpy as np

TABLES = [(0xB163F8, 2), (0xB16410, 116), (0xB167E8, 124), (0xB6FB08, 149), (0xB6FFC0, 104)]
SIZE = 80


def _lz77(d, off):
    assert d[off] == 0x10
    size = d[off + 1] | d[off + 2] << 8 | d[off + 3] << 16
    out = bytearray(); p = off + 4
    while len(out) < size:
        flags = d[p]; p += 1
        for b in range(8):
            if len(out) >= size: break
            if flags & (0x80 >> b):
                v = d[p] << 8 | d[p + 1]; p += 2
                n, disp = (v >> 12) + 3, (v & 0xFFF) + 1
                for _ in range(n): out.append(out[-disp])
            else:
                out.append(d[p]); p += 1
    return bytes(out[:size])


def _tiles_to_pixels(b, tw):
    th = len(b) // 32 // tw
    px = np.zeros((th * 8, tw * 8), np.uint8)
    a = np.frombuffer(b, np.uint8)
    for t in range(tw * th):
        tb = a[t * 32:(t + 1) * 32]
        tile = np.zeros((8, 8), np.uint8)
        tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
        px[(t // tw) * 8:(t // tw) * 8 + 8, (t % tw) * 8:(t % tw) * 8 + 8] = tile
    return px


def load(rom):
    d = open(rom, 'rb').read()
    out = []
    for start, n in TABLES:
        for k in range(n):
            g, p = struct.unpack_from('<2I', d, start + 8 * k)
            g -= 0x08000000; p -= 0x08000000
            px = _tiles_to_pixels(_lz77(d, g), SIZE // 8)
            pal = [struct.unpack_from('<H', d, p + 2 * i)[0] for i in range(16)]
            pal = np.array([((c & 31) << 3, ((c >> 5) & 31) << 3, ((c >> 10) & 31) << 3) for c in pal], np.uint8)
            out.append((len(out), px, pal))
    return out


def save_indexed(px, pal, path):
    from PIL import Image
    im = Image.fromarray(px, 'P')
    im.putpalette([int(v) for c in pal for v in c] + [0] * (768 - 48))
    im.info['transparency'] = 0
    im.save(path, transparency=0)


def catalogue(ports, path, first, count, scale=2, cols=8, bg=(110, 110, 130)):
    from PIL import Image, ImageDraw
    sel = ports[first:first + count]
    W = SIZE * scale + 4; H = SIZE * scale + 12
    im = Image.new('RGB', (cols * W, ((len(sel) + cols - 1) // cols) * H), (30, 30, 30))
    dr = ImageDraw.Draw(im)
    for k, (i, px, pal) in enumerate(sel):
        rgb = pal[px]; rgb[px == 0] = bg
        x, y = (k % cols) * W, (k // cols) * H
        im.paste(Image.fromarray(rgb).resize((SIZE * scale, SIZE * scale), Image.NEAREST), (x, y + 11))
        dr.text((x, y), f'#{i}', fill=(255, 255, 0))
    im.save(path)


if __name__ == '__main__':
    rom, out = sys.argv[1], sys.argv[2]
    os.makedirs(out, exist_ok=True)
    ports = load(rom)
    for i, px, pal in ports:
        save_indexed(px, pal, os.path.join(out, f'mm_{i:03d}.png'))
    for first in range(0, len(ports), 64):
        catalogue(ports, os.path.join(out, f'catalogue_{first:03d}.png'), first, 64)
    print(f'{len(ports)} portraits -> {out}')
