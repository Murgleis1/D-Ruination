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
