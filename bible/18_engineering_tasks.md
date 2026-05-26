<!-- This file is a split-section view derived from dreamstone_ruination_bible_v0.9.7.md (the canonical full bible at the repo root). Lines below correspond to the source lines noted in INDEX.md. Edit the canonical file and regenerate splits — do not edit splits directly. -->

## 14. Production Discipline

Story design and engineering proceed in parallel from v0.5 onward. The validation phase is complete (a prior Claude session verified the pipeline through real feature work). Every design decision continues to be one we can actually build.

### Pipeline status as of v0.9.3

**v0.9.3 is the post-Champion Ancient Cormoria side quests detail-lock patch** — touching Sections 6, 7, 13, 14. Key v0.9.3 additions:

- **Baxcaliburite quest ("The Origins of Cormoria's Dragons") fully specified** — Glaive accompanies the player; cave with ice puzzle; both the Baxcaliburite and Salamencite are discovered; **2v2 double battle Mega Baxcalibur + Mega Salamence vs. Roaring Moon + Walking Wake at level 120** (above-cap). Functions as the pre-cursor to the Sword Cult HQ raid + 7v9 final battle.
- **Ancient Peat Block quest ("The Shadow Self") fully specified** — the Blue Moon Hermit accompanies the player; ancient fog-shrouded Cormorian swamp setting (not a cave); **6v6 mirror match against the player's own shadow-self** with an identical-team opponent. Tests pure execution and outplaying.
- **Divine Cuirass quest ("The Sleeping Terror") fully specified** — *solo quest*; multi-floor puzzle temple where Koraidon sleeps; Hoopa Unbound guardian; **5-stage continuous gauntlet** (Blacephalon → Galarian Moltres → Iron Moth → Hoopa Unbound → Koraidon, all at level 100). Toughest combat encounter in the project outside the 7v9 final battle.
- **Glaive's Mega Salamence acquisition** locked as a byproduct of the Frigibax-picker's Baxcaliburite quest. Glaive faces Roaring Moon — the *Past Paradox version of his own Salamence*.
- **The Blue Moon Hermit** locked as a recurring named character — Trial 6 Master Tutor (teaches Blood Moon Ground for Bloodmoon Ursaluna evolution) + post-Champion Ancient Peat Block quest companion. *One character, two appearances*; consolidates a previously-open NPC identity.
- **Comparison table of the three side quests** locked across all distinguishing axes (setting, companion, combat structure, opponent count, emotional register, test of player skill, reward).
- **Above-cap encounter precedent established** — Roaring Moon and Walking Wake at level 120 are the first formally-locked above-cap encounters in the project; sets the design pattern for exceptional set-piece combat.

**v0.9.2 (preceding)** locked the Blue Moon Teddiursa line identity, the trio's offensive/defensive trinity, Frigibax/Tinkatink/Teddiursa ability suites, Blood Moon (Ground) custom move modification, Lunacy custom ability, Ancient Peat Block consumable, and the two-mechanic separation (Trial 6 Master Tutor evolution gates vs. post-Champion Ancient Cormoria side quests).

**v0.9.1 (preceding)** locked the Nobility Concordance senate structure, Leyline Resonance phenomenon, Cult Cosmological Framework (three conditions + Arceus-avoidance + Dreamstone-fragment failure), Domdaniel (House Moray's generational ace), Brie Moray full entry, Silas's Domdaniel-rejection wound, Nemo's secret-savior recharacterization, Baradus's three-fears framework, Goma's envy framing, Sylphon & Stone full status + Silph Co / Devon Corp descendants, Marshadow's Necropolis-Assault late-game deployment, and the Cormoria-as-mother-region note.

**v0.9 (preceding) was the Rhydia culmination patch** locking the original-purpose Rhydia character work and substantial worldbuilding (Cormor Dream-Eater origin, Justice's Iron Valiant truth, Generational Aces tier-system, Cormorian institutions).

**v0.8.2 (preceding)** locked the Hall of Fame unmasking sequence, the renunciation-not-amnesia epilogue framing, House Alban as Osrid's overseas cover identity, and the "Nomad" cultural designation.

**v0.8.1 (preceding)** locked the military rank hierarchy, surname-as-sacrament rule, House Surge, Manus Surge as 3rd Trial Baron, the ~50% Rhydia-learns-the-truth beat, and the Boran-Surge-to-Lt-Surge bloodline.

**v0.8 (preceding) was the largest single bible expansion** — Templar Arceus order, Tavern Pokemon Centers, Braviary travel, full Silas/Pierra/Baradus rewrites, Trial Barons Kimaris/Reid/Nemo, Sable Ashland, Mt. Ceram → Ancient Cormoria → Koraidon beat, the 7v9 final battle, Crabominable adoption, Ravage move, Mega Evolution policy, the Aerodactylite singular relic, and Cross-fandom References.

**Architecture note `[OPEN]`:** The bible is now approaching 2000 lines as a single document. At ~2500 lines this likely becomes unwieldy. We may need to split into multiple documents in a future revision:
- **World Bible** (Sections 1-4, 9, 11-12) — setting, institutions, mechanics, design principles, canon connections
- **Story Bible** (Sections 5-8, 10, 13) — characters, cults, story spine, open questions
- **Production Bible** (Section 14 + handoff doc) — engineering, patches, palettes, technical decisions

This split is not done now; it is flagged for consideration as the document continues to grow.

**Build environment strategy:** Hybrid — GenSpark for full compiles, Claude's Linux sandbox for source navigation, palette/sprite editing, patch generation, and data inspection
**Change delivery format:** Git-style patch files (`.patch`), applied via GenSpark
**Real production patches issued so far:**
- `0001-Frigibax-line-custom-shiny-palettes.patch` (v0.6) — 6 palette files for Frigibax/Arctibax/Baxcalibur custom shinies in Cormorian heraldic identity; pending user compile-and-verify
**Hybrid environment status:** Claude's Linux sandbox can clone, navigate, edit, and patch the Dreamstone Mysteries source tree. Claude **cannot** compile GBA ROMs locally. All compile/test work happens in GenSpark.

### Pending engineering work captured in v0.8

These are real production tasks that v0.8 has now formally specified, awaiting implementation:

1. **Custom Move: Ravage** (Guzzlord signature)
   - New move entry in `src/data/moves_info.h`: 130 BP / 85% acc / Dragon / Physical / no drawbacks
   - Add to MOVE constants enum
   - Customized Dragon Hammer animation (visual polish for gravitas)
   - Localization (move name + description text)
   - Add to Guzzlord's learnset (signature-only)
   - ~30-40 lines of code across 3-4 files

2. **Custom Crabominable Adoption Gift Event**
   - Triggered after mid-game Baradus encounter (~65-75% through)
   - Custom event script for discard scene + player-approach choice
   - Pre-set Pokemon: shiny Crabominable, perfect IVs, 252/129/129 EV optimization, holding Punching Glove
   - UI: nickname prompt, nature selector, ability selector (Slush Rush / Iron Fist / Defiant)
   - Set `FLAG_CRABOMINABLE_ADOPTED` for downstream dialogue checks
   - Conditional dialogue beats in final battle: Baradus's "refrigerated leftovers" line, Chien-Pao KO trigger, Beartic/Shardik KO trigger, final-KO trigger
   - ~4-6 hours focused implementation

3. **7v9 Final Battle Scripting**
   - Two consecutive double battles, no breaks/healing between
   - Battle 1: Player team + Ting-Lu vs Baradus Stage 1 team (Beartic Shardik, Abomasnow, Aurorus, Articuno, Froslass, Alolan Sandslash)
   - Battle 2: Same Player team + Ting-Lu vs Baradus Stage 2 team (Wo-Chien, Chi-Yu, Chien-Pao, Guzzlord)
   - Conditional dialogue triggers throughout
   - Silas's psychic-intervention scripted event after victory
   - Sealing cataclysm cinematic sequence
   - This is the most complex single scripting task in the project

4. **Custom Shiny Palettes Pending Reference Material**
   - Teddiursa line (3 species: Teddiursa, Ursaring, Ursaluna; plus Bloodmoon Ursaluna)
   - Tinkatink line (3 species: Tinkatink, Tinkatuff, Tinkaton)
   - Hisuian Braviary (Silas's Thauma — sinister color scheme)
   - Each: 2 .pal files per stage (battle + overworld), per the established pattern

5. **Mega Baxcalibur Sprite Project**
   - 64×64 front (pose locked from user reference, color/detail TBD)
   - 64×64 back (extrapolated from lower-quality reference)
   - 32×32 menu/dex icon
   - Footprint
   - Shiny variants in Cormorian heraldic identity
   - Species data: SPECIES_BAXCALIBUR_MEGA enum, stats, types, abilities, learnset
   - Item data: ITEM_BAXCALIBURITE
   - Mega Evolution table entry
   - Pokédex entry
   - Multi-session pixel art project

6. **Starter Selection Script Replacement**
   - Replace Gothita/Timburr/G-Zigzagoon with Frigibax/Teddiursa/Tinkatink in Umbra's gift scene
   - Modify existing script, preserve scene structure

7. **Ancient Cormoria Flashback Implementation**
   - Study DM's Ancient Ceram/Mirroh time-travel implementation as template
   - Adapt for our Mt. Ceram 70% beat sequence
   - Multiple custom map sequences (cave with Slither Wing, ancient temple with Koraidon)

8. **Memory-Erasure Mechanic for Silas**
   - May or may not require player-facing mechanics
   - Likely background-narrative only (no in-game "memory erasure" turn-by-turn battle effect)
   - May affect specific NPC dialogue states triggered by Silas's manipulation

9. **Hall of Fame Unmasking Sequence (v0.8.2 addition)**
   - Custom event sequence triggered after defeating Rhydia in the Champion battle
   - Daguerreotype-equivalent photographic capture animation for the team-preservation moment (Osrid captured *masked* in the eternal Hall record)
   - Vault-sealing visual effect
   - Sprite swap: masked Rainhawk sprite → unmasked Champion-Osrid sprite (one-time, persistent)
   - Crowd-reveal scene with mask-removal animation
   - Rhydia's announcement dialogue with player's chosen true name substitution
   - Coronation as Regent-King + Champion (UI flag updates, possible title-bar change)
   - This is the most narratively-loaded single custom event in the game; deserves significant polish budget

10. **Veddev Epilogue Implementation (v0.8.2 addition)**
   - New Veddev sprite distinct from both masked Rainhawk and unmasked Champion-Osrid (more lived-in, merchant clothing, no royal accents)
   - Dialogue layer change: player's chosen true name *stops appearing* after the renunciation; only "Veddev" appears in epilogue dialogue (significant text-state implication)
   - Paldean transaction scene with Eden recognition
   - Body-language recognition beat (Eden's dialogue lines acknowledging she knows him before any name-confirmation)
   - Marriage scene (cinematic or playable per `[OPEN]` decision)
   - Optional: cinematic showing Pierra and Rhydia mourning Osrid as dead (the "she never learns" beat made visible to the player even if not to the characters)

11. **Goma Assassination Subplot — Doubles-Format Scripted Battles (v0.9 addition)**
   - Post-Trial 2 narrative beat (~25-30% through)
   - Doubles-format scripted battles with player + Rhydia as allies vs. Beads Cult acolytes and Bishop
   - Rhydia's partner-AI needs to be *good* — she is canonically a superb trainer; her AI should not make stupid moves alongside the player
   - Training-team variant of Rhydia's cycling roster: lower-level (probably 30-35) versions of Aegislash, Swampert, Zebstrika, Hisuian Lilligant, Stonjourner, Talonflame
   - Custom dialogue throughout the doubles sequence
   - Plot-failure beats: Goma escapes, Dreamstone is preserved, Rhydia survives, sets up Mt. Ceram escalation later
   - Implementation effort: significant — first major scripted-cooperative-combat sequence in the game

12. **Rhydia's Champion Battle — Justice and Puff Custom Pokemon Data (v0.9 addition)**
   - **Justice** — shiny Iron Valiant with custom moveset (Sacred Sword / Tachyon Cutter / Bitter Blade / Mighty Cleave), Sharpness ability, Choice Scarf, Champion-level stat/EVs/IVs
   - **Puff** — shiny Drampa with Multiscale ability (Hidden Ability), Assault Vest, custom learnset including **Thunderclap** (Ruination-added — Drampa does not canonically learn Thunderclap; this is a Puff-specific learnset modification requiring engine-level learnset.h edit), plus Dragon Energy / Hyper Beam / Flash Cannon, Champion-level stat/EVs/IVs
   - Rhydia's full Champion-tier team data: Justice + Puff + 4 cycling members from the rotation
   - The cycling selection logic — Rhydia "scouts" the player and adjusts; this could be (a) deterministic based on player team composition (simple if-then logic), (b) random selection from her rotation, or (c) script-defined per-playthrough. Decision deferred.
   - Possible Mega Evolution authorization for Rhydia (`[OPEN]` Section 7 — she has Champion sanction; current team doesn't include obvious Mega candidates)

13. **Hall of Fame Daguerreotype Capture Animation Refinement (v0.9 follow-up)**
   - The Hall of Fame photographic-capture animation (Section 5 — Hall of Fame unmasking sequence) needs visual polish
   - The "Osrid captured masked in eternal record" detail requires the photograph asset to clearly show the masked Champion
   - Symbolic continuity: this photograph is preserved in the vault and may surface in late-game artwork or post-game lore

14. **Necropolis Assault Multi-Stage Scripted Battle Sequence (v0.9.1 addition)**
   - **Potentially the largest team-fight set-piece in the game outside the 7v9 final battle.**
   - Locked as a *playable* late-game beat in Act V or early Act VI (Section 10 — Act V; structural placement `[OPEN]`)
   - Multi-stage scripted battle sequence — distinct combat encounters across different areas of the Mirroh Necropolis, building toward a final confrontation with the cult's assault commander (Baradus personally? a lieutenant? `[OPEN]`)
   - **Player + Kimaris Langerin + Marshadow** as the central defensive force
   - Possible additional defenders: Templar Arceus operatives (named/unnamed), House Langerin retainers (named/unnamed), possibly Brie Moray + Domdaniel as part of a multi-house defensive convergence
   - Cult attackers: Sword Cult acolytes, Bishops or military-rank-equivalents (Section 8 — Sword Cult rank-naming convention `[OPEN]`), possibly Beads Cult support if Goma has chosen to ally with Baradus at this point (`[OPEN]`)
   - Marshadow combat profile at level 100 — Spectral Thief, Close Combat, Shadow Sneak, Bulk Up (likely; `[OPEN]` final kit); item: Marshadium Z or equivalent custom item
   - **Environmental design:** The Necropolis is a Cormorian-religious-grounds location with the Distortion gate hidden somewhere within it. Multiple battle areas — outer grounds, inner chambers, the gate chamber itself
   - **Win condition:** repel the assault, prevent the Distortion gate from being activated for Chien-Pao incarnation. The cult is repelled but not destroyed; this is *one major front* of the late-game cult war, not the final confrontation.
   - **Implementation effort:** *significant*. Custom maps for Necropolis areas if not already in DM source. Multi-stage scripted battle logic. Custom ally-AI for Marshadow at level 100 fighting alongside the player. Multiple custom-NPC trainers for cult attackers. Significant dialogue across the sequence. Possible cinematic moments (Marshadow's first deployment, gate-defense climax).
   - This is one of the *most production-heavy* beats in the project — comparable in scope to the climactic 7v9 final battle.

15. **Blue Moon Teddiursa Line — Pokemon Data + Sprites (v0.9.2; rebalanced v0.9.5)**
   - Custom Pokemon species variants for Teddiursa (Blue Moon), Ursaring (Blue Moon), Bloodmoon Ursaluna (Blue Moon)
   - Stat spreads (HP/Atk/Def/SpA/SpD/Spe) `[LOCKED v0.9.5]`:
     - Teddiursa (Blue Moon): **60/50/50/80/50/40** (BST 330) — pure Atk↔SpA swap from canonical
     - Ursaring (Blue Moon): **100/75/85/100/85/55** (BST 500) — swap + redistribute 30 SpA into HP/Def/SpD; BST preserved
     - Bloodmoon Ursaluna (Blue Moon): **113/75/85/145/90/52** (BST 560) — apex SpA 145, +15 Def, +15 SpD; BST increased from canonical 520 to 560
   - Custom learnsets per the Section 6 spec — Echoed Voice/Round/Disarming Voice/Mud-Slap/Mud Shot/Hyper Voice/Mud Bomb/Earth Power/Boomburst/Blood Moon/Hyper Beam/Moonblast/Calm Mind/Slack Off
   - Ability slots: Mind's Eye + Fur Coat (normal) + Soul-Heart (Hidden)
   - Evolution method modification: Ursaring (Blue Moon) → Bloodmoon Ursaluna (Blue Moon) at level 45 + Blood Moon known. **Skip regular Ursaluna stage entirely** for this evolutionary path.
   - Custom blue-and-black palettes per the reference image (sprites to be designed in a dedicated production pass)
   - Implementation effort: substantial. Three species variants × full Pokemon data sets + custom sprite work + evolution logic modification.

16. **Custom Ability Implementations (v0.9.2 addition)**
   - **Mind's Eye** — port to Teddiursa line (canonical: Bloodmoon Ursaluna only). Modify ability assignment table.
   - **Fur Coat** — port to Teddiursa line (canonical: Furfrou only). Logic should already exist; just modify assignment table.
   - **Soul-Heart** — port to Teddiursa line (canonical: Magearna only). Logic should already exist; just modify assignment table.
   - **Lunacy** — NEW ABILITY, must be implemented from scratch:
     - Passive at switch-in: +10% Speed per fainted ally (max +50%); parse `gPlayerPartyCount` for fainted allies
     - Reactive on KO: +1 Sp.Atk stage when user KOs an opponent; extend existing on-KO hooks similar to Soul-Heart implementation
     - Compatible with stat-stage cap (+6 max)
     - New ABILITY_LUNACY entry in abilities table
   - **Ice Scales** — port to Frigibax line (canonical: Frosmoth). Logic should already exist; modify assignment.
   - **Slush Rush** — already exists for various Ice-types (canonical). Modify assignment for Frigibax line.
   - **Armor Tail** — port to Frigibax line (canonical: Farigiraf). Logic should already exist; modify assignment.
   - **Cute Charm** — already exists for various Pokemon (canonical Tinkatink already has it). No port needed; confirm assignment.
   - **Battle Armor** — already exists (canonical). Modify assignment for Tinkatink line.
   - **Pixilate** — port to Tinkatink line (canonical: Sylveon, Mega Gardevoir/Diancie). Logic should already exist; modify assignment.
   - Implementation effort: low-to-moderate for most (assignment-table edits); high for Lunacy (new ability logic).

17. **Blood Moon (Ground) Custom Move Modification (v0.9.2 addition)**
   - Modify existing MOVE_BLOOD_MOON entry in moves_info.h
   - Change type from `TYPE_NORMAL` to `TYPE_GROUND`
   - All other move properties (BP 140, accuracy 100, special category, PP 5, no-consecutive-use restriction) preserved
   - Implementation effort: trivial (single-line type change in move data table)

18. **Ancient Peat Block Consumable Item (v0.9.2 addition)**
   - New ITEM_ANCIENT_PEAT_BLOCK consumable item
   - Item icon (32x32, post-Champion item aesthetic — possibly a glowing peat block with blue-glow effect to match the Blue Moon palette)
   - Use-from-bag event logic specific to Bloodmoon Ursaluna (Blue Moon) — refuses use on other species
   - Ability-replacement event handler — overwrite the Pokemon's current ability slot with ABILITY_LUNACY
   - UI confirmation dialogue before commit (one-way transformation must be confirmed)
   - Post-game flag check — item only obtainable in post-Champion content; tied to the Ancient Cormoria side quest (task #19 below)
   - Implementation effort: moderate. Item-use event logic with ability replacement is non-trivial but follows established patterns.

19. **Post-Champion Ancient Cormoria Starter Bonus Side Quests (v0.9.2 addition, expanded v0.9.3)**
   - Three distinct optional side quests gated by starter choice; player engages with one per playthrough
   - All three reuse the existing Ancient Cormoria map area (already implemented for the Mt. Ceram beat in Act III), but each requires distinct *sub-locations* (cave / swamp / temple)
   - Each quest has unique story content, characters, and combat encounters
   - Quest trigger flag: post-Hall-of-Fame-coronation completion; entry NPC or location TBD
   - Quest gating logic per starter choice — only the relevant quest is available per playthrough
   - Detour-or-skip mechanic: player can complete the quest or skip it; main story continues to Sword Cult HQ raid regardless
   - `[OPEN]` Whether the Act VI cult war state progresses while the player is on detour (narrative-cost) or pauses
   - `[OPEN]` "Point of no return" warning logic before Sword Cult HQ raid commits

   **19a. Baxcaliburite quest — "The Origins of Cormoria's Dragons" `[LOCKED v0.9.3]`:**
   - **Setting:** Cave in Ancient Cormoria with a unique ice puzzle
   - **Companion:** Glaive joins the player (NPC follower scripting required)
   - **Items discovered in cave:** Baxcaliburite + Salamencite (both stones placed in/near same cave)
   - **Climactic battle: 2v2 double battle, both player and Glaive Mega-evolve at battle start**
     - Player: Mega Baxcalibur (player must have Mega Stone equipped before battle initiation)
     - Glaive: Mega Salamence "Blackthorn"
     - Opponents: **Roaring Moon (level 120)** + **Walking Wake (level 120)** — *above standard cap*
   - **Implementation engineering:**
     - Custom trainer data for the Roaring Moon + Walking Wake encounter with above-cap level support — verify that pokeemerald-expansion level cap accommodates level 120 (likely uses internal MAX_LEVEL = 100 by default; will need engine modification or per-encounter override)
     - 2v2 double-battle scripting with ally-AI for Glaive's Mega Salamence (similar to existing partner-AI battle patterns in DM)
     - Cave map design with ice puzzle scripting
     - Glaive NPC follower system across the Ancient Cormoria journey
     - Battle initiation logic for *forced* Mega Evolution on turn 1 (both player and ally)
     - Post-battle scripting: Glaive thanks the player, Salamence's Mega capability persists for future encounters
     - `[OPEN]` Specific opponent kit details (likely Roaring Moon: Acrobatics / Dragon Dance / Crunch / Earthquake with Booster Energy; Walking Wake: Hydro Steam / Draco Meteor / Flamethrower / Dragon Pulse)
     - `[OPEN]` Whether Glaive's Mega Salamence persists post-quest for all future encounters with him (likely yes, including the Necropolis Assault if not yet completed)

   **19b. Ancient Peat Block quest — "The Shadow Self" `[LOCKED v0.9.3]`:**
   - **Setting:** Ancient fog-shrouded Cormorian swamp (sub-location of Ancient Cormoria map; *not* a cave)
   - **Companion:** The Blue Moon Hermit (Section 7 — Blue Moon Hermit entry; this is the player's continued relationship with the Trial 6 Master Tutor)
   - **Atmospheric design:** Fog density increases as the player progresses deeper; environmental lighting dims; dreamlike disorientation effects (possibly screen shaders or palette dimming)
   - **The shadow-self encounter:** Before reaching the Peat Block pedestal, a *shadow version of the player* emerges from the fog
   - **Combat: 6v6 mirror match against the shadow-self**
     - Shadow opponent's team is *cloned from the player's current party at the moment of battle initiation* — same species, same moves, same items, same EV/IV spreads, same nature
     - All Pokemon start at full HP regardless of the player's pre-battle state
   - **Implementation engineering:**
     - Mirror-team battle scripting: snapshot the player's party data at battle initiation and use it as the opponent's team data
     - Shadow-sprite asset for the player character (palette-swap to dark/grayscale)
     - Fog and atmospheric environmental scripting for the swamp area (custom map shader or palette manipulation)
     - ITEM_ANCIENT_PEAT_BLOCK acquisition logic upon victory (already designed in v0.9.2 task #18; this just ties the obtainment to this specific quest's win flag)
     - `[OPEN]` Whether the shadow-self has any dialogue (default: silent)
     - `[OPEN]` Whether the Blue Moon Hermit's role during the fight is purely observational or includes any pre-fight/post-fight dialogue significance

   **19c. Divine Cuirass quest — "The Sleeping Terror" `[LOCKED v0.9.3]`:**
   - **Setting:** Multi-floor puzzle temple where Koraidon sleeps (sub-location of Ancient Cormoria map; the same temple visited during Act III Mt. Ceram beat)
   - **Companion:** *None* — solo quest
   - **Structure:** Multi-floor puzzle dungeon; each floor presents puzzles the player must solve to descend further. `[OPEN]` Number of floors, puzzle types
   - **The combat gauntlet: 5 stages, continuous, no team-swap recovery between stages, all level 100:**
     - **Stage 1:** Blacephalon (Fire/Ghost; canonical Ultra Beast)
     - **Stage 2:** Galarian Moltres (Dark/Flying; canonical Galar regional variant)
     - **Stage 3:** Iron Moth (Fire/Poison; canonical Future Paradox)
     - **Stage 4:** Hoopa Unbound (Psychic/Dark; canonical Mythical)
     - **Stage 5:** Koraidon (Fighting/Dragon; canonical Past Paradox legendary)
   - **Win condition:** Defeat all 5 stages without losing
   - **Post-victory scripting:** Koraidon returns to sleep, Hoopa Unbound disappears, Divine Cuirass becomes claimable from a pedestal in a separate chamber behind the sleeping Koraidon
   - **Implementation engineering:**
     - Custom multi-floor temple map design (likely 3-5 floors based on Mt. Ceram template)
     - Puzzle scripting per floor (variety needed across floors — pushing blocks, switches, light-redirection puzzles, etc.)
     - 5-stage continuous gauntlet battle scripting — standard pokeemerald-expansion supports multi-battle trainers, but the gauntlet structure may require custom scripting if no team-swap between stages is desired (`[OPEN]` whether team-swap is allowed)
     - Custom encounter data for all 5 stages at level 100 with competitive kits
     - ITEM_DIVINE_CUIRASS held-item with custom stat-boost + heal-each-turn logic (species-lock to Tinkaton)
     - Koraidon sleeping → awakening → re-sleeping animation/scripting
     - Hoopa Unbound disappear animation upon defeat
     - Cuirass claim event scripting
     - `[OPEN]` Specific kits for the 5 opponents — likely include:
       - Blacephalon: Mind Blown / Shadow Ball / Flamethrower / Trick (Choice Specs)
       - Galarian Moltres: Fiery Wrath / Nasty Plot / Hurricane / Memento (Berserk + Life Orb)
       - Iron Moth: Fiery Dance / Sludge Wave / Discharge / Substitute (Quark Drive + Booster Energy)
       - Hoopa Unbound: Hyperspace Fury / Psychic / Dark Pulse / Drain Punch (Magician + Life Orb)
       - Koraidon: Collision Course / Flare Blitz / Outrage / Bulk Up (Orichalcum Pulse — sets sun automatically)
     - `[OPEN]` Ordering of stages 1-3 (Blacephalon/G-Moltres/Iron Moth) — sequential as listed, or some other arrangement
     - `[OPEN]` Whether stages 1-3 are presented as Hoopa "summoning" them on-screen (cinematic moments) or simply sequential battles

   **Implementation effort across all three quests: *very high*.** Three unique scripted quest sequences with distinct narratives, custom dialogue, NPC encounters, environmental design, and combat. **This is the largest single production task in the v0.9.x scope.**

20. **Trial 6 Master Tutor Implementation (v0.9.2 addition, partially resolved v0.9.3)**
   - Three Master Tutors as named characters in Cormoria — Blue Moon Hermit is now LOCKED (Section 7 entry); Mountain Gale tutor and Gigaton Hammer tutor still `[OPEN]` for identity and location
   - Each teaches the species-specific gating move:
     - Mountain Gale (Baxcalibur evolution)
     - Blood Moon (Ground) (Bloodmoon Ursaluna Blue Moon evolution; uses the v0.9.2 retyped move) — taught by **the Blue Moon Hermit**
     - Gigaton Hammer (Tinkaton evolution)
   - Quest structure per tutor — `[OPEN]` specific challenges, dialogue, narrative beats
   - Move tutor event logic — gating by species + level 45+
   - Evolution trigger logic — learning the tutor move at level 45+ triggers the evolution
   - Implementation effort: moderate per tutor; total moderate-to-high across three.

### Process discipline (carried forward from v0.4 + handoff doc + Frigibax work)

The handoff doc consolidates patterns we should follow. Highest-priority disciplines:

- **Read before editing.** `grep -rn <identifier>` first. The same data often lives in multiple files (enum + initializer + JSON); editing one without the others creates silent bugs.
- **Verify constants exist** before referencing them. This fork has custom items, abilities, and species. Never assume vanilla pokeemerald constants exist.
- **For sprite/palette work:** analyze the sprite's actual per-index pixel mapping (front and back separately if they differ) before designing a palette. Don't apply the same auto-recolor to both battle and overworld palettes — they have different index meanings. Preview visually before committing.
- **Pre-quantize palette colors to multiples of 8** for GBA-safe rendering. This ensures the preview matches the in-game result exactly.
- **Delete compiled `.gbapal` / `.4bpp` / `.lz` binaries** when changing their source `.pal` / `.png`. Stale binaries can confuse incremental builds. Issue clear "delete these files" instructions alongside any patch that changes source palette/sprite files.
- **Edit BOTH `.pory` and `.inc`** for map scripts. GenSpark's build may or may not regenerate `.inc` from `.pory`; editing both is cheap insurance.
- **For player-facing questions** (catchable? reachable map? NPC exists?), authority order is: user's experience → DM Dex spreadsheet → handoff doc → source tree → engine docs → canon.
- **When questions can be answered by running a command in the repo, run the command** rather than asking the user.
- **For sprite recolor work, always render preview PNGs and get user sign-off before producing a patch.** Iteration in design space is faster than iteration in compile space.

### Next priority order

1. **Verify v0.9.3 with user** — confirm the three Ancient Cormoria side quests, the Blue Moon Hermit character identity, and the Glaive Mega Salamence acquisition mechanic read as intended.
2. **Continue design discussion** — open items from the Section 13 Open Questions list, particularly:
   - Blue Moon Hermit's actual name and personal Pokemon team
   - Mountain Gale and Gigaton Hammer Master Tutor identities and locations
   - Whether Glaive's Mega Salamence is Frigibax-picker-only or off-screen for other paths
   - Shadow-self dialogue (if any) during the Ancient Peat Block quest
   - Hoopa Unbound's exact kit and ordering of the Divine Cuirass gauntlet summoned trio
   - Whether the Act VI cult war progresses during the post-Champion detour (narrative-cost vs. paused)
   - Remaining 5 Trial Barons (Trials 4-8) and their houses
   - Other senior houses' generational aces beyond Langerin (Marshadow) and Moray (Domdaniel)
   - Brie Moray's specific story role
   - Necropolis Assault structural placement and command
   - Sylphon and Stone family heads
   - Goma's full Pokemon team
3. **Teddiursa (Blue Moon) line custom sprites** — reference image received v0.9.2; production pass needed
4. **Tinkatink line custom shiny palettes** — still pending user-provided reference material
5. **Custom shiny Hisuian Braviary** for Silas's Thauma (when user provides reference material)
6. **Starter selection script replacement** (Gothita/Timburr/G-Zigzagoon → Frigibax/Teddiursa/Tinkatink)
7. **Custom move Ravage implementation** (small task, can be done as side work)
8. **Blood Moon (Ground) type retype** (trivial single-line change in moves data)
9. **Custom Lunacy ability implementation** — new ability requires full implementation
10. **Crabominable adoption event implementation** (~4-6 hours)
11. **Mega Baxcalibur sprite design** (multi-session pixel art project)
12. **Goma assassination subplot doubles-format battle implementation**
13. **Justice and Puff custom Pokemon data** for Rhydia's Champion battle
14. **Domdaniel custom Pokemon data** for Brie Moray's appearance(s)
15. **Necropolis Assault multi-stage scripted battle sequence**
16. **Blue Moon Teddiursa line full Pokemon data + custom sprites**
17. **Custom ability ports + Lunacy implementation**
18. **Ancient Peat Block consumable item + ability-replacement logic**
19. **Three post-Champion Ancient Cormoria side quests** — *now fully specified per v0.9.3*; remains the largest single production task in the v0.9.x scope. Includes:
    - 19a: Baxcaliburite quest (cave + ice puzzle + 2v2 Mega vs. Roaring Moon + Walking Wake at level 120)
    - 19b: Ancient Peat Block quest (fog-shrouded swamp + 6v6 mirror match against shadow-self)
    - 19c: Divine Cuirass quest (multi-floor puzzle temple + 5-stage gauntlet vs. Blacephalon/G-Moltres/Iron Moth/Hoopa Unbound/Koraidon)
20. **Trial 6 Master Tutor implementation** — Blue Moon Hermit LOCKED v0.9.3; Mountain Gale and Gigaton Hammer tutor identities still `[OPEN]`

### v0.9.4 new engineering tasks (post-cosmology-lock)

The v0.9.4 patch added substantial new mechanics, characters, and content. These tasks represent the engineering work needed to bring v0.9.4 lore to playable reality. Listed in approximate priority order:

21. **Three-mode difficulty system implementation (Classic / Elite / Paragon)** — `[MAJOR — foundational]`
    - Mode selection UI at game start (before character creation)
    - Mode flag tracking in save data
    - Difficulty modifiers applied across the game based on mode flag:
      - Level cap enforcement (none for Classic; match-cap for Elite; cap+5 for top-two in Paragon)
      - IV/EV settings for enemy trainer Pokemon (competitive for Classic; max IVs + scaling EVs for Elite; max IVs + optimized EVs for Paragon)
      - Item-use restrictions (unlimited for Classic; one per battle / one per round for Elite + Paragon)
      - AI behavior (standard for Classic; intensified for Elite; ruthless for Paragon)
    - Mode-locked content gates (Keerin sidequest only available in Elite or Paragon)
    - Player starter IV/EV settings (perfect from start in Paragon)
    - **This is the most architecturally significant engineering task in v0.9.4** — touches every battle in the game

22. **Unboxable-starter mechanic implementation** — `[MEDIUM]`
    - PC interface modification (Tavern Pokemon Caretaker) to check the deposit-Pokemon flag against the starter-species flag
    - Conditional refusal logic when player attempts to deposit the starter
    - Reaction dialogue from the Tavern Pokemon Caretaker NPC
    - Possibly a brief animation showing the starter refusing
    - Integration with Vandras epilogue scene (the starter must be present in party for epilogue dialogue to fire)

23. **Nuzlocke toggle system implementation** — `[MEDIUM]`
    - In-game menu toggle (accessible at any time during Elite or Paragon mode)
    - Death tracking (KO'd Pokemon flagged as "dead")
    - Party-removal-on-faint logic (KO'd Pokemon released or sent to designated death-zone)
    - **Starter exemption rule** — KO'd starter is NOT permanently removed (cosmic narrative significance preserved)
    - First-encounter rule logic (only first wild encounter per route can be caught)
    - Optional rule clauses (species, nickname, dupes)
    - Save-data architecture for Nuzlocke state

24. **Randomizer system implementation** — `[MEDIUM-MAJOR]`
    - Settings menu (substantial UI work for configurable options)
    - Randomization tables for: wild encounters, trainer teams, abilities, movesets, hold items
    - **Starter-and-evolutions exclusion logic** — Frigibax/Teddiursa Blue Moon/Tinkatink lines never randomized regardless of settings
    - Save-data architecture for randomizer state and seed
    - Compatibility logic with difficulty modes + Nuzlocke (all independent toggles)

25. **Keerin Pokemon data variants** — `[MEDIUM]`
    - Custom species data for Keerin (typing Normal/Ghost; BST ~720; full learnset)
    - **Two ability variants based on mode:**
      - Elite mode: **Opportunist** ability (Keerin variant data flagged "Elite")
      - Paragon mode: **Wonder Guard** ability (Keerin variant data flagged "Paragon"; perfect IVs and EV spread auto-applied)
    - Signature move designs `[OPEN]` — possibly a custom Normal STAB and a custom Ghost STAB
    - Sprite GBA-remastering from asset library (front, back, icon — normal + shiny palettes)
    - **Overworld following sprites for Keerin** — new development needed (not in asset library)

26. **Mt. Silver Future-Red sidequest scripted scene** — `[MASTER SCRIPTING TASK — major]`
    - Mt. Silver map recreation (visually identical to canonical HG/SS summit; environmental effects optional)
    - Future-Red NPC sprite (older Red, shadow-covered visual treatment)
    - Six custom-data legendary Pokemon at level 100 with optimized competitive kits:
      - Mewtwo (possibly Mega Mewtwo X or Y)
      - Urshifu Rapid Strike Form
      - Yveltal (the Keerin-counter)
      - Mega Rayquaza
      - Eternatus
      - Miraidon
    - **3v6 battle constraint logic** — player allowed only Keerin + 2 reserve Pokemon for this battle
    - Pre-battle Keerin dialogue + worthiness-test framing
    - Post-battle Future-Red dialogue + acknowledgment (`"... so this is the power of the past. Interesting."`)
    - Transportation effects (player transported to Mt. Silver, then blacks out and returns)
    - Conditional party-add logic (Keerin joins post-victory)
    - **Mode-gating** — sidequest only available in Elite or Paragon
    - **Difficulty-variant logic** — Keerin variant (Opportunist in Elite, Wonder Guard in Paragon)

27. **Book of the Moon implementation** — `[MAJOR]`
    - Custom Key Item: "Book of the Moon" (compiled, post-Hermit-compilation)
    - 10-11 Custom Key Items: "Book of the Moon Chapter [N]" (individual collectible fragments)
    - Item placement events scattered across Cormoria at locations of historical/cosmological significance
    - Hermit compilation event scripting (chapter-count check; conditional based on Teddiursa-picker auto-compile vs. Frigibax/Tinkatink separate-visit)
    - Readable book UI (multi-page interface; persistent across saves)
    - **Text content authoring for all 10-11 chapters + Hermit annotations** — substantial worldbuilding-text work (likely 5,000-8,000 words of in-game readable lore)

28. **Jousteel line full Pokemon data + sprite work** — `[MEDIUM]`
    - Custom species data for Joustroll and Jousteel (new dex slots)
    - Full Pokemon data: stats, abilities, learnsets, evolution method
    - Sprite GBA-remastering from asset library (front + back for both stages; icons need new development)
    - House Umbra cultivation logic — Joustroll/Jousteel encounters gated to Umbra-associated locations; no wild population
    - Cadmus Umbra's Jousteel competitive kit (moveset, item, ability, stat allocation)

29. **Madame Roma NPC implementation** — `[MEDIUM]`
    - Custom NPC sprite (likely adapted from Nise or Mirtha asset templates per `/home/claude/assets/ASSET_LIBRARY_INVENTORY.md`)
    - Multiple scripted appearances (royal court visits as soothsayer; fossil-revival event scenes; late-game dialogue beats; possibly post-game Book of the Moon synthesis moments)
    - Dialogue authoring establishing layered identity (Madame Roma public soothsayer + Roma Langerin centuries-old progenitor)
    - Possible personal Pokemon team data if combat encounter is designed (`[OPEN]`)

30. **Fossil revival system implementation** — `[MEDIUM]`
    - Fossil discovery item placements across Cormoria
    - Fossil item data (most fossils already exist in pokeemerald-expansion baseline; verify Galar mashup fossils)
    - Revival event scripting (player brings fossil to Madame Roma → revival animation/dialogue → Pokemon added to party or PC)
    - Pokemon data for all revived species (most already in pokeemerald-expansion baseline)
    - `[OPEN]` Special Tyrunt fossil event for the Rock Vizier backstory dialogue

31. **The Unified Necropolis Climactic Operation Master Scripting Task** — `[MASTER SCRIPTING TASK — *the largest single engineering task in the project*]`
    
    This task replaces the previously-separate Necropolis Assault + Sword Cult HQ raid tasks (which were merged into a single climactic operation in v0.9.4). The entire Act VI main-story sequence is one continuous scripted production:
    
    - **31a: Outer Necropolis combat sequence** — multi-stage scripted battle sequence; multiple combat encounters with cult Acolytes, Bishops, and possibly named cult lieutenants; ally NPCs (Kimaris with Marshadow at level 100, possibly Brie Moray with Domdaniel, possibly other house representatives, Templar Arceus operatives) fighting alongside the player
    - **31b: Inner Necropolis descent** — player pushes deeper through the mortuary complex toward the Distortion gate chamber; combat continues; environmental atmosphere (lit lanterns, ghost-touched mossy stone, darkened crypts)
    - **31c: Nemo death scene scripting** — finding Nemo dying in the gate chamber's antechamber; final dialogue ("help the prince put an end to this"); Ting-Lu pass to Osrid; Nemo's death animation/cinematic
    - **31d: The 7v9 final battle at the Distortion gate chamber** — two consecutive double battles, no breaks, no healing between them; Baradus Stage 1 + Stage 2 teams; Crabominable conditional dialogue logic if in player party; possibly Keerin in player party if sidequest completed
    - **31e: Silas's psychic-constraint death scene** — Silas's intervention to constrain Baradus; psychic backlash; Silas dies; Pierra is saved
    - **31f: The sealing ritual** — Ting-Lu initiates the sealing; all four Treasures sealed; the Distortion gate is NOT hijacked; Phancero's potential re-emergence pathway is closed
    - **31g: The post-sealing transition** — Osrid presumed dead by Cormoria; physical exhaustion / transient unconsciousness; setting up the Vandras-finds-Veddev epilogue
    
    **This is the production's single most ambitious scripting task** — coordinates 7 sub-sequences across multiple maps, multiple cast members, multi-stage combat logic, dialogue branches, and the cosmologically-weighted resolution beat. **Estimated production effort: 40-60 hours of focused implementation alone, not counting playtesting and iteration.**

32. **Phancero placeholder data** — `[SMALL]`
    - Custom species data entry for Phancero (typing TBD per `[OPEN]` design; possibly Dark/Ghost or Normal/Ghost-mirror)
    - Even though Phancero never appears as a battle opponent, placeholder data ensures any in-game scripted references (Book of the Moon lore text, late-game dialogue) can fire correctly
    - No sprite work required (Phancero is not visually represented in-game)

33. **Vandras epilogue scene update** — `[SMALL-MEDIUM]`
    - Updated dialogue script reflecting the recognition-but-deliberate-non-revelation moment
    - **"Wait...is this..."** — interrupted recognition dialogue
    - Veddev naming ceremony
    - Starter integration (the starter is present, recognizes Vandras, leads Vandras to Osrid)
    - Cinematic framing optional (`[OPEN]`)

34. **In-story Phancero fragment beats** — `[SMALL-MEDIUM]`
    - Dialogue scripting per fragment-moment placement (Cadmus Umbra fairy-tale-level hints, possibly Sable Ashland Ancient Cormoria inscription references, Templar Arceus warnings about Arceus's restraint, Nemo's dying hints about the Treasures, climactic confirmation moment before the 7v9 final battle)
    - These are *fairy-tale level* fragments only — the deep Phancero lore stays in the Book of the Moon for post-game engaged players

35. **Difficulty-mode-aware content gating across the game** — `[MEDIUM — ongoing]`
    - All Keerin sidequest entry points must check the mode flag
    - Optional difficulty-mode-specific dialogue from NPCs (e.g., Cadmus Umbra acknowledging the player's chosen challenge level)
    - Possibly difficulty-mode-specific rewards (Paragon-only rewards beyond Wonder Guard Keerin?) — `[OPEN]` design

### v0.9.7 new engineering tasks (post-character-expansion patch)

The v0.9.7 patch added a parallel main quest, three major character expansions, a new custom move, and a global terminology sweep. These tasks bring v0.9.7 lore to playable reality:

36. **Behemoth Bash custom move implementation** — `[SMALL-MEDIUM]`
    - Overwrite canonical MOVE_BEHEMOTH_BASH data in `src/data/moves_info.h`: 100 BP / 95% acc / Normal physical / 10 PP
    - **New MOVE_EFFECT flag for Steel-effectiveness override** — damage calculator checks: if move has this property and target is Steel-type, multiply final damage by 2× regardless of move's resolved type
    - Damage calculator integration in the type-effectiveness resolution stage
    - Localization (move name + description text, including the special-effectiveness note)
    - Learnset modification: remove from Zamazenta's learnset (Zamazenta does not appear in Ruination); add to Tinkatuff at Lv 30; add to Tinkaton's learnset persistence
    - ~30-40 lines across 4-5 files

37. **Mega-Dreamstone Shard Quest engine support** — `[MEDIUM]`
    - 9 new KEY_ITEM constants: MEGA_DREAMSTONE_SHARD_1 through MEGA_DREAMSTONE_SHARD_9
    - Optional UI key-item display: "Mega-Dreamstone Shards Recovered: X / 9" — `[OPEN]` whether visible to player or tracked silently
    - Reassembled MEGA_DREAMSTONE key-item that auto-triggers when all 9 shards are recovered (or when the player reaches the appropriate climactic moment with all 9)
    - Cinematic / animation for the reassembly moment
    - 9 distinct scripted event sequences for individual shard recovery (each tied to its location-specific narrative beat)
    - Integration with the Section 10 Act VI sealing-cataclysm cinematic — the Mega-Dreamstone is now the explicit catalyst for the sealing ritual

38. **Domdaniel custom Pokemon data — Brie's Trial 8 ace** — `[MEDIUM]`
    - Custom species data for shiny Scream Tail (Past Paradox; Fairy/Psychic; Huge Power)
    - Trial-tier moveset (Champion-tier capability with Brie's age-and-inexperience constraint applied — Domdaniel deployed slightly below Rhydia's-Justice tier)
    - Item assignment, IV/EV optimization
    - Trial 8 battle script integration with Brie's pre-battle and post-battle dialogue
    - Note: Domdaniel was already in the engineering queue (line 5584 / item 14); v0.9.7 upgrades this from "Brie's appearance" to "Brie's primary Trial 8 ace"

39. **Ambrose Caymen NPC and combat data** — `[MEDIUM]`
    - Custom NPC sprite (Archbishop iconography — religious robes with Steel-type heraldic accents); reference asset library for closest match
    - **Temperance** (shiny Kingambit) custom Pokemon data: shiny palette, Champion-tier moveset (Kowtow Cleave / Sucker Punch / Iron Head / Swords Dance likely), held item, IV/EV optimization, Defiant or Supreme Overlord ability
    - **Brunhilda** (shiny female Perrserker) custom Pokemon data: shiny palette, Steel-tier moveset (Iron Head / Throat Chop / U-Turn / Stealth Rock likely), held item, IV/EV optimization, Tough Claws or Steely Spirit ability
    - Rest of Ambrose's Steel-tier roster `[OPEN]`
    - Multi-stage scripted event for the bishop-coup foil → Archbishop fight → clarity-conversion sequence
    - Conditional ally-AI integration for the Necropolis Assault (Ambrose fighting alongside the player at Act VI)
    - Dialogue authoring across multiple appearances (pre-fight indecision, fight, post-fight clarity, recurring ally, Necropolis Assault, possibly Silas-lie-discovery scene)

40. **Female Rock Vizier NPC and combat data** — `[MEDIUM]`
    - Custom NPC sprite (Vizier-tier dignity; Rock-type aesthetic)
    - **Tyrantrum** custom Pokemon data: shiny palette ("regal" visual treatment per Section 7); Vizier-tier moveset (Head Smash / Earthquake / Dragon Claw / Fire Fang likely); held item; IV/EV optimization; Strong Jaw or Rock Head ability
    - Rest of her Vizier-tier roster `[OPEN]`
    - Vizier gauntlet integration (first Vizier fought in Act V; pre-battle and post-battle dialogue)
    - Possibly scripted appearance during the Roma-revival scene if the player witnesses her boyhood-Tyrunt revival in a flashback

41. **Jordan Ramses NPC and combat data** — `[MEDIUM]`
    - Custom NPC sprite (chef-themed; Poison-type accents)
    - Multi-tier Pokemon team data (Jordan's roster scales across his recurring appearances — assassin tier in Act II, reformed-trainer tier in mid-game, Paragon-Gauntlet tier in Act V)
    - Poison-type team composition `[OPEN]` — likely Drapion, Toxapex, Crobat, Gengar, Salazzle, Eternatus(?), etc.
    - Multi-scene scripted event for the cross-purposes encounter with Wakahisa
    - Multiple dialogue beats across his arc — assassin patter, conversion dialogue, recurring-friend dialogue, Paragon Gauntlet pre-battle
    - Optional: chef-vocabulary in his combat dialogue for engaged-player Easter eggs

42. **Wakahisa NPC and combat data** — `[MEDIUM]`
    - Custom NPC sprite (ninja-themed; Bug-type accents)
    - Multi-tier Pokemon team data (Wakahisa's roster scales across recurring appearances)
    - Bug-type team composition `[OPEN]` — likely Scizor, Volcarona, Galvantula, Frosmoth, Centiskorch, Heracross, etc.
    - Multi-scene scripted event for the cross-purposes encounter with Jordan
    - Multiple dialogue beats across the arc

43. **Eden's stolen starter — persistence engineering** — `[MEDIUM]`
    - Engine logic ensuring the stolen starter (species determined by Osrid's pick — see Section 6 type-counter table) is locked to Eden's team across all her appearances
    - Multi-tier scaling: stolen-starter level scales with Eden's appearances (juvenile in Act I, mid-game evolution stage in mid-game, fully-evolved by post-game)
    - Post-game marriage scene must include the stolen starter alongside Osrid's starter — both Pokemon are present at the Paldean wedding
    - Cinematic possibilities for the starter's appearances at key Eden moments

44. **Umbra's third starter — persistence engineering** — `[SMALL-MEDIUM]`
    - Engine logic ensuring the unstolen-third-starter remains with Umbra throughout the game
    - Determined by inverse of Osrid's pick and Eden's steal (the one that was neither picked nor stolen)
    - Scales to Vizier-tier by Act V (Umbra has been raising it across the entire game as a parallel partner)
    - Deployed in the Act V Vizier gauntlet as one of Umbra's Pokemon — possibly his ace or secondary ace

45. **The Tinkaton Matriarch — combat encounter scripting** — `[MEDIUM-MAJOR]`
    - Custom mid-game cave-temple map for the desert/mountain Matriarch's lair
    - Pre-encounter Tinkatink and Tinkatuff trainer battles (the clan defenders)
    - Boss-tier Matriarch encounter — likely above-cap (precedent established by Roaring Moon/Walking Wake)
    - Conditional party-composition dialogue (Arctibax / Tinkatuff / neutral framings)
    - Shard recovery scripted event after Matriarch defeat
    - Single-window event design — the Matriarch returns to sleep after the encounter; the player cannot re-fight her

46. **Trial Baron / Baroness terminology sweep across all `.pory` scripts and dialogue** — `[MEDIUM — ongoing]`
    - Bible sweep is complete (66 occurrences updated); engineering sweep is pending
    - All map scripts referencing "Trial Lord" must be updated to "Trial Baron"
    - Dialogue text containing "Trial Lord(s)" must be updated to "Trial Baron(s)" or "Trial Baroness" as appropriate
    - Item descriptions, key-item flavor text, NPC dialogue, mid-game tutorial text, signpost text
    - Gendering correction throughout: Brie Moray is a Trial Baroness; other current named Trial Barons (Kimaris, Reid, Manus, Nemo) are male; remaining `[OPEN]` Trial Barons should use Baron by default until female Trial Barons are introduced

47. **Supreme Sage → Lunacy rename across engine** — `[SMALL]`
    - ABILITY_SUPREME_SAGE → ABILITY_LUNACY (3 instances, already swept in bible; engine sweep pending)
    - Localization text update: ability name and description
    - Trigger-text updates: any in-game messages that reference the ability by name
    - No mechanical change; pure rename

48. **House Ramses worldbuilding integration** — `[SMALL]`
    - Background NPC dialogue references to the disgraced house (a single Tavern conversation reference, museum signage about the assassination attempt history, etc.) — establishing the worldbuilding without requiring narrative weight
    - Optional: a House Ramses estate ruin or remnant location the player can briefly visit for additional context

### v0.9.8 new engineering tasks (post-merged-PR — session 2)

Session 2 shipped a 27-commit merged PR that completed the starter-line rebalance and landed Joustroll/Jousteel as custom species. The following tasks reflect what changed, what's now LANDED, and what's now newly OPEN at the engine level.

#### Phase 1 starter-line work — STATUS

- **Phase 1 starter-line palettes (Frigibax, Teddiursa Blue Moon, Tinkatink)** — `[LANDED]` via commits `bef7b9f5` / `a984a437` / `8157e896` (Phase 1) plus starter-palette unification `8a6b6ae3` (Phase 2a). Prior task-list entries #3, #4, #5, #6 from earlier patches are superseded by the merged PR's actual deliverables.
- **Phase 1 starter-line shared learnsets (16 moves per line, Lv 1–77)** — `[LANDED]` in session 2.
- **Master Tutor evolution gating for Stage 2 → Stage 3 (Mountain Gale / Blood Moon / Gigaton Hammer)** — `[LANDED]` (engine-side conditional evolution check). Tutor *identities* and *map locations* for the Mountain Gale and Gigaton Hammer tutors remain `[OPEN]` (task #20 above).
- **Joustroll / Jousteel custom species data + sprite binaries** — `[LANDED]` in session 2 (item #28 above is now fully satisfied at the data-tier; House Umbra cultivation encounter logic remains to be scripted in-game).
- **Behemoth Bash Cormorian variant (data + learnset)** — `[LANDED]` in session 2. The engine-override hook is still pending — see task #50 below.

#### New tasks introduced by session 2's deliverables

49. **Engine type-effectiveness override — Behemoth Blade (Fairy override)** — `[SMALL — engine code]`
    - Behemoth Blade is implemented as Dragon-type, 120 BP, physical, 10 PP, learned at Lv 77 by Baxcalibur.
    - The engineering need: damage calculator hook so that against a **Fairy-type** target, the move resolves as super-effective (2×) regardless of the calculated Dragon-vs-Fairy 0× immunity that would otherwise apply.
    - Pattern: parallel to the existing **Freeze-Dry** override (Ice-type move with super-effective override vs. Water).
    - Implementation location: `src/battle_util.c` damage-modifier path; gate via a new `MOVE_EFFECT_*` flag on the move data entry.
    - Localization: move-description text should note the special-effectiveness behavior.
    - Estimated scope: ~30 lines across 2–3 files.

50. **Engine type-effectiveness override — Behemoth Bash (Steel override)** — `[SMALL — engine code]`
    - Behemoth Bash is implemented as Normal-type physical, 100 BP, 95% acc, 10 PP, learned at Lv 30 by Tinkatuff (carried to Tinkaton).
    - The engineering need: damage calculator hook so that against a **Steel-type** target, the move resolves as super-effective (2×) regardless of its Normal-type resolution (including post-Pixilate Fairy resolution).
    - This task supersedes the "New MOVE_EFFECT flag for Steel-effectiveness override" bullet inside task #36 above — that bullet described the same hook; this entry tracks it as standalone post-landing.
    - Pattern: parallel to Freeze-Dry.
    - Implementation location: `src/battle_util.c` damage-modifier path.
    - Estimated scope: ~30 lines across 2–3 files.

51. **Engine type-effectiveness override — Mountain Gale (Water override)** — `[SMALL — engine code]`
    - Mountain Gale is implemented as Ice-type physical, 95 BP, 95% acc, 15 PP, 33% flinch chance, learned by Master Tutor and gating Arctibax → Baxcalibur evolution.
    - The engineering need: damage calculator hook so that against a **Water-type** target, the move resolves as super-effective (2×) — flavoring the Cormorian-engineered ice weaponry as effective against water-bearing foes.
    - Pattern: parallel to Freeze-Dry (the closest existing analogue, also an Ice move with Water-effectiveness override).
    - Implementation location: `src/battle_util.c` damage-modifier path.
    - Estimated scope: ~20 lines (Freeze-Dry pattern is the precedent; this may share infrastructure with #49/#50 if a generic "additional-super-effective-types" array is implemented as the engine pattern).
    - **Cross-task note:** Tasks #49, #50, #51 are structurally identical. They should ideally be implemented as a single generic "additional super-effective types" engine pattern with per-move data, not as three independent hardcoded hooks. Recommend the engineering session implement the generic infrastructure once and apply to all three moves.

52. **Joustroll / Jousteel cry audio** — `[USER-AUTHORED DELIVERABLE]`
    - Both species currently use placeholder cries (`CRY_VAROOM` for Joustroll, `CRY_VOLCANION` for Jousteel) routed through the existing cry table.
    - Need: user-authored cry audio. Cry format is signed 8-bit PCM at 13379 Hz, typically ~0.5–1.0 seconds.
    - Replacement is a data-only change once the audio is recorded: replace the placeholder cry data files under `sound/direct_sound_samples/cries/` and update the cry table entry. No engine code required.
    - **Scope:** audio authoring effort by user; integration is <1 hour.

53. **Trial 4 Joustroll Egg sidequest — event scripting and map work** — `[MEDIUM-MAJOR — scripting + map design]`
    - Narrative is LOCKED in Section 10 (Trial 4 sidequest); engineering implementation is the open work.
    - **Components:**
      - New deep cavern map (Porymap, multi-floor descent with water and ice environmental elements per the Crawdaunt clan presence)
      - Mega Gyarados boss encounter — above-cap precedent (Section 9); needs custom data entry, scripted entry trigger, and unique pre-/post-battle dialogue
      - Crawdaunt-led water-Pokemon clan: ~6–10 trainer battles scattered through the cavern (Crawdaunt, Carvanha, Sharpedo, Basculin, possibly Whiscash, Quagsire)
      - Environmental puzzles — at minimum 2 (water-level manipulation and an ice-platform sequence are the natural fit)
      - Incubation shrine destination map (small, atmospheric, focused on the egg)
      - Egg dialogue beat with two-choice player response gating shiny-vs-normal Joustroll on hatch (engine support exists for `CMD_GIVEEGG` and conditional shiny flag; needs a new wrapper script)
      - Return-to-Cadmus dialogue scene with the locked closing line
      - Cadmus dispatch dialogue at sidequest entry
    - **Cross-references:** Section 7 (Cadmus Umbra entry), Section 9 (Jousteel line entry), Section 10 (Act II/III placement of Trial 4 sequence)
    - **Estimated production effort:** 25–40 hours focused implementation, not counting playtesting.

#### Other session-2 items recorded for completeness

- **Regular Hisuian Ursaluna unobtainability** — engine-side, the Teddiursa → Ursaring → Bloodmoon Ursaluna chain is direct (no intermediate Hisuian Ursaluna). Hisuian Ursaluna species data is preserved for Pokedex completion only; no encounter, no evolution path. No engineering task required — this is the *current* shipped state.
- **Build-pipeline JSON registry for new species** — the build emits informational lines `Unable to find Joustroll in json` and `Unable to find Jousteel in json`. These are non-fatal; the ROM compiles and links cleanly. Some JSON registry expects new-species metadata that hasn't been added. Low-priority follow-up; investigate when convenient. Likely a Porymap species JSON or an asset-pipeline mapping under `tools/` or `data/`.

### Production estimates summary `[UPDATED v0.9.7]`

The v0.9.4 production scope estimate of ~9-16 months of focused FTE development for a tier-one Pokemon ROM hack remains accurate as a baseline.

**v0.9.7 expanded scope adds approximately 1.5-3 months additional FTE:**
- The Mega-Dreamstone Shard Quest infrastructure and 9 individual shard recovery beats (parallel main quest implementation)
- Three new major NPC + combat data sets (Ambrose, Female Rock Vizier, Jordan, Wakahisa stub data)
- Brie's promotion to Trial Baroness 8 with full Trial 8 battle implementation
- Behemoth Bash custom move with Steel-effectiveness override (engine-level new code)
- Tinkaton Matriarch boss encounter
- Eden's stolen-starter and Umbra's third-starter persistence engineering
- Trial Baron terminology sweep across all in-game text (ongoing)
- Supreme Sage → Lunacy rename engine sweep
- Multiple new dialogue beats across the existing acts

**Revised total project estimate:** ~10.5-19 months of focused FTE development for the full v0.9.7-scope project. **The project remains in tier-one ROM hack territory** with the cosmological depth and emotional complexity that distinguishes it from purely-combat-difficulty hacks.

The project's narrative architecture is now substantially complete at the cosmological-and-character level. **Future patches (v0.9.8+) will focus on closing remaining `[OPEN]` items at the level of specific Trial Baron identities, Pokemon team compositions, dialogue refinement, and engineering implementation** — not foundational lore additions.

**Bible document size:** The v0.9.7 bible exceeds 6300 lines, well past the v0.9.3-flagged "becomes unwieldy at ~2500 lines" threshold. **The bible-split into World Bible / Story Bible / Production Bible** (per Section 14's architecture note) is *deferred to v0.9.8* — bundling a structural split with the v0.9.7 content patch would have added risk to the lock. The split should be the first task of the next major patch.

---

*End of v0.9.7. Document will be revised as decisions are made.*

**v0.9.7 patch notes (full):**

**Major character expansions:**
- **Eden promoted to formal deuteragonist status** (Section 7) — stolen starter persists through entire game into post-game marriage; deuteragonist resolution thesis (rivalry → true love through partnership) formally articulated
- **Brie Moray promoted to Trial Baroness of the 8th Trial (Fairy)** (Section 7) — full character expansion with Silas relationship complexity, parents-died-in-accident backstory, Domdaniel as her Trial ace, her direct-speech personality, and the moral-rebellion Fairy specialization
- **Ambrose Caymen as Archbishop of the Arceus Templar** (Section 7) — full character entry; Steel-type master with Temperance (shiny Kingambit) and Brunhilda (shiny female Perrserker); torn-three-ways pre-arc, partnership-through-combat clarity arc, post-arc staunch ally
- **Female Rock-master Vizier locked** (Section 7) — gender, shiny Tyrantrum ace (Roma's girlhood revival), Vizier gauntlet placement; name and portfolio still OPEN
- **Jordan Ramses introduced** (Section 7) — exiled youngest of disgraced House Ramses, Poison/chef-cover assassin, cross-purposes conversion arc with Wakahisa, recurring friend
- **Wakahisa introduced** (Section 7) — foreign-born Bug-type ninja, Goma-hired, cross-purposes conversion arc with Jordan, recurring friend

**Cosmology / Worldbuilding additions:**
- **The Mega-Dreamstone Shard Quest** (Section 9) — parallel clandestine main quest, 9 scattered shards, 2 locations locked (Tinkaton Matriarch's cave + Ambrose's secret holding), 7 OPEN
- **The Tinkatink Line — Cormorian Dragon-Slayer Bloodline** (Section 6) — full lore subsection explaining Cormoria's dragon scarcity through the Tinkaton clan's centuries of dragon-hunting
- **The Tinkaton Matriarch** (Sections 6, 9) — ancient sleeping Pokemon-cosmological-tier longevity, parallel-but-distinct from Cormor's Avalon sleep
- **The Solomonar title** (Section 2) — ancient honorific given twice in 2000 years (first in Cormor's third century with shiny Haxorus, identity forgotten; Glaive is the second)
- **House Nightfall holds the Dark-type Trial Baron seat** (Sections 2, 4) — identity OPEN
- **The Normal-type Trial Baron slot** (Section 4) — type locked; everything else OPEN
- **House Ramses footnote** (Section 2) — disgraced 20 years pre-story by failed Emperor-assassination attempt; surname retained per Arceus-blessing irrevocability rule
- **Templar Arceus order leadership filled** (Section 4) — Archbishop Ambrose Caymen named

**Mechanical locks:**
- **Tinkaton final stats:** 75/85/125/75/125/75 = BST 560 (parity with Bloodmoon Ursaluna)
- **Behemoth Bash custom move** (Section 9) — Normal physical, 100 BP, 95% acc, 10 PP, Steel-effectiveness override regardless of resolved type after Pixilate; learned Lv 30 on Tinkatuff; overwrites Zamazenta's canonical entry
- **The Eden Theft Scene** (Section 6) — type-counter starter steal logic locked; unstolen third starter stays with Umbra and is deployed in Act V Vizier gauntlet
- **Goma's Pokemon team** (Section 8) — Fighting-type specialist (deliberate Baradus-counter); Smolder (shiny Emboar) ace; Mega Houndoom secondary

**Story spine restructure (Section 10):**
- **Vizier gauntlet reordered:** Rock female → Umbra → Silas → Glaive → Rhydia (replaces v0.9.6 Umbra → ??? → Glaive → Silas order)
- **Silas's identity-reveal scene relocated:** Now after Silas's defeat as third Vizier; Silas witnesses Glaive's fight and Rhydia's Champion battle before the unmasking
- **Glaive becomes the final pre-Champion Vizier beat:** partnership-thesis fully realized as the climactic Vizier moment
- **Act II:** Jordan/Wakahisa cross-purposes assassin conversion arc added; mid-game Tinkaton clan side quest added
- **Act I:** Eden theft scene formalized with type-counter logic; Umbra shard-quest briefing locked
- **Act III/IV:** Ambrose-storyline beats added (bishop-coup foil → Archbishop-fight → clarity → staunch ally)
- **Act VI Necropolis Assault:** Named defender list updated to include Ambrose Caymen (Temperance + Brunhilda), Brie Moray (Domdaniel), and Kimaris Langerin (Marshadow at level 100)

**Terminology sweeps (mechanical, two global passes):**
- **Trial Lord → Trial Baron / Trial Baroness:** 66 occurrences swept clean across the bible; engineering sweep across `.pory` scripts and dialogue is pending (Section 14 engineering task #46)
- **Supreme Sage → Lunacy:** 29 occurrences swept (Sections 6, 9, 14); ABILITY_SUPREME_SAGE → ABILITY_LUNACY constant; mechanics unchanged; engineering sweep is pending (Section 14 engineering task #47)

**Design Principles additions (Section 11):**
- **The Three-Redemption-Arc Pattern (Silas / Glaive / Ambrose)** — all three major institutional figures resolve their moral arcs through partnership-thesis combat-demonstration; the project's central thesis applied at the institutional scale
- **Permanent Emotional Complexity Without Resolution (the Silas-Brie axis)** — v0.9.7 demonstration of Section 11 Principle 2; the bible commits to leaving certain relationships unresolved as a deliberate design choice

**Other:**
- Corrected stale v0.9.6 references to "two unnamed Viziers" (only one Vizier portfolio remains OPEN; the Rock Vizier is now characterized)
- Section 13 v0.9.7 closures and new opens documented
- Section 14 v0.9.7 engineering tasks (items 36-48) added
- Document size now ~6500 lines; bible-split deferred to v0.9.8

