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
- **Seafolk names decided (user 2026-11-25): "the fisherman class should just be called Fisher, and the guy with the
  anchor's class is Corsair, and the sailor should be called a Mariner"** (replacing the proposed Angler, Bosun,
  Oarsman).
- **The male Templar installed (2026-11-25)**: `graphics/trainers/front_pics/templar_male.png`,
  `graphics/object_events/pics/people/templar_male.png` (from `tools/npc/templar/male/male.py --install`), wired as
  the female was: `OBJ_EVENT_GFX_TEMPLAR_MALE` 289 (`NUM_OBJ_EVENT_GFX` 290), `OBJ_EVENT_PAL_TAG_TEMPLAR_MALE` 0x1133,
  `TRAINER_PIC_TEMPLAR_MALE` 136 (`TRAINER_PIC_COUNT` 137), under `TRAINER_CLASS_TEMPLAR`. Checked from the built
  ROM (front and overworld, pixels and palettes match) and **in the emulator** on a test ROM (Pelluca's east road
  guard in his graphics; 0 of 204 pixels differ; `assets/npc_survey/ingame_templar_male.png`); the save-state chain
  regenerated (all walks pass). **Two build gotchas found:** (1) changing `NUM_OBJ_EVENT_GFX` shifts the dynamic
  graphics ids the maps use, and `make` does not rebuild `maps.o` for it: `rm -f build/modern/data/maps.o` (as after
  a `map.bin` patch); (2) **a new INCBIN'd graphic can be linked missing without an error** (the .o's dependency scan
  predates the new line, so the .4bpp is never built): after adding graphics, remove the including file's .o (here
  `event_object_movement.o`) and **always read the graphics back from the ROM** (`tools/npc/sword_cult/check_rom.py`'s
  decoders) before trusting a build. And a playtest note: a save state taken inside a map has that map's objects
  already loaded; to see a test ROM's object changes, leave the map and come back (`templar_blue_check.py --reload`:
  down the harbour stair and back up).
- **Walking sprites, begun (user 2026-11-25: "proceed"; "many of the sprites we are replacing in Pelluca Valley
  first are some of these new ones").** The seafolk v1 (`tools/npc/walkers/seafolk.py`,
  `assets/npc_survey/seafolk_walkers_v1.png`), MonoMyth bodies at our cast's size: **Mariner** from MonoMyth 194 (its
  red cap toned to the front's red; the black clothes cream linen, the red trim leather, the blond hair brown);
  **Corsair** from MonoMyth 45 (bald, white-bearded, purple vest: MonoMyth's own walker for front 67): the vest
  oxblood, the greys sailcloth, the knotted headscarf over his crown (a knot at the back on the north frames, tails
  behind on the west); **Fisher** from MonoMyth 233 (a round felt hat; MonoMyth 87's pointed witch hat could not be
  lifted, its walker has 12 frames): the crown drawn up into a point, one narrower a row and leaning back, tan felt,
  the jacket wool under a leather jerkin (a first cone narrowed to one pixel and read as an antenna).
- **Seafolk walkers v2 (user 2026-11-25: "the base overworld sprites you chose for the mariner and fisher just are not
  the correct ones you need to modify"; picked: the Mariner **Fantasma 87**, "the Fisher is FA 221 ... what needs the
  pointy hat to match your new front sprite"):** Fantasma's own walkers, read by `tools/npc/fa_walker.py` (each
  walker's images-table entry points at its sheet, nine 256-byte frames back to back; the table's next entries are the
  next walkers, so reading entry by entry gave other people's frames). **Mariner**: the blue cap red (the knitted
  cap, on spare slots), the striped shirt linen and leather, the slops cream (his hair moved onto browns of its own),
  the red neckerchief kept. **Fisher**: the baseball cap cleared and **a pointed felt hat** drawn in its place (a brim
  a pixel wider than his head, a dark band, the crown one narrower a row and leaning back), black hair under the brim,
  the red jacket a leather jerkin, the white an undyed wool hood, the yellows tan breeches. The Corsair stays
  MonoMyth 45. `tools/npc/walkers/seafolk.py`, `assets/npc_survey/seafolk_walkers_v2.png`.
  The Fisher's hat redrawn (user: "looks like you cut it off at the very tip"; the crown had stopped at a 4-pixel row
  with no outline above it): even edges (the left stepping in every row, the right every other row, so it leans
  back), closing to a point **filled with felt to the end** (a 3-wide row, outline-felt-outline, capped by one
  outline pixel; a tip of bare outline, and a bent-over last pixel, read as a string: user "the tip looks like a
  string").
  **Then rebuilt on MonoMyth's own witch hat** (user 2026-11-26: "go look at witch overworld sprites in MonoMyth so
  you can see how a witch hat looks"): MonoMyth 87's hat is not a tall cone but **a short crown whose floppy tip
  folds over to the back, a dark band with a buckle, and a wide floppy brim drooping past the face at both sides**.
  Its hat is lifted frame for frame (its 12-frame order onto Emerald's 9: 0, 1, 2, 4, 5, 6, 7, 8, 9) onto the
  Fisher's head, its brim on his cap line; greens to tan felt, the band dark leather, the buckle tan, outlines kept
  (`seafolk.witch_hat`; `assets/npc_survey/fisher_walker_hat_v4.png`, MonoMyth's witch above for comparison).
  The brim set on the hat's last full-width row (it had been set on the row below, where the brim's tips droop past
  the face with hair between them, and the cleared cap left a gap under the brim: user "you got a weird gap here").
- **The seafolk approved, fronts and walkers (user 2026-11-26: "All the front and overworld sprites from your first
  three look great now").**
- **Women walkers v1** (`tools/npc/walkers/women.py`, `assets/npc_survey/women_walkers_v1.png`; MonoMyth's 12-frame
  walkers onto Emerald's 9: frames 0, 1, 2, 4, 5, 6, 7, 8, 9): **the witch** on MonoMyth 87 (MonoMyth's own witch),
  the greens the front's moss green, the red hair plum; **the old woman** on MonoMyth 108, the hair white, the skin
  fair, the dress the front's brown with a cream collar, **a felt hat in the gown's brown covering the top of her
  hair** (crown over the hair's top rows, brim at its widest row, a pixel wider each side; set on top of 108's big
  hair it had sat like a small cap) with a rose and a cream-gold flower on the crown, as her front's flowered hat.
- **Witch walker approved (user 2026-11-26: "The witch overworld sprite is perfect now").** Her plum hair, after "the
  back of her purple hair isn't long enough" and "should be more wide like her front battle sprite suggests": a
  12-wide curtain down six rows from the brim on the north frames (strand streaks, uneven tips), a mass down her
  back on the west frames, locks past both shoulders on the south frames. `women_walkers_v3.png`.
- **Old woman walker rebuilt on Fantasma 128** (user 2026-11-26, of the MonoMyth 108 version: "do you think this
  actually looks good ... Come on now"; 108's full-width hair buried her face and no brim could clear it). FA 128 is
  Fantasma's own little old woman (short stooped shape, shoulder hair, clear face). White hair (a touch of grey for
  form), tan shawl with cream lights, brown gown, spectacles removed (lenses to skin, each lens's top row a
  squinting eye), and a wide-brimmed brown hat: crown 8 wide with a dark band carrying a rose and a cream bloom, the
  brim the full 16 px with sagging tips. `women_walkers_v4.png`.
  Then (user: "the hat needs to cover more of the old lady's head"): the hat set down 2 rows, the crown over the
  top of her hair and the brim's lip on her forehead; hair shows only at the sides. `women_walkers_v5.png`.
  **Old woman approved (user 2026-11-26: "the old woman looks perfect now in all ways").**
- **Witch hat all green** (user: "on her front sprite her hat is completely green ... you have a black banner with a
  star emblem"): MonoMyth 87's dark band and yellow star recoloured to the hat's greens on the hat rows only.
  `women_walkers_v6.png`.
- **Merchant and Revenant walkers on their own characters' sprites** (user 2026-11-26: "the merchant's overworld
  sprite is the main male character choice in the post-game of monomyth, and the revenant is your main character
  you play as, the ghost Lorenzo in Fantasma"). `tools/npc/walkers/merchant_revenant.py`,
  `assets/npc_survey/merchant_revenant_walkers_v1.png`.
  - **Merchant on MonoMyth 70** (the post-game hero: wide brown hat, gold band, blue hair, gold coat): hat dark teal
    with a red band, hair chestnut, coat teal, trousers brown, tie and boots dark teal, as the recoloured front.
    MonoMyth 70 had been pencilled in for the farmer; the farmer needs another base.
  - **Revenant on Fantasma 545 = Lorenzo.** Fantasma's player sets share palette tag 4409 (entries 537-545: walk,
    run, bike, fishing...); 545 is the plain walk set. Its frames are 32x32 with the figure in columns 9-22, so the
    walker is columns 8-23 of each. Recoloured to the front's icy ramp: bone-blue face with dark sockets over the red
    eyes and a dark nose, navy-black hair and coat, the strap a dark fold, the misty legs icy blue.
  - **Revenant walker approved (user 2026-11-26: "the revenant looks great").** Merchant kept on MonoMyth 70 (user:
    "I'll take your word for it"; 70 is the gold-coat hero's only walk set: his 201 poses share the colours).
  - Finding a Fantasma walker by its front: rank the walker palettes by how many of the front's colours they
    contain (Lorenzo's tag came top), then read that tag's entries.  `assets/npc_survey/fisher_walker_hat_v3.png`.
- **Walkers for the last seven classes** (user 2026-11-26, on `walker_bases_v1.png`; walkers match the RECOLOURED
  fronts, user's choice). `tools/npc/walkers/townsfolk.py`, `assets/npc_survey/townsfolk_walkers_v1.png`.
  - **Old man on Fantasma 133**, the suit and trousers the front's green tweed, the watch gold, shoes brown (user: "if
    you're going to use Fantasma 133 ... recolor the overworld's shirt color to match his battle sprite").
  - **Farmer on Fantasma 262** (wide hat, beard, overalls; user of 212: "does not match the battle sprite at all"):
    hat straw, skin fair, beard brown, overalls green-grey wool, boots brown.
  - **Templar priest on Fantasma 231**, robe white, the Order's blue at the stole, the **lower robe gold** (user:
    "make sure the old man's pants area is gold like the front sprite"). His **front gets the gold lower robe too**
    (recolour.py: skirt slot 10 gold, its shading from row 37 onto the orb's gold slot 12).
  - **Adventurer on Fantasma 142**: hat tan with a red band, vest and hose red, linen under the vest, boots brown.
  - **Labourer renamed Woodsman** (user). On **MonoMyth 7** (spiky red hair; MonoMyth 179, a bald man in glasses, was
    wrong): hair and a drawn-in beard in the front's russet, vest dark leather, linen at the shoulders, trousers
    slate, boots dark.
  - **Minstrel on MonoMyth 0** (green turban with a white band, moustache, red coat: the front's own character; the
    pencilled MonoMyth 199 turned out a faceless hooded figure): turban teal, coat mustard.
  - **MonoMyth 30 is the Imperial Soldier** (user: "That's an Imperial Soldier...or an Officer if you think that
    sounds better"; spear and furs read rank-and-file, leaving "Officer" for a more decorated design later). On
    **MonoMyth 138** (the same white-haired warrior): hair black, uniform purple, fur gold.
  - **Fantasma 133 and 142 have no stepping frames**: their image tables are per-frame {data, size} and entries 3-8
    point back at the three standing frames. `fa_walker.py` now reads that format entry by entry (it had read them
    as one sheet and picked up other walkers' frames); the sheet format is told apart by the flag in its size word
    (0x10100). Earlier walkers re-extract byte-identical.
  - **Stepping frames drawn for the old man and the Adventurer** (user: "they must have some kind of walking
    animation ... they walk up to you before the trainer fight starts"). `townsfolk.add_steps`, after Fantasma's
    own stepping walkers (262, 231): the figure drops a row; south/north, one foot's half of the bottom three rows
    steps a column inward and the other lifts behind the hem (the two frames mirror images); west, the front foot
    a column forward and the back foot a column back, then the front foot lifted a row.
    `townsfolk_walkers_v2.png`, `steps_walk_v1.gif`.
- **Classes still missing (2026-11-26, checked against the approved cast list and Pelluca's object events):**
  Marauder; commoner man and woman (Pelluca's Man 1/3, Woman 1-5); children / Academy students (School Kid, Lass,
  Youngster, Boy, Tuber); innkeeper / cook (2 Cooks); nobleman / lord; nun; hunter / ranger; Beads cultists. Mocked,
  never signed off: the Dowager, the Sword Cult Cardinal and acolytes. Approved, not installed: the noble boy. Plan:
  finish these before the one-pass install.
- **Marauders** (user 2026-11-26: "we'll call them Marauders instead of Brigands as the new class. They're like
  pillagers and thieves that rob and steal from travellers and they form gangs on occasion to invade towns"; bible
  20 §16.6 item 8). Front candidates v1 (`tools/npc/marauder/cands.py`, `assets/npc_survey/marauder_cands_v1.png`):
  MonoMyth 39, 6, 37, 112, 91, 79, 138; Fantasma 55, 168, 181, 8, 151; female MonoMyth 38, 123, Fantasma 26, 95,
  113. Crown's fronts are not in it (its front table is dummied; they need capturing in the emulator).
- **Marauder picks (user 2026-11-26):** the bald thug (MonoMyth 91), the black-clad rogue (Fantasma 113) and the bald
  brute (Fantasma 151; "get rid of his bike, center him and give him a little hair and more medieval clothing"), as
  **Marauder Goon (male and female) and Marauder Chief**. v1 (`tools/npc/marauder/fronts.py`, `walkers.py`;
  `assets/npc_survey/marauder_fronts_v1.png`, `marauder_walkers_v1.png`). The gang's one shared mark is **oxblood**
  (purple is the Empire's). Goon M: tank top to undyed linen, camo trousers to brown leather, the camo face cloth
  oxblood; walker **MonoMyth 123** (the same masked bald thug). Goon F: purple top and gloves and the hair streak
  oxblood, the belt brass; walker **Fantasma 412** (her own: long black hair, pink-purple top). Chief: the motorcycle
  cut away (everything left of x 19, its handlebar and engine where they meet him, floating outline swept, the cut
  edge of his legs closed), centred (shifted 9 px), a short dark crop over the crown and temples (the scalp shine
  with it; slot 7 freed by folding its few fur and buckle pixels into 6 and 5), jeans and wristbands oxblood wool and
  leather, the leather vest, fur collar and black shirt kept; walker **Fantasma 227** (a big short-haired brute; the
  biker has no walker of his own), with the front's grey fur collar at the vest's top edge.
- **Chief: two more bike remnants removed** (user: "this thing on the Marauder Chief between his legs is a remnant of
  the bike you supposedly removed"): the seat and engine block between his knees (rows 46-53) and the tyre's bottom
  (row 56) cleared, the inner edges of his legs outlined; the bike's mirror behind his right shoulder (rows 3-6) too.
  Then (user: "what are these things behind his legs sticking out?") the bike's lower frame and tyre stub behind his
  shins (rows 52-56): blue there not joined to either leg's own trouser pixels (flooded from each thigh) cleared,
  the bar's outline swept, the shins outlined.
  `marauder_fronts_v2.png`.
- **Class names are 12 characters at most** (`struct TrainerClass` name[13]): "Marauder Goon" (13) and "Marauder
  Chief" (14) did not fit. **Decided (user 2026-11-26): the male goon is a "Goon", the female one a "Bandit", the
  chief a "Marauder"** (the gang as a whole are still the Marauders). **Eden is unrelated** (user: "Eden has nothing
  to do with these three trainer classes. They are all just bandits who are like the gangsters of Empire-era
  Cormoria, common thugs"): her Brigand class stays as it is.
- **Goon: face cloth charcoal, the oxblood on a sash** (user: "The male goon should be charcoal on a sash"). Front:
  the cloth's two slots charcoal; the belt's band (rows 29-30) and a tail at his right hip oxblood on slot 14 (freed
  by folding the trousers' two near browns into one). Walker: the cloth charcoal, the belt row oxblood.
  `marauder_fronts_v3.png`, `marauder_walkers_v3.png`.
- **Pelluca's townsfolk are walkers only** (2026-11-26): every human object event in Pelluca is a plain NPC
  (`TRAINER_TYPE_NONE`), so commoners, children, students, the cook, barkeep and healer need no fronts. Candidates
  from Fantasma's own townsfolk (`tools/npc/townsfolk/cands.py`, `assets/npc_survey/townsfolk_cands_v1.png`):
  commoner men 113, 150, 156 (alts 115, 155, 268, 270, 102); women 48, 49, 123, 125 (alts 51, 60, 61, 120); children
  36 and 42 (alts 37, 104, 44, 56, 58); Academy students 108-111 (a purple uniform and cap: the Empire's colour);
  cook / barkeep 254-256 (chef's cap); healer 137-140 (a nurse's cap: its cross to be redone). The cooks and healers
  have three frames only (stationary NPCs in Fantasma), which suits a barkeep, cook and healer.
- **Townsfolk one by one (user 2026-11-26: "Lets just do them one by one").** **Commoner woman A = Fantasma 60, pale
  skinned** (user: "a pale skinned version of this one for one of two commoner women variations"): the skin slots
  1-4 on Fantasma's own fair ramp, the long blue hair and rose dress kept. `tools/npc/townsfolk/women.py`,
  `assets/npc_survey/commoner_woman_a_v1.png`. Two commoner-woman variants in all.
  **Commoner woman B = Fantasma 48, darker skinned** (user: "and then a darker skinned version of this one"): red
  hair, green dress and white apron kept, the skin on Fantasma's dark ramp (60's own). `commoner_women_v1.png`.
  **Commoner man A = Fantasma 150, darker skinned** (user: "Darker skinned version of first one here"; two more
  variations to come from the user): spiky brown hair, pale-blue tunic and vest kept, the skin on the dark ramp.
  `tools/npc/townsfolk/men.py`, `commoner_men_v1.png`.
  **Commoner man B = Fantasma 270, fair skinned** (user: "White version of this one"): curly olive-brown hair and rose
  shirt kept, the skin on Fantasma's fair ramp.
  **Commoner man C = Fantasma 104, blonde in grey** (user: "blonde haired version of this guy with grey clothes"):
  hair blonde, tunic and trousers grey, the purple neckerchief (it shared the hair's slots) moved to two unused
  greys so it stays with the clothes; skin kept. Three commoner men in all.
  **Cook = Fantasma 255 with green hair** (user: "For the cook, lets do a greener haired version of this guy"): the
  navy hair slots green; cap, whites and skin kept; three frames (a cook stays at his counter).
  `tools/npc/townsfolk/staff.py`, `staff_v1.png`.
  **Barkeep from MonoMyth's Fort Elderflower tavern** (user: "There's a bartender sprite in the tavern of MonoMyth at
  fort elderflower we could recolor who would be perfect"). The tavern's map header is 0x86B244 (17 objects; our
  Pelluca tavern is built from the same map); MonoMyth graphics ids index the graphics-info pointer table at
  **0x93BF90** (285 entries; id 80 = catalogue 144). Behind the bar counter (y 2, the stools at y 3) stand objects 1-2,
  id 80 = **MonoMyth 144, a bald man in a maroon waistcoat** (the patrons on the stools are id 29 = catalogue 23).
  **Approved green** (user: "green is fine for him"): waistcoat and trousers forest green (slots 10, 12), and their
  darkest shade, which was the skin's outline brown (1), moved below the face to a free slot (13) in a darker green
  so no maroon is left. `staff_v3.png`.
  **Hair added** (user: "can we give him some hair too"): brown hair over his bald crown on free slots 14/15 (his side
  tufts, slot 6, in the same brown): south the crown, temples and sideburns; north the whole back of the head to the
  nape; west the crown and the back of the head behind the ear. `staff_v4.png`.
  **Clothes bronze** (user: "looks nice. Maybe make his clothing colors bronze instead to distinguish him more"):
  waistcoat and trousers bronze (184,128,64 / 144,96,46 / 104,64,30); his hair taken a shade darker so it stays
  apart from the bronze. `staff_v5.png`.
- **Children: MonoMyth 192, 94, 134, 50, 193** (user: "These kids are all great, just change all their hair colors
  and clothes colors to new ones"; candidates `children_cands_v1.png`). `tools/npc/townsfolk/kids.py`,
  `assets/npc_survey/kids_v1.png`; skin kept on all; slots shared by hair and clothes split by row:
  A (192) chestnut hair, pale-blue shirt, mustard tie, dark green shorts; B (94) auburn hair, navy dress, light-blue
  skirt, gold trim; C (134) black hair, green tunic, cream, maroon trim; D (50) ginger hair, mustard smock; E (193)
  light brown hair, blue dress.
  **Kid D (MonoMyth 50) floats in a swim ring** (user: "this kid is a kid who floats in the water, so we can't use him
  in town"): water only (a swimmer on a route or the bay); Pelluca's harbour Tuber will be one of the land kids (A, B,
  C or E) in the recast table.
- **Dorm student A = MonoMyth 29 with deeper gold hair** (user: "use this kid as a dorm student, just make his hair a
  deeper gold"). His hair's lightest tone was also his skin's light (slot 10): the hair's share moved to slot 6 by
  facing (crown on every frame, the back of the head north and west), then the hair ramp deepened.
  `tools/npc/townsfolk/students.py`, `assets/npc_survey/students_v1.png`.
  **Dorm students B and C = Crown 52 and 58, as they are** (user: "i like these guys as students"): Crown 52 a red
  feathered beret and red-and-gold doublet, Crown 58 orange hair and purple plaid. New `tools/npc/cr_walker.py` reads
  Crown's walkers (main table 0x839FDB0, palettes by tag from 0x9BCB4FC; per-frame raw 4bpp, Emerald's 9 frames).
  **Student D = MonoMyth 173 with dark blue hair** (user: "the third blonde one needs to be dark blue haired to be
  more interesting"): his hair's two darker tones were also his coat's gold trim; the trim (any 1/3 below the head not
  joined to the light hair through hair tones, so the hair's tail down his back stays hair) moves to slot 15 (it
  duplicated 6's navy) and keeps its gold; the hair goes dark blue. `students_v2.png`.
  **Student D is Logan Orphel** (user: "the blue haired one actually is the youngest teacher at the academy and one of
  Cadmus's first top honor student graduates at the academy, a guy named Logan, the last son of the minor noble family
  of Orphel"): not a student; his walker is renamed `logan` (bible 20 §16.6 item 9). The dorm's three students are
  A (MonoMyth 29), B (Crown 52) and C (Crown 58).
  **Logan's placement and quest** (user 2026-11-26): in Chapter 1 he stands at the front of the Academy classroom
  (`PellucaAcademyClassroom`) teaching a few students; a recurring quiz-and-battle mini-quest (three fights: on
  meeting him, after the 4th Trial, before the League; rewards Leftovers, Loaded Dice, then 33 Full Restores and
  33 Max Elixirs, each for all answers right and a win with no faints and no items). Recorded in bible 20 §16.6
  item 9. Trainer class: open.
  **Logan's battle front = MonoMyth's post-game Monty** (user: "It should be post-game Monty from monomyth (your male
  rival). You'll just need to make his battle sprite the appropriate blue color you just updated the overworld sprite
  to"): MonoMyth fronts 98 and 99 (the older Monty standing; 100/101 throw a ball). `tools/npc/logan/logan.py`,
  `assets/npc_survey/logan_front_v1.png`: his hair (crown, the long hair behind, on 98 the shoulder strands; never the
  gold sash, tassels or boots) in the walker's dark blue; shirt stripes, headband, skin and boots kept. Two slots are
  shared with his trousers' blues, so on 99 (arms crossed, hair over his legs) the hair and trousers sit close; 98
  keeps them apart. **Correction (user: "its this one"): post-game Monty is MonoMyth front 114** (blond ponytail, blue
  coat, orange sash), not 98-101 (my guess by the headband; MonoMyth's trainer data does not name the rival, so it
  could not be checked there). Logan's front = 114 with the hair (7, 10 and the hair's brown outline, moved to free
  slot 14) in the walker's dark blue; coat, sash and skin kept. `logan_front_v2.png`, `tools/npc/logan/out/
  logan_front.png`.
  **Scholar Logan** (user: "Scholar Logan is good. I think you need to change their clothes color on both overworld
  and front battle sprite to an orange and light grey mix and flip the front battle sprite horizontally"): class
  **Scholar**; front: coat and trousers light grey, the orange sash and V trim warmed, flipped; walker: the navy coat
  and trousers light grey, the gold trim orange. `logan_front_v3.png`, `students_v3.png`.
  **Front reworked from a gi to a tunic** (user: "make it so it looks less like a karate suit and more like a tunic on
  the battle front sprite"): the crossed lapels (the orange V) gone to plain cloth; the tied sash and its hanging tails
  replaced by a straight leather belt with an orange buckle; the tunic runs to mid-thigh, hemmed in orange; brown
  trousers below. `tools/npc/logan/logan.py` `tunic()`, `logan_front_v4.png`.
  **Belt and trousers fixed** (user: "His pants are weirdly two tone now and the belt isn't correct looking. Go study
  other belts on characters in crown and monomyth"): studied the belts on MonoMyth 30 and 37 and Fantasma 55 (Crown's
  fronts can't be read from its ROM: its front table is dummied). They are a dark leather band two pixels deep, the
  cloth meeting it plainly above and below, with a small metal buckle round a dark centre. Logan's belt now: rows
  34-35 near-black across the waist, a 3x4 orange-gold buckle frame with a dark centre. Trousers on one close brown
  ramp (light on 5, the mid and dark together on 15) instead of MonoMyth's wrinkle pattern in two far-apart browns;
  the gi's brown fold shading on his chest taken to the cloth's grey shade. `logan_front_v5.png`.
  Then (user: "The pants are not supposed to be two toned at all. look at your original And again....what is this"):
  the trousers back to the tunic's light grey, one colour head to foot as in the grey version; and the U of dark
  lines in the middle of the tunic skirt, the outline of the gi sash's hanging tails, left when only the tails' colours
  had been removed, taken out too (rows 37-44, x 26-33, all to plain cloth). `logan_front_v6.png`.
  The orange hem line across his thighs removed (user: "why did you draw a line here????"): with the trousers the
  tunic's grey it was a stray stripe. `logan_front_v7.png`.
  The flat patch where the sash tails had been (rows 37-44, x 26-33) given the cloth's own fold texture (user: "That
  grey block thing you have here looks super unnatural. Make it textured properly like the rest of the tunic"): one-
  pixel diagonal strokes of light, shade and crease like the cloth round it, drawing down into the crease above the
  crotch. `logan_front_v8.png`.
  **Logan's front approved** (user 2026-11-26: "much better. commit it").
- **Tavern healer = Fantasma 125 in light pink** (user: "I like this one for the healer. Make her clothing a light pink
  color"; candidates `healer_cands_v1.png`): bonnet and dress light pink, the shawl a deeper rose; apron, hair and skin
  kept. `tools/npc/townsfolk/staff.py`, `staff_v6.png`. With her, every Pelluca NPC has its new walker.
- **Youth candidates across all four games** (user 2026-11-26: "find me more young men/women/kids across Crown and the
  rest of the games"): `tools/npc/townsfolk/youth_cands.py`, `assets/npc_survey/youth_cands_v1.png` (south frames;
  MonoMyth 57, Fantasma 30, Crown 29, Odyssey 47). Crown and Odyssey are in FireRed's smaller style.

