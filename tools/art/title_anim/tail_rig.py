"""Chien-Pao tail rig: centreline skinning of the original tail pixels.
pose(bend) -> dict{(x, y): title index}.  bend(s) gives the extra joint angle (radians) at arc length s."""
import numpy as np
from PIL import Image
a = np.array(Image.open('dr_title.png')).astype(np.int16)
cp = np.load('mask_cp.npy')
Y, X = np.mgrid[0:160, 0:240]
TAIL = cp & (X >= 66) & (Y >= 108) & (Y <= 122) & (
    ((X <= 85) & (Y <= 118)) | ((X <= 82) & (Y == 119)) | ((X <= 81) & (Y >= 120)))
# the tail's own dark outline (slate/purple edge pixels the colour flood missed) moves with the tail
from scipy import ndimage as _nd
_tp = np.array(Image.open('dr_title.png').getpalette()[:768]).reshape(256, 3)
_lum = _tp[a].astype(float) @ [0.3, 0.59, 0.11]
# the tail's full drawn border: rim light on top, soft shadow underneath -- any non-background-bright pixel
# touching the silhouette (1-px ring) and connected to it (never the body)
_body = cp & ~TAIL
for _ in range(1):
    _ring = _nd.binary_dilation(TAIL, structure=np.ones((3, 3), bool)) & ~_body & (_lum < 150) & (Y >= 100) & (X >= 60)
    TAIL = TAIL | _ring
# rest centreline, base (joint) first
C0 = np.array([(86.0, 112.0), (83.5, 115.5), (81.0, 118.0), (77.5, 119.8), (73.5, 120.4), (70.5, 119.6),
               (68.4, 117.6), (67.6, 114.5), (68.4, 111.6), (70.8, 110.2), (73.5, 110.1), (76.0, 110.6)])
def resample(P, n=60):
    d = np.r_[0, np.cumsum(np.linalg.norm(np.diff(P, axis=0), axis=1))]
    s = np.linspace(0, d[-1], n)
    return np.c_[np.interp(s, d, P[:, 0]), np.interp(s, d, P[:, 1])], s
REST, S = resample(C0); L = S[-1]
def normals(P):
    t = np.gradient(P, axis=0); t /= np.linalg.norm(t, axis=1)[:, None]
    return t, np.c_[-t[:, 1], t[:, 0]]
T0, N0 = normals(REST)
def bent(bend):
    """rotate each segment by the cumulative bend; base point fixed"""
    seg = np.diff(REST, axis=0); ang = np.cumsum([bend(s) for s in S[:-1]])
    c, s_ = np.cos(ang), np.sin(ang)
    seg2 = np.c_[seg[:, 0] * c - seg[:, 1] * s_, seg[:, 0] * s_ + seg[:, 1] * c]
    return np.vstack([REST[:1], REST[0] + np.cumsum(seg2, axis=0)])
HALF = 3.4
def closest(P, q):
    """closest point on polyline P to points q (k,2): returns index-float u and signed normal offset n"""
    best_d = np.full(len(q), 1e9); best_u = np.zeros(len(q)); best_n = np.zeros(len(q))
    for i in range(len(P) - 1):
        A, B = P[i], P[i + 1]; ab = B - A; l2 = (ab ** 2).sum()
        tt = np.clip(((q - A) @ ab) / l2, 0, 1); foot = A + tt[:, None] * ab
        d = np.linalg.norm(q - foot, axis=1)
        nrm = np.array([-ab[1], ab[0]]) / np.sqrt(l2); nn = (q - foot) @ nrm
        m = d < best_d; best_d[m] = d[m]; best_u[m] = i + tt[m]; best_n[m] = nn[m]
    return best_u, best_n, best_d
# ownership on the rest pose: each tail pixel -> (u, n)
ty, tx = np.nonzero(TAIL); tq = np.c_[tx + 0.5, ty + 0.5]
U0, Nn0, D0 = closest(REST, tq)
def pose(bend):
    P = bent(bend)
    if bend is None: P = REST
    _, Nb = normals(P)
    out = {}
    # forward splat: each source pixel to its new position (rounded)
    i = np.floor(U0).astype(int).clip(0, len(P) - 2); fr = U0 - i
    base = P[i] * (1 - fr[:, None]) + P[i + 1] * fr[:, None]
    nrm = Nb[i] * (1 - fr[:, None]) + Nb[i + 1] * fr[:, None]; nrm /= np.linalg.norm(nrm, axis=1)[:, None]
    newp = base + Nn0[:, None] * nrm
    # inverse fill: for every output pixel near the new tail, take the source pixel whose new position is closest
    pts = np.floor(newp).astype(int)
    from collections import defaultdict
    cand = defaultdict(list)
    for k, (px, py) in enumerate(pts):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                cx, cy = px + dx, py + dy
                cand[(cx, cy)].append(k)
    for (cx, cy), ks in cand.items():
        ks = np.array(ks); d = np.linalg.norm(newp[ks] - (cx + 0.5, cy + 0.5), axis=1)
        j = d.argmin()
        if d[j] < 0.75: out[(cx, cy)] = a[ty[ks[j]], tx[ks[j]]]
    return out
if __name__ == '__main__':
    o = pose(lambda s: 0.0)
    orig = {(x, y): a[y, x] for y, x in zip(ty, tx)}
    same = sum(1 for k, v in orig.items() if o.get(k) == v); extra = sum(1 for k in o if k not in orig)
    print('tail px', len(orig), 'reproduced', same, 'missing', len(orig) - same, 'extra', extra, 'max |n|', np.abs(Nn0).max().round(2))
