# 1 "data/maps/MirrohInterior_1F/scripts.pory"

# 2 "data/maps/MirrohInterior_1F/scripts.pory"
    .set LOCALID_NURSE, 1
# 3 "data/maps/MirrohInterior_1F/scripts.pory"
    .set LOCALID_ROBBER, 2
# 4 "data/maps/MirrohInterior_1F/scripts.pory"
    .set LOCALID_CH1, 12
# 5 "data/maps/MirrohInterior_1F/scripts.pory"
    .set LOCALID_CH2, 13
# 6 "data/maps/MirrohInterior_1F/scripts.pory"
    .set LOCALID_CH3, 14        
# 7 "data/maps/MirrohInterior_1F/scripts.pory"
    .set LOCALID_CHANSEY_LAST, 20
# 8 "data/maps/MirrohInterior_1F/scripts.pory"
    .set LOCALID_GRUNT1, 17
# 9 "data/maps/MirrohInterior_1F/scripts.pory"
    .set LOCALID_GRUNT2, 10

MirrohInterior_1F_MapScripts::
	.byte 0


MirrohInterior_1F_EventScript_NurseQuest_Main::
# 14 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_Main_Text_0
# 15 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 17 "data/maps/MirrohInterior_1F/scripts.pory"
	startquest QUEST_MIRROH_NURSE_CHANSEY
# 18 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 1
# 19 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_NURSE_QUEST_START
# 20 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_EventScript_NurseQuest_MissingChansey::
# 24 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 25 "data/maps/MirrohInterior_1F/scripts.pory"
	faceplayer
# 26 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 27 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_0
# 28 "data/maps/MirrohInterior_1F/scripts.pory"
	call Common_EventScript_OutOfCenterPartyHeal
# 29 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_1
# 30 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 31 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_NURSE_QUEST_CHANSEYGET
# 32 "data/maps/MirrohInterior_1F/scripts.pory"
	clearflag FLAG_HIDE_MIRROH_LAST_CHANSEY
# 33 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 2
# 34 "data/maps/MirrohInterior_1F/scripts.pory"
	warp MAP_MIRROH_INTERIOR_1F, 42, 46
	return


MirrohInterior_1F_EventScript_NurseQuest_End::
# 37 "data/maps/MirrohInterior_1F/scripts.pory"
	compare VAR_MIRROH_NURSE_CHANSEY_QUEST, 2
	goto_if_eq MirrohInterior_1F_EventScript_NurseQuest_End_2
MirrohInterior_1F_EventScript_NurseQuest_End_1:
	end

MirrohInterior_1F_EventScript_NurseQuest_End_2:
# 39 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0
# 40 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 41 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 44 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 45 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH1, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_2
# 46 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH2, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_2
# 47 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH3, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_2
# 48 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 51 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH1, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_3
# 52 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH2, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_4
# 53 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH3, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_5
# 54 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement LOCALID_CH1
# 55 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 57 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_0
# 58 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 59 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_6
# 60 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 61 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_1
# 62 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 63 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CHANSEY_LAST, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_7
# 65 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 66 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_2
# 68 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 69 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 70 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_8
# 71 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 72 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_3
# 73 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 74 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CHANSEY_LAST, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_10
# 77 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 78 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 79 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_4
# 80 "data/maps/MirrohInterior_1F/scripts.pory"
	giveitem ITEM_EVIOLITE
# 81 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_5
# 82 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 83 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 84 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0
# 85 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 86 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 87 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_6
# 88 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 91 "data/maps/MirrohInterior_1F/scripts.pory"
	fadescreen FADE_TO_BLACK
# 92 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH1
# 93 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH2
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH3
# 95 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CHANSEY_LAST
# 96 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_NURSE
# 97 "data/maps/MirrohInterior_1F/scripts.pory"
	fadescreen FADE_FROM_BLACK
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	completequest QUEST_MIRROH_NURSE_CHANSEY
# 101 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 3
# 102 "data/maps/MirrohInterior_1F/scripts.pory"
	release
	goto MirrohInterior_1F_EventScript_NurseQuest_End_1


MirrohInterior_1F_Trainer_A::
# 125 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_A, MirrohInterior_1F_Trainer_A_Text_0, MirrohInterior_1F_Trainer_A_Text_1
# 126 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_A_Text_2
# 127 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_B::
# 132 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_B, MirrohInterior_1F_Trainer_B_Text_0, MirrohInterior_1F_Trainer_B_Text_1
# 133 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_B_Text_2
# 134 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_C::
# 139 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_C, MirrohInterior_1F_Trainer_C_Text_0, MirrohInterior_1F_Trainer_C_Text_1
# 140 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_C_Text_2
# 141 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_D::
# 146 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 147 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_0
# 148 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 149 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_ROBBER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_10
# 150 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 151 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 152 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_1
# 154 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_no_intro TRAINER_MIRROHINT_D, MirrohInterior_1F_Trainer_D_Text_2
# 155 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_3
# 156 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 157 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_Trainer_D_Movement_0
# 158 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_ROBBER, MirrohInterior_1F_Trainer_D_Movement_1
# 159 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 160 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_ROBBER
# 162 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_ROBBER
# 163 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_Trainer_E::
# 169 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_D, MirrohInterior_1F_Trainer_E_Text_0, MirrohInterior_1F_Trainer_E_Text_1
# 170 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_E_Text_2
# 171 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_NPC_A::
# 192 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_A_Text_0, MSGBOX_NPC
# 193 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_NPC_B::
# 198 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_B_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_C::
# 203 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_C_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_D::
# 209 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_D_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_E::
# 215 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_D_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_Pineco::
# 219 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_PINECO, CRY_MODE_NORMAL
# 220 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Pineco_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_A::
# 233 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_A, MirrohInterior_Bergmite_A_2
# 238 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 239 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_A
# 240 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 241 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_A_2:
# 234 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_B::
# 246 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_B, MirrohInterior_Bergmite_B_2
# 251 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 252 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_B
# 253 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 254 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_B_2:
# 247 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_C::
# 259 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_C, MirrohInterior_Bergmite_C_2
# 264 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 265 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_C
# 266 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 267 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_C_2:
# 260 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_SomberGrunts_Trigger::
# 292 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_INT_SOMBER_GRUNTS, MirrohInterior_1F_SomberGrunts_Trigger_2
# 294 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 295 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_0
# 296 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 297 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 298 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 299 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_1
# 300 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 301 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_1
# 302 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 303 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 304 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_2
# 305 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_3
# 306 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 307 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 309 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 310 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 311 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 312 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 314 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 315 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_4
# 316 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 318 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 319 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 320 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 321 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 323 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_no_intro TRAINER_MIRROHINT_E, MirrohInterior_1F_SomberGrunts_Trigger_Text_5
# 325 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 326 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 327 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 328 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 329 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_6
# 330 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 331 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 8
# 332 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_3
# 333 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 334 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 335 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_2
# 336 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_7
# 337 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 338 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 340 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_4
# 341 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_5
# 342 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 343 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 344 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 345 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_8
# 346 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_6
# 350 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_6
# 351 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 352 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_GRUNT2
# 353 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_7
# 354 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 355 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_GRUNT1
# 357 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_INT_SOMBER_GRUNTS
# 359 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end

MirrohInterior_1F_SomberGrunts_Trigger_2:
	end


MirrohInterior_1F_EventScript_Rubble::
# 365 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_Rubble_Text_0
	return


# 39 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0:
# 39 "data/maps/MirrohInterior_1F/scripts.pory"
	face_left
	step_end

# 40 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1:
# 40 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_right
# 40 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 45 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_2:
# 45 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 51 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_3:
# 51 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 51 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 51 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 51 "data/maps/MirrohInterior_1F/scripts.pory"
	face_left
	step_end

# 52 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_4:
# 52 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 52 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 52 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 53 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_5:
# 53 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 53 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_up
# 53 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 59 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_6:
# 59 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_up
# 59 "data/maps/MirrohInterior_1F/scripts.pory"
	face_right
	step_end

# 64 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_7:
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_right
	step_end

# 70 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_8:
# 70 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 70 "data/maps/MirrohInterior_1F/scripts.pory"
	face_right
	step_end

# 74 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9:
# 74 "data/maps/MirrohInterior_1F/scripts.pory"
	face_up
	step_end

# 76 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_10:
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_down
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 157 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_0:
# 157 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 157 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 158 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_1:
# 158 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 158 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 158 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 158 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 158 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 158 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 158 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

# 295 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_0:
# 295 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_down
	step_end

# 301 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_1:
# 301 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_up
	step_end

# 318 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_2:
# 318 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
	step_end

# 332 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_3:
# 332 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_question_mark
	step_end

# 340 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_4:
# 340 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
# 340 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 341 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_5:
# 341 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
# 341 "data/maps/MirrohInterior_1F/scripts.pory"
	face_up
	step_end

# 349 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_6:
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

# 353 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_7:
# 353 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

MirrohInterior_1F_EventScript_NurseQuest_Main_Text_0:
# 14 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I was taking these Chanseys up to\n"
	.string "Winterlily Hollow to help the Nurse Joy\l"
	.string "there, but there was a cave-in and one\l"
	.string "of the Chanseys got lost!\p"
	.string "We can't go through these caves alone -\n"
	.string "the Pokémon are too fierce.\p"
	.string "Please find Chansey for us!$"

MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_0:
# 27 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "seyy!!!\p"
	.string "Chansey looks so relieved...\n"
	.string "It's about to cry!\p"
	.string "It must have been really scared,\n"
	.string "stuck all alone in here.\p"
	.string "...\p"
	.string "Chansey stretches out a hand...$"

MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_1:
# 29 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Thank you Chansey!\p"
	.string "You don't need to worry any more.\n"
	.string "Let's go back to Nurse Joy!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_0:
# 57 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Chansey!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_1:
# 61 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Oh my! Chansey! Are you alright?$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_2:
# 66 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Seyyy!!!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_3:
# 72 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Thank you trainer! You saved Chansey!\p"
	.string "This group of people calling themselves\n"
	.string "Team Somber caused these cave-ins!\p"
	.string "They came in here with big machinery\n"
	.string "and collapsed parts of the cavern.\p"
	.string "They seemed so scary!\n"
	.string "I hope we don't run into them.\p"
	.string "We're all in your debt, {PLAYER}.\n"
	.string "There's not much in the way of a reward\l"
	.string "that I can...oh?$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_4:
# 79 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "seeyyy!!\p"
	.string "Chansey pulls something out of its\n"
	.string "pocket and hands it to you!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_5:
# 81 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Thank you Chansey!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_6:
# 87 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "We should go to Winterlily Hollow now.\n"
	.string "The nurse must be waiting for us.\p"
	.string "Thank you again, {PLAYER} and we wish\n"
	.string "you all the best in your journey.\p"
	.string "Drop by the Pokémon Center any time!$"

MirrohInterior_1F_Trainer_A_Text_0:
# 125 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I'm looking for a Bergmite but why I\n"
	.string "can't find any?$"

MirrohInterior_1F_Trainer_A_Text_1:
# 125 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "If I had a Bergmite I would've won!$"

MirrohInterior_1F_Trainer_A_Text_2:
# 126 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Maybe the Bergmite hide in the rocks or\n"
	.string "something...$"

MirrohInterior_1F_Trainer_B_Text_0:
# 132 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Nope! No way! That item's mine!$"

MirrohInterior_1F_Trainer_B_Text_1:
# 132 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Fine, you can have it...$"

MirrohInterior_1F_Trainer_B_Text_2:
# 133 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Travelers often leave rare items inside\n"
	.string "caves and mountains.$"

MirrohInterior_1F_Trainer_C_Text_0:
# 139 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I may switch to ICE type Pokémon after\n"
	.string "seeing the Pokémon here!$"

MirrohInterior_1F_Trainer_C_Text_1:
# 139 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I should just use ROCK types!$"

MirrohInterior_1F_Trainer_C_Text_2:
# 140 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "If you go deeper into the mountain,\n"
	.string "you'll find some rare ICE type Pokémon!$"

MirrohInterior_1F_Trainer_D_Text_0:
# 147 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hehehe - that Chansey in the corner is\n"
	.string "mine! I just need to figure out how to\l"
	.string "clear these rocks out of the way...$"

MirrohInterior_1F_Trainer_D_Text_1:
# 152 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Who're you? Mind your own business, kid.\p"
	.string "...\p"
	.string "You're going to return Chansey to Nurse\n"
	.string "Joy by the entrance?\p"
	.string "Hah! Fat chance. Ever heard about\n"
	.string "finders keepers? Well I'll teach you\l"
	.string "since nobody else did!$"

MirrohInterior_1F_Trainer_D_Text_2:
# 154 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "No! My new Chansey!$"

MirrohInterior_1F_Trainer_D_Text_3:
# 155 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Fine! You can go give that Chansey back\n"
	.string "to Nurse Joy! I'm outta here!$"

MirrohInterior_1F_Trainer_E_Text_0:
# 169 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I can't get through to Winterlily Hollow\n"
	.string "from this side. It's so frustrating!$"

MirrohInterior_1F_Trainer_E_Text_1:
# 169 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "You're also frustrating!$"

MirrohInterior_1F_Trainer_E_Text_2:
# 170 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I mean why even build a tunnel then?$"

MirrohInterior_1F_NPC_A_Text_0:
# 192 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I'm trekking to Winterlily Hollow! But my\n"
	.string "GRASS type Pokémon can't deal with all\l"
	.string "the ICE type Pokémon around here...$"

MirrohInterior_1F_NPC_B_Text_0:
# 198 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Winterlily Hollow is past the ledge\n"
	.string "above.\n"
	.string "But how do I cross the ledge?$"

MirrohInterior_1F_NPC_C_Text_0:
# 203 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Some dangerous looking people passed\n"
	.string "through here earlier with loads of\l"
	.string "heavy machinery. All that commotion\l"
	.string "caused a bunch of rocks to cave in!$"

MirrohInterior_1F_NPC_D_Text_0:
# 209 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Past this is the trek up to the\n"
	.string "mountain peak. The weather is harsh!$"

MirrohInterior_1F_Pineco_Text_0:
# 220 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Pineco looks cold!$"

MirrohInterior_Bergmite_A_Text_0:
# 234 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "There's nothing here.$"

MirrohInterior_Bergmite_A_Text_1:
# 238 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "{PLAYER} searched the rock...\p"
	.string "...but it wasn't a rock!\n"
	.string "It was a wild Pokémon!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_0:
# 298 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Grunt A$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_1:
# 299 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Did you move all the equipment? The\n"
	.string "boss is gonna be angry - we gotta get\l"
	.string "the Dreamalyser up and running quick!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_2:
# 304 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Grunt B$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_3:
# 305 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Would you relax? I'm not Gabrielle - of\n"
	.string "course I moved everything! Caused some\l"
	.string "cave-ins, but that's not our problem!\p"
	.string "Haha!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_4:
# 315 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey! Didn't your parents tell you it was\n"
	.string "rude to eavesdrop?$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_5:
# 323 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Argh! My Pokémon are so weak!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_6:
# 329 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Argh! Stupid Mime Jr! You're useless!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_7:
# 336 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey - aren't you that lab assistant who\n"
	.string "beat Melea back in Silversun City?$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_8:
# 345 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Yeah - the same one who beat Moxie up\n"
	.string "in Mt. Ceram too!\p"
	.string "The bosses will want to know this.\n"
	.string "Let's go!$"

MirrohInterior_1F_EventScript_Rubble_Text_0:
# 365 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "A small pile of rubble.\pSomething glints faintly between\nthe stones.$"
