"""Fantasma (user upload 2026-11-21: Fantasma_Part_I_rc_Water.gba; header FANTASMA / BFTE) reader.

A pokeemerald-expansion hack whose tilesets are compressed with the expansion's smol format (modes 1 and 6 seen),
not LZ77. Decompressed by `unsmol` (tools/fantasma/unsmol.cpp, built against the expansion's own compresSmol
sources: rh-hideout/pokeemerald-expansion tools/compresSmol; g++ -O2 -std=c++17 unsmol.cpp compressAlgo.cpp
tANS.cpp fileDispatcher.cpp). Map headers found with tools/monomyth/romlib.find_headers (MONOMYTH_ROM=the ROM).
Env: FANTASMA_ROM (default /home/claude/fantasma/fantasma.gba), UNSMOL (default /home/claude/smol/unsmol).
"""
import os, sys, struct, subprocess, tempfile, functools
import numpy as np
ROMP = os.environ.get('FANTASMA_ROM', '/home/claude/fantasma/fantasma.gba')
UNSMOL = os.environ.get('UNSMOL', '/home/claude/smol/unsmol')
ROM = open(ROMP, 'rb').read()
u16 = lambda o: struct.unpack_from('<H', ROM, o)[0]
u32 = lambda o: struct.unpack_from('<I', ROM, o)[0]
off = lambda p: p - 0x08000000

@functools.lru_cache(None)
def unsmol(o):
    fd, path = tempfile.mkstemp(); os.close(fd)
    subprocess.run([UNSMOL, ROMP, str(o), path], capture_output=True)
    d = open(path, 'rb').read(); os.unlink(path); return d

def lz77(o):
    size = ROM[o + 1] | ROM[o + 2] << 8 | ROM[o + 3] << 16; o += 4; out = bytearray()
    while len(out) < size:
        flags = ROM[o]; o += 1
        for bit in range(8):
            if len(out) >= size: break
            if flags & (0x80 >> bit):
                b1, b2 = ROM[o], ROM[o + 1]; o += 2
                n = (b1 >> 4) + 3; dd = ((b1 & 15) << 8 | b2) + 1
                for _ in range(n): out.append(out[-dd])
            else: out.append(ROM[o]); o += 1
    return bytes(out)

def smol_tilemap(o):
    """smol mode 8 (IS_TILEMAP): port of expansion SmolDecompressTilemap (DecodeInstructions + delta decode)."""
    h0, nlo = struct.unpack_from('<II', ROM, o)
    size, nsym = (h0 >> 4) & 0x3FFF, h0 >> 18
    d = o + 8; sym = list(struct.unpack_from('<%dH' % nsym, ROM, d))
    lo = d + nsym * 2 + 2 * (nsym % 2); end = lo + nlo; out = []; si = 0
    while lo < end:
        b0 = ROM[lo]
        if b0 & 0x80:
            ln = (b0 & 0x7F) | ROM[lo + 1] << 7; of = ROM[lo + 2] & 0x7F
            if ROM[lo + 2] & 0x80: of |= ROM[lo + 3] << 7; lo += 4
            else: lo += 3
        else:
            ln = b0 & 0x7F; of = ROM[lo + 1] & 0x7F
            if ROM[lo + 1] & 0x80: of |= ROM[lo + 2] << 7; lo += 3
            else: lo += 2
        if ln:
            out.append(sym[si]); si += 1
            for _ in range(ln): out.append(out[-of])
        else:
            out += sym[si:si + of]; si += of
    n = size // 2; out = np.array(out[:n], np.uint32)
    return (np.cumsum(out) & 0xFFFF).astype('<u2').tobytes()

def data(p, raw_len=0x8000):
    o = off(p)
    if ROM[o] == 0x10: return lz77(o)
    if ROM[o] & 0xF == 8: return smol_tilemap(o)
    if ROM[o] & 0xF in (1, 2, 3, 4, 5, 6): 
        d = unsmol(o)
        if d: return d
    return ROM[o:o + raw_len]

def tiles(ts):
    raw = data(ts['tiles']) if ts['compressed'] else ROM[off(ts['tiles']):off(ts['tiles']) + 512 * 32]
    n = len(raw) // 32; t = np.frombuffer(raw[:n * 32], np.uint8).reshape(n, 32)
    px = np.zeros((n, 8, 8), np.uint8); px[:, :, 0::2] = (t & 15).reshape(n, 8, 4); px[:, :, 1::2] = (t >> 4).reshape(n, 8, 4)
    return px

def pals(ts):
    o = off(ts['pals'])
    return [[((v & 31) << 3, ((v >> 5) & 31) << 3, ((v >> 10) & 31) << 3) for v in struct.unpack_from('<16H', ROM, o + i * 32)] for i in range(16)]

class TS:
    def __init__(s, L, n=8, npt=None, npm=None, nps=6):
        s.pt, s.st = tiles(L['primary']), tiles(L['secondary'])
        # Fantasma sizes primaries per tileset: most are 512 tiles / 512 metatiles, but some (e.g. the
        # 0x938b14c indoor primary) decompress to 640 tiles and then both the secondary tile and metatile
        # ranges start at 640. Sized from the decompressed primary.
        big = 640 if len(s.pt) > 512 else 512
        npt = npt or big; npm = npm or big
        pp, sp = pals(L['primary']), pals(L['secondary'])
        s.pal = np.array([pp[i] if i < nps else sp[i] for i in range(16)], np.uint8)
        s.pmt, s.smt = off(L['primary']['mt']), off(L['secondary']['mt']); s.n, s.npt, s.npm = n, npt, npm
        s.cache = {}
    def tile(s, tid):
        if tid < s.npt: return s.pt[tid] if tid < len(s.pt) else None
        t = tid - s.npt; return s.st[t] if t < len(s.st) else None
    def meta(s, mid):
        if mid in s.cache: return s.cache[mid]
        base = s.pmt + mid * s.n * 2 if mid < s.npm else s.smt + (mid - s.npm) * s.n * 2
        img = np.zeros((16, 16, 3), np.uint8)
        for q in range(s.n):
            e = u16(base + q * 2); t = s.tile(e & 0x3FF)
            if t is None: continue
            if e & 0x400: t = t[:, ::-1]
            if e & 0x800: t = t[::-1, :]
            pal = s.pal[e >> 12]; oy, ox = ((q % 4) // 2) * 8, ((q % 4) % 2) * 8
            blk = img[oy:oy + 8, ox:ox + 8]
            if q < 4: blk[:] = pal[t]
            else: m = t != 0; blk[m] = pal[t][m]
        s.cache[mid] = img; return img

def cells(L):
    W, H = L['w'], L['h']; o = off(L['map'])
    if ROM[o] == 0x10 and (ROM[o + 1] | ROM[o + 2] << 8 | ROM[o + 3] << 16) == W * H * 2:
        raw = lz77(o)
    else: raw = ROM[o:o + W * H * 2]
    return np.frombuffer(raw, '<u2').reshape(H, W) & 0x3FF

def render(L, n=8):
    ts = TS(L, n); c = cells(L); H, W = c.shape
    img = np.zeros((H * 16, W * 16, 3), np.uint8)
    for y in range(H):
        for x in range(W): img[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = ts.meta(int(c[y, x]))
    return img
