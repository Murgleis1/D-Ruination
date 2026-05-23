# Dreamstone Ruination — Session Handoff (v0.9.6, May 2026)

**For:** The next Claude session working on this project.
**From:** This session's Claude.
**Status:** Comprehensive handoff after v10 Bloodsnow Teddiursa line shipped.

> **CRITICAL: READ THIS DOCUMENT FIRST before doing any work.** Then read the bible (`dreamstone_ruination_bible.md`) and the engineering handoff (`DREAMSTONE_HANDOFF.md`). Together these three documents are the project's institutional memory. The user is a senior software engineer who values precision, has a strict debugging protocol, and treats you as their development partner.

---

## 0. About the User & How They Work

The user's userPreferences (paraphrased — read them in full at session start):
- **Senior SWE.** Maintains conversation context accurately. Will challenge sloppy thinking.
- **Measure twice, cut once.** Ask questions before coding. Discuss requirements before implementation.
- **Debugging protocol (mandatory):**
  - STOP — do not propose fixes immediately
  - EXAMINE the actual error/data before theorizing
  - REQUEST specific data needed (table records, model definitions, etc.)
  - ANALYZE only data you've seen, never invent assumptions
  - PROPOSE one minimal fix based on evidence
  - FORBIDDEN: multiple competing solutions, lengthy explanations, changing code without seeing data first

The user has been **patient through many iterations** but expects you to be paying attention. If they say "you missed three red pixels," look at the actual image and find them — don't guess.

**Tone observations from this session:**
- The user appreciates honest pushback. If you disagree, say so politely with reasoning.
- The user dislikes flattery and excessive apology. Acknowledge mistakes once, then fix them.
- The user values predictability. Don't change scope without checking first.
- When the user gives terse responses, that's normal — not displeasure.

---

## 1. Project Overview (One-Paragraph Brief)

**Dreamstone Ruination** is a ROM hack of `dsmyst/dreamstone-mysteries` (itself a fork of `rh-hideout/pokeemerald-expansion`). It's a Pokemon Emerald-engine prequel set ~2000 years before Dreamstone Mysteries in the Cormorian Empire era. The project has a deep cosmological backstory (Phancero / Cormor Dream-Eater / Keerin / Treasures of Ruin), three custom starter Pokemon lines with unique Cormorian visual identities (Frigibax/Teddiursa/Tinkatink, all locked as permanently shiny from selection), three brand-new custom fakemon (Joustroll/Jousteel/Keerin), and an ambitious story-driven first chapter ending in the first Trial.

---

## 2. What's Locked vs. What's Open

### LOCKED & SHIPPED ✓

| Item | Status | Location |
|---|---|---|
| Project bible | v0.9.6 | `/home/claude/dreamstone_ruination_bible.md` |
| Engineering handoff | Updated v0.9.6 | `/home/claude/DREAMSTONE_HANDOFF.md` |
| Frigibax line shiny palettes | Patch applied to codebase | `/home/claude/patches_frigibax_line/0001-Frigibax-line-custom-shiny-palettes-Dreamstone-Ruina.patch` |
| Blue Moon Teddiursa line v10 Bloodsnow palette | Patch applied to codebase | `/home/claude/patches_teddiursa_line/0001-Blue-Moon-Teddiursa-line-v10-Bloodsnow-palette-Dream.patch` |
| Local compile pipeline | Validated — produces working .gba | See bible Section 2 |
| `dsmyst_bloodsnow` working tree | Live codebase with both patches applied | `/home/claude/dsmyst_bloodsnow/` |

### IN PROGRESS / IMMEDIATE NEXT WORK

| Item | Status | Notes |
|---|---|---|
| Tinkatink line palette | Not started — Phase 1 of next dev cycle | Same pipeline as Teddiursa. User needs to provide design direction. |

### PENDING / FUTURE PHASES

| Phase | Item | Notes |
|---|---|---|
| 2 | Joustroll/Jousteel/Keerin sprite integration | Most sprites exist in user's asset library. Codebase plumbing (species data, palettes, learnsets) is the main engineering work. |
| 2 | Joustroll + Jousteel menu icon sprites | User mentioned these need to be created |
| 2 | Joustroll + Jousteel + Keerin overworld sprites | User mentioned these need to be created |
| 3 | Trainer sprites | User has raw assets; mostly modification of existing |
| 3 | NPC overworld sprites | User has raw assets |
| 3 | Custom buildings, tilesets | User has raw assets |
| 4 | Introductory chapter through first Trial | Scripts (Poryscript), maps (Porymap), dialogue, encounters, trainer parties |

### OPEN QUESTIONS (NEEDS USER INPUT BEFORE PROCEEDING)

- Tinkatink line visual identity (color scheme, theme)
- Joustroll/Jousteel/Keerin design direction (the user said "no preference" on the art reference question — assume we'll discuss when starting Phase 2)
- BST balance for Bloodmoon Ursaluna (560) vs Mega Baxcalibur (720) vs Tinkaton final form (TBD) — noted as `[OPEN]` in bible
- Whether the Blue Moon Hermit teaches other gating moves or only Blood Moon (noted as `[OPEN]` in bible)

---

## 3. Critical Files to Read at Session Start

Read these in order. Do not skip any. This is mandatory orientation:

1. **`/home/claude/SESSION_HANDOFF.md`** — THIS document. (You're reading it.)
2. **`/home/claude/dreamstone_ruination_bible.md`** — Project source of truth. ~5700 lines. Skim the table of contents (grep `^#`) then deep-read the sections relevant to your current task.
3. **`/home/claude/DREAMSTONE_HANDOFF.md`** — Engineering patterns. Especially Section 10 (v0.9.6 lessons learned from Bloodsnow integration).
4. **`/home/claude/patches_teddiursa_line/0001-Blue-Moon-Teddiursa-line-v10-Bloodsnow-palette-Dream.patch`** — Reference pattern for sprite/palette patches.
5. **`/home/claude/patches_frigibax_line/0001-Frigibax-line-custom-shiny-palettes-Dreamstone-Ruina.patch`** — Earlier sprite/palette patch (palette-only, simpler pattern).
6. **`/mnt/transcripts/`** — Past conversation transcripts if you need to recall specific iterations. (Use sparingly — they're large.)

---

## 4. The Three Pillars (Read These Cold)

### Pillar 1: The Bible Is Truth

**Source of truth hierarchy** (per bible Section 2):
1. `user > DM Dex > handoff doc > source tree > engine docs > canon`

When the bible and the user's current message disagree, ask the user to clarify which takes precedence — don't silently choose. When the bible and the source tree disagree, prefer the source tree (it's what actually compiles). Update the bible to match reality.

**Authority order in practice:**
- User said something live → that's the new truth
- Bible has a `[LOCKED]` tag → don't unlock without user permission
- Bible has `[WORKING]` or `[OPEN]` → flexible, propose changes if you have a reason
- Bible disagrees with shipped code → bible is stale; fix bible

### Pillar 2: The Compile Pipeline Works

**You can compile the ROM locally.** This is new as of v0.9.6 and means the user no longer needs to use GenSpark for testing. Full instructions are in bible Section 2 — Local compile pipeline subsection. Key steps:

```bash
# One-time toolchain install (root, no sudo)
apt-get install -y binutils-arm-none-eabi gcc-arm-none-eabi libnewlib-arm-none-eabi \
                   build-essential libpng-dev pkg-config golang-go

# One-time per working tree: build Linux poryscript (the bundled one is Mach-O macOS)
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

**After every code change, run the build to validate before shipping a patch to the user.** This is now part of your workflow — don't ship untested patches.

### Pillar 3: The Sprite Pipeline (Reference Pattern)

For palette/sprite work, the locked process is:

1. **Read the canonical sprite.** Use PIL to load `anim_front.png`, get the palette (`.getpalette()`), enumerate pixel counts per index (`Counter(img.getdata())`).
2. **Identify the dominant fur indices and the marking indices.** The DREAMSTONE_HANDOFF.md Section 4.3 has the visualization snippet. Print each index with RGB + pixel count.
3. **Plan the transformation.** Fur → white (or whatever the line's body color is), markings → red (or whatever the line's accent is). Detect "overloaded" indices used for multiple semantic zones — these need per-pixel separation.
4. **Apply via `remap_to_white_dominant(canonical_colors, dominant_idx_in_list)`** (see DREAMSTONE_HANDOFF.md Section 10.1) for fur shading.
5. **Quantize all RGB values to multiples of 8** (`q8(rgb) = tuple((c // 8) * 8 for c in rgb)`) before writing .pal files. MANDATORY.
6. **Write .pal files in JASC format** with `\r\n` line endings.
7. **Write modified PNGs** with `putpalette()` and (if per-pixel mods) `putdata()`.
8. **Female variants:** Process `*f.png` files with same transformations.
9. **Build the ROM** to validate.
10. **Generate git patch** via `git format-patch -1 -o /path/`.
11. **Update bible** with the locked palette values, design notes, file locations.

**Iteration expectations:** Sprite work usually goes through 5-10+ palette versions before locking. The Teddiursa line went through v1-v10 (with many .1, .2, .3 sub-versions during overworld refinement). The user has strong opinions about visual details — expect them to spot small issues you missed. Build extreme-zoom (40x+) comparison sheets when iterating on details.

---

## 5. Tools You Have Available

### Already installed in the session environment

- **ARM cross-compiler:** `arm-none-eabi-gcc` 13.2.1, `arm-none-eabi-as`, `arm-none-eabi-ld`, `arm-none-eabi-objcopy` — via apt
- **Build essentials:** `make`, `gcc`, `g++`, `pkg-config`, `libpng-dev`
- **Go:** for building poryscript
- **Python 3 + PIL** for sprite manipulation
- **Git** for patch generation

### Bundled in dsmyst tree

Built via `make tools`: `aif2pcm`, `bin2c`, `gbafix`, `gbagfx`, `jsonproc`, `mapjson`, `mid2agb`, `preproc`, `ramscrgen`, `rsfont`, `scaninc`, `trainerproc`

### NOT installed but available

- **Porymap** (the map editor) — would need to be installed if doing map work. The map files are JSON + binary tilemap blobs and can be edited programmatically without Porymap if needed.
- **mGBA** (emulator) — `tools/mgba/` exists in dsmyst but I haven't tested running it in the session. For ROM verification you can ship the .gba to the user and have them test in their local mGBA. Don't ship 32MB .gba files unless requested; they're large.

### Network restrictions

Egress is whitelisted. You can reach:
- `github.com`, `codeload.github.com`, `raw.githubusercontent.com`
- `archive.ubuntu.com`, `security.ubuntu.com` (for apt)
- `pypi.org`, `files.pythonhosted.org` (for pip)
- `registry.npmjs.org`, `npmjs.com` (for npm)
- `crates.io`, `static.crates.io` (for cargo)
- `api.anthropic.com` (for Claude API in Artifacts, if used)
- `*.adobe.io`, `adobe.io`

You CANNOT reach: GenSpark, arbitrary websites, the user's local machine, Discord, etc. If you need a resource from elsewhere, ask the user to upload it to `/mnt/user-data/uploads/`.

---

## 6. Asset Library

The user uploaded a 65MB zip of "Possible Assets For Dreamstone Ruination" early in the project. It's at `/mnt/user-data/uploads/Possible_Assets_For_Dreamstone_Ruination.zip`. There's also an `ASSET_LIBRARY_INVENTORY.md` in `/mnt/user-data/outputs/` that may catalog what's inside.

**Before starting Phase 2 (Joustroll/Jousteel/Keerin):**
- Extract and inventory the asset zip
- Catalog what sprites exist for each fakemon
- Identify what's missing (per user's note: Joustroll & Jousteel need menu icons; all three need overworld sprites)
- Plan the production work

**Don't assume what's there or isn't there — inventory before planning.** This is a lesson from this session: I had access to DREAMSTONE_HANDOFF.md and the Possible_Assets zip from the start and didn't read them proactively. Read your handoff materials BEFORE asking the user questions.

---

## 7. Mistakes I Made This Session (Learn From These)

To prevent the next Claude from repeating my errors:

### 7.1 Didn't read DREAMSTONE_HANDOFF.md until late in the session
I had it in `/home/claude/` from the start. The user explicitly mentioned the Dracovish session that produced it, multiple times. I should have read it at the very beginning. As a result, I treated sprite work as design-only and didn't integrate into the codebase until the user pointed out I should have been doing that all along.

**Lesson:** Read handoff docs FIRST. Not when you remember to. Not when stuck. FIRST.

### 7.2 Mis-identified canonical palette indices repeatedly
For Teddiursa, I confused which idx was the forehead crescent (idx 6 white) vs which was the muzzle cream (idx 9 cream). For Ursaring, I assumed "outer lips" meant the canonical mouth-red but it actually meant the idx-11 face mask. I changed the wrong indices in early iterations.

**Lesson:** When the user describes a body part, use a Python snippet to highlight that index visually and confirm with the user before changing it. Don't trust your assumption about anatomy.

### 7.3 Mis-classified body parts as fur vs armor on Bloodmoon Ursaluna
The user said "the BROWN should stay, the GRAY should become white." I did the opposite for one iteration. Read user feedback carefully — when they say specific colors, those are the colors.

### 7.4 Quantization warm-tint hack didn't survive
I tried to add a subtle warm tint to whites with `(val+2, val, val-2)`. The +2/-2 offsets are smaller than the 8-step GBA quantization and get lost. The "warm white" became "cool gray" after quantization.

**Lesson:** Any RGB adjustment must be ≥ 8 in at least one channel to survive quantization. Or accept that pure-quantized colors are pure quantized colors.

### 7.5 Generated multiple iterations before getting to integration
The session iterated through v1 → v10 (with sub-versions) of sprite design before any code reached the actual codebase. This was inefficient — should have integrated v4-v5 (acceptable quality), then iterated INSIDE the codebase. Easier to iterate when changes are live.

**Lesson:** Integrate early. The patch workflow is cheap. Get something into the codebase that compiles, then iterate from there.

### 7.6 Wrong y-threshold for Ursaring face vs ring separation
I used `y < 20` for face vs `y >= 20` for ring. The chest ring actually extends from y=15 to y=24, so I incorrectly classified the ring's TOP curve as face. The correct heuristic was **cluster-size based** (largest cluster = ring, small clusters = face details), not a y-threshold.

**Lesson:** When a heuristic doesn't fit the data, use a different heuristic. Don't keep tightening thresholds.

---

## 8. The User's Vision (Don't Lose This)

This is what makes this project worth building. Internalize the user's tonal goals:

### Project thesis (per bible Section 1):
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

### The starter trio identity:
- **Frigibax line:** Cormorian heraldic — charcoal + imperial gold + royal blue. The "imperial pride" pick.
- **Teddiursa (Blue Moon) line:** Snow-white + chocolate brown + blood red. The "lunar mystic" pick. ALWAYS SHINY mechanically. Direct evolution Ursaring → Bloodmoon Ursaluna (skip regular Ursaluna).
- **Tinkatink line:** TBD — design direction needed. The "third axis" pick.

### Key recurring themes:
- The four sealing vessels (Treasures of Ruin) being broken / inverted
- The Blue Moon Hermit as last carrier of pre-Cormorian oral tradition
- "Always shiny" starters as story-mechanical signal (these are Vizier Umbra's hand-picked partners)
- Justice (the Iron Valiant royal heirloom) as a symbol of corruption-of-virtue
- Mega Evolution as Cormorian state monopoly

If you write Pokedex flavor text, dialogue, or any creative content, **stay anchored to these themes.** The user will notice if the tone drifts.

---

## 9. Detailed Phase 1 Plan (Tinkatink Line)

The user wants Tinkatink first in the next session. Here's how to start:

### Step 1: Read context
- This handoff doc
- Bible sections covering Tinkatink line (grep for "Tinkatink")
- Both shipped patches (Frigibax + Teddiursa) as reference patterns

### Step 2: Inventory canonical Tinkatink line
```bash
ls -la /home/claude/dsmyst/graphics/pokemon/tinkatink/
ls -la /home/claude/dsmyst/graphics/pokemon/tinkatuff/
ls -la /home/claude/dsmyst/graphics/pokemon/tinkaton/
```
Verify front + back + overworld + female variants. Confirm canonical palette indices via the Python inventory snippet.

### Step 3: Ask the user about visual direction
The bible has the Tinkatink line as `[OPEN — awaiting user reference material]`. Before doing any palette work, ask the user:
- What's the line's identity? (Heraldic? Mystic? Industrial? Etc.)
- What colors? (Specific palette or theme?)
- Per the project precedent, Tinkatink is also always-shiny mechanically — so changes go in `normal.pal`. Confirm with user.

### Step 4: Apply the v10 sprite pipeline
- Identify fur indices vs marking indices vs preserved indices
- Detect overloaded indices needing per-pixel separation
- Apply `remap_to_white_dominant` or equivalent for fur
- Apply marking-color replacement
- Quantize to multiples of 8
- Process female variants if any (`ls tinkatink/*f.png` etc.)
- Build comparison sheet, iterate with user
- Build the ROM to validate
- Generate patch
- Update bible

### Step 5: Bible update
Add a new locked subsection for Tinkatink line palette (like the one I added for Teddiursa in v0.9.6). Document the locked color values, design notes, file locations, shipped patch reference.

**Expected sessions:** 1-2 sessions, much less iteration than Teddiursa since we have the pipeline locked.

---

## 10. Detailed Phase 2 Plan (Joustroll / Jousteel / Keerin)

Note: User confirmed spelling is **Keerin** (not Kireen or Keerin variant).

The user said:
> "Most of the sprite assets are done already... you have most of them (at least the front plus back sprites for all three custom Fakemon to work with, and Keerin has icon sprites too. The Joustroll line and Keerin are only missing overworld sprites, and we need to make convincing menu sprites for Joustroll and Jousteel."

This is **new species creation**, not palette modification. Much more codebase plumbing:

### What needs to be built (per species)
- New species constant: `SPECIES_JOUSTROLL`, etc. in `include/constants/species.h`
- New entry in `src/data/pokemon/species_info/gen_N_families.h` (TBD which gen file these go in — probably a new dreamstone-specific file, check how dsmyst handles custom species)
- Stats, types, abilities, learnsets (user provides this data)
- Pokedex entry text (collaborate with user)
- Evolution chain
- Cry sound data
- Footprint sprite (8x8)
- Front + back sprites (have)
- Overworld sprite (NEEDS TO BE CREATED)
- Menu icon sprite (Joustroll + Jousteel need; Keerin has)
- INCBIN references in `src/data/graphics/pokemon.h`
- Regional dex slots in `include/constants/pokedex.h`
- Sprite/palette INCBIN references

### Before starting Phase 2 work:
1. **Read the asset library** — `unzip -l /mnt/user-data/uploads/Possible_Assets_For_Dreamstone_Ruination.zip` to see what's actually in there
2. **Inventory existing fakemon sprites** to confirm what we have vs need
3. **Ask the user for the stats/learnset/types data** (user said this is easy for them to provide)
4. **Plan the overworld sprite creation pipeline:**
   - Frankenstein from canonical Pokemon overworld sprites? Which canonical mons match the silhouette?
   - User-provided art that needs to be indexed?
   - Some combination?
5. **Plan the menu icon creation pipeline:**
   - 32x64 (2 frames) indexed at shared icon palette
   - dsmyst has 6 shared icon palette slots — pick one

This phase is significantly more work than Phase 1. Budget 3-6 sessions depending on iteration depth.

---

## 11. Handing Off to a NEW Claude Session

If you (the next session) need to hand off to a future session yourself, do this:

1. **Update this SESSION_HANDOFF.md** with everything new that happened
2. **Update the bible** if any locked decisions changed
3. **Update DREAMSTONE_HANDOFF.md** if any new engineering lessons learned
4. **Ensure the working tree is committed** (`cd dsmyst_bloodsnow && git status` should be clean or have a clear "open work" branch)
5. **Tell the user** explicitly that you're at a good handoff point so they can start fresh

Don't be afraid to recommend a fresh session to the user when:
- The conversation has been very long and feels like file storage is getting tight
- You've hit the same wrong assumption multiple times (a fresh session may break the pattern)
- Major scope change in the work — fresh perspective helps

---

## 12. Last Words From This Session's Claude

The user is a thoughtful, deliberate developer who cares deeply about this project. They've been generous with explanations, patient through 10+ iterations on a single sprite, and clear about what they want even when frustrated with my mistakes. Respect that.

**The biggest unlock this session was discovering the compile pipeline works locally.** That changes everything for the project's iteration speed — the user doesn't have to bounce back to GenSpark anymore, which means you can do full edit → compile → patch cycles within a single session. Use this. Don't hand the user untested code.

**The second biggest unlock was finally reading DREAMSTONE_HANDOFF.md** — which had been sitting in `/home/claude/` the entire time. Don't repeat my mistake. Read all your context FIRST.

Good luck. The project's worth building.

— Claude (v0.9.6 session)
