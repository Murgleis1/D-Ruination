# Fantasma reference (study only)

Source: `Fantasma_Part_I_rc_Water.gba` (user upload 2026-11-21; header `FANTASMA` / `BFTE`). This is a
pokeemerald-expansion hack. Everything here is extracted from it for study. Before shipping any of it,
~~get the Fantasma team's OK and credit them~~ -- not needed: Fantasma's art is public assets (user 2026-11-22): no permission or credit needed.

Extraction tools: `tools/fantasma/` (see its README).

## Battle backgrounds (`battle_bgs/`, sheets `battle_bgs_sheet_1..3.png`)

There are 76 full-scene painted backgrounds, taken from the game's `gBattleEnvironmentInfo` (82 slots; six
are empty). Each one is 240×120 of art over a flat 40-pixel strip, which the text box covers. They are drawn
as a full scene, not on vanilla's oval platforms. The whole set shares one look: dark teal/violet, low fog
and warm candle accents.

- Tiles: about 496 (15.5 KB), which fits the vanilla 512-tile battle-BG slot.
- Palettes: three (palettes 2-4, 0x60 bytes raw), the same as vanilla.
- This matches Dreamstone's current `graphics/battle_terrain/*` layout (one scene, three palettes). For
  comparison, see `dreamstone_current_battle_bgs.png`.

The ones that fit the Chapter 1 Necropolis and Mirroh best are in `necropolis_picks_2x.png`:

| Fantasma name | Scene | Fit |
|---|---|---|
| Leader (12) | Ossuary chapel, skull niches, glowing gothic window | Kimaris chamber |
| Sanctum (39) | Domed rotunda lined with skull niches | Necropolis floor 2 (Gram) |
| Pyre Hall (45) | Catacomb tunnel, candles, skulls, violet doorway | Necropolis floor 1 (Dale) |
| Ghost Tower (46) | Graves in fog, violet will-o'-wisps | Necropolis grounds |
| Still Ice (30) | Frozen wave in an ice cavern | Trial lake |
| Depths (36) | Giant ribcage tunnel | Alternative for the Trial lake or deep catacombs |
| Burial Ground (25) | Moonlit pagoda graveyard | Graveyard terrain (needs re-theming; pagoda) |
| Snow (29) | Snowstorm, lit ruins on a crag | Mt. Mirroh exterior / Ancient Mirroh |

Other spooky ones are Ruined Mansion (47), Maris Court (40), Rule Chamber (42), Dream Rift (60), Broken
Hour (57), God (35) and God Eater (44).

## Overworld (`maps/`, `castle_interiors.png`, `prison_pit_shrine.png`)

Most of the overworld is vanilla Hoenn/Kanto recoloured into gloomy teal. The strong original set is a
**violet gothic castle interior** (mapsec 1). It has:

- skull bookcases and niches, gold skull banners;
- cyan spectral braziers;
- a glowing magic-circle floor, a summoning ring, a lava pit and a cross-shaped pool;
- a cell block (`s001_f650`).

That kit suits the Necropolis floors and Kimaris's chamber. The banners could be recoloured copper for the
Langerin crest, and the cyan braziers fit the Trial bonfires. `s140_dac4` (a cave shrine with a cracked seal
and a ritual dais) and `s008_1d30` (a pit ringed with bones/rocks) are smaller ideas.

`render_all.py` renders all 810 unique layouts; they are in scratch only, not committed.
