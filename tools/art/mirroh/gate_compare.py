"""Side-by-side sheets for the user to choose from: the south gatehouse styles, the hallway runner colours."""
import sys; sys.path.insert(0,'.')
import numpy as np
from PIL import Image, ImageDraw
import mirroh_v3 as v3, gate_hall as gh
from mirroh_mock import Map
def scene(style, carpet):
    M=Map(); W=26; y0=6
    for y in range(18):
        for x in range(W): M.ground(x,y,v3.snow_tile(x,y),'snow')
    for x in range(W):
        for k,m in enumerate([0x272,0x20e,0x20e,0x22b if x%7==3 else 0x20e,0x20e,0x20e,0x21e]): M.ground(x,y0+k,v3.ef(m),'wall')
    x0 = 6 if style=='roof' else 4
    lo,hi=v3.CARPETS[carpet]
    v3.gatehouse(M,x0,y0,style=style,far_mat=True,tone=lambda i: v3.ramp_tone(i,lo,hi))
    v3.cobbles(M, v3.rect(11,13,14,16))
    img=M.render()[:18*16,:W*16]
    return img
def hall(carpet):
    lo,hi=v3.CARPETS[carpet]
    gh.crimson=lambda img: v3.ramp_tone(img,lo,hi)
    rows=gh.hall(); return np.vstack([np.hstack(r) for r in rows])
a=scene('roof','brown-purple'); b=scene('towers','brown-purple')
h1=hall('brown-purple'); h2=hall('copper')
S=2
def lab(img,t):
    im=Image.fromarray(img).resize((img.shape[1]*S,img.shape[0]*S),0); d=ImageDraw.Draw(im)
    d.rectangle([0,0,len(t)*7+10,16],fill=(0,0,0)); d.text((4,3),t,fill=(255,255,255)); return im
ims=[lab(a,'A  roofed (roof in the stone\'s own darks), mat behind'),lab(b,'B  spired towers (Necropolis gate family), mat behind')]
top=Image.new('RGB',(sum(i.width for i in ims)+16,max(i.height for i in ims)),(255,255,255)); x=0
for i in ims: top.paste(i,(x,0)); x+=i.width+16
top.save('/home/claude/scratch/mirroh/cmp/gates_ab.png')
ims=[lab(h1,'brownish-purple'),lab(h2,'copper')]
hh=Image.new('RGB',(sum(i.width for i in ims)+16,max(i.height for i in ims)),(255,255,255)); x=0
for i in ims: hh.paste(i,(x,0)); x+=i.width+16
hh.save('/home/claude/scratch/mirroh/cmp/hall_carpets.png')
