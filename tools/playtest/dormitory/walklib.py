"""Walk the player around in the harness by BFS over a layout's collision/elevation/behaviour."""
import sys, struct, json, re, gzip
from collections import deque
sys.path.insert(0, '/home/claude/repo/tools/playtest')
from gba_harness import GBA
C = '/home/claude/repo/codebase'
IW, EW = 0x019000, 0x021000
BEH = {int(m.group(2), 0): m.group(1) for l in open(C + '/include/constants/metatile_behaviors.h')
       for m in [re.match(r'#define (MB_\w+)\s+(0x[0-9A-Fa-f]+|\d+)', l)] if m}
AVOID = ('WATER', 'OCEAN', 'WATERFALL', 'CURRENT', 'SEAWEED', 'JUMP', 'LEDGE', 'POND', 'PUDDLE_DEEP')
LAYOUTS = {l['id']: l for l in json.load(open(C + '/data/layouts/layouts.json'))['layouts'] if 'id' in l}
HDR = open(C + '/src/data/tilesets/headers.h').read(); MT = open(C + '/src/data/tilesets/metatiles.h').read()

def attrs(sym):
    m = re.search(r'const struct Tileset ' + sym + r'\s*=\s*\{(.*?)\};', HDR, re.S)
    a = re.search(r'\.metatileAttributes = (\w+)', m.group(1)).group(1)
    return open(C + '/' + re.search(a + r'\[\] = INCBIN_U16\("([^"]+)"', MT).group(1), 'rb').read()

class Grid:
    def __init__(self, mapname):
        m = json.load(open(f'{C}/data/maps/{mapname}/map.json')); L = LAYOUTS[m['layout']]
        self.w, self.h = L['width'], L['height']
        d = open(C + '/' + L['blockdata_filepath'], 'rb').read()
        pa, sa = attrs(L['primary_tileset']), attrs(L['secondary_tileset'])
        self.cell = {}
        for y in range(self.h):
            for x in range(self.w):
                v = struct.unpack_from('<H', d, (y * self.w + x) * 2)[0]; mid = v & 0x3FF
                a = pa if mid < 512 else sa; at = struct.unpack_from('<H', a, (mid % 512) * 2)[0] if (mid % 512) * 2 < len(a) else 0
                self.cell[(x, y)] = ((v >> 10) & 3, v >> 12, BEH.get(at & 0xFF, ''))
        self.objs = {(o['x'], o['y']) for o in m['object_events']}
    def ok(self, p, blocked=()):
        if p not in self.cell or p in blocked or p in self.objs: return False
        col, el, beh = self.cell[p]
        return col == 0 and not any(k in beh for k in AVOID)
    def path(self, a, b, blocked=()):
        D = {(1, 0): 'RIGHT', (-1, 0): 'LEFT', (0, 1): 'DOWN', (0, -1): 'UP'}
        prev = {a: None}; q = deque([a])
        while q:
            p = q.popleft()
            if p == b: break
            for (dx, dy), name in D.items():
                n = (p[0] + dx, p[1] + dy)
                if n in prev or not (self.ok(n, blocked) or n == b): continue
                e1, e2 = self.cell[p][1], self.cell[n][1]
                if e1 != e2 and e1 not in (0, 15) and e2 not in (0, 15): continue
                prev[n] = (p, name); q.append(n)
        if b not in prev: return None
        out = []; p = b
        while prev[p]: p, name = prev[p][0], prev[p][1]; out.append(name)
        return out[::-1]

def where(g):
    st = bytes(g.state()); sb1 = struct.unpack_from('<I', st, IW + (0x03006A08 - 0x03000000))[0]
    if not 0x02000000 <= sb1 < 0x02040000: return None
    b = EW + (sb1 - 0x02000000); return struct.unpack_from('<hh', st, b), struct.unpack_from('<bb', st, b + 4)

def step(g, d):
    """One tile: hold just long enough to start the step, then let it finish."""
    p = where(g)[0]; g.run(10, d); g.run(14)
    if where(g)[0] == p:              # it only turned to face that way: one more
        g.run(10, d); g.run(14)

def go(g, mapname, target, log=print, settle=10):
    """Walk to target on mapname; returns True when standing on target."""
    G = Grid(mapname); blocked = set()
    for attempt in range(12):
        pos = where(g)[0]
        if pos == target: return True
        steps = G.path(pos, target, blocked)
        if steps is None: log('no path', mapname, pos, target); return False
        for s in steps:
            before = where(g)[0]; step(g, s)
            after = where(g)
            if after is None: return False
            if after[0] == before:
                dx, dy = {'RIGHT': (1, 0), 'LEFT': (-1, 0), 'DOWN': (0, 1), 'UP': (0, -1)}[s]
                blocked.add((before[0] + dx, before[1] + dy)); break
    return where(g)[0] == target
