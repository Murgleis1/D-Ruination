Route11Farmhouse_MapScripts::
	.byte 0


DR_R11_FarmWife::
# 9 "data/maps/Route11Farmhouse/scripts.pory"
	lock
# 10 "data/maps/Route11Farmhouse/scripts.pory"
	faceplayer
# 11 "data/maps/Route11Farmhouse/scripts.pory"
	goto_if_set FLAG_DR_R11_THEFT_SEEN, DR_R11_FarmWife_2
# 14 "data/maps/Route11Farmhouse/scripts.pory"
	msgbox DR_R11_FarmWife_Text_1
DR_R11_FarmWife_1:
# 16 "data/maps/Route11Farmhouse/scripts.pory"
	release
	end

DR_R11_FarmWife_2:
# 12 "data/maps/Route11Farmhouse/scripts.pory"
	msgbox DR_R11_FarmWife_Text_0
	goto DR_R11_FarmWife_1


DR_R11_FarmDaughter::
# 21 "data/maps/Route11Farmhouse/scripts.pory"
	msgbox DR_R11_FarmDaughter_Text_0, MSGBOX_NPC
	end


DR_R11_FarmWife_Text_0:
# 12 "data/maps/Route11Farmhouse/scripts.pory"
	.string "We bar the shutters when the fog comes\n"
	.string "off Hollow Hill. Some nights you can\l"
	.string "hear marching in it.$"

DR_R11_FarmWife_Text_1:
# 14 "data/maps/Route11Farmhouse/scripts.pory"
	.string "A Templar lass stopped for water at\n"
	.string "dawn. She carried a little bird, black on\l"
	.string "one side and white on the other.$"

DR_R11_FarmDaughter_Text_0:
# 21 "data/maps/Route11Farmhouse/scripts.pory"
	.string "Mama says the Templars have a big\n"
	.string "cathedral up in the mountains\l"
	.string "somewhere. I would love to see it\l"
	.string "someday!$"
