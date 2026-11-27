"""Hollow Hill stage 2 trainers (2026-11-27): Adventurer Finn, Revenant Alphonse (by his grave), Witch Helga, Royal
Officer Denth. Each: walk into his sight (or speak to him), the intro and the battle opening; then, with his trainer
flag set, his after-line. Also the grave's text. Needs the r11_entry state (r11/walk1.py)."""
import os, sys, struct, gzip
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
go('Route11', (0, 20)); g.walk('LEFT', 2); g.run(60); print('Hollow Hill', where(g))
HH = bytes(g.state())
def encounter(label, approach, steps, n=7, beaten=()):
    g.restore(HH); g.run(5)
    for t in beaten: setflag(const('TRAINER_FLAGS_START') + const(t))
    g.run(5)
    for t in approach: go('HollowHill', t)
    for d in steps: g.walk(d, 1); g.run(4)
    for k in range(n):
        g.run(70); f = g.frame().copy()
        shots.append(('%s %d' % (label, k), f)); g.run(2, 'A'); g.run(6)
encounter('Finn', [(34, 48)], ['LEFT'] * 5)
encounter('Alphonse', [(13, 46)], ['LEFT'] * 2)
encounter('Denth', [(22, 36)], ['UP'] * 6, beaten=['TRAINER_DR_HH_ADVENTURER_FINN'])   # the way passes Finn
encounter('Helga', [(5, 31)], ['UP'] * 4, beaten=['TRAINER_DR_HH_REVENANT_ALPHONSE'])   # the way passes Alphonse
# after-lines and the grave
g.restore(HH); g.run(5)
for t in ('TRAINER_DR_HH_ADVENTURER_FINN', 'TRAINER_DR_HH_REVENANT_ALPHONSE', 'TRAINER_DR_HH_WITCH_HELGA', 'TRAINER_DR_HH_ROYAL_OFFICER_DENTH'):
    setflag(const('TRAINER_FLAGS_START') + const(t))
g.run(5)
go('HollowHill', (28, 47)); face('UP'); talk('Finn after')
go('HollowHill', (7, 46)); face('LEFT'); talk('Alphonse after')
go('HollowHill', (5, 47)); face('UP'); talk('The grave')
go('HollowHill', (7, 27)); face('RIGHT'); talk('Helga after')
go('HollowHill', (20, 28)); face('LEFT'); talk('Denth after')
sheet('/home/claude/repo/assets/hollowhill_reference/ingame_hh_trainers_walk.png')
