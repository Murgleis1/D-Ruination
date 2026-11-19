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
