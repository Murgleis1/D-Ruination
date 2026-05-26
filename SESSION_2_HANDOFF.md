# Dreamstone Ruination — Session 2 Handoff

**Status as of this doc:** PR #1 merged. 27 commits landed in `main`.
**Date written:** End of Session 2 (the session that designed and shipped 3 starter line rebalances + 2 custom species + initial bible sync).

This file is **session 2's handoff to session 3**. It is meant to be read fresh by the next Claude session. It supersedes nothing in the prior MASTER NOTES / SESSION_HANDOFF_MASTER files but adds focused context for what session 3 should pick up.

---

## What session 2 actually shipped

### Codebase (engine work) — 25 commits

**Three starter lines completely redesigned and rebalanced.** All 9 obtainable species now conform to the unified BST framework (375/480/600 across stages) with distinct role identities (Frigibax = physical-attacker+speed, Teddiursa Blue Moon = special-attacker apex, Tinkatink = defensive colossus).

- **Frigibax line:** new 16-move shared learnset, Lv 1-77; Cormorian Behemoth Blade as Lv 77 ace; tutor-Mountain-Gale gates Arctibax → Baxcalibur evolution; Lv 0 Ice Fang on Arctibax on-evolution; Mountain Gale buffed (95 BP / 95 acc / 15 PP / 33% flinch / Water override TODO).
- **Teddiursa Blue Moon line:** new 16-move shared learnset (lunar-mystic special-attacker — Echoed Voice, Confuse Ray, Psybeam, Scorching Sands, Torch Song, Moonblast, Lumina Crash, Lunar Blessing, Hyper Beam, Calm Mind, Aura Sphere, Moongeist Beam); Lv 0 Hyper Voice on Ursaring on-evolution; Blood Moon retyped Normal → Ground; Moongeist Beam buffed 100 → 140 BP; tutor-Blood-Moon gates Ursaring → Bloodmoon Ursaluna evolution; **regular Hisuian Ursaluna intentionally unobtainable** (canonical stats preserved for Pokedex).
- **Tinkatink line:** new 16-move shared learnset (Fake Out, Double Slap, Baby-Doll Eyes, Metal Claw, Covet, Low Sweep, Bulk Up, Behemoth Bash, Brutal Swing, Play Rough, Body Slam, Body Press, Headlong Rush, Shell Smash, Close Combat, Sunsteel Strike); Behemoth Bash Cormorian variant (Normal physical, 100/95/10, Steel override TODO); Sunsteel Strike Cormorian variant (Fire-type non-STAB, 140/100/10, ignoresTargetAbility preserved); tutor-Gigaton-Hammer gates Tinkatuff → Tinkaton evolution; **no Lv 0 on-evolution moves** for Tinkatuff or Tinkaton.

**Custom moves landed:**
- Behemoth Blade Cormorian (Dragon, 120 BP, Fairy override TODO)
- Behemoth Bash Cormorian (Normal, 100 BP, Steel override TODO)
- Mountain Gale Cormorian (Ice, 95 BP, Water override TODO)
- Sunsteel Strike Cormorian (Fire, 140 BP, ignoresTargetAbility)
- Moongeist Beam buffed (Ghost, 140 BP, ignoresTargetAbility)
- Double Slap + Covet retyped Normal → Fairy globally
- All Lv 77 starter aces normalized to 10 PP (Behemoth Blade / Moongeist Beam / Sunsteel Strike)

**Joustroll & Jousteel fully implemented as custom species** — SPECIES_JOUSTROLL = 1524, SPECIES_JOUSTEEL = 1525. New National Dex slots, complete species_info, level-up learnsets, teachable learnsets (= Varoom + Escavalier union, 39 TMs), evolution table (Joustroll → Jousteel at Lv 50), graphics-table registrations, sprite binaries (compiled from PNG sources via codebase-bundled gbagfx), overworld follower pic tables, Pokedex orderings (alphabetical/weight/height all sorted), category names, Pokedex descriptions, final height (1.0m / 1.7m) and weight (100kg / 530kg). Cry placeholders: CRY_VAROOM (Joustroll), CRY_VOLCANION (Jousteel). Lv 0 on-evolution Tachyon Cutter + King's Shield on Jousteel.

### Bible work — 2 commits

Only the highest-information-density bible files were synced this session. **Bible doctrine was updated** during session 2: the new workflow is **edit splits directly, regenerate canonical at end** (a reversal from the prior doctrine which had canonical as the only edit target). This change has NOT yet been written into `bible/INDEX.md` — that's deferred to session 3.

**Committed:**
- `bible/05_starter_lines.md` — full starter learnset rewrites; new BST framework subsection; new three-line role identity framework; new Frigibax-line detailed subsection (previously the file had no Frigibax-line equivalent to the Tinkatink/Teddiursa subsections); evolution-convention clarification (Lv 24 uniform for Stage 1→2, EVO_MOVE engine condition for Stage 2→3); v0.9.7 Tinkaton BST 560 lock superseded; v0.9.5 Blue Moon stat redistribution superseded.
- `bible/13_cosmology_mechanics.md` — six new custom-move subsections; new "Cormorian engineered-weapons twin-pair" narrative; full Joustroll/Jousteel canonical entry replacing the v0.9.4 stub; Cadmus's family-three-egg lore captured; species Pokedex descriptions and stat lines locked.

---

## What's DEFERRED to session 3

These are the bible sync items NOT yet committed. They were planned but deferred to keep session 2's context budget healthy.

| # | Target file | What needs to land |
|---|---|---|
| 1 | `bible/07_characters_viziers.md` | **Cadmus Umbra entry update** — add House Umbra Joustroll/Jousteel monopoly cross-reference, the three-egg-generation lore + Trial 4 sidequest hook. Most of this content already exists in 13_cosmology_mechanics.md commit `fa0b4666`; this is the Cadmus-side cross-reference. |
| 2 | `bible/14_story_spine.md` | **Trial 4 Joustroll Egg sidequest writeup.** The full narrative is documented in chat log: Cadmus dispatches player to deep cavern; cave is overrun by Mega Gyarados boss + Crawdaunt/water-Pokemon clan; player solves puzzles, defeats boss; reaches incubation shrine; egg dialogue "is it just me or is the egg glowing?" with two-choice response (shiny vs. normal Joustroll); return to Cadmus; Cadmus speech "Maybe our Jousteels can even face off in battle one day! Wouldn't that be exciting?" |
| 3 | `bible/17_open_questions.md` | Status updates: Trial 4 Egg sidequest moves from OPEN to LOCKED in narrative spec (still OPEN for event scripting/map work); Mega Baxcalibur BST 720 constraint (Speed > 120, Atk > 145) added; Hisuian Ursaluna unobtainable confirmed. |
| 4 | `bible/15_design_principles.md` | Unified starter-trio BST framework documented in design principles as a project-level pattern (currently lives only in 05_starter_lines.md); Lv 77 starter-ace 10-PP convention documented. |
| 5 | `bible/16_bloodlines_canon.md` | Cormorian engineered-weapons twin-pair narrative cross-reference (full version in 13_cosmology_mechanics.md commit `fa0b4666`); House Umbra Joustroll/Jousteel as the family's heraldic-symbol + Vizier-role-anchor across centuries. |
| 6 | `bible/18_engineering_tasks.md` | Engine TODOs: Behemoth Blade Fairy-effectiveness override, Behemoth Bash Steel-effectiveness override, Mountain Gale Water-effectiveness override (all parallel to Freeze-Dry's existing type-override damage-calc path). Phase 1 starter-line work status update to LANDED. Trial 4 sidequest scripting added as new task. Joustroll/Jousteel cry audio listed as user-authored deliverable. |
| 7 | `bible/INDEX.md` | **Doctrine update:** rewrite the "Canonical source... is the only file that gets edited" instruction to reflect the new workflow ("Splits are the active edit target; canonical is regenerated from splits at session end"). |
| 8 | `bible/dreamstone_ruination_bible_v0.9.7.md` (canonical) | **Regenerate from splits.** This is a mechanical operation: concatenate all 19 split files in section-number order, strip the per-file `<!-- This file is a split-section view... -->` header from each, output a single canonical document. The user wants to do this regeneration themselves locally (or have session 3 do it once all split edits are complete). Filename version may bump to v0.9.8 given the substantial v0.9.8 locks landed this session. |

**None of these are blocking the engine work.** The codebase is fully consistent with itself; the deferred bible items are documentation cleanup.

---

## Other deferred work (post-bible)

These are larger workstreams the project still needs but that were OUT of scope for session 2:

- **Joustroll/Jousteel cry audio** — user authoring; placeholders CRY_VAROOM and CRY_VOLCANION currently used
- **Trial 4 Joustroll Egg sidequest event scripting** — map work + scenario scripting; lore is locked, mechanics still need engineering session
- **Trainer team designs** — for the 9 Trial Barons, 4 Viziers, cult Harbingers, and the Champion fight. User flagged this as the next major workstream after bible cleanup.
- **Mega Baxcalibur stat lock** — BST 720 confirmed; specific stat distribution still OPEN; constraint locked (Speed > 120, Atk > 145).
- **Cadmus's personal Jousteel battle spec** — moveset, item, ability choice for the Vizier-gauntlet encounter. Open per bible.
- **Engine type-override implementation** — three damage-calc hooks in `src/battle_util.c` (Behemoth Blade/Bash/Mountain Gale), parallel to existing Freeze-Dry pattern. Dedicated engineering session.

---

## Critical context for session 3

### The new bible doctrine

**Edit splits directly, regenerate canonical at end of session.** This reverses the prior `bible/INDEX.md` instruction. The reason is pragmatic: the canonical bible is ~190K tokens and cannot fit in a Claude session's context. The splits (each ~25K tokens max) can.

Workflow for session 3:
1. Identify which split file your work touches
2. Fetch that split file directly via the Contents API
3. Edit it, commit it
4. After all edits, regenerate the canonical by concatenating splits in section-number order (mechanical operation)
5. Update `bible/INDEX.md` to reflect the new doctrine if not already done

### The codebase has been tested by inference, not compilation

Session 2 did NOT run `make` on the codebase. The 25 engine commits should compile based on pattern-matching against canonical species and verifying all referenced symbols exist, but the build has not been verified. **The user should compile-test before any further engine work** in session 3.

Possible failure modes to watch for if the build breaks:
- `enemyMonElevation` field on Jousteel — confirmed used by Aegislash, but field name in struct could differ
- `BACK_ANIM_H_VIBRATE` / `ANIM_H_VIBRATE` — confirmed used by other species but defined in an animation-constants file we didn't directly verify
- The 30 sprite binaries were generated by gbagfx in the sandbox — they should be byte-identical to what the codebase build would produce, but if the build system uses different compression parameters than the codebase-bundled gbagfx defaults, there could be subtle issues

### Token used by session 2

Session 2 used a fine-grained GitHub PAT issued by the user at session start with: Contents R/W + Pull Requests R/W on `Murgleis1/D-Ruination` only, 7-day expiration. The PAT was disposable and is being revoked by the user at the end of session 2. **Session 3 will receive a fresh PAT in the first message.** Session 2's PAT will not work and is not stored in this doc by design (GitHub's secret-scanning correctly blocks committing PATs to repo contents).

### The 5-version pattern

The Lv 77 ace pattern across the trio is one of the project's cleanest mechanical-narrative alignments:

| Line | Lv 77 ace | Source legendary (absent) | Type | Power | Effect |
|---|---|---|---|---|---|
| Frigibax | Behemoth Blade | Zacian-Crowned | Dragon | 120 | Fairy override |
| Teddiursa Blue Moon | Moongeist Beam | Lunala | Ghost | 140 | ignoresTargetAbility |
| Tinkatink | Sunsteel Strike | Solgaleo | Fire | 140 | ignoresTargetAbility |

Plus Behemoth Bash (Zamazenta) at Lv 30 on Tinkaton. **Four absent canonical legendaries have their signatures repurposed for Cormorian-line use.** This is the "Cormorian engineering > legendary gifts" thematic statement.

### Stat shape philosophy

- **Each Stage 3 has one signature stat at 145** OR paired 125s: Baxcalibur Atk 145, Bloodmoon Ursaluna SpA 145, Tinkaton Def 125/SpD 125.
- **Both physical-attacker lines (Frigibax, Tinkatink) dump SpA** because their kits are 100% physical.
- **Only the Blue Moon line uses SpA** (full special kit).
- **The three identities are visible at every stage**, not just final form.

---

## How to start session 3

If picking up where session 2 left off, the natural next workstream is **the bible sync follow-up** (the 6 deferred items above) followed by **trainer team designs** (the user-flagged next major workstream).

A reasonable session 3 opener:

> "Continuing Dreamstone Ruination work from session 2's handoff. Session 2 shipped the merged PR. Please read MASTER NOTES, SESSION_HANDOFF_MASTER, and this session-2 handoff doc, then read bible/INDEX.md to orient yourself. Don't pull the 190K-token canonical bible — work from splits per the new doctrine. After orientation, we'll start with the deferred bible sync items, then move into trainer team designs."

The user will provide a fresh PAT and confirm which workstream they want first.
