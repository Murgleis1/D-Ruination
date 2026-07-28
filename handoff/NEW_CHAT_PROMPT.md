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

**The most urgent open item** is a reproducible intro hang documented in
FINDINGS.md — the game never reaches player control, stalling in
`DR_Lab_Briefing` at PellucaUmbraLab (lab-stage var stuck at 1). It reproduces in
the stable-retro mGBA core; **I need to confirm whether it also hangs in my own
mGBA before you treat it as a real script bug** — ask me. After that, the tileset
work continues per handoff §4 (shared buildings into the Evernahn PRIMARY tileset,
then the Pelluca SECONDARY tileset, then the 80×60 map repaint).

Start by doing steps 1–4, then give me a short read-back of the current repo state
and what you understand the next task to be. Don't start changing things until
we've agreed on the plan.
