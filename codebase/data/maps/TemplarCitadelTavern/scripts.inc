TemplarCitadelTavern_MapScripts::
# 5 "data/maps/TemplarCitadelTavern/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, TemplarCitadelTavern_MapScripts_MAP_SCRIPT_ON_TRANSITION
	.byte 0

TemplarCitadelTavern_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 6 "data/maps/TemplarCitadelTavern/scripts.pory"
	setrespawn HEAL_LOCATION_TEMPLAR_HQ
	return


TemplarCitadelTavern_EventScript_Barkeep::
# 11 "data/maps/TemplarCitadelTavern/scripts.pory"
	lock
# 12 "data/maps/TemplarCitadelTavern/scripts.pory"
	faceplayer
# 13 "data/maps/TemplarCitadelTavern/scripts.pory"
	speakername TemplarCitadelTavern_EventScript_Barkeep_Text_0
# 14 "data/maps/TemplarCitadelTavern/scripts.pory"
	message TemplarCitadelTavern_EventScript_Barkeep_Text_1
# 15 "data/maps/TemplarCitadelTavern/scripts.pory"
	waitmessage
# 16 "data/maps/TemplarCitadelTavern/scripts.pory"
	pokemart TemplarCitadelTavern_Stock
# 17 "data/maps/TemplarCitadelTavern/scripts.pory"
	speakername TemplarCitadelTavern_EventScript_Barkeep_Text_0
# 18 "data/maps/TemplarCitadelTavern/scripts.pory"
	msgbox TemplarCitadelTavern_EventScript_Barkeep_Text_2
# 19 "data/maps/TemplarCitadelTavern/scripts.pory"
	closemessage
# 20 "data/maps/TemplarCitadelTavern/scripts.pory"
	release
	end


	.align 2
# 24 "data/maps/TemplarCitadelTavern/scripts.pory"
TemplarCitadelTavern_Stock:
# 25 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_POTION
# 26 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_SUPER_POTION
# 27 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_POKE_BALL
# 28 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_GREAT_BALL
# 29 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_ANTIDOTE
# 30 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_PARALYZE_HEAL
# 31 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_BURN_HEAL
# 32 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_ICE_HEAL
# 33 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_AWAKENING
# 34 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_REPEL
	.2byte ITEM_NONE

TemplarCitadelTavern_EventScript_Barkeep_Text_0:
# 13 "data/maps/TemplarCitadelTavern/scripts.pory"
	.string "Barkeep$"

TemplarCitadelTavern_EventScript_Barkeep_Text_1:
# 14 "data/maps/TemplarCitadelTavern/scripts.pory"
	.string "Mountain air works up a hunger. Need\n"
	.string "anything for the road?$"

TemplarCitadelTavern_EventScript_Barkeep_Text_2:
# 18 "data/maps/TemplarCitadelTavern/scripts.pory"
	.string "Arceus keep you.$"
