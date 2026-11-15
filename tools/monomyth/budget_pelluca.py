import sys,pickle,numpy as np
sys.path.insert(0,'/home/claude/repo/tools/monomyth')
from romlib import *
from render import tiles_of, pals_of
H={h['addr']:h for h in pickle.load(open('/home/claude/mono/headers.pkl','rb'))}
WA,FE=0x869580,0x86960c
B=[('Academy: WA hall',WA,(18,26,24,33)),('Cadmus: WA turret house',WA,(5,28,11,32)),
   ('Lab: WA stone tower',WA,(15,10,20,14)),('Residence: WA timber house',WA,(5,20,11,24)),
   ('Tavern: FE lodge G',FE,(37,40,44,47)),('Guardhouse: FE keep gate',FE,(27,12,34,18)),
   ('Residence: FE red house',FE,(4,40,10,45)),('Residence: FE steep house',FE,(16,39,22,45))]
cache={}
def ctx(a):
    if a not in cache:
        L=H[a]['layout']; pp=pals_of(L['primary']); sp=pals_of(L['secondary'])
        cache[a]=(L,tiles_of(L['primary']),tiles_of(L['secondary']),[pp[i] if i<6 else sp[i] for i in range(16)])
    return cache[a]
def quad_rgb(entries,ctxv):
    L,pt,st,pal=ctxv; img=np.full((8,8,3),-1,int)
    for e in entries:
        tid,xf,yf,sl=e&0x3ff,(e>>10)&1,(e>>11)&1,e>>12
        if tid==0: continue
        t=pt[tid] if tid<512 else st[tid-512]
        if xf: t=t[:,::-1]
        if yf: t=t[::-1]
        for y in range(8):
            for x in range(8):
                if t[y,x]: img[y,x]=pal[sl][t[y,x]]
    return img
def canon(img):
    vs=[img,img[:,::-1],img[::-1],img[::-1,::-1]]
    return min(v.tobytes() for v in vs)
allt=set(); allc=set(); rows=[]
for name,a,(x0,y0,x1,y1) in B:
    c=ctx(a); L=c[0]; mo=off(L['map']); W=L['w']; T=set(); cols=set()
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            mid=u16(mo+(y*W+x)*2)&0x3ff
            base=off(L['primary']['mt'])+mid*24 if mid<512 else off(L['secondary']['mt'])+(mid-512)*24
            e=[u16(base+i*2) for i in range(12)]
            for q in range(4):
                low=quad_rgb([e[q],e[4+q]],c); top=quad_rgb([e[8+q]],c)
                for im in (low,top):
                    if (im>=0).any():
                        T.add(canon(im)); cols.update(map(tuple,im.reshape(-1,3)[(im.reshape(-1,3)>=0).all(1)]))
    rows.append((name,(x1-x0+1)*(y1-y0+1),len(T),len(cols))); allt|=T; allc|=cols
for r in rows: print('%-28s cells %3d  unique 8x8 tiles %4d  colours %3d'%r)
print('ALL eight buildings: unique tiles',len(allt),' unique colours',len(allc))

# --- tighten: drop ground/fill tiles (images common across the whole source map)
from collections import Counter
def mapfreq(a):
    c=ctx(a); L=c[0]; mo=off(L['map']); W=L['w']; f=Counter()
    for i in range(W*L['h']):
        mid=u16(mo+i*2)&0x3ff
        base=off(L['primary']['mt'])+mid*24 if mid<512 else off(L['secondary']['mt'])+(mid-512)*24
        e=[u16(base+k*2) for k in range(12)]
        for q in range(4):
            for im in (quad_rgb([e[q],e[4+q]],c),quad_rgb([e[8+q]],c)):
                if (im>=0).any(): f[canon(im)]+=1
    return f
FQ={a:mapfreq(a) for a in (WA,FE)}
print('\nexcluding tiles placed >=40 times map-wide (ground fill):')
allt=set(); per={}
for name,a,(x0,y0,x1,y1) in B:
    c=ctx(a); L=c[0]; mo=off(L['map']); W=L['w']; T=set()
    for y in range(y0,y1+1):
        for x in range(x0,x1+1):
            mid=u16(mo+(y*W+x)*2)&0x3ff
            base=off(L['primary']['mt'])+mid*24 if mid<512 else off(L['secondary']['mt'])+(mid-512)*24
            e=[u16(base+i*2) for i in range(12)]
            for q in range(4):
                for im in (quad_rgb([e[q],e[4+q]],c),quad_rgb([e[8+q]],c)):
                    if (im>=0).any():
                        k=canon(im)
                        if FQ[a][k]<40: T.add(k)
    per[name]=T; allt|=T; print('%-28s %4d'%(name,len(T)))
print('ALL:',len(allt))
wa_only=set().union(*[per[n] for n,a,_ in B if a==WA]); print('WA four only:',len(wa_only))
