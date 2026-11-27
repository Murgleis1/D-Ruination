HollowHill_MapScripts::
	.byte 0


HollowHill_EventScript_ToMirroh16::
# 4 "data/maps/HollowHill/scripts.pory"
	setvar VAR_TEMP_1, 1
# 5 "data/maps/HollowHill/scripts.pory"
	warp MAP_MIRROH_GATE, 28, 21
	return


HollowHill_EventScript_ToMirroh17::
# 9 "data/maps/HollowHill/scripts.pory"
	setvar VAR_TEMP_1, 1
# 10 "data/maps/HollowHill/scripts.pory"
	warp MAP_MIRROH_GATE, 29, 21
	return


HollowHill_EventScript_ToMirroh18::
# 14 "data/maps/HollowHill/scripts.pory"
	setvar VAR_TEMP_1, 1
# 15 "data/maps/HollowHill/scripts.pory"
	warp MAP_MIRROH_GATE, 30, 21
	return


HollowHill_EventScript_ToMirroh19::
# 19 "data/maps/HollowHill/scripts.pory"
	setvar VAR_TEMP_1, 1
# 20 "data/maps/HollowHill/scripts.pory"
	warp MAP_MIRROH_GATE, 31, 21
	return


DR_HH_Finn::
# 27 "data/maps/HollowHill/scripts.pory"
	trainerbattle_single TRAINER_DR_HH_ADVENTURER_FINN, DR_HH_Finn_Text_0, DR_HH_Finn_Text_1
# 28 "data/maps/HollowHill/scripts.pory"
	msgbox DR_HH_Finn_Text_2, MSGBOX_AUTOCLOSE
	end


DR_HH_Alphonse::
# 33 "data/maps/HollowHill/scripts.pory"
	trainerbattle_single TRAINER_DR_HH_REVENANT_ALPHONSE, DR_HH_Alphonse_Text_0, DR_HH_Alphonse_Text_1
# 34 "data/maps/HollowHill/scripts.pory"
	msgbox DR_HH_Alphonse_Text_2, MSGBOX_AUTOCLOSE
	end


DR_HH_Helga::
# 39 "data/maps/HollowHill/scripts.pory"
	trainerbattle_single TRAINER_DR_HH_WITCH_HELGA, DR_HH_Helga_Text_0, DR_HH_Helga_Text_1
# 40 "data/maps/HollowHill/scripts.pory"
	msgbox DR_HH_Helga_Text_2, MSGBOX_AUTOCLOSE
	end


DR_HH_Denth::
# 45 "data/maps/HollowHill/scripts.pory"
	trainerbattle_single TRAINER_DR_HH_ROYAL_OFFICER_DENTH, DR_HH_Denth_Text_0, DR_HH_Denth_Text_1
# 46 "data/maps/HollowHill/scripts.pory"
	msgbox DR_HH_Denth_Text_2, MSGBOX_AUTOCLOSE
	end


DR_HH_Grave::
# 51 "data/maps/HollowHill/scripts.pory"
	msgbox DR_HH_Grave_Text_0, MSGBOX_SIGN
	end


DR_HH_Finn_Text_0:
# 27 "data/maps/HollowHill/scripts.pory"
	.string "Hail, masked one! Jake and I have sworn\n"
	.string "to rid Hollow Hill of every fell thing\l"
	.string "that haunts it, and you look foul\l"
	.string "enough to start with. En garde!$"

DR_HH_Finn_Text_1:
# 27 "data/maps/HollowHill/scripts.pory"
	.string "Mathematical! You fight like a hero out\n"
	.string "of the old songs.$"

DR_HH_Finn_Text_2:
# 28 "data/maps/HollowHill/scripts.pory"
	.string "Jake and I have been hunting for\n"
	.string "whatever made these webs. We've seen\l"
	.string "so many all over the Hill... yet never\l"
	.string "whatever spun them. I'm starting to\l"
	.string "hope we never do.$"

DR_HH_Alphonse_Text_0:
# 33 "data/maps/HollowHill/scripts.pory"
	.string "Warm... so warm. Your soul burns brighter\n"
	.string "than a hearth in winter. Let me have it!!$"

DR_HH_Alphonse_Text_1:
# 33 "data/maps/HollowHill/scripts.pory"
	.string "Cold again. It's always so cold.$"

DR_HH_Alphonse_Text_2:
# 34 "data/maps/HollowHill/scripts.pory"
	.string "That witch nearby woke me, and now the\n"
	.string "grave won't take me back. But I may\l"
	.string "have risen even without her\l"
	.string "interference. Something in the Hill\l"
	.string "won't let the dead sleep for long.$"

DR_HH_Helga_Text_0:
# 39 "data/maps/HollowHill/scripts.pory"
	.string "Don't look at me like that! I only\n"
	.string "wanted to ask the dead man where he'd\l"
	.string "hidden his coin, and now he won't lie\l"
	.string "back down.$"

DR_HH_Helga_Text_1:
# 39 "data/maps/HollowHill/scripts.pory"
	.string "Fine, fine! Just don't tell the Templars\n"
	.string "it was me.$"

DR_HH_Helga_Text_2:
# 40 "data/maps/HollowHill/scripts.pory"
	.string "I raised that man's spirit with a rite\n"
	.string "out of my grandmother's book. Now he\l"
	.string "floats about it day and night, and I\l"
	.string "daren't go near enough to lay him back\l"
	.string "to rest.$"

DR_HH_Denth_Text_0:
# 45 "data/maps/HollowHill/scripts.pory"
	.string "Halt! A mask, in these woods? You're one\n"
	.string "of Rip's, I'd stake my pay on it.$"

DR_HH_Denth_Text_1:
# 45 "data/maps/HollowHill/scripts.pory"
	.string "Whatever you are, you're no common\n"
	.string "cutthroat.$"

DR_HH_Denth_Text_2:
# 46 "data/maps/HollowHill/scripts.pory"
	.string "I owe you an apology, Rainhawk.\n"
	.string "Marauders have robbed every cart\l"
	.string "through these woods, and half of them\l"
	.string "hide their faces. I see a mask and I see\l"
	.string "a thief.$"

DR_HH_Grave_Text_0:
# 51 "data/maps/HollowHill/scripts.pory"
	.string "The headstone reads: ALPHONSE. The\n"
	.string "earth before it has been dug open, from\l"
	.string "below.$"
