import sys,struct,numpy as np
sys.path.insert(0,'/home/claude/repo/tools/playtest')
from gba_harness import GBA, load_checkpoint
from PIL import Image
IW,EW=0x019000,0x021000
def pos(st):
    sb1=struct.unpack_from('<I',st,IW+(0x03006A08-0x03000000))[0]
    if not 0x02000000<=sb1<0x02040000: return None
    b=EW+(sb1-0x02000000); return struct.unpack_from('<hh',st,b), struct.unpack_from('<bb',st,b+4)
im=Image.open('/home/claude/repo/codebase/graphics/portraits/eden_positive.png'); a=np.array(im); pal=np.array(im.getpalette()[:48]).reshape(16,3).astype(int)
want=(pal[a]//8*8); mask=a!=0
def eden(g):
    f=g.frame().astype(int); win=f[32:112,152:232]; return int(((np.abs(win-want).max(-1)>8)&mask).sum())
g=GBA('/home/claude/repo/codebase/pokeemerald.gba')
load_checkpoint(g,'/home/claude/repo/tools/playtest/checkpoints/dock_arrival.gz')
for i in range(260): g.tap('A'); g.run(10)
print('in lab at', pos(bytes(g.state())))
base=g.state()
for seq in (['LEFT','LEFT','UP','UP','UP'],['LEFT','LEFT','LEFT','UP','UP','UP'],['LEFT','LEFT','LEFT','LEFT','UP','UP','UP']):
    g.restore(base)
    for d in seq: g.walk(d,1)
    p=pos(bytes(g.state())); found=None
    for i in range(900):
        g.tap('A'); g.run(10)
        if eden(g)<20: found=i; break
    print(seq,'pos after walk',p,'eden smile found at tap',found)
    if found is not None:
        Image.fromarray(g.frame()).resize((720,480),Image.NEAREST).save('lab_eden_positive.png'); break
