#!/usr/bin/env python3
"""Wire the 7 Chapter-1 cast front pics + trainer classes. Run from codebase/."""
# (Name, stem, pic_id, class_id, class_name<=12, money)
CHARS = [('Osrid','osrid',128,0x64,'Rainhawk',15),('Cadmus','cadmus',129,0x65,'Vizier',30),
         ('Eden','eden',130,0x66,'Rogue',10),('Glaive','glaive',131,0x67,'Dragonmaster',25),
         ('Baradus','baradus',132,0x68,'Sword Zealot',20),('Kimaris','kimaris',133,0x69,'Wraith Lord',25),
         ('Ambrose','ambrose',134,0x6A,'Archbishop',30)]
ok = True
def ins(path, anchor, block, before=False):
    global ok; s = open(path).read()
    if anchor not in s: print(f'  MISS {path}: {anchor[:55]!r}'); ok = False; return
    open(path,'w').write(s.replace(anchor,(block+anchor) if before else (anchor+block),1)); print(f'  ok  {path}')
def repl(path, old, new):
    global ok; s = open(path).read()
    if old not in s: print(f'  MISS(repl) {path}: {old[:45]!r}'); ok = False; return
    open(path,'w').write(s.replace(old,new,1)); print(f'  ok(repl) {path}')

# 1. TRAINER_PIC constants + bump count
blk = '// --- Dreamstone Ruination Chapter 1 cast ---\n' + '\n'.join(
    f'#define TRAINER_PIC_{N.upper():<21} {pic}' for N,n,pic,cl,cn,mo in CHARS) + '\n'
ins('include/constants/trainers.h', '#define TRAINER_PIC_COUNT                 128', blk, before=True)
repl('include/constants/trainers.h', '#define TRAINER_PIC_COUNT                 128',
     '#define TRAINER_PIC_COUNT                 135')
# 2. TRAINER_CLASS constants + bump count
blk = '\n// --- Dreamstone Ruination Chapter 1 cast ---\n' + '\n'.join(
    f'#define TRAINER_CLASS_{N.upper():<16} 0x{cl:02X}' for N,n,pic,cl,cn,mo in CHARS)
ins('include/constants/trainers.h', '#define TRAINER_CLASS_CONTENDER      0x63', blk)
repl('include/constants/trainers.h', '#define TRAINER_CLASS_COUNT          0x64',
     '#define TRAINER_CLASS_COUNT          0x6B')
# 3. front-pic + palette INCBINs
blk = '\n\n// --- Dreamstone Ruination Chapter 1 cast ---\n' + '\n'.join(
    f'const u32 gTrainerFrontPic_{N}[] = INCBIN_U32("graphics/trainers/front_pics/{n}.4bpp.lz");\n'
    f'const u32 gTrainerPalette_{N}[] = INCBIN_U32("graphics/trainers/front_pics/{n}.gbapal.lz");'
    for N,n,pic,cl,cn,mo in CHARS)
ins('src/data/graphics/trainers.h',
    'const u32 gTrainerPalette_Rue[] = INCBIN_U32("graphics/trainers/my_trainers/rue.gbapal.lz");', blk)
# 4. TRAINER_SPRITE registrations
blk = '\n    // --- Dreamstone Ruination Chapter 1 cast ---\n' + '\n'.join(
    f'    TRAINER_SPRITE(TRAINER_PIC_{N.upper()}, gTrainerFrontPic_{N}, gTrainerPalette_{N}),'
    for N,n,pic,cl,cn,mo in CHARS)
ins('src/data/graphics/trainers.h',
    '    TRAINER_SPRITE(TRAINER_PIC_CHAMPION_LYNCH, gTrainerFrontPic_ChampionLynch, gTrainerPalette_ChampionLynch),', blk)
# 5. class name + money entries
blk = '\n    // --- Dreamstone Ruination Chapter 1 cast ---\n' + '\n'.join(
    f'    [TRAINER_CLASS_{N.upper()}] = {{ _("{cn}"), {mo} }},' for N,n,pic,cl,cn,mo in CHARS)
ins('src/battle_main.c', '    [TRAINER_CLASS_CONTENDER] = {_("Contender")},', blk)

print('DONE' if ok else 'SOME MISSED — review')
