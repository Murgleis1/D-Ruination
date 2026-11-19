# Pokémon Crown reference (asset source; credit: Blah and the Pokémon Crown team)

Supplied by the user 2026-11-19 as a source of medieval assets, used together with MonoMyth's. Crown is a
**FireRed** hack (BPRE) set in the medieval region of Guelder. The ROM is not in the repo: the tools in
`tools/odyssey/` read any FireRed ROM; point `ODYSSEY_ROM` at Crown.gba.

Measured:
- Map group table: pointer at 0x5524C -> 0x8711468, **43 groups, 370 maps** (255 indoor, 84 underground,
  11 routes, 5 towns/cities). Bound each group at the next group's start (the arrays are contiguous).
- Overworld sprites: main table at 0x839FDB0 (pointer at 0x5F2F4), **152 entries** (FireRed's cast, a few
  medieval repaints: hooded priest/nun 45-46, plumed knight 70, witches 39-42); 30 more sprite records
  outside it (rowboat, campfire, treasure chests, berry plants, some Pokémon). Sprite palettes: expanded
  table at 0x9BCB4FC (113 tags).
- Some interiors render with teal/purple blocks in frrender.py: Crown's tilesets need a closer look
  (tile counts or palettes) before anything is lifted from them.

Renders: `assets/crown_reference/` (four towns, 144 unique interiors in 4 sheets, NPC sheets).
Highlights: walled moated capital with fortress gate, heraldic banners and dragon statues; harbour market
town (striped stalls, watchtower, docks); gothic cathedral on a moat island with timber chalets; thatched
village. Interiors #75 chapel, #84 library, #82/#83 timber houses/inns, #86/#117/#118 great halls with
shields, #104 kitchen, #113-115 stone forge/armoury, #119 banquet hall.
