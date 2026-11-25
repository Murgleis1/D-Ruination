from PIL import Image, ImageDraw, ImageFont
M='/home/claude/mono/all/'; L='/home/claude/lazarus/maps/'
try: F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13); FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)
except Exception: F = FB = ImageFont.load_default()
def crop(p, box=None, h=420):
    im = Image.open(p).convert('RGB')
    if box: im = im.crop(tuple(v * 16 for v in box))
    sc = h / im.height; return im.resize((int(im.width * sc), h), Image.LANCZOS if sc < 1 else Image.NEAREST)
P = [
 (crop('odyssey/3.43_t3_24x30.png'), "Odyssey 3.43 - SAME tileset as Hollow Hill", ["One ruined temple front closes the head of a", "cliff-walled hollow. A broken flagstone path runs", "straight at it; one dark stele in the path is the", "focus. Dead trees, a log, mushrooms at the edges."]),
 (crop(M + '868f44_60x60.png'), "MonoMyth 868f44 - temple precinct", ["Terraces step in to an inner court on one N-S axis;", "stairs sit on the axis. Grass and trees retake the", "court; rubble and broken columns at the margins,", "never on the path. The forest presses in."]),
 (crop(M + '868f4c_60x80.png', (0, 0, 60, 46)), "MonoMyth 868f4c - the approach", ["The climb is the drama: a long, wide stair up the", "axis between flanking terraces and ruined", "colonnades to a gate at the very top."]),
 (crop(L + 'fac8bc_s65.png'), "Lazarus fac8bc - hilltop shrine", ["Symmetric terraces, one central stair line, the", "altar and its pillars alone at the summit;", "statues set in pairs along the terraces."]),
 (crop('crown/3.25_t3_42x30.png', (0, 0, 30, 16)), "Crown 3.25 - tower ruin in webbed woods", ["A broken stone tower with a dark doorway at its foot,", "deep in woods; cobwebs hang in the trees around it", "(also a reference for the webbed-trees job)."]),
 (crop('odyssey/1.89_t5_50x52.png', (8, 0, 42, 40)), "Odyssey 1.89 - inside the haunted forest", ["A stepped stone mound with one stair; pale ruin", "slabs and little shrine gates scattered through", "the woods: ruins as a trail of hints, not one block."]),
]
W = 1440; cols = 3; cw = W // cols; rows = []
for i in range(0, len(P), cols): rows.append(P[i:i + cols])
H = sum(max(p[0].height for p in r) + 110 for r in rows) + 50
S = Image.new('RGB', (W, H), (22, 22, 28)); d = ImageDraw.Draw(S)
d.text((10, 10), "Hollow Hill's ruin - references studied as whole compositions", font=FB, fill=(255, 255, 255))
y = 40
for r in rows:
    rh = max(p[0].height for p in r)
    for j, (im, t, lines) in enumerate(r):
        x = j * cw + 8
        if im.width > cw - 16: im = im.resize((cw - 16, int(im.height * (cw - 16) / im.width)), Image.LANCZOS)
        d.text((x, y), t, font=FB, fill=(255, 220, 90)); S.paste(im, (x, y + 20))
        for k, ln in enumerate(lines): d.text((x, y + 24 + im.height + k * 16), ln, font=F, fill=(220, 220, 220))
    y += rh + 110
S.save('/home/claude/repo/assets/hollowhill_reference/ruin_refs_v1.png'); print(S.size)
