PellucaDormitory1F_MapScripts::
	.byte 0


DR_Dorm_LockedDoor::
# 12 "data/maps/PellucaDormitory1F/scripts.pory"
	msgbox DR_Dorm_LockedDoor_Text_0
	end


DR_Dorm_OsridPlate::
# 17 "data/maps/PellucaDormitory1F/scripts.pory"
	msgbox DR_Dorm_OsridPlate_Text_0
	end


DR_Dorm_Cook::
# 23 "data/maps/PellucaDormitory1F/scripts.pory"
	lock
# 24 "data/maps/PellucaDormitory1F/scripts.pory"
	msgbox DR_Dorm_Cook_Text_0
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
	msgbox DR_Dorm_StudentTables_Text_0
# 34 "data/maps/PellucaDormitory1F/scripts.pory"
	closemessage
# 35 "data/maps/PellucaDormitory1F/scripts.pory"
	release
	end


DR_Dorm_StudentStage::
# 40 "data/maps/PellucaDormitory1F/scripts.pory"
	lock
# 41 "data/maps/PellucaDormitory1F/scripts.pory"
	faceplayer
# 42 "data/maps/PellucaDormitory1F/scripts.pory"
	msgbox DR_Dorm_StudentStage_Text_0
# 43 "data/maps/PellucaDormitory1F/scripts.pory"
	closemessage
# 44 "data/maps/PellucaDormitory1F/scripts.pory"
	release
	end


DR_Dorm_LockedDoor_Text_0:
# 12 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "It's locked.$"

DR_Dorm_OsridPlate_Text_0:
# 17 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "A brass plate beside the door reads:\n"
	.string "NOMAD ALBAN.$"

DR_Dorm_Cook_Text_0:
# 24 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "Supper's at sundown.\p"
	.string "We had a Tellian lad in this kitchen till\n"
	.string "word came his tribes were taking up\l"
	.string "arms against each other. He wrote once,\l"
	.string "and never again.$"

DR_Dorm_StudentTables_Text_0:
# 33 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "On debate nights a body can't hear\n"
	.string "himself think in here.\p"
	.string "Last week we argued whether Cormor\n"
	.string "Dream-Eater ever lived at all. Master\l"
	.string "Orphel never once said which side he\l"
	.string "favoured.$"

DR_Dorm_StudentStage_Text_0:
# 42 "data/maps/PellucaDormitory1F/scripts.pory"
	.string "A second-year argued at the lectern\n"
	.string "that the Empress-mother ought to\l"
	.string "leave her villa and sit her own throne.\p"
	.string "Half the hall cheered. The other half\n"
	.string "went very quiet.$"
