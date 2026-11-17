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
	speakername DR_Tavern_Sage_Text_0
# 53 "data/scripts/dr_tavern.pory"
	message DR_Tavern_Sage_Text_1
# 54 "data/scripts/dr_tavern.pory"
	waitmessage
# 55 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_2, 0
# 56 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_3, 1
# 57 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_4, 2
# 58 "data/scripts/dr_tavern.pory"
	goto_if_set FLAG_BADGE04_GET, DR_Tavern_Sage_2
DR_Tavern_Sage_1:
# 61 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_6, 4
# 62 "data/scripts/dr_tavern.pory"
	dynmultistack 0, 0, FALSE, 5, FALSE, 0, DYN_MULTICHOICE_CB_NONE
# 63 "data/scripts/dr_tavern.pory"
	switch VAR_RESULT
# 64 "data/scripts/dr_tavern.pory"
	case 0, DR_Tavern_Sage_6
# 65 "data/scripts/dr_tavern.pory"
	case 1, DR_Tavern_Sage_7
# 66 "data/scripts/dr_tavern.pory"
	case 2, DR_Tavern_Sage_8
# 67 "data/scripts/dr_tavern.pory"
	case 3, DR_Tavern_Sage_9
DR_Tavern_Sage_4:
# 69 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_2:
# 59 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_5, 3
	goto DR_Tavern_Sage_1

DR_Tavern_Sage_6:
# 64 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Rename
	goto DR_Tavern_Sage_4

DR_Tavern_Sage_7:
# 65 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Relearn
	goto DR_Tavern_Sage_4

DR_Tavern_Sage_8:
# 66 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Nature
	goto DR_Tavern_Sage_4

DR_Tavern_Sage_9:
# 67 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_ApexFruit
	goto DR_Tavern_Sage_4


DR_Tavern_Sage_Bye::
# 73 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 74 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Bye_Text_0
# 75 "data/scripts/dr_tavern.pory"
	closemessage
# 76 "data/scripts/dr_tavern.pory"
	release
	end


DR_Tavern_Sage_Rename::
# 81 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_0
# 82 "data/scripts/dr_tavern.pory"
	special ChoosePartyMon
# 83 "data/scripts/dr_tavern.pory"
	waitstate
# 84 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq DR_Tavern_Sage_Rename_2
DR_Tavern_Sage_Rename_1:
# 87 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, ScriptGetPartyMonSpecies
# 88 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, SPECIES_EGG
	goto_if_eq DR_Tavern_Sage_Rename_5
DR_Tavern_Sage_Rename_4:
# 93 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 94 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, MonOTNameNotPlayer
# 95 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 96 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, TRUE
	goto_if_eq DR_Tavern_Sage_Rename_8
DR_Tavern_Sage_Rename_7:
# 101 "data/scripts/dr_tavern.pory"
	call Common_EventScript_NameReceivedPartyMon
# 102 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 103 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 104 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_3
# 105 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_Rename_2:
# 85 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Rename_1

DR_Tavern_Sage_Rename_5:
# 89 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 90 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_1
# 91 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Rename_4

DR_Tavern_Sage_Rename_8:
# 97 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 98 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_2
# 99 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Rename_7


DR_Tavern_Sage_Relearn::
# 109 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Relearn_Text_0
# 110 "data/scripts/dr_tavern.pory"
	special ChooseMonForMoveRelearner
# 111 "data/scripts/dr_tavern.pory"
	waitstate
# 112 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq DR_Tavern_Sage_Relearn_2
DR_Tavern_Sage_Relearn_1:
# 115 "data/scripts/dr_tavern.pory"
	special IsSelectedMonEgg
# 116 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, TRUE
	goto_if_eq DR_Tavern_Sage_Relearn_5
DR_Tavern_Sage_Relearn_4:
# 121 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 0
	goto_if_eq DR_Tavern_Sage_Relearn_8
DR_Tavern_Sage_Relearn_7:
# 126 "data/scripts/dr_tavern.pory"
	special TeachMoveRelearnerMove
# 127 "data/scripts/dr_tavern.pory"
	waitstate
# 128 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_Relearn_2:
# 113 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Relearn_1

DR_Tavern_Sage_Relearn_5:
# 117 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 118 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Relearn_Text_1
# 119 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Relearn_4

DR_Tavern_Sage_Relearn_8:
# 122 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 123 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Relearn_Text_2
# 124 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Relearn_7


DR_Tavern_Sage_Nature::
# 132 "data/scripts/dr_tavern.pory"
	showmoneybox 18, 0
# 133 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_0, MSGBOX_YESNO
# 134 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, NO
	goto_if_eq DR_Tavern_Sage_Nature_2
DR_Tavern_Sage_Nature_1:
# 138 "data/scripts/dr_tavern.pory"
	checkmoney 2000
# 139 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, FALSE
	goto_if_eq DR_Tavern_Sage_Nature_5
DR_Tavern_Sage_Nature_4:
# 145 "data/scripts/dr_tavern.pory"
	hidemoneybox
# 146 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_2
# 147 "data/scripts/dr_tavern.pory"
	special ChoosePartyMon
# 148 "data/scripts/dr_tavern.pory"
	waitstate
# 149 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq DR_Tavern_Sage_Nature_8
DR_Tavern_Sage_Nature_7:
# 152 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, ScriptGetPartyMonSpecies
# 153 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, SPECIES_EGG
	goto_if_eq DR_Tavern_Sage_Nature_11
DR_Tavern_Sage_Nature_10:
# 158 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 159 "data/scripts/dr_tavern.pory"
	message DR_Tavern_Sage_Nature_Text_4
# 160 "data/scripts/dr_tavern.pory"
	waitmessage
# 161 "data/scripts/dr_tavern.pory"
	dynmultichoice 0, 0, TRUE, 5, 0, DYN_MULTICHOICE_CB_NONE, DR_Tavern_Sage_Nature_Text_5, DR_Tavern_Sage_Nature_Text_6, DR_Tavern_Sage_Nature_Text_7, DR_Tavern_Sage_Nature_Text_8, DR_Tavern_Sage_Nature_Text_9
# 162 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8005, VAR_RESULT
# 163 "data/scripts/dr_tavern.pory"
	message DR_Tavern_Sage_Nature_Text_10
# 164 "data/scripts/dr_tavern.pory"
	waitmessage
# 165 "data/scripts/dr_tavern.pory"
	dynmultichoice 0, 0, TRUE, 5, 0, DYN_MULTICHOICE_CB_NONE, DR_Tavern_Sage_Nature_Text_5, DR_Tavern_Sage_Nature_Text_6, DR_Tavern_Sage_Nature_Text_7, DR_Tavern_Sage_Nature_Text_8, DR_Tavern_Sage_Nature_Text_9
# 166 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_RESULT
# 167 "data/scripts/dr_tavern.pory"
	special DrTavernSetNature
# 168 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, FALSE
	goto_if_eq DR_Tavern_Sage_Nature_14
DR_Tavern_Sage_Nature_13:
# 172 "data/scripts/dr_tavern.pory"
	removemoney 2000
# 173 "data/scripts/dr_tavern.pory"
	playse SE_SHOP
# 174 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_12
# 175 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_Nature_2:
# 135 "data/scripts/dr_tavern.pory"
	hidemoneybox
# 136 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_1

DR_Tavern_Sage_Nature_5:
# 140 "data/scripts/dr_tavern.pory"
	hidemoneybox
# 141 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 142 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_1
# 143 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_4

DR_Tavern_Sage_Nature_8:
# 150 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_7

DR_Tavern_Sage_Nature_11:
# 154 "data/scripts/dr_tavern.pory"
	speakername DR_Tavern_Sage_Text_0
# 155 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_3
# 156 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_10

DR_Tavern_Sage_Nature_14:
# 169 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_11
# 170 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_13


DR_Tavern_Sage_ApexFruit::
# 179 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_ApexFruit_Text_0
# 180 "data/scripts/dr_tavern.pory"
	pokemart DR_Tavern_ApexStock
# 181 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return


	.align 2
# 184 "data/scripts/dr_tavern.pory"
DR_Tavern_ApexStock:
# 185 "data/scripts/dr_tavern.pory"
	.2byte ITEM_APEX_FRUIT
	.2byte ITEM_NONE

EventScript_DrUseApexFruit::
# 190 "data/scripts/dr_tavern.pory"
	lockall
# 191 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_0
# 192 "data/scripts/dr_tavern.pory"
	special ChoosePartyMon
# 193 "data/scripts/dr_tavern.pory"
	waitstate
# 194 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq EventScript_DrUseApexFruit_2
# 198 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, ScriptGetPartyMonSpecies
# 199 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, SPECIES_EGG
	goto_if_eq EventScript_DrUseApexFruit_5
# 204 "data/scripts/dr_tavern.pory"
	special DrTavernBufferAbilityChoices
# 205 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 0
	goto_if_eq EventScript_DrUseApexFruit_8
# 210 "data/scripts/dr_tavern.pory"
	message EventScript_DrUseApexFruit_Text_3
# 211 "data/scripts/dr_tavern.pory"
	waitmessage
# 212 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_4, 0
# 213 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 2
	goto_if_ge EventScript_DrUseApexFruit_11
EventScript_DrUseApexFruit_10:
# 216 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 3
	goto_if_ge EventScript_DrUseApexFruit_14
EventScript_DrUseApexFruit_13:
# 219 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_7, 3
# 220 "data/scripts/dr_tavern.pory"
	dynmultistack 0, 0, FALSE, 4, FALSE, 0, DYN_MULTICHOICE_CB_NONE
# 221 "data/scripts/dr_tavern.pory"
	switch VAR_RESULT
# 222 "data/scripts/dr_tavern.pory"
	case 0, EventScript_DrUseApexFruit_18
# 223 "data/scripts/dr_tavern.pory"
	case 1, EventScript_DrUseApexFruit_19
# 224 "data/scripts/dr_tavern.pory"
	case 2, EventScript_DrUseApexFruit_20
# 226 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_2:
# 195 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_5:
# 200 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_1
# 201 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_8:
# 206 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_2
# 207 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_11:
# 214 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_5, 1
	goto EventScript_DrUseApexFruit_10

EventScript_DrUseApexFruit_14:
# 217 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_6, 2
	goto EventScript_DrUseApexFruit_13

EventScript_DrUseApexFruit_16:
# 229 "data/scripts/dr_tavern.pory"
	special DrTavernSetAbilitySlot
# 230 "data/scripts/dr_tavern.pory"
	removeitem ITEM_APEX_FRUIT
# 231 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 232 "data/scripts/dr_tavern.pory"
	playse SE_USE_ITEM
# 233 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_8
# 234 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_18:
# 222 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_0x8007
	goto EventScript_DrUseApexFruit_16

EventScript_DrUseApexFruit_19:
# 223 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_0x8008
	goto EventScript_DrUseApexFruit_16

EventScript_DrUseApexFruit_20:
# 224 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_0x8009
	goto EventScript_DrUseApexFruit_16


DR_Tavern_Healer_Text_0:
# 12 "data/scripts/dr_tavern.pory"
	.string "Innkeeper$"

DR_Tavern_Healer_Text_1:
# 13 "data/scripts/dr_tavern.pory"
	.string "Welcome! A hot meal and a cool drink, and\n"
	.string "your Pokémon will be good as new. Shall I\l"
	.string "bring something out for them?$"

DR_Tavern_Healer_Text_2:
# 15 "data/scripts/dr_tavern.pory"
	.string "Coming right up.$"

DR_Tavern_Healer_Text_3:
# 23 "data/scripts/dr_tavern.pory"
	.string "Fed, watered and rested. Come back\n"
	.string "anytime.$"

DR_Tavern_Healer_Text_4:
# 25 "data/scripts/dr_tavern.pory"
	.string "Suit yourself. The kitchen is always\n"
	.string "open.$"

DR_Tavern_Caretaker_Text_0:
# 35 "data/scripts/dr_tavern.pory"
	.string "Caretaker$"

DR_Tavern_Caretaker_Text_1:
# 36 "data/scripts/dr_tavern.pory"
	.string "I look after the Pokémon you can't\n"
	.string "carry with you. Want to see them?$"

DR_Tavern_Caretaker_Text_2:
# 42 "data/scripts/dr_tavern.pory"
	.string "They're in good hands either way.$"

DR_Tavern_Sage_Text_0:
# 52 "data/scripts/dr_tavern.pory"
	.string "Sage$"

DR_Tavern_Sage_Text_1:
# 53 "data/scripts/dr_tavern.pory"
	.string "A new name, a forgotten move, a change\n"
	.string "of temper... What can I do for you?$"

DR_Tavern_Sage_Text_2:
# 55 "data/scripts/dr_tavern.pory"
	.string "A new name$"

DR_Tavern_Sage_Text_3:
# 56 "data/scripts/dr_tavern.pory"
	.string "Relearn a move$"

DR_Tavern_Sage_Text_4:
# 57 "data/scripts/dr_tavern.pory"
	.string "Change a nature$"

DR_Tavern_Sage_Text_5:
# 59 "data/scripts/dr_tavern.pory"
	.string "Apex Fruit$"

DR_Tavern_Sage_Text_6:
# 61 "data/scripts/dr_tavern.pory"
	.string "Nothing$"

DR_Tavern_Sage_Bye_Text_0:
# 74 "data/scripts/dr_tavern.pory"
	.string "Come back whenever you like.$"

DR_Tavern_Sage_Rename_Text_0:
# 81 "data/scripts/dr_tavern.pory"
	.string "Whose name shall we change?$"

DR_Tavern_Sage_Rename_Text_1:
# 90 "data/scripts/dr_tavern.pory"
	.string "That's an Egg. Let it hatch first, then\n"
	.string "we'll talk names.$"

DR_Tavern_Sage_Rename_Text_2:
# 98 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1} was named by the one\n"
	.string "who raised it. That name isn't mine to\l"
	.string "change.$"

DR_Tavern_Sage_Rename_Text_3:
# 104 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1}. A good name.$"

DR_Tavern_Sage_Relearn_Text_0:
# 109 "data/scripts/dr_tavern.pory"
	.string "Which Pokémon wants to remember?$"

DR_Tavern_Sage_Relearn_Text_1:
# 118 "data/scripts/dr_tavern.pory"
	.string "An Egg has nothing to remember yet.$"

DR_Tavern_Sage_Relearn_Text_2:
# 123 "data/scripts/dr_tavern.pory"
	.string "There's nothing that one has\n"
	.string "forgotten.$"

DR_Tavern_Sage_Nature_Text_0:
# 133 "data/scripts/dr_tavern.pory"
	.string "Changing a Pokémon's temper takes time\n"
	.string "and a good deal of patience. It costs\l"
	.string "¥2,000. Shall we?$"

DR_Tavern_Sage_Nature_Text_1:
# 142 "data/scripts/dr_tavern.pory"
	.string "You'll need ¥2,000 for that.$"

DR_Tavern_Sage_Nature_Text_2:
# 146 "data/scripts/dr_tavern.pory"
	.string "Whose nature shall we change?$"

DR_Tavern_Sage_Nature_Text_3:
# 155 "data/scripts/dr_tavern.pory"
	.string "Let the Egg hatch first.$"

DR_Tavern_Sage_Nature_Text_4:
# 159 "data/scripts/dr_tavern.pory"
	.string "Which side of it should grow stronger?$"

DR_Tavern_Sage_Nature_Text_5:
# 161 "data/scripts/dr_tavern.pory"
	.string "Attack$"

DR_Tavern_Sage_Nature_Text_6:
# 161 "data/scripts/dr_tavern.pory"
	.string "Defense$"

DR_Tavern_Sage_Nature_Text_7:
# 161 "data/scripts/dr_tavern.pory"
	.string "Sp. Atk$"

DR_Tavern_Sage_Nature_Text_8:
# 161 "data/scripts/dr_tavern.pory"
	.string "Sp. Def$"

DR_Tavern_Sage_Nature_Text_9:
# 161 "data/scripts/dr_tavern.pory"
	.string "Speed$"

DR_Tavern_Sage_Nature_Text_10:
# 163 "data/scripts/dr_tavern.pory"
	.string "And which should give a little? Choose\n"
	.string "the same one for a balanced temper.$"

DR_Tavern_Sage_Nature_Text_11:
# 169 "data/scripts/dr_tavern.pory"
	.string "It already has a {STR_VAR_2} nature.\n"
	.string "Keep your money.$"

DR_Tavern_Sage_Nature_Text_12:
# 174 "data/scripts/dr_tavern.pory"
	.string "There. Its nature is {STR_VAR_2}\n"
	.string "now.$"

DR_Tavern_Sage_ApexFruit_Text_0:
# 179 "data/scripts/dr_tavern.pory"
	.string "Apex Fruit. Feed one to a Pokémon and it\n"
	.string "draws out a different ability. Rare, and\l"
	.string "priced like it.$"

EventScript_DrUseApexFruit_Text_0:
# 191 "data/scripts/dr_tavern.pory"
	.string "Which Pokémon will eat the Apex Fruit?$"

EventScript_DrUseApexFruit_Text_1:
# 200 "data/scripts/dr_tavern.pory"
	.string "An Egg can't eat.$"

EventScript_DrUseApexFruit_Text_2:
# 206 "data/scripts/dr_tavern.pory"
	.string "It has no other ability to draw out.$"

EventScript_DrUseApexFruit_Text_3:
# 210 "data/scripts/dr_tavern.pory"
	.string "Which ability should it draw out?$"

EventScript_DrUseApexFruit_Text_4:
# 212 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1}$"

EventScript_DrUseApexFruit_Text_5:
# 214 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_2}$"

EventScript_DrUseApexFruit_Text_6:
# 217 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_3}$"

EventScript_DrUseApexFruit_Text_7:
# 219 "data/scripts/dr_tavern.pory"
	.string "Cancel$"

EventScript_DrUseApexFruit_Text_8:
# 233 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1}'s ability is now\n"
	.string "{STR_VAR_2}!$"
