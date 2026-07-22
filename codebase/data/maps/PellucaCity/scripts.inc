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
    .set LOCALID_DR_TIDAL, 61
# 17 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_DR_CADMUS, 62

PellucaCity_MapScripts::
# 22 "data/maps/PellucaCity/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaCity_MapScripts_MAP_SCRIPT_ON_TRANSITION
# 26 "data/maps/PellucaCity/scripts.pory"
	map_script MAP_SCRIPT_ON_FRAME_TABLE, PellucaCity_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE
	.byte 0

PellucaCity_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 23 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_VISITED_PELLUCA_CITY
# 24 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_SetLayout
	return

PellucaCity_MapScripts_MAP_SCRIPT_ON_FRAME_TABLE:
# 27 "data/maps/PellucaCity/scripts.pory"
	map_script_2 VAR_UNUSED_0x404E, 1, DR_PellucaCity_Arrival
# 28 "data/maps/PellucaCity/scripts.pory"
	map_script_2 VAR_PELLUCA_MAYOR_QUEST, 3, PellucaCityFlooded_MainEvent
	.2byte 0


PellucaCity_SetLayout::
# 33 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCity_SetLayout_2
# 38 "data/maps/PellucaCity/scripts.pory"
	setmaplayoutindex LAYOUT_PELLUCA_CITY
PellucaCity_SetLayout_1:
	return

PellucaCity_SetLayout_2:
# 34 "data/maps/PellucaCity/scripts.pory"
	setmaplayoutindex LAYOUT_PELLUCA_CITY_FLOODED
# 35 "data/maps/PellucaCity/scripts.pory"
	setweather WEATHER_RAIN_THUNDERSTORM
# 36 "data/maps/PellucaCity/scripts.pory"
	doweather
	goto PellucaCity_SetLayout_1


PellucaCity_MayorFight_Trigger::
# 53 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_MAYOR_FIGHT, PellucaCity_MayorFight_Trigger_2
# 55 "data/maps/PellucaCity/scripts.pory"
	lockall
# 58 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 59 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCity_MayorFight_Trigger_Movement_0
# 60 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 61 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 64 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_1
# 65 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 66 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 67 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 68 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_1
# 69 "data/maps/PellucaCity/scripts.pory"
	release
# 70 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 72 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_2
# 73 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 74 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 75 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 76 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_3
# 77 "data/maps/PellucaCity/scripts.pory"
	release
# 78 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 80 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_3
# 81 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 82 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 83 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 84 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_4
# 85 "data/maps/PellucaCity/scripts.pory"
	release
# 86 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 88 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_4
# 89 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 90 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 91 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 92 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_6
# 93 "data/maps/PellucaCity/scripts.pory"
	release
# 94 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 96 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_5
# 97 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 98 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 99 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 100 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_7
# 101 "data/maps/PellucaCity/scripts.pory"
	release
# 102 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 104 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_6
# 105 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_6
# 106 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 107 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 108 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_8
# 109 "data/maps/PellucaCity/scripts.pory"
	release
# 110 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 112 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_7
# 113 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 114 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 115 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 116 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_9
# 117 "data/maps/PellucaCity/scripts.pory"
	release
# 118 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 120 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_7
# 121 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 122 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 123 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_8
# 130 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 131 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 133 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 134 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_10
# 135 "data/maps/PellucaCity/scripts.pory"
	release
# 136 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 138 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_6
# 139 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_6
# 140 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 141 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 142 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_11
# 143 "data/maps/PellucaCity/scripts.pory"
	release
# 144 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 146 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_7
# 147 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 148 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 149 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 150 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_12
# 151 "data/maps/PellucaCity/scripts.pory"
	release
# 152 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 155 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_9
# 156 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 157 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_9
# 158 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_10
# 159 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 160 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_9
# 161 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_9
# 162 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_11
# 163 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 164 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_12
# 165 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_12
# 166 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_12
# 167 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 172 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_13
# 173 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 174 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 175 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 176 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_13
# 177 "data/maps/PellucaCity/scripts.pory"
	release
# 178 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 180 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_14
# 181 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 182 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 183 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 184 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_14
# 185 "data/maps/PellucaCity/scripts.pory"
	release
# 186 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 187 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_15
# 188 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 189 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 193 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 194 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCity_MayorFight_Trigger_Movement_16
# 195 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 196 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 198 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_MAYOR
# 199 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S1
# 200 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S2
# 201 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S3
# 202 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_MAYOR_FIGHT
# 204 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_MayorFight_Trigger_2:
	end


PellucaCity_Sailor_Entrance::
# 221 "data/maps/PellucaCity/scripts.pory"
	lockall
# 222 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 224 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 225 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_Entrance_Text_0
# 226 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 0
	goto_if_eq PellucaCity_Sailor_Entrance_2
# 227 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 1
	goto_if_eq PellucaCity_Sailor_Entrance_5
# 229 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_Multichoice
# 231 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Sailor_Entrance_2:
# 226 "data/maps/PellucaCity/scripts.pory"
	release
	end

PellucaCity_Sailor_Entrance_5:
# 227 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_Sailor_Multichoice::
# 235 "data/maps/PellucaCity/scripts.pory"
	message PellucaCity_Sailor_Multichoice_Text_0
# 236 "data/maps/PellucaCity/scripts.pory"
	waitmessage
# 237 "data/maps/PellucaCity/scripts.pory"
	dynmultichoice 0, 0, FALSE, 4, 0, DYN_MULTICHOICE_CB_NONE, PellucaCity_Sailor_Multichoice_Text_1, PellucaCity_Sailor_Multichoice_Text_2, PellucaCity_Sailor_Multichoice_Text_3
# 239 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 0
	goto_if_eq PellucaCity_Sailor_Multichoice_2
PellucaCity_Sailor_Multichoice_1:
# 240 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Sailor_Multichoice_5
PellucaCity_Sailor_Multichoice_4:
# 242 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Sailor_Multichoice_2:
# 239 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_QwilsquadExplanation
	goto PellucaCity_Sailor_Multichoice_1

PellucaCity_Sailor_Multichoice_5:
# 240 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_MemberCheck
	goto PellucaCity_Sailor_Multichoice_4


PellucaCity_Sailor_QwilsquadExplanation::
# 246 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 247 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_QwilsquadExplanation_Text_0
# 248 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_Multichoice
	return


PellucaCity_Sailor_MemberCheck::
# 251 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 252 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_0, MSGBOX_YESNO
# 254 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 0
	goto_if_eq PellucaCity_Sailor_MemberCheck_2
PellucaCity_Sailor_MemberCheck_1:
# 258 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Sailor_MemberCheck_5
PellucaCity_Sailor_MemberCheck_4:
# 280 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Sailor_MemberCheck_2:
# 255 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 256 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_1
	goto PellucaCity_Sailor_MemberCheck_1

PellucaCity_Sailor_MemberCheck_5:
# 259 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 260 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_2
# 261 "data/maps/PellucaCity/scripts.pory"
	release
# 264 "data/maps/PellucaCity/scripts.pory"
	special ChoosePartyMon
# 265 "data/maps/PellucaCity/scripts.pory"
	waitstate
# 266 "data/maps/PellucaCity/scripts.pory"
	copyvar VAR_0x800A, VAR_0x8004
# 267 "data/maps/PellucaCity/scripts.pory"
	copyvar VAR_0x8005, VAR_0x800A
# 268 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetTradeSpecies
# 270 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, SPECIES_QWILFISH_HISUI
	goto_if_eq PellucaCity_Sailor_MemberCheck_8
PellucaCity_Sailor_MemberCheck_7:
# 271 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, SPECIES_OVERQWIL
	goto_if_eq PellucaCity_Sailor_MemberCheck_11
PellucaCity_Sailor_MemberCheck_10:
# 273 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_ENTRANCE, PellucaCity_MayorFight_Trigger_Movement_7
# 274 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 275 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 276 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_3
	goto PellucaCity_Sailor_MemberCheck_4

PellucaCity_Sailor_MemberCheck_8:
# 270 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_MemberAccepted
	goto PellucaCity_Sailor_MemberCheck_7

PellucaCity_Sailor_MemberCheck_11:
# 271 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_MemberAccepted
	goto PellucaCity_Sailor_MemberCheck_10


PellucaCity_Sailor_MemberAccepted::
# 284 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_ENTRANCE, PellucaCity_MayorFight_Trigger_Movement_7
# 285 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 286 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 287 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberAccepted_Text_0
# 288 "data/maps/PellucaCity/scripts.pory"
	release
# 290 "data/maps/PellucaCity/scripts.pory"
	opendoor 3, 42
# 291 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 292 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_ENTRANCE, PellucaCity_MayorFight_Trigger_Movement_11
# 293 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 294 "data/maps/PellucaCity/scripts.pory"
	playse SE_EXIT
# 295 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S_ENTRANCE
# 296 "data/maps/PellucaCity/scripts.pory"
	closedoor 3, 42
# 297 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 299 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_QWILSQUAD_ENTRANCE
# 300 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Blocker::
# 315 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Blocker_Text_0
	end


PellucaCity_Blocker_Trigger::
# 319 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 10
	goto_if_eq PellucaCity_Blocker_Trigger_2
# 321 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_BLOCKER, PellucaCity_MayorFight_Trigger_Movement_7
# 322 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 323 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Blocker_Trigger_Text_0
# 324 "data/maps/PellucaCity/scripts.pory"
	release
# 325 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_Blocker_Trigger_Movement_0
# 326 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 327 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Blocker_Trigger_2:
	end


PellucaCityFlooded_TriggerDown::
# 347 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerDown_1
	end

PellucaCityFlooded_TriggerDown_1:
# 348 "data/maps/PellucaCity/scripts.pory"
	lockall
# 349 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 350 "data/maps/PellucaCity/scripts.pory"
	release
# 351 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_10
# 352 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 353 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_TriggerUp::
# 360 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerUp_1
	end

PellucaCityFlooded_TriggerUp_1:
# 361 "data/maps/PellucaCity/scripts.pory"
	lockall
# 362 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 363 "data/maps/PellucaCity/scripts.pory"
	release
# 364 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_11
# 365 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 366 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_TriggerLeft::
# 373 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerLeft_1
	end

PellucaCityFlooded_TriggerLeft_1:
# 374 "data/maps/PellucaCity/scripts.pory"
	lockall
# 375 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 376 "data/maps/PellucaCity/scripts.pory"
	release
# 377 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_9
# 378 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 379 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_TriggerRight::
# 386 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerRight_1
	end

PellucaCityFlooded_TriggerRight_1:
# 387 "data/maps/PellucaCity/scripts.pory"
	lockall
# 388 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 389 "data/maps/PellucaCity/scripts.pory"
	release
# 390 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_Blocker_Trigger_Movement_0
# 391 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 392 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_SaveCitizen_A::
# 399 "data/maps/PellucaCity/scripts.pory"
	lockall
# 400 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 401 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_A_Text_0
# 402 "data/maps/PellucaCity/scripts.pory"
	release
# 405 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 407 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_EAST
	goto_if_eq PellucaCityFlooded_SaveCitizen_A_2
# 412 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_A_Movement_1
# 413 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 414 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_A_1:
# 418 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A_SAVED
# 419 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 421 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_A_2:
# 408 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_A_Movement_0
# 409 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 410 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_A_1


PellucaCityFlooded_SaveCitizen_B::
# 425 "data/maps/PellucaCity/scripts.pory"
	lockall
# 426 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 427 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_B_Text_0
# 428 "data/maps/PellucaCity/scripts.pory"
	release
# 430 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 432 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_SOUTH
	goto_if_eq PellucaCityFlooded_SaveCitizen_B_2
# 437 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_B_Movement_1
# 438 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 439 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_B_1:
# 442 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B_SAVED
# 443 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 445 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_B_2:
# 433 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_B_Movement_0
# 434 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 435 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_B_1


PellucaCityFlooded_SaveCitizen_C::
# 449 "data/maps/PellucaCity/scripts.pory"
	lockall
# 450 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 451 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_C_Text_0
# 452 "data/maps/PellucaCity/scripts.pory"
	release
# 455 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 457 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_NORTH
	goto_if_eq PellucaCityFlooded_SaveCitizen_C_2
# 462 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_C_Movement_1
# 463 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 464 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_C_1:
# 467 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C_SAVED
# 468 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 470 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_C_2:
# 458 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_C_Movement_0
# 459 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 460 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_C_1


PellucaCityFlooded_SaveCitizen_D::
# 474 "data/maps/PellucaCity/scripts.pory"
	lockall
# 475 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 476 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_D_Text_0
# 477 "data/maps/PellucaCity/scripts.pory"
	release
# 480 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 482 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_WEST
	goto_if_eq PellucaCityFlooded_SaveCitizen_D_2
# 487 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_D_Movement_1
# 488 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 489 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_D_1:
# 492 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D_SAVED
# 493 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 495 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_D_2:
# 483 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_D_Movement_0
# 484 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 485 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_D_1


PellucaCityFlooded_MainEvent::
# 500 "data/maps/PellucaCity/scripts.pory"
	lockall
# 501 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAYOR_QUEST, 4
# 502 "data/maps/PellucaCity/scripts.pory"
	playbgm MUS_DUMMY, FALSE
# 504 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_SKIP_PELLUCA_CUTSCENE, PellucaCityFlooded_MainEvent_2
PellucaCityFlooded_MainEvent_1:
# 516 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCityFlooded_MainEvent_Cutscene
	return

PellucaCityFlooded_MainEvent_2:
# 505 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Text_0, MSGBOX_YESNO
# 506 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCityFlooded_MainEvent_4
	goto PellucaCityFlooded_MainEvent_1

PellucaCityFlooded_MainEvent_4:
# 507 "data/maps/PellucaCity/scripts.pory"
	fadescreen FADE_TO_WHITE
# 508 "data/maps/PellucaCity/scripts.pory"
	additem ITEM_HM03
# 509 "data/maps/PellucaCity/scripts.pory"
	special EnterSafariMode
# 510 "data/maps/PellucaCity/scripts.pory"
	fadescreen FADE_FROM_WHITE
# 511 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_MainEvent_Cutscene::
# 521 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_SKIP_PELLUCA_CUTSCENE
# 523 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 524 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_0
# 525 "data/maps/PellucaCity/scripts.pory"
	release
# 526 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 529 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 530 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_MainEvent_Cutscene_Movement_0
# 532 "data/maps/PellucaCity/scripts.pory"
	delay 60
# 535 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 536 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_2
# 537 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 538 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_3
# 539 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 540 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_4
# 541 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 542 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_5
# 543 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 544 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_6
# 547 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_6
# 548 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 549 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 550 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_7
# 551 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_3
# 552 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 553 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 554 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_8
# 557 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_CITIZEN, PellucaCityFlooded_MainEvent_Cutscene_Movement_1
# 558 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 559 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_9
# 560 "data/maps/PellucaCity/scripts.pory"
	release
# 561 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 563 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_5
# 564 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_5
# 565 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_5
# 566 "data/maps/PellucaCity/scripts.pory"
	applymovement 48, PellucaCity_MayorFight_Trigger_Movement_5
# 567 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 568 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 570 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 571 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_10
# 572 "data/maps/PellucaCity/scripts.pory"
	release
# 574 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_7
# 575 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_7
# 576 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_7
# 577 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_7
# 578 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCity_MayorFight_Trigger_Movement_7
# 579 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_7
# 580 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 581 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 583 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 584 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_11
# 585 "data/maps/PellucaCity/scripts.pory"
	release
# 587 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 590 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_12
# 591 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_13
# 592 "data/maps/PellucaCity/scripts.pory"
	release
# 593 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 595 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_5
# 596 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_5
# 597 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_5
# 598 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_5
# 599 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCityFlooded_MainEvent_Cutscene_Movement_2
# 600 "data/maps/PellucaCity/scripts.pory"
	applymovement 48, PellucaCity_MayorFight_Trigger_Movement_5
# 601 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_5
# 603 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 604 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_14
# 605 "data/maps/PellucaCity/scripts.pory"
	release
# 607 "data/maps/PellucaCity/scripts.pory"
	addobject LOCALID_FL_JANIA
# 608 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_MainEvent_Cutscene_Movement_3
# 609 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 611 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_4
# 612 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_4
# 613 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_4
# 614 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_4
# 615 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCity_MayorFight_Trigger_Movement_4
# 616 "data/maps/PellucaCity/scripts.pory"
	applymovement 48, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 617 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 618 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_4
# 620 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_7
# 621 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 622 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 623 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_15
# 624 "data/maps/PellucaCity/scripts.pory"
	release
# 625 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 627 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_7
# 628 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 629 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 630 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_16
# 631 "data/maps/PellucaCity/scripts.pory"
	release
# 632 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 634 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 635 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_18
# 636 "data/maps/PellucaCity/scripts.pory"
	release
# 637 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 639 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCityFlooded_MainEvent_Cutscene_Movement_6
# 640 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCityFlooded_MainEvent_Cutscene_Movement_6
# 641 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 642 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 644 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 645 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_19
# 646 "data/maps/PellucaCity/scripts.pory"
	release
# 647 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 648 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 649 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 650 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 651 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 652 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_20
# 653 "data/maps/PellucaCity/scripts.pory"
	release
# 654 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_SYS_SURF_ENABLED
# 656 "data/maps/PellucaCity/scripts.pory"
	checkitem ITEM_HM03
# 657 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, TRUE
	goto_if_eq PellucaCityFlooded_MainEvent_Cutscene_2
PellucaCityFlooded_MainEvent_Cutscene_1:
# 661 "data/maps/PellucaCity/scripts.pory"
	giveitem ITEM_HM03
# 662 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 663 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_MayorFight_Trigger_Movement_4
# 664 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 665 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 666 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_21
# 667 "data/maps/PellucaCity/scripts.pory"
	release
# 668 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 671 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_MainEvent_Cutscene_Movement_7
# 672 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 673 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCityFlooded_MainEvent_Cutscene_Movement_8
# 674 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 677 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 678 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 679 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 680 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 681 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_22
# 682 "data/maps/PellucaCity/scripts.pory"
	release
# 683 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 684 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 685 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_23
# 686 "data/maps/PellucaCity/scripts.pory"
	release
# 687 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 688 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 689 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_24
# 690 "data/maps/PellucaCity/scripts.pory"
	release
# 691 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 692 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 693 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_24
# 694 "data/maps/PellucaCity/scripts.pory"
	release
# 695 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 697 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_5
# 698 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_5
# 699 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 700 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_25
# 701 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 702 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_26
# 703 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 704 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_27
# 705 "data/maps/PellucaCity/scripts.pory"
	release
# 706 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 707 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_28
# 708 "data/maps/PellucaCity/scripts.pory"
	release
# 710 "data/maps/PellucaCity/scripts.pory"
	completesubquest QUEST_PELLUCA_CITY, SUB_QUEST_2
# 712 "data/maps/PellucaCity/scripts.pory"
	special EnterSafariMode
# 713 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 714 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_MainEvent_Cutscene_2:
# 658 "data/maps/PellucaCity/scripts.pory"
	removeitem ITEM_HM03
	goto PellucaCityFlooded_MainEvent_Cutscene_1


PellucaCityFlooded_Mayor::
# 720 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 721 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Mayor_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_QwilBoss::
# 725 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 726 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_QwilBoss_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC1::
# 730 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC1_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC2::
# 734 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC2_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC3::
# 738 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC3_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC4::
# 742 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC4_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSailor::
# 746 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSailor_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_A::
# 751 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_A_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_B::
# 755 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_B_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_C::
# 759 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_C_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_D::
# 763 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_D_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_EventScript_TimesUp::
# 767 "data/maps/PellucaCity/scripts.pory"
	lockall
# 768 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_EventScript_TimesUp_Text_0
# 769 "data/maps/PellucaCity/scripts.pory"
	release
# 772 "data/maps/PellucaCity/scripts.pory"
	removeitem ITEM_HM03
# 774 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_REGULAR_CITIZENS
# 775 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZENS
# 777 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A_SAVED
# 778 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B_SAVED
# 779 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C_SAVED
# 780 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D_SAVED
# 782 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A
# 783 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B
# 784 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C
# 785 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D
# 787 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAP_STATE, 1
# 789 "data/maps/PellucaCity/scripts.pory"
	delay 2
# 791 "data/maps/PellucaCity/scripts.pory"
	special ExitSafariMode
# 792 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAYOR_QUEST, 3
# 793 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAP_STATE, 1
# 794 "data/maps/PellucaCity/scripts.pory"
	warp MAP_PELLUCA_CITY, 43, 28
# 795 "data/maps/PellucaCity/scripts.pory"
	waitstate
	end


PellucaCityFlooded_EventScript_TimesRunningOut::
# 800 "data/maps/PellucaCity/scripts.pory"
	lockall
# 801 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_EventScript_TimesRunningOut_Text_0
# 802 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCityFlooded_Complete_Trigger::
# 809 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 8
	goto_if_eq PellucaCityFlooded_Complete_Trigger_2
	end

PellucaCityFlooded_Complete_Trigger_2:
# 811 "data/maps/PellucaCity/scripts.pory"
	special ExitSafariMode
# 813 "data/maps/PellucaCity/scripts.pory"
	lockall
# 814 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCityFlooded_MainEvent_Cutscene_Movement_8
# 815 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_Complete_Trigger_Movement_0
# 816 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 817 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 820 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 821 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_0
# 822 "data/maps/PellucaCity/scripts.pory"
	release
# 823 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 826 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 827 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_1
# 828 "data/maps/PellucaCity/scripts.pory"
	release
# 829 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 831 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 832 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_Complete_Trigger_Movement_1
# 833 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 837 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_7
# 838 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_7
# 839 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_7
# 840 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_7
# 841 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCity_MayorFight_Trigger_Movement_7
# 842 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_7
# 843 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 844 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 846 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 847 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_2
# 848 "data/maps/PellucaCity/scripts.pory"
	release
# 849 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 851 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_Complete_Trigger_Movement_2
# 852 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 853 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 854 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 856 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_6
# 857 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 858 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 859 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 860 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_3
# 861 "data/maps/PellucaCity/scripts.pory"
	release
# 862 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 865 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_3
# 866 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 867 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 868 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 869 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_4
# 870 "data/maps/PellucaCity/scripts.pory"
	release
# 871 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 873 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 874 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_5
# 875 "data/maps/PellucaCity/scripts.pory"
	release
# 876 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 880 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAYOR_QUEST, 9
# 881 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAP_STATE, 0
# 883 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_REGULAR_CITIZENS
# 884 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZENS
# 886 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A_SAVED
# 887 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B_SAVED
# 888 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C_SAVED
# 889 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D_SAVED
# 891 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_PC_CHARS
# 894 "data/maps/PellucaCity/scripts.pory"
	warp MAP_PELLUCA_CITY_POKEMON_CENTER, 7, 6
# 896 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Greta_Trigger0::
# 926 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_GRETA_PELLUCACITY, PellucaCity_Greta_Trigger0_2
# 928 "data/maps/PellucaCity/scripts.pory"
	lockall
# 929 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_Trigger0_Movement_0
# 930 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 931 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 932 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 933 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_Main
	return

PellucaCity_Greta_Trigger0_2:
	end


PellucaCity_Greta_Trigger1::
# 937 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_GRETA_PELLUCACITY, PellucaCity_Greta_Trigger1_2
# 939 "data/maps/PellucaCity/scripts.pory"
	lockall
# 940 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_Trigger1_Movement_0
# 941 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 942 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 943 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 944 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_Main
	return

PellucaCity_Greta_Trigger1_2:
	end


PellucaCity_Greta_Trigger2::
# 948 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_GRETA_PELLUCACITY, PellucaCity_Greta_Trigger2_2
# 950 "data/maps/PellucaCity/scripts.pory"
	lockall
# 951 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_Trigger2_Movement_0
# 952 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 953 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 954 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 955 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_Main
	return

PellucaCity_Greta_Trigger2_2:
	end


PellucaCity_Greta_Main::
# 960 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_Greta_Main_Text_0
# 961 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Greta_Main_Text_1
# 962 "data/maps/PellucaCity/scripts.pory"
	release
# 963 "data/maps/PellucaCity/scripts.pory"
	delay 20
# 964 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_Greta_Main_Text_0
# 965 "data/maps/PellucaCity/scripts.pory"
	msgbox Common_Text_Greta_Comecome
# 966 "data/maps/PellucaCity/scripts.pory"
	release
# 967 "data/maps/PellucaCity/scripts.pory"
	delay 20
# 969 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_ShowItemsForSale
	return


PellucaCity_Greta_GottaGo::
# 973 "data/maps/PellucaCity/scripts.pory"
	release
# 974 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_MayorFight_Trigger_Movement_7
# 975 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 976 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_Greta_Main_Text_0
# 977 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Greta_GottaGo_Text_0
# 978 "data/maps/PellucaCity/scripts.pory"
	release
# 979 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_GottaGo_Movement_0
# 980 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 981 "data/maps/PellucaCity/scripts.pory"
	removeobject 27
# 982 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_GRETA_PELLUCACITY
# 983 "data/maps/PellucaCity/scripts.pory"
	fadedefaultbgm
# 985 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_EventScripts_Gabrielle::
# 1005 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1006 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_GABRIELLE_CHOICEBAND, PellucaCity_EventScripts_Gabrielle_1
# 1012 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1013 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_2
# 1014 "data/maps/PellucaCity/scripts.pory"
	release
# 1015 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1016 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1017 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1018 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1019 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_3, MSGBOX_YESNO
# 1020 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_EventScripts_Gabrielle_5
# 1029 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1030 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1031 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_5
# 1032 "data/maps/PellucaCity/scripts.pory"
	release
PellucaCity_EventScripts_Gabrielle_4:
# 1034 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 1035 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1036 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_6
# 1037 "data/maps/PellucaCity/scripts.pory"
	release
# 1038 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1039 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1040 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1041 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1042 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_7
# 1043 "data/maps/PellucaCity/scripts.pory"
	release
# 1044 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem
	return

PellucaCity_EventScripts_Gabrielle_1:
# 1007 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1008 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_1
# 1009 "data/maps/PellucaCity/scripts.pory"
	release
	return

PellucaCity_EventScripts_Gabrielle_5:
# 1022 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1023 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1024 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1025 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_4
# 1026 "data/maps/PellucaCity/scripts.pory"
	release
	goto PellucaCity_EventScripts_Gabrielle_4


PellucaCity_Gab_ChoiceItem::
# 1049 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1050 "data/maps/PellucaCity/scripts.pory"
	message PellucaCity_Gab_ChoiceItem_Text_0
# 1051 "data/maps/PellucaCity/scripts.pory"
	waitmessage
# 1052 "data/maps/PellucaCity/scripts.pory"
	dynmultichoice 0, 0, TRUE, 4, 0, DYN_MULTICHOICE_CB_NONE, PellucaCity_Gab_ChoiceItem_Text_1, PellucaCity_Gab_ChoiceItem_Text_2, PellucaCity_Gab_ChoiceItem_Text_3
# 1053 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 0
	goto_if_eq PellucaCity_Gab_ChoiceItem_2
PellucaCity_Gab_ChoiceItem_1:
# 1054 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Gab_ChoiceItem_5
PellucaCity_Gab_ChoiceItem_4:
# 1055 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 2
	goto_if_eq PellucaCity_Gab_ChoiceItem_8
PellucaCity_Gab_ChoiceItem_7:
# 1056 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem_Give
	return

PellucaCity_Gab_ChoiceItem_2:
# 1053 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_0x8006, ITEM_CHOICE_SPECS
	goto PellucaCity_Gab_ChoiceItem_1

PellucaCity_Gab_ChoiceItem_5:
# 1054 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_0x8006, ITEM_CHOICE_BAND
	goto PellucaCity_Gab_ChoiceItem_4

PellucaCity_Gab_ChoiceItem_8:
# 1055 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_0x8006, ITEM_CHOICE_SCARF
	goto PellucaCity_Gab_ChoiceItem_7


PellucaCity_Gab_ChoiceItem_Give::
# 1060 "data/maps/PellucaCity/scripts.pory"
	showitemdescription
# 1061 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Gab_ChoiceItem_Give_Text_0, MSGBOX_YESNO
# 1062 "data/maps/PellucaCity/scripts.pory"
	hideitemdescription
# 1063 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Gab_ChoiceItem_Give_1
# 1064 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem
	return

PellucaCity_Gab_ChoiceItem_Give_1:
# 1063 "data/maps/PellucaCity/scripts.pory"
	giveitem VAR_0x8006
# 1063 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem_End
	return


PellucaCity_Gab_ChoiceItem_End::
# 1068 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1069 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Gab_ChoiceItem_End_Text_0
# 1070 "data/maps/PellucaCity/scripts.pory"
	release
# 1071 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_GABRIELLE_CHOICEBAND
# 1072 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1073 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1074 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Zorua::
# 1086 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1087 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1088 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_ZOROARK, CRY_MODE_NORMAL
# 1089 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Zorua_Text_0
# 1090 "data/maps/PellucaCity/scripts.pory"
	release
# 1091 "data/maps/PellucaCity/scripts.pory"
	applymovement 25, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1092 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1093 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Lycanroc::
# 1109 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_LYCANROC, CRY_MODE_NORMAL
# 1110 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Lycanroc_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC1::
# 1123 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC1_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC2::
# 1128 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC2_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC3::
# 1133 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC3_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC4::
# 1138 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC4_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC5::
# 1143 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1144 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC5_Text_0
# 1145 "data/maps/PellucaCity/scripts.pory"
	release
# 1146 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 1147 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCity_NPC5_Movement_0
# 1148 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1149 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 1150 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC5_Text_1
# 1151 "data/maps/PellucaCity/scripts.pory"
	release
# 1152 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 1153 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCity_NPC5_Movement_1
# 1154 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1155 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 1156 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC5_Text_2, MSGBOX_NPC
# 1157 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_NPC6::
# 1162 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC6_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC7::
# 1167 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC7_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC8::
# 1172 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC8_Text_0, MSGBOX_NPC
	end


PellucaCity_Sealeo::
# 1177 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1178 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1179 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_SEALEO, CRY_MODE_NORMAL
# 1180 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sealeo_Text_0, MSGBOX_NPC
# 1181 "data/maps/PellucaCity/scripts.pory"
	release
# 1182 "data/maps/PellucaCity/scripts.pory"
	applymovement 26, PellucaCity_MayorFight_Trigger_Movement_4
# 1183 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1184 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_NPC9::
# 1192 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC9_Text_0, MSGBOX_NPC
	end


PellucaCity_WingullGirl::
# 1201 "data/maps/PellucaCity/scripts.pory"
	lock
# 1202 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1203 "data/maps/PellucaCity/scripts.pory"
	message PellucaCity_WingullGirl_Text_0
# 1204 "data/maps/PellucaCity/scripts.pory"
	waitmessage
# 1205 "data/maps/PellucaCity/scripts.pory"
	dynmultichoice 16, 8, TRUE, 4, 0, DYN_MULTICHOICE_CB_NONE, PellucaCity_WingullGirl_Text_1, PellucaCity_WingullGirl_Text_2
# 1207 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_WingullGirl_2
# 1221 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullGirl_Text_5, MSGBOX_NPC
PellucaCity_WingullGirl_1:
# 1224 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_WingullGirl_2:
# 1209 "data/maps/PellucaCity/scripts.pory"
	applymovement 15, PellucaCity_MayorFight_Trigger_Movement_5
# 1210 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_5
# 1211 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullGirl_Text_3
# 1212 "data/maps/PellucaCity/scripts.pory"
	release
# 1213 "data/maps/PellucaCity/scripts.pory"
	applymovement 16, PellucaCity_MayorFight_Trigger_Movement_7
# 1214 "data/maps/PellucaCity/scripts.pory"
	applymovement 17, PellucaCity_MayorFight_Trigger_Movement_7
# 1215 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1216 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1217 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullGirl_Text_4
# 1218 "data/maps/PellucaCity/scripts.pory"
	setwildbattle SPECIES_WINGULL, 25
# 1219 "data/maps/PellucaCity/scripts.pory"
	dowildbattle
	goto PellucaCity_WingullGirl_1


PellucaCity_WingullMother::
# 1229 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullMother_Text_0, MSGBOX_NPC
	end


PellucaCity_WingullCritique::
# 1234 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullCritique_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC10::
# 1247 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC10_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC11::
# 1253 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_CITY_TM_GIVER, PellucaCity_NPC11_2
# 1258 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC11_Text_1, MSGBOX_NPC
# 1259 "data/maps/PellucaCity/scripts.pory"
	giveitem ITEM_TM31
# 1260 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_CITY_TM_GIVER
# 1261 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC11_Text_2, MSGBOX_NPC
	end

PellucaCity_NPC11_2:
# 1254 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC11_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC12::
# 1267 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC12_Text_0, MSGBOX_NPC
	end


PellucaCity_Stantler::
# 1272 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_STANTLER, CRY_MODE_NORMAL
# 1273 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Stantler_Text_0, MSGBOX_NPC
	end


PellucaCity_PostGymEvent_Trigger::
# 1300 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_POSTGYM, PellucaCity_PostGymEvent_Trigger_2
# 1302 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_BADGE07_GET, PellucaCity_PostGymEvent_Trigger_5
	end

PellucaCity_PostGymEvent_Trigger_2:
	end

PellucaCity_PostGymEvent_Trigger_5:
# 1303 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1306 "data/maps/PellucaCity/scripts.pory"
	opendoor 37, 8
# 1307 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 1310 "data/maps/PellucaCity/scripts.pory"
	addobject LOCALID_FL_JANIA
# 1311 "data/maps/PellucaCity/scripts.pory"
	setobjectxy LOCALID_FL_JANIA, 37, 8
# 1313 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_MayorFight_Trigger_Movement_10
# 1314 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1317 "data/maps/PellucaCity/scripts.pory"
	closedoor 37, 8
# 1319 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_Complete_Trigger_Movement_2
# 1320 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1322 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 1323 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_0
# 1324 "data/maps/PellucaCity/scripts.pory"
	release
# 1325 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_PostGymEvent_Trigger_Movement_0
# 1326 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_Complete_Trigger_Movement_2
# 1327 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1328 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1329 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_MayorFight_Trigger_Movement_5
# 1330 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1331 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1332 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 1333 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_1
# 1334 "data/maps/PellucaCity/scripts.pory"
	release
# 1336 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 1337 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_PostGymEvent_Trigger_Movement_1
# 1338 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_Complete_Trigger_Movement_0
# 1339 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1341 "data/maps/PellucaCity/scripts.pory"
	opendoor 37, 8
# 1342 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 1345 "data/maps/PellucaCity/scripts.pory"
	addobject LOCALID_GAB
# 1346 "data/maps/PellucaCity/scripts.pory"
	setobjectxy LOCALID_GAB, 37, 8
# 1347 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_PostGymEvent_Trigger_Movement_2
# 1348 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1349 "data/maps/PellucaCity/scripts.pory"
	closedoor 37, 8
# 1350 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1351 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1352 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_2
# 1353 "data/maps/PellucaCity/scripts.pory"
	release
# 1355 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_PostGymEvent_Trigger_Movement_3
# 1356 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1357 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 1358 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1359 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1361 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1362 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_3
# 1363 "data/maps/PellucaCity/scripts.pory"
	release
# 1364 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_MayorFight_Trigger_Movement_7
# 1365 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1366 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1367 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1368 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_4
# 1369 "data/maps/PellucaCity/scripts.pory"
	release
# 1370 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1371 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_4
# 1372 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_PostGymEvent_Trigger_Movement_4
# 1373 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1374 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1375 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1376 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_5
# 1377 "data/maps/PellucaCity/scripts.pory"
	release
# 1378 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_PostGymEvent_Trigger_Movement_5
# 1379 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1380 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1382 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 1385 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_FL_JANIA
# 1386 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_GAB
# 1389 "data/maps/PellucaCity/scripts.pory"
	startquest QUEST_STOP_TEAM_SOMBER
# 1390 "data/maps/PellucaCity/scripts.pory"
	subquestmenu QUEST_MENU_COMPLETE_QUEST, QUEST_STOP_TEAM_SOMBER, SUB_QUEST_1
# 1391 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_POSTGYM
	end


PellucaCity_Red_GymBlock::
# 1408 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Red_GymBlock_Text_0, MSGBOX_NPC
	end


DR_PellucaCity_Arrival::
# 1416 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1417 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_UNUSED_0x404E, 2
# 1418 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_5
# 1419 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1420 "data/maps/PellucaCity/scripts.pory"
	delay 20
# 1421 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_DR_CADMUS, DR_PellucaCity_Arrival_Movement_0
# 1422 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1423 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1424 "data/maps/PellucaCity/scripts.pory"
	speakername DR_PellucaCity_Arrival_Text_0
# 1425 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_1
# 1426 "data/maps/PellucaCity/scripts.pory"
	release
# 1427 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1428 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_DR_CADMUS, DR_PellucaCity_Arrival_Movement_1
# 1429 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1430 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_PellucaCity_Arrival_Movement_2
# 1431 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1432 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1433 "data/maps/PellucaCity/scripts.pory"
	playse SE_EXIT
# 1434 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_DR_CADMUS
# 1435 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1436 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_2
# 1437 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1438 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1439 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_UNUSED_0x884
# 1440 "data/maps/PellucaCity/scripts.pory"
	warp MAP_PELLUCA_UMBRA_LAB, 0
# 1441 "data/maps/PellucaCity/scripts.pory"
	waitstate
	end


# 59 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_0:
# 59 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 59 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 59 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 59 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 64 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_1:
# 64 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 64 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_left
	step_end

# 72 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_2:
# 72 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 72 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_right
	step_end

# 80 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_3:
# 80 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_left
	step_end

# 88 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_4:
# 88 "data/maps/PellucaCity/scripts.pory"
	face_down
	step_end

# 96 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_5:
# 96 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 104 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_6:
# 104 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_right
	step_end

# 112 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_7:
# 112 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
	step_end

# 123 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_8:
# 124 "data/maps/PellucaCity/scripts.pory"
	lock_anim
# 125 "data/maps/PellucaCity/scripts.pory"
	lock_facing_direction
# 126 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 127 "data/maps/PellucaCity/scripts.pory"
	unlock_anim
# 128 "data/maps/PellucaCity/scripts.pory"
	unlock_facing_direction
	step_end

# 155 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_9:
# 155 "data/maps/PellucaCity/scripts.pory"
	walk_left
	step_end

# 158 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_10:
# 158 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 162 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_11:
# 162 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 164 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_12:
# 164 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 164 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 164 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 164 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 164 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 164 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 164 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 164 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 164 "data/maps/PellucaCity/scripts.pory"
	walk_left
	step_end

# 172 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_13:
# 172 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 172 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 180 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_14:
# 180 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 180 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 180 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 180 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 180 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 180 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 187 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_15:
# 187 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 187 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 187 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 187 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 187 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 187 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 194 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_16:
# 194 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 194 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 194 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 194 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 325 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Blocker_Trigger_Movement_0:
# 325 "data/maps/PellucaCity/scripts.pory"
	walk_right
	step_end

# 408 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_A_Movement_0:
# 408 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 408 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 408 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 408 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 408 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 408 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 408 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 408 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 408 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 408 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
	step_end

# 412 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_A_Movement_1:
# 412 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 412 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 412 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 412 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 412 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 412 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 412 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 412 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 412 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
	step_end

# 433 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_B_Movement_0:
# 433 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 433 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 433 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 433 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 433 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 433 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 433 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 433 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 437 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_B_Movement_1:
# 437 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 437 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 437 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 437 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 437 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 437 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 437 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 458 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_C_Movement_0:
# 458 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 458 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 458 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 458 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 458 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 458 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 458 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 458 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
	step_end

# 462 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_C_Movement_1:
# 462 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 462 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 462 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 462 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 462 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 462 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 462 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
	step_end

# 483 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_D_Movement_0:
# 483 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 483 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 483 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 483 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 483 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 483 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 483 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 483 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 483 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 483 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
	step_end

# 487 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_D_Movement_1:
# 487 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 487 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 487 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 487 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 487 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 487 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 487 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 487 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 487 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
	step_end

# 530 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_0:
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 530 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 557 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_1:
# 557 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 557 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_down
	step_end

# 599 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_2:
# 599 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 599 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 608 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_3:
# 608 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 608 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 608 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 608 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 608 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 608 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 608 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 608 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 608 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 608 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 616 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_4:
# 616 "data/maps/PellucaCity/scripts.pory"
	face_right
	step_end

# 617 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_5:
# 617 "data/maps/PellucaCity/scripts.pory"
	face_left
	step_end

# 639 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_6:
# 639 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 639 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_up
	step_end

# 671 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_7:
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 671 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 673 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_8:
# 673 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 673 "data/maps/PellucaCity/scripts.pory"
	face_down
	step_end

# 815 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_Complete_Trigger_Movement_0:
# 815 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 815 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 815 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 832 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_Complete_Trigger_Movement_1:
# 832 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 832 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 851 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_Complete_Trigger_Movement_2:
# 851 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 851 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 929 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_Trigger0_Movement_0:
# 929 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 929 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 929 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 929 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 929 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 929 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 929 "data/maps/PellucaCity/scripts.pory"
	face_left
	step_end

# 940 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_Trigger1_Movement_0:
# 940 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 940 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 940 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 940 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 940 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 940 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 940 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 940 "data/maps/PellucaCity/scripts.pory"
	face_right
	step_end

# 951 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_Trigger2_Movement_0:
# 951 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 951 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 951 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 951 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 951 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 951 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 951 "data/maps/PellucaCity/scripts.pory"
	face_right
	step_end

# 979 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_GottaGo_Movement_0:
# 979 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 979 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 979 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 979 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 979 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 979 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 979 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 979 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 1147 "data/maps/PellucaCity/scripts.pory"
PellucaCity_NPC5_Movement_0:
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1147 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 1153 "data/maps/PellucaCity/scripts.pory"
PellucaCity_NPC5_Movement_1:
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 1153 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
	step_end

# 1325 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_0:
# 1325 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1325 "data/maps/PellucaCity/scripts.pory"
	face_down
	step_end

# 1337 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_1:
# 1337 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1337 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1337 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 1337 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 1337 "data/maps/PellucaCity/scripts.pory"
	walk_left
	step_end

# 1347 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_2:
# 1347 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1347 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
	step_end

# 1355 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_3:
# 1355 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1355 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1355 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1355 "data/maps/PellucaCity/scripts.pory"
	face_left
	step_end

# 1372 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_4:
# 1372 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1372 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1372 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1372 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 1378 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_5:
# 1378 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1378 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1378 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 1421 "data/maps/PellucaCity/scripts.pory"
DR_PellucaCity_Arrival_Movement_0:
# 1421 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1421 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1421 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1421 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1421 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 1428 "data/maps/PellucaCity/scripts.pory"
DR_PellucaCity_Arrival_Movement_1:
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1428 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1428 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 1430 "data/maps/PellucaCity/scripts.pory"
DR_PellucaCity_Arrival_Movement_2:
# 1430 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1430 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1430 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1430 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1430 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1430 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1430 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1430 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1430 "data/maps/PellucaCity/scripts.pory"
	walk_right
	step_end

PellucaCity_MayorFight_Trigger_Text_0:
# 67 "data/maps/PellucaCity/scripts.pory"
	.string "Mayor$"

PellucaCity_MayorFight_Trigger_Text_1:
# 68 "data/maps/PellucaCity/scripts.pory"
	.string "But you can't be doing this to our\n"
	.string "citizens! This is our city!$"

PellucaCity_MayorFight_Trigger_Text_2:
# 75 "data/maps/PellucaCity/scripts.pory"
	.string "Q-squad Boss$"

PellucaCity_MayorFight_Trigger_Text_3:
# 76 "data/maps/PellucaCity/scripts.pory"
	.string "I've told you a hundred times, you\n"
	.string "paper-pushing wimp! You ain't doing a\l"
	.string "single thing right for our city, so don't\l"
	.string "you dare mess with the Qwilsquad!\p"
	.string "This is our turf - we don't give a hoot\n"
	.string "about you and your title!$"

PellucaCity_MayorFight_Trigger_Text_4:
# 84 "data/maps/PellucaCity/scripts.pory"
	.string "No! Enough is enough! I'm putting my\n"
	.string "foot down.\p"
	.string "You and your lot aren't allowed in\n"
	.string "Pelluca City any more!$"

PellucaCity_MayorFight_Trigger_Text_5:
# 91 "data/maps/PellucaCity/scripts.pory"
	.string "Q-squad Grunt$"

PellucaCity_MayorFight_Trigger_Text_6:
# 92 "data/maps/PellucaCity/scripts.pory"
	.string "Hahaha! What a lame mayor!$"

PellucaCity_MayorFight_Trigger_Text_7:
# 100 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah! He really thinks he can tell us\n"
	.string "what to do!$"

PellucaCity_MayorFight_Trigger_Text_8:
# 108 "data/maps/PellucaCity/scripts.pory"
	.string "Go on boss - teach him a lesson!$"

PellucaCity_MayorFight_Trigger_Text_9:
# 116 "data/maps/PellucaCity/scripts.pory"
	.string "You heard 'em Mayor. Looks like my boys\n"
	.string "want me to prove that we own this city!\p"
	.string "Wanna try me? Right here?$"

PellucaCity_MayorFight_Trigger_Text_10:
# 134 "data/maps/PellucaCity/scripts.pory"
	.string "Nono - see, I'm not - look, I'm just\n"
	.string "asking for a little cooperation and -$"

PellucaCity_MayorFight_Trigger_Text_11:
# 142 "data/maps/PellucaCity/scripts.pory"
	.string "Hahaha! Look at the wimp! Poor guy.$"

PellucaCity_MayorFight_Trigger_Text_12:
# 150 "data/maps/PellucaCity/scripts.pory"
	.string "Got it, mayor? You're not in charge here.\p"
	.string "I am!\p"
	.string "And from now on, this city belongs\n"
	.string "to us - the Qwilsquad!$"

PellucaCity_MayorFight_Trigger_Text_13:
# 176 "data/maps/PellucaCity/scripts.pory"
	.string "Oh - a tourist! Were you standing there\n"
	.string "the whole time?\p"
	.string "...\p"
	.string "I'm sorry you had to witness that.\p"
	.string "Y-you know, we have a wonderful\n"
	.string "Game Corner! And the Apple Pie at the\l"
	.string "Pelluca Restaurant is to die for.$"

PellucaCity_MayorFight_Trigger_Text_14:
# 184 "data/maps/PellucaCity/scripts.pory"
	.string "Sigh...what will I do?$"

PellucaCity_Sailor_Entrance_Text_0:
# 225 "data/maps/PellucaCity/scripts.pory"
	.string "Beat it, kid! This is private property\n"
	.string "belonging to the Qwilsquad.$"

PellucaCity_Sailor_Multichoice_Text_0:
# 235 "data/maps/PellucaCity/scripts.pory"
	.string "Only Qwilsquad members can enter!$"

PellucaCity_Sailor_Multichoice_Text_1:
# 237 "data/maps/PellucaCity/scripts.pory"
	.string "What's a Qwilsquad?$"

PellucaCity_Sailor_Multichoice_Text_2:
# 237 "data/maps/PellucaCity/scripts.pory"
	.string "I'm a member!$"

PellucaCity_Sailor_Multichoice_Text_3:
# 237 "data/maps/PellucaCity/scripts.pory"
	.string "Okay...$"

PellucaCity_Sailor_QwilsquadExplanation_Text_0:
# 247 "data/maps/PellucaCity/scripts.pory"
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
# 252 "data/maps/PellucaCity/scripts.pory"
	.string "A pipsqueak like you is in the squad?\n"
	.string "You a new member? Got any proof?$"

PellucaCity_Sailor_MemberCheck_Text_1:
# 256 "data/maps/PellucaCity/scripts.pory"
	.string "Then beat it, kid!$"

PellucaCity_Sailor_MemberCheck_Text_2:
# 260 "data/maps/PellucaCity/scripts.pory"
	.string "Show me!$"

PellucaCity_Sailor_MemberCheck_Text_3:
# 276 "data/maps/PellucaCity/scripts.pory"
	.string "That don't look like no Qwilfish to me!\p"
	.string "Beat it, kid!$"

PellucaCity_Sailor_MemberAccepted_Text_0:
# 287 "data/maps/PellucaCity/scripts.pory"
	.string "Now that's what I'm talking about!\n"
	.string "You're one of us, kid.\p"
	.string "Go on, get inside!$"

PellucaCity_Blocker_Text_0:
# 315 "data/maps/PellucaCity/scripts.pory"
	.string "This is our city! Got any problems?$"

PellucaCity_Blocker_Trigger_Text_0:
# 323 "data/maps/PellucaCity/scripts.pory"
	.string "Hey kid, where d'you think yer goin?\n"
	.string "There's a toll if you wanna get out.\p"
	.string "That's right! You gotta pay ¥999999.\p"
	.string "Ain't got the money?\p"
	.string "Then get packing!$"

PellucaCityFlooded_SaveCitizen_A_Text_0:
# 401 "data/maps/PellucaCity/scripts.pory"
	.string "Help! Help! Over here!\p"
	.string "...\p"
	.string "Thank you so much - I'm saved!$"

PellucaCityFlooded_SaveCitizen_B_Text_0:
# 427 "data/maps/PellucaCity/scripts.pory"
	.string "I can't stay afloat any more!\p"
	.string "...\p"
	.string "You came just in time!$"

PellucaCityFlooded_SaveCitizen_C_Text_0:
# 451 "data/maps/PellucaCity/scripts.pory"
	.string "Ahh! It's too cold!\p"
	.string "...\p"
	.string "Waah! Wahh! It was so scary!$"

PellucaCityFlooded_SaveCitizen_D_Text_0:
# 476 "data/maps/PellucaCity/scripts.pory"
	.string "Help! Someone save me!\p"
	.string "...\p"
	.string "Yaay! You came!$"

PellucaCityFlooded_MainEvent_Text_0:
# 505 "data/maps/PellucaCity/scripts.pory"
	.string "Skip cutscene?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_0:
# 524 "data/maps/PellucaCity/scripts.pory"
	.string "What on earth is this?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_1:
# 535 "data/maps/PellucaCity/scripts.pory"
	.string "Citizen$"

PellucaCityFlooded_MainEvent_Cutscene_Text_2:
# 536 "data/maps/PellucaCity/scripts.pory"
	.string "What a disaster!\p"
	.string "How could we be so unlucky!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_3:
# 538 "data/maps/PellucaCity/scripts.pory"
	.string "What happened?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_4:
# 540 "data/maps/PellucaCity/scripts.pory"
	.string "A Mega Sharpedo came rampaging down\n"
	.string "from the Ivy River and kicked up a\l"
	.string "storm! The riverbanks have flooded.\p"
	.string "The city's underwater!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_5:
# 542 "data/maps/PellucaCity/scripts.pory"
	.string "Is everyone safe?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_6:
# 544 "data/maps/PellucaCity/scripts.pory"
	.string "No - there are still four people in the\n"
	.string "water! We have to save them fast!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_7:
# 550 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah, go on Mayor. Go save them!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_8:
# 554 "data/maps/PellucaCity/scripts.pory"
	.string "W-what do you mean? Weren't you the\n"
	.string "one in control of this city?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_9:
# 559 "data/maps/PellucaCity/scripts.pory"
	.string "ENOUGH!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_10:
# 571 "data/maps/PellucaCity/scripts.pory"
	.string "While you two bicker, it's us that pays\n"
	.string "the price every time! Both of you are\l"
	.string "strong - a tough trainer and a smart\l"
	.string "politician - and yet, neither of you\l"
	.string "bother to actually do anything for us\l"
	.string "citizens! And now people are in danger\l"
	.string "and you're still fighting! We've all had\l"
	.string "it up to here with you two!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_11:
# 584 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah!\p"
	.string "Hear hear!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_12:
# 590 "data/maps/PellucaCity/scripts.pory"
	.string "???$"

PellucaCityFlooded_MainEvent_Cutscene_Text_13:
# 591 "data/maps/PellucaCity/scripts.pory"
	.string "I agree too.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_14:
# 604 "data/maps/PellucaCity/scripts.pory"
	.string "Is that Jania?\p"
	.string "Yeah! It's the Gym Leader! In the flesh!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_15:
# 623 "data/maps/PellucaCity/scripts.pory"
	.string "Oh, Jania! It's you! Finally. Please - you\n"
	.string "have to save those still drowning!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_16:
# 630 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah, Jania! You're an even stronger\n"
	.string "trainer than I am. You can do it!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_17:
# 634 "data/maps/PellucaCity/scripts.pory"
	.string "Jania$"

PellucaCityFlooded_MainEvent_Cutscene_Text_18:
# 635 "data/maps/PellucaCity/scripts.pory"
	.string "No, I won't.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_19:
# 645 "data/maps/PellucaCity/scripts.pory"
	.string "Don't look at me like that!\p"
	.string "You two want to be responsible for this\n"
	.string "city? Start right here, right now.\p"
	.string "Your citizens are miserably tired of\n"
	.string "both of you - when will you two change?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_20:
# 652 "data/maps/PellucaCity/scripts.pory"
	.string "And who might you be?\p"
	.string "...\p"
	.string "{PLAYER}?\p"
	.string "...\p"
	.string "I see - so that's how you got involved\n"
	.string "with these two.\p"
	.string "Here, take this.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_21:
# 666 "data/maps/PellucaCity/scripts.pory"
	.string "Consider this my help.\p"
	.string "Now I'm going to track the Mega\n"
	.string "Sharpedo down and make sure it doesn't\l"
	.string "harm anyone else.\p"
	.string "And the two of you - and {PLAYER} -\n"
	.string "take this chance to do the right thing!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_22:
# 681 "data/maps/PellucaCity/scripts.pory"
	.string "Hmpf.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_23:
# 685 "data/maps/PellucaCity/scripts.pory"
	.string "Tchah!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_24:
# 689 "data/maps/PellucaCity/scripts.pory"
	.string "...$"

PellucaCityFlooded_MainEvent_Cutscene_Text_25:
# 700 "data/maps/PellucaCity/scripts.pory"
	.string "All of you! We've been letting you down.\n"
	.string "But now we're gonna prove that we care\l"
	.string "about this city with our actions!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_26:
# 702 "data/maps/PellucaCity/scripts.pory"
	.string "{PLAYER} - the two of us will handle\n"
	.string "the citizens on the bridge and on land.\l"
	.string "Can you surf and rescue the four\l"
	.string "remaining citizens?\p"
	.string "Once you've picked all four of them up,\n"
	.string "come back here.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_27:
# 704 "data/maps/PellucaCity/scripts.pory"
	.string "Good luck, {PLAYER}! We're on top of\n"
	.string "things here, so you go on into the river.\l"
	.string "You don't need to teach any Pokémon\l"
	.string "how to surf - just hop on the water!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_28:
# 707 "data/maps/PellucaCity/scripts.pory"
	.string "But hurry! There's not much time.$"

PellucaCityFlooded_Mayor_Text_0:
# 721 "data/maps/PellucaCity/scripts.pory"
	.string "Have you saved everyone yet?\n"
	.string "Please hurry!$"

PellucaCityFlooded_QwilBoss_Text_0:
# 726 "data/maps/PellucaCity/scripts.pory"
	.string "We're keeping the citizens safe, so you\n"
	.string "go get the rest!$"

PellucaCityFlooded_NPC1_Text_0:
# 730 "data/maps/PellucaCity/scripts.pory"
	.string "The Mayor and the Qwilsquad boss\n"
	.string "working together? Hah! I'll believe it\l"
	.string "when I see it.$"

PellucaCityFlooded_NPC2_Text_0:
# 734 "data/maps/PellucaCity/scripts.pory"
	.string "If the two of them collaborate, maybe\n"
	.string "things will finally improve...$"

PellucaCityFlooded_NPC3_Text_0:
# 738 "data/maps/PellucaCity/scripts.pory"
	.string "I'm so scared - I hope you can save the\n"
	.string "others!$"

PellucaCityFlooded_NPC4_Text_0:
# 742 "data/maps/PellucaCity/scripts.pory"
	.string "I hate that Mega Sharpedo for doing\n"
	.string "this to my home!$"

PellucaCityFlooded_NPCSailor_Text_0:
# 746 "data/maps/PellucaCity/scripts.pory"
	.string "Go on, {PLAYER}! Hurry up and do what\n"
	.string "the boss says.$"

PellucaCityFlooded_NPCSaved_A_Text_0:
# 751 "data/maps/PellucaCity/scripts.pory"
	.string "You saved me! I can't thank you enough,\n"
	.string "trainer.$"

PellucaCityFlooded_NPCSaved_B_Text_0:
# 755 "data/maps/PellucaCity/scripts.pory"
	.string "I owe you, trainer. I'll never forget\n"
	.string "this!$"

PellucaCityFlooded_NPCSaved_C_Text_0:
# 759 "data/maps/PellucaCity/scripts.pory"
	.string "Brr - the water was so cold! How do\n"
	.string "Pokémon swim in it?$"

PellucaCityFlooded_NPCSaved_D_Text_0:
# 763 "data/maps/PellucaCity/scripts.pory"
	.string "When I grow up, I wanna be just like you!$"

PellucaCityFlooded_EventScript_TimesUp_Text_0:
# 768 "data/maps/PellucaCity/scripts.pory"
	.string "The tides rise higher and higher...\n"
	.string "it's too late!$"

PellucaCityFlooded_EventScript_TimesRunningOut_Text_0:
# 801 "data/maps/PellucaCity/scripts.pory"
	.string "The water level is rising...\n"
	.string "There's not much time left!$"

PellucaCityFlooded_Complete_Trigger_Text_0:
# 821 "data/maps/PellucaCity/scripts.pory"
	.string "That's one, two, three...and four!\p"
	.string "Yup, we're all accounted for.$"

PellucaCityFlooded_Complete_Trigger_Text_1:
# 827 "data/maps/PellucaCity/scripts.pory"
	.string "Finally! Thank you {PLAYER}. You did\n"
	.string "us - all of us - a great service.\p"
	.string "You're a hero!$"

PellucaCityFlooded_Complete_Trigger_Text_2:
# 847 "data/maps/PellucaCity/scripts.pory"
	.string "Thank you {PLAYER}!\p"
	.string "You're the best!$"

PellucaCityFlooded_Complete_Trigger_Text_3:
# 860 "data/maps/PellucaCity/scripts.pory"
	.string "It looks like we're all safe for now.$"

PellucaCityFlooded_Complete_Trigger_Text_4:
# 869 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah. All that remains is to wait until\n"
	.string "the water recedes, and then we can go\l"
	.string "back to normal.\p"
	.string "Come, shall we wait in the Pokémon\n"
	.string "Center until then?$"

PellucaCityFlooded_Complete_Trigger_Text_5:
# 874 "data/maps/PellucaCity/scripts.pory"
	.string "Sounds like a good idea. {PLAYER} here\n"
	.string "needs some rest after everything\l"
	.string "that's just happened!$"

PellucaCity_Greta_Main_Text_0:
# 960 "data/maps/PellucaCity/scripts.pory"
	.string "Greta$"

PellucaCity_Greta_Main_Text_1:
# 961 "data/maps/PellucaCity/scripts.pory"
	.string "Oh, it's you again, {PLAYER}!\n"
	.string "Fancy seeing you in these parts.\l"
	.string "Route 6 was a tough trek, wasn't it?$"

PellucaCity_Greta_GottaGo_Text_0:
# 977 "data/maps/PellucaCity/scripts.pory"
	.string "Would you look at the time!\n"
	.string "I've gotta run. See you around!$"

PellucaCity_EventScripts_Gabrielle_Text_0:
# 1007 "data/maps/PellucaCity/scripts.pory"
	.string "Gabrielle$"

PellucaCity_EventScripts_Gabrielle_Text_1:
# 1008 "data/maps/PellucaCity/scripts.pory"
	.string "Ahh, I love the smell of the river!$"

PellucaCity_EventScripts_Gabrielle_Text_2:
# 1013 "data/maps/PellucaCity/scripts.pory"
	.string "I grew up here on this cliff without my\n"
	.string "parents. Life was hard.\p"
	.string "I didn't want my younger siblings to go\n"
	.string "through what I did, so when Team Somber\l"
	.string "promised me money, I took it.\p"
	.string "...\p"
	.string "Those grunts were really vicious to me.\n"
	.string "I was so scared I would lose Zoroark!$"

PellucaCity_EventScripts_Gabrielle_Text_3:
# 1019 "data/maps/PellucaCity/scripts.pory"
	.string "Was I just like that when you met me\n"
	.string "with that hiker with the Clefairy?$"

PellucaCity_EventScripts_Gabrielle_Text_4:
# 1025 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah...I doubt he'd ever forgive me.$"

PellucaCity_EventScripts_Gabrielle_Text_5:
# 1031 "data/maps/PellucaCity/scripts.pory"
	.string "You're just trying to make me feel\n"
	.string "better, aren't you? I don't need your\l"
	.string "pity. I know what I've done.$"

PellucaCity_EventScripts_Gabrielle_Text_6:
# 1036 "data/maps/PellucaCity/scripts.pory"
	.string "After getting kicked out of Team\n"
	.string "Somber, I feel like I've come to my\l"
	.string "senses a little. I'm going to support my\l"
	.string "family - but do it right. Be honest.\p"
	.string "Be responsible.$"

PellucaCity_EventScripts_Gabrielle_Text_7:
# 1042 "data/maps/PellucaCity/scripts.pory"
	.string "I want you to have this. As a thank you.\n"
	.string "For saving me - not just once, but so\l"
	.string "many times. You're a strong trainer, but\l"
	.string "more importantly - you're a good person.\l"
	.string "I hope to be like you.$"

PellucaCity_Gab_ChoiceItem_Text_0:
# 1050 "data/maps/PellucaCity/scripts.pory"
	.string "Choose any one you like.$"

PellucaCity_Gab_ChoiceItem_Text_1:
# 1052 "data/maps/PellucaCity/scripts.pory"
	.string "Choice Specs$"

PellucaCity_Gab_ChoiceItem_Text_2:
# 1052 "data/maps/PellucaCity/scripts.pory"
	.string "Choice Band$"

PellucaCity_Gab_ChoiceItem_Text_3:
# 1052 "data/maps/PellucaCity/scripts.pory"
	.string "Choice Scarf$"

PellucaCity_Gab_ChoiceItem_Give_Text_0:
# 1061 "data/maps/PellucaCity/scripts.pory"
	.string "Are you sure?$"

PellucaCity_Gab_ChoiceItem_End_Text_0:
# 1069 "data/maps/PellucaCity/scripts.pory"
	.string "The choices we make define who we are.\n"
	.string "Once we lock in, we can't change.\p"
	.string "I can't erase what I've done, but I'm\n"
	.string "going to make a better choice this time.\p"
	.string "I suppose you're going to head to the\n"
	.string "Mirroh Base Camp from here? Team\l"
	.string "Somber must've reached there already.\p"
	.string "Best of luck, {PLAYER}.$"

PellucaCity_Zorua_Text_0:
# 1089 "data/maps/PellucaCity/scripts.pory"
	.string "Gabrielle's Zoroark looks content.\n"
	.string "Life is more peaceful for it now!$"

PellucaCity_Lycanroc_Text_0:
# 1110 "data/maps/PellucaCity/scripts.pory"
	.string "Lycanroc is howling. It must be pining\n"
	.string "for a table at the restaurant!$"

PellucaCity_NPC1_Text_0:
# 1123 "data/maps/PellucaCity/scripts.pory"
	.string "Whee!!!$"

PellucaCity_NPC2_Text_0:
# 1128 "data/maps/PellucaCity/scripts.pory"
	.string "A tourist! Have you come to eat at the\n"
	.string "Pelluca Restaurant?\p"
	.string "...that's the only thing our mayor cares\n"
	.string "about promoting.$"

PellucaCity_NPC3_Text_0:
# 1133 "data/maps/PellucaCity/scripts.pory"
	.string "I would've trained up in Mt. Mirroh but\n"
	.string "that Qwilsquad grunt is blocking me!\l"
	.string "So I'm training here instead.$"

PellucaCity_NPC4_Text_0:
# 1138 "data/maps/PellucaCity/scripts.pory"
	.string "This bridge was built by Rivetshore\n"
	.string "Construction. It's nothing like the\l"
	.string "cycling roads in other regions though!$"

PellucaCity_NPC5_Text_0:
# 1144 "data/maps/PellucaCity/scripts.pory"
	.string "Look over there...$"

PellucaCity_NPC5_Text_1:
# 1150 "data/maps/PellucaCity/scripts.pory"
	.string "Jania, the Gym Leader, had her gym\n"
	.string "constructed on a separate island.$"

PellucaCity_NPC5_Text_2:
# 1156 "data/maps/PellucaCity/scripts.pory"
	.string "She stays on that island and trains.\n"
	.string "She never gets involved in city affairs!$"

PellucaCity_NPC6_Text_0:
# 1162 "data/maps/PellucaCity/scripts.pory"
	.string "Are you headed to the Mirroh Base Camp?\n"
	.string "You'll have to cross Route 7 and take\l"
	.string "the cable car up. I heard they're\l"
	.string "closing the gym there though.$"

PellucaCity_NPC7_Text_0:
# 1167 "data/maps/PellucaCity/scripts.pory"
	.string "With the way things are, I'm half in\n"
	.string "support of the Qwilsquad. I know\l"
	.string "they're bullies, but maybe they'll do\l"
	.string "something good for the city.$"

PellucaCity_NPC8_Text_0:
# 1172 "data/maps/PellucaCity/scripts.pory"
	.string "What's even the point of fishing if the\n"
	.string "Mega Sharpedo's going to scare all the\l"
	.string "fish away? I wish our mayor would do\l"
	.string "something about it.$"

PellucaCity_Sealeo_Text_0:
# 1180 "data/maps/PellucaCity/scripts.pory"
	.string "Sealeo wants to catch fish!$"

PellucaCity_NPC9_Text_0:
# 1192 "data/maps/PellucaCity/scripts.pory"
	.string "This is the Pelluca Fishery! But it's\n"
	.string "closed due to the Mega Sharpedo\l"
	.string "attacks.$"

PellucaCity_WingullGirl_Text_0:
# 1203 "data/maps/PellucaCity/scripts.pory"
	.string "Hahaha! I'm throwing stones at the\n"
	.string "Wingulls over there. Wanna throw some?$"

PellucaCity_WingullGirl_Text_1:
# 1205 "data/maps/PellucaCity/scripts.pory"
	.string "That's mean$"

PellucaCity_WingullGirl_Text_2:
# 1205 "data/maps/PellucaCity/scripts.pory"
	.string "Gimme a stone!$"

PellucaCity_WingullGirl_Text_3:
# 1211 "data/maps/PellucaCity/scripts.pory"
	.string "{PLAYER} threw a stone at a Wingull!$"

PellucaCity_WingullGirl_Text_4:
# 1217 "data/maps/PellucaCity/scripts.pory"
	.string "The Wingull gets angry!$"

PellucaCity_WingullGirl_Text_5:
# 1221 "data/maps/PellucaCity/scripts.pory"
	.string "Mean? You're mean!$"

PellucaCity_WingullMother_Text_0:
# 1229 "data/maps/PellucaCity/scripts.pory"
	.string "My daughter loves throwing stones at\n"
	.string "Wingulls. She's just so cute!$"

PellucaCity_WingullCritique_Text_0:
# 1234 "data/maps/PellucaCity/scripts.pory"
	.string "That little girl is so bad! Throwing\n"
	.string "stones at Pokémon...that's poor\l"
	.string "parenting.$"

PellucaCity_NPC10_Text_0:
# 1247 "data/maps/PellucaCity/scripts.pory"
	.string "I ate too many apple tarts! I'm too full.\n"
	.string "Whoever said people have a second\l"
	.string "stomach for dessert was lying!$"

PellucaCity_NPC11_Text_0:
# 1254 "data/maps/PellucaCity/scripts.pory"
	.string "Life is too short to worry!$"

PellucaCity_NPC11_Text_1:
# 1258 "data/maps/PellucaCity/scripts.pory"
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
# 1261 "data/maps/PellucaCity/scripts.pory"
	.string "It's time for me to pass the baton\n"
	.string "to someone young and hungry.\p"
	.string "Don't give up on your dreams!$"

PellucaCity_NPC12_Text_0:
# 1267 "data/maps/PellucaCity/scripts.pory"
	.string "The mayor isn't maintaining the city one\n"
	.string "bit! My Stantler eating the overgrown\l"
	.string "flowers is actually contributing to\l"
	.string "city maintenance.$"

PellucaCity_Stantler_Text_0:
# 1273 "data/maps/PellucaCity/scripts.pory"
	.string "Stantler is nonchalantly chomping on\n"
	.string "the flowers.$"

PellucaCity_PostGymEvent_Trigger_Text_0:
# 1323 "data/maps/PellucaCity/scripts.pory"
	.string "Excuse me.$"

PellucaCity_PostGymEvent_Trigger_Text_1:
# 1333 "data/maps/PellucaCity/scripts.pory"
	.string "Where am I going?\p"
	.string "I'm going to Rivetshore City.\n"
	.string "All the Gym Leaders have been called\l"
	.string "there.$"

PellucaCity_PostGymEvent_Trigger_Text_2:
# 1352 "data/maps/PellucaCity/scripts.pory"
	.string "{PLAYER}! Over here!$"

PellucaCity_PostGymEvent_Trigger_Text_3:
# 1362 "data/maps/PellucaCity/scripts.pory"
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
# 1368 "data/maps/PellucaCity/scripts.pory"
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
# 1376 "data/maps/PellucaCity/scripts.pory"
	.string "You'd better be there, {PLAYER}!$"

PellucaCity_Red_GymBlock_Text_0:
# 1408 "data/maps/PellucaCity/scripts.pory"
	.string "Jania's gone to deal with the Mega\n"
	.string "Sharpedo. You'll find her up in Ivy River\l"
	.string "somewhere.$"

DR_PellucaCity_Arrival_Text_0:
# 1424 "data/maps/PellucaCity/scripts.pory"
	.string "Cadmus$"

DR_PellucaCity_Arrival_Text_1:
# 1425 "data/maps/PellucaCity/scripts.pory"
	.string "10 years on and by the grace of\n"
	.string "Arceus... I am beyond elated to see you\l"
	.string "again, my Prince.\p"
	.string "Sending you away as a child to an\n"
	.string "overseas military installation, forcing\l"
	.string "you to bear the alias of Nomad Alban all\l"
	.string "of this time... none of it was fair. But it\l"
	.string "was all necessary to ensure your\l"
	.string "survival.\p"
	.string "But now, you are home at last... even if\n"
	.string "the circumstances that bring you home\l"
	.string "are grim. Dark forces are afoot, and\l"
	.string "they are gradually gaining leverage\l"
	.string "over our Empire in spite of my best\l"
	.string "efforts.\p"
	.string "But come - one of my labs here in\n"
	.string "Pelluca Valley is just ahead, and we\l"
	.string "have much to discuss.$"

PellucaCityFlooded_TriggerText::
# 343 "data/maps/PellucaCity/scripts.pory"
	.string "I need to save the drowning citizens!$"
