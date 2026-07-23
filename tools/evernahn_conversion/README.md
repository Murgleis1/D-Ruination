# Evernahn / Pelluca tileset conversion

Reusable tooling + record of the Pelluca Valley conversion. **Read
`lib_convert.py`'s docstrings first** - they encode findings from approaches that
were tried and failed, not just the happy path.

## Files
- `lib_convert.py` - the reusable library (downscale, keying, palette recovery,
  metatile encoding, gap fill). Import it; nothing runs on load.
- `convert_autotiles.py` - **DONE + committed.** Converts the grass/water/pool
  autotiles into `gTileset_Evernahn` (primary). Re-run only to rebuild from
  source. Idempotent-ish: it overwrites the evernahn tileset files.
- `merge_cliffs_paths.py` - **THE IMMEDIATE NEXT STEP.** Merges the selected
  `gTileset_Autumn` cliff/path metatiles into `gTileset_Evernahn`. Reads the
  committed selection in `assets/pelluca_dock_spec/autumn_cliff_path_selection.json`.

## The environment facts that bite
- Build: `cd codebase && timeout 290 make modern`. Foreground, ~5 min. Tileset
  changes need the `.png`/`.bin` present; the build compresses `tiles.png` ->
  `tiles.4bpp.lz` itself.
- A tileset dir needs **all 16** `NN.gbapal` + `NN.pal` even if only a few carry
  colour, or the build errors on the first missing one.
- Registering a new primary tileset touches THREE files, and the vanilla anchors
  (`gTileset_General`, `gMetatiles_General`, `gTilesetTiles_General`) may not be
  first - safest to PREPEND the new declarations to `graphics.h`/`metatiles.h`
  (declaration order is irrelevant) and insert before the General struct in
  `headers.h`.
- NUM_PALS_IN_PRIMARY = 6. A primary tileset owns sub-palettes 0-5; a secondary
  owns 6-12. So a primary map tile can only use palette slots 0-5.

## Palette budget of gTileset_Evernahn (primary, 6 slots)
- 0 grass, 1 water, 2 pool/clay  (USED - the autotile pass)
- 3, 4 - reserved for autumn cliff + path palettes (the merge step)
- 5 - free (buildings, or spill)

## Verification without a working image viewer
The `view`/image tool was blind for this entire project. Everything visual was
verified by (a) decoding the built `.4bpp` back to pixels and asserting it equals
the source `.png`, and (b) rendering metatiles to a PNG and using `present_files`
so the USER can see it. Always confirm colour counts / byte-equality in code;
never assume the build did what you intended.
