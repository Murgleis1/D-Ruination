"""Render a MonoMyth map whose blockdata may be LZ77-compressed (Mt. Thunder's is: plain reads give noise). Usage: mm_render.py 86d65c ..."""
import sys, struct, numpy as np, pickle
sys.path.insert(0, '/home/claude/mono')
from romlib import *
import render as R
from PIL import Image
def cells(L):
    o = off(L['map']); W, H = L['w'], L['h']
    if ROM[o] == 0x10 and (ROM[o+1] | ROM[o+2] << 8 | ROM[o+3] << 16) == W * H * 2:
        d = R.lz77(o); return list(struct.unpack('<%dH' % (W * H), d))
    return [u16(o + 2 * i) for i in range(W * H)]
def render(addr, out=None):
    L = layout(u32(addr)); ts = R.TS(L); c = cells(L); W, H = L['w'], L['h']
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W): img[y*16:y*16+16, x*16:x*16+16] = ts.meta(c[y*W+x] & 0x3ff)
    if out: Image.fromarray(img).save(out)
    return img, c, ts, L
if __name__ == '__main__':
    for a in sys.argv[1:]: render(int(a, 16), '/home/claude/scratch/mtthunder/%s.png' % a)
