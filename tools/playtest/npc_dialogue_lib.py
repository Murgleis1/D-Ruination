import sys, gzip, numpy as np
sys.path.insert(0, '/home/claude/scratch/dorm')
from walklib import GBA, go as _go, where, step
from PIL import Image, ImageDraw
g = GBA('/home/claude/repo/codebase/pokeemerald.gba')
import os
ST=os.environ.get('ST','/home/claude/scratch/r11/pelluca_west.state'); g.restore(gzip.decompress(open(ST, 'rb').read())); g.run(20)
shots = []
def shot(n): shots.append((n, g.frame().copy()))
def go(m, t, tries=4):
    for _ in range(tries):
        if _go(g, m, t, log=lambda *a: None): return True
        for _ in range(10): g.run(6, 'B'); g.run(10)
    return False
def face(d): g.run(3, d); g.run(10)
def boxopen(f):
    r=f[126:152, 24:216].astype(int)
    return ((r.min(axis=2)>235).mean() > 0.55) and (r.max(axis=2)<160).mean() > 0.02
def talk(label, maxpages=8):
    g.run(2,'A'); g.run(4); 
    for p in range(maxpages):
        g.run(150)
        f = g.frame().copy()
        if not boxopen(f): break
        shots.append(('%s p%d' % (label, p+1), f))
        g.run(2,'A'); g.run(6)
    for _ in range(4): g.run(2,'B'); g.run(20)
def sheet(path, cols=4):
    if not shots: print('no shots'); return
    S = Image.new('RGB', (240*cols, 172*((len(shots)+cols-1)//cols))); d = ImageDraw.Draw(S)
    for k,(n,f) in enumerate(shots):
        S.paste(Image.fromarray(f), ((k%cols)*240, (k//cols)*172+12)); d.text(((k%cols)*240+2,(k//cols)*172), n, fill=(255,255,0))
    S.save(path); print('saved', path, len(shots))
import struct as _st
from walklib import Grid
EWB=0x021000
def objs():
    st=bytes(g.state()); out={}
    for i in range(16):
        b=EWB+(0x02001888-0x02000000)+i*0x24
        if not st[b]&1: continue
        lid=st[b+8]; x,y=_st.unpack_from('<hh',st,b+0x10); out[lid]=(x-7,y-7,bool(st[b+2]&1))
    return out
def chase(m, lid, label, tries=8, near=None):
    G=Grid(m)
    if near: go(m,near,tries=2)
    for _ in range(tries):
        o=objs().get(lid)
        if not o: print('no obj',lid); return False
        x,y,_p=o
        for dx,dy,d in [(0,1,'UP'),(1,0,'LEFT'),(-1,0,'RIGHT'),(0,-1,'DOWN')]:
            t=(x+dx,y+dy)
            if t in G.cell and G.ok(t,()) or where(g)[0]==t:
                if go(m,t,tries=2):
                    face(d); g.run(2,'A'); g.run(6); g.run(130)
                    if boxopen(g.frame()):
                        shots.append(('%s p1'%label,g.frame().copy()))
                        for p in range(2,7):
                            g.run(2,'A'); g.run(150)
                            if not boxopen(g.frame()): break
                            shots.append(('%s p%d'%(label,p),g.frame().copy()))
                        for _ in range(4): g.run(2,'B'); g.run(20)
                        return True
                    for _ in range(3): g.run(2,'B'); g.run(10)
                break
        g.run(40)
    print('missed',label); return False
