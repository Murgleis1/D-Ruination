PellucaReflection_MapScripts::
# 9 "data/maps/PellucaReflection/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaReflection_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaReflection_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 10 "data/maps/PellucaReflection/scripts.pory"
	map_script_2 VAR_TEMP_1, 0, PellucaReflection_Cutscene
	.2byte 0


PellucaReflection_Cutscene::
# 15 "data/maps/PellucaReflection/scripts.pory"
	lockall
# 16 "data/maps/PellucaReflection/scripts.pory"
	setvar VAR_TEMP_1, 1
# 17 "data/maps/PellucaReflection/scripts.pory"
	special DrSetPlayerOsridSprite
# 18 "data/maps/PellucaReflection/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaReflection_Cutscene_Movement_0
# 19 "data/maps/PellucaReflection/scripts.pory"
	waitmovement 0
# 20 "data/maps/PellucaReflection/scripts.pory"
	delay 40
# 21 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_0
# 22 "data/maps/PellucaReflection/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 23 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_1
# 24 "data/maps/PellucaReflection/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 25 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_2
# 26 "data/maps/PellucaReflection/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 27 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_3
# 28 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_4
# 29 "data/maps/PellucaReflection/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 30 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_5
# 31 "data/maps/PellucaReflection/scripts.pory"
	hideportrait
# 32 "data/maps/PellucaReflection/scripts.pory"
	closemessage
# 33 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_6
# 34 "data/maps/PellucaReflection/scripts.pory"
	special DrDoPlayerNaming
# 35 "data/maps/PellucaReflection/scripts.pory"
	waitstate
# 36 "data/maps/PellucaReflection/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 37 "data/maps/PellucaReflection/scripts.pory"
	special DrSetPrinceNameplate
# 38 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_7
# 39 "data/maps/PellucaReflection/scripts.pory"
	hideportrait
# 40 "data/maps/PellucaReflection/scripts.pory"
	closemessage
# 41 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_8
# 42 "data/maps/PellucaReflection/scripts.pory"
	delay 40
# 43 "data/maps/PellucaReflection/scripts.pory"
	fadescreen FADE_TO_BLACK
# 44 "data/maps/PellucaReflection/scripts.pory"
	setvar VAR_UNUSED_0x404E, 1
# 45 "data/maps/PellucaReflection/scripts.pory"
	warp MAP_PELLUCA_CITY, 44, 52
# 46 "data/maps/PellucaReflection/scripts.pory"
	waitstate
# 47 "data/maps/PellucaReflection/scripts.pory"
	releaseall
	end


# 18 "data/maps/PellucaReflection/scripts.pory"
PellucaReflection_Cutscene_Movement_0:
# 18 "data/maps/PellucaReflection/scripts.pory"
	face_down
	step_end

PellucaReflection_Cutscene_Text_0:
# 21 "data/maps/PellucaReflection/scripts.pory"
	.string "A letter has come for you. The seal is\n"
	.string "plain wax, pressed without a crest.$"

PellucaReflection_Cutscene_Text_1:
# 23 "data/maps/PellucaReflection/scripts.pory"
	.string "Rainhawk Alban,\p"
	.string "The surgeon's report from Sevii reached\n"
	.string "my desk a week before your commander's\l"
	.string "did. A commander proud of his decisions\l"
	.string "does not take a week to report them.\p"
	.string "Burns to the face and neck, taken\n"
	.string "holding a beach that should have had\l"
	.string "twice the men on it. Commander Surge\l"
	.string "split his forces across two fronts, and\l"
	.string "you paid for his arithmetic.$"

PellucaReflection_Cutscene_Text_2:
# 25 "data/maps/PellucaReflection/scripts.pory"
	.string "The Commander has since been invited\n"
	.string "to explain that arithmetic to people\l"
	.string "who outrank us both. He will be\l"
	.string "explaining it for some time.$"

PellucaReflection_Cutscene_Text_3:
# 27 "data/maps/PellucaReflection/scripts.pory"
	.string "The army saw fit to give you a mending\n"
	.string "mask from Athanto while the burns heal.\l"
	.string "They are made to hasten healing and\l"
	.string "keep evil at bay, and in most lands they\l"
	.string "are worth more than a house, so expect\l"
	.string "to be stared at. Wear it as long as you\l"
	.string "need to.\p"
	.string "Your discharge is signed, with honors.\n"
	.string "You earned the rank of Rainhawk long\l"
	.string "before Sevii, and you keep it. From the\l"
	.string "day this reaches you, you serve under\l"
	.string "me, in the office of the Vizier of\l"
	.string "Education.$"

PellucaReflection_Cutscene_Text_4:
# 28 "data/maps/PellucaReflection/scripts.pory"
	.string "A ship called the Pale Veluza waits in\n"
	.string "the southern harbor. Her captain asks\l"
	.string "no questions, which is exactly why I\l"
	.string "hired her.\p"
	.string "Give your reply to the Templar chaplain\n"
	.string "at your barracks. It will reach me\l"
	.string "unopened.\p"
	.string "Sign it with the name you were born\n"
	.string "with, not the one I gave you. I would\l"
	.string "know your hand anywhere.$"

PellucaReflection_Cutscene_Text_5:
# 30 "data/maps/PellucaReflection/scripts.pory"
	.string "Then burn this. These days, too many\n"
	.string "people in Cormoria read letters that\l"
	.string "were never meant for them.\p"
	.string "C.$"

PellucaReflection_Cutscene_Text_6:
# 33 "data/maps/PellucaReflection/scripts.pory"
	.string "You take up the pen.$"

PellucaReflection_Cutscene_Text_7:
# 38 "data/maps/PellucaReflection/scripts.pory"
	.string "Received. I will be aboard the Veluza\n"
	.string "when she sails.\p"
	.string "It has been a long time since anyone\n"
	.string "asked me for that name.$"

PellucaReflection_Cutscene_Text_8:
# 41 "data/maps/PellucaReflection/scripts.pory"
	.string "You hold the letter over the lamp until\n"
	.string "there is nothing left to read.$"
