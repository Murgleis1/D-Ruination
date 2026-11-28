"""Survey the trainer front pictures of the reference ROMs (2026-11-27: candidates for Burglar Fenwick's look).
Finds sprite-sheet tables by their structure: runs of {ptr -> LZ77 data of 0x800 bytes (a 64x64 4bpp picture),
u16 0x800, u16 tag = 0, 1, 2, ...} (Emerald and FireRed alike), and palette tables likewise ({ptr -> LZ77 0x20 bytes,
u16 tag = 0, 1, 2, ...}). Every run of 40 or more is drawn with the palette table of the closest length that follows it
(the trainer table is the shorter of the two picture tables; the Pokemon table is drawn too and simply skipped).
Usage: python3 tools/art/trainer_front_survey.py ROM OUT_PREFIX"""
import sys, struct
import numpy as np
from PIL import Image, ImageDraw

def lz(rom, off, limit=1 << 16):
    if rom[off] != 0x10: return None
    size = rom[off + 1] | rom[off + 2] << 8 | rom[off + 3] << 16
    if size > limit: return None
    o = bytearray(); i = off + 4
    try:
        while len(o) < size:
            f = rom[i]; i += 1
            for b in range(8):
                if len(o) >= size: break
                if f & (0x80 >> b):
                    x = rom[i] << 8 | rom[i + 1]; i += 2; n = (x >> 12) + 3; d = (x & 0xFFF) + 1
                    if d > len(o): return None
                    for _ in range(n): o.append(o[-d])
                else: o.append(rom[i]); i += 1
    except IndexError: return None
    return bytes(o)

def runs(rom, ok, minlen=40):
    """runs of 8-byte entries whose tag (bytes 4-5 or 6-7) counts 0, 1, 2, ..."""
    N = len(rom); out = []
    e = 0
    while e < N - 8:
        k = 0
        while e + 8 * k < N - 8 and ok(e + 8 * k, k): k += 1
        if k >= minlen: out.append((e, k)); e += 8 * k
        else: e += 4
    return out

def main(path, out):
    rom = open(path, 'rb').read(); N = len(rom)
    isp = lambda v: 0x08000000 <= v < 0x08000000 + N
    def pic_ok(e, k):
        p, sz, tag = struct.unpack_from('<IHH', rom, e)
        return isp(p) and sz == 0x800 and tag == k      # (the data is checked when drawn: some hacks repoint a few)
    def pal_ok(e, k):
        p, tag = struct.unpack_from('<IH', rom, e)
        return isp(p) and tag == k and struct.unpack_from('<H', rom, e + 6)[0] == 0
    picruns, palruns = runs(rom, pic_ok), runs(rom, pal_ok)
    # FireRed: the trainer picture table sits right before its palette table (same length), and some entries of
    # hacks are repointed with other sizes: take it from the palette table's length
    for qe, qk in palruns:
        e0 = qe - 8 * qk
        if e0 > 0 and all(struct.unpack_from('<H', rom, e0 + 8 * k + 6)[0] == k for k in range(qk)) and not any(r[0] == e0 for r in picruns):
            picruns.append((e0, qk))
    print(path, 'picture tables', [(hex(e), k) for e, k in picruns], 'palette tables', [(hex(e), k) for e, k in palruns])
    for ti, (pe, pk) in enumerate(picruns):
        cand = [r for r in palruns if r[0] == pe + 8 * pk] or [r for r in palruns if abs(r[1] - pk) <= 2] or palruns
        if not cand: continue
        qe, qk = min(cand, key=lambda r: (abs(r[1] - pk), abs(r[0] - pe)))
        imgs = []
        for k in range(min(pk, qk)):
            p = struct.unpack_from('<I', rom, pe + 8 * k)[0] - 0x08000000
            q = struct.unpack_from('<I', rom, qe + 8 * k)[0] - 0x08000000
            raw, pal = lz(rom, p), lz(rom, q)
            if not raw or not pal or len(raw) < 0x800: continue
            raw = raw[:0x800]
            P = [((v & 31) << 3, (v >> 5 & 31) << 3, (v >> 10 & 31) << 3) for v in struct.unpack_from('<16H', pal, 0)]
            a = np.zeros((64, 64), int)
            for t in range(64):
                for i in range(32):
                    v = raw[t * 32 + i]; y = (t // 8) * 8 + i // 4; x = (t % 8) * 8 + (i % 4) * 2; a[y, x] = v & 15; a[y, x + 1] = v >> 4
            img = np.zeros((64, 64, 3), np.uint8); img[:] = (110, 110, 132)
            for i in range(1, 16): img[a == i] = P[i]
            imgs.append((k, img))
        cols, per = 16, 160
        for part in range(0, len(imgs), per):
            chunk = imgs[part:part + per]
            S = Image.new('RGB', (cols * 68, ((len(chunk) + cols - 1) // cols) * 80), (30, 30, 36)); d = ImageDraw.Draw(S)
            for n, (k, img) in enumerate(chunk):
                x = (n % cols) * 68; y = (n // cols) * 80
                S.paste(Image.fromarray(img), (x, y + 14)); d.text((x + 2, y + 1), '%d' % k, fill=(255, 255, 120))
            S.save('%s_t%d_%d.png' % (out, ti, part // per))
        print('  table %d at 0x%X: %d pictures (palettes 0x%X)' % (ti, pe, len(imgs), qe))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
