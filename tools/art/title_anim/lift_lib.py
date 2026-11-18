import os
os.environ.setdefault('TIP_LEN', '3')
import numpy as np
import tail_inv as T
from tail_rig import S, TAIL
from scipy import ndimage
S_K, SIG = 13.8, 2.5
DS = S[1] - S[0]
def bend_lift(th, curl, lift):
    g = lambda s: np.exp(-0.5 * ((s - S_K) / SIG) ** 2) / (SIG * np.sqrt(2 * np.pi))
    base = T.bendf(th, curl)
    return lambda s: base(s) + lift * g(s) * DS
cp = np.load('mask_cp.npy'); BODY = cp & ~TAIL
DIST = ndimage.distance_transform_cdt(~BODY, metric='chessboard')
def clearance(o, u_from=22.5):
    free = [p for p in o if T.U_OUT.get(p, 0) >= u_from]
    return int(min(DIST[y, x] for x, y in free)) - 1
S2, SIG2 = 19.5, 2.0
def bend_lift2(th, curl, lift, cf):
    g1 = lambda s: np.exp(-0.5 * ((s - S_K) / SIG) ** 2) / (SIG * np.sqrt(2 * np.pi))
    g2 = lambda s: np.exp(-0.5 * ((s - S2) / SIG2) ** 2) / (SIG2 * np.sqrt(2 * np.pi))
    base = T.bendf(th, curl)
    return lambda s: base(s) + lift * g1(s) * DS - cf * lift * g2(s) * DS
def clear2(o):
    obst = BODY.copy()
    for (x, y) in o:
        if T.U_OUT.get((x, y), 99) <= 15: obst[y, x] = True
    dist = ndimage.distance_transform_cdt(~obst, metric='chessboard')
    curl = [p for p in o if T.U_OUT.get(p, 0) >= 31]
    return int(min(dist[y, x] for x, y in curl)) - 1
def curl_shift(o, o0):
    c = np.array([p for p in o if T.U_OUT.get(p, 0) >= 31]).mean(0)
    return c
