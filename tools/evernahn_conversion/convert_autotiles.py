#!/usr/bin/env python3
"""
Convert Evernahn/Calvera autotile sources -> gTileset_Evernahn (primary).
ALREADY RUN; committed output is in codebase/data/tilesets/primary/evernahn/.
Re-run from repo root: python3 tools/evernahn_conversion/convert_autotiles.py

Roles (corrected against the user's description - filenames are misleading):
  Evernahn_Grass_3 = normal grass BASE (6 variants, NOT anim frames)
  Evernahn_Grass_1 = grass/shore edge (8 variants)
  Evernahn_Grass_2 = grass edge alt   (8 variants)
  Evernahn_Water/_2 = open water (flat single colour each)
  Calvera_Water(_Calm) = land-locked pools w/ red-brown CLAY banks. RMXP 3x4
    autotile template: slot 7 = water fill, slot 1 = unused white template
    (DROPPED), rest = clay-bank edges. Only 11 of 12 slots kept per set.
"""
import sys, os, struct
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import numpy as np
from PIL import Image
from collections import Counter, OrderedDict
import lib_convert as L

SRC = 'assets/pelluca_tileset_source'
D   = 'codebase/data/tilesets/primary/evernahn'

def tiles32(path):
    a = np.array(Image.open(path).convert('RGBA')); h, w, _ = a.shape
    return [a[ty*32:(ty+1)*32, tx*32:(tx+1)*32] for ty in range(h//32) for tx in range(w//32)]

def calvera_pieces(path):          # RMXP frame-0 3x4 block, drop white slot 1
    a = np.array(Image.open(path).convert('RGBA'))
    sel = [a[r*32:(r+1)*32, c*32:(c+1)*32] for r in range(4) for c in range(3)]
    return [t for i, t in enumerate(sel) if i != 1]

FAM = {'GRASS': ['Evernahn_Grass_3','Evernahn_Grass_1','Evernahn_Grass_2'],
       'WATER': ['Evernahn_Water','Evernahn_Water_2'],
       'POOL' : ['Calvera_Water','Calvera_Water_Calm']}
PAL = {'GRASS':0, 'WATER':1, 'POOL':2}

groups = {}
for name in ['Evernahn_Grass_3','Evernahn_Grass_1','Evernahn_Grass_2']:
    groups[name] = [L.downscale_box(t) for t in tiles32('%s/%s.png'%(SRC,name))]
for name in ['Evernahn_Water','Evernahn_Water_2']:
    groups[name] = [L.downscale_box(tiles32('%s/%s.png'%(SRC,name))[0])]
for name in ['Calvera_Water','Calvera_Water_Calm']:
    groups[name] = [L.downscale_box(t) for t in calvera_pieces('%s/%s.png'%(SRC,name))]

palettes = {}
for fam, members in FAM.items():
    cols = Counter()
    for m in members:
        for t in groups[m]:
            px = t.reshape(-1,4); px = px[px[:,3]>=128][:,:3]; cols.update(map(tuple, px.tolist()))
    uniq = [c for c, _ in cols.most_common()]
    if len(uniq) > 15:
        palettes[fam] = L.quantise_fastoctree(np.array([list(c) for c in uniq], np.uint8), 15, drop_halo=False)
    else:
        palettes[fam] = np.array([list(c) for c in uniq] + [[0,0,0]]*(15-len(uniq)), np.uint8)

tilemap = OrderedDict(); entries = []
for fam, members in FAM.items():
    pal = palettes[fam]
    for m in members:
        for t in groups[m]:
            op = t[:,:,3] >= 128; idx = np.zeros((16,16), np.uint8)
            px = t[op][:,:3].astype(int)
            if len(px):
                d = ((px[:,None,:]-pal[None,:,:].astype(int))**2).sum(2)
                idx[op] = d.argmin(1)+1
            entries.append((fam, L.split_to_tiles(idx, tilemap)))

os.makedirs(D+'/palettes', exist_ok=True)
TPR = 16; rows = (len(tilemap)+TPR-1)//TPR
sheet = np.zeros((rows*8, TPR*8), np.uint8)
for blob, i in tilemap.items():
    sheet[(i//TPR)*8:(i//TPR)*8+8, (i%TPR)*8:(i%TPR)*8+8] = np.frombuffer(blob, np.uint8).reshape(8,8)
img = Image.fromarray(sheet, 'P')
flat = [0,0,0]
for c in palettes['GRASS']: flat += [int(v) for v in c]
img.putpalette(flat[:48]); img.save(D+'/tiles.png')

for i in range(16):
    fam = {0:'GRASS',1:'WATER',2:'POOL'}.get(i)
    cols = ([(0,0,0)] + [tuple(int(v) for v in c) for c in palettes[fam]]) if fam else [(0,0,0)]*16
    L.write_gbapal('%s/palettes/%02d.gbapal'%(D,i), cols)
    L.write_jasc  ('%s/palettes/%02d.pal'%(D,i), cols)

mt = bytearray(); at = bytearray()
for fam, quad in entries:
    for t in quad: mt += L.metatile_entry(t, PAL[fam])
    for _ in range(4): mt += struct.pack('<H', 0)
    beh = 0x10 if fam in ('WATER','POOL') else 0x00       # MB_POND_WATER / MB_NORMAL
    at += L.metatile_attr(beh, 1)
open(D+'/metatiles.bin','wb').write(bytes(mt))
open(D+'/metatile_attributes.bin','wb').write(bytes(at))
print('wrote %d metatiles, %d unique tiles' % (len(entries), len(tilemap)))
