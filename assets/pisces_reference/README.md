# Pisces (user upload, 2026-11-15) — layout library

Pokemon Pisces is a pokeemerald-expansion hack with TRIPLE-LAYER metatiles
(primary metatiles->attributes spacing 12288 = 512 x 24), the same format as
MonoMyth and Ruination. The MonoMyth reader works unchanged:
`MONOMYTH_ROM=/path/Pokemon_Pisces.gba python3 -I -c "from romlib import find_headers"`
(tools/monomyth/romlib.py; the env var just names the ROM). 1387 header
candidates; 26 distinct town/city layouts, all decode cleanly (pisces_towns.png,
numbered; "secN" = region-map section id).

Notable layouts for Cormoria towns (structure, not art):
- 20 (sec12, 80x40): terraced seaside town, tiers stepping down to a beach + sea,
  grand hall on the top tier.
- 3 (sec1, 44x40): forest town around a pond with a central fountain island and
  four bridges.
- 5 (sec2, 56x42): beach village with two jetties.
- 11 (sec7, 47x44): forest hamlet, fenced gardens, sea on the west.
- 17/18 (sec10): dense stone port city; 22 (sec14): desert city around a crater lake;
  15 (sec9): walled castle city.
Pelluca stays on the user's reference image; these are the construction library
(how cliffs, shores and jetties are built) and candidates for later towns.
