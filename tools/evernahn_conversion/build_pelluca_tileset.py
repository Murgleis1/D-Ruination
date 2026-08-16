#!/usr/bin/env python3
"""
Build the Pelluca SECONDARY tileset from Evernahn source art.

WHAT THIS PRODUCES
------------------
  codebase/data/tilesets/secondary/pelluca/
      tiles.png                 indexed 4bpp page, 128px wide
      metatiles.bin             16 bytes per metatile
      metatile_attributes.bin   2 bytes per metatile
      palettes/00..15.gbapal    + matching JASC .pal

SOURCE ROWS ARE 32px CELLS
--------------------------
assets/pelluca_tileset_source/Evernahn.png is 256x6176 = 8 cols x 193 rows of
32px cells. The row numbers in the handoff are in THOSE cells, not 16px rows.
Reading them as 16px does not error -- it silently returns a different slice of
the sheet, which cost a full review cycle once already. Confirmed against
assets/pelluca_ship/ship_spec.json, which records cell_px 32 and whose rows
180-183 c0-c6 reproduce its recorded 218x124 bbox and 10-colour count exactly.

Each 32px source cell becomes ONE 16x16 game metatile, i.e. a 2x downscale.

DOWNSCALE IS MODE, NEVER AVERAGING
----------------------------------
Averaging 2x2 blocks invents colours that are not in the palette and turns
crisp pixel edges into mush -- the same failure diagnosed on the title screen.
Taking the most common index in each 2x2 block keeps every output pixel a
colour the artist chose and keeps edges hard. This matches the method recorded
in ship_spec.json ("MODE (most-common colour per block) ... NEVER averaging").

PALETTE ALLOCATION
------------------
A secondary tileset owns palette slots 6-12 (NUM_PALS_IN_PRIMARY=6,
NUM_PALS_TOTAL=13). One 15-colour slot per building set, reduced by
reduce_palette.py:

    slot 6  monastery      slot 8  house
    slot 7  tavern         slot 9  ship
    slots 10-12 left free for props, animation and later detail work.

Index 0 of every sub-palette is transparent, so each set gets 15 usable colours.

TILE BUDGET
-----------
A secondary owns tiles 512-1023, i.e. 512 tiles. 160 metatiles x 4 quadrants =
640 raw tiles, so deduplication is REQUIRED, not an optimisation. Tiles are
deduped on their exact index pattern and additionally on x/y flips, since the
metatile entry carries flip bits for free. The build asserts the final count
fits and reports headroom.

Usage: python3 tools/evernahn_conversion/build_pelluca_tileset.py [--dry-run]
"""
import argparse
import struct
import sys
from collections import OrderedDict
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from reduce_palette import CELL, SHEET, reduce_palette  # noqa: E402

REPO = HERE.parents[1]
OUT = REPO / "codebase" / "data" / "tilesets" / "secondary" / "pelluca"

# name -> (row0, row1, palette slot, col0, col1)
#
# COLUMN RANGE MATTERS. The first build took rows 179-186 x all 8 cols for the
# ship, which swept in the 32x128 object at c7 that ship_spec.json explicitly
# excludes, plus unrelated art in rows 179 and 184-186 -- roughly half those
# metatiles were junk. The ship is rows 180-183, cols c0-c6, and nothing else.
# BOUNDS CONFIRMED VISUALLY BY THE USER, one building at a time.
#
# The originals came from the handoff, found by "template + colour-sig
# matching" -- enough to LOCATE a building, never verified to BOUND one. The
# sheet is packed edge to edge with no gutters, so those ranges sliced through
# continuous art and the monastery stamped as a wall fragment with no roof
# ridge or foundation. Opacity analysis could not settle it (every row outside
# every crop still measures 0.6-0.9 opaque).
#
#   monastery  r17-26 c0-c6   was r18-23 c0-c7
#   tavern     r69-72 c0-c7   was r69-71 c0-c7
#   house      r99-104 c0-c7  was r100-104 c0-c7  (lower of two stacked houses)
BUILD = [
    ("monastery", 17, 26, 6, 0, 6),
    ("tavern", 69, 72, 7, 0, 7),
    ("house", 99, 104, 8, 0, 7),
    ("ship", 180, 183, 9, 0, 6),
]

# GROUND METATILE drawn UNDER every building tile (Evernahn primary grass).
GROUND_TILE_SRC = ("SHEET", 71, 5)

# GREY -> OAK, verbatim from assets/pelluca_ship/ship_spec.json.
# The greys are 95.3% of the ship; each maps to a wood tone at MATCHING
# luminance (preserved within ~1), snapped to multiples of 8 because the GBA
# stores 5 bits per channel. Red trim and the mast highlight are left alone.
# Without this the ship renders as the modern grey hull that the period ship
# exists to replace.
SHIP_RECOLOUR = {
    (40, 40, 48): (56, 40, 24),
    (56, 56, 64): (80, 48, 32),
    (56, 64, 72): (88, 56, 32),
    (71, 70, 78): (96, 64, 40),
    (88, 88, 96): (120, 80, 48),
    (104, 104, 112): (144, 96, 56),
    (120, 118, 124): (168, 104, 64),
}
RECOLOUR = {"ship": SHIP_RECOLOUR}
MAX_SECONDARY_TILES = 512
MAX_SECONDARY_METATILES = 512
MB_NORMAL, MB_IMPASSABLE = 0x00, 0x01
METATILE_LAYER_TYPE_NORMAL = 0     # middle + top (include/global.fieldmap.h:24)
GROUND_SLOT = 10                   # spare secondary slot for the ground colour


def mode_downscale(idx, opaque):
    """2x2 -> 1 by most common index. Block is transparent unless >=40% opaque."""
    h, w = idx.shape
    out = np.zeros((h // 2, w // 2), np.uint8)
    op = np.zeros((h // 2, w // 2), bool)
    for y in range(h // 2):
        for x in range(w // 2):
            blk = idx[y * 2:y * 2 + 2, x * 2:x * 2 + 2].ravel()
            msk = opaque[y * 2:y * 2 + 2, x * 2:x * 2 + 2].ravel()
            if msk.mean() < 0.40:
                continue
            vals = blk[msk]
            if not len(vals):
                continue
            out[y, x] = np.bincount(vals).argmax()
            op[y, x] = True
    return out, op


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    sheet = np.array(Image.open(SHEET).convert("RGBA"))
    tilemap = OrderedDict()          # index-pattern -> tile id
    metatiles, attrs, palettes = [], [], {}
    manifest = []

    # --- ground tile for the bottom layer of every building metatile ---
    _, gr, gc = GROUND_TILE_SRC
    gblk = sheet[gr * CELL:(gr + 1) * CELL, gc * CELL:(gc + 1) * CELL]
    gop = gblk[:, :, 3] > 128
    gpx = gblk[gop][:, :3].astype(int)
    gbase = gpx[np.argmin(gpx @ np.array([0.299, 0.587, 0.114]))]
    gfull = gblk.copy()
    gfull[~gop, :3] = gbase                     # composite over its own shadow tone
    gpal = [tuple(int(v) for v in c)
            for c in np.unique(gfull[:, :, :3].reshape(-1, 3), axis=0)][:15]
    gidx = np.zeros((CELL, CELL), np.uint8)
    P = np.array(gpal)
    flat = gfull[:, :, :3].reshape(-1, 3).astype(int)
    gidx = (np.argmin(((flat[:, None] - P[None]) ** 2).sum(2), axis=1) + 1)
    gidx = gidx.astype(np.uint8).reshape(CELL, CELL)
    gsmall, _ = mode_downscale(gidx, np.ones_like(gidx, bool))
    gsub = gsmall[:8, :8]
    # Register the ground tile as secondary-relative index 0 BEFORE any
    # building tiles, so dedupe() numbers buildings from 1 upward. Both get the
    # +512 offset applied at metatile-write time.
    tilemap[gsub.tobytes()] = 0
    ground_tid = 0 + MAX_SECONDARY_TILES      # -> 512
    palettes[GROUND_SLOT] = [(0, 0, 0)] + gpal
    print(f"  ground tile from sheet r{gr}c{gc}: {len(gpal)} colours, slot {GROUND_SLOT}")

    for name, r0, r1, slot, c0, c1 in BUILD:
        blk = sheet[r0 * CELL:(r1 + 1) * CELL, c0 * CELL:(c1 + 1) * CELL].copy()
        rc = RECOLOUR.get(name)
        if rc:
            rgb = blk[:, :, :3]
            hit = 0
            for src, dst in rc.items():
                m = (rgb[:, :, 0] == src[0]) & (rgb[:, :, 1] == src[1]) & \
                    (rgb[:, :, 2] == src[2])
                hit += int(m.sum())
                rgb[m] = dst
            print(f"  {name}: recoloured {hit} px grey->oak")
        op_full = blk[:, :, 3] > 128
        px = blk[op_full][:, :3].astype(int)
        uniq, counts = np.unique(px, axis=0, return_counts=True)
        pal = reduce_palette(uniq, counts, 15)

        # map every source pixel to a palette index; index 0 stays transparent
        flat = blk[:, :, :3].reshape(-1, 3).astype(int)
        d = ((flat[:, None, :].astype(np.int32) - pal[None].astype(np.int32)) ** 2).sum(2)
        idx_full = (d.argmin(1) + 1).astype(np.uint8).reshape(blk.shape[:2])
        idx_full[~op_full] = 0

        idx16, op16 = mode_downscale(idx_full, op_full)
        palettes[slot] = [(0, 0, 0)] + [tuple(int(v) for v in c) for c in pal]

        rows, cols = (r1 - r0 + 1), (c1 - c0 + 1)
        made = 0
        for ry in range(rows):
            for cx in range(cols):
                cell = idx16[ry * 16:(ry + 1) * 16, cx * 16:(cx + 1) * 16]
                cellop = op16[ry * 16:(ry + 1) * 16, cx * 16:(cx + 1) * 16]
                if cellop.mean() < 0.02:
                    continue                      # skip empty cells entirely
                quad = []
                for qy in range(2):
                    for qx in range(2):
                        sub = cell[qy * 8:(qy + 1) * 8, qx * 8:(qx + 1) * 8]
                        tid, xf, yf = dedupe(tilemap, sub)
                        # +512: tile ids are a shared 0-1023 space, secondary
                        # starts at NUM_TILES_IN_PRIMARY (src/fieldmap.c:912).
                        quad.append((tid + MAX_SECONDARY_TILES, xf, yf))
                # TWO-LAYER ENCODING -- this is what produced the black
                # margins. A pokeemerald metatile has a bottom and a top layer.
                # Colour index 0 in the BOTTOM layer renders as the BACKDROP
                # colour (black), NOT transparent; only the TOP layer composites
                # over what is beneath. Writing the building into the bottom
                # layer and leaving the top empty turned every transparent pixel
                # around a roof into a black block.
                #
                # Vanilla proves the pattern: 71% of Petalburg's and 81% of
                # Lilycove's metatiles use the top layer. Attribute layer type
                # must be 0 = METATILE_LAYER_TYPE_NORMAL (middle + top); the old
                # code wrote 1 = COVERED (bottom + middle), which is for tiles
                # the player walks BEHIND.
                mt = b""
                for _ in range(4):                       # bottom: solid ground
                    mt += struct.pack("<H", (ground_tid & 0x3FF) |
                                      ((GROUND_SLOT & 15) << 12))
                for tid, xf, yf in quad:                 # top: the building
                    assert tid >= MAX_SECONDARY_TILES, \
                        f"secondary tile id {tid} < 512 would read the PRIMARY tileset"
                    mt += struct.pack("<H", (tid & 0x3FF) | (xf << 10) |
                                      (yf << 11) | ((slot & 15) << 12))
                metatiles.append(mt)
                solid = cellop.mean() > 0.85
                attrs.append(struct.pack("<H",
                             (MB_IMPASSABLE if solid else MB_NORMAL)
                             | (METATILE_LAYER_TYPE_NORMAL << 12)))
                made += 1
        manifest.append((name, slot, made))
        print(f"  {name:10s} slot {slot}  {made:3d} metatiles  "
              f"(tiles so far {len(tilemap)})")

    n_t, n_m = len(tilemap), len(metatiles)
    print(f"\ntiles      {n_t}/{MAX_SECONDARY_TILES}   headroom {MAX_SECONDARY_TILES-n_t}")
    print(f"metatiles  {n_m}/{MAX_SECONDARY_METATILES}   headroom {MAX_SECONDARY_METATILES-n_m}")
    assert n_t <= MAX_SECONDARY_TILES, f"tile budget exceeded: {n_t}"
    assert n_m <= MAX_SECONDARY_METATILES, f"metatile budget exceeded: {n_m}"
    if a.dry_run:
        print("dry run - nothing written")
        return

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "palettes").mkdir(exist_ok=True)
    write_tiles(tilemap, palettes)
    (OUT / "metatiles.bin").write_bytes(b"".join(metatiles))
    (OUT / "metatile_attributes.bin").write_bytes(b"".join(attrs))
    for s in range(16):
        cols = palettes.get(s, [(0, 0, 0)] * 16)
        cols = (list(cols) + [(0, 0, 0)] * 16)[:16]
        write_gbapal(OUT / "palettes" / f"{s:02d}.gbapal", cols)
        write_jasc(OUT / "palettes" / f"{s:02d}.pal", cols)
    print(f"wrote {OUT}")


def dedupe(tilemap, sub):
    """Return (tile_id, xflip, yflip), reusing a flipped match when possible."""
    for xf in (0, 1):
        for yf in (0, 1):
            v = sub
            if xf:
                v = v[:, ::-1]
            if yf:
                v = v[::-1, :]
            k = v.tobytes()
            if k in tilemap:
                return tilemap[k], xf, yf
    tilemap[sub.tobytes()] = len(tilemap)
    return tilemap[sub.tobytes()], 0, 0


def write_tiles(tilemap, palettes):
    n = len(tilemap)
    cols, rows = 16, -(-n // 16)
    page = np.zeros((rows * 8, cols * 8), np.uint8)
    for k, tid in tilemap.items():
        t = np.frombuffer(k, np.uint8).reshape(8, 8)
        y, x = (tid // 16) * 8, (tid % 16) * 8
        page[y:y + 8, x:x + 8] = t
    im = Image.fromarray(page, "P")
    flat = []
    for c in (palettes.get(6) or [(0, 0, 0)] * 16):
        flat += list(c)
    im.putpalette((flat + [0] * 768)[:768])
    im.save(OUT / "tiles.png")


def write_gbapal(path, cols):
    with open(path, "wb") as f:
        for r, g, b in cols:
            f.write(struct.pack("<H", (r >> 3) | ((g >> 3) << 5) | ((b >> 3) << 10)))


def write_jasc(path, cols):
    with open(path, "wb") as f:
        f.write(b"JASC-PAL\r\n0100\r\n16\r\n")
        for r, g, b in cols:
            f.write(f"{r} {g} {b}\r\n".encode())


if __name__ == "__main__":
    main()
