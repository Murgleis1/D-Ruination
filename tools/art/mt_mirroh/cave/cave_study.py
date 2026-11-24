import sys, os, struct, numpy as np, json
from scipy import ndimage as nd
from PIL import Image, ImageDraw
OUT='/home/claude/scratch/cavestudy'
res=[]
def metrics(name, walk, water, img):
    ys,xs=np.nonzero(walk|water)
    if len(ys)==0: return
    y0,y1,x0,x1=ys.min(),ys.max()+1,xs.min(),xs.max()+1
    w=walk[y0:y1,x0:x1]; wa=water[y0:y1,x0:x1]
    d=nd.distance_transform_cdt(np.pad(w,1),metric='chessboard')[1:-1,1:-1]
    dv=d[w]
    lab,n=nd.label(~w & ~wa)
    sizes=nd.sum(np.ones_like(lab),lab,range(1,n+1))
    # islands: solid components not touching the bbox edge
    edge=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))
    isl=[i+1 for i in range(n) if (i+1) not in edge]
    r=dict(name=name, area=int(w.sum()), open_frac=round(float(w.mean()),3), med_d=float(np.median(dv)),
           wide=round(float((dv>=4).mean()),3), islands_per100=round(100*len(isl)/max(1,w.sum()),2),
           water=int(wa.sum()))
    res.append(r)
    Image.fromarray(img[y0*16:y1*16,x0*16:x1*16]).save(f'{OUT}/{name}.png')
# --- MonoMyth
sys.path.insert(0,'/home/claude/repo/tools/art/mt_mirroh'); sys.path.insert(0,'/home/claude/mono')
import mm_render as MR
from romlib import u16, off
MM={'mt_thunder_608':0x86d608,'mt_thunder_640':0x86d640,'mt_thunder_65c':0x86d65c,'mt_thunder_6cc':0x86d6cc,'mt_thunder_73c':0x86d73c,
    'barbed_e050':0x86e050,'barbed_e06c':0x86e06c,'blazing_e088':0x86e088,'oasis_d7e4':0x86d7e4,'reservoir_dee4':0x86dee4,
    'barbed2_ca70':0x86ca70,'oldbay_bf2c':0x86bf2c,'saltpeter_be14':0x86be14,'flooded_bf9c':0x86bf9c,'grotto_dde8':0x86dde8}
for n,a in MM.items():
    img,c,ts,L=MR.render(a); W,H=L['w'],L['h']
    sa,pa=off(L['secondary']['attr']),off(L['primary']['attr'])
    beh=lambda m:(u16(sa+2*(m-512)) if m>=512 else u16(pa+2*m))&0xff
    c=np.array(c).reshape(H,W)
    col=((c>>10)&3)>0; b=np.vectorize(lambda v: beh(v&0x3ff))(c)
    water=np.isin(b,[0x10,0x11,0x12,0x13,0x15,0x16,0x17,0x19,0x1a])
    metrics('mm_'+n, ~col & ~water, water, img)
json.dump(res,open(f'{OUT}/mm.json','w'))
