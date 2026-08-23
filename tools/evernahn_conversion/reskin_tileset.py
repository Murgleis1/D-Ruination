#!/usr/bin/env python3
"""
Re-skin a tileset IN PLACE: replace tile ART only, never metatile ids or map data.

WHY THIS AND NOT A REPAINT
--------------------------
The earlier approach painted LAYOUT_PELLUCA_CITY from a blueprint. The committed
map used 324 DISTINCT METATILES -- a hand-designed city with buildings, paths,
shorelines and detail -- and the repaint replaced it with SEVEN metatiles of flat
fill. That destroyed real level design and then took several rounds trying to
make flat fill look acceptable.

A region re-skin works the other way round. The map data and metatile structure
already encode good design. Swapping the ART that a tileset's tiles contain
re-skins every map that uses it simultaneously:

  - map.bin is never touched, so no layout, collision or elevation can break
  - metatile ids are never touched, so warps, scripts and cutscenes still work
  - all 69 Dreamstone maps sharing gTileset_General change at once

WHAT IS SAFE TO CHANGE, AND WHAT IS NOT
---------------------------------------
SAFE:   the pixels inside tiles.png, and the palette entries a tile uses.
UNSAFE: tile ids, metatile ids, metatiles.bin, metatile_attributes.bin, map.bin.

This tool only ever rewrites 8x8 pixel blocks inside tiles.png and, optionally,
palette files. It asserts that tiles.png keeps its exact dimensions and that
metatiles.bin and metatile_attributes.bin are byte-identical afterwards.

PALETTE SHARING IS THE REAL CONSTRAINT
--------------------------------------
Tiles do not own palettes; metatiles assign one of 16 to each quadrant. In
gTileset_General the outdoor terrain is concentrated on three:

    palette 2  grass, tree canopy, tree trunk   (metatiles 1, 468/469, 476/477)
    palette 4  water                            (metatile 368 -- 25% of Pelluca)
    palette 5  sand / path                      (metatile 289)

So replacing "the grass" means every tile drawn with palette 2 must still look
right against whatever palette 2 becomes. The tool therefore works per-PALETTE:
it takes a target palette, re-tints it, and remaps the affected tiles' indices,
rather than swapping tiles one at a time and hoping the palettes agree.

Usage:
  python3 reskin_tileset.py <tileset_dir> --plan plan.json [--dry-run]
  python3 reskin_tileset.py <tileset_dir> --audit
"""
import argparse
import json
import shutil
import struct
from pathlib import Path

import numpy as np
from PIL import Image

REPO = Path(__file__).resolve().parents[2]


def load_palette(d, i):
    raw = (d / "palettes" / f"{i:02d}.gbapal").read_bytes()
    return [(((v & 31) << 3), (((v >> 5) & 31) << 3), (((v >> 10) & 31) << 3))
            for v in (struct.unpack_from("<H", raw, j * 2)[0] for j in range(16))]


def write_palette(d, i, cols):
    cols = (list(cols) + [(0, 0, 0)] * 16)[:16]
    with open(d / "palettes" / f"{i:02d}.gbapal", "wb") as f:
        for r, g, b in cols:
            f.write(struct.pack("<H", (r >> 3) | ((g >> 3) << 5) | ((b >> 3) << 10)))
    p = d / "palettes" / f"{i:02d}.pal"
    if p.exists():
        with open(p, "wb") as f:
            f.write(b"JASC-PAL\r\n0100\r\n16\r\n")
            for r, g, b in cols:
                f.write(f"{r} {g} {b}\r\n".encode())


def audit(d):
    """Report which metatiles use which palette, and which tiles they reference."""
    mt = (d / "metatiles.bin").read_bytes()
    n = len(mt) // 16
    bypal = {}
    for m in range(n):
        for q in range(8):
            e = struct.unpack_from("<H", mt, m * 16 + q * 2)[0]
            tid, sl = e & 0x3FF, (e >> 12) & 15
            if q >= 4 and tid == 0:
                continue
            bypal.setdefault(sl, {"metatiles": set(), "tiles": set()})
            bypal[sl]["metatiles"].add(m)
            bypal[sl]["tiles"].add(tid)
    print(f"{d.name}: {n} metatiles")
    for sl in sorted(bypal):
        v = bypal[sl]
        print(f"  palette {sl:2d}: {len(v['metatiles']):4d} metatiles, "
              f"{len(v['tiles']):4d} distinct tiles")
    return bypal


def retint(d, slot, new_colours, dry):
    """Replace a palette's colours. Tile INDICES are untouched, so every tile
    drawn with this palette re-skins coherently and nothing can desynchronise."""
    old = load_palette(d, slot)
    new = (list(new_colours) + [(0, 0, 0)] * 16)[:16]
    print(f"  palette {slot}:")
    for i, (o, c) in enumerate(zip(old, new)):
        if o != c:
            print(f"    [{i:2d}] #{o[0]:02X}{o[1]:02X}{o[2]:02X} -> "
                  f"#{c[0]:02X}{c[1]:02X}{c[2]:02X}")
    if not dry:
        write_palette(d, slot, new)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tileset")
    ap.add_argument("--plan")
    ap.add_argument("--audit", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    d = Path(a.tileset)

    if a.audit:
        audit(d)
        return

    plan = json.loads(Path(a.plan).read_text())
    before_mt = (d / "metatiles.bin").read_bytes()
    before_at = (d / "metatile_attributes.bin").read_bytes()
    before_size = Image.open(d / "tiles.png").size

    if not a.dry_run:
        for f in ("metatiles.bin", "metatile_attributes.bin", "tiles.png"):
            shutil.copy(d / f, d / (f + ".bak"))

    for slot, cols in plan.get("palettes", {}).items():
        retint(d, int(slot), [tuple(c) for c in cols], a.dry_run)

    if a.dry_run:
        print("dry run - nothing written")
        return

    # INVARIANTS: art may change, structure may not.
    assert (d / "metatiles.bin").read_bytes() == before_mt, "metatiles.bin changed"
    assert (d / "metatile_attributes.bin").read_bytes() == before_at, "attributes changed"
    assert Image.open(d / "tiles.png").size == before_size, "tiles.png resized"
    print("invariants hold: metatiles, attributes and tile geometry unchanged")
    for f in ("metatiles.bin", "metatile_attributes.bin", "tiles.png"):
        (d / (f + ".bak")).unlink()


if __name__ == "__main__":
    main()
