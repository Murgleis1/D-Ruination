"""The Burglar Egg walked (2026-11-27): from Pelluca's west gate (the blast set, as the lab scene sets it) down to the
harbour; the old man beside the Tavern's door gives the quest; the two coins and the key, in order, along the beach; the
burglar appears by House Umbra's sealed door and battles (Skwovet, Klefki; test help: their HP set to 1); he runs off and
the loot is recovered; the old man offers the eggs by their look (the blue one refused, the green one taken), the
shiny-tease question (answered NO); then the player walks the quay until the egg hatches, and the hatch is filmed.
EGG=blue|green|warm picks the egg (default green). Needs the r11_entry state.
Writes assets/pelluca_reference/ingame_burglar_egg_walk.png."""
import os, sys, struct
os.environ.setdefault('ST', '/home/claude/scratch/r11/r11_entry.state')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch1_wild_walk.py')).read().split('# ---- the walk ----')[0]
exec(compile(_src, 'ch1_wild_walk', 'exec'))
EGG = os.environ.get('EGG', 'green')
OUT = '/home/claude/repo/assets/pelluca_reference/ingame_burglar_egg_walk.png'
ok_all = True
def check(name, cond, info=''):
    global ok_all
    print('%-52s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok_all &= bool(cond)
def flag(name):
    f = const(name); return bool(ram(sb(1) + FLAGS_OFF + f // 8, 1)[0] >> (f % 8) & 1)
def party(): return ram(MAPSYM['gPlayerPartyCount'], 1)[0]
ORDERS = ['GAEM','GAME','GEAM','GEMA','GMAE','GMEA','AGEM','AGME','AEGM','AEMG','AMGE','AMEG',
          'EGAM','EGMA','EAGM','EAMG','EMGA','EMAG','MGAE','MGEA','MAGE','MAEG','MEGA','MEAG']
def mon(i):
    """(species, isEgg, friendship = an egg's remaining hatch cycles) of party slot i, decrypted"""
    b = ram(MAPSYM['gPlayerParty'] + i * 100, 100)
    pid, otid = struct.unpack_from('<II', b, 0); key = pid ^ otid
    sec = bytearray(48)
    for w in range(12): struct.pack_into('<I', sec, w * 4, struct.unpack_from('<I', b, 32 + w * 4)[0] ^ key)
    gi = ORDERS[pid % 24].index('G'); G = sec[gi * 12:gi * 12 + 12]
    return SPNAME.get(struct.unpack_from('<H', G, 0)[0] & 0x7FF), bool(b[19] & 0x04), G[9]
HB = 'PellucaHarbour'

for _ in range(6): g.tap('A'); g.run(30)
setflag(const('FLAG_DR_STATUE_AWAKENED'))
for t in range(1, const('TRAINERS_COUNT')):
    if t != const('TRAINER_DR_PELLUCA_BURGLAR'): setflag(const('TRAINER_FLAGS_START') + t)
setflag(const('FLAG_DR_CHURCH_BLASTED')); g.run(5)          # (verify_nomad.py skips the story; the lab scene sets this)
go_wild('PellucaCity', (38, 36)); g.run(12, 'DOWN'); g.run(260)
# 1. the old man
go_wild(HB, (27, 18)); face('UP'); shot('the old man by the Tavern door'); talk('the old man', maxpages=10)
check('the quest has begun', flag('FLAG_DR_BURGLAR_QUEST_STARTED'))
# 2. the trail
for name, stand, fl in [('the first coin', (21, 18), 'FLAG_DR_BURGLAR_COIN1_FOUND'), ('the second coin', (16, 14), 'FLAG_DR_BURGLAR_COIN2_FOUND'),
                        ('the key', (14, 12), 'FLAG_DR_BURGLAR_KEY_FOUND')]:
    go_wild(HB, stand); face('UP'); shot(name); talk(name, maxpages=4)
    check('found ' + name, flag(fl))
g.run(30); shot('the burglar by the sealed door')
# 3. the burglar
go_wild(HB, (9, 10)); face('UP'); talk('the burglar', maxpages=4)
for _ in range(150):
    g.run(10)
    if cb2() == CB2_BATTLE and struct.unpack('<H', ram(G_BMONS + BMON_SIZE, 2))[0]: break
g.run(300); shot('the battle'); foes = []
for k in range(200):
    if cb2() == CB2_OVERWORLD: break
    sp = SPNAME.get(struct.unpack('<H', ram(G_BMONS + BMON_SIZE, 2))[0])
    if sp and sp != 'NONE' and sp not in foes: foes.append(sp)
    if struct.unpack('<H', ram(G_BMONS + BMON_SIZE + BMON_HP, 2))[0] > 1:
        poke(G_BMONS + BMON_SIZE + BMON_HP, struct.pack('<H', 1))          # test help: one hit takes it down
    poke(G_BMONS + BMON_HP, ram(G_BMONS + BMON_MAXHP, 2))
    g.run(4, 'A'); g.run(30)
check('his team: Skwovet, then Klefki', foes == ['SKWOVET', 'KLEFKI'], foes)
for k in range(6): g.run(40); shot('after the battle %d' % k); g.run(2, 'A')
g.run(200)
check('the loot is recovered', flag('FLAG_DR_BURGLAR_LOOT_RECOVERED'))
# 4. the eggs
before = party()
go_wild(HB, (27, 18)); face('UP')
def yesno():
    """the YES/NO box is up (its white panel right of centre, above the message box)"""
    f = g.frame()[84:112, 168:212].astype(int); return (f.min(axis=2) > 225).mean() > 0.5
def to_question(label):
    for p in range(10):
        g.run(150)
        if yesno(): shot(label); return True
        shot('%s (page %d)' % (label, p)); g.run(2, 'A')
    return False
g.run(2, 'A')
choice = {'blue': 0, 'green': 1, 'warm': 2}[EGG]
for i in range(3):
    check('egg question %d asked' % i, to_question('egg question %d' % i))
    if i == choice: g.run(2, 'A'); break                                               # YES
    g.run(2, 'B')                                                                      # NO
check('the shiny question asked', to_question('the shiny question')); g.run(2, 'B')    # NO
for p in range(6): g.run(150); shot('the egg %d' % p); g.run(2, 'A')
g.run(100)
check('the egg is in the party', party() == before + 1, (before, party()))
check('the egg is recorded', flag('FLAG_DR_BURGLAR_EGG_RECEIVED'))
egg = mon(party() - 1); print('the egg:', egg)
check('it is a %s egg with 6 hatch cycles left' % {'blue': 'Squirtle', 'green': 'Chespin', 'warm': 'Chimchar'}[EGG], egg == ({'blue': 'SQUIRTLE', 'green': 'CHESPIN', 'warm': 'CHIMCHAR'}[EGG], True, 6), egg)
# 5. walk the quay till it hatches
steps, hatched = 0, False
for _ in range(8): g.run(2, 'B'); g.run(30)
go_wild(HB, (18, 18))
while steps < 2000 and not hatched:
    for d in ('RIGHT', 'LEFT'):
        before_pos = where(g)[0]; step(g, d)
        if where(g)[0] != before_pos: steps += 1
        if where(g)[0] == before_pos:                                                   # the hatch script has the player
            hatched = True; break
print('steps walked before the hatch began:', steps, 'the egg now:', mon(party() - 1), where(g))
check('it hatches within about 900 steps', hatched and steps <= 950, steps)
for k in range(9): g.run(90); shot('hatching %d' % k); g.run(2, 'A' if k < 7 else 'B')
for _ in range(10): g.run(2, 'B'); g.run(30)
check('it hatched as a %s' % EGG, mon(party() - 1)[:2] == ({'blue': 'SQUIRTLE', 'green': 'CHESPIN', 'warm': 'CHIMCHAR'}[EGG], False), mon(party() - 1))
for _ in range(10): g.run(2, 'B'); g.run(30)
print('ALL OK' if ok_all else 'PROBLEM')
sheet(OUT, cols=5)
