"""Burglar Fenwick's battle picture (user 2026-11-27: Odyssey's ragged hooded thief, trainer picture 25, "with a darker
beige tunic and slightly bluer hair"). Read from the Odyssey ROM (FireRed trainer picture table 0x23957C, palettes
0x239A1C), recoloured, written as a DR trainer front picture.
Usage: python3 tools/art/pelluca/burglar/fenwick_front.py [--show | --write]"""
import os, sys, struct
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..'))
from trainer_front_survey import lz
ROM = '/home/claude/odyssey/odyssey.gba'
PICS, PALS, IDX = 0x23957C, 0x239A1C, 25
OUT = os.path.join(HERE, '..', '..', '..', '..', 'codebase/graphics/trainers/front_pics/dr_burglar.png')

def read():
    rom = open(ROM, 'rb').read()
    p = struct.unpack_from('<I', rom, PICS + 8 * IDX)[0] - 0x08000000
    q = struct.unpack_from('<I', rom, PALS + 8 * IDX)[0] - 0x08000000
    raw, pal = lz(rom, p)[:0x800], lz(rom, q)[:32]
    P = [((v & 31) << 3, (v >> 5 & 31) << 3, (v >> 10 & 31) << 3) for v in struct.unpack_from('<16H', pal, 0)]
    a = np.zeros((64, 64), np.uint8)
    for t in range(64):
        for i in range(32):
            v = raw[t * 32 + i]; y = (t // 8) * 8 + i // 4; x = (t % 8) * 8 + (i % 4) * 2; a[y, x] = v & 15; a[y, x + 1] = v >> 4
    return a, P

HEAD_ROWS = 26                       # the hood and hair; the same greys below are his leg wraps
def recolour(a, P):
    """the tunic (the ragged brown cloak) a darker beige; the hair a little bluer. The hair shares its greys with the leg
    wraps, so its pixels move to two slots freed by merging near-duplicates (the near-black into the black outline,
    the 2-pixel white into the lightest skin)."""
    a = a.copy(); P = list(P)
    a[a == 7] = 2; a[a == 11] = 10
    head = np.zeros_like(a, bool); head[:HEAD_ROWS] = True
    a[head & (a == 1)] = 7; a[head & (a == 3)] = 11; a[head & (a == 4)] = 11
    P[7], P[11] = (34, 46, 68), (60, 76, 102)                     # the hair: was (40,48,56) and (64,72,80)
    P[14], P[5], P[6], P[15] = (58, 50, 40), (84, 72, 56), (112, 98, 74), (146, 128, 94)   # the tunic, darker beige
    return a, P

def write(a, P, path):
    im = Image.fromarray(a, 'P'); flat = []
    for c in P: flat += list(c)
    im.putpalette(flat); im.save(path)

if __name__ == '__main__' and '--write' in sys.argv:
    a, P = recolour(*read()); write(a, P, os.path.abspath(OUT)); print('written', os.path.abspath(OUT))
elif __name__ == '__main__' and '--show' in sys.argv:
    from PIL import ImageDraw
    a0, P0 = read(); a1, P1 = recolour(a0, P0)
    def rgb(a, P):
        m = np.zeros((64, 64, 3), np.uint8); m[:] = (110, 110, 132)
        for j in range(1, 16): m[a == j] = P[j]
        return Image.fromarray(m).resize((256, 256), 0)
    S = Image.new('RGB', (520, 276), (30, 30, 36)); S.paste(rgb(a0, P0), (0, 20)); S.paste(rgb(a1, P1), (264, 20))
    d = ImageDraw.Draw(S); d.text((4, 4), 'Odyssey #25', fill=(255, 255, 0)); d.text((268, 4), 'Fenwick: darker beige tunic, bluer hair', fill=(255, 255, 0))
    S.save('/tmp/fenwick_recolour.png')
elif __name__ == '__main__':
    a, P = read()
    for i, c in enumerate(P): print(i, c, int((a == i).sum()))
    S = np.zeros((64, 64 * 16, 3), np.uint8)
    for i in range(16):
        m = np.zeros((64, 64, 3), np.uint8); m[:] = (110, 110, 132)
        for j in range(1, 16): m[a == j] = P[j] if j != i else (255, 0, 255)
        S[:, i * 64:(i + 1) * 64] = m
    Image.fromarray(S).resize((64 * 16 * 3, 192), 0).save('/tmp/fenwick_indices.png')
