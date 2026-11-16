#!/usr/bin/env python3
"""
build_portraits.py — Dreamstone Ruination portrait asset pipeline.

Converts the RGBA portrait masters (96x96) into GBA-ready 16-color indexed PNGs:
  - palette index 0 is reserved as the transparent color (sprite/OBJ transparency),
  - indices 1..15 hold up to 15 opaque bust colors (median-cut quantized),
  - originally-transparent pixels (alpha < 128) map to index 0.

Layout: the engine renders each 96x96 portrait as a 3x3 grid of 32x32 OAM
subsprites, so the .4bpp is built with `-mwidth 4 -mheight 4` (see
spritesheet_rules.mk) — the quantization step here is independent of that tiling.

Usage:
    python3 tools/portraits/build_portraits.py            # convert all masters
    python3 tools/portraits/build_portraits.py --check    # verify outputs only

Masters live in graphics/portraits/_src/*.png (RGBA, hand-editable).
Build inputs written to  graphics/portraits/*.png        (indexed, gbagfx-fed).
On first run, any RGBA PNGs still sitting directly in graphics/portraits/ are
moved into _src/ automatically.
"""
import os
import sys
import glob
import shutil

from PIL import Image

PORTRAIT_DIR = os.path.join("graphics", "portraits")
SRC_DIR = os.path.join(PORTRAIT_DIR, "_src")
EXPECT_W, EXPECT_H = 96, 96     # source master size
OUT_W, OUT_H = 64, 64           # output sprite (48x48 bust centred in 64x64)
MAX_OPAQUE_COLORS = 15          # 16 total minus index 0 (transparent)
ALPHA_CUTOFF = 128
SENTINEL = (255, 0, 255)        # index-0 fill (magenta); hardware-transparent for OBJ


def migrate_masters_into_src():
    """Move any RGBA PNGs left in graphics/portraits/ into _src/ as masters."""
    os.makedirs(SRC_DIR, exist_ok=True)
    for path in sorted(glob.glob(os.path.join(PORTRAIT_DIR, "*.png"))):
        name = os.path.basename(path)
        try:
            mode = Image.open(path).mode
        except Exception:
            continue
        # Only pull true-color masters back to _src; leave already-indexed outputs.
        if mode in ("RGBA", "RGB") and not os.path.exists(os.path.join(SRC_DIR, name)):
            shutil.move(path, os.path.join(SRC_DIR, name))
            print(f"  master -> _src/{name}")


def quantize(src_path, dst_path):
    im = Image.open(src_path).convert("RGBA")
    if im.size != (EXPECT_W, EXPECT_H):
        raise SystemExit(f"{src_path}: expected {EXPECT_W}x{EXPECT_H}, got {im.size[0]}x{im.size[1]}")

    # Dreamstone Ruination: render a smaller, sharper bust. Downscale the 96x96
    # master to 48x48 (LANCZOS resample smooths the pixelation) and centre it in
    # a 64x64 transparent canvas. The engine then draws it as a 2x2 grid of
    # 32x32 subsprites, so the visible art is ~50% smaller on screen. The 8px
    # transparent margin becomes index-0 (hardware-transparent).
    small = im.resize((48, 48), Image.LANCZOS)
    im = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    im.paste(small, (8, 8))

    rgb = list(im.convert("RGB").getdata())
    alpha = list(im.getchannel("A").getdata())
    opaque = [c for c, a in zip(rgb, alpha) if a >= ALPHA_CUTOFF]
    if not opaque:
        raise SystemExit(f"{src_path}: fully transparent image")

    # Fill transparent pixels with the most common opaque color so the 15-color
    # budget is spent only on the visible bust, not on transparent-region colors.
    fill = max(set(opaque), key=opaque.count)
    masked = [c if a >= ALPHA_CUTOFF else fill for c, a in zip(rgb, alpha)]

    tmp = Image.new("RGB", im.size)
    tmp.putdata(masked)
    q = tmp.quantize(colors=MAX_OPAQUE_COLORS, method=Image.MEDIANCUT, dither=Image.NONE)
    q_idx = list(q.getdata())                       # 0..14
    q_pal = q.getpalette()[: MAX_OPAQUE_COLORS * 3]  # 15 RGB triples

    # index 0 = transparent sentinel; opaque pixels shift into 1..15.
    out_idx = [(qi + 1) if a >= ALPHA_CUTOFF else 0 for qi, a in zip(q_idx, alpha)]
    palette = list(SENTINEL) + q_pal
    palette += [0, 0, 0] * (16 - len(palette) // 3)  # pad to exactly 16 entries

    out = Image.new("P", im.size)
    out.putpalette(palette)
    out.putdata(out_idx)
    out.save(dst_path)
    used = len(set(out_idx))
    return used


def check(dst_path):
    im = Image.open(dst_path)
    if im.mode != "P":
        return f"{dst_path}: not indexed (mode={im.mode})"
    if im.size != (OUT_W, OUT_H):
        return f"{dst_path}: wrong size {im.size}"
    idx = set(im.getdata())
    if max(idx) > 15:
        return f"{dst_path}: index {max(idx)} > 15 (more than 16 colors)"
    return None


def main():
    check_only = "--check" in sys.argv
    if not os.path.isdir(PORTRAIT_DIR):
        raise SystemExit("run from the codebase root (graphics/portraits not found)")

    if not check_only:
        migrate_masters_into_src()

    masters = sorted(glob.glob(os.path.join(SRC_DIR, "*.png")))
    if not masters:
        raise SystemExit("no masters in graphics/portraits/_src/")

    print(f"{'portrait':26s} {'result'}")
    ok = True
    for m in masters:
        name = os.path.basename(m)
        dst = os.path.join(PORTRAIT_DIR, name)
        if not check_only:
            used = quantize(m, dst)
            note = f"OK  ({used} colors incl. transparent)"
        else:
            note = "checked"
        err = check(dst)
        if err:
            ok = False
            note = "FAIL: " + err
        print(f"  {name:24s} {note}")
    if not ok:
        raise SystemExit("one or more portraits failed validation")
    print(f"\n{len(masters)} portraits ready in {PORTRAIT_DIR}/ (masters in {SRC_DIR}/)")


if __name__ == "__main__":
    main()
