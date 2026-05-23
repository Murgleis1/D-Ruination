# SESSION HANDOFF — Dreamstone Ruination Phase 2

**Read this document first.** This is your orientation. After this, read the other documents in this package in the order listed at the bottom.

You are a Claude instance picking up the Dreamstone Ruination ROM hack project from a prior Claude session. The prior session shipped **Phase 1** (custom palettes for all three starter Pokemon lines) and was about to begin **Phase 2** (integrating new Joustroll and Jousteel species as fully custom-implemented Pokemon) when context-window space ran out. This handoff is to give you everything needed to continue Phase 2 from a clean chat.

---

## The user

Senior software engineer working solo on a Pokemon Emerald ROM hack (Dreamstone Ruination). User-defined preferences in their account:

- **"Measure twice, cut once"** — engage in discussion before throwing code. Confirm understanding of goals, requirements, and environment before writing.
- **Retain context accurately at all times.** Ask if you need more information.
- **Real-world implications matter** — business best practices, customer expectations, practical considerations.
- **Debugging protocol** — STOP → examine actual error/stack → request specific data needed → analyze only the data provided → propose ONE minimal fix. NEVER suggest multiple solutions or change code without seeing actual data first.

The user has previously worked with multiple Claude sessions on this project. They are technically expert and will catch incorrect assertions immediately. Be honest when you're uncertain.

---

## The project

**Dreamstone Ruination** is a ROM hack of `dsmyst/dreamstone-mysteries` (which is itself a fork of `rh-hideout/pokeemerald-expansion`). It is a *prequel* to Dreamstone Mysteries set ~2000 years before that game's events, taking place in the ancient Cormorian Empire. The project is approximately *tier-one ROM hack* scope (comparable to Radical Red, Unbound, Empyrean).

The locked lore (Section 6 of the v0.9.7 bible) defines three starter Pokemon, each a customized version of a canonical Pokemon line, presented as "uniquely-colored Pokemon" to the prince by his tutor Cadmus Umbra:

1. **Frigibax line** (Dragon/Ice) — Cormorian imperial heraldic palette (charcoal + imperial gold + royal blue) — **Phase 1 shipped, commit `bef7b9f5`**
2. **Teddiursa "Blue Moon" line** → Bloodmoon Ursaluna — snow-white fur + blood-red lunar markings — **Phase 1 shipped, commit `a984a437`**
3. **Tinkatink line** — Cormorian Dragon-Slayer Clan palette (soft lavender body + white hair + copper hammer) — **Phase 1 shipped, commit `8157e896`**

All three starter lines are *always-shiny mechanically* — players never see the canonical pink/normal Tinkatink, the canonical brown Teddiursa, or the canonical normal Frigibax. The custom palettes are the only palettes the player encounters.

Beyond the starters, the project introduces **two fully custom species** as a key part of House Umbra's identity: **Joustroll** (Stage 1) and **Jousteel** (Stage 2). These do not exist in canonical Pokemon at all. They are a **Water/Steel** crab-knight evolution line cultivated exclusively by House Umbra (Vizier Cadmus Umbra's family), and they are **the only known Pokemon species that exists exclusively in Cormoria**. The user provided reference sprites for these in the `assets/Possible_Assets_For_Dreamstone_Ruination.zip` archive. **Phase 2 = implementing Joustroll and Jousteel as actual playable species in the codebase.**

---

## What this handoff package contains

```
phase2_handoff/
├── SESSION_HANDOFF_PHASE2.md        ← YOU ARE HERE — read first
├── README_START_HERE.md              ← Original handoff start doc (still valid)
├── DREAMSTONE_HANDOFF.md             ← Engineering doctrine (still authoritative)
│                                       Sections 1-9: general patterns
│                                       Section 10: v0.9.6 lessons from Bloodsnow integration
│                                       Section 10.5: ALWAYS-SHINY lines go in normal.pal
│                                       Section 10.6: female-variant per-pixel duplication
│                                       Section 10.7: compile pipeline (local, not GenSpark)
├── SESSION_HANDOFF_v096.md           ← The handoff doc Phase 1 started from (historical reference)
├── bible/
│   └── dreamstone_ruination_bible_v0.9.7.md   ← CURRENT LOCKED LORE (~6600 lines)
│                                       v0.9.7 included: Eden as deuteragonist, Brie as Trial
│                                       Baroness, Ambrose Caymen, Female Rock Vizier, Jordan
│                                       Ramses + Wakahisa, Mega-Dreamstone Shard Quest, Tinkatink
│                                       dragon-slayer bloodline, Solomonar title, Tinkaton BST
│                                       560, Behemoth Bash custom move, Vizier gauntlet reorder
│                                       Terminology sweeps: Trial Lord→Trial Baron (66 occurrences),
│                                       Supreme Sage→Lunacy (29 occurrences)
├── patches/
│   ├── 0001-Frigibax-line-custom-shiny-palettes-Dreamstone-Ruina.patch
│   ├── 0001-Blue-Moon-Teddiursa-line-v10-Bloodsnow-palette-Dream.patch
│   ├── 0001-Pipeline-validation-v2-Galarian-Zigzagoon-shiny-pale.patch
│   └── 0001-Tinkatink-line-Cormorian-Dragon-Slayer-Clan-palette-.patch   ← PHASE 1 SHIPPED
├── references/
│   ├── frigibax_line_shiny_final_review.png
│   ├── bloodsnow_v10_final_reference.png
│   ├── tinkatink_line_v3_final_reference.png   ← PHASE 1 visual confirmation
│   └── tinkatink_user_concept_art.png          ← User's hand-drawn concept (anchor reference)
├── codebase/
│   └── dsmyst_codebase_post_phase1.tar.gz      ← ~100MB; codebase with all 3 Phase 1 commits
│                                                  applied. Git log shows the three palette
│                                                  commits on top of Phase 1's baseline.
└── assets/
    └── Possible_Assets_For_Dreamstone_Ruination.zip   ← ~68MB; user's full asset library
                                                          including Joustroll/Jousteel front+back
                                                          reference sprites at 64x64 RGBA
```

---

## Critical lessons learned during Phase 1 (do not repeat my mistakes)

### Lesson 1: Read the bible's locked content, then read it again

The bible is the source of truth. It has been carefully iterated across many sessions. **Do not assume you remember it correctly.** I made mistakes earlier in the session by misremembering character relationships (Domdaniel vs Silas, Cadmus/Silas type specialties, etc.) and the user had to correct me. **When uncertain, grep or read the relevant bible section directly.**

### Lesson 2: Sprite design is not just palette swap

The Tinkatink palette work required:
- Per-index pixel-isolation analysis (DREAMSTONE_HANDOFF.md Section 10.1)
- Recognition that **front.png and back.png have DIFFERENT embedded palettes** in many species (Dracovish quirk, Section 4.3) — the canonical artist may have used the same logical palette index for different semantic body parts in the two sprites. This creates unsolvable palette-only-conflicts (Section 10.1 Ursaring problem).
- Separate analysis for the **overworld.png** which has its own 16-color palette with different index meanings than the battle sprite (Section 4.4)
- **All RGB values must be multiples of 8** (Section 10.3) — GBA uses 5 bits/channel; non-8-multiples get rounded by the build and won't match design-time preview

### Lesson 3: Phase 1 was palette-only; Phase 2 is from-scratch species addition

Phase 1's three patches are all palette-file modifications (`normal.pal`, `overworld_normal.pal`). No PNG byte modifications, no new species data. **Phase 2 is categorically different work** — adding new species per Section 9 of DREAMSTONE_HANDOFF.md is a multi-file operation touching at minimum:

- `graphics/pokemon/joustroll/` and `.../jousteel/` directories with ~9-12 files EACH (front.png, back.png, icon.png, overworld.png, footprint.png, normal.pal, shiny.pal, overworld_normal.pal, overworld_shiny.pal, plus the compiled `.gbapal` `.4bpp` `.4bpp.lz` `.gbapal.lz` artifacts that the build generates)
- New `SPECIES_JOUSTROLL` / `SPECIES_JOUSTEEL` constants in `include/constants/species.h`
- New `NATIONAL_DEX_*` enum entries (`include/constants/pokedex.h`)
- New species data in `src/data/pokemon/species_info/gen_N_families.h` (Gen 9 block recommended since they're new species; the bible has these mostly as `[OPEN]` items — stats/abilities/learnsets need to be designed)
- Cry data registration in audio data
- `pokedex_orders.h` entries
- Optional but desired: regional Hoenn dex registration (per Section 4.7)

### Lesson 4: Phase 2 is properly two phases

The prior Claude (me) recommended scoping Phase 2 tightly:
- **Phase 2a (this next session): sprite assets ONLY** — the four sprite contexts per species (front, back, icon, overworld) plus all their palette files, plus the conversion of the user's RGBA reference sprites to the indexed 4bpp PNG format the pokeemerald-expansion build expects.
- **Phase 2b (a separate session): species data integration** — stats, abilities, learnsets, evolution method, dex slot, encounter availability, possibly the Hoenn regional dex integration.

This scoping was about to be confirmed with the user when context-window space ran out. **Confirm with the user that this Phase 2a / Phase 2b split is still acceptable** before proceeding.

### Lesson 5: The compile pipeline is local, not GenSpark

DREAMSTONE_HANDOFF.md Section 10.7 documents the local ARM compile pipeline. The user typically has their own working build environment, so you do NOT need to attempt local compilation as part of delivery. **Ship the patch, the user verifies on their end.** The user has explicitly said (in the prior session) "I already know that these changes work due to my previous experience" — they trust the well-tested pipeline patterns and don't require us to compile-test.

If the user asks you to compile to verify, the install commands per Section 10.7 are:
```
apt-get install -y binutils-arm-none-eabi gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential libpng-dev pkg-config golang-go
```
Then replace the bundled Mach-O `tools/poryscript/poryscript` with a Linux ELF built from source at https://github.com/huderlem/poryscript.git, then `make tools && make -j$(nproc) modern`. Output: `pokeemerald.gba` 32MB BPEE01.

### Lesson 6: Approach context-management thoughtfully

This project generates a LOT of intermediate analysis artifacts — preview renders, isolation images, comparison sheets, multiple palette iterations. Each one consumes context window space. The prior Claude session burned through space on:
- Bible expansion (v0.9.7 took ~6600 lines)
- Three sprite-line analyses (Frigibax was inherited; Bloodsnow was inherited; Tinkatink was new this session)
- The Phase 2 setup investigation

**For Phase 2 sprite work, expect even more intermediate artifacts** because we'll be doing actual pixel art creation (icons + overworld follower animations require original sprite work, not just palette swaps).

To manage this:
- **Don't `view` the same image more than once.** Once you've inspected an isolation image and noted what it represents, work from notes.
- **Don't preview every intermediate step.** Iterate in code, preview only when meaningful progress justifies it.
- **Use comparison sheets sparingly** — a single end-of-iteration review sheet is more useful than 8 individual previews.
- **Clear unused script files when done** — don't accumulate 15 versions of palette files.

---

## Where Phase 2 stood when context ran out

The prior Claude completed the following Phase 2 investigation:

1. **Confirmed Joustroll/Jousteel are NOT in the codebase yet** — fully from-scratch species addition needed
2. **Located the reference sprites** at `Possible_Assets_For_Dreamstone_Ruination.zip` → `user_assets/Possible Assets For Dreamstone Ruination/Custom Asset Bases For Ruination/`
   - `Joustroll - Front.png` (64x64 RGBA, 10 unique colors)
   - `Joustroll  - Back.png` (64x64 RGBA, 9 unique colors — note the double-space in filename)
   - `Jousteel - Front.png` (64x64 RGBA, 12 unique colors)
   - `Jousteel - Back.png` (64x64 RGBA, 11 unique colors)
3. **Assessed sprite aesthetic** — both lines' battle sprites read as Gen 5-era pokeemerald-expansion modern style, which matches the project's `P_GBA_STYLE_SPECIES_GFX = FALSE` configuration. They will fit in.
4. **Assessed user's icon/overworld base intuitions:**
   - User suggested **Varoom** as base for Joustroll menu icon + overworld (because Joustroll has wheels)
   - User suggested **Escavalier** as base for Jousteel menu icon + overworld (because both are bipedal armored arthropod-knights)
   - **Both intuitions are sound.** Escavalier is the closer base. Varoom's silhouette is more vertical than Joustroll's horizontal-low-slung body, so Varoom is more "scaffolding/wheel-reference" than "color-swap candidate." Joustroll's menu icon and overworld follower will require **genuine pixel art work**, not just palette swaps.

### The three OPEN questions waiting on the user

The prior Claude posed these three questions and was awaiting user response when the context filled up:

**Q1: Joustroll front sprite — ship as-is or modify to 3/4 front-facing?**

The Joustroll reference sprite is in pure side-profile while the project's canonical sprites are 3/4 front-facing. Two options:
- **(a)** Ship side-profile as-is. Accept it'll be a stylistic outlier among the rest of the roster. Some ROM hacks accept this.
- **(b)** Modify to rotate toward 3/4 front-facing. Significant pixel art work — partial redraws of head/face, repositioned claws, re-pixeled wheel perspective. ~3-5 rounds of iteration likely.

**Q2: Are Varoom + Escavalier as bases locked, or open to alternatives?**

Escavalier seems definitively locked. Varoom is the right starting point but the silhouette mismatch with Joustroll means we may want to reference other wheeled or low-slung Pokemon icons too. User's call on flexibility.

**Q3: Scope confirmation — Phase 2a sprite-only this session, Phase 2b species-data integration in a separate session?**

Strongly recommended by the prior Claude. Visual deliverable can be verified cleanly before committing engineering work to a playable species.

---

## Critical bible facts to know about Joustroll/Jousteel before starting

From `bible/dreamstone_ruination_bible_v0.9.7.md` Section 9 "The Jousteel Line":

- **Cormorian-exclusive** — not wild, not held by other noble houses, not bred elsewhere. House Umbra cultivation is centuries-old family tradition.
- **Not a singular generational ace** — each Umbra raises their own Joustroll → Jousteel partnership. Cadmus's specific Jousteel is his lifelong partner from his Joustroll days.
- **Water/Steel typing locked**
- **Joustroll's evolution method** — `[OPEN]` (likely level-based 36-42)
- **Stats, abilities, learnsets** — all `[OPEN]` and will be designed in Phase 2b
- **Visual** (per bible, though bible's description of Joustroll as "crab-like quadruped" is contradicted by the user's reference sprites which show a clearly wheeled creature — the references override the bible text and we should treat the bible's description here as outdated):
  - **Joustroll:** low-slung wheeled body, red/striped carapace, crab-like front claws
  - **Jousteel:** bipedal armored knight stance, three lance-like crests on helmet, two clawed arms held in guard, blue-grey body under red crustacean carapace

The bible Section 14 also has an engineering entry (#28 in the v0.9.6 numbering, possibly renumbered in v0.9.7) for "Jousteel line full Pokemon data + sprite work" tagged `[MEDIUM]`. The sprite work is the Phase 2a deliverable.

---

## Recommended reading order on receipt

1. **This document (`SESSION_HANDOFF_PHASE2.md`)** — you've just read it
2. **`README_START_HERE.md`** — original project orientation
3. **`DREAMSTONE_HANDOFF.md`** — engineering doctrine, especially Sections 4 (verified patterns), 9 (adding new species), and 10 (sprite/palette lessons)
4. **`bible/dreamstone_ruination_bible_v0.9.7.md`** Sections 6 (starter lines), 7 (Cadmus Umbra), 9 (Jousteel Line subsection)
5. **`references/tinkatink_line_v3_final_reference.png`** — see the quality bar Phase 1 hit; Phase 2 should match
6. Extract `codebase/dsmyst_codebase_post_phase1.tar.gz` to a working directory
7. Extract `assets/Possible_Assets_For_Dreamstone_Ruination.zip` and find the four Joustroll/Jousteel reference sprites
8. Confirm git log shows the three Phase 1 commits: `cd dsmyst_bloodsnow && git log --oneline -5`

---

## Suggested first turn to the user

Once you've read everything, your first turn should be a brief orientation message confirming:
- You've absorbed Phase 1 status (three palette patches shipped)
- You have the v0.9.7 bible loaded
- You're ready to start Phase 2a (Joustroll/Jousteel sprite-only integration)
- You're awaiting their answers to the three questions above (Q1: Joustroll front-pose; Q2: base-flexibility; Q3: scope-split confirmation)

**Do not start sprite work until the user has answered.** The "measure twice, cut once" preference is strict on this.

---

## A note on tone

The user appreciates honest pushback when you disagree with them, but also takes correction well when *they* are wrong. Two examples from this session:

- I incorrectly told the user the canonical Tinkatink had no "cloth band on the hammer." The user's concept art included one. I was wrong but said so clearly and the user accepted the explanation about why I couldn't add it cleanly without per-pixel surgical PNG edits.
- I correctly pushed back when the user proposed renaming "Blue Moon Hermit" to "Blood Moon Hermit" — the Hermit name is load-bearing for the lunar motif. The user accepted the correction.

When honest pushback is warranted, deliver it. When honest correction comes back at you, accept it without performative apologizing. Direct engineering-style communication.

---

End of session handoff. Good luck with Phase 2.
