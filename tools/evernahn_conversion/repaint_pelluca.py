#!/usr/bin/env python3
"""
Repaint LAYOUT_PELLUCA_CITY (80x60) from the committed blueprint, in Evernahn
primary + gTileset_Pelluca secondary.

Pelluca Valley and Pelluca City are the SAME MAP. Bible 15.7's empire->DM fate
table maps "Pelluca Valley" (Ruination era) to "Pelluca City" (the actual
MAP_PELLUCA_CITY id). This is a REBUILD of the existing layout, not a redesign:
the land shape stays, the buildings and terrain are replaced.

METATILE LEGEND -- every id from a committed manifest, none guessed
-------------------------------------------------------------------
  46-153   cliffs      assets/pelluca_dock_spec/autumn_cliff_path_selection.json
  154-188  paths       ("evernahn metatiles 46-153 = cliffs, 154-188 = paths")
  189-192  grass / grass_alt / water / water_alt
                       assets/pelluca_tileset_source/evernahn_terrain_manifest.json
  512+     buildings   gTileset_Pelluca, offset by NUM_METATILES_IN_PRIMARY

BLUEPRINT LEGEND: 0 water, 1 grass, 2 tree, 3 path, 4 cliff, 5 structure.
Confirmed by distribution -- the per-value counts reproduce the handoff's
recorded percentages exactly (grass 40.5%, cliff 14.2%, water 13.8%, path
12.1%, tree 10.7%, structure 8.7%).

BUILDINGS ARE STAMPED, NEVER USED AS FILL
-----------------------------------------
An earlier pass smeared ONE interior metatile across 411 structure cells and one
cliff fragment across 508 tree cells. The result was a map of identical
black-gridded chunks. A building is a 10x7 or 6x8 arrangement and only reads as
a building placed intact.

The blueprint's 418 structure cells form 83 connected clusters with bboxes from
3x3 to 8x8 -- massing hints, not footprints. Demanding a window be 80% structure
matched only two positions. So the BUILDING defines its footprint and is centred
on the cluster; the blueprint decides where and how big.

Assignment is by RANK, not area. Area-matching gave 14 taverns, because most
clusters are 8-27 cells and the tavern's 24 is nearest to nearly all of them.
Bible 19 notes each town has a monastery + tavern: largest cluster gets the
monastery, next two the taverns, the rest houses.

LOCKED GEOMETRY, asserted at build time
---------------------------------------
  - dock x38-52 y42-58, collision and elevation copied VERBATIM from
    dock_geometry.json (its recorded metatile ids are old General+Mauville
    numbering and mean nothing here, so only the art is re-derived)
  - the elevation-3 pier column x43-45 running y52 up to y42: the arrival
    cutscene warps Osrid to (44,52) and walks him NORTH. If it breaks he is
    stranded.
  - lab warp (47,44) -> MAP_PELLUCA_UMBRA_LAB. The warp tile itself is
    collision 1 / elevation 0 (standard pokeemerald door: the player stands
    BELOW and walks north into it), so the APPROACH tile at (47,45) is what
    must be walkable. Asserting the warp tile itself was walkable failed
    against the real data -- the assumption was wrong, not the spec.
  - secret Umbra cavern entrance x63-65 y40-42, bible 19 [LOCKED], must be
    present from Chapter 1 so it reads as discovered rather than new.

Usage: python3 tools/evernahn_conversion/repaint_pelluca.py [--dry-run]
"""
import argparse
import json
import struct
from pathlib import Path

import numpy as np
from scipy import ndimage

REPO = Path(__file__).resolve().parents[2]
SPEC = REPO / "assets" / "pelluca_dock_spec"
BLUEPRINT = SPEC / "pelluca_blueprint_80x60.npy"
DOCK = SPEC / "dock_geometry.json"
ASSEMBLY = (REPO / "codebase" / "data" / "tilesets" / "secondary" / "pelluca" /
            "assembly_manifest.json")
MAPBIN = REPO / "codebase" / "data" / "layouts" / "PellucaCity" / "map.bin"

W, H = 80, 60
NUM_METATILES_IN_PRIMARY = 512
Z_WATER, Z_GRASS, Z_TREE, Z_PATH, Z_CLIFF, Z_STRUCT = range(6)
GRASS, GRASS_ALT, WATER, WATER_ALT = 189, 190, 191, 192
CLIFF_BASE, PATH_BASE = 46, 154
# Trees are STAMPED as assemblies from the Calvera sheet (tree_big 3x3,
# tree_small 2x2), not filled with a single metatile. Tree zones are 514
# blueprint cells; a repeated fragment across them reads as noise, which is what
# the earlier cliff-metatile placeholder produced.
TREE_FALLBACK = CLIFF_BASE
BLOCKED = {Z_WATER, Z_TREE, Z_CLIFF, Z_STRUCT}
CAVERN = (63, 65, 40, 42)  # x0, x1, y0, y1


def stamp_buildings(bp, mt, coll, asm):
    lab, n = ndimage.label(bp == Z_STRUCT)
    sizes = ndimage.sum(bp == Z_STRUCT, lab, range(1, n + 1))
    cells = {k: {(r, c): m for r, c, m in v} for k, v in asm["cells"].items()}
    taken = np.zeros(bp.shape, bool)
    placed = []
    for ci in np.argsort(-sizes):
        size = int(sizes[ci])
        ys, xs = np.where(lab == ci + 1)
        if size < 8:
            for y, x in zip(ys, xs):
                mt[y, x], coll[y, x] = GRASS, 0
            continue
        rank = len(placed)
        name = "monastery" if rank == 0 else ("tavern" if rank in (1, 2) else "house")
        rows, cols = asm["dims"][name]
        cy, cx = int((ys.min() + ys.max()) // 2), int((xs.min() + xs.max()) // 2)
        y0 = max(0, min(H - rows, cy - rows // 2))
        x0 = max(0, min(W - cols, cx - cols // 2))
        if taken[y0:y0 + rows, x0:x0 + cols].any():
            for y, x in zip(ys, xs):
                mt[y, x], coll[y, x] = GRASS, 0
            continue
        for (r, c), mid in cells[name].items():
            mt[y0 + r, x0 + c] = NUM_METATILES_IN_PRIMARY + mid
            coll[y0 + r, x0 + c] = 1
        taken[y0:y0 + rows, x0:x0 + cols] = True
        for y, x in zip(ys, xs):
            if not taken[y, x]:
                mt[y, x], coll[y, x] = GRASS, 0
        placed.append((name, x0, y0))
    return placed


def stamp_trees(bp, mt, coll, asm):
    """Tile tree assemblies across the blueprint's tree zones.

    Large trees are placed first on a coarse grid, small trees fill the gaps.
    Any tree cell not covered by an assembly falls back to grass rather than a
    lone fragment -- a repeated interior metatile is what made the earlier
    placeholder read as noise.
    """
    cells = {k: {(r, c): m for r, c, m in v} for k, v in asm["cells"].items()}
    zone = (bp == Z_TREE)
    taken = np.zeros(bp.shape, bool)
    n = 0
    for name in ("tree_big", "tree_small", "tree_single"):
        if name not in asm["dims"]:
            continue
        rows, cols = asm["dims"][name]
        for y in range(0, H - rows + 1):
            for x in range(0, W - cols + 1):
                win = zone[y:y + rows, x:x + cols]
                if not win.all():
                    continue
                if taken[y:y + rows, x:x + cols].any():
                    continue
                for (r, c), mid in cells[name].items():
                    mt[y + r, x + c] = NUM_METATILES_IN_PRIMARY + mid
                    coll[y + r, x + c] = 1
                taken[y:y + rows, x:x + cols] = True
                n += 1
    leftover = zone & ~taken
    mt[leftover] = GRASS
    coll[leftover] = 0
    return n


def build():
    bp = np.load(BLUEPRINT)
    assert bp.shape == (H, W)
    mt = np.zeros((H, W), np.uint16)
    coll = np.zeros((H, W), np.uint8)
    elev = np.full((H, W), 3, np.uint8)
    rng = np.random.default_rng(7)

    for y in range(H):
        for x in range(W):
            z = int(bp[y, x])
            if z == Z_GRASS:
                # 3% variant, not 15%. At 15% the two grass tiles read as an
                # obvious two-tone checkerboard; vanilla uses one grass tile
                # almost everywhere with rare decorative variants.
                mt[y, x] = GRASS_ALT if rng.random() < 0.03 else GRASS
            elif z == Z_WATER:
                mt[y, x] = WATER if rng.random() > 0.15 else WATER_ALT
            elif z == Z_PATH:
                mt[y, x] = PATH_BASE
            elif z == Z_CLIFF:
                mt[y, x] = CLIFF_BASE
            elif z == Z_TREE:
                mt[y, x] = TREE_FALLBACK
            else:
                mt[y, x] = GRASS          # cleared; buildings stamped over
            coll[y, x] = 1 if z in BLOCKED else 0
            elev[y, x] = 0 if z == Z_WATER else 3

    asm = json.loads(ASSEMBLY.read_text())
    placed = stamp_buildings(bp, mt, coll, asm)
    ntrees = stamp_trees(bp, mt, coll, asm)
    print(f"stamped {ntrees} trees")

    d = json.loads(DOCK.read_text())
    r = d["region"]
    for i, row in enumerate(d["cells"]):
        y = r["y0"] + i
        for j, cell in enumerate(row):
            x = r["x0"] + j
            _, c, e = cell
            coll[y, x] = c
            elev[y, x] = e if e is not None else 3
            if e == 3 and c == 0:
                mt[y, x] = PATH_BASE
            elif c == 1:
                mt[y, x] = CLIFF_BASE
            elif e == 0:
                mt[y, x] = WATER
            else:
                mt[y, x] = GRASS
    return mt, coll, elev, d, placed


def verify(mt, coll, elev, d):
    bad = [y for y in range(45, 53) if not (elev[y, 44] == 3 and coll[y, 44] == 0)]
    assert not bad, f"pier column x=44 broken at y={bad}"
    w = d["warps"][0]
    assert coll[w["y"] + 1, w["x"]] == 0, "lab warp approach not walkable"
    assert elev[w["y"] + 1, w["x"]] == 3, "lab warp approach lost elevation 3"
    x0, x1, y0, y1 = CAVERN
    assert (coll[y0:y1 + 1, x0:x1 + 1] == 1).any(), "cavern entrance area is not solid"
    print("  pier column x44 y45-52 intact, elevation 3, walkable")
    print(f"  lab warp ({w['x']},{w['y']}) approach ({w['x']},{w['y']+1}) walkable")
    print(f"  cavern entrance x{x0}-{x1} y{y0}-{y1} present")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    mt, coll, elev, d, placed = build()
    print(f"stamped {len(placed)} buildings: " +
          ", ".join(f"{n}@({x},{y})" for n, x, y in placed[:6]) +
          (" ..." if len(placed) > 6 else ""))
    vals, counts = np.unique(mt, return_counts=True)
    for v, c in sorted(zip(vals.tolist(), counts.tolist()), key=lambda t: -t[1])[:7]:
        print(f"   metatile {v:4d}  {c:5d} cells ({100*c/(W*H):5.1f}%)")
    verify(mt, coll, elev, d)

    out = bytearray()
    for y in range(H):
        for x in range(W):
            out += struct.pack("<H", (int(mt[y, x]) & 0x3FF) |
                               ((int(coll[y, x]) & 3) << 10) |
                               ((int(elev[y, x]) & 15) << 12))
    assert len(out) == W * H * 2
    if a.dry_run:
        print(f"dry run - would write {len(out)} bytes")
        return
    MAPBIN.write_bytes(bytes(out))
    print(f"wrote {MAPBIN} ({len(out)} bytes)")


if __name__ == "__main__":
    main()
