"""Convert every 2-layer metatiles.bin (8 entries, 16 B) to triple-layer (12 entries, 24 B).

Old engine (field_camera.c DrawMetatile, before 2026-11-15) by layer type:
    NORMAL : BG3 = 0x3014 filler x4, BG2 = e[0:4], BG1 = e[4:8]
    COVERED: BG3 = e[0:4],           BG2 = e[4:8], BG1 = 0 x4
    SPLIT  : BG3 = e[0:4],           BG2 = 0 x4,   BG1 = e[4:8]
New engine: BG3 = n[0:4], BG2 = n[4:8], BG1 = n[8:12], always.
So n = old (BG3, BG2, BG1) exactly, and every metatile draws the same tiles.
The NORMAL filler is kept on purpose: 1,575 NORMAL metatiles have transparent
pixels in their middle layer, where that filler is visible in-game today.

Only metatiles.bin changes. Attributes (incl. layer type, still used by gameplay
code) and tiles.png are untouched. Refuses files already 24 B/metatile.
Usage: python3 -I convert_metatiles.py <codebase dir> [--check]
"""
import re, struct, sys, os

FILL = 0x3014
def old_layers(e, layer):
    if layer == 0: return ([FILL] * 4, list(e[0:4]), list(e[4:8]))       # NORMAL
    if layer == 1: return (list(e[0:4]), list(e[4:8]), [0] * 4)          # COVERED
    if layer == 2: return (list(e[0:4]), [0] * 4, list(e[4:8]))          # SPLIT
    raise ValueError(f'unknown layer type {layer}')

def tilesets(C):
    hdr = open(os.path.join(C, 'src/data/tilesets/headers.h')).read()
    mth = open(os.path.join(C, 'src/data/tilesets/metatiles.h')).read()
    out = {}
    for m in re.finditer(r'const struct Tileset (gTileset_\w+) =\s*\{(.*?)\};', hdr, re.S):
        body = m.group(2)
        mt = re.search(r'\.metatiles\s*=\s*(\w+)', body).group(1)
        at = re.search(r'\.metatileAttributes\s*=\s*(\w+)', body).group(1)
        mp = re.search(mt + r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"', mth).group(1)
        ap = re.search(at + r'\[\]\s*=\s*INCBIN_U16\("([^"]+)"', mth).group(1)
        out.setdefault(mp, set()).add(ap)
    return out

def main():
    C = sys.argv[1]; check = '--check' in sys.argv
    files = tilesets(C); done = skipped = 0; total = 0
    for mp, aps in sorted(files.items()):
        assert len(aps) == 1, f'{mp} paired with several attribute files: {aps}'
        ap = next(iter(aps))
        mt = open(os.path.join(C, mp), 'rb').read(); at = open(os.path.join(C, ap), 'rb').read()
        n = len(at) // 2
        if len(mt) == n * 24:
            skipped += 1; continue
        assert len(mt) == n * 16, f'{mp}: {len(mt)} bytes for {n} attributes'
        out = bytearray()
        for i in range(n):
            e = struct.unpack_from('<8H', mt, i * 16)
            layer = (struct.unpack_from('<H', at, i * 2)[0] >> 12) & 0xF
            b3, b2, b1 = old_layers(e, layer)
            new = b3 + b2 + b1
            # invariant: the new draw reproduces the old draw on every BG
            assert (new[0:4], new[4:8], new[8:12]) == (b3, b2, b1)
            out += struct.pack('<12H', *new)
        assert len(out) == n * 24
        total += n; done += 1
        if not check:
            open(os.path.join(C, mp), 'wb').write(out)
    print(f'converted {done} files ({total} metatiles), already triple-layer {skipped}' + (' [check only]' if check else ''))

if __name__ == '__main__':
    main()
