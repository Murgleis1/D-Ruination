from PIL import Image, ImageDraw, ImageFont
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13); FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
FS = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
HH = Image.open('hh_now.png').convert('RGB')
X0, Y0, N = 14, 14, 32
def hhcrop():
    return HH.crop((X0 * 16, Y0 * 16, (X0 + N) * 16, (Y0 + N) * 16)).copy()
def cell(d, x, y, w=1, h=1, fill=None, outline=None, s=16, ox=0, oy=0, width=2):
    d.rectangle((ox + x * s, oy + y * s, ox + (x + w) * s - 1, oy + (y + h) * s - 1), fill=fill, outline=outline, width=width)
RED = (190, 30, 40)
# ---------- A: on the knoll as it is
A = hhcrop(); dA = ImageDraw.Draw(A, 'RGBA')
k = lambda x, y: (x - X0, y - Y0)
cell(dA, *k(26, 27), 7, 6, fill=(255, 255, 255, 40), outline=(255, 220, 90))
cell(dA, *k(27, 27), 5, 2, fill=(235, 232, 220, 230), outline=(90, 90, 110))          # roofless shrine
cell(dA, *k(29, 29), 1, 1, fill=(30, 50, 110, 255))                                   # stele
for c in [(26, 30), (32, 30), (26, 32), (32, 32)]: cell(dA, *k(*c), fill=(150, 150, 160, 230))
dA.line([((27 - X0) * 16, (27 - Y0) * 16), ((26 - X0) * 16 + 8, (30 - Y0) * 16 + 8)], fill=RED, width=2)
dA.line([((32 - X0) * 16, (27 - Y0) * 16), ((32 - X0) * 16 + 8, (30 - Y0) * 16 + 8)], fill=RED, width=2)
# ---------- C: raise the knoll
C = hhcrop(); dC = ImageDraw.Draw(C, 'RGBA')
cell(dC, *k(23, 24), 13, 12, outline=(140, 140, 160), width=1)
cell(dC, *k(20, 21), 19, 17, outline=(255, 120, 80), width=3)
cell(dC, *k(23, 24), 13, 10, fill=(255, 255, 255, 50), outline=(255, 220, 90))
cell(dC, *k(25, 24), 9, 4, fill=(235, 232, 220, 220), outline=(90, 90, 110))
cell(dC, *k(29, 29), 1, 1, fill=(30, 50, 110, 255))
for c in [(25, 29), (33, 29), (25, 32), (33, 32)]: cell(dC, *k(*c), fill=(150, 150, 160, 230))
# ---------- B: the summit as its own map
S = 14; W, H = 40, 36
B = Image.new('RGB', (W * S, H * S), (46, 50, 62)); d = ImageDraw.Draw(B, 'RGBA')
FLOOR, FLAG, CLIFF, TEMPLE = (58, 92, 88), (196, 194, 180), (52, 44, 66), (232, 230, 220)
for y in range(H):
    for x in range(W):
        if 3 <= x <= 36 and 4 <= y <= 33 and not ((x in (3, 36)) and (y in (4, 33))): cell(d, x, y, fill=FLOOR, s=S)
for x in range(3, 37): cell(d, x, 33, fill=CLIFF, s=S); cell(d, x, 34, fill=CLIFF, s=S)
for y in range(4, 34): cell(d, 2, y, fill=CLIFF, s=S); cell(d, 37, y, fill=CLIFF, s=S)
for x in range(9, 31): cell(d, x, 13, fill=CLIFF, s=S)                                  # upper terrace edge
cell(d, 9, 4, 22, 9, fill=(70, 96, 92), s=S)                                             # upper terrace
cell(d, 13, 4, 14, 6, fill=TEMPLE, outline=(110, 110, 130), s=S)                          # the temple front
for x, y in [(23, 4), (24, 4), (25, 4), (26, 4), (25, 5), (26, 5), (26, 6)]: cell(d, x, y, fill=(70, 96, 92), s=S)  # its fallen corner
cell(d, 24, 7, 4, 3, fill=(150, 146, 140), s=S)                                           # rubble
cell(d, 19, 9, 2, 1, fill=(20, 18, 26), s=S)                                               # the doorway (webbed shut)
cell(d, 18, 13, 4, 2, fill=(170, 170, 160), s=S)                                           # the wide stair on the axis
for yy in range(15, 27):
    for xx in range(15, 25):
        if (xx - 19.5) ** 2 / 25 + (yy - 20.5) ** 2 / 30 <= 1 and (xx * 7 + yy * 3) % 11: cell(d, xx, yy, fill=FLAG, s=S)
for yy in range(26, 33):
    for xx in range(17, 23):
        if (xx * 5 + yy * 7) % 9: cell(d, xx, yy, fill=FLAG, s=S)
cell(d, 19, 20, 2, 2, fill=(30, 50, 110), s=S)                                             # the stele: the erasure site
for x, y in [(11, 17), (27, 17), (11, 23), (27, 23)]: cell(d, x, y, 2, 2, fill=(130, 128, 140), outline=(80, 80, 90), s=S)
for y in range(15, 31, 3):
    for x in (6, 33):
        if y in (21,): cell(d, x - 1, y, 3, 1, fill=(150, 150, 160), s=S)                 # fallen column
        else: cell(d, x, y, fill=(175, 175, 185), s=S)
cell(d, 19, 33, 2, 2, fill=(170, 170, 160), s=S)                                           # the way up from the tunnel
for x, y in [(4, 5), (5, 6), (34, 5), (35, 6), (4, 29), (5, 31), (34, 30), (35, 28)]: d.polygon([(x * S + 7, y * S), (x * S, y * S + 13), (x * S + 14, y * S + 13)], fill=(214, 210, 196))
for x, y in [(8, 11), (31, 11), (9, 29), (30, 27)]: d.ellipse((x * S + 2, y * S + 2, x * S + 12, y * S + 12), fill=(110, 70, 50))
for a, b in [((13, 4), (6, 15)), ((27, 4), (33, 15)), ((6, 15), (6, 24)), ((33, 15), (33, 24)), ((13, 7), (9, 12)), ((27, 7), (31, 12))]:
    d.line([(a[0] * S + 7, a[1] * S + 7), (b[0] * S + 7, b[1] * S + 7)], fill=RED, width=2)
d.line([(19 * S, 9 * S + 3), (21 * S, 10 * S - 2)], fill=RED, width=3); d.line([(21 * S, 9 * S + 3), (19 * S, 10 * S - 2)], fill=RED, width=3)
lab = [((14, 1), "fog / the woods far below"), ((14, 5), "THE TEMPLE (Odyssey 3.43's front, broken)"), ((14, 11), "door webbed shut: the guardian's lair"),
       ((22, 13), "wide stair on the axis"), ((22, 19), "the stele: where"), ((22, 20), "Phancero was erased"), ((7, 25), "4 empty plinths"),
       ((23, 29), "flagstone causeway"), ((22, 33), "up from the sealed door's tunnel"), ((2, 16), "broken colonnade")]
for (x, y), t in lab:
    tw = d.textlength(t, font=FS); d.rectangle((x * S - 2, y * S - 1, x * S + tw + 2, y * S + 12), fill=(0, 0, 0, 150)); d.text((x * S, y * S - 1), t, font=FS, fill=(255, 240, 160))
# the knoll's crown for B (on Hollow Hill, from tiles it already has)
KB = hhcrop(); dK = ImageDraw.Draw(KB, 'RGBA')
for c in [(27, 27), (31, 27), (27, 30), (31, 30)]: cell(dK, *k(*c), fill=(175, 175, 185, 230))
cell(dK, *k(28, 28), 3, 2, fill=(196, 194, 180, 200))
# ---------- sheet
P = [("A - On the knoll as it is", A, ["The ruin sits on Hollow Hill's own knoll top (7x6", "cells), seen from ring 2 below, out of reach.", "+ one map, seen from the start.", "- tiny: a roofless shrine, a stele, four stones.", "- the tileset is full (4 of 512 spare): webs or", "  shades must be trimmed to pay for it.", "- no room for the guardian or the Red fight."]),
     ("C - Raise the knoll", C, ["Grow the knoll (orange) so its top is ~13x10,", "and rebuild ring 2 around it.", "+ a real ruin, on the hill itself.", "- ring 2's walk shrinks to 2-3 cells; the approved,", "  built layout and its walks are redone.", "- same tileset squeeze as A, worse."]),
     ("B - The summit as its own map (recommended)", B, ["The sealed door at the knoll's foot opens (later) on", "a tunnel climbing inside the knoll to a summit map", "(~40x36, its own tileset). One axis, south to north:", "causeway -> court with the stele and 4 empty plinths", "-> wide stair -> the broken temple front, its door", "webbed shut (the guardian). Room for the Red fight.", "Hollow Hill's knoll keeps a hint (inset, below)."])]
SW = 1660; Sh = Image.new('RGB', (SW, 930), (22, 22, 28)); dd = ImageDraw.Draw(Sh)
dd.text((10, 8), "Hollow Hill's ruin - where it goes (block plans, no art yet)", font=FB, fill=(255, 255, 255))
x = 10
for i, (t, im, lines) in enumerate(P):
    dd.text((x, 36), t, font=FB, fill=(255, 220, 90)); Sh.paste(im, (x, 60))
    for j, ln in enumerate(lines): dd.text((x, 70 + im.height + j * 17), ln, font=F, fill=(225, 225, 225))
    x += im.width + 24
kb = KB.crop(((24 - X0) * 16, (24 - Y0) * 16, (36 - X0) * 16, (37 - Y0) * 16))
bx = 10 + 512 + 24 + 512 + 24
Sh.paste(kb, (bx + 230, 712))
for j, t in enumerate(["B's hint on Hollow Hill:", "broken column stumps and", "slabs on the knoll top, from", "tiles it already has (to check)."]):
    dd.text((bx, 716 + j * 17), t, font=F, fill=(255, 220, 90) if j == 0 else (225, 225, 225))
Sh.save('/home/claude/repo/assets/hollowhill_reference/ruin_plans_v1.png'); print(Sh.size)
