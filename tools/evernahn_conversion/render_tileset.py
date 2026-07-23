#!/usr/bin/env python3
"""
Render any pokeemerald tileset to a PNG for present_files (the image viewer has
been blind this whole project - this is how visual work gets checked).

Usage from repo root:
  python3 tools/evernahn_conversion/render_tileset.py <primary_dir> [secondary_dir] [out.png]

Renders every metatile with palette/flip applied, numbered, to /home/claude/<name>_render.png.
Primary sub-palettes are 0-5; a secondary's own palettes occupy 6-12
(NUM_PALS_IN_PRIMARY = 6). Pass both dirs to render a secondary correctly.
"""
import sys, os, struct
import numpy as np
from PIL import Image, ImageDraw

NUM_PALS_IN_PRIMARY = 6

def gp(D, i):
    p = '%s/palettes/%02d.gbapal' % (D, i)
    if not os.path.exists(p): return [(255,0,255)]*16
    d = open(p,'rb').read()
    return [(((v&31)<<3),(((v>>5)&31)<<3),(((v>>10)&31)<<3))
            for v in (struct.unpack_from('<H', d, 2*j)[0] for j in range(16))]

def main():
    prim = sys.argv[1]
    sec  = sys.argv[2] if len(sys.argv) > 2 and os.path.isdir(sys.argv[2]) else None
    name = os.path.basename(prim.rstrip('/'))
    out  = sys.argv[-1] if sys.argv[-1].endswith('.png') else '/home/claude/%s_render.png' % name

    P = []
    for i in range(16):
        D = prim if i < NUM_PALS_IN_PRIMARY else (sec or prim)
        idx = i if i < NUM_PALS_IN_PRIMARY else i  # secondary palettes stored 06..
        P.append(gp(D, idx))
    P = np.array(P, np.uint8)

    ptiles = np.array(Image.open(prim+'/tiles.png').convert('P'))
    stiles = np.array(Image.open(sec+'/tiles.png').convert('P')) if sec else None
    ptpr = ptiles.shape[1]//8
    def tget(t):
        if t < 512:
            r=(t//ptpr)*8; c=(t%ptpr)*8; src=ptiles
        else:
            t-=512; tpr=stiles.shape[1]//8; r=(t//tpr)*8; c=(t%tpr)*8; src=stiles
        return src[r:r+8,c:c+8] if r+8<=src.shape[0] and c+8<=src.shape[1] else np.zeros((8,8),np.uint8)

    mt = open((sec or prim)+'/metatiles.bin','rb').read() if sec else open(prim+'/metatiles.bin','rb').read()
    n = len(mt)//16
    COLS = 16; rows = (n+COLS-1)//COLS
    cv = np.full((rows*16, COLS*16, 3), 35, np.uint8)
    for m in range(n):
        e = struct.unpack_from('<8H', mt, m*16); cell = np.zeros((16,16,3), np.uint8)
        for Ly in range(2):
            for i in range(4):
                v = e[Ly*4+i]
                if Ly and not (v & 0x3FF): continue
                idx = tget(v & 0x3FF); col = P[(v>>12)&15][idx]
                ty=(i//2)*8; tx=(i%2)*8
                if Ly==0: cell[ty:ty+8,tx:tx+8]=col
                else:
                    mk=idx!=0; cell[ty:ty+8,tx:tx+8][mk]=col[mk]
        cv[(m//COLS)*16:(m//COLS)*16+16,(m%COLS)*16:(m%COLS)*16+16]=cell
    S=6
    im=Image.fromarray(cv,'RGB').resize((COLS*16*S,rows*16*S),Image.NEAREST)
    d=ImageDraw.Draw(im)
    for m in range(n): d.text(((m%COLS)*16*S+2,(m//COLS)*16*S+2),str(m),fill=(255,230,120))
    im.save(out); print('rendered %d metatiles -> %s' % (n, out))

if __name__ == '__main__':
    main()
