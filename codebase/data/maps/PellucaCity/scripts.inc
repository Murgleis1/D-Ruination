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
    .set LOCALID_DR_TIDAL, 1
# 17 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_DR_CADMUS, 2
# 18 "data/maps/PellucaCity/scripts.pory"
    .set LOCALID_DR_SHRINE_KEEPER, 3

PellucaCity_MapScripts::
# 23 "data/maps/PellucaCity/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaCity_MapScripts_MAP_SCRIPT_ON_TRANSITION
	.byte 0

PellucaCity_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 24 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_VISITED_PELLUCA_CITY
# 25 "data/maps/PellucaCity/scripts.pory"
	call PellucaCity_EventScript_WimpodFlags
	return


PellucaCity_SetLayout::
# 30 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCity_SetLayout_2
# 35 "data/maps/PellucaCity/scripts.pory"
	setmaplayoutindex LAYOUT_PELLUCA_CITY
PellucaCity_SetLayout_1:
	return

PellucaCity_SetLayout_2:
# 31 "data/maps/PellucaCity/scripts.pory"
	setmaplayoutindex LAYOUT_PELLUCA_CITY_FLOODED
# 32 "data/maps/PellucaCity/scripts.pory"
	setweather WEATHER_RAIN_THUNDERSTORM
# 33 "data/maps/PellucaCity/scripts.pory"
	doweather
	goto PellucaCity_SetLayout_1


PellucaCity_MayorFight_Trigger::
# 50 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_MAYOR_FIGHT, PellucaCity_MayorFight_Trigger_2
# 52 "data/maps/PellucaCity/scripts.pory"
	lockall
# 55 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 56 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCity_MayorFight_Trigger_Movement_0
# 57 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 58 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 61 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_1
# 62 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 63 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 64 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 65 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_1
# 66 "data/maps/PellucaCity/scripts.pory"
	release
# 67 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 69 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_2
# 70 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 71 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 72 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 73 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_3
# 74 "data/maps/PellucaCity/scripts.pory"
	release
# 75 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 77 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_3
# 78 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 79 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 80 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 81 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_4
# 82 "data/maps/PellucaCity/scripts.pory"
	release
# 83 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 85 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_4
# 86 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 87 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 88 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 89 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_6
# 90 "data/maps/PellucaCity/scripts.pory"
	release
# 91 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 93 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_5
# 94 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 95 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 96 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 97 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_7
# 98 "data/maps/PellucaCity/scripts.pory"
	release
# 99 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 101 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_6
# 102 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_6
# 103 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 104 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 105 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_8
# 106 "data/maps/PellucaCity/scripts.pory"
	release
# 107 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 109 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_7
# 110 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 111 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 112 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 113 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_9
# 114 "data/maps/PellucaCity/scripts.pory"
	release
# 115 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 117 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_7
# 118 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 119 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 120 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_8
# 127 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 128 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 130 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 131 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_10
# 132 "data/maps/PellucaCity/scripts.pory"
	release
# 133 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 135 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_6
# 136 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_6
# 137 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 138 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 139 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_11
# 140 "data/maps/PellucaCity/scripts.pory"
	release
# 141 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 143 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_7
# 144 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 145 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 146 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 147 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_12
# 148 "data/maps/PellucaCity/scripts.pory"
	release
# 149 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 152 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_9
# 153 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 154 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_9
# 155 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_10
# 156 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 157 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_9
# 158 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_9
# 159 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_11
# 160 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 161 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S2, PellucaCity_MayorFight_Trigger_Movement_12
# 162 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S1, PellucaCity_MayorFight_Trigger_Movement_12
# 163 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S3, PellucaCity_MayorFight_Trigger_Movement_12
# 164 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 169 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_13
# 170 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 171 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 172 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 173 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_13
# 174 "data/maps/PellucaCity/scripts.pory"
	release
# 175 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 177 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_14
# 178 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 179 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 180 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 181 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_MayorFight_Trigger_Text_14
# 182 "data/maps/PellucaCity/scripts.pory"
	release
# 183 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 184 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_MAYOR, PellucaCity_MayorFight_Trigger_Movement_15
# 185 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 186 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 190 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 191 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCity_MayorFight_Trigger_Movement_16
# 192 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 193 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 195 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_MAYOR
# 196 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S1
# 197 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S2
# 198 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S3
# 199 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_MAYOR_FIGHT
# 201 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_MayorFight_Trigger_2:
	end


PellucaCity_Sailor_Entrance::
# 218 "data/maps/PellucaCity/scripts.pory"
	lockall
# 219 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 221 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 222 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_Entrance_Text_0
# 223 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 0
	goto_if_eq PellucaCity_Sailor_Entrance_2
# 224 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 1
	goto_if_eq PellucaCity_Sailor_Entrance_5
# 226 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_Multichoice
# 228 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Sailor_Entrance_2:
# 223 "data/maps/PellucaCity/scripts.pory"
	release
	end

PellucaCity_Sailor_Entrance_5:
# 224 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_Sailor_Multichoice::
# 232 "data/maps/PellucaCity/scripts.pory"
	message PellucaCity_Sailor_Multichoice_Text_0
# 233 "data/maps/PellucaCity/scripts.pory"
	waitmessage
# 234 "data/maps/PellucaCity/scripts.pory"
	dynmultichoice 0, 0, FALSE, 4, 0, DYN_MULTICHOICE_CB_NONE, PellucaCity_Sailor_Multichoice_Text_1, PellucaCity_Sailor_Multichoice_Text_2, PellucaCity_Sailor_Multichoice_Text_3
# 236 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 0
	goto_if_eq PellucaCity_Sailor_Multichoice_2
PellucaCity_Sailor_Multichoice_1:
# 237 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Sailor_Multichoice_5
PellucaCity_Sailor_Multichoice_4:
# 239 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Sailor_Multichoice_2:
# 236 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_QwilsquadExplanation
	goto PellucaCity_Sailor_Multichoice_1

PellucaCity_Sailor_Multichoice_5:
# 237 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_MemberCheck
	goto PellucaCity_Sailor_Multichoice_4


PellucaCity_Sailor_QwilsquadExplanation::
# 243 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 244 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_QwilsquadExplanation_Text_0
# 245 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_Multichoice
	return


PellucaCity_Sailor_MemberCheck::
# 248 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 249 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_0, MSGBOX_YESNO
# 251 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 0
	goto_if_eq PellucaCity_Sailor_MemberCheck_2
PellucaCity_Sailor_MemberCheck_1:
# 255 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Sailor_MemberCheck_5
PellucaCity_Sailor_MemberCheck_4:
# 277 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Sailor_MemberCheck_2:
# 252 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 253 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_1
	goto PellucaCity_Sailor_MemberCheck_1

PellucaCity_Sailor_MemberCheck_5:
# 256 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 257 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_2
# 258 "data/maps/PellucaCity/scripts.pory"
	release
# 261 "data/maps/PellucaCity/scripts.pory"
	special ChoosePartyMon
# 262 "data/maps/PellucaCity/scripts.pory"
	waitstate
# 263 "data/maps/PellucaCity/scripts.pory"
	copyvar VAR_0x800A, VAR_0x8004
# 264 "data/maps/PellucaCity/scripts.pory"
	copyvar VAR_0x8005, VAR_0x800A
# 265 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetTradeSpecies
# 267 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, SPECIES_QWILFISH_HISUI
	goto_if_eq PellucaCity_Sailor_MemberCheck_8
PellucaCity_Sailor_MemberCheck_7:
# 268 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, SPECIES_OVERQWIL
	goto_if_eq PellucaCity_Sailor_MemberCheck_11
PellucaCity_Sailor_MemberCheck_10:
# 270 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_ENTRANCE, PellucaCity_MayorFight_Trigger_Movement_7
# 271 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 272 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 273 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberCheck_Text_3
	goto PellucaCity_Sailor_MemberCheck_4

PellucaCity_Sailor_MemberCheck_8:
# 267 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_MemberAccepted
	goto PellucaCity_Sailor_MemberCheck_7

PellucaCity_Sailor_MemberCheck_11:
# 268 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Sailor_MemberAccepted
	goto PellucaCity_Sailor_MemberCheck_10


PellucaCity_Sailor_MemberAccepted::
# 281 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_ENTRANCE, PellucaCity_MayorFight_Trigger_Movement_7
# 282 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 283 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 284 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sailor_MemberAccepted_Text_0
# 285 "data/maps/PellucaCity/scripts.pory"
	release
# 287 "data/maps/PellucaCity/scripts.pory"
	opendoor 3, 42
# 288 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 289 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_ENTRANCE, PellucaCity_MayorFight_Trigger_Movement_11
# 290 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 291 "data/maps/PellucaCity/scripts.pory"
	playse SE_EXIT
# 292 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_S_ENTRANCE
# 293 "data/maps/PellucaCity/scripts.pory"
	closedoor 3, 42
# 294 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 296 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_QWILSQUAD_ENTRANCE
# 297 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Blocker::
# 312 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Blocker_Text_0
	end


PellucaCity_Blocker_Trigger::
# 316 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 10
	goto_if_eq PellucaCity_Blocker_Trigger_2
# 318 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_S_BLOCKER, PellucaCity_MayorFight_Trigger_Movement_7
# 319 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_5
# 320 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Blocker_Trigger_Text_0
# 321 "data/maps/PellucaCity/scripts.pory"
	release
# 322 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_Blocker_Trigger_Movement_0
# 323 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 324 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_Blocker_Trigger_2:
	end


PellucaCityFlooded_TriggerDown::
# 344 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerDown_1
	end

PellucaCityFlooded_TriggerDown_1:
# 345 "data/maps/PellucaCity/scripts.pory"
	lockall
# 346 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 347 "data/maps/PellucaCity/scripts.pory"
	release
# 348 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_10
# 349 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 350 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_TriggerUp::
# 357 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerUp_1
	end

PellucaCityFlooded_TriggerUp_1:
# 358 "data/maps/PellucaCity/scripts.pory"
	lockall
# 359 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 360 "data/maps/PellucaCity/scripts.pory"
	release
# 361 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_11
# 362 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 363 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_TriggerLeft::
# 370 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerLeft_1
	end

PellucaCityFlooded_TriggerLeft_1:
# 371 "data/maps/PellucaCity/scripts.pory"
	lockall
# 372 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 373 "data/maps/PellucaCity/scripts.pory"
	release
# 374 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_9
# 375 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 376 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_TriggerRight::
# 383 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAP_STATE, 1
	goto_if_eq PellucaCityFlooded_TriggerRight_1
	end

PellucaCityFlooded_TriggerRight_1:
# 384 "data/maps/PellucaCity/scripts.pory"
	lockall
# 385 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_TriggerText
# 386 "data/maps/PellucaCity/scripts.pory"
	release
# 387 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_Blocker_Trigger_Movement_0
# 388 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 389 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_SaveCitizen_A::
# 396 "data/maps/PellucaCity/scripts.pory"
	lockall
# 397 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 398 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_A_Text_0
# 399 "data/maps/PellucaCity/scripts.pory"
	release
# 402 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 404 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_EAST
	goto_if_eq PellucaCityFlooded_SaveCitizen_A_2
# 409 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_A_Movement_1
# 410 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 411 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_A_1:
# 415 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A_SAVED
# 416 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 418 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_A_2:
# 405 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_A_Movement_0
# 406 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 407 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_A_1


PellucaCityFlooded_SaveCitizen_B::
# 422 "data/maps/PellucaCity/scripts.pory"
	lockall
# 423 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 424 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_B_Text_0
# 425 "data/maps/PellucaCity/scripts.pory"
	release
# 427 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 429 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_SOUTH
	goto_if_eq PellucaCityFlooded_SaveCitizen_B_2
# 434 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_B_Movement_1
# 435 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 436 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_B_1:
# 439 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B_SAVED
# 440 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 442 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_B_2:
# 430 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_B_Movement_0
# 431 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 432 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_B_1


PellucaCityFlooded_SaveCitizen_C::
# 446 "data/maps/PellucaCity/scripts.pory"
	lockall
# 447 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 448 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_C_Text_0
# 449 "data/maps/PellucaCity/scripts.pory"
	release
# 452 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 454 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_NORTH
	goto_if_eq PellucaCityFlooded_SaveCitizen_C_2
# 459 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_C_Movement_1
# 460 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 461 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_C_1:
# 464 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C_SAVED
# 465 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 467 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_C_2:
# 455 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_C_Movement_0
# 456 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 457 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_C_1


PellucaCityFlooded_SaveCitizen_D::
# 471 "data/maps/PellucaCity/scripts.pory"
	lockall
# 472 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 473 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_SaveCitizen_D_Text_0
# 474 "data/maps/PellucaCity/scripts.pory"
	release
# 477 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetPlayerFacingDirection
# 479 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, DIR_WEST
	goto_if_eq PellucaCityFlooded_SaveCitizen_D_2
# 484 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_D_Movement_1
# 485 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 486 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
PellucaCityFlooded_SaveCitizen_D_1:
# 489 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D_SAVED
# 490 "data/maps/PellucaCity/scripts.pory"
	addvar VAR_PELLUCA_MAYOR_QUEST, 1
# 492 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_SaveCitizen_D_2:
# 480 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCityFlooded_SaveCitizen_D_Movement_0
# 481 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 482 "data/maps/PellucaCity/scripts.pory"
	removeobject VAR_LAST_TALKED
	goto PellucaCityFlooded_SaveCitizen_D_1


PellucaCityFlooded_MainEvent::
# 497 "data/maps/PellucaCity/scripts.pory"
	lockall
# 498 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAYOR_QUEST, 4
# 499 "data/maps/PellucaCity/scripts.pory"
	playbgm MUS_DUMMY, FALSE
# 501 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_SKIP_PELLUCA_CUTSCENE, PellucaCityFlooded_MainEvent_2
PellucaCityFlooded_MainEvent_1:
# 513 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCityFlooded_MainEvent_Cutscene
	return

PellucaCityFlooded_MainEvent_2:
# 502 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Text_0, MSGBOX_YESNO
# 503 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCityFlooded_MainEvent_4
	goto PellucaCityFlooded_MainEvent_1

PellucaCityFlooded_MainEvent_4:
# 504 "data/maps/PellucaCity/scripts.pory"
	fadescreen FADE_TO_WHITE
# 505 "data/maps/PellucaCity/scripts.pory"
	additem ITEM_HM03
# 506 "data/maps/PellucaCity/scripts.pory"
	special EnterSafariMode
# 507 "data/maps/PellucaCity/scripts.pory"
	fadescreen FADE_FROM_WHITE
# 508 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCityFlooded_MainEvent_Cutscene::
# 518 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_SKIP_PELLUCA_CUTSCENE
# 520 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 521 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_0
# 522 "data/maps/PellucaCity/scripts.pory"
	release
# 523 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 526 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 527 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_MainEvent_Cutscene_Movement_0
# 529 "data/maps/PellucaCity/scripts.pory"
	delay 60
# 532 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 533 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_2
# 534 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 535 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_3
# 536 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 537 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_4
# 538 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 539 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_5
# 540 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 541 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_6
# 544 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_6
# 545 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 546 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 547 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_7
# 548 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_3
# 549 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 550 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 551 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_8
# 554 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_CITIZEN, PellucaCityFlooded_MainEvent_Cutscene_Movement_1
# 555 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 556 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_9
# 557 "data/maps/PellucaCity/scripts.pory"
	release
# 558 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 560 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_5
# 561 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_5
# 562 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_5
# 563 "data/maps/PellucaCity/scripts.pory"
	applymovement 48, PellucaCity_MayorFight_Trigger_Movement_5
# 564 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 565 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 567 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 568 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_10
# 569 "data/maps/PellucaCity/scripts.pory"
	release
# 571 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_7
# 572 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_7
# 573 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_7
# 574 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_7
# 575 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCity_MayorFight_Trigger_Movement_7
# 576 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_7
# 577 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 578 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 580 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 581 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_11
# 582 "data/maps/PellucaCity/scripts.pory"
	release
# 584 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 587 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_12
# 588 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_13
# 589 "data/maps/PellucaCity/scripts.pory"
	release
# 590 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 592 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_5
# 593 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_5
# 594 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_5
# 595 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_5
# 596 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCityFlooded_MainEvent_Cutscene_Movement_2
# 597 "data/maps/PellucaCity/scripts.pory"
	applymovement 48, PellucaCity_MayorFight_Trigger_Movement_5
# 598 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_5
# 600 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 601 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_14
# 602 "data/maps/PellucaCity/scripts.pory"
	release
# 604 "data/maps/PellucaCity/scripts.pory"
	addobject LOCALID_FL_JANIA
# 605 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_MainEvent_Cutscene_Movement_3
# 606 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 608 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_4
# 609 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_4
# 610 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_4
# 611 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_4
# 612 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCity_MayorFight_Trigger_Movement_4
# 613 "data/maps/PellucaCity/scripts.pory"
	applymovement 48, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 614 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 615 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_4
# 617 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_7
# 618 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 619 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 620 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_15
# 621 "data/maps/PellucaCity/scripts.pory"
	release
# 622 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 624 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_7
# 625 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 626 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 627 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_16
# 628 "data/maps/PellucaCity/scripts.pory"
	release
# 629 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 631 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 632 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_18
# 633 "data/maps/PellucaCity/scripts.pory"
	release
# 634 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 636 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCityFlooded_MainEvent_Cutscene_Movement_6
# 637 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCityFlooded_MainEvent_Cutscene_Movement_6
# 638 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 639 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 641 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 642 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_19
# 643 "data/maps/PellucaCity/scripts.pory"
	release
# 644 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 645 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 646 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 647 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 648 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 649 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_20
# 650 "data/maps/PellucaCity/scripts.pory"
	release
# 651 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_SYS_SURF_ENABLED
# 653 "data/maps/PellucaCity/scripts.pory"
	checkitem ITEM_HM03
# 654 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, TRUE
	goto_if_eq PellucaCityFlooded_MainEvent_Cutscene_2
PellucaCityFlooded_MainEvent_Cutscene_1:
# 658 "data/maps/PellucaCity/scripts.pory"
	giveitem ITEM_HM03
# 659 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 660 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_MayorFight_Trigger_Movement_4
# 661 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 662 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 663 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_21
# 664 "data/maps/PellucaCity/scripts.pory"
	release
# 665 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 668 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_MainEvent_Cutscene_Movement_7
# 669 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 670 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCityFlooded_MainEvent_Cutscene_Movement_8
# 671 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 674 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 675 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 676 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 677 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 678 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_22
# 679 "data/maps/PellucaCity/scripts.pory"
	release
# 680 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 681 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 682 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_23
# 683 "data/maps/PellucaCity/scripts.pory"
	release
# 684 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 685 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 686 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_24
# 687 "data/maps/PellucaCity/scripts.pory"
	release
# 688 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 689 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 690 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_24
# 691 "data/maps/PellucaCity/scripts.pory"
	release
# 692 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 694 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_5
# 695 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_5
# 696 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 697 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_25
# 698 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 699 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_26
# 700 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 701 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_27
# 702 "data/maps/PellucaCity/scripts.pory"
	release
# 703 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 704 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_MainEvent_Cutscene_Text_28
# 705 "data/maps/PellucaCity/scripts.pory"
	release
# 707 "data/maps/PellucaCity/scripts.pory"
	completesubquest QUEST_PELLUCA_CITY, SUB_QUEST_2
# 709 "data/maps/PellucaCity/scripts.pory"
	special EnterSafariMode
# 710 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 711 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCityFlooded_MainEvent_Cutscene_2:
# 655 "data/maps/PellucaCity/scripts.pory"
	removeitem ITEM_HM03
	goto PellucaCityFlooded_MainEvent_Cutscene_1


PellucaCityFlooded_Mayor::
# 717 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 718 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Mayor_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_QwilBoss::
# 722 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 723 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_QwilBoss_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC1::
# 727 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC1_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC2::
# 731 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC2_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC3::
# 735 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC3_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPC4::
# 739 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPC4_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSailor::
# 743 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSailor_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_A::
# 748 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_A_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_B::
# 752 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_B_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_C::
# 756 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_C_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_NPCSaved_D::
# 760 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_NPCSaved_D_Text_0, MSGBOX_NPC
	end


PellucaCityFlooded_EventScript_TimesUp::
# 764 "data/maps/PellucaCity/scripts.pory"
	lockall
# 765 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_EventScript_TimesUp_Text_0
# 766 "data/maps/PellucaCity/scripts.pory"
	release
# 769 "data/maps/PellucaCity/scripts.pory"
	removeitem ITEM_HM03
# 771 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_REGULAR_CITIZENS
# 772 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZENS
# 774 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A_SAVED
# 775 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B_SAVED
# 776 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C_SAVED
# 777 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D_SAVED
# 779 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A
# 780 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B
# 781 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C
# 782 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D
# 784 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAP_STATE, 1
# 786 "data/maps/PellucaCity/scripts.pory"
	delay 2
# 788 "data/maps/PellucaCity/scripts.pory"
	special ExitSafariMode
# 789 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAYOR_QUEST, 3
# 790 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAP_STATE, 1
# 791 "data/maps/PellucaCity/scripts.pory"
	warp MAP_PELLUCA_CITY, 43, 28
# 792 "data/maps/PellucaCity/scripts.pory"
	waitstate
	end


PellucaCityFlooded_EventScript_TimesRunningOut::
# 797 "data/maps/PellucaCity/scripts.pory"
	lockall
# 798 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_EventScript_TimesRunningOut_Text_0
# 799 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCityFlooded_Complete_Trigger::
# 806 "data/maps/PellucaCity/scripts.pory"
	compare VAR_PELLUCA_MAYOR_QUEST, 8
	goto_if_eq PellucaCityFlooded_Complete_Trigger_2
	end

PellucaCityFlooded_Complete_Trigger_2:
# 808 "data/maps/PellucaCity/scripts.pory"
	special ExitSafariMode
# 810 "data/maps/PellucaCity/scripts.pory"
	lockall
# 811 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCityFlooded_MainEvent_Cutscene_Movement_8
# 812 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_Complete_Trigger_Movement_0
# 813 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 814 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 817 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 818 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_0
# 819 "data/maps/PellucaCity/scripts.pory"
	release
# 820 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 823 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 824 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_1
# 825 "data/maps/PellucaCity/scripts.pory"
	release
# 826 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 828 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 829 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_Complete_Trigger_Movement_1
# 830 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 834 "data/maps/PellucaCity/scripts.pory"
	applymovement 43, PellucaCity_MayorFight_Trigger_Movement_7
# 835 "data/maps/PellucaCity/scripts.pory"
	applymovement 44, PellucaCity_MayorFight_Trigger_Movement_7
# 836 "data/maps/PellucaCity/scripts.pory"
	applymovement 45, PellucaCity_MayorFight_Trigger_Movement_7
# 837 "data/maps/PellucaCity/scripts.pory"
	applymovement 46, PellucaCity_MayorFight_Trigger_Movement_7
# 838 "data/maps/PellucaCity/scripts.pory"
	applymovement 47, PellucaCity_MayorFight_Trigger_Movement_7
# 839 "data/maps/PellucaCity/scripts.pory"
	applymovement 51, PellucaCity_MayorFight_Trigger_Movement_7
# 840 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 841 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 843 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_1
# 844 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_2
# 845 "data/maps/PellucaCity/scripts.pory"
	release
# 846 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 848 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_Complete_Trigger_Movement_2
# 849 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 850 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 851 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 853 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_QWIL, PellucaCity_MayorFight_Trigger_Movement_6
# 854 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 855 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 856 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 857 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_3
# 858 "data/maps/PellucaCity/scripts.pory"
	release
# 859 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 862 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_MAYOR, PellucaCity_MayorFight_Trigger_Movement_3
# 863 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 864 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 865 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_0
# 866 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_4
# 867 "data/maps/PellucaCity/scripts.pory"
	release
# 868 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 870 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_MayorFight_Trigger_Text_2
# 871 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCityFlooded_Complete_Trigger_Text_5
# 872 "data/maps/PellucaCity/scripts.pory"
	release
# 873 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 877 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAYOR_QUEST, 9
# 878 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_PELLUCA_MAP_STATE, 0
# 880 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_REGULAR_CITIZENS
# 881 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZENS
# 883 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_A_SAVED
# 884 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_B_SAVED
# 885 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_C_SAVED
# 886 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_FLOODED_CITIZEN_DROWNING_D_SAVED
# 888 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_PELLUCA_PC_CHARS
# 891 "data/maps/PellucaCity/scripts.pory"
	warp MAP_PELLUCA_CITY_POKEMON_CENTER, 7, 6
# 893 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Greta_Trigger0::
# 923 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_GRETA_PELLUCACITY, PellucaCity_Greta_Trigger0_2
# 925 "data/maps/PellucaCity/scripts.pory"
	lockall
# 926 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_Trigger0_Movement_0
# 927 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 928 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 929 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 930 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_Main
	return

PellucaCity_Greta_Trigger0_2:
	end


PellucaCity_Greta_Trigger1::
# 934 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_GRETA_PELLUCACITY, PellucaCity_Greta_Trigger1_2
# 936 "data/maps/PellucaCity/scripts.pory"
	lockall
# 937 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_Trigger1_Movement_0
# 938 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 939 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 940 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 941 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_Main
	return

PellucaCity_Greta_Trigger1_2:
	end


PellucaCity_Greta_Trigger2::
# 945 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_GRETA_PELLUCACITY, PellucaCity_Greta_Trigger2_2
# 947 "data/maps/PellucaCity/scripts.pory"
	lockall
# 948 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_Trigger2_Movement_0
# 949 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 950 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 951 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 952 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_Main
	return

PellucaCity_Greta_Trigger2_2:
	end


PellucaCity_Greta_Main::
# 957 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_Greta_Main_Text_0
# 958 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Greta_Main_Text_1
# 959 "data/maps/PellucaCity/scripts.pory"
	release
# 960 "data/maps/PellucaCity/scripts.pory"
	delay 20
# 961 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_Greta_Main_Text_0
# 962 "data/maps/PellucaCity/scripts.pory"
	msgbox Common_Text_Greta_Comecome
# 963 "data/maps/PellucaCity/scripts.pory"
	release
# 964 "data/maps/PellucaCity/scripts.pory"
	delay 20
# 966 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Greta_ShowItemsForSale
	return


PellucaCity_Greta_GottaGo::
# 970 "data/maps/PellucaCity/scripts.pory"
	release
# 971 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_MayorFight_Trigger_Movement_7
# 972 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 973 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_Greta_Main_Text_0
# 974 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Greta_GottaGo_Text_0
# 975 "data/maps/PellucaCity/scripts.pory"
	release
# 976 "data/maps/PellucaCity/scripts.pory"
	applymovement 27, PellucaCity_Greta_GottaGo_Movement_0
# 977 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 978 "data/maps/PellucaCity/scripts.pory"
	removeobject 27
# 979 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_GRETA_PELLUCACITY
# 980 "data/maps/PellucaCity/scripts.pory"
	fadedefaultbgm
# 982 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_EventScripts_Gabrielle::
# 1002 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1003 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_GABRIELLE_CHOICEBAND, PellucaCity_EventScripts_Gabrielle_1
# 1009 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1010 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_2
# 1011 "data/maps/PellucaCity/scripts.pory"
	release
# 1012 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1013 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1014 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1015 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1016 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_3, MSGBOX_YESNO
# 1017 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_EventScripts_Gabrielle_5
# 1026 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1027 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1028 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_5
# 1029 "data/maps/PellucaCity/scripts.pory"
	release
PellucaCity_EventScripts_Gabrielle_4:
# 1031 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 1032 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1033 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_6
# 1034 "data/maps/PellucaCity/scripts.pory"
	release
# 1035 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1036 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1037 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1038 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1039 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_7
# 1040 "data/maps/PellucaCity/scripts.pory"
	release
# 1041 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem
	return

PellucaCity_EventScripts_Gabrielle_1:
# 1004 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1005 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_1
# 1006 "data/maps/PellucaCity/scripts.pory"
	release
	return

PellucaCity_EventScripts_Gabrielle_5:
# 1019 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1020 "data/maps/PellucaCity/scripts.pory"
	delay 24
# 1021 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1022 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScripts_Gabrielle_Text_4
# 1023 "data/maps/PellucaCity/scripts.pory"
	release
	goto PellucaCity_EventScripts_Gabrielle_4


PellucaCity_Gab_ChoiceItem::
# 1046 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1047 "data/maps/PellucaCity/scripts.pory"
	message PellucaCity_Gab_ChoiceItem_Text_0
# 1048 "data/maps/PellucaCity/scripts.pory"
	waitmessage
# 1049 "data/maps/PellucaCity/scripts.pory"
	dynmultichoice 0, 0, TRUE, 4, 0, DYN_MULTICHOICE_CB_NONE, PellucaCity_Gab_ChoiceItem_Text_1, PellucaCity_Gab_ChoiceItem_Text_2, PellucaCity_Gab_ChoiceItem_Text_3
# 1050 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 0
	goto_if_eq PellucaCity_Gab_ChoiceItem_2
PellucaCity_Gab_ChoiceItem_1:
# 1051 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Gab_ChoiceItem_5
PellucaCity_Gab_ChoiceItem_4:
# 1052 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 2
	goto_if_eq PellucaCity_Gab_ChoiceItem_8
PellucaCity_Gab_ChoiceItem_7:
# 1053 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem_Give
	return

PellucaCity_Gab_ChoiceItem_2:
# 1050 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_0x8006, ITEM_CHOICE_SPECS
	goto PellucaCity_Gab_ChoiceItem_1

PellucaCity_Gab_ChoiceItem_5:
# 1051 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_0x8006, ITEM_CHOICE_BAND
	goto PellucaCity_Gab_ChoiceItem_4

PellucaCity_Gab_ChoiceItem_8:
# 1052 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_0x8006, ITEM_CHOICE_SCARF
	goto PellucaCity_Gab_ChoiceItem_7


PellucaCity_Gab_ChoiceItem_Give::
# 1057 "data/maps/PellucaCity/scripts.pory"
	showitemdescription
# 1058 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Gab_ChoiceItem_Give_Text_0, MSGBOX_YESNO
# 1059 "data/maps/PellucaCity/scripts.pory"
	hideitemdescription
# 1060 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_Gab_ChoiceItem_Give_1
# 1061 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem
	return

PellucaCity_Gab_ChoiceItem_Give_1:
# 1060 "data/maps/PellucaCity/scripts.pory"
	giveitem VAR_0x8006
# 1060 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_Gab_ChoiceItem_End
	return


PellucaCity_Gab_ChoiceItem_End::
# 1065 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1066 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Gab_ChoiceItem_End_Text_0
# 1067 "data/maps/PellucaCity/scripts.pory"
	release
# 1068 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_GABRIELLE_CHOICEBAND
# 1069 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1070 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1071 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Zorua::
# 1083 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1084 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1085 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_ZOROARK, CRY_MODE_NORMAL
# 1086 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Zorua_Text_0
# 1087 "data/maps/PellucaCity/scripts.pory"
	release
# 1088 "data/maps/PellucaCity/scripts.pory"
	applymovement 25, PellucaCityFlooded_MainEvent_Cutscene_Movement_5
# 1089 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1090 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_Lycanroc::
# 1106 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_LYCANROC, CRY_MODE_NORMAL
# 1107 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Lycanroc_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC1::
# 1120 "data/maps/PellucaCity/scripts.pory"
	lock
# 1121 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1122 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC1_Text_0
# 1123 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1124 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_NPC2::
# 1129 "data/maps/PellucaCity/scripts.pory"
	lock
# 1130 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1131 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC2_Text_0
# 1132 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1133 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_NPC3::
# 1138 "data/maps/PellucaCity/scripts.pory"
	lock
# 1139 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1140 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC3_Text_0
# 1141 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1142 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_NPC4::
# 1147 "data/maps/PellucaCity/scripts.pory"
	lock
# 1148 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1149 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC4_Text_0
# 1150 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1151 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_NPC5::
# 1156 "data/maps/PellucaCity/scripts.pory"
	lock
# 1157 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1158 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC5_Text_0
# 1159 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1160 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_NPC6::
# 1165 "data/maps/PellucaCity/scripts.pory"
	lock
# 1166 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1167 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC6_Text_0
# 1168 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1169 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_NPC7::
# 1174 "data/maps/PellucaCity/scripts.pory"
	lock
# 1175 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1176 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC7_Text_0
# 1177 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1178 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_NPC8::
# 1183 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC8_Text_0, MSGBOX_NPC
	end


PellucaCity_Sealeo::
# 1188 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1189 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1190 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_SEALEO, CRY_MODE_NORMAL
# 1191 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Sealeo_Text_0, MSGBOX_NPC
# 1192 "data/maps/PellucaCity/scripts.pory"
	release
# 1193 "data/maps/PellucaCity/scripts.pory"
	applymovement VAR_LAST_TALKED, PellucaCity_MayorFight_Trigger_Movement_4
# 1194 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1195 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end


PellucaCity_NPC9::
# 1203 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC9_Text_0, MSGBOX_NPC
	end


PellucaCity_WingullGirl::
# 1212 "data/maps/PellucaCity/scripts.pory"
	lock
# 1213 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1214 "data/maps/PellucaCity/scripts.pory"
	message PellucaCity_WingullGirl_Text_0
# 1215 "data/maps/PellucaCity/scripts.pory"
	waitmessage
# 1216 "data/maps/PellucaCity/scripts.pory"
	dynmultichoice 16, 8, TRUE, 4, 0, DYN_MULTICHOICE_CB_NONE, PellucaCity_WingullGirl_Text_1, PellucaCity_WingullGirl_Text_2
# 1218 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, 1
	goto_if_eq PellucaCity_WingullGirl_2
# 1232 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullGirl_Text_5, MSGBOX_NPC
PellucaCity_WingullGirl_1:
# 1235 "data/maps/PellucaCity/scripts.pory"
	releaseall
	end

PellucaCity_WingullGirl_2:
# 1220 "data/maps/PellucaCity/scripts.pory"
	applymovement 15, PellucaCity_MayorFight_Trigger_Movement_5
# 1221 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_5
# 1222 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullGirl_Text_3
# 1223 "data/maps/PellucaCity/scripts.pory"
	release
# 1224 "data/maps/PellucaCity/scripts.pory"
	applymovement 16, PellucaCity_MayorFight_Trigger_Movement_7
# 1225 "data/maps/PellucaCity/scripts.pory"
	applymovement 17, PellucaCity_MayorFight_Trigger_Movement_7
# 1226 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1227 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1228 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullGirl_Text_4
# 1229 "data/maps/PellucaCity/scripts.pory"
	setwildbattle SPECIES_WINGULL, 25
# 1230 "data/maps/PellucaCity/scripts.pory"
	dowildbattle
	goto PellucaCity_WingullGirl_1


PellucaCity_WingullMother::
# 1240 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullMother_Text_0, MSGBOX_NPC
	end


PellucaCity_WingullCritique::
# 1245 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_WingullCritique_Text_0, MSGBOX_NPC
	end


PellucaCity_NPC10::
# 1258 "data/maps/PellucaCity/scripts.pory"
	lock
# 1259 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1260 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC10_Text_0
# 1261 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1262 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_NPC11::
# 1268 "data/maps/PellucaCity/scripts.pory"
	lock
# 1269 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1270 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC11_Text_0
# 1271 "data/maps/PellucaCity/scripts.pory"
	goto_if_unset FLAG_PELLUCA_CITY_TM_GIVER, PellucaCity_NPC11_2
PellucaCity_NPC11_1:
# 1276 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1277 "data/maps/PellucaCity/scripts.pory"
	release
	end

PellucaCity_NPC11_2:
# 1272 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC11_Text_1
# 1273 "data/maps/PellucaCity/scripts.pory"
	giveitem ITEM_TM31
# 1274 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_CITY_TM_GIVER
	goto PellucaCity_NPC11_1


PellucaCity_NPC12::
# 1283 "data/maps/PellucaCity/scripts.pory"
	lock
# 1284 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1285 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_NPC12_Text_0
# 1286 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1287 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_Stantler::
# 1292 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_STANTLER, CRY_MODE_NORMAL
# 1293 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Stantler_Text_0, MSGBOX_NPC
	end


PellucaCity_PostGymEvent_Trigger::
# 1320 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_PELLUCA_POSTGYM, PellucaCity_PostGymEvent_Trigger_2
# 1322 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_BADGE07_GET, PellucaCity_PostGymEvent_Trigger_5
	end

PellucaCity_PostGymEvent_Trigger_2:
	end

PellucaCity_PostGymEvent_Trigger_5:
# 1323 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1326 "data/maps/PellucaCity/scripts.pory"
	opendoor 37, 8
# 1327 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 1330 "data/maps/PellucaCity/scripts.pory"
	addobject LOCALID_FL_JANIA
# 1331 "data/maps/PellucaCity/scripts.pory"
	setobjectxy LOCALID_FL_JANIA, 37, 8
# 1333 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_MayorFight_Trigger_Movement_10
# 1334 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1337 "data/maps/PellucaCity/scripts.pory"
	closedoor 37, 8
# 1339 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_Complete_Trigger_Movement_2
# 1340 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1342 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 1343 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_0
# 1344 "data/maps/PellucaCity/scripts.pory"
	release
# 1345 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_PostGymEvent_Trigger_Movement_0
# 1346 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCityFlooded_Complete_Trigger_Movement_2
# 1347 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1348 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1349 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_MayorFight_Trigger_Movement_5
# 1350 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1351 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1352 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCityFlooded_MainEvent_Cutscene_Text_17
# 1353 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_1
# 1354 "data/maps/PellucaCity/scripts.pory"
	release
# 1356 "data/maps/PellucaCity/scripts.pory"
	special SpawnCameraObject
# 1357 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_FL_JANIA, PellucaCity_PostGymEvent_Trigger_Movement_1
# 1358 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_CAMERA, PellucaCityFlooded_Complete_Trigger_Movement_0
# 1359 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1361 "data/maps/PellucaCity/scripts.pory"
	opendoor 37, 8
# 1362 "data/maps/PellucaCity/scripts.pory"
	waitdooranim
# 1365 "data/maps/PellucaCity/scripts.pory"
	addobject LOCALID_GAB
# 1366 "data/maps/PellucaCity/scripts.pory"
	setobjectxy LOCALID_GAB, 37, 8
# 1367 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_PostGymEvent_Trigger_Movement_2
# 1368 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1369 "data/maps/PellucaCity/scripts.pory"
	closedoor 37, 8
# 1370 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1371 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1372 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_2
# 1373 "data/maps/PellucaCity/scripts.pory"
	release
# 1375 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_PostGymEvent_Trigger_Movement_3
# 1376 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1377 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCityFlooded_MainEvent_Cutscene_Movement_4
# 1378 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1379 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1381 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1382 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_3
# 1383 "data/maps/PellucaCity/scripts.pory"
	release
# 1384 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_MayorFight_Trigger_Movement_7
# 1385 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1386 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1387 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1388 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_4
# 1389 "data/maps/PellucaCity/scripts.pory"
	release
# 1390 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1391 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_4
# 1392 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_PostGymEvent_Trigger_Movement_4
# 1393 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1394 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1395 "data/maps/PellucaCity/scripts.pory"
	speakername PellucaCity_EventScripts_Gabrielle_Text_0
# 1396 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_PostGymEvent_Trigger_Text_5
# 1397 "data/maps/PellucaCity/scripts.pory"
	release
# 1398 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_GAB, PellucaCity_PostGymEvent_Trigger_Movement_5
# 1399 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1400 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1402 "data/maps/PellucaCity/scripts.pory"
	special RemoveCameraObject
# 1405 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_FL_JANIA
# 1406 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_GAB
# 1409 "data/maps/PellucaCity/scripts.pory"
	startquest QUEST_STOP_TEAM_SOMBER
# 1410 "data/maps/PellucaCity/scripts.pory"
	subquestmenu QUEST_MENU_COMPLETE_QUEST, QUEST_STOP_TEAM_SOMBER, SUB_QUEST_1
# 1411 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_PELLUCA_POSTGYM
	end


PellucaCity_Red_GymBlock::
# 1428 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_Red_GymBlock_Text_0, MSGBOX_NPC
	end


DR_PellucaCity_Arrival::
# 1436 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1437 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_UNUSED_0x404E, 2
# 1438 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_5
# 1439 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1440 "data/maps/PellucaCity/scripts.pory"
	delay 20
# 1444 "data/maps/PellucaCity/scripts.pory"
	speakername DR_PellucaCity_Arrival_Text_0
# 1445 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_1
# 1446 "data/maps/PellucaCity/scripts.pory"
	speakername DR_PellucaCity_Arrival_Text_2
# 1447 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_3
# 1448 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1449 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 1450 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_DR_CADMUS, DR_PellucaCity_Arrival_Movement_0
# 1451 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1452 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1453 "data/maps/PellucaCity/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_SMILE
# 1454 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_4
# 1455 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1456 "data/maps/PellucaCity/scripts.pory"
	delay 40
# 1457 "data/maps/PellucaCity/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 1458 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_5
# 1459 "data/maps/PellucaCity/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 1460 "data/maps/PellucaCity/scripts.pory"
	speakername DR_PellucaCity_Arrival_Text_6
# 1461 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_7
# 1462 "data/maps/PellucaCity/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 1463 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_8
# 1464 "data/maps/PellucaCity/scripts.pory"
	hideportrait
# 1465 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1466 "data/maps/PellucaCity/scripts.pory"
	release
# 1467 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1470 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_DR_CADMUS, DR_PellucaCity_Arrival_Movement_1
# 1471 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_PellucaCity_Arrival_Movement_2
# 1472 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1473 "data/maps/PellucaCity/scripts.pory"
	waitmovement LOCALID_DR_CADMUS
# 1474 "data/maps/PellucaCity/scripts.pory"
	delay 30
# 1475 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_9, MSGBOX_SIGN
# 1476 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1477 "data/maps/PellucaCity/scripts.pory"
	delay 40
# 1478 "data/maps/PellucaCity/scripts.pory"
	showportrait PORTRAIT_CADMUS, PORTRAIT_EXPR_NEUTRAL
# 1479 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_10
# 1480 "data/maps/PellucaCity/scripts.pory"
	hideportrait
# 1481 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1482 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_DR_CADMUS, PellucaCity_MayorFight_Trigger_Movement_5
# 1483 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1484 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1485 "data/maps/PellucaCity/scripts.pory"
	playse SE_EXIT
# 1486 "data/maps/PellucaCity/scripts.pory"
	removeobject LOCALID_DR_CADMUS
# 1487 "data/maps/PellucaCity/scripts.pory"
	delay 16
# 1488 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, DR_PellucaCity_Arrival_Movement_3
# 1489 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1490 "data/maps/PellucaCity/scripts.pory"
	delay 12
# 1491 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_UNUSED_0x884
# 1492 "data/maps/PellucaCity/scripts.pory"
	warp MAP_PELLUCA_UMBRA_LAB, 0
# 1493 "data/maps/PellucaCity/scripts.pory"
	waitstate
	end


DR_PellucaCity_Shrine::
# 1500 "data/maps/PellucaCity/scripts.pory"
	lock
# 1501 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_Arrival_Text_9, MSGBOX_SIGN
# 1502 "data/maps/PellucaCity/scripts.pory"
	release
	end


DR_PellucaCity_ShrineKeeper::
# 1507 "data/maps/PellucaCity/scripts.pory"
	lock
# 1508 "data/maps/PellucaCity/scripts.pory"
	faceplayer
# 1509 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_ShrineKeeper_Text_0
# 1510 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_ShrineKeeper_Text_1
# 1511 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_ShrineKeeper_Text_2
# 1512 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1513 "data/maps/PellucaCity/scripts.pory"
	applymovement LOCALID_DR_SHRINE_KEEPER, PellucaCity_MayorFight_Trigger_Movement_5
# 1514 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1515 "data/maps/PellucaCity/scripts.pory"
	release
	end


DR_PellucaCity_SignWest::
# 1520 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_SignWest_Text_0, MSGBOX_SIGN
	end


DR_PellucaCity_SignEast::
# 1525 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_SignEast_Text_0, MSGBOX_SIGN
	end


DR_PellucaCity_SignNorth::
# 1530 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_SignNorth_Text_0, MSGBOX_SIGN
	end


DR_PellucaCity_SignInn::
# 1535 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_SignInn_Text_0, MSGBOX_SIGN
	end


DR_PellucaCity_DoorCadmus::
# 1540 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_DoorCadmus_Text_0, MSGBOX_SIGN
	end


DR_PellucaCity_DoorLocked::
# 1545 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_DoorLocked_Text_0, MSGBOX_SIGN
	end


DR_PellucaCity_CaveSealed::
# 1550 "data/maps/PellucaCity/scripts.pory"
	msgbox DR_PellucaCity_CaveSealed_Text_0, MSGBOX_SIGN
	end


PellucaCity_EventScript_DrWestGate::
# 1560 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_DR_STATUE_AWAKENED, PellucaCity_EventScript_DrWestGate_2
# 1564 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1565 "data/maps/PellucaCity/scripts.pory"
	showportrait PORTRAIT_OSRID, PORTRAIT_EXPR_NEUTRAL
# 1566 "data/maps/PellucaCity/scripts.pory"
	special DrSetPrinceNameplate
# 1567 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_DR_CHURCH_BLASTED, PellucaCity_EventScript_DrWestGate_5
# 1570 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScript_DrWestGate_Text_1
PellucaCity_EventScript_DrWestGate_4:
# 1572 "data/maps/PellucaCity/scripts.pory"
	hideportrait
# 1573 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1574 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_Movement_DrWestGateBack
# 1575 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1576 "data/maps/PellucaCity/scripts.pory"
	releaseall
	return

PellucaCity_EventScript_DrWestGate_2:
# 1561 "data/maps/PellucaCity/scripts.pory"
	setvar VAR_TEMP_1, 1
	end

PellucaCity_EventScript_DrWestGate_5:
# 1568 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScript_DrWestGate_Text_0
	goto PellucaCity_EventScript_DrWestGate_4


# 1579 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Movement_DrWestGateBack:
# 1580 "data/maps/PellucaCity/scripts.pory"
	walk_right
	step_end

PellucaCity_EventScript_RoadGuardNorth::
# 1590 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScript_RoadGuardNorth_Text_0, MSGBOX_NPC
	end


PellucaCity_EventScript_RoadClosedNorth::
# 1595 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1596 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScript_RoadClosedNorth_Text_0
# 1597 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1598 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_10
# 1599 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1600 "data/maps/PellucaCity/scripts.pory"
	releaseall
	return


PellucaCity_EventScript_RoadGuardEast::
# 1604 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScript_RoadGuardEast_Text_0, MSGBOX_NPC
	end


PellucaCity_EventScript_RoadClosedEast::
# 1609 "data/maps/PellucaCity/scripts.pory"
	lockall
# 1610 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScript_RoadClosedEast_Text_0
# 1611 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1612 "data/maps/PellucaCity/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, PellucaCity_MayorFight_Trigger_Movement_9
# 1613 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1614 "data/maps/PellucaCity/scripts.pory"
	releaseall
	return


PellucaCity_EventScript_WimpodFlags::
# 1629 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_DR_HIDE_WIMPOD_FOUNTAIN
# 1630 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_DR_HIDE_WIMPOD_WELL
# 1631 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_DR_HIDE_WIMPOD_POND
# 1632 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_DR_WIMPOD_DONE, PellucaCity_EventScript_WimpodFlags_2
# 1632 "data/maps/PellucaCity/scripts.pory"
	goto_if_unset FLAG_DR_WIMPOD_QUEST_STARTED, PellucaCity_EventScript_WimpodFlags_2
# 1635 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_DR_WIMPOD_LEFT_WELL, PellucaCity_EventScript_WimpodFlags_7
# 1637 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_DR_WIMPOD_LEFT_FOUNTAIN, PellucaCity_EventScript_WimpodFlags_8
# 1640 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_DR_HIDE_WIMPOD_FOUNTAIN
PellucaCity_EventScript_WimpodFlags_6:
	return

PellucaCity_EventScript_WimpodFlags_2:
	return

PellucaCity_EventScript_WimpodFlags_7:
# 1636 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_DR_HIDE_WIMPOD_POND
	goto PellucaCity_EventScript_WimpodFlags_6

PellucaCity_EventScript_WimpodFlags_8:
# 1638 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_DR_HIDE_WIMPOD_WELL
	goto PellucaCity_EventScript_WimpodFlags_6


PellucaCity_EventScript_WimpodFountainRim::
# 1647 "data/maps/PellucaCity/scripts.pory"
	goto_if_set FLAG_DR_HIDE_WIMPOD_FOUNTAIN, PellucaCity_EventScript_WimpodFountainRim_2
# 1650 "data/maps/PellucaCity/scripts.pory"
	goto PellucaCity_EventScript_WimpodFountain
	return

PellucaCity_EventScript_WimpodFountainRim_2:
	end


PellucaCity_EventScript_WimpodFountain::
# 1654 "data/maps/PellucaCity/scripts.pory"
	lock
# 1655 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_WIMPOD, CRY_MODE_NORMAL
# 1656 "data/maps/PellucaCity/scripts.pory"
	applymovement 14, PellucaCity_MayorFight_Trigger_Movement_7
# 1657 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1658 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScript_WimpodFountain_Text_0
# 1659 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1660 "data/maps/PellucaCity/scripts.pory"
	applymovement 14, PellucaCity_EventScript_WimpodFountain_Movement_0
# 1661 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1662 "data/maps/PellucaCity/scripts.pory"
	removeobject 14
# 1663 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_DR_HIDE_WIMPOD_FOUNTAIN
# 1664 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_DR_WIMPOD_LEFT_FOUNTAIN
# 1665 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_DR_HIDE_WIMPOD_WELL
# 1666 "data/maps/PellucaCity/scripts.pory"
	addobject 15
# 1667 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_EventScript_WimpodWell::
# 1672 "data/maps/PellucaCity/scripts.pory"
	lock
# 1673 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_WIMPOD, CRY_MODE_NORMAL
# 1674 "data/maps/PellucaCity/scripts.pory"
	applymovement 15, PellucaCity_MayorFight_Trigger_Movement_7
# 1675 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1676 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScript_WimpodWell_Text_0
# 1677 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1678 "data/maps/PellucaCity/scripts.pory"
	applymovement 15, PellucaCity_EventScript_WimpodWell_Movement_0
# 1679 "data/maps/PellucaCity/scripts.pory"
	waitmovement 0
# 1680 "data/maps/PellucaCity/scripts.pory"
	removeobject 15
# 1681 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_DR_HIDE_WIMPOD_WELL
# 1682 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_DR_WIMPOD_LEFT_WELL
# 1683 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_DR_HIDE_WIMPOD_POND
# 1684 "data/maps/PellucaCity/scripts.pory"
	addobject 16
# 1685 "data/maps/PellucaCity/scripts.pory"
	release
	end


PellucaCity_EventScript_WimpodPond::
# 1690 "data/maps/PellucaCity/scripts.pory"
	lock
# 1691 "data/maps/PellucaCity/scripts.pory"
	msgbox PellucaCity_EventScript_WimpodPond_Text_0
# 1692 "data/maps/PellucaCity/scripts.pory"
	closemessage
# 1693 "data/maps/PellucaCity/scripts.pory"
	playmoncry SPECIES_WIMPOD, CRY_MODE_ENCOUNTER
# 1694 "data/maps/PellucaCity/scripts.pory"
	waitmoncry
# 1695 "data/maps/PellucaCity/scripts.pory"
	call DrShinyTease_Ask
# 1696 "data/maps/PellucaCity/scripts.pory"
	setwildbattle SPECIES_WIMPOD, 12
# 1697 "data/maps/PellucaCity/scripts.pory"
	createmon 1, 0, SPECIES_WIMPOD, 12, abilityNum = 2, move1 = MOVE_AQUA_JET, move2 = MOVE_BUG_BITE, move3 = MOVE_TRAILBLAZE, move4 = MOVE_NONE
# 1698 "data/maps/PellucaCity/scripts.pory"
	dowildbattle
# 1699 "data/maps/PellucaCity/scripts.pory"
	clearflag FLAG_FORCE_SHINY
# 1700 "data/maps/PellucaCity/scripts.pory"
	specialvar VAR_RESULT, GetBattleOutcome
# 1701 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, B_OUTCOME_WON
	goto_if_eq PellucaCity_EventScript_WimpodPond_2
# 1701 "data/maps/PellucaCity/scripts.pory"
	compare VAR_RESULT, B_OUTCOME_CAUGHT
	goto_if_eq PellucaCity_EventScript_WimpodPond_2
PellucaCity_EventScript_WimpodPond_1:
# 1706 "data/maps/PellucaCity/scripts.pory"
	release
	end

PellucaCity_EventScript_WimpodPond_2:
# 1702 "data/maps/PellucaCity/scripts.pory"
	removeobject 16
# 1703 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_DR_HIDE_WIMPOD_POND
# 1704 "data/maps/PellucaCity/scripts.pory"
	setflag FLAG_DR_WIMPOD_DONE
	goto PellucaCity_EventScript_WimpodPond_1


# 56 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_0:
# 56 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 56 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 56 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 56 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 61 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_1:
# 61 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 61 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_left
	step_end

# 69 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_2:
# 69 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 69 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_right
	step_end

# 77 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_3:
# 77 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_left
	step_end

# 85 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_4:
# 85 "data/maps/PellucaCity/scripts.pory"
	face_down
	step_end

# 93 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_5:
# 93 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 101 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_6:
# 101 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_right
	step_end

# 109 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_7:
# 109 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
	step_end

# 120 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_8:
# 121 "data/maps/PellucaCity/scripts.pory"
	lock_anim
# 122 "data/maps/PellucaCity/scripts.pory"
	lock_facing_direction
# 123 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 124 "data/maps/PellucaCity/scripts.pory"
	unlock_anim
# 125 "data/maps/PellucaCity/scripts.pory"
	unlock_facing_direction
	step_end

# 152 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_9:
# 152 "data/maps/PellucaCity/scripts.pory"
	walk_left
	step_end

# 155 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_10:
# 155 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 159 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_11:
# 159 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 161 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_12:
# 161 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 161 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 161 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 161 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 161 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 161 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 161 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 161 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 161 "data/maps/PellucaCity/scripts.pory"
	walk_left
	step_end

# 169 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_13:
# 169 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 169 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 177 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_14:
# 177 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 177 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 177 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 177 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 177 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 177 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 184 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_15:
# 184 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 184 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 184 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 184 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 184 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 184 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 191 "data/maps/PellucaCity/scripts.pory"
PellucaCity_MayorFight_Trigger_Movement_16:
# 191 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 191 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 191 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 191 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 322 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Blocker_Trigger_Movement_0:
# 322 "data/maps/PellucaCity/scripts.pory"
	walk_right
	step_end

# 405 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_A_Movement_0:
# 405 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 405 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 405 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 405 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 405 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 405 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 405 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 405 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 405 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 405 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
	step_end

# 409 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_A_Movement_1:
# 409 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 409 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 409 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 409 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 409 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 409 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 409 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 409 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 409 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
	step_end

# 430 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_B_Movement_0:
# 430 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 430 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 430 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 430 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 430 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 430 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 430 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 430 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 434 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_B_Movement_1:
# 434 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 434 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 434 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 434 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 434 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 434 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 434 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 455 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_C_Movement_0:
# 455 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 455 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 455 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 455 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 455 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 455 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 455 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 455 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
	step_end

# 459 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_C_Movement_1:
# 459 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 459 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 459 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 459 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 459 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 459 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 459 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
	step_end

# 480 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_D_Movement_0:
# 480 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 480 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 480 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 480 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 480 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 480 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 480 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 480 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 480 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 480 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
	step_end

# 484 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_SaveCitizen_D_Movement_1:
# 484 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 484 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 484 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 484 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 484 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 484 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 484 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 484 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
# 484 "data/maps/PellucaCity/scripts.pory"
	walk_fast_right
	step_end

# 527 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_0:
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_down
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 527 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

# 554 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_1:
# 554 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 554 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_down
	step_end

# 596 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_2:
# 596 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 596 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 605 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_3:
# 605 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 605 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 605 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 605 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 605 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 605 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 605 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 605 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 605 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 605 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 613 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_4:
# 613 "data/maps/PellucaCity/scripts.pory"
	face_right
	step_end

# 614 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_5:
# 614 "data/maps/PellucaCity/scripts.pory"
	face_left
	step_end

# 636 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_6:
# 636 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
# 636 "data/maps/PellucaCity/scripts.pory"
	jump_in_place_up
	step_end

# 668 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_7:
# 668 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 668 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 668 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 668 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 668 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 668 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 668 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 668 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 668 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 668 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 670 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_MainEvent_Cutscene_Movement_8:
# 670 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 670 "data/maps/PellucaCity/scripts.pory"
	face_down
	step_end

# 812 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_Complete_Trigger_Movement_0:
# 812 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 812 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 812 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 829 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_Complete_Trigger_Movement_1:
# 829 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 829 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 848 "data/maps/PellucaCity/scripts.pory"
PellucaCityFlooded_Complete_Trigger_Movement_2:
# 848 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 848 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 926 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_Trigger0_Movement_0:
# 926 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 926 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 926 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 926 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 926 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 926 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 926 "data/maps/PellucaCity/scripts.pory"
	face_left
	step_end

# 937 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_Trigger1_Movement_0:
# 937 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 937 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 937 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 937 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 937 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 937 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 937 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 937 "data/maps/PellucaCity/scripts.pory"
	face_right
	step_end

# 948 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_Trigger2_Movement_0:
# 948 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 948 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 948 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 948 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 948 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 948 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 948 "data/maps/PellucaCity/scripts.pory"
	face_right
	step_end

# 976 "data/maps/PellucaCity/scripts.pory"
PellucaCity_Greta_GottaGo_Movement_0:
# 976 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 976 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 976 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 976 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 976 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 976 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 976 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 976 "data/maps/PellucaCity/scripts.pory"
	walk_up
	step_end

# 1345 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_0:
# 1345 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1345 "data/maps/PellucaCity/scripts.pory"
	face_down
	step_end

# 1357 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_1:
# 1357 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1357 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1357 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 1357 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 1357 "data/maps/PellucaCity/scripts.pory"
	walk_left
	step_end

# 1367 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_2:
# 1367 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1367 "data/maps/PellucaCity/scripts.pory"
	emote_exclamation_mark
	step_end

# 1375 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_3:
# 1375 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1375 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1375 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1375 "data/maps/PellucaCity/scripts.pory"
	face_left
	step_end

# 1392 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_4:
# 1392 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1392 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1392 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1392 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 1398 "data/maps/PellucaCity/scripts.pory"
PellucaCity_PostGymEvent_Trigger_Movement_5:
# 1398 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1398 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1398 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 1450 "data/maps/PellucaCity/scripts.pory"
DR_PellucaCity_Arrival_Movement_0:
# 1450 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1450 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1450 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1450 "data/maps/PellucaCity/scripts.pory"
	walk_down
# 1450 "data/maps/PellucaCity/scripts.pory"
	walk_down
	step_end

# 1470 "data/maps/PellucaCity/scripts.pory"
DR_PellucaCity_Arrival_Movement_1:
# 1470 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1470 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1470 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1470 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1470 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1470 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1470 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1470 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1470 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1470 "data/maps/PellucaCity/scripts.pory"
	face_left
	step_end

# 1471 "data/maps/PellucaCity/scripts.pory"
DR_PellucaCity_Arrival_Movement_2:
# 1471 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1471 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1471 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1471 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1471 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1471 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1471 "data/maps/PellucaCity/scripts.pory"
	walk_left
# 1471 "data/maps/PellucaCity/scripts.pory"
	walk_up
# 1471 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 1488 "data/maps/PellucaCity/scripts.pory"
DR_PellucaCity_Arrival_Movement_3:
# 1488 "data/maps/PellucaCity/scripts.pory"
	face_right
# 1488 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1488 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1488 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1488 "data/maps/PellucaCity/scripts.pory"
	walk_right
# 1488 "data/maps/PellucaCity/scripts.pory"
	face_up
	step_end

# 1660 "data/maps/PellucaCity/scripts.pory"
PellucaCity_EventScript_WimpodFountain_Movement_0:
# 1660 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 1660 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 1660 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
# 1660 "data/maps/PellucaCity/scripts.pory"
	walk_fast_left
	step_end

# 1678 "data/maps/PellucaCity/scripts.pory"
PellucaCity_EventScript_WimpodWell_Movement_0:
# 1678 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1678 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
# 1678 "data/maps/PellucaCity/scripts.pory"
	walk_fast_up
	step_end

PellucaCity_MayorFight_Trigger_Text_0:
# 64 "data/maps/PellucaCity/scripts.pory"
	.string "Mayor$"

PellucaCity_MayorFight_Trigger_Text_1:
# 65 "data/maps/PellucaCity/scripts.pory"
	.string "But you can't be doing this to our\n"
	.string "citizens! This is our city!$"

PellucaCity_MayorFight_Trigger_Text_2:
# 72 "data/maps/PellucaCity/scripts.pory"
	.string "Q-squad Boss$"

PellucaCity_MayorFight_Trigger_Text_3:
# 73 "data/maps/PellucaCity/scripts.pory"
	.string "I've told you a hundred times, you\n"
	.string "paper-pushing wimp! You ain't doing a\l"
	.string "single thing right for our city, so don't\l"
	.string "you dare mess with the Qwilsquad!\p"
	.string "This is our turf - we don't give a hoot\n"
	.string "about you and your title!$"

PellucaCity_MayorFight_Trigger_Text_4:
# 81 "data/maps/PellucaCity/scripts.pory"
	.string "No! Enough is enough! I'm putting my\n"
	.string "foot down.\p"
	.string "You and your lot aren't allowed in\n"
	.string "Pelluca City any more!$"

PellucaCity_MayorFight_Trigger_Text_5:
# 88 "data/maps/PellucaCity/scripts.pory"
	.string "Q-squad Grunt$"

PellucaCity_MayorFight_Trigger_Text_6:
# 89 "data/maps/PellucaCity/scripts.pory"
	.string "Hahaha! What a lame mayor!$"

PellucaCity_MayorFight_Trigger_Text_7:
# 97 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah! He really thinks he can tell us\n"
	.string "what to do!$"

PellucaCity_MayorFight_Trigger_Text_8:
# 105 "data/maps/PellucaCity/scripts.pory"
	.string "Go on boss - teach him a lesson!$"

PellucaCity_MayorFight_Trigger_Text_9:
# 113 "data/maps/PellucaCity/scripts.pory"
	.string "You heard 'em Mayor. Looks like my boys\n"
	.string "want me to prove that we own this city!\p"
	.string "Wanna try me? Right here?$"

PellucaCity_MayorFight_Trigger_Text_10:
# 131 "data/maps/PellucaCity/scripts.pory"
	.string "Nono - see, I'm not - look, I'm just\n"
	.string "asking for a little cooperation and -$"

PellucaCity_MayorFight_Trigger_Text_11:
# 139 "data/maps/PellucaCity/scripts.pory"
	.string "Hahaha! Look at the wimp! Poor guy.$"

PellucaCity_MayorFight_Trigger_Text_12:
# 147 "data/maps/PellucaCity/scripts.pory"
	.string "Got it, mayor? You're not in charge here.\p"
	.string "I am!\p"
	.string "And from now on, this city belongs\n"
	.string "to us - the Qwilsquad!$"

PellucaCity_MayorFight_Trigger_Text_13:
# 173 "data/maps/PellucaCity/scripts.pory"
	.string "Oh - a tourist! Were you standing there\n"
	.string "the whole time?\p"
	.string "...\p"
	.string "I'm sorry you had to witness that.\p"
	.string "Y-you know, we have a wonderful\n"
	.string "Game Corner! And the Apple Pie at the\l"
	.string "Pelluca Restaurant is to die for.$"

PellucaCity_MayorFight_Trigger_Text_14:
# 181 "data/maps/PellucaCity/scripts.pory"
	.string "Sigh...what will I do?$"

PellucaCity_Sailor_Entrance_Text_0:
# 222 "data/maps/PellucaCity/scripts.pory"
	.string "Beat it, kid! This is private property\n"
	.string "belonging to the Qwilsquad.$"

PellucaCity_Sailor_Multichoice_Text_0:
# 232 "data/maps/PellucaCity/scripts.pory"
	.string "Only Qwilsquad members can enter!$"

PellucaCity_Sailor_Multichoice_Text_1:
# 234 "data/maps/PellucaCity/scripts.pory"
	.string "What's a Qwilsquad?$"

PellucaCity_Sailor_Multichoice_Text_2:
# 234 "data/maps/PellucaCity/scripts.pory"
	.string "I'm a member!$"

PellucaCity_Sailor_Multichoice_Text_3:
# 234 "data/maps/PellucaCity/scripts.pory"
	.string "Okay...$"

PellucaCity_Sailor_QwilsquadExplanation_Text_0:
# 244 "data/maps/PellucaCity/scripts.pory"
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
# 249 "data/maps/PellucaCity/scripts.pory"
	.string "A pipsqueak like you is in the squad?\n"
	.string "You a new member? Got any proof?$"

PellucaCity_Sailor_MemberCheck_Text_1:
# 253 "data/maps/PellucaCity/scripts.pory"
	.string "Then beat it, kid!$"

PellucaCity_Sailor_MemberCheck_Text_2:
# 257 "data/maps/PellucaCity/scripts.pory"
	.string "Show me!$"

PellucaCity_Sailor_MemberCheck_Text_3:
# 273 "data/maps/PellucaCity/scripts.pory"
	.string "That don't look like no Qwilfish to me!\p"
	.string "Beat it, kid!$"

PellucaCity_Sailor_MemberAccepted_Text_0:
# 284 "data/maps/PellucaCity/scripts.pory"
	.string "Now that's what I'm talking about!\n"
	.string "You're one of us, kid.\p"
	.string "Go on, get inside!$"

PellucaCity_Blocker_Text_0:
# 312 "data/maps/PellucaCity/scripts.pory"
	.string "This is our city! Got any problems?$"

PellucaCity_Blocker_Trigger_Text_0:
# 320 "data/maps/PellucaCity/scripts.pory"
	.string "Hey kid, where d'you think yer goin?\n"
	.string "There's a toll if you wanna get out.\p"
	.string "That's right! You gotta pay ¥999999.\p"
	.string "Ain't got the money?\p"
	.string "Then get packing!$"

PellucaCityFlooded_SaveCitizen_A_Text_0:
# 398 "data/maps/PellucaCity/scripts.pory"
	.string "Help! Help! Over here!\p"
	.string "...\p"
	.string "Thank you so much - I'm saved!$"

PellucaCityFlooded_SaveCitizen_B_Text_0:
# 424 "data/maps/PellucaCity/scripts.pory"
	.string "I can't stay afloat any more!\p"
	.string "...\p"
	.string "You came just in time!$"

PellucaCityFlooded_SaveCitizen_C_Text_0:
# 448 "data/maps/PellucaCity/scripts.pory"
	.string "Ahh! It's too cold!\p"
	.string "...\p"
	.string "Waah! Wahh! It was so scary!$"

PellucaCityFlooded_SaveCitizen_D_Text_0:
# 473 "data/maps/PellucaCity/scripts.pory"
	.string "Help! Someone save me!\p"
	.string "...\p"
	.string "Yaay! You came!$"

PellucaCityFlooded_MainEvent_Text_0:
# 502 "data/maps/PellucaCity/scripts.pory"
	.string "Skip cutscene?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_0:
# 521 "data/maps/PellucaCity/scripts.pory"
	.string "What on earth is this?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_1:
# 532 "data/maps/PellucaCity/scripts.pory"
	.string "Citizen$"

PellucaCityFlooded_MainEvent_Cutscene_Text_2:
# 533 "data/maps/PellucaCity/scripts.pory"
	.string "What a disaster!\p"
	.string "How could we be so unlucky!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_3:
# 535 "data/maps/PellucaCity/scripts.pory"
	.string "What happened?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_4:
# 537 "data/maps/PellucaCity/scripts.pory"
	.string "A Mega Sharpedo came rampaging down\n"
	.string "from the Ivy River and kicked up a\l"
	.string "storm! The riverbanks have flooded.\p"
	.string "The city's underwater!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_5:
# 539 "data/maps/PellucaCity/scripts.pory"
	.string "Is everyone safe?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_6:
# 541 "data/maps/PellucaCity/scripts.pory"
	.string "No - there are still four people in the\n"
	.string "water! We have to save them fast!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_7:
# 547 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah, go on Mayor. Go save them!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_8:
# 551 "data/maps/PellucaCity/scripts.pory"
	.string "W-what do you mean? Weren't you the\n"
	.string "one in control of this city?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_9:
# 556 "data/maps/PellucaCity/scripts.pory"
	.string "ENOUGH!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_10:
# 568 "data/maps/PellucaCity/scripts.pory"
	.string "While you two bicker, it's us that pays\n"
	.string "the price every time! Both of you are\l"
	.string "strong - a tough trainer and a smart\l"
	.string "politician - and yet, neither of you\l"
	.string "bother to actually do anything for us\l"
	.string "citizens! And now people are in danger\l"
	.string "and you're still fighting! We've all had\l"
	.string "it up to here with you two!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_11:
# 581 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah!\p"
	.string "Hear hear!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_12:
# 587 "data/maps/PellucaCity/scripts.pory"
	.string "???$"

PellucaCityFlooded_MainEvent_Cutscene_Text_13:
# 588 "data/maps/PellucaCity/scripts.pory"
	.string "I agree too.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_14:
# 601 "data/maps/PellucaCity/scripts.pory"
	.string "Is that Jania?\p"
	.string "Yeah! It's the Gym Leader! In the flesh!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_15:
# 620 "data/maps/PellucaCity/scripts.pory"
	.string "Oh, Jania! It's you! Finally. Please - you\n"
	.string "have to save those still drowning!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_16:
# 627 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah, Jania! You're an even stronger\n"
	.string "trainer than I am. You can do it!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_17:
# 631 "data/maps/PellucaCity/scripts.pory"
	.string "Jania$"

PellucaCityFlooded_MainEvent_Cutscene_Text_18:
# 632 "data/maps/PellucaCity/scripts.pory"
	.string "No, I won't.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_19:
# 642 "data/maps/PellucaCity/scripts.pory"
	.string "Don't look at me like that!\p"
	.string "You two want to be responsible for this\n"
	.string "city? Start right here, right now.\p"
	.string "Your citizens are miserably tired of\n"
	.string "both of you - when will you two change?$"

PellucaCityFlooded_MainEvent_Cutscene_Text_20:
# 649 "data/maps/PellucaCity/scripts.pory"
	.string "And who might you be?\p"
	.string "...\p"
	.string "{PLAYER}?\p"
	.string "...\p"
	.string "I see - so that's how you got involved\n"
	.string "with these two.\p"
	.string "Here, take this.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_21:
# 663 "data/maps/PellucaCity/scripts.pory"
	.string "Consider this my help.\p"
	.string "Now I'm going to track the Mega\n"
	.string "Sharpedo down and make sure it doesn't\l"
	.string "harm anyone else.\p"
	.string "And the two of you - and {PLAYER} -\n"
	.string "take this chance to do the right thing!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_22:
# 678 "data/maps/PellucaCity/scripts.pory"
	.string "Hmpf.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_23:
# 682 "data/maps/PellucaCity/scripts.pory"
	.string "Tchah!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_24:
# 686 "data/maps/PellucaCity/scripts.pory"
	.string "...$"

PellucaCityFlooded_MainEvent_Cutscene_Text_25:
# 697 "data/maps/PellucaCity/scripts.pory"
	.string "All of you! We've been letting you down.\n"
	.string "But now we're gonna prove that we care\l"
	.string "about this city with our actions!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_26:
# 699 "data/maps/PellucaCity/scripts.pory"
	.string "{PLAYER} - the two of us will handle\n"
	.string "the citizens on the bridge and on land.\l"
	.string "Can you surf and rescue the four\l"
	.string "remaining citizens?\p"
	.string "Once you've picked all four of them up,\n"
	.string "come back here.$"

PellucaCityFlooded_MainEvent_Cutscene_Text_27:
# 701 "data/maps/PellucaCity/scripts.pory"
	.string "Good luck, {PLAYER}! We're on top of\n"
	.string "things here, so you go on into the river.\l"
	.string "You don't need to teach any Pokémon\l"
	.string "how to surf - just hop on the water!$"

PellucaCityFlooded_MainEvent_Cutscene_Text_28:
# 704 "data/maps/PellucaCity/scripts.pory"
	.string "But hurry! There's not much time.$"

PellucaCityFlooded_Mayor_Text_0:
# 718 "data/maps/PellucaCity/scripts.pory"
	.string "Have you saved everyone yet?\n"
	.string "Please hurry!$"

PellucaCityFlooded_QwilBoss_Text_0:
# 723 "data/maps/PellucaCity/scripts.pory"
	.string "We're keeping the citizens safe, so you\n"
	.string "go get the rest!$"

PellucaCityFlooded_NPC1_Text_0:
# 727 "data/maps/PellucaCity/scripts.pory"
	.string "The Mayor and the Qwilsquad boss\n"
	.string "working together? Hah! I'll believe it\l"
	.string "when I see it.$"

PellucaCityFlooded_NPC2_Text_0:
# 731 "data/maps/PellucaCity/scripts.pory"
	.string "If the two of them collaborate, maybe\n"
	.string "things will finally improve...$"

PellucaCityFlooded_NPC3_Text_0:
# 735 "data/maps/PellucaCity/scripts.pory"
	.string "I'm so scared - I hope you can save the\n"
	.string "others!$"

PellucaCityFlooded_NPC4_Text_0:
# 739 "data/maps/PellucaCity/scripts.pory"
	.string "I hate that Mega Sharpedo for doing\n"
	.string "this to my home!$"

PellucaCityFlooded_NPCSailor_Text_0:
# 743 "data/maps/PellucaCity/scripts.pory"
	.string "Go on, {PLAYER}! Hurry up and do what\n"
	.string "the boss says.$"

PellucaCityFlooded_NPCSaved_A_Text_0:
# 748 "data/maps/PellucaCity/scripts.pory"
	.string "You saved me! I can't thank you enough,\n"
	.string "trainer.$"

PellucaCityFlooded_NPCSaved_B_Text_0:
# 752 "data/maps/PellucaCity/scripts.pory"
	.string "I owe you, trainer. I'll never forget\n"
	.string "this!$"

PellucaCityFlooded_NPCSaved_C_Text_0:
# 756 "data/maps/PellucaCity/scripts.pory"
	.string "Brr - the water was so cold! How do\n"
	.string "Pokémon swim in it?$"

PellucaCityFlooded_NPCSaved_D_Text_0:
# 760 "data/maps/PellucaCity/scripts.pory"
	.string "When I grow up, I wanna be just like you!$"

PellucaCityFlooded_EventScript_TimesUp_Text_0:
# 765 "data/maps/PellucaCity/scripts.pory"
	.string "The tides rise higher and higher...\n"
	.string "it's too late!$"

PellucaCityFlooded_EventScript_TimesRunningOut_Text_0:
# 798 "data/maps/PellucaCity/scripts.pory"
	.string "The water level is rising...\n"
	.string "There's not much time left!$"

PellucaCityFlooded_Complete_Trigger_Text_0:
# 818 "data/maps/PellucaCity/scripts.pory"
	.string "That's one, two, three...and four!\p"
	.string "Yup, we're all accounted for.$"

PellucaCityFlooded_Complete_Trigger_Text_1:
# 824 "data/maps/PellucaCity/scripts.pory"
	.string "Finally! Thank you {PLAYER}. You did\n"
	.string "us - all of us - a great service.\p"
	.string "You're a hero!$"

PellucaCityFlooded_Complete_Trigger_Text_2:
# 844 "data/maps/PellucaCity/scripts.pory"
	.string "Thank you {PLAYER}!\p"
	.string "You're the best!$"

PellucaCityFlooded_Complete_Trigger_Text_3:
# 857 "data/maps/PellucaCity/scripts.pory"
	.string "It looks like we're all safe for now.$"

PellucaCityFlooded_Complete_Trigger_Text_4:
# 866 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah. All that remains is to wait until\n"
	.string "the water recedes, and then we can go\l"
	.string "back to normal.\p"
	.string "Come, shall we wait in the Pokémon\n"
	.string "Center until then?$"

PellucaCityFlooded_Complete_Trigger_Text_5:
# 871 "data/maps/PellucaCity/scripts.pory"
	.string "Sounds like a good idea. {PLAYER} here\n"
	.string "needs some rest after everything\l"
	.string "that's just happened!$"

PellucaCity_Greta_Main_Text_0:
# 957 "data/maps/PellucaCity/scripts.pory"
	.string "Greta$"

PellucaCity_Greta_Main_Text_1:
# 958 "data/maps/PellucaCity/scripts.pory"
	.string "Oh, it's you again, {PLAYER}!\n"
	.string "Fancy seeing you in these parts.\l"
	.string "Route 6 was a tough trek, wasn't it?$"

PellucaCity_Greta_GottaGo_Text_0:
# 974 "data/maps/PellucaCity/scripts.pory"
	.string "Would you look at the time!\n"
	.string "I've gotta run. See you around!$"

PellucaCity_EventScripts_Gabrielle_Text_0:
# 1004 "data/maps/PellucaCity/scripts.pory"
	.string "Gabrielle$"

PellucaCity_EventScripts_Gabrielle_Text_1:
# 1005 "data/maps/PellucaCity/scripts.pory"
	.string "Ahh, I love the smell of the river!$"

PellucaCity_EventScripts_Gabrielle_Text_2:
# 1010 "data/maps/PellucaCity/scripts.pory"
	.string "I grew up here on this cliff without my\n"
	.string "parents. Life was hard.\p"
	.string "I didn't want my younger siblings to go\n"
	.string "through what I did, so when Team Somber\l"
	.string "promised me money, I took it.\p"
	.string "...\p"
	.string "Those grunts were really vicious to me.\n"
	.string "I was so scared I would lose Zoroark!$"

PellucaCity_EventScripts_Gabrielle_Text_3:
# 1016 "data/maps/PellucaCity/scripts.pory"
	.string "Was I just like that when you met me\n"
	.string "with that hiker with the Clefairy?$"

PellucaCity_EventScripts_Gabrielle_Text_4:
# 1022 "data/maps/PellucaCity/scripts.pory"
	.string "Yeah...I doubt he'd ever forgive me.$"

PellucaCity_EventScripts_Gabrielle_Text_5:
# 1028 "data/maps/PellucaCity/scripts.pory"
	.string "You're just trying to make me feel\n"
	.string "better, aren't you? I don't need your\l"
	.string "pity. I know what I've done.$"

PellucaCity_EventScripts_Gabrielle_Text_6:
# 1033 "data/maps/PellucaCity/scripts.pory"
	.string "After getting kicked out of Team\n"
	.string "Somber, I feel like I've come to my\l"
	.string "senses a little. I'm going to support my\l"
	.string "family - but do it right. Be honest.\p"
	.string "Be responsible.$"

PellucaCity_EventScripts_Gabrielle_Text_7:
# 1039 "data/maps/PellucaCity/scripts.pory"
	.string "I want you to have this. As a thank you.\n"
	.string "For saving me - not just once, but so\l"
	.string "many times. You're a strong trainer, but\l"
	.string "more importantly - you're a good person.\l"
	.string "I hope to be like you.$"

PellucaCity_Gab_ChoiceItem_Text_0:
# 1047 "data/maps/PellucaCity/scripts.pory"
	.string "Choose any one you like.$"

PellucaCity_Gab_ChoiceItem_Text_1:
# 1049 "data/maps/PellucaCity/scripts.pory"
	.string "Choice Specs$"

PellucaCity_Gab_ChoiceItem_Text_2:
# 1049 "data/maps/PellucaCity/scripts.pory"
	.string "Choice Band$"

PellucaCity_Gab_ChoiceItem_Text_3:
# 1049 "data/maps/PellucaCity/scripts.pory"
	.string "Choice Scarf$"

PellucaCity_Gab_ChoiceItem_Give_Text_0:
# 1058 "data/maps/PellucaCity/scripts.pory"
	.string "Are you sure?$"

PellucaCity_Gab_ChoiceItem_End_Text_0:
# 1066 "data/maps/PellucaCity/scripts.pory"
	.string "The choices we make define who we are.\n"
	.string "Once we lock in, we can't change.\p"
	.string "I can't erase what I've done, but I'm\n"
	.string "going to make a better choice this time.\p"
	.string "I suppose you're going to head to the\n"
	.string "Mirroh Base Camp from here? Team\l"
	.string "Somber must've reached there already.\p"
	.string "Best of luck, {PLAYER}.$"

PellucaCity_Zorua_Text_0:
# 1086 "data/maps/PellucaCity/scripts.pory"
	.string "Gabrielle's Zoroark looks content.\n"
	.string "Life is more peaceful for it now!$"

PellucaCity_Lycanroc_Text_0:
# 1107 "data/maps/PellucaCity/scripts.pory"
	.string "Lycanroc growls low, its eyes on the\n"
	.string "western hills.$"

PellucaCity_NPC1_Text_0:
# 1122 "data/maps/PellucaCity/scripts.pory"
	.string "Whee! I'm the Champion and you're the\n"
	.string "wicked dragon!\p"
	.string "Rhydia's beaten everyone for five whole\n"
	.string "years. When I'm grown I'll beat her, and\l"
	.string "she'll have to give me Justice!$"

PellucaCity_NPC2_Text_0:
# 1131 "data/maps/PellucaCity/scripts.pory"
	.string "A new face! Have a care on the east\n"
	.string "road.\p"
	.string "There's a bend in the Hoya by the old\n"
	.string "altar where no boatman will tie up after\l"
	.string "dark, and none will say why.$"

PellucaCity_NPC3_Text_0:
# 1140 "data/maps/PellucaCity/scripts.pory"
	.string "I meant to cross the Hoya Delta and see\n"
	.string "the Ashland Labyrinth, but the Templars\l"
	.string "bar the east road and won't say why.\p"
	.string "Just as well, says my father. He's not\n"
	.string "trusted an Ashland since the\l"
	.string "Prince-Consort was murdered.$"

PellucaCity_NPC4_Text_0:
# 1149 "data/maps/PellucaCity/scripts.pory"
	.string "Masons out of Rivetshore raised this\n"
	.string "bridge, House Stone's men every one.\l"
	.string "Their guild has raised the toll on the\l"
	.string "coast road again, third time in two\l"
	.string "years.\p"
	.string "Where all that coin goes, none can say.$"

PellucaCity_NPC5_Text_0:
# 1158 "data/maps/PellucaCity/scripts.pory"
	.string "Templar riders, flying west for Mirroh.\n"
	.string "Third pair since morning.\p"
	.string "My cousin writes that the whole\n"
	.string "mountain groaned one night two winters\l"
	.string "past, and a strange light shone from\l"
	.string "the caves till dawn.$"

PellucaCity_NPC6_Text_0:
# 1167 "data/maps/PellucaCity/scripts.pory"
	.string "Bound for Mirroh? Don't stop in the fog\n"
	.string "at Hollow Hill for anything you hear.\p"
	.string "My Lycanroc won't pass the treeline,\n"
	.string "and there's red webbing in those trees\l"
	.string "thick as ship's rigging. Thirty years in\l"
	.string "the woods, and I've never seen the\l"
	.string "spider that could spin it.$"

PellucaCity_NPC7_Text_0:
# 1176 "data/maps/PellucaCity/scripts.pory"
	.string "My cousin has sat two winters in\n"
	.string "Gleamdusk for a brace of trout, waiting\l"
	.string "on the Concordance to judge him.\p"
	.string "Half those lords haven't sat their\n"
	.string "seats in a year, folk say. A poor man may\l"
	.string "rot while they're about their own\l"
	.string "affairs.$"

PellucaCity_NPC8_Text_0:
# 1183 "data/maps/PellucaCity/scripts.pory"
	.string "What's even the point of fishing if the\n"
	.string "Mega Sharpedo's going to scare all the\l"
	.string "fish away? I wish our mayor would do\l"
	.string "something about it.$"

PellucaCity_Sealeo_Text_0:
# 1191 "data/maps/PellucaCity/scripts.pory"
	.string "Sealeo wants to catch fish!$"

PellucaCity_NPC9_Text_0:
# 1203 "data/maps/PellucaCity/scripts.pory"
	.string "This is the Pelluca Fishery! But it's\n"
	.string "closed due to the Mega Sharpedo\l"
	.string "attacks.$"

PellucaCity_WingullGirl_Text_0:
# 1214 "data/maps/PellucaCity/scripts.pory"
	.string "Hahaha! I'm throwing stones at the\n"
	.string "Wingulls over there. Wanna throw some?$"

PellucaCity_WingullGirl_Text_1:
# 1216 "data/maps/PellucaCity/scripts.pory"
	.string "That's mean$"

PellucaCity_WingullGirl_Text_2:
# 1216 "data/maps/PellucaCity/scripts.pory"
	.string "Gimme a stone!$"

PellucaCity_WingullGirl_Text_3:
# 1222 "data/maps/PellucaCity/scripts.pory"
	.string "{PLAYER} threw a stone at a Wingull!$"

PellucaCity_WingullGirl_Text_4:
# 1228 "data/maps/PellucaCity/scripts.pory"
	.string "The Wingull gets angry!$"

PellucaCity_WingullGirl_Text_5:
# 1232 "data/maps/PellucaCity/scripts.pory"
	.string "Mean? You're mean!$"

PellucaCity_WingullMother_Text_0:
# 1240 "data/maps/PellucaCity/scripts.pory"
	.string "My daughter loves throwing stones at\n"
	.string "Wingulls. She's just so cute!$"

PellucaCity_WingullCritique_Text_0:
# 1245 "data/maps/PellucaCity/scripts.pory"
	.string "That little girl is so bad! Throwing\n"
	.string "stones at Pokémon...that's poor\l"
	.string "parenting.$"

PellucaCity_NPC10_Text_0:
# 1260 "data/maps/PellucaCity/scripts.pory"
	.string "Six apple tarts, and all of them Moray\n"
	.string "apples.\p"
	.string "They say Vizier Moray rides out to the\n"
	.string "Empress-mother's villa near every day,\l"
	.string "bearing the first of the harvest\l"
	.string "himself. Ten years of it. There's a loyal\l"
	.string "man for you.$"

PellucaCity_NPC11_Text_0:
# 1270 "data/maps/PellucaCity/scripts.pory"
	.string "Worry is for tax collectors, friend.\p"
	.string "“Three stones had Cormor, and Keerin at\n"
	.string "his side...”\p"
	.string "There's a second verse, but it fell out\n"
	.string "of the song long ago, and no one in all\l"
	.string "Cormoria can give it back to me.$"

PellucaCity_NPC11_Text_1:
# 1272 "data/maps/PellucaCity/scripts.pory"
	.string "A traveller paid me with this for a song.\n"
	.string "I've no use for it, so it's yours.$"

PellucaCity_NPC12_Text_0:
# 1285 "data/maps/PellucaCity/scripts.pory"
	.string "Easy, girl, leave the Academy's flowers\n"
	.string "be.\p"
	.string "Her dam came from the Vilethorn\n"
	.string "country, where two of the Albans' field\l"
	.string "hands walked into the woods last\l"
	.string "harvest and never walked out. The\l"
	.string "family raised no search.$"

PellucaCity_Stantler_Text_0:
# 1293 "data/maps/PellucaCity/scripts.pory"
	.string "The Stantler is calmly munching the\n"
	.string "flowers.$"

PellucaCity_PostGymEvent_Trigger_Text_0:
# 1343 "data/maps/PellucaCity/scripts.pory"
	.string "Excuse me.$"

PellucaCity_PostGymEvent_Trigger_Text_1:
# 1353 "data/maps/PellucaCity/scripts.pory"
	.string "Where am I going?\p"
	.string "I'm going to Rivetshore City.\n"
	.string "All the Gym Leaders have been called\l"
	.string "there.$"

PellucaCity_PostGymEvent_Trigger_Text_2:
# 1372 "data/maps/PellucaCity/scripts.pory"
	.string "{PLAYER}! Over here!$"

PellucaCity_PostGymEvent_Trigger_Text_3:
# 1382 "data/maps/PellucaCity/scripts.pory"
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
# 1388 "data/maps/PellucaCity/scripts.pory"
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
# 1396 "data/maps/PellucaCity/scripts.pory"
	.string "You'd better be there, {PLAYER}!$"

PellucaCity_Red_GymBlock_Text_0:
# 1428 "data/maps/PellucaCity/scripts.pory"
	.string "Jania's gone to deal with the Mega\n"
	.string "Sharpedo. You'll find her up in Ivy River\l"
	.string "somewhere.$"

DR_PellucaCity_Arrival_Text_0:
# 1444 "data/maps/PellucaCity/scripts.pory"
	.string "Dockhand$"

DR_PellucaCity_Arrival_Text_1:
# 1445 "data/maps/PellucaCity/scripts.pory"
	.string "A Rainhawk, in a mask? Like something\n"
	.string "out of the old stories.$"

DR_PellucaCity_Arrival_Text_2:
# 1446 "data/maps/PellucaCity/scripts.pory"
	.string "Sailor$"

DR_PellucaCity_Arrival_Text_3:
# 1447 "data/maps/PellucaCity/scripts.pory"
	.string "That's the one who held the beach at\n"
	.string "Sevii. Burned for it, they say.$"

DR_PellucaCity_Arrival_Text_4:
# 1454 "data/maps/PellucaCity/scripts.pory"
	.string "Rainhawk Alban. Welcome to Pelluca\n"
	.string "Valley.$"

DR_PellucaCity_Arrival_Text_5:
# 1458 "data/maps/PellucaCity/scripts.pory"
	.string "And the burns? Are they healing?$"

DR_PellucaCity_Arrival_Text_6:
# 1460 "data/maps/PellucaCity/scripts.pory"
	.string "“Nomad”$"

DR_PellucaCity_Arrival_Text_7:
# 1461 "data/maps/PellucaCity/scripts.pory"
	.string "Slowly. The mask helps.$"

DR_PellucaCity_Arrival_Text_8:
# 1463 "data/maps/PellucaCity/scripts.pory"
	.string "Good. Walk with me. We will talk\n"
	.string "somewhere quieter.$"

DR_PellucaCity_Arrival_Text_9:
# 1475 "data/maps/PellucaCity/scripts.pory"
	.string "For Prince {PLAYER}, Keerin's Chosen.\n"
	.string "Wherever you are, come home.$"

DR_PellucaCity_Arrival_Text_10:
# 1479 "data/maps/PellucaCity/scripts.pory"
	.string "Rainhawk.$"

DR_PellucaCity_ShrineKeeper_Text_0:
# 1509 "data/maps/PellucaCity/scripts.pory"
	.string "The night the twins were born, Keerin\n"
	.string "was seen over Silversun Palace. She\l"
	.string "chose the boy, they said. First time in\l"
	.string "generations.$"

DR_PellucaCity_ShrineKeeper_Text_1:
# 1510 "data/maps/PellucaCity/scripts.pory"
	.string "Ten years now, and not one word of him.\n"
	.string "Most folk have stopped coming.$"

DR_PellucaCity_ShrineKeeper_Text_2:
# 1511 "data/maps/PellucaCity/scripts.pory"
	.string "Not the Regent-Queen, though. Her\n"
	.string "candles arrive every spring, right on\l"
	.string "time.$"

DR_PellucaCity_SignWest_Text_0:
# 1520 "data/maps/PellucaCity/scripts.pory"
	.string "West: Route 11, on the road to Mirroh.$"

DR_PellucaCity_SignEast_Text_0:
# 1525 "data/maps/PellucaCity/scripts.pory"
	.string "East: Hoya Delta.$"

DR_PellucaCity_SignNorth_Text_0:
# 1530 "data/maps/PellucaCity/scripts.pory"
	.string "North: Ivy River.$"

DR_PellucaCity_SignInn_Text_0:
# 1535 "data/maps/PellucaCity/scripts.pory"
	.string "The Seaside Tavern. Hot meals, warm\n"
	.string "beds, and rest for weary Pokémon.$"

DR_PellucaCity_DoorCadmus_Text_0:
# 1540 "data/maps/PellucaCity/scripts.pory"
	.string "Vizier Umbra's residence. The door is\n"
	.string "locked.$"

DR_PellucaCity_DoorLocked_Text_0:
# 1545 "data/maps/PellucaCity/scripts.pory"
	.string "The door is locked.$"

DR_PellucaCity_CaveSealed_Text_0:
# 1550 "data/maps/PellucaCity/scripts.pory"
	.string "A heavy stone slab seals the cave\n"
	.string "mouth. It bears the crest of House\l"
	.string "Umbra.$"

PellucaCity_EventScript_DrWestGate_Text_0:
# 1568 "data/maps/PellucaCity/scripts.pory"
	.string "Cadmus told me to meet him at the\n"
	.string "church.\p"
	.string "I shouldn't leave the Valley yet.$"

PellucaCity_EventScript_DrWestGate_Text_1:
# 1570 "data/maps/PellucaCity/scripts.pory"
	.string "I still have things to take care of here\n"
	.string "in the Valley.\p"
	.string "I shouldn't leave just yet.$"

PellucaCity_EventScript_RoadGuardNorth_Text_0:
# 1590 "data/maps/PellucaCity/scripts.pory"
	.string "Halt. The road north to the Ivy River is\n"
	.string "closed by order of the Templar Order.$"

PellucaCity_EventScript_RoadClosedNorth_Text_0:
# 1596 "data/maps/PellucaCity/scripts.pory"
	.string "Halt. The road north to the Ivy River is\n"
	.string "closed by order of the Templar Order.\l"
	.string "Turn back.$"

PellucaCity_EventScript_RoadGuardEast_Text_0:
# 1604 "data/maps/PellucaCity/scripts.pory"
	.string "Halt. The road east to Hoya Delta is\n"
	.string "closed by order of the Templar Order.$"

PellucaCity_EventScript_RoadClosedEast_Text_0:
# 1610 "data/maps/PellucaCity/scripts.pory"
	.string "Halt. The road east to Hoya Delta is\n"
	.string "closed by order of the Templar Order.\l"
	.string "Turn back.$"

PellucaCity_EventScript_WimpodFountain_Text_0:
# 1658 "data/maps/PellucaCity/scripts.pory"
	.string "Something is splashing in the fountain!\n"
	.string "A grey shell darts out and skitters\l"
	.string "away west.$"

PellucaCity_EventScript_WimpodWell_Text_0:
# 1676 "data/maps/PellucaCity/scripts.pory"
	.string "A clatter in the well bucket! The\n"
	.string "creature bolts north toward the pond.$"

PellucaCity_EventScript_WimpodPond_Text_0:
# 1691 "data/maps/PellucaCity/scripts.pory"
	.string "The creature has its back to the water.\n"
	.string "It turns to fight!$"

PellucaCityFlooded_TriggerText::
# 340 "data/maps/PellucaCity/scripts.pory"
	.string "I need to save the drowning citizens!$"
