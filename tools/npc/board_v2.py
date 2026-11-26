import sys
sys.path.insert(0, '.')
from board_src import *
from PIL import Image, ImageDraw, ImageFont
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)
FS = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 11)
NB = '/tmp/noble/'
def user(n):
    im = Image.open(NB + n).convert('RGBA'); b = Image.new('RGBA', im.size, (110, 110, 130, 255)); b.alpha_composite(im)
    return b.convert('RGB')
def user_ow(v): return user('%s_ow.png' % v).crop((0, 0, 16, 32)).resize((48, 96), Image.NEAREST)
def user_front(v): return user('%s_front_fit.png' % v).resize((128, 128), Image.NEAREST)
O = {'MM': mm_ow, 'CR': cr_ow, 'FA': fa_ow, 'OD': od_ow}
FR = {'MM': mm_front, 'FA': fa_front}
# role: (overworld picks, front picks, note); picks as 'SRC n'; '*' = needs redress
ROLES = [
 ('Noble boy (your set)', ['USER black', 'USER brown', 'USER blonde'], ['USERF black', 'USERF brown', 'USERF blonde'], 'approved'),
 ('Commoner man', ['MM 3', 'MM 197', 'MM 31', 'CR 47'], ['MM 102', 'FA 211*'], 'modern clothes on most fronts: redress to tunic'),
 ('Commoner woman', ['MM 20', 'MM 43', 'MM 34', 'MM 124'], ['MM 117', 'FA 15*'], ''),
 ('Old man', ['MM 13', 'MM 23', 'MM 45', 'MM 122'], ['FA 138', 'MM 66'], ''),
 ('Old woman', ['MM 16', 'MM 21', 'MM 24'], ['MM 22'], 'only one old-woman front found'),
 ('Children', ['MM 29', 'MM 59', 'MM 134', 'MM 237'], ['MM 47', 'MM 48'], ''),
 ('Farmer', ['MM 70', 'MM 25', 'MM 125', 'MM 232'], ['FA 212', 'MM 46'], ''),
 ('Labourer / smith', ['MM 51', 'MM 179', 'MM 11'], ['MM 39', 'MM 89'], ''),
 ('Nobleman / lord', ['MM 112', 'MM 208', 'MM 215', 'MM 188'], ['FA 198', 'MM 92', 'MM 78*'], ''),
 ('Noblewoman', ['MM 114', 'MM 26', 'MM 55', 'MM 28'], ['FA 21', 'FA 52', 'MM 33'], ''),
 ('Merchant', ['MM 119', 'MM 110', 'MM 233', 'MM 35'], ['MM 116', 'MM 103'], ''),
 ('Innkeeper / barmaid / cook', ['MM 22', 'MM 58', 'FA 254', 'FA 255'], ['FA 179', 'MM 71*'], ''),
 ('Templar knight / squire', ['CR 70', 'MM 47', 'MM 73'], ['MM 3', 'MM 95'], 'our Templar sprite stays for the order'),
 ('Acolyte / priest / bishop', ['CR 45', 'MM 68', 'MM 188', 'MM 57', 'MM 116'], ['FA 9', 'FA 110', 'MM 92'], ''),
 ('Nun', ['CR 46', 'MM 19'], ['MM 85', 'MM 33'], ''),
 ('Guard / soldier', ['MM 238', 'MM 239', 'MM 162', 'CR 70'], ['MM 3*', 'MM 30*'], 'no medieval soldier front: redress'),
 ('Hunter / ranger', ['MM 201', 'MM 79', 'MM 30'], ['MM 28', 'MM 123', 'FA 192'], ''),
 ('Sailor / dockworker / fisherman', ['FA 85', 'FA 87', 'MM 199', 'MM 196'], ['FA 39', 'FA 94', 'MM 67', 'FA 129'], ''),
 ('Hiker / pilgrim', ['MM 209', 'MM 200', 'MM 141'], ['MM 96', 'FA 0'], ''),
 ('Bard', ['MM 71', 'MM 221'], ['MM 31', 'MM 68'], 'thin: a lute-player front would need a redress'),
 ('Witch', ['MM 87', 'CR 39', 'CR 41'], ['MM 41', 'FA 14', 'MM 22'], ''),
 ('Sword Cult acolyte', ['SC acolyte_ow', 'SC acolyte_kneel_S'], ['SCF acolyte_front_64'], 'black + icy sky blue; walker MonoMyth 217 (to review), kneeling 84/89/90'),
 ('Sword Cult Cardinal', ['SC cardinal_ow'], ['SCF cardinal_front_64'], 'your masked villain, recoloured'),
 ('Other cultists (Beads etc.)', ['MM 105', 'MM 156'], ['MM 82', 'FA 196', 'FA 201'], 'left from the survey: for the other cults or drop'),
]
SCD = '/home/claude/repo/tools/npc/sword_cult/out/'
def sc(n, front):
    im = Image.open(SCD + n + '.png').convert('RGBA')
    if not front:
        w = 32 if 'cardinal' in n else 16
        im = im.crop((0, 0, w, 32))
    b = Image.new('RGBA', im.size, (110, 110, 130, 255)); b.alpha_composite(im)
    b = b.convert('RGB')
    return b.resize((b.width * (2 if front else 3), b.height * (2 if front else 3)), Image.NEAREST)
def get(p, front):
    s, n = p.split(); red = n.endswith('*'); n = n.rstrip('*')
    if s in ('SC', 'SCF'): return sc(n, s == 'SCF'), {'acolyte_ow': 'walker', 'acolyte_kneel_S': 'kneeling', 'cardinal_ow': 'cardinal', 'acolyte_front_64': 'acolyte', 'cardinal_front_64': 'cardinal'}[n], False
    if s == 'USER': return user_ow(n), n, False
    if s == 'USERF': return user_front(n), n, False
    im = (FR if front else O)[s](int(n))
    return im, '%s %s%s' % (s, n, ' redress' if red else ''), red
rows = []
for name, ow, fr, note in ROLES:
    rows.append((name, [get(p, False) for p in ow], [get(p, True) for p in fr], note))
for r, (name, ow, fr, note) in enumerate(rows):
    rows[r] = ('%d. %s' % (r + 1, name),
               [(im, '%d%s  %s' % (r + 1, 'abcdefgh'[k], lab), red) for k, (im, lab, red) in enumerate(ow)],
               [(im, '%d%s  %s' % (r + 1, 'ABCDEFGH'[k], lab), red) for k, (im, lab, red) in enumerate(fr)], note)
W = 1500; RH = 168
S = Image.new('RGB', (W, 40 + RH * len(rows)), (26, 26, 32)); d = ImageDraw.Draw(S)
d.text((8, 10), 'Cast v2: overworld (left, lower-case) and fronts (right, upper-case). Refine by code, e.g. "3b out, 16A redress".   MM MonoMyth, CR Crown, FA Fantasma', font=F, fill=(255, 255, 255))
for r, (name, ow, fr, note) in enumerate(rows):
    y = 40 + r * RH
    d.rectangle((0, y, W, y + RH - 4), fill=(34, 34, 42) if r % 2 else (30, 30, 37))
    d.text((8, y + 6), name, font=F, fill=(255, 225, 120)); d.text((8, y + 26), note, font=FS, fill=(200, 200, 200))
    x = 8
    for im, lab, red in ow:
        im2 = im.resize((im.width * 96 // im.height, 96), Image.NEAREST) if im.height != 96 else im
        S.paste(im2, (x, y + 44)); d.text((x, y + 144), lab, font=FS, fill=(255, 140, 120) if red else (190, 190, 200)); x += max(im2.width, 108) + 10
    x = max(x, 640)
    for im, lab, red in fr:
        im2 = im.resize((128, 128)) if im.size != (128, 128) else im
        S.paste(im2, (x, y + 18)); d.text((x, y + 148), lab, font=FS, fill=(255, 140, 120) if red else (190, 190, 200)); x += 140
S.save('/home/claude/repo/assets/npc_survey/cast_candidates_v2.png'); print(S.size)
