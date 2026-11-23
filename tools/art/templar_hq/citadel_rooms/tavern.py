"""The Citadel's Tavern (user 2026-11-23: Pelluca's Tavern room in the Citadel's colours, with the core staff).
Source: Pelluca's Seaside Tavern as built (PellucaCityPokemonCenter; MonoMyth's Elderflower tavern), as Mirroh's is.
Recolour: the floor planks to the cathedral's cream stone tones (everywhere but the walls, the hearth and the
counter), the furniture and walls to the courtyard houses' dark grey wood (citadel_mock.grey_wood), the hearth's brick
and fire kept warm, the exit mat in the Order's blue and gold. Returns (picture, solid, exits)."""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); TQ = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(TQ, '..', 'mirroh')); sys.path.insert(0, TQ)
FLOOR = {(136, 96, 56): (208, 200, 180), (112, 72, 48): (182, 172, 146), (104, 64, 40): (166, 156, 130),
         (72, 48, 32): (140, 132, 110), (56, 40, 32): (112, 104, 86), (96, 64, 40): (160, 150, 124), (128, 80, 56): (176, 166, 140)}

def room():
    import interiors as I, citadel_mock as CM
    img, solid = I.SOURCES['tavern']()
    H, W = solid.shape
    keep = {(x, y) for y in (0, 1) for x in range(W)} | {(x, y) for x in (4, 5, 6) for y in (1, 2)} | {(x, 4) for x in range(W)}
    a = img.astype(int); out = CM.grey_wood(img).astype(int)
    for y in range(H):
        for x in range(W):
            if (x, y) in keep: continue
            s = (slice(y * 16, y * 16 + 16), slice(x * 16, x * 16 + 16)); blk = a[s]; o = out[s]
            for src, dst in FLOOR.items(): o[(blk == src).all(-1)] = dst
    for x0 in (16, 176):                                          # (the two tables' tops stay grey wood, not floor)
        ts = (slice(112, 141), slice(x0, x0 + 32)); out[ts] = CM.grey_wood(img[ts].astype(np.uint8)).astype(int)
    hs = (slice(16, 48), slice(64, 112))                          # (the hearth, x 4-6 rows 1-2: brick and fire kept)
    out[hs] = np.where((a[hs].sum(-1) == 0)[..., None], out[hs], a[hs])
    # the mat (row 10, x 6-7): the Order's blue and gold
    ms = (slice(10 * 16, 11 * 16), slice(6 * 16, 8 * 16)); m = out[ms]
    L = .3 * m[..., 0] + .59 * m[..., 1] + .11 * m[..., 2]
    grey = (np.abs(m[..., 0] - m[..., 2]) < 24) & (L > 60)
    m[grey & (L > 150)] = (177, 149, 48); m[grey & (L <= 150)] = (36, 74, 155)
    return out.astype(np.uint8), solid, [(6, 10), (7, 10)]

if __name__ == '__main__':
    from PIL import Image
    img, solid, ex = room(); H, W = solid.shape
    Image.fromarray(img).resize((W * 32, H * 32), Image.NEAREST).save(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/tavern_v1.png')
