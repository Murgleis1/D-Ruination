# MonoMyth ROM reader (asset source, used with the developers' permission)

The ROM is NOT committed. Point `MONOMYTH_ROM` at your copy (default
`/home/claude/monomyth.gba`; header `POKEMON MONO` / `MONE`, RHH expansion,
sha1 ca01c7a7bb5cf09dd0be3f7be37c45b69dc9a18a).

## Facts measured, not assumed
- Region-map table at ROM 0xA166AC, 8-byte entries {x,y,w,h,name*}.
  mapsec 6 = Wood Avens, 9 = Fort Elderflower. "Wood Evans" does not exist.
- `romlib.find_headers()` finds 1361 map headers by validating that each one
  points at a sane layout with two valid Tileset structs.
- **METATILES ARE 24 BYTES (triple-layer: bottom/middle/top, 4 entries each).**
  Proven by table spacing: attr - metatiles = 12288 = 512 x 24 for every
  tileset checked. Reading them as 16 bytes renders a regular checkerboard of
  unrelated pieces -- that was the first, wrong render. Ruination is 2-layer
  (NUM_TILES_PER_METATILE 8), so imports must be flattened deliberately.
- 512 primary / 512 secondary tiles and metatiles, same as Ruination.
- Palettes: slot <6 from the primary, >=6 from the secondary.

## Key maps (header address -> layout)
| map | header | size | primary | secondary |
|---|---|---|---|---|
| Wood Avens (outdoor) | 0x869580 | 50x46 | 0x8730D5C | 0x8730F0C |
| Fort Elderflower (city) | 0x86960C | 60x76 | 0x8730D5C | 0x87311C4 |
| Fort Elderflower (outer) | 0x869C48 | 24x46 | 0x8730D5C | 0x87311C4 |

Measured: Wood Avens 300 metatiles (203 secondary), 133 use all 3 layers,
palette slots 0-4,7-9. Elderflower 325 (282 secondary), 164 use all 3 layers,
slots 0,1,4,6-11. Renders: `assets/monomyth_reference/`.

Tileset animations (water etc.) are not modelled by render.py.
