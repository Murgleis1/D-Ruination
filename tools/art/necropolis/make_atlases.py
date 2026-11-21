"""Atlases (cells + every metatile rendered) of FireRed-based maps, for the Necropolis mocks.
Usage: ODYSSEY_ROM=ROM python3 tools/art/necropolis/make_atlases.py GROUP_TABLE_HEX g:m:out.npz ...
Ghost Grey (table 83526A8): 1:93 -> /home/claude/scratch/necro/f1/gg_1_93.npz; Crown (table 8711468): 6:8 -> cr_6_8.npz."""
import os,sys,struct,numpy as np
sys.path.insert(0,'/home/claude/repo/tools/odyssey')
import frlib, frrender
from PIL import Image
def atlas(g,m,out,gt):
    R=frlib.ROM
    gp=frlib.u32(gt-0x08000000+g*4)-0x08000000; h=frlib.u32(gp+m*4)-0x08000000
    L=frlib.layout(frlib.u32(h)); ts=frrender.TS(L)
    c=np.array(frrender.map_cells(L),np.int32).reshape(L['h'],L['w'])&0x3ff
    full=np.zeros((1024,16,16,3),np.uint8)
    for mid in range(1024):
        try: full[mid]=ts.meta(mid)
        except Exception: pass
    np.savez_compressed(out,cells=c,full=full)
    img=frrender.render(L); Image.fromarray(img).save(out.replace('.npz','.png'))
    print(g,m,L['w'],L['h'])
if __name__=='__main__':
    gt=int(sys.argv[1],16)
    for spec in sys.argv[2:]:
        g,m,out=spec.split(':'); atlas(int(g),int(m),out,gt)
