"""The Fisherman's Dilemma walked (2026-11-27): from Pelluca's west gate (after the blast) down to the harbour; the
fisherman at the end of the great pier gives the quest; the Wimpod at the plaza fountain flees, then the one at the
well flees, then at the pond it turns to fight: the shiny-tease question (answered YES), a Lv.12 shiny Wimpod with
Aqua Jet / Bug Bite / Trailblaze and Tough Claws (its hidden slot) is read from the battle data, knocked out (test
help: its HP set to 1); then the fisherman gives the Old Rod (read from the bag). Needs the r11_entry state.
Writes assets/pelluca_reference/ingame_fisherman_dilemma_walk.png."""
import os, sys, struct
os.environ.setdefault('ST', '/home/claude/scratch/r11/r11_entry.state')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ch1_wild_walk.py')).read().split('# ---- the walk ----')[0]
exec(compile(_src, 'ch1_wild_walk', 'exec'))
OUT = '/home/claude/repo/assets/pelluca_reference/ingame_fisherman_dilemma_%s.png' % ('catch' if os.environ.get('CATCH') == '1' else 'walk')
MOVES = {int(m.group(2)): m.group(1) for l in open(C + '/include/constants/moves.h')
         for m in [re.match(r'#define MOVE_(\w+)\s+(\d+)\s*$', l)] if m}
ABIL = {int(m.group(2)): m.group(1) for l in open(C + '/include/constants/abilities.h')
        for m in [re.match(r'#define ABILITY_(\w+)\s+(\d+)\s*$', l)] if m}
ok_all = True
def check(name, cond, info=''):
    global ok_all
    print('%-52s %s %s' % (name, 'ok' if cond else 'PROBLEM', info)); ok_all &= bool(cond)
def flag(name):
    f = const(name); return bool(ram(sb(1) + FLAGS_OFF + f // 8, 1)[0] >> (f % 8) & 1)
def say(label, pages=6):
    """A, then shoot each page of the message until it closes"""
    talk(label, maxpages=pages)

for _ in range(6): g.tap('A'); g.run(30)
setflag(const('FLAG_DR_STATUE_AWAKENED'))
for t in range(1, const('TRAINERS_COUNT')): setflag(const('TRAINER_FLAGS_START') + t)
g.run(5)
# the state is made by verify_nomad.py, which skips the story: the blast (the lab scene) is set here, as the game sets it
go_wild('PellucaCity', (38, 36)); g.run(12, 'DOWN'); g.run(260)
go_wild('PellucaHarbour', (39, 25)); face('DOWN'); say('the fisherman before the blast')
setflag(const('FLAG_DR_CHURCH_BLASTED')); g.run(5)
check('the church has been blasted (the sandbox is open)', flag('FLAG_DR_CHURCH_BLASTED'))
# 1. the fisherman
SB1_BALLS = 1656                 # offsetof(struct SaveBlock1, bagPocket_PokeBalls), from the compiler
def spheres():
    key = struct.unpack('<I', ram(sb(2) + SB2_ENCKEY, 4))[0] & 0xFFFF
    return sum(q ^ key for it, q in (struct.unpack('<HH', ram(sb(1) + SB1_BALLS + i * 4, 4)) for i in range(16))
               if it == const('ITEM_POKE_BALL'))
before = spheres()
go_wild('PellucaHarbour', (39, 25)); face('DOWN'); say('the fisherman', pages=10)
check('the quest has begun', flag('FLAG_DR_WIMPOD_QUEST_STARTED'))
check('he gave 5 Poke Spheres', spheres() == before + 5, (before, spheres()))
go_wild('PellucaHarbour', (38, 7)); g.run(12, 'UP'); g.run(260)
# 2. the fountain
go_wild('PellucaCity', (37, 27)); face('UP'); shot('the Wimpod in the fountain'); say('the fountain')
g.run(60); shot('it has fled the fountain')
check('it left the fountain', flag('FLAG_DR_WIMPOD_LEFT_FOUNTAIN'))
# 3. the well
go_wild('PellucaCity', (15, 13)); face('UP'); shot('the Wimpod at the well'); say('the well')
g.run(60); shot('it has fled the well')
check('it left the well', flag('FLAG_DR_WIMPOD_LEFT_WELL'))
# 4. the pond: the question, the battle
go_wild('PellucaCity', (19, 13)); face('UP'); shot('the Wimpod at the pond')
g.run(2, 'A'); g.run(120); shot('the pond'); g.run(2, 'A'); g.run(200); shot('the question')
g.run(2, 'A'); g.run(30)                                         # YES (the cursor starts on YES)
for _ in range(120):
    g.run(10)
    if cb2() == CB2_BATTLE and struct.unpack('<H', ram(G_BMONS + BMON_SIZE, 2))[0]: break
g.run(300); shot('the battle')
foe = ram(G_BMONS + BMON_SIZE, BMON_SIZE)
sp = SPNAME.get(struct.unpack_from('<H', foe, 0)[0]); lv = foe[BMON_LEVEL]
mv = [MOVES.get(m, m) for m in struct.unpack_from('<4H', foe, 12)]
ab = ABIL.get(struct.unpack_from('<H', foe, 32)[0]); shiny = foe[93]
check('a Lv.12 Wimpod', (sp, lv) == ('WIMPOD', 12), (sp, lv))
check('its moves: Aqua Jet, Bug Bite, Trailblaze', mv[:3] == ['AQUA_JET', 'BUG_BITE', 'TRAILBLAZE'], mv)
check('its ability: Tough Claws (it does not flee)', ab == 'TOUGH_CLAWS', ab)
check('shiny (the question answered YES)', shiny == 1, shiny)
poke(G_BMONS + BMON_SIZE + BMON_HP, struct.pack('<H', 1))       # test help: one hit takes it down
poke(G_BMONS + BMON_HP, ram(G_BMONS + BMON_MAXHP, 2))
party_before = ram(MAPSYM['gPlayerPartyCount'], 1)[0]; outcome = 0
CATCH = os.environ.get('CATCH') == '1'                          # CATCH=1: throw one of his Poke Spheres instead
for k in range(80):
    if cb2() == CB2_OVERWORLD: break
    if CATCH:
        if k == 0: g.run(4, 'A'); g.run(300); shot('the battle menu')
        if k < 5:                                                            # up to all five of his Spheres
            g.run(4, 'RIGHT'); g.run(14); g.run(4, 'A'); g.run(120)          # Bag
            for _ in range(8):                                               # to the Spheres pocket
                if ram(MAPSYM['gBagPosition'] + 5, 1)[0] == 3: break         # (BALLS_POCKET)
                g.run(4, 'RIGHT'); g.run(30)
            g.run(4, 'A'); g.run(30); g.run(4, 'A'); g.run(420)
            shot('Poke Sphere %d' % (k + 1))
        if ram(MAPSYM['gBattleOutcome'], 1)[0] == 7:                       # caught
            outcome = 7
            for _ in range(3): g.run(4, 'A'); g.run(150)                      # Gotcha, the Pokedex note, its page
            shot('caught')
            for _ in range(20):                                              # B declines the nickname
                if cb2() == CB2_OVERWORLD: break
                g.run(4, 'B'); g.run(40)
        else:
            g.run(400)                                                       # it broke free: its turn, then the menu
        continue
    g.run(4, 'A'); g.run(30)                                     # Fight, the first move, then the texts
for _ in range(60):                                              # finish the battle (B: past the Pokedex page, no nickname)
    if cb2() == CB2_OVERWORLD: break
    g.run(4, 'B'); g.run(40)
g.run(60); outcome = ram(MAPSYM['gBattleOutcome'], 1)[0]
g.run(120); shot('after the battle')
party_after = ram(MAPSYM['gPlayerPartyCount'], 1)[0]
check('the Wimpod is %s: the quest step is done' % ('caught' if CATCH else 'beaten'), flag('FLAG_DR_WIMPOD_DONE'))
if CATCH: check('the outcome was a catch, the Wimpod joined the party', outcome == 7 and party_after == party_before + 1, (outcome, party_before, party_after))
# 5. the reward
go_wild('PellucaCity', (38, 36)); g.run(12, 'DOWN'); g.run(260)
go_wild('PellucaHarbour', (39, 25)); face('DOWN'); say('the reward', pages=8)
key = struct.unpack('<I', ram(sb(2) + SB2_ENCKEY, 4))[0] & 0xFFFF
items = [struct.unpack('<HH', ram(sb(1) + SB1_KEYITEMS + i * 4, 4)) for i in range(30)]
check('the Old Rod is in the bag', any(it == const('ITEM_OLD_ROD') for it, q in items))
check('the reward is recorded', flag('FLAG_DR_RECEIVED_OLD_ROD'))
go_wild('PellucaHarbour', (39, 25)); face('DOWN'); say('the fisherman afterwards')
print('ALL OK' if ok_all else 'PROBLEM')
sheet(OUT, cols=4)
