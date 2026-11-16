# 1 "data/maps/PellucaCity/scripts.pory"

# 2 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_GAB, 5
# 3 "data/maps/PellucaCity/scripts.pory"

# 4 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_MAYOR, 39
# 5 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_S1, 40
# 6 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_S2, 41
# 7 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_S3, 42
# 8 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_S_ENTRANCE, 8
# 9 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_S_BLOCKER, 7
# 10 "data/maps/PellucaCity/scripts.pory"

# 11 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_FL_MAYOR, 50
# 12 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_FL_QWIL, 49
# 13 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_FL_CITIZEN, 47
# 14 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_FL_JANIA, 56
# 15 "data/maps/PellucaCity/scripts.pory"

# 16 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_DR_TIDAL, 21
# 17 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_DR_CADMUS, 22

PellucaCity_MapScripts::
# 22 "data/maps/PellucaCity/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaCity_MapScripts_MAP_SCRIPT_ON_TRANSITION
# 25 "data/maps/PellucaCity/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaCity_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaCity_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 23 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_VISITED_PELLUCA_CITY
	return

PellucaCity_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 26 "data/maps/PellucaCity/scripts.pory"
	map_script_2 VAR_UNUSED_0x404E, 1, DR_PellucaCity_Arrival
	.2byte 0


PellucaCity_SetLayout::
# 31 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCity_SetLayout_2
# 36 "data/maps/PellucaCity/scripts.pory"
	setmaplayoutindex LAYOUT_PELLUCA_CITY
PellucaCity_SetLayout_1:
	return

PellucaCity_SetLayout_2:
# 32 "data/maps/PellucaCity/scripts.pory"
	setmaplayoutindex LAYOUT_PELLUCA_CITY_FLOODED
# 33 "data/maps/PellucaCity/scripts.pory"
	setweather WEATHER_RAIN_THUNDERSTORM
# 34 "data/maps/PellucaCity/scripts.pory"
	doweather
	goto PellucaCity_SetLayout_1


PellucaCity_MayorFight_Trigger::
# 51 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_MAYOR_FIGHT, PellucaCity_MayorFight_Trigger_2
# 53 "data/maps/PellucaCity/scripts.pory"
	lockall
# 56 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 57 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCity_MayorFight_Trigger_Movement_0
# 58 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 59 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 62 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_1
# 63 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 64 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 65 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 66 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_1
# 67 "data/maps/PellucaCity/scripts.pory"
	release
# 68 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 70 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_2
# 71 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 72 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 73 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 74 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_3
# 75 "data/maps/PellucaCity/scripts.pory"
	release
# 76 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 78 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_3
# 79 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 80 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 81 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 82 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_4
# 83 "data/maps/PellucaCity/scripts.pory"
	release
# 84 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 86 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_4
# 87 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 88 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 89 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 90 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_6
# 91 "data/maps/PellucaCity/scripts.pory"
	release
# 92 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 94 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_5
# 95 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 96 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 97 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 98 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_7
# 99 "data/maps/PellucaCity/scripts.pory"
	release
# 100 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 102 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_6
# 103 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_6
# 104 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 105 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 106 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_8
# 107 "data/maps/PellucaCity/scripts.pory"
	release
# 108 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 110 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_7
# 111 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 112 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 113 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 114 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_9
# 115 "data/maps/PellucaCity/scripts.pory"
	release
# 116 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 118 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_7
# 119 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 120 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 121 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_8
# 128 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 129 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 131 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 132 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_10
# 133 "data/maps/PellucaCity/scripts.pory"
	release
# 134 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 136 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_6
# 137 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_6
# 138 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 139 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 140 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_11
# 141 "data/maps/PellucaCity/scripts.pory"
	release
# 142 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 144 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_7
# 145 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 146 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 147 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 148 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_12
# 149 "data/maps/PellucaCity/scripts.pory"
	release
# 150 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 153 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_9
# 154 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 155 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_9
# 156 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_10
# 157 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 158 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_9
# 159 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_9
# 160 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_11
# 161 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 162 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_12
# 163 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_12
# 164 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_12
# 165 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 170 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_13
# 171 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 172 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 173 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 174 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_13
# 175 "data/maps/PellucaCity/scripts.pory"
	release
# 176 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 178 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_14
# 179 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 180 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 181 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 182 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_14
# 183 "data/maps/PellucaCity/scripts.pory"
	release
# 184 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 185 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_15
# 186 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 187 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 191 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 192 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCity_MayorFight_Trigger_Movement_16
# 193 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 194 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 196 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_MAYOR
# 197 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S1
# 198 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S2
# 199 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S3
# 200 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_MAYOR_FIGHT
# 202 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_MayorFight_Trigger_2:
	end


PellucaCity_Sailor_Entrance::
# 219 "data/maps/PellucaCity/scripts.pory"
	lockall
# 220 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 222 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 223 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_Entrance_Text_0
# 224 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 0
	goto_if_eq PellucaCity_Sailor_Entrance_2
# 225 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 1
	goto_if_eq PellucaCity_Sailor_Entrance_5
# 227 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_Multichoice
# 229 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Sailor_Entrance_2:
# 224 "data/maps/PellucaCity/scripts.pory"
	release
	end

PellucaCity_Sailor_Entrance_5:
# 225 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_Sailor_Multichoice::
# 233 "data/maps/PellucaCity/scripts.pory"
	message PellucaCity_Sailor_Multichoice_Text_0
# 234 "data/maps/PellucaCity/scripts.pory"
	waitmessage
# 235 "data/maps/PellucaCity/scripts.pory"
	dynmultichoice 0, 0, FALSE, 4, 0, DYN_MULTICHOICE_CB_NONE, PellucaCity_Sailor_Multichoice_Text_1, PellucaCity_Sailor_Multichoice_Text_2, PellucaCity_Sailor_Multichoice_Text_3
# 237 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 0
	goto_if_eq PellucaCity_Sailor_Multichoice_2
PellucaCity_Sailor_Multichoice_1:
# 238 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Sailor_Multichoice_5
PellucaCity_Sailor_Multichoice_4:
# 240 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Sailor_Multichoice_2:
# 237 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_QwilsquadExplanation
	goto PellucaCity_Sailor_Multichoice_1

PellucaCity_Sailor_Multichoice_5:
# 238 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_MemberCheck
	goto PellucaCity_Sailor_Multichoice_4


PellucaCity_Sailor_QwilsquadExplanation::
# 244 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 245 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_QwilsquadExplanation_Text_0
# 246 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_Multichoice
	return


PellucaCity_Sailor_MemberCheck::
# 249 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 250 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_0, MSGBOX_YESNO
# 252 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 0
	goto_if_eq PellucaCity_Sailor_MemberCheck_2
PellucaCity_Sailor_MemberCheck_1:
# 256 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Sailor_MemberCheck_5
PellucaCity_Sailor_MemberCheck_4:
# 278 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Sailor_MemberCheck_2:
# 253 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 254 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_1
	goto PellucaCity_Sailor_MemberCheck_1

PellucaCity_Sailor_MemberCheck_5:
# 257 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 258 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_2
# 259 "data/maps/PellucaCity/scripts.pory"
	release
# 262 "data/maps/PellucaCity/scripts.pory"
	special ChoosePartyMon
# 263 "data/maps/PellucaCity/scripts.pory"
	waitstate
# 264 "data/maps/PellucaCity/scripts.pory"
	copyvar VAR_0x800A, VAR_0x8004
# 265 "data/maps/PellucaCity/scripts.pory"
	copyvar VAR_0x8005, VAR_0x800A
# 266 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetTradeSpecies
# 268 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, SPECIES_QWILFISH_HISUI
	goto_if_eq PellucaCity_Sailor_MemberCheck_8
PellucaCity_Sailor_MemberCheck_7:
# 269 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, SPECIES_OVERQWIL
	goto_if_eq PellucaCity_Sailor_MemberCheck_11
PellucaCity_Sailor_MemberCheck_10:
# 271 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_ENTRANCE, PellucaCity_MayorFight_Trigger_Movement_7
# 272 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 273 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 274 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_3
	goto PellucaCity_Sailor_MemberCheck_4

PellucaCity_Sailor_MemberCheck_8:
# 268 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_MemberAccepted
	goto PellucaCity_Sailor_MemberCheck_7

PellucaCity_Sailor_MemberCheck_11:
# 269 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_MemberAccepted
	goto PellucaCity_Sailor_MemberCheck_10


PellucaCity_Sailor_MemberAccepted::
# 282 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_ENTRANCE, PellucaCity_MayorFight_Trigger_Movement_7
# 283 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 284 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 285 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberAccepted_Text_0
# 286 "data/maps/PellucaCity/scripts.pory"
	release
# 288 "data/maps/PellucaCity/scripts.pory"
	opendoor 3, 42
# 289 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 290 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_ENTRANCE, PellucaCity_MayorFight_Trigger_Movement_11
# 291 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 292 "data/maps/PellucaCity/scripts.pory"
	playse SE_EXIT
# 293 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S_ENTRANCE
# 294 "data/maps/PellucaCity/scripts.pory"
	closedoor 3, 42
# 295 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 297 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_QWILSQUAD_ENTRANCE
# 298 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Blocker::
# 313 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Blocker_Text_0
	end


PellucaCity_Blocker_Trigger::
# 317 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 10
	goto_if_eq PellucaCity_Blocker_Trigger_2
# 319 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_BLOCKER, PellucaCity_MayorFight_Trigger_Movement_7
# 320 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 321 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Blocker_Trigger_Text_0
# 322 "data/maps/PellucaCity/scripts.pory"
	release
# 323 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_Blocker_Trigger_Movement_0
# 324 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 325 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Blocker_Trigger_2:
	end


PellucaCityFlooded_TriggerDown::
# 345 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerDown_1
	end

PellucaCityFlooded_TriggerDown_1:
# 346 "data/maps/PellucaCity/scripts.pory"
	lockall
# 347 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 348 "data/maps/PellucaCity/scripts.pory"
	release
# 349 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_10
# 350 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 351 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_TriggerUp::
# 358 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerUp_1
	end

PellucaCityFlooded_TriggerUp_1:
# 359 "data/maps/PellucaCity/scripts.pory"
	lockall
# 360 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 361 "data/maps/PellucaCity/scripts.pory"
	release
# 362 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_11
# 363 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 364 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_TriggerLeft::
# 371 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerLeft_1
	end

PellucaCityFlooded_TriggerLeft_1:
# 372 "data/maps/PellucaCity/scripts.pory"
	lockall
# 373 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 374 "data/maps/PellucaCity/scripts.pory"
	release
# 375 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_9
# 376 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 377 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_TriggerRight::
# 384 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerRight_1
	end

PellucaCityFlooded_TriggerRight_1:
# 385 "data/maps/PellucaCity/scripts.pory"
	lockall
# 386 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 387 "data/maps/PellucaCity/scripts.pory"
	release
# 388 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_Blocker_Trigger_Movement_0
# 389 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 390 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_SaveCitizen_A::
# 397 "data/maps/PellucaCity/scripts.pory"
	lockall
# 398 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 399 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_A_Text_0
# 400 "data/maps/PellucaCity/scripts.pory"
	release
# 403 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 405 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_EAST
	goto_if_eq PellucaCityFlooded_SaveCitizen_A_2
# 410 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_A_Movement_1
# 411 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 412 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_A_1:
# 416 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A_SAVED
# 417 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 419 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_A_2:
# 406 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_A_Movement_0
# 407 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 408 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_A_1


PellucaCityFlooded_SaveCitizen_B::
# 423 "data/maps/PellucaCity/scripts.pory"
	lockall
# 424 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 425 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_B_Text_0
# 426 "data/maps/PellucaCity/scripts.pory"
	release
# 428 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 430 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_SOUTH
	goto_if_eq PellucaCityFlooded_SaveCitizen_B_2
# 435 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_B_Movement_1
# 436 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 437 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_B_1:
# 440 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B_SAVED
# 441 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 443 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_B_2:
# 431 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_B_Movement_0
# 432 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 433 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_B_1


PellucaCityFlooded_SaveCitizen_C::
# 447 "data/maps/PellucaCity/scripts.pory"
	lockall
# 448 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 449 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_C_Text_0
# 450 "data/maps/PellucaCity/scripts.pory"
	release
# 453 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 455 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_NORTH
	goto_if_eq PellucaCityFlooded_SaveCitizen_C_2
# 460 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_C_Movement_1
# 461 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 462 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_C_1:
# 465 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C_SAVED
# 466 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 468 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_C_2:
# 456 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_C_Movement_0
# 457 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 458 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_C_1


PellucaCityFlooded_SaveCitizen_D::
# 472 "data/maps/PellucaCity/scripts.pory"
	lockall
# 473 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 474 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_D_Text_0
# 475 "data/maps/PellucaCity/scripts.pory"
	release
# 478 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 480 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_WEST
	goto_if_eq PellucaCityFlooded_SaveCitizen_D_2
# 485 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_D_Movement_1
# 486 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 487 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_D_1:
# 490 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D_SAVED
# 491 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 493 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_D_2:
# 481 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_D_Movement_0
# 482 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 483 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_D_1


PellucaCityFlooded_MainEvent::
# 498 "data/maps/PellucaCity/scripts.pory"
	lockall
# 499 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAYOR_QUEST, 4
# 500 "data/maps/PellucaCity/scripts.pory"
	playbgm MUS_DUMMY, FALSE
# 502 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_SKIP_PELLUCA_CUTSCENE, PellucaCityFlooded_MainEvent_2
PellucaCityFlooded_MainEvent_1:
# 514 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCityFlooded_MainEvent_Cutscene
	return

PellucaCityFlooded_MainEvent_2:
# 503 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Text_0, MSGBOX_YESNO
# 504 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCityFlooded_MainEvent_4
	goto PellucaCityFlooded_MainEvent_1

PellucaCityFlooded_MainEvent_4:
# 505 "data/maps/PellucaCity/scripts.pory"
	fadescreen FADE_TO_WHITE
# 506 "data/maps/PellucaCity/scripts.pory"
	additem ITEM_HM03
# 507 "data/maps/PellucaCity/scripts.pory"
	special EnterSafariMode
# 508 "data/maps/PellucaCity/scripts.pory"
	fadescreen FADE_FROM_WHITE
# 509 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_MainEvent_Cutscene::
# 519 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_SKIP_PELLUCA_CUTSCENE
# 521 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 522 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_0
# 523 "data/maps/PellucaCity/scripts.pory"
	release
# 524 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 527 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 528 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_MainEvent_Cutscene_Movement_0
# 530 "data/maps/PellucaCity/scripts.pory"
	delay 60
# 533 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 534 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_2
# 535 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 536 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_3
# 537 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 538 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_4
# 539 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 540 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_5
# 541 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 542 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_6
# 545 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_6
# 546 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 547 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 548 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_7
# 549 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_3
# 550 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 551 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 552 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_8
# 555 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_CITIZEN, PellucaCityFlooded_MainEvent_Cutscene_Movement_1
# 556 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 557 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_9
# 558 "data/maps/PellucaCity/scripts.pory"
	release
# 559 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 561 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_5
# 562 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_5
# 563 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_5
# 564 "data/maps/PellucaCity/scripts.pory"
	applymovement 48, PellucaCity_MayorFight_Trigger_Movement_5
# 565 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 566 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 568 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 569 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_10
# 570 "data/maps/PellucaCity/scripts.pory"
	release
# 572 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_7
# 573 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_7
# 574 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_7
# 575 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_7
# 576 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCity_MayorFight_Trigger_Movement_7
# 577 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_7
# 578 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 579 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 581 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 582 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_11
# 583 "data/maps/PellucaCity/scripts.pory"
	release
# 585 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 588 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_12
# 589 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_13
# 590 "data/maps/PellucaCity/scripts.pory"
	release
# 591 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 593 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_5
# 594 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_5
# 595 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_5
# 596 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_5
# 597 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCityFlooded_MainEvent_Cutscene_Movement_2
# 598 "data/maps/PellucaCity/scripts.pory"
	applymovement 48, PellucaCity_MayorFight_Trigger_Movement_5
# 599 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_5
# 601 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 602 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_14
# 603 "data/maps/PellucaCity/scripts.pory"
	release
# 605 "data/maps/PellucaCity/scripts.pory"
	addobject LOCALID_FL_JANIA
# 606 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_MainEvent_Cutscene_Movement_3
# 607 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 609 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_4
# 610 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_4
# 611 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_4
# 612 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_4
# 613 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCity_MayorFight_Trigger_Movement_4
# 614 "data/maps/PellucaCity/scripts.pory"
	applymovement 48, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 615 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 616 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_4
# 618 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_7
# 619 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 620 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 621 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_15
# 622 "data/maps/PellucaCity/scripts.pory"
	release
# 623 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 625 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_7
# 626 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 627 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 628 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_16
# 629 "data/maps/PellucaCity/scripts.pory"
	release
# 630 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 632 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 633 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_18
# 634 "data/maps/PellucaCity/scripts.pory"
	release
# 635 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 637 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCityFlooded_MainEvent_Cutscene_Movement_6
# 638 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCityFlooded_MainEvent_Cutscene_Movement_6
# 639 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 640 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 642 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 643 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_19
# 644 "data/maps/PellucaCity/scripts.pory"
	release
# 645 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 646 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 647 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 648 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 649 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 650 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_20
# 651 "data/maps/PellucaCity/scripts.pory"
	release
# 652 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_SYS_SURF_ENABLED
# 654 "data/maps/PellucaCity/scripts.pory"
	checkitem ITEM_HM03
# 655 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, TRUE
	goto_if_eq PellucaCityFlooded_MainEvent_Cutscene_2
PellucaCityFlooded_MainEvent_Cutscene_1:
# 659 "data/maps/PellucaCity/scripts.pory"
	giveitem ITEM_HM03
# 660 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 661 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_MayorFight_Trigger_Movement_4
# 662 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 663 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 664 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_21
# 665 "data/maps/PellucaCity/scripts.pory"
	release
# 666 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 669 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_MainEvent_Cutscene_Movement_7
# 670 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 671 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCityFlooded_MainEvent_Cutscene_Movement_8
# 672 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 675 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 676 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 677 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 678 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 679 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_22
# 680 "data/maps/PellucaCity/scripts.pory"
	release
# 681 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 682 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 683 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_23
# 684 "data/maps/PellucaCity/scripts.pory"
	release
# 685 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 686 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 687 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_24
# 688 "data/maps/PellucaCity/scripts.pory"
	release
# 689 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 690 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 691 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_24
# 692 "data/maps/PellucaCity/scripts.pory"
	release
# 693 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 695 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_5
# 696 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_5
# 697 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 698 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_25
# 699 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 700 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_26
# 701 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 702 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_27
# 703 "data/maps/PellucaCity/scripts.pory"
	release
# 704 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 705 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_28
# 706 "data/maps/PellucaCity/scripts.pory"
	release
# 708 "data/maps/PellucaCity/scripts.pory"
	completesubquest QUEST_PELLUCA_CITY, SUB_QUEST_2
# 710 "data/maps/PellucaCity/scripts.pory"
	special EnterSafariMode
# 711 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 712 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_MainEvent_Cutscene_2:
# 656 "data/maps/PellucaCity/scripts.pory"
	removeitem ITEM_HM03
	goto PellucaCityFlooded_MainEvent_Cutscene_1


PellucaCityFlooded_Mayor::
# 718 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 719 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Mayor_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_QwilBoss::
# 723 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 724 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_QwilBoss_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC1::
# 728 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC1_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC2::
# 732 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC2_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC3::
# 736 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC3_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC4::
# 740 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC4_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSailor::
# 744 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSailor_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_A::
# 749 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_A_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_B::
# 753 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_B_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_C::
# 757 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_C_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_D::
# 761 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_D_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_EventScript_TimesUp::
# 765 "data/maps/PellucaCity/scripts.pory"
	lockall
# 766 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_EventScript_TimesUp_Text_0
# 767 "data/maps/PellucaCity/scripts.pory"
	release
# 770 "data/maps/PellucaCity/scripts.pory"
	removeitem ITEM_HM03
# 772 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_REGULAR_CITIZENS
# 773 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZENS
# 775 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A_SAVED
# 776 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B_SAVED
# 777 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C_SAVED
# 778 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D_SAVED
# 780 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A
# 781 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B
# 782 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C
# 783 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D
# 785 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAP_STATE, 1
# 787 "data/maps/PellucaCity/scripts.pory"
	delay 2
# 789 "data/maps/PellucaCity/scripts.pory"
	special ExitSafariMode
# 790 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAYOR_QUEST, 3
# 791 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAP_STATE, 1
# 792 "data/maps/PellucaCity/scripts.pory"
	warp MAP_PELLUCA_CITY, 43, 28
# 793 "data/maps/PellucaCity/scripts.pory"
	waitstate
	end


PellucaCityFlooded_EventScript_TimesRunningOut::
# 798 "data/maps/PellucaCity/scripts.pory"
	lockall
# 799 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_EventScript_TimesRunningOut_Text_0
# 800 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCityFlooded_Complete_Trigger::
# 807 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 8
	goto_if_eq PellucaCityFlooded_Complete_Trigger_2
	end

PellucaCityFlooded_Complete_Trigger_2:
# 809 "data/maps/PellucaCity/scripts.pory"
	special ExitSafariMode
# 811 "data/maps/PellucaCity/scripts.pory"
	lockall
# 812 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCityFlooded_MainEvent_Cutscene_Movement_8
# 813 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_Complete_Trigger_Movement_0
# 814 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 815 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 818 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 819 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_0
# 820 "data/maps/PellucaCity/scripts.pory"
	release
# 821 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 824 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 825 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_1
# 826 "data/maps/PellucaCity/scripts.pory"
	release
# 827 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 829 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 830 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_Complete_Trigger_Movement_1
# 831 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 835 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_7
# 836 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_7
# 837 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_7
# 838 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_7
# 839 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCity_MayorFight_Trigger_Movement_7
# 840 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_7
# 841 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 842 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 844 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 845 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_2
# 846 "data/maps/PellucaCity/scripts.pory"
	release
# 847 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 849 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_Complete_Trigger_Movement_2
# 850 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 851 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 852 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 854 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_6
# 855 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 856 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 857 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 858 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_3
# 859 "data/maps/PellucaCity/scripts.pory"
	release
# 860 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 863 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_3
# 864 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 865 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 866 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 867 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_4
# 868 "data/maps/PellucaCity/scripts.pory"
	release
# 869 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 871 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 872 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_5
# 873 "data/maps/PellucaCity/scripts.pory"
	release
# 874 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 878 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAYOR_QUEST, 9
# 879 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAP_STATE, 0
# 881 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_REGULAR_CITIZENS
# 882 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZENS
# 884 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A_SAVED
# 885 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B_SAVED
# 886 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C_SAVED
# 887 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D_SAVED
# 889 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_PC_CHARS
# 892 "data/maps/PellucaCity/scripts.pory"
	warp MAP_PELLUCA_CITY_POKEMON_CENTER, 7, 6
# 894 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Greta_Trigger0::
# 924 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_GRETA_PELLUCACITY, PellucaCity_Greta_Trigger0_2
# 926 "data/maps/PellucaCity/scripts.pory"
	lockall
# 927 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_Trigger0_Movement_0
# 928 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 929 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 930 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 931 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_Main
	return

PellucaCity_Greta_Trigger0_2:
	end


PellucaCity_Greta_Trigger1::
# 935 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_GRETA_PELLUCACITY, PellucaCity_Greta_Trigger1_2
# 937 "data/maps/PellucaCity/scripts.pory"
	lockall
# 938 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_Trigger1_Movement_0
# 939 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 940 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 941 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 942 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_Main
	return

PellucaCity_Greta_Trigger1_2:
	end


PellucaCity_Greta_Trigger2::
# 946 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_GRETA_PELLUCACITY, PellucaCity_Greta_Trigger2_2
# 948 "data/maps/PellucaCity/scripts.pory"
	lockall
# 949 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_Trigger2_Movement_0
# 950 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 951 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 952 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 953 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_Main
	return

PellucaCity_Greta_Trigger2_2:
	end


PellucaCity_Greta_Main::
# 958 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_Greta_Main_Text_0
# 959 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Greta_Main_Text_1
# 960 "data/maps/PellucaCity/scripts.pory"
	release
# 961 "data/maps/PellucaCity/scripts.pory"
	delay 20
# 962 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_Greta_Main_Text_0
# 963 "data/maps/PellucaCity/scripts.pory"
	msgbox Common_Text_Greta_Comecome
# 964 "data/maps/PellucaCity/scripts.pory"
	release
# 965 "data/maps/PellucaCity/scripts.pory"
	delay 20
# 967 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_ShowItemsForSale
	return


PellucaCity_Greta_GottaGo::
# 971 "data/maps/PellucaCity/scripts.pory"
	release
# 972 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_MayorFight_Trigger_Movement_7
# 973 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 974 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_Greta_Main_Text_0
# 975 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Greta_GottaGo_Text_0
# 976 "data/maps/PellucaCity/scripts.pory"
	release
# 977 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_GottaGo_Movement_0
# 978 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 979 "data/maps/PellucaCity/scripts.pory"
	removeobject 27
# 980 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_GRETA_PELLUCACITY
# 981 "data/maps/PellucaCity/scripts.pory"
	fadedefaultbgm
# 983 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_EventScripts_Gabrielle::
# 1003 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1004 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_GABRIELLE_CHOICEBAND, PellucaCity_EventScripts_Gabrielle_1
# 1010 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1011 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_2
# 1012 "data/maps/PellucaCity/scripts.pory"
	release
# 1013 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1014 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1015 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1016 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1017 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_3, MSGBOX_YESNO
# 1018 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_EventScripts_Gabrielle_5
# 1027 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1028 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1029 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_5
# 1030 "data/maps/PellucaCity/scripts.pory"
	release
PellucaCity_EventScripts_Gabrielle_4:
# 1032 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 1033 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1034 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_6
# 1035 "data/maps/PellucaCity/scripts.pory"
	release
# 1036 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1037 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1038 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1039 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1040 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_7
# 1041 "data/maps/PellucaCity/scripts.pory"
	release
# 1042 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem
	return

PellucaCity_EventScripts_Gabrielle_1:
# 1005 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1006 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_1
# 1007 "data/maps/PellucaCity/scripts.pory"
	release
	return

PellucaCity_EventScripts_Gabrielle_5:
# 1020 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1021 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1022 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1023 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_4
# 1024 "data/maps/PellucaCity/scripts.pory"
	release
	goto PellucaCity_EventScripts_Gabrielle_4


PellucaCity_Gab_ChoiceItem::
# 1047 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1048 "data/maps/PellucaCity/scripts.pory"
	message PellucaCity_Gab_ChoiceItem_Text_0
# 1049 "data/maps/PellucaCity/scripts.pory"
	waitmessage
# 1050 "data/maps/PellucaCity/scripts.pory"
	dynmultichoice 0, 0, TRUE, 4, 0, DYN_MULTICHOICE_CB_NONE, PellucaCity_Gab_ChoiceItem_Text_1, PellucaCity_Gab_ChoiceItem_Text_2, PellucaCity_Gab_ChoiceItem_Text_3
# 1051 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 0
	goto_if_eq PellucaCity_Gab_ChoiceItem_2
PellucaCity_Gab_ChoiceItem_1:
# 1052 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Gab_ChoiceItem_5
PellucaCity_Gab_ChoiceItem_4:
# 1053 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 2
	goto_if_eq PellucaCity_Gab_ChoiceItem_8
PellucaCity_Gab_ChoiceItem_7:
# 1054 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem_Give
	return

PellucaCity_Gab_ChoiceItem_2:
# 1051 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_0x8006, ITEM_CHOICE_SPECS
	goto PellucaCity_Gab_ChoiceItem_1

PellucaCity_Gab_ChoiceItem_5:
# 1052 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_0x8006, ITEM_CHOICE_BAND
	goto PellucaCity_Gab_ChoiceItem_4

PellucaCity_Gab_ChoiceItem_8:
# 1053 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_0x8006, ITEM_CHOICE_SCARF
	goto PellucaCity_Gab_ChoiceItem_7


PellucaCity_Gab_ChoiceItem_Give::
# 1058 "data/maps/PellucaCity/scripts.pory"
	showitemdescription
# 1059 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Gab_ChoiceItem_Give_Text_0, MSGBOX_YESNO
# 1060 "data/maps/PellucaCity/scripts.pory"
	hideitemdescription
# 1061 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Gab_ChoiceItem_Give_1
# 1062 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem
	return

PellucaCity_Gab_ChoiceItem_Give_1:
# 1061 "data/maps/PellucaCity/scripts.pory"
	giveitem VAR_0x8006
# 1061 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem_End
	return


PellucaCity_Gab_ChoiceItem_End::
# 1066 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1067 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Gab_ChoiceItem_End_Text_0
# 1068 "data/maps/PellucaCity/scripts.pory"
	release
# 1069 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_GABRIELLE_CHOICEBAND
# 1070 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1071 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1072 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Zorua::
# 1084 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1085 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1086 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_ZOROARK, CRY_MODE_NORMAL
# 1087 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Zorua_Text_0
# 1088 "data/maps/PellucaCity/scripts.pory"
	release
# 1089 "data/maps/PellucaCity/scripts.pory"
	applymovement 25, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1090 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1091 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Lycanroc::
# 1107 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_LYCANROC, CRY_MODE_NORMAL
# 1108 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Lycanroc_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC1::
# 1121 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC1_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC2::
# 1126 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC2_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC3::
# 1131 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC3_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC4::
# 1136 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC4_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC5::
# 1141 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1142 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC5_Text_0
# 1143 "data/maps/PellucaCity/scripts.pory"
	release
# 1144 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 1145 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCity_NPC5_Movement_0
# 1146 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1147 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 1148 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC5_Text_1
# 1149 "data/maps/PellucaCity/scripts.pory"
	release
# 1150 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 1151 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCity_NPC5_Movement_1
# 1152 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1153 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 1154 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC5_Text_2, MSGBOX_NPC
# 1155 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_NPC6::
# 1160 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC6_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC7::
# 1165 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC7_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC8::
# 1170 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC8_Text_0, MSGBOX_NPC
	end


PellucaCity_Sealeo::
# 1175 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1176 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1177 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_SEALEO, CRY_MODE_NORMAL
# 1178 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sealeo_Text_0, MSGBOX_NPC
# 1179 "data/maps/PellucaCity/scripts.pory"
	release
# 1180 "data/maps/PellucaCity/scripts.pory"
	applymovement 26, PellucaCity_MayorFight_Trigger_Movement_4
# 1181 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1182 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_NPC9::
# 1190 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC9_Text_0, MSGBOX_NPC
	end


PellucaCity_WingullGirl::
# 1199 "data/maps/PellucaCity/scripts.pory"
	lock
# 1200 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1201 "data/maps/PellucaCity/scripts.pory"
	message PellucaCity_WingullGirl_Text_0
# 1202 "data/maps/PellucaCity/scripts.pory"
	waitmessage
# 1203 "data/maps/PellucaCity/scripts.pory"
	dynmultichoice 16, 8, TRUE, 4, 0, DYN_MULTICHOICE_CB_NONE, PellucaCity_WingullGirl_Text_1, PellucaCity_WingullGirl_Text_2
# 1205 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_WingullGirl_2
# 1219 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullGirl_Text_5, MSGBOX_NPC
PellucaCity_WingullGirl_1:
# 1222 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_WingullGirl_2:
# 1207 "data/maps/PellucaCity/scripts.pory"
	applymovement 15, PellucaCity_MayorFight_Trigger_Movement_5
# 1208 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_5
# 1209 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullGirl_Text_3
# 1210 "data/maps/PellucaCity/scripts.pory"
	release
# 1211 "data/maps/PellucaCity/scripts.pory"
	applymovement 16, PellucaCity_MayorFight_Trigger_Movement_7
# 1212 "data/maps/PellucaCity/scripts.pory"
	applymovement 17, PellucaCity_MayorFight_Trigger_Movement_7
# 1213 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1214 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1215 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullGirl_Text_4
# 1216 "data/maps/PellucaCity/scripts.pory"
	setwildbattle SPECIES_WINGULL, 25
# 1217 "data/maps/PellucaCity/scripts.pory"
	dowildbattle
	goto PellucaCity_WingullGirl_1


PellucaCity_WingullMother::
# 1227 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullMother_Text_0, MSGBOX_NPC
	end


PellucaCity_WingullCritique::
# 1232 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullCritique_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC10::
# 1245 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC10_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC11::
# 1251 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_CITY_TM_GIVER, PellucaCity_NPC11_2
# 1256 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC11_Text_1, MSGBOX_NPC
# 1257 "data/maps/PellucaCity/scripts.pory"
	giveitem ITEM_TM31
# 1258 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_CITY_TM_GIVER
# 1259 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC11_Text_2, MSGBOX_NPC
	end

PellucaCity_NPC11_2:
# 1252 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC11_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC12::
# 1265 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC12_Text_0, MSGBOX_NPC
	end


PellucaCity_Stantler::
# 1270 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_STANTLER, CRY_MODE_NORMAL
# 1271 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Stantler_Text_0, MSGBOX_NPC
	end


PellucaCity_PostGymEvent_Trigger::
# 1298 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_POSTGYM, PellucaCity_PostGymEvent_Trigger_2
# 1300 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_BADGE07_GET, PellucaCity_PostGymEvent_Trigger_5
	end

PellucaCity_PostGymEvent_Trigger_2:
	end

PellucaCity_PostGymEvent_Trigger_5:
# 1301 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1304 "data/maps/PellucaCity/scripts.pory"
	opendoor 37, 8
# 1305 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 1308 "data/maps/PellucaCity/scripts.pory"
	addobject LOCALID_FL_JANIA
# 1309 "data/maps/PellucaCity/scripts.pory"
	setobjectxy LOCALID_FL_JANIA, 37, 8
# 1311 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_MayorFight_Trigger_Movement_10
# 1312 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1315 "data/maps/PellucaCity/scripts.pory"
	closedoor 37, 8
# 1317 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_Complete_Trigger_Movement_2
# 1318 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1320 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 1321 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_0
# 1322 "data/maps/PellucaCity/scripts.pory"
	release
# 1323 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_PostGymEvent_Trigger_Movement_0
# 1324 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_Complete_Trigger_Movement_2
# 1325 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1326 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1327 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_MayorFight_Trigger_Movement_5
# 1328 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1329 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1330 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 1331 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_1
# 1332 "data/maps/PellucaCity/scripts.pory"
	release
# 1334 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 1335 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_PostGymEvent_Trigger_Movement_1
# 1336 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_Complete_Trigger_Movement_0
# 1337 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1339 "data/maps/PellucaCity/scripts.pory"
	opendoor 37, 8
# 1340 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 1343 "data/maps/PellucaCity/scripts.pory"
	addobject LOCALID_GAB
# 1344 "data/maps/PellucaCity/scripts.pory"
	setobjectxy LOCALID_GAB, 37, 8
# 1345 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_PostGymEvent_Trigger_Movement_2
# 1346 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1347 "data/maps/PellucaCity/scripts.pory"
	closedoor 37, 8
# 1348 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1349 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1350 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_2
# 1351 "data/maps/PellucaCity/scripts.pory"
	release
# 1353 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_PostGymEvent_Trigger_Movement_3
# 1354 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1355 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 1356 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1357 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1359 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1360 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_3
# 1361 "data/maps/PellucaCity/scripts.pory"
	release
# 1362 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_MayorFight_Trigger_Movement_7
# 1363 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1364 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1365 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1366 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_4
# 1367 "data/maps/PellucaCity/scripts.pory"
	release
# 1368 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1369 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_4
# 1370 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_PostGymEvent_Trigger_Movement_4
# 1371 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1372 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1373 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1374 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_5
# 1375 "data/maps/PellucaCity/scripts.pory"
	release
# 1376 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_PostGymEvent_Trigger_Movement_5
# 1377 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1378 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1380 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 1383 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_FL_JANIA
# 1384 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_GAB
# 1387 "data/maps/PellucaCity/scripts.pory"
	startquest QUEST_STOP_TEAM_SOMBER
# 1388 "data/maps/PellucaCity/scripts.pory"
	subquestmenu QUEST_MENU_COMPLETE_QUEST, QUEST_STOP_TEAM_SOMBER, SUB_QUEST_1
# 1389 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_POSTGYM
	end


PellucaCity_Red_GymBlock::
# 1406 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Red_GymBlock_Text_0, MSGBOX_NPC
	end


DR_PellucaCity_Arrival::
# 1414 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1415 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_UNUSED_0x404E, 2
# 1416 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_5
# 1417 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1418 "data/maps/PellucaCity/scripts.pory"
	delay 20
# 1422 "data/maps/PellucaCity/scripts.pory"
	speakername DR_PellucaCity_Arrival_Text_0
# 1423 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_1
# 1424 "data/maps/PellucaCity/scripts.pory"
	speakername DR_PellucaCity_Arrival_Text_2
# 1425 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_3
# 1426 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1427 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 1428 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_DR_CADMUS, DR_PellucaCity_Arrival_Movement_0
# 1429 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1430 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1431 "data/maps/PellucaCity/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 1432 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_4
# 1433 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1434 "data/maps/PellucaCity/scripts.pory"
	delay 40
# 1435 "data/maps/PellucaCity/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 1436 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_5
# 1437 "data/maps/PellucaCity/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 1438 "data/maps/PellucaCity/scripts.pory"
	speakername DR_PellucaCity_Arrival_Text_6
# 1439 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_7
# 1440 "data/maps/PellucaCity/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 1441 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_8
# 1442 "data/maps/PellucaCity/scripts.pory"
	hideportrait
# 1443 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1444 "data/maps/PellucaCity/scripts.pory"
	release
# 1445 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1446 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_DR_CADMUS, DR_PellucaCity_Arrival_Movement_1
# 1447 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1448 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_PellucaCity_Arrival_Movement_2
# 1449 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1450 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1451 "data/maps/PellucaCity/scripts.pory"
	playse SE_EXIT
# 1452 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_DR_CADMUS
# 1453 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1454 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_2
# 1455 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1456 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1457 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_UNUSED_0x884
# 1458 "data/maps/PellucaCity/scripts.pory"
	warp MAP_PELLUCA_UMBRA_LAB, 0
# 1459 "data/maps/PellucaCity/scripts.pory"
	waitstate
	end


# 57 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_0:
# 57 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 57 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 57 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 57 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 62 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_1:
# 62 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 62 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_left
	step_end

# 70 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_2:
# 70 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 70 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_right
	step_end

# 78 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_3:
# 78 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_left
	step_end

# 86 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_4:
# 86 "data/maps/PellucaCity/scripts.pory"
	face_down
	step_end

# 94 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_5:
# 94 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 102 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_6:
# 102 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_right
	step_end

# 110 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_7:
# 110 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
	step_end

# 121 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_8:
# 122 "data/maps/PellucaCity/scripts.pory"
	lock_anim
# 123 "data/maps/PellucaCity/scripts.pory"
	lock_facing_direction
# 124 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 125 "data/maps/PellucaCity/scripts.pory"
	unlock_anim
# 126 "data/maps/PellucaCity/scripts.pory"
	unlock_facing_direction
	step_end

# 153 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_9:
# 153 "data/maps/PellucaCity/scripts.pory"
	walk_left
	step_end

# 156 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_10:
# 156 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 160 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_11:
# 160 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 162 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_12:
# 162 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 162 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 162 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 162 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 162 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 162 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 162 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 162 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 162 "data/maps/PellucaCity/scripts.pory"
	walk_left
	step_end

# 170 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_13:
# 170 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 170 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 178 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_14:
# 178 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 178 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 178 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 178 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 178 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 178 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 185 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_15:
# 185 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 185 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 185 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 185 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 185 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 185 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 192 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_16:
# 192 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 192 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 192 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 192 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 323 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Blocker_Trigger_Movement_0:
# 323 "data/maps/PellucaCity/scripts.pory"
	walk_right
	step_end

# 406 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_A_Movement_0:
# 406 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 406 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 406 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 406 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 406 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 406 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 406 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 406 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 406 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 406 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
	step_end

# 410 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_A_Movement_1:
# 410 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 410 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 410 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 410 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 410 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 410 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 410 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 410 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 410 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
	step_end

# 431 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_B_Movement_0:
# 431 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 431 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 431 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 431 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 431 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 431 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 431 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 431 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 435 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_B_Movement_1:
# 435 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 435 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 435 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 435 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 435 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 435 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 435 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 456 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_C_Movement_0:
# 456 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 456 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 456 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 456 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 456 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 456 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 456 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 456 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
	step_end

# 460 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_C_Movement_1:
# 460 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 460 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 460 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 460 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 460 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 460 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 460 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
	step_end

# 481 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_D_Movement_0:
# 481 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 481 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 481 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 481 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 481 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 481 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 481 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 481 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 481 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 481 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
	step_end

# 485 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_D_Movement_1:
# 485 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 485 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 485 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 485 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 485 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 485 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 485 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 485 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 485 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
	step_end

# 528 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_0:
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 528 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 555 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_1:
# 555 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 555 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_down
	step_end

# 597 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_2:
# 597 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 597 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 606 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_3:
# 606 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 606 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 606 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 606 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 606 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 606 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 606 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 606 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 606 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 606 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 614 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_4:
# 614 "data/maps/PellucaCity/scripts.pory"
	face_right
	step_end

# 615 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_5:
# 615 "data/maps/PellucaCity/scripts.pory"
	face_left
	step_end

# 637 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_6:
# 637 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 637 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_up
	step_end

# 669 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_7:
# 669 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 669 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 669 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 669 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 669 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 669 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 669 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 669 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 669 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 669 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 671 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_8:
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 671 "data/maps/PellucaCity/scripts.pory"
	face_down
	step_end

# 813 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_Complete_Trigger_Movement_0:
# 813 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 813 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 813 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 830 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_Complete_Trigger_Movement_1:
# 830 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 830 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 849 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_Complete_Trigger_Movement_2:
# 849 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 849 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 927 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_Trigger0_Movement_0:
# 927 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 927 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 927 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 927 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 927 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 927 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 927 "data/maps/PellucaCity/scripts.pory"
	face_left
	step_end

# 938 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_Trigger1_Movement_0:
# 938 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 938 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 938 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 938 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 938 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 938 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 938 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 938 "data/maps/PellucaCity/scripts.pory"
	face_right
	step_end

# 949 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_Trigger2_Movement_0:
# 949 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 949 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 949 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 949 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 949 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 949 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 949 "data/maps/PellucaCity/scripts.pory"
	face_right
	step_end

# 977 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_GottaGo_Movement_0:
# 977 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 977 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 977 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 977 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 977 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 977 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 977 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 977 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 1145 "data/maps/PellucaCity/scripts.pory"
PellucaCity_NPC5_Movement_0:
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1145 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 1151 "data/maps/PellucaCity/scripts.pory"
PellucaCity_NPC5_Movement_1:
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1151 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
	step_end

# 1323 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_0:
# 1323 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1323 "data/maps/PellucaCity/scripts.pory"
	face_down
	step_end

# 1335 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_1:
# 1335 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1335 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1335 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 1335 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 1335 "data/maps/PellucaCity/scripts.pory"
	walk_left
	step_end

# 1345 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_2:
# 1345 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1345 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
	step_end

# 1353 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_3:
# 1353 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1353 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1353 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1353 "data/maps/PellucaCity/scripts.pory"
	face_left
	step_end

# 1370 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_4:
# 1370 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1370 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1370 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1370 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 1376 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_5:
# 1376 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1376 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1376 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 1428 "data/maps/PellucaCity/scripts.pory"
DR_PellucaCity_Arrival_Movement_0:
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 1446 "data/maps/PellucaCity/scripts.pory"
DR_PellucaCity_Arrival_Movement_1:
# 1446 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1446 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1446 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1446 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1446 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1446 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1446 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1446 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1446 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1446 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 1448 "data/maps/PellucaCity/scripts.pory"
DR_PellucaCity_Arrival_Movement_2:
# 1448 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1448 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1448 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1448 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1448 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1448 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1448 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1448 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1448 "data/maps/PellucaCity/scripts.pory"
	walk_right
	step_end

PellucaCity_MayorFight_Trigger_Text_0:
# 65 "data/maps/PellucaCity/scripts.pory"
	.string "Mayor$"

PellucaCity_MayorFight_Trigger_Text_1:
# 66 "data/maps/PellucaCity/scripts.pory"
	.string "But you can't be doing this to our\n"
	.string "citizens! This is our city!$"

PellucaCity_MayorFight_Trigger_Text_2:
# 73 "data/maps/PellucaCity/scripts.pory"
	.string "Q-squad Boss$"

PellucaCity_MayorFight_Trigger_Text_3:
# 74 "data/maps/PellucaCity/scripts.pory"
	.string "I've told you a hundred times, you\n"
	.string "paper-pushing wimp! You ain't doing a\l"
	.string "single thing right for our city, so don't\l"
	.string "you dare mess with the Qwilsquad!\p"
	.string "This is our turf - we don't give a hoot\n"
	.string "about you and your title!$"

PellucaCity_MayorFight_Trigger_Text_4:
# 82 "data/maps/PellucaCity/scripts.pory"
	.string "No! Enough is enough! I'm putting my\n"
	.string "foot down.\p"
	.string "You and your lot aren't allowed in\n"
	.string "Pelluca City any more!$"

PellucaCity_MayorFight_Trigger_Text_5:
# 89 "data/maps/PellucaCity/scripts.pory"
	.string "Q-squad Grunt$"

PellucaCity_MayorFight_Trigger_Text_6:
# 90 "data/maps/PellucaCity/scripts.pory"
	.string "Hahaha! What a lame mayor!$"

PellucaCity_MayorFight_Trigger_Text_7:
# 98 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah! He really thinks he can tell us\n"
	.string "what to do!$"

PellucaCity_MayorFight_Trigger_Text_8:
# 106 "data/maps/PellucaCity/scripts.pory"
	.string "Go on boss - teach him a lesson!$"

PellucaCity_MayorFight_Trigger_Text_9:
# 114 "data/maps/PellucaCity/scripts.pory"
	.string "You heard 'em Mayor. Looks like my boys\n"
	.string "want me to prove that we own this city!\p"
	.string "Wanna try me? Right here?$"

PellucaCity_MayorFight_Trigger_Text_10:
# 132 "data/maps/PellucaCity/scripts.pory"
	.string "Nono - see, I'm not - look, I'm just\n"
	.string "asking for a little cooperation and -$"

PellucaCity_MayorFight_Trigger_Text_11:
# 140 "data/maps/PellucaCity/scripts.pory"
	.string "Hahaha! Look at the wimp! Poor guy.$"

PellucaCity_MayorFight_Trigger_Text_12:
# 148 "data/maps/PellucaCity/scripts.pory"
	.string "Got it, mayor? You're not in charge here.\p"
	.string "I am!\p"
	.string "And from now on, this city belongs\n"
	.string "to us - the Qwilsquad!$"

PellucaCity_MayorFight_Trigger_Text_13:
# 174 "data/maps/PellucaCity/scripts.pory"
	.string "Oh - a tourist! Were you standing there\n"
	.string "the whole time?\p"
	.string "...\p"
	.string "I'm sorry you had to witness that.\p"
	.string "Y-you know, we have a wonderful\n"
	.string "Game Corner! And the Apple Pie at the\l"
	.string "Pelluca Restaurant is to die for.$"

PellucaCity_MayorFight_Trigger_Text_14:
# 182 "data/maps/PellucaCity/scripts.pory"
	.string "Sigh...what will I do?$"

PellucaCity_Sailor_Entrance_Text_0:
# 223 "data/maps/PellucaCity/scripts.pory"
	.string "Beat it, kid! This is private property\n"
	.string "belonging to the Qwilsquad.$"

PellucaCity_Sailor_Multichoice_Text_0:
# 233 "data/maps/PellucaCity/scripts.pory"
	.string "Only Qwilsquad members can enter!$"

PellucaCity_Sailor_Multichoice_Text_1:
# 235 "data/maps/PellucaCity/scripts.pory"
	.string "What's a Qwilsquad?$"

PellucaCity_Sailor_Multichoice_Text_2:
# 235 "data/maps/PellucaCity/scripts.pory"
	.string "I'm a member!$"

PellucaCity_Sailor_Multichoice_Text_3:
# 235 "data/maps/PellucaCity/scripts.pory"
	.string "Okay...$"

PellucaCity_Sailor_QwilsquadExplanation_Text_0:
# 245 "data/maps/PellucaCity/scripts.pory"
	.string "You interested in joining, kid?\n"
	.string "The Qwilsquad is all about trust and\l"
	.string "brotherhood. In the Qwilsquad, you\l"
	.string "gotta have each other's backs!\p"
	.string "And you gotta be the proud trainer\n"
	.string "of a Qwilfish of course.\p"
	.string "We're from Pelluca, but we went down to\n"
	.string "Rivetshore to sail. Now we're back, and\l"
	.string "we're not happy with how the mayor is\l"
	.string "bungling his job! So we're taking\l"
	.string "matters into our own hands.$"

PellucaCity_Sailor_MemberCheck_Text_0:
# 250 "data/maps/PellucaCity/scripts.pory"
	.string "A pipsqueak like you is in the squad?\n"
	.string "You a new member? Got any proof?$"

PellucaCity_Sailor_MemberCheck_Text_1:
# 254 "data/maps/PellucaCity/scripts.pory"
	.string "Then beat it, kid!$"

PellucaCity_Sailor_MemberCheck_Text_2:
# 258 "data/maps/PellucaCity/scripts.pory"
	.string "Show me!$"

PellucaCity_Sailor_MemberCheck_Text_3:
# 274 "data/maps/PellucaCity/scripts.pory"
	.string "That don't look like no Qwilfish to me!\p"
	.string "Beat it, kid!$"

PellucaCity_Sailor_MemberAccepted_Text_0:
# 285 "data/maps/PellucaCity/scripts.pory"
	.string "Now that's what I'm talking about!\n"
	.string "You're one of us, kid.\p"
	.string "Go on, get inside!$"

PellucaCity_Blocker_Text_0:
# 313 "data/maps/PellucaCity/scripts.pory"
	.string "This is our city! Got any problems?$"

PellucaCity_Blocker_Trigger_Text_0:
# 321 "data/maps/PellucaCity/scripts.pory"
	.string "Hey kid, where d'you think yer goin?\n"
	.string "There's a toll if you wanna get out.\p"
	.string "That's right! You gotta pay ¥999999.\p"
	.string "Ain't got the money?\p"
	.string "Then get packing!$"

PellucaCityFlooded_SaveCitizen_A_Text_0:
# 399 "data/maps/PellucaCity/scripts.pory"
	.string "Help! Help! Over here!\p"
	.string "...\p"
	.string "Thank you so much - I'm saved!$"

PellucaCityFlooded_SaveCitizen_B_Text_0:
# 425 "data/maps/PellucaCity/scripts.pory"
	.string "I can't stay afloat any more!\p"
	.string "...\p"
	.string "You came just in time!$"

PellucaCityFlooded_SaveCitizen_C_Text_0:
# 449 "data/maps/PellucaCity/scripts.pory"
	.string "Ahh! It's too cold!\p"
	.string "...\p"
	.string "Waah! Wahh! It was so scary!$"

PellucaCityFlooded_SaveCitizen_D_Text_0:
# 474 "data/maps/PellucaCity/scripts.pory"
	.string "Help! Someone save me!\p"
	.string "...\p"
	.string "Yaay! You came!$"

PellucaCityFlooded_MainEvent_Text_0:
# 503 "data/maps/PellucaCity/scripts.pory"
	.string "Skip cutscene?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_0:
# 522 "data/maps/PellucaCity/scripts.pory"
	.string "What on earth is this?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_1:
# 533 "data/maps/PellucaCity/scripts.pory"
	.string "Citizen$"

PellucaCityFlooded_MainEvent_Cutscene_Text_2:
# 534 "data/maps/PellucaCity/scripts.pory"
	.string "What a disaster!\p"
	.string "How could we be so unlucky!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_3:
# 536 "data/maps/PellucaCity/scripts.pory"
	.string "What happened?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_4:
# 538 "data/maps/PellucaCity/scripts.pory"
	.string "A Mega Sharpedo came rampaging down\n"
	.string "from the Ivy River and kicked up a\l"
	.string "storm! The riverbanks have flooded.\p"
	.string "The city's underwater!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_5:
# 540 "data/maps/PellucaCity/scripts.pory"
	.string "Is everyone safe?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_6:
# 542 "data/maps/PellucaCity/scripts.pory"
	.string "No - there are still four people in the\n"
	.string "water! We have to save them fast!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_7:
# 548 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah, go on Mayor. Go save them!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_8:
# 552 "data/maps/PellucaCity/scripts.pory"
	.string "W-what do you mean? Weren't you the\n"
	.string "one in control of this city?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_9:
# 557 "data/maps/PellucaCity/scripts.pory"
	.string "ENOUGH!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_10:
# 569 "data/maps/PellucaCity/scripts.pory"
	.string "While you two bicker, it's us that pays\n"
	.string "the price every time! Both of you are\l"
	.string "strong - a tough trainer and a smart\l"
	.string "politician - and yet, neither of you\l"
	.string "bother to actually do anything for us\l"
	.string "citizens! And now people are in danger\l"
	.string "and you're still fighting! We've all had\l"
	.string "it up to here with you two!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_11:
# 582 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah!\p"
	.string "Hear hear!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_12:
# 588 "data/maps/PellucaCity/scripts.pory"
	.string "???$"

PellucaCityFlooded_MainEvent_Cutscene_Text_13:
# 589 "data/maps/PellucaCity/scripts.pory"
	.string "I agree too.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_14:
# 602 "data/maps/PellucaCity/scripts.pory"
	.string "Is that Jania?\p"
	.string "Yeah! It's the Gym Leader! In the flesh!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_15:
# 621 "data/maps/PellucaCity/scripts.pory"
	.string "Oh, Jania! It's you! Finally. Please - you\n"
	.string "have to save those still drowning!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_16:
# 628 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah, Jania! You're an even stronger\n"
	.string "trainer than I am. You can do it!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_17:
# 632 "data/maps/PellucaCity/scripts.pory"
	.string "Jania$"

PellucaCityFlooded_MainEvent_Cutscene_Text_18:
# 633 "data/maps/PellucaCity/scripts.pory"
	.string "No, I won't.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_19:
# 643 "data/maps/PellucaCity/scripts.pory"
	.string "Don't look at me like that!\p"
	.string "You two want to be responsible for this\n"
	.string "city? Start right here, right now.\p"
	.string "Your citizens are miserably tired of\n"
	.string "both of you - when will you two change?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_20:
# 650 "data/maps/PellucaCity/scripts.pory"
	.string "And who might you be?\p"
	.string "...\p"
	.string "{PLAYER}?\p"
	.string "...\p"
	.string "I see - so that's how you got involved\n"
	.string "with these two.\p"
	.string "Here, take this.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_21:
# 664 "data/maps/PellucaCity/scripts.pory"
	.string "Consider this my help.\p"
	.string "Now I'm going to track the Mega\n"
	.string "Sharpedo down and make sure it doesn't\l"
	.string "harm anyone else.\p"
	.string "And the two of you - and {PLAYER} -\n"
	.string "take this chance to do the right thing!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_22:
# 679 "data/maps/PellucaCity/scripts.pory"
	.string "Hmpf.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_23:
# 683 "data/maps/PellucaCity/scripts.pory"
	.string "Tchah!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_24:
# 687 "data/maps/PellucaCity/scripts.pory"
	.string "...$"

PellucaCityFlooded_MainEvent_Cutscene_Text_25:
# 698 "data/maps/PellucaCity/scripts.pory"
	.string "All of you! We've been letting you down.\n"
	.string "But now we're gonna prove that we care\l"
	.string "about this city with our actions!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_26:
# 700 "data/maps/PellucaCity/scripts.pory"
	.string "{PLAYER} - the two of us will handle\n"
	.string "the citizens on the bridge and on land.\l"
	.string "Can you surf and rescue the four\l"
	.string "remaining citizens?\p"
	.string "Once you've picked all four of them up,\n"
	.string "come back here.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_27:
# 702 "data/maps/PellucaCity/scripts.pory"
	.string "Good luck, {PLAYER}! We're on top of\n"
	.string "things here, so you go on into the river.\l"
	.string "You don't need to teach any Pokémon\l"
	.string "how to surf - just hop on the water!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_28:
# 705 "data/maps/PellucaCity/scripts.pory"
	.string "But hurry! There's not much time.$"

PellucaCityFlooded_Mayor_Text_0:
# 719 "data/maps/PellucaCity/scripts.pory"
	.string "Have you saved everyone yet?\n"
	.string "Please hurry!$"

PellucaCityFlooded_QwilBoss_Text_0:
# 724 "data/maps/PellucaCity/scripts.pory"
	.string "We're keeping the citizens safe, so you\n"
	.string "go get the rest!$"

PellucaCityFlooded_NPC1_Text_0:
# 728 "data/maps/PellucaCity/scripts.pory"
	.string "The Mayor and the Qwilsquad boss\n"
	.string "working together? Hah! I'll believe it\l"
	.string "when I see it.$"

PellucaCityFlooded_NPC2_Text_0:
# 732 "data/maps/PellucaCity/scripts.pory"
	.string "If the two of them collaborate, maybe\n"
	.string "things will finally improve...$"

PellucaCityFlooded_NPC3_Text_0:
# 736 "data/maps/PellucaCity/scripts.pory"
	.string "I'm so scared - I hope you can save the\n"
	.string "others!$"

PellucaCityFlooded_NPC4_Text_0:
# 740 "data/maps/PellucaCity/scripts.pory"
	.string "I hate that Mega Sharpedo for doing\n"
	.string "this to my home!$"

PellucaCityFlooded_NPCSailor_Text_0:
# 744 "data/maps/PellucaCity/scripts.pory"
	.string "Go on, {PLAYER}! Hurry up and do what\n"
	.string "the boss says.$"

PellucaCityFlooded_NPCSaved_A_Text_0:
# 749 "data/maps/PellucaCity/scripts.pory"
	.string "You saved me! I can't thank you enough,\n"
	.string "trainer.$"

PellucaCityFlooded_NPCSaved_B_Text_0:
# 753 "data/maps/PellucaCity/scripts.pory"
	.string "I owe you, trainer. I'll never forget\n"
	.string "this!$"

PellucaCityFlooded_NPCSaved_C_Text_0:
# 757 "data/maps/PellucaCity/scripts.pory"
	.string "Brr - the water was so cold! How do\n"
	.string "Pokémon swim in it?$"

PellucaCityFlooded_NPCSaved_D_Text_0:
# 761 "data/maps/PellucaCity/scripts.pory"
	.string "When I grow up, I wanna be just like you!$"

PellucaCityFlooded_EventScript_TimesUp_Text_0:
# 766 "data/maps/PellucaCity/scripts.pory"
	.string "The tides rise higher and higher...\n"
	.string "it's too late!$"

PellucaCityFlooded_EventScript_TimesRunningOut_Text_0:
# 799 "data/maps/PellucaCity/scripts.pory"
	.string "The water level is rising...\n"
	.string "There's not much time left!$"

PellucaCityFlooded_Complete_Trigger_Text_0:
# 819 "data/maps/PellucaCity/scripts.pory"
	.string "That's one, two, three...and four!\p"
	.string "Yup, we're all accounted for.$"

PellucaCityFlooded_Complete_Trigger_Text_1:
# 825 "data/maps/PellucaCity/scripts.pory"
	.string "Finally! Thank you {PLAYER}. You did\n"
	.string "us - all of us - a great service.\p"
	.string "You're a hero!$"

PellucaCityFlooded_Complete_Trigger_Text_2:
# 845 "data/maps/PellucaCity/scripts.pory"
	.string "Thank you {PLAYER}!\p"
	.string "You're the best!$"

PellucaCityFlooded_Complete_Trigger_Text_3:
# 858 "data/maps/PellucaCity/scripts.pory"
	.string "It looks like we're all safe for now.$"

PellucaCityFlooded_Complete_Trigger_Text_4:
# 867 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah. All that remains is to wait until\n"
	.string "the water recedes, and then we can go\l"
	.string "back to normal.\p"
	.string "Come, shall we wait in the Pokémon\n"
	.string "Center until then?$"

PellucaCityFlooded_Complete_Trigger_Text_5:
# 872 "data/maps/PellucaCity/scripts.pory"
	.string "Sounds like a good idea. {PLAYER} here\n"
	.string "needs some rest after everything\l"
	.string "that's just happened!$"

PellucaCity_Greta_Main_Text_0:
# 958 "data/maps/PellucaCity/scripts.pory"
	.string "Greta$"

PellucaCity_Greta_Main_Text_1:
# 959 "data/maps/PellucaCity/scripts.pory"
	.string "Oh, it's you again, {PLAYER}!\n"
	.string "Fancy seeing you in these parts.\l"
	.string "Route 6 was a tough trek, wasn't it?$"

PellucaCity_Greta_GottaGo_Text_0:
# 975 "data/maps/PellucaCity/scripts.pory"
	.string "Would you look at the time!\n"
	.string "I've gotta run. See you around!$"

PellucaCity_EventScripts_Gabrielle_Text_0:
# 1005 "data/maps/PellucaCity/scripts.pory"
	.string "Gabrielle$"

PellucaCity_EventScripts_Gabrielle_Text_1:
# 1006 "data/maps/PellucaCity/scripts.pory"
	.string "Ahh, I love the smell of the river!$"

PellucaCity_EventScripts_Gabrielle_Text_2:
# 1011 "data/maps/PellucaCity/scripts.pory"
	.string "I grew up here on this cliff without my\n"
	.string "parents. Life was hard.\p"
	.string "I didn't want my younger siblings to go\n"
	.string "through what I did, so when Team Somber\l"
	.string "promised me money, I took it.\p"
	.string "...\p"
	.string "Those grunts were really vicious to me.\n"
	.string "I was so scared I would lose Zoroark!$"

PellucaCity_EventScripts_Gabrielle_Text_3:
# 1017 "data/maps/PellucaCity/scripts.pory"
	.string "Was I just like that when you met me\n"
	.string "with that hiker with the Clefairy?$"

PellucaCity_EventScripts_Gabrielle_Text_4:
# 1023 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah...I doubt he'd ever forgive me.$"

PellucaCity_EventScripts_Gabrielle_Text_5:
# 1029 "data/maps/PellucaCity/scripts.pory"
	.string "You're just trying to make me feel\n"
	.string "better, aren't you? I don't need your\l"
	.string "pity. I know what I've done.$"

PellucaCity_EventScripts_Gabrielle_Text_6:
# 1034 "data/maps/PellucaCity/scripts.pory"
	.string "After getting kicked out of Team\n"
	.string "Somber, I feel like I've come to my\l"
	.string "senses a little. I'm going to support my\l"
	.string "family - but do it right. Be honest.\p"
	.string "Be responsible.$"

PellucaCity_EventScripts_Gabrielle_Text_7:
# 1040 "data/maps/PellucaCity/scripts.pory"
	.string "I want you to have this. As a thank you.\n"
	.string "For saving me - not just once, but so\l"
	.string "many times. You're a strong trainer, but\l"
	.string "more importantly - you're a good person.\l"
	.string "I hope to be like you.$"

PellucaCity_Gab_ChoiceItem_Text_0:
# 1048 "data/maps/PellucaCity/scripts.pory"
	.string "Choose any one you like.$"

PellucaCity_Gab_ChoiceItem_Text_1:
# 1050 "data/maps/PellucaCity/scripts.pory"
	.string "Choice Specs$"

PellucaCity_Gab_ChoiceItem_Text_2:
# 1050 "data/maps/PellucaCity/scripts.pory"
	.string "Choice Band$"

PellucaCity_Gab_ChoiceItem_Text_3:
# 1050 "data/maps/PellucaCity/scripts.pory"
	.string "Choice Scarf$"

PellucaCity_Gab_ChoiceItem_Give_Text_0:
# 1059 "data/maps/PellucaCity/scripts.pory"
	.string "Are you sure?$"

PellucaCity_Gab_ChoiceItem_End_Text_0:
# 1067 "data/maps/PellucaCity/scripts.pory"
	.string "The choices we make define who we are.\n"
	.string "Once we lock in, we can't change.\p"
	.string "I can't erase what I've done, but I'm\n"
	.string "going to make a better choice this time.\p"
	.string "I suppose you're going to head to the\n"
	.string "Mirroh Base Camp from here? Team\l"
	.string "Somber must've reached there already.\p"
	.string "Best of luck, {PLAYER}.$"

PellucaCity_Zorua_Text_0:
# 1087 "data/maps/PellucaCity/scripts.pory"
	.string "Gabrielle's Zoroark looks content.\n"
	.string "Life is more peaceful for it now!$"

PellucaCity_Lycanroc_Text_0:
# 1108 "data/maps/PellucaCity/scripts.pory"
	.string "Lycanroc is howling. It must be pining\n"
	.string "for a table at the restaurant!$"

PellucaCity_NPC1_Text_0:
# 1121 "data/maps/PellucaCity/scripts.pory"
	.string "Whee!!!$"

PellucaCity_NPC2_Text_0:
# 1126 "data/maps/PellucaCity/scripts.pory"
	.string "A tourist! Have you come to eat at the\n"
	.string "Pelluca Restaurant?\p"
	.string "...that's the only thing our mayor cares\n"
	.string "about promoting.$"

PellucaCity_NPC3_Text_0:
# 1131 "data/maps/PellucaCity/scripts.pory"
	.string "I would've trained up in Mt. Mirroh but\n"
	.string "that Qwilsquad grunt is blocking me!\l"
	.string "So I'm training here instead.$"

PellucaCity_NPC4_Text_0:
# 1136 "data/maps/PellucaCity/scripts.pory"
	.string "This bridge was built by Rivetshore\n"
	.string "Construction. It's nothing like the\l"
	.string "cycling roads in other regions though!$"

PellucaCity_NPC5_Text_0:
# 1142 "data/maps/PellucaCity/scripts.pory"
	.string "Look over there...$"

PellucaCity_NPC5_Text_1:
# 1148 "data/maps/PellucaCity/scripts.pory"
	.string "Jania, the Gym Leader, had her gym\n"
	.string "constructed on a separate island.$"

PellucaCity_NPC5_Text_2:
# 1154 "data/maps/PellucaCity/scripts.pory"
	.string "She stays on that island and trains.\n"
	.string "She never gets involved in city affairs!$"

PellucaCity_NPC6_Text_0:
# 1160 "data/maps/PellucaCity/scripts.pory"
	.string "Are you headed to the Mirroh Base Camp?\n"
	.string "You'll have to cross Route 7 and take\l"
	.string "the cable car up. I heard they're\l"
	.string "closing the gym there though.$"

PellucaCity_NPC7_Text_0:
# 1165 "data/maps/PellucaCity/scripts.pory"
	.string "With the way things are, I'm half in\n"
	.string "support of the Qwilsquad. I know\l"
	.string "they're bullies, but maybe they'll do\l"
	.string "something good for the city.$"

PellucaCity_NPC8_Text_0:
# 1170 "data/maps/PellucaCity/scripts.pory"
	.string "What's even the point of fishing if the\n"
	.string "Mega Sharpedo's going to scare all the\l"
	.string "fish away? I wish our mayor would do\l"
	.string "something about it.$"

PellucaCity_Sealeo_Text_0:
# 1178 "data/maps/PellucaCity/scripts.pory"
	.string "Sealeo wants to catch fish!$"

PellucaCity_NPC9_Text_0:
# 1190 "data/maps/PellucaCity/scripts.pory"
	.string "This is the Pelluca Fishery! But it's\n"
	.string "closed due to the Mega Sharpedo\l"
	.string "attacks.$"

PellucaCity_WingullGirl_Text_0:
# 1201 "data/maps/PellucaCity/scripts.pory"
	.string "Hahaha! I'm throwing stones at the\n"
	.string "Wingulls over there. Wanna throw some?$"

PellucaCity_WingullGirl_Text_1:
# 1203 "data/maps/PellucaCity/scripts.pory"
	.string "That's mean$"

PellucaCity_WingullGirl_Text_2:
# 1203 "data/maps/PellucaCity/scripts.pory"
	.string "Gimme a stone!$"

PellucaCity_WingullGirl_Text_3:
# 1209 "data/maps/PellucaCity/scripts.pory"
	.string "{PLAYER} threw a stone at a Wingull!$"

PellucaCity_WingullGirl_Text_4:
# 1215 "data/maps/PellucaCity/scripts.pory"
	.string "The Wingull gets angry!$"

PellucaCity_WingullGirl_Text_5:
# 1219 "data/maps/PellucaCity/scripts.pory"
	.string "Mean? You're mean!$"

PellucaCity_WingullMother_Text_0:
# 1227 "data/maps/PellucaCity/scripts.pory"
	.string "My daughter loves throwing stones at\n"
	.string "Wingulls. She's just so cute!$"

PellucaCity_WingullCritique_Text_0:
# 1232 "data/maps/PellucaCity/scripts.pory"
	.string "That little girl is so bad! Throwing\n"
	.string "stones at Pokémon...that's poor\l"
	.string "parenting.$"

PellucaCity_NPC10_Text_0:
# 1245 "data/maps/PellucaCity/scripts.pory"
	.string "I ate too many apple tarts! I'm too full.\n"
	.string "Whoever said people have a second\l"
	.string "stomach for dessert was lying!$"

PellucaCity_NPC11_Text_0:
# 1252 "data/maps/PellucaCity/scripts.pory"
	.string "Life is too short to worry!$"

PellucaCity_NPC11_Text_1:
# 1256 "data/maps/PellucaCity/scripts.pory"
	.string "The Pelluca Gym is across the water...\n"
	.string "when I was younger, I tried to challenge\l"
	.string "Jania many times, but I could never win.\p"
	.string "She was my classmate, you know?\n"
	.string "We grew up in Galecrest City together.\n"
	.string "She went on to become a big Gym Leader\l"
	.string "and I moved here too, with a regular\l"
	.string "family and a regular job.\p"
	.string "Whenever I look at the gym, I wonder...\p"
	.string "I don't battle anymore. Maybe you might\n"
	.string "like to use this.$"

PellucaCity_NPC11_Text_2:
# 1259 "data/maps/PellucaCity/scripts.pory"
	.string "It's time for me to pass the baton\n"
	.string "to someone young and hungry.\p"
	.string "Don't give up on your dreams!$"

PellucaCity_NPC12_Text_0:
# 1265 "data/maps/PellucaCity/scripts.pory"
	.string "The mayor isn't maintaining the city one\n"
	.string "bit! My Stantler eating the overgrown\l"
	.string "flowers is actually contributing to\l"
	.string "city maintenance.$"

PellucaCity_Stantler_Text_0:
# 1271 "data/maps/PellucaCity/scripts.pory"
	.string "Stantler is nonchalantly chomping on\n"
	.string "the flowers.$"

PellucaCity_PostGymEvent_Trigger_Text_0:
# 1321 "data/maps/PellucaCity/scripts.pory"
	.string "Excuse me.$"

PellucaCity_PostGymEvent_Trigger_Text_1:
# 1331 "data/maps/PellucaCity/scripts.pory"
	.string "Where am I going?\p"
	.string "I'm going to Rivetshore City.\n"
	.string "All the Gym Leaders have been called\l"
	.string "there.$"

PellucaCity_PostGymEvent_Trigger_Text_2:
# 1350 "data/maps/PellucaCity/scripts.pory"
	.string "{PLAYER}! Over here!$"

PellucaCity_PostGymEvent_Trigger_Text_3:
# 1360 "data/maps/PellucaCity/scripts.pory"
	.string "I overheard Jania talking to someone!\p"
	.string "...\p"
	.string "What? I wasn't eavesdropping!\n"
	.string "She was just nearby.\p"
	.string "She was talking to the eighth Gym\n"
	.string "Leader. They mentioned Team Somber!\p"
	.string "They must be up to something in\n"
	.string "Rivetshore City!\p"
	.string "...$"

PellucaCity_PostGymEvent_Trigger_Text_4:
# 1366 "data/maps/PellucaCity/scripts.pory"
	.string "You're off the case?\p"
	.string "...\p"
	.string "So?\p"
	.string "The {PLAYER} I know wouldn't be\n"
	.string "stopped by something like that!\p"
	.string "You taught me the difference between\n"
	.string "right and wrong. Have you forgotten why\l"
	.string "you're doing this in the first place?\p"
	.string "It was to find YOUR Professor.\n"
	.string "You don't need anyone's permission!\p"
	.string "...\p"
	.string "I'm not letting you give up, {PLAYER}.\p"
	.string "I'm going to Rivetshore City to get the\n"
	.string "final gym badge. It's south of Pelluca\l"
	.string "City - you can get there by surfing.\p"
	.string "I'll be waiting for you!$"

PellucaCity_PostGymEvent_Trigger_Text_5:
# 1374 "data/maps/PellucaCity/scripts.pory"
	.string "You'd better be there, {PLAYER}!$"

PellucaCity_Red_GymBlock_Text_0:
# 1406 "data/maps/PellucaCity/scripts.pory"
	.string "Jania's gone to deal with the Mega\n"
	.string "Sharpedo. You'll find her up in Ivy River\l"
	.string "somewhere.$"

DR_PellucaCity_Arrival_Text_0:
# 1422 "data/maps/PellucaCity/scripts.pory"
	.string "Dockhand$"

DR_PellucaCity_Arrival_Text_1:
# 1423 "data/maps/PellucaCity/scripts.pory"
	.string "A Rainhawk, in a mask? Like something\n"
	.string "out of the old stories.$"

DR_PellucaCity_Arrival_Text_2:
# 1424 "data/maps/PellucaCity/scripts.pory"
	.string "Sailor$"

DR_PellucaCity_Arrival_Text_3:
# 1425 "data/maps/PellucaCity/scripts.pory"
	.string "Heard Sevii took his face. The whole\n"
	.string "beach went up, they say.$"

DR_PellucaCity_Arrival_Text_4:
# 1432 "data/maps/PellucaCity/scripts.pory"
	.string "Rainhawk Alban. Welcome to Pelluca\n"
	.string "Valley.$"

DR_PellucaCity_Arrival_Text_5:
# 1436 "data/maps/PellucaCity/scripts.pory"
	.string "Does it still hurt?$"

DR_PellucaCity_Arrival_Text_6:
# 1438 "data/maps/PellucaCity/scripts.pory"
	.string "Nomad Alban$"

DR_PellucaCity_Arrival_Text_7:
# 1439 "data/maps/PellucaCity/scripts.pory"
	.string "Less than it did.$"

DR_PellucaCity_Arrival_Text_8:
# 1441 "data/maps/PellucaCity/scripts.pory"
	.string "Good. Walk with me. We will talk\n"
	.string "somewhere quieter.$"

PellucaCityFlooded_TriggerText::
# 341 "data/maps/PellucaCity/scripts.pory"
	.string "I need to save the drowning citizens!$"
