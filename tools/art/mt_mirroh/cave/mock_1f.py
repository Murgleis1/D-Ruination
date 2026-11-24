"""Mt. Mirroh 1F re-tiled (user 2026-11-23): MonoMyth's Glittering Grotto, made icy ("option A: deep ice"), on the
1F layout as built and walked (same collision and elevations). Extra ice and snow where it fits; the Grotto's large
and small crystals re-skinned as chunks of semi-see-through glassy ice, set at key places (user).
  * Rock (R): every wall of the layout and every cell the player cannot reach (the pockets once reached from 2F
    become solid rock). Open (O): every reachable cell. Drawn with the Grotto's own rounded rock masses: each
    cell's tile is learned from the Grotto by its 8-neighbour rock/open pattern (gg.py).
  * Plateau lips (Dreamstone Mysteries' raised edges, and the one-way ledge): the Grotto's ledge line, with frost.
  * Stairs: the Grotto's. Slippery ice (DM's ice floor): clear blue ice. Bridges: DM's planks, cooled.
  * Colours: the Grotto's indigo turned glacier blue; its gems frosted.
Usage: python3 mock_1f.py OUT.png  (also writes OUT's layers for the build: see build_1f_art.py)."""
import os, sys, struct, json, random, colorsys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, HERE)
import gg
C = ROOT + '/codebase'
W = H = 60
cells = list(struct.unpack('<3600H', open(C + '/data/layouts/MirrohInterior_1F/map.bin', 'rb').read()))
def attrs():
    p = open(C + '/data/tilesets/primary/general/metatile_attributes.bin', 'rb').read()
    s = open(C + '/data/tilesets/secondary/cave_alt/metatile_attributes.bin', 'rb').read()
    a = [struct.unpack_from('<H', p, 2 * i)[0] for i in range(len(p) // 2)]; a += [0] * (512 - len(a))
    return a + [struct.unpack_from('<H', s, 2 * i)[0] for i in range(len(s) // 2)]
A = attrs()
mt = lambda x, y: cells[y * W + x] & 0x3FF
col = lambda x, y: (cells[y * W + x] >> 10) & 3
el = lambda x, y: cells[y * W + x] >> 12
beh = lambda x, y: A[mt(x, y)] & 0xFF

def reach(start):
    seen = {start}; q = [start]
    while q:
        x, y = q.pop(); e = el(x, y)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < W and 0 <= ny < H): continue
            if beh(nx, ny) == 0x3B and dy == 1:
                l = (nx, ny + 1)
                if col(*l) == 0 and l not in seen: seen.add(l); q.append(l)
                continue
            if col(nx, ny): continue
            ne = el(nx, ny)
            if not (e in (0, 15) or ne in (0, 15) or ne == e): continue
            if (nx, ny) not in seen: seen.add((nx, ny)); q.append((nx, ny))
    return seen
OPEN = reach((55, 56))
STAIR = {(x, y) for y in range(H) for x in range(W) if mt(x, y) == 0x363}
ICE = {(x, y) for y in range(H) for x in range(W) if beh(x, y) == 0x20}
BRIDGE = {(x, y) for y in range(H) for x in range(W) if 0x393 <= mt(x, y) <= 0x39D}
LEDGE = {(x, y) for y in range(H) for x in range(W) if beh(x, y) == 0x3B}
ROCKS = {(x, y) for y in range(H) for x in range(W) if mt(x, y) in (0x37D, 0x37E) and col(x, y)}
LIPS = {(x, y) for y in range(H) for x in range(W) if mt(x, y) == 0x379 and (x, y) in OPEN
        and y > 0 and (x, y - 1) in OPEN and el(x, y - 1) not in (0, 15) and el(x, y - 1) != el(x, y)}
EXIT_S, EXIT_N = (55, 57), (54, 1)
def cls(x, y):
    if not (0 <= x < W and 0 <= y < H): return 'R'
    p = (x, y)
    if p in LEDGE: return 'R'
    return 'O' if (p in OPEN or p in STAIR or p in BRIDGE or p in ROCKS or p in (EXIT_S, EXIT_N)) else 'R'

# ---- colours: the Grotto's indigo to glacier blue (A: deep ice); bright gems frosted -------------------------------
_cc = {}
def ice(c):
    c = tuple(int(v) for v in c)
    if c in _cc: return _cc[c]
    h, s, v = colorsys.rgb_to_hsv(*(np.array(c) / 255))
    if s > 0.45 and v > 0.6: r = colorsys.hsv_to_rgb(0.55 + 0.05 * np.sin(h * 6.28), min(1, s * 0.5), min(1, v * 1.05))
    else: r = colorsys.hsv_to_rgb(0.585, min(1, s * 0.9 + 0.1), min(1, v * 1.35 + 0.05))
    _cc[c] = tuple(int(round(x * 255)) for x in r); return _cc[c]
_fc = {}
def ice_floor(c):
    """the open floor a step paler than the rock (the Grotto's share colours): packed ice."""
    c = tuple(int(v) for v in c)
    if c in _fc: return _fc[c]
    h, s, v = colorsys.hsv_to_rgb(*(0, 0, 0)) if False else colorsys.rgb_to_hsv(*(np.array(c) / 255))
    if s > 0.45 and v > 0.6: r = colorsys.hsv_to_rgb(0.53, min(1, s * 0.35), 1.0)
    else: r = colorsys.hsv_to_rgb(0.575, min(1, s * 0.55 + 0.12), min(1, v * 1.6 + 0.16))
    _fc[c] = tuple(int(round(x * 255)) for x in r); return _fc[c]
def recolour(img, role):
    out = img.copy()
    for fn, m in ((ice, ~role), (ice_floor, role)):
        sub = out[m]
        for c in {tuple(p) for p in sub.tolist()}:
            sub[(sub == c).all(1)] = fn(c)
        out[m] = sub
    return out

def glass(rgb, a, bg, tint=(205, 238, 255), keep=0.0):
    """a crystal sprite as a chunk of clear ice over bg: outline deep blue, faces see-through, glints white."""
    lum = rgb.astype(float).mean(2) / 255; out = bg.astype(float).copy()
    lo, hi = np.percentile(lum[a], 12), np.percentile(lum[a], 92)
    t = np.clip((lum - lo) / max(1e-3, hi - lo), 0, 1)
    edge = a & (t < 0.12); glint = a & (t > 0.93); face = a & ~edge & ~glint
    T = np.array(tint, float)
    k = (0.38 + 0.42 * t)[..., None]
    out[face] = (out * (1 - k) + (T * (0.72 + 0.28 * t[..., None])) * k)[face]
    if keep: out[face] = out[face] * (1 - keep) + rgb.astype(float)[face] * keep
    out[edge] = (52, 92, 150); out[glint] = (250, 254, 255)
    return out.astype(np.uint8)

def main(out):
    V = gg.Vocab(); rnd = random.Random(11)
    base = np.zeros((H * 16, W * 16, 3), np.uint8); ROLE = np.zeros((H * 16, W * 16), bool)
    for y in range(H):
        for x in range(W):
            key = cls(x, y) + ''.join(cls(x + dx, y + dy) for dx, dy in gg.N8)
            m = 0x219 if key == 'R' * 9 else V.pick(key, rnd)
            base[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = V.meta(m)
            if m in (0x200, 0x2F5, 0x2F6, 0x2C2, 0x2C0, 0x2BE): ROLE[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = True
            elif m != 0x219:                           # an edge: its floor pixels are the floor tile's, where the rock's differ
                t = V.meta(m); f = V.meta(0x200); r = V.meta(0x219)
                ROLE[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = (t == f).all(2) & ~(t == r).all(2) | ((t == f).all(2) & (key[0] == 'O'))
    # stairs and lips (the Grotto's), before the recolour
    for (x, y) in STAIR: base[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = V.meta(0x207)
    for (x, y) in LIPS | LEDGE:
        l, r = (x - 1, y) in LIPS | LEDGE, (x + 1, y) in LIPS | LEDGE
        base[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = V.meta(0x2C2 if l and r else 0x2C0 if r else 0x2BE if l else 0x2C2)
    img = recolour(base, ROLE)
    # frost along the lips: a pale rim on the edge line
    for (x, y) in LIPS | LEDGE:
        blk = img[y * 16:y * 16 + 16, x * 16:x * 16 + 16]
        lum = blk.astype(int).sum(2); dark = lum < np.percentile(lum, 18)
        for yy in range(1, 16):
            for xx in range(16):
                if dark[yy, xx] and not dark[yy - 1, xx]: blk[yy - 1, xx] = (226, 244, 255)
    # DM's bridges, cooled
    dm = np.array(Image.open('/tmp/1f_new.png').convert('RGB'))
    for (x, y) in BRIDGE:
        b = dm[y * 16:y * 16 + 16, x * 16:x * 16 + 16].astype(float)
        g = b.mean(2, keepdims=True); img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = np.clip(b * 0.55 + g * 0.3 + np.array([10, 22, 40]) * 0.6, 0, 255)
    # clear ice where DM has slippery ice: a pale glassy sheet with diagonal sheen
    for (x, y) in ICE:
        blk = img[y * 16:y * 16 + 16, x * 16:x * 16 + 16].astype(float)
        sheet = np.zeros((16, 16, 3)); yy, xx = np.mgrid[0:16, 0:16]
        band = ((xx + yy + 3 * x + 3 * y) % 12 < 2)
        sheet[:] = (150, 205, 240); sheet[band] = (225, 246, 255)
        img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = (blk * 0.25 + sheet * 0.75).astype(np.uint8)
    Image.fromarray(img).save(out)
    return img

if __name__ == '__main__': main(sys.argv[1] if len(sys.argv) > 1 else '/tmp/m1f.png')
