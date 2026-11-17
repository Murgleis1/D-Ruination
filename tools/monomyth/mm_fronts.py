import struct, numpy as np
from PIL import Image, ImageDraw
rom=open('/home/claude/monomyth.gba','rb').read(); N=len(rom)
def lz(off):
    assert rom[off]==0x10; size=rom[off+1]|rom[off+2]<<8|rom[off+3]<<16; o=bytearray(); i=off+4
    while len(o)<size:
        f=rom[i]; i+=1
        for b in range(8):
            if len(o)>=size: break
            if f&(0x80>>b):
                x=rom[i]<<8|rom[i+1]; i+=2; n=(x>>12)+3; d=(x&0xFFF)+1
                for _ in range(n): o.append(o[-d])
            else: o.append(rom[i]); i+=1
    return bytes(o)
PIC=0x49A4A4
pics={}
NPIC=(0x49A904-PIC)//8      # the palette table follows the pic table directly
skipped=[]
for k in range(NPIC):
    p,sz,tag=struct.unpack_from('<IHH',rom,PIC+8*k)
    if 0x08000000<=p<0x08000000+N and rom[p-0x08000000]==0x10 and (rom[p-0x08000000+1]|rom[p-0x08000000+2]<<8)>=0x800: pics[k]=p-0x08000000
    else: skipped.append((k,hex(p),hex(sz)))
print('skipped',skipped[:10])
print('pics',len(pics),'last idx',k)
# palette table: {ptr->LZ(32 bytes), u16 tag, u16 pad} with tags 0,1,2...
cand=None
for off in range(PIC+8*k, min(N-16,PIC+8*k+0x4000),4):
    ok=0
    for t in range(6):
        p,tag,pad=struct.unpack_from('<IHH',rom,off+8*t)
        if 0x08000000<=p<0x08000000+N and tag==t and rom[p-0x08000000]==0x10 and rom[p-0x08000000+1]==0x20: ok+=1
    if ok==6: cand=off; break
if cand is None:
    for off in range(0x100000,N-48,4):
        ok=all((lambda p,tag,pad:(0x08000000<=p<0x08000000+N and tag==t and rom[p-0x08000000]==0x10 and rom[p-0x08000000+1]==0x20))(*struct.unpack_from('<IHH',rom,off+8*t)) for t in range(6))
        if ok: cand=off; break
print('palette table @0x%X'%cand)
pals={}
for t in range(NPIC):
    p,tag,pad=struct.unpack_from('<IHH',rom,cand+8*t)
    if not (0x08000000<=p<0x08000000+N) or rom[p-0x08000000]!=0x10 or rom[p-0x08000000+1]<0x20: continue
    raw=lz(p-0x08000000); c=[struct.unpack_from('<H',raw,2*i)[0] for i in range(16)]
    pals[t]=[((v&31)<<3,(v>>5&31)<<3,(v>>10&31)<<3) for v in c]
print('pals',len(pals))
def pic(tag):
    raw=lz(pics[tag]); a=np.zeros((64,64),int)
    for t in range(64):
        for i in range(32):
            v=raw[t*32+i]; y=(t//8)*8+i//4; x=(t%8)*8+(i%4)*2; a[y,x]=v&15; a[y,x+1]=v>>4
    return a
if __name__=='__main__':
    import pickle; out={}
    tags=sorted(t for t in pics if t in pals)
    for t in tags: out[t]=(pic(t),pals[t])
    pickle.dump(out,open('mm_trainers.pkl','wb'))
    cols=16; S=Image.new('RGB',(cols*68,((len(tags)+cols-1)//cols)*80),(30,30,36)); d=ImageDraw.Draw(S)
    for n,t in enumerate(tags):
        a,pl=out[t]; o=np.zeros((64,64,3),np.uint8); o[:]=(110,110,132)
        for i in range(1,16): o[a==i]=pl[i]
        x=(n%cols)*68; y=(n//cols)*80; S.paste(Image.fromarray(o),(x,y+14)); d.text((x+2,y+1),'#%d'%t,fill=(255,255,120))
    S.save('mm_trainers_sheet.png'); print('sheet', S.size, len(tags))
