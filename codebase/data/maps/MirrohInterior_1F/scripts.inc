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


MirrohInterior_1F_Trainer_A::
# 31 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_A, MirrohInterior_1F_Trainer_A_Text_0, MirrohInterior_1F_Trainer_A_Text_1
# 32 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_A_Text_2
# 33 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_B::
# 38 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_B, MirrohInterior_1F_Trainer_B_Text_0, MirrohInterior_1F_Trainer_B_Text_1
# 39 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_B_Text_2
# 40 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_C::
# 45 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_C, MirrohInterior_1F_Trainer_C_Text_0, MirrohInterior_1F_Trainer_C_Text_1
# 46 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_C_Text_2
# 47 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_Trainer_D::
# 52 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 53 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_0
# 54 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 55 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_ROBBER, MirrohInterior_1F_Trainer_D_Movement_0
# 56 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 57 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 20
# 58 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_1
# 60 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_no_intro TRAINER_MIRROHINT_D, MirrohInterior_1F_Trainer_D_Text_2
# 61 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_D_Text_3
# 62 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 63 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohInterior_1F_Trainer_D_Movement_1
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_ROBBER, MirrohInterior_1F_Trainer_D_Movement_2
# 65 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 66 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_ROBBER
# 68 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_ROBBER
# 69 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_Trainer_E::
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_single TRAINER_MIRROHINT_D, MirrohInterior_1F_Trainer_E_Text_0, MirrohInterior_1F_Trainer_E_Text_1
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Trainer_E_Text_2
# 77 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	return


MirrohInterior_1F_NPC_A::
# 98 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_A_Text_0, MSGBOX_NPC
# 99 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end


MirrohInterior_1F_NPC_B::
# 104 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_B_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_C::
# 109 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_C_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_D::
# 115 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_D_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_NPC_E::
# 121 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_NPC_D_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_Pineco::
# 125 "data/maps/MirrohInterior_1F/scripts.pory"
	playmoncry SPECIES_PINECO, CRY_MODE_NORMAL
# 126 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_Pineco_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_A::
# 139 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_A, MirrohInterior_Bergmite_A_2
# 144 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 145 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_A
# 146 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 147 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_A_2:
# 140 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_B::
# 152 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_B, MirrohInterior_Bergmite_B_2
# 157 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 158 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_B
# 159 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 160 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_B_2:
# 153 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_Bergmite_C::
# 165 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_BERGMITE_C, MirrohInterior_Bergmite_C_2
# 170 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_1
# 171 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_BERGMITE_C
# 172 "data/maps/MirrohInterior_1F/scripts.pory"
	setwildbattle SPECIES_BERGMITE, 28
# 173 "data/maps/MirrohInterior_1F/scripts.pory"
	dowildbattle
	end

MirrohInterior_Bergmite_C_2:
# 166 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_Bergmite_A_Text_0, MSGBOX_NPC
	end


MirrohInterior_1F_SomberGrunts_Trigger::
# 198 "data/maps/MirrohInterior_1F/scripts.pory"
	goto_if_set FLAG_MIRROH_INT_SOMBER_GRUNTS, MirrohInterior_1F_SomberGrunts_Trigger_2
# 200 "data/maps/MirrohInterior_1F/scripts.pory"
	lockall
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_0
# 202 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 203 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 204 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 205 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_1
# 206 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 207 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_1
# 208 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 209 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 210 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_2
# 211 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_3
# 212 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 213 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 215 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 216 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 217 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 218 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 220 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 221 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_4
# 222 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 224 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_3
# 225 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_3
# 226 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 227 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 229 "data/maps/MirrohInterior_1F/scripts.pory"
	trainerbattle_no_intro TRAINER_MIRROHINT_E, MirrohInterior_1F_SomberGrunts_Trigger_Text_5
# 231 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_2
# 232 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 233 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 234 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 235 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_6
# 236 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 237 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 8
# 238 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_4
# 239 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 240 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 241 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_2
# 242 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_7
# 243 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 244 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 24
# 246 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_5
# 247 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_6
# 248 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 249 "data/maps/MirrohInterior_1F/scripts.pory"
	delay 16
# 250 "data/maps/MirrohInterior_1F/scripts.pory"
	speakername MirrohInterior_1F_SomberGrunts_Trigger_Text_0
# 251 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_SomberGrunts_Trigger_Text_8
# 252 "data/maps/MirrohInterior_1F/scripts.pory"
	release
# 255 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_7
# 256 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT2, MirrohInterior_1F_SomberGrunts_Trigger_Movement_7
# 257 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 258 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_GRUNT2
# 259 "data/maps/MirrohInterior_1F/scripts.pory"
	applymovement LOCALID_GRUNT1, MirrohInterior_1F_SomberGrunts_Trigger_Movement_8
# 260 "data/maps/MirrohInterior_1F/scripts.pory"
	waitmovement 0
# 261 "data/maps/MirrohInterior_1F/scripts.pory"
	removeobject LOCALID_GRUNT1
# 263 "data/maps/MirrohInterior_1F/scripts.pory"
	setflag FLAG_MIRROH_INT_SOMBER_GRUNTS
# 265 "data/maps/MirrohInterior_1F/scripts.pory"
	releaseall
	end

MirrohInterior_1F_SomberGrunts_Trigger_2:
	end


MirrohInterior_1F_EventScript_Rubble::
# 271 "data/maps/MirrohInterior_1F/scripts.pory"
	msgbox MirrohInterior_1F_EventScript_Rubble_Text_0
	return


# 55 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_0:
# 55 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_down
# 55 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 63 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_1:
# 63 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 63 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 64 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_Trainer_D_Movement_2:
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 64 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

# 201 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_0:
# 201 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_down
	step_end

# 207 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_1:
# 207 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_up
	step_end

# 215 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_2:
# 215 "data/maps/MirrohInterior_1F/scripts.pory"
	jump_in_place_right
# 215 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
	step_end

# 224 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_3:
# 224 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_right
	step_end

# 238 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_4:
# 238 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_question_mark
	step_end

# 246 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_5:
# 246 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
# 246 "data/maps/MirrohInterior_1F/scripts.pory"
	face_down
	step_end

# 247 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_6:
# 247 "data/maps/MirrohInterior_1F/scripts.pory"
	emote_exclamation_mark
# 247 "data/maps/MirrohInterior_1F/scripts.pory"
	face_up
	step_end

# 255 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_7:
# 255 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 255 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 255 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 255 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_left
# 255 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 255 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
# 255 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

# 259 "data/maps/MirrohInterior_1F/scripts.pory"
MirrohInterior_1F_SomberGrunts_Trigger_Movement_8:
# 259 "data/maps/MirrohInterior_1F/scripts.pory"
	walk_down
	step_end

MirrohInterior_1F_Trainer_A_Text_0:
# 31 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I'm looking for a Bergmite but why I\n"
	.string "can't find any?$"

MirrohInterior_1F_Trainer_A_Text_1:
# 31 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "If I had a Bergmite I would've won!$"

MirrohInterior_1F_Trainer_A_Text_2:
# 32 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Maybe the Bergmite hide in the rocks or\n"
	.string "something...$"

MirrohInterior_1F_Trainer_B_Text_0:
# 38 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Nope! No way! That item's mine!$"

MirrohInterior_1F_Trainer_B_Text_1:
# 38 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Fine, you can have it...$"

MirrohInterior_1F_Trainer_B_Text_2:
# 39 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Travelers often leave rare items inside\n"
	.string "caves and mountains.$"

MirrohInterior_1F_Trainer_C_Text_0:
# 45 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I may switch to ICE type Pokémon after\n"
	.string "seeing the Pokémon here!$"

MirrohInterior_1F_Trainer_C_Text_1:
# 45 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I should just use ROCK types!$"

MirrohInterior_1F_Trainer_C_Text_2:
# 46 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "If you go deeper into the mountain,\n"
	.string "you'll find some rare ICE type Pokémon!$"

MirrohInterior_1F_Trainer_D_Text_0:
# 53 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hehehe - that Chansey in the corner is\n"
	.string "mine! I just need to figure out how to\l"
	.string "clear these rocks out of the way...$"

MirrohInterior_1F_Trainer_D_Text_1:
# 58 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Who're you? Mind your own business, kid.\p"
	.string "...\p"
	.string "You're going to return Chansey to Nurse\n"
	.string "Joy by the entrance?\p"
	.string "Hah! Fat chance. Ever heard about\n"
	.string "finders keepers? Well I'll teach you\l"
	.string "since nobody else did!$"

MirrohInterior_1F_Trainer_D_Text_2:
# 60 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "No! My new Chansey!$"

MirrohInterior_1F_Trainer_D_Text_3:
# 61 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Fine! You can go give that Chansey back\n"
	.string "to Nurse Joy! I'm outta here!$"

MirrohInterior_1F_Trainer_E_Text_0:
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I can't get through to Winterlily Hollow\n"
	.string "from this side. It's so frustrating!$"

MirrohInterior_1F_Trainer_E_Text_1:
# 75 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "You're also frustrating!$"

MirrohInterior_1F_Trainer_E_Text_2:
# 76 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I mean why even build a tunnel then?$"

MirrohInterior_1F_NPC_A_Text_0:
# 98 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "I'm trekking to Winterlily Hollow! But my\n"
	.string "GRASS type Pokémon can't deal with all\l"
	.string "the ICE type Pokémon around here...$"

MirrohInterior_1F_NPC_B_Text_0:
# 104 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Winterlily Hollow is past the ledge\n"
	.string "above.\n"
	.string "But how do I cross the ledge?$"

MirrohInterior_1F_NPC_C_Text_0:
# 109 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Some dangerous looking people passed\n"
	.string "through here earlier with loads of\l"
	.string "heavy machinery. All that commotion\l"
	.string "caused a bunch of rocks to cave in!$"

MirrohInterior_1F_NPC_D_Text_0:
# 115 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Past this is the trek up to the\n"
	.string "mountain peak. The weather is harsh!$"

MirrohInterior_1F_Pineco_Text_0:
# 126 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Pineco looks cold!$"

MirrohInterior_Bergmite_A_Text_0:
# 140 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "There's nothing here.$"

MirrohInterior_Bergmite_A_Text_1:
# 144 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "{PLAYER} searched the rock...\p"
	.string "...but it wasn't a rock!\n"
	.string "It was a wild Pokémon!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_0:
# 204 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Grunt A$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_1:
# 205 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Did you move all the equipment? The\n"
	.string "boss is gonna be angry - we gotta get\l"
	.string "the Dreamalyser up and running quick!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_2:
# 210 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Grunt B$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_3:
# 211 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Would you relax? I'm not Gabrielle - of\n"
	.string "course I moved everything! Caused some\l"
	.string "cave-ins, but that's not our problem!\p"
	.string "Haha!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_4:
# 221 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey! Didn't your parents tell you it was\n"
	.string "rude to eavesdrop?$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_5:
# 229 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Argh! My Pokémon are so weak!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_6:
# 235 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Argh! Stupid Mime Jr! You're useless!$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_7:
# 242 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Hey - aren't you that lab assistant who\n"
	.string "beat Melea back in Silversun City?$"

MirrohInterior_1F_SomberGrunts_Trigger_Text_8:
# 251 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "Yeah - the same one who beat Moxie up\n"
	.string "in Mt. Ceram too!\p"
	.string "The bosses will want to know this.\n"
	.string "Let's go!$"

MirrohInterior_1F_EventScript_Rubble_Text_0:
# 271 "data/maps/MirrohInterior_1F/scripts.pory"
	.string "A small pile of rubble.\pSomething glints faintly between\nthe stones.$"
