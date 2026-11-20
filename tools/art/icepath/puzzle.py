"""The ice path's puzzle field (user design 2026-11-19, after Pokemon Pisces' Sootopolis gym).

Rules (engine: the vanilla thin-ice step callback): every thin-ice tile cracks when stepped on; stepping on a cracked
tile breaks it (the screen blacks out, the room resets). The way on opens once every ice tile has been cracked, so a
solution is a Hamiltonian path over the field's ice from the entry tile S to the exit tile E (beside the way on),
around the ice boulders.

generate(): random boulder layouts that keep the colour parity a grid path from S to E needs, kept only if a solution
exists and the number of solutions is small (a real puzzle, not a lawnmower sweep). count() is an exact backtracking
counter with the usual prunes (unvisited ice stays connected; no dead end other than E).
Usage: python3 tools/art/icepath/puzzle.py [seed]
"""
import random, sys, time

def neighbours(c, free):
    x, y = c
    for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        n = (x + d[0], y + d[1])
        if n in free: yield n

def count(free, S, E, cap=50, limit=20.0):
    """-> (solutions found (<= cap), one solution or None, timed out)."""
    free = set(free); N = len(free); t0 = time.time(); sols = [0]; first = [None]; path = [S]; seen = {S}
    timed = [False]
    def connected(rest, start):
        stack = [start]; got = {start}
        while stack:
            for n in neighbours(stack.pop(), rest):
                if n not in got: got.add(n); stack.append(n)
        return len(got) == len(rest)
    def dfs(c):
        if sols[0] >= cap: return
        if time.time() - t0 > limit: timed[0] = True; return
        if len(path) == N:
            if c == E:
                sols[0] += 1
                if first[0] is None: first[0] = list(path)
            return
        if c == E: return
        rest = free - seen
        # dead ends: an unvisited cell (not E) with fewer than 2 ways in/out cannot be passed through
        ends = 0
        for r in rest:
            k = sum(1 for n in neighbours(r, rest)) + (1 if c in set(neighbours(r, free)) else 0)
            if r != E and k < 2: ends += 1
            if k == 0: return
        if ends > 1: return
        if not connected(rest, E): return
        for n in sorted(neighbours(c, rest), key=lambda n: sum(1 for _ in neighbours(n, rest))):
            seen.add(n); path.append(n); dfs(n); path.pop(); seen.discard(n)
    dfs(S)
    return sols[0], first[0], timed[0]

def generate(W, H, S, E, pairs=9, seed=1, steps=600, target=4, cap=40):
    """Boulders added in pairs (one of each square colour, so the S->E parity a grid path needs is kept), each pair
    kept only if the field is still solvable and its solution count (capped) does not rise; spread out (no boulder
    beside S or E, no 2x2 block). Stops at `pairs` pairs with at most `target` solutions, else returns the best."""
    rng = random.Random(seed); cells = [(x, y) for x in range(W) for y in range(H)]
    colour = lambda c: (c[0] + c[1]) & 1
    near = {S, E} | set(neighbours(S, set(cells))) | set(neighbours(E, set(cells)))
    B = set(); n_cur = cap; best = None
    def blocky(B):
        return any({(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)} <= B for x in range(W - 1) for y in range(H - 1))
    for _ in range(steps):
        free = set(cells) - B - near
        a = rng.choice([c for c in free if colour(c) == 0]); b = rng.choice([c for c in free if colour(c) == 1])
        B2 = B | {a, b}
        if blocky(B2): continue
        n, sol, timed = count(set(cells) - B2, S, E, cap=cap, limit=4.0)
        if timed or n == 0 or n > n_cur: continue
        B, n_cur = B2, n
        if best is None or (len(B) // 2 >= pairs and n < best[0]) or len(B) > len(best[1]):
            best = (n, sorted(B), sol)
        if len(B) // 2 >= pairs and n <= target: break
        if len(B) // 2 >= pairs + 3: break
    return best

if __name__ == '__main__':
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    W, H = 12, 9; S, E = (5, 8), (6, 0)
    r = generate(W, H, S, E, seed=seed)
    if r:
        n, B, sol = r; order = {c: i for i, c in enumerate(sol)}
        print('solutions (capped 40):', n, 'boulders', len(B), 'ice', len(sol))
        for y in range(H):
            print(' '.join('##' if (x, y) in B else '%2d' % order[(x, y)] for x in range(W)))
