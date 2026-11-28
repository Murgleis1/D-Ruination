"""Chapter 1 wild Pokémon in the emulator (2026-11-27): walk the chapter from Pelluca's west gate to Mirroh Peak,
and on each map with a table stand in its grass (or cave floor) and step back and forth until N wild battles have
started. Each battle's species and level are read from the battle data (gBattleMons[1]) and the player runs.
Then, with the Old Rod put in the bag and registered, fish in Pelluca Harbour, on Route 11 and on the Mt. Mirroh river.
Every encounter seen is checked against the map's table in src/data/wild_encounters.json (species and level range).

Test-only helpers: every trainer's flag is set (so the walk is not stopped by battles), and the lead's battle Speed is
given Run Away (and its HP topped up) so it always gets away. Needs the r11_entry state (r11/walk1.py).
Writes assets/wild_reference/ingame_ch1_wild_walk.png (one frame per species seen) and prints the tallies."""
import os, sys, struct, gzip, json, re, collections
os.environ.setdefault('ST', '/home/claude/scratch/r11/r11_entry.state')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from npc_dialogue_lib import *
from npc_dialogue_lib import _go
import walklib
from walklib import Grid, step
from dr_consts import const, saveblock1_offsets

N = int(os.environ.get('N', 40)); NFISH = int(os.environ.get('NFISH', 12))
C = '/home/claude/repo/codebase'
MAPSYM = {m.group(2): int(m.group(1), 16) for l in open(C + '/pokeemerald.map')
          for m in [re.match(r'\s+0x([0-9a-f]{8})\s+(\w+)$', l)] if m}
G_MAIN, G_BMONS = MAPSYM['gMain'], MAPSYM['gBattleMons']
SYMAT = {v: k for k, v in MAPSYM.items()}
CB2_OVERWORLD, CB2_BATTLE = MAPSYM['CB2_Overworld'] | 1, MAPSYM['BattleMainCB2'] | 1
BMON_SIZE, BMON_LEVEL, BMON_SPEED, BMON_ABILITY, BMON_HP, BMON_MAXHP = 96, 44, 6, 32, 42, 46
SB1_KEYITEMS, SB1_REGISTERED, SB2_ENCKEY = 1536, 1174, 172     # offsetof(); the key at 0xAC (global.h)
SPNAME = {int(m.group(2)): m.group(1) for l in open(C + '/include/constants/species.h')
          for m in [re.match(r'#define SPECIES_(\w+)\s+(\d+)\s*$', l)] if m}
FLAGS_OFF = saveblock1_offsets()[0]
ABILITY_RUN_AWAY = int(re.search(r'#define ABILITY_RUN_AWAY (\d+)', open(C + '/include/constants/abilities.h').read()).group(1))
OUT = '/home/claude/repo/assets/wild_reference/ingame_ch1_wild_walk.png'

def ram(addr, n):
    st = bytes(g.state())
    base = EWB + addr - 0x02000000 if addr < 0x03000000 else IW + addr - 0x03000000
    return st[base:base + n]
def poke(addr, data):
    st = bytearray(g.state())
    base = EWB + addr - 0x02000000 if addr < 0x03000000 else IW + addr - 0x03000000
    st[base:base + len(data)] = data; g.restore(bytes(st))
IW = 0x019000
def sb(n): return struct.unpack('<I', ram(0x03006A08 if n == 1 else 0x03006A04, 4))[0]
def setflag(flag):
    a = sb(1) + FLAGS_OFF + flag // 8; poke(a, bytes([ram(a, 1)[0] | 1 << (flag % 8)]))
def cb2(): return struct.unpack('<I', ram(G_MAIN + 4, 4))[0]

tables = {}
for grp in json.load(open(C + '/src/data/wild_encounters.json'))['wild_encounter_groups']:
    for e in grp['encounters']:
        if 'map' in e: tables[e['map']] = e
MAPID = {json.load(open(f'{C}/data/maps/{d}/map.json'))['name']: json.load(open(f'{C}/data/maps/{d}/map.json'))['id']
         for d in os.listdir(C + '/data/maps') if os.path.exists(f'{C}/data/maps/{d}/map.json')}

seen = collections.defaultdict(collections.Counter); problems = []; firsts = {}
def battle(mapname, kind):
    """A wild battle has started: read the foe, raise our Speed, run."""
    for _ in range(80):
        g.run(10)
        if cb2() == CB2_BATTLE and struct.unpack('<H', ram(G_BMONS + BMON_SIZE, 2))[0]: break
        if cb2() == CB2_OVERWORLD: return               # not a battle: a door, a warp's fade, a script
    else:
        if cb2() != CB2_BATTLE:
            print('not a battle and not the overworld:', SYMAT.get(cb2() & ~1, hex(cb2())), where(g)); return
    g.run(240)
    foe = ram(G_BMONS + BMON_SIZE, BMON_SIZE); sp = struct.unpack_from('<H', foe, 0)[0]; lv = foe[BMON_LEVEL]
    name = SPNAME.get(sp, str(sp)); seen[(mapname, kind)][(name, lv)] += 1
    t = tables.get(MAPID[mapname], {}).get(kind + '_mons')
    rows = [r for r in (t or {}).get('mons', []) if r['species'] == 'SPECIES_' + name and r['min_level'] <= lv <= r['max_level']]
    if not rows: problems.append((mapname, kind, name, lv))
    if (mapname, name) not in firsts:
        firsts[(mapname, name)] = 1; shots.append(('%s %s: %s Lv%d' % (mapname, kind, name, lv), g.frame().copy()))
    poke(G_BMONS + BMON_ABILITY, struct.pack('<H', ABILITY_RUN_AWAY))
    poke(G_BMONS + BMON_HP, ram(G_BMONS + BMON_MAXHP, 2))
    for k in range(60):
        if cb2() == CB2_OVERWORLD: break
        g.run(4, 'B'); g.run(14); g.run(4, 'DOWN'); g.run(14); g.run(4, 'RIGHT'); g.run(14); g.run(4, 'A'); g.run(50)
    for _ in range(40):
        if cb2() == CB2_OVERWORLD: break
        g.run(2, 'A'); g.run(20)
    if cb2() != CB2_OVERWORLD:
        print('stuck:', SYMAT.get(cb2() & ~1, hex(cb2())), where(g))
        for k in range(8): g.run(2, 'A'); g.run(60); shots.append(('stuck +%d' % k, g.frame().copy()))
        shots.append(('STUCK in battle on %s' % mapname, g.frame().copy())); sheet(OUT, cols=6); raise SystemExit('stuck in battle')
    g.run(90)

def go_wild(mapname, target, tries=200):
    """Walk to target; a wild battle on the way is recorded, then the walk carries on."""
    G = Grid(mapname); blocked = set()
    for _ in range(tries):
        pos = where(g)[0]
        if pos == target: return True
        path = G.path(pos, target, blocked)
        if path is None: print('no path', mapname, pos, target); return False
        for s in path:
            before = where(g)[0]; step(g, s)
            if cb2() != CB2_OVERWORLD: battle(mapname, 'land'); break
            if where(g)[0] == before:            # a cell the grid can't tell is closed from this side (stairs' sides)
                dx, dy = {'RIGHT': (1, 0), 'LEFT': (-1, 0), 'DOWN': (0, 1), 'UP': (0, -1)}[s]
                blocked.add((before[0] + dx, before[1] + dy)); g.run(30); break
    return where(g)[0] == target

ENC = ('TALL_GRASS', 'LONG_GRASS', 'CAVE', 'INDOOR_ENCOUNTER', 'SAND', 'ASHGRASS')
def sample(mapname, near):
    """Stand on a pair of encounter tiles next to each other, nearest to `near`, and step between them."""
    G = Grid(mapname)
    cands = [p for p, (col, el, beh) in G.cell.items() if col == 0 and any(k in beh for k in ENC)
             and G.cell.get((p[0] + 1, p[1]), (1,))[0] == 0 and any(k in G.cell[(p[0] + 1, p[1])][2] for k in ENC)
             and p not in G.objs and (p[0] + 1, p[1]) not in G.objs]
    cands.sort(key=lambda p: abs(p[0] - near[0]) + abs(p[1] - near[1]))
    for a in cands[:12]:
        if G.path(where(g)[0], a) and go_wild(mapname, a): break
    else:
        print('no grass reached on', mapname); return
    start = sum(seen[(mapname, 'land')].values()); steps = 0
    while sum(seen[(mapname, 'land')].values()) - start < N and steps < 3000:
        for d in ('RIGHT', 'LEFT'):
            step(g, d); steps += 1
            if cb2() != CB2_OVERWORLD: battle(mapname, 'land'); go_wild(mapname, a)
    print('%-22s %3d battles in %4d steps' % (mapname, sum(seen[(mapname, 'land')].values()) - start, steps))

def give_old_rod():
    key = struct.unpack('<I', ram(sb(2) + SB2_ENCKEY, 4))[0] & 0xFFFF; base = sb(1) + SB1_KEYITEMS
    for i in range(30):
        it = struct.unpack('<H', ram(base + i * 4, 2))[0]
        if it == 0: poke(base + i * 4, struct.pack('<HH', const('ITEM_OLD_ROD'), 1 ^ key)); break
    poke(sb(1) + SB1_REGISTERED, struct.pack('<H', const('ITEM_OLD_ROD')))

WATER = ('OCEAN_WATER', 'POND_WATER', 'DEEP_WATER', 'SEMI_DEEP_WATER', 'NO_SURFACING')
def fish(mapname, near):
    """Stand on the shore tile nearest `near`, face the water, cast with SELECT until NFISH bites."""
    G = Grid(mapname); D = {'RIGHT': (1, 0), 'LEFT': (-1, 0), 'DOWN': (0, 1), 'UP': (0, -1)}
    spots = []
    for p, (col, el, beh) in G.cell.items():
        # the game fishes only from a level-3 cell with no edge on that side, facing level-1 water with no collision
        if not G.ok(p) or el != 3 or 'IMPASSABLE' in beh: continue
        for d, (dx, dy) in D.items():
            q = G.cell.get((p[0] + dx, p[1] + dy))
            if q and q[0] == 0 and q[1] == 1 and any(k in q[2] for k in WATER):
                spots.append((abs(p[0] - near[0]) + abs(p[1] - near[1]), p, d))
    for _, spot, facing in sorted(spots)[:15]:
        if G.path(where(g)[0], spot) and go_wild(mapname, spot): break
    else:
        print('no shore reached on', mapname); return
    face(facing); got = 0
    for k in range(NFISH * 6):
        g.run(2, 'SELECT'); g.run(30)
        for _ in range(90):                       # wait for the bite ("Oh! A bite!") or "Not even a nibble"
            g.run(10)
            if cb2() != CB2_OVERWORLD: break
            g.run(2, 'A')
        if cb2() != CB2_OVERWORLD:
            battle(mapname, 'fishing'); got += 1
            if got >= NFISH: break
        else:
            for _ in range(6): g.run(2, 'B'); g.run(15)
    print('%-22s %3d bites' % (mapname, got))

# ---- the walk ----
RESUME = os.environ.get('RESUME')
for _ in range(6): g.tap('A'); g.run(30)
setflag(const('FLAG_DR_STATUE_AWAKENED'))
for t in range(1, const('TRAINERS_COUNT')): setflag(const('TRAINER_FLAGS_START') + t)
g.run(5)
give_old_rod(); g.run(5)
START = where(g); print('start', START)
fish('PellucaCity', START[0])
go_wild('PellucaCity', (38, 36)); g.run(12, 'DOWN'); g.run(260); print('harbour', where(g))
fish('PellucaHarbour', (38, 14))
go_wild('PellucaHarbour', (38, 7)); g.run(12, 'UP'); g.run(260); print('town', where(g))
go_wild('PellucaCity', START[0])
for _ in range(3): g.walk('LEFT', 1); g.run(5)
print('Route 11', where(g))
sample('Route11', (20, 20))
fish('Route11', (20, 20))
go_wild('Route11', (0, 20)); g.walk('LEFT', 2); g.run(60); print('Hollow Hill', where(g))
sample('HollowHill', (40, 45))
for t in [(55, 40), (35, 51), (35, 47), (23, 44), (23, 41), (29, 36), (34, 22), (34, 17), (20, 12), (17, 6), (17, 1)]:
    go_wild('HollowHill', t)
def press(d, wait=160): g.run(12, d); g.run(14); g.run(wait)
press('UP')
for m, t, d in [('MirrohGate', (30, 7), 'UP'), ('MirrohSouthGatehouse', (4, 2), 'UP'), ('MirrohLower', (15, 7), 'UP'),
                ('MirrohUpper', (14, 10), 'UP'), ('MirrohNWGatehouse', (4, 2), 'UP')]:
    ok = go_wild(m, t); press(d); print(m, ok, '->', where(g))
sample('Route13', (17, 100))
open('/home/claude/scratch/wild/r13_sampled.state', 'wb').write(gzip.compress(bytes(g.state())))
go_wild('Route13', (8, 1)); press('UP', 200); print('Mt. Mirroh', where(g))
sample('MtMirrohExterior', (13, 20))
fish('MtMirrohExterior', (13, 20))
go_wild('MtMirrohExterior', (13, 11)); press('UP', 200); g.run(120); print('1F', where(g))
sample('MirrohInterior_1F', (54, 50))
go_wild('MirrohInterior_1F', (54, 2)); press('UP', 30); press('UP', 200); g.run(60); print('Peak', where(g))
sample('MirrohPeak', (26, 95))

print('\n== tallies ==')
for (m, kind), c in seen.items():
    sp = collections.Counter()
    for (n, lv), k in c.items(): sp[n] += k
    print('%-20s %-8s %3d: %s' % (m, kind, sum(c.values()), ', '.join('%s %d' % x for x in sp.most_common())))
print('PROBLEMS' if problems else 'every encounter matches its table', problems)
os.makedirs('/home/claude/repo/assets/wild_reference', exist_ok=True)
sheet(OUT, cols=6)
