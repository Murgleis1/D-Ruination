// Dreamstone Ruination - Chapter 1 cold open, Stage 1: the Professor Tenebris
// framing notes. White centered text revealed on a black screen over Osrid's
// Theme, then hands to the new-game init (placeholder: Carabrue) until Stage 2
// adds the reflection scene + Umbra's letter + the diegetic naming.
#include "global.h"
#include "main.h"
#include "task.h"
#include "bg.h"
#include "window.h"
#include "text.h"
#include "palette.h"
#include "gpu_regs.h"
#include "scanline_effect.h"
#include "sound.h"
#include "string_util.h"
#include "new_game.h"
#include "menu.h"
#include "overworld.h"
#include "constants/rgb.h"
#include "constants/songs.h"
#include "constants/characters.h"

void CB2_DrColdOpenIntro(void); // exported; hooked from the main menu's New Game action

static void DrIntro_VBlankCB(void);
static void DrIntro_MainCB2(void);
static void Task_DrIntro(u8 taskId);
static void DrIntro_InitBg(void);
static void DrIntro_InitWindow(void);
static void DrIntro_PrintBlock(const u8 *text);

// Narration text, pre-wrapped into lines (the printer does not auto-wrap).
static const u8 sTenebrisHeader[] = _("From the notes of Professor\nTenebris - XX-XX-29");
static const u8 sTenebrisP1[] = _(
    "3000 years before Red started\n"
    "his journey from Pallet Town,\n"
    "the world of Pokémon was\n"
    "a very different place.");
static const u8 sTenebrisP2[] = _(
    "It was a terrifying era of\n"
    "imperial conflict and strange\n"
    "cults, a setting so far removed\n"
    "from what we know in the modern\n"
    "Pokémon world that “they” who\n"
    "decided history have done\n"
    "everything they possibly could\n"
    "to bury those records forever.");
static const u8 sTenebrisP3[] = _(
    "This is the story I know of\n"
    "that place and time, the seed\n"
    "of all which would come to be...");
static const u8 sDefaultPlayerName[] = _("Osrid");

static const u8 *const sIntroBlocks[] = {
    sTenebrisHeader, sTenebrisP1, sTenebrisP2, sTenebrisP3,
};
#define NUM_INTRO_BLOCKS ARRAY_COUNT(sIntroBlocks)

// index 0 = black (backdrop + window fill), 1 = white (text), 2 = grey (shadow)
static const u16 sIntroPalette[16] = { RGB_BLACK, RGB_WHITE, RGB(12, 12, 12) };

#define WIN_INTRO        0
#define REVEAL_SPEED     3
#define HOLD_FRAMES      150
#define LINE_HEIGHT      16
#define WIN_W_PX         (28 * 8)
#define WIN_H_PX         (18 * 8)

enum { ST_FADEIN, ST_PRINT, ST_REVEAL, ST_HOLD, ST_FADEOUT, ST_DONE };
#define tState data[0]
#define tBlock data[1]
#define tTimer data[2]

static const struct BgTemplate sIntroBgTemplates[] = {
    { .bg = 0, .charBaseIndex = 0, .mapBaseIndex = 31, .screenSize = 0,
      .paletteMode = 0, .priority = 0, .baseTile = 0 },
};

static const struct WindowTemplate sIntroWinTemplates[] = {
    { .bg = 0, .tilemapLeft = 1, .tilemapTop = 1, .width = 28, .height = 18,
      .paletteNum = 0, .baseBlock = 1 },
    DUMMY_WIN_TEMPLATE,
};

static void DrIntro_VBlankCB(void)
{
    LoadOam();
    ProcessSpriteCopyRequests();
    TransferPlttBuffer();
}

static void DrIntro_MainCB2(void)
{
    RunTasks();
    AnimateSprites();
    BuildOamBuffer();
    UpdatePaletteFade();
    RunTextPrinters();
}

void CB2_DrColdOpenIntro(void)
{
    SetVBlankCallback(NULL);
    SetGpuReg(REG_OFFSET_DISPCNT, 0);
    SetGpuReg(REG_OFFSET_BG3CNT, 0);
    SetGpuReg(REG_OFFSET_BG2CNT, 0);
    SetGpuReg(REG_OFFSET_BG1CNT, 0);
    SetGpuReg(REG_OFFSET_BG0CNT, 0);
    SetGpuReg(REG_OFFSET_BG0HOFS, 0);
    SetGpuReg(REG_OFFSET_BG0VOFS, 0);
    DmaFill16(3, 0, VRAM, VRAM_SIZE);
    DmaFill32(3, 0, OAM, OAM_SIZE);
    DmaFill16(3, 0, PLTT, PLTT_SIZE);
    ScanlineEffect_Stop();
    ResetTasks();
    ResetSpriteData();
    ResetPaletteFade();
    FreeAllSpritePalettes();
    DrIntro_InitBg();
    DrIntro_InitWindow();

    PlayBGM(MUS_OSRID_THEME);

    BlendPalettes(PALETTES_ALL, 16, RGB_BLACK);
    BeginNormalPaletteFade(PALETTES_ALL, 0, 16, 0, RGB_BLACK);
    EnableInterrupts(1);
    SetVBlankCallback(DrIntro_VBlankCB);
    SetMainCallback2(DrIntro_MainCB2);

    {
        u8 taskId = CreateTask(Task_DrIntro, 0);
        gTasks[taskId].tState = ST_FADEIN;
        gTasks[taskId].tBlock = 0;
    }
}

static void DrIntro_InitBg(void)
{
    ResetBgsAndClearDma3BusyFlags(0);
    InitBgsFromTemplates(0, sIntroBgTemplates, ARRAY_COUNT(sIntroBgTemplates));
    SetGpuReg(REG_OFFSET_DISPCNT, DISPCNT_OBJ_ON | DISPCNT_OBJ_1D_MAP);
    ShowBg(0);
    SetGpuReg(REG_OFFSET_BLDCNT, 0);
    SetGpuReg(REG_OFFSET_BLDALPHA, 0);
    SetGpuReg(REG_OFFSET_BLDY, 0);
}

static void DrIntro_InitWindow(void)
{
    InitWindows(sIntroWinTemplates);
    DeactivateAllTextPrinters();
    LoadPalette(sIntroPalette, BG_PLTT_ID(0), sizeof(sIntroPalette));
    FillWindowPixelBuffer(WIN_INTRO, PIXEL_FILL(0));
    PutWindowTilemap(WIN_INTRO);
    CopyWindowToVram(WIN_INTRO, COPYWIN_FULL);
}

// Center the text block: horizontally on its widest line, vertically on its line count.
static void DrIntro_PrintBlock(const u8 *text)
{
    u8 color[3] = { 0, 1, 2 };
    u8 line[96];
    const u8 *p = text;
    u32 maxW = 0, w, x, y;
    u32 numLines = 1;

    while (*p != EOS)
    {
        u8 *dst = line;
        while (*p != EOS && *p != CHAR_NEWLINE)
            *dst++ = *p++;
        *dst = EOS;
        w = GetStringWidth(FONT_NORMAL, line, 0);
        if (w > maxW)
            maxW = w;
        if (*p == CHAR_NEWLINE)
        {
            numLines++;
            p++;
        }
    }

    x = (maxW < WIN_W_PX) ? (WIN_W_PX - maxW) / 2 : 0;
    y = (numLines * LINE_HEIGHT < WIN_H_PX) ? (WIN_H_PX - numLines * LINE_HEIGHT) / 2 : 0;

    FillWindowPixelBuffer(WIN_INTRO, PIXEL_FILL(0));
    AddTextPrinterParameterized4(WIN_INTRO, FONT_NORMAL, x, y, 0, 1, color, REVEAL_SPEED, text);
    CopyWindowToVram(WIN_INTRO, COPYWIN_FULL);
}

static void Task_DrIntro(u8 taskId)
{
    s16 *data = gTasks[taskId].data;

    // Let the player skip the whole framing.
    if (JOY_NEW(START_BUTTON) && tState != ST_DONE)
    {
        BeginNormalPaletteFade(PALETTES_ALL, 0, 0, 16, RGB_BLACK);
        tState = ST_DONE;
        return;
    }

    switch (tState)
    {
    case ST_FADEIN:
        if (!gPaletteFade.active)
            tState = ST_PRINT;
        break;
    case ST_PRINT:
        DrIntro_PrintBlock(sIntroBlocks[tBlock]);
        BeginNormalPaletteFade(PALETTES_ALL, 0, 16, 0, RGB_BLACK);
        tState = ST_REVEAL;
        break;
    case ST_REVEAL:
        if (!gPaletteFade.active && !IsTextPrinterActive(WIN_INTRO))
        {
            tTimer = HOLD_FRAMES;
            tState = ST_HOLD;
        }
        break;
    case ST_HOLD:
        if (--tTimer <= 0)
        {
            BeginNormalPaletteFade(PALETTES_ALL, 0, 0, 16, RGB_BLACK);
            tState = ST_FADEOUT;
        }
        break;
    case ST_FADEOUT:
        if (!gPaletteFade.active)
        {
            FillWindowPixelBuffer(WIN_INTRO, PIXEL_FILL(0));
            CopyWindowToVram(WIN_INTRO, COPYWIN_FULL);
            if (++tBlock >= (s16)NUM_INTRO_BLOCKS)
                tState = ST_DONE;
            else
                tState = ST_PRINT;
        }
        break;
    case ST_DONE:
        if (!gPaletteFade.active)
        {
            FreeAllWindowBuffers();
            // Placeholder handoff until Stage 2: default name, then standard new game.
            StringCopy(gSaveBlock2Ptr->playerName, sDefaultPlayerName);
            SetMainCallback2(CB2_NewGame);
        }
        break;
    }
}
