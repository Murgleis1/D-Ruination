import sys,struct,numpy as np
sys.path.insert(0,'/home/claude/lazlib')
from romlib import *
from PIL import Image
def lz77(o):
    assert ROM[o]==0x10, hex(ROM[o])
    size=ROM[o+1]|ROM[o+2]<<8|ROM[o+3]<<16; o+=4; out=bytearray()
    while len(out)<size:
        flags=ROM[o]; o+=1
        for bit in range(8):
            if len(out)>=size: break
            if flags&(0x80>>bit):
                b1,b2=ROM[o],ROM[o+1]; o+=2
                n=(b1>>4)+3; d=((b1&15)<<8|b2)+1
                for _ in range(n): out.append(out[-d])
            else: out.append(ROM[o]); o+=1
    return bytes(out)
def tiles_of(ts):
    raw=lz77(off(ts['tiles'])) if ts['compressed'] else None
    if raw is None: raise ValueError('uncompressed tiles: size unknown')
    n=len(raw)//32; a=np.frombuffer(raw,np.uint8).reshape(n,32)
    t=np.zeros((n,8,8),np.uint8); t[:,:,0::2]=(a&15).reshape(n,8,4); t[:,:,1::2]=(a>>4).reshape(n,8,4)
    return t
def pals_of(ts):
    o=off(ts['pals']); P=[]
    for i in range(16):
        P.append([((v&31)<<3,((v>>5)&31)<<3,((v>>10)&31)<<3) for v in struct.unpack_from('<16H',ROM,o+i*32)])
    return P
NPT=512  # tiles in primary; verified per-map below
NPM=512  # metatiles in primary
MS=24
class TS:
    def __init__(s,L):
        s.pt=tiles_of(L['primary']); s.st=tiles_of(L['secondary'])
        pp=pals_of(L['primary']); sp=pals_of(L['secondary'])
        s.pal=[pp[i] if i<6 else sp[i] for i in range(16)]
        s.pmt=off(L['primary']['mt']); s.smt=off(L['secondary']['mt']); s.cache={}
    def tile(s,tid): 
        if tid<NPT: return s.pt[tid] if tid<len(s.pt) else None
        t=tid-NPT; return s.st[t] if t<len(s.st) else None
    def meta(s,mid):
        if mid in s.cache: return s.cache[mid]
        base=s.pmt+mid*MS if mid<NPM else s.smt+(mid-NPM)*MS
        img=np.zeros((16,16,3),np.uint8); img[:]=s.pal[0][0]
        for q in range(MS//2):
            e=u16(base+q*2); tid,xf,yf,sl=e&0x3ff,(e>>10)&1,(e>>11)&1,e>>12
            t=s.tile(tid)
            if t is None: continue
            if xf: t=t[:,::-1]
            if yf: t=t[::-1,:]
            oy,ox=((q%4)//2)*8,((q%4)%2)*8
            for y in range(8):
                for x in range(8):
                    if t[y,x] or q<4: img[oy+y,ox+x]=s.pal[sl][t[y,x]] if t[y,x] else s.pal[0][0]
        s.cache[mid]=img; return img
def render_map(h,out):
    L=h['layout']; ts=TS(L); W,Hh=L['w'],L['h']; mo=off(L['map'])
    img=np.zeros((Hh*16,W*16,3),np.uint8); ids=[]
    for y in range(Hh):
        for x in range(W):
            mid=u16(mo+(y*W+x)*2)&0x3ff; ids.append(mid)
            img[y*16:y*16+16,x*16:x*16+16]=ts.meta(mid)
    Image.fromarray(img).save(out)
    return ids,ts
