<!-- This file is a split-section view derived from dreamstone_ruination_bible_v0.9.7.md (the canonical full bible at the repo root). Lines below correspond to the source lines noted in INDEX.md. Edit the canonical file and regenerate splits — do not edit splits directly. -->

## 13. Open Questions

Consolidated list of decisions deferred but not forgotten. Updated for v0.9.7.

### v0.9.8 closures (engine rebalance and custom-species lock)

The following major opens are now CLOSED in v0.9.8 (the post-merged-PR engine patch from session 2):

- ~~**Trial 4 Joustroll Egg sidequest narrative**~~ — **NARRATIVELY LOCKED in v0.9.8**: Cadmus dispatches the player to a deep cavern; the cavern is overrun by a Mega Gyarados boss flanked by a Crawdaunt-led clan of water Pokemon; the player solves environmental puzzles, defeats the boss, and reaches an incubation shrine where a single Joustroll egg is recovered. Egg dialogue: *"Is it just me or is the egg glowing?"* with a two-choice player response gating whether the hatched Joustroll is shiny or normal. On return to Cadmus, he delivers the line: *"Maybe our Jousteels can even face off in battle one day! Wouldn't that be exciting?"* See Section 10 — Trial 4 sidequest entry. **Event-scripting, map work, and battle scripting remain `[OPEN]`** — narrative is locked; engineering is task #53 in Section 14.
- ~~**Mega Baxcalibur BST distribution**~~ — **PARTIALLY RESOLVED in v0.9.8**: BST 720 confirmed. Constraint locked: Speed > 120 AND Atk > 145. Specific stat distribution still `[OPEN]` pending a stat-design pass.
- ~~**Hisuian (regular) Ursaluna obtainability**~~ — **RESOLVED in v0.9.8**: Hisuian Ursaluna is intentionally unobtainable in Ruination. The Teddiursa line evolves Teddiursa → Ursaring → Bloodmoon Ursaluna directly, gated by the Master Tutor teaching Blood Moon. Hisuian Ursaluna's canonical species data is preserved for Pokedex completeness only. See Section 6 — Teddiursa line evolution chain.
- ~~**Unified starter-trio BST framework**~~ — **RESOLVED in v0.9.8**: All three starter lines now conform to 375 (Stage 1) / 480 (Stage 2) / 600 (Stage 3) with distinct role identities (Frigibax = physical-attacker+speed, Teddiursa Blue Moon = special-attacker apex, Tinkatink = defensive colossus). See Section 6 — starter lines.
- ~~**Lv 77 starter-ace PP convention**~~ — **RESOLVED in v0.9.8**: All Lv 77 starter signature aces normalized to 10 PP (Behemoth Blade / Moongeist Beam / Sunsteel Strike). See Section 6 — starter learnsets.
- ~~**Joustroll & Jousteel full Pokemon data**~~ — **RESOLVED in v0.9.8**: Both species fully implemented as custom species in session 2 — `SPECIES_JOUSTROLL = 1524`, `SPECIES_JOUSTEEL = 1525`. Complete species_info, level-up + teachable learnsets (39 TMs = Varoom + Escavalier union), evolution table (Joustroll → Jousteel at Lv 50), graphics-table registrations, compiled sprite binaries, overworld follower pic tables, Pokedex orderings, category names, descriptions, height/weight. Cry placeholders `CRY_VAROOM` and `CRY_VOLCANION` pending user-authored audio (engineering task #52). See Section 9 — Jousteel line entry.
- ~~**Custom move signature collection**~~ — **RESOLVED in v0.9.8**: Behemoth Blade Cormorian (Dragon, 120 BP, Fairy override TODO), Behemoth Bash Cormorian (Normal, 100 BP, Steel override TODO), Mountain Gale Cormorian (Ice, 95 BP / 95 acc / 15 PP / 33% flinch, Water override TODO), Sunsteel Strike Cormorian (Fire non-STAB, 140 BP, ignoresTargetAbility preserved), Moongeist Beam buffed 100 → 140 BP. Double Slap and Covet retyped Normal → Fairy globally. See Section 9 — custom move subsections. **Engine type-override hooks for the three "override TODO" moves are engineering tasks #49, #50, #51.**
- ~~**Cormorian engineered-weapons twin-pair narrative**~~ — **RESOLVED in v0.9.8**: The thematic conceit that four absent canonical legendaries (Zacian-Crowned, Zamazenta, Lunala, Solgaleo) have their signature moves repurposed as Cormorian-engineered weapons handed to the starter lines. The "Cormorian engineering > legendary gifts" thematic statement of the trio. See Section 9 — Cormorian engineered-weapons twin-pair subsection; cross-referenced in Section 12 — Bloodlines.
- ~~**Trial 4 Trial Baron identity, House, type assignment**~~ — **RESOLVED in v0.9.8 (Trial 4 lock)**: **Trial 4 = Normal-type = House Sylphon = Simone Sylphon** (Trial Baroness, matriarch of House Sylphon, wife of Robard Sylphon who is Chairman of the Sylphon & Stone merchant guild). Forced double battle, level cap ~40, ace **Splendor** (shiny female Obstagoon, custom Fur Coat ability, Body Press / Sucker Punch / Bulk Up / Burning Bulwark, holding Leftovers). See Section 7 — Simone Sylphon for full entry.
- ~~**Trials 5/6/7 type-to-Trial-number assignment**~~ — **RESOLVED in v0.9.8**: Trial 5 = Flying / House Raptora, Trial 6 = Grass / House Alban, Trial 7 = Dark / House Nightfall. Specific Trial Baron identities for all three remain `[OPEN]`.
- ~~**Sylphon & Stone family heads — specific named characters within the guild leadership**~~ — **RESOLVED in v0.9.8**: Chairman **Robard Sylphon** and his wife **Simone Sylphon** are the named heads at story start. Robard's role is operational/commercial; Simone's role is fashion/luxury vertical + social-political network. The Stone branch's family heads remain `[OPEN]`.
- ~~**Sylphon & Stone splintering mechanism**~~ — **RESOLVED in v0.9.8**: Robard's forced resignation following the Act IV cult-funding exposure fractures the guild's organizational structure; continental Sylphon-branch fragments eventually become the 2000-year ancestry of Silph Co. of Kanto. Simone breaks cleanly from the structure by selling her shares and founding a Kalos-based merchant guild on her own terms. See Section 12 — Sylphon bloodline expansion v0.9.8.
- ~~**Ace-bonding overworld interaction pattern as project-level principle**~~ — **RESOLVED in v0.9.8**: Established as a new design principle (Section 11). Scope criterion: any named character with a locked ace Pokémon who appears in the overworld more than once across the story. 23 characters currently qualify; Simone-Splendor is the first full implementation. See Section 11 — Principle: Ace-Bonding Overworld Interactions; Section 14 engineering tasks #55, #56.
- ~~**Baradus's overworld ace identity and treatment**~~ — **RESOLVED in v0.9.8 (Option B)**: Shardik (shiny Beartic, Tough Claws) is Baradus's public-facing overworld ace with weapon-register interactions ("Shardik, cut him down" — emotionless command tone) covering ~95% of his overworld appearances. Guzzlord appears in a *single* late-game hard-to-find private-moment scene where Baradus believes he is unobserved — the only relationship in his life that wasn't a weapon, made briefly visible. The scene deepens his tragedy rather than redeems him. See Section 8 — Baradus entry v0.9.8 update.
- ~~**Goma's overworld ace treatment**~~ — **RESOLVED in v0.9.8**: Both Smolder (shiny Emboar, primary) and Mega Houndoom (secondary) qualify for ace-bonding overworld interactions. Goma's tone is *gruff-fond* with Smolder (war-veteran-with-old-partner register) and *respectful-watchful* with Mega Houndoom (high-discipline weapon she trusts but does not casually pet). The two-ace contrast reveals Goma's moral complexity vs. Baradus's irredeemability. See Section 8 — Goma v0.9.8 update.
- ~~**Sable Ashland's ace identity and combat structure**~~ — **EXPANDED in v0.9.8**: Sable now has a *two-ace structure*. **Solara (shiny male Pyroar, Competitive ability)** is his elder-statesman opener — a childhood gift from the Sylphon family, a twin to Simone Sylphon's female Pyroar (both from the same elite litter). **Gouging Fire (Paradox Past, raised from egg in Ancient Cormoria)** is his successor/cleanup ace — being groomed as the ultimate sweeper. Solara treats Gouging Fire as a much younger sibling; Gouging Fire defers to Solara as a big-brother figure. The size-mismatch is comedic and intentional. See Section 7 — Sable Ashland v0.9.8 update (Sable entry edits pending Q1 and Q2 from this session).
- ~~**Sable + Sylphon childhood friendship**~~ — **RESOLVED in v0.9.8**: Sable Ashland, Simone Sylphon, and Robard Sylphon were childhood friends. The Sylphons gifted Solara (one of two twin Pyroars from an elite litter) to young Sable as a rapport-building gesture. The remaining twin became Simone's own Pyroar (on her Trial 4 team). This establishes new cross-character connective tissue for the Sylphon Exposure beat in Act IV: Sable returns to a Cormoria where one childhood friend (Robard) has fallen into cult-funding compromise while another (Simone) is mid-marriage-crisis.
- ~~**Madame Roma's overworld ace**~~ — **PARTIALLY RESOLVED in v0.9.8**: Roma qualifies for the ace-bonding pattern with a recurring overworld ace. Species and specific combat profile remain `[OPEN]`. Interaction tone locked as *measured, oracular, with surprising flashes of warmth* — the affection of someone who has lived centuries.
- ~~**Blue Moon Hermit's overworld ace**~~ — **PARTIALLY RESOLVED in v0.9.8**: Lethys qualifies for the ace-bonding pattern with a recurring overworld ace. Species and specific combat profile remain `[OPEN]`. Interaction tone locked as *quiet, paternal, gently-curmudgeonly*.
- ~~**Eden's overworld interaction with her stolen starter**~~ — **RESOLVED in v0.9.8**: Eden's interaction *dialog* is constant regardless of which starter she stole; only the *visual sprite* and *cry* assets branch by player pick. Three tone-stages across her arc (early possessive, mid pivot, late unguarded) are the actual content branching. See Section 7 — Eden v0.9.8 update.
- ~~**Boran Surge as anti-pattern character**~~ — **RESOLVED in v0.9.8**: Boran is excluded from the ace-bonding overworld interaction pattern *by intentional design*, not by criterion-fail. His "Pokémon are weapons" philosophy means he has no bonds to demonstrate; the absence is itself characterization. His sole in-game appearance is as a trainer fight inside a PTSD dream sequence experienced by Osrid — custom sprite, custom dream-sequence visual treatment, intentionally unremarkable team. See Section 7 — Boran Surge v0.9.8 update; Section 14 engineering task #58.
- ~~**Sable Ashland's Shiny Charm side-quest battle**~~ — **RESOLVED in v0.9.8 (narrative)**: Second-half-of-game above-cap side-quest battle against Sable's full Fire team led by Solara (opener) and finished by Gouging Fire (cleanup sweeper). Player reward: the Shiny Charm key item. Specific levels, moveset, and additional team members `[OPEN]`. See Section 14 engineering task #57.
- ~~**Trial 5 Baron identity, type, ace, and combat profile**~~ — **RESOLVED in v0.9.8**: Falco Raptora, 100-year-old patriarch of House Raptora (one of the five-oldest noble families). Aces: Sturm (shiny Galarian Zapdos, Defiant) + Drang (shiny male Toucannon, custom Skill Link). Trial team locked (Crobat, Kilowattrel, Cramorant, Mega Aerodactyl). High-risk-high-reward setup-sweep strategy with Lock-On and Tailwind enabling guaranteed-hit signature moves. Trial level cap 41. See Section 7 — Falco Raptora for the full entry; Section 14 engineering tasks #59-63.
- ~~**The covert Resistance Triad existence**~~ — **RESOLVED in v0.9.8**: Cadmus Umbra (strategist) + Nemo Korolev (operator) + Falco Raptora (institutional-reach senior counsel) operate together against both Ruin Cults outside the official Concordance framework. Existence is one of the project's quietest political truths; never spoken aloud in the empire's visible institutions; engaged players piece it together from small consistent observations. Cross-referenced at the tops of Cadmus's, Nemo's, and Falco's entries.
- ~~**Trial Badge naming convention**~~ — **RESOLVED in v0.9.8**: Every Trial Badge will have a name. Trial 5's badge is named **Firmament** (locked). The other 8 Trial Badge names are `[OPEN]` and to be locked per-Trial as the Trial Baron entries are completed. *(Superseded v0.9.9 — all 9 names now locked; see below.)*
- ~~**Player Mega Evolution unlock mechanism**~~ — **RESOLVED in v0.9.8**: The player receives a **Z-Bracelet** from Falco Raptora upon Trial 5 victory; this globally unlocks Mega Evolution capability for the player for the rest of the game. Mega Stones come from the Mega-Dreamstone Shard hunt (parallel-main-quest, Section 4); the Z-Bracelet is the *enabler* that activates them. Pre-Trial-5, the player cannot Mega-Evolve even with Mega Stones in inventory. See Section 14 engineering task #62.
- ~~**Trial level cap structure**~~ — **RESOLVED in v0.9.8**: Trial 1: 18 / Trial 2: 25 / Trial 3: 31 / Trial 4: 36 / Trial 5: 41 / Trial 6: 45 / Trial 7: 50 / Trial 8: 65 / Trial 9: 80 / Vizier Gauntlet & Champion fight: 90 / Necropolis Final Fight: 100. **The Trial 7 → Trial 8 jump is +15 levels (the largest single jump in the Trial sequence).** See Section 4 — Trial Barons listing for full structure.
- ~~**Trial 4 (Simone) specific level cap**~~ — **RESOLVED in v0.9.8**: Trial 4 cap is 36 (per the locked Trial cap structure above; previously approximated as ~40 in earlier batch entries).
- ~~**Sable Shiny Charm sidequest level cap**~~ — **REFINED in v0.9.8**: Early 80s (peer-level for Trial 9 / pre-Vizier-Gauntlet), not above-cap. Per the locked Trial cap structure: Trial 9 cap is 80; Sable's sidequest sits in the 80-83 range as a peer-level fight rather than the L100+ above-cap register of Roaring Moon/Walking Wake at Mt. Ceram.
- ~~**Five-oldest Cormorian noble Houses framework**~~ — **RESOLVED in v0.9.8**: Langerin, Nightfall, Moray, Umbra, Raptora are the five-oldest. Ashland is *about as old* in bloodline terms but came to Cormoria with a pre-existing Naljo family name rather than receiving the empire's formal name-bestowal — they are functionally a sixth ancient House but structurally a *recent-arriving* House. House Raptora's signature empire-services: Braviary mount system (engineered by Raptora; operationalized by Templar Arceus order) + Bombirdier postal/aerial-delivery network (engineered and run by House Raptora directly). See Section 12 — Five-Oldest Houses subsection.
- ~~**Goma's two-ace framing**~~ — **CORRECTED in v0.9.8**: Goma has a *single* bonded ace (Smolder, shiny Emboar). Mega Houndoom is a *combat asset* she Mega-evolves in battle but does not have an overworld ace-bonding relationship with. The v0.9.7-introduced "Smolder + Mega Houndoom two-ace structure" framing was erroneous and is overturned. See Section 11 — Ace-Bonding Overworld Interactions table; Section 8 — Goma entry.
- ~~**Player-driven design over mainline canonicity**~~ — **LOCKED in v0.9.8 as a project-level principle**: When user-specified Pokémon kits, abilities, custom moves, or evolution mechanics diverge from mainline canon, the project implements the user's design. Empire-era Cormoria has its own breeding programs and training traditions that diverge from modern-canon Pokémon traits. The auditor's role is to flag *engine concerns*, not *canonicity concerns*. See Section 11 — Principle: Player-Driven Design Over Mainline Canonicity.
- ~~**Motifs are tools, not templates**~~ — **LOCKED in v0.9.8 as a meta-principle**: Project-level design patterns (two-ace structures, Pokémon-Pokémon overworld relationships, generational defensive aces, bloodline-to-modern-canon descents, etc.) are applied where they best serve the character or story. They are not requirements that must apply to every major character. Examples: Kimaris has only Crowley (no second ace); Goma has only Smolder (Mega Houndoom is a combat asset not a bonded ace); Baradus has inverted two-ace (Shardik public + Guzzlord private, no inter-Pokemon relationship). See Section 11 — Principle: Motifs Are Tools, Not Templates.
- ~~**Deferred locations protocol**~~ — **LOCKED in v0.9.8 as a project-level deferment policy**: Specific geographic and venue specifics in bible entries are intentionally deferred to a dedicated map-design session. Until that session, location-specific decisions are tagged `[OPEN — deferred to map-design session]`. Narrative structure (what happens at each Trial, in what order) remains locked; only *where* is open. See Section 11 — Principle: Deferred Locations Until Map-Design Session.
- ~~**The 5-Glaive-fight ladder structural backbone**~~ — **LOCKED in v0.9.8**: Glaive's character arc is told through 5 on-screen combat encounters across Acts I and II — G1 (Bagon + Turtonator, mid-Act-I), G2 (higher-Bagon + Turtonator + Scraggy, late Act I), G3 (Shelgon + Sandaconda + Turtonator + Scraggy-with-Eviolite, after Trial 3, Act I→II transition; ends with "Something is calling me. Let us meet again."), G4 (same scene as G3 ending — departure line), and G5 (Sandaconda + Scrafty + Turtonator + Dracovish + Shelgon, before Trial 6, with Umbra present; initiates the Hermit-revelation scene). The player observes Glaive's growth in real time via what he brings to each fight — show-don't-tell at its purest. See Section 7 — Glaive arc (restructured v0.9.8).
- ~~**Glaive failure of Garchomp quest as desert-sojourn premise**~~ — **LOCKED in v0.9.8**: Glaive enters the desert between G2 and G3 *pursuing* the legendary Garchomp; he *fails* to acquire it. The failure (combined with the sandstorm rescue by the Hermit and the partnership-training he receives) is what humbles him into the calmer, partnership-coded trainer the player meets at G3. **He returns with Sandaconda (the dragon he met) instead of Garchomp (the legendary he chased).** The Sandaconda's presence at G3 is the player-observable diagnosis of what the desert taught him.
- ~~**Trial 6 chapter onset structural lock**~~ — **LOCKED in v0.9.8**: Player arrives in Alban region → G5 Glaive fight with Umbra present → post-fight Glaive-Umbra-Osrid Hermit-revelation conversation → Hermit-quest unlock → Hermit ritual scene → dream-Boran trauma fight → starter Stage-2 → Stage-3 evolution → return to Alban region for Trial 6 Baron fight. The Trial 6 Baron identity remains `[OPEN]` per the deferred-content protocol. See Section 14 — Trial 6 chapter onset sequence; Section 14 engineering tasks #58 (refined), #64, #65.
- ~~**Starter Stage-2 → Stage-3 evolution mechanism**~~ — **LOCKED in v0.9.8**: The starter evolves to its Stage-3 600 BST form **via the Blue Moon Hermit's partnership-readiness ritual**, not via a level-up gate. The ritual triggers the dream-Boran trauma fight; victory in the fight triggers the Hermit teaching the signature gating move (Mountain Gale / Blood Moon / Gigaton Hammer); the starter then evolves *at whatever level it is currently at*. **Ritual-gated, not level-gated.** Loss does not punitively gate progression; the player retries until victorious. This is the project's tightest mechanical-narrative weld — the combat victory IS the psychological renunciation IS the evolution unlock. See Section 11 — Mechanical-Narrative Welds principle; Section 6 — starter evolution mechanics; Section 14 — Trial 6 chapter onset.
- ~~**Boran Surge PTSD dream-sequence placement**~~ — **LOCKED in v0.9.8**: Previously `[OPEN]` placement; now locked at the Trial 6 chapter Hermit-ritual gating event. Boran's only on-screen appearance. The dream-fight is the partnership-readiness ritual's *content* — the player demonstrates renunciation of "Pokémon as weapons" by defeating its avatar. See Section 7 — Boran Surge v0.9.8 update; Section 14 engineering task #58 (refined v0.9.8).
- ~~**"The chosen partner of Cormor's Legacy" cosmological phrase**~~ — **LOCKED in v0.9.8**: The Blue Moon Hermit speaks this phrase when describing the three lost moves (Mountain Gale, Blood Moon, Gigaton Hammer) to Glaive during the desert sojourn. Glaive recounts the phrase to Umbra and Osrid at the Trial 6 chapter onset G5 scene; **only Umbra and Osrid immediately catch its meaning** — the player's starter is the chosen partner of the empire's founding figure, Cormor. The phrase resonates forward to Mt. Ceram (Act III) and the Hall of Fame moment. *Show-don't-tell:* Glaive thinks it's babbling; the player sees Umbra's and Osrid's faces register recognition. See Section 14 — Trial 6 chapter onset; Section 1 — Cormor.
- ~~**Mechanical-Narrative Welds**~~ — **LOCKED in v0.9.8 as a project-level design principle**: When a mechanical gate exists in the project (player can or cannot progress past X), and when a narrative beat exists at the same point (player demonstrates Y), design them as *the same event*. The mechanic IS the narrative. Paradigmatic example: the Trial 6 chapter onset Hermit ritual + dream-Boran fight + starter Stage-3 evolution — three layers welded into a single event. Other examples: Crabominable adoption mechanic, Sable Shiny Charm sidequest, Z-Bracelet acquisition at Trial 5, Trial 4 doubles-only format. See Section 11 — Principle: Mechanical-Narrative Welds.
- ~~**Hermit as passive witness to the trauma ritual**~~ — **LOCKED in v0.9.8**: The Hermit's role in the partnership-readiness ritual is *acknowledgment*, not orchestration. The ritual surfaces what Osrid carries; the Hermit witnesses what Osrid does in response and honors it. This preserves the Hermit's gentle paternal character register from Section 7 — Blue Moon Hermit. The Hermit does not *cause* the trauma; the ritual *reveals* it; the Hermit *acknowledges* the player's response. See Section 14 — Trial 6 chapter onset.
- ~~**Dream-Boran starter-aware dialog branching**~~ — **LOCKED in v0.9.8**: One fight, same structure across all three starter paths; dialog references the starter-specific signature move being unlocked (Mountain Gale / Blood Moon / Gigaton Hammer per starter). Asset-light branching parallel to Eden's interaction model (Section 7 — Eden v0.9.8 lock). See Section 14 engineering task #58 (refined).
- ~~**Trial 7 Baron identity, type, ace, and combat profile**~~ — **RESOLVED in v0.9.8**: Bridget Nightfall, 30-year-old matriarch-by-default of declining House Nightfall; Osrid and Rhydia's first cousin (daughter of Eldred's older brother Dantalion). Ace: Grendel (shiny Grimmsnarl, custom Tangling Hair, Beat Up speed-control monster). Team built on speed control + relentless pivoting (Sharpedo Speed-Boost-Baton-Pass) + multiple sweepers (Mega Absol, Zweilous). Trial level cap 50. Very hard 6v6 single battle. See Section 7 — Bridget Nightfall; Section 14 engineering tasks #66-67.
- ~~**The Trial 7 family-reveal emotional climax**~~ — **LOCKED in v0.9.8**: After defeating Bridget, Osrid whispers something unheard and lifts his mask; Bridget breaks down crying and embraces him, regaining her heart and will to fight. She is the third person to learn Osrid's identity (after Umbra and Rhydia). Flagged as the project's flagship **Show-Don't-Tell directness exception** (Section 11). The whisper content stays permanently unheard. See Section 7 — Bridget Nightfall; Section 14 — Trial 7 chapter.
- ~~**The Nightfall family tree**~~ — **LOCKED in v0.9.8**: Mordred Nightfall (patriarch, former 50-year Champion defeated by 15-year-old Rhydia; childhood friend and lifelong rival of Falco Raptora) → sons Eldred (Prince-Consort, assassinated by Baradus) and Dantalion (the once-chosen heir, humiliated by Eldred's public defeat, self-exiled as Kalos diplomat, never on-screen) → Dantalion's wife Leah Alban Nightfall (married in from House Alban) → daughter Bridget (Trial 7 Baroness). See Section 6 — extended Nightfall family; Section 12 — Five-Oldest-Houses Nightfall bullet.
- ~~**The Falco-Mordred generational parallel**~~ — **LOCKED in v0.9.8**: Falco Raptora and Mordred Nightfall are childhood friends and lifelong rivals, the two strongest trainers of their generation, both with immense vitality. Deliberate authored mirror — two patriarchs of two five-oldest Houses, two failure modes of the same generational position (Falco clings / refuses to retire; Mordred collapsed / was forced out by Rhydia and watched his House decline). See Section 6 — Mordred; Section 12 — Nightfall bullet.
- ~~**Eldred's assassination as Widening-Eye-splintering catalyst**~~ — **LOCKED in v0.9.8**: While the Treasures' competing alignments were the underlying cause of the Widening Eye's four-way split, Baradus's assassination of Eldred Nightfall 10 years pre-game was the *triggering historical event* that broke the order open all at once and catalyzed the Swords of Ruin's rise. Layered onto (not replacing) the existing theological-cause framing. See Section 8 — Widening Eye origin.
- ~~**Glaive's identity-reveal timing**~~ — **CORRECTED in v0.9.8**: Glaive learns Osrid's identity *only* at the Vizier-of-War final fight before the Champion (when Glaive has his full team — `[OPEN]`). This is much later than previously framed ("mid-game major event"). Full reveal order: Umbra (always) → Rhydia (post-Trial-2 / ~50% Sword Cult encounter) → Bridget (Trial 7) → Glaive (Vizier-of-War fight, Act V). See Section 7 — Glaive arc point 11 (corrected); Section 14 — story spine Glaive references (corrected).
- ~~**ERROR FIX: "the unseen Champion's twin"**~~ — **CORRECTED in v0.9.8**: Rhydia's entry header in Section 6 previously read "the unseen Champion's twin," which was nonsensical — Rhydia is the *reigning, visible* Champion; *Osrid* is the hidden/unseen one (the masked Rainhawk). Corrected to "the empire's pride, the reigning Champion, the hidden prince's twin." See Section 6 — Rhydia entry header.
- ~~**ERROR FIX: Rhydia's Champion acquisition was undocumented**~~ — **CORRECTED in v0.9.8**: Rhydia's entry previously did not record *how* she became Champion. Now locked: she won the seat 5 years pre-game by defeating her grandfather Mordred Nightfall (the 50-year reigning Champion) at age 15. The Kimaris-Marshadow match (2 years pre-game) is a separate Champion's-*defense* match, not the acquisition. See Section 6 — Rhydia brief summary.
- ~~**Trial 6 Baron identity, type, ace, and combat profile**~~ — **RESOLVED in v0.9.8 (the last open Trial Baron seat — all 9 now named)**: Indrid Alban, scion and Trial Baron of House Alban, a Grass-type prodigy of the newest generation (peer of Osrid/Rhydia/Bridget) corrupted by Wo-Chien into massacring his own family. Ace: Nero (shiny Scovillain, Grassy Surge; adoptable by the player). Team: Sinistcha, Arboliva, Ludicolo, Breloom, Mega Venusaur. Trial cap 45. Badge: Verdant. See Section 7 — Indrid Alban; Section 14 — Trial 6 culmination; Section 14 engineering tasks #68-70.
- ~~**The Trial 6 horror sequence**~~ — **LOCKED in v0.9.8**: The project's most horror-tinged chapter. Decayed Alban estate, vine-puppeted reanimated family corpses, crazed Indrid in the Greenhouse. After defeat, Indrid tosses the Verdant Badge, has a lucid moment, then is devoured by Wo-Chien (player's first in-the-flesh Treasure-of-Ruin sighting). Baradus arrives to retrieve Wo-Chien; cooperative Glaive double-battle vs two cultists; Baradus re-contains Wo-Chien and flees; player may adopt Nero. See Section 7 — Indrid Alban; Section 14 — Trial 6 culmination.
- ~~**Indrid as the dark mirror of Osrid**~~ — **LOCKED in v0.9.8**: The Osrid/Indrid near-rhyme is intentional. Both are same-generation prodigies with darkness in their hearts that a Treasure-aligned force could exploit. The difference is who caught them — Osrid was protected (Umbra, the Hermit, the network around him) and overcame his Boran-planted darkness at the Hermit ritual *immediately preceding* this sequence; Indrid was caught by Wo-Chien and his darkness bloomed into the massacre of everyone he loved. Indrid is what Osrid could have become. The project's thesis rendered as horror.
- ~~**The two-phase Alban compromise + Neven's name + Wo-Chien Greenhouse staging**~~ — **LOCKED in v0.9.8**: Phase 1 — Harbinger Neven's Tablets Cult infiltrated House Alban as a "partner" agricultural company + direct investor, extracted critical Wo-Chien knowledge from the family's libraries, and used it to incarnate Wo-Chien at Hoya River (then Baradus slaughtered them and seized it). Phase 2 — Baradus planted the seized Wo-Chien in the Alban Greenhouse (a convenient Grass-type containment site, family already softened up) to destroy the troublesome family and corrupt the prodigal heir; he retrieves it during the Trial 6 chapter, never having lost possession. "Neven" locked as the Tablets Harbinger's name (filled the prior `[OPEN]`). Consistent with the locked Wo-Chien-since-before-game-start lore. See Section 8 — Tablets Cult / Wo-Chien custody; Section 7 — Indrid Alban.
- ~~**The Nero adoption weld**~~ — **LOCKED in v0.9.8**: After Wo-Chien devours Indrid, the player may adopt Nero (shiny Scovillain, doubly-traumatized — first by Wo-Chien's influence as the massacre weapon, then by watching Wo-Chien devour the trainer it grew up with). A Crabominable-style partnership weld — the player completes the reach toward connection Indrid was making when devoured. Nero arrives as-raised; species hidden ability set to Intimidate so Grassy Surge → Intimidate is reachable via Ability Patch. See Section 7 — Indrid Alban; Section 11 — Mechanical-Narrative Welds.
- ~~**Cooperative Glaive double-battle at Trial 6 climax**~~ — **LOCKED in v0.9.8**: Distinct from the five versus-Glaive fights (G1-G5). Glaive fights *alongside* the player (his G5 roster) vs two Sword cultists after Indrid's devouring. Glaive thus bookends the Trial 6 chapter — G5 versus-fight at the onset (triggering the Hermit revelation), cooperative ally-battle at the climax. See Section 7 — Glaive; Section 7 — Indrid Alban; Section 14 engineering task #70 (cooperative-ally double-battle engine support).
- ~~**Verdant Badge**~~ — **LOCKED in v0.9.8**: Trial 6 badge name = Verdant. (Second Trial Badge name locked, after Firmament/T5. Other 7 still `[OPEN]`.)
- ~~**All 9 Trial Barons named**~~ — **MILESTONE in v0.9.8**: With Indrid Alban (Trial 6) locked, all nine Trial Barons are now named and have at least their ace + core profile locked: Kimaris Langerin (1/Ghost), Reid Ashland (2/Fire), Manus Surge (3/Electric — fully locked v0.9.9), Simone Sylphon (4/Normal), Falco Raptora (5/Flying), Indrid Alban (6/Grass), Bridget Nightfall (7/Dark), Brie Moray (8/Fairy), Nemo Korolev (9/Ground).
- ~~**Kimaris Langerin substantial expansion — Reserve Champion + full personality + supporting team**~~ — **LOCKED in v0.9.8**: Kimaris's prior "former Champion" framing was a factual error — he is Cormoria's designated **Reserve Champion**, never having held the seat. He earned the designation 8 years pre-game by defeating all four Viziers in succession and tying with Champion Mordred Nightfall, then voluntarily renouncing the Champion seat for the Trial Baron + Langerin patriarchy. **The formal decree was issued by 12-year-old Princess Regent Rhydia Cormoria as her first major act as acting authority** — structurally significant in her backstory. Personality, vocation (spiritualist + sorcerer + exorcist), Templar Arceus consultancy with Ambrose, lifelong academy friendship with Cadmus Umbra (with Cadmus's deliberate Triad-compartmentalization of Kimaris as risk mitigation), Trial 1 team (Crowley + Dusclops + Shedinja + Honedge + Gastly + Dhelmise — stall-and-Curse-residual architecture), goofy-affectionate-baby-voice register with Crowley (the project's earliest Show-Don't-Tell partnership-thesis demonstration), and the post-Champion side quest with Kimaris's true Marshadow-led team — all locked v0.9.8. See Section 7 — Kimaris Langerin.
- ~~**Wraith Badge — Trial 1**~~ — **LOCKED in v0.9.8**: Trial 1 badge name = Wraith. Three Trial Badge names now locked (Wraith/T1, Firmament/T5, Verdant/T6); five `[OPEN]`.
- ~~**Haywire Badge — Trial 3**~~ — **LOCKED in v0.9.9**: Trial 3 badge name = Haywire — fitting the Electric trial and House Surge. Four Trial Badge names now locked (Wraith/T1, Haywire/T3, Firmament/T5, Verdant/T6); four `[OPEN]`.
- ~~**Final 5 Trial Badge names**~~ — **LOCKED in v0.9.9**: Smelt/T2 (Reid/Fire — volcanic refining), Nonpareil/T4 (Simone/Normal — "no equal," exceptions to the norm), Gloaming/T7 (Bridget/Dark — twilight, fading house), Glamour/T8 (Brie/Fairy — fae enchantment), Upheaval/T9 (Nemo/Ground — tectonic + the Usurper's political upheaval). **All 9 Trial Badges are now named:** Wraith/T1, Smelt/T2, Haywire/T3, Nonpareil/T4, Firmament/T5, Verdant/T6, Gloaming/T7, Glamour/T8, Upheaval/T9.
- ~~**The 12-year-old Rhydia Kimaris-decree as her first major Regent act**~~ — **LOCKED in v0.9.8**: 8 years pre-game, after Kimaris tied Mordred and renounced the Champion seat, the formal decree recognizing his renunciation + Trial Baron seat + Langerin patriarchy (over his two older brothers) was issued by 12-year-old Princess Regent Rhydia Cormoria. This was her first major act as acting authority of the empire — a structurally significant event in her backstory. See Section 6 — Rhydia summary; Section 7 — Kimaris Langerin.
- ~~**Kimaris's older brothers Dale and Gram Langerin**~~ — **LOCKED in v0.9.8**: Kimaris's two older brothers, the first and second sons of the previous Langerin patriarch. Minor characters; lesser Ghost trainers the player fights as opening encounters in the Mirroh Necropolis before reaching Kimaris. Their succession was supplanted by Rhydia's age-12 decree elevating Kimaris over them; they have accepted it.
- ~~**Cadmus-Kimaris academy friendship + deliberate Triad compartmentalization**~~ — **LOCKED in v0.9.8**: Cadmus Umbra and Kimaris Langerin grew up together at the academy and have been lifelong dearest friends. Kimaris's reverence for Cadmus is near-fanatical. Despite this, Cadmus deliberately compartmentalizes Kimaris out of the Resistance Triad's operational core (Kimaris is adjacent, not in) as risk mitigation — Kimaris's institutional exposure makes him a high-value cult-compromise target, and the Triad's existence must survive any possible Kimaris compromise. Kimaris does not know he is being compartmentalized. Mirrors the pattern with Bridget Nightfall (also Cadmus's individual contact, also kept structurally outside the Triad). See Section 7 — Cadmus Umbra; Section 7 — Kimaris Langerin.
- ~~**Templar Arceus / Langerin exorcist consultancy — the three-way institutional infrastructure web**~~ — **LOCKED in v0.9.8**: Archbishop Ambrose Caymen regularly calls on Kimaris Langerin and the Langerin family's top mediums to handle hauntings and supernatural phenomena beyond the lesser Templar priests' capability. This is an ongoing institutional relationship long predating the late-game Necropolis Assault — the Assault alliance is the late-game escalation of years of working institutional partnership. **The empire's senior institutional web (v0.9.8 framework):** House Raptora engineered the Braviary mount system; the Templar Arceus order operationalizes it + the daily religious-civic infrastructure; House Langerin handles supernatural-affairs consultancy beyond lesser-priest capability. Three old institutions, three complementary specialties. See Section 7 — Kimaris Langerin; Section 7 — Ambrose Caymen.
- ~~**Kimaris's post-Champion true-team side quest**~~ — **LOCKED in v0.9.8 (concept; design OPEN)**: Kimaris's actual best play (Marshadow-led true team) is a post-Champion final-act side quest, NOT the Trial 1 fight. Parallel structural pattern to Sable Ashland's Shiny Charm side quest. Specific team composition, levels, items, dialog, and reward all `[OPEN]` — design deferred to a future session. See Section 14 engineering task #72.
- ~~**Reid Ashland substantial expansion — personality, voice, pyrokinesis, sisters, full team, scholar arc**~~ — **LOCKED in v0.9.8**: The Trial 2 Baron entry was thin; substantial v0.9.8 expansion adds personality (confident-with-cracks, good-natured, dreams beyond combat, believes Sable is alive and is "placeholder" for him), Heatran name **Phlegein** + 4th move **Scorching Sands**, full Trial 2 team (Phlegein + Magmar + Coalossal + Charmeleon + Arcanine + Torkoal — sun-architecture with three burn vectors and triple win conditions), pyrokinesis lore (Reid + Sable are the only modern Ashlands with active fire-conjuring power), three sister names (Rain, Brook, River — none pyrokinetic), the Mt. Ceram pyrokinesis scene (Reid burns cultists to save sisters), the family-history-irony of the treason suspicion, and the locked scholar-arc retirement with team intact (Reid loves them all too much to ever let any of them go). See Section 7 — Reid Ashland for the full entry; Section 12 — House Ashland Naljo expansion; Section 14 — Mt. Ceram raid pyrokinesis scene; Section 14 engineering tasks #73-74.
- ~~**The Naljo cast-out reason and House Ashland pyrokinesis**~~ — **LOCKED in v0.9.8**: Varaneous (one of several major legendaries guarding Naljo's wild lands) demanded the Ashland family use their literal pyrokinetic power to enforce his isolationist violence — directing them to launch fireballs at incoming ships and to mobilize as enforcers who would burn dissenters alive. The Ashland family refused. **The cast-out was the consequence of moral refusal.** This single refusal is the foundation of House Ashland's identity across all subsequent generations. Pyrokinesis has diminished across most modern branches; succession follows strict pyrokinetic-strength rules; Reid and Sable are the only living modern Ashlands with active powers. See Section 12 — House Ashland Naljo backstory expansion.
- ~~**The House Ashland treason-suspicion historical irony**~~ — **LOCKED in v0.9.8**: The post-Eldred slander that "House Ashland probably helped assassinate Eldred Nightfall" is *inverted from the family's actual character*. Most Cormorians don't know the Ashland Naljo history; they slander the family without knowing what they're getting wrong — *the family that fled Naljo specifically to avoid being made instruments of violence against innocents* is now suspected of having abetted exactly such violence. **The historical ignorance is itself part of the tragedy.** See Section 7 — Reid Ashland; Section 12 — House Ashland Naljo expansion.
- ~~**Reid's three younger sisters: Rain, Brook, River Ashland**~~ — **LOCKED in v0.9.8**: All three lack pyrokinetic powers (which is *why* succession fell to Reid by family rule). The water-themed sister names against Reid's non-water name are the family's quiet open secret about who carries what gift. Specific ages and personalities `[OPEN]`. They appear on-screen meaningfully during the Mt. Ceram raid pyrokinesis scene.
- ~~**Phlegein the shiny Heatran — name and 4th move**~~ — **LOCKED in v0.9.8**: Heatran's name is **Phlegein** (Greek φλέγειν, "to blaze / to burn") — distinct register from Kimaris's Western-occult "Crowley" naming; Ashland tradition pulls from classical Greek/Latin per the family's "divine family of Fire magic users" Naljo origins. Phlegein's 4th move is **Scorching Sands** (Ground-type special, 30% burn) — closes the Heatran kit's coverage gaps and pairs with Earth Eater (Ground-immune ace with Ground-coverage offense = asymmetric defense).
- ~~**Reid's pyrokinesis Mt. Ceram raid scene**~~ — **LOCKED in v0.9.8 (narrative; engineering OPEN)**: Player witnesses Reid burn Beads cultists alive to save his sisters, arriving moments too late for conventional Pokemon-battle resolution to prevent it. **The first moment in the game where the partnership thesis fails in real time** — not because it's wrong, but because real violence sometimes outruns it. Flagged as Show-Don't-Tell directness exception (Section 11). Quiet aftermath (Reid does not celebrate, says little). One of the very few on-screen instances of a sympathetic main character killing humans directly — tonal-threshold scene. See Section 14 engineering task #74.

#### v0.9.8 explicit retcon — Glaive-Hermit sandstorm rescue timing

This is the project's first explicitly-documented retcon of a prior version's lock, recorded here so future bible readers and future sessions see the correction in the closure log rather than discover it through file-diff archaeology.

- ~~**Glaive-Hermit sandstorm rescue timing**~~ — **RETCONNED v0.9.7-or-earlier → v0.9.8**: The v0.9.4 framing placed the Hermit-Glaive sandstorm rescue and partnership-training in Glaive's *pre-game wandering years* during Osrid's overseas service. **v0.9.8 corrects this to an on-screen event during the early game** — Glaive's desert sojourn between fights G2 and G3 (during his failed pursuit of the legendary Garchomp). The rescue is *contemporary*, not historical; Glaive's recounting at the Trial 6 chapter onset (Section 14 — Trial 6 chapter G5 scene) is therefore a *recent transformation* he is describing, not a buried memory.
  - **What changes:** the *timing* of the Hermit-Glaive event. Glaive starts the game as a *fledgling* Dragon Master (Bagon + Turtonator only), not a previously-Hermit-trained one. His full team is built up *across the on-screen five-Glaive-fight ladder*, fight by fight. Sandaconda specifically is acquired during the desert sojourn between G2 and G3, alongside the Hermit rescue and the Bagon→Shelgon evolution. **The player observes Glaive's growth in real time**, rather than being told about pre-game development.
  - **What survives unchanged (structural significance preserved):**
    - The Hermit gave Glaive partnership-training that enabled Bagon→Shelgon
    - The Hermit recognized Glaive's psychic-empathic gift before Cadmus Umbra did
    - Cormoria's dragon-tradition is, at its root, downstream of the Hermit's teaching
    - The cross-canon Lance/Blackthorn City descent through Glaive's Dragon's Den order is unchanged
    - The Hermit's broader role as the project's master partnership-teacher is unchanged
    - The Trial 6 chapter onset G5 scene (Glaive recounting the Hermit story to Umbra and the player, leading to the Hermit-quest unlock) is unchanged in *structure* — only the *register* of Glaive's recounting changes from "buried-history" to "recent-transformation."
  - **Files updated in v0.9.8 to enact the retcon:** `bible/07_characters_viziers.md` (Glaive arc fully restructured), `bible/11_characters_legendary.md` (Hermit Function-2 entry rewritten), `bible/15_design_principles.md` (Glaive's-overworld-interactions reference corrected), `bible/17_open_questions.md` (v0.9.4 RESOLVED entry annotated + this explicit retcon entry added). See git history for the consistency-repair commit.
  - **Why the retcon:** the on-screen real-time framing aligns better with the project's *show-don't-tell* writing principle (Section 11 — Principle: Show, Don't Tell, locked v0.9.8). The player observes Glaive's transformation through *what he brings to combat across five fights* rather than being told about it via exposition. This is one of the clearest applications of the show-don't-tell principle in the project's character architecture.

### v0.9.8 new opens

These items emerged from v0.9.8 lock work and are deferred:

- **Mega Baxcalibur specific stat distribution** within the BST 720 + Speed>120 + Atk>145 constraint
- **Cadmus's personal Jousteel battle spec** (moveset, item, ability) for the Vizier-gauntlet encounter — `[OPEN]`
- **Engine type-override implementation pattern** — three damage-calc hooks (Behemoth Blade Fairy, Behemoth Bash Steel, Mountain Gale Water) parallel to existing Freeze-Dry pattern; engineering task #49–51
- **Joustroll/Jousteel cry audio** — user-authored deliverable; placeholders in place
- **Trial 4 Joustroll Egg sidequest event scripting** — map design, boss encounter, puzzle implementation, dialogue scripting; lore locked, engineering `[OPEN]`
- **Build-pipeline JSON registry for new custom species** — the compile log emits non-fatal "Unable to find Joustroll/Jousteel in json" lines; the build still succeeds but a JSON metadata file expects entries that haven't been added. Low priority; investigate when there's slack.
- **Trial 5, 6, 7 Baron identities** (Raptora, Alban, Nightfall) — type-to-Trial assignment locked v0.9.8; specific Baron names, aces, levels, team compositions, narrative roles all `[OPEN]`
- ~~**Manus Surge's ace, full team, level cap specifics**~~ — **RESOLVED v0.9.9**: ace **Modal** (shiny Toxtricity, Poison Puppeteer, Air Balloon); full 6-Pokémon singles matchup-judgment team locked at cap 31; full character profile, House-Surge schism, the Modal bond beat, and pre/post-Trial dialogue all locked. See Trial Baron profiles — Manus Surge.
- **Cadmus Umbra's overworld attendant Joustroll** — separate from his ace Jousteel; engineering and dialog beats `[OPEN]` (cross-ref: Section 9 — Joustroll/Jousteel Line)
- ~~**Silas Moray's primary ace species/name**~~ — **RESOLVED v0.9.9**: **Thauma** (shiny Hisuian Braviary, Psychic/Flying, Tinted Lens) is his **primary ace** in the Act V Vizier gauntlet; **Malamar** (Dark/Psychic, Contrary) is the backup ace. Full mind-domination team locked in Section 7 — Hypno, Galarian Slowking, Gallade, and Hatterene round it out.
- ~~**Female Rock Vizier name, House, Vizier portfolio**~~ — **RESOLVED v0.9.9**: **Zeldra Stone, House Stone, Vizier of Infrastructure** (Section 7 — Zeldra Stone). Ace **Regis** (blue shiny ♂ Tyrantrum, Strong Jaw); full Elite-Four-tier mono-Rock hazard/sand team locked (Regis, Tyranitar, Omastar, Probopass, Coalossal, Garganacl). **Also locked v0.9.9 in the same arc:** **Gideon Valic** (deceased previous Vizier of War, Glaive's adoptive father, assassinated by Baradus ~1yr pre-game — Section 7); **Glaive Valic** surname + foundling origin + vengeance-source — Section 7; **Northpoint Military Academy** + **ECTI** named institutions — Section 1; **Baradus's Chien-Pao radicalization** + the Ice-vs-Rock blind spot — Section 12.
- **Madame Roma's overworld ace species/name/combat profile** — qualifies for ace-bonding pattern; specifics `[OPEN]`
- **Blue Moon Hermit's overworld ace species/name/combat profile** — qualifies for ace-bonding pattern; specifics `[OPEN]`
- ~~**Jordan Ramses's full Poison-type team and named ace**~~ — **RESOLVED v0.9.9**: ace **Naga** (shiny ♀ Seviper, Multiscale); full mono-Poison team locked across all three fights (Naga, Fezandipiti, Toxapex, Toxicroak, Drapion, Amoonguss). See Section 7 — Jordan Ramses.
- ~~**Wakahisa's full Bug-type team and named ace, gender, foreign-origin country**~~ — **RESOLVED v0.9.9**: female; Johto shinobi-clan exile; ace **Hayate** (shiny ♂ Ninjask, Speed Boost); full Bug team locked across all three fights (Ninjask, Accelgor, Mega Beedrill, Durant, Frosmoth, Volcarona); relationships locked (brother-bond with Jordan, closeness with Eden, romance with Glaive → leaves for Johto). See Section 7 — Wakahisa.
- **Robard Sylphon's appearance, combat capability, post-exposure fate** — `[OPEN]` whether he appears on-screen, whether the player ever battles him, where he is after his forced resignation from Sylphon & Stone
- **Sable's post-Act-IV scene with Simone** (childhood friend reckoning with her marriage crisis) — `[OPEN]` whether on-screen, off-screen, or absent
- **PTSD dream sequence specific placement and triggering conditions** for Boran Surge fight — Section 14 task #58 `[OPEN]`
- **Late-game Guzzlord private-moment scene** — specific location, triggering conditions, dialog (if any) — Section 14 task #56.16 `[OPEN]`


**Trial 4 (Simone Sylphon) follow-up opens:**

- ~~**Trial 4 specific level cap number**~~ — **RESOLVED in v0.9.8** by the locked Trial cap structure (Trial 4 cap = 36). The prior interpolation note ("between Trial 3 35-40 and Trial 8 50-55") used stale per-Trial cap numbers that predated the locked v0.9.8 ladder; both endpoints are corrected by the ladder closure above. See Section 4 — Trial level cap structure.
- **Held items for Simone's 5 non-Splendor team members** (Hisuian Zoroark, Bewear, Grafaiai, Pyroar, shiny Farigiraf) — `[OPEN]`
- **IV/EV optimization and natures** for the 5 non-Splendor team members — `[OPEN]`
- **Robard Sylphon's appearance in the story** — does he appear in person, or remain offscreen as a referenced absent partner? If onscreen, in what scenes (palace functions? Act IV exposure scene? a confrontation with Simone post-exposure?). The fact that he raised three of Simone's Trial team Pokémon strongly implies he *is* a trainer; whether the player ever battles him is `[OPEN]`
- **Robard's combat capability and roster** — `[OPEN]` if he ever appears in combat
- **Specific Act IV Sylphon & Stone exposure scene scripting** — the moment Simone learns the full scale of Robard's compromise; the public revelation; the political-fallout scenes; the Simone-Robard private scene(s) following the public exposure — all `[OPEN]`
- **Whether Simone reappears in any Act V or Act VI scenes** before her Kalos departure — `[OPEN]`
- **Trial 4 chapter-specific geography** — the city or region where House Sylphon's seat is located — `[OPEN]`
- **Whether the player has any pre-Trial-4 social encounter with Simone** in a court or fashion-event setting — `[OPEN]`
- **Stone-branch family heads of Sylphon & Stone** — Robard's Stone-side counterpart who eventually produces the Devon Corporation lineage — `[OPEN]`

**Trials 5/6/7 follow-up opens (Raptora, Alban, Nightfall):**

- **Trial 5 (Flying / House Raptora) Baron identity** — name, gender, age, personality, ace, full team, level cap, narrative role — `[OPEN]`
- **House Raptora character** — the family's broader profile; Latin *raptor* etymology implies fierce-aristocratic-warrior register, but specifics `[OPEN]`
- **Trial 6 (Grass / House Alban) Baron identity** — name, gender, age, personality, ace, full team, level cap, narrative role — `[OPEN]`
- **Whether the Trial 6 (Alban) Baron knew "Nomad Alban" was Osrid** during the 10-year cover-identity period — `[OPEN]` (per existing lock; this open carries forward)
- **Trial 7 (Dark / House Nightfall) Baron identity** — name, gender, age, personality, ace, full team, level cap, narrative role — `[OPEN]`
- **Trial 7 Baron's familial relationship to Eldred Nightfall (Osrid's late father)** — successor cousin, sibling, distant nephew, or non-blood House successor? `[OPEN]`
- **Trial 7 Baron's awareness of Osrid being alive** — `[OPEN]` (likely no, but specific status undecided)

**Ace-bonding overworld interactions — per-character openness:**

- **5 ace locks are `[OPEN]`** for the 23 in-scope characters: T5 Raptora, T6 Alban, T7 Nightfall, Madame Roma, Blue Moon Hermit. (Manus's **Modal**, Jordan's **Naga**, Wakahisa's **Hayate**, and Silas's **Thauma** + **Malamar** locked v0.9.9.) Each unlock cascades to enable the corresponding interaction sub-task (engineering task #56).
- **Per-character interaction style content** for the 13 ready-to-design characters (excluding Simone-Splendor which is the locked example) — `[OPEN]` per character. Recommended approach: lock interaction style at the time each character's full bible entry is reviewed, not as a separate dedicated pass.

### v0.9.7 closures (character expansions and major narrative locks)

The following major opens are now CLOSED in v0.9.7:
- ~~**Tinkaton stat buff numbers**~~ — **RESOLVED in v0.9.7**: 75/85/125/75/125/75 = BST 560 (parity with Bloodmoon Ursaluna). See Section 6 — starter mechanical implementation.
- ~~**Does the player recover the stolen starter from Eden?**~~ — **RESOLVED in v0.9.7**: No. Eden keeps the stolen starter through the entire game and into the post-game marriage. See Section 7 — Eden.
- ~~**Supreme Sage final ability name**~~ — **RESOLVED in v0.9.7**: Renamed to **Lunacy**. Mechanics unchanged. ABILITY_LUNACY constant. See Section 9 — Lunacy entry.
- ~~**The 4th unnamed Vizier (besides Umbra/Education, Glaive/War, Silas/Commerce)**~~ — **RESOLVED v0.9.9**: **Zeldra Stone — Vizier of Infrastructure, House Stone**; ace Regis (blue shiny Tyrantrum); full team locked. See Section 7 — Zeldra Stone.
- ~~**Vizier gauntlet order in Act V**~~ — **RESOLVED in v0.9.7**: Rock female → Umbra → Silas → Glaive → Rhydia. See Section 10 — Act V.
- ~~**Silas's identity-reveal scene placement**~~ — **RESOLVED in v0.9.7**: Relocated to after Silas's defeat as third Vizier (no longer fourth); Silas then witnesses Glaive's fight and Rhydia's Champion battle before the unmasking. See Section 10 — Act V (Silas third fight bullet).
- ~~**Trial Lord vs Trial Baron terminology**~~ — **RESOLVED in v0.9.7**: Sweep complete; 66 occurrences updated to Trial Baron / Trial Baroness with appropriate gendering.
- ~~**Brie Moray's story role**~~ — **RESOLVED in v0.9.7**: Promoted to Trial Baroness of the 8th Trial (Fairy), with Domdaniel as her Trial ace; full character expansion including the Silas relationship complexity and the parents-died-in-accident backstory. See Section 7 — Brie Moray.
- ~~**Eden's full arc structure**~~ — **RESOLVED in v0.9.7**: Eden promoted to formal deuteragonist status. Stolen starter persists through entire game into post-game marriage. Section 7 — Eden expanded.
- ~~**Dragon scarcity in Cormoria — in-world explanation**~~ — **RESOLVED in v0.9.7**: Centuries of dragon-hunting by the Tinkaton clan in the deep desert. See Section 6 — Tinkatink Line Dragon-Slayer Bloodline.
- ~~**Solomonar title structure**~~ — **RESOLVED in v0.9.7**: Ancient title predating Cormoria; given only twice in empire history (first in Cormor's third century with a shiny Haxorus ace, identity forgotten; Glaive is the second). See Section 2 — Solomonar title.
- ~~**The Tinkatink starter's heritage**~~ — **RESOLVED in v0.9.7**: Egg taken by Umbra from the dragon-slayer clan in the deep desert; the hatchling does not know its heritage; Umbra tells Osrid the truth in a conditional return-to-lab scene if Osrid picked Tinkatink. See Section 6 — Tinkatink Line; Section 7 — Cadmus Umbra.
- ~~**Tinkatink line custom shiny palette identity**~~ — **PARTIALLY RESOLVED in v0.9.7**: Dragon-slayer-clan bloodline coloration is the locked visual identity; specific palette values TBD pending Phase 1 sprite production session. See Section 6 — Tinkatink line palette identities.
- ~~**Tinkatink/Tinkatuff/Tinkaton signature offensive move**~~ — **RESOLVED in v0.9.7**: Behemoth Bash (Cormorian variant) — Normal physical, 100 BP, 95% acc, 10 PP, custom Steel-effectiveness override regardless of resolved type after Pixilate. Learned at Lv 30 on Tinkatuff. See Section 9 — Behemoth Bash.
- ~~**Templar Arceus order leadership structure**~~ — **RESOLVED in v0.9.7**: Archbishop Ambrose Caymen leads the order. See Section 4 — Templar Arceus Order; Section 7 — Ambrose Caymen.
- ~~**Goma's Pokemon team**~~ — **RESOLVED v0.9.9**: full Fighting roster locked — Smolder (shiny Emboar, primary) / Flamigo / Lucario / Annihilape / Toxicroak / Mega Houndoom (secondary). Two fights (3 then 6). See Section 8 — Goma.
- ~~**House Nightfall Trial Baron seat**~~ — **PARTIALLY RESOLVED in v0.9.7**: House Nightfall holds the Dark-type Trial Baron seat; specific Trial Baron/Baroness identity still `[OPEN]`. See Section 4 — Trial Barons.
- ~~**Final Trial type slot**~~ — **PARTIALLY RESOLVED in v0.9.7**: The remaining Trial type is Normal; specific Trial Baron, House, and number `[OPEN]`. See Section 4 — Trial Barons; type coverage map.

### v0.9.4 closures (major cosmology and character locks)

The following major opens are now CLOSED:
- ~~**Phancero's nature, history, current state**~~ — **RESOLVED in v0.9.4**: Phancero is Arceus's shadow-self made manifest; Missingno is his first incursion; he was a worshipped fourth bird in early Kanto; erased (not sealed) from material world by Cormor + Keerin's pact; persists in the void. See Section 2 — Cormorian founding myth; Section 9 — Phancero entry.
- ~~**Keerin's identity and lore**~~ — **RESOLVED in v0.9.4**: Arceus's first companion; reassigned as observer-extension; cosmic-tier strength (BST ~720); Normal/Ghost typing; Wonder Guard (Paragon) / Opportunist (Elite); pact-partner with Cormor; loves only Arceus + Cormor + Osrid (lesser). See Section 9 — Keerin entry.
- ~~**Cormor's pre-dynastic motivation**~~ — **RESOLVED in v0.9.4**: Vengeance for his Celestica tribesmen killed by Phancero. Was originally a blacksmith of the Celestica before becoming a wandering benevolent brigand with Lethys. See Section 2 — Cormorian founding myth.
- ~~**Treasures of Ruin origin mechanism**~~ — **RESOLVED in v0.9.4**: They are inverted Dreamstones — Cormor's original tribal artifacts (forged with Roma's miko-consecration) gradually corrupted by Phancero's residual contamination across centuries. See Section 2; Section 8 — Cult Cosmological Framework; Section 9 — Dreamstone polarity update.
- ~~**Why Dreamstones resonate with Treasures**~~ — **RESOLVED in v0.9.4**: Same material, opposite polarity. Positive Dreamstones used to re-align inverted Treasure resonance frequency for material incarnation. See Section 9 — Dreamstone.
- ~~**Lore-reveal deliverer**~~ — **RESOLVED in v0.9.4**: The Blue Moon Hermit (Sage Lethys of the Celestica) via the Book of the Moon in post-game content. Plus in-story narrative fragments at fairy-tale level only. See Section 7 — Blue Moon Hermit; Section 9 — Book of the Moon.
- ~~**Sword Cult HQ location**~~ — **RESOLVED in v0.9.4**: The Sword Cult HQ has had a hidden location throughout the story (never visited by player). The Necropolis becomes the cult's *target* late in the story when Baradus discovers the Distortion gate. The Necropolis Assault is the unified climactic operation — no separate HQ raid. See Section 8 — Baradus's late-game discovery; Section 10 — Act VI.
- ~~**7v9 final battle location**~~ — **RESOLVED in v0.9.4**: The Distortion gate chamber at the deepest layer of the Mirroh Necropolis, during the unified climactic Necropolis operation. See Section 10 — Act VI.
- ~~**Nemo's death location**~~ — **RESOLVED in v0.9.4**: At the Necropolis itself — Baradus brought him there for the binding ritual. Found by player during the Necropolis Assault. See Section 10 — Act VI.
- ~~**Necropolis Assault structural placement**~~ — **RESOLVED in v0.9.4**: Early Act VI as the opening of the unified climactic operation. See Section 10 — Act VI.
- ~~**Blue Moon Hermit's name**~~ — **RESOLVED in v0.9.4**: **Sage Lethys of the Celestica.** Mentioned in passing in late-game dialogue. See Section 7 — Blue Moon Hermit.
- ~~**Cadmus Umbra's ace and Pokemon team specialty**~~ — **RESOLVED in v0.9.4**: Water family specialty; **Jousteel** (Water/Steel) as his ace; Umbra family exclusively cultivates the Jousteel line. See Section 7 — Cadmus Umbra; Section 9 — The Jousteel Line.
- ~~**Glaive's Bagon-to-Shelgon evolution context**~~ — **RESOLVED in v0.9.4; FRAMING RESTRUCTURED in v0.9.8**: Saved from sandstorm by the Blue Moon Hermit; Hermit gave him partnership-training; that training enabled the Bagon → Shelgon evolution. **v0.9.4 originally placed this event in Glaive's pre-game wandering years; v0.9.8 corrects this to an on-screen event during the early game (Glaive's desert sojourn between fights G2 and G3, during his failed pursuit of legendary Garchomp).** The structural significance of the Hermit's role is preserved (partnership-training, psychic-gift recognition, dragon-tradition root); only the *timing* changes from "pre-game backstory" to "on-screen event in real time." See Section 7 — Glaive arc, restructured v0.9.8.
- ~~**Glaive's introduction of the Blue Moon Hermit to the player**~~ — **RESOLVED in v0.9.4**: Mid-game, around level 45, during Cadmus Umbra discussion about final starter evolution. See Section 7 — Glaive arc.
- ~~**Vandras's awareness of Osrid's identity**~~ — **RESOLVED in v0.9.4**: Vandras *recognized* Osrid in the epilogue (through the starter first, then Osrid's face) but *deliberately chose not to reveal it* — giving Osrid the name Veddev as a gift of new identity. *"Wait...is this..."* but doesn't finish the thought. He carries the secret across the rest of his life. See Section 7 — Vandras Amber-Letz.
- ~~**Lore-reveal pattern across the story**~~ — **RESOLVED in v0.9.4**: Two complementary mechanisms — (1) in-story dialogue fragments at fairy-tale level only (every player sees these), and (2) the Book of the Moon for engaged players (post-game depth). Even Cadmus Umbra does not know the deep Phancero lore; only the Blue Moon Hermit carries the lost oral tradition. See Section 2.

### v0.9.4 new opens

These items emerged from v0.9.4 lock work and are deferred for future design:

- **Phancero's specific typing in data tables** (likely Dark/Ghost or Normal/Ghost-mirror; placeholder data for any in-game scripted reference)
- **Keerin's specific stat distribution** (120/120/120/120/120/120 mirror-of-Arceus vs. 120/100/130/130/130/110 observer-defensive specialization)
- **Keerin's full learnset and signature moves** (likely Normal STAB + Ghost STAB + defensive support + Dark coverage)
- **Keerin's specific encounter chamber location** for the Mt. Silver sidequest setup
- **Future-Red's specific movesets/items/abilities** for each of his six broken legendaries
- **Future-Red's encounter retry behavior** (does the game allow retry, or is there a meaningful failure state?)
- **Whether Future-Red retains Pikachu somehow** (deliberately absent from the six-legendary team — possibly the corrupted future Red lost or transcended his canonical bond)
- **Jousteel line's full Pokemon data** (BST, abilities, learnsets, evolution method)
- **Jousteel sprites and icon** for GBA-format remastering from asset library RPG Maker XP sources
- **Keerin overworld following sprites** (not in the asset library; require new development)
- **Book of the Moon chapter content** (10-11 chapters' worth of worldbuilding-text writing)
- **Book of the Moon chapter physical locations** across Cormoria
- **Madame Roma's full character design** (appearance, personality, dialogue voice)
- **Madame Roma's residence** (royal palace adjacent? traveling between locations?)
- **Madame Roma's Pokemon team** (if any beyond the metaphysical revival/soothsaying role)
- ~~**The Rock-type Vizier**~~ — **RESOLVED v0.9.9**: Zeldra Stone, House Stone, Vizier of Infrastructure; full profile, family (Sylphon & Stone / Devon weld), arc, and team locked. See Section 7 — Zeldra Stone.
- **Fossil revival quest specific narratives and locations** across Cormoria
- **Cormor's specific resting location** — `[OPEN]` permanently by design as part of the Avalon-sleep mystery
- **The exact mechanism by which Baradus discovers the Necropolis gate** in late Act V (likely Silas Moray's intelligence network indirectly leaking the knowledge — completing Silas's tragic-enabler arc)
- **Lethys and Roma's late-game dialogue** dropping Cormor-sleeping hints — specific lines maintaining ambiguity
- **Whether Lethys and Roma share an on-screen scene** in late-game Cormoria (cleanest design: yes, briefly, in late-game post-Necropolis content)
- **Specific in-story narrative-fragment beats** about cosmic stakes (Cadmus Umbra hints, Sable Ashland inscriptions, Templar Arceus warnings, Necropolis confirmation moment)
- **Difficulty mode implementation specifics** — UI design, save data architecture, mode-flag tracking
- **Nuzlocke specific rule set** — death rule + first-encounter rule + optional clauses (species, nickname, etc.)
- **Randomizer specific settings** — wild encounters, trainer teams, abilities, movesets, hold items
- **QoL improvements beyond Dreamstone Mysteries baseline** — `[OPEN]` discussion needed; many features to add

### v0.9.7 new opens

These items emerged from the v0.9.7 character-expansion and parallel-quest patch and are deferred for future design:

**The Mega-Dreamstone Shard Quest (Section 9):**
- 7 of the 9 shard locations (the Tinkaton Matriarch's cave and Ambrose's secret holding are locked; the remaining 7 are `[OPEN]`)
- The original shattering event — when did it happen, who or what caused it (cult-orchestrated vs. accident)
- Whether the reassembled Mega-Dreamstone has properties beyond a standard intact Dreamstone (its "Mega" designation suggests yes)
- Whether the shard quest has a visible tracker in the player's UI
- Whether the palace Dreamstone is also used in the climactic sealing alongside the reassembled Mega-Dreamstone
- The first shard recovery beat placement in Act I (which low-stakes event introduces the mechanic)

**The Tinkaton clan / Matriarch (Section 6):**
- Matriarch's name
- Clan name
- Desert/mountain region naming
- Matriarch's combat profile (level cap, exact moveset, abilities — likely above-cap encounter)
- Tinkatink-picker player special dialogue with the Matriarch
- Whether the Baxcaliburite post-Champion quest's "Origins of Cormoria's Dragons" content references the Tinkaton clan's ecological role
- Other named clan members (a Tinkaton lieutenant defending the cave entrance, etc.)

**Brie Moray (Section 7):**
- Full Trial 8 team beyond Domdaniel (Fairy-type companions)
- Specific dialogue lines for her truth-telling style about Silas during Trial 8
- Whether Brie has a scene with Osrid post-Silas-death resolving the parallel parental loss
- Whether Brie inherits House Moray formally after Silas's death (and at what age)
- Specific details of the accident that killed her parents (likely genuine accident, but `[OPEN]`)

**Ambrose Caymen (Section 7):**
- ~~Full Trial-tier roster beyond Temperance and Brunhilda~~ — **RESOLVED v0.9.9**: Roland (Escavalier) / Justice (Aegislash) / Fortitude (Corviknight) / Prudence (Bronzong) complete the four cardinal virtues + two named warriors. See Section 7 — Ambrose.
- Specific dialogue beats for pre-fight, post-fight clarity, and subsequent ally relationship
- Exact placement of the bishop-coup foil + Ambrose-fight sequence in Act III or IV
- Whether Ambrose's standard Braviary appears in his entourage (honest national bird counterpoint to Silas's Thauma)
- Specific scene where Ambrose learns Silas's lie about Nemo (likely post-Silas-death in Act V or VI)
- Whether Ambrose ever speaks to Osrid about the loss of Nemo as a shared grief
- Ambrose's age (likely 40s-50s given Archbishop status and 30-year Nemo friendship)
- Whether Ambrose explicitly forgives Silas posthumously or carries the betrayal with him

**Jordan Ramses & Wakahisa (Section 7):**
- Full Pokemon teams across multiple appearances
- Specific scenes and dialogue across both arcs
- ~~Wakahisa's gender, full backstory, origin country~~ — **RESOLVED v0.9.9**: female; Johto shinobi-clan heir exiled when her gender was exposed (patriarchal succession); Johto → Paldea → Cormoria.
- Jordan's preferred cuisine style
- Whether Jordan cooks for Osrid on-screen (almost certainly worth scripting)
- Whether the truth of the Ramses assassination attempt (guilty or framed) is ever revealed
- ~~Whether Wakahisa and Jordan develop a friendship with each other after both convert~~ — **RESOLVED v0.9.9**: yes — Jordan becomes the brother she never had.
- Exact Paragon Gauntlet structure with the two new additions (expand to 7-8 fights, alternate-track, or separate-event)
- Specific geographic location of the cross-purposes encounter and Osrid intervention

**The Female Rock Vizier (Section 7):**
- Name
- House identity (possibly ancient ties to the destroyed House Jalviss given Rock/Ground adjacency, possibly other lineage)
- ~~Specific Vizier portfolio~~ — **RESOLVED v0.9.9**: Infrastructure (the Rock ↔ construction weld).
- Personality, dialogue voice, backstory beyond the Tyrunt-revival event
- Full Trial-tier roster beyond Tyrantrum
- Age (likely 40s-60s given decades of Tyrantrum mastery)
- Connection to Pierra and/or Rhydia
- Awareness of the cult crisis at the Umbra-axis level vs. the within-her-portfolio level
- Whether she knows Roma's deeper identity

**The Solomonar title and history (Section 2):**
- First Solomonar's identity (intentionally permanent `[OPEN]` — historical footnote only, shiny Haxorus ace)
- Whether any other dragon-trainers were *almost* given the title across the 1700-year gap

**House Ramses (Section 2):**
- Whether the family was actually guilty of the assassination attempt or framed
- The previous Emperor's eventual cause of death (he survived the Ramses attempt but is deceased at story start)
- House Ramses pre-disgrace politics (Concordance seat, type tradition if any, political alliances)

**House Nightfall Dark-type Trial Baron (Section 2 / Section 4):**
- Specific Trial Baron/Baroness identity
- Whether Rhydia (half-Nightfall by blood) has any relationship with this Trial Baron
- Whether the Trial Baron knew Osrid was alive (likely no — only Umbra knew across the 10-year exile)

**The Normal-type Trial Baron (Section 4):**
- Specific Trial Baron, House identity, name, ace, level, narrative role — *all* `[OPEN]`

### Setting and politics
- Cormoria's specific cultural-aesthetic inspiration (Heian-era Japan? Tang Dynasty? Classical Mediterranean? Something invented?)
- Cormorian imperial capital location (existing DM city expanded, or a new location?)
- Cult stronghold geography (specifically: Sword Cult HQ where Nemo is held captive; Beads Cult bases before and after Mt. Ceram failure)
- Paldean diplomatic / commercial compound location in Cormoria
- Where does Pierra physically reside? Does she ever become lucid by the end of the game?
- Kalos's role (if any) in our game's plot — Mega Evolution origin partially answered via Jalviss, but Kalos's separate Mega-stone development is still ambiguous
- Specific identities of Trial Houses **4-8** (we have Kimaris Langerin / Ghost / Trial 1, Reid Ashland / Fire / Trial 2, Manus Surge / Electric / Trial 3, and Nemo Korolev / Ground / Trial 9 — five remaining)
- House Raptora (Flying) — needs detail and assignment to a specific Trial position
- **House Alban (Grass)** — Trial Baron identity `[OPEN]`. Specific Trial position number `[OPEN]`. Whether the Alban Trial Baron knew "Nomad Alban" was actually the prince Osrid (added to Section 2/Section 5 implications for v0.8.2)
- House Alban's level of complicity in Umbra's cover-identity plan — entire family knew vs. only head of household knew (Section 2)
- At least 1-2 other noble houses needed to fully populate the 8 noble Trial Baron seats (Nemo Korolev is the 9th and is non-noble)
- Which other Trial Baron positions shifted hands in the 10-year gap during Osrid's overseas service (Manus Surge's promotion is the established case; a few others may have shifted, specifics `[OPEN]`)
- The 4th unnamed Vizier (besides Umbra/Education, Glaive/War, Silas/Commerce)
- ~~The Tarasque-vs-Dawnstar rank reconciliation~~ — **RESOLVED in v0.8.1**: full rank order locked as Cadet → Lieutenant → Strategos → Windshear → Rainhawk → Tarasque → Dawnstar (Section 2)

### Characters
- ~~**Rhydia character work** — full profile pending~~ — **RESOLVED in v0.9**: Full Rhydia profile, complete team specs (Justice + Puff + cycling members), and political/emotional arc all locked. See Section 7.
- ~~Rhydia's Pokémon team~~ — **RESOLVED in v0.9**: Justice (Iron Valiant with Sharpness, Choice Scarf, four slicing moves) + Puff (shiny Drampa with Multiscale, Assault Vest, Dragon Energy / Hyper Beam / Thunderclap / Flash Cannon) + cycling members from Aegislash / Swampert / Zebstrika / Hisuian Lilligant / Stonjourner / Talonflame
- **Specific subplot details of the Goma assassination arc** — how exactly Osrid and Rhydia's paths first cross during this beat after Trial 2; the specific scripted-doubles encounter structure; geographic location of the palace
- ~~**House Moray's generational ace**~~ — **RESOLVED in v0.9.1**: **Domdaniel** (shiny Scream Tail with Huge Power). Rejected Silas as a child; only bonds with Brie Moray (Silas's 15-year-old niece). See Section 2 — Generational Aces; Section 7 — Silas/Brie; Section 9 — Domdaniel combat profile.
- ~~**Marshadow's specific late-game deployment trigger**~~ — **RESOLVED in v0.9.1**: The Sword Cult's late-game assault on the Mirroh Necropolis to use the Distortion gate as Chien-Pao's Leyline incarnation point. Kimaris deploys Marshadow in defense; player joins the defense as a playable beat. See Section 7 — Kimaris; Section 10 — Act V.
- **Other senior houses' generational aces** — full inventory of which houses have them and what their identities are (Langerin's Marshadow and Moray's Domdaniel now locked; remaining houses' aces still open)
- **Cormor Dream-Eater backstory specifics** — how the founding myth surfaces in-game, what Cormor himself was like as a person
- ~~**Nobility Concordance** details~~ — **RESOLVED in v0.9.1**: Full senate-equivalent structure locked. See Section 2 — Nobility Concordance. Remaining sub-opens (presiding officer, specific named members, chamber location, voting mechanics) preserved as future design.
- ~~**Sylphon & Stone** details~~ — **PARTIALLY RESOLVED in v0.9.1**: Full guild structure locked, including primary-funding-vehicle role for Beads Cult, mid-to-late-game exposure beat, and Silph Co. / Devon Corporation descendant lineages. See Section 2 — Sylphon & Stone; Section 12 — Sylphon/Stone lineage subsections.
- **Sylphon and Stone family heads** — specific named characters within the guild leadership `[OPEN]` (deferred per design decision)
- **The Royal Secret Villa** — whether the player visits it in the main game, whether Pierra ever learns the full truth about Silas or about Osrid's survival
- **Sword Cult organizational rank-naming convention** — whether the Sword Cult uses chess-piece naming like the Beads Cult (Acolyte/Bishop) or its own (likely military-styled given Baradus's Yo'aki background)
- ~~**Goma's full Pokemon team**~~ — **RESOLVED v0.9.9**: Smolder / Flamigo / Lucario / Annihilape / Toxicroak / Mega Houndoom (Fighting specialist + commanded Dark/Fire secondary). See Section 8 — Goma.
- **Brie Moray's specific story role** — confirmed locked as a character with a specific subplot/encounter; details `[OPEN]` for future design (likely involves Silas's late-game arc, possibly the Necropolis Assault defense, possibly House Moray succession after Silas's death)
- **Necropolis Assault structural placement** — exact placement in Act V or early Act VI; multi-stage scripted battle sequence design; command structure (Baradus personally? a lieutenant?)
- **Specific Dreamstone(s) used in the climactic sealing ritual** — the royal palace one? a different one? multiple?
- **Investigator(s) who expose Sylphon & Stone's cult-funding compromise** — Rhydia's intelligence network, Eden's defection-era knowledge, Nemo's pre-Trial-9 intel, or a combination
- **Locations of Wo-Chien and Ting-Lu's Leyline incarnation points** — Hoya River area for Wo-Chien; a deep forgotten cave system for Ting-Lu; specific geography still open
- ~~Glaive's specific stat-buff numbers for Turtonator~~ — **RESOLVED v0.9.9**: HP 60→100, SpA 91→115, SpD 85→100 (BST 485→564); new ability Dragon's Maw.
- ~~Glaive's roster progression across his 4-5 encounters~~ — **LOCKED v0.9.8** (G1–G5 ladder; see Section 7 — Glaive).
- ~~Glaive's Vizier-of-War final fight roster and Mega-Pokemon question~~ — **RESOLVED v0.9.9**: Mega Salamence / Dracovish / Turtonator / Sandaconda / Sceptile / Naganadel; team Mega = Mega Salamence (state-sanctioned). See Section 7 — Glaive.
- Glaive's "major mistake" at the mid-game reveal
- Umbra's full team (Vizier of Education)
- Umbra's Vizier-of-Education fight team
- Vandras's earlier appearances in the game (if any) before the epilogue
- The three Move Tutors' names and locations (for the unified starter evolution mechanic)
- Inciting incident in Act I
- The 6 stat-themed recurring rivals' names, identities, and encounter geography (only the Speed rival is sketched with Ninjask)
- Whether any of the 6 rivals have arc reversals (e.g., friend-to-corrupted vs. grudge-to-respect)
- **House Ashland family details** — Reid's three sisters, exact internal family dynamics
- **Goma's late-game return mechanism** — how/when the escaped Beads Cult Harbinger resurfaces as a desperate antagonist
- **The 5 other members of Baradus's mid-game team** (besides Crabominable) for the Crabominable discard encounter
- **Eden's specific fate** during the late-game cult crisis and final battle
- Sable Ashland's possible ongoing role beyond his Mt. Ceram return moment
- Reid Ashland's three sisters (names, ages, anything)
- **Whether Mega Evolution figures into Baradus's roster** (he has Tellius/Yo'aki tradecraft; possibly unauthorized Megas)
- Whether the Templar Arceus order's internal division (some secretly cult-aligned) becomes a named story thread

### Mechanics
- Other intermediate military ranks between common soldier and Rainhawk
- Could military rank be a progression mechanic for the player?
- Rainhawk mask mechanical effect (if any)
- Dreamstone representation mechanically (key item? story-flag? both?)
- Specific BST buffs for Tinkaton (numbers TBD; thematic role is "defensive starter")
- ~~Bloodmoon Ursaluna quest design specifics~~ — **RESOLVED in v0.9.2**: The Blue Moon Teddiursa line locks Bloodmoon Ursaluna as the *direct evolution* of Ursaring (Blue Moon) at level 45 via the Blood Moon (Ground) Master Tutor (Mechanic A — Trial 6 Evolution Gates). The Ancient Peat Block / Lunacy ability replacement is the *post-Champion* bonus via Mechanic B — Ancient Cormoria Side Quest. See Section 6.
- Does the player recover the stolen starter from Eden?
- Aerodactylite recovery quest specifics (location, gating, story role)
- Custom move **Ravage** implementation specifics (animation customization scope)
- 9th Trial level cap (Nemo Korolev) — appropriate to his position
- Reid Ashland's Heatran-related dialogue specifics
- **Three Master Tutors for Trial 6 starter evolution gates** — *Blood Moon (Ground) tutor* RESOLVED in v0.9.3 as the **Blue Moon Hermit** (Section 7 — Blue Moon Hermit entry; Section 6 — Mechanic A). Mountain Gale and Gigaton Hammer tutors still `[OPEN]` for identity, location, quest structures.
- ~~**Three post-Champion Ancient Cormoria Side Quests** — specific quest structures and narrative beats for the Baxcaliburite, Ancient Peat Block, and Divine Cuirass acquisitions~~ — **RESOLVED in v0.9.3**: All three quests structurally locked with combat structure, setting, companion, and emotional register specified. See Section 6 — Mechanic B subsections.
- **Lunacy ability final stat-boost numerics** — current spec is 10% Speed per fainted ally / max 50%; +1 Sp.Atk stage per KO (Section 9 — Lunacy spec)
- **Post-Champion detour-or-skip mechanic specifics** — whether the Act VI cult war progresses while the player is on the Ancient Cormoria detour, whether there's a "point of no return" warning before the Sword Cult HQ raid
- **Lore origin specifics for the Ancient Peat Block** — where Cormorian Ancient Peat naturally accumulates. v0.9.3 locks the swamp as the *acquisition location* (ancient fog-shrouded Cormorian swamp); the deeper lore-geological origin still `[OPEN]`
- **Blue Moon Hermit's actual name** beyond the title (Section 7 — Blue Moon Hermit; v0.9.3 confirms the character identity but the proper name remains open)
- **Blue Moon Hermit's personal Pokemon team** — competent trainer, possibly Champion-tier, lunar/dark/Psychic-thematic, possibly includes a Bloodmoon Ursaluna of their own
- **Shadow-self dialogue (if any) during the Ancient Peat Block mirror match** — default silent; design `[OPEN]` whether the shadow speaks the player's inner doubts/fears
- **Hoopa Unbound's exact kit and ordering of summoned trio** during the Divine Cuirass gauntlet — Hyperspace Fury locked; secondary moves/item/ordering of Blacephalon/G-Moltres/Iron Moth `[OPEN]`
- **Whether Glaive obtains Mega Salamence *only* through the Frigibax-picker Baxcaliburite quest** or off-screen in other playthroughs (Section 7 — Glaive entry; v0.9.3 leans Frigibax-picker-only for distinctive playthrough identity but officially `[OPEN]`)
- **Whether the gauntlet stages in the Divine Cuirass quest have any breaks** for healing/swap (default: no breaks, continuous gauntlet) or a single mid-gauntlet break

### Story
- Order of Trial encounters in Act II (Trials 2-8)
- Order of cult encounters in Acts II-III
- Specific climax structure beats — multiple `[OPEN]` items embedded in Section 10
- ~~Final resolution of Osrid's memory state in epilogue~~ — **RESOLVED in v0.8.2**: Osrid retains his full memory but *chooses* to discard his Osrid identity and live as Veddev going forward. Not amnesia — voluntary renunciation. See Section 5 Phase 3.
- Eden's exact involvement during the climactic sealing
- How much of the epilogue is playable vs. cinematic
- **Geographic location of the mid-game Baradus encounter** (where Crabominable adoption happens)
- Geographic location of the Sword Cult HQ where Nemo is held
- Sable Ashland's possible later quest involving his knowledge of Ancient Cormoria

### Mega Baxcalibur implementation (specific subset)
- Stat distribution: strict canon vs. adjusted for our game's balance
- Ability: strict canon vs. custom
- Sprite asset design from user-provided canon references (pose locked, color/detail still to design)
- Whether Mega Baxcalibur gets a custom signature move in our game

### Technical / Production
- **Done in v0.6: Frigibax line custom shiny palettes** — shipped as patch `0001-Frigibax-line-custom-shiny-palettes.patch`, awaiting user verification in compiled ROM
- **Pending: Teddiursa line custom shiny palettes** — waiting on user-provided reference material; will have a distinct palette identity (not Frigibax's heraldic colors)
- **Pending: Tinkatink line custom shiny palettes** — waiting on user-provided reference material; will have a distinct palette identity (not shared with either other line)
- **Pending: Custom shiny Hisuian Braviary** for Silas's Thauma — waiting on user-provided reference material; "sinister" color scheme
- **Pending: Mega Baxcalibur sprites** (front, back, menu, footprint, plus shiny variants)
- Investigate DM's existing starter selection script to plan our replacement (currently selects Gothita/Timburr/G-Zigzagoon; we replace with Frigibax/Teddiursa/Tinkatink)
- Investigate DM's Ancient Ceram/Mirroh time-travel implementation as template for Ancient Cormoria flashback
- Custom Ravage move implementation (~30-40 lines across moves_info.h, learnset, animation script, localization)
- Custom Crabominable adoption event implementation (~4-6 hours; nickname/nature/ability selector UI, party-add event, flag-checks for final battle, conditional dialogue variants)
- 7v9 double-battle final-fight scripting — two consecutive double battles, no breaks/healing between, with specific Crabominable conditional dialogue
- Engineering investigation of the bible's eventual splitting into multiple documents (world bible / story bible / mechanics bible) — flagged in Section 14 for future consideration as the document grows past 2000 lines

---

