"""Tail poses by INVERSE sampling: for every output pixel, map its centre back onto the rest tail through the
bent centreline (arc u, segment-normal offset n), then
  inside  = bilinear sample of the rest tail mask at that point >= 0.5   (smooth outline, no holes)
  colour  = nearest rest tail pixel to that point
Rest pose is the identity.  Joint region copied from the original."""
import numpy as np, pickle, sys
from PIL import Image
from scipy import ndimage
from scipy.spatial import cKDTree
from tail_rig import REST, S, L, TAIL, a, bent, tx, ty
NS = len(REST); DS = S[1] - S[0]
import os
THR = float(os.environ.get("THR", "0.5"))
MASK = TAIL.astype(float)
TREE = cKDTree(np.c_[tx + 0.5, ty + 0.5])
JOINT_S = 0.12 * L
TIP_LEN = float(os.environ.get('TIP_LEN', '4.0'))
cp_ = np.load('mask_cp.npy'); BODY = {(int(x), int(y)) for y, x in zip(*np.nonzero(cp_ & ~TAIL))}
ORIG = {(int(x), int(y)) for y, x in zip(ty, tx)}
U_OUT = {}
def seg_closest(P, q):
    best = np.full(len(q), 1e9); bu = np.zeros(len(q)); bn = np.zeros(len(q)); be = np.zeros(len(q)); bi = np.zeros(len(q), int); bt = np.zeros(len(q))
    for i in range(len(P) - 1):
        A, B = P[i], P[i + 1]; ab = B - A; l2 = (ab ** 2).sum()
        t = np.clip(((q - A) @ ab) / l2, 0, 1); foot = A + t[:, None] * ab
        nrm = np.array([-ab[1], ab[0]]) / np.sqrt(l2)
        along = (q - A) @ ab / np.sqrt(l2)
        d = np.linalg.norm(q - foot, axis=1)
        tu = t.copy()
        if i == len(P) - 2: tu = np.maximum(t, ((q - A) @ ab) / l2)          # past the tip: keep the overshoot
        tan = ab / np.sqrt(l2)
        foot_u = A + tu[:, None] * ab
        m = d < best; best[m] = d[m]; bu[m] = i + tu[m]; bn[m] = ((q - foot_u) @ nrm)[m]; be[m] = ((q - foot_u) @ tan)[m]; bi[m] = i; bt[m] = tu[m]
        # beyond the ends keep the true offset along the end tangent so the ends are not smeared
    return bu, bn, best, be, bi, bt
def to_rest(i, t, n, e):
    A, B = REST[i], REST[i + 1]; ab = B - A; l = np.linalg.norm(ab, axis=1)[:, None]
    nrm = np.c_[-ab[:, 1], ab[:, 0]] / l; tan = ab / l
    return A + t[:, None] * ab + n[:, None] * nrm + e[:, None] * tan
def bilinear(M, p):
    x = p[:, 0] - 0.5; y = p[:, 1] - 0.5
    x0 = np.floor(x).astype(int); y0 = np.floor(y).astype(int); fx = x - x0; fy = y - y0
    def g(yy, xx): return M[np.clip(yy, 0, 159), np.clip(xx, 0, 239)]
    return (g(y0, x0) * (1 - fx) * (1 - fy) + g(y0, x0 + 1) * fx * (1 - fy) + g(y0 + 1, x0) * (1 - fx) * fy + g(y0 + 1, x0 + 1) * fx * fy)
def pose_inv(bend):
    P = REST if bend is None else bent(bend)
    gy, gx = np.mgrid[92:132, 52:94]; q = np.c_[gx.ravel() + 0.5, gy.ravel() + 0.5]
    u, n, d, e, si, st = seg_closest(P, q)
    src = to_rest(si, st, n, e)
    val = bilinear(MASK, src)
    keep = (val >= THR) & (np.abs(n) <= 4.6) & (u > 0)
    s_arc = np.interp(u, np.arange(NS), S)
    out = {}
    global U_OUT
    U_OUT = {(int(x), int(y)): uu for (x, y), uu in zip(np.c_[gx.ravel(), gy.ravel()], u)}
    _, nearest = TREE.query(src)
    for (x, y), k_, ok, sa in zip(np.c_[gx.ravel(), gy.ravel()], nearest, keep, s_arc):
        if sa <= JOINT_S:                                   # joint: original pixels only
            if TAIL[y, x]: out[(int(x), int(y))] = a[y, x]
        elif ok: out[(int(x), int(y))] = a[ty[k_], tx[k_]]
    # tip: the last TIP_LEN px of arc moves as one rigid piece (exact original pixels)
    u_tip = np.interp(L - TIP_LEN, S, np.arange(NS))
    tip_out = [p for p, uu in zip(map(tuple, np.c_[gx.ravel(), gy.ravel()]), u) if uu >= u_tip and p in out]
    for p in tip_out: del out[(int(p[0]), int(p[1]))]
    k_end = NS - 1 - int(round(TIP_LEN / DS / 2))
    shift = np.round(P[k_end] - REST[k_end]).astype(int)
    for y, x in zip(ty, tx):
        if U_REST[(int(x), int(y))] >= u_tip: out[(int(x + shift[0]), int(y + shift[1]))] = a[y, x]
    # trim lone protruding pixels (outside the tip)
    for _ in range(2):
        for p in list(out):
            if U_OUT.get(p, 0) >= u_tip: continue
            if sum((p[0] + dx, p[1] + dy) in out or (p[0] + dx, p[1] + dy) in BODY for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))) <= 1 and p not in ORIG:
                del out[p]
    return out
DS_ = DS
def bendf(th, curl=0.0):
    def b(s):
        if s < 0.12 * L: return 0.0
        v = th / (0.88 * L) * DS_
        if s > 0.6 * L: v += curl / (0.4 * L) * DS_
        return v
    return b
_q = np.c_[tx + 0.5, ty + 0.5]; _u = seg_closest(REST, _q)[0]
U_REST = {(int(x), int(y)): uu for x, y, uu in zip(tx, ty, _u)}
KEYS = [(0.0, 0.0), (0.08, 0.04), (0.17, 0.09), (0.27, 0.14), (0.36, 0.20)]
if __name__ == '__main__':
    orig = {(int(x), int(y)): a[y, x] for y, x in zip(ty, tx)}
    r0 = pose_inv(None)
    print('rest: missing', sorted(set(orig) - set(r0)), 'extra', sorted(set(r0) - set(orig)), 'recoloured', sum(1 for p in orig if p in r0 and r0[p] != orig[p]))
