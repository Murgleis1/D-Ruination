"""The user's ten front picks (2026-11-25), pulled as indexed 64x64 PNGs from the ROMs (index 0 transparent):
MonoMyth by pic tag (tools/monomyth/mm_fronts.py), Fantasma by its front table (as tools/npc/tf_fant.py).
Usage: python3 extract.py   -> src/<SRC>_<n>.png and /tmp/cult/picks_check.png (each beside its board crop)"""
import os, sys, struct, io, contextlib
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
PICKS = [('FA', 138, 'old man'), ('MM', 22, 'old woman'), ('FA', 212, 'farmer'), ('MM', 89, 'labourer'),
         ('MM', 116, 'merchant'), ('FA', 110, 'monk'), ('MM', 30, 'imperial officer'), ('MM', 68, 'minstrel'),
         ('FA', 14, 'witch'), ('FA', 196, 'revenant')]


def save(px, pal, path):
    im = Image.fromarray(px.astype(np.uint8), 'P')
    flat = [v for c in pal for v in c]
    im.putpalette(flat + [0] * (768 - len(flat)))
    im.save(path, transparency=0)


def mm(tag):
    sys.path.insert(0, os.path.join(REPO, 'tools', 'monomyth'))
    with contextlib.redirect_stdout(io.StringIO()):
        import mm_fronts as M
    return M.pic(tag), M.pals[tag]


def fa(n):
    sys.path.insert(0, os.path.join(REPO, 'tools', 'fantasma'))
    import fsread as F
    d = F.ROM
    isp = lambda v: 0x08000000 <= v < 0x0A000000
    a, stride, po = FA_TABLE
    p = struct.unpack_from('<I', d, a + stride * n)[0]
    pp = struct.unpack_from('<I', d, a + stride * n + po)[0]
    o = F.off(p); b = F.lz77(o) if d[o] == 0x10 else F.unsmol(o)
    q = F.off(pp); raw = F.lz77(q)[:32] if d[q] == 0x10 else d[q:q + 32]
    c = struct.unpack('<16H', raw)
    pal = [((v & 31) << 3, ((v >> 5) & 31) << 3, ((v >> 10) & 31) << 3) for v in c]
    px = np.zeros((64, 64), np.uint8)
    for t in range(64):
        tb = np.frombuffer(b[t * 32:(t + 1) * 32], np.uint8); tile = np.zeros((8, 8), np.uint8)
        tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
        px[(t // 8) * 8:(t // 8) * 8 + 8, (t % 8) * 8:(t % 8) * 8 + 8] = tile
    return px, pal


def fa_table():
    sys.path.insert(0, os.path.join(REPO, 'tools', 'fantasma'))
    import fsread as F
    d = F.ROM; isp = lambda v: 0x08000000 <= v < 0x0A000000
    best = (0, 0, 0)
    cands = [a for a in range(0, len(d) - 8, 4) if struct.unpack_from('<HH', d, a + 4) == (0x800, 0) and isp(struct.unpack_from('<I', d, a)[0])]
    for a in cands:
        for stride in range(8, 80, 4):
            n = 0
            while True:
                p, sz, t = struct.unpack_from('<IHH', d, a + stride * n)
                if sz != 0x800 or t != n or not isp(p): break
                n += 1
            if n > best[0]: best = (n, a, stride)
    n, a, stride = best
    for po in range(8, stride, 4):
        if all(struct.unpack_from('<IH', d, a + stride * k + po)[1] == k and isp(struct.unpack_from('<I', d, a + stride * k + po)[0]) for k in range(5)):
            break
    return a, stride, po


if __name__ == '__main__':
    os.makedirs(os.path.join(HERE, 'src'), exist_ok=True)
    FA_TABLE = fa_table()
    sys.path.insert(0, os.path.join(REPO, 'tools', 'npc'))
    os.chdir(os.path.join(REPO, 'tools', 'npc'))
    from board_src import mm_front, fa_front
    S = Image.new('RGB', (10 * 280, 300), (36, 36, 44)); dr = ImageDraw.Draw(S)
    for i, (s, n, role) in enumerate(PICKS):
        px, pal = (mm if s == 'MM' else fa)(n)
        path = os.path.join(HERE, 'src', '%s_%d.png' % (s, n))
        save(px, pal, path)
        o = np.zeros((64, 64, 3), np.uint8); o[:] = (110, 110, 125)
        for k in range(1, 16): o[px == k] = pal[k]
        S.paste(Image.fromarray(o).resize((128, 128), Image.NEAREST), (i * 280, 20))
        S.paste((mm_front if s == 'MM' else fa_front)(n).resize((128, 128)), (i * 280 + 136, 20))
        dr.text((i * 280, 4), '%s %d %s: extracted | board' % (s, n, role), fill=(240, 220, 120))
    S.save('/tmp/cult/picks_check.png'); print('ok')
