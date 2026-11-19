"""Read maps from a FireRed-based ROM (Pokemon Odyssey). ODYSSEY_ROM env var, default /home/claude/odyssey/odyssey.gba.
FireRed layouts: {u32 w, u32 h, *border, *map, *primary, *secondary, u8 borderW, u8 borderH};
tilesets: {u8 compressed, u8 secondary, u16 pad, *tiles, *palettes, *metatiles, *callback, *attributes}."""
import os, struct
ROM = open(os.environ.get('ODYSSEY_ROM', '/home/claude/odyssey/odyssey.gba'), 'rb').read()
N = len(ROM)
def u32(o): return struct.unpack_from('<I', ROM, o)[0]
def isptr(v): return 0x08000000 <= v < 0x08000000 + N
def off(v): return v - 0x08000000
def tileset(p):
    if not isptr(p): return None
    o = off(p)
    if o + 24 > N or ROM[o] not in (0, 1) or ROM[o + 1] not in (0, 1): return None
    tiles, pals, mt, cb, attr = struct.unpack_from('<5I', ROM, o + 4)
    if not all(isptr(x) for x in (tiles, pals, mt, attr)) or not (cb == 0 or isptr(cb & ~1)): return None
    return dict(addr=p, compressed=ROM[o], secondary=ROM[o + 1], tiles=tiles, pals=pals, mt=mt, cb=cb, attr=attr)
def layout(p):
    if not isptr(p): return None
    o = off(p)
    if o + 24 > N: return None
    w, h, border, mp, pr, se = struct.unpack_from('<6I', ROM, o)
    if not (1 <= w <= 255 and 1 <= h <= 255) or not all(isptr(x) for x in (border, mp, pr, se)): return None
    P, S = tileset(pr), tileset(se)
    if not P or not S or P['secondary'] != 0 or S['secondary'] != 1: return None
    return dict(addr=p, w=w, h=h, border=border, map=mp, primary=P, secondary=S)
