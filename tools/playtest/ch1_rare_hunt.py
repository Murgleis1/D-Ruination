"""Hunt the 1% rares in the emulator (2026-11-27): on Route 11 (Blaze Breed Tauros, Miltank) and Hollow Hill (Houndour,
Hisuian Zorua), step back and forth in the grass, running from every wild battle, until both rares of the map have
appeared or CAP battles have passed. The harness presses buttons with fixed timing, and the game's random numbers
follow the frames, so before every step the RNG state (gRngValue, SFC32) is set from the host's random source: what
comes up then follows the table's real rates. Uses ch1_wild_walk.py's helpers. Needs the r11_entry state.
Writes assets/wild_reference/ingame_ch1_rare_hunt.png (the first sighting of each species) and prints tallies."""
import os, sys, random as _random
os.environ.setdefault('ST', '/home/claude/scratch/r11/r11_entry.state')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch1_wild_walk.py')).read().split('# ---- the walk ----')[0]
exec(compile(_src, 'ch1_wild_walk', 'exec'))
CAP = int(os.environ.get('CAP', 600))
G_RNG = MAPSYM['gRngValue']
def reseed(): poke(G_RNG, bytes(_random.getrandbits(8) for _ in range(16)))

def hunt(mapname, near, rares):
    G = Grid(mapname)
    cands = [p for p, (col, el, beh) in G.cell.items() if col == 0 and any(k in beh for k in ENC)
             and G.cell.get((p[0] + 1, p[1]), (1,))[0] == 0 and any(k in G.cell[(p[0] + 1, p[1])][2] for k in ENC)
             and p not in G.objs and (p[0] + 1, p[1]) not in G.objs]
    cands.sort(key=lambda p: abs(p[0] - near[0]) + abs(p[1] - near[1]))
    for a in cands[:12]:
        if G.path(where(g)[0], a) and go_wild(mapname, a): break
    got = lambda: {n for (n, lv) in seen[(mapname, 'land')]}
    n0 = sum(seen[(mapname, 'land')].values())
    while sum(seen[(mapname, 'land')].values()) - n0 < CAP and not set(rares) <= got():
        for d in ('RIGHT', 'LEFT'):
            reseed(); step(g, d)
            if cb2() != CB2_OVERWORLD: battle(mapname, 'land'); go_wild(mapname, a)
    n = sum(seen[(mapname, 'land')].values()) - n0
    print('%-12s %d battles; rares seen: %s' % (mapname, n, ', '.join('%s %s' % (r, 'YES' if r in got() else 'no') for r in rares)))

for _ in range(6): g.tap('A'); g.run(30)
setflag(const('FLAG_DR_STATUE_AWAKENED'))
for t in range(1, const('TRAINERS_COUNT')): setflag(const('TRAINER_FLAGS_START') + t)
g.run(5)
for _ in range(3): g.walk('LEFT', 1); g.run(5)
hunt('Route11', (20, 20), ['TAUROS_PALDEA_BLAZE', 'MILTANK'])
go_wild('Route11', (0, 20)); g.walk('LEFT', 2); g.run(60)
hunt('HollowHill', (40, 45), ['HOUNDOUR', 'ZORUA_HISUI'])
print('\n== tallies ==')
for (m, kind), c in seen.items():
    sp = collections.Counter()
    for (nm, lv), k in c.items(): sp[nm] += k
    print('%-12s %3d: %s' % (m, sum(c.values()), ', '.join('%s %d' % x for x in sp.most_common())))
print('PROBLEMS' if problems else 'every encounter matches its table', problems)
OUT = '/home/claude/repo/assets/wild_reference/ingame_ch1_rare_hunt.png'
sheet(OUT, cols=6)
