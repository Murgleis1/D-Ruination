Route11_MapScripts::
	.byte 0


DR_R11_Farmer::
# 8 "data/maps/Route11/scripts.pory"
	msgbox DR_R11_Farmer_Text_0, MSGBOX_NPC
	end


DR_R11_FisherTam::
# 13 "data/maps/Route11/scripts.pory"
	trainerbattle_single TRAINER_DR_R11_FISHER_TAM, DR_R11_FisherTam_Text_0, DR_R11_FisherTam_Text_1
# 14 "data/maps/Route11/scripts.pory"
	msgbox DR_R11_FisherTam_Text_2, MSGBOX_AUTOCLOSE
	end


DR_R11_Farmer_Text_0:
# 8 "data/maps/Route11/scripts.pory"
	.string "Marauders took two of my Mareep last\n"
	.string "moon. The drovers say their chief is a\l"
	.string "rogue called Rougehand.$"

DR_R11_FisherTam_Text_0:
# 13 "data/maps/Route11/scripts.pory"
	.string "The tide's out and the fish won't bite,\n"
	.string "so you'll have to do.$"

DR_R11_FisherTam_Text_1:
# 13 "data/maps/Route11/scripts.pory"
	.string "Bested by a man in a mask. My wife will\n"
	.string "never believe it.$"

DR_R11_FisherTam_Text_2:
# 14 "data/maps/Route11/scripts.pory"
	.string "Fishing's poor along this coast of late.\n"
	.string "Something big moves past the cove at\l"
	.string "night, and every fish with sense has\l"
	.string "fled it.$"
