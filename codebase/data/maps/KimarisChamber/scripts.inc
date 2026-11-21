KimarisChamber_MapScripts::
	.byte 0


KimarisChamber_EventScript_Kimaris::
# 4 "data/maps/KimarisChamber/scripts.pory"
	lock
# 5 "data/maps/KimarisChamber/scripts.pory"
	faceplayer
# 6 "data/maps/KimarisChamber/scripts.pory"
	msgbox KimarisChamber_EventScript_Kimaris_Text_0
# 7 "data/maps/KimarisChamber/scripts.pory"
	release
	return


KimarisChamber_EventScript_Kimaris_Text_0:
# 6 "data/maps/KimarisChamber/scripts.pory"
	.string "(Kimaris Langerin waits on the sigil.\nThe Trial is not written yet.)$"
