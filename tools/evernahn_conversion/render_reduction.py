#!/usr/bin/env python3
"""Render source-vs-reduced comparison sheets for the Evernahn building art."""
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, str(Path(__file__).resolve().parent))
from reduce_palette import SETS, run  # noqa: E402


def composite(block, bg=(32, 32, 38)):
    """Flatten RGBA onto a neutral background so alpha reads correctly."""
    rgb = block[:, :, :3].astype(int)
    a = (block[:, :, 3:4] > 128).astype(int)
    return (rgb * a + np.array(bg) * (1 - a)).astype(np.uint8)


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/reduction.png")
    only = sys.argv[2] if len(sys.argv) > 2 else None
    names = [only] if only else list(SETS)

    S = 3
    pad, top, gap = 20, 66, 40
    rows = []
    for n in names:
        blk, red, pal, orig, err = run(n, 15)
        rows.append((n, blk, red, pal, orig, err))

    wmax = max(r[1].shape[1] for r in rows) * S
    hsum = sum(r[1].shape[0] * S + gap + 34 for r in rows)
    cv = Image.new("RGB", (pad * 3 + wmax * 2, top + hsum), (26, 26, 30))
    dr = ImageDraw.Draw(cv)
    dr.text((pad, 14), "Evernahn source art reduced to GBA-native 15-colour palettes",
            fill=(240, 240, 240))
    dr.text((pad, 32), "LEFT: source        RIGHT: 15 colours, no dithering",
            fill=(165, 165, 175))
    dr.text((pad, 48), "Perceptual clustering, dark/light anchors pinned, "
                       "centroids snapped to real source colours.", fill=(165, 165, 175))

    y = top
    for n, blk, red, pal, orig, err in rows:
        h, w = blk.shape[0] * S, blk.shape[1] * S
        for i, b in enumerate((blk, red)):
            img = Image.fromarray(composite(b)).resize((w, h), Image.NEAREST)
            cv.paste(img, (pad + i * (wmax + pad), y))
        dr.text((pad, y + h + 8), f"{n}   {orig} -> {len(pal)} colours   "
                                  f"mean error {err:.2f}/255", fill=(210, 210, 220))
        # palette strip
        for j, c in enumerate(pal):
            dr.rectangle([pad + wmax + pad + j * 18, y + h + 24,
                          pad + wmax + pad + j * 18 + 16, y + h + 38],
                         fill=tuple(int(v) for v in c), outline=(90, 90, 95))
        y += h + gap + 34

    cv.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
