#!/usr/bin/env python3
"""
Render the dex screens from the REAL committed tilemaps under the current
palette and under the proposed re-tint, side by side, for the user to eyeball.

This is a PREVIEW of the background layers only -- text windows and sprites are
drawn at runtime and are not composited here. It is not a screenshot; it is an
exact render of the BG layers, which is what the palette change affects.

Usage: python3 tools/pokelog_palette/render_preview.py OUT.png
"""
import struct
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from retint_pokelog import MAP  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
DEX = REPO / "codebase" / "graphics" / "pokedex"
SCALE = 3

# screen, palette file, list of (bgTilemap, isOverlay) bottom-first
SCREENS = [
    ("Main list", "bg_hoenn", [("list_underlay.bin", False), ("list.bin", True)]),
    ("Entry page", "bg_hoenn", [("info_screen.bin", False)]),
    ("Search results", "search_results_bg", [("list_underlay.bin", False),
                                             ("list.bin", True)]),
]


def load_tiles():
    a = np.array(Image.open(DEX / "menu.png"))
    tw, th = a.shape[1] // 8, a.shape[0] // 8
    return [a[y * 8:y * 8 + 8, x * 8:x * 8 + 8]
            for y in range(th) for x in range(tw)]


def load_pal(name):
    d = (DEX / f"{name}.gbapal").read_bytes()
    out = []
    for i in range(len(d) // 2):
        v = struct.unpack_from("<H", d, i * 2)[0]
        out.append((v & 31, (v >> 5) & 31, (v >> 10) & 31))
    return out


def render(tiles, maps, W=32, H=20):
    P = np.zeros((H * 8, W * 8), np.int16)
    C = np.zeros((H * 8, W * 8), np.int16)
    for fn, overlay in maps:
        d = (DEX / fn).read_bytes()
        ents = [struct.unpack_from("<H", d, i)[0] for i in range(0, len(d), 2)]
        for i, v in enumerate(ents[:W * H]):
            tid, hf, vf, pal = v & 0x3FF, (v >> 10) & 1, (v >> 11) & 1, (v >> 12) & 0xF
            if tid >= len(tiles):
                continue
            t = tiles[tid]
            if hf:
                t = t[:, ::-1]
            if vf:
                t = t[::-1, :]
            y, x = (i // W) * 8, (i % W) * 8
            if overlay:
                m = t > 0                      # colour 0 is transparent
                blk_p, blk_c = P[y:y + 8, x:x + 8], C[y:y + 8, x:x + 8]
                blk_p[m], blk_c[m] = pal, t[m]
            else:
                P[y:y + 8, x:x + 8] = pal
                C[y:y + 8, x:x + 8] = t
    return P, C


def colourise(P, C, pal):
    out = np.zeros(P.shape + (3,), np.uint8)
    for p in range(6):
        for i in range(16):
            r, g, b = pal[p * 16 + i]
            out[(P == p) & (C == i)] = (r << 3, g << 3, b << 3)
    return out[:160, :240]


def main():
    dest = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/tmp/pokelog_preview.png")
    tiles = load_tiles()
    W, H = 240 * SCALE, 160 * SCALE
    pad, top = 24, 56
    canvas = Image.new("RGB", (pad + (W + pad) * 2, top + (H + 46) * len(SCREENS)),
                       (26, 26, 30))
    from PIL import ImageDraw
    dr = ImageDraw.Draw(canvas)
    dr.text((pad, 16), "PokeLog parchment re-tint  -  BG layers rendered from the "
                       "committed tilemaps (no text/sprites)", fill=(240, 240, 240))
    dr.text((pad, 34), "LEFT: current          RIGHT: proposed", fill=(170, 170, 180))

    for row, (label, palname, maps) in enumerate(SCREENS):
        P, C = render(tiles, maps)
        old = load_pal(palname)
        new = [MAP.get(c, c) for c in old]
        y = top + row * (H + 46)
        for col, pal in enumerate((old, new)):
            img = Image.fromarray(colourise(P, C, pal)).resize((W, H), Image.NEAREST)
            canvas.paste(img, (pad + col * (W + pad), y))
        dr.text((pad, y + H + 8), f"{label}  ({palname})", fill=(210, 210, 220))

    canvas.save(dest)
    print("wrote", dest)


if __name__ == "__main__":
    main()
