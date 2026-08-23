#include "global.h"
#include "bg.h"
#include "window.h"
#include "palette.h"
#include "decompress.h"
#include "malloc.h"
#include "script.h"
#include "field_message_box.h"
#include "portrait.h"
#include "constants/portraits.h"

// ---------------------------------------------------------------------------
// WHY THIS IS A BG WINDOW AND NOT AN OAM SPRITE
//
// Portraits used to be a 64x64 sprite drawn as a 2x2 grid of 32x32 subsprites,
// with only a 48x48 bust visible inside it. The source art is 96x96, so it was
// resampled DOWN by 1.5x -- a non-integer factor, where every output pixel is a
// blend of a 1.5x1.5 source region. Measured on the committed files:
//
//     cadmus_neutral   mean identical-pixel run 5.44px -> 4.30px
//     eden             mean identical-pixel run 5.30px -> 3.42px
//
// and bilinear resampling of a 46-colour source generates 1012 intermediate
// colours which are then crushed back to 16. The pipeline manufactured blur and
// then discarded the detail it blurred. That is the "blurry portraits" problem:
// the colour reduction was never at fault, the RESIZE was.
//
// A GBA OAM sprite caps at 64x64, so 96x96 art cannot be shown 1:1 as a sprite.
// Backgrounds have no such limit. As a BG0 window the 96x96 source displays
// EXACTLY as authored -- no downscale, no invented colours, ~4x the visible
// area of the old 48x48 bust.
//
// BUDGET (measured before writing this):
//   BG0 is priority 0 and sits above the map (BG1/2/3 are priority 1/2/3).
//   The field text box window starts at baseBlock 0x194 (tile 404) and Yes/No
//   at 0x125 (tile 293), so tiles below 293 are free. A 96x96 portrait is
//   12x12 = 144 tiles, placed at 0x080 (tile 128) and ending at 272 -- clear.
//   BG palettes 0-12 belong to the map tilesets and 15 to the text box, so the
//   portrait takes slot 13 and leaves 14 spare.
//
// The public API is unchanged, so no script or dialogue edits are needed.
// ---------------------------------------------------------------------------

#define PORTRAIT_WIDTH        96
#define PORTRAIT_HEIGHT       96
#define PORTRAIT_TILES_W      (PORTRAIT_WIDTH / 8)
#define PORTRAIT_TILES_H      (PORTRAIT_HEIGHT / 8)
#define PORTRAIT_NUM_TILES    (PORTRAIT_TILES_W * PORTRAIT_TILES_H)

#define PORTRAIT_BG           0
#define PORTRAIT_PALETTE      13
#define PORTRAIT_BASE_BLOCK   0x080

// Tilemap position in 8px units. Bottom-left, above the text box (which starts
// at tilemapTop 15). 12 tiles tall ending at row 15 means top row 3.
#define PORTRAIT_TILEMAP_LEFT 1
#define PORTRAIT_TILEMAP_TOP  1   // rows 1-12; row 13 is the nameplate

#include "data/portraits.h"

// Zero-initialised so no .data is emitted: pokeemerald's linker script places
// only .text/.rodata/.bss from src objects.
static bool8 sPortraitActive;
static u8 sPortraitWindowId;

static const struct WindowTemplate sPortraitWindowTemplate = {
    .bg = PORTRAIT_BG,
    .tilemapLeft = PORTRAIT_TILEMAP_LEFT,
    .tilemapTop = PORTRAIT_TILEMAP_TOP,
    .width = PORTRAIT_TILES_W,
    .height = PORTRAIT_TILES_H,
    .paletteNum = PORTRAIT_PALETTE,
    .baseBlock = PORTRAIT_BASE_BLOCK,
};

static const struct PortraitExpr *GetPortraitExpression(const struct Portrait *portrait, u8 expression)
{
    u32 i;

    if (portrait->expressions == NULL || portrait->numExpressions == 0)
        return NULL;

    for (i = 0; i < portrait->numExpressions; i++)
    {
        if (portrait->expressions[i].expression == expression)
            return &portrait->expressions[i];
    }

    return &portrait->expressions[0];
}

bool8 IsMsgPortraitActive(void)
{
    return sPortraitActive;
}

void FreeMsgPortrait(void)
{
    if (!sPortraitActive)
        return;

    ClearWindowTilemap(sPortraitWindowId);
    CopyWindowToVram(sPortraitWindowId, COPYWIN_MAP);
    RemoveWindow(sPortraitWindowId);
    sPortraitActive = FALSE;
}

void SetMsgPortrait(u8 portraitId, u8 expression)
{
    const struct Portrait *portrait;
    const struct PortraitExpr *expr;
    u8 *buffer;

    if (portraitId == PORTRAIT_NONE || portraitId >= PORTRAIT_COUNT)
        return;

    portrait = &gPortraits[portraitId];
    expr = GetPortraitExpression(portrait, expression);
    if (expr == NULL)
        return;

    FreeMsgPortrait();

    sPortraitWindowId = AddWindow(&sPortraitWindowTemplate);
    if (sPortraitWindowId == WINDOW_NONE)
        return;

    // The art is LZ77-compressed 4bpp in gbagfx's -mwidth/-mheight tile order,
    // which matches a window's pixel-buffer layout, so it decompresses straight
    // into the window rather than needing a per-tile blit.
    buffer = Alloc(PORTRAIT_NUM_TILES * TILE_SIZE_4BPP);
    if (buffer == NULL)
    {
        RemoveWindow(sPortraitWindowId);
        return;
    }
    LZ77UnCompWram(expr->tiles, buffer);
    CpuCopy16(buffer, (void *)GetWindowAttribute(sPortraitWindowId, WINDOW_TILE_DATA),
              PORTRAIT_NUM_TILES * TILE_SIZE_4BPP);
    Free(buffer);

    LoadPalette(expr->palette, BG_PLTT_ID(PORTRAIT_PALETTE), PLTT_SIZE_4BPP);

    PutWindowTilemap(sPortraitWindowId);
    CopyWindowToVram(sPortraitWindowId, COPYWIN_FULL);

    sPortraitActive = TRUE;

    if (portrait->name != NULL)
        SetSpeakerName(portrait->name);
}

void Script_ShowPortrait(struct ScriptContext *ctx)
{
    u8 portraitId = ScriptReadByte(ctx);
    u8 expression = ScriptReadByte(ctx);

    SetMsgPortrait(portraitId, expression);
}

void Script_HidePortrait(struct ScriptContext *ctx)
{
    FreeMsgPortrait();
}
