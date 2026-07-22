#!/usr/bin/env python3
"""RMXP-Essentials charset (128x192; 4x4 of 32x48; rows down/left/right/up, col0=stand)
   -> pokeemerald overworld sprite (144x32; nine 16x32 frames; index-0 transparent),
   matching Osrid's format (~16x20 sprite, bottom-aligned, 16 colors)."""
from PIL import Image

SRC = 'graphics/object_events/pics/people'
FW, FH, CONTENT_H = 16, 32, 20
DIR_ROW = {'S': 0, 'W': 1, 'N': 3}          # source rows (row2=right unused; east=west flipped in-engine)
STILL, STEPA, STEPB = 0, 1, 3               # source columns
# pokeemerald frame order (matches Osrid: 0-2 still S/N/W, 3-4 S steps, 5-6 N steps, 7-8 W steps)
FRAMES = [('S',STILL),('N',STILL),('W',STILL),('S',STEPA),('S',STEPB),
          ('N',STEPA),('N',STEPB),('W',STEPA),('W',STEPB)]

def quantize_idx0(rgba, ncolors=16):
    a = rgba.getchannel('A'); rgb = rgba.convert('RGB')
    q = rgb.quantize(colors=ncolors-1, method=Image.Quantize.MEDIANCUT)  # indices 0..14
    pal = q.getpalette()[:(ncolors-1)*3]
    out = Image.new('P', rgba.size, 0)
    out.putpalette([0,0,0] + pal + [0]*(768-3-len(pal)))
    qp, ap, op = q.load(), a.load(), out.load()
    for y in range(rgba.height):
        for x in range(rgba.width):
            op[x,y] = 0 if ap[x,y] < 128 else qp[x,y] + 1
    out.info['transparency'] = 0
    return out

def convert(name):
    im = Image.open(f'{SRC}/{name}_ow_essentials.png').convert('RGBA')
    W,H = im.size; cw,ch = W//4, H//4
    cells, boxes = {}, []
    for d,r in DIR_ROW.items():
        for c in (STILL,STEPA,STEPB):
            cell = im.crop((c*cw, r*ch, c*cw+cw, r*ch+ch)); cells[(d,c)] = cell
            bb = cell.getbbox()
            if bb: boxes.append(bb)
    x0=min(b[0] for b in boxes); y0=min(b[1] for b in boxes)
    x1=max(b[2] for b in boxes); y1=max(b[3] for b in boxes)
    sw,sh = x1-x0, y1-y0
    scale = CONTENT_H/sh; nw = max(1,round(sw*scale)); nh = CONTENT_H
    if nw > FW: scale = FW/sw; nw = FW; nh = max(1,round(sh*scale))
    sheet = Image.new('RGBA', (FW*9, FH), (0,0,0,0))
    for i,(d,c) in enumerate(FRAMES):
        spr = cells[(d,c)].crop((x0,y0,x1,y1)).resize((nw,nh), Image.NEAREST)
        sheet.alpha_composite(spr, (i*FW + (FW-nw)//2, FH-nh))
    out = quantize_idx0(sheet, 16)
    out.save(f'{SRC}/{name}.png')
    return f'{name}.png {out.size}  src_sprite {sw}x{sh} -> {nw}x{nh}'

names = ['cadmus','eden','glaive','baradus','kimaris','ambrose']
for n in names: print(convert(n))

# enlarged verification sheet: all 6 x 9 frames at 5x
S = 5
grid = Image.new('RGBA', (FW*9*S, FH*S*len(names)), (36,38,46,255))
for row,n in enumerate(names):
    spr = Image.open(f'{SRC}/{n}.png').convert('RGBA')
    grid.alpha_composite(spr.resize((spr.width*S, spr.height*S), Image.NEAREST), (0, row*FH*S))
grid.convert('RGB').save('/home/claude/ow_preview.png')
print('preview -> /home/claude/ow_preview.png (rows: '+', '.join(names)+')')
