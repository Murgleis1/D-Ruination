# Headless play-testing the ROM

**Status: VERIFIED WORKING**, not theoretical. Every claim below was executed in
this container (Python 3.12, x86-64 Ubuntu 24) against a freshly built
`pokeemerald.gba`.

---

## 1. Setup (30 seconds)

```bash
pip install --break-system-packages stable-retro
```

That's it. `stable-retro` is the maintained fork of the archived `openai/retro`
(gym-retro) and it ships the **mGBA** core — the same emulator the repo owner
tests with.

**Do NOT try to build the archived `openai/retro` source.** It needs cmake +
capnproto + lua5.1 and targets old Python; on 3.12 it's a fight for no benefit.

Verified working:

| thing | result |
|---|---|
| `stable_retro` version | 1.0.1 on Python 3.12.3 |
| core | `mgba.json` (GBA) |
| ROM load | `RetroEmulator('/path/pokeemerald.gba')` OK |
| framebuffer | `(160, 240, 3)` uint8 — exact GBA resolution |
| button input | works (12-button mask) |
| save state | `get_state()` 397,312 B; `set_state()` restores exactly |
| state on disk | 42,629 B gzipped; restores in a **fresh process**, frame diff 0.00 |

---

## 2. THE LIMITATION — READ THIS BEFORE USING IT

**The assistant's image/`view` tool is blind** (it has been for this entire
project). The emulator does **not** fix that. You can **capture** frames. You
**cannot look at them**.

So:

- ✅ Analyse frames **programmatically** — means, colour counts, frame diffs,
  per-block colour variety, "did anything change".
- ✅ Save screenshots / contact sheets and `present_files` them so **the user**
  can eyeball them.
- ❌ **Never say a screen "looks correct."** You don't know. Ask the user.

Treat this as *"I can run the game and measure it; you tell me if it looks
right."* That division of labour is still a huge speed-up, because most of the
bugs this project has hit were **detectable**, not subtle:

- the Eden battle crash (garbage sprite + static) — wildly abnormal colour
  distribution vs a real battle screen
- the garbled main-menu text — screen content where a clean save should be blank
- a softlocked cutscene — screen stops changing
- "I fixed X and broke Y" — regression diff against a stored baseline

---

## 3. Basic use

```python
import sys; sys.path.insert(0, 'tools/playtest')
from gba_harness import GBA, contact_sheet, save_checkpoint, load_checkpoint

g = GBA('codebase/pokeemerald.gba')
g.run(700)                     # boot + intro (~11.7s of game time)
g.tap('START')                 # press+release
g.run(120)
print(g.stats())               # {'frame':..., 'colours':..., 'mean':[...], 'std':...}
g.save('/tmp/shot.png')        # then present_files it for the user
```

Buttons: `A B START SELECT UP DOWN LEFT RIGHT L R`.
`g.walk('UP', tiles=3)` does overworld movement (~17 frames/tile).

**GOTCHA: one emulator instance per process.** A second `GBA(...)` in the same
process raises *"Cannot create multiple emulator instances per process"*. If you
need a fresh emulator, use a subprocess.

---

## 4. Checkpoints — the workflow that actually matters

Replaying the intro on every iteration is painful. Don't.

```python
# once: drive to the scene you care about, then
save_checkpoint(g, 'tools/playtest/checkpoints/lab_entry.gz')

# every time after: jump straight there (fresh process, after a rebuild)
g = GBA('codebase/pokeemerald.gba')
load_checkpoint(g, 'tools/playtest/checkpoints/lab_entry.gz')
```

42 KB gzipped, restores byte-exactly in a fresh process. **Store checkpoints in
the repo, not `/tmp`** — sandboxes reset between sessions, and a checkpoint that
took a user-confirmed drive to reach is worth committing.

⚠️ A checkpoint is tied to the ROM it was made from. After a rebuild that shifts
code/data layout, an old state may not restore cleanly. If a restored frame looks
wrong, re-drive and re-checkpoint.

---

## 5. Regression checking (the highest-value blind workflow)

```python
from gba_harness import frame_signature, compare_runs

def scripted_run(g):
    sigs = []
    for step in [(700,None), (30,'START'), (120,None), (30,'A'), (240,None)]:
        n, btn = step
        g.run(n, btn) if btn else g.run(n)
        sigs.append(frame_signature(g.frame()))
    return sigs

# baseline once, store as JSON in the repo; then after any change:
diffs = compare_runs(baseline, scripted_run(g))
```

Non-empty `diffs` = something changed at that step. It won't tell you *what* —
capture a contact sheet at those steps and hand it to the user.

---

## 6. Honest caveats found while testing

- **`garbage_score()` cannot use absolute thresholds.** On the *title screen* —
  a legitimately detailed image — it reports 22.7 colours/block and 85.8% of
  blocks over 12. A rich scene looks "noisy" by that metric. It only works
  **comparatively**: baseline the same scene when it's known-good, then compare.
- **Blind menu navigation is guesswork.** Driving from boot with button mashing
  got to screens that changed, but with no eyes I could not confirm *which*
  screens. The reliable pattern is collaborative: capture a contact sheet →
  user confirms where we are → checkpoint that spot → automate from there.
- **`changed_over()` reported `False` on the title screen.** Either the title is
  static at that moment or the default threshold (1.5) is too high for subtle
  animation. Tune per scene rather than trusting the default.
- The mGBA core here is stable-retro's build, not the user's mGBA. Behaviour
  should match, but if something renders differently, suspect the core before
  concluding the ROM is broken.

---

## 7. Suggested first task

Do this *with* the user, then commit the checkpoint:

1. Boot, capture a contact sheet through the title and main menu.
2. `present_files` it; ask the user which frame is the overworld start.
3. Drive to Cadmus's lab, capture again, confirm.
4. `save_checkpoint(g, 'tools/playtest/checkpoints/lab_entry.gz')` and commit it.

From then on, testing the Chapter-1 lab scene — briefing, three-ball selection,
the theft, the Eden fight — is a scripted run from that checkpoint plus a contact
sheet for the user, instead of them replaying it by hand every iteration.
