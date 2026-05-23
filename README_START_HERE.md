# Dreamstone Ruination — Master Handoff Package (v0.9.6)

**Date:** May 22, 2026
**Status:** Project state after Bloodsnow v10 Teddiursa line shipped
**Bible version:** v0.9.6

> This package contains the **complete state of the Dreamstone Ruination project** at the end of the v0.9.6 session. It's designed so you can either (a) start a fresh Claude session with full context, or (b) hand off to a different developer/AI tool and have them productive on their first message.

---

## What's In This Package

```
dreamstone_ruination_handoff_v096/
├── README_START_HERE.md                            ← This file. Read this first.
├── SESSION_HANDOFF.md                              ← Instructions for the NEXT Claude session
├── DREAMSTONE_HANDOFF.md                           ← Engineering patterns (updated v0.9.6)
├── dreamstone_ruination_bible_v0.9.6.md            ← Project source of truth (5700+ lines)
├── codebase/
│   └── dsmyst_bloodsnow_codebase.zip               ← Full dsmyst codebase with both patches applied (~120MB)
├── patches/
│   ├── 0001-Frigibax-line-custom-shiny-palettes-Dreamstone-Ruina.patch
│   ├── 0001-Blue-Moon-Teddiursa-line-v10-Bloodsnow-palette-Dream.patch
│   └── 0001-Pipeline-validation-v2-Galarian-Zigzagoon-shiny-pale.patch
└── references/
    ├── bloodsnow_v10_final_reference.png           ← v10 Teddiursa line final visual
    └── frigibax_line_shiny_final_review.png        ← Frigibax line final visual
```

---

## How to Use This Package

### Scenario A: Starting a Fresh Claude Session

1. Upload this entire handoff folder to the new Claude session (or extract the zip and upload pieces).
2. Tell Claude: **"Read SESSION_HANDOFF.md first, then the bible, then DREAMSTONE_HANDOFF.md. Once you've read all three, we'll start [Phase 1: Tinkatink line / Phase 2: Joustroll-Jousteel-Keerin / etc.]."**
3. Verify the new Claude can articulate:
   - What's locked vs open
   - The compile pipeline steps
   - The sprite production pattern
   - Your debugging protocol
4. Begin work.

### Scenario B: Resuming Work With Existing Claude

If you come back to the same Claude session later (within session memory), you don't need this whole package — just reference it as proof of state. The new session would need it.

### Scenario C: Handing to a Human Developer

The bible and DREAMSTONE_HANDOFF.md are the most important documents. They explain the project's design intent and the codebase's quirks. Send the human these plus the codebase zip and they can pick up.

---

## Project State Summary

### What's Been Built (Locked & Shipped)

✅ **Project bible v0.9.6** — ~5700 lines of locked design decisions covering:
- Cosmology (Phancero, Cormor Dream-Eater, Keerin, Treasures of Ruin)
- Cormorian Empire worldbuilding (military ranks, noble houses, geography, recent history)
- The three starter Pokemon lines (Frigibax, Teddiursa Blue Moon, Tinkatink) with stats, abilities, learnsets
- Mega Evolution policy
- Trial structure
- Story arcs (Glaive, Cadmus Umbra, Blue Moon Hermit, Vizier Umbra)

✅ **Frigibax line custom shiny palettes** (shipped patch) — Cormorian heraldic identity: charcoal + imperial gold + royal blue. Front + overworld palettes for Frigibax, Arctibax, Baxcalibur.

✅ **Blue Moon Teddiursa line v10 Bloodsnow palette** (shipped patch) — Snow-white + chocolate brown + blood red. Front + back + overworld for Teddiursa, Ursaring (male+female), Bloodmoon Ursaluna. All RGB values are GBA-safe multiples of 8.

✅ **Local compile pipeline** — Validated via successful compilation of 32MB BPEE01 ROM containing both shipped patches. No more GenSpark dependency.

### What's Next (Per Your Plan)

**Phase 1 — Tinkatink Line Palette** (next session, easiest)
- Same pipeline as Teddiursa. Needs your design direction on color theme.
- Bible currently has Tinkatink line as `[OPEN — awaiting user reference material]`.

**Phase 2 — Joustroll / Jousteel / Keerin Integration** (significant engineering work)
- Most sprite assets are in your asset library (`Possible_Assets_For_Dreamstone_Ruination.zip`).
- Need: menu icons for Joustroll + Jousteel, overworld sprites for all three.
- New species creation = species data, palettes, learnsets, INCBIN references, dex entries, cry sounds, evolution chains. Multi-file engineering work.

**Phase 3 — Trainers, NPCs, Buildings, Tilesets**
- Mostly modification of existing assets you provided.
- Sprite pipeline reuse from Phase 1 + 2 lessons.

**Phase 4 — Introductory Chapter Through First Trial**
- Maps (Porymap or programmatic), scripts (Poryscript), dialogue, trainer parties, wild encounters.
- The engineering-heavy phase.

---

## Critical Things The Next Claude Must Know

These are extracted from SESSION_HANDOFF.md but bear repeating here at the top level:

### 1. Read the handoff docs FIRST, not when stuck
The v0.9.6 session wasted significant effort because the previous Claude (me) didn't read DREAMSTONE_HANDOFF.md until very late in the session. It was in `/home/claude/` from the start. Don't repeat this mistake.

### 2. The compile pipeline runs locally now
No more GenSpark trips. Full instructions are in the bible Section 2 (Local compile pipeline subsection). Key gotcha: the bundled `tools/poryscript/poryscript` is a Mach-O macOS binary that doesn't run on Linux — must be rebuilt from source using Go.

### 3. The user's debugging protocol is strict
Read it in their `userPreferences`. Specifically: STOP, examine actual data, request specific data, analyze only what you've seen, propose ONE minimal fix. The user values precision and dislikes guessing.

### 4. Sprite work iterates many times
The Teddiursa line went through v1-v10 with many sub-versions. Expect 5-10+ iterations on visual details. Build extreme-zoom comparison sheets when the user reports a small issue you can't see at preview scale.

### 5. GBA color quantization is mandatory
All RGB values must be multiples of 8 before writing .pal files. Use `q8(rgb) = tuple((c // 8) * 8 for c in rgb)`. Color drift from non-quantized values will look wrong in-game.

### 6. The bible is canon, but it can be wrong
When the bible disagrees with shipped code, the code is right and the bible is stale. Update the bible. The hierarchy is: `user > DM Dex > handoff doc > source tree > engine docs > canon`.

---

## How to Build the ROM (Quick Reference)

If you're verifying the package or testing locally:

```bash
# 1. Extract the codebase
unzip codebase/dsmyst_bloodsnow_codebase.zip

# 2. Install toolchain (Ubuntu/Debian; root or sudo)
apt-get install -y binutils-arm-none-eabi gcc-arm-none-eabi libnewlib-arm-none-eabi \
                   build-essential libpng-dev pkg-config golang-go

# 3. Build poryscript (replace the bundled Mach-O binary)
cd /tmp && git clone --depth 1 https://github.com/huderlem/poryscript.git
cd /tmp/poryscript && go build -o poryscript .
cp /tmp/poryscript/poryscript <path>/dsmyst_bloodsnow/tools/poryscript/poryscript
chmod +x <path>/dsmyst_bloodsnow/tools/poryscript/poryscript

# 4. Build
cd <path>/dsmyst_bloodsnow
make tools                  # First-time only — builds bundled C/C++ tools
make -j$(nproc) modern      # Full build, ~4 minutes single-core

# 5. Result: pokeemerald.gba (32MB BPEE01)
file pokeemerald.gba
```

---

## How to Apply Patches (If Starting From Vanilla dsmyst)

If you have a fresh dsmyst clone and want to apply the Dreamstone Ruination patches:

```bash
cd <vanilla_dsmyst_clone>
git apply <handoff>/patches/0001-Frigibax-line-custom-shiny-palettes-Dreamstone-Ruina.patch
git apply <handoff>/patches/0001-Blue-Moon-Teddiursa-line-v10-Bloodsnow-palette-Dream.patch

# Optional: ignore the third patch (Galarian Zigzagoon validation) unless you want it.
```

The codebase zip already has both patches applied, so you don't need this step if you're using that zip directly.

---

## Visual References

In the `references/` folder:
- **`bloodsnow_v10_final_reference.png`** — Complete v10 Teddiursa line: Teddiursa, Ursaring (male shown), Bloodmoon Ursaluna with front + back + overworld sprites
- **`frigibax_line_shiny_final_review.png`** — Frigibax line shipped shiny palettes for reference

---

## Last Note From The v0.9.6 Session's Claude

This project is genuinely worth building. The cosmology is layered, the worldbuilding is detailed, and the gameplay design has clear vision. The user is a thoughtful, deliberate developer who's been generous with both context and patience.

The biggest insight from v0.9.6 was that I'd been treating sprite work as design-only when the user expected integration into the codebase as we went. The next session should integrate continuously — patch-test-iterate-patch — not "design 10 iterations then integrate at the end."

Good luck. Build something great.

— Claude (v0.9.6 session)
