import sys, os, struct, numpy as np, json
sys.path.insert(0,'/home/claude/repo/tools/odyssey'); sys.path.insert(0,'/home/claude/scratch/cavestudy')
import frlib
from frrender import render, map_cells, TS
exec(open('/home/claude/scratch/cavestudy/study.py').read().split('# --- MonoMyth')[0])
tag=sys.argv[1]; gptr=int(sys.argv[2],16); picks=json.loads(sys.argv[3])
starts=[frlib.u32(frlib.off(gptr)+4*g) for g in range(45)]
for g,n in picks:
    L=frlib.layout(frlib.u32(frlib.off(frlib.u32(frlib.off(starts[g])+4*n))))
    ts=TS(L); c=np.array(map_cells(L)).reshape(L['h'],L['w'])
    col=((c>>10)&3)>0
    b=np.vectorize(lambda v: ts.attr(v&0x3ff)&0x1ff)(c)
    water=np.isin(b,[0x10,0x11,0x12,0x13,0x15,0x16,0x17,0x19,0x1a])
    metrics(f'{tag}_{g}_{n}', ~col & ~water, water, render(L))
json.dump(res,open(f'/home/claude/scratch/cavestudy/{tag}.json','w'))
