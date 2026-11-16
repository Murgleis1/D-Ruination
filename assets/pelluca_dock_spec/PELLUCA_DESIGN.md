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

## BUILT — gTileset_Cormoria + gTileset_PellucaValley (2026-11-15)
tools/monomyth/build_cormoria.py -> codebase/data/tilesets/primary/cormoria,
secondary/pelluca_valley. Registered in headers/graphics/metatiles.h; NO map uses
them yet (deterministic run still 0 frames different).
- Palettes: WA terrain 4 + coastal 3 + buildings 5 = 12 of 13. Shared slots 0-5 =
  WA terrain + 2 coastal; slot 6 = 3rd coastal (shore colours are regional: a
  coastal town's secondary provides slot 6); slots 7-11 buildings; 12 spare.
- Tiles: shared 497/512 (terrain + residence + TAVERN art -- every town has a
  tavern), Pelluca 440/512 (Academy, Cadmus, lab, guardhouse, church).
- Metatiles copied layer-for-layer (triple-layer, nothing baked). Behaviours
  carried from MonoMyth (same vanilla numbering). Layer-type attr: NORMAL if the
  top layer is used, else COVERED (gameplay meaning only).
- verify_cormoria.py rebuilt every source region from the new tilesets alone:
  2,078 cells, 100% of pixels within the colour merge (worst 16), no conversion
  errors. Sheet: cormoria_rebuild_check.png.
- Bugs caught by the check and fixed: frequency filter dropped Elderflower's
  stone wall (guardhouse 22 -> 56 cells); church ground taken from an empty layer
  (Wood Avens keeps grass on the MIDDLE layer).
- Known, deliberate: tavern + guardhouse still carry painted snow (snow-removal
  pass next); colour merge darkens guardhouse stone / quay cobble slightly violet;
  no tileset animation callback yet (water is static until one is written).

## North entrance — decided 2026-11-15 (north_gate_options.png)
Route-gate model (as MonoMyth's North Edelweiss north exit): the stone arch
(4x5, already in gTileset_PellucaValley) set into the gap between the northern
cliff terraces leads into a separate WAYSTATION interior map (guard post), which
exits onto the northern route. The size of the wall around it is decided when
the map is built. DEFERRED by the user until the Pelluca map is near completion.

## Tavern snow removal — automatic attempts FAILED (2026-11-15, tavern_desnow_attempts.png)
- Snow colours picked from per-colour masks (white, pale/shade blues, blue cap
  outlines); lamp-post glass protected; outer crop columns are Elderflower's
  town wall (tavern box narrowed to x38-43).
- v1 (peel from edges + fill from below): holes through the roof valleys, streaks.
- v2 (row-wise shingle fill at the measured 4 px repeat, valley seams): central
  gable recovered; still grass holes between gable and side towers and along the
  cornice, stripe artefacts on the right tower.
- ~25% of this roof exists ONLY as snow; no snow-free copy of the lodge exists
  anywhere in MonoMyth (tile-shape search over every secondary: only Elderflower's
  own tileset matches). Making it right means hand-drawing roof geometry.

## Tavern snow removal — user's approach works (2026-11-15, tavern_desnow_options.png)
User: "replace the snow with roof" / "or with leaves". tools/monomyth/desnow.py
desnow_building(): two zones split at the balcony rail (row 88, found from the
longest gold-trim run). Roof zone: snow inside the building's row extent ->
shingles; caps above the roofline removed + outline redrawn; leftover gaps judged
on the COMBINED mid+top layers and refilled. Facade zone: snow -> the material
beside it in its row (or ivy, option 3). Snow ground below the facade -> removed
(grass shows). Lamp-post column protected.
Options: 2 roof fill, 3 roof fill + ivy on ledges, 4 tiled 8px roof patch
(rejected by me: flat pink patches, gable outlines lost).
Known residue in 2/3: vertical shingle bars on the right lower roof.

Decision (user, 2026-11-15): tavern = option 3, roof fill + ivy on ledges.

## Tavern finished + in gTileset_Cormoria (2026-11-15)
Roof colour: DUSK PLUM (user), read by the builder from tavern_roof_ramps.json --
the exact ramp shown in tavern_roof_colours.png panel 4. (A retyped copy was wrong
once; the builder never retypes approved values.) build_cormoria.tavern_finished()
reproduces snow removal + ivy + right-roof repair + plum from source.
Rebuilt: shared 469/512 tiles (snow gone, was 497), Pelluca 446/512, palettes 12/13.
Verify: tavern matches its finished art; every other region still 100% within the
colour merge. Guardhouse exact-match fell 33% -> 2.4% (merge representatives moved
once the snow whites left); visually checked: same art, stone slightly cooler.
Game unchanged: deterministic run 0 frames different.

## Roof colour options (2026-11-15, roof_colour_options.png; ramps in roof_ramps.json)
Roofs selected by SHAPE + COLOUR (tools/monomyth/roof_mask.py): slate greys also
appear in foundations/chimneys/frames, so only roof-colour pixels connected to the
roof's top rows are recoloured. Lab tower exception: its walls and roofs share the
same blue-greys, so its cone, main roof and porch gable are HAND-MARKED regions.
Recolour (roof_recolour.py) keeps each pixel's brightness (the shading) and sets a
new hue; slate is colourised, the church's lavender is re-hued. The lab slate is
much darker than the others: its options are brightened (x1.6) or pink reads maroon.

## Roof colours DECIDED (user, 2026-11-15)
Academy 1B cobalt | Arceus church 2B crimson + patch the dark holes on its roof with
red roof | Cadmus's house 3C rust | Umbra lab: unchanged slate grey | Residence
second colour 5B blue.

## Roofs BUILT into the tilesets (2026-11-15, pelluca_buildings_final.png)
Academy cobalt (1B), church crimson (2B) with its enclosed dark roof patches filled
from the same plank column, Cadmus rust (3C), lab slate (unchanged), residence blue
(5B), tavern dusk plum. Ramps read from roof_ramps.json.
- Recoloured buildings get PER-CELL metatiles: Cadmus and the residence share slate
  roof pieces, so recolouring a shared piece would have repainted both.
- Palette budget: guardhouse DEFERRED out of the tileset (north gate is deferred);
  coastal sand/stone/foliage take an extra tol-24 merge with WATER PROTECTED
  (0 of 38 water tiles changed; coastal_merge_check.png) -> coastal 3 -> 2 palettes.
- Residence: ALL Pelluca residences blue. Keeping slate AND blue in one town was
  built as a palette swap (wall-siding greys given duplicate palette entries so the
  swap only touches roof slots) but needs 14 palettes vs 13 -- kept behind
  RESIDENCE_PALETTE_SWAP=False for a town that can afford it.
- Result: 13/13 palettes, tiles 500 + 489. Verify: every region within its merge
  tolerance (coastal 40 = 16+24 by design). Game unchanged (0 frames differ).

## Tavern = Pokemon Center + Mart (user, 2026-11-15)
The tavern is the heal point AND the shop, and the centre of most empire-era
communities. EVERY major city uses the same tavern with a roof colour matching that
city's vibe. Its art is in the shared primary; its roof colour comes from the town's
secondary palette. TODO when the second city is built: give the tavern a dedicated
palette slot (today it shares a building palette in Pelluca), so another city
redefines one slot to recolour it.

## Layout method — draft 1 (traced) REJECTED as a method, kept as reference (2026-11-15)
tools/monomyth/layout_kit.py classifies every new metatile by how MonoMyth USES it
(collision + behaviour from the source cells; pixel colour alone called bright
conifers "grass"). tools/monomyth/autotile.py learns 3x3 class neighbourhoods ->
metatile from the hand-made source maps and lays a class plan out.
Draft 1 = the reference image traced to classes (layout_plan_traced.png) and
autotiled (layout_draft1_traced.png): structure right (forest belts, roads, plaza),
but only 31% of cells matched a full 3x3 source pattern; the lake speckled (the
water class also held quay stone-over-water pieces); cliffs broke (the reference
draws cliffs as 1-cell brown lines; Wood Avens cliffs are multi-cell tiers).
NEXT METHOD: plan in ELEVATION (lake / shore / town / terraces), roads as paths,
forests as regions, buildings as footprints; cliffs generated where elevation
steps, using face/corner rules learned from Wood Avens' own elevation bits; open
water separated from quay pieces.

## Layout drafts 2-3 — piece-rule generator (2026-11-15, layout_draft3_vs_reference.png)
tools/monomyth/pelluca_layout.py lays the map out from a written plan (forest belts,
cliff bands + stairs + one stepped corner, cobble roads, quay + pier, lake, buildings,
lamps, trees, hedges, lawns, flowers). Every piece rule was checked on screen first
(cliff_tests / decor_tests). Collision/elevation per piece come from how MonoMyth's own
maps set them (tools/monomyth/data/source_collision.json); quay wall + pier are walkable
at elevation 3 (dock lock). Arrival path (pier x44 y45-52, row y45 x44-47) is clear;
lab door (47,44); lab footprint x44-48 y40-44 (the DM lock had x45-49 -- not on the path).
Honest gap vs the reference: straight cobble roads, straight cliffs, stone-walled
square lake, sparse dressing. Next art pass: winding lawn paths (Wood Avens 99-109),
organic terraces (mirrored cliff metatiles, no new tiles), natural lake banks/beach
(needs shore art -- tile budget 23 secondary / 12 primary free, palettes 13/13),
fenced gardens, farm plot.
Church door has no door behaviour yet (Evernahn import) -> set MB_NON_ANIMATED_DOOR in
the builder. Tavern cells carry 0x5B (MB_UNUSED_5B, harmless); door 0x60.

## User feedback on draft 3 (2026-11-15)
- Building PLACEMENT approved ("all in the right places").
- Too empty, esp. approaching the centre -> a central MONUMENT. Lore (19_location_atlas,
  Pelluca hydrology, LOCKED): the wellspring beneath the city is its water source and the
  central plaza fountain draws from it -- the reason the fountain is the town's centre.
- Residences 6, 7, 8, 8b -> SMALLER houses (Evernahn, or Fort Elderflower small houses
  with ivy + roof-tile fixes instead of snow).
Candidates: houses_and_monument_options.png. FE gabled cottage (D, 5x4) and steep-roof
house (E, 5x6) de-snowed with the tavern pipeline (tools/monomyth/fe_houses_desnow.py):
bottom-layer art merged for interior + bottom-rim cells; castle wall cut from E's top
row; E's centre stripe filled with real shingles copied 16px sideways. ~62-68 tiles each.
Room: ~35 tiles free, but 220 tiles belong only to metatiles the layout does not use
(Port Ginseng warehouse fronts 137-154, the spare WA hall 56-96 inside the terrain
crop, snow rocks...); pruning them in the builder fits both houses + a monument.
Monument candidates: A Chamomile garden fountain, B Watercress statue fountain (the
only one with a statue), C Pisces octagon fountain. No human/king statue found yet
(MonoMyth Peak of Kings tileset = thrones/altars; DM tilesets checked: none).

## DECIDED (user, 2026-11-15 late)
- Residences 6, 7, 8, 8b = FE **gabled cottage** (D, 5x4). Lore: Pelluca Valley is rural but
  GROWING -- more people come to study to become trainers under Cadmus's programs.
- Monument = the **Watercress statue fountain**, modified so it differs from MonoMyth's, set in
  the centre of **Chamomile's paved garden ring enlarged to fill the plaza** (the wellspring fountain).
- Building 3 is NOT Osrid's cover house: it is the **student dormitory**. Osrid has his own room
  there so he can watch over and mingle with the students -- he is in charge of security and
  Cadmus wants him available to students who need help. Keeps the 7-wide Wood Avens timber
  building (a dorm needs the size). House 5 stays a WA residence (not asked to change).

## Draft 4 (2026-11-15 late, layout_draft4.png)
User feedback on draft 3 fixed: (1) the TAVERN's left wing was cut off -- the FE lodge is x37-43,
the box started at x38; now the full 7-wide lodge (door (6,3) of its grid). (2) road + stairs
misaligned -- roads are 3 wide, WA stairs 2: stairs under a road are now 3 wide (45 46 46),
verified on screen (stairs_tests option A).
Built: gabled COTTAGES for houses 6, 7, 8, 8b (plum roof = the tavern's dusk plum, shares its
palettes); the WELLSPRING MONUMENT fills the plaza (16x9; roads run into its N edge, the
east arm and -- via a jog beside the church -- the west arm; only the basin blocks).
Monument recoloured from its own materials (sandstone statue in the ring's brick shades,
basin in the ring's rim stone) and reduced to exactly 15 colours = one palette.
Tileset mechanics (tools/monomyth/build_cormoria.py):
- PRUNE: art of unused metatiles blanked, ids kept (data/pelluca_prune.json for the shared
  tileset; Pelluca's own unused pieces are found by key). Frees tiles: 497/512 + 462/512.
- ANCHOR: the approved build's colour merges are frozen (data/merge_anchor*.json). Re-clustering
  on new inputs moved approved colours (quay stone drifted 16-24 toward lavender) -- now every
  approved metatile/building is pixel-identical (checked: 73 terrain pieces, academy, Cadmus,
  lab, residence, church: 0 px changed; tavern differs only where its cut edge was).
- Terrain + coast palettes packed jointly (5 instead of 4+2); the freed shared slot holds
  the monument's palette. Cottage fitted into existing palettes (226 px nudged).
- Church door: MB_NON_ANIMATED_DOOR on its bottom-centre cell.
- Pelluca metatile ids shift when a building grows: run tools/monomyth/source_collision.py
  after every rebuild (layout collision table is keyed by id).
Game: builds; deterministic run frame-identical (no map uses these tilesets yet).

## Draft 5 (2026-11-16, layout_draft5.png) -- user feedback on draft 4
1. Cottages 6/7 now open straight onto the east road; yards vary (flowers / fenced lawn /
   chopping stumps / hedge) instead of a hedge at every house. Trees: GROVES (forest rules,
   two trees deep or one row) back the dorm, cottages, monastery, lab and the cliffs; singles,
   slim conifers (44/47/20) and bushes (97) are accents.
2. Lawn path (WA 99-104) from the Academy door to the north road.
3. Lab "cut off": in Wood Avens the chapel is built into a cliff -- its bottom layer held cliff
   rock beside the tower, the crop caught leaves + a branch. Builder now gives it grass ground,
   strips top-row greens (incl. teal), and keeps only cone pixels with a mirror twin
   (the tower is symmetric). A grove stands behind its flat roof.
4. Tavern moved left (x25-31, door (28,43)); garden + grove between it and the road; SW BEACH
   strip (sand 163 / surf 171 / wet sand 173, all walkable) with a bush fringe.
5. Pier HEAD: composed pier kit (N edge, corners, inside corners, lamp-on-stone) from the
   pier's own pixels; stem x43-45 y47-48, head x40-48 y49-52, lamps; south lip 155 over
   shadowed water 159 -- a ship can come alongside. (Deviates from the DM dock lock by user
   request; the arrival path x44 y45-52 stays walkable.)
Pruned more shared art for room (WA sand/dirt banks 164-170) -- tiles 509/512 + 460/512.
Open: east bay is still a plain rectangle; secret cavern (x63-65 y40-42) must be water-only;
the S.S. Tidal sits at (44,55) -- check its sprite against the new pier head in-game.

## Composition study (2026-11-16) -- user: "a sense of beauty, balance and cohesion"
Studied MonoMyth Wood Avens, Wormwood Borough, Chamomile Town, Mandrake City (beach town)
and Pisces #3/#5/#20. What they share:
1. ROAD HIERARCHY: one main spine between the exits through a landmark centre; smaller lanes
   branch to each building cluster; every major door connects to a road. Nothing floats.
2. Buildings face their road, in rows/clusters with consistent setbacks; clusters share a lane.
3. TREES ARE STRUCTURE: forest masses hug the town with ragged inner edges; tree PAIRS frame
   buildings; tree ROWS give rhythm along roads and terrace tops; clumps fill leftover corners.
   Open lawn is rare and deliberate.
4. Terraces split districts; stairs line up with a road or lane.
5. Balance: landmark on the main axis, density thinning toward the edges.
6. BEACHES sit BELOW the town at the foot of a cliff, reached by stairs (Mandrake): sand runs
   cliff-foot to a ragged waterline; props (pier, boats). Sand never meets lawn on a hard line.
Plan (composition_plan.png): main spine N exit -> monument -> quay -> pier; W/E main road
through the monument's arms. Lanes: Academy (built); dorm -> west stairs -> Cadmus -> W road;
house 5 -> east-terrace stairs -> E road -> cottages 8/8b. Tree rows along both terrace tops,
pairs flanking each building, ragged forest edges, clumps in corners; scattered singles,
bushes and random flowers removed. SW beach under the west cliff with stairs down and a
ragged waterline (diagonal surf pieces 172/174/176); cliff-foot-on-sand pieces composed
like the pier kit. Rocky east shore + cavern reachable only by water.

## Draft 7 (2026-11-16, layout_draft7.png) -- the approved composition, built
- Road hierarchy as approved: main spine N exit -> monument -> beach -> pier; W/E main road
  via the monument's arms. LANES (2-wide cobble): Academy; dorm -> round the pool -> west
  stairs -> spur to Cadmus's door -> W road; house 5 -> east-terrace stairs -> E road ->
  cottages 8/8b; on the beach (user): lanes to the tavern door and to the lab door, the east
  one running straight onto the pier.
- BEACH (user): ALL land below the lower cliff, around the dock and the lab. shore.py: per
  column surf row + water row, steps of one row, Old Bay Island pieces + hflipped twins
  (builder 'shore_flip'); 175 soft water edge. Sand twins ('onsand') of the cliff foot,
  stairs, road, lamps, and of the tavern + lab (bottom layer swapped -> no new tiles).
  Palms (palm.py: Mandrake palm in Wood Avens' tree colours) replace the shore's woods.
- Trees: rows along the top of the lower cliff, slim conifer pairs framing houses, groves
  behind; scattered singles/bushes/random flowers removed.
- connectivity.py: from the arrival point every door front and every exit is reachable,
  no cut-off pockets. ROM builds; deterministic run frame-identical; approved art unchanged.
OPEN: secret cavern must be water-only -- the east beach strip is reachable on foot; needs a
rock outcrop (Old Bay Island 'K') imported.

## Draft 8 (2026-11-16) -- harbour fixed (user: dock stone clashed with the road; gap by the tavern)
- The dock is ONE stone surface: a harbour apron (x40-48 y45-46) in the pier's stone at the lab
  door, the stem and head out from it. The harbour road (small cobble) ends against the apron's
  west rim (2 rows of contact) instead of running onto it. Pier rims now face sand/road/water
  alike; the wall lip only where water is below.
- The "gap" was a surf step pair half-hidden under the road. Rule: a step pair is never split by
  a covering surface -- one beach depth from the tavern to the lab, steps only in open sand.
- Road top edge piece 64 keeps grass in its art layer: its sand twin swaps those pixels.
Checks: connectivity all doors/exits; ROM builds; frame-identical; verifier clean.

## Draft 9 (2026-11-16) -- a full harbour (user: foam against the stone looked unnatural; the
## beach should be "below" the stone near the lab)
- HARBOUR: everything east of the harbour road below the lower cliff is one stone quay (pier
  kit surface) -- x37-50 down to y46, x51-71 down to y41; the lab stands on it (lab_tower_stone:
  ground swapped to quay stone), the stairs + cliff foot land on it ('onstone' twins), the pier
  runs out from its wall, a short jetty in the bay moors the rowboats; lamps on stone.
- The BEACH is west of the road (tavern, palms). Junction rule: the quay's wall row = the
  beach's surf row (y46), so the waterline runs straight on into the quay wall, and the wet band
  tapers off with a water step one column before the stone -- foam never touches stone.
- Concave quay corners use the Port Ginseng corner pieces 156/158.
Checks: connectivity all doors/exits; ROM builds; frame-identical; verifier clean.

## Draft 10 (2026-11-16) -- beach/harbour edge + bustling docks
- Edge (user: the line between beach and dock looked strange): the pier-kit rim is a WATER edge;
  against sand it read as a seam. Rims now only where stone meets water; the paving simply stops
  at the sand, with two palms along the edge so it is not one long straight cut (edge_options:
  B + D chosen over the rim and over a road strip).
- Ships are object events; previews draw them (pelluca_layout.SHIPS): S.S. Tidal alongside the
  pier head, a second ship at the bay jetty, two rowboats (see PELLUCA_EVENTS.md).

## Notes (user 2026-11-16 morning)
- Beach/harbour edge: still not fully satisfying; idea for later -- a fence with a gap, or
  something more natural. Parked, not dropped.
- Cavern entrance: locked lore (19_location_atlas, hydrology) puts it on the EAST shore of the
  southern lake (~x63-65 y40-42), across the water, not reachable on foot. The harbour now
  occupies that shore (public, busy) -- conflicts with "Umbra-sealed, unknown to the public".
  Placement question put to the user.

## Draft 12 (2026-11-16) -- purposeful trees; dorm off the river (user)
Every tree now has a job: north-road AVENUE (lamps at the entrance, slim conifer pairs down both
sides); tree ROWS along the foot of the east terrace and the top of the lower cliff; matching
FRAME pairs at the Academy, dorm, monastery, house 5 and the cottages; a conifer at each corner
of the fountain plaza; woods only as forest edges (a column behind the dorm, the north forest
stepping down beside house 5). Removed: free-floating groves, the lone round tree, stray conifers.
Dorm moved 2 west onto the forest edge (x8-14, door (11,8)); conifer between it and the river.

## Draft 14 (2026-11-16) -- grounds for the Academy and the monastery (user: too much empty lawn)
- Academy grounds: two-deep woods either side of the north entrance (x32-35 and x42-45,
  mirrored about the road), flower hedges at their foot, flower beds by the Academy's front.
- Monastery grounds: its orchard wood on the fountain side (x26-29 y17-21), a hedge row
  where the garden meets the road.
- Dorm corner: the north forest steps down between the dorm and the river (gap removed);
  the dorm's top roof rows are now unreachable walk-behind cells (expected).

## Draft 15 (2026-11-16) -- things, not just trees (user: academy grounds + dorm need more)
- Prop kit in the tileset: picket fence (98, ends/corners 116 120 128 121, sides 123 111),
  berry hedge 42/43, hydrangea 21/117, mushrooms 36, rope posts 114/115, low stone walls 48/49/105-107.
- ACADEMY: fenced practice yard on its east side (x31-35 y6-11, Wood Avens fence construction,
  gate onto the lane), training posts inside, hydrangeas; the forest steps down behind it.
- DORM: berry hedges and hydrangeas either side of the door, the students' clothesline,
  mushrooms toward the forest.

## Draft 16 (2026-11-16) -- town props (user: "I'd like all that stuff")
- New art (tools/monomyth/props.py): Chamomile park bench (2x1), Farmstead signpost, Mandrake
  covered well (1x2, lid row walk-behind), Mandrake barrel, Mandrake crate (its greens -> its own
  dark wood: a crate of goods). Each sits on Pelluca's own ground by swapping the bottom layer:
  bench/sign/well on grass (6), barrel/crate on harbour stone (157). 22 secondary tiles, 9 metatiles.
- Palettes: props fit LAST, into the finished palettes (least colour error, free entries first),
  so every approved piece -- cottage included -- stays pixel-identical (measured: 0 px outside
  the 20 changed cells). Sign lettering and bevel take the sign's own outline/body colours.
- Placed: bench in the Academy practice yard (north fence, facing the posts), two benches either
  side of the north road facing the fountain; the well in the dorm garden by the clothesline;
  signposts at the three entrances (Route 11 W, Hoya Delta E, north road); barrels and crates by
  the lab, at the bay jetty and at the second ship's berth.
- Budget after: primary tiles 506/512, secondary 504/512, palettes 6+7 (full).
