#include "global.h"
#include "palette.h"
#include "event_object_movement.h"
#include "naming_screen.h"
#include "overworld.h"
#include "field_screen_effect.h"
#include "constants/event_objects.h"
#include "constants/rgb.h"
#include "constants/characters.h"
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
// The prince's name defaults to Osrid (bible 16.2 Beat 1: diegetic signature, default Osrid, editable).
static const u8 sText_DefaultPrinceName[] = _("Osrid");

void DrDoPlayerNaming(void)
{
    if (gSaveBlock2Ptr->playerName[0] == EOS)
        StringCopy(gSaveBlock2Ptr->playerName, sText_DefaultPrinceName);
    DoNamingScreen(NAMING_SCREEN_PLAYER, gSaveBlock2Ptr->playerName,
                   gSaveBlock2Ptr->playerGender, 0, 0, CB2_ReturnToFieldContinueScript);
}

static u8 sOsridNameplate[24];

// Private scenes: set the speaker label to the name the player signed with (cold-open reply,
// talks alone with Cadmus).
// Later covers (e.g. Nomad Alban) set their own nameplate.
void DrSetPrinceNameplate(void)
{
    if (gSaveBlock2Ptr->playerName[0] == EOS)   // signed with nothing: he is still Osrid
        StringCopy(gSaveBlock2Ptr->playerName, sText_DefaultPrinceName);
    // In private his label is simply the name the player signed with (user 2026-11-18);
    // in public scenes the scripts use the cover label "Nomad" instead.
    StringCopy(sOsridNameplate, gSaveBlock2Ptr->playerName);
    SetSpeakerName(sOsridNameplate);
}

// Chapter 1 harbor arrival: Cadmus speaks under his own name, replacing the
// private-name label that the cold open leaves set.
static const u8 sText_Cadmus[] = _("Cadmus");
static u8 sCadmusNameplate[24];
void DrSetCadmusNameplate(void)
{
    StringCopy(sCadmusNameplate, sText_Cadmus);
    SetSpeakerName(sCadmusNameplate);
}
