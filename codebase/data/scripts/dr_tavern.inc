DR_Tavern_Healer::
# 10 "data/scripts/dr_tavern.pory"
	lock
# 11 "data/scripts/dr_tavern.pory"
	faceplayer
# 12 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Healer_Text_0
# 13 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Healer_Text_1, MSGBOX_YESNO
# 14 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, YES
	goto_if_eq DR_Tavern_Healer_2
# 25 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Healer_Text_4
DR_Tavern_Healer_1:
# 27 "data/scripts/dr_tavern.pory"
	closemessage
# 28 "data/scripts/dr_tavern.pory"
	release
	end

DR_Tavern_Healer_2:
# 15 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Healer_Text_2
# 16 "data/scripts/dr_tavern.pory"
	closemessage
# 17 "data/scripts/dr_tavern.pory"
	fadescreen FADE_TO_BLACK
# 18 "data/scripts/dr_tavern.pory"
	playfanfare MUS_HEAL
# 19 "data/scripts/dr_tavern.pory"
	waitfanfare
# 20 "data/scripts/dr_tavern.pory"
	special HealPlayerParty
# 21 "data/scripts/dr_tavern.pory"
	fadescreen FADE_FROM_BLACK
# 22 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Healer_Text_0
# 23 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Healer_Text_3
	goto DR_Tavern_Healer_1


DR_Tavern_Caretaker::
# 33 "data/scripts/dr_tavern.pory"
	lock
# 34 "data/scripts/dr_tavern.pory"
	faceplayer
# 35 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Caretaker_Text_0
# 36 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Caretaker_Text_1, MSGBOX_YESNO
# 37 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, YES
	goto_if_eq DR_Tavern_Caretaker_2
# 42 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Caretaker_Text_2
# 43 "data/scripts/dr_tavern.pory"
	closemessage
DR_Tavern_Caretaker_1:
# 45 "data/scripts/dr_tavern.pory"
	release
	end

DR_Tavern_Caretaker_2:
# 38 "data/scripts/dr_tavern.pory"
	closemessage
# 39 "data/scripts/dr_tavern.pory"
	special ShowPokemonStorageSystemPC
# 40 "data/scripts/dr_tavern.pory"
	waitstate
	goto DR_Tavern_Caretaker_1


DR_Tavern_Sage::
# 50 "data/scripts/dr_tavern.pory"
	lock
# 51 "data/scripts/dr_tavern.pory"
	faceplayer
# 52 "data/scripts/dr_tavern.pory"
	goto_if_unset FLAG_DR_SAGE_MASK_REMARK, DR_Tavern_Sage_2
DR_Tavern_Sage_1:
# 57 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 58 "data/scripts/dr_tavern.pory"
	message DR_Tavern_Sage_Text_2
# 59 "data/scripts/dr_tavern.pory"
	waitmessage
# 60 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_3, 0
# 61 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_4, 1
# 62 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_5, 2
# 63 "data/scripts/dr_tavern.pory"
	goto_if_set FLAG_BADGE04_GET, DR_Tavern_Sage_5
DR_Tavern_Sage_4:
# 66 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_7, 4
# 67 "data/scripts/dr_tavern.pory"
	dynmultistack 0, 0, FALSE, 5, FALSE, 0, DYN_MULTICHOICE_CB_NONE
# 68 "data/scripts/dr_tavern.pory"
	switch VAR_RESULT
# 69 "data/scripts/dr_tavern.pory"
	case 0, DR_Tavern_Sage_9
# 70 "data/scripts/dr_tavern.pory"
	case 1, DR_Tavern_Sage_10
# 71 "data/scripts/dr_tavern.pory"
	case 2, DR_Tavern_Sage_11
# 72 "data/scripts/dr_tavern.pory"
	case 3, DR_Tavern_Sage_12
DR_Tavern_Sage_7:
# 74 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_2:
# 53 "data/scripts/dr_tavern.pory"
	setflag FLAG_DR_SAGE_MASK_REMARK
# 54 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 55 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Text_1
	goto DR_Tavern_Sage_1

DR_Tavern_Sage_5:
# 64 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_6, 3
	goto DR_Tavern_Sage_4

DR_Tavern_Sage_9:
# 69 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Rename
	goto DR_Tavern_Sage_7

DR_Tavern_Sage_10:
# 70 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Relearn
	goto DR_Tavern_Sage_7

DR_Tavern_Sage_11:
# 71 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Nature
	goto DR_Tavern_Sage_7

DR_Tavern_Sage_12:
# 72 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_ApexFruit
	goto DR_Tavern_Sage_7


DR_Tavern_Sage_Bye::
# 78 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 79 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Bye_Text_0
# 80 "data/scripts/dr_tavern.pory"
	closemessage
# 81 "data/scripts/dr_tavern.pory"
	release
	end


DR_Tavern_Sage_Rename::
# 86 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_0
# 87 "data/scripts/dr_tavern.pory"
	special ChoosePartyMon
# 88 "data/scripts/dr_tavern.pory"
	waitstate
# 89 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq DR_Tavern_Sage_Rename_2
DR_Tavern_Sage_Rename_1:
# 92 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, ScriptGetPartyMonSpecies
# 93 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, SPECIES_EGG
	goto_if_eq DR_Tavern_Sage_Rename_5
DR_Tavern_Sage_Rename_4:
# 98 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 99 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, MonOTNameNotPlayer
# 100 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 101 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, TRUE
	goto_if_eq DR_Tavern_Sage_Rename_8
DR_Tavern_Sage_Rename_7:
# 106 "data/scripts/dr_tavern.pory"
	call Common_EventScript_NameReceivedPartyMon
# 107 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 108 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 109 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_3
# 110 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_Rename_2:
# 90 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Rename_1

DR_Tavern_Sage_Rename_5:
# 94 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 95 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_1
# 96 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Rename_4

DR_Tavern_Sage_Rename_8:
# 102 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 103 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_2
# 104 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Rename_7


DR_Tavern_Sage_Relearn::
# 114 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Relearn_Text_0
# 115 "data/scripts/dr_tavern.pory"
	special ChooseMonForMoveRelearner
# 116 "data/scripts/dr_tavern.pory"
	waitstate
# 117 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq DR_Tavern_Sage_Relearn_2
DR_Tavern_Sage_Relearn_1:
# 120 "data/scripts/dr_tavern.pory"
	special IsSelectedMonEgg
# 121 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, TRUE
	goto_if_eq DR_Tavern_Sage_Relearn_5
DR_Tavern_Sage_Relearn_4:
# 126 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 0
	goto_if_eq DR_Tavern_Sage_Relearn_8
DR_Tavern_Sage_Relearn_7:
# 131 "data/scripts/dr_tavern.pory"
	special TeachMoveRelearnerMove
# 132 "data/scripts/dr_tavern.pory"
	waitstate
# 133 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_Relearn_2:
# 118 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Relearn_1

DR_Tavern_Sage_Relearn_5:
# 122 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 123 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Relearn_Text_1
# 124 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Relearn_4

DR_Tavern_Sage_Relearn_8:
# 127 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 128 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Relearn_Text_2
# 129 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Relearn_7


DR_Tavern_Sage_Nature::
# 137 "data/scripts/dr_tavern.pory"
	showmoneybox 18, 0
# 138 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_0, MSGBOX_YESNO
# 139 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, NO
	goto_if_eq DR_Tavern_Sage_Nature_2
DR_Tavern_Sage_Nature_1:
# 143 "data/scripts/dr_tavern.pory"
	checkmoney 2000
# 144 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, FALSE
	goto_if_eq DR_Tavern_Sage_Nature_5
DR_Tavern_Sage_Nature_4:
# 150 "data/scripts/dr_tavern.pory"
	hidemoneybox
# 151 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_2
# 152 "data/scripts/dr_tavern.pory"
	special ChoosePartyMon
# 153 "data/scripts/dr_tavern.pory"
	waitstate
# 154 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq DR_Tavern_Sage_Nature_8
DR_Tavern_Sage_Nature_7:
# 157 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, ScriptGetPartyMonSpecies
# 158 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, SPECIES_EGG
	goto_if_eq DR_Tavern_Sage_Nature_11
DR_Tavern_Sage_Nature_10:
# 163 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 164 "data/scripts/dr_tavern.pory"
	message DR_Tavern_Sage_Nature_Text_4
# 165 "data/scripts/dr_tavern.pory"
	waitmessage
# 166 "data/scripts/dr_tavern.pory"
	dynmultichoice 0, 0, TRUE, 5, 0, DYN_MULTICHOICE_CB_NONE, DR_Tavern_Sage_Nature_Text_5, DR_Tavern_Sage_Nature_Text_6, DR_Tavern_Sage_Nature_Text_7, DR_Tavern_Sage_Nature_Text_8, DR_Tavern_Sage_Nature_Text_9
# 167 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8005, VAR_RESULT
# 168 "data/scripts/dr_tavern.pory"
	message DR_Tavern_Sage_Nature_Text_10
# 169 "data/scripts/dr_tavern.pory"
	waitmessage
# 170 "data/scripts/dr_tavern.pory"
	dynmultichoice 0, 0, TRUE, 5, 0, DYN_MULTICHOICE_CB_NONE, DR_Tavern_Sage_Nature_Text_5, DR_Tavern_Sage_Nature_Text_6, DR_Tavern_Sage_Nature_Text_7, DR_Tavern_Sage_Nature_Text_8, DR_Tavern_Sage_Nature_Text_9
# 171 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_RESULT
# 172 "data/scripts/dr_tavern.pory"
	special DrTavernSetNature
# 173 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, FALSE
	goto_if_eq DR_Tavern_Sage_Nature_14
DR_Tavern_Sage_Nature_13:
# 177 "data/scripts/dr_tavern.pory"
	removemoney 2000
# 178 "data/scripts/dr_tavern.pory"
	playse SE_SHOP
# 179 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_12
# 180 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_Nature_2:
# 140 "data/scripts/dr_tavern.pory"
	hidemoneybox
# 141 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_1

DR_Tavern_Sage_Nature_5:
# 145 "data/scripts/dr_tavern.pory"
	hidemoneybox
# 146 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 147 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_1
# 148 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_4

DR_Tavern_Sage_Nature_8:
# 155 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_7

DR_Tavern_Sage_Nature_11:
# 159 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 160 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_3
# 161 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_10

DR_Tavern_Sage_Nature_14:
# 174 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_11
# 175 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_13


DR_Tavern_Sage_ApexFruit::
# 184 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_ApexFruit_Text_0
# 185 "data/scripts/dr_tavern.pory"
	pokemart DR_Tavern_ApexStock
# 186 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return


	.align 2
# 189 "data/scripts/dr_tavern.pory"
DR_Tavern_ApexStock:
# 190 "data/scripts/dr_tavern.pory"
	.2byte ITEM_APEX_FRUIT
	.2byte ITEM_NONE

EventScript_DrUseApexFruit::
# 195 "data/scripts/dr_tavern.pory"
	lockall
# 196 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_0
# 197 "data/scripts/dr_tavern.pory"
	special ChoosePartyMon
# 198 "data/scripts/dr_tavern.pory"
	waitstate
# 199 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq EventScript_DrUseApexFruit_2
# 203 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, ScriptGetPartyMonSpecies
# 204 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, SPECIES_EGG
	goto_if_eq EventScript_DrUseApexFruit_5
# 209 "data/scripts/dr_tavern.pory"
	special DrTavernBufferAbilityChoices
# 210 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 0
	goto_if_eq EventScript_DrUseApexFruit_8
# 215 "data/scripts/dr_tavern.pory"
	message EventScript_DrUseApexFruit_Text_3
# 216 "data/scripts/dr_tavern.pory"
	waitmessage
# 217 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_4, 0
# 218 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 2
	goto_if_ge EventScript_DrUseApexFruit_11
EventScript_DrUseApexFruit_10:
# 221 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 3
	goto_if_ge EventScript_DrUseApexFruit_14
EventScript_DrUseApexFruit_13:
# 224 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_7, 3
# 225 "data/scripts/dr_tavern.pory"
	dynmultistack 0, 0, FALSE, 4, FALSE, 0, DYN_MULTICHOICE_CB_NONE
# 226 "data/scripts/dr_tavern.pory"
	switch VAR_RESULT
# 227 "data/scripts/dr_tavern.pory"
	case 0, EventScript_DrUseApexFruit_18
# 228 "data/scripts/dr_tavern.pory"
	case 1, EventScript_DrUseApexFruit_19
# 229 "data/scripts/dr_tavern.pory"
	case 2, EventScript_DrUseApexFruit_20
# 231 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_2:
# 200 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_5:
# 205 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_1
# 206 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_8:
# 211 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_2
# 212 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_11:
# 219 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_5, 1
	goto EventScript_DrUseApexFruit_10

EventScript_DrUseApexFruit_14:
# 222 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_6, 2
	goto EventScript_DrUseApexFruit_13

EventScript_DrUseApexFruit_16:
# 234 "data/scripts/dr_tavern.pory"
	special DrTavernSetAbilitySlot
# 235 "data/scripts/dr_tavern.pory"
	removeitem ITEM_APEX_FRUIT
# 236 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 237 "data/scripts/dr_tavern.pory"
	playse SE_USE_ITEM
# 238 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_8
# 239 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_18:
# 227 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_0x8007
	goto EventScript_DrUseApexFruit_16

EventScript_DrUseApexFruit_19:
# 228 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_0x8008
	goto EventScript_DrUseApexFruit_16

EventScript_DrUseApexFruit_20:
# 229 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_0x8009
	goto EventScript_DrUseApexFruit_16


DR_Tavern_Healer_Text_0:
# 12 "data/scripts/dr_tavern.pory"
	.string "Innkeeper$"

DR_Tavern_Healer_Text_1:
# 13 "data/scripts/dr_tavern.pory"
	.string "Welcome in, traveller! A hot meal, a cool\n"
	.string "cup, and your Pokémon set to rights.\l"
	.string "Shall I bring something out for them?$"

DR_Tavern_Healer_Text_2:
# 15 "data/scripts/dr_tavern.pory"
	.string "Right away.$"

DR_Tavern_Healer_Text_3:
# 23 "data/scripts/dr_tavern.pory"
	.string "Fed, watered and rested. The Templars\n"
	.string "keep this hearth for any trainer on the\l"
	.string "road.$"

DR_Tavern_Healer_Text_4:
# 25 "data/scripts/dr_tavern.pory"
	.string "As you like. The kitchen fire never goes\n"
	.string "out.$"

DR_Tavern_Caretaker_Text_0:
# 35 "data/scripts/dr_tavern.pory"
	.string "Caretaker$"

DR_Tavern_Caretaker_Text_1:
# 36 "data/scripts/dr_tavern.pory"
	.string "I tend the Pokémon a traveller can't\n"
	.string "carry on the road. Shall I fetch yours?$"

DR_Tavern_Caretaker_Text_2:
# 42 "data/scripts/dr_tavern.pory"
	.string "They're in good hands either way.$"

DR_Tavern_Sage_Text_0:
# 54 "data/scripts/dr_tavern.pory"
	.string "Sage$"

DR_Tavern_Sage_Text_1:
# 55 "data/scripts/dr_tavern.pory"
	.string "That mask is Athanto work. There'll be\n"
	.string "no more of them now.\p"
	.string "Two years past, the guardian of that\n"
	.string "land came down from its mountain and\l"
	.string "left neither king nor lord alive.$"

DR_Tavern_Sage_Text_2:
# 58 "data/scripts/dr_tavern.pory"
	.string "A new name, a forgotten art, a change of\n"
	.string "temper... What would you have of me?$"

DR_Tavern_Sage_Text_3:
# 60 "data/scripts/dr_tavern.pory"
	.string "A new name$"

DR_Tavern_Sage_Text_4:
# 61 "data/scripts/dr_tavern.pory"
	.string "Relearn a move$"

DR_Tavern_Sage_Text_5:
# 62 "data/scripts/dr_tavern.pory"
	.string "Change a nature$"

DR_Tavern_Sage_Text_6:
# 64 "data/scripts/dr_tavern.pory"
	.string "Apex Fruit$"

DR_Tavern_Sage_Text_7:
# 66 "data/scripts/dr_tavern.pory"
	.string "Nothing$"

DR_Tavern_Sage_Bye_Text_0:
# 79 "data/scripts/dr_tavern.pory"
	.string "Come again whenever you've need.$"

DR_Tavern_Sage_Rename_Text_0:
# 86 "data/scripts/dr_tavern.pory"
	.string "Whose name shall we change?$"

DR_Tavern_Sage_Rename_Text_1:
# 95 "data/scripts/dr_tavern.pory"
	.string "That's an Egg. Let it hatch first, then\n"
	.string "we'll talk names.$"

DR_Tavern_Sage_Rename_Text_2:
# 103 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1} was named by the one\n"
	.string "who raised it. That name isn't mine to\l"
	.string "change.$"

DR_Tavern_Sage_Rename_Text_3:
# 109 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1}. A good name.$"

DR_Tavern_Sage_Relearn_Text_0:
# 114 "data/scripts/dr_tavern.pory"
	.string "Which Pokémon wants to remember?$"

DR_Tavern_Sage_Relearn_Text_1:
# 123 "data/scripts/dr_tavern.pory"
	.string "An Egg has nothing to remember yet.$"

DR_Tavern_Sage_Relearn_Text_2:
# 128 "data/scripts/dr_tavern.pory"
	.string "There's nothing that one has\n"
	.string "forgotten.$"

DR_Tavern_Sage_Nature_Text_0:
# 138 "data/scripts/dr_tavern.pory"
	.string "Changing a Pokémon's temper takes time\n"
	.string "and a good deal of patience. It costs\l"
	.string "¥2,000. Shall we?$"

DR_Tavern_Sage_Nature_Text_1:
# 147 "data/scripts/dr_tavern.pory"
	.string "You'll need ¥2,000 for that.$"

DR_Tavern_Sage_Nature_Text_2:
# 151 "data/scripts/dr_tavern.pory"
	.string "Whose nature shall we change?$"

DR_Tavern_Sage_Nature_Text_3:
# 160 "data/scripts/dr_tavern.pory"
	.string "Let the Egg hatch first.$"

DR_Tavern_Sage_Nature_Text_4:
# 164 "data/scripts/dr_tavern.pory"
	.string "Which side of it should grow stronger?$"

DR_Tavern_Sage_Nature_Text_5:
# 166 "data/scripts/dr_tavern.pory"
	.string "Attack$"

DR_Tavern_Sage_Nature_Text_6:
# 166 "data/scripts/dr_tavern.pory"
	.string "Defense$"

DR_Tavern_Sage_Nature_Text_7:
# 166 "data/scripts/dr_tavern.pory"
	.string "Sp. Atk$"

DR_Tavern_Sage_Nature_Text_8:
# 166 "data/scripts/dr_tavern.pory"
	.string "Sp. Def$"

DR_Tavern_Sage_Nature_Text_9:
# 166 "data/scripts/dr_tavern.pory"
	.string "Speed$"

DR_Tavern_Sage_Nature_Text_10:
# 168 "data/scripts/dr_tavern.pory"
	.string "And which should give a little? Choose\n"
	.string "the same one for a balanced temper.$"

DR_Tavern_Sage_Nature_Text_11:
# 174 "data/scripts/dr_tavern.pory"
	.string "It already has a {STR_VAR_2} nature.\n"
	.string "Keep your money.$"

DR_Tavern_Sage_Nature_Text_12:
# 179 "data/scripts/dr_tavern.pory"
	.string "There. Its nature is {STR_VAR_2}\n"
	.string "now.$"

DR_Tavern_Sage_ApexFruit_Text_0:
# 184 "data/scripts/dr_tavern.pory"
	.string "Apex Fruit. Feed one to a Pokémon and it\n"
	.string "draws out a different ability. Rare, and\l"
	.string "priced like it.$"

EventScript_DrUseApexFruit_Text_0:
# 196 "data/scripts/dr_tavern.pory"
	.string "Which Pokémon will eat the Apex Fruit?$"

EventScript_DrUseApexFruit_Text_1:
# 205 "data/scripts/dr_tavern.pory"
	.string "An Egg can't eat.$"

EventScript_DrUseApexFruit_Text_2:
# 211 "data/scripts/dr_tavern.pory"
	.string "It has no other ability to draw out.$"

EventScript_DrUseApexFruit_Text_3:
# 215 "data/scripts/dr_tavern.pory"
	.string "Which ability should it draw out?$"

EventScript_DrUseApexFruit_Text_4:
# 217 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1}$"

EventScript_DrUseApexFruit_Text_5:
# 219 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_2}$"

EventScript_DrUseApexFruit_Text_6:
# 222 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_3}$"

EventScript_DrUseApexFruit_Text_7:
# 224 "data/scripts/dr_tavern.pory"
	.string "Cancel$"

EventScript_DrUseApexFruit_Text_8:
# 238 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1}'s ability is now\n"
	.string "{STR_VAR_2}!$"
