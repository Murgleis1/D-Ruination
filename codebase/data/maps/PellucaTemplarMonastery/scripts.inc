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
	speakername DR_Monastery_Cell_Text_0
# 27 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_1
# 28 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 29 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_2
# 30 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_3
# 31 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 32 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 33 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_0
# 34 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_4
# 35 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 36 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_5
# 37 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 38 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 39 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_0
# 40 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_6
# 41 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 42 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_7
# 43 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 44 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_8
# 45 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 46 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_9
# 47 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 48 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 49 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement LOCALID_DRM_EDEN, DR_Monastery_Cell_Movement_1
# 50 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 51 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 52 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_10
# 53 "data/maps/PellucaTemplarMonastery/scripts.pory"
	goto_if_set FLAG_DR_LOST_TO_EDEN_LAB, DR_Monastery_Cell_2
# 63 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 64 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_13
# 65 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 66 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 67 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 50
# 68 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 69 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_14
DR_Monastery_Cell_1:
# 71 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 72 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 73 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement LOCALID_DRM_TEMPLAR, DR_Monastery_Cell_Movement_2
# 74 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 75 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_0
# 76 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_15
# 77 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 78 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_16
# 79 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 80 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 81 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement LOCALID_DRM_CADMUS, DR_Monastery_Cell_Movement_3
# 82 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Monastery_Cell_Movement_3
# 83 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 84 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 16
# 85 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 86 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_17
# 87 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_18
# 88 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 89 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 90 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Monastery_Cell_Movement_0
# 91 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 92 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 16
# 93 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 94 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_19
# 95 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_20
# 96 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 97 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 98 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement LOCALID_DRM_CADMUS, DR_Monastery_Cell_Movement_4
# 99 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Monastery_Cell_Movement_5
# 100 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 101 "data/maps/PellucaTemplarMonastery/scripts.pory"
	fadescreen FADE_TO_BLACK
# 102 "data/maps/PellucaTemplarMonastery/scripts.pory"
	setvar VAR_UNUSED_0x40A1, 3
# 103 "data/maps/PellucaTemplarMonastery/scripts.pory"
	warp MAP_PELLUCA_UMBRA_LAB, 9, 9
# 104 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitstate
# 105 "data/maps/PellucaTemplarMonastery/scripts.pory"
	releaseall
	end

DR_Monastery_Cell_2:
# 55 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 56 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_11
# 57 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 58 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 59 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 50
# 60 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 61 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_12
	goto DR_Monastery_Cell_1


# 23 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_0:
# 23 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_up
	step_end

# 49 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_1:
# 49 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_up
# 49 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay_16
# 49 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay_16
# 49 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_down
	step_end

# 73 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_2:
# 73 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_left
	step_end

# 81 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_3:
# 81 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_down
	step_end

# 98 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_4:
# 98 "data/maps/PellucaTemplarMonastery/scripts.pory"
	walk_down
# 98 "data/maps/PellucaTemplarMonastery/scripts.pory"
	walk_down
	step_end

# 99 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_5:
# 99 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_down
# 99 "data/maps/PellucaTemplarMonastery/scripts.pory"
	walk_down
# 99 "data/maps/PellucaTemplarMonastery/scripts.pory"
	walk_down
	step_end

DR_Monastery_Cell_Text_0:
# 26 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Templar$"

DR_Monastery_Cell_Text_1:
# 27 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "State your name.$"

DR_Monastery_Cell_Text_2:
# 29 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Thief$"

DR_Monastery_Cell_Text_3:
# 30 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "...Eden.$"

DR_Monastery_Cell_Text_4:
# 34 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Eden of where?$"

DR_Monastery_Cell_Text_5:
# 36 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Of here, apparently. Lovely view.$"

DR_Monastery_Cell_Text_6:
# 40 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "The Pokémon you stole will remain in the\n"
	.string "Order's keeping.$"

DR_Monastery_Cell_Text_7:
# 42 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "For now.$"

DR_Monastery_Cell_Text_8:
# 44 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Who sent you?$"

DR_Monastery_Cell_Text_9:
# 46 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Nobody you'd want to meet, Vizier Umbra.\n"
	.string "And nobody who'll leave me down here for\l"
	.string "long.$"

DR_Monastery_Cell_Text_10:
# 52 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "...They told me it'd be the Vizier and an\n"
	.string "empty lab. Nobody said a word about a\l"
	.string "Rainhawk.$"

DR_Monastery_Cell_Text_11:
# 56 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "You fought like a soldier, Nomad Alban.\n"
	.string "All orders, not one word to that little\l"
	.string "partner of yours. It tried its best\l"
	.string "anyway.$"

DR_Monastery_Cell_Text_12:
# 61 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Just saying... it'll be something to see,\n"
	.string "the day the two of you actually fight\l"
	.string "together. I mean it.$"

DR_Monastery_Cell_Text_13:
# 64 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "You really did fight well, Nomad Alban.\n"
	.string "Your little partner there beat Pilfer to\l"
	.string "a pulp, and yet you never said one word\l"
	.string "to it. Just gestures.$"

DR_Monastery_Cell_Text_14:
# 69 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Just saying... that's pretty amazing. I\n"
	.string "mean it.$"

DR_Monastery_Cell_Text_15:
# 76 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Vizier. Rainhawk. I must ask you to\n"
	.string "leave her with me now. She is trying to\l"
	.string "buy time... though for what reason, I do\l"
	.string "not know.$"

DR_Monastery_Cell_Text_16:
# 78 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Of course. Come, Rainhawk. We have much\n"
	.string "to discuss.$"

DR_Monastery_Cell_Text_17:
# 86 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Eden$"

DR_Monastery_Cell_Text_18:
# 87 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "I'll be seeing you again, Rainhawk. When\n"
	.string "I make a promise, I keep it.$"

DR_Monastery_Cell_Text_19:
# 94 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "“Nomad”$"

DR_Monastery_Cell_Text_20:
# 95 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "If the fates allow it, I'll welcome it...\n"
	.string "Eden.$"
