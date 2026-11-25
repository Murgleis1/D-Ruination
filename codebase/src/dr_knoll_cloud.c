// Dreamstone Ruination: the cap of cloud over Hollow Hill's knoll (user 2026-11-25; tools/art/hollowhill/knoll_cloud.py).
// It hides the knoll's whole top, so the hill reads as rising into cloud (the summit beyond the sealed door is
// somewhere up in it): the cloud itself in the map's tiles, and 64x32 billows of Emerald's weather cloud
// (knoll_cloud.lens_indices) turning round its rim. Created whenever the player is on Hollow Hill and the sprites are not there (after a warp,
// a battle, crossing from Route 11), destroyed on leaving. Drawn above the map; the player and people always in front of it.
#include "global.h"
#include "sprite.h"
#include "trig.h"
#include "event_object_movement.h"
#include "field_weather.h"
#include "fieldmap.h"
#include "dr_knoll_cloud.h"
#include "constants/maps.h"
#include "gpu_regs.h"

#define TAG_KNOLL_CLOUD  0x1140
#define NUM_CLOUDS       26
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
    .shape = SPRITE_SHAPE(64x32),
    .size = SPRITE_SIZE(64x32),
    .priority = 1,          // (over the tree crowns where it spills off the knoll; the player and people stay in front)
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

// v3 (user 2026-11-25: "the WHOLE top area of the hill peak needs clouds"): the knoll's whole top above the door's
// band is cloud in the map itself (tools/art/hollowhill/hh_door.py, knoll_cloud.under_cells); these billows travel
// slowly clockwise round its outline (a lap in 160 s), always covering its hard cell edge (knoll_cloud.conveyor_check:
// the edge never shows, the low door never covered, at most 8 billows on a scanline). Their track:
#include "data/dr_knoll_cloud_path.h"
#define NUM_RIM      20
#define LAP_FRAMES   9600
// and six more circling inside it over the cloud's middle, clockwise, a turn in 160 s too (on an ellipse 96x40 about
// a point 16 px above the centre: only where few rim billows cross the same lines; 9 at most on any line in all)
#define NUM_INNER    6
#define INNER_RX     48
#define INNER_RY     20
#define INNER_CY     (-16)
#define PATH_LEN     ARRAY_COUNT(sKnollCloudPath)

static EWRAM_DATA u32 sKnollCloudPhase = 0;
static EWRAM_DATA u8 sKnollCloudIds[NUM_CLOUDS] = {0};

#define sSlot   data[1]

static bool32 OnHollowHill(void)
{
    return gSaveBlock1Ptr->location.mapGroup == MAP_GROUP(HOLLOW_HILL)
        && gSaveBlock1Ptr->location.mapNum == MAP_NUM(HOLLOW_HILL);
}

// sine of an angle in 1/1024ths of a turn, Q8 (256 = 1), interpolated between the 256-step table's entries
static s32 Sin1024(u32 a)
{
    u32 i = (a >> 2) & 0xFF, f = a & 3;
    return (gSineTable[i] * (4 - f) + gSineTable[(i + 1) & 0xFF] * f) / 4;
}

static void SpriteCB_KnollCloud(struct Sprite *sprite)
{
    s32 sx, sy;
    if (sprite->sSlot < NUM_RIM)
    {
        u32 i = (sprite->sSlot * PATH_LEN / NUM_RIM + sKnollCloudPhase * PATH_LEN / LAP_FRAMES) % PATH_LEN;
        sprite->x2 = sKnollCloudPath[i][0];
        sprite->y2 = sKnollCloudPath[i][1];
    }
    else
    {
        u32 a = ((sprite->sSlot - NUM_RIM) * 1024 / NUM_INNER + sKnollCloudPhase * 1024 / LAP_FRAMES) & 1023;
        sprite->x2 = (INNER_RX * Sin1024(a + 256)) / 256;
        sprite->y2 = INNER_CY + (INNER_RY * Sin1024(a)) / 256;
    }
    sprite->subpriority = 240 - (sprite->y2 + 128) / 8;           // (the player and people in front; nearer billows over far)
    sx = sprite->x + sprite->x2 + gSpriteCoordOffsetX;
    sy = sprite->y + sprite->y2 + gSpriteCoordOffsetY;
    sprite->invisible = (sx < -40 || sx > DISPLAY_WIDTH + 40 || sy < -24 || sy > DISPLAY_HEIGHT + 24);
}

static void CreateKnollCloud(void)
{
    u32 n;
    s16 x = CENTRE_X, y = CENTRE_Y;
    LoadSpriteSheet(&sKnollCloudSheet);
    LoadSpritePalette(&sKnollCloudPalette);
    // (not passed through the weather's palette blend: the fog would wash it to its own pale green)
    SetSpritePosToOffsetMapCoords(&x, &y, CENTRE_DX, CENTRE_DY);
    for (n = 0; n < NUM_CLOUDS; n++)
    {
        u8 id = CreateSprite(&sKnollCloudTemplate, x, y, 240);
        sKnollCloudIds[n] = id;
        if (id == MAX_SPRITES)
            continue;
        gSprites[id].coordOffsetEnabled = TRUE;
        gSprites[id].sSlot = n;
        StartSpriteAnim(&gSprites[id], n % 4);
        SpriteCB_KnollCloud(&gSprites[id]);
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
        if (++sKnollCloudPhase >= LAP_FRAMES)
            sKnollCloudPhase = 0;
        // the cloud and the fog together need more sprite time on a line than Emerald's field leaves (it gives the
        // H-blank to OAM access, which nothing on this map uses): give it back to the sprites while here
        if (GetGpuReg(REG_OFFSET_DISPCNT) & DISPCNT_HBLANK_INTERVAL)
            ClearGpuRegBits(REG_OFFSET_DISPCNT, DISPCNT_HBLANK_INTERVAL);
    }
    else if (loaded)
    {
        DestroyKnollCloud();
        SetGpuRegBits(REG_OFFSET_DISPCNT, DISPCNT_HBLANK_INTERVAL);
    }
}
