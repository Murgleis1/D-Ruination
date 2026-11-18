import sys, pickle, numpy as np
import lift_lib as LL, tail_inv as T
import tail_repair as R
from tail_rig import a, tx, ty
M, CF, OUT = float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
fr = [0, 0.25, 0.5, 0.75, 1.0]
poses, gaps = [], []
for j, f in enumerate(fr):
    o = T.pose_inv(None) if j == 0 else T.pose_inv(LL.bend_lift2(T.KEYS[j][0], T.KEYS[j][1], M * f, CF))
    g = LL.clear2(o)
    if j: o = R.repair(o)
    poses.append(o); gaps.append(g)
orig = {(int(x), int(y)): a[y, x] for y, x in zip(ty, tx)}
print('rest == original', poses[0] == orig)
for j, o in enumerate(poses): print('key', j, 'px', len(o), 'notches/spurs', [len(d) for d in R.defects(o)], 'gap to body', gaps[j])
pickle.dump(poses, open(OUT, 'wb'))
pickle.dump((poses, [[0, 30], [1, 9], [2, 8], [3, 9], [4, 24], [3, 10], [2, 9], [1, 10]]), open(OUT.replace('keys', 'poses'), 'wb'))
