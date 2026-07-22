#!/usr/bin/env python3
"""Wire the 7 Chapter-1 cast overworld sprites into pokeemerald's object-event system.
Run from codebase/. Idempotent-ish: aborts a step if its anchor is missing."""
# (Name, file_stem, gfx_id, pal_tag)
CHARS = [('Osrid','osrid',276,0x1128),('Cadmus','cadmus',277,0x1129),('Eden','eden',278,0x112A),
         ('Glaive','glaive',279,0x112B),('Baradus','baradus',280,0x112C),('Kimaris','kimaris',281,0x112D),
         ('Ambrose','ambrose',282,0x112E)]
ok = True
def edit(path, anchor, block, before=False):
    global ok
    s = open(path).read()
    if anchor not in s:
        print(f'  MISS {path}: {anchor[:55]!r}'); ok = False; return
    open(path,'w').write(s.replace(anchor, (block+anchor) if before else (anchor+block), 1))
    print(f'  ok  {path}')

# 1) constants: GFX ids
blk = '\n// --- Dreamstone Ruination Chapter 1 cast (overworld) ---\n' + '\n'.join(
    f'#define OBJ_EVENT_GFX_{N.upper():<22} {i}' for N,n,i,p in CHARS)
edit('include/constants/event_objects.h', '#define OBJ_EVENT_GFX_PROF_TENEBRIS               275', blk)
# 2) bump the count 276 -> 283
edit('include/constants/event_objects.h',
     '#define NUM_OBJ_EVENT_GFX                          276',
     '')  # no-op insert to check anchor
s = open('include/constants/event_objects.h').read().replace(
     '#define NUM_OBJ_EVENT_GFX                          276',
     '#define NUM_OBJ_EVENT_GFX                          283', 1)
open('include/constants/event_objects.h','w').write(s); print('  ok  NUM_OBJ_EVENT_GFX -> 283')
# 3) palette tags
blk = '\n// --- Dreamstone Ruination Chapter 1 cast palettes ---\n' + '\n'.join(
    f'#define OBJ_EVENT_PAL_TAG_{N.upper():<21} 0x{p:04X}' for N,n,i,p in CHARS)
edit('include/constants/event_objects.h',
     '#define OBJ_EVENT_PAL_TAG_MUNUCU                  0x1124    //dynamic pal used to be 0x1124', blk)

# 4) INCBINs (pic + palette)
blk = '\n\n// --- Dreamstone Ruination Chapter 1 cast (overworld) ---\n' + '\n'.join(
    f'const u32 gObjectEventPic_{N}[] = INCBIN_U32("graphics/object_events/pics/people/{n}.4bpp");\n'
    f'const u16 gObjectEventPal_{N}[] = INCBIN_U16("graphics/object_events/pics/people/{n}.gbapal");'
    for N,n,i,p in CHARS)
edit('src/data/object_events/object_event_graphics.h',
     'const u32 gObjectEventPic_MunucuUnderwater[] = INCBIN_U32("graphics/object_events/pics/custom/munucu/underwater.4bpp");', blk)

# 5) pic tables (insert before munucu's)
blk = '// --- Dreamstone Ruination Chapter 1 cast (overworld) ---\n' + '\n'.join(
    f'static const struct SpriteFrameImage sPicTable_{N}[] = {{ overworld_ascending_frames(gObjectEventPic_{N}, 2, 4), }};'
    for N,n,i,p in CHARS) + '\n\n'
edit('src/data/object_events/object_event_pic_tables.h',
     'static const struct SpriteFrameImage sPicTable_MunucuNormal[] = {', blk, before=True)

# 6) graphics-info structs (insert before Woman1)
def ginfo(N,n,i,p):
    return (f'const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_{N} = {{\n'
            f'    .tileTag = TAG_NONE,\n    .paletteTag = OBJ_EVENT_PAL_TAG_{N.upper()},\n'
            f'    .reflectionPaletteTag = OBJ_EVENT_PAL_TAG_NONE,\n    .size = 256,\n    .width = 16,\n    .height = 32,\n'
            f'    .paletteSlot = PALSLOT_NPC_1,\n    .shadowSize = SHADOW_SIZE_M,\n    .inanimate = FALSE,\n'
            f'    .compressed = FALSE,\n    .tracks = TRACKS_FOOT,\n    .oam = &gObjectEventBaseOam_16x32,\n'
            f'    .subspriteTables = sOamTables_16x32,\n    .anims = sAnimTable_Standard,\n    .images = sPicTable_{N},\n'
            f'    .affineAnims = gDummySpriteAffineAnimTable,\n}};\n\n')
blk = '// --- Dreamstone Ruination Chapter 1 cast (overworld) ---\n' + ''.join(ginfo(*c) for c in CHARS)
edit('src/data/object_events/object_event_graphics_info.h',
     'const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_Woman1 = {', blk, before=True)

# 7) externs + pointer entries
blk = '\n// --- Dreamstone Ruination Chapter 1 cast ---\n' + '\n'.join(
    f'extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_{N};' for N,n,i,p in CHARS)
edit('src/data/object_events/object_event_graphics_info_pointers.h',
     'extern const struct ObjectEventGraphicsInfo gObjectEventGraphicsInfo_Woman1;', blk)
blk = '\n    // --- Dreamstone Ruination Chapter 1 cast ---\n' + '\n'.join(
    f'    [OBJ_EVENT_GFX_{N.upper()}] = &gObjectEventGraphicsInfo_{N},' for N,n,i,p in CHARS)
edit('src/data/object_events/object_event_graphics_info_pointers.h',
     '    [OBJ_EVENT_GFX_WOMAN_1] =                  &gObjectEventGraphicsInfo_Woman1,', blk)

# 8) palette table
blk = '\n    // --- Dreamstone Ruination Chapter 1 cast ---\n' + '\n'.join(
    f'    {{gObjectEventPal_{N}, OBJ_EVENT_PAL_TAG_{N.upper()}}},' for N,n,i,p in CHARS)
edit('src/event_object_movement.c',
     '    {gObjectEventPal_Munucu,                OBJ_EVENT_PAL_TAG_MUNUCU},', blk)

# 9) build rules (.4bpp; .gbapal uses the generic png rule)
blk = '\n\n# --- Dreamstone Ruination Chapter 1 cast (overworld) ---\n' + '\n'.join(
    f'$(OBJEVENTGFXDIR)/people/{n}.4bpp: %.4bpp: %.png\n\t$(GFX) $< $@ -mwidth 2 -mheight 4' for N,n,i,p in CHARS)
edit('spritesheet_rules.mk',
     '$(OBJEVENTGFXDIR)/custom/munucu/underwater.4bpp: %.4bpp: %.png\n\t$(GFX) $< $@ -mwidth 2 -mheight 4', blk)

print('DONE' if ok else 'SOME ANCHORS MISSED — review above')
