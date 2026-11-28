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
	applymovement 2, PellucaHarbour_Arrival_Movement_4
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
	applymovement OBJ_EVENT_ID_PLAYER, PellucaHarbour_Arrival_Movement_5
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


PellucaHarbour_EventScript_Fisherman::
# 77 "data/maps/PellucaHarbour/scripts.pory"
	lock
# 78 "data/maps/PellucaHarbour/scripts.pory"
	faceplayer
# 79 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_RECEIVED_OLD_ROD, PellucaHarbour_EventScript_Fisherman_2
# 81 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_WIMPOD_DONE, PellucaHarbour_EventScript_Fisherman_3
# 85 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_WIMPOD_QUEST_STARTED, PellucaHarbour_EventScript_Fisherman_4
# 87 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_unset FLAG_DR_CHURCH_BLASTED, PellucaHarbour_EventScript_Fisherman_5
# 90 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_4
# 91 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_5
# 92 "data/maps/PellucaHarbour/scripts.pory"
	giveitem ITEM_POKE_BALL, 5
# 93 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_WIMPOD_QUEST_STARTED
PellucaHarbour_EventScript_Fisherman_1:
# 95 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 96 "data/maps/PellucaHarbour/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaHarbour_EventScript_Fisherman_Movement_0
# 97 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 98 "data/maps/PellucaHarbour/scripts.pory"
	release
	end

PellucaHarbour_EventScript_Fisherman_2:
# 80 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_0
	goto PellucaHarbour_EventScript_Fisherman_1

PellucaHarbour_EventScript_Fisherman_3:
# 82 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_1
# 83 "data/maps/PellucaHarbour/scripts.pory"
	giveitem ITEM_OLD_ROD
# 84 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_RECEIVED_OLD_ROD
	goto PellucaHarbour_EventScript_Fisherman_1

PellucaHarbour_EventScript_Fisherman_4:
# 86 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_2
	goto PellucaHarbour_EventScript_Fisherman_1

PellucaHarbour_EventScript_Fisherman_5:
# 88 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_3
	goto PellucaHarbour_EventScript_Fisherman_1


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
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 48 "data/maps/PellucaHarbour/scripts.pory"
	face_up
	step_end

# 59 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_4:
# 59 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 59 "data/maps/PellucaHarbour/scripts.pory"
	face_up
	step_end

# 65 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_5:
# 65 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
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
	walk_up
# 65 "data/maps/PellucaHarbour/scripts.pory"
	face_up
	step_end

# 96 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_EventScript_Fisherman_Movement_0:
# 96 "data/maps/PellucaHarbour/scripts.pory"
	face_down
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

PellucaHarbour_EventScript_Fisherman_Text_0:
# 80 "data/maps/PellucaHarbour/scripts.pory"
	.string "The tide's turning, and the fish turn\n"
	.string "with it. Try the river up Mt. Mirroh one\l"
	.string "day, they say the Basculin there fight\l"
	.string "like wolves.$"

PellucaHarbour_EventScript_Fisherman_Text_1:
# 82 "data/maps/PellucaHarbour/scripts.pory"
	.string "A Wimpod, was it? The Sevii fishermen\n"
	.string "call them shore-scavengers, and a\l"
	.string "hungry one will strip a net bare before\l"
	.string "dawn. Here, take my old rod for your\l"
	.string "trouble. Cast it off any pier or\l"
	.string "riverbank and see what bites.$"

PellucaHarbour_EventScript_Fisherman_Text_2:
# 86 "data/maps/PellucaHarbour/scripts.pory"
	.string "It went up into town, I'm sure of it.\n"
	.string "Look wherever there's fresh water, the\l"
	.string "fountain first.$"

PellucaHarbour_EventScript_Fisherman_Text_3:
# 88 "data/maps/PellucaHarbour/scripts.pory"
	.string "Quiet waters today. Even the gulls have\n"
	.string "gone looking for better luck.$"

PellucaHarbour_EventScript_Fisherman_Text_4:
# 90 "data/maps/PellucaHarbour/scripts.pory"
	.string "Curse the tide! Something took hold of\n"
	.string "my line off this pier, all grey shell and\l"
	.string "claws, and dragged half my catch up\l"
	.string "into town. By the way it scrabbled, I'd\l"
	.string "wager it went looking for fresh water.\l"
	.string "Catch that thief for me and you'll not\l"
	.string "leave empty-handed.$"

PellucaHarbour_EventScript_Fisherman_Text_5:
# 91 "data/maps/PellucaHarbour/scripts.pory"
	.string "Take these Poké Spheres along. It's\n"
	.string "quick and slippery, and you'll want a way\l"
	.string "to hold it.$"
