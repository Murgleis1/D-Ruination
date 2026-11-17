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
# 23 "data/maps/PellucaUmbraLab/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION
# 36 "data/maps/PellucaUmbraLab/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 24 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x886
# 25 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x887
# 26 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x88E
# 29 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x40A1, 1
	goto_if_le PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_2
# 32 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x885
PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_1:
	return

PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_2:
# 30 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x885
	goto PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_1

PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 37 "data/maps/PellucaUmbraLab/scripts.pory"
	map_script_2 VAR_UNUSED_0x40A1, 0, DR_Lab_Briefing
# 38 "data/maps/PellucaUmbraLab/scripts.pory"
	map_script_2 VAR_UNUSED_0x40A1, 3, DR_Lab_ShardBriefing
	.2byte 0


DR_Lab_Briefing::
# 44 "data/maps/PellucaUmbraLab/scripts.pory"
	lockall
# 45 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x40A1, 1
# 46 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 47 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Lab_Briefing_Movement_0
# 48 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 49 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_CADMUS, DR_Lab_Briefing_Movement_1
# 50 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 51 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 52 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 53 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_0
# 54 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 55 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 56 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_1
# 57 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 58 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 59 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_2
# 60 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 61 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 62 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_3
# 63 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 64 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 40
# 65 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 66 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_4
# 67 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 68 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 69 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_5
# 70 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 71 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_6
# 72 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 73 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_7
# 74 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_8
# 75 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 76 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 77 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_9
# 78 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 79 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_10
# 80 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 81 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 82 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_11
# 83 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 84 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_12
# 85 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 86 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 87 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_13
# 88 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 89 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_14
# 90 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 91 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 40
# 92 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 93 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_15
# 94 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 95 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 96 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_16
# 97 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 98 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_17
# 99 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 100 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 101 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_18
# 102 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 103 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_19
# 104 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 105 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 106 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_20
# 107 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 108 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_21
# 109 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 110 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 111 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_22
# 112 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 113 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_23
# 114 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 115 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 116 "data/maps/PellucaUmbraLab/scripts.pory"
	playfanfare MUS_OBTAIN_ITEM
# 117 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_24
# 118 "data/maps/PellucaUmbraLab/scripts.pory"
	waitfanfare
# 119 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_SYS_POKEDEX_GET
# 120 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 121 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 122 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_25
# 123 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 124 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 125 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_26
# 126 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 127 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 128 "data/maps/PellucaUmbraLab/scripts.pory"
	releaseall
	end


DR_Lab_BallFrigibax::
# 133 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 134 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 135 "data/maps/PellucaUmbraLab/scripts.pory"
	showmonpicshiny SPECIES_FRIGIBAX, 10, 3
# 136 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallFrigibax_Text_0
# 137 "data/maps/PellucaUmbraLab/scripts.pory"
	hidemonpic
# 138 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallFrigibax_Text_1, MSGBOX_YESNO
# 139 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq DR_Lab_BallFrigibax_2
DR_Lab_BallFrigibax_1:
# 146 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

DR_Lab_BallFrigibax_2:
# 140 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x4083, 1
# 141 "data/maps/PellucaUmbraLab/scripts.pory"
	givemon SPECIES_FRIGIBAX, 5, item = ITEM_SITRUS_BERRY, isShiny = TRUE
# 142 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_FRIG
# 143 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 144 "data/maps/PellucaUmbraLab/scripts.pory"
	goto DR_Lab_Theft
	goto DR_Lab_BallFrigibax_1


DR_Lab_BallTeddiursa::
# 151 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 152 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 153 "data/maps/PellucaUmbraLab/scripts.pory"
	showmonpic SPECIES_TEDDIURSA, 10, 3
# 154 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTeddiursa_Text_0
# 155 "data/maps/PellucaUmbraLab/scripts.pory"
	hidemonpic
# 156 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTeddiursa_Text_1, MSGBOX_YESNO
# 157 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq DR_Lab_BallTeddiursa_2
DR_Lab_BallTeddiursa_1:
# 164 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

DR_Lab_BallTeddiursa_2:
# 158 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x4083, 2
# 159 "data/maps/PellucaUmbraLab/scripts.pory"
	givemon SPECIES_TEDDIURSA, 5, item = ITEM_SITRUS_BERRY
# 160 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TEDD
# 161 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 162 "data/maps/PellucaUmbraLab/scripts.pory"
	goto DR_Lab_Theft
	goto DR_Lab_BallTeddiursa_1


DR_Lab_BallTinkatink::
# 169 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 170 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 171 "data/maps/PellucaUmbraLab/scripts.pory"
	showmonpic SPECIES_TINKATINK, 10, 3
# 172 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTinkatink_Text_0
# 173 "data/maps/PellucaUmbraLab/scripts.pory"
	hidemonpic
# 174 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTinkatink_Text_1, MSGBOX_YESNO
# 175 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq DR_Lab_BallTinkatink_2
DR_Lab_BallTinkatink_1:
# 182 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

DR_Lab_BallTinkatink_2:
# 176 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x4083, 3
# 177 "data/maps/PellucaUmbraLab/scripts.pory"
	givemon SPECIES_TINKATINK, 5, item = ITEM_SITRUS_BERRY
# 178 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TINK
# 179 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 180 "data/maps/PellucaUmbraLab/scripts.pory"
	goto DR_Lab_Theft
	goto DR_Lab_BallTinkatink_1


DR_Lab_Theft::
# 187 "data/maps/PellucaUmbraLab/scripts.pory"
	lockall
# 188 "data/maps/PellucaUmbraLab/scripts.pory"
	additem ITEM_POTION, 1
# 189 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x40A1, 2
# 190 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_SYS_POKEMON_GET
# 191 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 192 "data/maps/PellucaUmbraLab/scripts.pory"
	fadeoutbgm 4
# 193 "data/maps/PellucaUmbraLab/scripts.pory"
	fadescreen FADE_TO_BLACK
# 194 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 45
# 195 "data/maps/PellucaUmbraLab/scripts.pory"
	setobjectxy OBJ_EVENT_ID_PLAYER, 4, 10
# 196 "data/maps/PellucaUmbraLab/scripts.pory"
	turnobject OBJ_EVENT_ID_PLAYER, DIR_NORTH
# 197 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x886
# 198 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_EDEN
# 199 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 1
	goto_if_eq DR_Lab_Theft_2
DR_Lab_Theft_1:
# 200 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 2
	goto_if_eq DR_Lab_Theft_5
DR_Lab_Theft_4:
# 201 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 3
	goto_if_eq DR_Lab_Theft_8
DR_Lab_Theft_7:
# 202 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 45
# 203 "data/maps/PellucaUmbraLab/scripts.pory"
	fadescreen FADE_FROM_BLACK
# 204 "data/maps/PellucaUmbraLab/scripts.pory"
	playbgm MUS_ENCOUNTER_AQUA, FALSE
# 205 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 40
# 206 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 207 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_0
# 208 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 209 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 210 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_2
# 211 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 212 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_3
# 213 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 214 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 215 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_4
# 216 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 217 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_5
# 218 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 219 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 220 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x887
# 221 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_NEPTUNE
# 222 "data/maps/PellucaUmbraLab/scripts.pory"
	playmoncry SPECIES_JOUSTEEL, CRY_MODE_NORMAL
# 223 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmoncry
# 224 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 16
# 225 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_NEPTUNE, DR_Lab_Theft_Movement_0
# 226 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 227 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 228 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 229 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 230 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_6
# 231 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 232 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 233 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Lab_Theft_Movement_1
# 234 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_EDEN, DR_Lab_Theft_Movement_2
# 235 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 236 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 12
# 237 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 238 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 239 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_7
# 240 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 241 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_8
# 242 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_9
# 243 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 244 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 245 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_10
# 246 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 247 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 248 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x88E
# 249 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_PILFER
# 250 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_PILFER, DR_Lab_Theft_Movement_2
# 251 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 252 "data/maps/PellucaUmbraLab/scripts.pory"
	playmoncry SPECIES_NICKIT, CRY_MODE_NORMAL
# 253 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmoncry
# 254 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 255 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 1
	goto_if_eq DR_Lab_Theft_11
DR_Lab_Theft_10:
# 256 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 2
	goto_if_eq DR_Lab_Theft_14
DR_Lab_Theft_13:
# 257 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 3
	goto_if_eq DR_Lab_Theft_17
DR_Lab_Theft_16:
# 258 "data/maps/PellucaUmbraLab/scripts.pory"
	lockall
# 259 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 260 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 261 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 262 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_11
# 263 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 264 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_8
# 265 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_12
# 266 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 267 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 268 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_13
# 269 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 270 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_8
# 271 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_14
# 272 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 273 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 274 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_15
# 275 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 276 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_16
# 277 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 278 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 279 "data/maps/PellucaUmbraLab/scripts.pory"
	playmoncry SPECIES_JOUSTEEL, CRY_MODE_NORMAL
# 280 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmoncry
# 281 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 30
# 282 "data/maps/PellucaUmbraLab/scripts.pory"
	fadescreen FADE_TO_BLACK
# 283 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x885
# 284 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x886
# 285 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x887
# 286 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x88E
# 287 "data/maps/PellucaUmbraLab/scripts.pory"
	warp MAP_PELLUCA_TEMPLAR_MONASTERY, 6, 6
# 288 "data/maps/PellucaUmbraLab/scripts.pory"
	waitstate
# 289 "data/maps/PellucaUmbraLab/scripts.pory"
	releaseall
	end

DR_Lab_Theft_2:
# 199 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TINK
	goto DR_Lab_Theft_1

DR_Lab_Theft_5:
# 200 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_FRIG
	goto DR_Lab_Theft_4

DR_Lab_Theft_8:
# 201 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TEDD
	goto DR_Lab_Theft_7

DR_Lab_Theft_11:
# 255 "data/maps/PellucaUmbraLab/scripts.pory"
	trainerbattle_no_intro TRAINER_DR_EDEN_LAB_1, DR_Lab_Text_EdenDefeat
	goto DR_Lab_Theft_10

DR_Lab_Theft_14:
# 256 "data/maps/PellucaUmbraLab/scripts.pory"
	trainerbattle_no_intro TRAINER_DR_EDEN_LAB_2, DR_Lab_Text_EdenDefeat
	goto DR_Lab_Theft_13

DR_Lab_Theft_17:
# 257 "data/maps/PellucaUmbraLab/scripts.pory"
	trainerbattle_no_intro TRAINER_DR_EDEN_LAB_3, DR_Lab_Text_EdenDefeat
	goto DR_Lab_Theft_16


DR_Lab_ShardBriefing::
# 301 "data/maps/PellucaUmbraLab/scripts.pory"
	lockall
# 302 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x40A1, 4
# 303 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Lab_ShardBriefing_Movement_0
# 304 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_CADMUS, DR_Lab_Briefing_Movement_1
# 305 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 306 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 307 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 308 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_0
# 309 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 310 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 311 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_1
# 312 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 313 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_2
# 314 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_3
# 315 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_4
# 316 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 317 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 318 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_5
# 319 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 320 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_6
# 321 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 322 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 323 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_7
# 324 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 325 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_8
# 326 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 327 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 328 "data/maps/PellucaUmbraLab/scripts.pory"
	releaseall
	end


PellucaUmbraLab_EventScript_Umbra::
# 333 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 334 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 335 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 336 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x40A1, 4
	goto_if_ge PellucaUmbraLab_EventScript_Umbra_2
# 339 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox PellucaUmbraLab_EventScript_Umbra_Text_1
PellucaUmbraLab_EventScript_Umbra_1:
# 341 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 342 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 343 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

PellucaUmbraLab_EventScript_Umbra_2:
# 337 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox PellucaUmbraLab_EventScript_Umbra_Text_0
	goto PellucaUmbraLab_EventScript_Umbra_1


# 47 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Briefing_Movement_0:
# 47 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_up
# 47 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_up
	step_end

# 49 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Briefing_Movement_1:
# 49 "data/maps/PellucaUmbraLab/scripts.pory"
	face_down
	step_end

# 225 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Theft_Movement_0:
# 225 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_down
# 225 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_down
# 225 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_left
# 225 "data/maps/PellucaUmbraLab/scripts.pory"
	face_up
	step_end

# 233 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Theft_Movement_1:
# 233 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_fast_left
# 233 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_fast_up
# 233 "data/maps/PellucaUmbraLab/scripts.pory"
	face_left
	step_end

# 234 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Theft_Movement_2:
# 234 "data/maps/PellucaUmbraLab/scripts.pory"
	face_right
	step_end

# 303 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_ShardBriefing_Movement_0:
# 303 "data/maps/PellucaUmbraLab/scripts.pory"
	face_up
	step_end

DR_Lab_Briefing_Text_0:
# 53 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Welcome home, my Prince. Forgive the\n"
	.string "chaos.\p"
	.string "This lab is my personal environment, and\n"
	.string "a place where we can communicate\l"
	.string "openly, without reservations.$"

DR_Lab_Briefing_Text_1:
# 56 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Cadmus raises a hand toward your mask.$"

DR_Lab_Briefing_Text_2:
# 59 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Will you let me see your face?$"

DR_Lab_Briefing_Text_3:
# 62 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "...No. I could not bear it. It is a\n"
	.string "complete ruin.$"

DR_Lab_Briefing_Text_4:
# 66 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "...I understand. I will not press the\n"
	.string "matter.\p"
	.string "The last time you were in Pelluca, you\n"
	.string "and your sister were ten years old. You\l"
	.string "fell out of the Academy's apple tree in\l"
	.string "front of half the faculty. Do you\l"
	.string "remember?$"

DR_Lab_Briefing_Text_5:
# 69 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "I remember the tree.$"

DR_Lab_Briefing_Text_6:
# 71 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "How I miss those days.$"

DR_Lab_Briefing_Text_7:
# 73 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "But alas, let us speak about the\n"
	.string "present, and your immediate future.\p"
	.string "To the Empire, you are Nomad Alban, a\n"
	.string "Rainhawk discharged honorably due to\l"
	.string "injury and now formally reassigned to\l"
	.string "the Ministry of Education.\p"
	.string "The Academy has also named you its\n"
	.string "head of security, which mostly means no\l"
	.string "door in Pelluca Valley will be closed to\l"
	.string "you... along with most places in the\l"
	.string "Empire.$"

DR_Lab_Briefing_Text_8:
# 74 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "There is a dormitory northwest of here\n"
	.string "with your cover name on the door, the\l"
	.string "largest study on the first floor. It\l"
	.string "isn't much, but the door locks and the\l"
	.string "bed is comfy.$"

DR_Lab_Briefing_Text_9:
# 77 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "And the “real” reason I am here?$"

DR_Lab_Briefing_Text_10:
# 79 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "It is as you probably guessed. Earn the\n"
	.string "Trial Badges. All of them.\p"
	.string "A Rainhawk who holds every badge has\n"
	.string "the right to challenge the Champion.\l"
	.string "She is someone you know quite well...\l"
	.string "someone who loves you even more than I\l"
	.string "do.$"

DR_Lab_Briefing_Text_11:
# 82 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "My sister.$"

DR_Lab_Briefing_Text_12:
# 84 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Your sister. Rhydia has held the title\n"
	.string "for five years now, and she rules the\l"
	.string "Empire in your mother's name besides.\p"
	.string "A man who beats the Champion in front\n"
	.string "of the whole Empire can tell everyone\l"
	.string "who he really is, and no one will dare\l"
	.string "touch him.$"

DR_Lab_Briefing_Text_13:
# 87 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Does she know I'm here?$"

DR_Lab_Briefing_Text_14:
# 89 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "No, though in time this could change.$"

DR_Lab_Briefing_Text_15:
# 93 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Let us move on, however. What are\n"
	.string "Pokémon, to you?$"

DR_Lab_Briefing_Text_16:
# 96 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "...Assets. You keep them fed, you keep\n"
	.string "them sharp, and you use them carefully.$"

DR_Lab_Briefing_Text_17:
# 98 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Those sound like Surge's words.$"

DR_Lab_Briefing_Text_18:
# 101 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "They kept me alive.$"

DR_Lab_Briefing_Text_19:
# 103 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Certainly they did... but they also left\n"
	.string "you burned to ashes on that beach.$"

DR_Lab_Briefing_Text_20:
# 106 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Enough.\p"
	.string "Those balls behind you... are those\n"
	.string "Starter Pokémon? I thought those were\l"
	.string "only given to noble children.$"

DR_Lab_Briefing_Text_21:
# 108 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Usually. These three are different.\p"
	.string "Read the note beside each one before\n"
	.string "you choose. I wrote them myself, so\l"
	.string "forgive the handwriting.$"

DR_Lab_Briefing_Text_22:
# 111 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Choose? Me?$"

DR_Lab_Briefing_Text_23:
# 113 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Yes, you. Before you choose, however,\n"
	.string "you must take this.\p"
	.string "You'll be meeting a great many Pokémon\n"
	.string "from here on, and you should keep a\l"
	.string "record of them. I will explain in greater\l"
	.string "detail later.$"

DR_Lab_Briefing_Text_24:
# 117 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "{PLAYER} received the PokéLog!$"

DR_Lab_Briefing_Text_25:
# 122 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "The Log is merely paper and ink. It isn't\n"
	.string "elaborate, but it will serve us well.\l"
	.string "Write down each one you meet, what it is\l"
	.string "and how it fights, in your own hand.\p"
	.string "In the army, someone else wrote the\n"
	.string "reports and you read them. This time,\l"
	.string "you see each Pokémon for yourself.$"

DR_Lab_Briefing_Text_26:
# 125 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Understood.$"

DR_Lab_BallFrigibax_Text_0:
# 136 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Heraldic Frigibax.\p"
	.string "Hatched from an egg I found on Mt.\n"
	.string "Mirroh. Note the coloring. I have never\l"
	.string "seen another like it.\p"
	.string "It favors Dragon and Ice moves, though\n"
	.string "it learns a good deal more if you are\l"
	.string "patient with it.\p"
	.string "Its final form, Baxcalibur, is so rare\n"
	.string "that only one other has been recorded\l"
	.string "on this continent in two hundred years.\p"
	.string "One old text claims it can grow stronger\n"
	.string "still with the help of a special stone. I\l"
	.string "have found nothing to confirm it.$"

DR_Lab_BallFrigibax_Text_1:
# 138 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take the Heraldic Frigibax as your\n"
	.string "partner?$"

DR_Lab_BallTeddiursa_Text_0:
# 154 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Bloodmoon Teddiursa.\p"
	.string "The Blood Moon line has been rumored\n"
	.string "for over a century. I found this cub by\l"
	.string "chance a year ago, on a small wooded\l"
	.string "island far to the east.\p"
	.string "Much about it is still a mystery. What I\n"
	.string "have seen suggests a gift for special\l"
	.string "attacks and a sturdy constitution, and\l"
	.string "its moves seem to grow along the same\l"
	.string "lines.$"

DR_Lab_BallTeddiursa_Text_1:
# 156 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take the Bloodmoon Teddiursa as your\n"
	.string "partner?$"

DR_Lab_BallTinkatink_Text_0:
# 172 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Dragonmaul Tinkatink.\p"
	.string "I came across this egg in the dunes\n"
	.string "north of Mt. Ceram a few months ago, and\l"
	.string "I still can't quite believe my luck.\p"
	.string "The Tinkatink clans of Cormoria's\n"
	.string "deserts are said to share this coloring,\l"
	.string "and to learn moves suited to hunting\l"
	.string "dragons, and even other Fairy types.\p"
	.string "A colleague tells me a Cormorian\n"
	.string "Tinkaton can grow stronger still with\l"
	.string "some rare material worked into its gear.\l"
	.string "I have not been able to confirm it.$"

DR_Lab_BallTinkatink_Text_1:
# 174 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take the Dragonmaul Tinkatink as your\n"
	.string "partner?$"

DR_Lab_Theft_Text_0:
# 207 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Who put out the lamps?$"

DR_Lab_Theft_Text_1:
# 209 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Thief$"

DR_Lab_Theft_Text_2:
# 210 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Don't mind me, gentlemen. I'll only be a\n"
	.string "moment.$"

DR_Lab_Theft_Text_3:
# 212 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Put that down.$"

DR_Lab_Theft_Text_4:
# 215 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Mm, no. I came a long way for this one.$"

DR_Lab_Theft_Text_5:
# 217 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Neptune.$"

DR_Lab_Theft_Text_6:
# 230 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "So the stories about your Jousteel are\n"
	.string "true. He's bigger than I was told.\p"
	.string "Fine. I'll find another way out.$"

DR_Lab_Theft_Text_7:
# 239 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Is that a mending mask? From Athanto?\n"
	.string "That's worth more than this whole\l"
	.string "cellar. Who are you supposed to be?$"

DR_Lab_Theft_Text_8:
# 241 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Nomad Alban$"

DR_Lab_Theft_Text_9:
# 242 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Put it back.$"

DR_Lab_Theft_Text_10:
# 245 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "You'll have to take it off me. Pilfer, up!$"

DR_Lab_Theft_Text_11:
# 262 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Who are you?$"

DR_Lab_Theft_Text_12:
# 265 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Nomad Alban.$"

DR_Lab_Theft_Text_13:
# 268 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Never heard of you.$"

DR_Lab_Theft_Text_14:
# 271 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Good.$"

DR_Lab_Theft_Text_15:
# 274 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Ha! All right, Nomad Alban. I want a\n"
	.string "rematch, the minute I get out of\l"
	.string "whatever hole they're about to put me\l"
	.string "in.$"

DR_Lab_Theft_Text_16:
# 276 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "You'll find it a very deep hole.$"

DR_Lab_ShardBriefing_Text_0:
# 308 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "She knew where to look, and she knew\n"
	.string "exactly what to take. Someone told her\l"
	.string "both.$"

DR_Lab_ShardBriefing_Text_1:
# 311 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Someone who knew I was coming.$"

DR_Lab_ShardBriefing_Text_2:
# 313 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Or someone who knew I was preparing for\n"
	.string "someone. Either way, I can't put off\l"
	.string "telling you about the other half of\l"
	.string "your work.$"

DR_Lab_ShardBriefing_Text_3:
# 314 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Cormoria once had a Mega-Dreamstone.\n"
	.string "The old tales call it the heart of the\l"
	.string "Empire. I understand it less than I\l"
	.string "would like, but I am certain it matters.\p"
	.string "It was shattered long ago. A friend of\n"
	.string "mine, whose name you don't need, has\l"
	.string "found where nine of the pieces came to\l"
	.string "rest.$"

DR_Lab_ShardBriefing_Text_4:
# 315 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "There are cults in Cormoria, more of\n"
	.string "them every year, and two of them want\l"
	.string "those pieces as badly as I do. If they\l"
	.string "reach them first, I don't think either\l"
	.string "of us will like what they wake up.$"

DR_Lab_ShardBriefing_Text_5:
# 318 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "And the badges?$"

DR_Lab_ShardBriefing_Text_6:
# 320 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "The badges are why no one will ask what\n"
	.string "you are doing on a mountain. A Rainhawk\l"
	.string "chasing Trials can go anywhere he likes.\p"
	.string "Bring the pieces to me. I know someone\n"
	.string "who can make the stone whole again.$"

DR_Lab_ShardBriefing_Text_7:
# 323 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Where do I start?$"

DR_Lab_ShardBriefing_Text_8:
# 325 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "West, past Route 11, toward Mirroh.\n"
	.string "Kimaris Langerin oversees the first\l"
	.string "Trial there, and there are rumors of a\l"
	.string "piece on the mountain above it.\p"
	.string "But take a day in the valley first.\n"
	.string "Learn your partner's habits before\l"
	.string "someone tests them for you.$"

PellucaUmbraLab_EventScript_Umbra_Text_0:
# 337 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "The valley first, then Mirroh. And sleep,\n"
	.string "if you can manage it.$"

PellucaUmbraLab_EventScript_Umbra_Text_1:
# 339 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take your time. They have waited this\n"
	.string "long.$"

DR_Lab_Text_EdenDefeat::
# 293 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Five minutes with that Pokémon and you\n"
	.string "fight like you've had it for years. Who\l"
	.string "taught you that?$"
