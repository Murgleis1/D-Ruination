// Dreamstone Ruination: Tavern Sage services (user design, 2026-11-16).
// Nature change and Apex Fruit ability change, driven from scripts:
//   VAR_0x8004 = party slot (from ChoosePartyMon)
#include "global.h"
#include "pokemon.h"
#include "event_data.h"
#include "string_util.h"
#include "constants/pokemon.h"
#include "constants/abilities.h"

// Menu order the player sees: Attack, Defense, Sp. Atk, Sp. Def, Speed.
static const u8 sMenuStat[5] = {STAT_ATK, STAT_DEF, STAT_SPATK, STAT_SPDEF, STAT_SPEED};

// In:  VAR_0x8004 slot, VAR_0x8005 stat to raise (menu index), VAR_0x8006 stat to lower (menu index).
//      Same index twice = a neutral nature.
// Out: VAR_RESULT = FALSE if the Pokemon already has that nature (nothing changed), TRUE otherwise.
//      gStringVar2 = the new nature's name.
void DrTavernSetNature(void)
{
    struct Pokemon *mon = &gPlayerParty[gSpecialVar_0x8004];
    u8 up, down;
    u32 n, nature = NUM_NATURES;

    gSpecialVar_Result = FALSE;
    if (gSpecialVar_0x8005 >= 5 || gSpecialVar_0x8006 >= 5)
        return;
    up = sMenuStat[gSpecialVar_0x8005];
    down = sMenuStat[gSpecialVar_0x8006];
    for (n = 0; n < NUM_NATURES; n++)
    {
        if (gNaturesInfo[n].statUp == up && gNaturesInfo[n].statDown == down)
        {
            nature = n;
            break;
        }
    }
    if (nature == NUM_NATURES)
        return;
    StringCopy(gStringVar2, gNaturesInfo[nature].name);
    if (GetMonData(mon, MON_DATA_HIDDEN_NATURE) == nature)
        return;
    SetMonData(mon, MON_DATA_HIDDEN_NATURE, &nature);
    CalculateMonStats(mon);
    gSpecialVar_Result = TRUE;
}

// Buffers the species' abilities other than the current one into gStringVar1..3 for a menu.
// Out: VAR_0x8005 = how many choices; VAR_0x8007/8/9 = the ability slot behind each choice.
void DrTavernBufferAbilityChoices(void)
{
    struct Pokemon *mon = &gPlayerParty[gSpecialVar_0x8004];
    u16 species = GetMonData(mon, MON_DATA_SPECIES);
    u16 current = GetMonAbility(mon);
    u8 *bufs[3] = {gStringVar1, gStringVar2, gStringVar3};
    u16 *slots[3] = {&gSpecialVar_0x8007, &gSpecialVar_0x8008, &gSpecialVar_0x8009};
    u16 seen[NUM_ABILITY_SLOTS];
    u32 i, j, count = 0;

    for (i = 0; i < NUM_ABILITY_SLOTS && count < 3; i++)
    {
        u16 ability = gSpeciesInfo[species].abilities[i];
        bool32 dup = FALSE;
        if (ability == ABILITY_NONE || ability == current)
            continue;
        for (j = 0; j < count; j++)
            if (seen[j] == ability)
                dup = TRUE;
        if (dup)
            continue;
        seen[count] = ability;
        StringCopy(bufs[count], gAbilitiesInfo[ability].name);
        *slots[count] = i;
        count++;
    }
    gSpecialVar_0x8005 = count;
}

// In: VAR_0x8004 slot, VAR_0x8006 ability slot (0-2). Out: gStringVar2 = the new ability's name.
void DrTavernSetAbilitySlot(void)
{
    struct Pokemon *mon = &gPlayerParty[gSpecialVar_0x8004];
    u8 slot = gSpecialVar_0x8006;
    if (slot >= NUM_ABILITY_SLOTS)
        return;
    SetMonData(mon, MON_DATA_ABILITY_NUM, &slot);
    StringCopy(gStringVar2, gAbilitiesInfo[GetMonAbility(mon)].name);
}
