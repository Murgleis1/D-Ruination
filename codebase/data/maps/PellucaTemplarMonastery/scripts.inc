# 1 "data/maps/PellucaTemplarMonastery/scripts.pory"

# 2 "data/maps/PellucaTemplarMonastery/scripts.pory"
    .set LOCALID_DRM_EDEN,    1
# 3 "data/maps/PellucaTemplarMonastery/scripts.pory"
    .set LOCALID_DRM_CADMUS,  2
# 4 "data/maps/PellucaTemplarMonastery/scripts.pory"
    .set LOCALID_DRM_TEMPLAR, 3

PellucaTemplarMonastery_MapScripts::
# 16 "data/maps/PellucaTemplarMonastery/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaTemplarMonastery_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaTemplarMonastery_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 17 "data/maps/PellucaTemplarMonastery/scripts.pory"
	map_script_2 VAR_UNUSED_0x40A1, 2, DR_Monastery_Cell
	.2byte 0


DR_Monastery_Cell::
# 22 "data/maps/PellucaTemplarMonastery/scripts.pory"
	lockall
# 23 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Monastery_Cell_Movement_0
# 24 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 25 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 30
# 26 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_0
# 27 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 28 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_1
# 29 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_2
# 30 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 31 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_3
# 32 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_4
# 33 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 34 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 35 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_1
# 36 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_5
# 37 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 38 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_6
# 39 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 40 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 41 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_1
# 42 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_7
# 43 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 44 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_8
# 45 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 46 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_9
# 47 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 48 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_10
# 49 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 50 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 51 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_11
# 52 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 53 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 54 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_12
# 55 "data/maps/PellucaTemplarMonastery/scripts.pory"
	goto_if_set FLAG_DR_LOST_TO_EDEN_LAB, DR_Monastery_Cell_2
# 67 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 68 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_16
# 69 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 70 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 71 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_14
# 72 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 73 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 20
# 74 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 75 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_17
DR_Monastery_Cell_1:
# 77 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 78 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 79 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement LOCALID_DRM_TEMPLAR, DR_Monastery_Cell_Movement_1
# 80 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 81 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_1
# 82 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_18
# 83 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 84 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_19
# 85 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 86 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 87 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement LOCALID_DRM_CADMUS, DR_Monastery_Cell_Movement_2
# 88 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Monastery_Cell_Movement_2
# 89 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 90 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 16
# 91 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 92 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_20
# 93 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_21
# 94 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 95 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 96 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Monastery_Cell_Movement_0
# 97 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 98 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 16
# 99 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 100 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_22
# 101 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_23
# 102 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 103 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 104 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement LOCALID_DRM_CADMUS, DR_Monastery_Cell_Movement_3
# 105 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Monastery_Cell_Movement_4
# 106 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 107 "data/maps/PellucaTemplarMonastery/scripts.pory"
	fadescreen FADE_TO_BLACK
# 108 "data/maps/PellucaTemplarMonastery/scripts.pory"
	setvar VAR_UNUSED_0x40A1, 3
# 109 "data/maps/PellucaTemplarMonastery/scripts.pory"
	warp MAP_PELLUCA_UMBRA_LAB, 9, 9
# 110 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitstate
# 111 "data/maps/PellucaTemplarMonastery/scripts.pory"
	releaseall
	end

DR_Monastery_Cell_2:
# 57 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 58 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_13
# 59 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 60 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 61 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_14
# 62 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 63 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 20
# 64 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 65 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_15
	goto DR_Monastery_Cell_1


# 23 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_0:
# 23 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_up
	step_end

# 79 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_1:
# 79 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_left
	step_end

# 87 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_2:
# 87 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_down
	step_end

# 104 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_3:
# 104 "data/maps/PellucaTemplarMonastery/scripts.pory"
	walk_down
# 104 "data/maps/PellucaTemplarMonastery/scripts.pory"
	walk_down
	step_end

# 105 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_4:
# 105 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_down
# 105 "data/maps/PellucaTemplarMonastery/scripts.pory"
	walk_down
# 105 "data/maps/PellucaTemplarMonastery/scripts.pory"
	walk_down
	step_end

DR_Monastery_Cell_Text_0:
# 26 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Later, in a holding cell beneath the\n"
	.string "Templar monastery.$"

DR_Monastery_Cell_Text_1:
# 28 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Templar$"

DR_Monastery_Cell_Text_2:
# 29 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "State your name.$"

DR_Monastery_Cell_Text_3:
# 31 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Thief$"

DR_Monastery_Cell_Text_4:
# 32 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "...Eden.$"

DR_Monastery_Cell_Text_5:
# 36 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Eden of where?$"

DR_Monastery_Cell_Text_6:
# 38 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Of here, apparently. Lovely view.$"

DR_Monastery_Cell_Text_7:
# 42 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "The Pokémon you stole will remain in the\n"
	.string "Order's keeping.$"

DR_Monastery_Cell_Text_8:
# 44 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "For now.$"

DR_Monastery_Cell_Text_9:
# 46 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Who sent you?$"

DR_Monastery_Cell_Text_10:
# 48 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Nobody you'd want to meet, Vizier Umbra.\n"
	.string "And nobody who'll leave me down here for\l"
	.string "long.$"

DR_Monastery_Cell_Text_11:
# 51 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "She glances at the bars, then away.$"

DR_Monastery_Cell_Text_12:
# 54 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "...They told me it'd be the Vizier and an\n"
	.string "empty lab. Nobody said a word about a\l"
	.string "Rainhawk.$"

DR_Monastery_Cell_Text_13:
# 58 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "You fought like a soldier, Nomad Alban.\n"
	.string "All orders, not one word to that little\l"
	.string "partner of yours. It tried its best\l"
	.string "anyway.$"

DR_Monastery_Cell_Text_14:
# 61 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "A pause.$"

DR_Monastery_Cell_Text_15:
# 65 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Just saying... it'll be something to see,\n"
	.string "the day the two of you actually fight\l"
	.string "together. I mean it.$"

DR_Monastery_Cell_Text_16:
# 68 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "You really did fight well, Nomad Alban.\n"
	.string "Your little partner there beat Pilfer to\l"
	.string "a pulp, and yet you never said one word\l"
	.string "to it. Just gestures.$"

DR_Monastery_Cell_Text_17:
# 75 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Just saying... that's pretty amazing. I\n"
	.string "mean it.$"

DR_Monastery_Cell_Text_18:
# 82 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Vizier. Rainhawk. I must ask you to\n"
	.string "leave her with me now. She is trying to\l"
	.string "buy time... though for what reason, I do\l"
	.string "not know.$"

DR_Monastery_Cell_Text_19:
# 84 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Of course. Come, Rainhawk. We have much\n"
	.string "to discuss.$"

DR_Monastery_Cell_Text_20:
# 92 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Eden$"

DR_Monastery_Cell_Text_21:
# 93 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "I'll be seeing you again, Rainhawk. When\n"
	.string "I make a promise, I keep it.$"

DR_Monastery_Cell_Text_22:
# 100 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Nomad Alban$"

DR_Monastery_Cell_Text_23:
# 101 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "If the fates allow it, I'll welcome it...\n"
	.string "Eden.$"
