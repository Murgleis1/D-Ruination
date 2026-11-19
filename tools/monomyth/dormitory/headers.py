"""Cached MonoMyth map headers + region-map names (find_headers() scans the whole ROM, ~1 min)."""
import os, sys, pickle
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE))
CACHE = '/tmp/mm_headers.pkl'
def load():
    if os.path.exists(CACHE): return pickle.load(open(CACHE, 'rb'))
    import romlib
    from romlib import u32, dec, off
    H = romlib.find_headers(); names = {}
    for i in range(120):
        p = u32(0xA166AC + 8 * i + 4)
        if romlib.isptr(p):
            try: names[i] = dec(off(p), 30)
            except Exception: pass
    pickle.dump((H, names), open(CACHE, 'wb')); return H, names
