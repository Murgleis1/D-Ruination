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
	.string "you paid the price for his witless folly.$"

PellucaReflection_Cutscene_Text_2:
# 25 "data/maps/PellucaReflection/scripts.pory"
	.string "The Commander has since been invited\n"
	.string "to explain his excruciatingly poor\l"
	.string "judgement to people who outrank us\l"
	.string "both. He will be explaining it for some\l"
	.string "time, at the bottom of a cell that has\l"
	.string "never seen the light of day.$"

PellucaReflection_Cutscene_Text_3:
# 27 "data/maps/PellucaReflection/scripts.pory"
	.string "I learned that the army gifted you a\n"
	.string "mending mask from Athanto while your\l"
	.string "burns heal. These masks hasten healing\l"
	.string "and ward off evil. In most lands, such a\l"
	.string "rare artifact is worth more than a\l"
	.string "nobleman's estate, so expect a few\l"
	.string "stares.\p"
	.string "I have a feeling it will help you in the\n"
	.string "long term, so wear it well.\p"
	.string "Your discharge has been signed, with\n"
	.string "honors. You earned the rank of Rainhawk\l"
	.string "partly as a result of what happened\l"
	.string "during the Sevii campaign, and to reach\l"
	.string "it at your age is an amazing\l"
	.string "achievement, whatever the surrounding\l"
	.string "circumstances.\p"
	.string "In any case, effective the day you\n"
	.string "receive this letter, you will serve\l"
	.string "directly under me in the Office of the\l"
	.string "Vizier of Education.$"

PellucaReflection_Cutscene_Text_4:
# 28 "data/maps/PellucaReflection/scripts.pory"
	.string "With that said, here are your immediate\n"
	.string "orders.\p"
	.string "There is a ship called the Pale Veluza\n"
	.string "that waits in the southern harbor, not\l"
	.string "far from your location. Her captain\l"
	.string "asks no questions, which is exactly why\l"
	.string "I hired them.\p"
	.string "Give your written reply and\n"
	.string "acknowledgement of this letter to the\l"
	.string "Templar chaplain at your barracks. It\l"
	.string "will reach me quickly.\p"
	.string "Sign it with the name you were born\n"
	.string "with, not the one I gave you a decade\l"
	.string "ago, and I will know it is truly you.$"

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
	.string "Received and acknowledged. I will be\n"
	.string "aboard the Veluza when she sails.\p"
	.string "It...will be good to be home again.$"

PellucaReflection_Cutscene_Text_8:
# 41 "data/maps/PellucaReflection/scripts.pory"
	.string "You hold the letter over the lamp until\n"
	.string "there is nothing left to read.$"
