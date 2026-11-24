"""Render a FireRed-based ROM's map (Ghost Grey) from its header address: layout, both tilesets (LZ77 or raw)."""
import struct, numpy as np, sys
R=open(sys.argv[1] if __name__=='__main__' else '/home/claude/ghostgrey/Ghost_Grey_EX.gba','rb').read()
u32=lambda o: struct.unpack_from('<I',R,o)[0]; u16=lambda o: struct.unpack_from('<H',R,o)[0]
off=lambda v: v-0x08000000
def lz(o):
    size=R[o+1]|R[o+2]<<8|R[o+3]<<16; o+=4; out=bytearray()
    while len(out)<size:
        f=R[o]; o+=1
        for b in range(8):
            if len(out)>=size: break
            if f&(0x80>>b):
                b1,b2=R[o],R[o+1]; o+=2; n=(b1>>4)+3; d=((b1&15)<<8|b2)+1
                for _ in range(n): out.append(out[-d])
            else: out.append(R[o]); o+=1
    return bytes(out)
def ts(p, n):
    o=off(p); comp=R[o]; tiles,pals,mt,cb,attr=[u32(o+4+4*i) for i in range(5)]
    raw=lz(off(tiles)) if comp else R[off(tiles):off(tiles)+n*32]
    k=len(raw)//32; a=np.frombuffer(raw[:k*32],np.uint8).reshape(k,32)
    t=np.zeros((k,8,8),np.uint8); t[:,:,0::2]=(a&15).reshape(k,8,4); t[:,:,1::2]=(a>>4).reshape(k,8,4)
    P=[[((v&31)<<3,((v>>5)&31)<<3,((v>>10)&31)<<3) for v in struct.unpack_from('<16H',R,off(pals)+i*32)] for i in range(16)]
    return t,P,off(mt)
def render(h):
    L=off(u32(h)); W,H=u32(L),u32(L+4); m=off(u32(L+12)); pt,st=u32(L+16),u32(L+20)
    PT,PP,PM=ts(pt,640); ST,SP,SM=ts(st,384)
    pal=[PP[i] if i<7 else SP[i] for i in range(16)]
    def tile(i): return PT[i] if i<640 else (ST[i-640] if i-640<len(ST) else np.zeros((8,8),np.uint8))
    cache={}
    def meta(mi):
        if mi in cache: return cache[mi]
        base=PM+mi*16 if mi<640 else SM+(mi-640)*16
        img=np.zeros((16,16,3),np.uint8)
        for layer in (0,1):
            for k in range(4):
                e=u16(base+layer*8+k*2); t=tile(e&0x3ff)
                if e&0x400: t=t[:,::-1]
                if e&0x800: t=t[::-1]
                pp=np.array(pal[e>>12]); y,x=(k//2)*8,(k%2)*8
                if layer==0: img[y:y+8,x:x+8]=pp[t]
                else:
                    msk=t!=0; reg=img[y:y+8,x:x+8]; reg[msk]=pp[t][msk]
        cache[mi]=img; return img
    out=np.zeros((H*16,W*16,3),np.uint8)
    for y in range(H):
        for x in range(W): out[y*16:y*16+16,x*16:x*16+16]=meta(u16(m+2*(y*W+x))&0x3ff)
    return out,W,H
