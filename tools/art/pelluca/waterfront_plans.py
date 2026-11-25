"""Pelluca Valley's south waterfront, redesign: three block-plan options (user 2026-11-24: "Why didn't you study
Watercress City's port and all that from MonoMyth before you designed the whole dock area in Pelluca Valley?";
then "proceed... Do this ahead of the last three stage 1 jobs because this is a big deal and we need to get the design
right").

The references, studied as compositions (assets/pelluca_dock_spec/waterfront_refs.png):
  * MonoMyth, Watercress Port (0x869C10): the town steps down in terraces to ONE quay; a stair on the main axis lands
    mid-quay; light dressed stone with a white kerb and a shadowed drop to the water; pier FINGERS of different
    lengths at a rhythm, boats moored in the slips between; harbour kiosks, crate stacks at the pier roots, flower
    boxes, lamp pairs with bunting strung between; a breakwater of rocks round the basin; cliffs into the water;
  * Crown, the harbour market town: a stone town on a raised sea wall (drain grates in its face), stairs down to a
    lower WOODEN boardwalk and wooden piers loaded with barrels and crates; market stalls on the stone;
  * Lazarus, its autumn harbour (faa2ac): cliff terraces with stairs down to a landing on a sheltered lagoon, the
    lagoon closed by rocky reef arms; pale shallow water inside, deep outside; rowboats moored inside;
  * Odyssey 3.1 / 3.22: a pale shallow band along every shore, deep water beyond, rocks scattered off the coast;
  * MonoMyth Port Ginseng: stone-edged canal quays and bridges.
What Pelluca must carry (unchanged above row 33; everything below may change):
  * the town's two stairs down the lower cliff: the main spine's (x 37-39) and the west one (x 24-25);
  * the Seaside Tavern (x 25-31, door (28, 43)) and the Umbra lab tower (x 44-49, door (47, 44)); either may move a
    little with its warp; the sealed cave door in the west cliff (10-11, 35);
  * the cold open (DR_PellucaCity_Arrival): the Pale Veluza berths, Osrid lands, Cadmus walks down to meet him, the two
    walk past the SHRINE to the lost prince (and its keeper) to the lab door; its movements are rewritten to fit;
  * the fisherman of the Fisherman's Dilemma (the south dock), the second ship, two rowboats, the beach people;
  * the south edge stays open water (the Surf way to Route 10).
Letters (rows 34-59 only): '#' cliff/rock, 'S' stairs, 'q' quay stone, 'k' quay kerb (walkable edge), 'x' sea wall
(solid), 'p' stone pier, 'w' wooden boardwalk/pier, 's' sand, 'B' building, 'K' kiosk/stall, 'm' market stall,
'c' crates/barrels, 'l' lamp, 'f' flower box, 'h' shrine, 'P' palm, 'o' rock in water, 'r' rowboat, 'V' big ship,
'-' shallow water, '~' deep water, 'T' trees.
Usage: python3 waterfront_plans.py OUTDIR"""
import os, sys, math
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__))
W, H, TOP = 80, 60, 34

def base():
    G = np.full((H, W), '~', dtype='<U1')
    G[:TOP] = '.'                                     # (the town above: drawn from the game's own render)
    G[34:36, :] = '#'
    G[34:36, 37:40] = 'S'; G[34:36, 24:26] = 'S'
    G[36:46, 0:8] = 'T'; G[36:46, 72:80] = 'T'
    return G
def r(G, x0, y0, x1, y1, ch): G[y0:y1 + 1, x0:x1 + 1] = ch
def shore(G, x0, x1, rows, ch='s'):
    """sand from row 36 down to a ragged waterline rows[x - x0]"""
    for x in range(x0, x1 + 1):
        G[36:rows[x - x0] + 1, x] = ch
def shallow(G, depth=2):
    """a pale shallow band (Odyssey/Lazarus) along every land edge, `depth` cells out"""
    land = ~np.isin(G, ['~', '-', 'o', 'r', 'V'])
    from scipy.ndimage import binary_dilation
    near = binary_dilation(land, iterations=depth) & (G == '~')
    G[near] = '-'

# ------------------------------------------------------------------------------------------------- A: Watercress
def option_a():
    """A, the Watercress harbour: the main stair lands mid-quay; one quay of pale dressed stone with a white kerb
    from the beach's sea wall to the east woods; three stone pier fingers at a rhythm (the great pier on the axis for
    the Pale Veluza, a short one for the rowboats, a long one for the second ship); the lab and the shrine at the great
    pier's root; a harbour kiosk, crates at each pier root, lamp pairs with bunting; a rock breakwater closing the
    basin with a mouth to the south; the beach west of a low sea wall with steps, the fisherman's wooden jetty."""
    G = base()
    r(G, 33, 36, 71, 41, 'q'); r(G, 33, 41, 71, 41, 'k')                      # one quay, six deep (as Watercress')
    r(G, 32, 36, 32, 41, 'x'); r(G, 32, 38, 32, 39, 'S')                      # (the low sea wall, steps through it)
    r(G, 44, 36, 49, 39, 'B')                                                 # the lab tower against the cliff (door (47, 39))
    G[40, 42] = 'h'                                                           # the shrine, at the great pier's root
    r(G, 56, 36, 59, 37, 'K')                                                 # the harbour master's kiosk
    for x in (34, 35, 41, 51, 52, 53, 62, 63, 66, 67, 68): G[36, x] = 'f'     # flower boxes along the cliff foot
    # the great pier on the axis (x 37-39), its head widened (x 35-41), the Pale Veluza's berth to its east
    r(G, 37, 42, 39, 52, 'p'); r(G, 35, 50, 41, 53, 'p')
    r(G, 42, 49, 47, 55, 'V')
    G[41, 36] = 'l'; G[41, 40] = 'l'; G[50, 35] = 'l'; G[50, 41] = 'l'
    r(G, 34, 40, 35, 40, 'c'); r(G, 40, 53, 41, 53, 'c')
    # the short pier (rowboats either side) and the long east pier (the second ship)
    r(G, 53, 42, 54, 47, 'p'); G[44, 51] = 'r'; G[45, 56] = 'r'; G[40, 52] = 'c'; G[40, 55] = 'c'
    r(G, 63, 42, 65, 52, 'p'); r(G, 66, 44, 70, 51, 'V'); r(G, 61, 40, 62, 40, 'c'); G[41, 63] = 'l'; G[41, 65] = 'l'
    G[41, 47] = 'l'; G[41, 58] = 'l'
    # the breakwater: rocks in a close arc from the east woods round the basin's south; the mouth at x 46-56
    arc = [(71, 46), (71, 48), (71, 50), (70, 52), (69, 54), (67, 55), (65, 56), (63, 57), (61, 57), (59, 58), (57, 58),
           (45, 58), (43, 58), (41, 58), (39, 57), (37, 57), (35, 56), (33, 56), (31, 55), (29, 55)]
    for (x, y) in arc: G[y, x] = 'o'
    # the beach: sand to a ragged waterline, the tavern, palms in groups, the fisherman's jetty
    rows = [46, 46, 47, 47, 47, 48, 48, 48, 47, 47, 47, 46, 46, 46, 47, 47, 46, 46, 45, 45, 45, 44, 44, 44]
    shore(G, 8, 31, rows)
    r(G, 25, 37, 31, 42, 'B')                                                 # the Seaside Tavern (door (28, 42))
    for (x, y) in [(10, 37), (12, 38), (17, 37), (19, 39), (13, 43), (21, 41), (9, 42)]: G[y, x] = 'P'
    r(G, 16, 47, 17, 53, 'w'); r(G, 15, 52, 18, 53, 'w'); G[54, 19] = 'r'
    for (x, y) in [(3, 47), (5, 48), (2, 50), (6, 51), (9, 52)]: G[y, x] = 'o'
    shallow(G); return G

# ------------------------------------------------------------------------------------------------ B: Crown's wall
def option_b():
    """B, Crown's sea wall and boardwalk market: the town's stone runs out onto an upper quay that ends in a tall
    sea wall (drain grates in its face); three stairs down it to a lower wooden boardwalk along the water, from which
    wooden piers run out, loaded with barrels and crates; the harbour market's striped stalls on the upper quay; the
    lab and the shrine on the upper quay by the axis stair; the boardwalk runs west down onto the beach."""
    G = base()
    r(G, 33, 36, 71, 41, 'q'); r(G, 33, 42, 71, 42, 'x')                      # the upper quay, its sea wall
    for x0 in (37, 55, 67): r(G, x0, 42, x0 + 1, 42, 'S')
    r(G, 29, 43, 71, 45, 'w')                                                 # the lower boardwalk
    r(G, 44, 36, 49, 40, 'B'); G[41, 42] = 'h'                                # the lab (door (47, 40)), the shrine
    for x in range(51, 65, 3): r(G, x, 37, x + 1, 37, 'm')                    # the market: two rows of stalls
    for x in range(52, 66, 3): r(G, x, 39, x + 1, 39, 'm')
    for (x, y) in [(34, 37), (35, 37), (66, 37), (69, 38), (70, 38)]: G[y, x] = 'c'
    # wooden piers: the axis pier for the Pale Veluza, two more
    r(G, 37, 46, 39, 55, 'w'); r(G, 40, 50, 45, 56, 'V'); r(G, 36, 55, 40, 55, 'c')
    r(G, 51, 46, 52, 50, 'w'); G[47, 49] = 'r'; G[48, 54] = 'r'
    r(G, 62, 46, 63, 53, 'w'); r(G, 64, 47, 68, 53, 'V')
    for x in (31, 41, 47, 58, 70): G[44, x] = 'c'
    # the beach: the boardwalk comes down onto it; the tavern; palms; the fisherman at a rock point
    rows = [46, 46, 47, 47, 48, 48, 48, 47, 47, 46, 46, 47, 47, 48, 48, 47, 47, 46, 46, 46, 45]
    shore(G, 8, 28, rows)
    r(G, 25, 37, 31, 42, 'B'); r(G, 29, 37, 32, 42, 's'); r(G, 25, 37, 31, 42, 'B')
    for (x, y) in [(10, 38), (13, 37), (18, 38), (20, 40), (11, 43), (16, 44)]: G[y, x] = 'P'
    for (x, y) in [(9, 49), (10, 50), (12, 50), (13, 51)]: G[y, x] = 'o'
    for (x, y) in [(3, 47), (5, 49), (22, 53), (30, 57), (50, 58), (74, 55)]: G[y, x] = 'o'
    shallow(G); return G

# --------------------------------------------------------------------------------------------- C: Lazarus' cove
def option_c():
    """C, Lazarus' sheltered cove: below the cliff the town comes down in two stone tiers (the upper quay; stairs
    on the axis to a lower landing on the water); the harbour is a lagoon closed by two rocky arms reaching round
    from the east shore and the beach's west point, pale shallow water inside, deep outside; rowboats and a small
    jetty inside; the great pier runs out from the landing through the lagoon's mouth to deep water, where the Pale
    Veluza and the second ship lie; the beach is the lagoon's inner west shore."""
    G = base()
    r(G, 33, 36, 71, 40, 'q'); r(G, 33, 41, 71, 41, 'x'); r(G, 37, 41, 39, 41, 'S'); r(G, 60, 41, 61, 41, 'S')
    r(G, 34, 42, 66, 44, 'q'); r(G, 34, 44, 66, 44, 'k')                      # the lower landing
    r(G, 44, 36, 49, 39, 'B'); G[40, 42] = 'h'
    r(G, 56, 36, 59, 37, 'K'); r(G, 35, 36, 36, 37, 'c'); r(G, 68, 37, 69, 38, 'c')
    r(G, 37, 45, 39, 56, 'p'); r(G, 35, 55, 41, 57, 'p'); r(G, 42, 54, 47, 59, 'V')
    r(G, 52, 45, 53, 48, 'w'); G[46, 50] = 'r'; G[47, 55] = 'r'; G[49, 57] = 'r'
    # the arms: rock and sand reefs, the mouth at x 34-45
    east = [(70, 45), (69, 46), (68, 47), (68, 48), (67, 49), (66, 50), (64, 51), (62, 52), (60, 53), (58, 54),
            (56, 54), (54, 55), (52, 55), (50, 56), (48, 56)]
    for (x, y) in east: r(G, x - 1, y, x, y, 'o')
    r(G, 70, 44, 71, 47, 'o'); r(G, 66, 51, 67, 52, 's'); r(G, 57, 54, 58, 55, 's')
    west = [(20, 50), (21, 51), (22, 52), (24, 53), (26, 54), (28, 54), (30, 55), (32, 55)]
    for (x, y) in west: r(G, x, y, x + 1, y, 'o')
    r(G, 23, 52, 25, 52, 's')
    r(G, 64, 55, 69, 59, 'V') if False else None
    r(G, 66, 50, 71, 54, '~'); r(G, 72, 47, 77, 53, 'V')                       # (the second ship outside the east arm)
    rows = [46, 46, 47, 47, 48, 48, 49, 49, 49, 50, 50, 50, 49, 49, 48, 47, 47, 46, 46, 45, 45, 44, 44, 44, 44]
    shore(G, 8, 32, rows)
    r(G, 25, 37, 31, 42, 'B')
    for (x, y) in [(10, 37), (12, 39), (17, 37), (19, 39), (14, 44), (21, 42), (9, 43)]: G[y, x] = 'P'
    r(G, 27, 45, 28, 49, 'w')
    for (x, y) in [(3, 47), (5, 48), (6, 50)]: G[y, x] = 'o'
    # the lagoon: shallow inside the arms
    from scipy.ndimage import binary_fill_holes
    lag = np.zeros(G.shape, bool); lag[42:57, 20:72] = True
    inside = lag & (G == '~')
    for y in range(42, 57):
        for x in range(20, 72):
            if G[y, x] != '~': continue
            # inside if a rock or land lies south of it in this column, within the arms' span
            if any(G[yy, x] in 'os' for yy in range(y, min(H, 57))) and 20 <= x <= 71: G[y, x] = '-'
    for y in range(45, 56):
        for x in range(33, 48):
            if G[y, x] == '~': G[y, x] = '-'
    shallow(G, 1); return G

COL = {'#': (92, 84, 104), 'S': (238, 196, 110), 'q': (214, 212, 204), 'k': (246, 246, 240), 'x': (150, 146, 150),
       'p': (196, 194, 188), 'w': (178, 132, 84), 's': (236, 214, 150), 'B': (150, 70, 90), 'K': (220, 120, 120),
       'm': (210, 90, 90), 'c': (130, 90, 50), 'l': (60, 60, 70), 'f': (230, 120, 170), 'h': (250, 230, 120),
       'P': (60, 150, 80), 'o': (110, 110, 124), 'r': (160, 110, 60), 'V': (250, 250, 252), '-': (110, 170, 230),
       '~': (44, 96, 180), 'T': (34, 100, 60), '.': (0, 0, 0)}

def picture(G, title, town, s=10):
    top0 = 22
    im = Image.new('RGB', (W * s, (H - top0) * s + 20), (20, 20, 28)); d = ImageDraw.Draw(im)
    t = town.crop((0, top0 * 16, W * 16, TOP * 16)).resize((W * s, (TOP - top0) * s))
    im.paste(t, (0, 20))
    for y in range(TOP, H):
        for x in range(W):
            c = COL[G[y, x]]; d.rectangle((x * s, 20 + (y - top0) * s, x * s + s - 1, 20 + (y - top0) * s + s - 1), fill=c)
            if G[y, x] == 'k': d.line((x * s, 20 + (y - top0) * s + s - 1, x * s + s - 1, 20 + (y - top0) * s + s - 1), fill=(90, 90, 110))
    d.line((38 * s + s // 2, 20, 38 * s + s // 2, 20 + 4), fill=(255, 255, 0))
    d.text((4, 4), title, fill=(255, 255, 255))
    return im

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else '/tmp'
    town = Image.open(sys.argv[2]) if len(sys.argv) > 2 else Image.open('/home/claude/scratch/pelluca_now.png')
    ims = [picture(option_a(), 'A  Watercress harbour: one quay, three stone piers, a breakwater', town),
           picture(option_b(), "B  Crown's sea wall: upper quay + market, stairs down to a wooden boardwalk and piers", town),
           picture(option_c(), "C  Lazarus' cove: two stone tiers down to a lagoon closed by rocky arms", town)]
    leg = [('#', 'cliff'), ('S', 'stairs'), ('q', 'quay stone'), ('k', 'quay kerb'), ('x', 'sea wall'), ('p', 'stone pier'),
           ('w', 'wooden pier'), ('s', 'sand'), ('B', 'tavern / lab'), ('K', 'kiosk'), ('m', 'market stall'),
           ('c', 'crates'), ('l', 'lamp'), ('f', 'flower box'), ('h', 'shrine'), ('P', 'palm'), ('o', 'rocks'),
           ('r', 'rowboat'), ('V', 'ship'), ('-', 'shallows'), ('~', 'deep water')]
    sheet = Image.new('RGB', (ims[0].width, sum(i.height for i in ims) + 90), (20, 20, 28)); y = 0
    for i in ims: sheet.paste(i, (0, y)); y += i.height
    d = ImageDraw.Draw(sheet); x = 6; yy = y + 8
    for k, n in leg:
        d.rectangle((x, yy, x + 12, yy + 12), fill=COL[k]); d.text((x + 16, yy + 1), n, fill=(230, 230, 230)); x += 112
        if x > sheet.width - 112: x = 6; yy += 22
    sheet.save(os.path.join(out, 'waterfront_layouts_v1.png'))
