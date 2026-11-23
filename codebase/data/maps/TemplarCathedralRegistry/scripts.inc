TemplarCathedralRegistry_MapScripts::
	.byte 0


TemplarCathedralRegistry_EventScript_Braviary::
# 4 "data/maps/TemplarCathedralRegistry/scripts.pory"
	lock
# 5 "data/maps/TemplarCathedralRegistry/scripts.pory"
	faceplayer
# 6 "data/maps/TemplarCathedralRegistry/scripts.pory"
	playmoncry SPECIES_BRAVIARY, CRY_MODE_NORMAL
# 7 "data/maps/TemplarCathedralRegistry/scripts.pory"
	msgbox TemplarCathedralRegistry_EventScript_Braviary_Text_0
# 8 "data/maps/TemplarCathedralRegistry/scripts.pory"
	waitmoncry
# 9 "data/maps/TemplarCathedralRegistry/scripts.pory"
	release
	end


TemplarCathedralRegistry_EventScript_Rufflet::
# 14 "data/maps/TemplarCathedralRegistry/scripts.pory"
	lock
# 15 "data/maps/TemplarCathedralRegistry/scripts.pory"
	faceplayer
# 16 "data/maps/TemplarCathedralRegistry/scripts.pory"
	playmoncry SPECIES_RUFFLET, CRY_MODE_NORMAL
# 17 "data/maps/TemplarCathedralRegistry/scripts.pory"
	msgbox TemplarCathedralRegistry_EventScript_Rufflet_Text_0
# 18 "data/maps/TemplarCathedralRegistry/scripts.pory"
	waitmoncry
# 19 "data/maps/TemplarCathedralRegistry/scripts.pory"
	release
	end


TemplarCathedralRegistry_EventScript_Braviary_Text_0:
# 7 "data/maps/TemplarCathedralRegistry/scripts.pory"
	.string "Braviary: Kreeaw!$"

TemplarCathedralRegistry_EventScript_Rufflet_Text_0:
# 17 "data/maps/TemplarCathedralRegistry/scripts.pory"
	.string "Rufflet: Ruff!$"
