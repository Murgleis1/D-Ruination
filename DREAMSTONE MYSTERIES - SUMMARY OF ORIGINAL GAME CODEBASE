# Dreamstone Mysteries — Codebase Modification Handoff

This document is a handoff from a prior Claude session that successfully made
~15 changes to the Pokemon Dreamstone Mysteries ROM hack source and produced a
working compiled `.gba`. The goal of this document is to give the next Claude
working on the codebase the patterns, file locations, and gotchas needed to
make further changes correctly on the first try.

---

## 1. What the codebase is

Dreamstone Mysteries is a **fork of pokeemerald-expansion** (rh-hideout) with
custom content (region called Cormoria, custom Pokémon roster, custom maps,
custom story). It builds with the standard pokeemerald-expansion toolchain
(`make` or `make modern`).

If you've worked on pokeemerald or pokeemerald-expansion before, all of those
patterns apply here. The fork-specific things are described below.

---

## 2. High-level file layout that matters

```
graphics/pokemon/<species>/      Sprites + palettes for each species
src/data/pokemon/species_info/   Per-species data (stats, abilities, evos)
  gen_1_families.h through gen_9_families.h
src/data/moves_info.h            All move data (power, PP, type, category, …)
src/data/pokemon/pokedex_orders.h Pokédex sort orders (alphabetical, etc.)
include/constants/pokedex.h      HOENN_DEX_* enum + NATIONAL_DEX_* enum
include/constants/items.h        ITEM_* constants (verify before use!)
include/constants/abilities.h    ABILITY_* constants
src/pokemon.c                    HOENN_TO_NATIONAL() initializer for regional dex
src/player_pc.c                  PC starting items (NewGameInitPCItems)
data/maps/<MapName>/             Per-map scripts, events, JSON
  scripts.pory                   Poryscript SOURCE
  scripts.inc                    Compiled assembly (auto-generated from .pory)
  events.inc                     Object events / coord triggers
  map.json                       Map metadata + objects
```

---

## 3. Universal rule: read before you edit

Before changing **anything**, run:

```bash
grep -rn "<exact identifier you're targeting>" src/ include/ data/
```

The reason: in pokeemerald-expansion, the same data shows up in multiple files
(an enum + an initializer + sometimes a JSON), and you need to update *all of
them* for a change to take effect. If you only edit one place, the build may
succeed but the change won't appear in-game (or worse, will misbehave).

**Always confirm a constant exists before referencing it.** E.g. don't assume
`ITEM_RARE_SHARD` is in stock pokeemerald — verify with grep:
```bash
grep "ITEM_RARE_SHARD" include/constants/items.h
```
This fork has custom items. Same for abilities and species.

---

## 4. Verified patterns by change type

### 4.1 Editing Pokémon stats / abilities / evolutions

**Location:** `src/data/pokemon/species_info/gen_N_families.h` where N is the
generation that introduced the species' family.

**To find a species fast:**
```bash
grep -rn "SPECIES_<NAME>\b\] =" src/data/pokemon/species_info/
```

Stats are simple struct fields:
```c
.baseHP = 100, .baseAttack = 120, .baseDefense = 65, ...
```

**Abilities** are a 3-slot array `{ ability1, ability2, hidden }`. To force a
single ability, fill all three slots with the same value:
```c
.abilities = { ABILITY_DEFIANT, ABILITY_DEFIANT, ABILITY_DEFIANT },
```

**Evolutions** use the `EVOLUTION(...)` macro. Common forms:
```c
.evolutions = EVOLUTION({EVO_LEVEL, 28, SPECIES_SCOVILLAIN}),
.evolutions = EVOLUTION({EVO_ITEM, ITEM_FIRE_STONE, SPECIES_SCOVILLAIN}),
.evolutions = EVOLUTION({EVO_FRIENDSHIP, 0, SPECIES_UMBREON}),
```

When swapping evolution methods, remove the old condition entirely and write
the new one — don't try to add a second condition unless that's intentional.

### 4.2 Editing moves

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
When the user asks for a specific power value, **replace the entire ternary
with the literal value**. Leaving the ternary in place means the value depends
on a config flag and you may not get the value the user wanted.

### 4.3 Sprite + palette work (battle sprites)

For each species there's a `graphics/pokemon/<species>/` directory containing:

| File | Purpose |
|---|---|
| `front.png` | Front battle sprite (indexed, 4bpp source) |
| `back.png` | Back battle sprite (indexed) |
| `normal.pal` | JASC-format palette for normal coloring |
| `shiny.pal` | JASC-format palette for shiny coloring |
| `icon.png` | Menu icon (32x64 = 2 frames) |
| `overworld.png` | Overworld follower sprite |
| `overworld_normal.pal` | Follower normal palette |
| `overworld_shiny.pal` | Follower shiny palette |
| `footprint.png` | Tiny footprint |
| `*.4bpp`, `*.4bpp.lz`, `*.gbapal`, `*.gbapal.lz` | **Compiled outputs — do not edit by hand** |

**The model:** the 4bpp sprite data references colors by *palette index*, not
by RGB. At runtime, the engine loads either `normal.gbapal` or `shiny.gbapal`
and that determines what each index renders as. So shiny coloring is a pure
palette swap — same pixel data, different colors.

**To fix a broken shiny palette:**

1. Look at the `front.png` palette indices and figure out which index
   represents which body part. Easiest way: write a small Python script that
   isolates each index and shows it as a colored region on the sprite. Example:

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

2. Determine what color each palette index should be in the shiny form
   (based on the user's reference image / official shiny art).

3. Write a new `shiny.pal` in JASC format:
   ```
   JASC-PAL
   0100
   16
   <R> <G> <B>           ← 16 lines, one per palette slot, space-separated
   ...
   ```
   Index 0 is typically the transparent/background color and is conventionally
   `152 208 160` (the standard pokeemerald sprite background green).

4. **Preview before committing.** Apply the new palette to the indexed PNG in
   software and visually confirm it matches the reference. Don't ship a
   palette you haven't visually verified.

5. **Delete the stale compiled artifacts** so the build regenerates them:
   ```bash
   rm graphics/pokemon/<species>/shiny.gbapal \
      graphics/pokemon/<species>/shiny.gbapal.lz \
      graphics/pokemon/<species>/overworld_shiny.gbapal \
      graphics/pokemon/<species>/overworld_shiny.gbapal.lz
   ```
   The make rule `%.gbapal: %.pal` should rebuild them, but stale binaries can
   confuse incremental builds. Removing them is cheap insurance.

**Quirk that tripped me up:** in some species (Dracovish was one),
`back.png`'s embedded PNG palette differs from `front.png`'s. The embedded
palettes only affect the PNG→4bpp conversion at build time — at runtime the
game uses `normal.gbapal`/`shiny.gbapal` for *both* sprites. So:
- If you open back.png in an image viewer, it may look "wrong" — that's
  pre-existing repo behavior, not a real bug.
- What matters is that for a given logical palette index, the front and back
  sprites use that index for the same body part (e.g. "main body color"). If
  the original artist set this up correctly, your shiny palette swap works
  uniformly across both sprites. If they didn't, you have a deeper sprite
  problem that requires re-indexing one of the PNGs.

**Menu icons have no shiny variant in this codebase.** The species struct has
`iconPalIndex` (one of 6 shared icon palettes) but no `iconShinyPalIndex`. So
the menu icon will look the same whether the Pokemon is shiny or not. If a
user reports "the menu icon looks wrong on my shiny", that's an engine
limitation, not a per-species fix.

### 4.4 Overworld follower palettes

Same pattern as battle sprites but a different palette file pair
(`overworld_normal.pal` + `overworld_shiny.pal`). The overworld sprite uses
its own 16-color palette — usually with **different index meanings** than the
battle sprite. Don't reuse the battle shiny palette directly; analyze the
overworld PNG's indices separately.

### 4.5 Editing in-game scripts (dialogue, wild encounters, eggs, etc.)

Every map under `data/maps/<MapName>/` has:
- **`scripts.pory`** — Poryscript source. This is what you should think of as
  "the source of truth."
- **`scripts.inc`** — The compiled assembly output, generated from `.pory` by
  the poryscript tool during build.

**Big gotcha:** depending on how the user builds the project, the `.inc` may
or may not be regenerated automatically. **To be safe, edit BOTH the `.pory`
and the `.inc`.** This is what I did and it worked under GenSpark's build.

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
- Preserve `\n` (line break), `\l` (line break, no scroll), `\p` (page break),
  and the trailing `$` (end of string marker)

**Don't rename internal script labels or flag names** (`FLAG_*`, `LOCALID_*`,
script function names like `Route4_Dewpider_Trigger`) when changing what they
*do*. These are just identifiers; the user never sees them. Renaming them
forces you to find every reference across `.pory`/`.inc`/`events.inc`/`map.json`
and update them all — high risk for cosmetic gain.

**Overworld sprites for Pokemon NPCs** use the `OBJ_EVENT_GFX_SPECIES(NAME)`
macro. Change in three places:
- `data/maps/<MapName>/events.inc` (the `object_event` line)
- `data/maps/<MapName>/map.json` (the `graphics_id` field)
- (If referenced in `scripts.pory`, that too, but rare)

### 4.6 PC starting items

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

**Important:** this affects **new games only**. Existing save files don't
retroactively gain items — that's a save-state limitation, not something code
can fix.

### 4.7 Adding Pokemon to the regional Pokédex

This fork uses Hoenn dex numbering for the in-game regional dex. To add a
species:

**Step 1.** Add an enum entry in `include/constants/pokedex.h`. The enum is
called by `HOENN_DEX_<NAME>` and the auto-incrementing values are sensitive —
**inserting in the middle shifts the values of all subsequent entries**.
That's safe as long as no other code stores Hoenn dex numbers persistently
(seen/caught flags are stored by *National* dex number, so they're unaffected).

```c
HOENN_DEX_AERODACTYL,
HOENN_DEX_CAPSAKID,     // ← new
HOENN_DEX_SCOVILLAIN,   // ← new
HOENN_DEX_SCREAM_TAIL,
```

**Step 2.** Add the matching `HOENN_TO_NATIONAL(NAME)` line in
`src/pokemon.c` so the regional→national mapping table is initialized:

```c
HOENN_TO_NATIONAL(AERODACTYL),
HOENN_TO_NATIONAL(CAPSAKID),     // ← new
HOENN_TO_NATIONAL(SCOVILLAIN),   // ← new
HOENN_TO_NATIONAL(SCREAM_TAIL),
```

**Step 3.** Verify the species already has `.natDexNum = NATIONAL_DEX_<NAME>`
in its species_info entry. (Usually it does — it's set automatically when the
species is defined in a `gen_N_families.h` file.)

**Step 4.** The sort orders in `src/data/pokemon/pokedex_orders.h` (alphabetical
etc.) usually already include every species in the build — check, but typically
no edit needed.

---

## 5. Things that look like they should work but don't

- **Don't edit the `*.4bpp` / `*.4bpp.lz` / `*.gbapal` / `*.gbapal.lz` files
  directly.** They're compiled binary outputs from the PNG/PAL sources. Edit
  the source, delete the binary, rebuild.

- **Don't assume vanilla pokeemerald item/ability/species names exist.** This
  fork has additions and may have removed/renamed things. Always grep first.

- **Don't try to give the menu icon a per-species shiny variant** — the
  engine field doesn't exist (`iconPalIndex` exists, `iconShinyPalIndex`
  doesn't). Adding it is a non-trivial engine modification.

- **Don't rename `FLAG_*`, `LOCALID_*`, or script label identifiers** just
  because the user-facing content changed. The identifiers are internal;
  cascading renames break things and gain nothing.

- **Don't only edit `.pory` and assume the build will regenerate `.inc`.**
  Edit both. Cheap insurance, no downside.

---

## 6. Build and verify

- The project builds with `make` (legacy) or `make modern` (recommended).
- The `build/` directory holds .o files and can be deleted any time —
  `make clean` does this. When shipping a zip of the source for someone else
  to build, **exclude `build/`** to save space and avoid stale-cache issues.
- After making changes, the user typically tests on mGBA. If you can't run a
  build yourself, do a final grep pass to confirm every change landed in
  every file it needed to.

---

## 7. Working style that produced clean results

The user's stated preference is "measure twice, cut once" — confirm before
coding. In practice for this project that means:

1. When the user asks for a change, first grep to **locate every file the
   change touches**. Pokemon ROM hacks repeatedly have data in multiple
   places (species_info + pokedex enum + pokedex mapping; .pory + .inc; etc.).
2. For sprite/palette work, **preview visually before committing.**
3. For data files, **verify constants exist** before referencing them.
4. **Edit both .pory and .inc** for map scripts.
5. **Checkpoint progress** when a task list is large rather than pushing
   through and hoping nothing breaks. Tell the user what's done and what's
   still pending.
6. Flag tradeoffs honestly. Examples from the prior session:
   - "Top of head will be magenta because palette index is shared with body
     trim" — couldn't be cleanly separated without redrawing the sprite.
   - "PC items only apply to new games" — save-state limitation.
   - "Hoenn dex enum shift is safe because seen/caught are stored by national
     dex" — explained why the change wouldn't corrupt saves.

---

## 8. Quick reference — concrete examples from the prior session

These all worked end-to-end (game compiled, ran in mGBA, behaved correctly):

- **Stat buff:** Skarmory → `gen_2_families.h`, change `.baseAttack`/`.baseSpeed`.
- **Ability change:** Skarmory → `.abilities = { ABILITY_DEFIANT, ABILITY_DEFIANT, ABILITY_DEFIANT }`.
- **Move category swap:** Tachyon Cutter → `moves_info.h`, change `.category` from `DAMAGE_CATEGORY_SPECIAL` to `DAMAGE_CATEGORY_PHYSICAL`.
- **Move type swap:** Twineedle Bug→Dark → change `.type = TYPE_DARK`.
- **Evolution method swap:** Capsakid stone→level → `.evolutions = EVOLUTION({EVO_LEVEL, 28, SPECIES_SCOVILLAIN}),`.
- **Wild encounter swap:** Route 4 NPC battle Dewpider→Capsakid level 12 → both `.pory` and `.inc` in `data/maps/Route4/`, plus overworld sprite in `events.inc` and `map.json`.
- **Egg given by NPC:** `giveegg(SPECIES_HONEDGE)` → `giveegg(SPECIES_GOLETT)` in both `.pory` and `.inc`.
- **PC items:** add entries to `sNewGamePCItems` in `src/player_pc.c`.
- **Regional dex registration:** add enum entries in `pokedex.h` + matching `HOENN_TO_NATIONAL` lines in `pokemon.c`.
- **Shiny palette rewrite:** edit `shiny.pal` and `overworld_shiny.pal`, delete compiled `.gbapal` binaries, rebuild.

---

## 9. If you're starting a new game built on this codebase

The patterns above remain the same. The most common large-scale operations
will be:

- **Adding a new map** — clone an existing map directory; new entries in
  `data/maps/map_groups.json`, `include/constants/map_groups.h`,
  `data/layouts/layouts.json`. Tile in Porymap.
- **Adding a new species** — new directory under `graphics/pokemon/<name>/`,
  new entry in a `gen_N_families.h`, new `SPECIES_*` and `NATIONAL_DEX_*` and
  optionally `HOENN_DEX_*` constants, references in `pokedex_orders.h`,
  cry registered in sound data. This is a multi-file operation — grep an
  existing species (e.g. `Capsakid`) and mimic every reference.
- **Adding a new item / ability / move** — similar: a constant, a data table
  entry, and any UI strings.
- **Custom story scripts** — write them in `.pory`. Run poryscript to compile
  to `.inc`, or edit both if you can't run the toolchain.

The rule of thumb is consistent: **search the codebase for an existing
analogous thing, then mimic every reference.** Pokemon ROM hack engines have
high coupling across files, so doing half the work always produces silent
bugs.

---

## 10. Lessons learned from v10 Bloodsnow integration (Teddiursa line, May 2026)

This section is appended after the Blue Moon Teddiursa line was shipped as
patch `0001-Blue-Moon-Teddiursa-line-v10-Bloodsnow-palette-...`. Several
gotchas surfaced during integration that weren't covered in earlier
sections:

### 10.1 Per-pixel PNG edits, not just .pal swaps

The Frigibax line shipped as a **palette-only** patch — `shiny.pal` and
`overworld_shiny.pal` files modified, no PNG changes. This works when the
canonical artist used distinct palette indices for every semantically
distinct body part.

**The Teddiursa line did NOT have that luxury.** Specifically:
- Canonical Ursaring uses **idx 8 (cream yellow #F8E880) for BOTH the chest
  ring AND the chest fluff/upper-lip area on the face.** A pure palette swap
  to red would put red on the face, not just the ring.
- Canonical Ursaring uses **idx 12 (tan #C09848) for BOTH the lower lip AND
  body shadow accents.** A pure palette swap of fur to white would lose the
  lip detail.
- Canonical Teddiursa uses **idx 6 (white) for the forehead crescent AND
  small body highlights.** Swapping idx 6 to red would put red dots on the
  body.

The solution was **per-pixel index reassignment in the PNG** before applying
the palette swap. This requires modifying the indexed PNG bytes themselves
(via PIL or similar), then writing back. Steps:

1. Identify which canonical palette index is "overloaded" (used for multiple
   semantically distinct body parts).
2. Find a free or duplicate palette slot. Common candidates: idx 15 if the
   canonical embedded palette has a duplicate, or repurpose idx 13/14 if
   they're rarely used.
3. Reassign the **specific pixels** of one usage zone (e.g., face pixels)
   to the new slot.
4. Write the new palette so the original slot = red marking, the new slot =
   preserved canonical color.

This requires **spatial clustering** to identify which pixels belong to which
usage zone. The Bloodsnow integration used 8-connected pixel clustering with
position-based heuristics (e.g., "the largest cluster in the lower half of
the frame is the chest ring; smaller scattered clusters are face details").

**Code pattern (Python/PIL):**
```python
from PIL import Image

img = Image.open("anim_front.png")
pixels = list(img.getdata())  # flat list of palette indices
w, h = img.size

# Find all positions of a given palette index
positions = [(x, y) for y in range(h) for x in range(w) if pixels[y*w + x] == TARGET_IDX]

# Cluster them by spatial proximity (8-connected)
def find_clusters(positions):
    pos_set = set(positions)
    clusters = []
    while pos_set:
        seed = pos_set.pop()
        cluster = {seed}
        stack = [seed]
        while stack:
            cx, cy = stack.pop()
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0: continue
                    n = (cx + dx, cy + dy)
                    if n in pos_set:
                        pos_set.remove(n)
                        cluster.add(n)
                        stack.append(n)
        clusters.append(cluster)
    return clusters

# Identify "the body cluster" vs "the face cluster" by position/size heuristic
# Apply reassignment to one cluster only
new_pixels = list(pixels)
for x, y in face_cluster:
    new_pixels[y*w + x] = NEW_FREE_IDX

img.putdata(new_pixels)
img.putpalette(new_palette_list)
img.save("anim_front.png")
```

### 10.2 The "snout edge" / small-detail problem

Pokemon sprites often have **tiny isolated pixel clusters (3-6 pixels)** of
a body color that serve as anatomical edge details — the snout edge meeting
the cheek, the inner ear curl, the brow ridge. These tiny clusters often use
the *same palette index* as the large body color (because canonically they
were "the same brown fur"), so when the body becomes white in the Bloodsnow
remap, these tiny details ALSO become white and the sprite loses anatomical
silhouette readability.

The fix is **per-pixel surgical preservation** — identify the specific 3-6
pixel cluster and reassign its index to a slot mapped to canonical brown.

For Ursaring front frame 1, the snout-edge cluster was at exactly
`(22, 7), (22, 8), (22, 9), (23, 6)`. Frame 2's equivalent was found via
small-cluster detection (clusters ≤ 6px in the face area).

**When iterating with a user on sprite quality, expect to do 2-4 rounds of
this kind of surgical detail work.** The user will spot tiny issues that
you might miss at preview scale. Build extreme-zoom comparison sheets (40x+)
to verify each surgical fix worked.

### 10.3 GBA color quantization is mandatory

**RGB values must be quantized to multiples of 8 before writing .pal files.**
The GBA uses 5 bits per channel = 32 discrete values per channel = 8-step
quantization (0, 8, 16, ..., 248). Non-multiple-of-8 values get rounded by
the build, so what you preview in design-time PIL won't match what the game
renders.

```python
def q8(rgb):
    return tuple((c // 8) * 8 for c in rgb)
```

Apply this to every RGB triple before writing to the `.pal` file or before
calling `img.putpalette()`. The Frigibax patch's commit message explicitly
notes "all RGB values are GBA-safe multiples of 8 for accurate
preview-to-render fidelity" — this is the rule.

**Side effect on design-time hacks:** Some palette-design code uses tiny
warm-tint adjustments like `(val + 2, val, val - 2)` to make whites read as
"slightly warm." These offsets are lost in quantization (since 2 < 8) and
the result is pure cool gray. If you want a warm-tinted white that survives
quantization, the offset needs to be 8+ in at least one channel, which is
visually too much. Accept that pure-quantized whites are pure cool whites.

### 10.4 The `P_GBA_STYLE_SPECIES_GFX` flag

In `dsmyst/include/config/pokemon.h:48`:
```c
#define P_GBA_STYLE_SPECIES_GFX         FALSE
```

When FALSE (default in dsmyst), the build uses `anim_front.png`,
`back.png`, `normal.pal` — the modern Gen 4/5-style sprites.

When TRUE, the build uses `anim_front_gba.png`, `back_gba.png`,
`normal_gba.pal` — the legacy GBA-style sprites.

**For all production work, modify the non-`_gba` files only.** The `_gba`
variants are the alternative code path that the current project does not
use. If a future config change flips this flag, the `_gba` variants would
also need to be updated, but that's a separate engineering decision the
user would explicitly make.

### 10.5 "Always shiny" lines go in normal.pal, not shiny.pal

The Frigibax patch shipped as `shiny.pal` modifications because Frigibax
canonically has a "non-shiny" form and a "shiny" form, and the user wanted
the Cormorian heraldic identity to be the shiny appearance.

**The Blue Moon Teddiursa line is mechanically always-shiny from
selection** — players never see a non-shiny version. Per the user's
explicit direction in v0.9.6, the Bloodsnow palette was written to
`normal.pal` (not `shiny.pal`) because what players see *is* the normal
form to them, mechanically.

This is a project-specific design decision. For the Tinkatink line (Phase 1
of the next development cycle), the same logic applies — write to
`normal.pal`. For the Joustroll/Jousteel/Keerin lines (Phase 2), they're
new species so the normal/shiny distinction is whatever we define it to be.

### 10.6 Female Pokemon variants

Some species have **female variants** with different sprite files:
- `anim_front.png` (male) + `anim_frontf.png` (female)
- `back.png` + `backf.png`
- `overworld.png` + `overworldf.png`

Ursaring is one of these. Both male and female variants share the same
`normal.pal` and `overworld_normal.pal`, so palette work applies to both
automatically. But if you're doing per-pixel PNG modifications, you need
to **process the female variants separately** with the same transformations
applied. The Bloodsnow patch processed all 6 Ursaring sprite files
(`anim_front.png`, `anim_frontf.png`, `back.png`, `backf.png`,
`overworld.png`, `overworldf.png`).

When working on a new species, run:
```bash
ls graphics/pokemon/<species>/*f.png 2>/dev/null
```
to detect female variant files. If present, mirror all PNG modifications
to them.

### 10.7 Compile pipeline runs locally (NOT GenSpark anymore)

As of v0.9.6, the Claude session environment has a working ARM cross-compile
pipeline:
- Install: `apt-get install -y binutils-arm-none-eabi gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential libpng-dev pkg-config golang-go`
- Replace Mach-O `poryscript` with Linux ELF build from source
- `make tools && make -j$(nproc) modern`
- Output: `pokeemerald.gba` (32MB, BPEE01)

See bible Section 2 — Local compile pipeline subsection — for full
details. **Do not send the user back to GenSpark for compilation.**

---

End of v0.9.6 lessons.

