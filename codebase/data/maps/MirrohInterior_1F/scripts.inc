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


MirrohInterior_1F_EventScript_NurseQuest_Trigger0::
# 15 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_NURSE_QUEST_START, MirrohInterior_1F_EventScript_NurseQuest_Trigger0_2
# 16 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 17 "data/maps/MirrohInterior_1F/scripts.pory"
	call MirrohInterior_1F_EventScript_NurseQuest_Exclamation
# 19 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_Trigger0_Movement_0
# 20 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 21 "data/maps/MirrohInterior_1F/scripts.pory"
	goto MirrohInterior_1F_EventScript_NurseQuest_Main
	return

MirrohInterior_1F_EventScript_NurseQuest_Trigger0_2:
	end


MirrohInterior_1F_EventScript_NurseQuest_Trigger1::
# 24 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_NURSE_QUEST_START, MirrohInterior_1F_EventScript_NurseQuest_Trigger1_2
# 25 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 26 "data/maps/MirrohInterior_1F/scripts.pory"
	call MirrohInterior_1F_EventScript_NurseQuest_Exclamation
# 28 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_Trigger1_Movement_0
# 29 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 30 "data/maps/MirrohInterior_1F/scripts.pory"
	goto MirrohInterior_1F_EventScript_NurseQuest_Main
	return

MirrohInterior_1F_EventScript_NurseQuest_Trigger1_2:
	end


MirrohInterior_1F_EventScript_NurseQuest_Trigger2::
# 33 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_NURSE_QUEST_START, MirrohInterior_1F_EventScript_NurseQuest_Trigger2_2
# 34 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 35 "data/maps/MirrohInterior_1F/scripts.pory"
	call MirrohInterior_1F_EventScript_NurseQuest_Exclamation
# 37 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_Trigger2_Movement_0
# 38 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 39 "data/maps/MirrohInterior_1F/scripts.pory"
	goto MirrohInterior_1F_EventScript_NurseQuest_Main
	return

MirrohInterior_1F_EventScript_NurseQuest_Trigger2_2:
	end


MirrohInterior_1F_EventScript_NurseQuest_Exclamation::
# 48 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 49 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 50 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 52 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Text_0
# 53 "data/maps/MirrohInterior_1F/scripts.pory"
	release
	return


MirrohInterior_1F_EventScript_NurseQuest_Main::
# 57 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_Main_Text_0
# 58 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 60 "data/maps/MirrohInterior_1F/scripts.pory"
	startquest QUEST_MIRROH_NURSE_CHANSEY
# 61 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 1
# 62 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_NURSE_QUEST_START
# 63 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_EventScript_NurseQuest_MissingChansey::
# 67 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 68 "data/maps/MirrohInterior_1F/scripts.pory"
	faceplayer
# 69 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 70 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_0
# 71 "data/maps/MirrohInterior_1F/scripts.pory"
	call Common_EventScript_OutOfCenterPartyHeal
# 72 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_1
# 73 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 74 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_NURSE_QUEST_CHANSEYGET
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	clearflag FLAG_HIDE_MIRROH_LAST_CHANSEY
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 2
# 77 "data/maps/MirrohInterior_1F/scripts.pory"
	warp MAP_MIRROH_INTERIOR_1F, 42, 46
	return


MirrohInterior_1F_EventScript_NurseQuest_End::
# 80 "data/maps/MirrohInterior_1F/scripts.pory"
	compare VAR_MIRROH_NURSE_CHANSEY_QUEST, 2
	goto_if_eq MirrohInterior_1F_EventScript_NurseQuest_End_2
MirrohInterior_1F_EventScript_NurseQuest_End_1:
	end

MirrohInterior_1F_EventScript_NurseQuest_End_2:
# 82 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0
# 83 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 84 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 87 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 88 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH1, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 89 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH2, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 90 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH3, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 91 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH1, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_2
# 95 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH2, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_3
# 96 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH3, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_4
# 97 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement LOCALID_CH1
# 98 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_0
# 101 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 102 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_5
# 103 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 104 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_1
# 105 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 106 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 107 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CHANSEY_LAST, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_6
# 108 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 109 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_2
# 111 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 112 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 113 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_7
# 114 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 115 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_3
# 116 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 117 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_8
# 118 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 119 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CHANSEY_LAST, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9
# 120 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 121 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 122 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_4
# 123 "data/maps/MirrohInterior_1F/scripts.pory"
	giveitem ITEM_EVIOLITE
# 124 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_5
# 125 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 126 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 127 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0
# 128 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 129 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 130 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_6
# 131 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 134 "data/maps/MirrohInterior_1F/scripts.pory"
	fadescreen FADE_TO_BLACK
# 135 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH1
# 136 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH2
# 137 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH3
# 138 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CHANSEY_LAST
# 139 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_NURSE
# 140 "data/maps/MirrohInterior_1F/scripts.pory"
	fadescreen FADE_FROM_BLACK
# 143 "data/maps/MirrohInterior_1F/scripts.pory"
	completequest QUEST_MIRROH_NURSE_CHANSEY
# 144 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 3
# 145 "data/maps/MirrohInterior_1F/scripts.pory"
	release
	goto MirrohInterior_1F_EventScript_NurseQuest_End_1


MirrohInterior_1F_Trainer_A::
# 168 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_A, MirrohInterior_1F_Trainer_A_Text_0, MirrohInterior_1F_Trainer_A_Text_1
# 169 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_A_Text_2
# 170 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_B::
# 175 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_B, MirrohInterior_1F_Trainer_B_Text_0, MirrohInterior_1F_Trainer_B_Text_1
# 176 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_B_Text_2
# 177 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_C::
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_C, MirrohInterior_1F_Trainer_C_Text_0, MirrohInterior_1F_Trainer_C_Text_1
# 183 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_C_Text_2
# 184 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_D::
# 189 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 190 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_0
# 191 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 192 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_ROBBER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9
# 193 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 194 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 195 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_1
# 197 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_no_intro TRAINER_MIRROHINT_D, MirrohInterior_1F_Trainer_D_Text_2
# 198 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_3
# 199 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 200 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_Trainer_D_Movement_0
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_ROBBER, MirrohInterior_1F_Trainer_D_Movement_1
# 202 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 203 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_ROBBER
# 205 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_ROBBER
# 206 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_Trainer_E::
# 212 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_D, MirrohInterior_1F_Trainer_E_Text_0, MirrohInterior_1F_Trainer_E_Text_1
# 213 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_E_Text_2
# 214 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_NPC_A::
# 235 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_A_Text_0, MSGBOX_NPC
# 236 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_NPC_B::
# 241 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_B_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_C::
# 246 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_C_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_D::
# 252 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_D_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_E::
# 258 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_D_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_Pineco::
# 262 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_PINECO, CRY_MODE_NORMAL
# 263 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Pineco_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_A::
# 276 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_A, MirrohInterior_Bergmite_A_2
# 281 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 282 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_A
# 283 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 284 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_A_2:
# 277 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_B::
# 289 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_B, MirrohInterior_Bergmite_B_2
# 294 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 295 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_B
# 296 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 297 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_B_2:
# 290 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_C::
# 302 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_C, MirrohInterior_Bergmite_C_2
# 307 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 308 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_C
# 309 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 310 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_C_2:
# 303 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_SomberGrunts_Trigger::
# 335 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_INT_SOMBER_GRUNTS, MirrohInterior_1F_SomberGrunts_Trigger_2
# 337 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 338 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_0
# 339 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 340 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 341 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 342 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_1
# 343 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 344 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_1
# 345 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 346 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 347 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_2
# 348 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_3
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 350 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 352 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 353 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 354 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 355 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 357 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 358 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_4
# 359 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 361 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 362 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 363 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 364 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 366 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_no_intro TRAINER_MIRROHINT_E, MirrohInterior_1F_SomberGrunts_Trigger_Text_5
# 368 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 369 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 370 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 371 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 372 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_6
# 373 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 374 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 8
# 375 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_3
# 376 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 377 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 378 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_2
# 379 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_7
# 380 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 381 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 383 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_4
# 384 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_5
# 385 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 386 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 387 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 388 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_8
# 389 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 392 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_6
# 393 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_6
# 394 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 395 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_GRUNT2
# 396 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_7
# 397 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 398 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_GRUNT1
# 400 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_INT_SOMBER_GRUNTS
# 402 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end

MirrohInterior_1F_SomberGrunts_Trigger_2:
	end


MirrohInterior_1F_EventScript_Rubble::
# 408 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_Rubble_Text_0
	return


# 19 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_Trigger0_Movement_0:
# 19 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 19 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 19 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 19 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 19 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 19 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 19 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
	step_end

# 28 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_Trigger1_Movement_0:
# 28 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 28 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 28 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 28 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 28 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 28 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
	step_end

# 37 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_Trigger2_Movement_0:
# 37 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 37 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 37 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 37 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 37 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
	step_end

# 48 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0:
# 48 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_right
# 48 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 82 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0:
# 82 "data/maps/MirrohInterior_1F/scripts.pory"
	face_left
	step_end

# 88 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1:
# 88 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 94 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_2:
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	face_left
	step_end

# 95 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_3:
# 95 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 95 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 95 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 96 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_4:
# 96 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 96 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_up
# 96 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 102 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_5:
# 102 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_up
# 102 "data/maps/MirrohInterior_1F/scripts.pory"
	face_right
	step_end

# 107 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_6:
# 107 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_right
	step_end

# 113 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_7:
# 113 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 113 "data/maps/MirrohInterior_1F/scripts.pory"
	face_right
	step_end

# 117 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_8:
# 117 "data/maps/MirrohInterior_1F/scripts.pory"
	face_up
	step_end

# 119 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9:
# 119 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_down
# 119 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 200 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_0:
# 200 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 200 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 201 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_1:
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

# 338 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_0:
# 338 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_down
	step_end

# 344 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_1:
# 344 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_up
	step_end

# 361 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_2:
# 361 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
	step_end

# 375 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_3:
# 375 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_question_mark
	step_end

# 383 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_4:
# 383 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
# 383 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 384 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_5:
# 384 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
# 384 "data/maps/MirrohInterior_1F/scripts.pory"
	face_up
	step_end

# 392 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_6:
# 392 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 392 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 392 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 392 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 392 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 392 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 392 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

# 396 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_7:
# 396 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Text_0:
# 52 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey! Are you a trainer? I need your\n"
	.string "help!$"

MirrohInterior_1F_EventScript_NurseQuest_Main_Text_0:
# 57 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I was taking these Chanseys up to\n"
	.string "Winterlily Hollow to help the Nurse Joy\l"
	.string "there, but there was a cave-in and one\l"
	.string "of the Chanseys got lost!\p"
	.string "We can't go through these caves alone -\n"
	.string "the Pokémon are too fierce.\p"
	.string "Please find Chansey for us!$"

MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_0:
# 70 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "seyy!!!\p"
	.string "Chansey looks so relieved...\n"
	.string "It's about to cry!\p"
	.string "It must have been really scared,\n"
	.string "stuck all alone in here.\p"
	.string "...\p"
	.string "Chansey stretches out a hand...$"

MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_1:
# 72 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Thank you Chansey!\p"
	.string "You don't need to worry any more.\n"
	.string "Let's go back to Nurse Joy!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_0:
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Chansey!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_1:
# 104 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Oh my! Chansey! Are you alright?$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_2:
# 109 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Seyyy!!!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_3:
# 115 "data/maps/MirrohInterior_1F/scripts.pory"
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
# 122 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "seeyyy!!\p"
	.string "Chansey pulls something out of its\n"
	.string "pocket and hands it to you!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_5:
# 124 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Thank you Chansey!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_6:
# 130 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "We should go to Winterlily Hollow now.\n"
	.string "The nurse must be waiting for us.\p"
	.string "Thank you again, {PLAYER} and we wish\n"
	.string "you all the best in your journey.\p"
	.string "Drop by the Pokémon Center any time!$"

MirrohInterior_1F_Trainer_A_Text_0:
# 168 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I'm looking for a Bergmite but why I\n"
	.string "can't find any?$"

MirrohInterior_1F_Trainer_A_Text_1:
# 168 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "If I had a Bergmite I would've won!$"

MirrohInterior_1F_Trainer_A_Text_2:
# 169 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Maybe the Bergmite hide in the rocks or\n"
	.string "something...$"

MirrohInterior_1F_Trainer_B_Text_0:
# 175 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Nope! No way! That item's mine!$"

MirrohInterior_1F_Trainer_B_Text_1:
# 175 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Fine, you can have it...$"

MirrohInterior_1F_Trainer_B_Text_2:
# 176 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Travelers often leave rare items inside\n"
	.string "caves and mountains.$"

MirrohInterior_1F_Trainer_C_Text_0:
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I may switch to ICE type Pokémon after\n"
	.string "seeing the Pokémon here!$"

MirrohInterior_1F_Trainer_C_Text_1:
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I should just use ROCK types!$"

MirrohInterior_1F_Trainer_C_Text_2:
# 183 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "If you go deeper into the mountain,\n"
	.string "you'll find some rare ICE type Pokémon!$"

MirrohInterior_1F_Trainer_D_Text_0:
# 190 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hehehe - that Chansey in the corner is\n"
	.string "mine! I just need to figure out how to\l"
	.string "clear these rocks out of the way...$"

MirrohInterior_1F_Trainer_D_Text_1:
# 195 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Who're you? Mind your own business, kid.\p"
	.string "...\p"
	.string "You're going to return Chansey to Nurse\n"
	.string "Joy by the entrance?\p"
	.string "Hah! Fat chance. Ever heard about\n"
	.string "finders keepers? Well I'll teach you\l"
	.string "since nobody else did!$"

MirrohInterior_1F_Trainer_D_Text_2:
# 197 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "No! My new Chansey!$"

MirrohInterior_1F_Trainer_D_Text_3:
# 198 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Fine! You can go give that Chansey back\n"
	.string "to Nurse Joy! I'm outta here!$"

MirrohInterior_1F_Trainer_E_Text_0:
# 212 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I can't get through to Winterlily Hollow\n"
	.string "from this side. It's so frustrating!$"

MirrohInterior_1F_Trainer_E_Text_1:
# 212 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "You're also frustrating!$"

MirrohInterior_1F_Trainer_E_Text_2:
# 213 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I mean why even build a tunnel then?$"

MirrohInterior_1F_NPC_A_Text_0:
# 235 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I'm trekking to Winterlily Hollow! But my\n"
	.string "GRASS type Pokémon can't deal with all\l"
	.string "the ICE type Pokémon around here...$"

MirrohInterior_1F_NPC_B_Text_0:
# 241 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Winterlily Hollow is past the ledge\n"
	.string "above.\n"
	.string "But how do I cross the ledge?$"

MirrohInterior_1F_NPC_C_Text_0:
# 246 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Some dangerous looking people passed\n"
	.string "through here earlier with loads of\l"
	.string "heavy machinery. All that commotion\l"
	.string "caused a bunch of rocks to cave in!$"

MirrohInterior_1F_NPC_D_Text_0:
# 252 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Past this is the trek up to the\n"
	.string "mountain peak. The weather is harsh!$"

MirrohInterior_1F_Pineco_Text_0:
# 263 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Pineco looks cold!$"

MirrohInterior_Bergmite_A_Text_0:
# 277 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "There's nothing here.$"

MirrohInterior_Bergmite_A_Text_1:
# 281 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "{PLAYER} searched the rock...\p"
	.string "...but it wasn't a rock!\n"
	.string "It was a wild Pokémon!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_0:
# 341 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Grunt A$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_1:
# 342 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Did you move all the equipment? The\n"
	.string "boss is gonna be angry - we gotta get\l"
	.string "the Dreamalyser up and running quick!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_2:
# 347 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Grunt B$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_3:
# 348 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Would you relax? I'm not Gabrielle - of\n"
	.string "course I moved everything! Caused some\l"
	.string "cave-ins, but that's not our problem!\p"
	.string "Haha!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_4:
# 358 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey! Didn't your parents tell you it was\n"
	.string "rude to eavesdrop?$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_5:
# 366 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Argh! My Pokémon are so weak!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_6:
# 372 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Argh! Stupid Mime Jr! You're useless!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_7:
# 379 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey - aren't you that lab assistant who\n"
	.string "beat Melea back in Silversun City?$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_8:
# 388 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Yeah - the same one who beat Moxie up\n"
	.string "in Mt. Ceram too!\p"
	.string "The bosses will want to know this.\n"
	.string "Let's go!$"

MirrohInterior_1F_EventScript_Rubble_Text_0:
# 408 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "A small pile of rubble.\pSomething glints faintly between\nthe stones.$"
