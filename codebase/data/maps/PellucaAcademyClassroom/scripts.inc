PellucaAcademyClassroom_MapScripts::
	.byte 0


DR_Class_Logan::
# 10 "data/maps/PellucaAcademyClassroom/scripts.pory"
	lock
# 11 "data/maps/PellucaAcademyClassroom/scripts.pory"
	faceplayer
# 12 "data/maps/PellucaAcademyClassroom/scripts.pory"
	speakername DR_Class_Logan_Text_0
# 13 "data/maps/PellucaAcademyClassroom/scripts.pory"
	msgbox DR_Class_Logan_Text_1
# 14 "data/maps/PellucaAcademyClassroom/scripts.pory"
	closemessage
# 15 "data/maps/PellucaAcademyClassroom/scripts.pory"
	release
	end


DR_Class_StudentA::
# 20 "data/maps/PellucaAcademyClassroom/scripts.pory"
	lock
# 21 "data/maps/PellucaAcademyClassroom/scripts.pory"
	msgbox DR_Class_StudentA_Text_0
# 22 "data/maps/PellucaAcademyClassroom/scripts.pory"
	closemessage
# 23 "data/maps/PellucaAcademyClassroom/scripts.pory"
	release
	end


DR_Class_StudentB::
# 28 "data/maps/PellucaAcademyClassroom/scripts.pory"
	lock
# 29 "data/maps/PellucaAcademyClassroom/scripts.pory"
	msgbox DR_Class_StudentB_Text_0
# 30 "data/maps/PellucaAcademyClassroom/scripts.pory"
	closemessage
# 31 "data/maps/PellucaAcademyClassroom/scripts.pory"
	release
	end


DR_Class_StudentC::
# 36 "data/maps/PellucaAcademyClassroom/scripts.pory"
	lock
# 37 "data/maps/PellucaAcademyClassroom/scripts.pory"
	msgbox DR_Class_StudentC_Text_0
# 38 "data/maps/PellucaAcademyClassroom/scripts.pory"
	closemessage
# 39 "data/maps/PellucaAcademyClassroom/scripts.pory"
	release
	end


DR_Class_Logan_Text_0:
# 12 "data/maps/PellucaAcademyClassroom/scripts.pory"
	.string "Logan$"

DR_Class_Logan_Text_1:
# 13 "data/maps/PellucaAcademyClassroom/scripts.pory"
	.string "You'll be the Rainhawk the Headmaster\n"
	.string "spoke of. Logan Orphel.\p"
	.string "The Headmaster built this school so\n"
	.string "trainers would know their Pokémon\l"
	.string "before they learn to win with them. I\l"
	.string "ask questions, and I remember who\l"
	.string "answers them.$"

DR_Class_StudentA_Text_0:
# 21 "data/maps/PellucaAcademyClassroom/scripts.pory"
	.string "Master Orphel calls on whoever looks\n"
	.string "least ready. I make a point of always\l"
	.string "looking ready.$"

DR_Class_StudentB_Text_0:
# 29 "data/maps/PellucaAcademyClassroom/scripts.pory"
	.string "Master Orphel took top honours in the\n"
	.string "Headmaster's first class. He's the last\l"
	.string "of House Orphel, and all that old name\l"
	.string "rests on him alone.$"

DR_Class_StudentC_Text_0:
# 37 "data/maps/PellucaAcademyClassroom/scripts.pory"
	.string "I still can't see why a Ghost shrugs off\n"
	.string "a Normal blow.\p"
	.string "They say Baron Kimaris coos at his\n"
	.string "Spiritomb like a babe in swaddling. Can\l"
	.string "that be true of a Reserve Champion?$"
