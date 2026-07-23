# Dreamstone Ruination — Session Handoff

**Project:** ROM-hack prequel to Dreamstone Mysteries. Repo `Murgleis1/D-Ruination`
(user's own public repo). Empire-era Cormoria; the player is **Osrid** ("Nomad").
**Read this whole file before touching anything.** Then skim the referenced bible
sections. The prior session's full detail is in the conversation transcript.

---

## 0. FIRST FIVE MINUTES (do these before any work)

1. **Re-arm the GitHub token** (it lives only in the sandbox git config, resets
   between conversations — the user must paste it):
   ```
   git -C /home/claude/repo remote set-url origin https://<TOKEN>@github.com/Murgleis1/D-Ruination.git
   ```
2. **Restore the poryscript exec bit** (clears on reset):
   ```
   chmod +x /home/claude/repo/codebase/tools/poryscript/poryscript
   ```
3. **Confirm you're synced:** `cd /home/claude/repo && git fetch -q origin && git log --oneline -3`.
   Latest commit should be at or after `612892ba`.
4. **Committer identity** is preconfigured for commits:
   `Dreamstone Ruination (bible session) <bible@dreamstone.local>`.
5. **NEVER `git add -A` blindly.** The Linux poryscript binary must stay
   uncommitted (committing it breaks the user's macOS build). Always:
   ```
   git add -A && git reset -q HEAD codebase/tools/poryscript/poryscript
   ```

---

## 1. ENVIRONMENT

- **Repo root** `/home/claude/repo`; **codebase** `/home/claude/repo/codebase`
  (a pokeemerald-expansion/DM checkout). Bible in `bible/`, assets in `assets/`.
- **Sandbox persists within a conversation, resets between them.** Anything in
  `/home/claude/*.py` or `/tmp` is scratch — recreate as needed. Durability =
  `git push`. Commit meaningful units so nothing is lost.
- **Build:** `cd codebase && timeout 290 make modern > /tmp/b.log 2>&1`.
  Foreground, 1 core, ~5 min. Exit **124** = still building (rerun same command),
  **0** = done, **2** = error (grep the log). Output `codebase/pokeemerald.gba`
  (~33 MB, ROM is ~87% full — fine).
- **Show the user a build:** `cp codebase/pokeemerald.gba /home/claude/Dreamstone_Ruination.gba`
  then `present_files`.
- **THE IMAGE/`view` TOOL HAS BEEN BLIND THE ENTIRE PROJECT** (returns blank).
  Verify ALL visual work two ways: (a) in code — decode the built `.4bpp`/`.bin`
  and assert equality/colour-counts against the source; (b) render to a PNG and
  `present_files` so the *user* sees it. Never assume the build did what you meant.
- **Poryscript:** maps with `scripts.pory` compile it to `scripts.inc` at build.
  EDIT THE `.pory`. Standalone check:
  `codebase/tools/poryscript/poryscript -i <f>.pory -o /tmp/t.inc -fc codebase/tools/poryscript/font_config.json -cc codebase/tools/poryscript/command_config.json`

---

## 2. WORKING STYLE (the user is a senior engineer — this matters as much as the code)

- **Evidence before action.** Examine the exact error / the actual data / the
  real source pixels FIRST. Look things up in the code; do not guess or assume.
  The user gets (reasonably) frustrated by guessing and by shipping unverified work.
- **Debugging protocol:** read the exact error + stack, request/inspect the
  specific data it names, add try/catch to get detail, propose ONE minimal
  evidence-based fix. No theorising about data you haven't seen; no shotgun of
  "possible" fixes.
- **On asset/design choices, run the analysis process** (measure, compare
  numerically, present) rather than picking by taste. Example that worked: the
  cliff tileset was chosen by colour-distance to the reference, not by eye.
- The user does their own in-game testing (mGBA) and sends screenshots. Diagnose
  from the screenshot + code, root-cause it, fix once.
- **Copyright:** the user's OWN assets/text are fine to use. Always redact tokens
  in any command output:
  `sed -E 's#(https://)[^@/[:space:]]+@#\1REDACTED@#g; s#github_pat_[A-Za-z0-9_]+#REDACTED#g'`

---

## 3. THE PROCESS FOR TILESET / PIXEL-ART WORK  ← the part the user wants preserved

All of this is now committed as runnable tools in **`tools/evernahn_conversion/`**
(read `README.md` and the docstrings in `lib_convert.py` — they record failures,
not just the happy path). The hard-won rules:

### Downscaling (32px RMXP → 16px metatile, or hi-res art → 64px sprite)
- **Use BOX or NEAREST. Never a smoothing filter.** Measured on flat pixel art:
  BOX/NEAREST preserve exact colour counts (9→9); HAMMING gives 90-127; LANCZOS
  gives 117. Smoothing invents colours the palette can't hold and kills hard edges.

### Converting supplied character art to a GBA sprite
- **Key the background by NEUTRALITY, not brightness.** A warm bone mask
  (235,230,217) and a neutral near-white background (R=G=B) share luminance; a
  brightness threshold deletes the mask. Test R==G==B within tolerance AND bright,
  then FLOOD-FILL from the border so interior neutral pixels aren't cut. Then keep
  only the largest connected component to drop specks.
- **If the art is a resampled PNG (tens of thousands of near-dupe colours),
  RECOVER the artist's ~15 colours** (merge near-dupes, fold rarest into nearest)
  rather than re-quantising — re-quantising mutes the hues. The user noticed this
  immediately when an early sprite came out "muted."
- **If you must genuinely quantise, use FASTOCTREE, not MEDIANCUT.** MEDIANCUT
  weights by pixel count so a big dark region dominates and it caps ~luminance
  128, dropping a bright mask and bright hair. FASTOCTREE spans the full range.
  Exclude the near-white edge halo from the palette source so it doesn't waste a slot.
- **Downsample the indexed image by MODE (most-common index per block), not
  averaging.** Averaging blends outline+fill into mud. Require a block ≥40% opaque
  to be drawn so the silhouette stays clean.
- **Best case: if the user hands you a finished 64×64 with ≤15 colours, apply it
  1:1 with ZERO resampling.** That is the only thing that preserved the 1px
  Eye-of-Horus mask glyph — every downscale destroyed it. (`osrF64.png` was done
  this way.)
- **Emerald trainer-sprite house style** (measured from brendan/may/steven/wally):
  ~14-15 of 15 palette slots used, darkest colour pure (0,0,0), luminance spans
  0-255, silhouette outlined in pure black, outline share 24-68%. If source art
  lacks a black outline, reserve palette index 1 = black and snap the edge to it.
  (Skip if the art already has one — the user's later art did.)
- **Repairing a porous silhouette:** ONE bounded 3×3 morphological closing
  (dilate once, erode once) — bridges ≤2px gaps, cannot run away. DO NOT loop a
  "fill if ≥N neighbours" with loosening thresholds; it cascades and fills the
  whole bbox (this literally turned a 1068px sprite into a 2847px diamond once).

### pokeemerald tileset mechanics
- A **metatile** = 8 u16 tile-entries (16 bytes): entries 0-3 bottom layer, 4-7
  top layer (top drawn transparent over colour 0). Entry bits: 0-9 tileId
  (<512 primary, ≥512 secondary-512), 10 xflip, 11 yflip, 12-15 palette slot.
- **metatile_attributes.bin:** one u16 per metatile; bits 0-7 behaviour (`MB_*`,
  e.g. `MB_NORMAL`=0x00, `MB_POND_WATER`=0x10 = surfable), bits 12-13 layer type
  (use 1).
- **Map cell** (map.bin u16): 0-9 metatile_id | 10-11 collision | 12-15 elevation.
- **`NUM_PALS_IN_PRIMARY = 6`.** A primary tileset owns sub-palettes 0-5; a
  secondary owns 6-12. Max 2 tilesets per map. A primary tile can only use slots 0-5.
- **A tileset dir needs ALL 16** `NN.gbapal` + `NN.pal` files even if only a few
  carry colour, or the build errors on the first missing one.
- **Registering a new primary tileset touches 3 files** — `graphics.h`,
  `metatiles.h`, `headers.h`. The vanilla anchors may not be first; safest to
  PREPEND declarations to graphics.h/metatiles.h (order is irrelevant) and insert
  the struct before `gTileset_General` in headers.h. Use `render_tileset.py` to
  verify visually afterward.
- **Tilesets keyed in `data/layouts/layouts.json`** (per-layout primary/secondary
  + width/height/blockdata paths), NOT map.json. `map_groups.json` lists maps by
  NAME string (a MAP_ constant auto-generates from it — and if a map is missing
  from map_groups.json, a warp to it fails to link with an obscure `>>`/`&`
  "undefined symbol" error, which is how the monastery-map bug manifested).

---

## 4. WHERE THE EVERNAHN / PELLUCA CONVERSION STANDS

**Goal:** repaint Pelluca Valley (80×60) in the Evernahn tileset per the user's
layout reference. Bible §18 documents this as a build task.

**Done + committed:**
- `gTileset_Evernahn` PRIMARY tileset exists (`codebase/data/tilesets/primary/evernahn/`),
  **46 metatiles, 145 tiles** (budget 512 each): 0-5 grass base, 6-13 grass/shore
  edge, 14-21 grass edge alt, 22-23 open water, 24-34 pool+clay, 35-45 pool calm.
  Palettes 0 grass / 1 water / 2 pool. Water+pool = `MB_POND_WATER` (surfable).
- Autotile roles were CORRECTED against the user's description (Grass_3 = base
  grass not anim; Calvera = clay-banked pools; white RMXP template slot dropped).

**THE IMMEDIATE NEXT STEP — cliff/path merge (awaiting user OK):**
- Selection committed at `assets/pelluca_dock_spec/autumn_cliff_path_selection.json`
  — 108 cliff + 35 path metatiles from `gTileset_Autumn`, chosen by colour-distance
  to the reference (autumn palettes 2+3 won: cliff 23.0, path 13.4).
- The user was reviewing rendered sheets `autumn_cliffs.png` / `autumn_paths.png`
  (regenerate with `render_tileset.py` if the sandbox reset). **Once they confirm,
  run `python3 tools/evernahn_conversion/merge_cliffs_paths.py` then rebuild.**
  It puts autumn pal2→Evernahn slot 3, pal3→slot 4 (no quantising) and appends the
  metatiles. Then render + present_files to verify.

**Then, in order:**
1. Convert the 3 shared buildings into PRIMARY (each town has a monastery+tavern):
   Templar Monastery `Evernahn.png` rows **18-23**, Pokémon Tavern rows **69-71**,
   generic house rows **100-104**. (Building rows located by template + colour-sig
   matching, confirmed by the user.)
2. Convert Pelluca SECONDARY: Cadmus's lab rows **173-178**, period ship rows
   **179-186** (replaces the modern SS_TIDAL at the dock), dock, decoration.
3. Repaint the 80×60 map from scratch per the blueprint (below).

---

## 5. THE MAP REPAINT — committed reference data

- **Blueprint:** `assets/pelluca_dock_spec/pelluca_blueprint_80x60.npy` — zone grid
  from the user's layout reference (grass 40.5%, cliff 14.2%, water 13.8%, path
  12.1%, tree 10.7%, structure 8.7%). Water is confined to the SOUTHERN THIRD
  (rows ~34-59), unlike the current map's 25% everywhere.
- **DOCK — CRITICAL, must be recreated exactly:**
  `assets/pelluca_dock_spec/dock_geometry.json` — full cell grid + warps + objects
  for x38-52, y42-58. The arrival cutscene warps Osrid to **(44,52)** and walks him
  north up the pier, so **the walkable elevation-3 column y52→y45 MUST survive.**
  Pier = metatile 175; lab warp (47,44); ferry localid 61 at (44,55) → replace with
  the Evernahn ship.
- **Four exits (LOCKED, atlas §15.6):** N gatehouse behind monastery → Ivy River;
  E gatehouse → Hoya Delta; W plain Route 11 → Hollow Hill; S water Surf-gated →
  Rivetshore (Route 10). **Secret Umbra cavern entrance at x63-65, y40-42** (across
  water, unreachable on foot — suits Umbra-sealed; must exist from Chapter 1).
- **Gotchas to fix during repaint:** `PellucaCity/map.json` connections currently
  wire **left→ROUTE7** (should be Route 11) and **down→ROUTE8** (should be
  impassable water for the Surf gate). **Route 11, Route 10, and Hollow Hill maps
  DON'T EXIST** — the W/S exits need stub maps created (the "Route11" dirs in the
  repo are vanilla Route101-110; "WinterlilyHollow" is unrelated). Repaint-from-
  scratch was chosen over re-skin (re-skin remaps every metatile id in the map.bin).

---

## 6. OTHER OPEN THREADS

- **Chapter-1 lab scene** (`codebase/data/maps/PellucaUmbraLab/scripts.pory`) is
  built and working: briefing → 3-starter select → Eden theft/fight → monastery
  cell warp. Music beat added (silence on blackout → `MUS_ENCOUNTER_AQUA` on Eden
  reveal). Starter shininess: Frigibax shiny, Teddiursa/Tinkatink normal.
- **Osrid sprites:** front (`osrF64.png`) applied 1:1, mask intact. **Back sprite
  is still my conversion** (duller than the front). If the user sends a hand-fixed
  320×320 back sprite, apply it 1:1 the lossless way (their palette verbatim,
  mode-per-5×5-block). The full back-sprite wiring is in place (TRAINER_BACK_PIC_OSRID
  = 12; sTrainerBackSpriteTemplates entry; palette + reshow + safari + recorded
  paths + trainer card all point at Osrid).
- **Monastery cell dialogue** — deferred, to be written separately.
- **Bible amendments** are committed but tagged `[AMENDED — Chapter-1 balance pass]`
  / `[LOCKED — ...]` WITHOUT version numbers. **The user stamps versions** — leave
  the tags un-versioned.
- **Trainer slots:** only 6 of 9 spare before overflow; Eden is fought 5× and
  branching each 3 ways would need 15 — flag before mass-creating Eden trainers.

---

## 7. KEY CONSTANTS / FACTS (quick reference)

- Species: FRIGIBAX 1388, TEDDIURSA 216, TINKATINK 1345, NICKIT 827, THIEVUL 828,
  JOUSTEEL 1525.
- Active learnset set is **gen_9.h** (of gen_1..gen_9 alternatives). Frigibax Lv5 =
  Tackle/Leer/Mud Slap; Tinkatink Lv5 = Pound/Growl. Eden's parties use natural
  learnsets. Nickit line has Prankster in slot 1 (trainer ability not in species
  slots silently falls back to slot 0 — this is why the edit was mandatory).
- Portraits: PORTRAIT_OSRID 1 / CADMUS 2 / EDEN 3. Missing expressions fall back to
  expr[0] (neutral) — Cadmus-angry, Eden-happy/upset call the right expression in
  script already; no code change needed when art is added.
- Free resources used: VAR_UNUSED_0x40A1 (lab stage), VAR_UNUSED_0x4083 (starter
  pick), FLAG_UNUSED_0x885/886/887/88E.
- `TRAINER_CLASS_BRIGAND` = 0x6C (money 15 → 300 reward). Eden trainers
  TRAINER_DR_EDEN_LAB_1/2/3 = 855-857, declared in include/constants/opponents.h
  (trainer IDs are NOT auto-generated). Difficulty: game runs DIFFICULTY_NORMAL,
  so trainers must exist at [DIFFICULTY_NORMAL] (an EASY-only entry = all-zero
  trainer = battle crash).
