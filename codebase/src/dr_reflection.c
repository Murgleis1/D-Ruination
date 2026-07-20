#include "global.h"
#include "palette.h"
#include "event_object_movement.h"
#include "naming_screen.h"
#include "overworld.h"
#include "field_screen_effect.h"
#include "constants/event_objects.h"
#include "constants/rgb.h"
#include "string_util.h"
#include "field_message_box.h"

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

static const u8 sText_Prince[] = _("Prince ");
static u8 sOsridNameplate[24];

// Cold-open cutscene: set the speaker nameplate to "Prince <chosen name>" for
// Osrid's reply, resolving "Prince ???" into the name the player just entered.
// Later covers (e.g. Nomad Alban) set their own nameplate.
void DrSetPrinceNameplate(void)
{
    StringCopy(sOsridNameplate, sText_Prince);
    StringAppend(sOsridNameplate, gSaveBlock2Ptr->playerName);
    SetSpeakerName(sOsridNameplate);
}
