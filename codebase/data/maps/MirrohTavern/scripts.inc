MirrohTavern_MapScripts::
# 5 "data/maps/MirrohTavern/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, MirrohTavern_MapScripts_MAP_SCRIPT_ON_TRANSITION
	.byte 0

MirrohTavern_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 6 "data/maps/MirrohTavern/scripts.pory"
	setrespawn HEAL_LOCATION_MIRROH
	return


MirrohTavern_EventScript_Barkeep::
# 11 "data/maps/MirrohTavern/scripts.pory"
	lock
# 12 "data/maps/MirrohTavern/scripts.pory"
	faceplayer
# 13 "data/maps/MirrohTavern/scripts.pory"
	speakername MirrohTavern_EventScript_Barkeep_Text_0
# 14 "data/maps/MirrohTavern/scripts.pory"
	message MirrohTavern_EventScript_Barkeep_Text_1
# 15 "data/maps/MirrohTavern/scripts.pory"
	waitmessage
# 16 "data/maps/MirrohTavern/scripts.pory"
	pokemart MirrohTavern_Stock
# 17 "data/maps/MirrohTavern/scripts.pory"
	speakername MirrohTavern_EventScript_Barkeep_Text_0
# 18 "data/maps/MirrohTavern/scripts.pory"
	msgbox MirrohTavern_EventScript_Barkeep_Text_2
# 19 "data/maps/MirrohTavern/scripts.pory"
	closemessage
# 20 "data/maps/MirrohTavern/scripts.pory"
	release
	end


	.align 2
# 24 "data/maps/MirrohTavern/scripts.pory"
MirrohTavern_Stock:
# 25 "data/maps/MirrohTavern/scripts.pory"
	.2byte ITEM_POTION
# 26 "data/maps/MirrohTavern/scripts.pory"
	.2byte ITEM_SUPER_POTION
# 27 "data/maps/MirrohTavern/scripts.pory"
	.2byte ITEM_POKE_BALL
# 28 "data/maps/MirrohTavern/scripts.pory"
	.2byte ITEM_ANTIDOTE
# 29 "data/maps/MirrohTavern/scripts.pory"
	.2byte ITEM_PARALYZE_HEAL
# 30 "data/maps/MirrohTavern/scripts.pory"
	.2byte ITEM_BURN_HEAL
# 31 "data/maps/MirrohTavern/scripts.pory"
	.2byte ITEM_ICE_HEAL
# 32 "data/maps/MirrohTavern/scripts.pory"
	.2byte ITEM_AWAKENING
	.2byte ITEM_NONE

MirrohTavern_EventScript_Barkeep_Text_0:
# 13 "data/maps/MirrohTavern/scripts.pory"
	.string "Barkeep$"

MirrohTavern_EventScript_Barkeep_Text_1:
# 14 "data/maps/MirrohTavern/scripts.pory"
	.string "Cold out there. Stock up before you go.$"

MirrohTavern_EventScript_Barkeep_Text_2:
# 18 "data/maps/MirrohTavern/scripts.pory"
	.string "Keep warm.$"
