"""The great window's central light: Arceus in true stained glass, from the user's design.
User 2026-11-23: "look at the original Arceus I shared, look at each color on it, then replace that pixel with the
appropriately colored stained glass cell"; and, on a try that matched by nearest colour: Empire's gold cells are
(240,184,48)/(243,192,39), not khaki; the white skin and the background cells too must be Empire's glass.
So each pixel of the design (registered on the nave mock: scale 2.13, offset (32, 12.5), sampled per game pixel) is
read for WHAT it is, then given Empire's own glass for that:
- dark (luminance < 70) -> Empire's lead (12,13,18); lone lead specks are dropped (hairlines broken by scaling);
- by hue and saturation -> a glass family: white (Arceus's body), pale (the halo's cream), yellow (the rays), gold
  (the wheel, the hooves), blue, red, green (eyes, jewels);
- within a family, the design's lightness picks the shade (its quantiles over the light), dark -> light.
Every family's shades are exact colours found in Empire's windows (the great window and its tileset's glass), so
nothing is a blend. The light and the arch above it are filled solid between their frames (none of the old figure's
lead survives); the arch is taken row by row and can only narrow toward its tip; the side lights stay Empire's.
Usage: python3 arceus_glass.py MOCK.png OUT.png [LEAD_THRESHOLD]"""
import os
import numpy as np, sys, colorsys
from PIL import Image, ImageDraw
from collections import Counter
REPO=os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..','..'))
EMP=os.path.join(REPO,'assets/templar_hq_reference/empire')+'/'
S,OX,OY=2.13,32.0,12.5; X0,X1,Y0,Y1=104,232,0,128; CX0,CX1,ARCH=137,202,34
LEAD=(12,13,18)
STONE={(182,172,146),(192,182,156),(196,186,160),(200,190,164),(112,104,86),(132,105,66),(148,105,74),(88,80,70),(54,45,24),(38,32,17),(33,32,33),(0,0,0)}
lum=lambda a:.30*a[...,0]+.59*a[...,1]+.11*a[...,2]
# Empire's glasses, by family, dark -> light (every one found in Empire's windows)
FAM={
 'white': [(139,148,183),(189,182,197),(202,202,200),(229,227,231),(255,255,254)],
 'pale':  [(250,235,196),(255,253,182),(255,255,228)],
 'yellow':[(248,221,14),(255,241,19),(255,255,60)],
 'gold':  [(186,88,21),(240,184,48),(243,192,39),(248,221,14)],
 'blue':  [(28,44,143),(26,60,145),(7,82,172),(20,103,193),(5,124,198),(61,187,234)],
 'red':   [(142,24,27),(200,27,28),(224,36,29)],
 'green': [(12,125,108)],
}
MOCK,OUT=sys.argv[1],sys.argv[2]
T=float(sys.argv[3]) if len(sys.argv)>3 else 70
m=np.array(Image.open(MOCK).convert('RGB')).astype(int)
win=m[Y0:Y1,X0:X1]
is_stone=np.array([[tuple(p) in STONE for p in r] for r in win])
glass=np.zeros(win.shape[:2],bool)
for y in range(win.shape[0]):
    xs=np.nonzero(~is_stone[y])[0]
    if len(xs): glass[y,xs.min():xs.max()+1]=True
glass&=~is_stone
xx=np.arange(X0,X1)[None]; yy=np.arange(Y0,Y1)[:,None]
r0=glass&(((xx>=CX0)&(xx<CX1))|(yy<ARCH))
region=np.zeros_like(r0)
for y in range(r0.shape[0]):
    xs=np.nonzero(r0[y])[0]
    if len(xs): region[y,xs.min():xs.max()+1]=True
ax=(CX0+CX1)//2-X0; inside=np.zeros_like(region)
wallc={tuple(p) for p in win[0:ARCH,0:8].reshape(-1,3)}|{tuple(p) for p in win[0:ARCH,-8:].reshape(-1,3)}
bright=(lum(win)>60)&~np.array([[tuple(p) in wallc for p in r] for r in win])
for y in range(ARCH):
    xs=np.nonzero(bright[y])[0]; xs=xs[np.abs(xs-ax)<=35]
    if len(xs): inside[y,xs.min():xs.max()+1]=True
# an arch only narrows toward its tip: no row wider than the row below it
for y in range(ARCH-2,-1,-1):
    inside[y]&=inside[y+1] if inside[y+1].any() else False
region&=inside|(yy>=ARCH)
u=Image.open(EMP+'user_arceus_window_mockup.png').convert('RGB'); pad=Image.new('RGB',(u.size[0]+200,u.size[1]+200)); pad.paste(u,(100,100))
smp=np.array(pad.resize((X1-X0,Y1-Y0),Image.BOX,box=tuple(v+100 for v in (X0*S-OX,Y0*S-OY,X1*S-OX,Y1*S-OY)))).astype(int)
H,W=smp.shape[:2]
fam=np.empty((H,W),object); val=np.zeros((H,W))
for y in range(H):
    for x in range(W):
        r,g,b=smp[y,x]/255.; h,s,v=colorsys.rgb_to_hsv(r,g,b); h*=360; val[y,x]=v
        if lum(smp[y,x])<T: f='lead'
        elif s<0.20: f='white'
        elif 38<=h<75 and s<0.50 and v>0.78: f='pale'
        elif 46<=h<75 and v>=0.72: f='yellow'
        elif 15<=h<75: f='gold'
        elif 75<=h<170: f='green'
        elif 170<=h<290: f='blue'
        else: f='red'
        fam[y,x]=f
# lone specks of a family (no 8-neighbour of the same family) take their neighbours' family
for _ in range(2):
    f2=fam.copy()
    for y in range(H):
        for x in range(W):
            if not region[y,x]: continue
            nb=[fam[yy_,xx_] for yy_ in range(max(0,y-1),min(H,y+2)) for xx_ in range(max(0,x-1),min(W,x+2)) if (yy_,xx_)!=(y,x)]
            if fam[y,x] not in nb: f2[y,x]=Counter(nb).most_common(1)[0][0]
    fam=f2
out=win.copy()
for f,shades in FAM.items():
    sel=(fam==f)&region
    if not sel.any(): continue
    vs=val[sel]; n=len(shades)
    qs=np.quantile(vs,np.linspace(0,1,n+1)[1:-1]) if n>1 else []
    k=np.searchsorted(qs,val[sel]) if n>1 else np.zeros(sel.sum(),int)
    out[sel]=np.array(shades)[k]
out[(fam=='lead')&region]=LEAD
o=m.copy(); o[Y0:Y1,X0:X1]=out
Image.fromarray(o.astype(np.uint8)).save(OUT)
Image.fromarray(o.astype(np.uint8)).resize((o.shape[1]*2,o.shape[0]*2),Image.NEAREST).save(OUT.replace('.png','_2x.png'))
a=Image.fromarray(smp.astype(np.uint8)); b=Image.fromarray(out.astype(np.uint8))
c=Image.new('RGB',(W*2+4,H),(20,20,20)); c.paste(a,(0,0)); c.paste(b,(W+4,0))
c.resize((c.size[0]*4,c.size[1]*4),Image.NEAREST).save(OUT.replace('.png','_vs_design.png'))
print(Counter(fam[region]).most_common())
