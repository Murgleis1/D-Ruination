"""Mt. Mirroh B1F, core layout options v3 (user 2026-11-24: "that purple thing going through everything and the thing
at the center of the ruin at the top doesn't look good and needs more work. This layout you've designed is all over the
place. Go look at more examples in the games I mentioned and come up with a better core design").

What the references taught (assets/mt_mirroh_reference/b1f_refs_v3.png):
  * a strong set-piece chamber has ONE axis and ONE focal piece, walls stepping in toward it: MonoMyth's funnel
    (86ce0c, terraces converging on the point at the top), Crown's shrine nave (2.35), Odyssey's crystal shrine (2.34,
    the monolith set in the back wall, crystals and bones strewn), Crown's octagon sanctum (1.120, a cross-shaped dais);
  * destruction is told with the floor, not with light: Lazarus' blast pit (facf4c: a dark pit, crack decals all
    over the floor, boulders flung out), its pillar-ringed chamber (facaec);
  * a hideout sits in a pocket framed by the cave (MonoMyth's Mt. Thunder hideout, 86d774).
Three options, each a whole new core; the purple fissure and the painted round dais are gone from all three (the
shattering is shown by cracked floor, a pit, flung stone; violet light only in the wound itself).

Letters: '#' rock, '.' floor, 'S' stairs, 'L' ladder, 'D' dressed stone floor (the temple's), 'A' the altar,
'P' the pit (solid), 'k' cracked floor (walkable), 'p' pillar standing (solid), 'b' pillar broken/toppled (solid),
'r' rubble (solid), 'w' temple wall, broken (solid), 'c' the camp (props, solid), 'e' the empty shard sockets.
Usage: python3 plan_b1f3.py OUTDIR"""
import os, sys, math
import numpy as np
from PIL import Image, ImageDraw

def grid(W, H): return np.full((H, W), '#', dtype='<U1')
def r(G, x0, y0, x1, y1, ch): G[y0:y1 + 1, x0:x1 + 1] = ch
def ell(G, cx, cy, rx, ry, ch, only=None):
    H, W = G.shape
    for y in range(H):
        for x in range(W):
            if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1 and (only is None or G[y, x] in only): G[y, x] = ch

def option_a():
    """A, the Processional Nave (MonoMyth 86ce0c + Crown 2.35): the ladder lands at the foot of a long nave that
    climbs north in three tiers between ranks of the temple's pillars, most broken, its walls stepping inward; at the
    head, up the last stairs, the apse: the altar against the back wall, split, the floor around it cracked, the
    empty sockets of the nine Shards before it. The camp in a side pocket off the lowest tier; a side chapel fallen in
    on the other side."""
    W, H = 32, 44; G = grid(W, H)
    r(G, 12, 38, 19, 42, '.'); G[41, 15] = 'L'                      # the landing
    r(G, 7, 29, 24, 37, '.')                                       # tier 1
    r(G, 9, 18, 22, 28, '.')                                       # tier 2
    r(G, 11, 4, 20, 17, '.')                                       # the apse (tier 3)
    for (y, x0, x1) in ((28, 9, 22), (17, 11, 20)):                 # the bands between tiers, stairs on the axis
        r(G, x0, y, x1, y, '#'); r(G, 15, y, 16, y, 'S')
    r(G, 15, 37, 16, 37, 'S')                                       # landing up into tier 1
    r(G, 7, 37, 14, 37, '#'); r(G, 17, 37, 24, 37, '#')
    r(G, 12, 5, 19, 13, 'D'); r(G, 14, 4, 17, 5, 'A')               # the apse's dressed floor, the altar
    for x in (13, 15, 16, 18): G[8, x] = 'e'
    for x in (12, 19): G[10, x] = 'e'
    G[11, 14] = 'e'; G[11, 17] = 'e'; G[9, 15] = 'e'
    for (x, y) in ((14, 6), (17, 6), (13, 7), (18, 7), (15, 7), (16, 9), (14, 10), (17, 12), (12, 12), (19, 9)):
        if G[y, x] in '.D': G[y, x] = 'k'
    for (x, y, ch) in ((8, 30, 'p'), (8, 33, 'b'), (8, 36, 'p'), (23, 30, 'b'), (23, 33, 'p'), (23, 36, 'r'),
                       (10, 20, 'p'), (10, 23, 'b'), (10, 26, 'p'), (21, 20, 'r'), (21, 23, 'p'), (21, 26, 'b'),
                       (12, 14, 'p'), (19, 14, 'b'), (12, 5, 'p'), (19, 5, 'p')):
        G[y, x] = ch
    r(G, 1, 31, 6, 36, '.'); r(G, 2, 32, 4, 34, 'c')                # the camp's pocket
    r(G, 25, 19, 30, 27, 'r'); r(G, 23, 22, 24, 24, '.')            # the fallen side chapel (sealed by rubble)
    G[22, 25] = '.'; G[23, 25] = '.'
    return G

def option_b():
    """B, the Blast Crater (Lazarus facf4c + facaec + MonoMyth 86e14c): one great round cavern; where the altar and
    its Dreamstone stood is now a pit, the floor around it cracked in rings, the temple's ring of pillars flung outward
    and toppled, a few still standing; the back half of the cavern a raised rim (the temple's surviving terrace,
    stairs up), its broken facade along the back wall; the altar's last half teetering on the pit's north lip. The
    ladder in a short passage south, the camp in a south-west alcove."""
    W, H = 40, 38; G = grid(W, H)
    ell(G, 20, 17, 17.5, 14.5, '.')
    r(G, 17, 31, 23, 35, '.'); G[34, 20] = 'L'                      # the passage and the ladder
    r(G, 2, 24, 8, 30, '.'); r(G, 3, 26, 5, 28, 'c'); r(G, 7, 26, 9, 28, '.')   # the camp's alcove
    # the rim: the back (north) half raised behind a band, stairs up at both sides
    for x in range(W):
        for y in range(H):
            if G[y, x] == '.' and 6 <= y <= 7 and 6 <= x <= 34: G[y, x] = '#'
    r(G, 9, 6, 10, 7, 'S'); r(G, 29, 6, 30, 7, 'S')
    r(G, 10, 3, 29, 5, 'D'); r(G, 11, 2, 28, 2, 'w')                # the terrace's dressed floor, the broken facade
    for x in (13, 17, 22, 26): G[2, x] = '.'                        # (breaches in it)
    ell(G, 20, 18, 9.5, 6.5, 'k', only='.')                         # cracked floor round the pit
    ell(G, 20, 18, 5.5, 3.8, 'P')                                   # the pit
    r(G, 19, 13, 21, 14, 'A')                                       # the altar's half on the north lip
    for k in range(10):                                             # the pillar ring, flung outward
        a = 2 * math.pi * k / 10 + 0.3; x = int(round(20 + 12.5 * math.cos(a))); y = int(round(18 + 8.8 * math.sin(a)))
        if 0 < y < H and G[y, x] in '.k': G[y, x] = 'p' if k in (1, 4, 8) else 'b'
        x2 = int(round(20 + 14.5 * math.cos(a))); y2 = int(round(18 + 10.5 * math.sin(a)))
        if k not in (1, 4, 8) and G[y2, x2] == '.': G[y2, x2] = 'r'
    return G

def option_c():
    """C, Cave then Sanctum (MonoMyth 86d774 + Crown 1.120/1.122 + Odyssey 2.34): two rooms on one axis. The ladder
    comes down into a rough cave where the cult camped, its tents in a hollow ringed by the cave's terraces. North of
    it the temple's facade spans the cave, seen face on, broken open in the middle, rubble heaped either side. Through
    the breach, the sanctum: an octagon of dressed stone, pillars at its corners (two broken), a cross-shaped floor,
    and at its head against the back wall the altar, split, the floor cracked out from it, the nine Shards' empty
    sockets in a ring before it."""
    W, H = 32, 46; G = grid(W, H)
    # the cave (south)
    r(G, 3, 29, 28, 42, '.'); r(G, 3, 29, 5, 31, '#'); r(G, 26, 29, 28, 31, '#'); r(G, 3, 40, 6, 42, '#'); r(G, 25, 39, 28, 42, '#')
    G[41, 22] = 'L'; G[40, 22] = '.'
    r(G, 11, 33, 20, 38, '.'); r(G, 10, 32, 21, 32, '#'); r(G, 10, 39, 13, 39, '#'); r(G, 18, 39, 21, 39, '#')  # the hollow
    r(G, 10, 32, 10, 39, '#'); r(G, 21, 32, 21, 39, '#'); r(G, 14, 39, 17, 39, 'S')
    for (x0, y0, x1, y1) in ((12, 34, 13, 35), (18, 34, 19, 35), (15, 36, 16, 36)): r(G, x0, y0, x1, y1, 'c')
    # the facade, face on, its breach
    r(G, 4, 26, 27, 28, 'w'); r(G, 14, 26, 17, 28, '.'); r(G, 14, 28, 17, 28, 'S')
    for (x, y) in ((12, 29), (13, 29), (18, 29), (19, 29), (11, 30), (20, 30)): G[y, x] = 'r'
    # the sanctum: an octagon
    r(G, 6, 4, 25, 25, '.')
    for k in range(4):
        for t in range(4 - k):
            for (x, y) in ((6 + t, 4 + k), (25 - t, 4 + k), (6 + t, 25 - k), (25 - t, 25 - k)): G[y, x] = '#'
    r(G, 13, 5, 18, 24, 'D'); r(G, 8, 13, 23, 17, 'D')              # the cross-shaped floor
    r(G, 14, 4, 17, 6, 'A')                                         # the altar against the back wall
    for (x, y) in ((15, 7), (16, 8), (14, 8), (17, 9), (13, 7), (18, 7), (15, 10), (12, 9), (19, 10)): G[y, x] = 'k'
    for k in range(9):
        a = math.pi * (0.15 + 0.7 * k / 8); x = int(round(15.5 - 4.6 * math.cos(a))); y = int(round(9 + 3.6 * math.sin(a)))
        G[y, x] = 'e'
    for (x, y, ch) in ((10, 8, 'p'), (21, 8, 'b'), (10, 21, 'b'), (21, 21, 'p'), (8, 12, 'p'), (23, 12, 'p'),
                       (8, 18, 'b'), (23, 18, 'p')):
        G[y, x] = ch
    return G

COL = {'#': (58, 60, 78), '.': (176, 196, 220), 'S': (240, 180, 80), 'L': (250, 220, 60), 'D': (214, 214, 226),
       'A': (120, 90, 160), 'P': (14, 8, 24), 'k': (150, 150, 170), 'p': (240, 240, 250), 'b': (130, 130, 150),
       'r': (110, 100, 96), 'w': (150, 140, 170), 'c': (190, 120, 70), 'e': (160, 110, 230)}
SOLID = set('#PApbrwc')

def check(G):
    """every walkable cell reachable from the ladder"""
    H, W = G.shape; L = tuple(np.argwhere(G == 'L')[0])
    seen = {L}; st = [L]
    while st:
        y, x = st.pop()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            q = (y + dy, x + dx)
            if 0 <= q[0] < H and 0 <= q[1] < W and q not in seen and G[q] not in SOLID: seen.add(q); st.append(q)
    walk = {tuple(p) for p in np.argwhere(~np.isin(G, list(SOLID)))}
    return len(walk - seen)

def picture(G, title, s=10):
    H, W = G.shape; im = Image.new('RGB', (W * s, H * s + 18), (20, 20, 28)); d = ImageDraw.Draw(im)
    for y in range(H):
        for x in range(W):
            c = COL[G[y, x]]; d.rectangle((x * s, 18 + y * s, x * s + s - 1, 18 + y * s + s - 1), fill=c)
            if G[y, x] == 'P': pass
            if G[y, x] == 'k': d.line((x * s + 2, 18 + y * s + 2, x * s + s - 3, 18 + y * s + s - 3), fill=(80, 80, 100))
    if (G == 'P').any():                                            # (the wound's faint violet, in the pit alone)
        for (y, x) in np.argwhere(G == 'P'):
            if ((G[max(0, y - 1):y + 2, max(0, x - 1):x + 2] == 'P').all()):
                d.rectangle((x * s + 3, 18 + y * s + 3, x * s + s - 4, 18 + y * s + s - 4), fill=(70, 30, 110))
    d.text((4, 3), title, fill=(255, 255, 255))
    return im

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
    ims = []
    for f, t in ((option_a, 'A  Processional Nave  32x44'), (option_b, 'B  Blast Crater  40x38'),
                 (option_c, 'C  Cave, then Sanctum  32x46')):
        G = f(); print(t, 'unreachable', check(G)); ims.append(picture(G, t))
    Wt = sum(i.width for i in ims) + 40; Ht = max(i.height for i in ims) + 150
    sheet = Image.new('RGB', (Wt, Ht), (20, 20, 28)); x = 10
    for i in ims: sheet.paste(i, (x, 0)); x += i.width + 10
    d = ImageDraw.Draw(sheet); y = Ht - 140; x = 10
    for k, name in (('#', 'rock'), ('.', 'cave floor'), ('D', 'temple floor'), ('S', 'stairs'), ('L', 'ladder up'),
                    ('A', 'altar (split)'), ('e', "Shards' empty sockets"), ('k', 'cracked floor'), ('P', 'pit'),
                    ('p', 'pillar'), ('b', 'broken pillar'), ('r', 'rubble'), ('w', 'temple wall, broken'),
                    ('c', 'cult camp')):
        d.rectangle((x, y, x + 14, y + 14), fill=COL[k]); d.text((x + 20, y + 2), name, fill=(230, 230, 230))
        x += 190
        if x > Wt - 190: x = 10; y += 24
    sheet.save(os.path.join(out, 'b1f_layouts_v3.png'))
