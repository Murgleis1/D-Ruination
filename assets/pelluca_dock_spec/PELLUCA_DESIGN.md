# Pelluca Valley — layout design decisions

Design basis: `pelluca_layout_reference.png` (badged: `pelluca_layout_reference_badged.png`).
Style: **Wood Avens (MonoMyth) meets Evernahn**, roofs recoloured to the reference.
The reference's dock area is NOT authoritative — `dock_geometry.json` is.

## Building roles — decided by the user, 2026-11-15

| badge | role | notes |
|---|---|---|
| 1 | **Academy** (Cadmus is resident headmaster) | Shift it LEFT, toward the river, so the north road is clearer |
| 2 | **Arceus church** | Rework the reference's tavern-looking building into the church |
| 3 | **Osrid's cover house** ("Nomad Alban") | Sits by the river dive spot |
| 4 | **Cadmus's house** | |
| 9 | **Seaside Tavern** (empire-era Pokémon Center) | Burglar-Egg old man blocks it |
| 10 | **Umbra lab** | Its door must be the LOCKED lab warp (47,44); approach (47,45) |
| 5,6,7,8 | Residences | Assigned as Chapter 1 work needs them |
| 11 | Boathouse / fishery | Fisherman's Dilemma — unconfirmed |

## Art source per role — agreed 2026-11-15 (candidate numbers from building_candidates.png)

| map badge | role | candidate |
|---|---|---|
| 1 | Academy | 3 Wood Avens gambrel hall — roof recoloured to the reference blue (user, 2026-11-15) |
| 2 | Arceus church | 9 Evernahn monastery — roof recoloured |
| 3 | Osrid's cover house | **shared Wood Avens timber house, unique roof colour** (user 2026-11-15; was Evernahn house, -78 tiles). Lore: hiding in plain sight |
| 4 | Cadmus's house | 2 Wood Avens turret-bay house |
| 9 | Seaside Tavern | **Elderflower building G** = candidate 7, the large lodge (confirmed by the user; see monomyth_reference/elderflower_badged.png) — snow removed AND recoloured so it does not read as MonoMyth's tavern |
| 10 | Umbra lab | 4 Wood Avens stone chapel tower — door on locked warp (47,44) |
| 18 | North guardhouse | 8 Elderflower keep gate — snow repainted out |
| 5-8 | Residences | 1, 5, 6 with roofs recoloured to the reference |

## Terrain / route features — decided by the user

- **North exit (badge 18):** a clear road north out of town that passes THROUGH a
  **covered guardhouse / waystation**. (Previously the bible put the north
  gatehouse against the back of the Templar Monastery; the gatehouse is now its
  own structure on the north road.)
- **River dive spot (near badges 21 / 3):** the river near Osrid's house must be an
  accessible point where it flows into Pelluca's secret underground area — a
  Dive spot. Consistent with the locked hydrology: this is where the river goes
  underground.

## Still open

- Secret cavern entrance (yellow, x63-65 y40-42): the reference makes it
  reachable on foot from the stairs by house 8; the lock says water must separate it.
- Whether the Arceus church (2) IS the Templar Monastery of earlier canon
  (the PellucaTemplarMonastery interior + holding cell already exist).
- Dive spot gating (Dive HM / story flag) and whether it is usable in Chapter 1.

## Locked constraints carried forward

- Dock x38-52 y42-58 collision/elevation verbatim; pier column x43-45, y52->y42
  walkable at elevation 3 (arrival cutscene).
- Lab warp (47,44) -> MAP_PELLUCA_UMBRA_LAB.
- Four exits: N Ivy River, W Route 11, E Hoya Delta, S Surf-gated water (Route 10).
- Every one of the current 62 objects / 48 triggers / 9 warps / 6 signs gets an
  explicit fate (move / keep / cut) approved before map data is edited.

## Tile budget — measured 2026-11-15 (tools/monomyth/budget_pelluca.py)

Unique 8x8 tiles after flattening MonoMyth's 3 layers to 2 (bottom+middle merged,
top kept), flips deduped, ground fill (images placed >=40x map-wide) excluded:

| building | tiles |
|---|---|
| Academy — WA hall | 142 |
| Cadmus — WA turret house | 74 |
| Lab — WA stone tower | 78 |
| Residence — WA timber house | 51 |
| Tavern — FE lodge G | 170 |
| Guardhouse — FE keep gate | 38 |
| Residence — FE red house | 100 |
| Residence — FE steep house | 105 |
| **all eight** | **718** (95 colours) |

A secondary tileset holds 512 tiles; the Evernahn church + Osrid house + props
are not yet counted. **Does not fit in one secondary.** Decision pending.

## Tileset architecture — decided by the user 2026-11-15 (applies to EVERY town)

The Cormorian Empire is one unified culture with regional variation, so:

- **Shared primary tileset** (one, used by every city/town): terrain + the building
  types every town repeats (Tavern, Arceus church, the residence model) + common
  props.
- **Per-town secondary tileset**: that town's unique buildings (Pelluca: Academy,
  Umbra lab, Cadmus's house, north guardhouse, Osrid's house) + its regional
  palettes.
- **Regional roof colours cost zero tiles.** A metatile entry picks the palette
  slot, independent of which tileset owns the tile (engine: slots 0-5 load from
  the primary, 6-12 from the secondary; fieldmap.c LoadTilesetPalette). So the
  shared house TILES live in the primary, while each town's SECONDARY holds the
  metatiles placing them with that town's roof palette (slot >= 6). Same tiles,
  different roofs per town. Cross-origin palette entries are standard: 52 of 81
  vanilla secondaries use them.
- Residences: one shared model (Wood Avens timber house) in several roof colours;
  the two Elderflower houses are dropped as residences (-205 tiles).
- Regional variation beyond colour: "a few new building types here and there" go
  in each town's secondary.

## Full budget — measured 2026-11-15 (tools/monomyth/budget_shared.py)

| item | tiles | tileset |
|---|---|---|
| terrain: gTileset_Evernahn today / all Wood Avens terrain+props | 320 / 408 | shared |
| Arceus church — Evernahn monastery r17-26 c0-c6 | 202 (43 colours) | shared |
| Tavern — FE lodge G | 170 | shared |
| Residence — WA timber house | 51 | shared |
| Academy 142, Osrid house 78, Lab 78, Cadmus 74, Guardhouse 38 | 410 | Pelluca |

Demand ~1,150 vs capacity 1,024 (props not yet counted). Pelluca secondary fits
(410/512); the SHARED primary does not (743+ / 512). Levers under discussion:
curated terrain, Osrid house as a residence variant, which shared building
moves to the town secondary, and post-desnow re-measure of the tavern.

## Terrain style — decided 2026-11-15

- **Base: Wood Avens (MonoMyth)** for Pelluca: cliffs + stairs, cobble road
  (user: WA road beats Evernahn's), fences/flower hedges, forest. Reasons: matches
  the reference's tiered layout, matches the MonoMyth buildings' native-16px style
  (Evernahn is 32px art halved, which reads softer/busier), and Pelluca is a
  forested seaside valley, not a marsh.
- **Evernahn = accents** where they blend: the Arceus church, Osrid's house, and
  any other piece judged to meld (user: "feel free").
- **Evernahn's marsh look is reserved for the Shadowmarshes / Hoya Delta** (east
  arm) -- regional variation.
- **Water/shore:** Wood Avens has none; source from a MonoMyth coastal map so the
  lake matches, not Evernahn's clay banks.
- **Colour:** the locked mauve/dusk palette stands; Wood Avens' mint is graded
  toward dusk rather than shipped as-is.

## Water / dock / shore sources — approved 2026-11-15 (water_candidates*.png)

| piece | use in Pelluca |
|---|---|
| G, H Port Ginseng stone quays | main dock (art only; dock geometry stays locked) |
| F Cascade Boardwalk wooden pier | SW fishermen's jetty |
| I Port Ginseng surf-foam beach | SW beach meeting the lake |
| A Watercress cliff into water + rocks | lake edges below the terraces |
| C Watercress fountain | central wellspring fountain |
| J Old Bay Island river sandbank | river by Osrid's house / dive spot |
| K Old Bay Island rock outcrop w/ steps | secret cavern entrance, far shore |
B (grey stone pier) rejected as modern. Port Ginseng/Old Bay grass is olive:
take stone/water/rock only, redraw grass edges in Wood Avens grass.

## Budget re-measured with real flattening — 2026-11-15 (tools/monomyth/budget_terrain.py)

Flattening now merges layers ONLY for metatiles using all 3 MonoMyth layers
(<=2 layers map onto Ruination's two unchanged). Saves little (terrain 611->570):
most of these metatiles genuinely use 3 layers.

Exact approved crop windows (generous boxes swept in warehouses -> 1173, wrong):
| piece | tiles (new after earlier rows) |
|---|---|
| Wood Avens terrain, no snow tier/buildings | 280 |
| A cliff-into-water | 60 | C fountain | 44 | G quay | 42 | I surf beach | 45 |
| F boardwalk | 28 | J river sandbank | 13 | K rock outcrop | 58 |
| **terrain total** | **570** |
| + Academy 127, Cadmus 61, Lab 64, Residence 46, Tavern 175, Guardhouse 43 | 1086 |
| + Evernahn church ~202, Osrid house ~78 | **~1366 vs 1024 for one map** |

## Engine fact for any map split (verified src/fieldmap.c FillConnection)
A connected map's raw metatile ids are copied into the current map's buffer and
drawn with the CURRENT map's tilesets. A seam between maps with different
secondaries must therefore use only shared-primary metatiles (or identical ids)
for the strip visible across the edge, or the far side draws as garbage.

## Option 2 chosen — ONE map (user, 2026-11-15)
"Dump the fountain and anything too elaborate that isn't the buildings themselves."
A split felt wrong for a valley that doesn't have a ton of stuff.

Cuts, measured (budget_terrain.py + coverage analysis of Wood Avens terrain):
- Dropped: C fountain, K rock outcrop (cavern entrance -> Wood Avens cliff + cave
  mouth), F boardwalk (jetty reuses quay art), I surf beach (beach from J sandbank).
- Wood Avens terrain has a long tail: 67 of 128 terrain metatiles placed <=2x
  cost 202 of 280 tiles (95% of cells need only 149). Dropped from it: grey
  mountain/snow tier, grass texture variants (map to base grass), INN signboard,
  carved stone face, the well.
- Dropping A (Watercress cliff-into-water) and flower-hedge variants too
  (lake edges = Wood Avens cliff base + J shoreline).
- Palette-unifying all sources saves only 11 tiles (351 -> 340 by shape).
- Church crop r17-26 c0-c6 includes 6 junk cells (r17c0-1 bushes, r17c5-6 stair
  fragment, r18c0 water swatch, r18c6 vine): real church ~178, not 202.
Result: ~1,054 vs 1,024 before signs/door frames -> one more ~80-tile lever needed.

## Budget CLOSED — 2026-11-15
Osrid's house -> shared residence model (user approved). One map:
~976 of 1,024 tiles, ~48 headroom for signs / door frames / small props.
Next gate before building: PALETTE packing (13 slots x 15 colours) across all
sources after the dusk regrade -- measured, not assumed.

## Palette gate — measured 2026-11-15 (tools/monomyth/palette_pack.py)
Approved set (budget-closed): 160 distinct colours -> 23 palettes needed vs 13.
No tile exceeds 15 colours; it is a packing problem.

| merge tolerance (max RGB step per channel) | colours | palettes (best of 400 packings) |
|---|---|---|
| 0 | 160 | 23 |
| 8 | 111 | 17 |
| 16 | 71 | **13** |
| 24 | 43 | 8 |

Visual check on a real Wood Avens screen (palette_tolerance_compare.png):
tolerance 24 FLATTENS the grass into fill and kills roof highlights -- rejected.
Tolerance 16 keeps texture (stddev 43.5 vs 44.6, edge 17.5 vs 17.8). It fits 13
palettes exactly, leaving NO slot for regional roof-colour variants. Heaviest
colour users: Lab tower 47 colours, Cadmus house 37, Academy 33.
Next: hand-designed dusk master palettes with a fixed roof-ramp index convention
so roof colours can ride in existing palettes, and targeted colour reduction on
the heaviest buildings.

## Palette decision — 2026-11-15 (palette_merge_compare.png)
- Roof-ramp convention MEASURED and rejected: the residence's slate ramp is in 53
  of its 60 tiles (wall trim included), so a roof palette must pin 12 of 15
  slots; every roof colour costs ~1 whole palette (14 -> 19 for six colours).
- "Safe" merge (never merge colours that share a tile) reaches 13 palettes only
  at tolerance 40 (12 at 48) and LOOKS WRONG: cobble turns purple/yellow speckle,
  roofs streak yellow, red flowers go brown, beige patches in grass. Its stddev
  and edge metrics went UP (45.2/45.7 vs 44.6) -- the metrics rewarded the
  damage. Judge by eye on real screens, not by these numbers alone.
- **Chosen: plain merge at tolerance 16 -> 71 colours, 13 palettes.**
- **Roof colours:** regional (per-TOWN) variation is free -- the residence's
  palette goes in a secondary slot (6-12), so every town's secondary defines its
  own residence colours. Within Pelluca, variety comes from the unique buildings
  (Academy, church, tavern, lab, Cadmus, guardhouse each get a designed roof);
  residences share one roof colour unless a palette is freed by trimming the
  heaviest colour user (Lab tower, 47 colours).

## WHY MonoMyth fits and we don't — measured 2026-11-15
Same hardware, same base (Emerald): 512+512 tiles, 13 BG palettes per map.
- Wood Avens ALONE natively uses 8 palette slots (0-4, 7-9). Flattened to our
  2-layer format the SAME map needs 16 palettes (palette_pack.py), and 639 tiles.
  Fort Elderflower alone: 10 palettes, 641 tiles after flattening.
- Cause: MonoMyth runs TRIPLE-LAYER metatiles (24 bytes; bottom/middle/top each
  drawn on its own BG). Ground and the object over it are separate tiles, each
  with its OWN palette. Our engine (NUM_TILES_PER_METATILE 8, field_camera.c
  DrawMetatile) draws two layers, so a 3-layer metatile must bake two layers into
  one tile -> that tile needs BOTH layers' colours in ONE palette, and every
  object-over-ground combination becomes a new tile.
- Second factor: MonoMyth builds each town from one art family designed together;
  Pelluca mixes six source maps across four tilesets.
- The field engine already owns all three map BGs (BG1/BG2/BG3); a SPLIT
  metatile writes BG3 + BG1 and blanks BG2. Triple-layer support is a metatile
  FORMAT + DrawMetatile change, not a VRAM change.

## Re-measured under TRIPLE-LAYER (engine d18a04803) — 2026-11-15
Same approved set; every MonoMyth layer now imports as-is (FLATTEN=triple, the
budget tool's new default).
| | 2-layer (merged) | triple-layer |
|---|---|---|
| tiles | 985 | **942 / 1024** |
| palettes, no colour merge | 21 | 16 |
| palettes, merge tol 8 | 18 | 14 |
| palettes, merge tol 16 | 13 (0 spare) | **11 (2 spare -> roof colours)** |
Remaining pressure is from mixing six source maps, not from layering.
Plan: tol-16 merge (the look approved on screen), 2 spare palettes for
residence roof variants, ~80 tiles headroom for signs/doors.
