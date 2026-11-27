"""Items in the wild on Route 11, the farmhouse and Hollow Hill (2026-11-27): walk to each Poké Ball and hidden item,
face it and press A; the sheet shows each pick-up message. Needs the r11_entry state (r11/walk1.py)."""
import os, sys, struct, json
os.environ.setdefault('ST', '/home/claude/scratch/r11/r11_entry.state')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from npc_dialogue_lib import *
from dr_consts import const, saveblock1_offsets
FLAGS_OFF = saveblock1_offsets()[0]; IW = 0x019000
def setflag(flag):
    st = bytearray(g.state()); sb1 = struct.unpack_from('<I', st, IW + (0x03006A08 - 0x03000000))[0]
    off = EWB + (sb1 - 0x02000000) + FLAGS_OFF + flag // 8; st[off] |= 1 << (flag % 8); g.restore(bytes(st))
for _ in range(6): g.tap('A'); g.run(30)
setflag(const('FLAG_DR_STATUE_AWAKENED')); g.run(5)
for _ in range(3): g.walk('LEFT', 1); g.run(5)
C = '/home/claude/repo/codebase/data/maps/%s/map.json'
DIRS = {(-1, 0): 'RIGHT', (1, 0): 'LEFT', (0, 1): 'UP', (0, -1): 'DOWN'}   # stand offset -> facing
# (the follower walks a step behind: approaching a hidden item on open ground from the side keeps it off the cell)
def items(m):
    j = json.load(open(C % m)); out = []
    for o in j['object_events']:
        if o['script'] == 'Common_EventScript_FindItem' and o['flag'].startswith('FLAG_DR_ITEM'): out.append((o['x'], o['y'], o['trainer_sight_or_berry_tree_id']))
    for b in j['bg_events']:
        if b.get('type') == 'hidden_item' and b['flag'].startswith('FLAG_DR_ITEM'): out.append((b['x'], b['y'], b['item'] + ' (hidden)'))
    return out
res = {}
def pick(m, x, y, label):
    G = Grid(m)
    for (dx, dy), d in DIRS.items():
        t = (x + dx, y + dy)
        if G.ok(t) and go(m, t, tries=3):
            face(d); talk(label, maxpages=4); res[label] = True; return
    res[label] = False
for x, y, it in items('Route11'):
    if x >= 76: go('Route11', (77, 24)); go('Route11', (77, 28))             # the east beach, by its stairs
    elif y >= 26 and x < 47: go('Route11', (20, 22))
    pick('Route11', x, y, 'Route 11 ' + it)
go('Route11', (55, 15)); g.walk('UP', 1); g.run(120)
for x, y, it in items('Route11Farmhouse'): pick('Route11Farmhouse', x, y, 'Farmhouse ' + it)
go('Route11Farmhouse', (6, 8)); g.walk('DOWN', 1); g.run(120)
go('Route11', (0, 20)); g.walk('LEFT', 2); g.run(60); print('into Hollow Hill', where(g))
for x, y, it in items('HollowHill'): pick('HollowHill', x, y, 'Hollow Hill ' + it)
print(res)
sheet('/home/claude/repo/assets/route11_reference/ingame_items_walk.png')
