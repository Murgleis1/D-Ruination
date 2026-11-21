NecropolisLake_MapScripts::
	.byte 0


NecropolisLake_EventScript_Necromancer::
# 5 "data/maps/NecropolisLake/scripts.pory"
	lock
# 6 "data/maps/NecropolisLake/scripts.pory"
	faceplayer
# 7 "data/maps/NecropolisLake/scripts.pory"
	msgbox NecropolisLake_EventScript_Necromancer_Text_0
# 8 "data/maps/NecropolisLake/scripts.pory"
	release
	return


NecropolisLake_EventScript_Necromancer_Text_0:
# 7 "data/maps/NecropolisLake/scripts.pory"
	.string "(A necromancer of House Langerin.\nNo battle yet: the Trial is not written.)$"
