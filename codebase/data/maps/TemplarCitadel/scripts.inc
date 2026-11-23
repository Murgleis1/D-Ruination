TemplarCitadel_MapScripts::
	.byte 0


TemplarCitadel_EventScript_ToRoute13_18::
# 4 "data/maps/TemplarCitadel/scripts.pory"
	setvar VAR_TEMP_1, 1
# 5 "data/maps/TemplarCitadel/scripts.pory"
	warp MAP_ROUTE13, 32, 1
	return


TemplarCitadel_EventScript_ToRoute13_19::
# 9 "data/maps/TemplarCitadel/scripts.pory"
	setvar VAR_TEMP_1, 1
# 10 "data/maps/TemplarCitadel/scripts.pory"
	warp MAP_ROUTE13, 33, 1
	return


TemplarCitadel_EventScript_ToRoute13_20::
# 14 "data/maps/TemplarCitadel/scripts.pory"
	setvar VAR_TEMP_1, 1
# 15 "data/maps/TemplarCitadel/scripts.pory"
	warp MAP_ROUTE13, 34, 1
	return


TemplarCitadel_EventScript_Route15Guard::
# 20 "data/maps/TemplarCitadel/scripts.pory"
	speakername TemplarCitadel_EventScript_Route15Guard_Text_0
# 21 "data/maps/TemplarCitadel/scripts.pory"
	msgbox TemplarCitadel_EventScript_Route15Guard_Text_1, MSGBOX_NPC
	end


TemplarCitadel_EventScript_Route15Guard_Text_0:
# 20 "data/maps/TemplarCitadel/scripts.pory"
	.string "Templar$"

TemplarCitadel_EventScript_Route15Guard_Text_1:
# 21 "data/maps/TemplarCitadel/scripts.pory"
	.string "There's been an incident on Route 15.\n"
	.string "We're observing the situation.\p"
	.string "Until something changes, nobody is\n"
	.string "allowed in or out that way.$"
