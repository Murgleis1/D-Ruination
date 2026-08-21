#!/usr/bin/env python3
"""
Add grass and water terrain to gTileset_Evernahn (PRIMARY), palette slot 5.

WHY THIS IS NEEDED
------------------
The 80x60 Pelluca repaint is blocked without it. The blueprint is 40.5% grass
and 13.8% water -- 2605 of 4800 cells -- and gTileset_Evernahn contains NO
grass and no usable water. Its 189 metatiles are the gTileset_Autumn cliff/path
merge plus Evernahn structural pieces.

GRASS COMES FROM THE MAIN SHEET, NOT THE Evernahn_Grass_*.png STRIPS
--------------------------------------------------------------------
All three Grass_*.png strips depict FLOWERS (Grass_2, Grass_3) or brown dirt
tufts (Grass_1) -- decorative overlays meant to layer over ground, only 50-67%
opaque. Painting a map with them produced a full screen of magenta and yellow
speckle that was unreadable in-game.

Real plain grass was inside the building blocks of Evernahn.png the whole time.
The user identified the exact cells:

    row 71 col c5   mean RGB (123,147,77)  G-R +24  4 colours   <- lighter
    row 72 col c5   mean RGB ( 90,116,45)  G-R +26  4 colours   <- darker

Four colours each is already flat, so no contrast surgery is applied -- unlike
the 9-11 colour flower strips. They are ~80-87% opaque (they carry transparent
tufts) so they still go through composite_over_base.

PALETTE SLOT 5
--------------
The only free slot in the primary: slots 0-4 carry 444/8/88/339/449 quadrant
references, slot 5 none. The handoff earmarked it for the three shared
buildings, but those moved to gTileset_Pelluca SECONDARY once measurement showed
they need ~5 slots between them. That move freed the slot the terrain needs.

Slot 1 looks nearly free (2 colours) but IS referenced by 8 quadrants, so it is
not safe to reclaim without tracing what uses it. Left alone.

APPENDS ONLY. Existing metatile ids 0-188 are untouched, so every map already
painted against this tileset keeps working. New terrain starts at 189.

Downscale is 32->16 by MODE, never averaging -- averaging invents colours
outside the palette and softens edges.

Usage: python3 tools/evernahn_conversion/add_terrain.py [--dry-run]
"""
import argparse
import json
import struct
from pathlib import Path

import numpy as np
from PIL import Image

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SRC = REPO / "assets" / "pelluca_tileset_source"
TS = REPO / "codebase" / "data" / "tilesets" / "primary" / "evernahn"
SHEET_PNG = "Evernahn.png"
SLOT = 5
CELL = 32
MAX_PRIMARY_TILES = 512
MAX_PRIMARY_METATILES = 512

# label -> (source, cell). source is a strip filename or ("SHEET", row, col).
# GROUND GRASS comes from Calvera r170c4. TALL/ROUTE GRASS is the Evernahn
# foliage cell that was previously (wrongly) used as ground.
#
# WHY THE SWAP. Evernahn r71c5 has a luminance range of 0-200: foliage art with
# deep black shadow gaps, which read as depth between bushes. Tiled 150 times
# across a screen as ground it measured stddev 41.9 against vanilla Emerald
# grass at 10-18, and rendered in-game as an unreadable green-and-tan
# checkerboard. Those same dark gaps are exactly right for TALL GRASS, so the
# cell is kept -- just for the correct job.
#
# Calvera r170c4 measures stddev 9.4 tiled, RGB(129,169,145), 3 colours -- a
# muted sage that sits in vanilla's band and suits Pelluca's dusk palette.
#
# The search that found it had a bug worth recording: the green test was
# "G > R + 8" and never compared green to BLUE, so blue-grey WATER at
# RGB(94,127,163) passed as grass. A colour test for green must beat both other
# channels.
TERRAIN = [
    ("grass", ("CALVERA", 170, 4), 0),
    ("grass_alt", ("CALVERA", 170, 3), 0),
    ("tall_grass", ("SHEET", 71, 5), 0),
    ("water", "Evernahn_Water.png", 0),
    ("water_alt", "Evernahn_Water.png", 1),
]
CALVERA_PNG = "Calvera.png"
MB_TALL_GRASS = 0x02
MB_NORMAL, MB_IMPASSABLE = 0x00, 0x01
METATILE_LAYER_TYPE_COVERED = 1     # ground: bottom + middle, nothing above


def fetch(src, cell):
    """Return a 32x32 RGBA block from either an autotile strip or the main sheet."""
    if isinstance(src, tuple) and src[0] in ("SHEET", "CALVERA"):
        kind, r, c = src
        png = SHEET_PNG if kind == "SHEET" else CALVERA_PNG
        a = np.array(Image.open(SRC / png).convert("RGBA"))
        return a[r * CELL:(r + 1) * CELL, c * CELL:(c + 1) * CELL]
    a = np.array(Image.open(SRC / src).convert("RGBA"))
    return a[0:CELL, cell * CELL:(cell + 1) * CELL]


def composite_over_base(blk):
    """Flatten a partly-transparent cell onto a solid base so it works as ground.

    Base is the darkest colour present, which is the shadow/earth tone the
    artist intended underneath. Ground tiles occupy the BOTTOM layer where
    colour index 0 renders as backdrop black, so they must be fully opaque.
    """
    rgb = blk[:, :, :3].astype(int)
    op = blk[:, :, 3] > 128
    if not op.any():
        return blk
    vis = rgb[op]
    base = vis[np.argmin(vis @ np.array([0.299, 0.587, 0.114]))]
    out = blk.copy()
    out[~op, :3] = base
    out[:, :, 3] = 255
    return out


def mode_downscale(idx):
    h, w = idx.shape
    out = np.zeros((h // 2, w // 2), np.uint8)
    for y in range(h // 2):
        for x in range(w // 2):
            blk = idx[y * 2:y * 2 + 2, x * 2:x * 2 + 2].ravel()
            out[y, x] = np.bincount(blk).argmax()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    pal = []
    blocks = {}
    for label, src, cell in TERRAIN:
        blk = composite_over_base(fetch(src, cell))
        blocks[label] = blk
        for c in np.unique(blk[:, :, :3].reshape(-1, 3), axis=0):
            t = tuple(int(v) for v in c)
            if t not in pal:
                pal.append(t)
    assert len(pal) <= 15, f"terrain needs {len(pal)} colours, slot holds 15"
    print(f"shared palette: {len(pal)}/15 colours, no reduction applied")

    page = np.array(Image.open(TS / "tiles.png").convert("P"))
    tw = page.shape[1] // 8
    n_existing = tw * (page.shape[0] // 8)
    mt_old = (TS / "metatiles.bin").read_bytes()
    at_old = (TS / "metatile_attributes.bin").read_bytes()
    n_mt = len(mt_old) // 16
    print(f"existing: {n_mt} metatiles, {n_existing} tile slots")

    newtiles, newmt, newat, manifest = {}, [], [], []
    P = np.array(pal)
    for label, _, _ in TERRAIN:
        blk = blocks[label]
        flat = blk[:, :, :3].reshape(-1, 3).astype(int)
        idx = (np.argmin(((flat[:, None] - P[None]) ** 2).sum(2), axis=1) + 1)
        idx = idx.astype(np.uint8).reshape(CELL, CELL)
        small = mode_downscale(idx)
        quad = []
        for qy in range(2):
            for qx in range(2):
                sub = small[qy * 8:(qy + 1) * 8, qx * 8:(qx + 1) * 8]
                k = sub.tobytes()
                if k not in newtiles:
                    newtiles[k] = n_existing + len(newtiles)
                quad.append(newtiles[k])
        mt = b""
        for tid in quad:
            mt += struct.pack("<H", (tid & 0x3FF) | ((SLOT & 15) << 12))
        mt += struct.pack("<H", 0) * 4
        newmt.append(mt)
        if label.startswith("water"):
            beh = MB_IMPASSABLE
        elif label == "tall_grass":
            beh = MB_TALL_GRASS
        else:
            beh = MB_NORMAL
        newat.append(struct.pack("<H", beh |
                                 (METATILE_LAYER_TYPE_COVERED << 12)))
        manifest.append((label, n_mt + len(newmt) - 1))

    tot_t, tot_m = n_existing + len(newtiles), n_mt + len(newmt)
    print(f"\nnew: {len(newtiles)} tiles, {len(newmt)} metatiles")
    print(f"tiles      {tot_t}/{MAX_PRIMARY_TILES}")
    print(f"metatiles  {tot_m}/{MAX_PRIMARY_METATILES}")
    for label, mid in manifest:
        print(f"   metatile {mid:3d}  {label}")
    assert tot_t <= MAX_PRIMARY_TILES and tot_m <= MAX_PRIMARY_METATILES
    if a.dry_run:
        print("dry run - nothing written")
        return

    rows = -(-tot_t // tw)
    newpage = np.zeros((rows * 8, tw * 8), np.uint8)
    newpage[:page.shape[0], :page.shape[1]] = page
    for k, tid in newtiles.items():
        t = np.frombuffer(k, np.uint8).reshape(8, 8)
        y, x = (tid // tw) * 8, (tid % tw) * 8
        newpage[y:y + 8, x:x + 8] = t
    im = Image.fromarray(newpage, "P")
    im.putpalette(Image.open(TS / "tiles.png").convert("P").getpalette())
    im.save(TS / "tiles.png")

    (TS / "metatiles.bin").write_bytes(mt_old + b"".join(newmt))
    (TS / "metatile_attributes.bin").write_bytes(at_old + b"".join(newat))

    cols = ([(0, 0, 0)] + pal + [(0, 0, 0)] * 16)[:16]
    with open(TS / "palettes" / f"{SLOT:02d}.gbapal", "wb") as fh:
        for r, g, b in cols:
            fh.write(struct.pack("<H", (r >> 3) | ((g >> 3) << 5) | ((b >> 3) << 10)))
    with open(TS / "palettes" / f"{SLOT:02d}.pal", "wb") as fh:
        fh.write(b"JASC-PAL\r\n0100\r\n16\r\n")
        for r, g, b in cols:
            fh.write(f"{r} {g} {b}\r\n".encode())

    (SRC / "evernahn_terrain_manifest.json").write_text(
        json.dumps({label: mid for label, mid in manifest}, indent=2))
    print("wrote tileset + evernahn_terrain_manifest.json")


if __name__ == "__main__":
    main()
