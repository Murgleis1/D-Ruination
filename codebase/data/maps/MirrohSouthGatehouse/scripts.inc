MirrohSouthGatehouse_MapScripts::
	.byte 0


MirrohGatehouse_EventScript_Guard::
# 4 "data/maps/MirrohSouthGatehouse/scripts.pory"
	lock
# 5 "data/maps/MirrohSouthGatehouse/scripts.pory"
	faceplayer
# 6 "data/maps/MirrohSouthGatehouse/scripts.pory"
	msgbox MirrohGatehouse_EventScript_Guard_Text_0
# 7 "data/maps/MirrohSouthGatehouse/scripts.pory"
	release
	return


MirrohGatehouse_EventScript_Guard_Text_0:
# 6 "data/maps/MirrohSouthGatehouse/scripts.pory"
	.string "Mirroh's gate. Keep to the road, traveller.$"
