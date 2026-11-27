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
	message TemplarCitadelTavern_EventScript_Barkeep_Text_0
# 14 "data/maps/TemplarCitadelTavern/scripts.pory"
	waitmessage
# 15 "data/maps/TemplarCitadelTavern/scripts.pory"
	pokemart TemplarCitadelTavern_Stock
# 16 "data/maps/TemplarCitadelTavern/scripts.pory"
	msgbox TemplarCitadelTavern_EventScript_Barkeep_Text_1
# 17 "data/maps/TemplarCitadelTavern/scripts.pory"
	closemessage
# 18 "data/maps/TemplarCitadelTavern/scripts.pory"
	release
	end


	.align 2
# 22 "data/maps/TemplarCitadelTavern/scripts.pory"
TemplarCitadelTavern_Stock:
# 23 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_POTION
# 24 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_SUPER_POTION
# 25 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_POKE_BALL
# 26 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_GREAT_BALL
# 27 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_ANTIDOTE
# 28 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_PARALYZE_HEAL
# 29 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_BURN_HEAL
# 30 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_ICE_HEAL
# 31 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_AWAKENING
# 32 "data/maps/TemplarCitadelTavern/scripts.pory"
	.2byte ITEM_REPEL
	.2byte ITEM_NONE

TemplarCitadelTavern_EventScript_Barkeep_Text_0:
# 13 "data/maps/TemplarCitadelTavern/scripts.pory"
	.string "Mountain air works up a hunger. Need\n"
	.string "anything for the road?$"

TemplarCitadelTavern_EventScript_Barkeep_Text_1:
# 16 "data/maps/TemplarCitadelTavern/scripts.pory"
	.string "Arceus keep you.$"
