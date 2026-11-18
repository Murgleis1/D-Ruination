"""Idle timing for the tail (60 fps frames): uneven rests, full / half / most-of-the-way curls; ~38 s loop."""
import pickle
ps = pickle.load(open('tail_keys_l10.pkl', 'rb'))
def full(hold=44): return [[1, 16], [2, 13], [3, 13], [4, hold], [3, 15], [2, 16], [1, 20]]
def half(hold=34): return [[1, 18], [2, hold], [1, 22]]
def most(hold=40): return [[1, 16], [2, 14], [3, hold], [2, 17], [1, 21]]
SEQ = ([[0, 150]] + full(44) + [[0, 260]] + half(34) + [[0, 190]] + full(72) + [[0, 300]]
       + most(40) + [[0, 230]] + half(26) + [[0, 160]] + full(50) + [[0, 280]])
if __name__ == '__main__':
    pickle.dump((ps, SEQ), open('tail_poses_l10_idle.pkl', 'wb'))
    print('loop %.1f s' % (sum(t for _, t in SEQ) / 60))
