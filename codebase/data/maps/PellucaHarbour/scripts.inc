PellucaHarbour_MapScripts::
# 2 "data/maps/PellucaHarbour/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaHarbour_MapScripts_MAP_SCRIPT_ON_TRANSITION
# 5 "data/maps/PellucaHarbour/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaHarbour_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaHarbour_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 3 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_VISITED_PELLUCA_CITY
	return

PellucaHarbour_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 6 "data/maps/PellucaHarbour/scripts.pory"
	map_script_2 VAR_UNUSED_0x404E, 1, PellucaHarbour_Arrival
	.2byte 0


PellucaHarbour_Arrival::
# 18 "data/maps/PellucaHarbour/scripts.pory"
	lockall
# 19 "data/maps/PellucaHarbour/scripts.pory"
	setvar VAR_UNUSED_0x404E, 2
# 20 "data/maps/PellucaHarbour/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaHarbour_Arrival_Movement_0
# 21 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 22 "data/maps/PellucaHarbour/scripts.pory"
	delay 20
# 23 "data/maps/PellucaHarbour/scripts.pory"
	speakername PellucaHarbour_Arrival_Text_0
# 24 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_1
# 25 "data/maps/PellucaHarbour/scripts.pory"
	speakername PellucaHarbour_Arrival_Text_2
# 26 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_3
# 27 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 28 "data/maps/PellucaHarbour/scripts.pory"
	delay 30
# 29 "data/maps/PellucaHarbour/scripts.pory"
	applymovement 2, PellucaHarbour_Arrival_Movement_1
# 30 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 31 "data/maps/PellucaHarbour/scripts.pory"
	delay 12
# 32 "data/maps/PellucaHarbour/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 33 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_4
# 34 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 35 "data/maps/PellucaHarbour/scripts.pory"
	delay 40
# 36 "data/maps/PellucaHarbour/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 37 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_5
# 38 "data/maps/PellucaHarbour/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 39 "data/maps/PellucaHarbour/scripts.pory"
	speakername PellucaHarbour_Arrival_Text_6
# 40 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_7
# 41 "data/maps/PellucaHarbour/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 42 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_8
# 43 "data/maps/PellucaHarbour/scripts.pory"
	hideportrait
# 44 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 45 "data/maps/PellucaHarbour/scripts.pory"
	release
# 46 "data/maps/PellucaHarbour/scripts.pory"
	delay 12
# 47 "data/maps/PellucaHarbour/scripts.pory"
	applymovement 2, PellucaHarbour_Arrival_Movement_2
# 48 "data/maps/PellucaHarbour/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaHarbour_Arrival_Movement_3
# 49 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 50 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 2
# 51 "data/maps/PellucaHarbour/scripts.pory"
	delay 30
# 52 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_9, MSGBOX_SIGN
# 53 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 54 "data/maps/PellucaHarbour/scripts.pory"
	delay 40
# 55 "data/maps/PellucaHarbour/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 56 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_10
# 57 "data/maps/PellucaHarbour/scripts.pory"
	hideportrait
# 58 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 59 "data/maps/PellucaHarbour/scripts.pory"
	applymovement 2, PellucaHarbour_Arrival_Movement_0
# 60 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 61 "data/maps/PellucaHarbour/scripts.pory"
	delay 12
# 62 "data/maps/PellucaHarbour/scripts.pory"
	playse SE_EXIT
# 63 "data/maps/PellucaHarbour/scripts.pory"
	removeobject 2
# 64 "data/maps/PellucaHarbour/scripts.pory"
	delay 16
# 65 "data/maps/PellucaHarbour/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaHarbour_Arrival_Movement_4
# 66 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 67 "data/maps/PellucaHarbour/scripts.pory"
	delay 12
# 68 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_UNUSED_0x884
# 69 "data/maps/PellucaHarbour/scripts.pory"
	warp MAP_PELLUCA_UMBRA_LAB, 0
# 70 "data/maps/PellucaHarbour/scripts.pory"
	waitstate
	end


# 20 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_0:
# 20 "data/maps/PellucaHarbour/scripts.pory"
	face_up
	step_end

# 29 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_1:
# 29 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 29 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 29 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 29 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 29 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
	step_end

# 47 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_2:
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 47 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 47 "data/maps/PellucaHarbour/scripts.pory"
	face_left
	step_end

# 48 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_3:
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_left
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_left
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	face_up
	step_end

# 65 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_4:
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 65 "data/maps/PellucaHarbour/scripts.pory"
	face_up
	step_end

PellucaHarbour_Arrival_Text_0:
# 23 "data/maps/PellucaHarbour/scripts.pory"
	.string "Dockhand$"

PellucaHarbour_Arrival_Text_1:
# 24 "data/maps/PellucaHarbour/scripts.pory"
	.string "A Rainhawk, in a mask? Like something\n"
	.string "out of the old stories.$"

PellucaHarbour_Arrival_Text_2:
# 25 "data/maps/PellucaHarbour/scripts.pory"
	.string "Sailor$"

PellucaHarbour_Arrival_Text_3:
# 26 "data/maps/PellucaHarbour/scripts.pory"
	.string "That's the one who held the beach at\n"
	.string "Sevii. Burned for it, they say.$"

PellucaHarbour_Arrival_Text_4:
# 33 "data/maps/PellucaHarbour/scripts.pory"
	.string "Rainhawk Alban. Welcome to Pelluca\n"
	.string "Valley.$"

PellucaHarbour_Arrival_Text_5:
# 37 "data/maps/PellucaHarbour/scripts.pory"
	.string "And the burns? Are they healing?$"

PellucaHarbour_Arrival_Text_6:
# 39 "data/maps/PellucaHarbour/scripts.pory"
	.string "“Nomad”$"

PellucaHarbour_Arrival_Text_7:
# 40 "data/maps/PellucaHarbour/scripts.pory"
	.string "Slowly. The mask helps.$"

PellucaHarbour_Arrival_Text_8:
# 42 "data/maps/PellucaHarbour/scripts.pory"
	.string "Good. Walk with me. We will talk\n"
	.string "somewhere quieter.$"

PellucaHarbour_Arrival_Text_9:
# 52 "data/maps/PellucaHarbour/scripts.pory"
	.string "For Prince {PLAYER}, Keerin's Chosen.\n"
	.string "Wherever you are, come home.$"

PellucaHarbour_Arrival_Text_10:
# 56 "data/maps/PellucaHarbour/scripts.pory"
	.string "Rainhawk.$"
