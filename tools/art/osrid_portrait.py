"""Osrid's portrait, redesigned in MonoMyth's style on KAKUGO's portrait (MonoMyth #69/#70) so it
matches his new Kakugo-based overworld sprite (user 2026-11-16: "redesign Osrid's portrait sprite to
be in alignment with MonoMyth's style"; "Kakugo's sprite is meant to be the new base for Osrid").

Kakugo's drawing, Osrid's identity (regions measured on #69):
  * spiked helmet (rows above the visor, brown ramp 2-5 + gold 7) -> his spiky red-orange hair
  * visor band (black 1, rows ~40-50) + ruby goggles + lower face plate -> ONE cream mask
    (new ramp in the freed ruby slots 8/9/11); the ruby eyes -> the mask's black eye holes
  * white scarf (10 / 15)                                         -> his dark green scarf
  * dark coat (6, 13, 14) and the outline (12)                     -> kept
Run: python3 -I osrid_portrait.py MONOMYTH_ROM OUT_DIR
"""
import os, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '../monomyth'))
import mm_portraits as mp

HAIR = {2: (92, 28, 16), 3: (160, 62, 28), 4: (204, 92, 38), 5: (124, 44, 22), 7: (236, 132, 60)}
MASK_PAL = {8: (172, 146, 108), 9: (222, 206, 168), 11: (242, 230, 200)}
SCARF = {10: (72, 106, 76), 15: (46, 70, 52)}
RUBY = (8, 9, 11)


def build(px, pal):
    px = px.copy(); pal = pal.copy().astype(int)
    H, W = px.shape
    # visor top = first row where the black band (1) spans >= 8 px between x 8..48
    band_rows = [y for y in range(H) if (px[y, 8:48] == 1).sum() >= 8]
    vtop = band_rows[0]
    face = np.zeros_like(px, bool)
    # per column, the mask starts where the visor band (1) first appears at/below the visor top --
    # the helmet above it stays hair, so there is no straight seam across the hair
    for x in range(6, 50):
        col = np.nonzero(px[vtop - 2:min(vtop + 14, H), x] == 1)[0]
        if len(col): face[vtop - 2 + col[0]:min(vtop + 26, H), x] = True
    face &= np.isin(px, (1, 2, 3, 4, 5, 7) + RUBY)
    # the black band's outer edge stays as the mask's outline: band pixels touching outside stay 1
    edge = np.zeros_like(face)
    for y in range(H):
        for x in range(W):
            if face[y, x] and px[y, x] == 1:
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < H and 0 <= xx < W and px[yy, xx] in (0, 12, 6, 13, 14, 10, 15): edge[y, x] = True
    ruby = face & np.isin(px, RUBY)
    out = px.copy()
    lum = {i: int(pal[i].sum()) for i in range(16)}
    for y in range(H):
        for x in range(W):
            if not face[y, x] or edge[y, x]: continue
            v = px[y, x]
            if ruby[y, x]: out[y, x] = 1                              # eye holes
            elif v == 1: out[y, x] = 9                                # visor band -> mask
            else: out[y, x] = 8 if lum[v] < 330 else (9 if lum[v] < 470 else 11)
    for i, c in {**HAIR, **MASK_PAL, **SCARF}.items(): pal[i] = c
    return out, pal.astype(np.uint8)


if __name__ == '__main__':
    rom, od = sys.argv[1], sys.argv[2]; os.makedirs(od, exist_ok=True)
    P = mp.load(rom)
    for name, i in (('osrid', 69), ('osrid_alt', 70)):
        _, px, pal = P[i]; o, p2 = build(px, pal); mp.save_indexed(o, p2, os.path.join(od, name + '.png'))
