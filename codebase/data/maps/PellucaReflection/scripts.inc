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
	msgbox PellucaReflection_Cutscene_Text_0, MSGBOX_SIGN
# 23 "data/maps/PellucaReflection/scripts.pory"
	special DrParchmentOn
# 24 "data/maps/PellucaReflection/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 25 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_1
# 26 "data/maps/PellucaReflection/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 27 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_2
# 28 "data/maps/PellucaReflection/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 29 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_3
# 30 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_4
# 31 "data/maps/PellucaReflection/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 32 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_5
# 33 "data/maps/PellucaReflection/scripts.pory"
	hideportrait
# 34 "data/maps/PellucaReflection/scripts.pory"
	closemessage
# 35 "data/maps/PellucaReflection/scripts.pory"
	special DrDoPlayerNaming
# 36 "data/maps/PellucaReflection/scripts.pory"
	waitstate
# 37 "data/maps/PellucaReflection/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 38 "data/maps/PellucaReflection/scripts.pory"
	special DrSetPrinceNameplate
# 39 "data/maps/PellucaReflection/scripts.pory"
	msgbox PellucaReflection_Cutscene_Text_6
# 40 "data/maps/PellucaReflection/scripts.pory"
	hideportrait
# 41 "data/maps/PellucaReflection/scripts.pory"
	closemessage
# 42 "data/maps/PellucaReflection/scripts.pory"
	special DrParchmentOff
# 44 "data/maps/PellucaReflection/scripts.pory"
	delay 30
# 45 "data/maps/PellucaReflection/scripts.pory"
	playse SE_M_EMBER
# 46 "data/maps/PellucaReflection/scripts.pory"
	waitse
# 47 "data/maps/PellucaReflection/scripts.pory"
	delay 40
# 48 "data/maps/PellucaReflection/scripts.pory"
	fadescreen FADE_TO_BLACK
# 49 "data/maps/PellucaReflection/scripts.pory"
	setvar VAR_UNUSED_0x404E, 1
# 50 "data/maps/PellucaReflection/scripts.pory"
	warp MAP_PELLUCA_HARBOUR, 40, 21
# 51 "data/maps/PellucaReflection/scripts.pory"
	waitstate
# 52 "data/maps/PellucaReflection/scripts.pory"
	releaseall
	end


# 18 "data/maps/PellucaReflection/scripts.pory"
PellucaReflection_Cutscene_Movement_0:
# 18 "data/maps/PellucaReflection/scripts.pory"
	face_down
	step_end

PellucaReflection_Cutscene_Text_0:
# 21 "data/maps/PellucaReflection/scripts.pory"
	.string "A sealed letter. Plain wax, no crest.$"

PellucaReflection_Cutscene_Text_1:
# 25 "data/maps/PellucaReflection/scripts.pory"
	.string "Nomad Alban,\p"
	.string "The surgeon's report from Sevii reached\n"
	.string "my desk a week before your commander's\l"
	.string "did. A commander proud of his decisions\l"
	.string "does not take a week to report them.\p"
	.string "Burns to the face and neck, taken\n"
	.string "holding a beach that needed twice the\l"
	.string "men. Commander Surge split his forces\l"
	.string "across two fronts, and you paid for his\l"
	.string "folly.$"

PellucaReflection_Cutscene_Text_2:
# 27 "data/maps/PellucaReflection/scripts.pory"
	.string "The Commander has since been invited\n"
	.string "to explain his judgement to people who\l"
	.string "outrank us both. He will be explaining it\l"
	.string "for some time, from a cell that has\l"
	.string "never seen daylight.$"

PellucaReflection_Cutscene_Text_3:
# 29 "data/maps/PellucaReflection/scripts.pory"
	.string "I am told the army gave you a rare\n"
	.string "mending mask from the Athanto kingdom\l"
	.string "while your burns heal. Such masks\l"
	.string "hasten healing and ward off evil.\l"
	.string "Athanto's enchanters almost never let\l"
	.string "their work leave the kingdom, and one is\l"
	.string "worth more than most noble estates, so\l"
	.string "expect a few stares.\p"
	.string "Wear it well. I suspect it will serve you\n"
	.string "longer than the burns require.\p"
	.string "I am pleased to inform you that, for\n"
	.string "your actions on that beach and in light\l"
	.string "of your injuries, you have been granted\l"
	.string "an honorable discharge from further\l"
	.string "military service, with lifetime benefits.\p"
	.string "You have also been raised to the rank\n"
	.string "of Rainhawk. At twenty, you are the\l"
	.string "youngest in Cormorian history to hold\l"
	.string "it. The rank carries the right to\l"
	.string "challenge the Trials, should you choose\l"
	.string "to, a right the Empire rarely extends\l"
	.string "beyond its noble houses. I suspect you\l"
	.string "will choose to.\p"
	.string "Word of all this has travelled faster\n"
	.string "than any ship. Criers have carried the\l"
	.string "tale of Sevii through every square from\l"
	.string "Silversun to Rivetshore: the beach, the\l"
	.string "burns, and the masked soldier made\l"
	.string "Rainhawk at twenty.\p"
	.string "Notices bearing a likeness of your mask\n"
	.string "hang in half the taverns of the Empire,\l"
	.string "so do not be surprised when strangers\l"
	.string "know you on sight.\p"
	.string "As of the day this letter reaches you,\n"
	.string "you will serve under me in the Ministry\l"
	.string "of Education.$"

PellucaReflection_Cutscene_Text_4:
# 30 "data/maps/PellucaReflection/scripts.pory"
	.string "Your immediate orders are as follows.\n"
	.string "The Pale Veluza waits in the harbor\l"
	.string "south of your barracks. You are to\l"
	.string "board her and return home. She sails for\l"
	.string "Pelluca Valley, where I will meet you at\l"
	.string "the docks.\p"
	.string "Write your reply and leave it with the\n"
	.string "Templar chaplain at your barracks. It\l"
	.string "will reach me quickly. Sign it with the\l"
	.string "name you were born with, not the one I\l"
	.string "gave you a decade ago, and I will know it\l"
	.string "is truly you.$"

PellucaReflection_Cutscene_Text_5:
# 32 "data/maps/PellucaReflection/scripts.pory"
	.string "Then burn this. These days, too many\n"
	.string "people in Cormoria read letters never\l"
	.string "meant for them.\p"
	.string "C.$"

PellucaReflection_Cutscene_Text_6:
# 39 "data/maps/PellucaReflection/scripts.pory"
	.string "Received and acknowledged. I will be\n"
	.string "aboard the Veluza when she sails.\p"
	.string "It... will be good to be home again.$"
