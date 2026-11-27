DR_Tavern_Healer::
# 10 "data/scripts/dr_tavern.pory"
	lock
# 11 "data/scripts/dr_tavern.pory"
	faceplayer
# 12 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Healer_Text_0, MSGBOX_YESNO
# 13 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, YES
	goto_if_eq DR_Tavern_Healer_2
# 23 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Healer_Text_3
DR_Tavern_Healer_1:
# 25 "data/scripts/dr_tavern.pory"
	closemessage
# 26 "data/scripts/dr_tavern.pory"
	release
	end

DR_Tavern_Healer_2:
# 14 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Healer_Text_1
# 15 "data/scripts/dr_tavern.pory"
	closemessage
# 16 "data/scripts/dr_tavern.pory"
	fadescreen FADE_TO_BLACK
# 17 "data/scripts/dr_tavern.pory"
	playfanfare MUS_HEAL
# 18 "data/scripts/dr_tavern.pory"
	waitfanfare
# 19 "data/scripts/dr_tavern.pory"
	special HealPlayerParty
# 20 "data/scripts/dr_tavern.pory"
	fadescreen FADE_FROM_BLACK
# 21 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Healer_Text_2
	goto DR_Tavern_Healer_1


DR_Tavern_Caretaker::
# 31 "data/scripts/dr_tavern.pory"
	lock
# 32 "data/scripts/dr_tavern.pory"
	faceplayer
# 33 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Caretaker_Text_0, MSGBOX_YESNO
# 34 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, YES
	goto_if_eq DR_Tavern_Caretaker_2
# 39 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Caretaker_Text_1
# 40 "data/scripts/dr_tavern.pory"
	closemessage
DR_Tavern_Caretaker_1:
# 42 "data/scripts/dr_tavern.pory"
	release
	end

DR_Tavern_Caretaker_2:
# 35 "data/scripts/dr_tavern.pory"
	closemessage
# 36 "data/scripts/dr_tavern.pory"
	special ShowPokemonStorageSystemPC
# 37 "data/scripts/dr_tavern.pory"
	waitstate
	goto DR_Tavern_Caretaker_1


DR_Tavern_Sage::
# 47 "data/scripts/dr_tavern.pory"
	lock
# 48 "data/scripts/dr_tavern.pory"
	faceplayer
# 49 "data/scripts/dr_tavern.pory"
	goto_if_unset FLAG_DR_SAGE_MASK_REMARK, DR_Tavern_Sage_2
DR_Tavern_Sage_1:
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
	goto_if_set FLAG_BADGE04_GET, DR_Tavern_Sage_5
DR_Tavern_Sage_4:
# 61 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_6, 4
# 62 "data/scripts/dr_tavern.pory"
	dynmultistack 0, 0, FALSE, 5, FALSE, 0, DYN_MULTICHOICE_CB_NONE
# 63 "data/scripts/dr_tavern.pory"
	switch VAR_RESULT
# 64 "data/scripts/dr_tavern.pory"
	case 0, DR_Tavern_Sage_9
# 65 "data/scripts/dr_tavern.pory"
	case 1, DR_Tavern_Sage_10
# 66 "data/scripts/dr_tavern.pory"
	case 2, DR_Tavern_Sage_11
# 67 "data/scripts/dr_tavern.pory"
	case 3, DR_Tavern_Sage_12
DR_Tavern_Sage_7:
# 69 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_2:
# 50 "data/scripts/dr_tavern.pory"
	setflag FLAG_DR_SAGE_MASK_REMARK
# 51 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Text_0
	goto DR_Tavern_Sage_1

DR_Tavern_Sage_5:
# 59 "data/scripts/dr_tavern.pory"
	dynmultipush DR_Tavern_Sage_Text_5, 3
	goto DR_Tavern_Sage_4

DR_Tavern_Sage_9:
# 64 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Rename
	goto DR_Tavern_Sage_7

DR_Tavern_Sage_10:
# 65 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Relearn
	goto DR_Tavern_Sage_7

DR_Tavern_Sage_11:
# 66 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Nature
	goto DR_Tavern_Sage_7

DR_Tavern_Sage_12:
# 67 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_ApexFruit
	goto DR_Tavern_Sage_7


DR_Tavern_Sage_Bye::
# 73 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Bye_Text_0
# 74 "data/scripts/dr_tavern.pory"
	closemessage
# 75 "data/scripts/dr_tavern.pory"
	release
	end


DR_Tavern_Sage_Rename::
# 80 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_0
# 81 "data/scripts/dr_tavern.pory"
	special ChoosePartyMon
# 82 "data/scripts/dr_tavern.pory"
	waitstate
# 83 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq DR_Tavern_Sage_Rename_2
DR_Tavern_Sage_Rename_1:
# 86 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, ScriptGetPartyMonSpecies
# 87 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, SPECIES_EGG
	goto_if_eq DR_Tavern_Sage_Rename_5
DR_Tavern_Sage_Rename_4:
# 91 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 92 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, MonOTNameNotPlayer
# 93 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 94 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, TRUE
	goto_if_eq DR_Tavern_Sage_Rename_8
DR_Tavern_Sage_Rename_7:
# 98 "data/scripts/dr_tavern.pory"
	call Common_EventScript_NameReceivedPartyMon
# 99 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 100 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_3
# 101 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_Rename_2:
# 84 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Rename_1

DR_Tavern_Sage_Rename_5:
# 88 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_1
# 89 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Rename_4

DR_Tavern_Sage_Rename_8:
# 95 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Rename_Text_2
# 96 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Rename_7


DR_Tavern_Sage_Relearn::
# 105 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Relearn_Text_0
# 106 "data/scripts/dr_tavern.pory"
	special ChooseMonForMoveRelearner
# 107 "data/scripts/dr_tavern.pory"
	waitstate
# 108 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq DR_Tavern_Sage_Relearn_2
DR_Tavern_Sage_Relearn_1:
# 111 "data/scripts/dr_tavern.pory"
	special IsSelectedMonEgg
# 112 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, TRUE
	goto_if_eq DR_Tavern_Sage_Relearn_5
DR_Tavern_Sage_Relearn_4:
# 116 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 0
	goto_if_eq DR_Tavern_Sage_Relearn_8
DR_Tavern_Sage_Relearn_7:
# 120 "data/scripts/dr_tavern.pory"
	special TeachMoveRelearnerMove
# 121 "data/scripts/dr_tavern.pory"
	waitstate
# 122 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_Relearn_2:
# 109 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Relearn_1

DR_Tavern_Sage_Relearn_5:
# 113 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Relearn_Text_1
# 114 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Relearn_4

DR_Tavern_Sage_Relearn_8:
# 117 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Relearn_Text_2
# 118 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Relearn_7


DR_Tavern_Sage_Nature::
# 126 "data/scripts/dr_tavern.pory"
	showmoneybox 18, 0
# 127 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_0, MSGBOX_YESNO
# 128 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, NO
	goto_if_eq DR_Tavern_Sage_Nature_2
DR_Tavern_Sage_Nature_1:
# 132 "data/scripts/dr_tavern.pory"
	checkmoney 2000
# 133 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, FALSE
	goto_if_eq DR_Tavern_Sage_Nature_5
DR_Tavern_Sage_Nature_4:
# 138 "data/scripts/dr_tavern.pory"
	hidemoneybox
# 139 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_2
# 140 "data/scripts/dr_tavern.pory"
	special ChoosePartyMon
# 141 "data/scripts/dr_tavern.pory"
	waitstate
# 142 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq DR_Tavern_Sage_Nature_8
DR_Tavern_Sage_Nature_7:
# 145 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, ScriptGetPartyMonSpecies
# 146 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, SPECIES_EGG
	goto_if_eq DR_Tavern_Sage_Nature_11
DR_Tavern_Sage_Nature_10:
# 150 "data/scripts/dr_tavern.pory"
	message DR_Tavern_Sage_Nature_Text_4
# 151 "data/scripts/dr_tavern.pory"
	waitmessage
# 152 "data/scripts/dr_tavern.pory"
	dynmultichoice 0, 0, TRUE, 5, 0, DYN_MULTICHOICE_CB_NONE, DR_Tavern_Sage_Nature_Text_5, DR_Tavern_Sage_Nature_Text_6, DR_Tavern_Sage_Nature_Text_7, DR_Tavern_Sage_Nature_Text_8, DR_Tavern_Sage_Nature_Text_9
# 153 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8005, VAR_RESULT
# 154 "data/scripts/dr_tavern.pory"
	message DR_Tavern_Sage_Nature_Text_10
# 155 "data/scripts/dr_tavern.pory"
	waitmessage
# 156 "data/scripts/dr_tavern.pory"
	dynmultichoice 0, 0, TRUE, 5, 0, DYN_MULTICHOICE_CB_NONE, DR_Tavern_Sage_Nature_Text_5, DR_Tavern_Sage_Nature_Text_6, DR_Tavern_Sage_Nature_Text_7, DR_Tavern_Sage_Nature_Text_8, DR_Tavern_Sage_Nature_Text_9
# 157 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_RESULT
# 158 "data/scripts/dr_tavern.pory"
	special DrTavernSetNature
# 159 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, FALSE
	goto_if_eq DR_Tavern_Sage_Nature_14
DR_Tavern_Sage_Nature_13:
# 163 "data/scripts/dr_tavern.pory"
	removemoney 2000
# 164 "data/scripts/dr_tavern.pory"
	playse SE_SHOP
# 165 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_12
# 166 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return

DR_Tavern_Sage_Nature_2:
# 129 "data/scripts/dr_tavern.pory"
	hidemoneybox
# 130 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_1

DR_Tavern_Sage_Nature_5:
# 134 "data/scripts/dr_tavern.pory"
	hidemoneybox
# 135 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_1
# 136 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_4

DR_Tavern_Sage_Nature_8:
# 143 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_7

DR_Tavern_Sage_Nature_11:
# 147 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_3
# 148 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_10

DR_Tavern_Sage_Nature_14:
# 160 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_Nature_Text_11
# 161 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	goto DR_Tavern_Sage_Nature_13


DR_Tavern_Sage_ApexFruit::
# 170 "data/scripts/dr_tavern.pory"
	msgbox DR_Tavern_Sage_ApexFruit_Text_0
# 171 "data/scripts/dr_tavern.pory"
	pokemart DR_Tavern_ApexStock
# 172 "data/scripts/dr_tavern.pory"
	goto DR_Tavern_Sage_Bye
	return


	.align 2
# 175 "data/scripts/dr_tavern.pory"
DR_Tavern_ApexStock:
# 176 "data/scripts/dr_tavern.pory"
	.2byte ITEM_APEX_FRUIT
	.2byte ITEM_NONE

EventScript_DrUseApexFruit::
# 181 "data/scripts/dr_tavern.pory"
	lockall
# 182 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_0
# 183 "data/scripts/dr_tavern.pory"
	special ChoosePartyMon
# 184 "data/scripts/dr_tavern.pory"
	waitstate
# 185 "data/scripts/dr_tavern.pory"
	compare VAR_0x8004, PARTY_NOTHING_CHOSEN
	goto_if_eq EventScript_DrUseApexFruit_2
# 189 "data/scripts/dr_tavern.pory"
	specialvar VAR_RESULT, ScriptGetPartyMonSpecies
# 190 "data/scripts/dr_tavern.pory"
	compare VAR_RESULT, SPECIES_EGG
	goto_if_eq EventScript_DrUseApexFruit_5
# 195 "data/scripts/dr_tavern.pory"
	special DrTavernBufferAbilityChoices
# 196 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 0
	goto_if_eq EventScript_DrUseApexFruit_8
# 201 "data/scripts/dr_tavern.pory"
	message EventScript_DrUseApexFruit_Text_3
# 202 "data/scripts/dr_tavern.pory"
	waitmessage
# 203 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_4, 0
# 204 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 2
	goto_if_ge EventScript_DrUseApexFruit_11
EventScript_DrUseApexFruit_10:
# 207 "data/scripts/dr_tavern.pory"
	compare VAR_0x8005, 3
	goto_if_ge EventScript_DrUseApexFruit_14
EventScript_DrUseApexFruit_13:
# 210 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_7, 3
# 211 "data/scripts/dr_tavern.pory"
	dynmultistack 0, 0, FALSE, 4, FALSE, 0, DYN_MULTICHOICE_CB_NONE
# 212 "data/scripts/dr_tavern.pory"
	switch VAR_RESULT
# 213 "data/scripts/dr_tavern.pory"
	case 0, EventScript_DrUseApexFruit_18
# 214 "data/scripts/dr_tavern.pory"
	case 1, EventScript_DrUseApexFruit_19
# 215 "data/scripts/dr_tavern.pory"
	case 2, EventScript_DrUseApexFruit_20
# 217 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_2:
# 186 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_5:
# 191 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_1
# 192 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_8:
# 197 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_2
# 198 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_11:
# 205 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_5, 1
	goto EventScript_DrUseApexFruit_10

EventScript_DrUseApexFruit_14:
# 208 "data/scripts/dr_tavern.pory"
	dynmultipush EventScript_DrUseApexFruit_Text_6, 2
	goto EventScript_DrUseApexFruit_13

EventScript_DrUseApexFruit_16:
# 220 "data/scripts/dr_tavern.pory"
	special DrTavernSetAbilitySlot
# 221 "data/scripts/dr_tavern.pory"
	removeitem ITEM_APEX_FRUIT
# 222 "data/scripts/dr_tavern.pory"
	special BufferMonNickname
# 223 "data/scripts/dr_tavern.pory"
	playse SE_USE_ITEM
# 224 "data/scripts/dr_tavern.pory"
	msgbox EventScript_DrUseApexFruit_Text_8
# 225 "data/scripts/dr_tavern.pory"
	releaseall
	end

EventScript_DrUseApexFruit_18:
# 213 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_0x8007
	goto EventScript_DrUseApexFruit_16

EventScript_DrUseApexFruit_19:
# 214 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_0x8008
	goto EventScript_DrUseApexFruit_16

EventScript_DrUseApexFruit_20:
# 215 "data/scripts/dr_tavern.pory"
	copyvar VAR_0x8006, VAR_0x8009
	goto EventScript_DrUseApexFruit_16


DR_Tavern_Healer_Text_0:
# 12 "data/scripts/dr_tavern.pory"
	.string "Welcome in, traveller! A hot meal, a cool\n"
	.string "cup, and your Pokémon set to rights.\l"
	.string "Shall I bring something out for them?$"

DR_Tavern_Healer_Text_1:
# 14 "data/scripts/dr_tavern.pory"
	.string "Right away.$"

DR_Tavern_Healer_Text_2:
# 21 "data/scripts/dr_tavern.pory"
	.string "Fed, watered and rested. The Templars\n"
	.string "keep this hearth for any trainer on the\l"
	.string "road.$"

DR_Tavern_Healer_Text_3:
# 23 "data/scripts/dr_tavern.pory"
	.string "As you like. The kitchen fire never goes\n"
	.string "out.$"

DR_Tavern_Caretaker_Text_0:
# 33 "data/scripts/dr_tavern.pory"
	.string "I tend the Pokémon a traveller can't\n"
	.string "carry on the road. Shall I fetch yours?$"

DR_Tavern_Caretaker_Text_1:
# 39 "data/scripts/dr_tavern.pory"
	.string "They're in good hands either way.$"

DR_Tavern_Sage_Text_0:
# 51 "data/scripts/dr_tavern.pory"
	.string "That mask is Athanto work. There'll be\n"
	.string "no more of them now.\p"
	.string "Two years past, the guardian of that\n"
	.string "land came down from its mountain and\l"
	.string "left neither king nor lord alive.$"

DR_Tavern_Sage_Text_1:
# 53 "data/scripts/dr_tavern.pory"
	.string "A new name, a forgotten art, a change of\n"
	.string "temper... What would you have of me?$"

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
# 73 "data/scripts/dr_tavern.pory"
	.string "Come again whenever you've need.$"

DR_Tavern_Sage_Rename_Text_0:
# 80 "data/scripts/dr_tavern.pory"
	.string "Whose name shall we change?$"

DR_Tavern_Sage_Rename_Text_1:
# 88 "data/scripts/dr_tavern.pory"
	.string "That's an Egg. Let it hatch first, then\n"
	.string "we'll talk names.$"

DR_Tavern_Sage_Rename_Text_2:
# 95 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1} was named by the one\n"
	.string "who raised it. That name isn't mine to\l"
	.string "change.$"

DR_Tavern_Sage_Rename_Text_3:
# 100 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1}. A good name.$"

DR_Tavern_Sage_Relearn_Text_0:
# 105 "data/scripts/dr_tavern.pory"
	.string "Which Pokémon wants to remember?$"

DR_Tavern_Sage_Relearn_Text_1:
# 113 "data/scripts/dr_tavern.pory"
	.string "An Egg has nothing to remember yet.$"

DR_Tavern_Sage_Relearn_Text_2:
# 117 "data/scripts/dr_tavern.pory"
	.string "There's nothing that one has\n"
	.string "forgotten.$"

DR_Tavern_Sage_Nature_Text_0:
# 127 "data/scripts/dr_tavern.pory"
	.string "Changing a Pokémon's temper takes time\n"
	.string "and a good deal of patience. It costs\l"
	.string "¥2,000. Shall we?$"

DR_Tavern_Sage_Nature_Text_1:
# 135 "data/scripts/dr_tavern.pory"
	.string "You'll need ¥2,000 for that.$"

DR_Tavern_Sage_Nature_Text_2:
# 139 "data/scripts/dr_tavern.pory"
	.string "Whose nature shall we change?$"

DR_Tavern_Sage_Nature_Text_3:
# 147 "data/scripts/dr_tavern.pory"
	.string "Let the Egg hatch first.$"

DR_Tavern_Sage_Nature_Text_4:
# 150 "data/scripts/dr_tavern.pory"
	.string "Which side of it should grow stronger?$"

DR_Tavern_Sage_Nature_Text_5:
# 152 "data/scripts/dr_tavern.pory"
	.string "Attack$"

DR_Tavern_Sage_Nature_Text_6:
# 152 "data/scripts/dr_tavern.pory"
	.string "Defense$"

DR_Tavern_Sage_Nature_Text_7:
# 152 "data/scripts/dr_tavern.pory"
	.string "Sp. Atk$"

DR_Tavern_Sage_Nature_Text_8:
# 152 "data/scripts/dr_tavern.pory"
	.string "Sp. Def$"

DR_Tavern_Sage_Nature_Text_9:
# 152 "data/scripts/dr_tavern.pory"
	.string "Speed$"

DR_Tavern_Sage_Nature_Text_10:
# 154 "data/scripts/dr_tavern.pory"
	.string "And which should give a little? Choose\n"
	.string "the same one for a balanced temper.$"

DR_Tavern_Sage_Nature_Text_11:
# 160 "data/scripts/dr_tavern.pory"
	.string "It already has a {STR_VAR_2} nature.\n"
	.string "Keep your money.$"

DR_Tavern_Sage_Nature_Text_12:
# 165 "data/scripts/dr_tavern.pory"
	.string "There. Its nature is {STR_VAR_2}\n"
	.string "now.$"

DR_Tavern_Sage_ApexFruit_Text_0:
# 170 "data/scripts/dr_tavern.pory"
	.string "Apex Fruit. Feed one to a Pokémon and it\n"
	.string "draws out a different ability. Rare, and\l"
	.string "priced like it.$"

EventScript_DrUseApexFruit_Text_0:
# 182 "data/scripts/dr_tavern.pory"
	.string "Which Pokémon will eat the Apex Fruit?$"

EventScript_DrUseApexFruit_Text_1:
# 191 "data/scripts/dr_tavern.pory"
	.string "An Egg can't eat.$"

EventScript_DrUseApexFruit_Text_2:
# 197 "data/scripts/dr_tavern.pory"
	.string "It has no other ability to draw out.$"

EventScript_DrUseApexFruit_Text_3:
# 201 "data/scripts/dr_tavern.pory"
	.string "Which ability should it draw out?$"

EventScript_DrUseApexFruit_Text_4:
# 203 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1}$"

EventScript_DrUseApexFruit_Text_5:
# 205 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_2}$"

EventScript_DrUseApexFruit_Text_6:
# 208 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_3}$"

EventScript_DrUseApexFruit_Text_7:
# 210 "data/scripts/dr_tavern.pory"
	.string "Cancel$"

EventScript_DrUseApexFruit_Text_8:
# 224 "data/scripts/dr_tavern.pory"
	.string "{STR_VAR_1}'s ability is now\n"
	.string "{STR_VAR_2}!$"
