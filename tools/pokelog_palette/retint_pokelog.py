#!/usr/bin/env python3
"""
PokeLog parchment re-tint  --  value-keyed, luminance-preserving.

WHY THIS EXISTS
---------------
The first parchment pass re-tinted the dex background ramp "at matching
luminance". Measurement showed that is exactly what stops it reading as paper:

    reference (Johto Legends, PREDEFPAL_BETA_POKEGEAR)  page field  lum 209  sat 148
    ours before                            (#FFFFDE)    page field  lum 251  sat  33

Near-white with a faint cream tint reads as a normal white dex screen. Parchment
needs luminance DROPPED and saturation RAISED into the yellow-orange band.

Worse, the first pass only touched the cream ramp (indices 1-6) and left the
vanilla GREEN chrome (indices 10/12/13) untouched. Measured pixel coverage of
the real tilemaps proves that is what dominates:

    MAIN LIST SCREEN   #EFF73A 30.7%   #FFFFDE 17.6%   #31D64A 14.2%   #198421 14.2%
    INFO/ENTRY SCREEN  #FFFFDE 60.1% (pal0+1+3)        #F7E6BD 23.6%

So ~59% of the list screen was still green. That is why the effect never landed.

WHY VALUE-KEYED, NOT INDEX-KEYED
--------------------------------
The six sub-palettes reuse the same indices for different roles: idx2 is the
parchment ramp in pal0 but a RED accent (#C52121) in pal1/2/4/5; idx12/13 are
green in pal0/1/3 but BLUE (#B5CEF7/#318CFF) in pal2/5 and red/teal in pal4.
A blanket per-index transform would destroy the UI's colour coding. Mapping by
VALUE touches only the greys/creams/greens and provably cannot hit an accent.

TRANSFORM RULE
--------------
Every mapping below preserves the source colour's LUMINANCE (so every contrast
relationship in the UI survives) and moves only hue/saturation into the warm
band -- except the page field and its ramp, which are deliberately DARKENED to
the reference's measured luminance, because that is the whole point.

The chrome is then re-anchored BELOW the new page field (163 vs 204) to keep the
original figure/ground order: the chrome was 34 lum darker than the field before,
and merging them would flatten the screen. Reads as leather cover / paper inserts.

    role            before                  after
    page field      #FFFFDE lum 251  ->  (31,25,14) lum 204
    ramp 2          #F7E6BD lum 230  ->  (29,22,12) lum 184
    ramp 3          #D6BD9C lum 193  ->  (25,19,11) lum 159
    ramp 4          #B5A58C lum 167  ->  (21,16,10) lum 134
    ramp 5          #736352 lum 102  ->  (14,11, 7) lum  92
    ramp 6          #3A3A29 lum  56  ->  ( 8, 6, 4) lum  51
    chrome hi       #EFF73A lum 217  ->  (26,20, 8) lum 163
    chrome mid      #31D64A lum 145  ->  (24,17, 9) lum 145   (preserved)
    chrome dark     #198421 lum  86  ->  (15,10, 5) lum  88   (preserved)
    natl green mid  #7BA573 lum 143  ->  (24,17, 9) lum 145   (preserved)
    natl green dark #4A7342 lum  95  ->  (16,11, 6) lum  96   (preserved)

DELIBERATELY UNTOUCHED
----------------------
  #C52121 #BD0000            red accents
  #B5CEF7 #318CFF #4A94B5 #085A84  blue/teal accents (blue ink on parchment is
                                   period-correct, so these are left alone)
  #FFEF00 #FFBD00 #FF7300    pal3 gradient, already warm
  #293A6B #000029 #000000    ink
  #FF00BD                    transparency marker
  #BD9C5A                    already tan
  #7B8400                    sub-palette entry 0; never loaded
                             (src/pokedex.c LoadPokedexBgPalette starts at +1)

NOTE ON FILE FORMAT
-------------------
Makefile:346 is `%.gbapal: %.pal`, so the JASC .pal is the SOURCE OF TRUTH and
the .gbapal is regenerated from it at build time. Editing only the .gbapal is
silently overwritten. Both are tracked here, so this tool writes both and the
build then confirms by regenerating the .gbapal byte-identically.

JASC .pal stores 8-bit channels as (rgb15 << 3) -- 31 -> 248, NOT 255. gbagfx
converts back with >>3. The files use CRLF; that is preserved.

Usage:  python3 tools/pokelog_palette/retint_pokelog.py [--check]
        --check  report what would change, write nothing
"""
import struct
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEX = REPO / "codebase" / "graphics" / "pokedex"
TARGETS = ["bg_hoenn", "bg_national", "search_results_bg"]

# source rgb15 -> target rgb15
MAP = {
    (31, 31, 27): (31, 25, 14),   # page field
    (30, 28, 23): (29, 22, 12),   # ramp 2
    (26, 23, 19): (25, 19, 11),   # ramp 3
    (22, 20, 17): (21, 16, 10),   # ramp 4
    (14, 12, 10): (14, 11, 7),    # ramp 5
    (7, 7, 5):    (8, 6, 4),      # ramp 6
    (29, 30, 7):  (26, 20, 8),    # chrome hi   (green-yellow -> tanned leather)
    (6, 26, 9):   (24, 17, 9),    # chrome mid  (green -> oak)
    (3, 16, 4):   (15, 10, 5),    # chrome dark (green -> dark oak)
    (15, 20, 14): (24, 17, 9),    # national green mid
    (9, 14, 8):   (16, 11, 6),    # national green dark

    # search_results_bg.pal was never touched by the first pass -- it is still
    # fully vanilla (pure-white field, neutral greys, its own greens). Without
    # these it would end up a WHITE page inside a leather frame.
    (31, 31, 31): (31, 25, 14),   # sr page field (pure white)
    (27, 27, 27): (29, 22, 12),   # sr ramp 2
    (23, 23, 23): (25, 19, 11),   # sr ramp 3
    (20, 20, 20): (21, 16, 10),   # sr ramp 4
    (12, 12, 14): (14, 11, 7),    # sr ramp 5 (blue-grey)
    (5, 7, 8):    (8, 6, 4),      # sr ramp 6 (blue-grey)
    (6, 6, 8):    (7, 6, 4),      # sr dark blue-grey
    (15, 18, 4):  (21, 15, 8),    # sr green mid
    (5, 10, 0):   (10, 7, 3),     # sr green dark
}


def lum15(c):
    r, g, b = (v << 3 for v in c)
    return 0.299 * r + 0.587 * g + 0.114 * b


def read_pal(path):
    raw = path.read_bytes()
    crlf = b"\r\n" in raw
    lines = raw.decode("ascii").replace("\r\n", "\n").rstrip("\n").split("\n")
    header, body = lines[:3], lines[3:]
    cols = []
    for ln in body:
        if not ln.strip():
            continue
        r, g, b = (int(x) for x in ln.split())
        cols.append((r >> 3, g >> 3, b >> 3))
    return header, cols, crlf


def write_pal(path, header, cols, crlf):
    out = list(header) + [f"{r << 3} {g << 3} {b << 3}" for r, g, b in cols]
    text = "\n".join(out) + "\n"
    if crlf:
        text = text.replace("\n", "\r\n")
    path.write_bytes(text.encode("ascii"))


def write_gbapal(path, cols):
    path.write_bytes(b"".join(
        struct.pack("<H", (b << 10) | (g << 5) | r) for r, g, b in cols))


def main():
    check = "--check" in sys.argv
    grand = 0
    for name in TARGETS:
        p_pal = DEX / f"{name}.pal"
        if not p_pal.exists():
            print(f"  SKIP {name}.pal (absent)")
            continue
        header, cols, crlf = read_pal(p_pal)
        changed, new = 0, []
        for c in cols:
            t = MAP.get(c)
            if t is None:
                new.append(c)
            else:
                new.append(t)
                changed += 1
        grand += changed
        print(f"{name}: {changed}/{len(cols)} entries re-tinted")
        for src, dst in MAP.items():
            n = cols.count(src)
            if n:
                print(f"    {n:2d}x  {''.join(f'{v<<3:02X}' for v in src)}"
                      f" lum {lum15(src):5.1f}  ->  "
                      f"{''.join(f'{v<<3:02X}' for v in dst)} lum {lum15(dst):5.1f}")
        if not check:
            write_pal(p_pal, header, new, crlf)
            write_gbapal(DEX / f"{name}.gbapal", new)
            print(f"    wrote {name}.pal + {name}.gbapal")
    print(f"\ntotal entries re-tinted: {grand}")
    # guard: none of the protected accents may appear as a MAP key
    protected = {(24, 4, 4), (23, 0, 0), (22, 25, 30), (6, 17, 31),
                 (9, 18, 22), (1, 11, 16), (31, 29, 0), (31, 23, 0),
                 (31, 14, 0), (5, 7, 13), (0, 0, 5), (0, 0, 0), (31, 0, 23)}
    clash = protected & set(MAP)
    assert not clash, f"transform would hit a protected accent: {clash}"
    print("guard OK: no protected accent is in the transform map")


if __name__ == "__main__":
    main()
