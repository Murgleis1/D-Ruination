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

## Water / shore sources on Wood Avens' primary (0x8730D5C) — 50 outdoor maps share it
| map | header | water | useful for |
|---|---|---|---|
| Watercress Port (mapsec 3) | 0x869C10 | 32% | cliff-into-water edge, rocks, stone pier, plaza fountain (buildings are modern: no) |
| Route 24 (mapsec 39) | 0x8698AC | 35% | sand beach, sand-to-water shore |
| Cascade Boardwalk (mapsec 52) | 0x869B84 | 22% | wooden boardwalk pier (tent/shops modern: no) |
| Camp Tarragon (mapsec 4) | 0x8695F0 | 27% | snow shore only -- not useful |
Ranked by cells whose behaviour byte (attr u16 low byte) is 0x10-0x17.

## Ports surveyed at the user's suggestion (2026-11-15)
| map | header | finding |
|---|---|---|
| New Old Bay City 96x78 (mapsec 54) | 0x86D870 | modern metropolis, no dock; red-brick terraces noted for a later city |
| New Old Bay City 26x22 | 0x86B880 | renders scrambled -- header does not decode like real outdoor maps |
| Port Ginseng 48x48 (mapsec 95) | 0x86D88C | open sea + surf-foam beach shoreline |
| Port Ginseng 64x64 | 0x86DB2C | stone quays, canals, bridges, moored piers; warehouses/market stalls; parking lot (modern) |
| Old Bay Island, 22 maps (mapsec 91) | 0x86D8C4.. | wilderness: rivers w/ sandbanks + waterfalls (0x86DA14, 0x86DA30), no docks; 0x86DD24 scrambled |
These use primaries 0x873132C / 0x87311DC, NOT Wood Avens' 0x8730D5C: style match judged by eye.
