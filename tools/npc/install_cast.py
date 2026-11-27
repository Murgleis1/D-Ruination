"""Install the Chapter 1 cast into the game (user 2026-11-26: "proceed", on installing every finished class and walker
in one pass). Follows the male Templar's wiring (commit dd390e3d0), for each walker:
  graphics/object_events/pics/people/dr_<name>.png  (144x32, 9 frames, indexed, index 0 transparent)
  include/constants/event_objects.h                 OBJ_EVENT_GFX_DR_<NAME> (290..), NUM_OBJ_EVENT_GFX,
                                                    OBJ_EVENT_PAL_TAG_DR_<NAME> (0x1170..; 0x1134-0x114F skipped: 0x1140
                                                    is the knoll cloud's sprite tag)
  spritesheet_rules.mk                              the 2x4-tile rule
  src/data/object_events/object_event_graphics.h    gObjectEventPic_/Pal_Dr<Name>
  src/data/object_events/object_event_pic_tables.h  sPicTable_Dr<Name>
  src/data/object_events/object_event_graphics_info.h + _pointers.h
  src/event_object_movement.c                       sObjectEventSpritePalettes
and for each battle front:
  graphics/trainers/front_pics/dr_<name>.png        (64x64, indexed)
  include/constants/trainers.h                      TRAINER_PIC_DR_<NAME> (137..), TRAINER_PIC_COUNT
  src/data/graphics/trainers.h                      gTrainerFrontPic_/Palette_Dr<Name>, gTrainerSprites
and the trainer classes whose names the user has given (TRAINER_CLASS_<NAME>, 0x6D..; gTrainerClasses names <= 16 (data.h name[17], widened 2026-11-26)).
Every insertion sits between "// DR_CAST begin/end" markers, so a rerun replaces it.
Run: python3 install_cast.py"""
import os
import re
import shutil

from PIL import Image

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
CB = os.path.join(REPO, 'codebase')
T = os.path.join(REPO, 'tools', 'npc')

# (CONSTANT_SUFFIX, CamelName, file stem, source png)
WALKERS = [
    ('OLD_MAN', 'OldMan', 'old_man', 'walkers/out/old_man_ow.png'),
    ('OLD_WOMAN', 'OldWoman', 'old_woman', 'walkers/out/old_woman_ow.png'),
    ('FARMER', 'Farmer', 'farmer', 'walkers/out/farmer_ow.png'),
    ('WOODSMAN', 'Woodsman', 'woodsman', 'walkers/out/woodsman_ow.png'),
    ('MERCHANT', 'Merchant', 'merchant', 'walkers/out/merchant_ow.png'),
    ('TEMPLAR_PRIEST', 'TemplarPriest', 'templar_priest', 'walkers/out/templar_priest_ow.png'),
    ('ROYAL_OFFICER', 'RoyalOfficer', 'royal_officer', 'walkers/out/royal_officer_ow.png'),
    ('MINSTREL', 'Minstrel', 'minstrel', 'walkers/out/minstrel_ow.png'),
    ('WITCH', 'Witch', 'witch', 'walkers/out/witch_ow.png'),
    ('REVENANT', 'Revenant', 'revenant', 'walkers/out/revenant_ow.png'),
    ('ADVENTURER', 'Adventurer', 'adventurer', 'walkers/out/adventurer_ow.png'),
    ('MARINER', 'Mariner', 'mariner', 'walkers/out/mariner_ow.png'),
    ('CORSAIR', 'Corsair', 'corsair', 'walkers/out/corsair_ow.png'),
    ('FISHER', 'Fisher', 'fisher', 'walkers/out/fisher_ow.png'),
    ('GOON', 'Goon', 'goon', 'marauder/out/marauder_goon_m_ow.png'),
    ('BANDIT', 'Bandit', 'bandit', 'marauder/out/marauder_goon_f_ow.png'),
    ('MARAUDER', 'Marauder', 'marauder', 'marauder/out/marauder_chief_ow.png'),
    ('LOGAN', 'Logan', 'logan', 'townsfolk/out/logan_ow.png'),
    ('COMMONER_WOMAN_A', 'CommonerWomanA', 'commoner_woman_a', 'townsfolk/out/commoner_woman_a_ow.png'),
    ('COMMONER_WOMAN_B', 'CommonerWomanB', 'commoner_woman_b', 'townsfolk/out/commoner_woman_b_ow.png'),
    ('COMMONER_MAN_A', 'CommonerManA', 'commoner_man_a', 'townsfolk/out/commoner_man_a_ow.png'),
    ('COMMONER_MAN_B', 'CommonerManB', 'commoner_man_b', 'townsfolk/out/commoner_man_b_ow.png'),
    ('COMMONER_MAN_C', 'CommonerManC', 'commoner_man_c', 'townsfolk/out/commoner_man_c_ow.png'),
    ('COOK', 'Cook', 'cook', 'townsfolk/out/cook_ow.png'),
    ('BARKEEP', 'Barkeep', 'barkeep', 'townsfolk/out/barkeep_ow.png'),
    ('HEALER', 'Healer', 'healer', 'townsfolk/out/healer_ow.png'),
    ('KID_A', 'KidA', 'kid_a', 'townsfolk/out/kid_a_ow.png'),
    ('KID_B', 'KidB', 'kid_b', 'townsfolk/out/kid_b_ow.png'),
    ('KID_C', 'KidC', 'kid_c', 'townsfolk/out/kid_c_ow.png'),
    ('KID_E', 'KidE', 'kid_e', 'townsfolk/out/kid_e_ow.png'),
    ('STUDENT_A', 'StudentA', 'student_a', 'townsfolk/out/student_a_ow.png'),
    ('STUDENT_B', 'StudentB', 'student_b', 'townsfolk/out/student_b_ow.png'),
    ('STUDENT_C', 'StudentC', 'student_c', 'townsfolk/out/student_c_ow.png'),
]
FRONTS = [
    ('OLD_MAN', 'OldMan', 'old_man', 'picks/out/FA_138.png'),
    ('OLD_WOMAN', 'OldWoman', 'old_woman', 'picks/out/MM_22.png'),
    ('FARMER', 'Farmer', 'farmer', 'picks/out/FA_212.png'),
    ('WOODSMAN', 'Woodsman', 'woodsman', 'picks/out/MM_89.png'),
    ('MERCHANT', 'Merchant', 'merchant', 'picks/out/MM_116.png'),
    ('TEMPLAR_PRIEST', 'TemplarPriest', 'templar_priest', 'picks/out/FA_110.png'),
    ('ROYAL_OFFICER', 'RoyalOfficer', 'royal_officer', 'picks/out/officer.png'),
    ('MINSTREL', 'Minstrel', 'minstrel', 'picks/out/MM_68.png'),
    ('WITCH', 'Witch', 'witch', 'picks/out/FA_14.png'),
    ('REVENANT', 'Revenant', 'revenant', 'picks/out/FA_196.png'),
    ('ADVENTURER', 'Adventurer', 'adventurer', 'picks/out/FA_0.png'),
    ('MARINER', 'Mariner', 'mariner', 'picks/out/FA_94.png'),
    ('CORSAIR', 'Corsair', 'corsair', 'picks/out/MM_67.png'),
    ('FISHER', 'Fisher', 'fisher', 'picks/out/FA_129.png'),
    ('GOON', 'Goon', 'goon', 'marauder/out/goon.png'),
    ('BANDIT', 'Bandit', 'bandit', 'marauder/out/bandit.png'),
    ('MARAUDER', 'Marauder', 'marauder', 'marauder/out/marauder.png'),
    ('LOGAN', 'Logan', 'logan', 'logan/out/logan_front.png'),
]
# trainer classes the user has named (12 characters at most); money as the Templar's 20 / Brigand's 15 scale
CLASSES = [('REVENANT', 'Revenant', 12), ('ADVENTURER', 'Adventurer', 10), ('FISHER', 'Fisher', 8),
           ('CORSAIR', 'Corsair', 14), ('MARINER', 'Mariner', 10), ('WOODSMAN', 'Woodsman', 10),
           ('MERCHANT', 'Merchant', 24), ('GOON', 'Goon', 12), ('BANDIT', 'Bandit', 14),
           ('MARAUDER', 'Marauder', 20), ('SCHOLAR', 'Scholar', 18), ('WITCH', 'Witch', 14),
           ('MINSTREL', 'Minstrel', 10), ('ROYAL_OFFICER', 'Royal Officer', 16)]

GFX0, TAG0, PIC0, CLS0 = 290, 0x1170, 137, 0x6D
B, E = '// DR_CAST begin', '// DR_CAST end'
MKB, MKE = '# DR_CAST begin', '# DR_CAST end'


def put(path, anchor, block, after=True, mk=False, key=None):
    """Insert block (wrapped in markers named by key) after/before the first line containing anchor; replaces a
    previous block of the same key (a file can hold several)."""
    p = os.path.join(CB, path)
    s = open(p).read()
    b, e = (MKB, MKE) if mk else (B, E)
    key = key or anchor
    tag = ' [%s]' % re.sub(r'[^A-Za-z0-9_]', '', key)[:40]
    b, e = b + tag, e + tag
    s = re.sub(r'\n?' + re.escape(b) + r'.*?' + re.escape(e) + r'\n', '\n', s, flags=re.S)
    i = s.index(anchor)
    if after:
        j = s.index('\n', i) + 1
    else:
        j = s.rfind('\n', 0, i) + 1
    s = s[:j] + b + '\n' + block.rstrip('\n') + '\n' + e + '\n' + s[j:]
    open(p, 'w').write(s)


def sub(path, pattern, repl):
    p = os.path.join(CB, path)
    s = open(p).read()
    s2, n = re.subn(pattern, repl, s, count=1, flags=re.M)
    assert n == 1, (path, pattern)
    open(p, 'w').write(s2)


def check_png(path, size):
    im = Image.open(path)
    assert im.mode == 'P' and im.size == size, (path, im.mode, im.size)
    assert max(im.get_flattened_data()) < 16, path


def main():
    # graphics files
    for k, cam, stem, src in WALKERS:
        sp = os.path.join(T, src)
        check_png(sp, (144, 32))
        shutil.copy(sp, os.path.join(CB, 'graphics/object_events/pics/people/dr_%s.png' % stem))
    for k, cam, stem, src in FRONTS:
        sp = os.path.join(T, src)
        check_png(sp, (64, 64))
        shutil.copy(sp, os.path.join(CB, 'graphics/trainers/front_pics/dr_%s.png' % stem))
    n = len(WALKERS)
    # event_objects.h: ids, count, palette tags
    put('include/constants/event_objects.h', '#define OBJ_EVENT_GFX_TEMPLAR_MALE',
        '\n'.join('#define OBJ_EVENT_GFX_DR_%-28s %d' % (k, GFX0 + i) for i, (k, _, _, _) in enumerate(WALKERS)))
    sub('include/constants/event_objects.h', r'^#define NUM_OBJ_EVENT_GFX\s+\d+',
        '#define NUM_OBJ_EVENT_GFX                          %d' % (GFX0 + n))
    put('include/constants/event_objects.h', '#define OBJ_EVENT_PAL_TAG_TEMPLAR_MALE',
        '\n'.join('#define OBJ_EVENT_PAL_TAG_DR_%-24s 0x%04X' % (k, TAG0 + i) for i, (k, _, _, _) in enumerate(WALKERS)))
    # spritesheet rules
    put('spritesheet_rules.mk', '$(OBJEVENTGFXDIR)/people/templar_male.4bpp: %.4bpp: %.png',
        ''.join('$(OBJEVENTGFXDIR)/people/dr_%s.4bpp: %%.4bpp: %%.png\n\t$(GFX) $< $@ -mwidth 2 -mheight 4\n\n' % stem
                for _, _, stem, _ in WALKERS), mk=True)
    # pics and palettes
    put('src/data/object_events/object_event_graphics.h', 'gObjectEventPal_TemplarMale[]',
        ''.join('const u32 gObjectEventPic_Dr%s[] = INCBIN_U32("graphics/object_events/pics/people/dr_%s.4bpp");\n'
                'const u16 gObjectEventPal_Dr%s[] = INCBIN_U16("graphics/object_events/pics/people/dr_%s.gbapal");\n'
                % (cam, stem, cam, stem) for _, cam, stem, _ in WALKERS))
    put('src/data/object_events/object_event_pic_tables.h', 'sPicTable_TemplarMale[]',
        ''.join('static const struct SpriteFrameImage sPicTable_Dr%s[] = { overworld_ascending_frames(gObjectEventPic_Dr%s, 2, 4), };\n'
                % (cam, cam) for _, cam, _, _ in WALKERS))
    info = ''
    for k, cam, _, _ in WALKERS:
        info += ('const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_Dr%s = {\n'
                 '    .tileTag = TAG_NONE,\n    .paletteTag = OBJ_EVENT_PAL_TAG_DR_%s,\n'
                 '    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,\n    .size = 256,\n    .width = 16,\n'
                 '    .height = 32,\n    .paletteSlot = PALSLOT_NPC_1,\n    .shadowSize = SHADOW_SIZE_M,\n'
                 '    .inanimate = FALSE,\n    .compressed = FALSE,\n    .tracks = TRACKS_FOOT,\n'
                 '    .oam = &gObjectEventBaseOam_16x32,\n    .subspriteTables = sOamTables_16x32,\n'
                 '    .anims = sAnimTable_Standard,\n    .images = sPicTable_Dr%s,\n'
                 '    .affineAnims = gDummySpriteAffineAnimTable,\n};\n\n') % (cam, k, cam)
    p = os.path.join(CB, 'src/data/object_events/object_event_graphics_info.h')
    s = open(p).read()
    bi, ei = B + ' [info]', E + ' [info]'
    s = re.sub(r'\n?' + re.escape(bi) + r'.*?' + re.escape(ei) + r'\n\n?', '\n', s, flags=re.S)
    anchor = 'const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_DrShrine = {'
    i = s.index(anchor)
    s = s[:i] + bi + '\n' + info + ei + '\n\n' + s[i:]
    open(p, 'w').write(s)
    put('src/data/object_events/object_event_graphics_info_pointers.h',
        'extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_TemplarMale;',
        ''.join('extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_Dr%s;\n' % cam
                for _, cam, _, _ in WALKERS))
    put('src/data/object_events/object_event_graphics_info_pointers.h',
        '[OBJ_EVENT_GFX_TEMPLAR_MALE] = &gObjectEventGraphicsInfo_TemplarMale,',
        ''.join('    [OBJ_EVENT_GFX_DR_%s] = &gObjectEventGraphicsInfo_Dr%s,\n' % (k, cam) for k, cam, _, _ in WALKERS))
    put('src/event_object_movement.c', '{gObjectEventPal_TemplarMale, OBJ_EVENT_PAL_TAG_TEMPLAR_MALE},',
        ''.join('    {gObjectEventPal_Dr%s, OBJ_EVENT_PAL_TAG_DR_%s},\n' % (cam, k) for k, cam, _, _ in WALKERS))
    # trainer pics
    m = len(FRONTS)
    put('include/constants/trainers.h', '#define TRAINER_PIC_TEMPLAR_MALE',
        '\n'.join('#define TRAINER_PIC_DR_%-20s %d' % (k, PIC0 + i) for i, (k, _, _, _) in enumerate(FRONTS)))
    sub('include/constants/trainers.h', r'^#define TRAINER_PIC_COUNT\s+\d+',
        '#define TRAINER_PIC_COUNT                 %d' % (PIC0 + m))
    put('src/data/graphics/trainers.h', 'gTrainerPalette_TemplarMale[] = INCBIN_U32',
        ''.join('const u32 gTrainerFrontPic_Dr%s[] = INCBIN_U32("graphics/trainers/front_pics/dr_%s.4bpp.lz");\n'
                'const u32 gTrainerPalette_Dr%s[] = INCBIN_U32("graphics/trainers/front_pics/dr_%s.gbapal.lz");\n'
                % (cam, stem, cam, stem) for _, cam, stem, _ in FRONTS))
    put('src/data/graphics/trainers.h', 'TRAINER_SPRITE(TRAINER_PIC_TEMPLAR_MALE,',
        ''.join('    TRAINER_SPRITE(TRAINER_PIC_DR_%s, gTrainerFrontPic_Dr%s, gTrainerPalette_Dr%s),\n' % (k, cam, cam)
                for k, cam, _, _ in FRONTS))
    # trainer classes
    for k, name, _ in CLASSES:
        assert len(name) <= 16, name
    put('include/constants/trainers.h', '#define TRAINER_CLASS_BRIGAND',
        '\n'.join('#define TRAINER_CLASS_%-15s 0x%02X' % (k, CLS0 + i) for i, (k, _, _) in enumerate(CLASSES)))
    sub('include/constants/trainers.h', r'^#define TRAINER_CLASS_COUNT\s+0x[0-9A-Fa-f]+',
        '#define TRAINER_CLASS_COUNT          0x%02X' % (CLS0 + len(CLASSES)))
    put('src/battle_main.c', '[TRAINER_CLASS_BRIGAND] = {',
        ''.join('    [TRAINER_CLASS_%s] = { _("%s"), %d },\n' % (k, name, money) for k, name, money in CLASSES))
    print('walkers %d (gfx %d-%d, tags 0x%04X-0x%04X); fronts %d (pics %d-%d); classes %d (0x%02X-0x%02X)' % (
        n, GFX0, GFX0 + n - 1, TAG0, TAG0 + n - 1, m, PIC0, PIC0 + m - 1, len(CLASSES), CLS0, CLS0 + len(CLASSES) - 1))


if __name__ == '__main__':
    main()
