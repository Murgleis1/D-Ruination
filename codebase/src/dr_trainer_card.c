// Dreamstone Ruination: the player's own Trainer Card (layout A, approved 2026-11-18).
// One parchment sheet: the cover name, Money / PokeLog / Time, Osrid's portrait in a frame, and nine
// boxes that each Trial stamps with its symbol in its own ink once that Trial's badge is earned.
// No back side. Art and layout come from tools/art/trainer_card/build_card.py.
//   BG3  parchment with the name, labels, frame and boxes baked in (static)
//   BG2  the earned stamps (2x2 tiles each, transparent elsewhere)
//   BG1  windows: the live numbers (Jacquarda Bastarda digits) and the trainer portrait
// Link / Union Room cards still use the vanilla trainer_card.c.
#include "global.h"
#include "bg.h"
#include "decompress.h"
#include "dr_trainer_card.h"
#include "event_data.h"
#include "gpu_regs.h"
#include "main.h"
#include "malloc.h"
#include "money.h"
#include "palette.h"
#include "pokedex.h"
#include "scanline_effect.h"
#include "sound.h"
#include "sprite.h"
#include "task.h"
#include "text.h"
#include "trainer_pokemon_sprites.h"
#include "window.h"
#include "constants/rgb.h"
#include "constants/songs.h"
#include "constants/trainers.h"

#include "data/dr_trainer_card.h"

static const u32 sCardBgGfx[] = INCBIN_U32("graphics/trainer_card/dr/card_bg.4bpp.lz");
static const u32 sCardBgMap[] = INCBIN_U32("graphics/trainer_card/dr/card_bg.bin.lz");
static const u16 sCardPal[]   = INCBIN_U16("graphics/trainer_card/dr/card_bg.gbapal");
static const u32 sStampGfx[]  = INCBIN_U32("graphics/trainer_card/dr/stamps.4bpp");
static const u32 sDigitGfx[]  = INCBIN_U32("graphics/trainer_card/dr/digits.4bpp");

#define NUM_TRIALS        9
#define PIC_PALETTE_SLOT  8
#define VALUES_LEFT_TILE  8    // the numbers window spans x 64..127, y 32..87
#define VALUES_TOP_TILE   4

enum { WIN_VALUES, WIN_PIC };

static const struct BgTemplate sBgTemplates[] =
{
    { .bg = 1, .charBaseIndex = 2, .mapBaseIndex = 28, .screenSize = 0, .paletteMode = 0, .priority = 0, .baseTile = 0 },
    { .bg = 2, .charBaseIndex = 0, .mapBaseIndex = 29, .screenSize = 0, .paletteMode = 0, .priority = 1, .baseTile = 0 },
    { .bg = 3, .charBaseIndex = 0, .mapBaseIndex = 30, .screenSize = 0, .paletteMode = 0, .priority = 2, .baseTile = 0 },
};

static const struct WindowTemplate sWindowTemplates[] =
{
    [WIN_VALUES] = { .bg = 1, .tilemapLeft = VALUES_LEFT_TILE, .tilemapTop = VALUES_TOP_TILE, .width = 8, .height = 7, .paletteNum = 0, .baseBlock = 1 },
    [WIN_PIC]    = { .bg = 1, .tilemapLeft = DR_CARD_PIC_TILE_X, .tilemapTop = DR_CARD_PIC_TILE_Y, .width = 8, .height = 8, .paletteNum = PIC_PALETTE_SLOT, .baseBlock = 1 + 8 * 7 },
    DUMMY_WIN_TEMPLATE,
};

struct DrCard
{
    MainCallback callback;
    u16 bg1Map[BG_SCREEN_SIZE / 2];
    u16 bg2Map[BG_SCREEN_SIZE / 2];
    u16 bg3Map[BG_SCREEN_SIZE / 2];
};

static EWRAM_DATA struct DrCard *sCard = NULL;

static void CB2_DrCardInit(void);
static void CB2_DrCardMain(void);
static void VBlankCB_DrCard(void);
static void Task_DrCard(u8 taskId);

void DrShowPlayerTrainerCard(void (*callback)(void))
{
    sCard = AllocZeroed(sizeof(*sCard));
    sCard->callback = callback;
    SetMainCallback2(CB2_DrCardInit);
}

static u16 GetTrialFlag(u32 trial)
{
    return trial < 8 ? FLAG_BADGE01_GET + trial : FLAG_BADGE09_GET;
}

static void DrawStamps(void)
{
    u32 i;
    for (i = 0; i < NUM_TRIALS; i++)
    {
        u32 x = DR_CARD_STAMP_TILE_X0 + i * DR_CARD_STAMP_TILE_STEP, y = DR_CARD_STAMP_TILE_Y;
        u16 tile = DR_CARD_STAMP_TILE_BASE + i * 4;
        if (!FlagGet(GetTrialFlag(i)))
            continue;
        sCard->bg2Map[y * 32 + x]           = tile;
        sCard->bg2Map[y * 32 + x + 1]       = tile + 1;
        sCard->bg2Map[(y + 1) * 32 + x]     = tile + 2;
        sCard->bg2Map[(y + 1) * 32 + x + 1] = tile + 3;
    }
    CopyBgTilemapBufferToVram(2);
}

// Digits 0-9 are glyphs 0-9, ':' is glyph 10. Right-aligned at DR_CARD_VALUES_RIGHT, like the mockup.
static void DrawGlyphs(const u8 *glyphs, u32 count, u32 rowY)
{
    u32 i, width = 0;
    s32 x;
    for (i = 0; i < count; i++)
        width += sDrCardDigitAdvance[glyphs[i]];
    x = (DR_CARD_VALUES_RIGHT - VALUES_LEFT_TILE * 8) - width;
    for (i = 0; i < count; i++)
    {
        BlitBitmapRectToWindow(WIN_VALUES, (const u8 *)sDigitGfx, glyphs[i] * 8, 0, DR_CARD_DIGITS_WIDTH, 16,
                               x, rowY - VALUES_TOP_TILE * 8, 8, 16);
        x += sDrCardDigitAdvance[glyphs[i]];
    }
}

static u32 NumberToGlyphs(u32 value, u8 *out)
{
    u8 tmp[10];
    u32 n = 0, i;
    do { tmp[n++] = value % 10; value /= 10; } while (value != 0 && n < ARRAY_COUNT(tmp));
    for (i = 0; i < n; i++)
        out[i] = tmp[n - 1 - i];
    return n;
}

static void DrawValues(void)
{
    u8 g[12];
    u32 n;
    u16 caught = IsNationalPokedexEnabled() ? GetNationalPokedexCount(FLAG_GET_CAUGHT) : GetHoennPokedexCount(FLAG_GET_CAUGHT);

    FillWindowPixelBuffer(WIN_VALUES, PIXEL_FILL(0));
    n = NumberToGlyphs(GetMoney(&gSaveBlock1Ptr->money), g);
    DrawGlyphs(g, n, sDrCardRowY[0]);
    n = NumberToGlyphs(caught, g);
    DrawGlyphs(g, n, sDrCardRowY[1]);
    n = NumberToGlyphs(gSaveBlock2Ptr->playTimeHours, g);
    g[n++] = 10;                                            // ':'
    g[n++] = gSaveBlock2Ptr->playTimeMinutes / 10;
    g[n++] = gSaveBlock2Ptr->playTimeMinutes % 10;
    DrawGlyphs(g, n, sDrCardRowY[2]);
    PutWindowTilemap(WIN_VALUES);
    CopyWindowToVram(WIN_VALUES, COPYWIN_FULL);
}

static void DrawPortrait(void)
{
    FillWindowPixelBuffer(WIN_PIC, PIXEL_FILL(0));
    CreateTrainerCardTrainerPicSprite(TRAINER_PIC_OSRID, TRUE, 0, 0, PIC_PALETTE_SLOT, WIN_PIC);
    PutWindowTilemap(WIN_PIC);
    CopyWindowToVram(WIN_PIC, COPYWIN_FULL);
}

static void CB2_DrCardInit(void)
{
    u32 i;

    switch (gMain.state)
    {
    case 0:
        SetVBlankCallback(NULL);
        SetHBlankCallback(NULL);
        SetGpuReg(REG_OFFSET_DISPCNT, 0);
        ScanlineEffect_Stop();
        DmaClearLarge16(3, (void *)VRAM, VRAM_SIZE, 0x1000);
        DmaClear32(3, (void *)OAM, OAM_SIZE);
        DmaClear16(3, (void *)PLTT, PLTT_SIZE);
        ResetPaletteFade();
        ResetSpriteData();
        FreeAllSpritePalettes();
        ResetTasks();
        gMain.state++;
        break;
    case 1:
        ResetBgsAndClearDma3BusyFlags(0);
        InitBgsFromTemplates(0, sBgTemplates, ARRAY_COUNT(sBgTemplates));
        for (i = 0; i < 4; i++)                       // the overworld leaves its scroll in the BG registers
        {
            ChangeBgX(i, 0, BG_COORD_SET);
            ChangeBgY(i, 0, BG_COORD_SET);
        }
        SetBgTilemapBuffer(1, sCard->bg1Map);
        SetBgTilemapBuffer(2, sCard->bg2Map);
        SetBgTilemapBuffer(3, sCard->bg3Map);
        InitWindows(sWindowTemplates);
        DeactivateAllTextPrinters();
        gMain.state++;
        break;
    case 2:
        LZ77UnCompVram(sCardBgGfx, (void *)BG_CHAR_ADDR(0));
        CpuCopy32(sStampGfx, (void *)(BG_CHAR_ADDR(0) + DR_CARD_STAMP_TILE_BASE * TILE_SIZE_4BPP), sizeof(sStampGfx));
        LZ77UnCompWram(sCardBgMap, sCard->bg3Map);
        CopyBgTilemapBufferToVram(3);
        LoadPalette(sCardPal, BG_PLTT_ID(0), PLTT_SIZE_4BPP);
        gMain.state++;
        break;
    case 3:
        DrawStamps();
        DrawValues();
        DrawPortrait();
        gMain.state++;
        break;
    default:
        SetGpuReg(REG_OFFSET_BLDCNT, 0);
        SetGpuReg(REG_OFFSET_DISPCNT, DISPCNT_OBJ_ON | DISPCNT_OBJ_1D_MAP);
        ShowBg(1);
        ShowBg(2);
        ShowBg(3);
        HideBg(0);
        BeginNormalPaletteFade(PALETTES_ALL, 0, 16, 0, RGB_BLACK);
        SetVBlankCallback(VBlankCB_DrCard);
        CreateTask(Task_DrCard, 0);
        SetMainCallback2(CB2_DrCardMain);
        break;
    }
}

static void CB2_DrCardMain(void)
{
    RunTasks();
    AnimateSprites();
    BuildOamBuffer();
    UpdatePaletteFade();
}

static void VBlankCB_DrCard(void)
{
    LoadOam();
    ProcessSpriteCopyRequests();
    TransferPlttBuffer();
}

// A or B closes the card (there is no back to flip to).
static void Task_DrCard(u8 taskId)
{
    switch (gTasks[taskId].data[0])
    {
    case 0:
        if (!gPaletteFade.active && JOY_NEW(A_BUTTON | B_BUTTON))
        {
            PlaySE(SE_SELECT);
            BeginNormalPaletteFade(PALETTES_ALL, 0, 0, 16, RGB_BLACK);
            gTasks[taskId].data[0]++;
        }
        break;
    case 1:
        if (!gPaletteFade.active)
        {
            MainCallback callback = sCard->callback;
            FreeAllWindowBuffers();
            DestroyTask(taskId);
            FREE_AND_SET_NULL(sCard);
            SetMainCallback2(callback);
        }
        break;
    }
}
