from PIL import Image
import numpy as np
R = '/home/claude/repo/assets/'
MMOW = Image.open(R + 'monomyth_ow/catalogue_ow16x32.png').convert('RGB')
CROW = Image.open(R + 'crown_reference/npcs_main_table.png').convert('RGB')
FAOW = Image.open('ow_fantasma.png').convert('RGB')
ODOW = Image.open('ow_odyssey.png').convert('RGB')
MMF = [Image.open(R + 'monomyth_reference/trainer_fronts/mm_fronts_part%d.png' % k).convert('RGB') for k in range(3)]
FAF = Image.open('tf_fantasma.png').convert('RGB')
def mm_ow(n):   # cell 202x110, first facing (south) ~ x 2..50, y 12..108
    x, y = (n % 10) * 202, (n // 10) * 110; return MMOW.crop((x, y + 10, x + 50, y + 108))
def cr_ow(n):   # 18 cols of 80 px, rows of 116 px
    x, y = (n % 18) * 80, (n // 18) * 116; return CROW.crop((x, y + 20, x + 64, y + 112))
def gen_ow(img, n):  # ow_scan sheet: 16 cols, W 104, H 110, +20 top; sprite at x+(32-w)*3//2, y+12
    x, y = (n % 16) * 104, (n // 16) * 110 + 20; return img.crop((x + 20, y + 12, x + 84, y + 108))
fa_ow = lambda n: gen_ow(FAOW, n); od_ow = lambda n: gen_ow(ODOW, n)
MMF_LABELS = [[n for n in range(0, 49) if n != 17], [n for n in range(50, 99) if n != 59], [n for n in range(99, 140) if n != 129]]
def mm_front(n):
    k = 0 if n <= 48 else (1 if n <= 98 else 2); i = MMF_LABELS[k].index(n)
    x, y = (i % 12) * 132, (i // 12) * 142; return MMF[k].crop((x + 2, y + 12, x + 130, y + 140))
def fa_front(n):
    x, y = (n % 12) * 134, (n // 12) * 142 + 20; return FAF.crop((x, y + 12, x + 128, y + 140))
