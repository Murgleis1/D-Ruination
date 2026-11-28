PellucaHarbour_MapScripts::
# 2 "data/maps/PellucaHarbour/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaHarbour_MapScripts_MAP_SCRIPT_ON_TRANSITION
# 6 "data/maps/PellucaHarbour/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaHarbour_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaHarbour_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 3 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_VISITED_PELLUCA_CITY
# 4 "data/maps/PellucaHarbour/scripts.pory"
	call PellucaHarbour_EventScript_BurglarFlags
	return

PellucaHarbour_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 7 "data/maps/PellucaHarbour/scripts.pory"
	map_script_2 VAR_UNUSED_0x404E, 1, PellucaHarbour_Arrival
	.2byte 0


PellucaHarbour_Arrival::
# 19 "data/maps/PellucaHarbour/scripts.pory"
	lockall
# 20 "data/maps/PellucaHarbour/scripts.pory"
	setvar VAR_UNUSED_0x404E, 2
# 21 "data/maps/PellucaHarbour/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaHarbour_Arrival_Movement_0
# 22 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 23 "data/maps/PellucaHarbour/scripts.pory"
	delay 20
# 24 "data/maps/PellucaHarbour/scripts.pory"
	speakername PellucaHarbour_Arrival_Text_0
# 25 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_1
# 26 "data/maps/PellucaHarbour/scripts.pory"
	speakername PellucaHarbour_Arrival_Text_2
# 27 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_3
# 28 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 29 "data/maps/PellucaHarbour/scripts.pory"
	delay 30
# 30 "data/maps/PellucaHarbour/scripts.pory"
	applymovement 2, PellucaHarbour_Arrival_Movement_1
# 31 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 32 "data/maps/PellucaHarbour/scripts.pory"
	delay 12
# 33 "data/maps/PellucaHarbour/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 34 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_4
# 35 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 36 "data/maps/PellucaHarbour/scripts.pory"
	delay 40
# 37 "data/maps/PellucaHarbour/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 38 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_5
# 39 "data/maps/PellucaHarbour/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 40 "data/maps/PellucaHarbour/scripts.pory"
	speakername PellucaHarbour_Arrival_Text_6
# 41 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_7
# 42 "data/maps/PellucaHarbour/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 43 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_8
# 44 "data/maps/PellucaHarbour/scripts.pory"
	hideportrait
# 45 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 46 "data/maps/PellucaHarbour/scripts.pory"
	release
# 47 "data/maps/PellucaHarbour/scripts.pory"
	delay 12
# 48 "data/maps/PellucaHarbour/scripts.pory"
	applymovement 2, PellucaHarbour_Arrival_Movement_2
# 49 "data/maps/PellucaHarbour/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaHarbour_Arrival_Movement_3
# 50 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 51 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 2
# 52 "data/maps/PellucaHarbour/scripts.pory"
	delay 30
# 53 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_9, MSGBOX_SIGN
# 54 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 55 "data/maps/PellucaHarbour/scripts.pory"
	delay 40
# 56 "data/maps/PellucaHarbour/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 57 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_Arrival_Text_10
# 58 "data/maps/PellucaHarbour/scripts.pory"
	hideportrait
# 59 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 60 "data/maps/PellucaHarbour/scripts.pory"
	applymovement 2, PellucaHarbour_Arrival_Movement_4
# 61 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 62 "data/maps/PellucaHarbour/scripts.pory"
	delay 12
# 63 "data/maps/PellucaHarbour/scripts.pory"
	playse SE_EXIT
# 64 "data/maps/PellucaHarbour/scripts.pory"
	removeobject 2
# 65 "data/maps/PellucaHarbour/scripts.pory"
	delay 16
# 66 "data/maps/PellucaHarbour/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaHarbour_Arrival_Movement_5
# 67 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 68 "data/maps/PellucaHarbour/scripts.pory"
	delay 12
# 69 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_UNUSED_0x884
# 70 "data/maps/PellucaHarbour/scripts.pory"
	warp MAP_PELLUCA_UMBRA_LAB, 0
# 71 "data/maps/PellucaHarbour/scripts.pory"
	waitstate
	end


PellucaHarbour_EventScript_Fisherman::
# 78 "data/maps/PellucaHarbour/scripts.pory"
	lock
# 79 "data/maps/PellucaHarbour/scripts.pory"
	faceplayer
# 80 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_RECEIVED_OLD_ROD, PellucaHarbour_EventScript_Fisherman_2
# 82 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_WIMPOD_DONE, PellucaHarbour_EventScript_Fisherman_3
# 86 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_WIMPOD_QUEST_STARTED, PellucaHarbour_EventScript_Fisherman_4
# 88 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_unset FLAG_DR_CHURCH_BLASTED, PellucaHarbour_EventScript_Fisherman_5
# 91 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_4
# 92 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_5
# 93 "data/maps/PellucaHarbour/scripts.pory"
	giveitem ITEM_POKE_BALL, 5
# 94 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_WIMPOD_QUEST_STARTED
PellucaHarbour_EventScript_Fisherman_1:
# 96 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 97 "data/maps/PellucaHarbour/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaHarbour_EventScript_Fisherman_Movement_0
# 98 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 99 "data/maps/PellucaHarbour/scripts.pory"
	release
	end

PellucaHarbour_EventScript_Fisherman_2:
# 81 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_0
	goto PellucaHarbour_EventScript_Fisherman_1

PellucaHarbour_EventScript_Fisherman_3:
# 83 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_1
# 84 "data/maps/PellucaHarbour/scripts.pory"
	giveitem ITEM_OLD_ROD
# 85 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_RECEIVED_OLD_ROD
	goto PellucaHarbour_EventScript_Fisherman_1

PellucaHarbour_EventScript_Fisherman_4:
# 87 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_2
	goto PellucaHarbour_EventScript_Fisherman_1

PellucaHarbour_EventScript_Fisherman_5:
# 89 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_Fisherman_Text_3
	goto PellucaHarbour_EventScript_Fisherman_1


PellucaHarbour_EventScript_BurglarFlags::
# 119 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_HIDE_BURGLAR_COIN1
# 120 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_HIDE_BURGLAR_COIN2
# 121 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_HIDE_BURGLAR_KEY
# 122 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_HIDE_BURGLAR
# 123 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_HIDE_EGG_OLD_MAN
# 124 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_CHURCH_BLASTED, PellucaHarbour_EventScript_BurglarFlags_2
PellucaHarbour_EventScript_BurglarFlags_1:
# 127 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_unset FLAG_DR_BURGLAR_QUEST_STARTED, PellucaHarbour_EventScript_BurglarFlags_5
# 127 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_BURGLAR_LOOT_RECOVERED, PellucaHarbour_EventScript_BurglarFlags_5
# 130 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_BURGLAR_KEY_FOUND, PellucaHarbour_EventScript_BurglarFlags_10
# 132 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_BURGLAR_COIN2_FOUND, PellucaHarbour_EventScript_BurglarFlags_11
# 134 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_BURGLAR_COIN1_FOUND, PellucaHarbour_EventScript_BurglarFlags_12
# 137 "data/maps/PellucaHarbour/scripts.pory"
	clearflag FLAG_DR_HIDE_BURGLAR_COIN1
PellucaHarbour_EventScript_BurglarFlags_9:
	return

PellucaHarbour_EventScript_BurglarFlags_2:
# 125 "data/maps/PellucaHarbour/scripts.pory"
	clearflag FLAG_DR_HIDE_EGG_OLD_MAN
	goto PellucaHarbour_EventScript_BurglarFlags_1

PellucaHarbour_EventScript_BurglarFlags_5:
	return

PellucaHarbour_EventScript_BurglarFlags_10:
# 131 "data/maps/PellucaHarbour/scripts.pory"
	clearflag FLAG_DR_HIDE_BURGLAR
	goto PellucaHarbour_EventScript_BurglarFlags_9

PellucaHarbour_EventScript_BurglarFlags_11:
# 133 "data/maps/PellucaHarbour/scripts.pory"
	clearflag FLAG_DR_HIDE_BURGLAR_KEY
	goto PellucaHarbour_EventScript_BurglarFlags_9

PellucaHarbour_EventScript_BurglarFlags_12:
# 135 "data/maps/PellucaHarbour/scripts.pory"
	clearflag FLAG_DR_HIDE_BURGLAR_COIN2
	goto PellucaHarbour_EventScript_BurglarFlags_9


PellucaHarbour_EventScript_EggOldMan::
# 143 "data/maps/PellucaHarbour/scripts.pory"
	lock
# 144 "data/maps/PellucaHarbour/scripts.pory"
	faceplayer
# 145 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_BURGLAR_EGG_RECEIVED, PellucaHarbour_EventScript_EggOldMan_2
# 147 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_BURGLAR_LOOT_RECOVERED, PellucaHarbour_EventScript_EggOldMan_3
# 150 "data/maps/PellucaHarbour/scripts.pory"
	goto_if_set FLAG_DR_BURGLAR_QUEST_STARTED, PellucaHarbour_EventScript_EggOldMan_4
# 153 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_EggOldMan_Text_3
# 154 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_BURGLAR_QUEST_STARTED
# 155 "data/maps/PellucaHarbour/scripts.pory"
	clearflag FLAG_DR_HIDE_BURGLAR_COIN1
# 156 "data/maps/PellucaHarbour/scripts.pory"
	addobject 17
PellucaHarbour_EventScript_EggOldMan_1:
# 158 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 159 "data/maps/PellucaHarbour/scripts.pory"
	applymovement 16, PellucaHarbour_EventScript_Fisherman_Movement_0
# 160 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 161 "data/maps/PellucaHarbour/scripts.pory"
	release
	end

PellucaHarbour_EventScript_EggOldMan_2:
# 146 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_EggOldMan_Text_0
	goto PellucaHarbour_EventScript_EggOldMan_1

PellucaHarbour_EventScript_EggOldMan_3:
# 148 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_EggOldMan_Text_1
# 149 "data/maps/PellucaHarbour/scripts.pory"
	call PellucaHarbour_EventScript_ChooseEgg
	goto PellucaHarbour_EventScript_EggOldMan_1

PellucaHarbour_EventScript_EggOldMan_4:
# 151 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_EggOldMan_Text_2
	goto PellucaHarbour_EventScript_EggOldMan_1


PellucaHarbour_EventScript_ChooseEgg::
# 167 "data/maps/PellucaHarbour/scripts.pory"
	setvar VAR_0x8004, SPECIES_NONE
PellucaHarbour_EventScript_ChooseEgg_2:
# 168 "data/maps/PellucaHarbour/scripts.pory"
	compare VAR_0x8004, SPECIES_NONE
	goto_if_eq PellucaHarbour_EventScript_ChooseEgg_3
PellucaHarbour_EventScript_ChooseEgg_1:
# 185 "data/maps/PellucaHarbour/scripts.pory"
	call DrShinyTease_Ask
# 186 "data/maps/PellucaHarbour/scripts.pory"
	giveegg VAR_0x8004
# 187 "data/maps/PellucaHarbour/scripts.pory"
	clearflag FLAG_FORCE_SHINY
# 188 "data/maps/PellucaHarbour/scripts.pory"
	compare VAR_RESULT, MON_CANT_GIVE
	goto_if_eq PellucaHarbour_EventScript_ChooseEgg_6
# 192 "data/maps/PellucaHarbour/scripts.pory"
	setvar VAR_0x8005, 6
# 193 "data/maps/PellucaHarbour/scripts.pory"
	special DrSetLastEggCycles
# 194 "data/maps/PellucaHarbour/scripts.pory"
	playfanfare MUS_OBTAIN_ITEM
# 195 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_ChooseEgg_Text_4
# 196 "data/maps/PellucaHarbour/scripts.pory"
	waitfanfare
# 197 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_BURGLAR_EGG_RECEIVED
# 198 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_EggOldMan_Text_0
	return

PellucaHarbour_EventScript_ChooseEgg_3:
# 169 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_ChooseEgg_Text_0, MSGBOX_YESNO
# 170 "data/maps/PellucaHarbour/scripts.pory"
	compare VAR_RESULT, YES
	goto_if_eq PellucaHarbour_EventScript_ChooseEgg_9
# 174 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_ChooseEgg_Text_1, MSGBOX_YESNO
# 175 "data/maps/PellucaHarbour/scripts.pory"
	compare VAR_RESULT, YES
	goto_if_eq PellucaHarbour_EventScript_ChooseEgg_12
# 179 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_ChooseEgg_Text_2, MSGBOX_YESNO
# 180 "data/maps/PellucaHarbour/scripts.pory"
	compare VAR_RESULT, YES
	goto_if_eq PellucaHarbour_EventScript_ChooseEgg_14
	goto PellucaHarbour_EventScript_ChooseEgg_2

PellucaHarbour_EventScript_ChooseEgg_6:
# 189 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_ChooseEgg_Text_3
	return

PellucaHarbour_EventScript_ChooseEgg_9:
# 171 "data/maps/PellucaHarbour/scripts.pory"
	setvar VAR_0x8004, SPECIES_SQUIRTLE
	goto PellucaHarbour_EventScript_ChooseEgg_1

PellucaHarbour_EventScript_ChooseEgg_12:
# 176 "data/maps/PellucaHarbour/scripts.pory"
	setvar VAR_0x8004, SPECIES_CHESPIN
	goto PellucaHarbour_EventScript_ChooseEgg_1

PellucaHarbour_EventScript_ChooseEgg_14:
# 181 "data/maps/PellucaHarbour/scripts.pory"
	setvar VAR_0x8004, SPECIES_CHIMCHAR
	goto PellucaHarbour_EventScript_ChooseEgg_1


PellucaHarbour_EventScript_BurglarCoin1::
# 203 "data/maps/PellucaHarbour/scripts.pory"
	lock
# 204 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_BurglarCoin1_Text_0
# 205 "data/maps/PellucaHarbour/scripts.pory"
	removeobject 17
# 206 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_HIDE_BURGLAR_COIN1
# 207 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_BURGLAR_COIN1_FOUND
# 208 "data/maps/PellucaHarbour/scripts.pory"
	clearflag FLAG_DR_HIDE_BURGLAR_COIN2
# 209 "data/maps/PellucaHarbour/scripts.pory"
	addobject 18
# 210 "data/maps/PellucaHarbour/scripts.pory"
	release
	end


PellucaHarbour_EventScript_BurglarCoin2::
# 215 "data/maps/PellucaHarbour/scripts.pory"
	lock
# 216 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_BurglarCoin2_Text_0
# 217 "data/maps/PellucaHarbour/scripts.pory"
	removeobject 18
# 218 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_HIDE_BURGLAR_COIN2
# 219 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_BURGLAR_COIN2_FOUND
# 220 "data/maps/PellucaHarbour/scripts.pory"
	clearflag FLAG_DR_HIDE_BURGLAR_KEY
# 221 "data/maps/PellucaHarbour/scripts.pory"
	addobject 19
# 222 "data/maps/PellucaHarbour/scripts.pory"
	release
	end


PellucaHarbour_EventScript_BurglarKey::
# 227 "data/maps/PellucaHarbour/scripts.pory"
	lock
# 228 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_BurglarKey_Text_0
# 229 "data/maps/PellucaHarbour/scripts.pory"
	removeobject 19
# 230 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_HIDE_BURGLAR_KEY
# 231 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_BURGLAR_KEY_FOUND
# 232 "data/maps/PellucaHarbour/scripts.pory"
	clearflag FLAG_DR_HIDE_BURGLAR
# 233 "data/maps/PellucaHarbour/scripts.pory"
	addobject 20
# 234 "data/maps/PellucaHarbour/scripts.pory"
	release
	end


PellucaHarbour_EventScript_Burglar::
# 239 "data/maps/PellucaHarbour/scripts.pory"
	trainerbattle_single TRAINER_DR_PELLUCA_BURGLAR, PellucaHarbour_EventScript_Burglar_Text_0, PellucaHarbour_EventScript_Burglar_Text_1, PellucaHarbour_EventScript_BurglarBeaten
	end


PellucaHarbour_EventScript_BurglarBeaten::
# 244 "data/maps/PellucaHarbour/scripts.pory"
	lock
# 245 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_BurglarBeaten_Text_0
# 246 "data/maps/PellucaHarbour/scripts.pory"
	closemessage
# 247 "data/maps/PellucaHarbour/scripts.pory"
	applymovement 20, PellucaHarbour_EventScript_BurglarBeaten_Movement_0
# 248 "data/maps/PellucaHarbour/scripts.pory"
	waitmovement 0
# 249 "data/maps/PellucaHarbour/scripts.pory"
	removeobject 20
# 250 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_HIDE_BURGLAR
# 251 "data/maps/PellucaHarbour/scripts.pory"
	setflag FLAG_DR_BURGLAR_LOOT_RECOVERED
# 252 "data/maps/PellucaHarbour/scripts.pory"
	msgbox PellucaHarbour_EventScript_BurglarBeaten_Text_1
# 253 "data/maps/PellucaHarbour/scripts.pory"
	release
	end


# 21 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_0:
# 21 "data/maps/PellucaHarbour/scripts.pory"
	face_up
	step_end

# 30 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_1:
# 30 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 30 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 30 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 30 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 30 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
	step_end

# 48 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_2:
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
	walk_right
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 48 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 48 "data/maps/PellucaHarbour/scripts.pory"
	face_left
	step_end

# 49 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_3:
# 49 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 49 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 49 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 49 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 49 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 49 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 49 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 49 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 49 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 49 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 49 "data/maps/PellucaHarbour/scripts.pory"
	face_up
	step_end

# 60 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_4:
# 60 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 60 "data/maps/PellucaHarbour/scripts.pory"
	face_up
	step_end

# 66 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_Arrival_Movement_5:
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_down
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_right
# 66 "data/maps/PellucaHarbour/scripts.pory"
	walk_up
# 66 "data/maps/PellucaHarbour/scripts.pory"
	face_up
	step_end

# 97 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_EventScript_Fisherman_Movement_0:
# 97 "data/maps/PellucaHarbour/scripts.pory"
	face_down
	step_end

# 247 "data/maps/PellucaHarbour/scripts.pory"
PellucaHarbour_EventScript_BurglarBeaten_Movement_0:
# 247 "data/maps/PellucaHarbour/scripts.pory"
	walk_fast_right
# 247 "data/maps/PellucaHarbour/scripts.pory"
	walk_fast_right
# 247 "data/maps/PellucaHarbour/scripts.pory"
	walk_fast_right
# 247 "data/maps/PellucaHarbour/scripts.pory"
	walk_fast_right
# 247 "data/maps/PellucaHarbour/scripts.pory"
	walk_fast_right
# 247 "data/maps/PellucaHarbour/scripts.pory"
	walk_fast_right
	step_end

PellucaHarbour_Arrival_Text_0:
# 24 "data/maps/PellucaHarbour/scripts.pory"
	.string "Dockhand$"

PellucaHarbour_Arrival_Text_1:
# 25 "data/maps/PellucaHarbour/scripts.pory"
	.string "A Rainhawk, in a mask? Like something\n"
	.string "out of the old stories.$"

PellucaHarbour_Arrival_Text_2:
# 26 "data/maps/PellucaHarbour/scripts.pory"
	.string "Sailor$"

PellucaHarbour_Arrival_Text_3:
# 27 "data/maps/PellucaHarbour/scripts.pory"
	.string "That's the one who held the beach at\n"
	.string "Sevii. Burned for it, they say.$"

PellucaHarbour_Arrival_Text_4:
# 34 "data/maps/PellucaHarbour/scripts.pory"
	.string "Rainhawk Alban. Welcome to Pelluca\n"
	.string "Valley.$"

PellucaHarbour_Arrival_Text_5:
# 38 "data/maps/PellucaHarbour/scripts.pory"
	.string "And the burns? Are they healing?$"

PellucaHarbour_Arrival_Text_6:
# 40 "data/maps/PellucaHarbour/scripts.pory"
	.string "“Nomad”$"

PellucaHarbour_Arrival_Text_7:
# 41 "data/maps/PellucaHarbour/scripts.pory"
	.string "Slowly. The mask helps.$"

PellucaHarbour_Arrival_Text_8:
# 43 "data/maps/PellucaHarbour/scripts.pory"
	.string "Good. Walk with me. We will talk\n"
	.string "somewhere quieter.$"

PellucaHarbour_Arrival_Text_9:
# 53 "data/maps/PellucaHarbour/scripts.pory"
	.string "For Prince {PLAYER}, Keerin's Chosen.\n"
	.string "Wherever you are, come home.$"

PellucaHarbour_Arrival_Text_10:
# 57 "data/maps/PellucaHarbour/scripts.pory"
	.string "Rainhawk.$"

PellucaHarbour_EventScript_Fisherman_Text_0:
# 81 "data/maps/PellucaHarbour/scripts.pory"
	.string "The tide's turning, and the fish turn\n"
	.string "with it. Try the river up Mt. Mirroh one\l"
	.string "day, they say the Basculin there fight\l"
	.string "like wolves.$"

PellucaHarbour_EventScript_Fisherman_Text_1:
# 83 "data/maps/PellucaHarbour/scripts.pory"
	.string "A Wimpod, was it? The Sevii fishermen\n"
	.string "call them shore-scavengers, and a\l"
	.string "hungry one will strip a net bare before\l"
	.string "dawn. Here, take my old rod for your\l"
	.string "trouble. Cast it off any pier or\l"
	.string "riverbank and see what bites.$"

PellucaHarbour_EventScript_Fisherman_Text_2:
# 87 "data/maps/PellucaHarbour/scripts.pory"
	.string "It went up into town, I'm sure of it.\n"
	.string "Look wherever there's fresh water, the\l"
	.string "fountain first.$"

PellucaHarbour_EventScript_Fisherman_Text_3:
# 89 "data/maps/PellucaHarbour/scripts.pory"
	.string "Quiet waters today. Even the gulls have\n"
	.string "gone looking for better luck.$"

PellucaHarbour_EventScript_Fisherman_Text_4:
# 91 "data/maps/PellucaHarbour/scripts.pory"
	.string "Curse the tide! Something took hold of\n"
	.string "my line off this pier, all grey shell and\l"
	.string "claws, and dragged half my catch up\l"
	.string "into town. By the way it scrabbled, I'd\l"
	.string "wager it went looking for fresh water.\l"
	.string "Catch that thief for me and you'll not\l"
	.string "leave empty-handed.$"

PellucaHarbour_EventScript_Fisherman_Text_5:
# 92 "data/maps/PellucaHarbour/scripts.pory"
	.string "Take these Poké Spheres along. It's\n"
	.string "quick and slippery, and you'll want a way\l"
	.string "to hold it.$"

PellucaHarbour_EventScript_EggOldMan_Text_0:
# 146 "data/maps/PellucaHarbour/scripts.pory"
	.string "Keep it warm and keep walking. An egg\n"
	.string "like that hatches faster with the road\l"
	.string "under it.$"

PellucaHarbour_EventScript_EggOldMan_Text_1:
# 148 "data/maps/PellucaHarbour/scripts.pory"
	.string "My purse and my key! Bless you, child.\n"
	.string "These eggs came from distant lands, and\l"
	.string "Vizier Umbra would want one in good\l"
	.string "hands. Choose, and choose well.$"

PellucaHarbour_EventScript_EggOldMan_Text_2:
# 151 "data/maps/PellucaHarbour/scripts.pory"
	.string "He fled along the beach toward the\n"
	.string "cliffs. Follow the glint of my coins.$"

PellucaHarbour_EventScript_EggOldMan_Text_3:
# 153 "data/maps/PellucaHarbour/scripts.pory"
	.string "Thieves in Pelluca, in broad daylight! A\n"
	.string "burglar broke into my cottage and made\l"
	.string "off with my purse and my house key. He\l"
	.string "left the three eggs I keep for Vizier\l"
	.string "Umbra, praise Arceus, but I can't get\l"
	.string "back in to tend them. He fled along the\l"
	.string "beach, dropping coins as he ran.$"

PellucaHarbour_EventScript_ChooseEgg_Text_0:
# 169 "data/maps/PellucaHarbour/scripts.pory"
	.string "The blue egg, cool as river stone. Will\n"
	.string "you take this one?$"

PellucaHarbour_EventScript_ChooseEgg_Text_1:
# 174 "data/maps/PellucaHarbour/scripts.pory"
	.string "The green egg, hard with spines. Will you\n"
	.string "take this one?$"

PellucaHarbour_EventScript_ChooseEgg_Text_2:
# 179 "data/maps/PellucaHarbour/scripts.pory"
	.string "The warm egg that smells of ash. Will you\n"
	.string "take this one?$"

PellucaHarbour_EventScript_ChooseEgg_Text_3:
# 189 "data/maps/PellucaHarbour/scripts.pory"
	.string "You've no room to carry it, child. Come\n"
	.string "back when you do.$"

PellucaHarbour_EventScript_ChooseEgg_Text_4:
# 195 "data/maps/PellucaHarbour/scripts.pory"
	.string "{PLAYER} received the Egg!$"

PellucaHarbour_EventScript_BurglarCoin1_Text_0:
# 204 "data/maps/PellucaHarbour/scripts.pory"
	.string "A silver coin lies in the sand, stamped\n"
	.string "with the Regent-Queen's face. Another\l"
	.string "glints further along the beach.$"

PellucaHarbour_EventScript_BurglarCoin2_Text_0:
# 216 "data/maps/PellucaHarbour/scripts.pory"
	.string "Another coin, half-buried, beside a\n"
	.string "boot print heading west.$"

PellucaHarbour_EventScript_BurglarKey_Text_0:
# 228 "data/maps/PellucaHarbour/scripts.pory"
	.string "A brass key on a red cord, dropped in\n"
	.string "haste. The boot prints end at the cliff.$"

PellucaHarbour_EventScript_Burglar_Text_0:
# 239 "data/maps/PellucaHarbour/scripts.pory"
	.string "Wha? How did you find me? I covered my\n"
	.string "tracks perfect, I did. Wait, are those\l"
	.string "my coins in your hand?$"

PellucaHarbour_EventScript_Burglar_Text_1:
# 239 "data/maps/PellucaHarbour/scripts.pory"
	.string "All right, all right! Take the old fool's\n"
	.string "trinkets.$"

PellucaHarbour_EventScript_BurglarBeaten_Text_0:
# 245 "data/maps/PellucaHarbour/scripts.pory"
	.string "Not a word to the Templars. I've mouths\n"
	.string "to feed, even if one of them is a\l"
	.string "Skwovet.$"

PellucaHarbour_EventScript_BurglarBeaten_Text_1:
# 252 "data/maps/PellucaHarbour/scripts.pory"
	.string "{PLAYER} recovered the old man's\n"
	.string "purse and house key.$"
