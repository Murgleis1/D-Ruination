"""Mock of the underground ice path below Pelluca's Arceus church (user design 2026-11-19).

Story (bible 20_chapter1_build.md, 16.2): Eden's escape blast cracks the church floor; the player drops through the
crack into a frozen hollow. The puzzle (after Pokemon Pisces' Sootopolis gym; user: one big field, black out and
reset on a second step): a 12x9 field of thin ice with ice boulders; every ice tile must be cracked exactly once,
a single unbroken route from the landing to the ice wall's gate (tools/art/icepath/puzzle.py: this layout has
exactly two solutions). Then the gate's ice gives way, opening the shrine: the half-thawed Arceus statue (the
pre-imperial evidence; the Sparkling Opal) and a ladder back up into the church.
Art: Pokemon Crown's ice room (group 2 #54; credit: Blah and the Crown team, with permission): the snowy rock walls,
the frozen flagstone floor, the ladder; vanilla Emerald's thin ice (Sootopolis gym) and Shoal Cave ice boulders;
the Arceus statue from the Pokemon Rejuvenation team's ArceusRuins sheet (as in the church), half encased in ice.
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/icepath/icepath_mock.py [out]
"""
import os, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
for p in ("tools/crown", "tools", "tools/art/templar", "tools/art/icepath"): sys.path.insert(0, os.path.join(ROOT, p))
from crown_pieces import map_layout, TS
import render_layout as RL

TSI = TS(map_layout(2, 54)); SOOT = RL.TS('LAYOUT_SOOTOPOLIS_CITY_GYM_1F')
OUT_TL, TOP, OUT_TR, LEFT, IN_TL, IN_TOP, IN_TR, RIGHT, IN_L, IN_R, BOTTOM = \
    0x29B, 0x2C4, 0x29C, 0x2C7, 0x29B, 0x299, 0x29C, 0x2C6, 0x292, 0x290, 0x289
ROCK, LADDER_TOP, LADDER_FOOT = 0x2D9, 0x28F, 0x297
THIN, CRACKED, BROKEN = 0x20D, 0x20E, 0x206             # Sootopolis gym ice (the build gives them our own ids)

FW, FH = 12, 9                       # the field
FIELD_X, FIELD_Y = 2, 11             # (the shrine above: eight rows, room to stand back from the statue)
S, E = (5, 8), (6, 0)                # field coordinates: entry from the landing, exit to the gate
BOULDERS = [(2, 0), (2, 2), (5, 2), (8, 2), (0, 3), (10, 3), (2, 4), (3, 4), (5, 4), (8, 4), (9, 4), (5, 5), (6, 5),
            (11, 5), (1, 6), (2, 6), (5, 6), (8, 6), (2, 7), (3, 7), (0, 8), (9, 8)]
W, H = FW + 4, FIELD_Y + FH + 2      # walls two thick each side; the landing row; the bottom wall
WALL_ROW = FIELD_Y - 1               # the ice wall between the field and the shrine (its gate above E)
GATE = (FIELD_X + E[0], WALL_ROW)
LANDING = (FIELD_X + S[0], FIELD_Y + FH)
LADDER = (FIELD_X, 1)                # back up to the church, from the shrine's corner
STATUE_CX = FIELD_X + E[0]           # the statue's column: straight on from the gate
STATUE_BASE = 5                      # the row the statue's base sits on (its foot at the row's bottom)
FIRES = (STATUE_CX - 3, STATUE_CX + 3)   # fire rings level with each other either side of the statue (user)
LOGS = (STATUE_CX - 4, STATUE_CX + 4)    # the camp's log benches beside them, fossilised to stone (user)
FLOWERS = (STATUE_CX - 1, STATUE_CX + 1) # offerings at the foot of the statue's ice

def boulder():
    """Shoal Cave's ice boulder (vanilla Emerald; assets/vanilla_reference/ice_boulder.png, cut from the ice room)."""
    a = np.array(Image.open(os.path.join(ROOT, 'assets', 'vanilla_reference', 'ice_boulder.png')).convert('RGBA'))
    return a[..., :3], a[..., 3] > 0

ICE_RAMP = [(90, 140, 170), (120, 180, 214), (150, 206, 232), (176, 226, 244), (214, 240, 250), (244, 252, 255)]

def frost(rgb, m, top_frac):
    """Lock the part of a piece below top_frac in ice: its pixels seen through clear blue ice (blended and lifted),
    a jagged bright rim along the ice's top edge and a darker foot."""
    out = rgb.astype(float).copy(); h, w = m.shape; top = int(h * top_frac)
    rng = np.random.default_rng(5); edge = [top + int(rng.integers(-2, 3)) for _ in range(w)]
    for x in range(w):
        for y in range(max(0, edge[x]), h):
            if m[y, x]: out[y, x] = out[y, x] * 0.4 + np.array(ICE_RAMP[3]) * 0.6
        if 0 <= edge[x] < h and m[edge[x], x]: out[edge[x], x] = ICE_RAMP[5]
    return out.astype(np.uint8)

def statue_half_thawed():
    """The reformed Arceus statue (tools/art/icepath/arceus_statue.py): gem-laden cave stone, half locked in ice."""
    sys.path.insert(0, HERE); import arceus_statue
    return arceus_statue.statue(ice=True)

def gate():
    """The gate in the ice wall: a boulder of clearer, paler ice (it gives way when the field is done)."""
    b, bm = boulder(); out = b.copy()
    lum = b.astype(int).sum(-1)
    for i, (lo, hi) in enumerate(((0, 300), (300, 420), (420, 560), (560, 700), (700, 800))):
        out[(lum >= lo) & (lum < hi) & bm] = ICE_RAMP[min(5, i + 1)]
    return out, bm

def grid():
    g = [[ROCK] * W for _ in range(H)]
    g[0] = [OUT_TL] + [TOP] * (W - 2) + [OUT_TR]
    g[1] = [LEFT, IN_TL] + [IN_TOP] * (W - 4) + [IN_TR, RIGHT]
    for y in range(2, H - 1): g[y][0], g[y][1], g[y][W - 2], g[y][W - 1] = LEFT, IN_L, IN_R, RIGHT
    g[H - 1] = [BOTTOM] * W
    g[LADDER[1]][LADDER[0]] = LADDER_TOP; g[LADDER[1] + 1][LADDER[0]] = LADDER_FOOT
    return g

def compose():
    """-> (image, cells: dict of 'ice', 'boulder', 'gate', 'landing', 'shrine' sets)."""
    g = grid(); img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = TSI.meta(g[y][x])
    thin = SOOT.metatile(THIN); b, bm = boulder()
    ice, boulders = set(), set()
    for fy in range(FH):
        for fx in range(FW):
            x, y = FIELD_X + fx, FIELD_Y + fy; c = thin.copy()
            if (fx, fy) in BOULDERS: c[bm] = b[bm]; boulders.add((x, y))
            else: ice.add((x, y))
            img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = c
    rock = TSI.meta(ROCK)
    for x in range(FIELD_X, FIELD_X + FW):                    # the ice wall above the field, the landing row below
        for y in (WALL_ROW, FIELD_Y + FH):
            if (x, y) == LANDING: continue
            c = rock.copy(); c[bm] = b[bm]; img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = c; boulders.add((x, y))
    gx, gy = GATE; boulders.discard(GATE)                     # the gate: a block of clearer ice
    gr, gm = gate(); c = rock.copy(); c[gm] = gr[gm]; img[gy * 16:gy * 16 + 16, gx * 16:gx * 16 + 16] = c
    # the worship site (user: Camp Tarragon's pieces; no statue-pillars; then "broken and smooshed": everything given
    # room): the statue at the back on the gate's line; the arch of the two great tusks, in stone, as a gateway
    # standing over the path between the gate and the statue; fire rings level with each other either side of the
    # statue with the camp's log benches beside them, fossilised to grey stone (user); blue flowers at its foot
    def piece(name):
        a = np.array(Image.open(os.path.join(ROOT, 'assets', 'monomyth_reference', 'pieces', f'tarragon_{name}.png')).convert('RGBA'))
        return a[..., :3], a[..., 3] > 0
    def stone(rgb, m):                                    # (user: the bone arches shaded as the statue's stone)
        import arceus_statue as AS
        ramp = [AS.OUT, AS.D1, AS.D2, AS.MID, AS.LIGHT, AS.TOP, (168, 176, 188)]; out = rgb.copy()
        lum = rgb.astype(int).sum(-1); lo, hi = lum[m].min(), lum[m].max()
        for y, x in zip(*np.nonzero(m)): out[y, x] = ramp[min(6, int((lum[y, x] - lo) / max(1, hi - lo + 1) * 7))]
        rng = np.random.default_rng(4); ys, xs = np.nonzero(m & (lum > lo + (hi - lo) // 2))
        for i in rng.choice(len(ys), size=len(ys) // 30, replace=False): out[ys[i], xs[i]] = AS.GEMS[i % 3]
        return out, m
    def put(rgb, m, px, py):
        sub = img[py:py + m.shape[0], px:px + m.shape[1]]; sub[m[:sub.shape[0], :sub.shape[1]]] = rgb[:sub.shape[0], :sub.shape[1]][m[:sub.shape[0], :sub.shape[1]]]
    from scipy.ndimage import label
    cx = STATUE_CX * 16 + 8
    st, sm = statue_half_thawed()
    put(st, sm, cx - st.shape[1] // 2, (STATUE_BASE + 1) * 16 - st.shape[0])
    ar, am = piece('tusk_arch'); lab, n = label(am, structure=np.ones((3, 3)))
    outer = np.zeros(am.shape, bool)                       # the two great tusks only (the inner pair and charm left out)
    for i in range(1, n + 1):
        if np.nonzero(lab == i)[0].min() < 8: outer |= lab == i
    ys, xs = np.nonzero(outer); ar, am = stone(ar[:ys.max() + 1], outer[:ys.max() + 1])
    put(ar, am, cx - am.shape[1] // 2, WALL_ROW * 16 - am.shape[0])
    po, pm = piece('post'); fr, fm = piece('fire_ring'); fl, flm = piece('blue_flowers')
    lum = po.astype(int).sum(-1); lo, hi = lum[pm].min(), lum[pm].max(); fossil = po.copy()
    FOSSIL = [(62, 62, 68), (88, 88, 94), (112, 112, 118), (138, 138, 144), (166, 166, 170), (196, 196, 200)]
    for y, x in zip(*np.nonzero(pm)): fossil[y, x] = FOSSIL[min(5, int((lum[y, x] - lo) / max(1, hi - lo + 1) * 6))]
    for x in FIRES: put(fr, fm, x * 16, STATUE_BASE * 16)
    for x in LOGS: put(fossil, pm, x * 16 + 8 - pm.shape[1] // 2, (STATUE_BASE + 1) * 16 - pm.shape[0] + 2)
    for x in FLOWERS: put(fl, flm, x * 16 + (-6 if x < STATUE_CX else 6), (STATUE_BASE + 1) * 16)
    shrine = {(x, y) for x in range(FIELD_X, FIELD_X + FW) for y in range(2, WALL_ROW)}
    return img, dict(ice=ice, boulders=boulders, gate={GATE}, landing={LANDING}, shrine=shrine,
                     statue={(STATUE_CX, 2), (STATUE_CX + 1, 2), (STATUE_CX, 3), (STATUE_CX + 1, 3)})

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/pisces/icepath_mock.png'
    img, _ = compose(); Image.fromarray(img).resize((W * 32, H * 32), 0).save(out); print(out)
