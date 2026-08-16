#!/usr/bin/env python3
"""
Render map.bin at 1:1 GBA resolution -- 240x160, exactly one screen.

WHY THIS EXISTS
---------------
Every preview in this project before it was zoomed 3-8x, or a whole-map view at
16px per cell. Neither shows what the player sees. A busy tile looks like
pleasant texture at 3x and unreadable noise at 1x, and a repaint shipped with
grass measuring three times vanilla's tile contrast -- caught only by playing
the ROM.

Worse, the metrics used were invented. Real shipped Emerald towns measure:

    Littleroot  stddev 31.3  edge 15.2  38 colours on screen
    Oldale      stddev 32.5  edge 12.5  37
    Lilycove    stddev 32.0  edge 14.0  32

Those are the target. A self-invented "calm ground: stddev < 12" would have
flattened the map into mush. Compare against vanilla, not against a number.

TWO SEPARATE ID SPACES, AND CONFLATING THEM BREAKS EVERYTHING
--------------------------------------------------------------
METATILE ids: 0-511 primary, 512+ secondary.
TILE ids inside a metatile entry: a SHARED 0-1023 space -- 0-511 index the
primary tileset's tile page, 512-1023 the secondary's, regardless of which
tileset the metatile came from (src/fieldmap.c:912 CopySecondaryTilesetToVram
loads the secondary at VRAM offset NUM_TILES_IN_PRIMARY). A secondary metatile
routinely references primary tiles; every vanilla tileset does.

A renderer that gets this wrong will happily draw a broken tileset as if it
were fine -- which is exactly how a build shipped with every building pointing
at terrain tiles.

Usage:
  python3 gba_viewport.py <map.bin> <primary_dir> <secondary_dir> <out.png>
                          [--at X,Y] [--zoom N] [--metrics] [--width W]
"""
import argparse
import struct
from pathlib import Path

import numpy as np
from PIL import Image

SCREEN_W, SCREEN_H = 240, 160          # 15 x 10 metatiles


def load(d):
    d = Path(d)
    t = np.array(Image.open(d / "tiles.png").convert("P"))
    pals = []
    for i in range(16):
        raw = (d / "palettes" / f"{i:02d}.gbapal").read_bytes()
        pals.append([(((v & 31) << 3), (((v >> 5) & 31) << 3), (((v >> 10) & 31) << 3))
                     for v in (struct.unpack_from("<H", raw, j * 2)[0] for j in range(16))])
    return t, t.shape[1] // 8, pals, (d / "metatiles.bin").read_bytes()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mapbin")
    ap.add_argument("primary")
    ap.add_argument("secondary")
    ap.add_argument("out")
    ap.add_argument("--at", default="40,50")
    ap.add_argument("--zoom", type=int, default=1)
    ap.add_argument("--width", type=int, default=80)
    ap.add_argument("--metrics", action="store_true")
    a = ap.parse_args()
    W = a.width

    pt, ptw, ppal, pmt = load(a.primary)
    st, stw, spal, smt = load(a.secondary)

    def draw(mid):
        mt, m = (smt, mid - 512) if mid >= 512 else (pmt, mid)
        c = np.zeros((16, 16, 3), np.uint8)
        if m * 16 + 16 > len(mt):
            return c
        for q in range(8):
            e = struct.unpack_from("<H", mt, m * 16 + q * 2)[0]
            tid, xf, yf, sl = e & 0x3FF, (e >> 10) & 1, (e >> 11) & 1, (e >> 12) & 15
            if q >= 4 and tid == 0:
                continue
            tiles, tw, pals, lt = ((st, stw, spal, tid - 512) if tid >= 512
                                   else (pt, ptw, ppal, tid))
            y, x = (lt // tw) * 8, (lt % tw) * 8
            if y + 8 > tiles.shape[0]:
                continue
            t = tiles[y:y + 8, x:x + 8]
            if xf:
                t = t[:, ::-1]
            if yf:
                t = t[::-1, :]
            oy, ox = ((q % 4) // 2) * 8, ((q % 4) % 2) * 8
            for yy in range(8):
                for xx in range(8):
                    if t[yy, xx]:
                        c[oy + yy, ox + xx] = pals[sl][t[yy, xx]]
        return c

    raw = Path(a.mapbin).read_bytes()
    H = len(raw) // 2 // W
    cx, cy = (int(v) for v in a.at.split(","))
    x0 = max(0, min(W - 15, cx - 7))
    y0 = max(0, min(H - 10, cy - 5))

    cache = {}
    img = np.zeros((SCREEN_H, SCREEN_W, 3), np.uint8)
    for j in range(10):
        for i in range(15):
            v = struct.unpack_from("<H", raw, ((y0 + j) * W + (x0 + i)) * 2)[0]
            mid = v & 0x3FF
            if mid not in cache:
                cache[mid] = draw(mid)
            img[j * 16:(j + 1) * 16, i * 16:(i + 1) * 16] = cache[mid]

    if a.metrics:
        lum = img @ np.array([0.299, 0.587, 0.114])
        dx = np.abs(np.diff(lum, axis=1)).mean()
        dy = np.abs(np.diff(lum, axis=0)).mean()
        cols = len(np.unique(img.reshape(-1, 3), axis=0))
        print(f"at ({x0},{y0})  stddev {lum.std():.1f}  edge {(dx+dy)/2:.1f}  "
              f"{cols} colours    [vanilla: ~32 / 12-15 / 32-38]")

    out = Image.fromarray(img)
    if a.zoom > 1:
        out = out.resize((SCREEN_W * a.zoom, SCREEN_H * a.zoom), Image.NEAREST)
    out.save(a.out)
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
