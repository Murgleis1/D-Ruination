import numpy as np, struct
import sys
d=open(sys.argv[1] if len(sys.argv)>1 else '/mnt/user-data/uploads/Pokemon_MonoMyth_1.gba','rb').read()
A=np.frombuffer(d,np.uint8)
def stream(ph):
    n=(len(A)-ph)//3
    b=A[ph:ph+3*n].reshape(-1,3).astype(np.uint32)
    s=np.stack([b[:,0]>>2, ((b[:,0]&3)<<4)|(b[:,1]>>4), ((b[:,1]&15)<<2)|(b[:,2]>>6), b[:,2]&63],1)
    return s.reshape(-1).astype(np.uint8)
def tosyms(text):
    out=[]
    for c in text:
        if c==' ': out.append(0)
        elif 'a'<=c<='z': out.append(ord(c)-96)
        elif 'A'<=c<='Z': out+= [0x1b, ord(c)-64]
        elif c=='.': out.append(0x26)
        elif c==',': out.append(0x27)
    return bytes(out)
DICT=[]
tbl=0x484874
for i in range(245):
    p,l=struct.unpack_from('<II',d,tbl+8*i); DICT.append(d[p-0x08000000:p-0x08000000+l])
cs={}
for i in range(0xBB,0xD5): cs[i]=chr(ord('A')+i-0xBB)
for i in range(0xD5,0xEF): cs[i]=chr(ord('a')+i-0xD5)
for i in range(0xA1,0xAB): cs[i]=chr(ord('0')+i-0xA1)
cs.update({0:' ',0xAB:'!',0xAC:'?',0xAD:'.',0xAE:'-',0xB0:'…',0xB1:'"',0xB2:'"',0xB3:"'",0xB4:"'",0xB8:',',0xBA:'/',0xF0:':',0x1B:'é',0x36:';',0x5C:'(',0x5D:')'})
def word(i,cap):
    w=''.join(cs.get(b,'?') for b in DICT[i]) if i<len(DICT) else '<W%d>'%i
    return w[0].upper()+w[1:] if cap and w else w
def decode_syms(syms):
    out='';cap=False;mode=0;code=0
    for s in syms:
        s=int(s)
        if mode==1: code=s<<6; mode=2; continue
        if mode==2:
            code|=s; mode=0; hi=code>>8
            if hi==2: out+=word(code&0xff,cap)
            elif hi==0: out+='{FC19:%02x}'%(code&0xff)
            elif hi==1: out+='{FC1C:%02x}'%(code&0xff)
            else: out+='{?%03x}'%code
            cap=False; continue
        if 1<=s<=26: out+=chr(96+s).upper() if cap else chr(96+s); cap=False
        elif 0x1c<=s<=0x25: out+=chr(48+s-0x1c); cap=False
        elif s==0: out+=' '; cap=False
        elif s==0x1b: cap=True
        elif s==0x37: mode=1
        elif s==0x3f: out+='<END>'; break
        elif s==0x3e: out+='<3E>'; cap=False
        else:
            m={0x26:'.',0x27:',',0x28:';',0x29:'?',0x2a:'!',0x2b:'-',0x2c:':',0x2d:'/',0x2e:'(',0x2f:')',0x30:'…',0x31:'é',0x32:'\n',0x33:' ',0x34:' | ',0x35:'"',0x36:"'",0x38:'{V38}',0x39:'{V39}',0x3a:'{V3A}',0x3b:'{V3B}',0x3c:'{V3C}',0x3d:'{PLAYER}'}
            out+=m.get(s,'?'); cap=False
    return out

def dec_at(o, maxb=4000):
    syms=[]; i=o
    while i<o+maxb:
        b0,b1,b2=d[i],d[i+1],d[i+2]
        for k,s in enumerate((b0>>2, ((b0&3)<<4)|(b1>>4), ((b1&15)<<2)|(b2>>6), b2&63)):
            syms.append(s)
            if s==0x3f:
                end=i+(1,1,2,3)[k] if k else i+1
                return decode_syms(syms), end
        i+=3
    return decode_syms(syms), i
def walk(o,n):
    out=[]
    for _ in range(n):
        t,e=dec_at(o); out.append((o,t)); o=e
    return out
