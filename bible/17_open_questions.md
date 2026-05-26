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

### v0.9.8 new opens

These items emerged from v0.9.8 lock work and are deferred:

- **Mega Baxcalibur specific stat distribution** within the BST 720 + Speed>120 + Atk>145 constraint
- **Cadmus's personal Jousteel battle spec** (moveset, item, ability) for the Vizier-gauntlet encounter — `[OPEN]`
- **Engine type-override implementation pattern** — three damage-calc hooks (Behemoth Blade Fairy, Behemoth Bash Steel, Mountain Gale Water) parallel to existing Freeze-Dry pattern; engineering task #49–51
- **Joustroll/Jousteel cry audio** — user-authored deliverable; placeholders in place
- **Trial 4 Joustroll Egg sidequest event scripting** — map design, boss encounter, puzzle implementation, dialogue scripting; lore locked, engineering `[OPEN]`
- **Build-pipeline JSON registry for new custom species** — the compile log emits non-fatal "Unable to find Joustroll/Jousteel in json" lines; the build still succeeds but a JSON metadata file expects entries that haven't been added. Low priority; investigate when there's slack.
- **Trial 5, 6, 7 Baron identities** (Raptora, Alban, Nightfall) — type-to-Trial assignment locked v0.9.8; specific Baron names, aces, levels, team compositions, narrative roles all `[OPEN]`
- **Manus Surge's ace, full team, level cap specifics** — locked at Trial 3 in v0.9.7; profile remains thin
- **Cadmus Umbra's overworld attendant Joustroll** — separate from his ace Jousteel; engineering and dialog beats `[OPEN]` (cross-ref: Section 9 — Joustroll/Jousteel Line)
- **Silas Moray's primary ace species/name** — Vizier-of-Commerce; Psychic-type tradition; Thauma (shiny Hisuian Braviary) is locked as either his Templar mount or secondary ace, `[OPEN]` whether it is the primary ace deployed in Act V Vizier gauntlet
- **Female Rock Vizier name, House, Vizier portfolio** — character locked at trait-level v0.9.7; specific name and house assignment `[OPEN]`
- **Madame Roma's overworld ace species/name/combat profile** — qualifies for ace-bonding pattern; specifics `[OPEN]`
- **Blue Moon Hermit's overworld ace species/name/combat profile** — qualifies for ace-bonding pattern; specifics `[OPEN]`
- **Jordan Ramses's full Poison-type team and named ace** — recurring rival; locked as in-scope for ace-bonding pattern; specifics `[OPEN]`
- **Wakahisa's full Bug-type team and named ace, gender, foreign-origin country** — recurring rival; locked as in-scope for ace-bonding pattern; specifics `[OPEN]`
- **Robard Sylphon's appearance, combat capability, post-exposure fate** — `[OPEN]` whether he appears on-screen, whether the player ever battles him, where he is after his forced resignation from Sylphon & Stone
- **Sable's post-Act-IV scene with Simone** (childhood friend reckoning with her marriage crisis) — `[OPEN]` whether on-screen, off-screen, or absent
- **PTSD dream sequence specific placement and triggering conditions** for Boran Surge fight — Section 14 task #58 `[OPEN]`
- **Late-game Guzzlord private-moment scene** — specific location, triggering conditions, dialog (if any) — Section 14 task #56.16 `[OPEN]`


**Trial 4 (Simone Sylphon) follow-up opens:**

- **Trial 4 specific level cap number** — interpolated between Trial 3 (35-40) and Trial 8 (50-55); likely ~40; specific number `[OPEN]`
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

- **9 ace locks are `[OPEN]`** for the 23 in-scope characters: Manus, T5 Raptora, T6 Alban, T7 Nightfall, Silas's primary, Jordan, Wakahisa, Madame Roma, Blue Moon Hermit. Each unlock cascades to enable the corresponding interaction sub-task (engineering task #56).
- **Per-character interaction style content** for the 13 ready-to-design characters (excluding Simone-Splendor which is the locked example) — `[OPEN]` per character. Recommended approach: lock interaction style at the time each character's full bible entry is reviewed, not as a separate dedicated pass.

### v0.9.7 closures (character expansions and major narrative locks)

The following major opens are now CLOSED in v0.9.7:
- ~~**Tinkaton stat buff numbers**~~ — **RESOLVED in v0.9.7**: 75/85/125/75/125/75 = BST 560 (parity with Bloodmoon Ursaluna). See Section 6 — starter mechanical implementation.
- ~~**Does the player recover the stolen starter from Eden?**~~ — **RESOLVED in v0.9.7**: No. Eden keeps the stolen starter through the entire game and into the post-game marriage. See Section 7 — Eden.
- ~~**Supreme Sage final ability name**~~ — **RESOLVED in v0.9.7**: Renamed to **Lunacy**. Mechanics unchanged. ABILITY_LUNACY constant. See Section 9 — Lunacy entry.
- ~~**The 4th unnamed Vizier (besides Umbra/Education, Glaive/War, Silas/Commerce)**~~ — **PARTIALLY RESOLVED in v0.9.7**: type is Rock, gender is female, ace is shiny Tyrantrum (Roma's revival of her girlhood Tyrunt fossil); name, House, portfolio still `[OPEN]`. See Section 7 — Female Rock Vizier; Section 4 — Viziers.
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
- ~~**Goma's Pokemon team**~~ — **PARTIALLY RESOLVED in v0.9.7**: Fighting-type specialist (deliberate counter to Baradus's Ice signature); Smolder (shiny Emboar) as primary ace; Mega Houndoom as secondary; rest of roster `[OPEN]`. See Section 8 — Goma.
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
- ~~**Glaive's Bagon-to-Shelgon evolution context**~~ — **RESOLVED in v0.9.4**: Saved from sandstorm by the Blue Moon Hermit; Hermit gave him partnership-training; that training enabled the Bagon → Shelgon evolution. See Section 7 — Glaive arc steps 5-7.
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
- **The Rock-type Vizier** — name, House identity, Vizier portfolio, full character profile. **v0.9.7 update:** gender locked as female; her shiny Tyrantrum ace via Roma's revival is locked; the rest remains `[OPEN]`
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
- Full Trial-tier roster beyond Temperance and Brunhilda
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
- Wakahisa's gender, full backstory, origin country
- Jordan's preferred cuisine style
- Whether Jordan cooks for Osrid on-screen (almost certainly worth scripting)
- Whether the truth of the Ramses assassination attempt (guilty or framed) is ever revealed
- Whether Wakahisa and Jordan develop a friendship with each other after both convert
- Exact Paragon Gauntlet structure with the two new additions (expand to 7-8 fights, alternate-track, or separate-event)
- Specific geographic location of the cross-purposes encounter and Osrid intervention

**The Female Rock Vizier (Section 7):**
- Name
- House identity (possibly ancient ties to the destroyed House Jalviss given Rock/Ground adjacency, possibly other lineage)
- Specific Vizier portfolio (Industry? Infrastructure? Justice? Religious affairs?)
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
- **Goma's full Pokemon team** — Beads Cult thematic, Champion-tier-ish given her status as best-trainer-besides-Baradus
- **Brie Moray's specific story role** — confirmed locked as a character with a specific subplot/encounter; details `[OPEN]` for future design (likely involves Silas's late-game arc, possibly the Necropolis Assault defense, possibly House Moray succession after Silas's death)
- **Necropolis Assault structural placement** — exact placement in Act V or early Act VI; multi-stage scripted battle sequence design; command structure (Baradus personally? a lieutenant?)
- **Specific Dreamstone(s) used in the climactic sealing ritual** — the royal palace one? a different one? multiple?
- **Investigator(s) who expose Sylphon & Stone's cult-funding compromise** — Rhydia's intelligence network, Eden's defection-era knowledge, Nemo's pre-Trial-9 intel, or a combination
- **Locations of Wo-Chien and Ting-Lu's Leyline incarnation points** — Hoya River area for Wo-Chien; a deep forgotten cave system for Ting-Lu; specific geography still open
- Glaive's specific stat-buff numbers for Turtonator
- Glaive's roster progression across his 4-5 encounters
- Glaive's Vizier-of-War final fight roster and Mega-Pokemon question
- Glaive's specific stat-buff numbers for Turtonator
- Glaive's roster progression across his 4-5 encounters
- Glaive's Vizier-of-War final fight roster and Mega-Pokemon question
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

