#include "global.h"
#include "sprite.h"
#include "decompress.h"
#include "script.h"
#include "field_message_box.h"
#include "portrait.h"
#include "constants/portraits.h"

// Only one portrait is ever shown at a time, so it owns a single pair of VRAM tags.
#define PORTRAIT_TILE_TAG   0x4B00
#define PORTRAIT_PAL_TAG    0x4B00

#define PORTRAIT_WIDTH      96
#define PORTRAIT_HEIGHT     96
#define PORTRAIT_NUM_TILES  ((PORTRAIT_WIDTH / 8) * (PORTRAIT_HEIGHT / 8))   // 144

// On-screen anchor (the sprite's centre). Bottom-left, sitting above the text
// box. Nudge these two if the bust needs repositioning.
#define PORTRAIT_CENTER_X   52
#define PORTRAIT_CENTER_Y   60

#include "data/portraits.h"

// sPortraitActive tracks whether a bust is on screen. It is zero-initialised
// (inactive at boot) so no initialised .data is emitted: pokeemerald's linker
// script places only .text/.rodata/.bss from src objects, and a non-zero-init
// global (e.g. = MAX_SPRITES) would fall through to /DISCARD/ at link time.
static bool8 sPortraitActive;
static u8 sPortraitSpriteId;

// A 96x96 bust is drawn as a 3x3 grid of 32x32 OAM subsprites. gbagfx builds the
// tiles with -mwidth 4 -mheight 4, i.e. nine contiguous 32x32 cells in reading
// order, so each cell is 16 tiles and the tileOffsets step by 16. .x/.y are the
// cell's top-left offset from the sprite centre.
static const struct Subsprite sPortraitSubsprites[] = {
    { .x = -48, .y = -48, .shape = SPRITE_SHAPE(32x32), .size = SPRITE_SIZE(32x32), .tileOffset =   0, .priority = 0 },
    { .x = -16, .y = -48, .shape = SPRITE_SHAPE(32x32), .size = SPRITE_SIZE(32x32), .tileOffset =  16, .priority = 0 },
    { .x =  16, .y = -48, .shape = SPRITE_SHAPE(32x32), .size = SPRITE_SIZE(32x32), .tileOffset =  32, .priority = 0 },
    { .x = -48, .y = -16, .shape = SPRITE_SHAPE(32x32), .size = SPRITE_SIZE(32x32), .tileOffset =  48, .priority = 0 },
    { .x = -16, .y = -16, .shape = SPRITE_SHAPE(32x32), .size = SPRITE_SIZE(32x32), .tileOffset =  64, .priority = 0 },
    { .x =  16, .y = -16, .shape = SPRITE_SHAPE(32x32), .size = SPRITE_SIZE(32x32), .tileOffset =  80, .priority = 0 },
    { .x = -48, .y =  16, .shape = SPRITE_SHAPE(32x32), .size = SPRITE_SIZE(32x32), .tileOffset =  96, .priority = 0 },
    { .x = -16, .y =  16, .shape = SPRITE_SHAPE(32x32), .size = SPRITE_SIZE(32x32), .tileOffset = 112, .priority = 0 },
    { .x =  16, .y =  16, .shape = SPRITE_SHAPE(32x32), .size = SPRITE_SIZE(32x32), .tileOffset = 128, .priority = 0 },
};

static const struct SubspriteTable sPortraitSubspriteTable[] = {
    { ARRAY_COUNT(sPortraitSubsprites), sPortraitSubsprites },
};

// Base OAM is a template only; SUBSPRITES_ON makes the subsprite table drive
// rendering (the base object itself is not drawn).
static const struct OamData sPortraitOam = {
    .affineMode = ST_OAM_AFFINE_OFF,
    .objMode = ST_OAM_OBJ_NORMAL,
    .bpp = ST_OAM_4BPP,
    .shape = SPRITE_SHAPE(32x32),
    .size = SPRITE_SIZE(32x32),
    .priority = 0,
};

static const struct SpriteTemplate sPortraitSpriteTemplate = {
    .tileTag = PORTRAIT_TILE_TAG,
    .paletteTag = PORTRAIT_PAL_TAG,
    .oam = &sPortraitOam,
    .anims = gDummySpriteAnimTable,
    .images = NULL,
    .affineAnims = gDummySpriteAffineAnimTable,
    .callback = SpriteCallbackDummy,
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

    return &portrait->expressions[0];   // fall back to the character's default expression
}

bool8 IsMsgPortraitActive(void)
{
    return sPortraitActive;
}

void FreeMsgPortrait(void)
{
    if (!sPortraitActive)
        return;

    DestroySprite(&gSprites[sPortraitSpriteId]);
    FreeSpriteTilesByTag(PORTRAIT_TILE_TAG);
    FreeSpritePaletteByTag(PORTRAIT_PAL_TAG);
    sPortraitActive = FALSE;
}

void SetMsgPortrait(u8 portraitId, u8 expression)
{
    const struct Portrait *portrait;
    const struct PortraitExpr *expr;
    struct CompressedSpriteSheet sheet;
    struct SpritePalette palette;
    u32 spriteId;

    if (portraitId == PORTRAIT_NONE || portraitId >= PORTRAIT_COUNT)
        return;

    portrait = &gPortraits[portraitId];
    expr = GetPortraitExpression(portrait, expression);
    if (expr == NULL)
        return;

    // Clear any portrait already on screen (handles speaker / expression swaps).
    FreeMsgPortrait();

    sheet.data = expr->tiles;
    sheet.size = PORTRAIT_NUM_TILES * TILE_SIZE_4BPP;
    sheet.tag = PORTRAIT_TILE_TAG;
    palette.data = expr->palette;
    palette.tag = PORTRAIT_PAL_TAG;

    LoadCompressedSpriteSheet(&sheet);
    LoadSpritePalette(&palette);

    spriteId = CreateSprite(&sPortraitSpriteTemplate, PORTRAIT_CENTER_X, PORTRAIT_CENTER_Y, 0);
    if (spriteId == MAX_SPRITES)
    {
        FreeSpriteTilesByTag(PORTRAIT_TILE_TAG);
        FreeSpritePaletteByTag(PORTRAIT_PAL_TAG);
        return;
    }

    SetSubspriteTables(&gSprites[spriteId], sPortraitSubspriteTable);
    sPortraitSpriteId = spriteId;
    sPortraitActive = TRUE;

    // Default the nameplate from the registry. Portraits with no default name
    // (e.g. Osrid) leave any script-set speaker name untouched.
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
