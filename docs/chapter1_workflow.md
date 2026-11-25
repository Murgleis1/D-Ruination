# Chapter 1 workflow: the completion order

**Locked by the user, 2026-11-19.** Read this before starting any Chapter 1 work, and check the next task against
it. Also recorded in `bible/20_chapter1_build.md` §16.10. It replaces the 2026-11-18 three-step process.

Chapter 1 is completed and polished in exactly this order:

1. **Towns and routes.** Design every area first and perfect them visually: exteriors and interiors, no NPC design yet.
2. **NPCs and enemy trainers.** All secondary NPCs and non-critical trainer fights (basic route trainers and the like).
3. **Quests.** Side quests, then main-quest work, which leads into
4. **Main story.** Important characters, scripted events, dialogue.
5. **Wild Pokémon,** overworld static encounters, special non-quest events.
6. **Items** to pick up or find lying around, including a few hidden items.
7. **Everything else.** New QoL features, anything missed.

Rules that follow from the order:
- In stage 1, an interior is designed for its look alone. Who lives in a home, its NPCs and its dialogue are stage 2
  or later.
- A puzzle's mechanics (scripts) belong to its quest (stage 3). Its map is stage 1.
- Areas that belong to later chapters wait for those chapters, even when they sit inside Chapter 1's map. One example
  is the Umbra sanctuary below Pelluca's beach cliff door, which is mid-game.

Map design rules (user 2026-11-20, "design 101"): **never cut a tree (or any object) in half, never let trees
smoosh on top of each other, never let them bleed into buildings, cliffs, walls or water.** Trees and props are
placed as whole units on a clear footprint; dense woods use the source tileset's own stacking pattern and end in
complete trees. **Terrain changes gradually**, the way MonoMyth's and Crown's routes do it at their boundaries: one
ground shade reaches into the next in patches with proper edge pieces, and tree kinds mix before they change.

Town rule (user 2026-11-21, a core design tenet): **buildings in a town must be easy to get into and out of.** Every
door opens onto wide open ground that joins the street directly. Never make the player squeeze between a building and
a wall, a fence or a line of props to reach a door. GBA doors face south, so put buildings where the ground in front
of them is open: with the street running along their fronts, not with their backs to it. Check this in the mock
before building.

How each area is done in stage 1: mock it first, get the user's approval, build it, verify it in the emulator,
add a bible note (`20_chapter1_build.md`), then commit and push.

## Stage 1 status

Done (each has a note in `bible/20_chapter1_build.md`):
- Pelluca Valley exterior. Doors: Umbra Lab, Seaside Tavern, dormitory, Templar hall, the Academy.
- Umbra Lab, Seaside Tavern, dormitory (1F, 2F, Osrid's room), Templar hall, the Templar holding cell.
- Academy main hall plus office, library, classroom and haunted lounge. The lounge is locked; its rusted-key unlock
  is a quest item.
- Cadmus's manor (`PellucaUmbraManor`). Locked until the mid-game sanctuary mission, when Cadmus gives House
  Umbra's sigil.
- Pelluca's five houses (`PellucaHouse1`-`5`).
- The ice path under the church (`PellucaIcePath`) with its thin-ice puzzle working (stages 1 and 3 combined for this
  piece, user), the hall after Eden's blast (a second hall layout, behind `FLAG_DR_CHURCH_BLASTED`), and the shrine's
  awakening with the Sparkling Opal (user asked for it now). Still stages 3-4: the blast scene, the Templar, the
  Opal-for-Warding-Ring exchange with Archbishop Ambrose (and the Ring's on/off repel).
- Route 11 (`Route11`, 90x40: the approved 90x30 picture with five rows of woods and sea above and below, out of
  reach), connected to Pelluca's west road. Its own secondary tileset under Pelluca's primary, built from the
  composer by `tools/art/route11/build_route11.py`. A provisional story gate on Pelluca's west road (open once the
  shrine is awakened; stage 4 sets the real condition). Music: MonoMyth's Route 15 theme (`MUS_DR_MM_ROUTE15`); Ghost Grey's Route 1 became Hollow Hill's theme (`MUS_DR_HOLLOW_HILL`). Pelluca's theme is now Crown's route theme 292 on piano (`MUS_DR_CROWN_PELLUCA_PIANO`). The east beach has no way
  down yet (revisit later, user). The west end waits for Hollow Hill.
- Hollow Hill: built (2026-11-20; mock v8: bone woods, dark stone, blood, red webs; the way north goes over the hill),
  connected to Route 11, thinned fog. Its tileset is nearly full. Later: a ruined structure on the top, the guardian
  quest (user). Next: the Mirroh area.
- Mirroh: built and walked, 2026-11-21, as three maps (`MirrohGate`, `MirrohLower`, `MirrohUpper`) and two
  gatehouse hallways. Reached from Hollow Hill's way north by a short fade.
  Interiors built and walked 2026-11-22: the Tavern (respawn point), the chapel, House Langerin's hall, the specialty
  shop and three homes (each with a bed). Homes need beds (user 2026-11-22).
- Mirroh Necropolis grounds (`NecropolisGrounds`): built and walked, 2026-11-21. Reached from Mirroh's skull gate.
- The Trial lake (`NecropolisLake`): built and walked, 2026-11-21. Reached from the grounds' grand entrance. Its
  frozen bank and its bonfires (unlit, and lit with an animated ghost flame for the Trial script to switch on) are done.
- Kimaris's chamber (`KimarisChamber`): built and walked, 2026-11-21. Fantasma's room, four MonoMyth cauldrons,
  copper, Mirroh stone.

Remaining (proposed order; re-reviewed with the user 2026-11-22). The way to the chapter's climax runs north from
Mirroh's north-west gatehouse (region map, column 4): Mirroh -> **Route 13** -> **Templar Headquarters ("Templar
Citadel")** -> **Mt. Mirroh** -> **Mirroh Peak**. Routes 14 (Mt. Mirroh east to Pierra's Manor) and 15 (Templar HQ east
to the Ivy River) are later chapters.
1. ~~Route 13~~: built and walked 2026-11-22 (40x128; forks to Templar HQ and Mt. Mirroh; stage 2: two trainers on the
   switchback ascent).
2. Templar Headquarters: courtyard BUILT and walked 2026-11-22 (`TemplarCitadel`, a fade from Route 13's NE exit). **The four courtyard houses BUILT and walked 2026-11-23** (the Tavern with its staff and heal point, the barracks, the armoury, the watch house; `citadel_rooms/build_houses.py`; walk `tools/playtest/citadel_houses_walk.py`). **The cathedral BUILT and walked 2026-11-23** (`TemplarCathedral` the nave; the study, the bishops' hall and dormitory, the Braviary registry, the kitchen, the storehouse; the Sanctum built, sealed; `tools/art/templar_hq/cathedral/build_cathedral.py`; walk `tools/playtest/cathedral_walk.py`). The east house became a watch house (user: a mews would repeat the registry). Stage 1 for the Citadel is complete. (Was in progress 2026-11-22: zone plan v2, the church cut from Pokémon Empire's Arceus church; required before Mt. Mirroh, the first Ambrose meeting; interior two levels, cathedral + offices, the Sanctum above). Was: Crown's gothic cathedral on its moat island with timber chalets, alpine snow, perhaps an
   outer wall (bible 16.10 art plan). In Chapter 1 the way to the mountain passes it; Loulan recurs there.
3. Mt. Mirroh and Mirroh Peak (in progress 2026-11-23; **the exterior BUILT and walked**, `tools/playtest/mt_mirroh_exterior_walk.py`; **1F BUILT and walked, approved 2026-11-24** (Mt. Thunder construction, Grotto glass-ice crystals, crystal maze, formations), `tools/playtest/mt_mirroh_1f_walk.py`; **the Peak BUILT and walked 2026-11-24** with MonoMyth's bastion backdrop behind its summit, `tools/playtest/mt_mirroh_peak_walk.py`; **B1F BUILT and walked 2026-11-24**, the Blast Crater (mock v3 approved), `tools/playtest/mt_mirroh_b1f_walk.py` on a test ROM): **an expansion of Dreamstone Mysteries' Mt. Mirroh** (user): the exterior climb (dojo removed), 1F (hikers, trainers, the torture scene by the exit up to the Peak, the Shard under rubble at the old Peak exit; 2F removed), the Peak (the cardinal, Baradus, Eden, Kimaris; summit ruins). B1F: Alaric's sealed Ting-Lu ritual site, made now, reached later by a ladder beside the exterior's cave mouth under a Rock Smash rock. Art: Route 13's, MonoMyth's Mt. Thunder, DM's snow, Crown's if any. The base game's maps (`MtMirrohExterior`, `MirrohPeak`, the caves `MirrohInterior_*`) are DM-era, on old
   tilesets: rebuild or replace.
4. ~~The Ancient Cormoria slip (Beat 8e)~~: BUILT and walked 2026-11-24 (`AncientCormoriaSlip`, its own tilesets and
   the ancient backdrop; walk `tools/playtest/ancient_cormoria_slip_walk.py` on a test ROM, as nothing leads in until
   stage 3's script). Approved ("It is perfect now"). DM's `AncientMirroh` cluster kept for a later chapter.
5. Pelluca's other exits (Ivy River, Hoya Delta, Route 10) as far as Chapter 1 uses them (closed for now).
Later, from stage 1 notes: Hollow Hill's ruined structure on its top (the guardian quest; **built 2026-11-25** as its own summit map, `HollowHillSummit`); Route 11's east beach;
Hollow Hill's webbed rocks and cobwebbed trees (user 2026-11-24).
Also done 2026-11-24: Route 11's farmhouse interior (`Route11Farmhouse`, door (55, 14); walk
`tools/playtest/route11_farmhouse_walk.py`). Note: `build_route11.py`'s `write_map()` is stale (it rewrites Pelluca's
gate events and Route 11's connections); do not re-run it as is.

Update this list as areas are finished.

## ROM space

- 2026-11-23: the ROM is at 95.75% (32,126,720 of 33,554,432 bytes; about 1.36 MB free) after the Templar cathedral.
- 2026-11-24: 95.82% after Mirroh Peak's backdrop and deleting 15 unused Dreamstone Mysteries maps (bible: Mirroh Base Camp, Pelluca's old gym/mart/restaurant etc.).
- 2026-11-24: 95.93% after the Ancient Cormoria slip (new map AncientCormoriaSlip, its own tilesets: 1015 of 1023 tiles, 255 of them its backdrop).
- 2026-11-24: 95.95% after Route 11's farmhouse interior (Route11Farmhouse).
- 2026-11-24: 95.98% after Mt. Mirroh B1F, the Blast Crater (MirrohInterior_B1F rebuilt 40x40, its own tilesets: 626 tiles).
- 2026-11-25: 96.12% with the harbour's water animated (was 96.08% after Pelluca Harbour (the waterfront as its own map, 569 tiles; four vessel sprites; PellucaCity cut to 80x42)).
- 2026-11-25: 96.23% after Hollow Hill's summit (new map HollowHillSummit, its own tilesets: 988 tiles).
- **User 2026-11-23:** unused maps may be deleted to make room (e.g. Dreamstone Mysteries' other cities that nothing of
  ours uses so far). When space runs short: list the candidates (unused maps, their tilesets and music, the bytes each
  frees, after checking no kept map, script, warp, heal location or region-map entry points at them), show the list,
  then delete and clear their references.
- 2026-11-25: 96.24% (32,293,608 bytes) after Hollow Hill's webs v2, sealed door v2 and cloud cap v3.
- **Where the space goes (measured 2026-11-25 from pokeemerald.map; 30.8 of 32 MiB used; 32 MiB is the GBA's hard
  limit):** Pokemon cries, every species Gen 1-9, 8.0 MiB; Pokemon battle sprites/icons/palettes 6.7 MiB; Pokemon
  follower overworld sprites 1.46 MiB; music 3.0 MiB (our 4 imported songs 1.85 of it: A Legend Unfolds 1.2 MiB,
  MonoMyth Route 15 409 KiB, Crown Pelluca 172 KiB, Old HQ 110 KiB) + instrument samples/voice groups 1.0 MiB; code
  2.2 MiB; map tilesets 1.9 MiB (ours 10-30 KiB each: Hollow Hill 30, its summit 19, the harbour 13); event scripts
  and text 1.5 MiB; map layouts, all 646, 1.2 MiB (Dreamstone Mysteries' and ours 0.56 of it); other graphics 1.2 MiB;
  people/object overworld sprites 0.67 MiB; trainer battle sprites 0.23 MiB; battle backgrounds 0.12 MiB.
- **The budget (user 2026-11-25: "keep all of it in mind as we progress"):** replacing Emerald's and Dreamstone
  Mysteries' maps, overworld and trainer sprites and battle backgrounds with ours is roughly break-even if counts and
  sizes stay alike. What decides whether the whole game fits: (1) **leaving out Pokemon families the game never uses**
  (include/config/species_enabled.h drops a family's cries, sprites, followers and data: the biggest lever, likely
  8-10 MiB); (2) **music on shared instruments** (each imported song carrying its own samples costs ~110 KiB-1.2 MiB;
  30-40 more like that would not fit; re-voiced onto one shared voice group ~30-100 KiB each); (3) **sharing a tileset
  across an area** rather than one per map where the look allows. Smaller: Emerald's own music and instruments
  (~2 MiB as ours replace them), the minigames the expansion added (pinball, pachinko, blackjack, derby, mining,
  ~0.4 MiB), the Colosseum link data, Battle Frontier and contest content.
- **If space ever runs short (user 2026-11-25):** cut base Emerald material or base Dreamstone Mysteries material to
  compensate (as above: list candidates and the bytes each frees, check nothing kept points at them, show the list,
  then cut). **Some Pokemon can go because they would not exist in Empire-era Cormoria** (user): to be listed with the
  user before any family is disabled.

## Dialogue audit (user 2026-11-23)
Once the next few phases of Chapter 1 are further along, the user wants **another full sweep audit and analysis of all of Chapter 1's dialogue and everything else**. Flag this when those phases land.
