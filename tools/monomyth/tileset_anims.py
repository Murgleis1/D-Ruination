"""Recover a MonoMyth tileset animation's frames from its callback, without disassembling: walk the literal
pools of the init function and of the functions it references, collect (a) arrays of >= 2 ROM pointers to
equally spaced data (frame lists) and (b) VRAM destinations (0x0600xxxx). The destination gives the tile the
frames are copied over: tile = (dest - 0x06000000) // 32 (BG tiles start at char base 0)."""
import os, sys, struct
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from romlib import ROM, u32, isptr, off

def pool_words(start, span=0x600):
    o = off(start & ~1) & ~3
    return [u32(o + 4 * i) for i in range(span // 4) if o + 4 * i + 4 <= len(ROM)]

def frame_list(p):
    """p -> list of frame pointers if p is an array of >= 2 equally spaced ROM pointers, else None."""
    if not isptr(p) or p & 3: return None
    fr = []
    for i in range(16):
        v = u32(off(p) + 4 * i)
        if not isptr(v) or v & 1: break
        fr.append(v)
    if len(fr) < 2: return None
    steps = {fr[i + 1] - fr[i] for i in range(len(fr) - 1)}
    if len(steps) == 1 and 0 < steps.pop() <= 0x2000: return fr
    return None

def anims(cb, depth=2):
    seen, frames, dests, todo = set(), {}, set(), [(cb, 0)]
    while todo:
        f, d = todo.pop()
        if f in seen: continue
        seen.add(f)
        for w in pool_words(f):
            if 0x06000000 <= w < 0x06010000: dests.add(w)
            elif isptr(w) and w & 1 and d < depth and abs(w - f) < 0x4000: todo.append((w, d + 1))
            elif isptr(w):
                fl = frame_list(w)
                if fl: frames[w] = fl
    return frames, sorted(dests)
