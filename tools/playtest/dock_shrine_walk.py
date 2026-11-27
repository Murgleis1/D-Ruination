"""The dock shrine (2026-11-27: MonoMyth's wayside shrine in House Umbra black, against the cliff right of the harbour's
main stair, cells (40-41, 9-10)): from the town's west gate down the main stair to the harbour; the shrine is solid
(walking up into it from below does not move the player); its inscription read from both cells below it; its keeper
at (42, 11), spoken to from below, faces the player and then turns back to the shrine. Needs pelluca_west.state."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from npc_dialogue_lib import *
HB = 'PellucaHarbour'
go('PellucaCity', (38, 36)); g.run(12, 'DOWN'); g.run(200); g.run(60); print('harbour', where(g))
for x in (40, 41):
    go(HB, (x, 11)); before = where(g)[0]; g.run(12, 'UP'); g.run(20)
    print('solid above (%d, 11):' % x, where(g)[0] == before); shot('below the shrine (%d, 11)' % x)
    talk('inscription from (%d, 11)' % x)
go(HB, (42, 12)); face('UP'); talk('the keeper'); g.run(30); shot('the keeper turns back to the shrine')
sheet('/home/claude/repo/assets/pelluca_reference/ingame_dock_shrine_walk.png', cols=4)
