"""Render FireRed-format maps and metatiles (Pokemon Odyssey). 2-layer metatiles, 640 primary tiles/metatiles,
palettes 0-6 primary, 7-12 secondary."""
import os, sys, struct
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from frlib import ROM, off, isptr, u32

def lz77(o):
    assert ROM[o] == 0x10, hex(ROM[o])
    size = ROM[o + 1] | ROM[o + 2] << 8 | ROM[o + 3] << 16; o += 4; out = bytearray()
    while len(out) < size:
        flags = ROM[o]; o += 1
        for bit in range(8):
            if len(out) >= size: break
            if flags & (0x80 >> bit):
                b1, b2 = ROM[o], ROM[o + 1]; o += 2
                n = (b1 >> 4) + 3; d = ((b1 & 15) << 8 | b2) + 1
                for _ in range(n): out.append(out[-d])
            else: out.append(ROM[o]); o += 1
    return bytes(out)

def tiles_of(ts, count):
    raw = lz77(off(ts['tiles'])) if ts['compressed'] else ROM[off(ts['tiles']):off(ts['tiles']) + 32 * count]
    a = np.frombuffer(raw, np.uint8)[: len(raw) // 32 * 32].reshape(-1, 32)
    t = np.zeros((len(a), 8, 8), np.uint8)
    t[:, :, 0::2] = (a & 15).reshape(-1, 8, 4); t[:, :, 1::2] = (a >> 4).reshape(-1, 8, 4)
    return t

def pals_of(ts):
    o = off(ts['pals']); out = []
    for p in range(16):
        row = []
        for i in range(16):
            c = struct.unpack_from('<H', ROM, o + 32 * p + 2 * i)[0]
            row.append(((c & 31) << 3, ((c >> 5) & 31) << 3, ((c >> 10) & 31) << 3))
        out.append(row)
    return out

_cache = {}
class TS:
    def __init__(self, L):
        P, S = L['primary'], L['secondary']
        key = (P['addr'], S['addr'])
        if key in _cache: self.__dict__ = _cache[key].__dict__; return
        self.P, self.S = P, S
        self.pt, self.st = tiles_of(P, 640), tiles_of(S, 384)
        pp, sp = pals_of(P), pals_of(S)
        self.pal = [pp[i] if i < 7 else sp[i] for i in range(16)]
        self.cache = {}; _cache[key] = self
    def tile(self, t):
        if t < 640: return self.pt[t] if t < len(self.pt) else np.zeros((8, 8), np.uint8)
        t -= 640; return self.st[t] if t < len(self.st) else np.zeros((8, 8), np.uint8)
    def ents(self, mid):
        ts, i = (self.P, mid) if mid < 640 else (self.S, mid - 640)
        return struct.unpack_from('<8H', ROM, off(ts['mt']) + 16 * i)
    def attr(self, mid):
        ts, i = (self.P, mid) if mid < 640 else (self.S, mid - 640)
        return u32(off(ts['attr']) + 4 * i)
    def meta(self, mid):
        if mid in self.cache: return self.cache[mid]
        img = np.zeros((16, 16, 3), np.uint8)
        try: e = self.ents(mid)
        except struct.error: return img
        for layer in range(2):
            for q in range(4):
                v = e[layer * 4 + q]; t = self.tile(v & 0x3FF)
                if v & 0x400: t = t[:, ::-1]
                if v & 0x800: t = t[::-1, :]
                pal = np.array(self.pal[(v >> 12) & 15], np.uint8)
                y, x = (q // 2) * 8, (q % 2) * 8
                blk = img[y:y + 8, x:x + 8]
                if layer == 0: blk[:] = pal[t]
                else: m = t != 0; blk[m] = pal[t][m]
        self.cache[mid] = img; return img

def map_cells(L):
    return struct.unpack_from('<%dH' % (L['w'] * L['h']), ROM, off(L['map']))

def render(L):
    ts = TS(L); c = map_cells(L); W, H = L['w'], L['h']
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = ts.meta(c[y * W + x] & 0x3FF)
    return img
