"""Route 11 stage 2 (people and dialogue): the farmer, the farmhouse wife (both lines) and daughter, Fisher Tam
(intro and battle start; his after-battle line with his trainer flag set). Needs the r11_entry state (r11/walk1.py)."""
import os, sys, struct
os.environ.setdefault('ST', '/home/claude/scratch/r11/r11_entry.state')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from npc_dialogue_lib import *
from dr_consts import const, saveblock1_offsets
FLAGS_OFF = saveblock1_offsets()[0]
IW = 0x019000
def setflag(flag):
    st = bytearray(g.state()); sb1 = struct.unpack_from('<I', st, IW + (0x03006A08 - 0x03000000))[0]
    off = EWB + (sb1 - 0x02000000) + FLAGS_OFF + flag // 8; st[off] |= 1 << (flag % 8); g.restore(bytes(st))
for _ in range(6): g.tap('A'); g.run(30)       # the state is saved on the gate's message: finish it
setflag(const('FLAG_DR_STATUE_AWAKENED')); g.run(5)   # opens the west gate
for _ in range(3): g.walk('LEFT', 1); g.run(5)
g.run(30); print('on route', where(g))
ok = {}
ok['farmer'] = chase('Route11', 1, 'Farmer', near=(44, 12))   # objects spawn only once in view
ok['door'] = go('Route11', (55, 15)); g.walk('UP', 1); g.run(120); print('in', where(g))
ok['wife'] = go('Route11Farmhouse', (6, 7)); face('UP'); talk('Wife (before the theft)')
setflag(const('FLAG_DR_R11_THEFT_SEEN')); g.run(5)
face('UP'); talk('Wife (after the theft)')
ok['daughter'] = chase('Route11Farmhouse', 2, 'Daughter', tries=12)   # she wanders a step either way
ok['out'] = go('Route11Farmhouse', (6, 8)); g.walk('DOWN', 1); g.run(120); print('out', where(g))
ok['stairs'] = go('Route11', (58, 28)); print('beach', where(g))
go('Route11', (58, 29))                        # row 29: Tam's line of sight (he faces east, range 4)
for _ in range(2): g.walk('LEFT', 1); g.run(4)
for k in range(6):
    g.run(90); f = g.frame().copy(); shots.append(('Tam %d' % k, f))
    g.run(2, 'A'); g.run(6)
for k in range(3): g.run(120); shots.append(('battle %d' % k, g.frame().copy()))
# the after-battle line: reload, set Tam's trainer flag and speak to him
g.restore(gzip.decompress(open(os.environ['ST'], 'rb').read())); g.run(20)
for _ in range(6): g.tap('A'); g.run(30)
setflag(const('FLAG_DR_STATUE_AWAKENED')); setflag(const('TRAINER_FLAGS_START') + const('TRAINER_DR_R11_FISHER_TAM')); g.run(5)
for _ in range(3): g.walk('LEFT', 1); g.run(5)
go('Route11', (58, 28)); go('Route11', (53, 29)); face('LEFT'); talk('Tam (after his defeat)')
print(ok)
sheet('/home/claude/repo/assets/route11_reference/ingame_route11_people.png')
