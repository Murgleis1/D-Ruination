<!-- This file is a split-section view derived from dreamstone_ruination_bible_v0.9.7.md (the canonical full bible at the repo root). Lines below correspond to the source lines noted in INDEX.md. Edit the canonical file and regenerate splits — do not edit splits directly. -->

## 16. Chapter 1 Build Plan `[v0.9.11]`

### 16.1 Purpose

This section is the **buildable blueprint** for Chapter 1 and the Pelluca Valley map — consolidating design that had lived only in working conversation so it is safely recorded and can be built against. It covers the Chapter-1 playthrough (beat by beat), the Pelluca Valley build spec (all map layers), the portrait dialogue system, the new Chapter-1 mechanics, and the committed sprite-asset inventory. It cross-references existing sections. **Where this section introduces NEW canon or flags an unconfirmed item, it says so explicitly** — several Chapter-1 details are new design or need confirmation against the older canon.

### 16.2 Chapter 1 — playthrough spec

Chapter 1 is the **western arm**: start → Route 11 → Hollow Hill → Mirroh → Necropolis (Trial 1) → Mt. Mirroh Peak. It ends with the first **Dreamstone Fragment** recovery and the player's first contact with both the Sword and Beads cults.

**Beat 1 — Cold open.** The masked prince's overworld sprite stands alone in darkness, looking down at his masked reflection in dark water (music: *How Distant Your Heart*, 4:03). Below, a letter from **Cadmus Umbra, Vizier of Education**: he recalls the Prince from the front, references frustration with **Boran Surge** and the Sevii-campaign injuries, notes the discharge at rank **Rainhawk**, hints at a "true destiny," and closes "burn this letter — there are eyes everywhere" plus a request to sign a reply with his true name. The player then composes a short reply and **signs** — a *diegetic* name prompt (default **Osrid**, editable). Screen fades; Pelluca Valley music comes up; Osrid stands on the southern **dock** with a ship behind him; Umbra meets him and takes him to the secret laboratory (staircase behind stone pillars by the estate). Uses the **portrait system** (§16.4): Umbra's portrait toggles **neutral ↔ smile** through the letter, then switches to **Osrid's masked portrait** for his reply.
- *Canon:* Rainhawk = the "grooming rank" for future nobility/Barons (§4); **Boran Surge "Windshear"** is Osrid's combat *mentor*, minor noble of House Surge (§7); the campaign is the Kanto-Johto-Hoenn war, Sevii lost to Kanto (§4).
- *Optional, NOT locked (design intent only):* reflection ripple at the moment of signing; the letter visibly burns to ash after signing; the shot bookends with the Veddev/Eden ending. Keep or drop per the game's layered-depth philosophy.

**Beat 2 — Starter selection (Umbra's lab).** Three Poké-Ball-like objects on the table. Umbra explains the unfolding situation and gives a starter. Starters (§5): **Frigibax** (Dragon/Ice → Baxcalibur), **Teddiursa** (Blue Moon → Bloodmoon Ursaluna, Normal → Normal/Ground), **Tinkatink** (Fairy/Steel → Tinkaton).

**Beat 3 — Eden theft.** **Eden** steals the starter mechanically strongest against the player's choice (type-counter table, §5/§6). She plays a self-interested rogue; the stolen starter becomes her **permanent partner** for the whole game and the post-game marriage (§8, `[LOCKED v0.9.7]`). Explicit Silver/Crystal homage.

**Beat 4 — Pelluca sandbox (three OPTIONAL sidequests, before Route 11).** Umbra gives permission to explore. NPC chatter, flavor, wild grass, and three sidequests that double as a town tutorial. All three share one shape — *NPC → search the valley → confrontation → choice-reward*, and lean on the shiny-tease mechanic (§16.5) — so one script scaffold serves all three:
1. **The Burglar Egg.** An old man blocking the **Tavern** (the empire-era Pokémon Center; §4) reports a burglar on a robbery spree who stole his money and house key but *not* the three Pokémon eggs he nurtures under Vizier Umbra's orders. Track the burglar across town → beat him → key item **Burglar Loot** → return → choose 1 of 3 eggs. The egg is a **shiny-tease Dark-type** (random **Impidimp / Sandile / Galarian Zigzagoon**), giving early Dark options otherwise scarce. **NOTE:** this is DISTINCT from the **Joustroll egg** (the third Umbra egg sealed in the deep cavern — that is the *Trial-4* sidequest, §6/§9). Pelluca's deep cavern exists in Ch.1 but its quest is Trial-4-gated.
2. **Underground Ice Path.** At the Arceus church, a **Templar** reports a foundation crack that opened an underground ice cave. Descend → **crack-tile ice puzzle** (each tile cracks on first step; a second step blacks out and resets to the start) → a half-thawed Arceus statue with key item **Sparkling Opal**. The Templar hails it as **pre-imperial evidence of Arceus worship** — the Order's standing goal (§16.6) — and reports the player to the Archbishop (**Ambrose Caymen**). Reward: choice of **Never-Melt Ice / Metal Coat / Soft Sand** (aligned to the three starters' types; confirm the exact mapping, esp. Soft Sand → the Bloodmoon Ursaluna Ground side).
3. **The Fisherman's Dilemma.** A fisherman at the south dock says he hooked a rare Water-type that overpowered him and fled into town. Find it in **three hiding spots** (the DM Skitty-quest pattern); on the third it turns to fight → shiny-tease prompt → **Lv.12 Wimpod**, catch or defeat. Custom Wimpod moveset (**Aqua Jet / Bug Bite / Trailblaze**). See §16.5 for the tied **Golisopod Tough-Claws** viability change.

**Beat 5 — Route 11 hook (the plot beat).** Heading past Route 11 toward Hollow Hill, the player sees a **Sword Cultist and a Beads Cultist fighting over a stolen shiny Eiscue** — just taken from a young female Templar knight-priest, **Loulan** (§16.6), who was traveling toward Pelluca. The Eiscue bolts toward Hollow Hill and the cultists chase it. Loulan asks the player to retrieve it. This single scene introduces **both cults and their mutual enmity** (canon: Sword and Beads hate each other) before either is a solo threat — show, don't tell.

**Beat 6 — Hollow Hill.** Retrieve the Eiscue → the player's **first double battle (1v2)** against both cultists, furious at the interference. Reward: choice of **Metronome OR Quick Claw** (the un-chosen one is buyable post-Trial-9 from a Victory Cape merchant — a scarcity-with-safety-valve choice; add that vendor to the Victory Cape atlas entry). *Hollow Hill canon (§1/§15):* the forgotten site where Cormor erased Phancero and the Treasures were corrupted — cursed, Ghost-drawing. **OPEN:** the 1v2 is pre-Trial-1 and inherently hard — tune it (cultists weakened from fighting each other? Loulan assists? scripted help?) so it's a spike, not a wall.

**Beat 7 — Mirroh + Necropolis (Trial 1).** The haunted city, then the Mirroh Necropolis. **Trial 1: Kimaris Langerin** (Ghost; **Wraith** badge; level cap **18**). Team (`[LOCKED v0.9.8]`): **Crowley** (shiny Spiritomb, Prankster) + Dusclops + Shedinja + Honedge + Gastly + Dhelmise — a Curse-stall wall; Fire/Fairy coverage helps. Kimaris = **Reserve Champion**, Cadmus's lifelong dearest friend, Templar consultant (§3/§7). His true Marshadow-led team is a *post-Champion* fight, not this one.

**Beat 8 — Mt. Mirroh Peak (chapter climax).** First **Sword Cult** contact (hunting Dreamstone fragments), first **Baradus** encounter — his Pokémon demolishes the underleveled player. **NEEDS-CONFIRMATION:** Baradus's canonical aces are **Guzzlord** and **Shardik** (shiny Beartic, Tough Claws) (§12); the earlier "Crabominable" reference for this fight appears to be an error — confirm the actual Ch.1 encounter mon (likely a cult mon or Beartic). Then the player's **first slip into Ancient Cormoria** — a scripted set-piece, the single Ancient-Cormoria area in Ch.1 (scope: small scripted zone). **Kimaris pulls Osrid back** to the present (*from design discussion — confirm*). Recover the **first Dreamstone Fragment**. Chapter close.

### 16.3 Pelluca Valley — build spec

Base decision (§15): **expand and re-skin DM's Pelluca City** into the grander empire-era **Pelluca Valley**, keeping DM's coastal/flooded footprint as the continuity anchor, adding the Umbra estate/academy, the deep cavern, the seaside docks, and the four nexus exits. A pokeemerald town is ~eight layers; this is the checklist:

1. **Tileset** — the **Evernahn conversion** (32px-RMXP → 16px-metatile correspondence + palette fit; §18). **Prerequisite** — nothing gets placed until the tiles exist in-engine.
2. **Outdoor layout** — the four-arm nexus (§15): N Ivy River, W Route 11 → Mirroh, E Hoya Delta, S Route 10 → Rivetshore; plus Umbra estate + Academy + secret lab, the deep-cavern entrance, seaside docks (the cold-open dock; fishing-village character), a Tavern, the Arceus church, houses/shops.
3. **Connections** — the four directional exits, stubbed until those routes are built.
4. **Interiors** (each its own map): Umbra estate + secret lab (starter scene), the Tavern, the Arceus church (+ the underground ice-path sub-map), the deep cavern (Joustroll egg — Trial-4-gated), houses/shops. *Interior list to finalize.*
5. **NPCs (object events)** — quest-givers (the old man/burglar, the church Templar, the fisherman, Loulan) + flavor NPCs. Each needs an overworld sprite (user-provided) and dialogue. *Roster to build.*
6. **Scripts (poryscript)** — cold open, starter selection, Eden theft, the three sidequests, the Route-11/Eiscue hook, the Hollow Hill 1v2.
7. **Wild encounters** — Pelluca grass tables + the three Wimpod hiding spots. *Table to define.*
8. **Metadata** — name (Pelluca Valley), MAPSEC, music, weather, map type.

**First concrete build step (recommended):** extract and render DM's *actual* Pelluca City (its real layout, NPCs, warps) so the expansion works from the true starting map, not memory.

### 16.4 Portrait dialogue system — engineering spec `[NEW feature]`

Opt-in per character (the Pokémon Empire model): **dialogue is portrait-less by default** (ordinary Pokémon textbox). Only a line explicitly tagged with a *registered* character + expression shows a framed **portrait window** to the left of the box, matching the textbox theme.
- **Portrait registry:** character ID → portrait art + expression set (committed portraits: Osrid masked; Cadmus neutral + smile; Eden). Only cast members who "earn" a portrait are registered; all other NPC dialogue is untouched.
- **Per-line tag:** portrait ID + expression, supporting mid-sequence **expression swaps** (Umbra neutral ↔ smile) and **speaker swaps** (Umbra → Osrid).
- **First use case:** the cold open (§16.2 Beat 1).
- **Implementation:** C against the codebase (portrait-window draw + a message/script tag + registry lookup + load from `graphics/portraits/`). This is engine code, **verifiable against source** — the reliable lane. Add as an §18 engineering task.

### 16.5 New Chapter-1 mechanics `[NEW — flagged additions]`

1. **Shiny-decision ("shiny-tease") mechanic.** At certain scripted encounters/eggs the game asks whether the Pokémon "seems oddly colored / is it shining, or a trick of the light?" *before* the reveal; answer yes → guaranteed shiny, no → normal. A recurring signature used by the **Burglar Egg**, the **Fisherman's Wimpod**, and (later) the **Trial-4 Joustroll egg**. Spec once, reuse.
2. **Golisopod viability buff.** Golisopod gains **Tough Claws as a Hidden Ability** (in addition to / replacing Emergency Exit). *Rationale (record so it is not "fixed" back):* Emergency Exit is anti-fun on a slow bulky attacker; Tough Claws (boosting First Impression / Close Combat / Aqua Jet / Liquidation) keeps the Lv.30 Wimpod→Golisopod power spike a worthwhile all-game investment. Wimpod also gets a custom Lv.12 kit (Aqua Jet / Bug Bite / Trailblaze) so the pre-evolution grind isn't dead weight. Add to §18 engineering.
3. **Crack-tile ice puzzle.** The underground ice path: each floor tile cracks on first step; stepping on an already-cracked tile blacks the screen and resets the room to the entrance (a memory/pathing puzzle, distinct from momentum ice-sliding). Custom map script.

### 16.6 New / updated canon `[NEW — flagged additions]`

1. **Templar Arceus Order — standing organizational goal** (addition to §4): beyond maintaining Arceus's civic presence (Taverns, Braviary travel, religious infrastructure), the Order actively seeks **proof that pre-Cormorian peoples worshipped Arceus *before* Cormor founded the Empire** — hunting old ruins and artifacts for validation of their faith. Motivates the ice-path quest (the Sparkling Opal reads as *pre-imperial evidence*, which is why it's reported to the Archbishop). Consistent with the pre-Cormorian nomadic cosmology and the Blue Moon Hermit as "the last of the pre-Cormorian tribe" (§1/§7).
2. **Loulan** (minor NPC, addition to §7): a young female **Templar knight-priest** with a shiny **Eiscue** overworld partner. Chapter-1 questgiver (the Route-11 Eiscue-retrieval hook); recurs minorly at **Templar Headquarters** with the Eiscue and has minor involvement around the **Ambrose Caymen** fight. Not a major character — this single entry exists so she is canon and not accidentally re-invented or contradicted.

### 16.7 Sprite-asset inventory (committed to the repo)

- **Osrid** — `trainers/front_pics/osrid.png` (64×64 indexed), `object_events/pics/people/osrid.png` (144×32 overworld, 9-frame), `trainers/back_pics/osrid.png` (64×64 battle back), `portraits/osrid.png` (96×96 masked). All engine-format. Unmasked portrait = a *future* post-Champion reveal only.
- **Cadmus** — `trainers/front_pics/cadmus.png` (64×64 indexed; narrow in-frame — optional reframe later), `object_events/pics/people/cadmus_ow_essentials.png` (128×192 recolored **source** — needs 16×32/144×32 conversion), `portraits/cadmus_neutral.png` + `cadmus_smile.png` (96×96).
- **Eden** — `trainers/front_pics/eden.png` (64×64 indexed), `object_events/pics/people/eden_ow_essentials.png` (128×192 **source** — needs conversion), `portraits/eden.png` (96×96).
- **Pending for all:** the two overworld **sources** need the 32×48 → 16×32/144×32 conversion (best verified in-engine); front pics need build-generated compiled forms; everything needs **wiring into the object-event graphics + trainer-pic tables**; and the **portrait system (§16.4)** must be built for the portraits to be used.
- **Division that works (established this cycle):** the user provides base art + does pixel-precision edits (masks, hair/silhouette shaping); the assistant does deterministic recolor/format/index/commit and the engine-code (portrait system, wiring). Blind pixel-editing of small sprites is the assistant's weak spot; palette/format/code work is reliable.

### 16.8 Open items / needs-confirmation

- **Baradus's Ch.1 (Mt. Mirroh Peak) encounter Pokémon** — canonical aces are Guzzlord + Shardik (Beartic); "Crabominable" is likely an error. Confirm.
- **Kimaris's rescue at the Peak** — from design discussion; confirm as canon.
- **Hollow Hill 1v2 tuning** — assisted vs. hard wall.
- **Ice-path reward mapping** — which item aligns to which starter (esp. Soft Sand ↔ Ursaluna's Ground side).
- **Trial 3 (Rivetshore) + Trial 4 (Sylphon seat)** placements — still `[PROPOSED]`/`[OPEN]` in §15.
- **Pelluca build decisions (§16.3):** layout size, which DM-Pelluca elements to keep vs. cut, the full interior list, the NPC roster, and the wild-encounter table.
- **Cold-open optional flourishes** — reflection ripple, letter-burn, ending bookend: pick or drop.
