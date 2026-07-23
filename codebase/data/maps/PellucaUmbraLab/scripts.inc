# 1 "data/maps/PellucaUmbraLab/scripts.pory"

# 2 "data/maps/PellucaUmbraLab/scripts.pory"
    .set LOCALID_DRL_CADMUS,     1
# 3 "data/maps/PellucaUmbraLab/scripts.pory"
    .set LOCALID_DRL_BALL_FRIG,  2
# 4 "data/maps/PellucaUmbraLab/scripts.pory"
    .set LOCALID_DRL_BALL_TEDD,  3
# 5 "data/maps/PellucaUmbraLab/scripts.pory"
    .set LOCALID_DRL_BALL_TINK,  4
# 6 "data/maps/PellucaUmbraLab/scripts.pory"
    .set LOCALID_DRL_EDEN,       5
# 7 "data/maps/PellucaUmbraLab/scripts.pory"
    .set LOCALID_DRL_NEPTUNE,    6
# 8 "data/maps/PellucaUmbraLab/scripts.pory"
    .set LOCALID_DRL_PILFER,     7

PellucaUmbraLab_MapScripts::
# 17 "data/maps/PellucaUmbraLab/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION
# 28 "data/maps/PellucaUmbraLab/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 18 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x886
# 19 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x887
# 20 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x88E
# 21 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x40A1, 1
	goto_if_eq PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_2
# 24 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x885
PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_1:
	return

PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_2:
# 22 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x885
	goto PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_1

PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 29 "data/maps/PellucaUmbraLab/scripts.pory"
	map_script_2 VAR_UNUSED_0x40A1, 0, DR_Lab_Briefing
	.2byte 0


DR_Lab_Briefing::
# 34 "data/maps/PellucaUmbraLab/scripts.pory"
	lockall
# 35 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x40A1, 1
# 36 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 37 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Lab_Briefing_Movement_0
# 38 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 39 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_CADMUS, DR_Lab_Briefing_Movement_1
# 40 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 41 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 42 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 43 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_0
# 44 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 45 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 46 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_1
# 47 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 48 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_2
# 49 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 50 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 51 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_3
# 52 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 53 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_4
# 54 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 55 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 56 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 57 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_CADMUS, DR_Lab_Briefing_Movement_2
# 58 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 59 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 60 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x885
# 61 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_BALL_FRIG
# 62 "data/maps/PellucaUmbraLab/scripts.pory"
	playse SE_BALL_TRAY_ENTER
# 63 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 14
# 64 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_BALL_TEDD
# 65 "data/maps/PellucaUmbraLab/scripts.pory"
	playse SE_BALL_TRAY_ENTER
# 66 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 14
# 67 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_BALL_TINK
# 68 "data/maps/PellucaUmbraLab/scripts.pory"
	playse SE_BALL_TRAY_ENTER
# 69 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 24
# 70 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_CADMUS, DR_Lab_Briefing_Movement_3
# 71 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 72 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 16
# 73 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 74 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 75 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_5
# 76 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 77 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_6
# 78 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 79 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 80 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_7
# 81 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 82 "data/maps/PellucaUmbraLab/scripts.pory"
	releaseall
	end


DR_Lab_BallFrigibax::
# 87 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 88 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 89 "data/maps/PellucaUmbraLab/scripts.pory"
	showmonpicshiny SPECIES_FRIGIBAX, 10, 3
# 90 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallFrigibax_Text_0
# 91 "data/maps/PellucaUmbraLab/scripts.pory"
	hidemonpic
# 92 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallFrigibax_Text_1, MSGBOX_YESNO
# 93 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq DR_Lab_BallFrigibax_2
DR_Lab_BallFrigibax_1:
# 100 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

DR_Lab_BallFrigibax_2:
# 94 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x4083, 1
# 95 "data/maps/PellucaUmbraLab/scripts.pory"
	givemon SPECIES_FRIGIBAX, 5, item = ITEM_SITRUS_BERRY, isShiny = TRUE
# 96 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_FRIG
# 97 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 98 "data/maps/PellucaUmbraLab/scripts.pory"
	goto DR_Lab_Theft
	goto DR_Lab_BallFrigibax_1


DR_Lab_BallTeddiursa::
# 105 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 106 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 107 "data/maps/PellucaUmbraLab/scripts.pory"
	showmonpic SPECIES_TEDDIURSA, 10, 3
# 108 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTeddiursa_Text_0
# 109 "data/maps/PellucaUmbraLab/scripts.pory"
	hidemonpic
# 110 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTeddiursa_Text_1, MSGBOX_YESNO
# 111 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq DR_Lab_BallTeddiursa_2
DR_Lab_BallTeddiursa_1:
# 118 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

DR_Lab_BallTeddiursa_2:
# 112 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x4083, 2
# 113 "data/maps/PellucaUmbraLab/scripts.pory"
	givemon SPECIES_TEDDIURSA, 5, item = ITEM_SITRUS_BERRY
# 114 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TEDD
# 115 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 116 "data/maps/PellucaUmbraLab/scripts.pory"
	goto DR_Lab_Theft
	goto DR_Lab_BallTeddiursa_1


DR_Lab_BallTinkatink::
# 123 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 124 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 125 "data/maps/PellucaUmbraLab/scripts.pory"
	showmonpic SPECIES_TINKATINK, 10, 3
# 126 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTinkatink_Text_0
# 127 "data/maps/PellucaUmbraLab/scripts.pory"
	hidemonpic
# 128 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTinkatink_Text_1, MSGBOX_YESNO
# 129 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq DR_Lab_BallTinkatink_2
DR_Lab_BallTinkatink_1:
# 136 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

DR_Lab_BallTinkatink_2:
# 130 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x4083, 3
# 131 "data/maps/PellucaUmbraLab/scripts.pory"
	givemon SPECIES_TINKATINK, 5, item = ITEM_SITRUS_BERRY
# 132 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TINK
# 133 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 134 "data/maps/PellucaUmbraLab/scripts.pory"
	goto DR_Lab_Theft
	goto DR_Lab_BallTinkatink_1


DR_Lab_Theft::
# 141 "data/maps/PellucaUmbraLab/scripts.pory"
	lockall
# 142 "data/maps/PellucaUmbraLab/scripts.pory"
	additem ITEM_POTION, 1
# 143 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x40A1, 2
# 144 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_SYS_POKEMON_GET
# 145 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 146 "data/maps/PellucaUmbraLab/scripts.pory"
	fadeoutbgm 4
# 147 "data/maps/PellucaUmbraLab/scripts.pory"
	fadescreen FADE_TO_BLACK
# 148 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 45
# 149 "data/maps/PellucaUmbraLab/scripts.pory"
	setobjectxy OBJ_EVENT_ID_PLAYER, 4, 10
# 150 "data/maps/PellucaUmbraLab/scripts.pory"
	turnobject OBJ_EVENT_ID_PLAYER, DIR_NORTH
# 151 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x886
# 152 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_EDEN
# 153 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 1
	goto_if_eq DR_Lab_Theft_2
DR_Lab_Theft_1:
# 154 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 2
	goto_if_eq DR_Lab_Theft_5
DR_Lab_Theft_4:
# 155 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 3
	goto_if_eq DR_Lab_Theft_8
DR_Lab_Theft_7:
# 156 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 45
# 157 "data/maps/PellucaUmbraLab/scripts.pory"
	fadescreen FADE_FROM_BLACK
# 158 "data/maps/PellucaUmbraLab/scripts.pory"
	playbgm MUS_ENCOUNTER_AQUA, FALSE
# 159 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 40
# 160 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_ANGER
# 161 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_0
# 162 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 163 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_1
# 164 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_ANGER
# 165 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_2
# 166 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 167 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 168 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x887
# 169 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_NEPTUNE
# 170 "data/maps/PellucaUmbraLab/scripts.pory"
	playmoncry SPECIES_JOUSTEEL, CRY_MODE_NORMAL
# 171 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmoncry
# 172 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 16
# 173 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_NEPTUNE, DR_Lab_Theft_Movement_0
# 174 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 175 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 176 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEGATIVE
# 177 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_3
# 178 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 179 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 180 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Lab_Theft_Movement_1
# 181 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_EDEN, DR_Lab_Theft_Movement_2
# 182 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 183 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 12
# 184 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 185 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 186 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_4
# 187 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 188 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_5
# 189 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 190 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 191 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x88E
# 192 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_PILFER
# 193 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_PILFER, DR_Lab_Theft_Movement_2
# 194 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 195 "data/maps/PellucaUmbraLab/scripts.pory"
	playmoncry SPECIES_NICKIT, CRY_MODE_NORMAL
# 196 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmoncry
# 197 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 198 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 1
	goto_if_eq DR_Lab_Theft_11
DR_Lab_Theft_10:
# 199 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 2
	goto_if_eq DR_Lab_Theft_14
DR_Lab_Theft_13:
# 200 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 3
	goto_if_eq DR_Lab_Theft_17
DR_Lab_Theft_16:
# 201 "data/maps/PellucaUmbraLab/scripts.pory"
	lockall
# 202 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 203 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 204 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_6
# 205 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 206 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 207 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_7
# 208 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 209 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_8
# 210 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_ANGER
# 211 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_9
# 212 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 213 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 214 "data/maps/PellucaUmbraLab/scripts.pory"
	playmoncry SPECIES_JOUSTEEL, CRY_MODE_NORMAL
# 215 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmoncry
# 216 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 30
# 217 "data/maps/PellucaUmbraLab/scripts.pory"
	fadescreen FADE_TO_BLACK
# 218 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x885
# 219 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x886
# 220 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x887
# 221 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x88E
# 222 "data/maps/PellucaUmbraLab/scripts.pory"
	warp MAP_PELLUCA_TEMPLAR_MONASTERY, 6, 6
# 223 "data/maps/PellucaUmbraLab/scripts.pory"
	waitstate
# 224 "data/maps/PellucaUmbraLab/scripts.pory"
	releaseall
	end

DR_Lab_Theft_2:
# 153 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TINK
	goto DR_Lab_Theft_1

DR_Lab_Theft_5:
# 154 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_FRIG
	goto DR_Lab_Theft_4

DR_Lab_Theft_8:
# 155 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TEDD
	goto DR_Lab_Theft_7

DR_Lab_Theft_11:
# 198 "data/maps/PellucaUmbraLab/scripts.pory"
	trainerbattle_no_intro TRAINER_DR_EDEN_LAB_1, DR_Lab_Text_EdenDefeat
	goto DR_Lab_Theft_10

DR_Lab_Theft_14:
# 199 "data/maps/PellucaUmbraLab/scripts.pory"
	trainerbattle_no_intro TRAINER_DR_EDEN_LAB_2, DR_Lab_Text_EdenDefeat
	goto DR_Lab_Theft_13

DR_Lab_Theft_17:
# 200 "data/maps/PellucaUmbraLab/scripts.pory"
	trainerbattle_no_intro TRAINER_DR_EDEN_LAB_3, DR_Lab_Text_EdenDefeat
	goto DR_Lab_Theft_16


PellucaUmbraLab_EventScript_Umbra::
# 233 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 234 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 235 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 236 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox PellucaUmbraLab_EventScript_Umbra_Text_0
# 237 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 238 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end


# 37 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Briefing_Movement_0:
# 37 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_up
# 37 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_up
	step_end

# 39 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Briefing_Movement_1:
# 39 "data/maps/PellucaUmbraLab/scripts.pory"
	face_down
	step_end

# 57 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Briefing_Movement_2:
# 57 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_left
# 57 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_left
# 57 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_left
# 57 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_up
# 57 "data/maps/PellucaUmbraLab/scripts.pory"
	face_up
	step_end

# 70 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Briefing_Movement_3:
# 70 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_down
# 70 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_right
# 70 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_right
# 70 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_right
# 70 "data/maps/PellucaUmbraLab/scripts.pory"
	face_down
	step_end

# 173 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Theft_Movement_0:
# 173 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_down
# 173 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_down
# 173 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_left
# 173 "data/maps/PellucaUmbraLab/scripts.pory"
	face_up
	step_end

# 180 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Theft_Movement_1:
# 180 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_fast_left
# 180 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_fast_up
# 180 "data/maps/PellucaUmbraLab/scripts.pory"
	face_left
	step_end

# 181 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Theft_Movement_2:
# 181 "data/maps/PellucaUmbraLab/scripts.pory"
	face_right
	step_end

DR_Lab_Briefing_Text_0:
# 43 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Welcome back to Pelluca Valley, my\n"
	.string "Prince. As you can see, the place is\l"
	.string "still a mess.\p"
	.string "You and Rhydia were just 10 years old\n"
	.string "the last time I let you roam around. How\l"
	.string "does it feel?$"

DR_Lab_Briefing_Text_1:
# 46 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "... I remember it well, but it feels like it\n"
	.string "was a different life. It feels strange\l"
	.string "to be here, like I'm somehow out of\l"
	.string "place.$"

DR_Lab_Briefing_Text_2:
# 48 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "I'm sure it does feel strange. You've\n"
	.string "grown into a fine young man, albeit\l"
	.string "under challenging circumstances.\p"
	.string "Tell me... what do you think of Pokémon,\n"
	.string "my Prince?$"

DR_Lab_Briefing_Text_3:
# 51 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "... I don't have any strong feelings\n"
	.string "towards them. I directed soldiers who\l"
	.string "trained and used Pokémon on the\l"
	.string "battlefield.\p"
	.string "But I was never given any formal\n"
	.string "instruction on being a Trainer. Why do\l"
	.string "you ask?$"

DR_Lab_Briefing_Text_4:
# 53 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Because in order for you to become what\n"
	.string "Cormoria needs you to be, you will need\l"
	.string "to fully utilize the power that comes\l"
	.string "from bonding with Pokémon.\p"
	.string "I know a thing or two about what you\n"
	.string "have experienced in your last few\l"
	.string "years, especially if someone like Boran\l"
	.string "Surge was your commanding officer.\p"
	.string "I simply have this to say: you WILL\n"
	.string "need to unlearn what Surge and anyone\l"
	.string "else taught you about Pokémon,\l"
	.string "starting from today. And it begins with\l"
	.string "this-$"

DR_Lab_Briefing_Text_5:
# 75 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "... are those starter Pokémon? I've\n"
	.string "heard that Cormorian noble children are\l"
	.string "given one and a Trainer certification\l"
	.string "by the Concordance every year.\p"
	.string "Are these the same kind?$"

DR_Lab_Briefing_Text_6:
# 77 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Not exactly. These three are\n"
	.string "exceptionally special. Go look at each\l"
	.string "one and see which one catches your\l"
	.string "fancy.\p"
	.string "I attached notes to each Ball for you\n"
	.string "to learn more about them before\l"
	.string "deciding.$"

DR_Lab_Briefing_Text_7:
# 80 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "... alright.$"

DR_Lab_BallFrigibax_Text_0:
# 90 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Heraldic Frigibax\p"
	.string "Hatched from an egg I found at Mt.\n"
	.string "Mirroh. It has unique coloring and\l"
	.string "powerful offensive capabilities with\l"
	.string "Dragon and Ice type attacks, but it has\l"
	.string "a diverse movepool.\p"
	.string "My research indicates that it's final\n"
	.string "form, Baxcaliber, is so rare on the\l"
	.string "continent that only one other has been\l"
	.string "seen in the past 200 years.\p"
	.string "One document I found hypothesized\n"
	.string "that it can evolve further beyond with\l"
	.string "the help of a special stone, but this\l"
	.string "information is not confirmed.$"

DR_Lab_BallFrigibax_Text_1:
# 92 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take the Heraldic Frigibax as your\n"
	.string "partner?$"

DR_Lab_BallTeddiursa_Text_0:
# 108 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Bloodmoon Teddiursa\p"
	.string "The Blood Moon variant of the Teddiursa\n"
	.string "has been whispered about in legends for\l"
	.string "over a century, but I only found this\l"
	.string "cub by chance during a survey I\l"
	.string "conducted on a small forested island to\l"
	.string "the far east of Cormoria one year ago.\p"
	.string "Much about this long rumored species is\n"
	.string "a mystery, but I surmise that they have\l"
	.string "a tendency toward high Special Attack\l"
	.string "and Defense stats, with a movepool and\l"
	.string "evolutionary path reflecting these\l"
	.string "traits.$"

DR_Lab_BallTeddiursa_Text_1:
# 110 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take the Bloodmoon Teddiursa as your\n"
	.string "partner?$"

DR_Lab_BallTinkatink_Text_0:
# 126 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Dragonmaul Tinkatuff\p"
	.string "While visiting the dunes north of Mt.\n"
	.string "Ceram several months ago, I was\l"
	.string "extremely fortunate enough to run\l"
	.string "across a wayward egg of this extremely\l"
	.string "rare Steel/Fairy species.\p"
	.string "Supposedly the Tinkatuff clan that\n"
	.string "dwell in Cormoria's deserts are all\l"
	.string "uniquely colored and learn moves that\l"
	.string "make them exceptionally suited to\l"
	.string "hunting dragons and even other\l"
	.string "Fairy-types.\p"
	.string "A fellow academic informed me that\n"
	.string "Cormorian Tinkaton can theoretically\l"
	.string "become even stronger by equipping some\l"
	.string "sort of unique material, but I was not\l"
	.string "able to confirm this rumor.$"

DR_Lab_BallTinkatink_Text_1:
# 128 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take the Dragonmaul Tinkatuff as your\n"
	.string "partner?$"

DR_Lab_Theft_Text_0:
# 161 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "What? How did the steam generator get\n"
	.string "cut off?$"

DR_Lab_Theft_Text_1:
# 163 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Sorry for the intrusion, boys! But on\n"
	.string "behalf of the Beads Of Ruin, I'm taking\l"
	.string "this 'mon for my team.$"

DR_Lab_Theft_Text_2:
# 165 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "You just made the biggest mistake of\n"
	.string "your life, little girl. Do you know who I\l"
	.string "am?\p"
	.string "Neptune, block her escape path!$"

DR_Lab_Theft_Text_3:
# 177 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "So that's the one-of-kind special 'mon\n"
	.string "I was told about. Your reputation\l"
	.string "certainly precedes you, Vizier Umbra.\p"
	.string "But I don't need a door to escape!$"

DR_Lab_Theft_Text_4:
# 186 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "I don't know who you are, but I will stop\n"
	.string "you here.$"

DR_Lab_Theft_Text_5:
# 188 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "You wish, mask-boy! Let's see what your\n"
	.string "made of! Pilfer, lets go!$"

DR_Lab_Theft_Text_6:
# 204 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "There's no way a novice could beat me. I\n"
	.string "even stole the Pokémon that was strong\l"
	.string "against yours.\p"
	.string "Who are you? No...WHAT are you?$"

DR_Lab_Theft_Text_7:
# 207 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Nomad Alban. Rainhawk. That was a good\n"
	.string "battle, huh?$"

DR_Lab_Theft_Text_8:
# 209 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Hah...it actually was! We'll need to do it\n"
	.string "again sometime. See you soon-$"

DR_Lab_Theft_Text_9:
# 211 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "You aren't going anywhere.$"

PellucaUmbraLab_EventScript_Umbra_Text_0:
# 236 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take the time you need. When you are\n"
	.string "ready, we will begin in earnest.$"

DR_Lab_Text_EdenDefeat::
# 228 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Did I just lose against a nobody with\n"
	.string "zero battling experience? I really\l"
	.string "screwed this up.$"
