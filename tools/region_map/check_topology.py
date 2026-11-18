"""Topology checks for the region map: places that must be islands are islands, and so on.
Usage: python3 tools/region_map/check_topology.py   (exits non-zero on a failure)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import classify
from layout import LAYOUT
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'region_map', 'cormorian_empire_illustrated.png')
ISLANDS = ['Windrunner Island', 'Keerin Shrine']                 # own landmass, not the mainland
MAINLAND = ['Rivetshore City', 'Pelluca Valley', 'Mirroh', 'Victory Cape', 'Agustrei Heights', 'Fennilahl']
def landmass(lab, name):
    for n, k, x, y, w, h in LAYOUT:
        if n == name:
            ids = []
            for i in range(x, x + w):
                for j in range(y, y + h):
                    sub = lab[16 + 8*j:24 + 8*j, 8 + 8*i:16 + 8*i]; v = sub[sub > 0]
                    if len(v): ids.append(int(np.bincount(v).argmax()))
            return set(ids)
    raise KeyError(name)
if __name__ == '__main__':
    cm = classify.class_map(SRC); lab, _ = classify.land_components(cm)
    main = landmass(lab, 'Fennilahl'); bad = 0
    for n in MAINLAND:
        ok = bool(landmass(lab, n) & main); bad += not ok; print(('ok  ' if ok else 'FAIL'), n, 'on the mainland')
    for n in ISLANDS:
        ok = not (landmass(lab, n) & main); bad += not ok; print(('ok  ' if ok else 'FAIL'), n, 'is an island')
    sys.exit(1 if bad else 0)
