# Pokémon Ghost Grey Version EX reference (asset source, used with permission; credit: JoeyZeed)

Supplied by the user 2026-11-19 as the reference for the **underground Mirroh Necropolis**: the catacombs
under its Lavender Town. Ghost Grey is a **FireRed** hack (BPRE, internal title "GG OBLIVION") by JoeyZeed,
whose visuals are all drawn originally for it. **Used with permission (user, 2026-11-19); credit JoeyZeed** in the
notes and credits for anything derived from them. The ROM is
not in the repo: read it with `tools/odyssey/` (`ODYSSEY_ROM=.../Ghost_Grey_EX.gba`).

Measured: map group table at FireRed's own address (pointer 0x5524C -> 0x83526A8), 43 groups, 705 maps.
Lavender Town is region section 92; its catacombs are section 140, six maps reached from it:
group 1 maps 89-94 (24x20, 24x20, 34x21, 24x33, 41x32, 24x20). Rounded cavern chambers ringed by brick, rows
of grave niches cut into the floor, demon-face reliefs over each passage, chasms crossed on ledges and islands;
the last (1.94) is a pillared chamber with a sealed gate and a carved floor seal (a natural Distortion-gate
room). All in Game Boy greyscale: they need a real palette (user).

Renders: `assets/ghostgrey_reference/` (`catacombs_1_89..94.png`, `catacombs_sheet.png`, `lavender_town_sheet.png`).

**Opal Village** (user 2026-11-20: loves its reflecting ice; study its landscape and its indoor and outdoor tiles for
Mirroh): Ghost Grey's northernmost town, region section 128 ("Opal Village", name pointer at 0x3F1D4C), outdoor map
group 33 map 5 (35x39, layout 0x8812780, snow weather; primary 0x82D4A94, secondary 0x82D4E24, no tile animation in
the secondary). Raised snowbanks held by brick retaining walls with stone stairs; dark icy paths strewn with
sparkles; two square sheets of reflecting ice (long diagonal reflection streaks) sunk inside brick rims, boulders at
their corners, a low fence along the front; snowy pines, benches, lamp posts, a snowman, a picket fence along the
south edge. Interiors: houses with kitchens and dining tables (33.7, 33.9-33.11), the Credits Museum's display halls
(33.8, 33.16: plinths on pale stone over a dark tiled floor), a rest room (34.8), more in group 1 (1.10, 1.11, 1.21).
All Game Boy greyscale like the rest of Ghost Grey: they need real palettes.
Renders: `assets/ghostgrey_reference/opal_village_33_5.png`, `opal_village_ice_zoom.png`, `opal_village_interiors.png`.


**Heater Forest** (user 2026-11-21: the model for the Necropolis Trial's ice-sliding puzzle; sliding ice, no cracking
ice): region section 130, maps 33.6 (32x46), 33.13 (22x22), 33.14 (30x29), 33.15, 36.5 (30x30), 36.6, 36.7.
Wide sheets of sliding ice (long diagonal streaks) walled by snowy pines; boulders scattered on the ice as the
stoppers, a few patches of snow on the ice where a slide also stops, the way on at the far side; in 33.6 dark
pits in the ice too. Step onto the ice and you slide until a boulder, a tree or the snow stops you.
Renders: `assets/ghostgrey_reference/heater_forest_33_6.png`, `heater_forest_33_14.png`, `heater_forest_36_5.png`.
