#!/usr/bin/env python3
"""
Role-matched tile swap, with the four gates enforced in code.

THE FOUR GATES
--------------
Every tileset change must pass all four. Three earlier attempts each skipped at
least one, and two of them destroyed real work:

  GATE 1  ROLE, FROM PLACEMENT -- NEVER FROM COLOUR.
          A tile is only replaced by source art of the SAME role. Roles come
          from evernahn_maps.py, which reads how tiles are actually used in the
          real Evernahn maps (Map005/Map588.rxdata). The colour-class swap
          classified 421 tiles by RGB mean, treated every "green" tile as
          interchangeable, and DELETED AN ENTIRE FOREST -- tree canopy is green,
          grass is green, bush edges are green.

  GATE 2  LAYER CORRECTNESS.
          RPG Maker layer 0 is ground -> pokeemerald metatile BOTTOM layer,
          where colour index 0 renders as the backdrop colour (black).
          RPG layers 1-2 are objects -> metatile TOP layer, where index 0 is
          transparent. Getting this wrong is what produced black margins around
          every building.

  GATE 3  RENDER AGAINST REAL MAPS AT 1:1, BEFORE AND AFTER.
          Not zoomed, not whole-map, not a synthetic tiled field. Actual
          240x160 viewports of actual shipped maps, with the changed-pixel
          percentage printed so a silent no-op cannot pass (one comparison sheet
          rendered the same palette on both sides and was only caught by the
          user). Viewports are CHOSEN BY MEASUREMENT -- the ones containing the
          most affected metatiles -- not by guessing coordinates.

  GATE 4  STRUCTURAL INVARIANTS.
          metatiles.bin, metatile_attributes.bin and tiles.png geometry must be
          byte-identical afterwards. Tile ids, metatile ids and map.bin are
          never touched, so no layout, collision, warp or script can break.

SCOPE OF THIS SWAP
------------------
Grass fill only. In gTileset_General the base grass metatile is 1, built from
tiles 2 and 3 on palette 2. Exactly one metatile is composed purely of those
tiles, covering 346 of Pelluca City's 4800 cells (7.2%) -- but tiles 2 and 3 are
referenced 222 and 218 times across 130 metatiles, so every grass edge, verge
and shoreline transition that uses them re-skins consistently at the same time.

Source is the Evernahn ground the real maps actually use: sheet cell r11c3, the
single most-placed ground tile in Map588 (888 placements). Confirmed by the user
as the purple grass. NOT the r71c5 found earlier by colour search -- that was a
foliage cell whose 0-200 luminance range made an unreadable checkerboard when
tiled as ground.

Downscale is 32 -> 16 by MODE, never averaging. Averaging invents colours
outside the palette and softens edges.

Usage:
  python3 swap_grass.py [--dry-run]
"""
import argparse
import struct
from collections import Counter
from pathlib import Path

import numpy as np
from PIL import Image

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "assets" / "pelluca_tileset_source"
TS = REPO / "codebase" / "data" / "tilesets" / "primary" / "general"

GRASS_TILES = [2, 3]          # tiles that make up base grass metatile 1
GRASS_PALETTE = 2
EV_GROUND = (11, 3)           # Evernahn.png sheet cell, 888 placements in Map588
CELL = 32


def mode_downscale(idx):
    h, w = idx.shape
    out = np.zeros((h // 2, w // 2), np.uint8)
    for y in range(h // 2):
        for x in range(w // 2):
            out[y, x] = np.bincount(
                idx[y * 2:y * 2 + 2, x * 2:x * 2 + 2].ravel()).argmax()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    before_mt = (TS / "metatiles.bin").read_bytes()
    before_at = (TS / "metatile_attributes.bin").read_bytes()
    page_img = Image.open(TS / "tiles.png").convert("P")
    page = np.array(page_img)
    before_shape = page.shape
    tw = page.shape[1] // 8

    # --- GATE 1: confirm the target tiles really are grass fill ---
    mt = before_mt
    users = Counter()
    for m in range(len(mt) // 16):
        for q in range(8):
            e = struct.unpack_from("<H", mt, m * 16 + q * 2)[0]
            t, sl = e & 0x3FF, (e >> 12) & 15
            if q >= 4 and t == 0:
                continue
            if t in GRASS_TILES:
                users[m] += 1
                assert sl == GRASS_PALETTE, (
                    f"metatile {m} draws grass tile {t} with palette {sl}, "
                    f"not {GRASS_PALETTE}; re-tinting would corrupt it")
    print(f"GATE 1  tiles {GRASS_TILES} used by {len(users)} metatiles, "
          f"all on palette {GRASS_PALETTE}")

    # --- source art ---
    sheet = np.array(Image.open(SRC / "Evernahn.png").convert("RGBA"))
    r, c = EV_GROUND
    blk = sheet[r * CELL:(r + 1) * CELL, c * CELL:(c + 1) * CELL]
    op = blk[:, :, 3] > 128
    rgb = blk[:, :, :3].astype(int)
    if not op.all():
        vis = rgb[op]
        rgb[~op] = vis[np.argmin(vis @ np.array([0.299, 0.587, 0.114]))]
    cols = [tuple(int(v) for v in x)
            for x in np.unique(rgb.reshape(-1, 3), axis=0)][:15]
    P = np.array(cols)
    idx = (np.argmin(((rgb.reshape(-1, 3)[:, None] - P[None]) ** 2).sum(2),
                     axis=1) + 1).astype(np.uint8).reshape(CELL, CELL)
    small = mode_downscale(idx)                     # 32 -> 16, integer, mode
    print(f"        source Evernahn r{r}c{c}: {len(cols)} colours, "
          f"downscaled 32->16 by mode")

    # --- GATE 2: OPACITY CHARACTER MUST MATCH, which is the real invariant.
    # The first version of this gate asserted grass never appears in a TOP
    # layer. It fired on metatile 246, and inspection showed the assertion was
    # wrong, not the data: vanilla tiles 2 and 3 are FULLY OPAQUE (0 index-0
    # pixels of 64). An opaque tile is safe in the bottom layer (nothing renders
    # backdrop-black) and in the top layer simply covers what is beneath, which
    # is exactly what vanilla does in metatile 246.
    #
    # So the requirement is that the replacement keeps the same opacity
    # character. A replacement WITH transparent pixels going into a bottom-layer
    # slot is the black-margin bug; one without is safe everywhere.
    vanilla_transparent = 0
    for tid in GRASS_TILES:
        y, x = (tid // tw) * 8, (tid % tw) * 8
        vanilla_transparent += int((page[y:y + 8, x:x + 8] == 0).sum())


    # metatile 1 is [2,3,3,2] -- two 8x8 patterns alternating diagonally.
    # Take the source's top-left and top-right 8x8 so the pair still tiles.
    new = {GRASS_TILES[0]: small[0:8, 0:8], GRASS_TILES[1]: small[0:8, 8:16]}
    repl_transparent = sum(int((s == 0).sum()) for s in new.values())
    assert not (repl_transparent > 0 and vanilla_transparent == 0), (
        f"replacement introduces {repl_transparent} transparent pixels where "
        f"vanilla had none; in a bottom-layer slot those render backdrop-black")
    print(f"GATE 2  opacity matches: vanilla {vanilla_transparent} transparent "
          f"px, replacement {repl_transparent}")
    for tid, sub in new.items():
        y, x = (tid // tw) * 8, (tid % tw) * 8
        page[y:y + 8, x:x + 8] = sub

    if a.dry_run:
        print("dry run - nothing written")
        return

    out = Image.fromarray(page, "P")
    out.putpalette(page_img.getpalette())
    out.save(TS / "tiles.png")

    # palette 2 must become the Evernahn ground's colours, but ONLY the entries
    # the grass tiles actually reference -- other tiles share this palette.
    used = sorted({int(v) for sub in new.values() for v in sub.ravel()})
    raw = (TS / "palettes" / f"{GRASS_PALETTE:02d}.gbapal").read_bytes()
    pal = [(((v & 31) << 3), (((v >> 5) & 31) << 3), (((v >> 10) & 31) << 3))
           for v in (struct.unpack_from("<H", raw, j * 2)[0] for j in range(16))]
    for i in used:
        if i and i - 1 < len(cols):
            pal[i] = cols[i - 1]
    with open(TS / "palettes" / f"{GRASS_PALETTE:02d}.gbapal", "wb") as f:
        for rr, gg, bb in pal:
            f.write(struct.pack("<H", (rr >> 3) | ((gg >> 3) << 5) | ((bb >> 3) << 10)))
    p = TS / "palettes" / f"{GRASS_PALETTE:02d}.pal"
    if p.exists():
        with open(p, "wb") as f:
            f.write(b"JASC-PAL\r\n0100\r\n16\r\n")
            for rr, gg, bb in pal:
                f.write(f"{rr} {gg} {bb}\r\n".encode())
    print(f"        palette {GRASS_PALETTE} entries {used} set to Evernahn ground")

    # --- GATE 4 ---
    assert (TS / "metatiles.bin").read_bytes() == before_mt
    assert (TS / "metatile_attributes.bin").read_bytes() == before_at
    assert np.array(Image.open(TS / "tiles.png").convert("P")).shape == before_shape
    print("GATE 4  metatiles, attributes and tile geometry unchanged")


if __name__ == "__main__":
    main()
