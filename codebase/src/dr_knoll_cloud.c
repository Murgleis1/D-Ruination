// Dreamstone Ruination: the cap of cloud over Hollow Hill's knoll (user 2026-11-25; tools/art/hollowhill/knoll_cloud.py).
// It hides the knoll's small flat top, so the hill reads as rising into cloud (the summit beyond the sealed door is
// somewhere up in it). Thirteen sprites sharing one picture (Emerald's own top-down weather cloud, recoloured to the
// fog's greys): a still heart, an inner ring of 4 turning one way, an outer ring of 8 turning the other, on ellipses;
// a quarter turn takes 40 seconds (user: "a lot slower and smoother"), positions computed in 1/1024ths of a turn, so
// each billow creeps a fraction of a pixel a frame. Created whenever the player is on Hollow Hill and the sprites are
// not there (after a warp, a battle, a connection crossing), destroyed on leaving. Drawn behind every object.
#include "global.h"
#include "sprite.h"
#include "trig.h"
#include "event_object_movement.h"
#include "field_weather.h"
#include "fieldmap.h"
#include "dr_knoll_cloud.h"
#include "constants/maps.h"

#define TAG_KNOLL_CLOUD  0x1140
#define NUM_CLOUDS       13
#define QUARTER_FRAMES   2400                 // 40 seconds at 60 fps for a quarter turn
#define FULL_FRAMES      (QUARTER_FRAMES * 4)
#define CENTRE_X         (29 + MAP_OFFSET)    // the knoll's top: cell 29 (+8 px) ...
#define CENTRE_Y         (29 + MAP_OFFSET)    // ... row 29 (+7 px): the cap's foot ends just above the sealed door's
#define CENTRE_DX        8                    // row (35), so from the door's forecourt it hangs right overhead
#define CENTRE_DY        7

static const u32 sKnollCloudGfx[] = INCBIN_U32("graphics/field_effects/pics/dr_knoll_cloud.4bpp");
static const u16 sKnollCloudPal[] = INCBIN_U16("graphics/field_effects/pics/dr_knoll_cloud.gbapal");

static const struct SpriteSheet sKnollCloudSheet = {sKnollCloudGfx, sizeof(sKnollCloudGfx), TAG_KNOLL_CLOUD};
static const struct SpritePalette sKnollCloudPalette = {sKnollCloudPal, TAG_KNOLL_CLOUD};

static const struct OamData sKnollCloudOam = {
    .affineMode = ST_OAM_AFFINE_OFF,
    .objMode = ST_OAM_OBJ_NORMAL,
    .shape = SPRITE_SHAPE(64x64),
    .size = SPRITE_SIZE(64x64),
    .priority = 2,
};

static const union AnimCmd sAnim_Plain[]   = {ANIMCMD_FRAME(0, 30), ANIMCMD_END};
static const union AnimCmd sAnim_HFlip[]   = {ANIMCMD_FRAME(0, 30, .hFlip = TRUE), ANIMCMD_END};
static const union AnimCmd sAnim_VFlip[]   = {ANIMCMD_FRAME(0, 30, .vFlip = TRUE), ANIMCMD_END};
static const union AnimCmd sAnim_HVFlip[]  = {ANIMCMD_FRAME(0, 30, .hFlip = TRUE, .vFlip = TRUE), ANIMCMD_END};
static const union AnimCmd *const sKnollCloudAnims[] = {sAnim_Plain, sAnim_HFlip, sAnim_VFlip, sAnim_HVFlip};

static void SpriteCB_KnollCloud(struct Sprite *sprite);

static const struct SpriteTemplate sKnollCloudTemplate = {
    .tileTag = TAG_KNOLL_CLOUD,
    .paletteTag = TAG_KNOLL_CLOUD,
    .oam = &sKnollCloudOam,
    .anims = sKnollCloudAnims,
    .images = NULL,
    .affineAnims = gDummySpriteAffineAnimTable,
    .callback = SpriteCB_KnollCloud,
};

// the rings (knoll_cloud.py RINGS): x radius, y radius, turning direction, copies, their two flips, a start angle
struct KnollRing { u8 rx, ry; s8 dir; u8 count; u8 flips[2]; u16 start; };
static const struct KnollRing sRings[] = {
    { 0,  0,  1, 1, {0, 0}, 0},
    {22, 14,  1, 4, {1, 2}, 0},
    {46, 33, -1, 8, {0, 3}, 65},            // (0.4 rad)
};
#define CY_OFFSET 8

static EWRAM_DATA u32 sKnollCloudPhase = 0;
static EWRAM_DATA u8 sKnollCloudIds[NUM_CLOUDS] = {0};

#define sRing   data[0]
#define sSlot   data[1]

// sine of an angle in 1/1024ths of a turn, Q8 (256 = 1), interpolated between the 256-step table's entries
static s32 Sin1024(u32 a)
{
    u32 i = (a >> 2) & 0xFF, f = a & 3;
    return (gSineTable[i] * (4 - f) + gSineTable[(i + 1) & 0xFF] * f) / 4;
}

static bool32 OnHollowHill(void)
{
    return gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(HOLLOW_HILL)
        && gSaveBlock1Ptr->location.mapNum == MAP_NUM(HOLLOW_HILL);
}

static void SpriteCB_KnollCloud(struct Sprite *sprite)
{
    const struct KnollRing *ring = &sRings[sprite->sRing];
    u32 rot = (sKnollCloudPhase * 256) / QUARTER_FRAMES;                  // 1/1024ths turned so far
    u32 a = (ring->start + sprite->sSlot * 1024 / ring->count + (ring->dir > 0 ? rot : 1024 * 4 - rot)) & 1023;
    s32 s = Sin1024(a), c = Sin1024(a + 256);
    s32 sx, sy;
    sprite->x2 = (ring->rx * c) / 256;
    sprite->y2 = CY_OFFSET + (ring->ry * s) / 256;
    // the far side first, the near side over it; all behind every object (the player, people)
    sprite->subpriority = 250 - (s + 256) / 16;
    sx = sprite->x + sprite->x2 + gSpriteCoordOffsetX;
    sy = sprite->y + sprite->y2 + gSpriteCoordOffsetY;
    sprite->invisible = (sx < -40 || sx > DISPLAY_WIDTH + 40 || sy < -40 || sy > DISPLAY_HEIGHT + 40);
}

static void CreateKnollCloud(void)
{
    u32 r, j, n = 0;
    s16 x = CENTRE_X, y = CENTRE_Y;
    LoadSpriteSheet(&sKnollCloudSheet);
    LoadSpritePalette(&sKnollCloudPalette);
    // (not passed through the weather's palette blend: the fog would wash it to its own pale green)
    SetSpritePosToOffsetMapCoords(&x, &y, CENTRE_DX, CENTRE_DY);
    for (r = 0; r < ARRAY_COUNT(sRings); r++)
    {
        for (j = 0; j < sRings[r].count && n < NUM_CLOUDS; j++, n++)
        {
            u8 id = CreateSprite(&sKnollCloudTemplate, x, y, 250);
            sKnollCloudIds[n] = id;
            if (id == MAX_SPRITES)
                continue;
            gSprites[id].coordOffsetEnabled = TRUE;
            gSprites[id].sRing = r;
            gSprites[id].sSlot = j;
            StartSpriteAnim(&gSprites[id], sRings[r].flips[j % 2]);
            SpriteCB_KnollCloud(&gSprites[id]);
        }
    }
}

static void DestroyKnollCloud(void)
{
    u32 n;
    for (n = 0; n < NUM_CLOUDS; n++)
    {
        u8 id = sKnollCloudIds[n];
        if (id < MAX_SPRITES && gSprites[id].inUse && gSprites[id].template == &sKnollCloudTemplate)
            DestroySprite(&gSprites[id]);
        sKnollCloudIds[n] = MAX_SPRITES;
    }
    FreeSpriteTilesByTag(TAG_KNOLL_CLOUD);
    FreeSpritePaletteByTag(TAG_KNOLL_CLOUD);
}

void DrKnollCloud_Update(void)
{
    bool32 loaded = (GetSpriteTileStartByTag(TAG_KNOLL_CLOUD) != 0xFFFF);
    if (OnHollowHill())
    {
        if (!loaded)
            CreateKnollCloud();
        if (++sKnollCloudPhase >= FULL_FRAMES)
            sKnollCloudPhase = 0;
    }
    else if (loaded)
    {
        DestroyKnollCloud();
    }
}
