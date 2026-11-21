#include "global.h"
#include "battle.h"
#include "title_screen.h"
#include "sprite.h"
#include "gba/m4a_internal.h"
#include "clear_save_data_menu.h"
#include "decompress.h"
#include "event_data.h"
#include "intro.h"
#include "m4a.h"
#include "main.h"
#include "main_menu.h"
#include "palette.h"
#include "reset_rtc_screen.h"
#include "berry_fix_program.h"
#include "sound.h"
#include "sprite.h"
#include "task.h"
#include "scanline_effect.h"
#include "gpu_regs.h"
#include "trig.h"
#include "graphics.h"
#include "constants/rgb.h"
#include "constants/songs.h"

enum {
    TAG_VERSION = 1000,
    TAG_PRESS_START_COPYRIGHT,
    TAG_LOGO_SHINE,
};

#define VERSION_BANNER_RIGHT_TILEOFFSET 64
#define VERSION_BANNER_LEFT_X 98
#define VERSION_BANNER_RIGHT_X 162
#define VERSION_BANNER_Y 2
#define VERSION_BANNER_Y_GOAL 72
#define START_BANNER_X 128

#define CLEAR_SAVE_BUTTON_COMBO (B_BUTTON | SELECT_BUTTON | DPAD_UP)
#define RESET_RTC_BUTTON_COMBO (B_BUTTON | SELECT_BUTTON | DPAD_LEFT)
#define BERRY_UPDATE_BUTTON_COMBO (B_BUTTON | SELECT_BUTTON)
#define A_B_START_SELECT (A_BUTTON | B_BUTTON | START_BUTTON | SELECT_BUTTON)

static void MainCB2(void);
static void Task_TitleScreenPhase1(u8);
static void Task_TitleScreenPhase2(u8);
static void Task_TitleScreenPhase3(u8);
static void CB2_GoToMainMenu(void);
static void RestoreSoundChannels(void);
static void CB2_GoToClearSaveDataScreen(void);
static void CB2_GoToResetRtcScreen(void);
static void CB2_GoToBerryFixScreen(void);
static void CB2_GoToCopyrightScreen(void);
static void UpdateLegendaryMarkingColor(u8);
static void Task_TitleAnim(u8);
static void ResetTitleAnimGpu(void);

static void SpriteCB_VersionBannerLeft(struct Sprite *sprite);
static void SpriteCB_VersionBannerRight(struct Sprite *sprite);
static void SpriteCB_PressStartCopyrightBanner(struct Sprite *sprite);
static void SpriteCB_PokemonLogoShine(struct Sprite *sprite);

#define TITLE_SOUND_CHANNELS   10  // sampled voices while the title theme plays (the engine allows up to 12)
#define DEFAULT_SOUND_CHANNELS 10  // the game's default (m4aSoundInit in m4a.c; raised from 5 for the ported songs)

// const rom data
static const u16 sUnusedUnknownPal[] = INCBIN_U16("graphics/title_screen/unused.gbapal");

static const u32 sTitleScreenRayquazaGfx[] = INCBIN_U32("graphics/title_screen/dsmyst.4bpp.lz");
static const u32 sTitleScreenRayquazaTilemap[] = INCBIN_U32("graphics/title_screen/dsmyst.bin.lz");
static const u32 sTitleScreenLogoShineGfx[] = INCBIN_U32("graphics/title_screen/logo_shine.4bpp.lz");
static const u32 sTitleScreenCloudsGfx[] = INCBIN_U32("graphics/title_screen/clouds.4bpp.lz");

// Dreamstone Ruination: animated title. Four 8bpp layers share one tile set at char base 0
// (built by tools/art/title_anim/export_rom.py from the approved preview):
//   BG3  Chien-Pao's tail (front); its 6x6-tile window is rewritten with one of 5 poses
//   BG0  the static scene + logo; sky pixels transparent; logo fill = palette bands for the glint
//   BG1/BG2  512x48 sky strip, scrolled one pixel apart and alpha-blended -> smooth sub-pixel drift
static const u32 sDrTitleAnimTiles[] = INCBIN_U32("graphics/title_screen/dr_title_anim_tiles.8bpp.lz");
static const u16 sDrTitleAnimPal[] = INCBIN_U16("graphics/title_screen/dr_title_anim_tiles.gbapal");
static const u32 sDrTitleAnimFgMap[] = INCBIN_U32("graphics/title_screen/dr_title_anim_fg.bin.lz");
static const u32 sDrTitleAnimSkyMap[] = INCBIN_U32("graphics/title_screen/dr_title_anim_sky.bin.lz");
static const u32 sDrTitleAnimTailMap[] = INCBIN_U32("graphics/title_screen/dr_title_anim_tail.bin.lz");
static const u32 sDrTitleTailPoses[] = INCBIN_U32("graphics/title_screen/dr_title_tail_poses.8bpp");

#include "data/title_screen_anim.h"

#define TITLE_FG_SCREENBASE    28
#define TITLE_TAIL_SCREENBASE  29
#define TITLE_SKY_SCREENBASE   30   // 512x256 map: screenblocks 30-31
#define TITLE_SKY_FRAMES_PER_PX 8   // cloud drift speed (60 fps -> 7.5 px/s)
#define TITLE_SKY_WIDTH        512
#define TITLE_GLINT_PERIOD     480  // a glint sweep every 8 s
#define TITLE_GLINT_SPEED      2    // px per frame along the diagonal

// Values the animation task computes each frame; VBlankCB writes them to the hardware.
static EWRAM_DATA u32 sTitleAnimFrame = 0;
static EWRAM_DATA u16 sTitleSkyHofs = 0;
static EWRAM_DATA u16 sTitleSkyBlend = 0;
static EWRAM_DATA u8 sTitleTailSeqIdx = 0;
static EWRAM_DATA u16 sTitleTailSeqTimer = 0;
static EWRAM_DATA s8 sTitleTailPosePending = 0;    // pose to copy into VRAM at the next VBlank (-1 = none; set at init)
static EWRAM_DATA bool8 sTitleGlintActive = FALSE;



// Used to blend "Emerald Version" as it passes over over the Pokémon banner.
// Also used by the intro to blend the Game Freak name/logo in and out as they appear and disappear
const u16 gTitleScreenAlphaBlend[64] =
{
    BLDALPHA_BLEND(16, 0),
    BLDALPHA_BLEND(16, 1),
    BLDALPHA_BLEND(16, 2),
    BLDALPHA_BLEND(16, 3),
    BLDALPHA_BLEND(16, 4),
    BLDALPHA_BLEND(16, 5),
    BLDALPHA_BLEND(16, 6),
    BLDALPHA_BLEND(16, 7),
    BLDALPHA_BLEND(16, 8),
    BLDALPHA_BLEND(16, 9),
    BLDALPHA_BLEND(16, 10),
    BLDALPHA_BLEND(16, 11),
    BLDALPHA_BLEND(16, 12),
    BLDALPHA_BLEND(16, 13),
    BLDALPHA_BLEND(16, 14),
    BLDALPHA_BLEND(16, 15),
    BLDALPHA_BLEND(15, 16),
    BLDALPHA_BLEND(14, 16),
    BLDALPHA_BLEND(13, 16),
    BLDALPHA_BLEND(12, 16),
    BLDALPHA_BLEND(11, 16),
    BLDALPHA_BLEND(10, 16),
    BLDALPHA_BLEND(9, 16),
    BLDALPHA_BLEND(8, 16),
    BLDALPHA_BLEND(7, 16),
    BLDALPHA_BLEND(6, 16),
    BLDALPHA_BLEND(5, 16),
    BLDALPHA_BLEND(4, 16),
    BLDALPHA_BLEND(3, 16),
    BLDALPHA_BLEND(2, 16),
    BLDALPHA_BLEND(1, 16),
    BLDALPHA_BLEND(0, 16),
    [32 ... 63] = BLDALPHA_BLEND(0, 16)
};

static const struct OamData sVersionBannerLeftOamData =
{
    .y = DISPLAY_HEIGHT,
    .affineMode = ST_OAM_AFFINE_OFF,
    .objMode = ST_OAM_OBJ_NORMAL,
    .mosaic = FALSE,
    .bpp = ST_OAM_8BPP,
    .shape = SPRITE_SHAPE(64x32),
    .x = 0,
    .matrixNum = 0,
    .size = SPRITE_SIZE(64x32),
    .tileNum = 0,
    .priority = 0,
    .paletteNum = 0,
    .affineParam = 0,
};

static const struct OamData sVersionBannerRightOamData =
{
    .y = DISPLAY_HEIGHT,
    .affineMode = ST_OAM_AFFINE_OFF,
    .objMode = ST_OAM_OBJ_NORMAL,
    .mosaic = FALSE,
    .bpp = ST_OAM_8BPP,
    .shape = SPRITE_SHAPE(64x32),
    .x = 0,
    .matrixNum = 0,
    .size = SPRITE_SIZE(64x32),
    .tileNum = 0,
    .priority = 0,
    .paletteNum = 0,
    .affineParam = 0,
};

static const union AnimCmd sVersionBannerLeftAnimSequence[] =
{
    ANIMCMD_FRAME(0, 30),
    ANIMCMD_END,
};

static const union AnimCmd sVersionBannerRightAnimSequence[] =
{
    ANIMCMD_FRAME(VERSION_BANNER_RIGHT_TILEOFFSET, 30),
    ANIMCMD_END,
};

static const union AnimCmd *const sVersionBannerLeftAnimTable[] =
{
    sVersionBannerLeftAnimSequence,
};

static const union AnimCmd *const sVersionBannerRightAnimTable[] =
{
    sVersionBannerRightAnimSequence,
};

static const struct SpriteTemplate sVersionBannerLeftSpriteTemplate =
{
    .tileTag = TAG_VERSION,
    .paletteTag = TAG_VERSION,
    .oam = &sVersionBannerLeftOamData,
    .anims = sVersionBannerLeftAnimTable,
    .images = NULL,
    .affineAnims = gDummySpriteAffineAnimTable,
    .callback = SpriteCB_VersionBannerLeft,
};

static const struct SpriteTemplate sVersionBannerRightSpriteTemplate =
{
    .tileTag = TAG_VERSION,
    .paletteTag = TAG_VERSION,
    .oam = &sVersionBannerRightOamData,
    .anims = sVersionBannerRightAnimTable,
    .images = NULL,
    .affineAnims = gDummySpriteAffineAnimTable,
    .callback = SpriteCB_VersionBannerRight,
};

static const struct CompressedSpriteSheet sSpriteSheet_EmeraldVersion[] =
{
    {
        .data = gTitleScreenEmeraldVersionGfx,
        .size = 0x1000,
        .tag = TAG_VERSION
    },
    {},
};

static const struct OamData sOamData_CopyrightBanner =
{
    .y = DISPLAY_HEIGHT,
    .affineMode = ST_OAM_AFFINE_OFF,
    .objMode = ST_OAM_OBJ_NORMAL,
    .mosaic = FALSE,
    .bpp = ST_OAM_4BPP,
    .shape = SPRITE_SHAPE(32x8),
    .x = 0,
    .matrixNum = 0,
    .size = SPRITE_SIZE(32x8),
    .tileNum = 0,
    .priority = 0,
    .paletteNum = 0,
    .affineParam = 0,
};

static const union AnimCmd sAnim_PressStart_0[] =
{
    ANIMCMD_FRAME(1, 4),
    ANIMCMD_END,
};
static const union AnimCmd sAnim_PressStart_1[] =
{
    ANIMCMD_FRAME(5, 4),
    ANIMCMD_END,
};
static const union AnimCmd sAnim_PressStart_2[] =
{
    ANIMCMD_FRAME(9, 4),
    ANIMCMD_END,
};
static const union AnimCmd sAnim_PressStart_3[] =
{
    ANIMCMD_FRAME(13, 4),
    ANIMCMD_END,
};
static const union AnimCmd sAnim_PressStart_4[] =
{
    ANIMCMD_FRAME(17, 4),
    ANIMCMD_END,
};
static const union AnimCmd sAnim_Copyright_0[] =
{
    ANIMCMD_FRAME(21, 4),
    ANIMCMD_END,
};
static const union AnimCmd sAnim_Copyright_1[] =
{
    ANIMCMD_FRAME(25, 4),
    ANIMCMD_END,
};
static const union AnimCmd sAnim_Copyright_2[] =
{
    ANIMCMD_FRAME(29, 4),
    ANIMCMD_END,
};
static const union AnimCmd sAnim_Copyright_3[] =
{
    ANIMCMD_FRAME(33, 4),
    ANIMCMD_END,
};
static const union AnimCmd sAnim_Copyright_4[] =
{
    ANIMCMD_FRAME(37, 4),
    ANIMCMD_END,
};

// The "Press Start" and copyright graphics are each 5 32x8 segments long
#define NUM_PRESS_START_FRAMES 5
#define NUM_COPYRIGHT_FRAMES 5

static const union AnimCmd *const sStartCopyrightBannerAnimTable[NUM_PRESS_START_FRAMES + NUM_COPYRIGHT_FRAMES] =
{
    sAnim_PressStart_0,
    sAnim_PressStart_1,
    sAnim_PressStart_2,
    sAnim_PressStart_3,
    sAnim_PressStart_4,
    [NUM_PRESS_START_FRAMES] =
    sAnim_Copyright_0,
    sAnim_Copyright_1,
    sAnim_Copyright_2,
    sAnim_Copyright_3,
    sAnim_Copyright_4,
};

static const struct SpriteTemplate sStartCopyrightBannerSpriteTemplate =
{
    .tileTag = TAG_PRESS_START_COPYRIGHT,
    .paletteTag = TAG_PRESS_START_COPYRIGHT,
    .oam = &sOamData_CopyrightBanner,
    .anims = sStartCopyrightBannerAnimTable,
    .images = NULL,
    .affineAnims = gDummySpriteAffineAnimTable,
    .callback = SpriteCB_PressStartCopyrightBanner,
};

static const struct CompressedSpriteSheet sSpriteSheet_PressStart[] =
{
    {
        .data = gTitleScreenPressStartGfx,
        .size = 0x520,
        .tag = TAG_PRESS_START_COPYRIGHT
    },
    {},
};

static const struct SpritePalette sSpritePalette_PressStart[] =
{
    {
        .data = gTitleScreenPressStartPal,
        .tag = TAG_PRESS_START_COPYRIGHT
    },
    {},
};

static const struct OamData sPokemonLogoShineOamData =
{
    .y = DISPLAY_HEIGHT,
    .affineMode = ST_OAM_AFFINE_OFF,
    .objMode = ST_OAM_OBJ_NORMAL,
    .mosaic = FALSE,
    .bpp = ST_OAM_4BPP,
    .shape = SPRITE_SHAPE(64x64),
    .x = 0,
    .matrixNum = 0,
    .size = SPRITE_SIZE(64x64),
    .tileNum = 0,
    .priority = 0,
    .paletteNum = 0,
    .affineParam = 0,
};

static const union AnimCmd sPokemonLogoShineAnimSequence[] =
{
    ANIMCMD_FRAME(0, 4),
    ANIMCMD_END,
};

static const union AnimCmd *const sPokemonLogoShineAnimTable[] =
{
    sPokemonLogoShineAnimSequence,
};

static const struct SpriteTemplate sPokemonLogoShineSpriteTemplate =
{
    .tileTag = TAG_LOGO_SHINE,
    .paletteTag = TAG_PRESS_START_COPYRIGHT,
    .oam = &sPokemonLogoShineOamData,
    .anims = sPokemonLogoShineAnimTable,
    .images = NULL,
    .affineAnims = gDummySpriteAffineAnimTable,
    .callback = SpriteCB_PokemonLogoShine,
};

static const struct CompressedSpriteSheet sPokemonLogoShineSpriteSheet[] =
{
    {
        .data = sTitleScreenLogoShineGfx,
        .size = 0x800,
        .tag = TAG_LOGO_SHINE
    },
    {},
};

// Task data for the main title screen tasks (Task_TitleScreenPhase#)
#define tCounter    data[0]
#define tSkipToNext data[1]
#define tPointless  data[2] // Incremented but never used to do anything.
#define tBg2Y       data[3]
#define tBg1Y       data[4]

// Sprite data for sVersionBannerLeftSpriteTemplate / sVersionBannerRightSpriteTemplate
#define sAlphaBlendIdx data[0]
#define sParentTaskId  data[1]

static void SpriteCB_VersionBannerLeft(struct Sprite *sprite)
{
    if (gTasks[sprite->sParentTaskId].tSkipToNext)
    {
        sprite->oam.objMode = ST_OAM_OBJ_NORMAL;
        sprite->y = VERSION_BANNER_Y_GOAL;
    }
    else
    {
        if (sprite->y != VERSION_BANNER_Y_GOAL)
            sprite->y++;
        if (sprite->sAlphaBlendIdx != 0)
            sprite->sAlphaBlendIdx--;
        SetGpuReg(REG_OFFSET_BLDALPHA, gTitleScreenAlphaBlend[sprite->sAlphaBlendIdx]);
    }
}

static void SpriteCB_VersionBannerRight(struct Sprite *sprite)
{
    if (gTasks[sprite->sParentTaskId].tSkipToNext)
    {
        sprite->oam.objMode = ST_OAM_OBJ_NORMAL;
        sprite->y = VERSION_BANNER_Y_GOAL;
    }
    else
    {
        if (sprite->y != VERSION_BANNER_Y_GOAL)
            sprite->y++;
    }
}

// Sprite data for SpriteCB_PressStartCopyrightBanner
#define sAnimate data[0]
#define sTimer   data[1]

static void SpriteCB_PressStartCopyrightBanner(struct Sprite *sprite)
{
    if (sprite->sAnimate == TRUE)
    {
        // Dreamstone Ruination: calm blink -- shown 40 frames, hidden 24
        sprite->invisible = (sprite->sTimer >= 40);
        sprite->sTimer = (sprite->sTimer + 1) & 63;
    }
    else
    {
        sprite->invisible = FALSE;
    }
}

static void CreatePressStartBanner(s16 x, s16 y)
{
    u8 i;
    u8 spriteId;

    x -= 64;
    for (i = 0; i < NUM_PRESS_START_FRAMES; i++, x += 32)
    {
        spriteId = CreateSprite(&sStartCopyrightBannerSpriteTemplate, x, y, 0);
        StartSpriteAnim(&gSprites[spriteId], i);
        gSprites[spriteId].sAnimate = TRUE;
    }
}

static void CreateCopyrightBanner(s16 x, s16 y)
{
    u8 i;
    u8 spriteId;

    x -= 64;
    for (i = 0; i < NUM_COPYRIGHT_FRAMES; i++, x += 32)
    {
        spriteId = CreateSprite(&sStartCopyrightBannerSpriteTemplate, x, y, 0);
        StartSpriteAnim(&gSprites[spriteId], i + NUM_PRESS_START_FRAMES);
    }
}

#undef sAnimate
#undef sTimer

// Defines for SpriteCB_PokemonLogoShine
enum {
    SHINE_MODE_SINGLE_NO_BG_COLOR,
    SHINE_MODE_DOUBLE,
    SHINE_MODE_SINGLE,
};

#define SHINE_SPEED  4

#define sMode     data[0]
#define sBgColor  data[1]

static void SpriteCB_PokemonLogoShine(struct Sprite *sprite)
{
    if (sprite->x < DISPLAY_WIDTH + 32)
    {
        // In any mode except SHINE_MODE_SINGLE_NO_BG_COLOR the background
        // color will change, in addition to the shine sprite moving.
        if (sprite->sMode != SHINE_MODE_SINGLE_NO_BG_COLOR)
        {
            u16 backgroundColor;

            if (sprite->x < DISPLAY_WIDTH / 2)
            {
                // Brighten background color
                if (sprite->sBgColor < 31)
                    sprite->sBgColor++;
                if (sprite->sBgColor < 31)
                    sprite->sBgColor++;
            }
            else
            {
                // Darken background color
                if (sprite->sBgColor != 0)
                    sprite->sBgColor--;
                if (sprite->sBgColor != 0)
                    sprite->sBgColor--;
            }

            backgroundColor = _RGB(sprite->sBgColor, sprite->sBgColor, sprite->sBgColor);

            // Flash the background green for 4 frames of movement.
            // Otherwise use the updating color.
            // if (sprite->x == DISPLAY_WIDTH / 2 + (3 * SHINE_SPEED)
            //  || sprite->x == DISPLAY_WIDTH / 2 + (4 * SHINE_SPEED)
            //  || sprite->x == DISPLAY_WIDTH / 2 + (5 * SHINE_SPEED)
            //  || sprite->x == DISPLAY_WIDTH / 2 + (6 * SHINE_SPEED))
            //     gPlttBufferFaded[0] = RGB(24, 31, 12);
            // else
                gPlttBufferFaded[0] = backgroundColor;
        }

        sprite->x += SHINE_SPEED;
    }
    else
    {
        // Sprite has moved fully offscreen
        gPlttBufferFaded[0] = RGB_BLACK;
        DestroySprite(sprite);
    }
}

static void SpriteCB_PokemonLogoShine_Fast(struct Sprite *sprite)
{
    if (sprite->x < DISPLAY_WIDTH + 32)
        sprite->x += SHINE_SPEED * 2;
    else
        DestroySprite(sprite);
}

static void StartPokemonLogoShine(u8 mode)
{
    u8 spriteId;

    switch (mode)
    {
    case SHINE_MODE_SINGLE_NO_BG_COLOR:
    case SHINE_MODE_SINGLE:
        // Create one regular shine sprite.
        // If mode is SHINE_MODE_SINGLE it will also change the background color.
        spriteId = CreateSprite(&sPokemonLogoShineSpriteTemplate, 0, 68, 0);
        gSprites[spriteId].oam.objMode = ST_OAM_OBJ_WINDOW;
        gSprites[spriteId].sMode = mode;
        break;
    case SHINE_MODE_DOUBLE:
        // Create an invisible sprite with mode set to update the background color
        spriteId = CreateSprite(&sPokemonLogoShineSpriteTemplate, 0, 68, 0);
        gSprites[spriteId].oam.objMode = ST_OAM_OBJ_WINDOW;
        gSprites[spriteId].sMode = mode;
        gSprites[spriteId].invisible = TRUE;

        // Create two faster shine sprites
        spriteId = CreateSprite(&sPokemonLogoShineSpriteTemplate, 0, 68, 0);
        gSprites[spriteId].callback = SpriteCB_PokemonLogoShine_Fast;
        gSprites[spriteId].oam.objMode = ST_OAM_OBJ_WINDOW;

        spriteId = CreateSprite(&sPokemonLogoShineSpriteTemplate, -80, 68, 0);
        gSprites[spriteId].callback = SpriteCB_PokemonLogoShine_Fast;
        gSprites[spriteId].oam.objMode = ST_OAM_OBJ_WINDOW;
        break;
    }
}

#undef sMode
#undef sBgColor

static void VBlankCB(void)
{
    ScanlineEffect_InitHBlankDmaTransfer();
    LoadOam();
    ProcessSpriteCopyRequests();
    TransferPlttBuffer();
    // Sky: BG1 at x, BG2 one pixel further, blended by how far we are toward the next pixel
    SetGpuReg(REG_OFFSET_BG1HOFS, sTitleSkyHofs);
    SetGpuReg(REG_OFFSET_BG2HOFS, (sTitleSkyHofs + 1) & (TITLE_SKY_WIDTH - 1));
    SetGpuReg(REG_OFFSET_BLDALPHA, sTitleSkyBlend);
    // Tail: swap in a new pose (36 8bpp tiles) when the idle sequence moves on
    if (sTitleTailPosePending >= 0)
    {
        DmaCopy16(3, (const u8 *)sDrTitleTailPoses + sTitleTailPosePending * TITLE_TAIL_TILES * TILE_SIZE_8BPP,
                  (void *)(BG_CHAR_ADDR(0) + TITLE_TAIL_TILE_BASE * TILE_SIZE_8BPP), TITLE_TAIL_TILES * TILE_SIZE_8BPP);
        sTitleTailPosePending = -1;
    }
}

void CB2_InitTitleScreen(void)
{
    switch (gMain.state)
    {
    default:
    case 0:
        SetVBlankCallback(NULL);
        SetGpuReg(REG_OFFSET_BLDCNT, 0);
        SetGpuReg(REG_OFFSET_BLDALPHA, 0);
        SetGpuReg(REG_OFFSET_BLDY, 0);
        *((u16 *)PLTT) = RGB_WHITE;
        SetGpuReg(REG_OFFSET_DISPCNT, 0);
        SetGpuReg(REG_OFFSET_BG2CNT, 0);
        SetGpuReg(REG_OFFSET_BG1CNT, 0);
        SetGpuReg(REG_OFFSET_BG0CNT, 0);
        SetGpuReg(REG_OFFSET_BG2HOFS, 0);
        SetGpuReg(REG_OFFSET_BG2VOFS, 0);
        SetGpuReg(REG_OFFSET_BG1HOFS, 0);
        SetGpuReg(REG_OFFSET_BG1VOFS, 0);
        SetGpuReg(REG_OFFSET_BG0HOFS, 0);
        SetGpuReg(REG_OFFSET_BG0VOFS, 0);
        DmaFill16(3, 0, (void *)VRAM, VRAM_SIZE);
        DmaFill32(3, 0, (void *)OAM, OAM_SIZE);
        DmaFill16(3, 0, (void *)(PLTT + 2), PLTT_SIZE - 2);
        ResetPaletteFade();
        gMain.state = 1;
        break;
    case 1:
        // Dreamstone Ruination: shared 8bpp tile set + the four layer maps; tail starts at rest (pose 0)
        LZ77UnCompVram(sDrTitleAnimTiles, (void *)(BG_CHAR_ADDR(0)));
        LZ77UnCompVram(sDrTitleAnimFgMap, (void *)(BG_SCREEN_ADDR(TITLE_FG_SCREENBASE)));
        LZ77UnCompVram(sDrTitleAnimTailMap, (void *)(BG_SCREEN_ADDR(TITLE_TAIL_SCREENBASE)));
        LZ77UnCompVram(sDrTitleAnimSkyMap, (void *)(BG_SCREEN_ADDR(TITLE_SKY_SCREENBASE)));
        DmaCopy16(3, sDrTitleTailPoses, (void *)(BG_CHAR_ADDR(0) + TITLE_TAIL_TILE_BASE * TILE_SIZE_8BPP),
                  TITLE_TAIL_TILES * TILE_SIZE_8BPP);
        LoadPalette(sDrTitleAnimPal, BG_PLTT_ID(0), 16 * PLTT_SIZE_4BPP);
        sTitleAnimFrame = 0;
        sTitleSkyHofs = 0;
        sTitleSkyBlend = BLDALPHA_BLEND(16, 0);
        sTitleTailSeqIdx = 0;
        sTitleTailSeqTimer = 0;
        sTitleTailPosePending = -1;
        sTitleGlintActive = FALSE;
        ScanlineEffect_Stop();
        ResetTasks();
        ResetSpriteData();
        FreeAllSpritePalettes();
        gReservedSpritePaletteCount = 9;
        LoadCompressedSpriteSheet(&sSpriteSheet_EmeraldVersion[0]);
        LoadCompressedSpriteSheet(&sSpriteSheet_PressStart[0]);
        LoadCompressedSpriteSheet(&sPokemonLogoShineSpriteSheet[0]);
        LoadPalette(gTitleScreenEmeraldVersionPal, OBJ_PLTT_ID(0), PLTT_SIZE_4BPP);
        LoadSpritePalette(&sSpritePalette_PressStart[0]);
        gMain.state = 2;
        break;
    case 2:
    {
        u8 taskId = CreateTask(Task_TitleScreenPhase1, 0);

        gTasks[taskId].tCounter = 256;
        gTasks[taskId].tSkipToNext = FALSE;
        gTasks[taskId].tPointless = -16;
        gTasks[taskId].tBg2Y = -32;
        gMain.state = 3;
        break;
    }
    case 3:
        BeginNormalPaletteFade(PALETTES_ALL, 1, 16, 0, RGB_WHITEALPHA);
        SetVBlankCallback(VBlankCB);
        gMain.state = 4;
        break;
    case 4:
        SetGpuReg(REG_OFFSET_BG3CNT, BGCNT_PRIORITY(0) | BGCNT_CHARBASE(0) | BGCNT_SCREENBASE(TITLE_TAIL_SCREENBASE) | BGCNT_256COLOR | BGCNT_TXT256x256);
        SetGpuReg(REG_OFFSET_BG0CNT, BGCNT_PRIORITY(1) | BGCNT_CHARBASE(0) | BGCNT_SCREENBASE(TITLE_FG_SCREENBASE) | BGCNT_256COLOR | BGCNT_TXT256x256);
        SetGpuReg(REG_OFFSET_BG1CNT, BGCNT_PRIORITY(2) | BGCNT_CHARBASE(0) | BGCNT_SCREENBASE(TITLE_SKY_SCREENBASE) | BGCNT_256COLOR | BGCNT_TXT512x256);
        SetGpuReg(REG_OFFSET_BG2CNT, BGCNT_PRIORITY(3) | BGCNT_CHARBASE(0) | BGCNT_SCREENBASE(TITLE_SKY_SCREENBASE) | BGCNT_256COLOR | BGCNT_TXT512x256);
        SetGpuReg(REG_OFFSET_BG0HOFS, 0);
        SetGpuReg(REG_OFFSET_BG0VOFS, 0);
        SetGpuReg(REG_OFFSET_BG1HOFS, 0);
        SetGpuReg(REG_OFFSET_BG1VOFS, 0);
        SetGpuReg(REG_OFFSET_BG2HOFS, 1);
        SetGpuReg(REG_OFFSET_BG2VOFS, 0);
        SetGpuReg(REG_OFFSET_BG3HOFS, 0);
        SetGpuReg(REG_OFFSET_BG3VOFS, 0);
        // the sky is BG1 blended over BG2 (the same strip one pixel on); nothing else is blended
        SetGpuReg(REG_OFFSET_BLDCNT, BLDCNT_TGT1_BG1 | BLDCNT_EFFECT_BLEND | BLDCNT_TGT2_BG2);
        SetGpuReg(REG_OFFSET_BLDALPHA, BLDALPHA_BLEND(16, 0));
        EnableInterrupts(INTR_FLAG_VBLANK);
        SetGpuReg(REG_OFFSET_DISPCNT, DISPCNT_MODE_0
                                    | DISPCNT_OBJ_1D_MAP
                                    | DISPCNT_BG0_ON
                                    | DISPCNT_BG1_ON
                                    | DISPCNT_BG2_ON
                                    | DISPCNT_BG3_ON
                                    | DISPCNT_OBJ_ON);
        // Dreamstone Ruination: the title theme is a pedalled piano whose notes ring on in long
        // release tails; give it 10 sampled voices while the title screen is up (the game default is 5,
        // m4aSoundInit). RestoreSoundChannels() puts it back on the way out, so other music is unchanged.
        m4aSoundMode(TITLE_SOUND_CHANNELS << SOUND_MODE_MAXCHN_SHIFT);
        m4aSongNumStart(MUS_DR_TITLE);
        gMain.state = 5;
        break;
    case 5:
        if (!UpdatePaletteFade())
            SetMainCallback2(MainCB2);
        break;
    }
}

static void MainCB2(void)
{
    RunTasks();
    AnimateSprites();
    BuildOamBuffer();
    UpdatePaletteFade();
}

// Dreamstone Ruination: one task drives the whole title animation, one step per frame.
//  - sky: drifts left 1 px every TITLE_SKY_FRAMES_PER_PX frames; in between, BG1 (at x) is blended
//    toward BG2 (at x+1) in 16ths, so the clouds glide instead of stepping
//  - tail: steps through the generated idle sequence (pose, frames); VBlankCB copies a new pose in
//  - glint: every TITLE_GLINT_PERIOD frames a two-stripe glint crosses the logo; the logo's white fill
//    is split into diagonal palette bands, recoloured from the generated colour table
// Palette writes go to the faded buffer only while no fade runs, so fades in/out are untouched.
static void Task_TitleAnim(u8 taskId)
{
    u32 t = sTitleAnimFrame++;
    u32 step = t % TITLE_SKY_FRAMES_PER_PX;
    u32 evb = step * 16 / TITLE_SKY_FRAMES_PER_PX;
    s32 pos;
    u32 b;

    sTitleSkyHofs = (t / TITLE_SKY_FRAMES_PER_PX) & (TITLE_SKY_WIDTH - 1);
    sTitleSkyBlend = BLDALPHA_BLEND(16 - evb, evb);

    // frame t shows entry k for exactly its listed number of frames (check first, then count)
    if (sTitleTailSeqTimer >= sTitleTailSeq[sTitleTailSeqIdx][1])
    {
        sTitleTailSeqTimer = 0;
        if (++sTitleTailSeqIdx >= ARRAY_COUNT(sTitleTailSeq))
            sTitleTailSeqIdx = 0;
        if (sTitleTailSeq[sTitleTailSeqIdx][0] != sTitleTailSeq[(sTitleTailSeqIdx + ARRAY_COUNT(sTitleTailSeq) - 1) % ARRAY_COUNT(sTitleTailSeq)][0])
            sTitleTailPosePending = sTitleTailSeq[sTitleTailSeqIdx][0];
    }
    sTitleTailSeqTimer++;

    if (gPaletteFade.active)
        return;
    pos = TITLE_GLINT_UMIN - 30 + (s32)(t % TITLE_GLINT_PERIOD) * TITLE_GLINT_SPEED;
    if (pos < TITLE_GLINT_UMAX + 40)
    {
        for (b = 0; b < TITLE_GLINT_BANDS; b++)
        {
            s32 d = (s32)(TITLE_GLINT_UMIN + b * 3 + 1) - pos;
            u16 color = RGB_WHITE;
            if (d >= TITLE_GLINT_DMIN && d <= TITLE_GLINT_DMAX)
                color = sTitleGlintColors[d - TITLE_GLINT_DMIN];
            gPlttBufferFaded[TITLE_GLINT_PAL_BASE + b] = color;
        }
        sTitleGlintActive = TRUE;
    }
    else if (sTitleGlintActive)
    {
        for (b = 0; b < TITLE_GLINT_BANDS; b++)
            gPlttBufferFaded[TITLE_GLINT_PAL_BASE + b] = gPlttBufferUnfaded[TITLE_GLINT_PAL_BASE + b];
        sTitleGlintActive = FALSE;
    }
}

static void Task_TitleScreenPhase1(u8 taskId)
{
    // Dreamstone Ruination: the full title art is already on screen, so skip the
    // vanilla logo-shine + version-banner intro. Show Press Start and take input.
    CreatePressStartBanner(START_BANNER_X, 108);
    // DSMYST credit banner removed (was the flashing bottom credit)
    CreateTask(Task_TitleAnim, 2);
    gTasks[taskId].tCounter = 0;
    gTasks[taskId].func = Task_TitleScreenPhase3;
}

#undef sParentTaskId
#undef sAlphaBlendIdx

// Create "Press Start" and copyright banners, and slide Pokémon logo up
static void Task_TitleScreenPhase2(u8 taskId)
{
    u32 yPos;

    // Skip to next phase when A, B, Start, or Select is pressed
    if (JOY_NEW(A_B_START_SELECT) || gTasks[taskId].tSkipToNext)
    {
        gTasks[taskId].tSkipToNext = TRUE;
        gTasks[taskId].tCounter = 0;
    }

    if (gTasks[taskId].tCounter != 0)
    {
        gTasks[taskId].tCounter--;
    }
    else
    {
        gTasks[taskId].tSkipToNext = TRUE;
        SetGpuReg(REG_OFFSET_BLDCNT, BLDCNT_TGT1_BG1 | BLDCNT_EFFECT_BLEND | BLDCNT_TGT2_BG0 | BLDCNT_TGT2_BD);
        SetGpuReg(REG_OFFSET_BLDALPHA, BLDALPHA_BLEND(6, 15));
        SetGpuReg(REG_OFFSET_BLDY, 0);
        SetGpuReg(REG_OFFSET_DISPCNT, DISPCNT_MODE_1
                                    | DISPCNT_OBJ_1D_MAP
                                    | DISPCNT_BG0_ON
                                    | DISPCNT_BG1_ON
                                    | DISPCNT_BG2_ON
                                    | DISPCNT_OBJ_ON);
        CreatePressStartBanner(START_BANNER_X, 108);
        // DSMYST credit banner removed (was the flashing bottom credit)
        gTasks[taskId].tBg1Y = 0;
        gTasks[taskId].func = Task_TitleScreenPhase3;
    }

    if (!(gTasks[taskId].tCounter & 3) && gTasks[taskId].tPointless != 0)
        gTasks[taskId].tPointless++;
    if (!(gTasks[taskId].tCounter & 1) && gTasks[taskId].tBg2Y != 0)
        gTasks[taskId].tBg2Y++;

    // Slide Pokémon logo up
    yPos = gTasks[taskId].tBg2Y * 256;
    SetGpuReg(REG_OFFSET_BG2Y_L, yPos);
    SetGpuReg(REG_OFFSET_BG2Y_H, yPos / 0x10000);

    gTasks[taskId].data[5] = 15; // Unused
    gTasks[taskId].data[6] = 6;  // Unused
}

// Show Rayquaza silhouette and process main title screen input
static void Task_TitleScreenPhase3(u8 taskId)
{
    if (JOY_NEW(A_BUTTON) || JOY_NEW(START_BUTTON))
    {
        FadeOutBGM(4);
        BeginNormalPaletteFade(PALETTES_ALL, 0, 0, 16, RGB_BLACK);
        SetMainCallback2(CB2_GoToMainMenu);
    }
    else if (JOY_HELD(CLEAR_SAVE_BUTTON_COMBO) == CLEAR_SAVE_BUTTON_COMBO)
    {
        SetMainCallback2(CB2_GoToClearSaveDataScreen);
    }
    else if (JOY_HELD(RESET_RTC_BUTTON_COMBO) == RESET_RTC_BUTTON_COMBO
      && CanResetRTC() == TRUE)
    {
        FadeOutBGM(4);
        BeginNormalPaletteFade(PALETTES_ALL, 0, 0, 16, RGB_BLACK);
        SetMainCallback2(CB2_GoToResetRtcScreen);
    }
    else if (JOY_HELD(BERRY_UPDATE_BUTTON_COMBO) == BERRY_UPDATE_BUTTON_COMBO)
    {
        FadeOutBGM(4);
        BeginNormalPaletteFade(PALETTES_ALL, 0, 0, 16, RGB_BLACK);
        SetMainCallback2(CB2_GoToBerryFixScreen);
    }
    else
    {
        // (vanilla scrolled BG1 here for the Rayquaza clouds; BG1 is the drifting sky now -- Task_TitleAnim)
        if ((gMPlayInfo_BGM.status & 0xFFFF) == 0)
        {
            BeginNormalPaletteFade(PALETTES_ALL, 0, 0, 16, RGB_WHITEALPHA);
            SetMainCallback2(CB2_GoToCopyrightScreen);
        }
    }
}

static void RestoreSoundChannels(void)
{
    // Back to the game's default voice count. Set directly rather than through m4aSoundMode(), which
    // would also silence every channel and cut the title theme's fade-out; the next m4aSoundMode()
    // channel change (the title screen again) clears all channels anyway.
    SOUND_INFO_PTR->maxChans = DEFAULT_SOUND_CHANNELS;
    ResetTitleAnimGpu();
}

// Leave no title-screen display state behind for the next screen: our VBlank callback (sky scroll,
// blend, tail copies), the blend registers and the three extra layers.
static void ResetTitleAnimGpu(void)
{
    SetVBlankCallback(NULL);
    sTitleTailPosePending = -1;
    ClearGpuRegBits(REG_OFFSET_DISPCNT, DISPCNT_BG1_ON | DISPCNT_BG2_ON | DISPCNT_BG3_ON);
    SetGpuReg(REG_OFFSET_BLDCNT, 0);
    SetGpuReg(REG_OFFSET_BLDALPHA, 0);
    SetGpuReg(REG_OFFSET_BG1CNT, 0);
    SetGpuReg(REG_OFFSET_BG2CNT, 0);
    SetGpuReg(REG_OFFSET_BG3CNT, 0);
    SetGpuReg(REG_OFFSET_BG1HOFS, 0);
    SetGpuReg(REG_OFFSET_BG2HOFS, 0);
    SetGpuReg(REG_OFFSET_BG3HOFS, 0);
}

static void CB2_GoToMainMenu(void)
{
    if (!UpdatePaletteFade())
    {
        RestoreSoundChannels();
        SetMainCallback2(CB2_InitMainMenu);
    }
}

static void CB2_GoToCopyrightScreen(void)
{
    if (!UpdatePaletteFade())
    {
        RestoreSoundChannels();
        SetMainCallback2(CB2_InitCopyrightScreenAfterTitleScreen);
    }
}

static void CB2_GoToClearSaveDataScreen(void)
{
    if (!UpdatePaletteFade())
    {
        RestoreSoundChannels();
        SetMainCallback2(CB2_InitClearSaveDataScreen);
    }
}

static void CB2_GoToResetRtcScreen(void)
{
    if (!UpdatePaletteFade())
    {
        RestoreSoundChannels();
        SetMainCallback2(CB2_InitResetRtcScreen);
    }
}

static void CB2_GoToBerryFixScreen(void)
{
    if (!UpdatePaletteFade())
    {
        m4aMPlayAllStop();
        RestoreSoundChannels();
        SetMainCallback2(CB2_InitBerryFixProgram);
    }
}

static void UpdateLegendaryMarkingColor(u8 frameNum)
{
    if ((frameNum % 4) == 0) // Change color every 4th frame
    {
        s32 intensity = Cos(frameNum, 128) + 128;
        s32 r = 31 - ((intensity * 32 - intensity) / 256);
        s32 g = 31 - (intensity * 22 / 256);
        s32 b = 12;

        u16 color = RGB(r, g, b);
        LoadPalette(&color, BG_PLTT_ID(14) + 15, sizeof(color));
   }
}
