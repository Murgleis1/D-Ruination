# Dreamstone Ruination — Master Session Handoff

**Read this document first.** This is your orientation, your engineering reference, and your historical context for the project. It is the single source of truth for new Claude sessions joining the Dreamstone Ruination ROM hack project. Together with the bible (`bible/dreamstone_ruination_bible_v0.9.7.md`) and the source tree itself, it is the project's institutional memory.

**Status as of last update:** Phase 2a shipped (Joustroll & Jousteel sprite assets + starter palette unification). Phase 2b (Joustroll/Jousteel species data integration) is the next phase.

---

## Table of Contents

1. About the User & How They Work
2. Project Overview
3. Current Status — What's Locked, What's Open
4. Critical Files to Read at Session Start
5. Source-of-Truth Hierarchy
6. The Palette Unification — **READ THIS BEFORE TOUCHING PALETTES**
7. The Icon Non-Issue — **READ BEFORE PROPOSING ICON CHANGES**
8. Repo Structure — How D-Ruination Is Organized
9. How to Read the Bible Without Burning ~190K Tokens
10. Engineering Doctrine — File Layout
11. Engineering Doctrine — Verified Patterns by Change Type
12. The Compile Pipeline
13. The Sprite Pipeline — Reference Pattern
14. Tools Available in the Session Environment
15. Asset Library
16. Hard-Won Lessons from Prior Sessions
17. The User's Vision — Don't Lose This
18. Phase 2b Plan — Species Data Integration
19. Future Phases
20. Handing Off to a New Session
21. Last Words

---

## 1. About the User & How They Work

The user is a senior software engineer working solo on a Pokemon Emerald ROM hack. User-defined preferences (paraphrased — read them in full at session start in the userPreferences):

- **Senior SWE.** Maintains conversation context accurately. Will challenge sloppy thinking.
- **Measure twice, cut once.** Ask questions before coding. Discuss requirements before implementation. Blindly throwing code is a waste of time when goals, requirements, and environmental conditions (customer expectations, business best practices, practical considerations) haven't been confirmed.
- **Debugging protocol (mandatory):**
  - STOP — do not propose fixes immediately
  - EXAMINE the actual error message and stack trace first
  - REQUEST specific data needed (table records, model definitions, etc.)
  - ANALYZE only data you've seen, never invent assumptions
  - ADD try/catch around failing code to get detailed error information if not already present
  - IDENTIFY the exact field/property causing mismatches
  - PROPOSE ONE minimal fix based on evidence
  - **FORBIDDEN:** multiple competing solutions, lengthy explanations, changing code without seeing data first, complex workarounds when simple model changes will fix it

The user has worked with multiple Claude sessions on this project. They are technically expert and will catch incorrect assertions immediately.

**Tone observations from prior sessions:**

- The user appreciates honest pushback. If you disagree, say so politely with reasoning.
- The user dislikes flattery and excessive apology. Acknowledge mistakes once, then fix them.
- The user values predictability. Don't change scope without checking first.
- When the user gives terse responses, that's normal — not displeasure.
- When the user expresses frustration (which has happened legitimately when sessions made avoidable mistakes), acknowledge directly without performative apologizing, identify what specifically went wrong, then verify the fix before claiming completion.
- **Be honest when you are uncertain.** Performative confidence has caused real damage in prior sessions. Say "I'm uncertain because X" rather than guessing.

---

## 2. Project Overview

**Dreamstone Ruination** is a ROM hack of `dsmyst/dreamstone-mysteries` (itself a fork of `rh-hideout/pokeemerald-expansion`). It is a prequel to Dreamstone Mysteries set ~2000 years before that game's events, taking place in the ancient Cormorian Empire.

The project has approximately tier-one ROM hack scope (comparable to Radical Red, Unbound, Empyrean). It features a deep cosmological backstory (Phancero, Cormor Dream-Eater, Keerin, Treasures of Ruin), three custom starter Pokemon lines with unique Cormorian visual identities (all mechanically guaranteed-unique from selection), custom fakemon (Joustroll/Jousteel/Keerin), and an ambitious story-driven first chapter ending in the first Trial.

Project codename: `ruination` at the repo/operational level. The narrative title "Dreamstone Ruination" appears throughout the bible and commit messages. Both names are correct in their respective contexts. Do not "fix" one to the other in either direction.

### The three starter lines

| Line | Design Identity | Phase 1 Commit |
|---|---|---|
| Frigibax → Arctibax → Baxcalibur | Cormorian heraldic — charcoal + imperial gold + royal blue | `bef7b9f5` |
| Teddiursa → Ursaring → Bloodmoon Ursaluna | Bloodsnow — snow-white + chocolate brown + blood-red lunar markings | `a984a437` |
| Tinkatink → Tinkatuff → Tinkaton | Cormorian Dragon-Slayer Clan — lavender body + white hair + copper hammer | `8157e896` |

**Critical design rule:** the player's starter is mechanically guaranteed-unique — locked to display the Dreamstone Ruination design, never the canonical Game Freak design. The intent is to eliminate any shiny-hunting incentive for the starter. Players already have the only unique one in the world. See Section 6 for how this is implemented at the palette level.

### The Jousteel line

Two custom species exclusive to House Umbra's identity (Vizier Cadmus Umbra's family):

- **Joustroll** (Stage 1) — Water/Steel — low-slung wheeled body, red carapace, crab-like front claws
- **Jousteel** (Stage 2) — Water/Steel — bipedal armored arthropod-knight, **floating crystalline streamer attached at back of neck**, blue chest gem

These do not exist in canonical Pokemon. House Umbra cultivation is a centuries-old family tradition; they are the only known Pokemon species existing exclusively in Cormoria.

**Important Jousteel anatomy detail (commonly misread by AI references):** what looks like a "wrench" on the upper edge of the Jousteel overworld AI reference is actually the floating crystalline streamer. From the front it's mostly hidden behind the helmet. From the back it's prominently visible as a flowing curl on the upper-left. From the sides it flows up-and-back behind the helmet. Do not interpret this as a metallic tool — it's a flowing cyan/blue crystalline ribbon attached at the back of the neck.

### Keerin

A third fully custom fakemon mentioned in earlier project planning. Status in current phase pipeline: **[OPEN — confirm with user]**. Phase 2a delivered Joustroll/Jousteel sprite work only. Keerin sprite work and species data are not yet shipped. Before proceeding with Keerin-related work, confirm scope with user.

---

## 3. Current Status — What's Locked, What's Open

### LOCKED & SHIPPED ✓

| Item | Status | Reference |
|---|---|---|
| Project bible | v0.9.7 | `bible/dreamstone_ruination_bible_v0.9.7.md` |
| Engineering doctrine | This document, Sections 10-13 | This file |
| Frigibax line custom palette | Patch applied to codebase | Commit `bef7b9f5` |
| Blue Moon Teddiursa line Bloodsnow palette | Patch applied to codebase | Commit `a984a437` |
| Tinkatink line Cormorian Dragon-Slayer palette | Patch applied to codebase | Commit `8157e896` |
| Joustroll & Jousteel sprite assets | All 18 files committed | Commit `28a03cc8` |
| Starter palette unification | normal.pal == shiny.pal for all 9 starter species | Commit `8a6b6ae3` |
| Local compile pipeline | Validated in v0.9.6 session — recommend re-verification in new session | See Section 12 |

### IN PROGRESS / IMMEDIATE NEXT WORK

| Item | Status | Notes |
|---|---|---|
| Joustroll/Jousteel species data integration (Phase 2b) | Not started | Stats, abilities, learnsets, evolution table, INCBIN hookups |
| Keerin sprite work and species data | **[OPEN — confirm scope with user]** | Was mentioned in earlier planning; not delivered in Phase 2a |

### PENDING / FUTURE PHASES

| Phase | Item | Notes |
|---|---|---|
| 2b | Joustroll/Jousteel species data integration | See Section 18 for detailed plan |
| 3 | Trainer sprites | User has raw assets; mostly modification of existing |
| 3 | NPC overworld sprites | User has raw assets |
| 3 | Custom buildings, tilesets | User has raw assets |
| 4 | Introductory chapter through first Trial | Scripts (Poryscript), maps (Porymap), dialogue, encounters, trainer parties |

### OPEN QUESTIONS (NEED USER INPUT BEFORE PROCEEDING)

- Joustroll evolution method and level (likely level-based 36-42, specific number [OPEN])
- Joustroll & Jousteel base stats (all [OPEN])
- Joustroll & Jousteel abilities (primary + secondary + hidden, all [OPEN])
- Joustroll & Jousteel movepool / learnset (all [OPEN])
- Catch rate, EV yields, base experience yield (all [OPEN])
- Egg groups (likely Mineral or Water 3 or unique combination — [OPEN])
- Gender ratio (per bible, House Umbra cultivates these specifically — may be genderless or asymmetric — [OPEN])
- National dex slot placement among Gen 9 newcomers ([OPEN])
- Hoenn regional dex inclusion ([OPEN])
- Encounter availability — how the player acquires Joustroll/Jousteel in-game (gift event, story trigger, etc.) — [OPEN]
- Keerin scope ([OPEN])
- BST balance for Bloodmoon Ursaluna (560) vs Mega Baxcalibur (720) vs Tinkaton final form (TBD)
- Whether the Blue Moon Hermit teaches other gating moves or only Blood Moon ([OPEN])
- **Repo structure** — the codebase-as-zip pattern is fighting against ongoing development workflow. See Section 8 for the open question and three real options.

---

## 4. Critical Files to Read at Session Start

Read these in order at the start of any new session. Do not skip.

1. **This document** — you're reading it
2. **`README_START_HERE.md`** in the D-Ruination repo — original project orientation, still relevant for background
3. **`bible/INDEX.md`** in the D-Ruination repo — index of bible splits (see Section 9 for usage)
4. **Phase-relevant bible splits** — fetch only the sections you need for the current task
5. **For Phase 2b specifically:** `bible/13_cosmology_mechanics.md` (Jousteel line cosmology + custom species patterns), `bible/18_engineering_tasks.md` (engineering planning entry), `bible/07_characters_viziers.md` (Cadmus Umbra cultivation context), `bible/05_starter_lines.md` (starter palette work context)
6. **`references/`** in the D-Ruination repo — visual deliverables for quality bar reference

After reading, verify the codebase git log shows the expected commits:

```
8a6b6ae3 Unify starter palettes: make Dreamstone Ruination designs appear regardless of shiny state
28a03cc8 Phase 2a: Joustroll & Jousteel sprite assets
8157e896 Tinkatink line Cormorian Dragon-Slayer Clan palette (Dreamstone Ruination starters)
a984a437 Blue Moon Teddiursa line v10 Bloodsnow palette (Dreamstone Ruination starters)
bef7b9f5 Frigibax line custom shiny palettes (Dreamstone Ruination starters)
f7997186 Reapply "small"
```

If the git log differs, ask the user before proceeding — the codebase may have been further iterated between sessions.

---

## 5. Source-of-Truth Hierarchy

When sources of information disagree, the resolution order is:

1. **User (live message)** — the user said it now, that's the truth
2. **DM Dex** — historical canonical reference if invoked
3. **This handoff document**
4. **The source tree** — what actually compiles is authoritative for engine behavior
5. **Engine docs (pokeemerald / pokeemerald-expansion documentation)**
6. **Canon Pokemon facts** — least authoritative; this is a ROM hack with intentional deviations

When the bible and the user's current message disagree, **ask the user to clarify which takes precedence — don't silently choose.** When the bible and the source tree disagree, prefer the source tree (it's what actually compiles). Update the bible to match reality.

**Authority order in practice:**

- User said something live → that's the new truth
- Bible has a `[LOCKED]` tag → don't unlock without user permission
- Bible has `[WORKING]` or `[OPEN]` → flexible, propose changes if you have a reason
- Bible disagrees with shipped code → bible is stale; fix bible

---

## 6. The Palette Unification — READ THIS BEFORE TOUCHING PALETTES

**This section is critical. Skipping it will cause you to "fix" intentional design back into the bug we eliminated.**

### What was done

Commit `8a6b6ae3` made `normal.pal == shiny.pal` (byte-for-byte identical) for all 9 starter species, and same for `overworld_normal.pal == overworld_shiny.pal`. This is intentional.

### Why

Phase 1 patches placed the new Dreamstone Ruination designs inconsistently across the three starter lines:

- **Frigibax line:** new design in `shiny.pal`, vanilla colors in `normal.pal`
- **Teddiursa line:** new design in `normal.pal` (and also new PNG sprite art), vanilla in `shiny.pal`
- **Tinkatink line:** new design in `normal.pal`, vanilla in `shiny.pal`

The user's design intent is that the player's starter is mechanically guaranteed-unique and the player should see the Dreamstone Ruination design regardless of how the engine handles the shiny flag. The inconsistency across the three lines made this hard to implement at the engine level.

The user's solution: unify the palettes. Both `normal.pal` and `shiny.pal` contain the new design for all 9 species. Now it doesn't matter what the engine's shiny flag is set to — the player sees the Dreamstone Ruination design either way.

### What this means for future sessions

- **You do NOT need to special-case the starter's shiny flag** to make it display the right colors at the engine level. Whether the engine renders the species as shiny or not, the same Dreamstone Ruination design appears.
- **If at any point you find yourself thinking "the shiny palette is identical to the normal palette, that must be a bug" — STOP.** It is not a bug. It is the intentional design. Re-read this section.
- **Do not "fix" this back to having different normal/shiny palettes.** Doing so would re-introduce the inconsistency problem and break the design intent.
- **If the user explicitly requests distinct shiny palettes for these species later,** that's fine and the work is straightforward — but don't preemptively introduce that distinction.

### Which species are affected

All 9 starter species:
- `frigibax`, `arctibax`, `baxcalibur`
- `teddiursa`, `ursaring`, `ursaluna/bloodmoon`
- `tinkatink`, `tinkatuff`, `tinkaton`

Joustroll and Jousteel (Phase 2a) DO have distinct normal/shiny palettes — silver+gold scheme for shiny, warm peach-red for normal. They are not starters and are not subject to the unification.

---

## 7. The Icon Non-Issue — READ BEFORE PROPOSING ICON CHANGES

**This was investigated and documented as a non-issue. Do not re-open.**

### The situation

Menu icons (party menu, PC box, summary screens) for the 9 starter species render with their **canonical vanilla Game Freak colors**, not the Dreamstone Ruination designs. This is because icons render against shared icon palettes (`graphics/pokemon/icon_palettes/pal0.pal` through `pal5.pal`), NOT the species-specific `normal.pal` / `shiny.pal` files. The unification does not affect icons.

### Why this is NOT a problem

This is consistent with how the rest of the codebase treats Pokemon icons. **No Pokemon in the codebase has a "shiny icon" variant.** Icons are always shiny-agnostic, by engine design. The `iconPalIndex` field in the species data exists, but no `iconShinyPalIndex` exists. Adding it would be a non-trivial engine modification.

The starter icons looking "vanilla" matches the convention used for every other species in the game. The user has explicitly designated this a non-issue.

### What NOT to do

Do not attempt to "fix" icons by:
- Adding new shared icon palettes (pal6/pal7/pal8)
- Repainting icon PNGs with new slot indices
- Updating `iconPalIndex` in `species_info.h` to point at custom palettes
- Modifying `src/pokemon_icon.c` to add shiny icon support

Any of these would re-introduce inconsistency with the rest of the codebase and would be solving a non-problem.

### Why this is documented

A prior session spent significant effort investigating, designing, and partially implementing a fix for this "problem" before the user clarified it was a non-issue. The investigation cost real time. This documentation prevents future sessions from repeating the mistake.

---

## 8. Repo Structure — How D-Ruination Is Organized

### Current structure

The D-Ruination repo at `https://github.com/Murgleis1/D-Ruination` (default branch: `main`) is structured as a **handoff package** containing:

- Handoff documentation (this file, README, original DREAMSTONE_HANDOFF, prior phase handoffs)
- Bible (canonical + split files)
- Patches (historical Phase 1 patches)
- References (visual deliverables, concept art)
- Codebase (the actual pokeemerald-expansion fork, currently delivered as a zip)
- Assets (raw source materials, user-provided concept art, AI reference sprites)

You can fetch any file via:
```
https://raw.githubusercontent.com/Murgleis1/D-Ruination/main/<path>
```

### Repo top-level layout

```
D-Ruination/
├── SESSION_HANDOFF_MASTER.md          ← THIS DOCUMENT (read first)
├── README_START_HERE.md                ← Original project orientation
├── (historical handoffs may exist as archives)
├── bible/
│   ├── dreamstone_ruination_bible_v0.9.7.md   ← Canonical full bible (~190K tokens — do NOT fetch unless grep needed)
│   ├── INDEX.md                                ← FETCH FIRST when you need lore
│   ├── 00_thesis_and_overview.md       (~2K tokens)
│   ├── 01_cormoria_worldbuilding.md    (~20K tokens — large)
│   ├── 02_geopolitics.md               (~1K tokens)
│   ├── 03_trial_barons_viziers.md      (~4K tokens)
│   ├── 04_protagonist_arc.md           (~7K tokens — full Osrid profile)
│   ├── 05_starter_lines.md             (~17K tokens — Phase 1 starter context)
│   ├── 06_characters_royal_family.md   (~6K tokens)
│   ├── 07_characters_viziers.md        (~14K — includes Cadmus Umbra)
│   ├── 08_characters_eden_recurring.md (~8K)
│   ├── 09_characters_cult.md           (~1K)
│   ├── 10_characters_trial_barons.md   (~10K)
│   ├── 11_characters_legendary.md      (~11K)
│   ├── 12_cults.md                     (~13K)
│   ├── 13_cosmology_mechanics.md       (~23K — Jousteel line + custom species patterns)
│   ├── 14_story_spine.md               (~11K — Acts I-VI)
│   ├── 15_design_principles.md         (~11K)
│   ├── 16_bloodlines_canon.md          (~7K)
│   ├── 17_open_questions.md            (~8K — operational, not narrative)
│   └── 18_engineering_tasks.md         (~15K — engineering planning)
├── patches/                            ← Historical Phase 1 patches (reference)
├── references/                         ← Visual deliverables, concept art
├── codebase/                           ← The actual pokeemerald-expansion fork
│   └── (current codebase delivery, name varies per phase)
└── assets/                             ← Source/working materials
    └── Possible Assets For Dreamstone Ruination/
        └── Custom Asset Bases For Ruination/   ← Joustroll/Jousteel reference sprites
```

### Open question — repo structure for ongoing development

**Flagged at end of Phase 2a as unresolved.** The codebase-as-zip pattern (`codebase/dsmyst_codebase_post_phase2a_final.zip`, ~119 MB) was workable for the original handoff model but fights against ongoing development:

- Each codebase iteration is a new ~100+ MB file that may exceed GitHub's 100 MB single-file limit (depending on account specifics)
- Future trainer sprite work, additional species, etc. cannot be tracked as small incremental commits — every iteration repackages the whole zip
- Git diff/blame/log workflows don't work meaningfully on the contents

The user explicitly does NOT want to fork the upstream `dsmyst/dreamstone-mysteries` publicly (privacy concern — work-in-progress should not be visible to anyone with a GitHub URL). The user also explicitly rejected GitHub Releases as an option because Releases are for frozen snapshots, not active development.

Three remaining options:

1. **Convert D-Ruination into the live codebase repo (private),** with bible/patches/docs as folders alongside the codebase tree. GitHub free accounts support unlimited private repos. This is the most idiomatic git workflow.
2. **Keep the current zip-in-folder structure** and use Git LFS to handle the size limit. Requires LFS installation; has bandwidth quota concerns over time.
3. **Split the codebase into chunks under 100 MB** and commit as multiple zips. Ugly but works without LFS.

This is an OPEN QUESTION for the next session to resolve with the user **before** doing significant work that depends on the answer. If Phase 2b's deliverables are small enough to ship as a patch file (per the Phase 1 pattern), the structural question can be deferred again.

---

## 9. How to Read the Bible Without Burning ~190K Tokens

The canonical bible (`bible/dreamstone_ruination_bible_v0.9.7.md`) is ~6600 lines / ~190K tokens. **Do NOT fetch it in full unless you need to grep across the entire document.**

Use the split-section files instead:

**Process:**
1. Fetch `bible/INDEX.md` FIRST (~2K tokens). It lists 19 per-section files with summaries and token estimates.
2. Read the index, decide which 1-3 sections your current task actually requires.
3. Fetch only those.

**Typical fetch patterns:**

- Phase 2b engineering planning → `INDEX.md` + `13_cosmology_mechanics.md` (Jousteel line section) + `18_engineering_tasks.md`
- Cadmus Umbra context for Jousteel design → add `07_characters_viziers.md`
- Story arc context → `14_story_spine.md`
- Cosmology / Treasures / mechanics → `13_cosmology_mechanics.md` (~23K tokens, the largest single split file)
- Just want a brief overview → `00_thesis_and_overview.md` (~2K tokens)

**Edit policy:** The canonical full bible remains the authoritative reference. **All edits go to the canonical file**, then splits are regenerated. **Do not edit the split files directly** — they are derived artifacts.

---

## 10. Engineering Doctrine — File Layout

```
graphics/pokemon/<species>/      Sprites + palettes for each species
src/data/pokemon/species_info/   Per-species data (stats, abilities, evos)
  gen_1_families.h through gen_9_families.h
src/data/moves_info.h            All move data (power, PP, type, category, …)
src/data/pokemon/pokedex_orders.h Pokédex sort orders (alphabetical, etc.)
include/constants/pokedex.h      HOENN_DEX_* enum + NATIONAL_DEX_* enum
include/constants/items.h        ITEM_* constants (verify before use!)
include/constants/abilities.h    ABILITY_* constants
include/constants/species.h      SPECIES_* constants
src/pokemon.c                    HOENN_TO_NATIONAL() initializer for regional dex
src/player_pc.c                  PC starting items (NewGameInitPCItems)
data/maps/<MapName>/             Per-map scripts, events, JSON
  scripts.pory                   Poryscript SOURCE
  scripts.inc                    Compiled assembly (auto-generated from .pory)
  events.inc                     Object events / coord triggers
  map.json                       Map metadata + objects
graphics/pokemon/icon_palettes/  Shared icon palettes (pal0-pal5)
src/pokemon_icon.c               Engine code for icon rendering
include/config/pokemon.h         Pokemon-related config flags (P_GBA_STYLE_SPECIES_GFX, etc.)
```

### Universal rule: read before you edit

Before changing **anything**, run:

```bash
grep -rn "<exact identifier you're targeting>" src/ include/ data/
```

The reason: in pokeemerald-expansion, the same data shows up in multiple files (an enum + an initializer + sometimes a JSON), and you need to update *all of them* for a change to take effect. If you only edit one place, the build may succeed but the change won't appear in-game (or worse, will misbehave).

**Always confirm a constant exists before referencing it.** E.g. don't assume `ITEM_RARE_SHARD` is in stock pokeemerald — verify with grep:

```bash
grep "ITEM_RARE_SHARD" include/constants/items.h
```

This fork has custom items, abilities, and species. Always grep first.

---

## 11. Engineering Doctrine — Verified Patterns by Change Type

These patterns are verified across the Phase 1 and Phase 2a work plus prior Dracovish session.

### 11.1 Editing Pokémon stats / abilities / evolutions

**Location:** `src/data/pokemon/species_info/gen_N_families.h` where N is the generation that introduced the species' family.

**To find a species fast:**

```bash
grep -rn "SPECIES_<NAME>\b\] =" src/data/pokemon/species_info/
```

Stats are simple struct fields:

```c
.baseHP = 100, .baseAttack = 120, .baseDefense = 65, ...
```

**Abilities** are a 3-slot array `{ ability1, ability2, hidden }`. To force a single ability, fill all three slots with the same value:

```c
.abilities = { ABILITY_DEFIANT, ABILITY_DEFIANT, ABILITY_DEFIANT },
```

**Evolutions** use the `EVOLUTION(...)` macro. Common forms:

```c
.evolutions = EVOLUTION({EVO_LEVEL, 28, SPECIES_SCOVILLAIN}),
.evolutions = EVOLUTION({EVO_ITEM, ITEM_FIRE_STONE, SPECIES_SCOVILLAIN}),
.evolutions = EVOLUTION({EVO_FRIENDSHIP, 0, SPECIES_UMBREON}),
```

When swapping evolution methods, remove the old condition entirely and write the new one — don't try to add a second condition unless that's intentional.

### 11.2 Editing moves

**Location:** `src/data/moves_info.h`. One giant file, one entry per move.

**To find a move:**

```bash
grep -n "MOVE_<NAME>\] =" src/data/moves_info.h
```

Key fields:

```c
.power = 85,
.type = TYPE_FIGHTING,
.accuracy = 100,
.pp = 15,
.category = DAMAGE_CATEGORY_PHYSICAL,  // or _SPECIAL or _STATUS
```

**Gotcha — gen-conditional values.** Several moves use:

```c
.power = B_UPDATED_MOVE_DATA >= GEN_9 ? 120 : 100,
```

When the user asks for a specific power value, **replace the entire ternary with the literal value**. Leaving the ternary in place means the value depends on a config flag and you may not get the value the user wanted.

### 11.3 Sprite + palette work (battle sprites)

For each species there's a `graphics/pokemon/<species>/` directory containing:

| File | Purpose |
|---|---|
| `front.png` or `anim_front.png` | Front battle sprite (indexed, 4bpp source) |
| `back.png` | Back battle sprite (indexed) |
| `normal.pal` | JASC-format palette for normal coloring |
| `shiny.pal` | JASC-format palette for shiny coloring |
| `icon.png` | Menu icon (32x64 = 2 frames stacked vertically) |
| `overworld.png` | Overworld follower sprite (192x32 = 6 frames for canonical Gen 5+ style) |
| `overworld_normal.pal` | Follower normal palette |
| `overworld_shiny.pal` | Follower shiny palette |
| `footprint.png` | Tiny footprint (16x16) |
| `*.4bpp`, `*.4bpp.lz`, `*.gbapal`, `*.gbapal.lz` | **Compiled outputs — do not edit by hand** |
| `*f.png` variants (e.g., `anim_frontf.png`, `backf.png`) | Female variants (some species only) |

**The model:** the 4bpp sprite data references colors by *palette index*, not by RGB. At runtime, the engine loads either `normal.gbapal` or `shiny.gbapal` and that determines what each index renders as. So shiny coloring is normally a pure palette swap — same pixel data, different colors. (Exception: the Teddiursa Bloodsnow work replaced the actual PNG pixel art, not just the palette. See Section 16.4.)

### 11.4 Overworld follower palettes

Same pattern as battle sprites but a different palette file pair (`overworld_normal.pal` + `overworld_shiny.pal`). The overworld sprite uses its own 16-color palette — usually with **different index meanings** than the battle sprite. Don't reuse the battle shiny palette directly; analyze the overworld PNG's indices separately.

### 11.5 Editing in-game scripts (dialogue, wild encounters, eggs, etc.)

Every map under `data/maps/<MapName>/` has:

- **`scripts.pory`** — Poryscript source. This is what you should think of as "the source of truth."
- **`scripts.inc`** — The compiled assembly output, generated from `.pory` by the poryscript tool during build.

**Big gotcha:** depending on how the user builds the project, the `.inc` may or may not be regenerated automatically. **To be safe, edit BOTH the `.pory` and the `.inc`.** This is cheap insurance with no downside.

Common edit patterns:

| Need | Pattern (.pory) | Pattern (.inc) |
|---|---|---|
| Change wild battle species/level | `setwildbattle(SPECIES_X, lvl)` | `setwildbattle SPECIES_X, lvl` |
| Change cry | `playmoncry(SPECIES_X, CRY_MODE_NORMAL)` | `playmoncry SPECIES_X, CRY_MODE_NORMAL` |
| Change egg given | `giveegg(SPECIES_X)` | `giveegg SPECIES_X` |
| Change dialogue | `msgbox(format("text"))` | `.string "text$"` in the `*_Text_N:` label section |

When changing dialogue:

- Find the matching `Route<N>_<ScriptName>_Text_<N>:` label in the `.inc`
- Replace the `.string "..."` content
- Preserve `\n` (line break), `\l` (line break, no scroll), `\p` (page break), and the trailing `$` (end of string marker)

**Don't rename internal script labels or flag names** (`FLAG_*`, `LOCALID_*`, script function names like `Route4_Dewpider_Trigger`) when changing what they *do*. These are just identifiers; the user never sees them. Renaming them forces you to find every reference across `.pory`/`.inc`/`events.inc`/`map.json` and update them all — high risk for cosmetic gain.

**Overworld sprites for Pokemon NPCs** use the `OBJ_EVENT_GFX_SPECIES(NAME)` macro. Change in three places:

- `data/maps/<MapName>/events.inc` (the `object_event` line)
- `data/maps/<MapName>/map.json` (the `graphics_id` field)
- (If referenced in `scripts.pory`, that too, but rare)

### 11.6 PC starting items

**Location:** `src/player_pc.c`, the `sNewGamePCItems[][2]` array.

```c
static const u16 sNewGamePCItems[][2] =
{
    { ITEM_POTION, 1 },
    { ITEM_RARE_CANDY, 1 },
    // add new entries here
    { ITEM_NONE, 0 }      // sentinel — must remain last
};
```

**Important:** this affects **new games only**. Existing save files don't retroactively gain items — that's a save-state limitation, not something code can fix.

### 11.7 Adding Pokemon to the regional Pokédex

This fork uses Hoenn dex numbering for the in-game regional dex. To add a species:

**Step 1.** Add an enum entry in `include/constants/pokedex.h`. The enum is called by `HOENN_DEX_<NAME>` and the auto-incrementing values are sensitive — **inserting in the middle shifts the values of all subsequent entries**. That's safe as long as no other code stores Hoenn dex numbers persistently (seen/caught flags are stored by *National* dex number, so they're unaffected).

```c
HOENN_DEX_AERODACTYL,
HOENN_DEX_CAPSAKID,     // ← new
HOENN_DEX_SCOVILLAIN,   // ← new
HOENN_DEX_SCREAM_TAIL,
```

**Step 2.** Add the matching `HOENN_TO_NATIONAL(NAME)` line in `src/pokemon.c` so the regional→national mapping table is initialized:

```c
HOENN_TO_NATIONAL(AERODACTYL),
HOENN_TO_NATIONAL(CAPSAKID),     // ← new
HOENN_TO_NATIONAL(SCOVILLAIN),   // ← new
HOENN_TO_NATIONAL(SCREAM_TAIL),
```

**Step 3.** Verify the species already has `.natDexNum = NATIONAL_DEX_<NAME>` in its species_info entry. (Usually it does — it's set automatically when the species is defined in a `gen_N_families.h` file.)

**Step 4.** The sort orders in `src/data/pokemon/pokedex_orders.h` (alphabetical, etc.) usually already include every species in the build — check, but typically no edit needed.

### 11.8 Things that look like they should work but don't

- **Don't edit the `*.4bpp` / `*.4bpp.lz` / `*.gbapal` / `*.gbapal.lz` files directly.** They're compiled binary outputs from the PNG/PAL sources. Edit the source, delete the binary, rebuild.
- **Don't assume vanilla pokeemerald item/ability/species names exist.** This fork has additions and may have removed/renamed things. Always grep first.
- **Don't try to give the menu icon a per-species shiny variant** — see Section 7.
- **Don't rename `FLAG_*`, `LOCALID_*`, or script label identifiers** just because the user-facing content changed. The identifiers are internal; cascading renames break things and gain nothing.
- **Don't only edit `.pory` and assume the build will regenerate `.inc`.** Edit both. Cheap insurance, no downside.
- **Don't fetch the canonical full bible** unless you actually need grep-across-document — use the splits.

---

## 12. The Compile Pipeline

**The project compiles locally in the Claude session environment.** This was validated in v0.9.6. **Recommend re-verification in a new session before relying on it** — toolchain state may shift between sessions.

```bash
# One-time toolchain install (root, no sudo)
apt-get install -y binutils-arm-none-eabi gcc-arm-none-eabi libnewlib-arm-none-eabi \
                   build-essential libpng-dev pkg-config golang-go

# One-time per working tree: build Linux poryscript
# (The bundled one is Mach-O macOS and won't run on Linux)
cd /tmp && git clone --depth 1 https://github.com/huderlem/poryscript.git
cd /tmp/poryscript && go build -o poryscript .
cp /tmp/poryscript/poryscript <working_tree>/tools/poryscript/poryscript
chmod +x <working_tree>/tools/poryscript/poryscript

# Build
cd <working_tree>
make tools          # Builds bundled C/C++ tools (first time only)
make -j$(nproc) modern

# Output: pokeemerald.gba (32MB BPEE01)
```

**After every code change, run the build to validate before shipping a patch to the user.** This is now part of the workflow — don't ship untested patches if the pipeline works.

**Build artifacts:**
- The `build/` directory holds .o files and can be deleted any time — `make clean` does this. When shipping a zip of the source for someone else to build, **exclude `build/`** to save space and avoid stale-cache issues.
- After making changes, the user typically tests on mGBA. If you can't run a build yourself, do a final grep pass to confirm every change landed in every file it needed to.
- Don't ship 32MB .gba files to the user unless requested; they're large.

---

## 13. The Sprite Pipeline — Reference Pattern

For palette/sprite work, the locked process is:

1. **Read the canonical sprite.** Use PIL to load `anim_front.png` (or `front.png`), get the palette (`.getpalette()`), enumerate pixel counts per index (`Counter(img.getdata())`).

2. **Identify the dominant fur indices and the marking indices.** Print each index with RGB + pixel count. Write a small Python script that isolates each index visually:

```python
from PIL import Image
import numpy as np
img = Image.open("front.png")
arr = np.array(img)
for idx in range(16):
    iso = np.full((64,64,3), 200, dtype=np.uint8)
    iso[arr == idx] = [255, 0, 0]
    Image.fromarray(iso).resize((512,512), Image.NEAREST).save(f"idx_{idx:02d}.png")
```

3. **Plan the transformation.** Fur → white (or whatever the line's body color is), markings → red (or whatever the line's accent is). Detect "overloaded" indices used for multiple semantic zones — these need per-pixel separation (see Section 16.4).

4. **Quantize all RGB values to multiples of 8 before writing .pal files** (MANDATORY — see Section 16.6):

```python
def q8(rgb):
    return tuple((c // 8) * 8 for c in rgb)
```

5. **Write .pal files in JASC format** with proper newlines:

```python
def write_jasc(path, palette):
    lines = ["JASC-PAL", "0100", "16"]
    for r, g, b in palette:
        lines.append(f"{r} {g} {b}")
    # Use plain "\n" — let git's autocrlf handle EOL conversion if needed
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
```

**Format:**
```
JASC-PAL
0100
16
<R> <G> <B>           ← 16 lines, one per palette slot, space-separated
...
```

Index 0 is typically the transparent/background color and is conventionally `152 208 160` (the standard pokeemerald sprite background green).

6. **Write modified PNGs** with `putpalette()` and (if per-pixel mods) `putdata()`. Process female variants if any (`ls <species>/*f.png`).

7. **Delete the stale compiled artifacts** so the build regenerates them:

```bash
rm graphics/pokemon/<species>/shiny.gbapal \
   graphics/pokemon/<species>/shiny.gbapal.lz \
   graphics/pokemon/<species>/overworld_shiny.gbapal \
   graphics/pokemon/<species>/overworld_shiny.gbapal.lz
```

The make rule `%.gbapal: %.pal` should rebuild them, but stale binaries can confuse incremental builds. Removing them is cheap insurance.

8. **Preview visually before committing.** Apply the new palette to the indexed PNG in software and confirm it matches the reference. **Render the PNG with the actual palette the engine will load** — don't claim "done" without this step. See Section 16.1.

9. **Build the ROM** to validate (Section 12).

10. **Generate git patch** via `git format-patch -1 -o /path/`.

11. **Update bible** with the locked palette values, design notes, file locations.

### Iteration expectations

Sprite work usually goes through 5-10+ palette versions before locking. The Teddiursa line went through v1-v10 (with many .1, .2, .3 sub-versions during overworld refinement). The user has strong opinions about visual details — expect them to spot small issues you missed. Build extreme-zoom (40x+) comparison sheets when iterating on details.

---

## 14. Tools Available in the Session Environment

### Already installed (typically)

- **ARM cross-compiler:** `arm-none-eabi-gcc` 13.2.1, `arm-none-eabi-as`, `arm-none-eabi-ld`, `arm-none-eabi-objcopy` (via apt)
- **Build essentials:** `make`, `gcc`, `g++`, `pkg-config`, `libpng-dev`
- **Go:** for building poryscript
- **Python 3 + PIL** for sprite manipulation
- **Git** for patch generation

Verify availability at session start:

```bash
which arm-none-eabi-gcc && arm-none-eabi-gcc --version
which make && which python3
```

### Bundled in dsmyst tree

Built via `make tools`: `aif2pcm`, `bin2c`, `gbafix`, `gbagfx`, `jsonproc`, `mapjson`, `mid2agb`, `preproc`, `ramscrgen`, `rsfont`, `scaninc`, `trainerproc`

### NOT installed but available

- **Porymap** (the map editor) — would need to be installed if doing map work. Map files are JSON + binary tilemap blobs and can be edited programmatically without Porymap if needed.
- **mGBA** (emulator) — `tools/mgba/` exists in dsmyst but typically not run in-session. For ROM verification you can ship the .gba to the user and have them test in their local mGBA.

### Network restrictions

Egress is whitelisted. You can typically reach:

- `github.com`, `codeload.github.com`, `raw.githubusercontent.com` (for fetching project files)
- `archive.ubuntu.com`, `security.ubuntu.com` (for apt)
- `pypi.org`, `files.pythonhosted.org` (for pip)
- `registry.npmjs.org`, `npmjs.com` (for npm)
- `crates.io`, `static.crates.io` (for cargo)
- `api.anthropic.com` (for Claude API in Artifacts, if used)

You CANNOT reach arbitrary websites or the user's local machine. If you need a resource from elsewhere, ask the user to upload it to `/mnt/user-data/uploads/`.

---

## 15. Asset Library

The user has uploaded reference assets to the D-Ruination repo at `assets/Possible Assets For Dreamstone Ruination/`. The Joustroll/Jousteel custom asset bases live at `assets/Possible Assets For Dreamstone Ruination/Custom Asset Bases For Ruination/`:

- `Joustroll - Front.png` (64x64 RGBA, 10 colors)
- `Joustroll - Back.png` (note double-space in filename; 64x64 RGBA, 9 colors)
- `Jousteel - Front.png` (64x64 RGBA, 12 colors)
- `Jousteel - Back.png` (64x64 RGBA, 11 colors)

**Before starting any phase that uses these assets:**
- Confirm the assets are still present in the repo at the expected paths
- Inventory what sprites exist for each species/fakemon
- Identify what's missing
- Plan the production work

**Don't assume what's there or isn't — inventory before planning.** This is a recurring lesson: prior sessions have failed to read available materials proactively and asked the user questions that were already answered in the asset library.

---

## 16. Hard-Won Lessons from Prior Sessions

These mistakes were made in prior sessions and cost real time. Future sessions must internalize them.

### 16.1 "Done" requires verification of player-visible output

The previous Claude session shipped three Phase 1 starter palette patches and called them done. Files were committed, palettes were valid, builds worked. But **no one actually rendered the sprites and looked at them** to confirm the player would see the intended design.

It turned out the Phase 1 patches placed the new designs in inconsistent slots across the three lines (`shiny.pal` for Frigibax, `normal.pal` for the other two). This would have caused the player to see vanilla colors for Teddiursa and Tinkatink lines when the starter was given as guaranteed-shiny. The bug shipped silently across three commits because no session verified by rendering.

**Rule:** When you finish sprite or palette work, **render the PNG with the actual palette the engine will load** and look at the output. Confirm the player's experience matches the design intent. Do not claim "done" without this step.

A byte-level verification pattern: render PNG + palette → bytes → compare with expected. Use this approach to programmatically verify rendered output matches design intent.

### 16.2 Don't trust AI reference at face value

The user's AI-generated reference sprites for Jousteel's overworld misinterpreted the floating crystalline streamer as a metallic wrench tool. A prior interpretation went deep down the path of treating it as a wrench before the user corrected the misread. Always cross-check overworld AI references against the actual battle sprite anatomy — the battle sprite is the source of truth.

### 16.3 Read engine wiring before designing fixes that touch it

A prior session started designing a new shared icon palette system (pal6/7/8) for the starter lines before realizing the user considered the icon mismatch a non-issue (see Section 7). Significant time was wasted on a fix to a non-bug. Before touching engine code (`src/pokemon_icon.c`, `src/data/pokemon/species_info/*.h`, `src/graphics.c`), confirm with the user that the underlying problem is one they want solved at all.

### 16.4 Per-pixel PNG edits, not just .pal swaps (Bloodsnow lesson)

The Frigibax line shipped as a palette-only patch — `shiny.pal` and `overworld_shiny.pal` files modified, no PNG changes. This works when the canonical artist used distinct palette indices for every semantically distinct body part.

**The Teddiursa line did NOT have that luxury.** Specifically:

- Canonical Ursaring uses idx 8 (cream yellow #F8E880) for BOTH the chest ring AND the chest fluff/upper-lip area on the face. A pure palette swap to red would put red on the face, not just the ring.
- Canonical Ursaring uses idx 12 (tan #C09848) for BOTH the lower lip AND body shadow accents. A pure palette swap of fur to white would lose the lip detail.
- Canonical Teddiursa uses idx 6 (white) for the forehead crescent AND small body highlights. Swapping idx 6 to red would put red dots on the body.

The solution was **per-pixel index reassignment in the PNG** before applying the palette swap. This requires:

1. Identify which canonical palette index is "overloaded" (used for multiple semantically distinct body parts)
2. Find a free or duplicate palette slot (e.g., idx 15 if the canonical embedded palette has a duplicate, or repurpose idx 13/14 if rarely used)
3. Reassign the **specific pixels** of one usage zone (e.g., face pixels) to the new slot via spatial clustering (8-connected pixel clustering with position/size heuristics)
4. Write the new palette so the original slot = red marking, the new slot = preserved canonical color

This kind of surgical preservation also applies to **tiny isolated pixel clusters (3-6 pixels)** that serve as anatomical edge details — the snout edge meeting the cheek, the inner ear curl, the brow ridge. These tiny clusters use the same palette index as the large body color, so when the body becomes white in the Bloodsnow remap, these tiny details ALSO become white and the sprite loses anatomical readability. Fix is per-pixel surgical preservation.

When iterating with the user on sprite quality, expect 2-4 rounds of this kind of surgical detail work. Build extreme-zoom comparison sheets (40x+) to verify each surgical fix worked.

### 16.5 Quirk: front.png and back.png have DIFFERENT embedded palettes in some species

In some species (Dracovish was one), `back.png`'s embedded PNG palette differs from `front.png`'s. The embedded palettes only affect the PNG→4bpp conversion at build time — at runtime the game uses `normal.gbapal`/`shiny.gbapal` for *both* sprites.

So:
- If you open back.png in an image viewer, it may look "wrong" — that's pre-existing repo behavior, not a real bug.
- What matters is that for a given logical palette index, the front and back sprites use that index for the same body part (e.g. "main body color"). If the original artist set this up correctly, your shiny palette swap works uniformly across both sprites. If they didn't, you have a deeper sprite problem that requires re-indexing one of the PNGs.

### 16.6 GBA color quantization is mandatory

**RGB values must be quantized to multiples of 8 before writing .pal files.** The GBA uses 5 bits per channel = 32 discrete values per channel = 8-step quantization (0, 8, 16, ..., 248). Non-multiple-of-8 values get rounded by the build, so what you preview in design-time PIL won't match what the game renders.

```python
def q8(rgb):
    return tuple((c // 8) * 8 for c in rgb)
```

Apply this to every RGB triple before writing to the `.pal` file or before calling `img.putpalette()`.

**Side effect on design-time hacks:** Some palette-design code uses tiny warm-tint adjustments like `(val + 2, val, val - 2)` to make whites read as "slightly warm." These offsets are lost in quantization (since 2 < 8) and the result is pure cool gray. If you want a warm-tinted white that survives quantization, the offset needs to be 8+ in at least one channel, which is visually too much. Accept that pure-quantized whites are pure cool whites.

### 16.7 The CRLF byte-level bug

When writing JASC `.pal` files in Python, do NOT use `open(path, "w", newline="\r\n")` combined with explicit `"\r\n".join(lines)`. Python interprets the `newline` parameter as a translation directive, and writing `"\r\n"` explicitly produces `"\r\r\n"` (double-CRLF) on disk. This creates files that parse silently incorrectly — readers may get wrong color values without any error message, and the bug surfaces only at render time when colors come out wrong.

**Correct pattern:** `open(path, "w")` with `"\n".join(lines) + "\n"`. Let git's autocrlf handle EOL conversion on commit if the project's `.gitattributes` requires CRLF for `.pal` files.

### 16.8 Wrong y-threshold for cluster separation

Prior session iteration used a y-coordinate threshold (`y < 20` for face vs `y >= 20` for ring) to separate two regions sharing a palette index. The chest ring actually extended from y=15 to y=24, so the threshold incorrectly classified part of the ring as face. The correct heuristic was **cluster-size based** (largest cluster = ring, small clusters = face details), not a y-threshold.

**Lesson:** When a heuristic doesn't fit the data, use a different heuristic. Don't keep tightening thresholds.

### 16.9 The `P_GBA_STYLE_SPECIES_GFX` flag

In `dsmyst/include/config/pokemon.h:48`:

```c
#define P_GBA_STYLE_SPECIES_GFX         FALSE
```

When FALSE (default in dsmyst), the build uses `anim_front.png`, `back.png`, `normal.pal` — the modern Gen 4/5-style sprites.

When TRUE, the build uses `anim_front_gba.png`, `back_gba.png`, `normal_gba.pal` — the legacy GBA-style sprites.

**For all production work, modify the non-`_gba` files only.** The `_gba` variants are the alternative code path the current project does not use. If a future config change flips this flag, the `_gba` variants would need to be updated, but that's a separate engineering decision.

### 16.10 Female Pokemon variants

Some species have **female variants** with different sprite files:

- `anim_front.png` (male) + `anim_frontf.png` (female)
- `back.png` + `backf.png`
- `overworld.png` + `overworldf.png`

Ursaring is one of these. Both male and female variants share the same `normal.pal` and `overworld_normal.pal`, so palette work applies to both automatically. But if you're doing per-pixel PNG modifications, you need to **process the female variants separately** with the same transformations applied. The Bloodsnow patch processed all 6 Ursaring sprite files.

When working on a species, run:

```bash
ls graphics/pokemon/<species>/*f.png 2>/dev/null
```

to detect female variant files. If present, mirror all PNG modifications to them.

### 16.11 Read handoff docs FIRST, not when stuck

A prior session had DREAMSTONE_HANDOFF.md available from session start and didn't read it until late in the session. As a result, that session treated sprite work as design-only and didn't integrate into the codebase until the user pointed out it should have been doing so all along.

**Lesson:** Read handoff docs FIRST. Not when you remember to. Not when stuck. FIRST.

### 16.12 Mis-identified canonical palette indices repeatedly

In Teddiursa work, a prior session confused which idx was the forehead crescent (idx 6 white) vs which was the muzzle cream (idx 9 cream). For Ursaring, "outer lips" was assumed to mean the canonical mouth-red but it actually meant the idx-11 face mask. The wrong indices got changed in early iterations.

**Lesson:** When the user describes a body part, use a Python snippet to highlight that index visually and confirm with the user before changing it. Don't trust your assumption about anatomy.

### 16.13 Integrate early, iterate inside the codebase

A prior session iterated through v1 → v10 (with sub-versions) of sprite design before any code reached the actual codebase. This was inefficient — should have integrated v4-v5 (acceptable quality), then iterated INSIDE the codebase. Easier to iterate when changes are live.

**Lesson:** Integrate early. The patch workflow is cheap. Get something into the codebase that compiles, then iterate from there.

### 16.14 Context management for sprite-heavy sessions

This project generates a LOT of intermediate analysis artifacts — preview renders, isolation images, comparison sheets, multiple palette iterations. Each consumes context window space. To manage:

- Use the bible splits. Don't fetch the canonical full bible unless you need cross-section grep.
- Don't view the same image more than once. Once inspected, work from notes.
- Don't preview every intermediate step. Iterate in code, preview only when meaningful progress justifies it.
- Use comparison sheets sparingly — a single end-of-iteration review is more useful than 8 individual previews.
- Clear unused script files when done — don't accumulate 15 versions of palette files.

---

## 17. The User's Vision — Don't Lose This

This is what makes this project worth building. Internalize the user's tonal goals.

### Project thesis (per bible Section 1)

> "Partnership with Pokemon is sacred and irreplaceable. The villain is not a person — it is the COSMIC HORROR of having that bond corrupted, stolen, or replaced."

### The Cormorian Empire is...

- A nominally-civilized imperial nation hiding genuine darkness
- The kind of place where "noble" titles carry weight but the rank-and-file military has its own honor codes
- Where children of "Nomad" rank are designated as expendable
- Where the founding myth (Cormor Dream-Eater + Keerin pact) is whispered about but actively suppressed

### The first Trial chapter is...

- The player's first contact with the cosmological horror
- Should feel mythic — a small village quest that turns into something Vastly Larger Than Expected
- The pacing should be deliberately slow at the start (build relationships with starter, party, environment) then accelerate

### The starter trio identity

- **Frigibax line:** Cormorian heraldic — charcoal + imperial gold + royal blue. The "imperial pride" pick.
- **Teddiursa (Blue Moon / Bloodsnow) line:** Snow-white + chocolate brown + blood red. The "lunar mystic" pick. Direct evolution Ursaring → Bloodmoon Ursaluna (skip regular Ursaluna).
- **Tinkatink (Cormorian Dragon-Slayer Clan) line:** Soft lavender body + white hair + copper hammer. The "third axis" pick.

All three are guaranteed-unique mechanically — players never see the canonical pink/normal Tinkatink, the canonical brown Teddiursa, or the canonical normal Frigibax. The custom palettes are the only ones the player encounters.

### Key recurring themes

- The four sealing vessels (Treasures of Ruin) being broken / inverted
- The Blue Moon Hermit as last carrier of pre-Cormorian oral tradition
- "Always unique" starters as story-mechanical signal (these are Vizier Cadmus Umbra's hand-picked partners)
- Justice (the Iron Valiant royal heirloom) as a symbol of corruption-of-virtue
- Mega Evolution as Cormorian state monopoly

If you write Pokedex flavor text, dialogue, or any creative content, **stay anchored to these themes.** The user will notice if the tone drifts.

---

## 18. Phase 2b Plan — Species Data Integration

Phase 2b is the **species data integration** for Joustroll and Jousteel. The sprite assets are in place at `graphics/pokemon/joustroll/` and `graphics/pokemon/jousteel/`. They need to be wired into the engine as actual playable species.

### Files Phase 2b will touch (minimum scope)

- **`include/constants/species.h`** — Add `SPECIES_JOUSTROLL` and `SPECIES_JOUSTEEL` enum entries
- **`include/constants/pokedex.h`** — Add `NATIONAL_DEX_JOUSTROLL` and `NATIONAL_DEX_JOUSTEEL` enum entries (and optionally `HOENN_DEX_*` entries if including in regional dex)
- **`src/data/pokemon/species_info/gen_9_families.h`** — Add full `SpeciesInfo` entries for both species (recommended block since they're new species). Includes:
  - `iconSprite`, `iconPalIndex`
  - Base stats
  - Types (Water/Steel for both)
  - Abilities (primary + secondary + hidden)
  - EV yields, catch rate, base experience yield, friendship
  - Growth rate, egg groups, gender ratio
  - Evolution table (Joustroll → Jousteel)
  - Learnset reference, tutor moves, TM compatibility
  - Pokedex entries (heightAndWeight, dexDescription, color, body shape)
- **`src/data/graphics/pokemon.h`** (or equivalent) — INCBIN references for the new species' graphics files
- **`src/data/pokemon/pokedex_orders.h`** — National dex ordering entries
- **Audio/cry data** — Cry sound registration (the build will need at least placeholder cry files)
- **Evolution table data** — Joustroll → Jousteel evolution method
- **Learnset files** — Move learnsets

### Design decisions [OPEN] for Phase 2b

Per bible Section 9 "The Jousteel Line" (fetch `bible/13_cosmology_mechanics.md`), the following are open and need user input:

- Evolution method and level (likely level-based ~36-42, specific number [OPEN])
- Base stats (all [OPEN])
- Abilities (primary + secondary + hidden, all [OPEN])
- Movepool (learnset, TM compatibility, all [OPEN])
- Catch rate, EV yields, base experience yield ([OPEN])
- Egg groups (likely Mineral or Water 3 or unique combination — [OPEN])
- Gender ratio — may be genderless or asymmetric ([OPEN])
- National dex slot placement ([OPEN])
- Hoenn regional dex inclusion ([OPEN])
- Encounter availability — how the player acquires them ([OPEN])

**Strongly recommended:** Phase 2b should start with a design discussion of these open items BEFORE touching code. The "measure twice, cut once" rule applies hard here. Get the user's intent on stats/abilities/learnsets/etc., then implement.

### Optional but desirable for Phase 2b

- Evolution scene rendering verification — new species may need verification that they animate correctly
- Dex entries text content (needs user-provided lore)
- Joustroll/Jousteel real footprints (currently blank placeholders — see Section 16 for the placeholder approach)

### Recommended Phase 2b workflow

1. Re-read this handoff and confirm Phase 2a state matches expectations (git log verification)
2. Fetch bible/13_cosmology_mechanics.md and bible/18_engineering_tasks.md for design context
3. Open design conversation with user on the [OPEN] items above
4. Once user provides intent, plan the file modifications using the grep-first pattern from Section 10
5. Implement species_info entry first, then INCBIN hookups, then constants, then dex registration
6. Build the ROM to validate
7. Generate patch
8. Update bible with locked design decisions

---

## 19. Future Phases

| Phase | Item | Notes |
|---|---|---|
| 3 | Trainer sprites | User has raw assets; mostly modification of existing |
| 3 | NPC overworld sprites | User has raw assets |
| 3 | Custom buildings, tilesets | User has raw assets |
| 4 | Introductory chapter through first Trial | Scripts (Poryscript), maps (Porymap), dialogue, encounters, trainer parties |

These phases will increase the pressure on the repo structure question (Section 8). Trainer sprites in particular will produce many small commits over time, which fights against the codebase-as-zip pattern.

---

## 20. Handing Off to a New Session

If you (the current session) need to hand off to a future session, do this:

1. **Update this MASTER handoff doc** with everything new that happened — preserve the "evolving truth" aspect
2. **Update the bible** if any locked decisions changed
3. **Update the engineering doctrine sections** if any new patterns/lessons learned
4. **Ensure the working tree is committed** (`cd <codebase> && git status` should be clean or have a clearly-marked WIP branch)
5. **Tell the user** explicitly that you're at a good handoff point so they can start fresh

Don't be afraid to recommend a fresh session to the user when:

- The conversation has been very long and context space is tight
- You've hit the same wrong assumption multiple times (a fresh session may break the pattern)
- Major scope change in the work — fresh perspective helps

---

## 21. Last Words

The user is a thoughtful, deliberate developer who cares deeply about this project. They have been generous with explanations, patient through extensive iteration, and clear about what they want even when frustrated with avoidable mistakes. Respect that.

**The biggest unlocks established through prior phases:**

- **The compile pipeline works locally** (v0.9.6). Don't hand the user untested code.
- **Read handoff docs FIRST** (v0.9.6 lesson, repeated in Phase 2a). All your context first.
- **Verify rendered output before claiming "done"** (Phase 2a hard lesson). Files compiling is not the same as the player seeing the right thing.

When honest pushback is warranted, deliver it with reasoning. When honest correction comes back at you, accept it without performative apologizing. Direct engineering-style communication.

The project is worth building.

— Synthesized from v0.9.6 SESSION_HANDOFF, DREAMSTONE_HANDOFF engineering doctrine, and Phase 2a/2b handoff drafts.
