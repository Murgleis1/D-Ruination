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
  shrine is awakened; stage 4 sets the real condition). Music: MonoMyth's Route 15 theme (`MUS_DR_MM_ROUTE15`); Ghost Grey's Route 1 became Hollow Hill's theme (`MUS_DR_HOLLOW_HILL`). Pelluca's theme is now Crown's route theme 292 on piano (`MUS_DR_CROWN_PELLUCA_PIANO`). The east beach has its own
  stairs down (x 77-78, 2026-11-25). The west end waits for Hollow Hill.
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
5. ~~Pelluca's other exits~~ (Ivy River, Hoya Delta: closed, guards; checked 2026-11-25, `tools/playtest/pelluca_exits_walk.py`;
   the west gate's rows 31-32 closed too). Route 10 has no departure point yet: a later chapter's decision.
Later, from stage 1 notes: Hollow Hill's ruined structure on its top (the guardian quest; **built 2026-11-25** as its own summit map, `HollowHillSummit`); Route 11's east beach (**stairs built 2026-11-25**);
Hollow Hill's webbed rocks and cobwebbed trees (user 2026-11-24; **webs v2 built 2026-11-25**).
Also done 2026-11-24: Route 11's farmhouse interior (`Route11Farmhouse`, door (55, 14); walk
`tools/playtest/route11_farmhouse_walk.py`). Note: `build_route11.py`'s `write_map()` is stale (it rewrites Pelluca's
gate events and Route 11's connections); do not re-run it as is.

Update this list as areas are finished.

**Stage 1 review pass (2026-11-25; `tools/review/`, sheets in `assets/stage1_review/`):** all 60 Chapter 1 maps rendered
by area; every warp checked to land on an existing map and warp, every object, sign and warp on its map (`check.py`: 0
problems); every walkable cell no warp or road reaches listed and looked at (`reach.py`): all are pockets out of reach
by design (wall tops, the holding cell behind its bars, the kitchen's corner behind the stove, the snow behind the
Citadel's houses and Mirroh's towers, cliff tops on the DM-era exterior), none a trap. Every map edge the player can
reach on foot leads somewhere or turns the player back (`tools/playtest/pelluca_exits_walk.py`); the west gate's
rows 31-32 were the one gap, closed. All standing walks pass.

**Build gotcha (2026-11-25):** the Makefile does not track a layout's `map.bin` (it is `.incbin`'d through
data/layouts/layouts.inc), so a map.bin patched alone is not rebuilt: after changing one, `rm -f
codebase/build/modern/data/maps.o` before `make` (builders that also rewrite layouts.json or tilesets trigger it anyway).

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

## Stage 2 begins: the NPC and trainer cast (user 2026-11-25)

- **Direction (user):** look over every NPC and replace them with proper overworld sprites and trainer front sprites
  from Crown, MonoMyth, Odyssey and Fantasma; "a good mix of medieval men, women, knights, noblemen, noblewomen,
  merchants, etc."; **every typical Emerald NPC sprite and trainer type is deleted** as the new set comes in.
- **Decisions (user 2026-11-25):** Lazarus left out (its people are drawn chunky and big-headed, unlike the others and
  Emerald); **redress where needed**: where no sprite fits a role as is, recolour and redress the closest body
  (doublets, tunics, gowns, armour), as for Osrid; **Emerald's own maps and trainers are cut too**, not just
  redirected (list every dependency first, show it, then cut: the engine's references to Emerald maps — new-game
  start, heal locations, Battle Frontier, contests, secret bases and the like — come out with them).
- **Survey (`assets/npc_survey/`, `tools/npc/`):** overworld people: MonoMyth 246 (assets/monomyth_ow), Crown 152
  (FireRed's cast plus priests, nuns, a plumed knight, witches; assets/crown_reference/npcs_main_table.png), Odyssey
  264 (Emerald-era, mostly modern), Fantasma 2188 records (people and Pokemon; people mostly modern). Trainer fronts:
  MonoMyth ~150 (assets/monomyth_reference/trainer_fronts), Fantasma 219 (vanilla-style; a few robes, gowns, a captain,
  a sage), Odyssey 148 (a loud cartoon style; palettes not yet read right). **Crown's trainer-front table is dummied**
  (every entry points at one placeholder): its fronts must be read another way (captured in battle in the emulator).
- **Scale:** Emerald has 289 overworld graphics ids, 137 trainer pics, 98 trainer classes; 4,032 object events across
  all maps use 328 graphics.
- **Cast list approved (user 2026-11-25: "generally correct"), plus robed cultists from MonoMyth** (user: "you also
  missed some robed cultists from MonoMyth"). Candidates (MonoMyth overworld numbers; frames in
  `assets/npc_survey/mm_frames/`, sheet `monomyth_robed_hooded.png`): 217 navy hooded robe with gold trim; 105 and 131
  grey robes with an eye sigil; 156 brown pointed hood; 84, 89, 90 deep blue hoods; 102 red-hooded figure kneeling;
  also robed clergy and sages: 68 and 188 white-and-blue robes, 115 blue-robed bearded sage, 116 blonde in blue robes,
  57 red-robed elder, 141 white-haired green robe. Trainer fronts to pair: MonoMyth #82 (dark hooded figure), #96
  (staff-bearing robed wanderer), #85 (nun-like), #92 and #93 (robed elders).
- **Kept (user 2026-11-25, "I like these at least"):** MonoMyth overworld **188** (white-and-blue robed elder, tall
  hat), **84, 89, 90** (the three deep blue hoods), **57** (red-robed elder), **116** (blonde in blue robes). The
  hoods' north-facing frames came out blank in the extraction: check whether MonoMyth has them before import (the
  extractor reads frame k from images[k-1]; they may use a shorter frame table). **The user will supply a few sprite
  sets of their own** to go with these.
- **The user's own sets (user 2026-11-25):** first, a **young nobleman** (Essentials-style front, 2x, and a 4x4 walking
  sheet, 2x; `tools/npc/noble_boy/src_*.png`): "three variations of this boy with black, light brown and blonde hair
  plus his overworld sprite (and slightly different shades of skin color) ... a great set of spoiled noble boy
  trainers for almost the entire game"; "change the color of his outfit a bit for each variation too". Mock v1
  (`tools/npc/noble_boy/noble_boy.py`, `assets/npc_survey/noble_boy_v1.png`): black hair, fair skin, burgundy coat and
  gold waistcoat; light brown hair, medium skin, forest green and cream; blonde, light-tan skin, navy and silver; each
  15 colours. **The fronts are 74 px tall at native size, Emerald's frame is 64x64**: two fits offered (scaled to fit,
  or full detail cropped at the shins). The overworld frames (16x24) fit Emerald's 16x32 as they are.
- **Fit decided (user 2026-11-25: "the shrinking works"):** trainer fronts taller than Emerald's 64x64 frame are
  **scaled to fit** (whole body, feet included), not cropped; the standard for every set from now on. The noble boy's
  three variants are approved as mocked (`assets/npc_survey/noble_boy_v1.png`).
- **The Sword Cult set (user 2026-11-25).** The cult's colours are **black with icy sky-blue trim**, a smooth, clear mix,
  for the acolytes, the masked **Cardinals** (directly under leaders such as Baradus) and Baradus's clothes. The user's
  sprites: the masked villain (front, a doubled pair, a 4x4 overworld sheet) for the Cardinals; trainer030 (hooded robe)
  for the acolytes. Mock v1 (`tools/npc/sword_cult/sword_cult.py`, `baradus.py`, `board_v1.py`;
  `assets/npc_survey/sword_cult_v1.png`): Cardinal cloak black, gold rim to ice, green trousers to slate, the pale mask
  and red eye kept; front fitted to 64x64 (nearest keeps the one-pixel trim whole; an area shrink smeared the mask colour
  onto the cloak), overworld converted to Emerald's 9 frames at 32x32. Acolyte robe black, ice at the hood rim, cuff,
  belt and hem, boots black. **MonoMyth 84/89/90 are one short hunched hooded figure in three facings (east, south, west)
  with no north and no walk frames** (the "blank north frames"): usable as static kneeling acolytes; **MonoMyth 217
  (navy robe, gold band and face plate, all 9 frames) recoloured is offered as the walking acolyte.**
- **Baradus (user 2026-11-25): his sunglasses go sky blue** to contrast with his black hair, beard and clothes, and his
  coat takes the trim; "make sure any changes you do reflect properly across all his assets" (battle front, overworld,
  the three portraits). Same rules everywhere (`baradus.py`): ice collar piping (coat pixels touching the neck), on the
  front also cuffs and a hem; three palette slots freed per asset by merging near-identical blacks (1-12 levels; on the
  anger portrait the 2-px tooth glint into the white beside it). **Glasses: frames are the grey-blues, glass is the
  enclosed black; a black pixel touching hair, skin or transparency is a line, not glass, and stays black** (user: the
  top row of the right lens under his hair "should be a black line ... not sky blue"; "clearly differentiate between the
  black glass versus the frames"). On the front the glasses' top row is that line and row 9 the glass; on the
  overworld the F row the line, the A pixels the glass, index 3 the frame. Two options mocked: **A** ice glass (frames
  as they are), **B** ice frames (glass black). The overworld takes the collar only (cuffs at 16 px read as gloves).
  Mock only: nothing installed yet.
- **Baradus decided (user 2026-11-25): glasses option A** ("Glasses A is correct on the glasses part of his
  portrait": the glass ice blue, frames as they are) and **no trim on his clothes** ("Only the glasses area you did
  should have the blue"; taken off all five assets, as the user's own paints of the overworld and front carry none).
  **The user painted the overworld and front as targets** ("just cleaner than what I did"), matched to the sprites
  pixel for pixel (the overworld paint at 28 px a pixel, mean error 4; the front at 1.83x, error 7): **overworld,
  two 3x2 lenses at x 4-6 and 8-10 on the glasses' two rows** (the old 1-px glass, its frame and the outer grey),
  the bridge x 7 dark, the west frames one 2x2 lens at x 4-5; **front, rows 8-9 (row 7 his brows), left lens x 26-27,
  right x 30-32**, the bridge dark. Each lens: a light pixel top-left, the top row light ice, the bottom row deeper,
  as the portraits. Mock v2: `tools/npc/sword_cult/board_baradus_v2.py`, `assets/npc_survey/baradus_glasses_v2.png`,
  `baradus_glasses_v2_close.png`. **Installed (user 2026-11-25: "I love what you have done with Baradus now ... He's
  almost like the human incarnation visually of Chien-Pao. Very cool and yes implement them")**: the five PNGs in
  `codebase/graphics/` rewritten (originals kept in `tools/npc/sword_cult/src_baradus/`, which `baradus.py` now reads,
  so a re-run cannot apply twice). Checked: `tools/npc/sword_cult/check_rom.py` decodes all five from the built ROM,
  pixels and palettes match the PNGs, three ice slots each; **in the emulator** on a test ROM (the harbour arrival with
  Cadmus drawn as Baradus, his three portraits in Cadmus's lines, a test battle against TRAINER_ROUTE1_A in his
  picture; edits reverted, the real ROM rebuilt to the same checksum): `tools/playtest/baradus_assets_test.py`, the
  three portraits exact, the battle front exact (0 of 855 pixels in view differ), the overworld exact in rows 0-24
  (7 pixels at his feet differ where the player stands over them). `assets/npc_survey/ingame_baradus_glasses.png`,
  `ingame_baradus_crops.png`.
- **Cast board v2** (`tools/npc/board_v2.py`, `assets/npc_survey/cast_candidates_v2.png`): every pick coded (role
  number, a-h overworld, A-H fronts) for refining by code; rows 22-23 the Sword Cult set, 24 the other cultists.
- **Roles rethought (user 2026-11-25): "'commoner' seems like the wrong thing here in the context of the empire. We
  need a better list."** The user is supplying sets role by role.
- **The older noblewoman class (user 2026-11-25):** the user's three 'socialite' designs (fronts and overworld
  sheets; `tools/npc/dowager/user_*_2x.png`): "good older empire female noblewomen ... All variations of the same older
  female trainer class you can come up with that fits the Empire era lore". **The user's overworld sheets are Gen 4
  size** (figures 16-17 x 24-26 in 32x32 cells) **against our cast's MonoMyth size** (MonoMyth 57 and 188 14x20,
  Baradus 13x19): a head taller than everyone; the user: "if these overworld sprites aren't the right generation, feel
  free to find the closest matches". (The noble boy's overworld, 16x24, is the same Gen 4 size: flagged.) Mock v1
  (`tools/npc/dowager/dowager.py`, `assets/npc_survey/older_noblewoman_v1.png`): fronts fitted to 64x64; three
  colourways each (outfit and accent as house-palette suggestions, hair white / silver / iron grey, skin fair /
  medium / bronzed, the last the Yo'aki tone); overworlds from MonoMyth at our size: **design 1 MonoMyth 24 with a
  brimmed hat drawn on** (no MonoMyth old woman wears one) and the front's rose scarf at the neck (the bare tan collar
  under her chin read as a beard), **design 2 MonoMyth 16** (grey bun, lilac dress), **design 3 MonoMyth 24**.
  (MonoMyth 21, white-haired in the catalogue, is a bearded old man.)
- **The user's picks from the cast board (2026-11-25, "These are the ones you gave me that I like"):** 4A Fantasma 138
  (old man, cane and watch), 5A MonoMyth 22 (old woman, grey gown and flowered hat), 7A Fantasma 212 (farmer),
  8B MonoMyth 89 (red-bearded labourer), 11A MonoMyth 116 (gold coat and hat), 14B Fantasma 110 (bald monk with a
  staff), 16B MonoMyth 30 (white-haired spearman), 20B MonoMyth 68 (flute player), 21B Fantasma 14 (purple witch),
  24B Fantasma 196 (ghost). **All to be recoloured** ("to make them different from Monomyth and distinguish them
  more"). **MonoMyth 116 -> the Merchant class** ("if you redesigned his colors, hair color and altered his hat a
  bit"); **MonoMyth 30 -> the Imperial Officer class** ("with some major color changes and tweaks"); **Fantasma 196
  -> the Revenant class** (user: the class name "should be Revenant"): undead trainers met here and there round
  Hollow Hill, an actual ghost fighting with ghosts. **Templars are a trainer class too** (user: "though I don't think
  you fight that many in Chapter 1 ... like just one or two"); the class, front and overworld exist since 2026-07-22
  (`TRAINER_CLASS_TEMPLAR`, `TRAINER_PIC_TEMPLAR`, `OBJ_EVENT_GFX_TEMPLAR`: a brown hooded robe).
  Recolour v1 (`tools/npc/picks/extract.py` pulls the ten indexed from the ROMs; `recolour.py`;
  `assets/npc_survey/picks_v1.png`): palette edits, each sprite's own shading kept: the old man's suit dark green
  tweed; the old woman's gown forest green, ribbons rose, flowers cream-gold; the farmer's overalls green-grey wool,
  hat straw; the labourer dark-haired, leather vest, linen sleeves, slate trousers, brass belt; **the Merchant** a
  bottle-green coat (the hat and collar with it), chestnut hair, a white plume with a red tip in his hat and a red
  band; the monk as a Templar priest (white robe, the Order's blue stole, gold orb); the minstrel teal and mustard;
  the witch moss green, plum hair; **the Revenant** ashen spectral blue, the red eyes brighter. **The Imperial
  Officer:** the torch, its shaft and the round bag slung behind his right shoulder cleared down to the pauldron's own
  outline (a first cut had sliced the pauldron: user "his shoulder busted now"); the leather the uniform, the fur
  (moved to its own slot, rows 17-37, not his face or hands) the mantle; **three options, as the army has no colours
  on record**: A crimson and grey fur, B imperial purple and gold, C forest green and brass. Overworlds to follow
  once the fronts are settled.
- **Picks v2 (user 2026-11-25):** **the Officer purple and gold** ("Purple is the Empire's main color"; the user
  wrote "C", the purple one being third of the four in the comparison sent, source first: read as purple); **his
  shoulder** ("still needs a bit of work"): the notch the bag left between collar and pauldron closed with the
  pauldron's dark plate and an outline; **black hair and brows** ("why didn't you just make his hair and eyebrows
  black?"): a first pass recoloured by palette slot and turned his bushy white brows (two rows, set straight on his
  black eye lines) and an eye white into one dark band ("racoon eye"); redone by feature: the hair black with dark
  steel sheen, each brow a thin two-pixel stroke a row above its eye with skin between, both eye whites kept ((29, 9)
  and (24, 10); the user caught the second missing), the grin kept. **The Merchant** teal (not green), the hat's crown raised two rows (a capotain) with a red band (a plume read
  as a stick and was dropped), his face's shading moved off the coat's slots (it had turned teal), **flipped**
  ("his pose would look better"). **The old woman's gown brown.** **The Revenant**: a skull face (sockets with red
  pinpoints, nose cavity, hollow cheeks, teeth), rotted hair (bald patches, lank strands over the face, a ragged
  crown), the coat in rags (torn notches down both edges, a ragged hem the wisps eat into, rips with ghost-light).
  `assets/npc_survey/picks_v2.png`. **Purple recorded as canon** (bible 16.6 item 7).
- **Decisions (user 2026-11-25):** **the Templars move to the Order's blue** ("for sure"); **the older noblewoman
  class is the Dowager** ("Dowager sounds right"); **the Sword Cult's walking acolytes use MonoMyth 217**, the hooded
  figures 84/89/90 the kneeling ones ("I think so"). **Templar blue v1** (`tools/npc/templar/templar_blue.py`,
  `assets/npc_survey/templar_blue_v1.png`; originals kept in `tools/npc/templar/src/`): the robe's slots matched by
  brightness onto the cathedral nave runner's ramp (so its shading keeps its depth), skin and legs kept; on the front
  a brown crease colour joins the robe and the cord belt and creases that were brown become the Order's gold (the
  study's rug pairs the Order blue with gold), in a slot freed by merging two robe browns that land on the same blue.
  The monk-priest's stole moved onto the same ramp. **Approved (user 2026-11-25: "That's a good female templar")
  and installed**: the existing Templar is the female; checked from the built ROM (front and overworld, pixels and
  palettes match) and **in the emulator** (`tools/playtest/templar_blue_check.py`: Pelluca's north road guard, 0 of
  186 pixels differ; `assets/npc_survey/ingame_templar_blue.png`), after regenerating the save-state chain (a state
  from the build before froze the player: the new graphics shift the ROM). **The male Templar** (user: "Here is the
  male variant one that should be recolored blue properly"; the user's trainer322 front and trchar322 overworld,
  `tools/npc/templar/male/user_*.png`; the overworld 16x32 frames, our cast's size): mock v1
  (`tools/npc/templar/male/male.py`, `assets/npc_survey/templar_male_v1.png`): the coat and trousers the Order's navy
  (by brightness, as the female), the round shield's face the Order blue with its spokes and boss gold (the chest
  pattern within it blue and gold too, a tabard), the staff with its flame, his blond hair and skin as drawn; the
  front fitted to 64x64 by `fit64_phased` (`tools/npc/sword_cult/sword_cult.py`: nearest sampling at the phase that
  keeps the most coloured pixels; a plain shrink had dropped the staff's one-pixel wood line and left its two
  outlines touching), 15 colours; the overworld as Emerald's 9 frames.
- **Male Templar v2 (user 2026-11-25: "The male templar's helmet and blade should be gold colored"):** what read as
  blond hair is his **helmet** and the staff's flame-shaped top a **blade**: both onto the Order's gold ramp by
  brightness (front: the head's helmet colours and everything of the staff above row 24; overworld: the helmet
  colours in each frame's head rows). `assets/npc_survey/templar_male_v2.png`.
- **The Adventurer class (user 2026-11-25):** the Hiker, which "in Empire-era Cormoria he'd simply be called an
  Adventurer": **Fantasma 0** (19B on the cast board: feathered hat, backpack, walking stick), "more medieval colors
  (like a red and beige mix of clothes with dark brown leather boots)": the vest and hose red, the shirt sleeves beige
  linen, the boots (and the hat's shadow) dark brown leather, the neckerchief beige (the reds from row 15 down onto
  the sleeves' slots; the feather and his cheeks keep the reds), the tan breeches and pack as drawn.
  `tools/npc/picks/recolour.py`, `assets/npc_survey/adventurer_v1.png`.
- **The male Templar and the Adventurer approved (user 2026-11-25: "I love the completed work you have done now on
  the male templar and the Adventurer class. Great job").**
- **The seafolk (user 2026-11-25): Fantasma 94, MonoMyth 67, Fantasma 129** ("make them proper medieval era clothed";
  "new names that sound less modern than just fisherman or sailor"; "the sailor and the old guy with the anchor
  probably just need adjusted designs to make them seem more appropriate for an empire era setting"; "The fisherman
  just needs more of a pointed style witch hat"). Names proposed: **Oarsman** (the flexing sailor: a galley rower),
  **Bosun** (the old seaman with the anchor and chain: the boatswain kept anchors and rigging), **Angler** (the
  fisherman; Old English for the fishhook). v1 (`tools/npc/picks/recolour.py`, `assets/npc_survey/seafolk_v1.png`):
  the Oarsman's sailor cap and its ribbon tails a red knitted cap, the navy square collar a leather jerkin's neck and
  shoulder, the shirt's navy bands a leather belt, shirt and slops cream linen, the red neckerchief kept (a first
  pass caught his face shading in the cap's area and reddened it); the Bosun's purple vest oxblood leather (purple is
  the Empire's), his greys weathered sailcloth, **a knotted headscarf** in the vest's oxblood over his bald crown,
  tied at the back; the chain, anchor, peg leg and pipe kept; the Angler **a pointed hat**: Fantasma 14's (the witch;
  her head his width) with four rows cut from its straight crown so the crooked tip fits the frame, five pixels right
  on his head, brim on his old cap's line, its purples onto his tan and leather browns (a felt hat to match his
  leather jerkin, once an orange vest), his hood undyed wool, the cooler a wooden crate, the bobber cork-brown.
