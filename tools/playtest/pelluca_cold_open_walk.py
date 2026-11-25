"""The cold open's arrival in Pelluca Harbour, watched (2026-11-25; the waterfront split into its own map,
tools/art/pelluca/build_harbour.py + split_pelluca.py). From a new game: the intro, the letter, the naming, then the
arrival scene on the harbour (map 2.75): Osrid lands at (40, 21), Cadmus comes down the great pier, they walk up it, the
stop at the shrine (38, 12), the walk along the kerb (row 14) to the lab door (47, 13), the warp into the lab (0.29).
Frames are taken on the harbour every few steps of the scene; the positions the player passes through are logged and
checked against the planned walk. Writes a frame sheet.
Usage: python3 tools/playtest/pelluca_cold_open_walk.py [ROM] [OUT.png]"""
import sys, struct
sys.path.insert(0, '/home/claude/repo/tools/playtest')
from gba_harness import GBA
from PIL import Image, ImageDraw
ROM = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/repo/codebase/pokeemerald.gba'
OUT = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/scratch/cold_open_walk.png'
IW, EW = 0x019000, 0x021000
HARBOUR, LAB = (2, 75), (0, 29)
def where(g):
    st = bytes(g.state()); sb1 = struct.unpack_from('<I', st, IW + (0x03006A08 - 0x03000000))[0]
    if not 0x02000000 <= sb1 < 0x02040000: return None
    b = EW + (sb1 - 0x02000000); return struct.unpack_from('<hh', st, b), struct.unpack_from('<bb', st, b + 4)
def naming(f): return f[:16].mean() > 120 and f[20:60, 40:200].mean() > 150
g = GBA(ROM); g.run(700); g.tap('START'); g.run(120)
shots, path = [], []
for i in range(2200):
    w = where(g); f = g.frame()
    if naming(f): g.run(40); g.tap('START'); g.run(20); g.tap('A'); g.run(90); continue
    if w and w[1] == HARBOUR:
        if not path or path[-1] != w[0]: path.append(w[0]); shots.append((str(w[0]), f.copy()))
        elif i % 12 == 0 and len(shots) < 40: shots.append((str(w[0]), f.copy()))
    if w and w[1] == LAB: break
    g.tap('A'); g.run(8)
ok = True
def check(name, cond, info=''):
    global ok
    print('%-50s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok &= bool(cond)
check('lands on the harbour at (40, 21)', path and path[0] == (40, 21), path[:1])
check('walks up the great pier to the kerb (40, 14)', (40, 14) in path)
check('stops at the shrine (38, 12)', (38, 12) in path)
check('goes along the kerb to (47, 14)', (47, 14) in path)
check('ends in the lab', where(g) and where(g)[1] == LAB, where(g))
print('path', path)
print('ALL OK' if ok else 'PROBLEM')
keep = shots[::max(1, len(shots) // 16)][:16]
S = Image.new('RGB', (240 * 4, 172 * ((len(keep) + 3) // 4))); d = ImageDraw.Draw(S)
for k, (n, f) in enumerate(keep):
    S.paste(Image.fromarray(f), ((k % 4) * 240, (k // 4) * 172 + 12)); d.text(((k % 4) * 240 + 2, (k // 4) * 172), n, fill=(255, 255, 0))
S.save(OUT)
