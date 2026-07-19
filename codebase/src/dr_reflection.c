#include "global.h"
#include "palette.h"
#include "constants/rgb.h"

// Cold open reflection scene (PellucaReflection).
// Blacks out the map's tileset BG palettes so the scene reads as a pure-black void.
// The pond metatile keeps its MB_POND_WATER behavior, so the standing character's
// reflection still renders on the now-black water -- exactly the reference look.
// BG palettes 0-12 are the two tilesets; 13-15 are left alone for text/UI.
void DrReflectionMakeBlack(void)
{
    CpuFill16(RGB_BLACK, &gPlttBufferUnfaded[BG_PLTT_ID(0)], 13 * PLTT_SIZE_4BPP);
    CpuFill16(RGB_BLACK, &gPlttBufferFaded[BG_PLTT_ID(0)], 13 * PLTT_SIZE_4BPP);
}
