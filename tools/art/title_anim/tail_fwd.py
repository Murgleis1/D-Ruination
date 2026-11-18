"""Tail keyframes by moving the ORIGINAL pixels along the bent centreline (rest = original exactly).
Each source pixel keeps its (arc u, offset n); new position = P'(u) + n * N'(u), rounded.  1-px gaps between
moved pixels are bridged from their neighbours; the joint is locked to the original."""
import numpy as np, pickle
from PIL import Image
from scipy import ndimage
from tail_rig import REST, S, L, TAIL, a, bent, normals, U0, Nn0, tx, ty
NS = len(REST); DS = S[1] - S[0]
JOINT_U = 0.12 * (NS - 1)
def mapped(P):
    _, Nb = normals(P)
    i = np.floor(U0).astype(int).clip(0, NS - 2); fr = U0 - i
    base = P[i] * (1 - fr[:, None]) + P[i + 1] * fr[:, None]
    nrm = Nb[i] * (1 - fr[:, None]) + Nb[i + 1] * fr[:, None]; nrm /= np.linalg.norm(nrm, axis=1)[:, None]
    return base + Nn0[:, None] * nrm
REST_MAP = mapped(REST)
def pose_fwd(bend):
    newp = mapped(bent(bend))
    disp = np.round(newp - REST_MAP).astype(int)              # displacement vs the rest mapping: 0 at rest
    out, src = {}, {}
    order = np.argsort(np.abs(Nn0))                           # centre pixels claim first
    lost = []
    for k in order:
        p = (int(tx[k] + disp[k, 0]), int(ty[k] + disp[k, 1]))
        if p in out: lost.append(k); continue
        out[p] = a[ty[k], tx[k]]; src[p] = (tx[k], ty[k])
    for k in lost:                                            # nothing is dropped: take the free neighbour nearest the exact spot
        exact = REST_MAP[k] + (newp[k] - REST_MAP[k]) + (np.array([tx[k], ty[k]]) + 0.5 - REST_MAP[k])
        t0 = (int(tx[k] + disp[k, 0]), int(ty[k] + disp[k, 1]))
        cands = [(t0[0] + dx, t0[1] + dy) for r in (1, 2) for dx in range(-r, r + 1) for dy in range(-r, r + 1)
                 if max(abs(dx), abs(dy)) == r and (t0[0] + dx, t0[1] + dy) not in out]
        if not cands: continue
        best = min(cands, key=lambda c: (c[0] + 0.5 - exact[0]) ** 2 + (c[1] + 0.5 - exact[1]) ** 2)
        out[best] = a[ty[k], tx[k]]; src[best] = (tx[k], ty[k])
    for k in np.nonzero(U0 <= JOINT_U + 1.0)[0]:
        p = (int(tx[k]), int(ty[k])); out[p] = a[ty[k], tx[k]]; src[p] = (tx[k], ty[k])
    # bridge 1-px gaps: an empty pixel with tail on both sides (h, v or diagonal pairs) takes the darker neighbour
    for _ in range(2):
        add = {}
        xs = [x for x, _ in out]; ys = [y for _, y in out]
        for y in range(min(ys) - 1, max(ys) + 2):
            for x in range(min(xs) - 1, max(xs) + 2):
                if (x, y) in out: continue
                pairs = [((x - 1, y), (x + 1, y)), ((x, y - 1), (x, y + 1)), ((x - 1, y - 1), (x + 1, y + 1)), ((x - 1, y + 1), (x + 1, y - 1))]
                for p, q in pairs:
                    if p in src and q in src and max(abs(src[p][0] - src[q][0]), abs(src[p][1] - src[q][1])) <= 1:
                        add[(x, y)] = (out[p], src[p]); break            # only gaps the bend opened
        for k_, (v, sp) in add.items(): out[k_] = v; src[k_] = sp
    return out
def bendf(th, curl=0.0):
    def b(s):
        if s < 0.12 * L: return 0.0
        v = th / (0.88 * L) * DS
        if s > 0.6 * L: v += curl / (0.4 * L) * DS
        return v
    return b
if __name__ == '__main__':
    KEYS = [(0.0, 0.0), (0.08, 0.04), (0.17, 0.09), (0.27, 0.14), (0.36, 0.20)]
    poses = [pose_fwd(bendf(*k)) for k in KEYS]
    orig = {(int(x), int(y)): a[y, x] for y, x in zip(ty, tx)}
    k0 = poses[0]
    print('key0 == original:', k0 == orig, '| missing', sum(1 for p in orig if p not in k0), 'extra', sum(1 for p in k0 if p not in orig))
    cp = np.load('mask_cp.npy'); body = cp & ~TAIL
    for j, o in enumerate(poses):
        m = np.zeros((160, 240), bool)
        for (x, y) in o: m[y, x] = True
        full = m | body; pin = ndimage.binary_fill_holes(full) & ~full
        lab, n = ndimage.label(pin); small = [(lab == q).sum() for q in range(1, n + 1) if (lab == q).sum() <= 3]
        print('key', j, 'px', len(o), 'small holes', small, 'pieces', ndimage.label(m)[1])
    pickle.dump(poses, open('tail_keys_fwd.pkl', 'wb'))
    im = Image.open('dr_title.png'); tp = np.array(im.getpalette()[:768]).reshape(256, 3)
    bgf = np.load('bg_filled.npy'); scene = a.copy(); scene[TAIL] = bgf[TAIL]
    tiles = [Image.fromarray(tp[a][104:126, 62:90].astype(np.uint8)).resize((224, 176), Image.NEAREST)]
    for o in poses:
        sc = tp[scene].copy()
        for (x, y), v in o.items(): sc[y, x] = tp[v]
        tiles.append(Image.fromarray(sc[104:126, 62:90].astype(np.uint8)).resize((224, 176), Image.NEAREST))
    s = Image.new('RGB', (len(tiles) * 230, 176), (0, 0, 0))
    for i, t in enumerate(tiles): s.paste(t, (i * 230, 0))
    s.save('/tmp/tailfwd.png')
