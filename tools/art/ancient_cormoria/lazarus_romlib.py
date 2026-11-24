import struct
ROM=open('/home/claude/lazarus/Lazarus.gba','rb').read()
def u32(o): return struct.unpack_from('<I',ROM,o)[0]
def u16(o): return struct.unpack_from('<H',ROM,o)[0]
def isptr(v): return 0x08000000<=v<0x08000000+len(ROM)
def off(v): return v-0x08000000
def enc(s):
    out=[]
    for ch in s:
        if ch==' ': out.append(0)
        elif 'A'<=ch<='Z': out.append(0xBB+ord(ch)-65)
        elif 'a'<=ch<='z': out.append(0xD5+ord(ch)-97)
        elif '0'<=ch<='9': out.append(0xA1+ord(ch)-48)
        elif ch=='.': out.append(0xAD)
        elif ch=="'": out.append(0xB4)
        elif ch=='-': out.append(0xAE)
    return bytes(out)
DEC={0:' ',0xAD:'.',0xB4:"'",0xAE:'-',0xFF:'$'}
for i in range(26): DEC[0xBB+i]=chr(65+i); DEC[0xD5+i]=chr(97+i)
for i in range(10): DEC[0xA1+i]=chr(48+i)
def dec(o,n=40):
    s=''
    for b in ROM[o:o+n]:
        if b==0xFF: break
        s+=DEC.get(b,'?')
    return s
def tileset(p):
    if not isptr(p): return None
    o=off(p)
    if (ROM[o] & 1) not in (0,1) or ROM[o+2] not in (0,) and False: return None
    tiles,pals,mt,attr=(u32(o+4),u32(o+8),u32(o+12),u32(o+16))
    if not all(isptr(x) for x in (tiles,pals,mt,attr)): return None
    return dict(addr=p,compressed=ROM[o]&1,secondary=(ROM[o]>>4)&1 if ROM[o]>1 else ROM[o+1],tiles=tiles,pals=pals,mt=mt,attr=attr,cb=u32(o+20))
def layout(p):
    if not isptr(p) or p&3: return None
    o=off(p); w,h=struct.unpack_from('<ii',ROM,o)
    if not (1<=w<=300 and 1<=h<=300): return None
    b,m,pt,st=(u32(o+8),u32(o+12),u32(o+16),u32(o+20))
    if not (isptr(b) and isptr(m)): return None
    P=tileset(pt); S=tileset(st)
    if not P or not S: return None
    return dict(addr=p,w=w,h=h,border=b,map=m,primary=P,secondary=S,bw=ROM[o+24],bh=ROM[o+25])
def find_headers():
    out=[]
    for o in range(0,len(ROM)-0x1c,4):
        v=u32(o)
        if not isptr(v) or v&3: continue
        if not (isptr(u32(o+4)) and isptr(u32(o+8))): continue
        c=u32(o+12)
        if c and not isptr(c): continue
        L=layout(v)
        if L: out.append(dict(addr=o,layout=L,music=u16(o+16),layout_id=u16(o+18),mapsec=ROM[o+20],weather=ROM[o+22],maptype=ROM[o+23]))
    return out
