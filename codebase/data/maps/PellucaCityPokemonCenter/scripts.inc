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


	.align 2
# 28 "data/maps/PellucaCityPokemonCenter/scripts.pory"
DR_Tavern_Stock:
# 29 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_POTION
# 30 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_POKE_BALL
# 31 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_ANTIDOTE
# 32 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_PARALYZE_HEAL
# 33 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_BURN_HEAL
# 34 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.2byte ITEM_AWAKENING
	.2byte ITEM_NONE

DR_Tavern_Sailor::
# 38 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	lock
# 39 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	faceplayer
# 40 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Sailor_Text_0
# 41 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Sailor_Text_1
# 42 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 43 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	release
	end


DR_Tavern_Fisherman::
# 48 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	lock
# 49 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	faceplayer
# 50 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	speakername DR_Tavern_Fisherman_Text_0
# 51 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox DR_Tavern_Fisherman_Text_1
# 52 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	closemessage
# 53 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	release
	end


PellucaCity_PokemonCenter_Nurse1::
# 59 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse1_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Nurse2::
# 64 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse2_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Nurse3::
# 69 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse3_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Nurse4::
# 74 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Nurse4_Text_0, MSGBOX_NPC
	end


PellucaCity_PokemonCenter_Chansey::
# 79 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	playmoncry SPECIES_CHANSEY, CRY_MODE_NORMAL
# 80 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	msgbox PellucaCity_PokemonCenter_Chansey_Text_0, MSGBOX_NPC
	end


DR_Tavern_Barkeep_Text_0:
# 17 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Barkeep$"

DR_Tavern_Barkeep_Text_1:
# 18 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Supplies for the road? Take a look.$"

DR_Tavern_Barkeep_Text_2:
# 22 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Safe travels.$"

DR_Tavern_Sailor_Text_0:
# 40 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Sailor$"

DR_Tavern_Sailor_Text_1:
# 41 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Two ships in at once this week. The\n"
	.string "harbour hasn't been this busy since\l"
	.string "before the war.$"

DR_Tavern_Fisherman_Text_0:
# 50 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Fisherman$"

DR_Tavern_Fisherman_Text_1:
# 51 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "The Vizier keeps his lamps burning half\n"
	.string "the night up in that tower. Scholars.\l"
	.string "Never sleep.$"

PellucaCity_PokemonCenter_Nurse1_Text_0:
# 59 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "We've had enough of the Heal Pass\n"
	.string "system. We're unionising!$"

PellucaCity_PokemonCenter_Nurse2_Text_0:
# 64 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Down with Heal Passes! Or at least\n"
	.string "station us in decent spots!$"

PellucaCity_PokemonCenter_Nurse3_Text_0:
# 69 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "We've all got it bad, but the worst is\n"
	.string "the nurse up in Winterlily Hollow!\p"
	.string "I'm going up there with these Chanseys\n"
	.string "to help her out.$"

PellucaCity_PokemonCenter_Nurse4_Text_0:
# 74 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "The nurse in Winterlily Hollow requested\n"
	.string "for some extra help. Since the\l"
	.string "higher-ups don't care, we're going to\l"
	.string "look out for our sisters!$"

PellucaCity_PokemonCenter_Chansey_Text_0:
# 80 "data/maps/PellucaCityPokemonCenter/scripts.pory"
	.string "Seeyyy!!\p"
	.string "Chansey wants to unionise too!$"
