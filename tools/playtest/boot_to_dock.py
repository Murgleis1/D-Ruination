"""Boot the ROM fresh, mash A through the intro, and capture the Pelluca dock.

Use this, NOT a checkpoint, when judging tile art: a checkpoint restores the
VRAM of the ROM it was made from, so it shows the OLD tiles.
Usage: python3 -I boot_to_dock.py <rom.gba> <out_prefix>
"""
import sys,struct,numpy as np
sys.path.insert(0,'/home/claude/repo/tools/playtest')
from gba_harness import GBA
from PIL import Image
rom,out=sys.argv[1],sys.argv[2]
IW,EW=0x019000,0x021000
def loc(st):
    sb1=struct.unpack_from('<I',st,IW+(0x03006A08-0x03000000))[0]
    if not 0x02000000<=sb1<0x02040000: return None,None
    b=EW+(sb1-0x02000000)
    return struct.unpack_from('<hh',st,b), struct.unpack_from('<bb',st,b+4)
g=GBA(rom); g.run(700); g.tap('START'); g.run(120)
for i in range(3000):
    g.tap('A'); g.run(6)
    p,m=loc(bytes(g.state()))
    if m==(2,5):
        print('dock at press',i,'pos',p); break
# let the scene settle; capture a few frames while the cutscene plays
for k in range(4):
    g.run(30); f=g.frame().copy(); p,m=loc(bytes(g.state()))
    Image.fromarray(f).save(f'{out}_{k}.png'); print(k,m,p,'colours',len(np.unique(f.reshape(-1,3),axis=0)))
