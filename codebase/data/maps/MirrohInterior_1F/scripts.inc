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


MirrohInterior_1F_EventScript_Chansey::
# 15 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 16 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_Chansey_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_EventScript_NurseQuest_Trigger0::
# 21 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_NURSE_QUEST_START, MirrohInterior_1F_EventScript_NurseQuest_Trigger0_2
# 22 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 23 "data/maps/MirrohInterior_1F/scripts.pory"
	call MirrohInterior_1F_EventScript_NurseQuest_Exclamation
# 25 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_Trigger0_Movement_0
# 26 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 27 "data/maps/MirrohInterior_1F/scripts.pory"
	goto MirrohInterior_1F_EventScript_NurseQuest_Main
	return

MirrohInterior_1F_EventScript_NurseQuest_Trigger0_2:
	end


MirrohInterior_1F_EventScript_NurseQuest_Trigger1::
# 30 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_NURSE_QUEST_START, MirrohInterior_1F_EventScript_NurseQuest_Trigger1_2
# 31 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 32 "data/maps/MirrohInterior_1F/scripts.pory"
	call MirrohInterior_1F_EventScript_NurseQuest_Exclamation
# 34 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_Trigger1_Movement_0
# 35 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 36 "data/maps/MirrohInterior_1F/scripts.pory"
	goto MirrohInterior_1F_EventScript_NurseQuest_Main
	return

MirrohInterior_1F_EventScript_NurseQuest_Trigger1_2:
	end


MirrohInterior_1F_EventScript_NurseQuest_Trigger2::
# 39 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_NURSE_QUEST_START, MirrohInterior_1F_EventScript_NurseQuest_Trigger2_2
# 40 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 41 "data/maps/MirrohInterior_1F/scripts.pory"
	call MirrohInterior_1F_EventScript_NurseQuest_Exclamation
# 43 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_Trigger2_Movement_0
# 44 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 45 "data/maps/MirrohInterior_1F/scripts.pory"
	goto MirrohInterior_1F_EventScript_NurseQuest_Main
	return

MirrohInterior_1F_EventScript_NurseQuest_Trigger2_2:
	end


MirrohInterior_1F_EventScript_NurseQuest_Exclamation::
# 54 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 55 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 56 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 58 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Text_0
# 59 "data/maps/MirrohInterior_1F/scripts.pory"
	release
	return


MirrohInterior_1F_EventScript_NurseQuest_Main::
# 63 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_Main_Text_0
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 66 "data/maps/MirrohInterior_1F/scripts.pory"
	startquest QUEST_MIRROH_NURSE_CHANSEY
# 67 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 1
# 68 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_NURSE_QUEST_START
# 69 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_EventScript_NurseQuest_MissingChansey::
# 73 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 74 "data/maps/MirrohInterior_1F/scripts.pory"
	faceplayer
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_0
# 77 "data/maps/MirrohInterior_1F/scripts.pory"
	call Common_EventScript_OutOfCenterPartyHeal
# 78 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_1
# 79 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 80 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_NURSE_QUEST_CHANSEYGET
# 81 "data/maps/MirrohInterior_1F/scripts.pory"
	clearflag FLAG_HIDE_MIRROH_LAST_CHANSEY
# 82 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 2
# 83 "data/maps/MirrohInterior_1F/scripts.pory"
	warp MAP_MIRROH_INTERIOR_1F, 42, 46
	return


MirrohInterior_1F_EventScript_NurseQuest_End::
# 86 "data/maps/MirrohInterior_1F/scripts.pory"
	compare VAR_MIRROH_NURSE_CHANSEY_QUEST, 2
	goto_if_eq MirrohInterior_1F_EventScript_NurseQuest_End_2
MirrohInterior_1F_EventScript_NurseQuest_End_1:
	end

MirrohInterior_1F_EventScript_NurseQuest_End_2:
# 88 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0
# 89 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 90 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 93 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH1, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 95 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH2, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 96 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH3, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1
# 97 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH1, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_2
# 101 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH2, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_3
# 102 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CH3, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_4
# 103 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement LOCALID_CH1
# 104 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 106 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_0
# 107 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 108 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_5
# 109 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 110 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_1
# 111 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 112 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 113 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CHANSEY_LAST, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_6
# 114 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 115 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_2
# 117 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 118 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 119 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_NURSE, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_7
# 120 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 121 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_3
# 122 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 123 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_8
# 124 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 125 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_CHANSEY_LAST, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9
# 126 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 127 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 128 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_4
# 129 "data/maps/MirrohInterior_1F/scripts.pory"
	giveitem ITEM_EVIOLITE
# 130 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_5
# 131 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 132 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 133 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0
# 134 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 135 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 136 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_NurseQuest_End_Text_6
# 137 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 140 "data/maps/MirrohInterior_1F/scripts.pory"
	fadescreen FADE_TO_BLACK
# 141 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH1
# 142 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH2
# 143 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CH3
# 144 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_CHANSEY_LAST
# 145 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_NURSE
# 146 "data/maps/MirrohInterior_1F/scripts.pory"
	fadescreen FADE_FROM_BLACK
# 149 "data/maps/MirrohInterior_1F/scripts.pory"
	completequest QUEST_MIRROH_NURSE_CHANSEY
# 150 "data/maps/MirrohInterior_1F/scripts.pory"
	setvar VAR_MIRROH_NURSE_CHANSEY_QUEST, 3
# 151 "data/maps/MirrohInterior_1F/scripts.pory"
	release
	goto MirrohInterior_1F_EventScript_NurseQuest_End_1


MirrohInterior_1F_Trainer_A::
# 174 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_A, MirrohInterior_1F_Trainer_A_Text_0, MirrohInterior_1F_Trainer_A_Text_1
# 175 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_A_Text_2
# 176 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_B::
# 181 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_B, MirrohInterior_1F_Trainer_B_Text_0, MirrohInterior_1F_Trainer_B_Text_1
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_B_Text_2
# 183 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_C::
# 188 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_C, MirrohInterior_1F_Trainer_C_Text_0, MirrohInterior_1F_Trainer_C_Text_1
# 189 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_C_Text_2
# 190 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_D::
# 195 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 196 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_0
# 197 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 198 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_ROBBER, MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9
# 199 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 200 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_1
# 203 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_no_intro TRAINER_MIRROHINT_D, MirrohInterior_1F_Trainer_D_Text_2
# 204 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_3
# 205 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 206 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_Trainer_D_Movement_0
# 207 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_ROBBER, MirrohInterior_1F_Trainer_D_Movement_1
# 208 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 209 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_ROBBER
# 211 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_ROBBER
# 212 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_Trainer_E::
# 218 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_D, MirrohInterior_1F_Trainer_E_Text_0, MirrohInterior_1F_Trainer_E_Text_1
# 219 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_E_Text_2
# 220 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_NPC_A::
# 241 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_A_Text_0, MSGBOX_NPC
# 242 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_NPC_B::
# 247 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_B_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_C::
# 252 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_C_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_D::
# 258 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_D_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_E::
# 264 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_D_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_Pineco::
# 268 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_PINECO, CRY_MODE_NORMAL
# 269 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Pineco_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_A::
# 282 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_A, MirrohInterior_Bergmite_A_2
# 287 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 288 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_A
# 289 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 290 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_A_2:
# 283 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_B::
# 295 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_B, MirrohInterior_Bergmite_B_2
# 300 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 301 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_B
# 302 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 303 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_B_2:
# 296 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_C::
# 308 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_C, MirrohInterior_Bergmite_C_2
# 313 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 314 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_C
# 315 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 316 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_C_2:
# 309 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_SomberGrunts_Trigger::
# 341 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_INT_SOMBER_GRUNTS, MirrohInterior_1F_SomberGrunts_Trigger_2
# 343 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 344 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_0
# 345 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 346 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 347 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 348 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_1
# 349 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 350 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_1
# 351 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 352 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 353 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_2
# 354 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_3
# 355 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 356 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 358 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 359 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 360 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 361 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 363 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 364 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_4
# 365 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 367 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 368 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 369 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 370 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 372 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_no_intro TRAINER_MIRROHINT_E, MirrohInterior_1F_SomberGrunts_Trigger_Text_5
# 374 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0
# 375 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 376 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 377 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 378 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_6
# 379 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 380 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 8
# 381 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_3
# 382 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 383 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 384 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_2
# 385 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_7
# 386 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 387 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 389 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_4
# 390 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_5
# 391 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 392 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 393 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 394 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_8
# 395 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 398 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_6
# 399 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_6
# 400 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 401 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_GRUNT2
# 402 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_7
# 403 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 404 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_GRUNT1
# 406 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_INT_SOMBER_GRUNTS
# 408 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end

MirrohInterior_1F_SomberGrunts_Trigger_2:
	end


MirrohInterior_1F_EventScript_Rubble::
# 414 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_Rubble_Text_0
	return


# 25 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_Trigger0_Movement_0:
# 25 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 25 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 25 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 25 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 25 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 25 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 25 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
	step_end

# 34 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_Trigger1_Movement_0:
# 34 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 34 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 34 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 34 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 34 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 34 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
	step_end

# 43 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_Trigger2_Movement_0:
# 43 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 43 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 43 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 43 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 43 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
	step_end

# 54 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Movement_0:
# 54 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_right
# 54 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 88 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_0:
# 88 "data/maps/MirrohInterior_1F/scripts.pory"
	face_left
	step_end

# 94 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_1:
# 94 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 100 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_2:
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 100 "data/maps/MirrohInterior_1F/scripts.pory"
	face_left
	step_end

# 101 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_3:
# 101 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 101 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 101 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 102 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_4:
# 102 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
# 102 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_up
# 102 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 108 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_5:
# 108 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_up
# 108 "data/maps/MirrohInterior_1F/scripts.pory"
	face_right
	step_end

# 113 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_6:
# 113 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_right
	step_end

# 119 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_7:
# 119 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 119 "data/maps/MirrohInterior_1F/scripts.pory"
	face_right
	step_end

# 123 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_8:
# 123 "data/maps/MirrohInterior_1F/scripts.pory"
	face_up
	step_end

# 125 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_EventScript_NurseQuest_End_Movement_9:
# 125 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_down
# 125 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 206 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_0:
# 206 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 206 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 207 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_1:
# 207 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 207 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 207 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 207 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 207 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 207 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 207 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

# 344 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_0:
# 344 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_down
	step_end

# 350 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_1:
# 350 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_up
	step_end

# 367 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_2:
# 367 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
	step_end

# 381 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_3:
# 381 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_question_mark
	step_end

# 389 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_4:
# 389 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
# 389 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 390 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_5:
# 390 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
# 390 "data/maps/MirrohInterior_1F/scripts.pory"
	face_up
	step_end

# 398 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_6:
# 398 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 398 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 398 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 398 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 398 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 398 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 398 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

# 402 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_7:
# 402 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

MirrohInterior_1F_EventScript_Chansey_Text_0:
# 16 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Chansey looks stressed!\n"
	.string "Must be worried about its friend.$"

MirrohInterior_1F_EventScript_NurseQuest_Exclamation_Text_0:
# 58 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey! Are you a trainer? I need your\n"
	.string "help!$"

MirrohInterior_1F_EventScript_NurseQuest_Main_Text_0:
# 63 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I was taking these Chanseys up to\n"
	.string "Winterlily Hollow to help the Nurse Joy\l"
	.string "there, but there was a cave-in and one\l"
	.string "of the Chanseys got lost!\p"
	.string "We can't go through these caves alone -\n"
	.string "the Pokémon are too fierce.\p"
	.string "Please find Chansey for us!$"

MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_0:
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "seyy!!!\p"
	.string "Chansey looks so relieved...\n"
	.string "It's about to cry!\p"
	.string "It must have been really scared,\n"
	.string "stuck all alone in here.\p"
	.string "...\p"
	.string "Chansey stretches out a hand...$"

MirrohInterior_1F_EventScript_NurseQuest_MissingChansey_Text_1:
# 78 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Thank you Chansey!\p"
	.string "You don't need to worry any more.\n"
	.string "Let's go back to Nurse Joy!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_0:
# 106 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Chansey!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_1:
# 110 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Oh my! Chansey! Are you alright?$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_2:
# 115 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Seyyy!!!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_3:
# 121 "data/maps/MirrohInterior_1F/scripts.pory"
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
# 128 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "seeyyy!!\p"
	.string "Chansey pulls something out of its\n"
	.string "pocket and hands it to you!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_5:
# 130 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Thank you Chansey!$"

MirrohInterior_1F_EventScript_NurseQuest_End_Text_6:
# 136 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "We should go to Winterlily Hollow now.\n"
	.string "The nurse must be waiting for us.\p"
	.string "Thank you again, {PLAYER} and we wish\n"
	.string "you all the best in your journey.\p"
	.string "Drop by the Pokémon Center any time!$"

MirrohInterior_1F_Trainer_A_Text_0:
# 174 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I'm looking for a Bergmite but why I\n"
	.string "can't find any?$"

MirrohInterior_1F_Trainer_A_Text_1:
# 174 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "If I had a Bergmite I would've won!$"

MirrohInterior_1F_Trainer_A_Text_2:
# 175 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Maybe the Bergmite hide in the rocks or\n"
	.string "something...$"

MirrohInterior_1F_Trainer_B_Text_0:
# 181 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Nope! No way! That item's mine!$"

MirrohInterior_1F_Trainer_B_Text_1:
# 181 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Fine, you can have it...$"

MirrohInterior_1F_Trainer_B_Text_2:
# 182 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Travelers often leave rare items inside\n"
	.string "caves and mountains.$"

MirrohInterior_1F_Trainer_C_Text_0:
# 188 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I may switch to ICE type Pokémon after\n"
	.string "seeing the Pokémon here!$"

MirrohInterior_1F_Trainer_C_Text_1:
# 188 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I should just use ROCK types!$"

MirrohInterior_1F_Trainer_C_Text_2:
# 189 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "If you go deeper into the mountain,\n"
	.string "you'll find some rare ICE type Pokémon!$"

MirrohInterior_1F_Trainer_D_Text_0:
# 196 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hehehe - that Chansey in the corner is\n"
	.string "mine! I just need to figure out how to\l"
	.string "clear these rocks out of the way...$"

MirrohInterior_1F_Trainer_D_Text_1:
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Who're you? Mind your own business, kid.\p"
	.string "...\p"
	.string "You're going to return Chansey to Nurse\n"
	.string "Joy by the entrance?\p"
	.string "Hah! Fat chance. Ever heard about\n"
	.string "finders keepers? Well I'll teach you\l"
	.string "since nobody else did!$"

MirrohInterior_1F_Trainer_D_Text_2:
# 203 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "No! My new Chansey!$"

MirrohInterior_1F_Trainer_D_Text_3:
# 204 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Fine! You can go give that Chansey back\n"
	.string "to Nurse Joy! I'm outta here!$"

MirrohInterior_1F_Trainer_E_Text_0:
# 218 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I can't get through to Winterlily Hollow\n"
	.string "from this side. It's so frustrating!$"

MirrohInterior_1F_Trainer_E_Text_1:
# 218 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "You're also frustrating!$"

MirrohInterior_1F_Trainer_E_Text_2:
# 219 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I mean why even build a tunnel then?$"

MirrohInterior_1F_NPC_A_Text_0:
# 241 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I'm trekking to Winterlily Hollow! But my\n"
	.string "GRASS type Pokémon can't deal with all\l"
	.string "the ICE type Pokémon around here...$"

MirrohInterior_1F_NPC_B_Text_0:
# 247 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Winterlily Hollow is past the ledge\n"
	.string "above.\n"
	.string "But how do I cross the ledge?$"

MirrohInterior_1F_NPC_C_Text_0:
# 252 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Some dangerous looking people passed\n"
	.string "through here earlier with loads of\l"
	.string "heavy machinery. All that commotion\l"
	.string "caused a bunch of rocks to cave in!$"

MirrohInterior_1F_NPC_D_Text_0:
# 258 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Past this is the trek up to the\n"
	.string "mountain peak. The weather is harsh!$"

MirrohInterior_1F_Pineco_Text_0:
# 269 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Pineco looks cold!$"

MirrohInterior_Bergmite_A_Text_0:
# 283 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "There's nothing here.$"

MirrohInterior_Bergmite_A_Text_1:
# 287 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "{PLAYER} searched the rock...\p"
	.string "...but it wasn't a rock!\n"
	.string "It was a wild Pokémon!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_0:
# 347 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Grunt A$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_1:
# 348 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Did you move all the equipment? The\n"
	.string "boss is gonna be angry - we gotta get\l"
	.string "the Dreamalyser up and running quick!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_2:
# 353 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Grunt B$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_3:
# 354 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Would you relax? I'm not Gabrielle - of\n"
	.string "course I moved everything! Caused some\l"
	.string "cave-ins, but that's not our problem!\p"
	.string "Haha!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_4:
# 364 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey! Didn't your parents tell you it was\n"
	.string "rude to eavesdrop?$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_5:
# 372 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Argh! My Pokémon are so weak!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_6:
# 378 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Argh! Stupid Mime Jr! You're useless!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_7:
# 385 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey - aren't you that lab assistant who\n"
	.string "beat Melea back in Silversun City?$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_8:
# 394 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Yeah - the same one who beat Moxie up\n"
	.string "in Mt. Ceram too!\p"
	.string "The bosses will want to know this.\n"
	.string "Let's go!$"

MirrohInterior_1F_EventScript_Rubble_Text_0:
# 414 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "A small pile of rubble.\pSomething glints faintly between\nthe stones.$"
