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


MirrohInterior_1F_EventScript_NurseQuest_Trigger2::
# 14 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_NURSE_QUEST_START, MirrohInterior_1F_EventScript_NurseQuest_Trigger2_2
# 15 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 16 "data/maps/MirrohInterior_1F/scripts.pory"
	call MirrohInterior_1F_EventScript_NurseQuest_Exclamation
# 18 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_Trigger2_Movement_0
# 19 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 20 "data/maps/MirrohInterior_1F/scripts.pory"
	goto MirrohInterior_1F_EventScript_NurseQuest_Main
	return

MirrohInterior_1F_EventScript_NurseQuest_Trigger2_2:
	end


MirrohInterior_1F_EventScript_NurseQuest_Exclamation::
# 29 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 30 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 31 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 33 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Text_0
# 34 "data/maps/MirrohInterior_1F/scripts.pory"
	release
	return


MirrohInterior_1F_EventScript_NurseQuest_Main::
# 38 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_Main_Text_0
# 39 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 41 "data/maps/MirrohInterior_1F/scripts.pory"
	startquest QUEST_MIRROH_NURSE_CHANSEY
# 42 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 1
# 43 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_NURSE_QUEST_START
# 44 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_EventScript_NurseQuest_MissingChansey::
# 48 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 49 "data/maps/MirrohInterior_1F/scripts.pory"
	faceplayer
# 50 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 51 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_0
# 52 "data/maps/MirrohInterior_1F/scripts.pory"
	call Common_EventScript_OutOfCenterPartyHeal
# 53 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_1
# 54 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 55 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_NURSE_QUEST_CHANSEYGET
# 56 "data/maps/MirrohInterior_1F/scripts.pory"
	clearflag FLAG_HIDE_MIRROH_LAST_CHANSEY
# 57 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 2
# 58 "data/maps/MirrohInterior_1F/scripts.pory"
	warp MAP_MIRROH_INTERIOR_1F, 42, 46
	return


MirrohInterior_1F_EventScript_NurseQuest_End::
# 61 "data/maps/MirrohInterior_1F/scripts.pory"
	compare VAR_MIRROH_NURSE_CHANSEY_QUEST, 2
	goto_if_eq MirrohInterior_1F_EventScript_NurseQuest_End_2
MirrohInterior_1F_EventScript_NurseQuest_End_1:
	end

MirrohInterior_1F_EventScript_NurseQuest_End_2:
# 63 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 65 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 68 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 69 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH1, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 70 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH2, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 71 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH3, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 72 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH1, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_2
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH2, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_3
# 77 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH3, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_4
# 78 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement LOCALID_CH1
# 79 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 81 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_0
# 82 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 83 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_5
# 84 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 85 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_1
# 86 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 87 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 88 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CHANSEY_LAST, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_6
# 89 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 90 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_2
# 92 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 93 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_7
# 95 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 96 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_3
# 97 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 98 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_8
# 99 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CHANSEY_LAST, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9
# 101 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 102 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 103 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_4
# 104 "data/maps/MirrohInterior_1F/scripts.pory"
	giveitem ITEM_EVIOLITE
# 105 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_5
# 106 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 107 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 108 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0
# 109 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 110 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 111 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_6
# 112 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 115 "data/maps/MirrohInterior_1F/scripts.pory"
	fadescreen FADE_TO_BLACK
# 116 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH1
# 117 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH2
# 118 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH3
# 119 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CHANSEY_LAST
# 120 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_NURSE
# 121 "data/maps/MirrohInterior_1F/scripts.pory"
	fadescreen FADE_FROM_BLACK
# 124 "data/maps/MirrohInterior_1F/scripts.pory"
	completequest QUEST_MIRROH_NURSE_CHANSEY
# 125 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 3
# 126 "data/maps/MirrohInterior_1F/scripts.pory"
	release
	goto MirrohInterior_1F_EventScript_NurseQuest_End_1


MirrohInterior_1F_Trainer_A::
# 149 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_A, MirrohInterior_1F_Trainer_A_Text_0, MirrohInterior_1F_Trainer_A_Text_1
# 150 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_A_Text_2
# 151 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_B::
# 156 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_B, MirrohInterior_1F_Trainer_B_Text_0, MirrohInterior_1F_Trainer_B_Text_1
# 157 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_B_Text_2
# 158 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_C::
# 163 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_C, MirrohInterior_1F_Trainer_C_Text_0, MirrohInterior_1F_Trainer_C_Text_1
# 164 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_C_Text_2
# 165 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_D::
# 170 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 171 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_0
# 172 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 173 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_ROBBER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9
# 174 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 175 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 176 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_1
# 178 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_no_intro TRAINER_MIRROHINT_D, MirrohInterior_1F_Trainer_D_Text_2
# 179 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_3
# 180 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 181 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_Trainer_D_Movement_0
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_ROBBER, MirrohInterior_1F_Trainer_D_Movement_1
# 183 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 184 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_ROBBER
# 186 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_ROBBER
# 187 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_Trainer_E::
# 193 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_D, MirrohInterior_1F_Trainer_E_Text_0, MirrohInterior_1F_Trainer_E_Text_1
# 194 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_E_Text_2
# 195 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_NPC_A::
# 216 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_A_Text_0, MSGBOX_NPC
# 217 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_NPC_B::
# 222 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_B_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_C::
# 227 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_C_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_D::
# 233 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_D_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_E::
# 239 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_D_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_Pineco::
# 243 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_PINECO, CRY_MODE_NORMAL
# 244 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Pineco_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_A::
# 257 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_A, MirrohInterior_Bergmite_A_2
# 262 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 263 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_A
# 264 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 265 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_A_2:
# 258 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_B::
# 270 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_B, MirrohInterior_Bergmite_B_2
# 275 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 276 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_B
# 277 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 278 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_B_2:
# 271 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_C::
# 283 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_C, MirrohInterior_Bergmite_C_2
# 288 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 289 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_C
# 290 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 291 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_C_2:
# 284 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_SomberGrunts_Trigger::
# 316 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_INT_SOMBER_GRUNTS, MirrohInterior_1F_SomberGrunts_Trigger_2
# 318 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 319 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_0
# 320 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 321 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 322 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 323 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_1
# 324 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 325 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_1
# 326 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 327 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 328 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_2
# 329 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_3
# 330 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 331 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 333 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 334 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 335 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 336 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 338 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 339 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_4
# 340 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 342 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 343 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 344 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 345 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 347 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_no_intro TRAINER_MIRROHINT_E, MirrohInterior_1F_SomberGrunts_Trigger_Text_5
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 350 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 351 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 352 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 353 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_6
# 354 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 355 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 8
# 356 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_3
# 357 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 358 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 359 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_2
# 360 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_7
# 361 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 362 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 364 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_4
# 365 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_5
# 366 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 367 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 368 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 369 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_8
# 370 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 373 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_6
# 374 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_6
# 375 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 376 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_GRUNT2
# 377 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_7
# 378 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 379 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_GRUNT1
# 381 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_INT_SOMBER_GRUNTS
# 383 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end

MirrohInterior_1F_SomberGrunts_Trigger_2:
	end


MirrohInterior_1F_EventScript_Rubble::
# 389 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_Rubble_Text_0
	return


# 18 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_Trigger2_Movement_0:
# 18 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 18 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 18 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 18 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 18 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
	step_end

# 29 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0:
# 29 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_right
# 29 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 63 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0:
# 63 "data/maps/MirrohInterior_1F/scripts.pory"
	face_left
	step_end

# 69 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1:
# 69 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 75 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_2:
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	face_left
	step_end

# 76 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_3:
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 77 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_4:
# 77 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 77 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_up
# 77 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 83 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_5:
# 83 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_up
# 83 "data/maps/MirrohInterior_1F/scripts.pory"
	face_right
	step_end

# 88 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_6:
# 88 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_right
	step_end

# 94 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_7:
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	face_right
	step_end

# 98 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_8:
# 98 "data/maps/MirrohInterior_1F/scripts.pory"
	face_up
	step_end

# 100 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9:
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_down
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 181 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_0:
# 181 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 181 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 182 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_1:
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

# 319 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_0:
# 319 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_down
	step_end

# 325 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_1:
# 325 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_up
	step_end

# 342 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_2:
# 342 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
	step_end

# 356 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_3:
# 356 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_question_mark
	step_end

# 364 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_4:
# 364 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
# 364 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 365 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_5:
# 365 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
# 365 "data/maps/MirrohInterior_1F/scripts.pory"
	face_up
	step_end

# 373 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_6:
# 373 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 373 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 373 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 373 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 373 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 373 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 373 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

# 377 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_7:
# 377 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Text_0:
# 33 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey! Are you a trainer? I need your\n"
	.string "help!$"

MirrohInterior_1F_EventScript_NurseQuest_Main_Text_0:
# 38 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I was taking these Chanseys up to\n"
	.string "Winterlily Hollow to help the Nurse Joy\l"
	.string "there, but there was a cave-in and one\l"
	.string "of the Chanseys got lost!\p"
	.string "We can't go through these caves alone -\n"
	.string "the Pokémon are too fierce.\p"
	.string "Please find Chansey for us!$"

MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_0:
# 51 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "seyy!!!\p"
	.string "Chansey looks so relieved...\n"
	.string "It's about to cry!\p"
	.string "It must have been really scared,\n"
	.string "stuck all alone in here.\p"
	.string "...\p"
	.string "Chansey stretches out a hand...$"

MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_1:
# 53 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Thank you Chansey!\p"
	.string "You don't need to worry any more.\n"
	.string "Let's go back to Nurse Joy!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_0:
# 81 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Chansey!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_1:
# 85 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Oh my! Chansey! Are you alright?$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_2:
# 90 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Seyyy!!!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_3:
# 96 "data/maps/MirrohInterior_1F/scripts.pory"
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
# 103 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "seeyyy!!\p"
	.string "Chansey pulls something out of its\n"
	.string "pocket and hands it to you!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_5:
# 105 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Thank you Chansey!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_6:
# 111 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "We should go to Winterlily Hollow now.\n"
	.string "The nurse must be waiting for us.\p"
	.string "Thank you again, {PLAYER} and we wish\n"
	.string "you all the best in your journey.\p"
	.string "Drop by the Pokémon Center any time!$"

MirrohInterior_1F_Trainer_A_Text_0:
# 149 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I'm looking for a Bergmite but why I\n"
	.string "can't find any?$"

MirrohInterior_1F_Trainer_A_Text_1:
# 149 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "If I had a Bergmite I would've won!$"

MirrohInterior_1F_Trainer_A_Text_2:
# 150 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Maybe the Bergmite hide in the rocks or\n"
	.string "something...$"

MirrohInterior_1F_Trainer_B_Text_0:
# 156 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Nope! No way! That item's mine!$"

MirrohInterior_1F_Trainer_B_Text_1:
# 156 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Fine, you can have it...$"

MirrohInterior_1F_Trainer_B_Text_2:
# 157 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Travelers often leave rare items inside\n"
	.string "caves and mountains.$"

MirrohInterior_1F_Trainer_C_Text_0:
# 163 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I may switch to ICE type Pokémon after\n"
	.string "seeing the Pokémon here!$"

MirrohInterior_1F_Trainer_C_Text_1:
# 163 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I should just use ROCK types!$"

MirrohInterior_1F_Trainer_C_Text_2:
# 164 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "If you go deeper into the mountain,\n"
	.string "you'll find some rare ICE type Pokémon!$"

MirrohInterior_1F_Trainer_D_Text_0:
# 171 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hehehe - that Chansey in the corner is\n"
	.string "mine! I just need to figure out how to\l"
	.string "clear these rocks out of the way...$"

MirrohInterior_1F_Trainer_D_Text_1:
# 176 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Who're you? Mind your own business, kid.\p"
	.string "...\p"
	.string "You're going to return Chansey to Nurse\n"
	.string "Joy by the entrance?\p"
	.string "Hah! Fat chance. Ever heard about\n"
	.string "finders keepers? Well I'll teach you\l"
	.string "since nobody else did!$"

MirrohInterior_1F_Trainer_D_Text_2:
# 178 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "No! My new Chansey!$"

MirrohInterior_1F_Trainer_D_Text_3:
# 179 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Fine! You can go give that Chansey back\n"
	.string "to Nurse Joy! I'm outta here!$"

MirrohInterior_1F_Trainer_E_Text_0:
# 193 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I can't get through to Winterlily Hollow\n"
	.string "from this side. It's so frustrating!$"

MirrohInterior_1F_Trainer_E_Text_1:
# 193 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "You're also frustrating!$"

MirrohInterior_1F_Trainer_E_Text_2:
# 194 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I mean why even build a tunnel then?$"

MirrohInterior_1F_NPC_A_Text_0:
# 216 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I'm trekking to Winterlily Hollow! But my\n"
	.string "GRASS type Pokémon can't deal with all\l"
	.string "the ICE type Pokémon around here...$"

MirrohInterior_1F_NPC_B_Text_0:
# 222 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Winterlily Hollow is past the ledge\n"
	.string "above.\n"
	.string "But how do I cross the ledge?$"

MirrohInterior_1F_NPC_C_Text_0:
# 227 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Some dangerous looking people passed\n"
	.string "through here earlier with loads of\l"
	.string "heavy machinery. All that commotion\l"
	.string "caused a bunch of rocks to cave in!$"

MirrohInterior_1F_NPC_D_Text_0:
# 233 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Past this is the trek up to the\n"
	.string "mountain peak. The weather is harsh!$"

MirrohInterior_1F_Pineco_Text_0:
# 244 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Pineco looks cold!$"

MirrohInterior_Bergmite_A_Text_0:
# 258 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "There's nothing here.$"

MirrohInterior_Bergmite_A_Text_1:
# 262 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "{PLAYER} searched the rock...\p"
	.string "...but it wasn't a rock!\n"
	.string "It was a wild Pokémon!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_0:
# 322 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Grunt A$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_1:
# 323 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Did you move all the equipment? The\n"
	.string "boss is gonna be angry - we gotta get\l"
	.string "the Dreamalyser up and running quick!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_2:
# 328 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Grunt B$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_3:
# 329 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Would you relax? I'm not Gabrielle - of\n"
	.string "course I moved everything! Caused some\l"
	.string "cave-ins, but that's not our problem!\p"
	.string "Haha!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_4:
# 339 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey! Didn't your parents tell you it was\n"
	.string "rude to eavesdrop?$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_5:
# 347 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Argh! My Pokémon are so weak!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_6:
# 353 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Argh! Stupid Mime Jr! You're useless!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_7:
# 360 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey - aren't you that lab assistant who\n"
	.string "beat Melea back in Silversun City?$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_8:
# 369 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Yeah - the same one who beat Moxie up\n"
	.string "in Mt. Ceram too!\p"
	.string "The bosses will want to know this.\n"
	.string "Let's go!$"

MirrohInterior_1F_EventScript_Rubble_Text_0:
# 389 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "A small pile of rubble.\pSomething glints faintly between\nthe stones.$"
