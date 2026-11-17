PellucaCityPokemonCenter_MapScripts::
# 8 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	map_script MAP_SCRIPT_ON_TRANSITION, PellucaCityPokemonCenter_MapScripts_MAP_SCRIPT_ON_TRANSITION
	.byte 0

PellucaCityPokemonCenter_MapScripts_MAP_SCRIPT_ON_TRANSITION:
# 9 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	setrespawn HEAL_LOCATION_PELLUCA_CITY
	return


DR_Tavern_Innkeeper::
# 14 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	lock
# 15 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	faceplayer
# 16 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Innkeeper_Text_0
# 17 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Innkeeper_Text_1, MSGBOX_YESNO
# 18 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	compare VAR_RESULT, YES
	goto_if_eq DR_Tavern_Innkeeper_2
# 29 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Innkeeper_Text_4
DR_Tavern_Innkeeper_1:
# 31 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 32 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	release
	end

DR_Tavern_Innkeeper_2:
# 19 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Innkeeper_Text_2
# 20 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 21 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	fadescreen FADE_TO_BLACK
# 22 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	playfanfare MUS_HEAL
# 23 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	waitfanfare
# 24 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	special HealPlayerParty
# 25 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	fadescreen FADE_FROM_BLACK
# 26 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Innkeeper_Text_0
# 27 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Innkeeper_Text_3
	goto DR_Tavern_Innkeeper_1


DR_Tavern_Barkeep::
# 37 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	lock
# 38 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	faceplayer
# 39 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Barkeep_Text_0
# 40 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	message DR_Tavern_Barkeep_Text_1
# 41 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	waitmessage
# 42 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	pokemart DR_Tavern_Stock
# 43 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Barkeep_Text_0
# 44 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Barkeep_Text_2
# 45 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 46 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	release
	end


	.align 2
# 50 "data/maps/PellucaCityPokemonCenter/scripts.pory"
DR_Tavern_Stock:
# 51 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_POTION
# 52 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_POKE_BALL
# 53 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_ANTIDOTE
# 54 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_PARALYZE_HEAL
# 55 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_BURN_HEAL
# 56 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_AWAKENING
	.2byte ITEM_NONE

DR_Tavern_Sailor::
# 60 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	lock
# 61 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	faceplayer
# 62 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Sailor_Text_0
# 63 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Sailor_Text_1
# 64 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 65 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	release
	end


DR_Tavern_Fisherman::
# 70 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	lock
# 71 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	faceplayer
# 72 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Fisherman_Text_0
# 73 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Fisherman_Text_1
# 74 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 75 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	release
	end


PellucaCity_PokemonCenter_Nurse1::
# 81 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse1_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Nurse2::
# 86 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse2_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Nurse3::
# 91 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse3_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Nurse4::
# 96 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse4_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Chansey::
# 101 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 102 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Chansey_Text_0, MSGBOX_NPC
	end


DR_Tavern_Innkeeper_Text_0:
# 16 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Innkeeper$"

DR_Tavern_Innkeeper_Text_1:
# 17 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Welcome to the Seaside Tavern. Your\n"
	.string "Pokémon look like they could use a rest.\l"
	.string "Shall I see to them?$"

DR_Tavern_Innkeeper_Text_2:
# 19 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Leave them with me a moment.$"

DR_Tavern_Innkeeper_Text_3:
# 27 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Fed, rested and ready. Come back\n"
	.string "anytime.$"

DR_Tavern_Innkeeper_Text_4:
# 29 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Suit yourself. The door is always open.$"

DR_Tavern_Barkeep_Text_0:
# 39 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Barkeep$"

DR_Tavern_Barkeep_Text_1:
# 40 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Supplies for the road? Take a look.$"

DR_Tavern_Barkeep_Text_2:
# 44 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Safe travels.$"

DR_Tavern_Sailor_Text_0:
# 62 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Sailor$"

DR_Tavern_Sailor_Text_1:
# 63 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Two ships in at once this week. The\n"
	.string "harbour hasn't been this busy since\l"
	.string "before the war.$"

DR_Tavern_Fisherman_Text_0:
# 72 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Fisherman$"

DR_Tavern_Fisherman_Text_1:
# 73 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "The Vizier keeps his lamps burning half\n"
	.string "the night up in that tower. Scholars.\l"
	.string "Never sleep.$"

PellucaCity_PokemonCenter_Nurse1_Text_0:
# 81 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "We've had enough of the Heal Pass\n"
	.string "system. We're unionising!$"

PellucaCity_PokemonCenter_Nurse2_Text_0:
# 86 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Down with Heal Passes! Or at least\n"
	.string "station us in decent spots!$"

PellucaCity_PokemonCenter_Nurse3_Text_0:
# 91 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "We've all got it bad, but the worst is\n"
	.string "the nurse up in Winterlily Hollow!\p"
	.string "I'm going up there with these Chanseys\n"
	.string "to help her out.$"

PellucaCity_PokemonCenter_Nurse4_Text_0:
# 96 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "The nurse in Winterlily Hollow requested\n"
	.string "for some extra help. Since the\l"
	.string "higher-ups don't care, we're going to\l"
	.string "look out for our sisters!$"

PellucaCity_PokemonCenter_Chansey_Text_0:
# 102 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Seeyyy!!\p"
	.string "Chansey wants to unionise too!$"
