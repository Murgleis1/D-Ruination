import sys,numpy as np
sys.path.insert(0,'/home/claude/scratch'); exec(open('budget.py').read().split('# --- tighten')[0].replace("for r in rows: print","for r in []: print").replace("print('ALL eight","0 and print('ALL eight"))
from PIL import Image
ev=np.array(Image.open('/home/claude/repo/assets/pelluca_tileset_source/Evernahn.png').convert('RGBA'))
def ev_tiles(r0,r1,c0,c1):
    a=ev[r0*32:(r1+1)*32, c0*32:(c1+1)*32]; h,w=a.shape[0]//2,a.shape[1]//2
    out=np.full((h,w,3),-1,int)
    for y in range(h):
        for x in range(w):
            blk=a[y*2:y*2+2,x*2:x*2+2].reshape(-1,4); op=blk[blk[:,3]>0]
            if len(op)>=2:
                u,c=np.unique(op[:,:3],axis=0,return_counts=True); out[y,x]=u[c.argmax()]
    T=set(); cols=set()
    for y in range(0,h,8):
        for x in range(0,w,8):
            t=out[y:y+8,x:x+8]
            if (t>=0).any(): T.add(canon(t)); cols.update(map(tuple,t.reshape(-1,3)[(t.reshape(-1,3)>=0).all(1)]))
    return T,cols
ch,chc=ev_tiles(17,26,0,6); oh,ohc=ev_tiles(99,104,0,4)
print('Evernahn church (r17-26 c0-c6): tiles',len(ch),'colours',len(chc))
print('Evernahn Osrid house (r99-104 c0-c4): tiles',len(oh),'colours',len(ohc))
from PIL import Image as I
e=I.open('/home/claude/repo/codebase/data/tilesets/primary/evernahn/tiles.png'); print('gTileset_Evernahn tiles.png',e.size,'=',e.size[0]*e.size[1]//64,'tile slots')
# Wood Avens terrain+props: whole map minus the 4 building crops
c=ctx(WA); L=c[0]; mo=off(L['map']); W=L['w']; T=set()
crops=[b[2] for b in B if b[1]==WA]
for y in range(L['h']):
    for x in range(W):
        if any(x0<=x<=x1 and y0<=y<=y1 for x0,y0,x1,y1 in crops): continue
        mid=u16(mo+(y*W+x)*2)&0x3ff
        base=off(L['primary']['mt'])+mid*24 if mid<512 else off(L['secondary']['mt'])+(mid-512)*24
        e2=[u16(base+i*2) for i in range(12)]
        for q in range(4):
            for im in (quad_rgb([e2[q],e2[4+q]],c),quad_rgb([e2[8+q]],c)):
                if (im>=0).any(): T.add(canon(im))
print('Wood Avens terrain+props (whole map minus buildings): tiles',len(T))
