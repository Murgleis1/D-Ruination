#include "global.h"
#include "palette.h"
#include "event_object_movement.h"
#include "naming_screen.h"
#include "overworld.h"
#include "field_screen_effect.h"
#include "constants/event_objects.h"
#include "constants/rgb.h"

// (unused now that the black-palette tileset handles the void; harmless)
void DrReflectionMakeBlack(void)
{
    CpuFill16(RGB_BLACK, &gPlttBufferUnfaded[BG_PLTT_ID(0)], 13 * PLTT_SIZE_4BPP);
    CpuFill16(RGB_BLACK, &gPlttBufferFaded[BG_PLTT_ID(0)], 13 * PLTT_SIZE_4BPP);
}

// Cold-open cutscene: make the player character appear as the masked Osrid.
void DrSetPlayerOsridSprite(void)
{
    ObjectEventSetGraphicsId(&gObjectEvents[gPlayerAvatar.objectEventId], OBJ_EVENT_GFX_OSRID);
}

// Cold-open cutscene: open the player naming screen; the map script resumes after.
void DrDoPlayerNaming(void)
{
    DoNamingScreen(NAMING_SCREEN_PLAYER, gSaveBlock2Ptr->playerName,
                   gSaveBlock2Ptr->playerGender, 0, 0, CB2_ReturnToFieldContinueScript);
}
