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
| 3 | Osrid's cover house | 11 Evernahn house (building columns c0-c4 only) |
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
