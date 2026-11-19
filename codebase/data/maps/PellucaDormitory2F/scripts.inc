PellucaDormitory2F_MapScripts::
	.byte 0


DR_Dorm_StudentHall::
# 8 "data/maps/PellucaDormitory2F/scripts.pory"
	lock
# 9 "data/maps/PellucaDormitory2F/scripts.pory"
	faceplayer
# 10 "data/maps/PellucaDormitory2F/scripts.pory"
	speakername DR_Dorm_StudentHall_Text_0
# 11 "data/maps/PellucaDormitory2F/scripts.pory"
	msgbox DR_Dorm_StudentHall_Text_1
# 12 "data/maps/PellucaDormitory2F/scripts.pory"
	closemessage
# 13 "data/maps/PellucaDormitory2F/scripts.pory"
	release
	end


DR_Dorm_StudentHall_Text_0:
# 10 "data/maps/PellucaDormitory2F/scripts.pory"
	.string "Student$"

DR_Dorm_StudentHall_Text_1:
# 11 "data/maps/PellucaDormitory2F/scripts.pory"
	.string "Quiet hours start at dark. Somebody\n"
	.string "always forgets.$"
