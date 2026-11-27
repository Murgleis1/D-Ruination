PellucaCityPokemonCenter_MapScripts::
# 9 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaCityPokemonCenter_MapScripts_MAP_SCRIPT_ON_TRANSITION
	.byte 0

PellucaCityPokemonCenter_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 10 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	setrespawn HEAL_LOCATION_PELLUCA_CITY
	return


DR_Tavern_Barkeep::
# 15 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	lock
# 16 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	faceplayer
# 17 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Barkeep_Text_0
# 18 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	message DR_Tavern_Barkeep_Text_1
# 19 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	waitmessage
# 20 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	pokemart DR_Tavern_Stock
# 21 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Barkeep_Text_0
# 22 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Barkeep_Text_2
# 23 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 24 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	release
	end


DR_PellucaTavern_Caretaker::
# 30 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	lock
# 31 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	faceplayer
# 32 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_PellucaTavern_Caretaker_Text_0
# 33 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_PellucaTavern_Caretaker_Text_1, MSGBOX_YESNO
# 34 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	compare VAR_RESULT, YES
	goto_if_eq DR_PellucaTavern_Caretaker_2
DR_PellucaTavern_Caretaker_1:
# 39 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_PellucaTavern_Caretaker_Text_0
# 40 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_PellucaTavern_Caretaker_Text_2
# 41 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 42 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	release
	end

DR_PellucaTavern_Caretaker_2:
# 35 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 36 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	special ShowPokemonStorageSystemPC
# 37 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	waitstate
	goto DR_PellucaTavern_Caretaker_1


	.align 2
# 46 "data/maps/PellucaCityPokemonCenter/scripts.pory"
DR_Tavern_Stock:
# 47 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_POTION
# 48 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_POKE_BALL
# 49 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_ANTIDOTE
# 50 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_PARALYZE_HEAL
# 51 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_BURN_HEAL
# 52 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_AWAKENING
	.2byte ITEM_NONE

DR_Tavern_Sailor::
# 56 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	lock
# 57 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	faceplayer
# 58 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Sailor_Text_0
# 59 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Sailor_Text_1
# 60 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 61 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	release
	end


DR_Tavern_Fisherman::
# 66 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	lock
# 67 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	faceplayer
# 68 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Fisherman_Text_0
# 69 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Fisherman_Text_1
# 70 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 71 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	release
	end


PellucaCity_PokemonCenter_Nurse1::
# 77 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse1_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Nurse2::
# 82 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse2_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Nurse3::
# 87 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse3_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Nurse4::
# 92 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse4_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Chansey::
# 97 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 98 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Chansey_Text_0, MSGBOX_NPC
	end


DR_Tavern_Barkeep_Text_0:
# 17 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Barkeep$"

DR_Tavern_Barkeep_Text_1:
# 18 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Provisions for the road? Have a look.$"

DR_Tavern_Barkeep_Text_2:
# 22 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Safe roads. Aye, the prices rose again.\p"
	.string "Every ball and tonic on that shelf\n"
	.string "comes through Sylphon & Stone, and\l"
	.string "their factor wants his coin before the\l"
	.string "crates are opened.$"

DR_PellucaTavern_Caretaker_Text_0:
# 32 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Caretaker$"

DR_PellucaTavern_Caretaker_Text_1:
# 33 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "I tend the Pokémon a traveller can't\n"
	.string "carry on the road. Shall I fetch yours?$"

DR_PellucaTavern_Caretaker_Text_2:
# 40 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "They're in good hands. Half the beasts I\n"
	.string "board belong to sailors who won't sail\l"
	.string "east, with Paldea's lords at each\l"
	.string "other's throats and Kalos little better.$"

DR_Tavern_Sailor_Text_0:
# 58 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Mariner$"

DR_Tavern_Sailor_Text_1:
# 59 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Two ships in this week, and one came\n"
	.string "round by Sevii. Kanto's bird-priests\l"
	.string "have taken the old chapel of Arceus for\l"
	.string "their own, her crew say.\p"
	.string "And still the skirmishes off Johto, for\n"
	.string "all the talk of peace. But you'd know\l"
	.string "more of that than I, Rainhawk.$"

DR_Tavern_Fisherman_Text_0:
# 68 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Fisherman$"

DR_Tavern_Fisherman_Text_1:
# 69 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Something's breeding in the water by\n"
	.string "the sealed cave.\p"
	.string "My nets come up in ribbons, and every\n"
	.string "time there's Crawdaunt in them. More\l"
	.string "than I've ever seen in one place.$"

PellucaCity_PokemonCenter_Nurse1_Text_0:
# 77 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "We've had enough of the Heal Pass\n"
	.string "system. We're unionising!$"

PellucaCity_PokemonCenter_Nurse2_Text_0:
# 82 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Down with Heal Passes! Or at least\n"
	.string "station us in decent spots!$"

PellucaCity_PokemonCenter_Nurse3_Text_0:
# 87 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "We've all got it bad, but the worst is\n"
	.string "the nurse up in Winterlily Hollow!\p"
	.string "I'm going up there with these Chanseys\n"
	.string "to help her out.$"

PellucaCity_PokemonCenter_Nurse4_Text_0:
# 92 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "The nurse in Winterlily Hollow requested\n"
	.string "for some extra help. Since the\l"
	.string "higher-ups don't care, we're going to\l"
	.string "look out for our sisters!$"

PellucaCity_PokemonCenter_Chansey_Text_0:
# 98 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Seeyyy!!\p"
	.string "Chansey wants to unionise too!$"
