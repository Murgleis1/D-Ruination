@ ===========================================================================
@ Dreamstone Ruination - reusable "shiny-tease" helper (bible S16.5)
@
@ At a scripted egg/encounter the player is asked whether the Pokemon "seems
@ oddly colored - shining, or a trick of the light?". Answer YES -> the next
@ wild/gift Pokemon is guaranteed shiny; NO -> normal. Used by the Burglar Egg,
@ the Fisherman's Wimpod, and (later) the Trial-4 Joustroll egg.
@
@ Usage from any quest script:
@     call DrShinyTease_Ask          @ asks; on YES sets FLAG_FORCE_SHINY
@     giveegg SPECIES_IMPIDIMP       @ or givemon / setwildbattle -> forced shiny if the flag is set
@     clearflag FLAG_FORCE_SHINY     @ ALWAYS clear afterwards
@
@ FLAG_FORCE_SHINY is wired to P_FLAG_FORCE_SHINY, which the mon generator honors
@ for both wild and gift Pokemon.
@ ===========================================================================

DrShinyTease_Ask::
	msgbox DrShinyTease_Text_Ask, MSGBOX_YESNO
	compare VAR_RESULT, YES
	goto_if_eq DrShinyTease_SetShiny
	return

DrShinyTease_SetShiny::
	setflag FLAG_FORCE_SHINY
	return

DrShinyTease_Text_Ask:
	.string "It looks oddly colored…\n"
	.string "Is it shining, or a trick of the light?$"
