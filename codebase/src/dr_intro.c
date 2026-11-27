// Dreamstone Ruination - Chapter 1 cold open, Stage 1: the Professor Tenebris
// framing notes. White centered text revealed on a black screen over Osrid's
// Theme (now MonoMyth's "A Legend Unfolds", MUS_DR_LEGEND_UNFOLDS), then hands to the new-game init (placeholder: Carabrue) until Stage 2
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
#include "m4a.h"
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
// Tenebris's notes (user's text, approved 2026-11-26): to the Dreamstone Mysteries player, now Champion;
// she has found her ancestor Cadmus Umbra's papers. One screen per block.
static const u8 sTenebrisGreeting[] = _(
    "To my favourite\n"
    "lab assistant-turned-Champion,");

static const u8 sTenebrisP1[] = _(
    "I hope this finds you well!\n"
    "I know you've got a lot on\n"
    "your plate these days, but I\n"
    "thought you'd appreciate an\n"
    "update since our last chat\n"
    "at the lab.");

static const u8 sTenebrisP2[] = _(
    "I finished rummaging through\n"
    "my old family home and...\n"
    "I can barely believe it.\n"
    "I found writings from over\n"
    "two thousand years ago that\n"
    "actually document the lost\n"
    "age of the Cormorian Empire!");

static const u8 sTenebrisP3[] = _(
    "Try to wrap your mind\n"
    "around this.");

static const u8 sTenebrisP4[] = _(
    "Two thousand years before Red\n"
    "became Champion of the\n"
    "Indigo League in Kanto,\n"
    "the world of Pokémon was\n"
    "a very different place,\n"
    "and Cormoria most of all.\n"
    "It was almost unrecognisable.");

static const u8 sTenebrisP5[] = _(
    "You and I are no strangers\n"
    "to travelling into the\n"
    "distant past, but even so,\n"
    "this period in history was\n"
    "like a black hole.\n"
    "Even I knew almost nothing\n"
    "about it. Until now.");

static const u8 sTenebrisP6[] = _(
    "It was an age of empires\n"
    "and of stranger faiths,\n"
    "when every nation vied for\n"
    "supremacy over the others.");

static const u8 sTenebrisP7[] = _(
    "But those who wrote the\n"
    "histories that came after\n"
    "did their best to bury every\n"
    "trace of what happened.\n"
    "And now I have the proof.");

static const u8 sTenebrisP8[] = _(
    "I've barely begun to piece\n"
    "it all together, but if what\n"
    "these papers say is true,\n"
    "everything we thought we knew\n"
    "about the modern world\n"
    "is going to change.");

static const u8 sTenebrisP9[] = _(
    "My ancestor, Cadmus Umbra,\n"
    "was a Vizier of the Cormorian\n"
    "Empire in its waning years,\n"
    "and he was extremely thorough\n"
    "in recording what he saw.\n"
    "So brace yourself, kiddo.\n"
    "It's one wild tale.");

static const u8 sTenebrisP10[] = _(
    "It all starts with his own\n"
    "copy of a letter he sent\n"
    "to someone very important...");

static const u8 sDefaultPlayerName[] = _("Osrid");

static const u8 *const sIntroBlocks[] = {
    sTenebrisHeader, sTenebrisGreeting, sTenebrisP1, sTenebrisP2, sTenebrisP3, sTenebrisP4, sTenebrisP5,
    sTenebrisP6, sTenebrisP7, sTenebrisP8, sTenebrisP9, sTenebrisP10,
};
#define NUM_INTRO_BLOCKS ARRAY_COUNT(sIntroBlocks)

// index 0 = black (backdrop + window fill), 1 = white (text), 2 = grey (shadow)
static const u16 sIntroPalette[16] = { RGB_BLACK, RGB_WHITE, RGB(12, 12, 12) };

#define WIN_INTRO        0
#define REVEAL_SPEED     10
#define HOLD_FRAMES      180
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

    // MonoMyth's "A Legend Unfolds" (the museum's storybook legend of Athanto) carries the whole cold open:
    // these Tenebris notes, Cadmus's letter in PellucaReflection (same map music, so it is not restarted) and
    // on until Osrid lands in Pelluca City, whose town music takes over (user 2026-11-20; it replaced the
    // former title theme, "Far Horizons").
    m4aMPlayAllStop();
    m4aSongNumStart(MUS_DR_LEGEND_UNFOLDS);
    ContinueCurrentBGMAsMapMusic(MUS_DR_LEGEND_UNFOLDS);

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
