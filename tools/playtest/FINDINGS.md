# Play-test findings

## Reading real game state out of the emulator (works, and beats guessing)

`RetroEmulator` exposes no memory API, but `get_state()` returns the mGBA save
state, which contains GBA RAM. Offsets pinned for this ROM by anchoring on the
player name bytes and cross-checking against known values:

| thing | value |
|---|---|
| IWRAM base inside the state blob | `0x019000` |
| EWRAM base inside the state blob | `0x021000` |
| `gSaveBlock1Ptr` (from `pokeemerald.map`) | `0x03006A08` |
| SaveBlock1 `pos` / `location` | `+0x00` / `+0x04` |
| **vars array offset in SaveBlock1** | **`0x15B8`** |

The `/*0x139C*/` comment on `vars[]` in `include/global.h` is **stale** for this
fork - using it reads garbage. `0x15B8` was derived empirically and verified by
watching the lab-stage var transition 0 -> 1 on entering the lab.

```python
sb1  = u32(state, IW + (0x03006A08 - 0x03000000))
base = EW + (sb1 - 0x02000000)
pos  = struct.unpack_from('<hh', state, base)        # player x, y
mg, mn = struct.unpack_from('<bb', state, base + 4)  # map group, map num
var  = lambda v: u16(state, base + 0x15B8 + (v - 0x4000) * 2)
```

Resolve `mg, mn` against `include/constants/map_groups.h`, e.g. `(2,5)` is
`MAP_PELLUCA_CITY`, `(0,29)` is `MAP_PELLUCA_UMBRA_LAB`.

## Detecting player control - do it DIFFERENTIALLY

Wrong: "the screen changed while I held a direction". Cutscenes animate on their
own, so this reports control that does not exist (it fooled me for several runs).

Right: from an **identical saved state**, run N frames idle and N frames holding
a direction, then compare the two resulting frames. Non-zero difference means
real control. Better still, just read the player's `pos` before and after.

## Open bug: the intro never yields control (REPRODUCIBLE)

Boot -> START -> press A repeatedly. Measured route:

`map(0,0)` intro -> `map(0,28)` PellucaReflection (7,6) -> `map(2,5)` Pelluca
City dock (44,52) -> `map(0,29)` PellucaUmbraLab (5,11) - **and it stops there**.

At that point `VAR_UNUSED_0x40A1` (lab stage) is **1**, meaning `DR_Lab_Briefing`
started (it sets 1 on its 2nd line) and never reached its closing `releaseall`,
so `lockall` is still in force. Confirmed:

- no direction ever moves the player off (5,11), at any input speed
- pressing B does not release it
- the script pointer freezes near `PellucaUmbraLab_EventScript_Umbra` (0x0838DD30)
- **not caused by the PokeLog edit** - a build with the pre-PokeLog lab script
  behaves identically
- 25,700 A presses / 442,000 frames (~2 hours game time) never escapes it
- unaffected by input pacing (16-frame and 48-frame gaps both hang)

NOT yet confirmed whether this reproduces in the repo owner's own mGBA, or
whether it is specific to stable-retro's mGBA core (see PLAYTEST.md s6).

## Checkpoints

- `checkpoints/dock_arrival.gz` - Pelluca City dock, verified by RAM as
  `map(2,5) pos(44,52)`, the documented arrival tile. Saves ~12,000 frames of
  replay. Note the player name in this save is junk ("Aaaaaac") because it was
  produced by mashing A through name entry.
