#!/usr/bin/env python3
"""
Render a tileset's metatiles by decoding metatiles.bin exactly as the engine
does, so the preview shows what the game will draw -- not what the source art
looked like.

This is the check that matters: it exercises the real tile ids, the real flip
bits and the real palette-slot assignments. A preview built from the source art
instead would still look fine even if the encoding were wrong.

Usage: python3 render_metatiles.py <tileset_dir> <out.png> [cols]
"""
import struct
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


def main():
    d = Path(sys.argv[1])
    out = Path(sys.argv[2])
    cols = int(sys.argv[3]) if len(sys.argv) > 3 else 16

    tiles_img = np.array(Image.open(d / "tiles.png").convert("P"))
    pals = []
    for i in range(16):
        raw = (d / "palettes" / f"{i:02d}.gbapal").read_bytes()
        p = []
        for j in range(16):
            v = struct.unpack_from("<H", raw, j * 2)[0]
            p.append((((v & 31) << 3), (((v >> 5) & 31) << 3), (((v >> 10) & 31) << 3)))
        pals.append(p)

    mt = (d / "metatiles.bin").read_bytes()
    n = len(mt) // 16
    tw = tiles_img.shape[1] // 8

    def tile(tid):
        y, x = (tid // tw) * 8, (tid % tw) * 8
        return tiles_img[y:y + 8, x:x + 8]

    rows = -(-n // cols)
    S = 3
    pad, top = 16, 46
    cv = Image.new("RGB", (pad * 2 + cols * 16 * S, top + rows * 16 * S + 20), (26, 26, 30))
    dr = ImageDraw.Draw(cv)
    dr.text((pad, 12), f"{d.name}: {n} metatiles decoded from metatiles.bin "
                       f"(real tile ids, flips and palette slots)", fill=(240, 240, 240))
    dr.text((pad, 28), "checkerboard = transparent (colour index 0)", fill=(160, 160, 170))

    for m in range(n):
        canvas = np.zeros((16, 16, 3), np.uint8)
        alpha = np.zeros((16, 16), bool)
        for q in range(4):
            e = struct.unpack_from("<H", mt, m * 16 + q * 2)[0]
            tid, xf, yf, slot = e & 0x3FF, (e >> 10) & 1, (e >> 11) & 1, (e >> 12) & 15
            t = tile(tid)
            if xf:
                t = t[:, ::-1]
            if yf:
                t = t[::-1, :]
            oy, ox = (q // 2) * 8, (q % 2) * 8
            for yy in range(8):
                for xx in range(8):
                    v = t[yy, xx]
                    if v:
                        canvas[oy + yy, ox + xx] = pals[slot][v]
                        alpha[oy + yy, ox + xx] = True
        # checkerboard behind transparency
        for yy in range(16):
            for xx in range(16):
                if not alpha[yy, xx]:
                    canvas[yy, xx] = (58, 58, 66) if ((yy // 4 + xx // 4) % 2) else (44, 44, 50)
        img = Image.fromarray(canvas).resize((16 * S, 16 * S), Image.NEAREST)
        cv.paste(img, (pad + (m % cols) * 16 * S, top + (m // cols) * 16 * S))

    cv.save(out)
    print("wrote", out, f"({n} metatiles)")


if __name__ == "__main__":
    main()
