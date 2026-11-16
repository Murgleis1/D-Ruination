"""MonoMyth overworld sprites: catalogue + full-frame extraction (user 2026-11-16: base Osrid's
overworld sprite on the masked man from Sunbeached Cliffs).

How (measured, 2026-11-16):
  * The headless mGBA core hangs MonoMyth at boot on flash-ID detection (unknown game code ->
    wrong save type). A scratch copy with the game code set to BPEE (Emerald: FLASH1M + RTC
    override) boots normally. The real ROM is never modified.
  * Overworld sheets are stored in a MonoMyth-specific packed container (not LZ77, not smol);
    images[k] = {container*, k, 0xFF}. Rather than reverse it, the GAME decodes it: from a save
    state in the player's bedroom (assets/monomyth_ow/mm_bedroom.state) the player sprite's cached
    images pointer (EWRAM, state offset 0x424DC) is swapped for the target sprite's, the player
    turns, and the decoded frame is read from OBJ VRAM tiles 0-7.
  * Frame order is the standard 9: S, N, W, walk S x2, walk N x2, walk W x2. Turning NORTH copies
    images[1]; turning back SOUTH after a pause copies images[0]; images[k>=1] = UP on the pointer
    shifted by k-1 entries.
  * Graphics-info structs found by pattern (tileTag 0xFFFF, size/width/height); palettes by tag.

Usage:
  python3 -I mm_overworld.py ROM catalogue OUT.png        all 16x32 sprites, 4 facings, numbered
  python3 -I mm_overworld.py ROM extract N OUT.png        sprite #N as a 144x32 9-frame indexed sheet
"""
import os, re, sys, struct
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, '../../assets/monomyth_ow/mm_bedroom.state')
SLOT = 0x424DC
VRAM_OBJ = 0x11000          # mGBA state: VRAM at 0x1000, OBJ VRAM at +0x10000
isp = lambda v: 0x08000000 <= v < 0x0A000000


def patched_rom(rom, out='/tmp/mm_bpee.gba'):
    d = bytearray(open(rom, 'rb').read())
    d[0xAC:0xB0] = b'BPEE'
    c = 0
    for i in range(0xA0, 0xBD): c = (c - d[i]) & 0xFF
    d[0xBD] = (c - 0x19) & 0xFF
    open(out, 'wb').write(d)
    return out


def scan(d):
    infos = []
    for m in re.finditer(re.escape(b'\xff\xff'), d):
        a = m.start()
        if a % 4 or a > len(d) - 64: continue
        tag, pal, refl, size, w, h = struct.unpack_from('<HHHHhh', d, a)
        if (w, h, size) != (16, 32, 256): continue
        ptrs = [struct.unpack_from('<I', d, a + o)[0] for o in range(16, 36, 4)]
        if sum(isp(p) for p in ptrs) < 4: continue
        infos.append((a, pal, ptrs[3]))
    tags = {i[1] for i in infos}; pals = {}
    for a in range(0, len(d) - 8, 4):
        p, t, z = struct.unpack_from('<IHH', d, a)
        if t in tags and t not in pals and isp(p) and z == 0:
            q = p - 0x08000000
            cols = [struct.unpack_from('<H', d, q + 2 * i)[0] for i in range(16)]
            if all(c < 0x8000 for c in cols):
                pals[t] = np.array([((c & 31) << 3, ((c >> 5) & 31) << 3, ((c >> 10) & 31) << 3) for c in cols], np.uint8)
    return infos, pals


def tiles2px(b):
    px = np.zeros((32, 16), np.uint8)
    for t in range(8):
        tb = np.frombuffer(b[t * 32:(t + 1) * 32], np.uint8); tile = np.zeros((8, 8), np.uint8)
        tile[:, 0::2] = (tb & 15).reshape(8, 4); tile[:, 1::2] = (tb >> 4).reshape(8, 4)
        px[(t // 2) * 8:(t // 2) * 8 + 8, (t % 2) * 8:(t % 2) * 8 + 8] = tile
    return px


def _gba(rom):
    sys.path.insert(0, os.path.join(HERE, '../playtest'))
    from gba_harness import GBA
    return GBA(patched_rom(rom)), bytearray(open(STATE, 'rb').read())


def extract(rom, n):
    d = open(rom, 'rb').read(); infos, pals = scan(d)
    a, tag, images = infos[n]; im = images - 0x08000000
    count = 0
    while d[im + 8 * count:im + 8 * count + 4] == d[im:im + 4] and d[im + 8 * count + 5] == 0xFF: count += 1
    g, base = _gba(rom); frames = []
    for k in range(count):
        st = bytearray(base); st[SLOT:SLOT + 4] = struct.pack('<I', images + 8 * max(k - 1, 0)); g.restore(bytes(st))
        if k == 0: g.run(2, 'UP'); g.run(20); g.run(2, 'DOWN'); g.run(20)
        else: g.run(2, 'UP'); g.run(10)
        frames.append(tiles2px(bytes(g.state())[VRAM_OBJ:VRAM_OBJ + 256]))
    return np.concatenate(frames, 1), pals[tag]


def save_indexed(px, pal, path):
    from PIL import Image
    img = Image.fromarray(px, 'P'); img.putpalette([int(v) for c in pal for v in c] + [0] * (768 - 48))
    img.save(path, transparency=0)


if __name__ == '__main__':
    rom, mode = sys.argv[1], sys.argv[2]
    if mode == 'extract':
        px, pal = extract(rom, int(sys.argv[3])); save_indexed(px, pal, sys.argv[4]); print(px.shape)
    else:
        from PIL import Image, ImageDraw
        d = open(rom, 'rb').read(); infos, pals = scan(d); g, base = _gba(rom)
        S, cols = 3, 10; W, H = 4 * 16 * S + 10, 32 * S + 14
        out = Image.new('RGB', (cols * W, ((len(infos) + cols - 1) // cols) * H), (30, 30, 30)); dr = ImageDraw.Draw(out)
        for i, (a, tag, images) in enumerate(infos):
            st = bytearray(base); st[SLOT:SLOT + 4] = struct.pack('<I', images); g.restore(bytes(st))
            x, y = (i % cols) * W, (i // cols) * H; dr.text((x, y), f'#{i}', fill=(255, 255, 0))
            for j, btn in enumerate(('DOWN', 'LEFT', 'UP', 'RIGHT')):
                g.run(4, btn); g.run(6); px = tiles2px(bytes(g.state())[VRAM_OBJ:VRAM_OBJ + 256])
                rgb = pals[tag][px] if tag in pals else np.stack([px * 17] * 3, -1).astype(np.uint8); rgb[px == 0] = (110, 110, 130)
                out.paste(Image.fromarray(rgb).resize((16 * S, 32 * S), Image.NEAREST), (x + j * 16 * S, y + 12))
        out.save(sys.argv[3])
