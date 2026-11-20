"""Mock: the shrine's awakening (user 2026-11-20). With the field solved, pressing A on the Arceus statue awakens the
holy power of the site: the ice melts off the statue, a holy light floods the chamber, the two fire rings beside the
logs light up, then Osrid: "Something fell down out of the ice... could this be...!!" and the player finds the
Sparkling Opal.

This draws the art the sequence needs, for approval before it is built:
  * the melt: frames of the ice block sinking, thinning and dripping off the statue, then the bare statue standing
    in a little meltwater;
  * the lit fire rings: flame frames (animated in game) in two colourings to choose from: warm firelight, or a holy
    sapphire-and-white flame matching the statue's gems;
  * the Sparkling Opal's bag icon (24x24; drawn here: a milky opal with a play of colour).
Usage: ODYSSEY_ROM=/path/Crown.gba python3 tools/art/icepath/awaken_mock.py [outdir]
"""
import os, sys
os.environ.setdefault('ODYSSEY_ROM', '/home/claude/crown/Crown.gba')
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import arceus_statue as AS
import icepath_mock as M

WATER = [(70, 120, 160), (104, 160, 200), (150, 200, 226)]

def melted(f, seed=11):
    """The statue with its ice at melt stage f (0 = as found, 1 = gone): the block's top sinks, the crystal points
    shorten, the ice thins (more stone shows through), drips hang off its rim; past 1, none."""
    img, m = AS.statue(ice=False); H, W = m.shape
    if f >= 1: return img, m
    fr, fm = AS.figure(); fh = fm.shape[0]
    top = int(fh * 0.72 + (H - 4 - fh * 0.72) * f); rng = np.random.default_rng(seed)
    edge = np.full(W, top + 6)
    for _ in range(9):
        cx = int(rng.integers(2, W - 2)); hgt = int(rng.integers(4, 11) * (1 - f)); half = int(rng.integers(2, 5))
        for x in range(max(0, cx - half), min(W, cx + half + 1)):
            edge[x] = min(edge[x], top + 6 - hgt + abs(x - cx) * hgt // (half + 1))
    ice = np.zeros(m.shape, bool)
    shrink = int(round(f * 4))                              # the block narrows as it melts
    for x in range(W):
        for y in range(max(0, edge[x]), H):
            flare = (y - top) // 6
            inset = max(0, 4 - flare) + shrink
            if x < inset or x > W - 1 - inset: continue
            ice[y, x] = True
    out = img.astype(float).copy(); om = m.copy()
    facet = ((np.arange(W)[None, :] + np.arange(H)[:, None] // 2) // 4) % 2
    clear = 0.5 + 0.35 * f                                  # thinner ice: more stone through it
    for y, x in zip(*np.nonzero(ice)):
        tone = np.array(AS.ICE[3] if facet[y, x] else AS.ICE[4], float)
        out[y, x] = out[y, x] * clear + tone * (1 - clear) if m[y, x] else tone
        om[y, x] = True
    for y, x in zip(*np.nonzero(ice)):
        up = y == 0 or not ice[y - 1, x]
        side = x == 0 or x == W - 1 or not ice[y, x - 1] or not ice[y, x + 1]
        if up: out[y, x] = AS.ICE[5]
        elif side or y == H - 1: out[y, x] = AS.ICE[1]
    if 0 < f < 1:                                           # drips: wet streaks down the block's face
        for x in rng.choice(np.nonzero(ice.any(0))[0], 5, replace=False):
            ys = np.nonzero(ice[:, x])[0]; y0 = ys.min() + 1
            for y in range(y0, min(H, y0 + int(rng.integers(3, 7)))): out[y, x] = AS.ICE[2]
            out[min(H - 1, y0 + 7), x] = AS.ICE[5]
    return out.astype(np.uint8), om

def puddle(img, cx, y, f):
    """Meltwater spreading on the floor at the statue's foot (grows with f)."""
    w = int(8 + 12 * f); h = 1 + int(2 * f)
    yy, xx = np.mgrid[0:h * 2 + 1, 0:w * 2 + 1]
    e = ((xx - w) / max(1, w)) ** 2 + ((yy - h) / max(1, h)) ** 2 <= 1
    for (dy, dx) in zip(*np.nonzero(e)):
        py, px = y - h + dy, cx - w + dx
        if 0 <= py < img.shape[0] and 0 <= px < img.shape[1]:
            img[py, px] = (img[py, px].astype(int) * 0.55 + np.array(WATER[1]) * 0.45).astype(np.uint8)
            if dy == 0 or (dy < h and (dx + dy) % 7 == 0): img[py, px] = WATER[2]

FLAMES = {'warm': [(150, 36, 20), (220, 84, 24), (248, 160, 40), (252, 224, 120), (255, 250, 220)],
          'holy': [(28, 56, 120), (48, 104, 176), (96, 176, 240), (170, 228, 250), (250, 254, 255)]}

def flame(k, scheme, seed=3, scale=1.0):
    """Frame k (0-3) of a campfire's flames (16 wide, 18 tall, base at the bottom): three teardrop tongues, each
    drawn as nested shells (outer dark, then mid, hot core, white-hot heart), whose heights and lean change from
    frame to frame."""
    P = FLAMES[scheme]; rng = np.random.default_rng(seed + 7 * k)
    h, w = 18, 16; idx = np.full((h, w), -1)
    tongues = [(5.0, 11, 2.8), (8.0, 16, 3.6), (11.0, 12, 2.8)]
    for cx, ht, half in tongues:
        ht = int(round((ht + int(rng.integers(-2, 3))) * scale)); lean = float(rng.uniform(-1.6, 1.6))
        for level, scale in ((1, 1.0), (2, 0.72), (3, 0.46), (4, 0.22)):
            H_ = ht * (0.55 + 0.45 * scale); hw = half * scale + 0.2
            for y in range(int(H_)):
                frac = y / H_; width = hw * (1 - frac) ** 0.6 * (1 + 0.35 * np.sin(frac * 3.1))
                x0 = cx + lean * frac ** 1.5
                for x in range(w):
                    if abs(x + 0.5 - x0 - 0.5) <= width:
                        yy = h - 1 - y
                        if idx[yy, x] < level: idx[yy, x] = level
    for x in range(4, 12): idx[h - 1, x] = max(idx[h - 1, x], 1 + (x % 2))       # the embers
    img = np.zeros((h, w, 3), np.uint8); m = idx >= 0
    for lv in range(5): img[idx == lv] = P[lv]
    img[idx == 0] = P[0]
    return img, m

def opal_icon():
    """24x24 bag icon: a cabochon opal, milky blue-white, with soft patches of play of colour (blue, green, a little
    pink and gold), a dark rim and a bright highlight."""
    S = 24; img = np.zeros((S, S, 3), np.uint8); m = np.zeros((S, S), bool)
    yy, xx = np.mgrid[0:S, 0:S]; e = ((xx - 11.5) / 9.5) ** 2 + ((yy - 12.5) / 7.5) ** 2
    body = e <= 1; rim = body & (e > 0.8)
    BODY = [(150, 170, 204), (184, 202, 228), (212, 226, 244), (238, 244, 252)]
    shade = np.clip(((yy - 6) / 14 + (xx - 4) / 30) * 4, 0, 3).astype(int)
    for y, x in zip(*np.nonzero(body)): img[y, x] = BODY[3 - shade[y, x]]; m[y, x] = True
    import colorsys
    rng = np.random.default_rng(12)                   # play of colour (user: more rainbow): a patchwork of flashes,
    seeds = [(int(rng.integers(7, 19)), int(rng.integers(4, 20))) for _ in range(13)]   # each cell of the patchwork
    hues = [(i / 7 + rng.uniform(-0.03, 0.03)) % 1 for i in range(7)] * 2              # one spectral colour; a few
    rng.shuffle(hues)                                                                   # left milky
    d = np.stack([np.hypot(yy - sy, xx - sx) for sy, sx in seeds]); near = d.argmin(0); d.sort(0)
    for y, x in zip(*np.nonzero(body & ~rim)):
        k = near[y, x]
        if k == 3: continue
        edge = d[1, y, x] - d[0, y, x] < 0.5           # a milky seam between flashes
        if edge: continue
        lit = (y + x) % 5 == 0 or d[0, y, x] < 1.2
        r, g, b_ = colorsys.hsv_to_rgb(hues[k], 0.4 if lit else 0.78, 1.0 if lit else 0.95)
        c = np.array((r * 255, g * 255, b_ * 255)); a_ = 0.95 - 0.2 * (shade[y, x] / 3)
        img[y, x] = (img[y, x] * (1 - a_) + c * a_).astype(np.uint8)
    img[rim] = (64, 76, 116)
    img[6:8, 8:11] = (255, 255, 255); img[8, 7] = (255, 255, 255); img[16, 17] = (255, 255, 255)   # highlights
    return img, m

def shrine_base():
    """The composed ice path with the statue taken out (its cells back to floor, its head's wall row back to wall)."""
    full, _ = M.compose()
    base = full.copy(); cx = M.STATUE_CX * 16 + 8
    st0, sm0 = AS.statue(ice=True); y0 = (M.STATUE_BASE + 1) * 16 - st0.shape[0]; x0 = cx - st0.shape[1] // 2
    floor = M.TSI.meta(M.ROCK)
    for y in range(y0 // 16, (y0 + st0.shape[0] - 1) // 16 + 1):
        for x in range(x0 // 16, (x0 + st0.shape[1] - 1) // 16 + 1):
            if y >= 2: base[y * 16:y * 16 + 16, x * 16:x * 16 + 16] = floor
    wall = M.TSI.meta(M.IN_TOP)
    for x in range(x0 // 16, (x0 + st0.shape[1] - 1) // 16 + 1): base[16:32, x * 16:x * 16 + 16] = wall
    return base

FLAME_SCALE = 0.72                                    # (the build: the flames kept inside the fire ring's cell)

def scene(img_base, statue, fire_scheme=None, fire_k=0, puddle_f=None, glow=0.0):
    img = img_base.copy(); cx = M.STATUE_CX * 16 + 8
    st, sm = statue
    if puddle_f is not None: puddle(img, cx, (M.STATUE_BASE + 1) * 16 + 2, puddle_f)
    y0 = (M.STATUE_BASE + 1) * 16 - st.shape[0]; x0 = cx - st.shape[1] // 2
    sub = img[y0:y0 + st.shape[0], x0:x0 + st.shape[1]]; sub[sm] = st[sm]
    if fire_scheme:
        fl, fm = flame(fire_k, fire_scheme, scale=FLAME_SCALE)
        for x in M.FIRES:
            px, py = x * 16, (M.STATUE_BASE + 1) * 16 - fl.shape[0] - 3
            fm = fm.copy(); fm[:max(0, M.STATUE_BASE * 16 - py)] = False        # clipped to the ring's cell
            s2 = img[py:py + fl.shape[0], px:px + fl.shape[1]]; s2[fm] = fl[fm]
    if glow:
        img = (img.astype(float) * (1 - glow) + 255 * glow).astype(np.uint8)
    return img

def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    base = shrine_base(); floor = M.TSI.meta(M.ROCK)
    crop = lambda im: im[0:8 * 16, 2 * 16:14 * 16]
    frames = []
    for i, f in enumerate((0.0, 0.3, 0.55, 0.8, 1.0)):
        frames.append(crop(scene(base, melted(f), puddle_f=None if f == 0 else f)))
    frames.append(crop(scene(base, melted(1.0), puddle_f=1.0, glow=0.75)))          # the holy light
    for scheme in ('warm', 'holy'):
        frames.append(crop(scene(base, melted(1.0), fire_scheme=scheme, fire_k=0, puddle_f=1.0)))
    labels = ['as found', 'melting 1', 'melting 2', 'melting 3', 'melted', 'holy light', 'fires: warm', 'fires: holy']
    h, w = frames[0].shape[:2]; cols = 4; S = 3
    sheet = Image.new('RGB', (cols * (w * S + 8), 2 * (h * S + 8)), (24, 24, 28))
    for i, fr in enumerate(frames):
        sheet.paste(Image.fromarray(fr).resize((w * S, h * S), 0), ((i % cols) * (w * S + 8), (i // cols) * (h * S + 8)))
    sheet.save(os.path.join(outdir, 'awaken_sequence.png'))
    # flame frames and the icon, big
    tiles = []
    for scheme in ('warm', 'holy'):
        for k in range(4):
            fl, fm = flame(k, scheme); ring, rm = Image.open(os.path.join(M.ROOT, 'assets/monomyth_reference/pieces/tarragon_fire_ring.png')).convert('RGBA'), None
            c = np.array(floor).copy(); c = np.vstack([np.array(floor)[-6:], c])
            r = np.array(ring); rmask = r[..., 3] > 0; c[6:][rmask] = r[..., :3][rmask]
            sub = c[22 - fl.shape[0] - 3:22 - 3]; sub[fm] = fl[fm]
            tiles.append(c)
    ic, im_ = opal_icon(); icon = np.zeros((24, 24, 3), np.uint8) + 40; icon[im_] = ic[im_]
    row = np.concatenate([np.pad(t, ((0, 2), (0, 2), (0, 0))) for t in tiles], 1)
    big = Image.fromarray(row).resize((row.shape[1] * 6, row.shape[0] * 6), 0)
    out = Image.new('RGB', (big.width + 24 * 6 + 30, big.height), (24, 24, 28)); out.paste(big, (0, 0))
    out.paste(Image.fromarray(icon).resize((144, 144), 0), (big.width + 20, 0))
    out.save(os.path.join(outdir, 'awaken_fires_opal.png'))
    print(outdir)

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/scratch/icebuild/awaken')
