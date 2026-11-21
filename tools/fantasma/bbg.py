"""Fantasma battle backgrounds: walks gBattleEnvironmentInfo (expansion struct, 64-byte entries:
name[26] (game charset), naturePower, secretPowerAnimation*, secretPowerEffect, camouflageType, camouflageBlend,
entry{tileset,tilemap}, background{tileset,tilemap}, palette*, battleIntroSlide) and renders each background.
Usage: python3 bbg.py OUTDIR [TABLE_ADDR]   (Fantasma rc_Water: table found by scanning; see find_table)."""
import os, sys, struct, numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fsread as F
R = F.ROM
CH = {0: ' ', 0xAD: '.', 0xAE: '-', 0xB4: "'", 0xBA: '/'}
CH.update({0xBB + i: chr(65 + i) for i in range(26)}); CH.update({0xD5 + i: chr(97 + i) for i in range(26)})
CH.update({0xA1 + i: str(i) for i in range(10)})
def name(o):
    s = ''
    for b in R[o:o + 26]:
        if b == 0xFF: break
        s += CH.get(b, '?')
    return s
isd = lambda p: 0x08000000 <= p < 0x08000000 + len(R) and p % 4 == 0
def ok(o):
    v = struct.unpack_from('<6I', R, o + 40)
    return all(isd(p) for p in v[:5]) and v[5] & 1 and v[5] < 0x08400000
def find_table():
    n = len(R) // 4; w = np.frombuffer(R[:n * 4], '<u4')
    d = (w >= 0x08000000) & (w < 0x08000000 + len(R)) & (w % 4 == 0); c = (w >= 0x08000000) & (w < 0x08400000) & (w % 2 == 1)
    idx = np.where(d[:-5] & d[1:-4] & d[2:-3] & d[3:-2] & d[4:-1] & c[5:])[0] * 4
    for a in idx:
        if a + 64 in set(idx.tolist()): o = a - 40; break
    while ok(o - 64): o -= 64
    return o
def pal(p):
    raw = F.data(p, 0x200); raw = raw[:len(raw) // 2 * 2]
    v = np.frombuffer(raw, '<u2'); return np.stack([(v & 31) << 3, ((v >> 5) & 31) << 3, ((v >> 10) & 31) << 3], 1).astype(np.uint8)
def render(ts, tm, pl, palbase=2):
    t = np.frombuffer(F.data(ts), np.uint8); n = len(t) // 32; t = t[:n * 32].reshape(n, 32)
    px = np.zeros((n, 8, 8), np.uint8); px[:, :, 0::2] = (t & 15).reshape(n, 8, 4); px[:, :, 1::2] = (t >> 4).reshape(n, 8, 4)
    m = np.frombuffer(F.data(tm), '<u2'); P = np.zeros((16 * 16, 3), np.uint8); p = pal(pl); P[palbase * 16:palbase * 16 + len(p)] = p[:256 - palbase * 16]
    W = 32; H = len(m) // W; img = np.zeros((H * 8, W * 8, 3), np.uint8)
    for i, e in enumerate(m):
        tid = e & 0x3FF
        if tid >= n: continue
        g = px[tid]
        if e & 0x400: g = g[:, ::-1]
        if e & 0x800: g = g[::-1]
        y, x = divmod(i, W); img[y * 8:y * 8 + 8, x * 8:x * 8 + 8] = P[(e >> 12) * 16 + g]
    return img
if __name__ == '__main__':
    out = sys.argv[1]; o = int(sys.argv[2], 16) - 0x08000000 if len(sys.argv) > 2 else find_table()
    print('table', hex(o + 0x08000000)); k = 0; miss = 0
    while miss < 4:
        if not ok(o):
            print(k, name(o), 'empty/invalid', [hex(x) for x in struct.unpack_from('<6I', R, o + 40)])
            o += 64; k += 1; miss += 1; continue
        miss = 0
        v = struct.unpack_from('<6I', R, o + 40); nm = name(o)
        try:
            img = render(v[2], v[3], v[4])[:160, :240]
            Image.fromarray(img).save('%s/bb_%02d_%s.png' % (out, k, nm.replace(' ', '_').replace('/', '_') or 'x'))
            print(k, nm, [hex(x) for x in v[:5]])
        except Exception as e: print(k, nm, 'fail', e)
        o += 64; k += 1
