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
2. Templar Headquarters (in progress 2026-11-22: zone plan v2, the church cut from Pokémon Empire's Arceus church; required before Mt. Mirroh, the first Ambrose meeting; interior two levels, cathedral + offices, the Sanctum above). Was: Crown's gothic cathedral on its moat island with timber chalets, alpine snow, perhaps an
   outer wall (bible 16.10 art plan). In Chapter 1 the way to the mountain passes it; Loulan recurs there.
3. Mt. Mirroh (the climb: Beat 8a, the tortured Beads cultist) and Mirroh Peak (Beats 8b-8c: Baradus, Eden,
   Kimaris). The base game's maps (`MtMirrohExterior`, `MirrohPeak`, the caves `MirrohInterior_*`) are DM-era, on old
   tilesets: rebuild or replace.
4. The Ancient Cormoria slip (Beat 8e): one small scripted zone. A new map: DM's `AncientMirroh` maps are DM's window
   into *our* era (bible 01), not Cormor's.
5. Pelluca's other exits (Ivy River, Hoya Delta, Route 10) as far as Chapter 1 uses them (closed for now).
Later, from stage 1 notes: Hollow Hill's ruined structure on its top (the guardian quest); Route 11's east beach.

Update this list as areas are finished.
