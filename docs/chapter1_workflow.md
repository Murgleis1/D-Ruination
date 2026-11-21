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
- Mirroh Necropolis grounds (`NecropolisGrounds`): built and walked, 2026-11-21. Reached from Mirroh's skull gate.
- The Trial lake (`NecropolisLake`): built and walked, 2026-11-21. Reached from the grounds' grand entrance. Its
  frozen bank and its bonfires (unlit, and lit with an animated ghost flame for the Trial script to switch on) are done.
- Kimaris's chamber (`KimarisChamber`): built and walked, 2026-11-21. Fantasma's room, four MonoMyth cauldrons,
  copper, Mirroh stone.

Remaining (proposed order):
1. Mirroh's interiors (next session), then Mt. Mirroh and Mirroh Peak (the one after).
   The base game's Mirroh maps are still on old tilesets.
2. Pelluca's other exits (Ivy River, Hoya Delta, Route 10) as far as Chapter 1 uses them.

Update this list as areas are finished.
