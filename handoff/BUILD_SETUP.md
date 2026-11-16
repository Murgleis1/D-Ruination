# Building the ROM in a fresh container

**Short version: you do NOT need devkitPro.** pokeemerald's `make modern` uses
the plain `arm-none-eabi-*` toolchain from `PATH`, which installs from the normal
Ubuntu archive (which IS in the network allowlist). A verified-working build was
produced this way with `DEVKITARM` and `DEVKITPRO` both empty.

The Makefile states this itself (around line 37):

```make
TOOLCHAIN := $(DEVKITARM)
# don't use dkP's base_tools anymore
# ... or use arm-none-eabi binaries on the system
# if dkP is not installed on this system
ifneq (,$(TOOLCHAIN))
  ifneq ($(wildcard $(TOOLCHAIN)/bin),)
    export PATH := $(TOOLCHAIN)/bin:$(PATH)
  endif
endif
PREFIX := arm-none-eabi-
```

If `DEVKITARM` is empty the whole block is skipped and it falls through to
`arm-none-eabi-` on `PATH`. **A failed devkitPro fetch is not a blocker.**

---

## 1. ARM toolchain (from apt — `archive.ubuntu.com` is allowlisted)

```bash
sudo apt-get update
sudo apt-get install -y binutils-arm-none-eabi gcc-arm-none-eabi libnewlib-arm-none-eabi
arm-none-eabi-gcc --version     # verify
```

Known-good versions in the working environment:

| package | version |
|---|---|
| `gcc-arm-none-eabi` | 15:13.2.rel1-2 (gcc 13.2.1) |
| `binutils-arm-none-eabi` | 2.42-1ubuntu1+23 |
| `libnewlib-arm-none-eabi` | 4.4.0.20231231-2 |

Host arch is **x86_64** — so any committed macOS/arm64 binary in the repo is
unusable here and must be replaced (see §3).

## 2. Host tools (C programs that run on the build machine)

Build deps — all present in the working environment:

```bash
sudo apt-get install -y build-essential libpng-dev zlib1g-dev pkg-config
```

The host tools live in `codebase/tools/*/` and are **built automatically by
`make modern`**; no separate step is required. To force them:

```bash
cd codebase && make tools
```

They must end up as **x86-64 ELF** binaries:
`gbagfx scaninc preproc bin2c rsfont aif2pcm mid2agb jsonproc mapjson trainerproc`

Verify: `file tools/gbagfx/gbagfx` → `ELF 64-bit LSB ... x86-64`

**`agbcc` is NOT needed** — that's only for the non-modern (`make`) target. We
build `make modern`, which uses `arm-none-eabi-gcc` directly.

## 3. poryscript — the one binary that needs replacing

`codebase/tools/poryscript/poryscript` is **committed as a macOS arm64 Mach-O**
(that's the copy the repo owner uses on their own machine). It will not run on an
x86-64 Linux host. Fetch the Linux build instead — `github.com` and
`release-assets.githubusercontent.com` are allowlisted:

```bash
cd /tmp && rm -rf poryx && mkdir poryx && cd poryx
curl -sL -o poryscript.zip \
  https://github.com/huderlem/poryscript/releases/download/3.6.1/poryscript-linux.zip
unzip -q poryscript.zip            # extracts into a poryscript-linux/ SUBDIR
cp poryscript-linux/poryscript /home/claude/repo/codebase/tools/poryscript/poryscript
chmod +x /home/claude/repo/codebase/tools/poryscript/poryscript
/home/claude/repo/codebase/tools/poryscript/poryscript -v    # expect 3.6.1
```

**CRITICAL — never commit this replacement.** Committing the Linux ELF would break
the repo owner's macOS build. Every commit must exclude it:

```bash
git add -A && git reset -q HEAD codebase/tools/poryscript/poryscript
```

Also note `git stash` will swallow it (it shows as a modified tracked file), so
re-copy it from `/tmp/poryx/` if it reverts to Mach-O. Check with:
`file codebase/tools/poryscript/poryscript`

## 4. Build

```bash
cd /home/claude/repo/codebase
timeout 290 make modern > /tmp/build.log 2>&1; echo "EXIT=$?"
```

- **exit 124** = still compiling (the container is 1-core, a full build is ~5 min)
  → just run the same command again; make resumes.
- **exit 0** = done → `pokeemerald.gba` (33,554,432 bytes).
- **exit 2** = error → `grep -iE "error" /tmp/build.log | head`.

Show the user the result:

```bash
cp pokeemerald.gba /home/claude/Dreamstone_Ruination.gba
# then call present_files on that path
```

## 5. Verified working state (captured from a successful build)

```
host:            x86_64 Ubuntu 24
DEVKITARM:       (empty)      DEVKITPRO: (empty)
arm-none-eabi-gcc 13.2.1 at /usr/bin/arm-none-eabi-gcc  (apt, not devkitPro)
host tools:      all 10 built as x86-64 ELF
poryscript:      3.6.1 Linux x86-64 (statically linked Go), NOT the committed Mach-O
make modern:     EXIT=0, pokeemerald.gba 33554432 bytes, ROM ~87% full
```

## 6. Network allowlist (relevant entries)

`archive.ubuntu.com`, `security.ubuntu.com` (apt) · `github.com`,
`codeload.github.com`, `raw.githubusercontent.com`,
`release-assets.githubusercontent.com` (poryscript, sources) · `pypi.org`,
`files.pythonhosted.org` (Python) · `registry.npmjs.org`, `crates.io`.

devkitPro's own domain is **not** allowlisted — which is fine, because it isn't needed.

## 7. Fresh clone fails on sprite sheets (found 2026-11-15)

`spritesheet_rules.mk` asks for `-mwidth 12 -mheight 12` on 32px-tall sheets
(brendan/acro_bike 864x32, mach_bike 288x32, every custom character). gbagfx
cannot convert them, so this fork has ALWAYS built from the committed `.4bpp`.
A fresh clone gives files arbitrary mtimes and make tries to regenerate them:
`The height in tiles (4) isn't a multiple of the specified metatile height (12)`.

Container-only fix, changes nothing in the repo: touch every tracked `.4bpp`
whose `.png` has no later commit (on 2026-11-15 that was all 9,918; none stale):

```bash
cd codebase && git ls-files '*.4bpp' | while read f; do p="${f%.4bpp}.png";
  [ -f "$p" ] && [ "$(git log -1 --format=%ct -- "$p")" -le "$(git log -1 --format=%ct -- "$f")" ] && echo "$f";
done | xargs touch
```
Recheck the "png newer" case before touching if sprite art changed recently.

## 8. TRIPLE-LAYER METATILES (since d18a04803, 2026-11-15) -- READ BEFORE PORYMAP

Ruination now uses **triple-layer metatiles**: 12 entries (24 bytes) each --
bottom -> BG3, middle -> BG2, top -> BG1 (over sprites), drawn regardless of
layer type. Format reference: `tools/metatile_format.py`.

**Porymap MUST be switched to triple-layer before opening the project.**
`porymap.project.cfg` is gitignored (local only), so set it on each machine:
`enable_triple_layer_metatiles=1` (Options -> Project Settings -> "Enable
Triple Layer Metatiles"). Check: the Tileset Editor shows THREE layers per
metatile. A 2-layer Porymap misreads every tileset, and SAVING a tileset in that
state corrupts metatiles.bin.

- Converted with `tools/triple_layer/convert_metatiles.py` (idempotent; asserts
  each BG gets the same tile as before). 165/165 frames of a deterministic run
  were pixel-identical old vs new ROM.
- NORMAL metatiles keep tile 0x3014 in their bottom layer: the old engine always
  drew it there and 1,575 metatiles show it through transparent pixels. Porymap
  will now display it too -- that is what the game draws.
- Layer type is still used by gameplay code (shop object occlusion, decoration
  placement checks); it no longer chooses BG layers.
- gTileset_DrBlackReflection has its own `metatiles_drblack.bin` (it overrides
  metatile 161's layering for the reflection scene).
- NOT verified on screen: the shop buy-menu map preview and secret-base
  decorations (verified by code review only; the test run never opens them).
- 2-layer scripts in tools/evernahn_conversion/ now refuse to run (hard stop),
  except gba_viewport.py, which is ported to 24-byte metatiles.
