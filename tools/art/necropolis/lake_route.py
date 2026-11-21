"""The lake's route, proved and drawn (user 2026-11-21: make sure there are paths to all four bonfires and then
to the door of Kimaris's chamber).

Checks, on the chosen layout (lake_mock.SEED):
  - from the landing every bonfire and the door's landing can be reached;
  - from EVERY place the player can come to a stop, every bonfire, the door and the landing can still be
    reached (no dead ends, whatever order the player takes);
  - the shortest full tour, landing -> four bonfires (best order) -> the door.
Draws that tour on the lit mock: each leg its own colour, each slide an arrow, the stops numbered.
Usage: python3 lake_route.py [mockdir] [outpng]
"""
import itertools, os, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import lake_puzzle as P
import lake_mock as L

def check(g):
    T = P.targets(); dist, _ = P.bfs(g, P.START)
    for k, cells in T.items():
        assert any(c in dist for c in cells), 'unreachable: ' + k
    for s in dist:                                     # from every stopping place, everything still reachable
        ds, _ = P.bfs(g, s)
        assert P.START in ds, 'stuck at %s' % (s,)
        for k, cells in T.items(): assert any(c in ds for c in cells), 'from %s cannot reach %s' % (s, k)
    return len(dist)

def path(g, src, cells):
    dist, prev = P.bfs(g, src)
    end = min((c for c in cells if c in dist), key=lambda c: dist[c]); out = []; p = end
    while prev[p] is not None: q, d = prev[p]; out.append((q, p)); p = q
    return out[::-1], end

def tour(g):
    T = P.targets(); best = None
    for order in itertools.permutations(['NW', 'NE', 'SW', 'SE']):
        p, legs = P.START, []
        for k in list(order) + ['door']:
            seg, p = path(g, p, T[k]); legs.append((k, seg))
        n = sum(len(s) for _, s in legs)
        if best is None or n < best[0]: best = (n, legs)
    return best

COL = {'NW': (255, 110, 110), 'NE': (110, 240, 130), 'SW': (110, 170, 255), 'SE': (255, 210, 80), 'door': (255, 255, 255)}
def draw(img, legs):
    d = ImageDraw.Draw(img); s = 32; step = 0
    c = lambda p: (p[0] * s + s // 2, p[1] * s + s // 2)
    for k, seg in legs:
        for (a, b) in seg:
            (x0, y0), (x1, y1) = c(a), c(b)
            d.line([(x0, y0), (x1, y1)], fill=COL[k], width=4)
            dx, dy = (x1 > x0) - (x1 < x0), (y1 > y0) - (y1 < y0)       # an arrowhead at the stop
            hx, hy = x1 - dx * 9, y1 - dy * 9
            d.polygon([(x1, y1), (hx - dy * 6, hy - dx * 6), (hx + dy * 6, hy + dx * 6)], fill=COL[k])
        for (a, b) in seg:
            step += 1; x, y = c(b)
            d.rectangle([x - 9, y - 16, x + 9, y - 4], fill=(0, 0, 0)); d.text((x - 7, y - 16), str(step), fill=COL[k])
    y = 4
    for k, seg in legs:
        d.rectangle([8, y, 26, y + 12], fill=COL[k])
        d.text((32, y), ('to the door of Kimaris\'s chamber' if k == 'door' else 'to the %s bonfire' % k) + ': %d moves' % len(seg), fill=(255, 255, 255))
        y += 16
    return img

if __name__ == '__main__':
    mockdir = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/necro'
    out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(mockdir, 'necropolis_lake_route.png')
    g, _, _ = P.generate(L.SEED, n_graves=L.NGRAVES)
    n = check(g); total, legs = tour(g)
    print('stopping places', n, '- all can reach every bonfire, the door and the landing')
    print('tour', total, 'moves:', ', '.join('%s %d' % (k, len(s)) for k, s in legs))
    img = Image.open(os.path.join(mockdir, 'necropolis_lake_lit_2x.png')).convert('RGB')
    draw(img, legs).save(out)
