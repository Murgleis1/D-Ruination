// Dreamstone Ruination: small helpers for Chapter 1's sidequests (2026-11-27).
#include "global.h"
#include "pokemon.h"
#include "event_data.h"

// The Burglar Egg: the egg the old man gives should hatch during the Pelluca sandbox or on Route 11, not ~2,700 steps
// later. An egg's remaining hatch cycles live in its friendship field (128 steps each: P_EGG_CYCLE_LENGTH is Gen 8+).
// In:  VAR_0x8005 = cycles to leave on it. Sets the last egg in the party (the one just given).
// Out: VAR_RESULT = TRUE if an egg was found in the party (FALSE if it went to the PC: left as it was).
void DrSetLastEggCycles(void)
{
    s32 i;
    u8 cycles = gSpecialVar_0x8005;

    gSpecialVar_Result = FALSE;
    for (i = gPlayerPartyCount - 1; i >= 0; i--)
    {
        if (GetMonData(&gPlayerParty[i], MON_DATA_IS_EGG))
        {
            SetMonData(&gPlayerParty[i], MON_DATA_FRIENDSHIP, &cycles);
            gSpecialVar_Result = TRUE;
            return;
        }
    }
}
