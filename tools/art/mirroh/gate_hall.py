"""Mirroh's gatehouse hallways (the south gate's and the north-west gate's interior maps), mock.

The user's direction (2026-11-21): you go in at the gate, pass down a short hallway with guards, and come out on
the far side; study MonoMyth's North Edelweiss gate, Crown's pass-through buildings and Ghost Grey's Saffron gates.
Layout: North Edelweiss's gate hallway (MonoMyth, group 6 map 20): a long hall, a dark doorway at its top, a runner
up its middle, guard desks facing each other across it, benches and plants along the walls, the mat at its foot.
Mirroh's: cold stone instead of its warm wood and tile (Elderflower's stone and paving), the runner crimson, gloomier.
Guards (marked) stand behind the desks.
Usage: python3 tools/art/mirroh/gate_hall.py [outdir]
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mirroh_v3 as v3
from mirroh_mock import gloom

REF = '/home/claude/scratch/mirroh/ref'
NE = np.load(f'{REF}/mm_ne_gate.npz')
ROWS = [0, 1, 2, 3, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]   # (its first benches dropped: shorter)
CARPET = {0x1e0, 0x1e1, 0x1e2, 0x1e8, 0x1e9, 0x1ea, 0x1f0, 0x1f1, 0x1f2, 0x1cb, 0x1cc, 0x1cd}

def crimson(img):
    f = img.astype(float); l = v3._lum(f) / 255.0
    lo, hi = np.array([46, 10, 20]), np.array([150, 36, 46])
    return (lo + (hi - lo) * np.clip((l - 0.35) / 0.6, 0, 1)[..., None]).astype(np.uint8)

_FLOOR = {tuple(p) for p in np.unique(NE['full'][0x1ad].reshape(-1, 3), axis=0)}
_PAVE = v3.ef(0x275)
def tile(m):
    """An NE hallway piece in Mirroh's stone: its warm floor Elderflower's dark paving (pixel for pixel), its runner
    crimson, the rest restoned."""
    img = NE['full'][m]
    fl = np.array([[tuple(p) in _FLOOR for p in row] for row in img])
    if m in CARPET:
        f = img.astype(int); warm = (f[..., 0] - f[..., 2] > 60) & (f[..., 0] > 150) if m < 0x1cb or m > 0x1cd else (f[..., 0] - f[..., 2] > 30)
        out = v3.to_ef(img); out[warm] = crimson(img)[warm]; out[fl & ~warm] = _PAVE[fl & ~warm]; return out
    out = v3.to_ef(img); out[fl] = _PAVE[fl]
    f = img.astype(int); wood = (f[..., 0] - f[..., 2] > 40) & ~fl
    out[wood] = gloom(img, 0.45, (30, 24, 30), keep_snow=False)[wood]
    return out

def hall():
    c = NE['cells']
    rows = []
    for y in ROWS:
        rows.append([tile(int(c[y, x])) for x in range(1, 11)])
    # every warm floor left (its shaded rows): the paving, pixel for pixel
    for row in rows:
        for t in row:
            f = t.astype(int); l = v3._lum(f.astype(float))
            warm = (f[..., 0] - f[..., 2] > 18) & (f[..., 0] - f[..., 2] < 90) & (l > 95) & (f[..., 0] < 235)
            t[warm] = _PAVE[warm]
    return rows

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    rows = hall()
    img = np.vstack([np.hstack(r) for r in rows])
    im = Image.fromarray(img).resize((img.shape[1] * 3, img.shape[0] * 3), 0)
    d = ImageDraw.Draw(im)
    S = 48
    for (x, y), t in (((0, 6), 'guard'), ((9, 6), 'guard')):
        cx, cy = x * S + S // 2, y * S + S // 2
        d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], outline=(255, 220, 90), width=3); d.text((cx - 14, cy + 14), t, fill=(255, 220, 90))
    im.save(os.path.join(outdir, 'mirroh_gate_hall.png'))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/mirroh/hall')
