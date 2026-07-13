# Bible v0.9.15 — Split Section Index

This directory contains the v0.9.15 bible split into per-section files so Claude sessions can fetch only the sections they actually need, rather than burning ~190K tokens reading the canonical file in full.

**Canonical source:** `bible/dreamstone_ruination_bible_v0.9.15.md` (at repo root). The canonical file is a regenerated artifact — it is mechanically reconstituted from the splits at the end of each session.

## Edit policy (changed in session 2)

**The splits are the active edit target.** Do not edit the canonical file directly.

This reverses the prior v0.9.7 doctrine which had the canonical as the only edit target. The reason for the reversal is pragmatic: the canonical file is ~190K tokens and does not fit in a Claude session's context window for grep-and-patch workflows. The splits (each ≤ ~25K tokens) do fit.

**Workflow:**
1. Identify which split file(s) your edit touches.
2. Fetch the split via the Contents API.
3. Edit and commit it.
4. After all session edits are done, regenerate the canonical by concatenating the 21 splits in section-number order (`00_thesis_and_overview.md` through `20_chapter1_build.md`), stripping each file's `<!-- This file is a split-section view... -->` header, and writing the result as `bible/dreamstone_ruination_bible_v0.9.X.md` with an updated version banner.
5. Commit the regenerated canonical alongside the splits.

The canonical is therefore a *derived* artifact for grep-and-archive purposes only; it is never the place to make changes.

## How to use this directory

**For lore discussions:** consult the per-file summaries below, fetch the 1-3 files relevant to your conversation, and ask the user clarifying questions before fetching more.

**For engineering work:** fetch `18_engineering_tasks.md` and the specific narrative section(s) relevant to the task at hand.

**For full grep:** use the canonical full bible (`bible/dreamstone_ruination_bible_v0.9.15.md`). Splits don't help for grep across the whole document.

## File index

### `00_thesis_and_overview.md` — ~1,754 tokens (L1-68)

Sections 1 (Canon Contract — what the project is, hard/soft constraints, canon humility). Includes the bible v0.9.8 header + patch summary.

### `01_cormoria_worldbuilding.md` — ~19,833 tokens (L69-773)

Section 2 (Worldbuilding Foundations) — Cormorian history, military ranks, surnames-as-sacrament, Solomonar title, noble house structure, Mega Evolution policy, founding myth (Cormor Dream-Eater), Justice the Iron Valiant, generational aces, Leyline Resonance, Nobility Concordance, Sylphon & Stone vs Amber-Letz, Royal Secret Villa. The single largest worldbuilding file.

### `02_geopolitics.md` — ~965 tokens (L774-824)

Section 3 (Geopolitics) — Cormoria, Paldea (Eden's homeland), the Western Coalition (Kanto/Johto/Hoenn), the Long Arc of how the modern Pokemon world forms over 2000 years. Short and conceptually tight.

### `03_trial_barons_viziers.md` — ~3,887 tokens (L825-940)

Section 4 (Cormorian Empire internal structure) — political structure, military culture, the 9 Trials / 4 Viziers / Champion system, Templar Arceus Order, Taverns (empire-era Pokemon Centers), the cult-created political crisis, cultural register, geography. Reference for institutional roles.

### `04_protagonist_arc.md` — ~6,591 tokens (L941-1106)

Section 5 (Protagonist — Osrid/Rainhawk/Veddev) — three-phase identity, character arc, the double irony of his Rainhawk rank, character-tied mechanics. The full Osrid profile lives here (not in Section 7).

### `05_starter_lines.md` — ~17,105 tokens (L1107-1657)

Section 6 (Starter Trio + Umbra's Gift Scene) — gift scene, Eden theft scene, three starter lines (Frigibax/Teddiursa/Tinkatink), Tinkatink Dragon-Slayer Bloodline, Blue Moon Teddiursa lore, starter ability assignments, Trial 6 Master Tutor evolution gates, post-Champion side quests, Unboxable Starter mechanic. All three Phase 1-shipped palette lines documented here.

### `06_characters_royal_family.md` — ~6,132 tokens (L1658-1835)

Section 7 (Major NPCs) — Royal Family cluster: Royal Family of Cormoria overview, Queen-Regent Rhydia Cormoria. Pierra Cormoria I and Eldred Nightfall are covered in the family overview. (Osrid himself is in 04_protagonist_arc.md.)

### `07_characters_viziers.md` — ~14,161 tokens (non-contiguous: L1836-2051, L2162-2271, L3108-3219)

Section 7 — Viziers cluster: Glaive (Vizier of War / second Solomonar), Cadmus Umbra (Vizier of Education / Pokemon Philosopher / shard-quest handler). NOTE: Silas Moray (Vizier of Commerce) lives in this file too — entry starts at line 2162 in the canonical bible but his Vizier identity dominates so he's grouped here, not with the cult cluster.

### `08_characters_eden_recurring.md` — ~8,153 tokens (non-contiguous: L2052-2151, L2509-2560, L2679-2726, L3220-3289)

Section 7 — Eden and merchant cluster: Vandras Amber-Letz (merchant guild head who gifts Osrid the Veddev identity), Eden (Paldean thief / Beads Cult recruit / deuteragonist / future spouse — promoted to deuteragonist status in v0.9.7). Additional recurring rivals Jordan Ramses, Wakahisa, Sable Ashland, and Boran Surge are split into separate ranges in this file too — see file content.

### `09_characters_cult.md` — ~528 tokens (non-contiguous: L2152-2161, L3290-3310)

Section 7 — Cult cluster: Harbinger Baradus stub (Sword Cult leader). NOTE: most cult content lives in Section 8 (07_cults.md). The bulk of Baradus characterization is in Section 8. This Section 7 stub is the cross-reference entry. Goma, Alaric, and Harbinger info live in 07_cults.md.

### `10_characters_trial_barons.md` — ~10,378 tokens (non-contiguous: L2272-2508, L2561-2658)

Section 7 — Trial Barons cluster: Brie Moray (Trial Baroness 8 / Fairy / Domdaniel's chosen — promoted to Trial Baroness in v0.9.7), Nemo Korolev (9th Trial Baron / "The Usurper"), Sable Ashland (returned from Ancient Cormoria), Reid Ashland (2nd Trial Baron / Fire / House Ashland prodigy), Kimaris Langerin (1st Trial Baron / Ghost / Reserve Champion — v0.9.8 corrected from "former Champion"), Manus Surge (3rd Trial Baron / Electric).

### `11_characters_legendary.md` — ~11,103 tokens (L2727-3107)

Section 7 — Legendary/cosmic figures cluster: Blue Moon Hermit / Sage Lethys of the Celestica (last of his tribe / master partnership-teacher / Cormor's old companion), Future-Red (multiverse-displaced strongest trainer, post-game Mt. Silver content), Madame Roma / Roma Langerin (Royal Soothsayer / fossil-reviver / progenitor of House Langerin).

### `12_cults.md` — ~12,994 tokens (L3311-3765)

Section 8 (The Four Ruin Cults) — Origin (The Widening Eye), nature of Treasures' influence, the Harbingers (full profiles of Baradus / Goma / Alaric / Wo-Chien cult leader), cult cosmological framework, Goma's Royal Palace Assassination subplot, the Sword vs Beads enmity, Sword Cult HQ, the Necropolis assault buildup.

### `13_cosmology_mechanics.md` — ~22,733 tokens (L3766-4787)

Section 9 (Key Artifacts and Mechanics) — Treasures of Ruin (Chien-Pao/Wo-Chien/Ting-Lu/Chi-Yu detailed), Dreamstone polarity, Justice combat profile, Domdaniel, Marshadow, Crowley the Spiritomb, Reid's Heatran, Cadmus's Jousteel line, Cogita, Keerin, Phancero/Missingno, Mega-Dreamstone Shard Quest, fossil revival system, Book of the Moon, Behemoth Bash custom move, Blood Moon Ground retyping, Lunacy ability, custom Crabominable mechanic, difficulty modes (Classic/Veteran/Paragon + Nuzlocke/Randomizer toggles).

### `14_story_spine.md` — ~11,201 tokens (L4788-5079)

Section 10 (Story Spine) — Acts I through VI walkthrough: Act I homecoming and Eden theft, Act II two-cult war (Royal Palace assassination, Jordan/Wakahisa cross-purposes arc, Tinkaton clan side quest, ~50%% Rhydia reveal), Act III Mt. Ceram, Act IV Sylphon&Stone exposure + Nemo Trial 9, Act V Meritocratic Gate / Vizier gauntlet (Rock→Umbra→Silas→Glaive→Rhydia) / Hall of Fame unmasking, Act VI Necropolis Assault and sealing cataclysm.

### `15_design_principles.md` — ~10,624 tokens (L5080-5423)

Section 11 (Design Principles Carried Forward from Dreamstone Mysteries) — the project's recurring rivals (6 stat-themed), Paragon Gauntlet, partnership thesis in Cormoria's founding myth, Cormor-as-original/Player-as-renewal mirroring, the three-redemption-arc pattern (Silas/Glaive/Ambrose), permanent emotional complexity without resolution (Silas-Brie axis).

### `16_bloodlines_canon.md` — ~7,104 tokens (L5424-5707)

Section 12 (Bloodlines and Canon Connections) — Cormor Dream-Eater → Cormorian Royal Dynasty → Osrid/Rhydia, Eldred Nightfall blood/Dark-type lineage flowing to Rhydia, Eden's Paldean origins, Vandras → Berlitz family ~2000 years later, Glaive → Blackthorn City founding, the Bloodmoon Ursaring lineage, Justice as royal heirloom across the Cormoria→DM gap.

### `17_open_questions.md` — ~7,886 tokens (L5708-5975)

Section 13 (Open Questions) — v0.9.4 closures and remaining opens, v0.9.7 closures and new opens, setting/politics opens, mechanics opens, story opens. Operational rather than narrative content — useful for project-planning conversations but not for lore discussions.

### `18_engineering_tasks.md` — ~15,132 tokens (L5976-6611)

Section 14 (Production Discipline) — all engineering tasks (~48 numbered items): sprite work, custom moves, custom abilities, scripted events, dialogue scripts, mode-gating, fossil system, Templar Tavern network, terminology sweeps. Operational rather than narrative — for engineering-planning conversations.

### `19_location_atlas.md` — ~2,900 tokens

Section 15 (Cormoria Location Atlas) — the canonical empire-era region layout, established from the illustrated region map and cross-referenced against DM's codebase map: the DM relationship (prequel / end-game calamity / DM-fate), region overview, every major location by region with story/trial role and connections, the 9 Trial venue assignments, the route list (two duplicate route numbers flagged for assignment), the empire→DM fate mapping, and open placements (Trial 3/4/8 confirmations, calamity epicenter, Shadowmarshes). The geography reference for map-building.

### `20_chapter1_build.md` — ~3,400 tokens

Section 16 (Chapter 1 Build Plan) — the buildable blueprint consolidated from working conversation: the Chapter-1 playthrough beat-by-beat (cold open + letter, starter/Eden theft, the three Pelluca sidequests, the Route-11/Eiscue hook, Mirroh/Necropolis Trial 1, Mt. Mirroh Peak climax); the Pelluca Valley build spec (all eight map layers); the opt-in portrait dialogue system engineering spec; new Chapter-1 mechanics (shiny-decision egg, Golisopod Tough-Claws HA + Wimpod kit, crack-tile ice puzzle); new/updated canon (Templar pre-Cormorian-proof goal, Loulan); the committed sprite-asset inventory; and open/needs-confirmation items. Verification-checked against canon; new and unconfirmed items flagged.

---

**Total content across all splits:** ~188,264 tokens (canonical full bible is ~187,470 tokens).

Sum of splits will be slightly LARGER than the canonical due to per-file headers. Token counts are estimates (~4 chars per token).
