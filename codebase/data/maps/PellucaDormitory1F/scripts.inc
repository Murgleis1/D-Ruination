PellucaDormitory1F_MapScripts::
	.byte 0


DR_Dorm_LockedDoor::
# 11 "data/maps/PellucaDormitory1F/scripts.pory"
	msgbox DR_Dorm_LockedDoor_Text_0
	end


DR_Dorm_OsridPlate::
# 16 "data/maps/PellucaDormitory1F/scripts.pory"
	msgbox DR_Dorm_OsridPlate_Text_0
	end


DR_Dorm_Cook::
# 22 "data/maps/PellucaDormitory1F/scripts.pory"
	lock
# 23 "data/maps/PellucaDormitory1F/scripts.pory"
	speakername DR_Dorm_Cook_Text_0
# 24 "data/maps/PellucaDormitory1F/scripts.pory"
	msgbox DR_Dorm_Cook_Text_1
# 25 "data/maps/PellucaDormitory1F/scripts.pory"
	closemessage
# 26 "data/maps/PellucaDormitory1F/scripts.pory"
	release
	end


DR_Dorm_StudentTables::
# 31 "data/maps/PellucaDormitory1F/scripts.pory"
	lock
# 32 "data/maps/PellucaDormitory1F/scripts.pory"
	faceplayer
# 33 "data/maps/PellucaDormitory1F/scripts.pory"
	speakername DR_Dorm_StudentTables_Text_0
# 34 "data/maps/PellucaDormitory1F/scripts.pory"
	msgbox DR_Dorm_StudentTables_Text_1
# 35 "data/maps/PellucaDormitory1F/scripts.pory"
	closemessage
# 36 "data/maps/PellucaDormitory1F/scripts.pory"
	release
	end


DR_Dorm_StudentStage::
# 41 "data/maps/PellucaDormitory1F/scripts.pory"
	lock
# 42 "data/maps/PellucaDormitory1F/scripts.pory"
	faceplayer
# 43 "data/maps/PellucaDormitory1F/scripts.pory"
	speakername DR_Dorm_StudentTables_Text_0
# 44 "data/maps/PellucaDormitory1F/scripts.pory"
	msgbox DR_Dorm_StudentStage_Text_0
# 45 "data/maps/PellucaDormitory1F/scripts.pory"
	closemessage
# 46 "data/maps/PellucaDormitory1F/scripts.pory"
	release
	end


DR_Dorm_LockedDoor_Text_0:
# 11 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "It's locked.$"

DR_Dorm_OsridPlate_Text_0:
# 16 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "A brass plate beside the door reads:\n"
	.string "NOMAD ALBAN.$"

DR_Dorm_Cook_Text_0:
# 23 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "Cook$"

DR_Dorm_Cook_Text_1:
# 24 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "Supper's at sundown. If you miss it,\n"
	.string "there's bread and whatever's left in\l"
	.string "the pot.$"

DR_Dorm_StudentTables_Text_0:
# 33 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "Student$"

DR_Dorm_StudentTables_Text_1:
# 34 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "On debate nights you can't hear\n"
	.string "yourself think in here. The rest of the\l"
	.string "week, it's the best place to study.$"

DR_Dorm_StudentStage_Text_0:
# 44 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "Anyone may take the lectern on debate\n"
	.string "night. Most lose their nerve on the way\l"
	.string "up.$"
