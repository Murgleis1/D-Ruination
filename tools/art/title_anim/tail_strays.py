"""Remove lone protruding pixels (<=1 side neighbour) that the bend leaves in the bent poses (keys 1-4)."""
import pickle, sys
import tail_repair as R
f = sys.argv[1]
ps = pickle.load(open(f, 'rb'))
for k in range(1, 5):
    for _ in range(2):
        for p in R.defects(ps[k])[1]: del ps[k][p]
pickle.dump(ps, open(f, 'wb'))
print(f, [(len(o), [len(d) for d in R.defects(o)]) for o in ps])
