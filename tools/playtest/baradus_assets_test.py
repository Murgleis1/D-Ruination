"""Baradus's sprites in the game (2026-11-25, sky-blue glasses), on a TEST ROM only: the cold open's arrival with
Cadmus drawn as Baradus (OBJ_EVENT_GFX_BARADUS), his portraits shown in place of Cadmus's (positive, anger, negative,
positive, anger), and a test battle against TRAINER_ROUTE1_A wearing TRAINER_PIC_BARADUS (after a given Eevee).
The test edits (PellucaHarbour scripts.pory and map.json, trainers.party) are reverted after the test ROM is built.
Finds each portrait on screen by matching its 80x80 window against the PNG, and the battle front by matching the 64x64
picture anywhere on screen. Writes a sheet of the frames.
Usage: python3 tools/playtest/baradus_assets_test.py TEST_ROM [OUT.png]"""
import sys, struct
import numpy as np
sys.path.insert(0, '/home/claude/repo/tools/playtest')
from gba_harness import GBA
from PIL import Image, ImageDraw

ROM = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/scratch/baradus_assets_test.png'
CB = '/home/claude/repo/codebase/'
IW, EW = 0x019000, 0x021000
HARBOUR, LAB = (2, 75), (0, 29)


def where(g):
    st = bytes(g.state()); sb1 = struct.unpack_from('<I', st, IW + (0x03006A08 - 0x03000000))[0]
    if not 0x02000000 <= sb1 < 0x02040000: return None
    b = EW + (sb1 - 0x02000000); return struct.unpack_from('<hh', st, b), struct.unpack_from('<bb', st, b + 4)


def naming(f): return f[:16].mean() > 120 and f[20:60, 40:200].mean() > 150


def want(rel):
    im = Image.open(CB + rel); a = np.array(im); p = np.array(im.getpalette()[:48]).reshape(16, 3).astype(int)
    return p[a] // 8 * 8, a != 0


PORTRAITS = {e: want('graphics/portraits/baradus_%s.png' % e) for e in ('positive', 'anger', 'negative')}
FRONT = want('graphics/trainers/front_pics/baradus.png')


def portrait_on(f):
    win = f[32:112, 152:232].astype(int) // 8 * 8
    for e, (w, m) in PORTRAITS.items():
        if int(((np.abs(win - w).max(-1) > 8) & m).sum()) < 20:
            return e
    return None


FY, FX = np.nonzero(FRONT[1])
_rng = np.random.default_rng(1)
_SAMPLE = _rng.choice(len(FY), 160, replace=False)
SY, SX = FY[_SAMPLE], FX[_SAMPLE]
SW = FRONT[0][SY, SX]


def front_on(f, visible_h=112):
    """The battle front anywhere on screen: a sampled search over every offset (its pixels above the battle text
    box, row 112), then the masked mismatch at the best offset over the pixels in view. Returns (bad, x, y, n)."""
    a = f.astype(int) // 8 * 8
    oy, ox = np.mgrid[0:160 - 64 + 1, 0:240 - 64 + 1]
    gy = oy[..., None] + SY
    got = a[np.minimum(gy, 159), ox[..., None] + SX]
    vis = gy < visible_h
    bad = ((np.abs(got - SW).max(-1) > 8) & vis).sum(-1) / np.maximum(vis.sum(-1), 1)
    bad[vis.sum(-1) < 60] = 1
    y, x = np.unravel_index(bad.argmin(), bad.shape)
    w, m = FRONT
    m2 = m.copy()
    m2[max(0, visible_h - y):] = False
    full = int(((np.abs(a[y:y + 64, x:x + 64] - w).max(-1) > 8) & m2).sum())
    return full, int(x), int(y), int(m2.sum())


OWI = np.array(Image.open(CB + 'graphics/object_events/pics/people/baradus.png'))
OWP = np.array(Image.open(CB + 'graphics/object_events/pics/people/baradus.png').getpalette()[:48]).reshape(16, 3).astype(int)


def ow_on(f):
    """Baradus's south-facing overworld frames (0, 3, 4) anywhere on screen; returns (bad, x, y, frame)."""
    a = f.astype(int) // 8 * 8
    best = None
    for k in (0, 3, 4):
        idx = OWI[:, k * 16:(k + 1) * 16]
        w = OWP[idx] // 8 * 8
        m = idx != 0
        ys, xs = np.nonzero(m)
        oy, ox = np.mgrid[0:160 - 32 + 1, 0:240 - 16 + 1]
        got = a[oy[..., None] + ys, ox[..., None] + xs]
        bad = (np.abs(got - w[ys, xs]).max(-1) > 8).sum(-1)
        y, x = np.unravel_index(bad.argmin(), bad.shape)
        if best is None or bad[y, x] < best[0]:
            best = (int(bad[y, x]), int(x), int(y), k)
    return best


g = GBA(ROM); g.run(700); g.tap('START'); g.run(120)
shots, seen = [], set()
tail, ow_best = [], None
for i in range(3000):
    w = where(g); f = g.frame()
    if naming(f): g.run(40); g.tap('START'); g.run(20); g.tap('A'); g.run(90); continue
    e = portrait_on(f)
    if e and e not in seen:
        seen.add(e); shots.append(('portrait %s' % e, f.copy()))
    if w and w[1] == HARBOUR and seen and i % 4 == 0 and not e:
        o = ow_on(f)
        if ow_best is None or o[0] < ow_best[0][0]:
            ow_best = (o, f.copy())
    if len(seen) >= 3:
        # every frame from here to the battle menu: the trainer slides in for a moment
        for _ in range(8):
            g.run(1); tail.append(g.frame().copy())
        g.tap('A')
        if len(tail) > 1600: break
        continue
    g.tap('A'); g.run(8)
battle = None
for k in range(0, len(tail), 2):
    b = front_on(tail[k])
    if b[3] >= 200 and (battle is None or b[0] / b[3] < battle[0][0] / battle[0][3]):
        battle = (b, tail[k])
if battle:
    b, f = battle
    shots.append(('battle front: %d of %d pixels in view differ, at (%d, %d)' % (b[0], b[3], b[1], b[2]), f))
    z = Image.fromarray(f).crop((b[1], b[2], b[1] + 64, min(160, b[2] + 64))).resize((256, 4 * (min(160, b[2] + 64) - b[2])), Image.NEAREST)
    z.save(OUT.replace('.png', '_front.png'))
if ow_best:
    (bad, x, y, k), f = ow_best
    shots.append(('overworld frame %d: %d pixels differ at (%d, %d)' % (k, bad, x, y), f))
    Image.fromarray(f).crop((max(0, x - 16), max(0, y - 8), x + 32, y + 40)).resize((192, 192), Image.NEAREST).save(OUT.replace('.png', '_ow.png'))
ok = True
def check(name, cond, info=''):
    global ok
    print('%-46s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok &= bool(cond)
for e in ('positive', 'anger', 'negative'):
    check('portrait %s shown exactly' % e, e in seen)
check('battle front shown exactly (pixels in view)', battle is not None and battle[0][0] <= 2, battle and battle[0])
check('overworld shown exactly (south frame)', ow_best is not None and ow_best[0][0] <= 2, ow_best and ow_best[0])
print('ALL OK' if ok else 'PROBLEM')
S = Image.new('RGB', (240 * 3 * 2, 172 * 2 * ((len(shots) + 2) // 3)), (20, 20, 24)); d = ImageDraw.Draw(S)
for k, (n, f) in enumerate(shots):
    S.paste(Image.fromarray(f).resize((480, 320), Image.NEAREST), ((k % 3) * 480, (k // 3) * 344 + 22))
    d.text(((k % 3) * 480 + 4, (k // 3) * 344 + 4), n, fill=(255, 255, 0))
S.save(OUT); print(OUT)
