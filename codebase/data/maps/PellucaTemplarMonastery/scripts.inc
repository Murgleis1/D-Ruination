# 1 "data/maps/PellucaTemplarMonastery/scripts.pory"

# 2 "data/maps/PellucaTemplarMonastery/scripts.pory"
    .set LOCALID_DRM_EDEN,    1
# 3 "data/maps/PellucaTemplarMonastery/scripts.pory"
    .set LOCALID_DRM_CADMUS,  2
# 4 "data/maps/PellucaTemplarMonastery/scripts.pory"
    .set LOCALID_DRM_TEMPLAR, 3

PellucaTemplarMonastery_MapScripts::
# 13 "data/maps/PellucaTemplarMonastery/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaTemplarMonastery_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaTemplarMonastery_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 14 "data/maps/PellucaTemplarMonastery/scripts.pory"
	map_script_2 VAR_UNUSED_0x40A1, 2, DR_Monastery_Cell
	.2byte 0


DR_Monastery_Cell::
# 19 "data/maps/PellucaTemplarMonastery/scripts.pory"
	lockall
# 20 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Monastery_Cell_Movement_0
# 21 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 22 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 30
# 23 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_0
# 24 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 25 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_1
# 26 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_2
# 27 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 28 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_3
# 29 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_4
# 30 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 31 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 32 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_1
# 33 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_5
# 34 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 35 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_6
# 36 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 37 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 38 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_1
# 39 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_7
# 40 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 41 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_8
# 42 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 43 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_9
# 44 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_10
# 45 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 46 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_11
# 47 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 48 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_12
# 49 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 50 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 51 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 40
# 52 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 53 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_13
# 54 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 55 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 56 "data/maps/PellucaTemplarMonastery/scripts.pory"
	applymovement LOCALID_DRM_TEMPLAR, DR_Monastery_Cell_Movement_1
# 57 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitmovement 0
# 58 "data/maps/PellucaTemplarMonastery/scripts.pory"
	speakername DR_Monastery_Cell_Text_1
# 59 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_14
# 60 "data/maps/PellucaTemplarMonastery/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 61 "data/maps/PellucaTemplarMonastery/scripts.pory"
	msgbox DR_Monastery_Cell_Text_15
# 62 "data/maps/PellucaTemplarMonastery/scripts.pory"
	hideportrait
# 63 "data/maps/PellucaTemplarMonastery/scripts.pory"
	closemessage
# 64 "data/maps/PellucaTemplarMonastery/scripts.pory"
	delay 20
# 65 "data/maps/PellucaTemplarMonastery/scripts.pory"
	fadescreen FADE_TO_BLACK
# 66 "data/maps/PellucaTemplarMonastery/scripts.pory"
	setvar VAR_UNUSED_0x40A1, 3
# 67 "data/maps/PellucaTemplarMonastery/scripts.pory"
	warp MAP_PELLUCA_UMBRA_LAB, 5, 11
# 68 "data/maps/PellucaTemplarMonastery/scripts.pory"
	waitstate
# 69 "data/maps/PellucaTemplarMonastery/scripts.pory"
	releaseall
	end


# 20 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_0:
# 20 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_up
	step_end

# 56 "data/maps/PellucaTemplarMonastery/scripts.pory"
DR_Monastery_Cell_Movement_1:
# 56 "data/maps/PellucaTemplarMonastery/scripts.pory"
	face_left
	step_end

DR_Monastery_Cell_Text_0:
# 23 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Later, in a holding cell beneath the\n"
	.string "Templar monastery.$"

DR_Monastery_Cell_Text_1:
# 25 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Templar$"

DR_Monastery_Cell_Text_2:
# 26 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Name.$"

DR_Monastery_Cell_Text_3:
# 28 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Thief$"

DR_Monastery_Cell_Text_4:
# 29 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Eden.$"

DR_Monastery_Cell_Text_5:
# 33 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Eden of where?$"

DR_Monastery_Cell_Text_6:
# 35 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Of here, apparently.$"

DR_Monastery_Cell_Text_7:
# 39 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "The Pokémon you took will stay in the\n"
	.string "Order's keeping.$"

DR_Monastery_Cell_Text_8:
# 41 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "For now.$"

DR_Monastery_Cell_Text_9:
# 43 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Nomad Alban$"

DR_Monastery_Cell_Text_10:
# 44 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Who sent you?$"

DR_Monastery_Cell_Text_11:
# 46 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Nobody sends me anywhere. I go where\n"
	.string "the good things are.$"

DR_Monastery_Cell_Text_12:
# 48 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Your little one did all the work back\n"
	.string "there, you know. And you never said a\l"
	.string "word to it. Just orders.$"

DR_Monastery_Cell_Text_13:
# 53 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Just saying.$"

DR_Monastery_Cell_Text_14:
# 59 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Vizier. Rainhawk. If you would leave her\n"
	.string "with me.$"

DR_Monastery_Cell_Text_15:
# 61 "data/maps/PellucaTemplarMonastery/scripts.pory"
	.string "Of course. Rainhawk, with me.$"
