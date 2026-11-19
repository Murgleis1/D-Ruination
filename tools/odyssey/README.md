# Pokemon Odyssey (v4.1) reference tools

Odyssey is a **FireRed** hack (BPRE): 2-layer metatiles (16 bytes), 640 primary tiles/metatiles,
palettes 0-6 primary / 7-12 secondary, 4-byte metatile attributes. Not in the repo: point
`ODYSSEY_ROM` at the ROM (default /home/claude/odyssey/odyssey.gba).

- `frlib.py` - layout/tileset readers (FireRed struct order: tiles, palettes, metatiles, callback, attributes).
- `frrender.py` - renders FireRed maps/metatiles (`TS`, `render`, `map_cells`).
- `dorm_odyssey_mock.py` - proposal: Odyssey's brick hearth, food plates and barrels in the Pelluca dormitory.

Survey (2026-11-19): 774 map headers (group table at 0x83526A8), 350 unique indoor layouts. Mostly modern
FRLG-style; the medieval-useful sets are the **rustic barn** (layout 0x871F950 / 0x8319030, secondary
0x82D5034: plank walls, barrels, hay, rough tables, stools, counter) and the **brick fireplace hall**
(layout 0x8319414, secondary 0x82D4EE4: timbered brick, hearth + chimney, stone floor, stove, cabinets,
rugs, food plates). Sheets in assets/odyssey_reference/. Objects in both sit on the top layer (floor
below), one palette per family, so they lift cleanly onto our floors/tables.
