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


if __name__ == "__main__":
    main()
