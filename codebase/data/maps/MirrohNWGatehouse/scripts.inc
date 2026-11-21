MirrohNWGatehouse_MapScripts::
	.byte 0


MirrohNWGatehouse_EventScript_RoadClosed::
# 4 "data/maps/MirrohNWGatehouse/scripts.pory"
	lock
# 5 "data/maps/MirrohNWGatehouse/scripts.pory"
	msgbox MirrohNWGatehouse_EventScript_RoadClosed_Text_0
# 6 "data/maps/MirrohNWGatehouse/scripts.pory"
	applymovement OBJ_EVENT_ID_PLAYER, MirrohNWGatehouse_Movement_StepBack
# 7 "data/maps/MirrohNWGatehouse/scripts.pory"
	waitmovement 0
# 8 "data/maps/MirrohNWGatehouse/scripts.pory"
	release
	return


# 11 "data/maps/MirrohNWGatehouse/scripts.pory"
MirrohNWGatehouse_Movement_StepBack:
# 12 "data/maps/MirrohNWGatehouse/scripts.pory"
	walk_down
	step_end

MirrohNWGatehouse_EventScript_RoadClosed_Text_0:
# 5 "data/maps/MirrohNWGatehouse/scripts.pory"
	.string "The road beyond is snowed in.\n(Mt. Mirroh is not built yet.)$"
