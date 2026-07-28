> Paste this whole message into a fresh chat to start a new Dreamstone Ruination
> session. Replace `<PASTE_TOKEN_HERE>` with a fresh GitHub PAT (rotate it after —
> a token pasted into chat is compromised). Nothing else needs editing.

---

I'm working on **Dreamstone Ruination**, my pokeemerald-expansion ROM-hack prequel
(repo `Murgleis1/D-Ruination`). This is a continuing project; a detailed handoff
lives in the repo. Work like a careful senior engineer: evidence before action,
measure twice, verify before shipping, ask when a decision is genuinely mine to
make. Don't dump code before the goal and constraints are clear.

**Do this first, in order:**

1. Clone into `/home/claude/repo` (the container starts empty — nothing persists
   between sessions):
   ```
   git clone https://<PASTE_TOKEN_HERE>@github.com/Murgleis1/D-Ruination.git /home/claude/repo
   ```
   Redact the token from any output you show me.
2. `chmod +x /home/claude/repo/codebase/tools/poryscript/poryscript`
3. **Read `handoff/SESSION_HANDOFF.md` in full before touching anything**, then
   `handoff/BUILD_SETUP.md`, `tools/playtest/PLAYTEST.md`, and
   `tools/playtest/FINDINGS.md`. Skim bible §18 (engineering tasks) and §19
   (location atlas). The handoff points at everything else.
4. Set the committer identity to `Dreamstone Ruination (bible session)
   <bible@dreamstone.local>` and confirm you're synced with origin.

**Things the handoff explains but that bite immediately if missed:**

- The build works here — devkitPro is NOT required. `apt-get install
  gcc-arm-none-eabi ...` + a Linux poryscript from GitHub releases; recipe in
  BUILD_SETUP.md. The committed poryscript is a macOS binary and won't run in the
  Linux container — replace it locally but **NEVER commit the Linux one** (it
  breaks my macOS build): `git add -A && git reset -q HEAD codebase/tools/poryscript/poryscript`.
- The `view` tool is unreliable on image files (treat as blind) — verify visuals
  in code AND with `present_files` for me. If you're stuck on something visual,
  ask me to paste a screenshot; those you read fine.
- Headless play-testing is set up (`pip install --break-system-packages
  stable-retro`). You can boot the ROM, read real game state out of the save
  state (offsets in FINDINGS.md), and hand me contact sheets. Emulation is ~2000
  fps; there's a verified checkpoint at the dock so you can skip the long intro.

**Current Chapter-1 status — the full picture (details in handoff §6):**

*Blocking / needs my input:*
- **Intro hang (TOP PRIORITY).** The game never reaches player control — it drives
  boot → PellucaReflection → Pelluca City dock (44,52) → PellucaUmbraLab (5,11) and
  stops there, with the lab-stage var (`VAR_UNUSED_0x40A1`) stuck at 1, meaning
  `DR_Lab_Briefing` started but never hit its closing `releaseall`. Full trace in
  `tools/playtest/FINDINGS.md`. It reproduces in stable-retro's mGBA core; it is NOT
  caused by the recent PokeLog edit (a pre-PokeLog build hangs identically).
  **Ask me whether it also hangs in my own mGBA before treating it as a real script
  bug** — that fork decides the whole diagnosis. If it's real, find the exact
  command in `DR_Lab_Briefing` that never returns.
- **PokéLog paper aesthetic — unresolved.** The dex background palettes were
  re-tinted to parchment, but I could not tell what was going on from a
  background-only composite. Capture a REAL dex screen with the harness and show me
  before we call it done. (The PokéLog itself works: Cadmus grants it before the
  starter choice; it's a functional Pokédex, `src/pokedex.c` untouched.)

*Built this session but NOT yet confirmed in-game (the hang blocks reaching them):*
- Party now appears in the start menu (`setflag(FLAG_SYS_POKEMON_GET)` added in
  `DR_Lab_Theft` — it was missing). A save from before the lab won't have this.
- Blackout after starter selection shortened 180→90 frames.
- Eden's post-defeat line rewritten (wants a rematch "after I escape").
- PokéLog handover + fanfare + `FLAG_SYS_POKEDEX_GET`; 10 strings renamed
  POKéDEX→POKéLOG in `src/strings.c` (same length).
- Pelluca Valley + Pelluca City Houses music → `MUS_LILYCOVE`.
- Period ship at the dock: replaced the modern SS Tidal with a wooden Evernahn ship
  — but as a SPRITE shared by 11 maps (interim; the metatile version supersedes it).

*Deferred content (waiting on me or a later task):*
- **Monastery cell dialogue** — the scene after Eden jails you; to be written.
- **Cormorian regional dex** — a joint task for later; the Hoenn/National dex-mode
  strings were deliberately left un-renamed because they belong to it.
- **Osrid back sprite** — still the assistant's duller conversion; I'll send a
  hand-fixed 320×320 to apply 1:1. (Front sprite is final. Wiring is all in place.)

*Risks to flag before acting (don't just barrel in):*
- **Eden trainer slots** — only 6 of 9 spare; Eden is fought 5×, and 3-way
  branching would need 15. Flag before mass-creating Eden trainers.
- **PellucaFishery** is still `MUS_SLATEPORT` (left deliberately; switch only if it
  clashes with the valley theme).
- **Bible amendment tags** (`[AMENDED …]` / `[LOCKED …]`) are un-versioned on
  purpose — I stamp versions, so leave them alone.

*After Chapter 1 polish, the tileset track (handoff §4):* the 3 shared buildings
into the Evernahn PRIMARY tileset (slot 5 is the LAST free palette slot — measure
combined colour count before converting), then the Pelluca SECONDARY tileset, then
the 80×60 map repaint from the committed blueprint.

Start by doing steps 1–4, then give me a short read-back of the current repo state
and what you understand the open Chapter-1 items to be. Don't change anything until
we've agreed on the plan.
