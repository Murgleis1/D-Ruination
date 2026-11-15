#!/usr/bin/env python3
"""
Derive tile ROLES from the real Evernahn maps, instead of guessing from colour.

WHY THIS EXISTS
---------------
Three tileset attempts failed because none of them knew what a tile WAS:

  1. Blueprint repaint  -- replaced a 324-metatile hand-designed map with 7
     metatiles of flat fill. Destroyed the level design. Reverted.
  2. Palette re-tint    -- recoloured vanilla Hoenn art. Still Hoenn trees and
     a Hoenn gym, just different colours. Too subtle to be a re-skin.
  3. Colour-class swap  -- classified 421 tiles by RGB mean, then wrote one
     source cell into every tile of a class. Tree canopy is green. Grass is
     green. Bush edges are green. It DELETED AN ENTIRE FOREST and mangled the
     gym, because a colour class is not a role.

The information was available the whole time. assets/pelluca_tileset_source/
contains Map005.rxdata and Map588.rxdata -- real RPG Maker maps built with the
Evernahn tileset -- plus Tilesets.rxdata describing the tilesets themselves.
How a tile is USED in a finished map tells you its role with no guessing:

  - a tile covering 88% of layer 0 is the ground fill
  - tiles that only ever appear on layer 1/2 are objects drawn OVER ground
  - tiles that appear directly above a ground tile in a fixed pair are the
     bottom half of a two-tile object (a trunk under a canopy)
  - a tile's neighbour distribution says whether it is a field, an edge or a
     corner

RPG MAKER LAYERS MAP CLEANLY ONTO GBA METATILE LAYERS
------------------------------------------------------
RPG Maker XP maps have 3 layers; a pokeemerald metatile has a bottom and a top.
Layer 0 is always ground, so it corresponds to the metatile BOTTOM layer, where
colour index 0 renders as backdrop black. Layers 1-2 are objects composited
over it, which is the metatile TOP layer where index 0 is transparent. This is
the same distinction that caused the black margins around buildings earlier.

Usage:
  python3 evernahn_maps.py --summary
  python3 evernahn_maps.py --roles          # infer and print tile roles
  python3 evernahn_maps.py --render out.png # draw the real Evernahn maps
"""
import argparse
import struct
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from rubymarshal.reader import loads

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "assets" / "pelluca_tileset_source"
MAPS = ["Map588.rxdata", "Map005.rxdata"]
# ONLY Map588 is built with the Evernahn tileset (Tilesets.rxdata id 30).
# Map005 uses id 23 "Polaris", whose image is NOT in the repo. Pooling it and
# reading its ids against Evernahn.png contributed 866 of 1453 role entries and
# flipped 37 Evernahn roles (measured 2026-11-15). Roles come from id-30 maps only.
EVERNAHN_TILESET_ID = 30

# RPG Maker XP tile id layout: ids below 384 are autotiles (48 variants each,
# starting at 48); 384+ index the tileset bitmap in reading order, 8 per row.
AUTOTILE_BASE = 384
TILESET_COLS = 8


def read_table(userdef):
    b = userdef._private_data if hasattr(userdef, "_private_data") else None
    if b is None:
        d = userdef.attributes
        b = list(d.values())[0]
    dim, xs, ys, zs, n = struct.unpack_from("<5i", b, 0)
    arr = np.frombuffer(b, dtype="<u2", count=n, offset=20)
    return arr.reshape((zs, ys, xs))


def load_map(name):
    m = loads((SRC / name).read_bytes())
    a = m.attributes
    return {
        "name": name,
        "tileset_id": a["@tileset_id"],
        "w": a["@width"],
        "h": a["@height"],
        "data": read_table(a["@data"]),
    }


def tile_to_cell(tid):
    """Tileset bitmap cell (row, col) for a non-autotile id."""
    if tid < AUTOTILE_BASE:
        return None
    i = tid - AUTOTILE_BASE
    return (i // TILESET_COLS, i % TILESET_COLS)


def infer_roles(maps):
    """Roles derived from placement, not colour."""
    layer_use = defaultdict(Counter)      # tid -> which layers it appears on
    counts = Counter()
    below = defaultdict(Counter)          # tid -> what sits directly under it
    for m in maps:
        d = m["data"]
        for z in range(d.shape[0]):
            for y in range(d.shape[1]):
                for x in range(d.shape[2]):
                    tid = int(d[z, y, x])
                    if tid == 0:
                        continue
                    layer_use[tid][z] += 1
                    counts[tid] += 1
                    if z > 0 and y + 1 < d.shape[1]:
                        below[tid][int(d[z, y + 1, x])] += 1

    roles = {}
    total_ground = sum(c for t, c in counts.items() if layer_use[t][0] == counts[t])
    for tid, n in counts.items():
        lu = layer_use[tid]
        ground_only = lu.get(0, 0) == n
        object_only = lu.get(0, 0) == 0
        if ground_only and n > total_ground * 0.05:
            roles[tid] = "ground_fill"
        elif ground_only:
            roles[tid] = "ground_detail"
        elif object_only:
            roles[tid] = "object"
        else:
            roles[tid] = "mixed"
    return roles, counts, layer_use


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--roles", action="store_true")
    ap.add_argument("--render")
    a = ap.parse_args()
    maps = [load_map(n) for n in MAPS]
    for m in maps:
        if m["tileset_id"] != EVERNAHN_TILESET_ID:
            print(f'{m["name"]}: tileset {m["tileset_id"]} is not Evernahn -- excluded')
    maps = [m for m in maps if m["tileset_id"] == EVERNAHN_TILESET_ID]

    if a.summary or not (a.roles or a.render):
        for m in maps:
            d = m["data"]
            print(f'{m["name"]}: tileset {m["tileset_id"]}, {m["w"]}x{m["h"]}, '
                  f'{d.shape[0]} layers')
            for z in range(d.shape[0]):
                c = Counter(d[z].ravel().tolist())
                c.pop(0, None)
                tot = sum(c.values())
                top = c.most_common(3)
                print(f"   layer {z}: {len(c):4d} tiles, {tot:5d} placements, "
                      f"top {[(t, f'{100*n/max(1,tot):.0f}%') for t, n in top]}")

    if a.roles:
        roles, counts, layer_use = infer_roles(maps)
        by = Counter(roles.values())
        print("\nroles inferred from PLACEMENT across both maps:")
        for k, n in by.most_common():
            print(f"  {n:5d}  {k}")
        print("\nground fills (the tiles that ARE the terrain):")
        for tid, r in sorted(roles.items(), key=lambda kv: -counts[kv[0]]):
            if r != "ground_fill":
                continue
            cell = tile_to_cell(tid)
            print(f"  tile {tid:5d}  {counts[tid]:6d} placements  "
                  f"sheet cell {cell}")


    if a.render:
        render(maps, a.render)


def render(maps, out):
    """Draw each Evernahn map at GAME scale (32px cells -> 16px by 2x MODE).

    Layers 0,1,2 composited in order, exactly as RPG Maker draws them.
    Autotiles (ids < 384) are drawn from the first 32x32 cell of their strip
    when present -- an approximation, marked as such; they are 4-7% of cells.
    """
    from PIL import Image
    sheet = Image.open(SRC / "Evernahn.png").convert("RGBA")
    auto = {}
    names = ["Evernahn_Grass_1", "Evernahn_Grass_2", "Evernahn_Grass_3",
             "Evernahn_Water", "Evernahn_Water_2"]
    for i, n in enumerate(names):
        f = SRC / f"{n}.png"
        if f.exists():
            auto[i] = Image.open(f).convert("RGBA").crop((0, 0, 32, 32))
    for m in maps:
        d = m["data"]
        img = Image.new("RGBA", (m["w"] * 32, m["h"] * 32), (0, 0, 0, 255))
        for z in range(d.shape[0]):
            for y in range(m["h"]):
                for x in range(m["w"]):
                    t = int(d[z, y, x])
                    if t == 0:
                        continue
                    if t >= AUTOTILE_BASE:
                        r, c = tile_to_cell(t)
                        cell = sheet.crop((c * 32, r * 32, c * 32 + 32, r * 32 + 32))
                    else:
                        cell = auto.get(t // 48 - 1)
                        if cell is None:
                            continue
                    img.alpha_composite(cell, (x * 32, y * 32))
        a = np.array(img)
        h, w = a.shape[0] // 2, a.shape[1] // 2
        blocks = a.reshape(h, 2, w, 2, 4).transpose(0, 2, 1, 3, 4).reshape(h, w, 4, 4)
        small = np.zeros((h, w, 4), np.uint8)
        for yy in range(h):
            for xx in range(w):
                u, cnt = np.unique(blocks[yy, xx], axis=0, return_counts=True)
                small[yy, xx] = u[cnt.argmax()]
        p = Path(out)
        dest = p.with_name(f"{p.stem}_{m['name'].split('.')[0]}{p.suffix}")
        Image.fromarray(small).convert("RGB").save(dest)
        print(f"wrote {dest} ({w}x{h}, game scale)")


if __name__ == "__main__":
    main()
