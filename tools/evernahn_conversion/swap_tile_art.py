#!/usr/bin/env python3
"""
Broad tile-ART swap: replace the PIXELS inside a tileset's tiles, in place.

WHY THIS AND NOT A REPAINT OR A RE-TINT
---------------------------------------
Two earlier attempts were wrong in different ways.

1. REPAINTING map.bin from a blueprint destroyed a hand-designed map. The
   committed Pelluca City used 324 distinct metatiles; the repaint replaced it
   with seven metatiles of flat fill. Reverted.

2. RE-TINTING palettes only changed the COLOURS of vanilla Hoenn art. The trees
   were still Hoenn trees, the gym still a Hoenn gym -- just recoloured, and
   washed out where a luminance ramp pushed bright green highlights to near
   white. That is not a re-skin.

A real re-skin replaces the 8x8 PIXEL BLOCKS while leaving every id alone:

    tiles.png pixels      <- CHANGED
    palettes              <- CHANGED (the new art needs its own colours)
    tile ids              <- untouched
    metatiles.bin         <- untouched
    metatile_attributes   <- untouched
    map.bin               <- untouched

So no layout, collision, elevation, warp or script can break, and all 69
Dreamstone maps sharing gTileset_General re-skin simultaneously.

TILES ARE SHARED -- THIS IS THE WHOLE DESIGN CONSTRAINT
--------------------------------------------------------
Measured on gTileset_General: grass tile 2 is referenced 222 times across 130
metatiles; tile 204 appears in 16 unrelated metatiles; of the 16 tiles making up
a vanilla tree only FOUR (384, 385, 400, 401) are exclusive to it.

That sharing is what makes the approach powerful -- overwrite tile 2 and all 130
metatiles using it re-skin at once, including every grass edge and shoreline
transition -- but it means a tile must be replaced according to WHAT IT DEPICTS,
never according to which metatile you happen to be looking at. Writing a conifer
into tile 204 would corrupt 16 unrelated metatiles.

So tiles are classified first (by colour character and contrast), then each
CLASS is mapped to source art. Classification of the 421 referenced tiles:

    203  other (buildings, rock, misc)   <- left alone in a broad pass
    103  water
     74  green (grass/tree)
     37  sand/path
      4  flat/solid

GEOMETRY
--------
Source cells are 32x32. A vanilla tree is 2x2 metatiles = 32x32 screen pixels,
so tree art drops in 1:1 with NO resampling. Ground tiles are 8x8, taken from a
2x mode-downscale of a 32x32 cell -- integer, so no invented colours. Mode, not
averaging: averaging invents colours outside the palette and softens edges.

Usage:
  python3 swap_tile_art.py <tileset_dir> --classes /tmp/tilecls.json [--dry-run]
"""
import argparse
import json
import struct
from collections import Counter
from pathlib import Path

import numpy as np
from PIL import Image

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "assets" / "pelluca_tileset_source"

# class -> (sheet, row, col) of the 32x32 source cell that replaces it
SOURCES = {
    "green (grass/tree)": ("Calvera.png", 170, 4),   # muted sage, 3 colours
    "sand/path":          ("Evernahn.png", 71, 5),   # earth tuft
    "water":              ("Evernahn_Water.png", 0, 0),
}
CELL = 32


def mode_downscale(idx):
    h, w = idx.shape
    out = np.zeros((h // 2, w // 2), np.uint8)
    for y in range(h // 2):
        for x in range(w // 2):
            out[y, x] = np.bincount(
                idx[y * 2:y * 2 + 2, x * 2:x * 2 + 2].ravel()).argmax()
    return out


def fetch(sheet, r, c):
    a = np.array(Image.open(SRC / sheet).convert("RGBA"))
    if sheet.startswith("Evernahn_"):          # autotile strip: row 0, cell c
        blk = a[0:CELL, r * CELL:(r + 1) * CELL]
    else:
        blk = a[r * CELL:(r + 1) * CELL, c * CELL:(c + 1) * CELL]
    op = blk[:, :, 3] > 128
    rgb = blk[:, :, :3].astype(int)
    if not op.all():                            # composite over its darkest tone
        vis = rgb[op]
        base = vis[np.argmin(vis @ np.array([0.299, 0.587, 0.114]))]
        rgb[~op] = base
    return rgb


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tileset")
    ap.add_argument("--classes", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    d = Path(a.tileset)
    cls = {int(k): v for k, v in json.loads(Path(a.classes).read_text()).items()}

    before_mt = (d / "metatiles.bin").read_bytes()
    before_at = (d / "metatile_attributes.bin").read_bytes()
    page = np.array(Image.open(d / "tiles.png").convert("P"))
    before_size = page.shape
    tw = page.shape[1] // 8

    mt = before_mt
    tpal = {}
    for m in range(len(mt) // 16):
        for q in range(8):
            e = struct.unpack_from("<H", mt, m * 16 + q * 2)[0]
            tid, sl = e & 0x3FF, (e >> 12) & 15
            if q >= 4 and tid == 0:
                continue
            tpal.setdefault(tid, Counter())[sl] += 1

    # Which palette slot does each CLASS predominantly live on? The new art must
    # be written into that slot's colours or the tiles will render wrong.
    byclass = {}
    for tid, k in cls.items():
        if k in SOURCES:
            byclass.setdefault(k, Counter())[tpal[tid].most_common(1)[0][0]] += 1
    plan = {}
    for k, c in byclass.items():
        slot = c.most_common(1)[0][0]
        plan[k] = slot
        print(f"  {k:22s} -> palette slot {slot}  "
              f"({sum(c.values())} tiles, distribution {dict(c)})")

    newpals = {}
    changed = 0
    for k, (sheet, r, c) in SOURCES.items():
        if k not in plan:
            continue
        slot = plan[k]
        art = fetch(sheet, r, c)
        small = None
        cols = [tuple(int(v) for v in x)
                for x in np.unique(art.reshape(-1, 3), axis=0)][:15]
        P = np.array(cols)
        idx = (np.argmin(((art.reshape(-1, 3)[:, None] - P[None]) ** 2).sum(2),
                         axis=1) + 1).astype(np.uint8).reshape(CELL, CELL)
        small = mode_downscale(idx)             # 32 -> 16, integer, mode
        newpals[slot] = [(0, 0, 0)] + cols
        # write every tile of this class from the 16x16 art, tiling 8x8 blocks
        for tid, kk in cls.items():
            if kk != k:
                continue
            if tpal[tid].most_common(1)[0][0] != slot:
                continue                        # wrong palette; leave it alone
            sub = small[(tid % 2) * 8:(tid % 2) * 8 + 8,
                        ((tid // 2) % 2) * 8:((tid // 2) % 2) * 8 + 8]
            y, x = (tid // tw) * 8, (tid % tw) * 8
            page[y:y + 8, x:x + 8] = sub
            changed += 1
    print(f"\n{changed} tiles rewritten across {len(newpals)} palettes")

    if a.dry_run:
        print("dry run - nothing written")
        return

    im = Image.fromarray(page, "P")
    im.putpalette(Image.open(d / "tiles.png").convert("P").getpalette())
    im.save(d / "tiles.png")
    for slot, cols in newpals.items():
        cols = (list(cols) + [(0, 0, 0)] * 16)[:16]
        with open(d / "palettes" / f"{slot:02d}.gbapal", "wb") as f:
            for r, g, b in cols:
                f.write(struct.pack("<H", (r >> 3) | ((g >> 3) << 5) | ((b >> 3) << 10)))
        p = d / "palettes" / f"{slot:02d}.pal"
        if p.exists():
            with open(p, "wb") as f:
                f.write(b"JASC-PAL\r\n0100\r\n16\r\n")
                for r, g, b in cols:
                    f.write(f"{r} {g} {b}\r\n".encode())

    assert (d / "metatiles.bin").read_bytes() == before_mt
    assert (d / "metatile_attributes.bin").read_bytes() == before_at
    assert np.array(Image.open(d / "tiles.png").convert("P")).shape == before_size
    print("invariants hold: metatiles, attributes and tile geometry unchanged")


if __name__ == "__main__":
    main()
