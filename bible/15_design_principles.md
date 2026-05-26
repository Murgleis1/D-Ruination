<!-- This file is a split-section view derived from dreamstone_ruination_bible_v0.9.7.md (the canonical full bible at the repo root). Lines below correspond to the source lines noted in INDEX.md. Edit the canonical file and regenerate splits — do not edit splits directly. -->

## 11. Design Principles (Carried Forward from Dreamstone Mysteries)

These are the design DNA of Dreamstone Mysteries that we are carrying into Dreamstone Ruination — and in most cases, *expanding*. Each principle has been verified in the DM codebase (specific files cited). When designing any feature for Ruination, consult this section: if a proposed feature *violates* one of these principles, we must consciously decide whether it's a deliberate departure or a mistake.

### Principle 1 — Living-World NPCs with Characterized Pokémon `[LOCKED]`

**What it is:** In Dreamstone Mysteries, NPC Pokémon are characterized as *individuals with internal states* — desires, moods, relationships with their trainers. The dialogue treats them as characters, not possessions.

**Verified examples from DM source:**
- `PellucaCity/scripts.pory:1104`: Lycanroc howling, "It must be pining for a table at the restaurant!"
- `PellucaCity/scripts.pory:1175`: Sealeo wanting to catch fish
- `CeramBaseCamp/scripts.pory:347`: Bergmite says hello ("keee!!!") and the dialogue replies in character
- `FennilahlTown/scripts.pory:97`: Breech the hiker *adopts Clefairy as a "hiking partner"* — explicitly framed as friendship, not capture. Later at Galecrest's Detective Academy, Clefairy *itself* gives the player an item and the player thanks Clefairy directly.

**The underlying design intent:** the player builds a relationship with the world through *observation*, not just battle. Every Pokémon is potentially someone's friend, partner, or character. This quietly reinforces the **Pokémon-as-partners-not-weapons** thesis at the world-default level. Trainers in Cormorian culture treat their Pokémon as companions; that becomes the universe's *normal*.

**Implementation pattern:** A `playmoncry()` call followed by an `MSGBOX_NPC` line framing the cry as a character moment. Cheap to implement, enormous payoff to atmosphere. Two lines of script for what feels like an entire character.

**Efficiency note:** This is also how DM avoids writing every NPC's full backstory. A single "Lycanroc is howling. It must be pining for a table at the restaurant!" tells you about the trainer, the Pokémon, the restaurant, and the city in fifteen words. *Efficient worldbuilding through character vignettes.*

**Ruination's extension:**
- Cities will be *significantly expanded* in our era (empire-era, larger and more developed)
- The per-city NPC density and characterized-Pokémon density should *scale up proportionally*
- We deliberately preserve a sense of nostalgia and familiarity for DM players — when they walk through Mt. Ceram or Vilethorn Woods in our era, they should recognize the shape of the place even though it's older, more populous, and more developed
- The thesis statement we are trying to embody: *"even after 2000 years, some things actually don't change much...and it's a beautiful thing"*

### Principle 2 — Permanent Consequential Choice and Scarcity `[LOCKED]`

**What it is:** Throughout Dreamstone Mysteries, the player is forced to pick "one" thing at the expense of another, *with no way back*. No loopholes, no alternate paths to acquire the unpicked option.

**Verified examples from DM source:**
- Starter selection (Gothita / Timburr / Galarian Zigzagoon) — the two not picked are not catchable in the wild anywhere in the game
- `CeramBaseCamp/scripts.pory:245-263`: The hiker outside the supply store offers a single choice between **King's Rock** and **Quick Claw**. Confirms with `MSGBOX_YESNO`, then sets `FLAG_CERAMBASECAMP_NPCITEM` permanently. Dialogue framing: *"I found these weird trinkets when I went up Mt. Ceram. Do you want one?"* — the **singular "one"** makes scarcity feel natural, not arbitrary.

**The underlying design intent:**
- **Replay value:** a player who chose King's Rock has a *reason* to play again to try Quick Claw
- **Choice feels weighty:** when an item costs another item, the player actually *thinks* about which fits their team
- **Player identity:** "I'm a Tinkatink player" becomes meaningful in a way "I picked Charmander but also have my Bulbasaur" never does
- **Scarcity is narrative-grounded:** "These Pokémon are vanishingly rare in this era" (the starter framing in Umbra's gift scene) is much stronger than arbitrary restriction. The *in-world* explanation makes the player accept the constraint as part of the setting.

**Tensions to be deliberate about:**
- *Choices must be informed.* A 12-year-old picking King's Rock vs. Quick Claw blind is just guessing; the choice should make sense once explained. DM mostly does this well; we should too.
- *Choice density matters.* Too many irrevocable choices and players freeze. Aim for *significant choices at significant moments*, not constant micro-choices.
- *Failed choices should not feel like failures.* Both options should be genuinely useful for some team build, so the player feels they made a *trade*, not a *mistake*.

**Ruination's extension:**
- More irrevocable choices, deliberately placed at moments of narrative weight
- Particularly: starter choice (already designed), Move Tutor access (limited and choice-driven), Mega Stone acquisition timing (Baxcaliburite vs. other rewards), possibly some Trial House loyalty interactions where helping one House costs you a relationship with another

### Principle 1+2 Exemplar — The Crabominable Adoption Mechanic `[LOCKED]`

The **Crabominable adoption mechanic** (Section 8 — Baradus profile, Section 9 — mechanics) is the cleanest single design moment where Principle 1 (Living-World Pokémon) and Principle 2 (Permanent Consequential Choice) intersect at full power, with the project's central thesis ("Pokémon are partners, not weapons") realized at the level of game mechanics.

**The moment:** After the player defeats Baradus in the mid-game encounter, Baradus fanatically rages that he could lose to a "nameless worthless nobody" and **discards his shiny Crabominable in cruel theatrical fashion**. The player has the optional choice to approach the discarded Pokémon, offer food and water, and befriend it. If the player chooses to befriend, Crabominable joins the party as a shiny, holds a Punching Glove, has perfect IVs and maxed EVs (252 Attack / 129 Defense / 129 Special Defense), and the player can choose its nature, ability, and nickname.

**Why this is the cleanest thesis-instantiation in the project:**
- **Baradus's discard demonstrates the antithesis** ("Pokémon are weapons that can be discarded when they fail") in a single visceral scene
- **The player's compassion embodies the thesis** ("Pokémon are partners; this discarded one deserves to be lifted up") in a single optional gameplay choice
- **The IV/EV mechanic encodes the thesis biologically:** Crabominable's response to the player's compassion brings out its full potential — potential Baradus failed to see because he didn't bond. **Partnership produces what engineering cannot.**
- **The final-battle dialogue triggers** (Section 9) close the irony loop: Baradus mocks the adoption as "refrigerated leftovers," and specific KO dialogue fires if Crabominable defeats Chien-Pao or Beartic (Shardik)

**This is design as thesis demonstration.** Other moments in the project make thematic statements through dialogue or character arcs; this moment makes it through a *gameplay mechanic* the player performs by their own free choice. Players who befriend Crabominable enact the thesis in real-time. Players who walk past have made a different choice that the game *allows* but does not require, preserving Principle 2's choice integrity.

**The deeper thematic layer — overcoming Osrid's conditioning:**

The Crabominable adoption scene is *doubly* charged because of Osrid's character backstory (Section 5). For nearly a decade overseas, **Osrid was mentored by Boran Surge**, a brilliant cold strategist whose philosophy is that *"Pokemon are purely military assets."* This corrupted Osrid's natural kindness — he returns from war with Boran's instrumental view of Pokemon partially internalized.

When the player has the option to approach the discarded Crabominable, **they are not enacting Osrid's default disposition.** Osrid's default disposition, after 10 years of Boran's training, is closer to "leave the broken asset behind and move on." The player's compassion in this moment is *consciously overriding 10 years of conditioning*.

**The act of compassion costs Osrid something internally.** He has to fight his own conditioning to walk over and offer food. The mechanic remains optional precisely because **the choice itself is the character arc happening in real time.** The player is not just choosing for Crabominable's benefit — they are choosing *who Osrid will become* on the other side of this moment. Players who consistently choose compassion across the game are *actively re-civilizing* their protagonist from the Boran-Surge influence; players who don't are leaving Osrid in his post-Boran state.

This is the thesis stated through agency: **partnership is not just what Pokemon deserve, it is what trainers have to choose against their own conditioning to give.** Other characters in the project (Glaive, Eden) demonstrate this through their own arcs of overcoming weapon-thinking. The player gets to do it for themselves, through Osrid, in a single optional scene.

### Principle 3 — Recurring Trainer Arcs `[LOCKED]`

**What it is:** Several DM side trainers — not main rivals — *recur* throughout the game. The same NPC first encountered on an early route shows up again on a mid-game route, then again at the championship. Each appearance, they're significantly stronger. By endgame they're championship-tier opponents.

**Verified example from DM source:** *Stanja the Bug Maniac*. First fought in Vilethorn Woods. Then in Ivy River. Then at `Championship_R2/scripts.pory:40` he's a championship participant with the dialogue: *"I know you. I've lost to you before. We fought in Vilethorn Woods. And then again in the Ivy River. But this battle is different. The stakes are different. I'M different!"* On defeat: *"Good luck, {PLAYER}. You're tough — I'm rooting for you!"* The **grudge-becomes-respect arc** is closed within the dialogue itself.

**The underlying design intent:** route trainers normally feel like *filler*. Recurring them turns the player's whole journey through Cormoria into a web of *relationships with the world's denizens*. Filler becomes story.

**Ruination's extension — The Six Stat-Themed Rivals + The Paragon Gauntlet:**

We introduce **6 recurring side rival trainers**, each thematically organized around maximizing one of Pokémon's core stats. They are *type-agnostic* — their team compositions are diverse, but their training philosophy is unified around a single stat axis.

| # | Stat Axis | Strategic Identity |
|---|---|---|
| 1 | **HP** | Attrition, healing, walls; outlast the opponent |
| 2 | **Attack** | One-or-two-shot KOs with high-attack physical sweepers |
| 3 | **Defense** | Physical tanking; counter-stall the opponent |
| 4 | **Special Attack** | High-SpA sweepers with coverage moves |
| 5 | **Special Defense** | Special tanking; specially-bulky strategies |
| 6 | **Speed** | Outspeed everything; signature ace is a shiny Ninjask (Speed Boost ability) that eventually learns **Bolt Beak + Fishious Rend** (move-first damage doubling), **Obstruct** (protection + defense lowering), and **Leech Life** (recovery). A late-game menace. |

**Design rationale:** stat-themed teams are an *organic in-game tutorial* for competitive battle strategy. By the time the player reaches the gauntlet, they have fought every fundamental stat archetype multiple times with escalating sophistication. They are *competitively literate* through play, not through reading guides.

**The Paragon Gauntlet** — the prerequisite for facing the Viziers:

The Cormorian trainer-merit gate has four tiers:
1. **The 9 Trials** (presided by the 9 noble Trial Houses, monotype each)
2. **The Paragon Gauntlet** — a no-holds-barred tournament restricted to the 6 best trainers who passed the Trials within a year. Six rivals fight in succession. **Limited healing: one healing item between fights**, no Pokémon Center breaks, no full heals.
3. **The 4 Viziers** (Umbra, Glaive-as-Vizier-of-War, Silas Moray, and one more `[OPEN]`)
4. **The Champion** (Rhydia)

The 5 gauntlet rivals besides the player are *the 6 stat-themed trainers, minus one* (whichever one the player has met fewest times, or whatever makes narrative sense — `[OPEN]` exact selection logic). All 6 stat trainers reappear here at their *maximum* power, with full 6-Pokémon teams.

**Departure from DM:** DM's championship gives free healing between rounds via a lobby nurse (`Championship_R1_Lobby/scripts.pory:27`). Our Paragon Gauntlet *removes that healing* — a deliberate harder variant that fits Cormorian imperial meritocracy ("only the most consistent trainer wins").

**Structural elegance:** All six stat-themed rivals appear in the gauntlet at their full power. The player has seen each of them grow across the game. The gauntlet is the *payoff* of the recurring-trainer structure — every previous fight with these rivals was setup for this finale.

**Open questions for the 6 rivals:**
- `[OPEN]` Names and personality identities of all six
- `[OPEN]` Geographic encounter order (which routes / cities do they each first appear on)
- `[OPEN]` Whether any have arc reversals (grudge-to-respect like Stanja vs. friend-to-corrupted)
- `[OPEN]` The exact gauntlet seeding/order

### Principle 4 — One-Way Routes, Drifblim Pass, and HealPass Scarcity `[LOCKED]`

**What it is:** Routes in DM are designed so that once the player enters them, they *cannot manually backtrack* to the previous city. Map tilemaps use hedges, cliffs, drops, or other un-traversable terrain to enforce single-direction movement. The only way to return to earlier cities is via the **Drifblim Pass** (a Fly-equivalent fast-travel system between cities), acquired mid-game. Routes feature occasional **Nurse Joy + Chansey** healing stations that consume one **HealPass** item per use; the HealPass is reissued at Pokemon Centers.

**Verified in DM source:**
- Drifblim Pass acquisition: `PellucaCityHouses/scripts.pory:43-47` — a complimentary tourist-promotion gift. *"Using this, you'll be able to use the Drifblim outside our Pokémon Center to fly to other cities in Cormoria!"* Implemented as `ITEM_DRIFBLIM_TRAVELS_PASS`. The system is even named *Drifblim Travels Pvt. Ltd.* — a delightful flavor detail.
- HealPass mechanic: `TempCopyMap/scripts.pory:548-583` (`Common_EventScript_NurseJoyOnRoute`) consumes the HealPass and triggers `Common_EventScript_OutOfCenterPartyHeal`. Nurse Joys are paired with Chansey NPCs (`Common_EventScript_ChanseyOnRoute`) for the living-world Pokemon flavor.
- HealPass restamp at any Pokemon Center: `data/scripts/pkmn_center_nurse.inc:87-93`, `EventScript_PkmnCenterNurse_ExplainHealPass` and `EventScript_PkmnCenterNurse_GiveHealPass` — the nurse hands out a new HealPass after a full heal.

**The underlying design intent:**
- **Forced commitment to a resource budget.** Whatever potions, repels, status healers, and Pokeballs the player carries when entering a route are *what they have* until reaching the next city. Pokemart shopping becomes *logistics planning*.
- **Encourages slow city engagement.** Players linger in cities — buying excess supplies, talking to NPCs, doing sidequests — exactly the behavior that pays off Principle 1 (living-world NPCs).
- **The HealPass is a one-mistake safety net.** It prevents the design from being unfair (players don't have to grind cautiously), while keeping the route as a real challenge (one mistake per route, no more).
- **The Drifblim Pass is a *milestone reward*** — receiving it transforms the game's movement model. That's a narrative beat the one-way design earns.

**Implementation pattern:** Map tilemap design (hedges, cliffs) does the heavy lifting. Active scripted blockers are used sparingly. This is **important for Ruination's expanded maps** — when we add new areas or expand existing routes, the one-way property must be preserved by terrain design, not by hoping the player obeys NPCs telling them not to backtrack.

**Pacing note:** the Drifblim Pass is acquired in DM at **Pelluca City**, which is roughly mid-game. The Pass's *timing* is critical:
- Too early: the one-way design loses bite, since players can fly back from anywhere
- Too late: players feel trapped, can't complete optional content from earlier areas
- Pelluca City placement seems to land this well; Ruination should target similar pacing

**Ruination's extension:**
- One-way route design is **preserved**. Expansions to existing routes (per Principle 1 — bigger cities and somewhat-expanded routes) must maintain one-way terrain unless we're consciously revising pacing.
- HealPass mechanic preserved exactly as DM implements it. Issued by Pokemon Center nurses (now **Tavern Templars** in our era — Section 4) after a full heal.
- **The Drifblim Pass is replaced by the Templar Arceus Braviary travel system** `[LOCKED]`:
  - **Braviary is the national Pokémon of Cormoria.** The Templar Arceus order in every city carries Braviary as their partner Pokemon.
  - **Player pays a small fee** to the local Templar to be flown to another city. **Fee scales by distance** — closer cities cheaper, distant cities more expensive (realistic empire-era pricing).
  - **Mid-game acquisition milestone** (like DM's Drifblim Pass timing) — `[OPEN — specific gating moment]`. The acquisition transforms the player's movement model.
  - **Religiously grounded, not commercial.** Templars serve Arceus, not a corporation. The system fits empire-era flavor better than a private travel company.
  - **Quietly thematic:** the *honest* national Pokemon (Normal/Flying Braviary) carried by *honest civic servants* (Templars) is the public infrastructure. The *aberrant* form (Psychic/Flying Hisuian Braviary) is carried by the corrupted Vizier of Commerce (Silas's Thauma). Two versions of the national bird; two versions of national service.
  - See Section 9 for full mechanical details and Section 4 for Templar Arceus order details.
- New settlements we introduce in our era (camps, fortresses, embassies, the imperial capital) must each have a clear answer: does this location have a Tavern, and therefore a HealPass restamp + Braviary travel? Or is it a *pure wilderness* location where the player must rely on what they carried in?

### Principle 5 — Eden's Crafty Item-Disruption Battle Style `[LOCKED]`

**What it is:** Eden's signature isn't raw power — it's *disruption*. Her teams are Dark-type oriented and her favorite move is **Knock Off**. Her strategies center on stealing items, swapping bad items into the player's inventory, disabling abilities, and inflicting status conditions.

**The underlying design intent:**
- Every other trainer in the game tests a single stat or type axis. Eden tests **adaptability** — can the player win when their strategy is being actively disrupted? That's a different skill, and her recurring presence forces players to develop it.
- Her battle style is *consistent with her character*. She's a Paldean serf-class thief who learned to win by *taking what others have*. Her early-game theft (your starter) is literal; her mid-game battles are metaphorical theft (your items, abilities, plans); her endgame is *reclaiming what she gave up* (returning to Veddev / her own identity).
- The mechanical layer reflects the character layer. The rival you fight reflects the person she is.

**Move pool examples (illustrative, not exhaustive):** Knock Off, Trick, Switcheroo, Taunt, Gastro Acid, Worry Seed, Toxic, Will-O-Wisp, Embargo, Magic Room, Memento, Parting Shot.

**Ruination implementation note:** Eden's encounters require careful test-play. Disruption strategies can feel *miserable* against an unprepared player — the goal is "this rival is a fascinating puzzle to solve," not "this rival is just frustrating." Each Eden encounter should give the player tools to respond *before* the fight (item slot management, Pokemon with abilities like Sticky Hold, Pokemon with Mental Herb, etc. should become available naturally around when Eden recurs).

### Principle 6 — Glaive's Dragon Affinity (First in Cormorian History, Hidden Psychic Gift) `[LOCKED — CORRECTED]`

**What it is:** Glaive is a traditional rival in his trajectory (childhood friend → rival → ascended Vizier of War). But what makes him *mechanically and thematically* distinctive is twofold:

1. **He is the first trainer in all of Cormorian history who can tame multiple dragons and has a true affinity for them.** Dragons in our era are generally regarded as the most wild and hostile Pokemon type to humans; no family has ever specialized in or mastered them. Glaive is *the founder* of a tradition that doesn't yet exist. His personal anomaly becomes humanity's eventual normal — by DM's era (~2000 years later), dragons are tamed normally enough to have Dragon-type institutions.

2. **His dragon affinity is actually an unrecognized psychic gift.** Glaive does not know this about himself. He has a *dragon-empathic* ability that lets him feel the emotions of dragons and dragon-egg-group Pokémon, and psychically communicate his own emotions to them. Vizier Umbra theorizes about this later in the game but does not tell Glaive directly. Most other characters never learn this truth.

**This is a major correction from earlier bible drafts that framed Glaive as inheriting a "family tradition of Dragon mastery." There is no such tradition; Glaive is inventing dragon mastery from scratch, by trial and error, with the quiet metaphysical help of a gift he doesn't recognize.**

**Team composition philosophy:** Since no Cormorian family before Glaive codified dragon mastery, he has had to *invent* dragon training. He has learned through trial and error that the *dragon spirit* manifests across the **Dragon egg group**, not just the typing. His roster reflects this:

- **Bagon → Shelgon → Salamence (Blackthorn)** — his signature, raised from Bagon and named after the rare mutated shiny Bagon he originally caught. Black-and-crimson Salamence.
- **Sandaconda** — Ground type, Dragon egg group; defensively counters Ice (the canonical Dragon-counter)
- **Gyarados** — Water/Flying, Dragon egg group; Mega Gyarados presents draconically and covers Dragon weaknesses
- **Turtonator** — Fire/Dragon; legitimately a Dragon Pokemon. **Will be buffed significantly in Ruination** (specific stat buff numbers `[OPEN]`).
- **Sceptile** — Grass, Dragon egg group; resists Electric and Ground (Salamence's weaknesses)
- **Heliolisk** — Electric/Normal, Dragon egg group; Special attacker complementing his Physical-leaning core
- **Scrafty** — Dark/Fighting, Dragon egg group; immune to Psychic, resists Dark

**The underlying design intent:** Glaive isn't a "Dragon master who's bad at his typing weaknesses" — he's a **trainer with a metaphysical gift he doesn't know about, who has invented dragon mastery from scratch with that gift's quiet help, and who has compensated for his typing's natural weaknesses through egg-group selection.** The team comp *embodies his character arc*: youth was about strength-as-weapon ("become strong enough to conquer Kanto"); maturity is about depth-of-mastery (understanding the *idea* of dragons through their kin); the deeper truth is that he is *quietly metaphysical* and his bonds with his Pokemon are mediated by an empathic gift his soul has been using without his awareness.

**The thesis statement embedded in Glaive:** real bonds with Pokemon are *quietly metaphysical* even when the trainer doesn't notice. Pokémon-as-partners-not-weapons isn't just a moral stance — it touches something cosmic that even materialistically-minded trainers participate in unconsciously.

**Turtonator buff:** Turtonator is a perpetual underdog (BST 485, great typing and signature move held back by frailty). Buffing it in Ruination both (a) makes Glaive's late fight harder and (b) gives the player a *catchable* version worth using. Glaive's Turtonator should arguably be the version that demonstrates *why* the buff matters — players who fight him then want to use it themselves.

**Frigibax-pick player dialogue:** If the player picked Frigibax, Glaive has extra respectful dialogue acknowledging the Frigibax (a Dragon-egg-group Pokemon) in their party. **Glaive recognizes the Frigibax, not the player themselves.** The player does not share Glaive's psychic gift; Glaive is empathizing with the dragon-egg-group Pokemon in the player's care.

**Open questions for Glaive:**
- `[OPEN]` Specific stat buff numbers for Turtonator
- `[OPEN]` Exact roster progression across the 4-5 Glaive encounters (which Pokemon he brings at which encounter)
- `[OPEN]` His Vizier-of-War final fight roster (which members of the above list, and at what levels)
- `[OPEN]` Whether Mega Gyarados or any other Mega is part of his final fight (gating: state Mega sanction; he has Vizier-of-War authorization)
- `[OPEN]` The specific dialogue beat where Umbra theorizes about Glaive's gift to the player

### Principle 7 — The Rival Hierarchy `[LOCKED — UPDATED v0.9]`

This consolidates Principles 3, 5, and 6 into a single ordering:

- **The 6 stat-themed rivals** are *recurring side rivals*. They appear on routes throughout the game, grow stronger between encounters, and culminate in the Paragon Gauntlet.
- **Eden** is a *main rival* — she has her own arc (thief → cult recruit → defector → ally → spouse) that runs parallel to but separate from the 6 stat rivals.
- **Glaive** is the *primary rival* — childhood friend, the traditional Pokemon-rival role. His arc culminates in the Vizier of War battle, which is the **last gate before Rhydia**.
- **Rhydia** is the *Champion battle* — sister, regent, strongest trainer in generations. **Her relationship with the player is *cooperative-first, then adversarial*** — a deliberate inversion of the standard fan-game rival pattern.

**The Rhydia cooperative-then-adversarial design `[LOCKED]`:**

This is one of the project's most distinctive structural choices:

- **Cooperative phase (Act II, post-Trial 2):** The player and Rhydia fight on the *same side* in the Goma Royal Palace Assassination subplot (Section 10). The player participates in doubles-format scripted battles alongside Rhydia against Beads Cult acolytes and one Bishop. They learn each other's combat styles through *partnership*, not opposition.
- **Identity-reveal phase (~50%):** Rhydia learns that "Rainhawk Alban" is her brother during the joint Sword Cult encounter. The cooperative relationship deepens — now she fights alongside her returned brother knowingly, without yet being able to state the truth publicly.
- **Adversarial phase (climax of Act V):** Rhydia is the Champion battle — the final formal trainer-tier gate before Osrid is named her successor. **They fight knowing they are family.** The emotional weight of opposition is built entirely on the prior partnership.
- **Resolution phase (post-Champion):** Rhydia loses; Osrid is named Champion + Regent-King through the Hall of Fame unmasking sequence. Rhydia retains House Nightfall and continues as a major political figure. They are united again, this time publicly.

**Why this design is exceptional:**

Most fan-game Pokemon protagonists meet their Champion-tier opponent through *opposition first* (the Champion is a stranger or distant figure the player only faces at the end). Our player meets Rhydia *cooperatively first* in the early game. **Every battle the player fights with Rhydia as a partner is investment in the eventual adversarial battle.** The player will know her cycling team members (from the doubles preview), will have seen her dialogue patterns, will have respect for her combat decisions. **The Champion fight is *personal* in a way most fan-game Champion fights are not.**

This inverts the *standard* Pokemon-rival narrative arc (introduction-as-opposition → grudging-respect → final-respect) into a *richer* arc (cooperation-as-respect → revelation → opposition-through-circumstance → resolution-through-revelation). **The player and Rhydia are *family* by the climax, in a way no other fan-game protagonist-Champion relationship is.**

**Encounter order in the endgame:**
1. Player completes all 9 Trials
2. Paragon Gauntlet: 5 of the 6 stat-themed rivals (selected per logic TBD)
3. The 4 Viziers in succession (order TBD; Glaive is one of them as Vizier of War)
4. **Rhydia — the Champion fight.** Confirmed as locked endgame battle (no longer `[OPEN]` whether she is fought).
5. Hall of Fame unmasking sequence (Section 5)

`[OPEN]` Whether Eden has a final battle slot in the rival hierarchy, or her arc concludes pre-endgame and her final scenes are story-only.

### Design Principles — Summary Mantras

When reviewing a proposed feature, ask:

1. **Does it make the world feel alive?** (Principle 1)
2. **Does it respect the player's choices as permanent?** (Principle 2)
3. **Does it give recurring characters room to grow?** (Principle 3)
4. **Does it preserve resource scarcity and forced planning?** (Principle 4)
5. **Does each rival feel like a distinct person, not just a stat block?** (Principles 5, 6, 7)
6. **Does it embody Pokémon-as-partners-not-weapons?** (The overarching thesis from Section 1)
7. **Does it honor the partnership-thesis as baked into Cormoria's founding myth?** (Principle below — v0.9.4)
8. **Does it mirror Cormor's original partnership in the player's modern arc?** (Principle below — v0.9.4)

If a feature fails any of these, we either revise it or consciously document the departure.

### Principle: The partnership-thesis is baked into Cormoria's founding myth `[LOCKED v0.9.4]`

**Cormoria's existence is downstream of the most amazing bond that ever happened in Pokemon history.** Per Section 2 — Cormorian founding myth and Section 9 — Keerin entry:

- Cormor + Keerin's pact is *the* foundational partnership-thesis event of the project's cosmology
- Cormor saved reality not by *commanding* Keerin but by *partnering* with her — the firstborn-of-creation chose to share herself with a single mortal across the divine-mortal gap
- **Every Cormorian institution, every noble house, every cultural tradition descends from this original act of partnership**
- The partnership-thesis is not a *theme* imposed on Cormoria; it is the *foundation* on which Cormoria was built

**This principle has implications for every design choice:**

- **Trainer-Pokemon relationships are *historically real* in Cormoria.** The Templar Arceus order venerates the partnership-tradition; the surname-sacrament tradition is descended from Cormor's first Arceus-blessing of Roma; Glaive's eventual founding of the Blackthorn dragon-tradition is downstream of the Hermit's partnership-teaching which is downstream of the Cormor + Keerin tradition. **The thesis is *ambient* in Cormorian culture, not a moral lesson the game has to teach.**
- **The four cults represent the *inversion* of the partnership-thesis.** They treat Pokemon as cosmic-tools to be incarnated and wielded — not as partners. The cults' fundamental cosmological error is *not understanding what the Treasures of Ruin actually are* — Cormoria's own founding-myth artifacts gradually corrupted by Phancero's residue. **Defeating the cults is not just stopping a power-grab; it is *re-affirming Cormoria's founding partnership-thesis* against its inverted form.**
- **Osrid's renunciation (Veddev epilogue) is *consistent with* the founding thesis** — Cormor was a tribesman who became a king through cosmic accomplishment, and Osrid is a king who becomes a free man through cosmic accomplishment. The dynasty's truth is that royal identity is *earned-through-circumstance*, not divine-inherited. Osrid's renunciation completes a cycle the founding myth initiated.
- **Modern Pokemon canon's partnership-thesis (the canonical "friendship beats strength" trope) is downstream of Cormoria's lost founding.** Pokemon canon teaches partnership-as-power-multiplier; Cormoria's founding myth is *why* that lesson has cosmic weight. Players who engage with the Book of the Moon learn this; players who don't still benefit from the texture.

**The partnership-thesis is *the* design DNA that distinguishes Ruination from other Pokemon ROM hacks.** Many ROM hacks embrace harsh combat difficulty (Radical Red, Drayano hacks, etc.); few embrace *partnership-as-cosmological-foundation*. Ruination's combat difficulty exists *to make the partnership-thesis matter* — *the* harder the combat, the more the player must lean on their partnerships, the more the thesis is enacted through play.

### Principle: Cormor-as-original / Player-as-renewal mirroring `[LOCKED v0.9.4]`

**The player's arc *re-enacts* Cormor's founding partnership-arc at the modern scale.** This is not a coincidence; it is a deliberate design choice that creates cross-generational resonance.

| Cormor's arc (founding era) | Player's arc (modern era) |
|---|---|
| Member of nomadic Celestica tribe; lost his people to Phancero | Cormorian prince in exile; lost his father to House Nightfall's destruction |
| Pursued vengeance through cosmic-tier mission | Pursues the cult war through political-military mission |
| Pacted with Keerin (cosmic-tier partner) | Bonds with starter + Ting-Lu (cosmic-tier partners) |
| Used four Dreamstone-material objects in resonance ritual | Uses Dreamstone catalyst in sealing ritual |
| Erased Phancero from material world | Seals the four inverted-Dreamstone Treasures, preventing Phancero's re-emergence |
| Founded a dynasty | Renounces dynasty, founds the Berlitz line through Vandras's compassion |
| Eventually weary unto sleep | Eventually weary unto renunciation (chooses Veddev identity) |

**Mirroring details:**

- **The player's Mt. Silver Future-Red test mirrors Cormor's worthiness-test.** Keerin explicitly invokes this — *"Let us see if you are as worthy as Cormor was."* The same partner-Pokemon tests both heroes; the same partnership-thesis is enacted across the millennia gap.
- **The Necropolis Climactic Operation mirrors the original erasing ritual.** Both involve resonance-channeling through Dreamstone-material objects to address a cosmic-tier threat; both succeed through partnership rather than domination.
- **Cormor's eventual renunciation-of-engagement (sleep) mirrors Osrid's renunciation-of-identity (Veddev).** Both founding-figures eventually *step back* from the world they shaped, leaving their work to descendants.
- **The Hermit's centuries-long grief-preservation mirrors the player's late-game discovery of the lost cosmology.** Lethys preserved what Cormoria forgot; the engaged player rediscovers it through the Book of the Moon. **The chain of partnership-tradition closes when the player reads what the Hermit has been preserving for thousands of years.**

**Why this mirroring matters for the project's emotional resonance:**

- Players who recognize the mirroring experience the climax as *something larger than their own playthrough*. They are doing what their character's ancestor did, against a similarly-cosmic threat, with similar partnership-tier allies.
- **The greatness of Cormor's founding act is *re-discovered through the player's actions.*** The audience doesn't just *learn* about Cormor; they *embody* what made Cormor great.
- The project's emotional core is therefore *cross-generational*. Engaged players experience the past through the present, and the present is meaningful because it echoes the past. **This is the deepest layer of narrative-mechanical integration the project achieves.**

**Implementation implications:**

- **Late-game dialogue should explicitly invoke Cormor at key moments.** Examples already locked: Keerin's pre-battle dialogue ("as worthy as Cormor was") and possibly Madame Roma or the Blue Moon Hermit dropping similar hints during late-game encounters.
- **The 7v9 final battle should have visual/audio cues that mirror the original erasing ritual** — possibly resonance-themed environmental effects, possibly Dreamstone-glow visuals during the sealing
- **The post-Necropolis epilogue should have a quiet moment of historical resonance** — possibly the Hermit (if present at the post-game Book of the Moon compilation) reflecting on how the player walked Cormor's path

### Principle: Three-Redemption-Arc Pattern (Silas / Glaive / Ambrose) `[LOCKED v0.9.7]`

The project has *three* parallel major redemption-or-clarity arcs that all resolve through the same mechanism: **Osrid wins a Pokemon battle against a confused institutional figure, and the partnership-demonstration in combat communicates a moral truth that political argument could not.**

| Character | Institutional role | Initial state | Resolved through | Outcome |
|---|---|---|---|---|
| **Silas Moray** | Vizier of Commerce; Sword Cult 2IC | Corrupted under false pretenses (Baradus's manipulation post-Pierra-grief) | Vizier defeat by Osrid in Act V (third Vizier fought) | Silas pledges true loyalty; dies in sealing cataclysm as final act of love |
| **Glaive** | Vizier of War; future Solomonar | Vengeance-driven trainer carrying unrecognized dragon-empathic gift | Vizier defeat by Osrid in Act V (fourth Vizier fought, immediately before Champion) | Heart fully opens; leaves to found Blackthorn City |
| **Ambrose Caymen** | Archbishop of the Arceus Templar | Paralyzed by three-way pressure (Silas's lies, Umbra's trust, Nemo friendship) | Archbishop fight in Act III/IV after Osrid foils the cult-aligned bishop coup | Surrenders Mega-Dreamstone shard; cleanses cult influence from Templar; becomes staunch ally |

**The pattern's significance:**

- **The partnership thesis is weaponized at the institutional scale.** Osrid doesn't just save Cormoria from cults; he saves three major institutional figures from their respective forms of moral confusion. **He does this by *winning Pokemon battles against them.***
- **All three figures are not enemies in the cult sense** — they are not Baradus and Goma. Two are Viziers; one is the Archbishop. All three are *institutional figures of Cormoria whose moral clarity has been compromised.* They are *opponents whose defeat is also their liberation.*
- **The partnership-demonstration carries information that political argument couldn't.** Combat in this project is *moral revelation*, not just strategic resolution. Players who notice this pattern across three encounters realize: *the project's combat system is itself a vehicle for the project's central thesis.* Each Pokemon battle is an enactment of the partnership belief; each victory against a confused figure is that belief reaching them.
- **This is a worldbuilding-level extension of Section 1's thematic thesis.** "Pokemon are partners, not weapons" → "*A trainer's bond with their Pokemon, demonstrated in combat, is itself a form of moral testimony.*" The project's mechanical system *is* its moral argument.

**Implementation implications:**

- All three resolution fights should have *similar pacing structure* — combat is real and difficult, but the narrative purpose is the opposing figure's clarity, not the player's progression
- Post-victory dialogue should *each time* include the figure's recognition that "something in how you fought told me what argument could not"
- The pattern need not be stated explicitly to the player; the *recognition* is the engaged-player reward

### Principle: Permanent Emotional Complexity Without Resolution (the Silas-Brie axis) `[LOCKED v0.9.7]`

A v0.9.7 demonstration of Section 11 Principle 2 (the player's choices have permanent consequences; the world doesn't reset).

**The Silas-Brie relationship is the cleanest project example of *permanent emotional complexity that cannot be resolved by player choice or narrative resolution.*** The bible defines the relationship's structure (Section 7 — Brie Moray):

- Silas raised Brie like a daughter after her parents' accident-death (~10 years pre-story)
- Silas genuinely loves her like a daughter
- Silas envies Domdaniel's choice of Brie over him
- Brie loved Silas as a father-figure as a small child
- Brie has watched Silas "change" across the past decade — losing him slowly without being able to name what she was losing
- Brie's Fairy specialization is moral rebellion against the corrupted Psychic-tradition her uncle represents
- Brie *and* Silas *both* know they are losing each other

**The relationship is built to not resolve:**

- Silas dies in the sealing cataclysm at the end of Act VI. **Brie's love and grief and rebellion and complicity all coexist in a single teenage girl's heart at the moment of her uncle's death.** No narrative beat can clean this up; it is *meant to remain layered*.
- The player has no agency to "fix" the Silas-Brie relationship. There is no dialogue option that makes Brie forgive Silas or makes Silas explain himself. The complexity is *the point.*
- **This is the project's tightest demonstration of why Cormoria's stories don't tie neatly.** Family relationships fail because family is hard. Love and disappointment coexist because that's what love is. **Brie loses her father-figure twice when Silas dies — once to corruption (over a decade) and once to redemption (suddenly, in his final act).** Both deaths arrive in the same moment, and neither cancels the other.

**Implementation implication:** Late-game scenes involving Brie should *acknowledge the complexity* without resolving it. Brie's reactions to her uncle's death (if witnessed onscreen) should be *layered* — grief that includes the years of corruption-loss, recognition that includes the redemption-relief, **none of it resolving into a single clean emotion.** The dialogue writing must be willing to leave this contradictory.

### Principle: Unified Starter-Trio BST Framework `[LOCKED v0.9.8]`

All three Dreamstone Ruination starter lines (Frigibax → Arctibax → Baxcalibur; Teddiursa Blue Moon → Ursaring Blue Moon → Bloodmoon Ursaluna; Tinkatink → Tinkatuff → Tinkaton) conform to a **single unified BST framework**:

- **Stage 1: 375 BST**
- **Stage 2: 480 BST**
- **Stage 3: 600 BST** (Bloodmoon Ursaluna; baseline) — with cross-line variance pushed into stat *shape* rather than total, except where a specific final form has a named higher tier (Mega Baxcalibur sits at 720 per the Mega Evolution policy).

**Distinct role identities at every stage, not just final form:**

| Line | Role | Stat-shape signature |
|---|---|---|
| Frigibax → Baxcalibur | Physical attacker + speed | Baxcalibur signature stat: **Atk 145** |
| Teddiursa Blue Moon → Bloodmoon Ursaluna | Special-attacker apex | Bloodmoon Ursaluna signature stat: **SpA 145** |
| Tinkatink → Tinkaton | Defensive colossus | Tinkaton paired signature stats: **Def 125 / SpD 125** |

**Why the framework matters at the design level:**

- **Selectability without strict mechanical dominance.** A player picking any of the three starters sees roughly the same BST budget; the *choice* is which role identity to play, not which stat package to grab.
- **Both physical-attacker lines (Frigibax, Tinkatink) dump SpA**, since their full kits are 100% physical. SpA stats below 70 across all stages signal to engaged players that these lines aren't intended for mixed builds.
- **Only the Blue Moon line uses SpA**, with a full special kit (Echoed Voice → Psybeam → Torch Song → Moonblast → Lumina Crash → Moongeist Beam) that signals its identity from Lv 1.
- **Identity-from-Stage-1.** Stage 1 stat shape already telegraphs role; players don't have to wait three evolutions to see what they picked. This is a deliberate departure from canonical Gen 1 starter-trio design (where Stages 1 and 2 are similar; identity emerges only at Stage 3).

**This principle is the project-level abstraction of the Section 6 starter-line lock.** Detailed stat tables live in Section 6 — Starter Trio. The framework itself is the *pattern*; the stats are the *implementation*.

### Principle: Lv 77 Starter-Ace 10-PP Convention `[LOCKED v0.9.8]`

All three Stage-3 starter signatures learned at Lv 77 are normalized to **10 PP**:

- **Behemoth Blade** (Baxcalibur, Lv 77, Dragon, 120 BP, Fairy-effectiveness override) — 10 PP
- **Moongeist Beam** (Bloodmoon Ursaluna, Lv 77, Ghost, buffed 100 → 140 BP, ignoresTargetAbility) — 10 PP
- **Sunsteel Strike** (Tinkaton, Lv 77, Fire non-STAB, 140 BP, ignoresTargetAbility) — 10 PP

**Why the convention matters:**

- **Signature-move scarcity is preserved.** A Lv 77 ace with 10 PP can be deployed ~8 times per battle (10 PP — modulo Leftovers/items). Players cannot spam it; they must choose moments.
- **Cross-line equivalence.** The three signatures should *feel* equivalent in resource-cost terms. Different BP, different effects, different types — but the *opportunity cost* of pressing the button is the same across all three.
- **Mechanical-narrative alignment.** The Lv 77 ace pattern across the trio is one of the project's cleanest mechanical-narrative alignments. **Four absent canonical legendaries** (Zacian-Crowned, Zamazenta, Lunala, Solgaleo) have their signatures repurposed for Cormorian-engineered use: Behemoth Blade on Frigibax, Behemoth Bash on Tinkaton (Lv 30), Moongeist Beam on Teddiursa Blue Moon, Sunsteel Strike on Tinkatink. **The "Cormorian engineering > legendary gifts" thematic statement is delivered through the trio's combined learnsets.** The 10-PP convention is the mechanical glue that makes the cross-line equivalence legible to engaged players.

Full custom-move data lives in Section 9 — Custom Move subsections.

### Principle: Ace-Bonding Overworld Interactions `[LOCKED v0.9.8]`

A project-level design principle establishing how the partnership-thesis is demonstrated *outside combat*. This complements Section 11's earlier principles (which all centered on in-combat partnership demonstrations) by formalizing the project's commitment to **showcasing major trainers' bonds with their named ace Pokémon through overworld interactions outside of battle.**

**What the pattern is:**

When the player encounters a major named trainer in the overworld (i.e., not in a battle screen), that trainer's named ace Pokémon is present beside them whenever narratively appropriate, and the trainer is shown *interacting with the ace* in a way that demonstrates their bond and reveals character. Examples of the kind of interaction the pattern produces:

- **Simone Sylphon with Splendor (shiny female Obstagoon):** the fashion-and-luxury register — *"Oh darling, you look so fabulous with that beautiful fur today. There is no other Pokémon on the continent that can even BEGIN to compare. We MUST go shopping for a new ribbon for you tomorrow, mustn't we, darling?"* (See Section 7 — Simone Sylphon for the full Trial 4 entry; this is the inaugural full implementation of the principle.)

The interactions are designed to be **distinct per trainer-Pokémon pair** — Kimaris's interactions with Crowley should not sound like Simone's interactions with Splendor; Brie's interactions with Domdaniel should not sound like Manus's interactions with his ace. **The interaction *reveals* the bond's specific character**, not a generic "trainer loves Pokémon" register.

**Engine implementation:**

Each interaction is a small scripted event triggered by player proximity (or sometimes by a specific scripted scene). The technical components are:

- **Emoticon-over-head visual flourish** above the trainer (or the Pokémon, or both, depending on the interaction's emotional register)
- **Cry of the named Pokémon** is played during the interaction
- **Brief dialogue text** in the trainer's voice (or the Pokémon's mannerism-driven response, where applicable)
- The interaction is **non-blocking** — it plays out as the player passes through the area; it is not a forced cutscene the player has to dismiss

The aggregate effect is a setting that *feels lived-in*. Trainers and their Pokémon are *together,* visibly, in ways that read as ongoing relationship rather than gameplay convenience.

**Why the principle matters:**

The partnership-thesis is the project's central design commitment. Section 11's earlier principles demonstrate partnership through *combat* — Eden's item-disruption style, Glaive's dragon-empathic ability, the three-redemption-arc pattern, etc. But partnership in real life is *not primarily a combat phenomenon* — it is daily presence, small affection, accumulated routine. **A project committed to partnership as its central thesis must show partnership in the unspectacular daily forms it actually takes**, not only in the dramatic combat moments where it pays off.

The ace-bonding overworld interactions are the project's commitment to showing partnership at *non-combat resolution*. The contrast is also generative — players see Simone fuss over Splendor's ribbon in the overworld, then face an Obstagoon-Farigiraf doubles core that exploits Armor Tail priority blocking in Trial 4. *Same Simone, two domains, both real.* The fashion-register and the tactical-register are not in tension; they are the same expressed differently.

**Characters this principle applies to `[LOCKED v0.9.8 — narrative; engineering OPEN per character]`:**

**Scope criterion:** *Any named character with a locked ace Pokémon who appears in the overworld more than once across the story.* This criterion is the principle's actual gate — the list below is the v0.9.8 enumeration of who currently qualifies. As new aces are locked or new characters added, the criterion automatically determines whether they enter scope without bible amendment.

**Currently in scope (23 characters as of v0.9.8):**

| # | Character | Role | Ace(s) | Ace status |
|---|---|---|---|---|
| 1 | Kimaris Langerin | Trial Baron 1 (Ghost) | Crowley (shiny Spiritomb, Prankster) | Locked |
| 2 | Reid Ashland | Trial Baron 2 (Fire) | unique shiny Heatran (Earth Eater) | Locked |
| 3 | Manus Surge | Trial Baron 3 (Electric) | `[OPEN]` | Open |
| 4 | Simone Sylphon | Trial Baroness 4 (Normal) | Splendor (shiny female Obstagoon, Fur Coat) | Locked v0.9.8 |
| 5 | Trial 5 Baron (Raptora) | Trial Baron 5 (Flying) | `[OPEN]` | Open |
| 6 | Trial 6 Baron (Alban) | Trial Baron 6 (Grass) | `[OPEN]` | Open |
| 7 | Trial 7 Baron (Nightfall) | Trial Baron 7 (Dark) | `[OPEN]` | Open |
| 8 | Brie Moray | Trial Baroness 8 (Fairy) | Domdaniel (shiny Scream Tail, Huge Power) | Locked |
| 9 | Nemo Korolev | Trial Baron 9 (Ground) | **Manticore** (shiny Gliscor, Adaptability) **+ Ting-Lu** (two-ace structure) | Locked |
| 10 | Cadmus Umbra | Vizier of Education | Jousteel | Locked v0.9.8 |
| 11 | Glaive | Vizier of War | Salamence (Shelgon currently; evolves mid-game) | Locked |
| 12 | Silas Moray | Vizier of Commerce | primary ace `[OPEN]` + Thauma (shiny Hisuian Braviary) | Partial |
| 13 | Female Rock Vizier | Vizier (portfolio `[OPEN]`) | shiny Tyrantrum | Locked |
| 14 | Rhydia | Champion | **Justice** (Iron Valiant, Sharpness) **+ Puff** (shiny Drampa, Multiscale) (two-ace structure) | Locked |
| 15 | Goma | Beads Cult Harbinger | **Smolder** (shiny Emboar) **+ Mega Houndoom** (two-ace structure) | Locked |
| 16 | Baradus | Sword Cult leader | **Shardik** (shiny Beartic, Tough Claws — public-facing overworld ace, weapon-register interactions) **+ Guzzlord** (Dragon's Maw — strategic-deployment ace; *single late-game private-moment overworld scene only*) | Locked v0.9.8 (Option B arrangement) |
| 17 | Jordan Ramses | Poison-type recurring rival | `[OPEN]` | Open |
| 18 | Wakahisa | Bug-type recurring rival | `[OPEN]` | Open |
| 19 | Ambrose Caymen | Archbishop of the Templar Arceus Order (Steel) | **Temperance** (shiny Kingambit) **+ Brunhilda** (shiny female Perrserker) (two-ace structure) | Locked v0.9.7 |
| 20 | Eden | Deuteragonist / future spouse | her stolen starter (Frigibax / Teddiursa Blue Moon / Tinkatink — type-counter-locked to player's pick per the Eden Theft Scene) | Locked |
| 21 | Madame Roma | Soothsayer / progenitor of House Langerin | `[OPEN]` | Open |
| 22 | Blue Moon Hermit (Lethys) | Sage / Master Tutor (Blood Moon) | `[OPEN]` | Open |
| 23 | Sable Ashland | Returned-from-Ancient-Cormoria, uncle of Reid | **Solara** (shiny male Pyroar, Competitive — opener / elder-statesman ace; twin of Simone's Pyroar, gifted to childhood-Sable by the Sylphons) **+ Gouging Fire** (raised from egg in Ancient Cormoria — successor / cleanup-sweeper ace) (two-ace structure with elder/younger-sibling dynamic) | Locked v0.9.8 |

**Notable structural observations:**

- **Six characters have *two-ace* structures** (Nemo, Rhydia, Goma, Ambrose, Sable, plus Silas's partial Thauma secondary) — for these, the overworld interaction style may differ between primary and secondary aces, reflecting the trainer's distinct bonds with each. *Nemo's bond with Manticore is military-respectful; Nemo's bond with Ting-Lu is the older-soldier-with-a-tool-that-could-burn-him register.* Different bonds, same character. **Sable's two-ace structure is unique in featuring a Pokémon-Pokémon bond visible in the overworld** — Solara treats Gouging Fire as a much younger sibling (despite Gouging Fire being 10× Solara's mass); Gouging Fire defers to Solara as a big-brother figure. The size-mismatch is comedic and intentional. **Baradus's two-ace structure is the project's antagonist-inverted version of the pattern** — Shardik gets the standard repeated public overworld presence (treated as weapon, demonstrating the anti-thesis); Guzzlord gets a *single* hard-to-find late-game private moment (the one bond Baradus refused to extend to anything else). See Section 8 — Baradus entry for the Option B narrative lock.
- **One ace evolves mid-game (Glaive's Shelgon → Salamence)** — Glaive's overworld interactions therefore need *two versions* of the dialogue/animation, pre- and post-evolution. The Hermit-saved-Glaive-from-sandstorm-which-enabled-Bagon→Shelgon backstory (Section 7 — Glaive arc) is already a locked partnership-thesis demonstration; the overworld interactions extend it into the everyday register.
- **Eden's ace is type-counter-locked to the player's pick.** Engineering work for Eden's overworld interactions branches three ways (one per possible starter). This is moderate-scope additional work; the system must conditionally select the right interaction set based on the player's Act I choice.

**Characters explicitly OUT of scope (recorded for clarity):**

- **Vandras Amber-Letz** — merchant role, no locked ace Pokémon partnership; criterion-fail. Adding an ace to him solely to fit the pattern would inflate his character against his role; the bible holds him deliberately at the *quiet observer-gifter* role he occupies.
- **Boran Surge — the *anti-pattern* exclusion `[LOCKED v0.9.8]`.** Boran's exclusion is *not* a criterion-fail in the technical sense — it is *intentional characterization by absence.* Boran's "Pokemon are weapons" philosophy means he forms no deep bonds with his Pokémon; he commands without affection, deploys without partnership. There is no bond there to demonstrate, and the bible makes that absence visible. **The reader of the bible (and the engaged player) is meant to notice that every other locked-ace trainer in Cormoria has visible overworld bond-moments — and that Boran *doesn't*. The absence is the diagnosis.** Boran's only in-game appearance is as a PTSD-dream-sequence trainer fight (Section 7 — Boran Surge, v0.9.8 update); the dream-sequence Pokémon team is intentionally *unremarkable, military-effective, without bond-shaped optimization* — what hyper-competent training looks like *without* partnership. The contrast against the patterned characters is itself the principle's silent demonstration of why partnership matters.
- **Pierra** — Queen Mother, character role primarily political/familial rather than trainer-focused; no locked ace
- **Future-Red, Cogita, other cross-canon characters** — appear as set-piece encounters rather than recurring overworld presences; criterion-fail

`[OPEN]` Whether the overworld interaction pattern extends to *secondary* named Pokémon on these trainers' teams beyond the two-ace cases already enumerated (Justice + Puff for Rhydia, Smolder + Mega Houndoom for Goma, Temperance + Brunhilda for Ambrose, Manticore + Ting-Lu for Nemo). Recommendation: only the locked two-ace pairs receive the dual-treatment; if other trainers acquire a second named ace later, the criterion auto-adopts them.

`[OPEN]` Whether *minor* named NPCs with notable Pokémon (e.g., recurring tavern NPCs, key plot NPCs without recurring overworld presence) also receive ace-bonding overworld interactions. Recommendation: no — keep the principle reserved for major named recurring trainers, where the bond-demonstration earns its engineering cost.

---

