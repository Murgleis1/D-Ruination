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
# 24 "data/maps/PellucaUmbraLab/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION
# 37 "data/maps/PellucaUmbraLab/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 25 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x886
# 26 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x887
# 27 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x88E
# 30 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x40A1, 1
	goto_if_le PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_2
# 33 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x885
PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_1:
	return

PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_2:
# 31 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x885
	goto PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_TRANSITION_1

PellucaUmbraLab_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 38 "data/maps/PellucaUmbraLab/scripts.pory"
	map_script_2 VAR_UNUSED_0x40A1, 0, DR_Lab_Briefing
# 39 "data/maps/PellucaUmbraLab/scripts.pory"
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
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 68 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_5
# 69 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 70 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 71 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_6
# 72 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 73 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_7
# 74 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 75 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_8
# 76 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_9
# 77 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 78 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 79 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_10
# 80 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 81 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_11
# 82 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_12
# 83 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 84 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 85 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_13
# 86 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 87 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_14
# 88 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 89 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 90 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_15
# 91 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 92 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_16
# 93 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 94 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 40
# 95 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 96 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_17
# 97 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 98 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 99 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_18
# 100 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 101 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_19
# 102 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 103 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 104 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_20
# 105 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 106 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_21
# 107 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 108 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 109 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_22
# 110 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 111 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_23
# 112 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 113 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 114 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_24
# 115 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 116 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_25
# 117 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 118 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 119 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_26
# 120 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 121 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_27
# 122 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 123 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 124 "data/maps/PellucaUmbraLab/scripts.pory"
	playfanfare MUS_OBTAIN_ITEM
# 125 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_28
# 126 "data/maps/PellucaUmbraLab/scripts.pory"
	waitfanfare
# 127 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_SYS_POKEDEX_GET
# 128 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 129 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 130 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_29
# 131 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 132 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 133 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_30
# 134 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 135 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Briefing_Text_31
# 136 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 137 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 138 "data/maps/PellucaUmbraLab/scripts.pory"
	releaseall
	end


DR_Lab_BallFrigibax::
# 143 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 144 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 145 "data/maps/PellucaUmbraLab/scripts.pory"
	showmonpicshiny SPECIES_FRIGIBAX, 10, 3
# 146 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallFrigibax_Text_0
# 147 "data/maps/PellucaUmbraLab/scripts.pory"
	hidemonpic
# 148 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallFrigibax_Text_1, MSGBOX_YESNO
# 149 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq DR_Lab_BallFrigibax_2
DR_Lab_BallFrigibax_1:
# 156 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

DR_Lab_BallFrigibax_2:
# 150 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x4083, 1
# 151 "data/maps/PellucaUmbraLab/scripts.pory"
	givemon SPECIES_FRIGIBAX, 5, item = ITEM_SITRUS_BERRY, isShiny = TRUE
# 152 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_FRIG
# 153 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 154 "data/maps/PellucaUmbraLab/scripts.pory"
	goto DR_Lab_Theft
	goto DR_Lab_BallFrigibax_1


DR_Lab_BallTeddiursa::
# 161 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 162 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 163 "data/maps/PellucaUmbraLab/scripts.pory"
	showmonpic SPECIES_TEDDIURSA, 10, 3
# 164 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTeddiursa_Text_0
# 165 "data/maps/PellucaUmbraLab/scripts.pory"
	hidemonpic
# 166 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTeddiursa_Text_1, MSGBOX_YESNO
# 167 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq DR_Lab_BallTeddiursa_2
DR_Lab_BallTeddiursa_1:
# 174 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

DR_Lab_BallTeddiursa_2:
# 168 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x4083, 2
# 169 "data/maps/PellucaUmbraLab/scripts.pory"
	givemon SPECIES_TEDDIURSA, 5, item = ITEM_SITRUS_BERRY
# 170 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TEDD
# 171 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 172 "data/maps/PellucaUmbraLab/scripts.pory"
	goto DR_Lab_Theft
	goto DR_Lab_BallTeddiursa_1


DR_Lab_BallTinkatink::
# 179 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 180 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 181 "data/maps/PellucaUmbraLab/scripts.pory"
	showmonpic SPECIES_TINKATINK, 10, 3
# 182 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTinkatink_Text_0
# 183 "data/maps/PellucaUmbraLab/scripts.pory"
	hidemonpic
# 184 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_BallTinkatink_Text_1, MSGBOX_YESNO
# 185 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq DR_Lab_BallTinkatink_2
DR_Lab_BallTinkatink_1:
# 192 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

DR_Lab_BallTinkatink_2:
# 186 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x4083, 3
# 187 "data/maps/PellucaUmbraLab/scripts.pory"
	givemon SPECIES_TINKATINK, 5, item = ITEM_SITRUS_BERRY
# 188 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TINK
# 189 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 190 "data/maps/PellucaUmbraLab/scripts.pory"
	goto DR_Lab_Theft
	goto DR_Lab_BallTinkatink_1


DR_Lab_Theft::
# 197 "data/maps/PellucaUmbraLab/scripts.pory"
	lockall
# 198 "data/maps/PellucaUmbraLab/scripts.pory"
	additem ITEM_POTION, 1
# 199 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x40A1, 2
# 200 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_SYS_POKEMON_GET
# 201 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 202 "data/maps/PellucaUmbraLab/scripts.pory"
	fadeoutbgm 4
# 203 "data/maps/PellucaUmbraLab/scripts.pory"
	fadescreen FADE_TO_BLACK
# 204 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 45
# 205 "data/maps/PellucaUmbraLab/scripts.pory"
	setobjectxy OBJ_EVENT_ID_PLAYER, 4, 10
# 206 "data/maps/PellucaUmbraLab/scripts.pory"
	turnobject OBJ_EVENT_ID_PLAYER, DIR_NORTH
# 207 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x886
# 208 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_EDEN
# 209 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 1
	goto_if_eq DR_Lab_Theft_2
DR_Lab_Theft_1:
# 210 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 2
	goto_if_eq DR_Lab_Theft_5
DR_Lab_Theft_4:
# 211 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 3
	goto_if_eq DR_Lab_Theft_8
DR_Lab_Theft_7:
# 212 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 45
# 213 "data/maps/PellucaUmbraLab/scripts.pory"
	fadescreen FADE_FROM_BLACK
# 214 "data/maps/PellucaUmbraLab/scripts.pory"
	playbgm MUS_ENCOUNTER_AQUA, FALSE
# 215 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 40
# 216 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 217 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_0
# 218 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 219 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 220 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_2
# 221 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 222 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_3
# 223 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 224 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 225 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_4
# 226 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 227 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_5
# 228 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 229 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 230 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x887
# 231 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_NEPTUNE
# 232 "data/maps/PellucaUmbraLab/scripts.pory"
	playmoncry SPECIES_JOUSTEEL, CRY_MODE_NORMAL
# 233 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmoncry
# 234 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 16
# 235 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_NEPTUNE, DR_Lab_Theft_Movement_0
# 236 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 237 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 238 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_6
# 239 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 240 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 241 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 242 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_7
# 243 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 244 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 245 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_8
# 246 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 247 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_9
# 248 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_10
# 249 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 250 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_11
# 251 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 252 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 253 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_12
# 254 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_13
# 255 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 256 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_14
# 257 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 258 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_15
# 259 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 260 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 261 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Lab_Theft_Movement_1
# 262 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_EDEN, DR_Lab_Theft_Movement_2
# 263 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 264 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 12
# 265 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_16
# 266 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 267 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 268 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 269 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_17
# 270 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 271 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 272 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_18
# 273 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 274 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_19
# 275 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_20
# 276 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 277 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 278 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_21
# 279 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 280 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 281 "data/maps/PellucaUmbraLab/scripts.pory"
	clearflag FLAG_UNUSED_0x88E
# 282 "data/maps/PellucaUmbraLab/scripts.pory"
	addobject LOCALID_DRL_PILFER
# 283 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_PILFER, DR_Lab_Theft_Movement_2
# 284 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 285 "data/maps/PellucaUmbraLab/scripts.pory"
	playmoncry SPECIES_NICKIT, CRY_MODE_NORMAL
# 286 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmoncry
# 287 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 288 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 1
	goto_if_eq DR_Lab_Theft_11
DR_Lab_Theft_10:
# 289 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 2
	goto_if_eq DR_Lab_Theft_14
DR_Lab_Theft_13:
# 290 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x4083, 3
	goto_if_eq DR_Lab_Theft_17
DR_Lab_Theft_16:
# 291 "data/maps/PellucaUmbraLab/scripts.pory"
	lockall
# 292 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 293 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 294 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 295 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_22
# 296 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 297 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_19
# 298 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_23
# 299 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_NEUTRAL
# 300 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 301 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_24
# 302 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 303 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_19
# 304 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_25
# 305 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_EDEN, PORTRAIT_EXPR_POSITIVE
# 306 "data/maps/PellucaUmbraLab/scripts.pory"
	speakername DR_Lab_Theft_Text_1
# 307 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_26
# 308 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 309 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_Theft_Text_27
# 310 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 311 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 312 "data/maps/PellucaUmbraLab/scripts.pory"
	playmoncry SPECIES_JOUSTEEL, CRY_MODE_NORMAL
# 313 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmoncry
# 314 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 30
# 315 "data/maps/PellucaUmbraLab/scripts.pory"
	fadescreen FADE_TO_BLACK
# 316 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x885
# 317 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x886
# 318 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x887
# 319 "data/maps/PellucaUmbraLab/scripts.pory"
	setflag FLAG_UNUSED_0x88E
# 320 "data/maps/PellucaUmbraLab/scripts.pory"
	warp MAP_PELLUCA_TEMPLAR_MONASTERY, 6, 6
# 321 "data/maps/PellucaUmbraLab/scripts.pory"
	waitstate
# 322 "data/maps/PellucaUmbraLab/scripts.pory"
	releaseall
	end

DR_Lab_Theft_2:
# 209 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TINK
	goto DR_Lab_Theft_1

DR_Lab_Theft_5:
# 210 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_FRIG
	goto DR_Lab_Theft_4

DR_Lab_Theft_8:
# 211 "data/maps/PellucaUmbraLab/scripts.pory"
	removeobject LOCALID_DRL_BALL_TEDD
	goto DR_Lab_Theft_7

DR_Lab_Theft_11:
# 288 "data/maps/PellucaUmbraLab/scripts.pory"
	trainerbattle_no_intro TRAINER_DR_EDEN_LAB_1, DR_Lab_Text_EdenDefeat
	goto DR_Lab_Theft_10

DR_Lab_Theft_14:
# 289 "data/maps/PellucaUmbraLab/scripts.pory"
	trainerbattle_no_intro TRAINER_DR_EDEN_LAB_2, DR_Lab_Text_EdenDefeat
	goto DR_Lab_Theft_13

DR_Lab_Theft_17:
# 290 "data/maps/PellucaUmbraLab/scripts.pory"
	trainerbattle_no_intro TRAINER_DR_EDEN_LAB_3, DR_Lab_Text_EdenDefeat
	goto DR_Lab_Theft_16


DR_Lab_ShardBriefing::
# 334 "data/maps/PellucaUmbraLab/scripts.pory"
	lockall
# 335 "data/maps/PellucaUmbraLab/scripts.pory"
	setvar VAR_UNUSED_0x40A1, 4
# 336 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_Lab_ShardBriefing_Movement_0
# 337 "data/maps/PellucaUmbraLab/scripts.pory"
	applymovement LOCALID_DRL_CADMUS, DR_Lab_Briefing_Movement_1
# 338 "data/maps/PellucaUmbraLab/scripts.pory"
	waitmovement 0
# 339 "data/maps/PellucaUmbraLab/scripts.pory"
	delay 20
# 340 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 341 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_0
# 342 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 343 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 344 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_1
# 345 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 346 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_2
# 347 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_3
# 348 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_4
# 349 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_5
# 350 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 351 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 352 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_6
# 353 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 354 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_7
# 355 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_8
# 356 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 357 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_9
# 358 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 359 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 360 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_10
# 361 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 362 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_11
# 363 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_12
# 364 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 365 "data/maps/PellucaUmbraLab/scripts.pory"
	special DrSetPrinceNameplate
# 366 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_13
# 367 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 368 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_14
# 369 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 370 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox DR_Lab_ShardBriefing_Text_15
# 371 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 372 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 373 "data/maps/PellucaUmbraLab/scripts.pory"
	releaseall
	end


PellucaUmbraLab_EventScript_Umbra::
# 378 "data/maps/PellucaUmbraLab/scripts.pory"
	lock
# 379 "data/maps/PellucaUmbraLab/scripts.pory"
	faceplayer
# 380 "data/maps/PellucaUmbraLab/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 381 "data/maps/PellucaUmbraLab/scripts.pory"
	compare VAR_UNUSED_0x40A1, 4
	goto_if_ge PellucaUmbraLab_EventScript_Umbra_2
# 384 "data/maps/PellucaUmbraLab/scripts.pory"
	msgbox PellucaUmbraLab_EventScript_Umbra_Text_1
PellucaUmbraLab_EventScript_Umbra_1:
# 386 "data/maps/PellucaUmbraLab/scripts.pory"
	hideportrait
# 387 "data/maps/PellucaUmbraLab/scripts.pory"
	closemessage
# 388 "data/maps/PellucaUmbraLab/scripts.pory"
	release
	end

PellucaUmbraLab_EventScript_Umbra_2:
# 382 "data/maps/PellucaUmbraLab/scripts.pory"
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

# 235 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Theft_Movement_0:
# 235 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_down
# 235 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_down
# 235 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_left
# 235 "data/maps/PellucaUmbraLab/scripts.pory"
	face_up
	step_end

# 261 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Theft_Movement_1:
# 261 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_fast_left
# 261 "data/maps/PellucaUmbraLab/scripts.pory"
	walk_fast_up
# 261 "data/maps/PellucaUmbraLab/scripts.pory"
	face_left
	step_end

# 262 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_Theft_Movement_2:
# 262 "data/maps/PellucaUmbraLab/scripts.pory"
	face_right
	step_end

# 336 "data/maps/PellucaUmbraLab/scripts.pory"
DR_Lab_ShardBriefing_Movement_0:
# 336 "data/maps/PellucaUmbraLab/scripts.pory"
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
	.string "...No. I can't. It is a complete ruin.$"

DR_Lab_Briefing_Text_4:
# 66 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "...If that is how you feel now, I will not\n"
	.string "press the matter further.$"

DR_Lab_Briefing_Text_5:
# 68 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Being here together after all this\n"
	.string "time... it fills my heart with joy.\p"
	.string "The last time you were in Pelluca, you\n"
	.string "and your sister were ten years old. You\l"
	.string "fell out of the Academy's apple tree in\l"
	.string "front of half the faculty. Do you\l"
	.string "remember?$"

DR_Lab_Briefing_Text_6:
# 71 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "I remember the tree. Rhydia wouldn't\n"
	.string "stop laughing.$"

DR_Lab_Briefing_Text_7:
# 73 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "How I miss those days...$"

DR_Lab_Briefing_Text_8:
# 75 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "But alas, let us speak about the\n"
	.string "present, and your immediate future.\p"
	.string "To the Empire right now, you are Nomad\n"
	.string "Alban, a Rainhawk discharged honorably\l"
	.string "due to injury and now formally\l"
	.string "reassigned to the Ministry of\l"
	.string "Education.\p"
	.string "The Academy has also named you its\n"
	.string "head of security, which mostly means no\l"
	.string "door in Pelluca Valley will be closed to\l"
	.string "you. And under my authority, most\l"
	.string "places in the Empire are open to you as\l"
	.string "well.$"

DR_Lab_Briefing_Text_9:
# 76 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "There is a dormitory northwest of here\n"
	.string "with your cover name on the door, the\l"
	.string "largest study on the first floor. It\l"
	.string "isn't much, but the door locks and the\l"
	.string "bed is comfy.$"

DR_Lab_Briefing_Text_10:
# 79 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "That's all well and good. But why, after\n"
	.string "ten years, did you finally bring me\l"
	.string "home? After Father's assassination, I\l"
	.string "thought-$"

DR_Lab_Briefing_Text_11:
# 81 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Because there was too much back then I\n"
	.string "didn't know... only that you were the\l"
	.string "next target.\p"
	.string "I barely had the political means to\n"
	.string "protect your sister and mother, and I\l"
	.string "needed to take drastic measures to\l"
	.string "hide you, which is why my agents and I\l"
	.string "established a false identity for you\l"
	.string "and sent you overseas.\p"
	.string "But now... I have a clearer idea of what\n"
	.string "is happening in Cormoria, and of who I\l"
	.string "believe killed your father.\p"
	.string "The time was right to bring you home,\n"
	.string "though I wish to Arceus it were under\l"
	.string "better circumstances.$"

DR_Lab_Briefing_Text_12:
# 82 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "So, you have two missions, and we will\n"
	.string "discuss the first now.\p"
	.string "A Rainhawk who clears every Trial has\n"
	.string "the right to challenge the Champion.\l"
	.string "She is someone you know quite well...\l"
	.string "someone who loves you even more than I\l"
	.string "do.$"

DR_Lab_Briefing_Text_13:
# 85 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "My sister, huh. She got her starter\n"
	.string "right before you sent me away, if I\l"
	.string "recall.$"

DR_Lab_Briefing_Text_14:
# 87 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Your sister. Rhydia has held the\n"
	.string "Champion title for five years now, and\l"
	.string "she rules the Empire in your mother's\l"
	.string "name besides.\p"
	.string "She is one of the most talented\n"
	.string "Trainers we have seen in generations,\l"
	.string "but our enemies are closing in... I\l"
	.string "believe her power will not be enough to\l"
	.string "save Cormoria.\p"
	.string "A man who beats the Champion in front\n"
	.string "of the whole Empire can tell everyone\l"
	.string "who he really is, and no one will dare\l"
	.string "touch him at that point.$"

DR_Lab_Briefing_Text_15:
# 90 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Does Rhydia know I'm here? What about\n"
	.string "my mother?$"

DR_Lab_Briefing_Text_16:
# 92 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Neither of them does, though we will\n"
	.string "make sure they know when the time is\l"
	.string "right.$"

DR_Lab_Briefing_Text_17:
# 96 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Let us move on, however, to the most\n"
	.string "critical topic.\p"
	.string "My Prince... what are Pokémon to you?$"

DR_Lab_Briefing_Text_18:
# 99 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "...Tools. You keep them fed, you keep\n"
	.string "them sharp, and you use them carefully\l"
	.string "to control outcomes upon the\l"
	.string "battlefield.$"

DR_Lab_Briefing_Text_19:
# 101 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Those sound like Surge's words.$"

DR_Lab_Briefing_Text_20:
# 104 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "They kept me alive.$"

DR_Lab_Briefing_Text_21:
# 106 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Certainly they did... but they also left\n"
	.string "you burned to ashes on that beach.$"

DR_Lab_Briefing_Text_22:
# 109 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Enough debate.\p"
	.string "Those balls behind you... are those\n"
	.string "starter Pokémon? I thought those were\l"
	.string "only given to noble children.$"

DR_Lab_Briefing_Text_23:
# 111 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Usually. These three are different, and\n"
	.string "all are one of a kind.\p"
	.string "One of them shall be your first step\n"
	.string "toward becoming who you were always\l"
	.string "meant to be.$"

DR_Lab_Briefing_Text_24:
# 114 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "It feels surreal to be able to choose a\n"
	.string "partner of my own at twenty. If things\l"
	.string "had been different, I would have gotten\l"
	.string "my own before I was sent away...$"

DR_Lab_Briefing_Text_25:
# 116 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "We cannot change the past, my Prince,\n"
	.string "but perhaps there is a silver lining...\p"
	.string "In any case, read the note beside each\n"
	.string "one before you choose. I wrote them\l"
	.string "myself, so forgive the handwriting.$"

DR_Lab_Briefing_Text_26:
# 119 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "I will.$"

DR_Lab_Briefing_Text_27:
# 121 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Also, before you choose, please take\n"
	.string "this.\p"
	.string "You'll be meeting a great many Pokémon\n"
	.string "from here on, and you should keep a\l"
	.string "record of them. I will explain in greater\l"
	.string "detail later.$"

DR_Lab_Briefing_Text_28:
# 125 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "{PLAYER} received the PokéLog!$"

DR_Lab_Briefing_Text_29:
# 130 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "The Log is standard for all new Trainers\n"
	.string "in the current era. It isn't elaborate,\l"
	.string "but it will serve us well.\p"
	.string "Write down each one you meet, what it is\n"
	.string "and how it fights, in your own hand. It\l"
	.string "also features the latest map of the\l"
	.string "region, right before the index.$"

DR_Lab_Briefing_Text_30:
# 133 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Thank you. I will choose now.$"

DR_Lab_Briefing_Text_31:
# 135 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Proceed, my Lord. This is an important\n"
	.string "choice.$"

DR_Lab_BallFrigibax_Text_0:
# 146 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Heraldic Frigibax.\p"
	.string "I hatched this one from an egg I found\n"
	.string "on Mt. Mirroh. Note its coloring. In all\l"
	.string "my years I have never seen another like\l"
	.string "it.\p"
	.string "It favors Dragon and Ice moves, though\n"
	.string "it will learn a great deal more if you are\l"
	.string "patient with it.\p"
	.string "Its final form, Baxcalibur, is so rare\n"
	.string "that only one other has been recorded\l"
	.string "on this continent in two hundred years.\p"
	.string "One old text claims it can grow stronger\n"
	.string "still with the help of a special stone. I\l"
	.string "have yet to find any proof that\l"
	.string "confirms this, however.$"

DR_Lab_BallFrigibax_Text_1:
# 148 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take the Heraldic Frigibax as your\n"
	.string "partner?$"

DR_Lab_BallTeddiursa_Text_0:
# 164 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Bloodmoon Teddiursa.\p"
	.string "Whispers of a Blood Moon line have\n"
	.string "circulated for over a century. I found\l"
	.string "this cub by pure chance a year ago, on a\l"
	.string "small wooded island far to the east.\p"
	.string "Much about it is still a mystery. What I\n"
	.string "have seen so far suggests a gift for\l"
	.string "special attacks and a sturdy\l"
	.string "constitution, and its moves seem to\l"
	.string "grow along the same lines.$"

DR_Lab_BallTeddiursa_Text_1:
# 166 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take the Bloodmoon Teddiursa as your\n"
	.string "partner?$"

DR_Lab_BallTinkatink_Text_0:
# 182 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Dragonmaul Tinkatink.\p"
	.string "I came across this egg in the dunes\n"
	.string "north of Mt. Ceram a few months ago, and\l"
	.string "I still can scarcely believe my luck.\p"
	.string "The Tinkatink clans of Cormoria's\n"
	.string "deserts are said to share this coloring,\l"
	.string "and to learn moves suited to hunting\l"
	.string "dragons, and even other Fairy types.\p"
	.string "A colleague tells me these clans can\n"
	.string "grow stronger still with some rare\l"
	.string "material worked into their gear. I have\l"
	.string "not been able to confirm it.$"

DR_Lab_BallTinkatink_Text_1:
# 184 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take the Dragonmaul Tinkatink as your\n"
	.string "partner?$"

DR_Lab_Theft_Text_0:
# 217 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "...The lamps just went out. It seems we\n"
	.string "have an uninvited guest.$"

DR_Lab_Theft_Text_1:
# 219 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Thief$"

DR_Lab_Theft_Text_2:
# 220 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Don't mind me, gentlemen. This won't\n"
	.string "take long.$"

DR_Lab_Theft_Text_3:
# 222 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "There is nowhere for you to go, little\n"
	.string "thief.$"

DR_Lab_Theft_Text_4:
# 225 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Mmm... I have my ways. But I have what I\n"
	.string "need now, so I'll just-$"

DR_Lab_Theft_Text_5:
# 227 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Neptune. Bar the door, and keep one eye\n"
	.string "on the window. If she runs, pin her.\l"
	.string "Gently.$"

DR_Lab_Theft_Text_6:
# 238 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Neptune, Cadmus's Jousteel, takes the\n"
	.string "doorway. The room suddenly feels much\l"
	.string "smaller.$"

DR_Lab_Theft_Text_7:
# 242 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "...Nobody said anything about a\n"
	.string "Jousteel...$"

DR_Lab_Theft_Text_8:
# 245 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "...But it doesn't matter. Lay a hand on\n"
	.string "me and you'll have a lot of explaining to\l"
	.string "do, Vizier. Bigger people than you want\l"
	.string "this delivered.$"

DR_Lab_Theft_Text_9:
# 247 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Bigger people, you say? No person\n"
	.string "stands above my authority except the\l"
	.string "Empress, child.$"

DR_Lab_Theft_Text_10:
# 248 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Unless... hmm. Could this be...?$"

DR_Lab_Theft_Text_11:
# 250 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "How kind of THEM to drop a lead right\n"
	.string "into my lap.$"

DR_Lab_Theft_Text_12:
# 253 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "......$"

DR_Lab_Theft_Text_13:
# 254 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "I... I work alone, Vizier.$"

DR_Lab_Theft_Text_14:
# 256 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Of course you do. I'm looking forward to\n"
	.string "hearing ALL about it.$"

DR_Lab_Theft_Text_15:
# 258 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Rainhawk, our guest seems eager to\n"
	.string "test herself. Would you oblige her?\l"
	.string "Consider it your first lesson with your\l"
	.string "new partner. Neptune and I will mind the\l"
	.string "door.$"

DR_Lab_Theft_Text_16:
# 265 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "You step between the thief and the\n"
	.string "table.$"

DR_Lab_Theft_Text_17:
# 269 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "...And nobody said anything about a\n"
	.string "soldier, either.$"

DR_Lab_Theft_Text_18:
# 272 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Who might you be? Is that a mending\n"
	.string "mask? From Athanto? That's worth more\l"
	.string "than this whole lab.$"

DR_Lab_Theft_Text_19:
# 274 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Nomad Alban$"

DR_Lab_Theft_Text_20:
# 275 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Put the ball back and surrender quietly.$"

DR_Lab_Theft_Text_21:
# 278 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "If you want it so badly, come and take\n"
	.string "it. Pilfer, up!$"

DR_Lab_Theft_Text_22:
# 295 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "How did you crush me so easily? I even\n"
	.string "picked the starter that was strong\l"
	.string "against yours!\p"
	.string "Who are you? No... WHAT are you?$"

DR_Lab_Theft_Text_23:
# 298 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Nomad Alban. I'm the youngest Rainhawk\n"
	.string "in history.$"

DR_Lab_Theft_Text_24:
# 301 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Never heard of you!$"

DR_Lab_Theft_Text_25:
# 304 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "That's fine. I've never heard of you\n"
	.string "either.$"

DR_Lab_Theft_Text_26:
# 307 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Hah... you've got a sharp tongue on you,\n"
	.string "Nomad. Just know that people like me\l"
	.string "don't stay in cells for long.\p"
	.string "And when I'm out, I want a rematch...\n"
	.string "with relish.$"

DR_Lab_Theft_Text_27:
# 309 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "A rematch that will never happen. The\n"
	.string "Templars keep their holes very deep,\l"
	.string "and very dark. And they are not known\l"
	.string "for their mercy.\p"
	.string "Neptune, our guest is leaving. Escort\n"
	.string "her.$"

DR_Lab_ShardBriefing_Text_0:
# 341 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "That girl knew exactly where to look,\n"
	.string "and exactly what to take. Someone\l"
	.string "knows more about this place than they\l"
	.string "should.\p"
	.string "But just how could that be...$"

DR_Lab_ShardBriefing_Text_1:
# 344 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Someone who knew I was coming?$"

DR_Lab_ShardBriefing_Text_2:
# 346 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Or someone who knew I was preparing for\n"
	.string "someone. Either way... I can no longer\l"
	.string "put off telling you about your... other\l"
	.string "mission. And this one is even more\l"
	.string "important than the Trials.$"

DR_Lab_ShardBriefing_Text_3:
# 347 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Long ago, Cormoria possessed three\n"
	.string "great treasures... the Mega\l"
	.string "Dreamstones. The old tales called them\l"
	.string "the Legacy of Cormor.\p"
	.string "I confess I understand the why of it\n"
	.string "less than I would like, but the\l"
	.string "significance is quite telling.$"

DR_Lab_ShardBriefing_Text_4:
# 348 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "In any case... one of these stones was\n"
	.string "shattered at some point in the past. A\l"
	.string "friend of mine, whose name you are\l"
	.string "better off not knowing, has learned\l"
	.string "where its nine pieces came to rest.$"

DR_Lab_ShardBriefing_Text_5:
# 349 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "There are powerful cults in Cormoria.\n"
	.string "Two of them want those pieces for\l"
	.string "reasons I am unsure of, but based on\l"
	.string "what I have learned in the past\l"
	.string "decade... they are not planning\l"
	.string "anything good.\p"
	.string "If they reach the shards first... I fear\n"
	.string "neither of us will like what they\l"
	.string "awaken.$"

DR_Lab_ShardBriefing_Text_6:
# 352 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "And the Trials?$"

DR_Lab_ShardBriefing_Text_7:
# 354 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Besides serving as a path for you to\n"
	.string "reveal your identity, and a means to\l"
	.string "grow into your potential as a Trainer,\l"
	.string "the Trials are the reason no one will\l"
	.string "question what a Rainhawk is doing on a\l"
	.string "mountaintop, and my name never has to\l"
	.string "come up.\p"
	.string "A Trial challenger can go almost\n"
	.string "anywhere he pleases.$"

DR_Lab_ShardBriefing_Text_8:
# 355 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Your second mission, therefore, is\n"
	.string "ultimately simple. Bring the pieces to\l"
	.string "me... and do it quietly, without\l"
	.string "attracting unneeded attention.$"

DR_Lab_ShardBriefing_Text_9:
# 357 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Which means no more announcing\n"
	.string "yourself to thieves as the youngest\l"
	.string "Rainhawk in history.$"

DR_Lab_ShardBriefing_Text_10:
# 360 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "...She asked.$"

DR_Lab_ShardBriefing_Text_11:
# 362 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "I know someone who can make the stone\n"
	.string "whole again, and keep the cults from\l"
	.string "taking control of it.$"

DR_Lab_ShardBriefing_Text_12:
# 363 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "That is also what the PokéLog is for.\n"
	.string "Every Pokémon you record tells me where\l"
	.string "you have been and what lives there.\p"
	.string "If a shard is nearby, the Pokémon there\n"
	.string "will be affected in various ways. I have\l"
	.string "quite a few potential leads as well, but\l"
	.string "you are not yet strong enough to\l"
	.string "pursue them.$"

DR_Lab_ShardBriefing_Text_13:
# 366 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Where do I begin? Surely there must be\n"
	.string "something I can do, even if I'm\l"
	.string "currently a novice Trainer.$"

DR_Lab_ShardBriefing_Text_14:
# 368 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "West, past Route 11, toward Mirroh.\n"
	.string "Kimaris Langerin oversees the first\l"
	.string "Trial there, and there are rumors of a\l"
	.string "piece on the mountain above it.$"

DR_Lab_ShardBriefing_Text_15:
# 370 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "But first, take a day to settle in. See\n"
	.string "the valley, and get to know your new\l"
	.string "partner. Learn its habits before\l"
	.string "someone else tests them for you.$"

PellucaUmbraLab_EventScript_Umbra_Text_0:
# 382 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "The valley first, then Mirroh. And do try\n"
	.string "to get some sleep.$"

PellucaUmbraLab_EventScript_Umbra_Text_1:
# 384 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Take your time. This is an important\n"
	.string "choice.$"

DR_Lab_Text_EdenDefeat::
# 326 "data/maps/PellucaUmbraLab/scripts.pory"
	.string "Wh-what? You've had that Pokémon for\n"
	.string "less than two minutes!$"
